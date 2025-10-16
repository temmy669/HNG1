import logging
import requests
from datetime import datetime, timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
from django_ratelimit.decorators import ratelimit

# Set up logging
logger = logging.getLogger(__name__)

@api_view(['GET'])
@ratelimit(key='ip', rate='10/m', method='GET', block=True)
def me(request):
    CAT_FACT_URL = settings.FACT_URL

    logger.info(f"Request received from {request.META.get('REMOTE_ADDR')}")

    try:
        response = requests.get(CAT_FACT_URL, timeout=5)
        response.raise_for_status()
        cat_fact = response.json().get("fact", "Cats always land on their feet!")
        logger.info("Successfully fetched cat fact")
    except requests.RequestException as e:
        logger.error(f"Failed to fetch cat fact: {e}")
        cat_fact = "Could not fetch a cat fact at the moment."

    data = {
        "status": "success",
        "user": {
            "email": settings.EMAIL,
            "name": settings.NAME,
            "stack": settings.STACK
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return Response(data, status=status.HTTP_200_OK, content_type="application/json")
