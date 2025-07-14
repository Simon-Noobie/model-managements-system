from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import ModelManagement, UserProfile
from .serializers import ModelManagementSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import RestrictedAccessMixin

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index_page')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

class index_page(LoginRequiredMixin, RestrictedAccessMixin, TemplateView):
    template_name = 'index.html'

class create_page(LoginRequiredMixin, RestrictedAccessMixin, TemplateView):
    template_name = 'crud-op/create.html'

class read_page(LoginRequiredMixin, RestrictedAccessMixin, TemplateView):
    template_name = 'crud-op/read.html'

class update_page(LoginRequiredMixin, RestrictedAccessMixin, TemplateView):
    template_name = 'crud-op/update.html'

class delete_page(LoginRequiredMixin, RestrictedAccessMixin, TemplateView):
    template_name = 'crud-op/delete.html'

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists')
                return render(request, 'register.html', {'form': form})

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            profile = UserProfile.objects.create(
                user=user,
                name=name,
                email=email,
                password=password
            )
            profile.save()

            return redirect('login_page')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

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
    # Check permissions for non-superusers on restricted methods
    if not request.user.is_superuser and request.method in ['DELETE', 'PUT']:
        return Response({"error": "You don't have permission to perform this action."},
                       status=status.HTTP_403_FORBIDDEN)

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