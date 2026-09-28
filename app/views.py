from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView as ApiView

from app.models import Users
from app.serializers import UserSerializer

class UserView(ApiView):

    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

