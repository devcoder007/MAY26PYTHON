from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserApisSerializer
from .models import UserApis
from django.shortcuts import get_object_or_404
# Create your views here.


class UserApisView(APIView):
    def get(self, request):
        print(request.data)
        queryset  = UserApis.objects.filter(email=request.data.get('email'))

        if queryset:
            if queryset.values('password').first()['password'] == request.data.get('password'):

                return Response("Succesfully logged in")
            else:
                return Response("Password Incorrect")
        else:
            return Response("User not registered")

    def post(self, request):
        queryset = request.data 
        serializer = UserApisSerializer(data=queryset)

        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()

        return Response ({"Success":"User {} creatred".format(save_data.name)})


    def delete(self, request, pk):
        queryset = get_object_or_404(UserApis.objects.all(), pk=pk)
        queryset.delete()
        return Response("User Deleted succesfully")


