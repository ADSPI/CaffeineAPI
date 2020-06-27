from rest_framework.views import Response
from rest_framework import status


class AppResponse:
    @staticmethod
    def get_success(data=None):
        return Response({
            "success": True,
            "data": data
        })
    @staticmethod
    def get_error(reason="Error", statuscode=status.HTTP_500_INTERNAL_SERVER_ERROR):
        return Response({
            "success": False,
            "reason": reason
        }, status=statuscode)

    @staticmethod
    def get_forbidden():
        return AppResponse.get_error(reason='Forbidden',statuscode=status.HTTP_403_FORBIDDEN)