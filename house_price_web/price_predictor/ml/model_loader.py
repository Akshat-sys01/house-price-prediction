import logging
import pickle
import os

logger = logging.getLogger('price_predictor')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MODEL_PATH = os.path.join(BASE_DIR, 'model', 'house_price_model.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'model', 'scaler.pkl')

def load_model():
    logger.info("Loading ML model")
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    logger.info("ML model loaded successfully!")
    return model

def load_scaler():
    with open(SCALER_PATH, 'rb') as f:
        scaler = pickle.load(f)
    return scaler