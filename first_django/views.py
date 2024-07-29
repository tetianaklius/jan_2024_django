from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from first_django.models import CarModel


class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        res = [model_to_dict(car) for car in cars]
        return Response(res, status.HTTP_200_OK)
        # return Response("hello from get all")

    def post(self, *args, **kwargs):
        data = self.request.data
        car = CarModel.objects.create(**data)
        car_dict = model_to_dict(car)
        return Response(car_dict, status.HTTP_201_CREATED)
        # return Response("hello from post")


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = self.kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response("not found", status.HTTP_404_NOT_FOUND)
        return Response(model_to_dict(car), status.HTTP_200_OK)

        # print(self.request.query_params.dict())
        # return Response("hello from get single")

    def put(self, *args, **kwargs):
        pk = kwargs["pk"]
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response("not found", status.HTTP_404_NOT_FOUND)
        car.brand = data["brand"]
        car.price = data["price"]
        car.year = data["year"]
        car.save()

        return Response(model_to_dict(car), status.HTTP_200_OK)
        # return Response("hello from put")

    # def patch(self, *args, **kwargs):
    #     return Response("hello from patch")

    def delete(self, *args, **kwargs):
        pk = self.kwargs["pk"]
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            return Response("not found", status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
