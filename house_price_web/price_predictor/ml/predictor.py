import logging
import numpy as np
from .model_loader import load_model, load_scaler

logger = logging.getLogger('price_predictor')

# Load once
model = load_model()
scaler = load_scaler()

# Hardcoded RMSE (from training metrics)
RMSE = 4.939058614756458

def predict_price_with_confidence(area, bedrooms, bathrooms, age):
    """
    Takes raw user input and returns predicted house price
    """
    logger.info("ML prediction started")

    # Feature engineering
    total_rooms = bedrooms + bathrooms
    area_per_room = area / total_rooms

    if age <= 5:
        age_category = 0
    elif age <= 15:
        age_category = 1
    else:
        age_category = 2

    input_data = np.array([
        [
            area,
            bedrooms,
            bathrooms,
            age,
            total_rooms,
            age_category,
            area_per_room
        ]
    ])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]
    lower_price = prediction - RMSE
    upper_price = prediction + RMSE

    logger.info(
        "ML prediction completed | predicted=%s, range=(%s, %s)",
        prediction, lower_price, upper_price
    )

    return {
        "prediction": round(prediction, 2),
        "lower": round(lower_price, 2),
        "upper": round(upper_price, 2)
    }