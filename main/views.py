from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import ModelManagement
from .serializers import ModelManagementSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

def login_page(request):
    return render(request, 'login.html')

def index_page(request):
    return render(request, 'index.html')

def create_page(request):
        return render(request, 'crud-op/create.html')

def read_page(request):
    return render(request, 'crud-op/read.html')

def update_page(request):
    return render(request, 'crud-op/update.html')

def delete_page(request):
    return render(request, 'crud-op/delete.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    username = (request.data.get('username'))
    password = (request.data.get('password'))

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.id,
            "username": user.username
        }, status=status.HTTP_200_OK)
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def model_management_list(request):
    if request.method == 'GET':
        try:
            models = ModelManagement.objects.all()
            serializer = ModelManagementSerializer(models, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
        try:
            serializer = ModelManagementSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        try:
            model_id = request.data.get('id')
            if not model_id:
                return Response({"error": "Model ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            model = ModelManagement.objects.get(model_id=model_id)
            model.delete()
            return Response({"message": "Model deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except ModelManagement.DoesNotExist:
            return Response({"error": "Model not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    elif request.method == 'PUT':
        try:
            model_id = request.data.get('model_id')
            if not model_id:
                return Response({"error": "Model ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            model = ModelManagement.objects.get(model_id=model_id)
            serializer = ModelManagementSerializer(model, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ModelManagement.DoesNotExist:
            return Response({"error": "Model not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


