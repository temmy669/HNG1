# HNG1 - Dynamic Profile Endpoint

This is a Django REST API that implements a dynamic profile endpoint as per the Backend Wizards Stage 0 Task.

## Features

- GET `/me` endpoint returning user profile with dynamic cat facts
- Fetches real-time cat facts from external API
- Dynamic UTC timestamp in ISO 8601 format
- Error handling for external API failures
- CORS enabled for cross-origin requests
- Rate limiting (10 requests per minute per IP)
- Logging for debugging and monitoring
- Redis cache backend for rate limiting (production-ready)

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/temmy669/HNG1.git
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

**Rate Limit:** 10 requests per minute per IP address

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

**Error Response (Rate Limit Exceeded):**
```json
{
  "status": "error",
  "message": "Rate limit exceeded. Too many requests from your IP address.",
  "retry_after_seconds": 60,
  "error_code": "RATE_LIMIT_EXCEEDED"
}
```

## API Documentation

The API includes comprehensive documentation accessible through multiple formats:

### Swagger UI
Interactive API documentation with testing capabilities:
```
http://127.0.0.1:8000/api/docs/swagger/
```

### ReDoc
Alternative documentation view with clean, responsive design:
```
http://127.0.0.1:8000/api/docs/redoc/
```

### OpenAPI Schema
Raw OpenAPI 3.0 specification in JSON format:
```
http://127.0.0.1:8000/api/schema/
```

The documentation includes:
- Detailed endpoint descriptions
- Request/response schemas
- Example responses
- Rate limiting information
- Error response formats

## Dependencies

- Django==5.2.7
- djangorestframework==3.16.1
- python-decouple==3.8
- django-cors-headers==4.9.0
- requests==2.32.5
- django-ratelimit==4.1.0
- django-redis==6.0.0
- redis (for production cache backend)

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

### Production Cache Configuration

For production deployment, update the cache configuration in `settings.py` to use Redis:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Update with your Redis URL
    }
}
```

Install Redis and update the `LOCATION` with your Redis connection string.


