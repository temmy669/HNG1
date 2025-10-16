from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled
from django_ratelimit.exceptions import Ratelimited
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, Throttled):
        custom_response_data = {
            "status": "error",
            "message": f"Rate limit exceeded. Try again in {exc.wait} seconds.",
            "retry_after_seconds": exc.wait,
            "error_code": "RATE_LIMIT_EXCEEDED"
        }
        if response:
            response.data = custom_response_data
        else:
            response = Response(custom_response_data, status=429)
    elif isinstance(exc, Ratelimited):
        custom_response_data = {
            "status": "error",
            "message": "Rate limit exceeded. Too many requests from your IP address.",
            "retry_after_seconds": 60,  # Default 1 minute for django-ratelimit
            "error_code": "RATE_LIMIT_EXCEEDED"
        }
        if response:
            response.data = custom_response_data
        else:
            response = Response(custom_response_data, status=429)
            
    elif isinstance(exc, Exception) and response is None:
        custom_response_data = {
            "status": "error",
            "message": "An unexpected error occurred. Please try again later.",
            "error_code": "INTERNAL_SERVER_ERROR"
        }
        response = Response(custom_response_data, status=500)

    return response
