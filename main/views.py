from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes
from .models import ModelManagement
from .serializers import ModelManagementSerializer

@api_view(['GET','POST'])
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
