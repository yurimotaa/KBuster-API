from rest_framework.views import APIView, Request, Response, status
from users.models import User
from users.serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import GetUserPermission
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserGetIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [GetUserPermission]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)

        # Verificar se a senha está presente nos dados enviados
        if "password" in request.data:
            # Criar o hash da nova senha
            new_password = make_password(request.data["password"])
            request.data["password"] = new_password

        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
