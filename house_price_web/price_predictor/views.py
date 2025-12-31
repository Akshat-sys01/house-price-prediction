from django.shortcuts import render
from django.conf import settings
import pickle
import numpy as np
import os

# Load the model
BASE_DIR = settings.BASE_DIR
model_path = os.path.join(
    BASE_DIR.parent,
    "model",
    "house_price_model.pkl"
)

with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Create your views here.
def home(request):
    prediction = None
    error = None

    if request.method == 'POST':
        try:   
            area = float(request.POST.get('area'))
            bedrooms = float(request.POST.get('bedrooms'))
            bathrooms = float(request.POST.get('bathrooms'))
            age = float(request.POST.get('age'))

            # Validation rules
            if area <= 0 or bedrooms <= 0 or bathrooms <= 0 or age < 0:
                raise ValueError("Invalid input values")

            # Prepare data for model
            input_data = np.array([[area, bedrooms, bathrooms, age]])
        
            # Predict
            prediction = round(model.predict(input_data)[0], 2)

        except:
            error = "Please enter valid positive values."

    return render(request, 'home.html', {
        'prediction': prediction,
        'error': error
    })