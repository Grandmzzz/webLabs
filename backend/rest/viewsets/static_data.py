from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_INTEGER, TYPE_STRING
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class StaticDataViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_description="Возвращает тестовые данные для проверки работоспособности сервера",
        responses={200: Schema(
            type=TYPE_OBJECT,
            properties={
                "id": Schema(type=TYPE_INTEGER),
                "description": Schema(type=TYPE_STRING)
            }
        )})
    @action(methods=["get"], detail=False)
    def get_test_data(self, request):
        return Response([
            {
                "id": id_index,
                "description": chr(ord("a") + id_index)
            }
            for id_index in range(13)
        ])
