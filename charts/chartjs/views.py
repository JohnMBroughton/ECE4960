# from django.http import JsonResponse

from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

from chartjs.models import LotSize
from chartjs.models import RFID


class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'chartjs/index.html')


####################################################

## if you don't want to user rest_framework

# def get_data(request, *args, **kwargs):
#
# data ={
#			 "sales" : 100,
#			 "person": 10000,
#	 }
#
# return JsonResponse(data) # http response


#######################################################

## using rest_framework classes

class ChartData(APIView):
	authentication_classes = []
	permission_classes = []

	def get(self, request, format = None):
		labels = [LotSize.name for LotSize in LotSize.objects.all()]
		chartLabel = "Number of Available Spaces"
		
		chartdata = [(LotSize.num_spaces - RFID.objects.filter(Lot=LotSize.name).count()) for LotSize in LotSize.objects.all()]
		data ={
					"labels":labels,
					"chartLabel":chartLabel,
					"chartdata":chartdata,
			}
		return Response(data)
