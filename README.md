# PocketSmart AI

PocketSmart AI is a Generative AI-powered budget planning web application built using FastAPI, Jinja2, SQLite and Google Gemini API.

The application helps users create practical budget plans for:

- Home Interior
- Party Planning
- Jewelry Planning

Users can enter their budget and requirements, and the application generates an AI-powered recommendation with budget allocation, estimated costs, useful tips and shopping search links.

---

## Features

### 1. User Authentication

- User registration
- User login
- Secure password hashing
- Cookie-based authentication
- Logout functionality

### 2. Home Interior Planner

Users can provide:

- Total budget
- Rooms
- Number of lights
- Number of fans
- Furniture requirements
- Dining table requirements
- Interior style
- Additional requirements

The application generates a personalized home interior budget plan.

### 3. Party Planner

Users can provide:

- Total budget
- Event type
- Guest count
- Venue type
- Catering requirement
- Decoration requirement
- Entertainment requirement
- Location
- Additional requirements

The application generates a complete party budget recommendation.

### 4. Jewelry Planner

Users can provide:

- Total budget
- Occasion
- Style preferences
- Metal preference
- Additional requirements
- Optional reference image

The application generates a jewelry recommendation based on the provided requirements.

### 5. AI Recommendations

Google Gemini API is used to generate personalized recommendations.

The AI response contains:

- Recommendation title
- Summary
- Budget breakdown
- Recommended items
- Estimated prices
- Quantity
- Planning tips
- Warnings

### 6. Recommendation History

Generated recommendations are stored in the SQLite database.

Users can:

- View previous recommendations
- Open detailed recommendations
- Review previous budgets
- Access saved plans from the dashboard

### 7. Shopping Search Links

Recommended items can be searched directly through supported platforms such as:

- Amazon
- Flipkart
- IKEA
- Myntra
- Meesho
- Swiggy
- Zomato
- OYO

The application creates search links based on the recommended item.

---

## Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Backend

- Python
- FastAPI
- Uvicorn

### Database

- SQLite
- SQLAlchemy

### AI

- Google Gemini API

### Authentication

- JWT
- HTTP Cookies
- Scrypt password hashing

