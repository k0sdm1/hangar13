from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.accounts.models import CustomUser


class UserViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["POST"])
    def is_username_available(self, request):
        """
        Returns True if username is available.
        """
        data = request.data
        if "username" not in data:
            return Response({"errors": True, "message": "No username in the payload"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            username = str(data["username"])
            return Response(
                {
                    "errors": False,
                    "message": "",
                    "data": {
                        "result": not CustomUser.objects.filter(
                            username=username,
                        ).exists()
                    },
                }, status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "errors": True,
                    "message": f"Во время выполнения запроса произошла ошибка: {str(e)}",
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=["POST"])
    def is_display_name_available(self, request):
        """
        Returns True if display name is available.
        """
        data = request.data
        if "username" not in data:
            return Response({"errors": True, "message": "No username in the payload"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            username = str(data["username"])
            return Response(
                {
                    "errors": False,
                    "message": "",
                    "data": {
                        "result": not CustomUser.objects.filter(
                            username=username,
                        ).exists()
                    },
                }, status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "errors": True,
                    "message": f"Во время выполнения запроса произошла ошибка: {str(e)}",
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )