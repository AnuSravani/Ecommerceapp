from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Products,Categories
from .serializers import CategorySerializer,ProductSerializer,UserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework import authentication,permissions
# Create your views here.

class CustomerView(ViewSet):


    def list(self,request,*args,**kwargs):
        qs=User.objects.all()
        serializer=UserSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def create (self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            user=User.objects.create_user(**serializer.validated_data)
            serializer=UserSerializer(user,many=False)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=User.objects.get(id=id)
        serializer=UserSerializer(qs,many=False)
        return Response(data=serializer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=User.objects.get(id=id)
        serializer=UserSerializer(data=request.data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        User.objects.get(id=id).delete()
        return Response(data="deleted") 

     

class CategoryView(ModelViewSet):
    serializer_class=CategorySerializer
    queryset=Categories.objects.all()

class ProductsView(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProductSerializer
    model=Products
    queryset=Products.objects.all()

    def create(self, request, *args, **kwargs):
        raise serializers.ValidationError("method not allowed")

    @action(methods=["POST"],detail=True)
    def product_make(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        category=Categories.objects.get(id=id)
        user=User.objects.get(id=id)
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=category,customer=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
   
    def list(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    @action(methods=["POST"],detail=True)
    def status_done(self,request,*args,**kwargs):
        # qs=self.get_object()
        id=kwargs.get("pk")
        Products.objects.filter(id=id).update(is_active=True)
        return Response(data="updated")
        
    @action(methods=["GET"],detail=False)
    def incomplete_Product(self,request,*args,**kwargs):
        qs=Products.objects.filter(is_active=False)
        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    @action(methods=["POST"],detail=True)
    def statusnot_done(self,request,*args,**kwargs):
        # qs=self.get_object()
        id=kwargs.get("pk")
        Products.objects.filter(id=id).update(is_active=False)
        return Response(data="updated")
    
