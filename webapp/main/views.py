from django.shortcuts import render

from PIL import Image, ImageOps
import numpy as np
import requests

IMG_SIZE = 128
PREDICTION_API_URL = "PREDICTION_API_URL"

def index(request):
	if request.method == "POST":
		image = request.FILES["image_field"]
		image = Image.open(image)
		image = ImageOps.grayscale(image)
		image = image.resize((IMG_SIZE, IMG_SIZE))
		image = np.asarray(image)

		prediction = requests.post(PREDICTION_API_URL, json={"image": image.tolist()}).json()

		context = {}
		context["classification"] = "Pneumonia" if prediction["probability"] > 0.5 else "No Pneumonia"
		context["probability"] = str(round(prediction["probability"] * 100, 2)) + "%"
		return render(request, "main/index.html", context)

	return render(request, "main/index.html")

def info(request):
	return render(request, "main/info.html")
