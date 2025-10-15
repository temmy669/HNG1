# HNG1 - Dynamic Profile Endpoint

This is a Django REST API that implements a dynamic profile endpoint as per the Backend Wizards Stage 0 Task.

## Features

- GET `/me` endpoint returning user profile with dynamic cat facts
- Fetches real-time cat facts from external API
- Dynamic UTC timestamp in ISO 8601 format
- Error handling for external API failures
- CORS enabled for cross-origin requests

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd HNG1
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following variables:
   ```
   URL=https://catfact.ninja/fact
   EMAIL=your-email@example.com
   NAME=Your Full Name
   STACK=Your Backend Stack
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoint

### GET /me

Returns user profile information with a dynamic cat fact.

**Response Format:**
```json
{
  "status": "success",
  "user": {
    "email": "your-email@example.com",
    "name": "Your Full Name",
    "stack": "Your Backend Stack"
  },
  "timestamp": "2025-10-15T12:34:56.789Z",
  "fact": "A random cat fact from the API"
}
```

## Dependencies

- Django==5.2.7
- djangorestframework==3.16.1
- python-decouple==3.8
- django-cors-headers==4.9.0
- requests==2.32.5

## Environment Variables

- `URL`: Cat Facts API endpoint (default: https://catfact.ninja/fact)
- `EMAIL`: Your email address
- `NAME`: Your full name
- `STACK`: Your backend technology stack

## Testing

Test the endpoint using curl:
```bash
curl http://127.0.0.1:8000/me
```

Or open in browser: `http://127.0.0.1:8000/me`

## Deployment

This API can be deployed to platforms like Railway, Heroku, or AWS. Ensure environment variables are set in your deployment platform's configuration.
