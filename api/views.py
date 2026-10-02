"""
SVCloud API views.

Stage 1: Health check only.
"""

from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema


class HealthCheckView(APIView):
    """
    Simple health check to confirm the SVCloud API is running.

    Returns {"status": "ok"} when the server is healthy.
    """

    @extend_schema(
        summary="Health check",
        description="Returns a simple status response confirming the API is running.",
        responses={
            200: {
                "type": "object",
                "properties": {
                    "status": {
                        "type": "string",
                        "example": "ok",
                    },
                },
            },
        },
    )
    def get(self, request):
        return Response({"status": "ok"})
