from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import API_Key
import datetime
from django.utils import timezone
import pytz

from PIL import Image, ImageOps
import numpy as np
import requests

CALL_LIMIT_TIME = 30
IMG_SIZE = 128
PREDICTION_API_URL = "PREDICTION_API_URL"

@api_view(["GET"])
def main(request):
	data = {}
	data["message"] = "Up and running!"
	return Response(data)

@api_view(["POST"])
def predict(request):
	data = {}
	try:
		key = request.data["key"]
	except:
		data["detail"] = "API Key was not provided."
		return Response(data, status=status.HTTP_400_BAD_REQUEST)

	try:
		api_key = API_Key.objects.get(key=key)
	except:
		data["detail"] = "API Key is not valid."
		return Response(data, status=status.HTTP_400_BAD_REQUEST)

	print(api_key.last_called)

	if (datetime.datetime.now() - api_key.last_called.replace(tzinfo=None)).seconds < CALL_LIMIT_TIME:
		data["detail"] = "API key was used too recently."
		return Response(data, status=status.HTTP_400_BAD_REQUEST)

	try:
		image = request.data["image"]
	except:
		data["detail"] = "Image was not provided."
		return Response(data, status=status.HTTP_400_BAD_REQUEST)

	api_key.last_called = timezone.now()
	api_key.save()

	image = Image.open(image)
	image = ImageOps.grayscale(image)
	image = image.resize((IMG_SIZE, IMG_SIZE))
	image = np.asarray(image)

	prediction = requests.post(PREDICTION_API_URL, json={"image": image.tolist()}).json()

	data["classification"] = "Pneumonia" if prediction["probability"] > 0.5 else "No Pneumonia"
	data["probability"] = round(prediction["probability"] * 100, 2)
	return Response(data)
