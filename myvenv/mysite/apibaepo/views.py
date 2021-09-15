from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .serializers import LiftSerializer,LiftModifySerializer
from .models import Lift  # model 호출


def lift_view(request):
    lifts = Lift.objects.all()
    return render(request, 'index.html', {'lifts': lifts})


class LiftViewSet(ModelViewSet):
    queryset = Lift.objects.all()
    serializer_class = LiftSerializer


lift_list = LiftViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

lift_detail = LiftViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
