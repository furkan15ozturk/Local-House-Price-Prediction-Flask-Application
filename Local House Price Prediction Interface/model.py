import tensorflow as tf
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import RootMeanSquaredError
import locale


with open(r'C:\Users\furka\OneDrive\Masaüstü\GPII Project\Local House Price Prediction Interface\Model\scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


def preprocessor(X):
  A = np.copy(X)
  A = scaler.transform(X)
  return A


deep_learning_model = Sequential([
    InputLayer((13,)),
    Dense(32, activation='relu'),
    Dropout(0.2),
    Dense(16, activation='relu'),
    Dropout(0.1),
    Dense(1, activation='linear')
])

opt = Adam(learning_rate=0.1)
deep_learning_model.compile(optimizer=opt, loss='mse', metrics=[RootMeanSquaredError()])

deep_learning_model.load_weights(r'C:\Users\furka\OneDrive\Masaüstü\GPII Project\Local House Price Prediction Interface\Model\large_nn_weights.h5')

locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')


def prediction(area, absolute_area, room, floor_count, building_age, lat, lng, model_number=0):
    area_abs_area_difference = area - absolute_area
    area_room_ratio = area / room
    building_age_new = float(0)
    building_age_young = float(0)
    building_age_mid = float(0)
    building_age_old = float(0)
    building_age_very_old = float(0)
    if 5 >= building_age >= 0:
        building_age_new = float(1)
        building_age_young = float(0)
        building_age_mid = float(0)
        building_age_old = float(0)
        building_age_very_old = float(0)
    elif 10 >= building_age > 5:
        building_age_new = float(0)
        building_age_young = float(1)
        building_age_mid = float(0)
        building_age_old = float(0)
        building_age_very_old = float(0)
    elif 15 >= building_age > 10:
        building_age_new = float(0)
        building_age_young = float(0)
        building_age_mid = float(1)
        building_age_old = float(0)
        building_age_very_old = float(0)
    elif 20 >= building_age > 15:
        building_age_new = float(0)
        building_age_young = float(0)
        building_age_mid = float(0)
        building_age_old = float(1)
        building_age_very_old = float(0)
    elif building_age > 20:
        building_age_new = float(0)
        building_age_young = float(0)
        building_age_mid = float(0)
        building_age_old = float(0)
        building_age_very_old = float(1)

    input_values = np.array([area, absolute_area, room, floor_count, lat, lng,
                             area_abs_area_difference, area_room_ratio,
                             building_age_new, building_age_young, building_age_mid, building_age_old,
                             building_age_very_old])

    preprocessed_input = preprocessor(input_values.reshape(1, -1))
    if model_number == 0:
        # _prediction = linear_regression_model.predict(preprocessed_input)
        pass
    elif model_number == 1:
        # _prediction = knn_model.predict(preprocessed_input)
        pass
    elif model_number == 2:
        # _prediction = rfr_model.predict(preprocessed_input)
        pass
    elif model_number == 3:
        # _prediction = gbr_model.predict(preprocessed_input)
        pass
    elif model_number == 4:
        _prediction = deep_learning_model.predict(preprocessed_input)



    # Round the number
    rounded_number = round(int(_prediction[0][0]), -4)

    # Format the number with grouping and currency symbol
    formatted_number = locale.format_string('%.0f', rounded_number, grouping=True)

    # Add the currency symbol
    formatted_number += ' TL'

    return formatted_number

