from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from account.api.serializers import UserSerializer, UserRegisterSerializer
from account.models import User

from rest_framework_simplejwt.authentication import JWTAuthentication, JWTTokenUserAuthentication


# @login_required(login_url="/login/")
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def manage_user(request):
    user = User.objects.get(email='pranav@gmail.com')
    serializer = UserSerializer(user, )
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ManageUser(APIView):
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    # serializer_class = UserSerializer

    def get(self, request):
        user = User.objects.get(email=request.user.email)
        serializer = UserSerializer(user, )
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(data=request.data, instance=request.user)
        print("data: ", request.headers)

        if serializer.is_valid():
            serializer.update(request.user, request.data,)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        # return self.update(request.user, request.data)
        return Response()
