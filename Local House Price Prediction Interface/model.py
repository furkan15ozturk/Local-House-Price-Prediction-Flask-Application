from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import pickle

with open('Model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)