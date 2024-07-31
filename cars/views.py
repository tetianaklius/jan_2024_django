# from django.forms import model_to_dict
# from rest_framework import status
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
# from cars.models import CarModel
# from cars.serializers import CarSerializer
#
#
# class CarListCreateView(GenericAPIView):
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         cars = CarModel.objects.all()
#         res = [model_to_dict(car) for car in cars]
#         return Response(res, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         car = CarModel.objects.create(**data)
#         car_dict = model_to_dict(car)
#         return Response(car_dict, status.HTTP_201_CREATED)
#         # return Response("hello from post")
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     def get(self, *args, **kwargs):
#         pk = self.kwargs['pk']
#         try:
#             car = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             return Response("not found", status.HTTP_404_NOT_FOUND)
#         return Response(model_to_dict(car), status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = kwargs["pk"]
#         data = self.request.data
#         try:
#             car = CarModel.objects.get(pk=pk)
#         except CarModel.DoesNotExist:
#             return Response("not found", status.HTTP_404_NOT_FOUND)
#         car.brand = data["brand"]
#         car.price = data["price"]
#         car.year = data["year"]
#         car.save()
#
#         return Response(model_to_dict(car), status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = self.kwargs["pk"]
#         try:
#             car = CarModel.objects.get(pk=pk)
#             car.delete()
#         except CarModel.DoesNotExist:
#             return Response("not found", status.HTTP_404_NOT_FOUND)
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin

from cars.filter import car_filter
from cars.models import CarModel
from cars.serializers import CarSerializer


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()




