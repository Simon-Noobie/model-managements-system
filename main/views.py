from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from .models import ModelManagement
from .serializers import ModelManagementSerializer

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def model_management_list(request):
    if request.method == 'GET':
        models = ModelManagement.objects.all()
        serializer = ModelManagementSerializer(models, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ModelManagementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        model_id = request.data.get('id')
        if not model_id:
            return Response({"error": "Model ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fixed: Use model_id instead of id for the primary key
            model = ModelManagement.objects.get(model_id=model_id)
            model.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ModelManagement.DoesNotExist:
            return Response({"error": "Model not found"}, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'PUT':
        model_id = request.data.get('model_id')  # Fixed: Use model_id
        if not model_id:
            return Response({"error": "Model ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fixed: Use model_id instead of id for the primary key
            model = ModelManagement.objects.get(model_id=model_id)
            serializer = ModelManagementSerializer(model, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ModelManagement.DoesNotExist:
            return Response({"error": "Model not found"}, status=status.HTTP_404_NOT_FOUND)
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from .models import ModelManagement
from .serializers import ModelManagementSerializer

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def model_management_list(request):
    if request.method == 'GET':
        models = ModelManagement.objects.all()
        serializer = ModelManagementSerializer(models, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ModelManagementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        model_id = request.data.get('id')
        if not model_id:
            return Response({"error": "Model ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fixed: Use model_id instead of id for the primary key
            model = ModelManagement.objects.get(model_id=model_id)
            model.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ModelManagement.DoesNotExist:
            return Response({"error": "Model not found"}, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'PUT':
        model_id = request.data.get('model_id')  # Fixed: Use model_id
        if not model_id:
            return Response({"error": "Model ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fixed: Use model_id instead of id for the primary key
            model = ModelManagement.objects.get(model_id=model_id)
            serializer = ModelManagementSerializer(model, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ModelManagement.DoesNotExist:
            return Response({"error": "Model not found"}, status=status.HTTP_404_NOT_FOUND)