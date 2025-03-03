from django.shortcuts import render

# Create your views here.
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from django.shortcuts import render
from .forms import BarcodeUploadForm
from .models import Barcode

def scan_barcode(request):
    if request.method == "POST":
        form = BarcodeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            barcode_obj = form.save()
            image_path = barcode_obj.image.path
            
            # Read Image using OpenCV
            image = cv2.imread(image_path)
            barcodes = decode(image)

            barcode_data = []
            for barcode in barcodes:
                barcode_text = barcode.data.decode("utf-8")
                barcode_data.append(barcode_text)

            return render(request, "barcode_scanner/result.html", {"barcode_data": barcode_data})
    else:
        form = BarcodeUploadForm()

    return render(request, "barcode_scanner/upload.html", {"form": form})
