from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission

from rest_framework.throttling import UserRateThrottle


from app.models import Stu
from app.serializers import Stuserializers
from rest_framework import mixins

# class Mypermission(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         pass



class StuListViewSet(mixins.ListModelMixin,mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Stu.objects.all()
    serializer_class = Stuserializers

    authentication_classes = (SessionAuthentication, BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    throttle_classes = (UserRateThrottle,)

    def printsomething(self,request):
        if request.data:
            print(request.data)
            return True
        else:
            return False

# class StuListViewSet(APIView):
#     def get(self,request,format=None):
#         stu = Stu.objects.all()
#         serializer = Stuserializers(stu,many=True)
#         return Response(serializer.data)