from datetime import datetime, timedelta, timezone
from typing import Annotated

import base64
import hashlib
import hmac
import os

import jwt

from fastapi import (
    Cookie,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.config import get_settings
from app.database import get_db
from app.models import User


settings = get_settings()

ALGORITHM = "HS256"


def hash_password(password: str) -> str:

    salt = os.urandom(16)

    derived = hashlib.scrypt(
        password.encode("utf-8"),
        salt=salt,
        n=2**14,
        r=8,
        p=1,
    )

    return (
        "scrypt$"
        + base64.b64encode(salt).decode()
        + "$"
        + base64.b64encode(derived).decode()
    )


def verify_password(
    password: str,
    encoded: str,
) -> bool:

    try:

        scheme, salt_b64, hash_b64 = encoded.split(
            "$",
            2,
        )

        if scheme != "scrypt":
            return False

        salt = base64.b64decode(
            salt_b64
        )

        expected = base64.b64decode(
            hash_b64
        )

        actual = hashlib.scrypt(
            password.encode("utf-8"),
            salt=salt,
            n=2**14,
            r=8,
            p=1,
        )

        return hmac.compare_digest(
            actual,
            expected,
        )

    except Exception:
        return False


def create_access_token(
    user_id: int,
) -> str:

    expires = (
        datetime.now(timezone.utc)
        + timedelta(
            minutes=settings.access_token_expire_minutes
        )
    )

    return jwt.encode(
        {
            "sub": str(user_id),
            "exp": expires,
        },
        settings.secret_key,
        algorithm=ALGORITHM,
    )


def decode_access_token(
    token: str,
) -> int:

    try:

        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[ALGORITHM],
        )

        return int(
            payload["sub"]
        )

    except (
        jwt.PyJWTError,
        KeyError,
        ValueError,
        TypeError,
    ):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session.",
        )


def get_current_user(
    access_token: Annotated[
        str | None,
        Cookie()
    ] = None,

    db: Session = Depends(get_db),
) -> User:

    if not access_token:

        raise HTTPException(
            status_code=401,
            detail="Authentication required.",
        )

    user_id = decode_access_token(
        access_token
    )

    user = db.get(
        User,
        user_id,
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found.",
        )

    return user