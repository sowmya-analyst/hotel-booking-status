import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Path to the saved model and its components
MODEL_PATH = 'artifacts/model_data.joblib'

# Load the model and its components
model_data = joblib.load(MODEL_PATH)
model = model_data['model']
scaler = model_data['scaler']
features = model_data['features']   # features in x_train_1_encoded or x_test_encoded df
cols_to_scale = model_data['cols_to_scale']


def prepare_input(no_of_adults,no_of_weekend_nights,no_of_week_nights,type_of_meal_plan,
                   required_car_parking_space,lead_time,market_segment_type,repeated_guest,
                     no_of_previous_bookings_not_canceled,avg_price_per_room,
                     no_of_special_requests):

    # Create a dictionary with input values and dummy values for missing features
    input_data = {
        'no_of_adults': no_of_adults,
        'no_of_weekend_nights': no_of_weekend_nights,
        'no_of_week_nights': no_of_week_nights,
        'type_of_meal_plan': type_of_meal_plan,
        'required_car_parking_space': required_car_parking_space,
        'lead_time':lead_time,
        'market_segment_type': market_segment_type,
        'repeated_guest': repeated_guest,
        'no_of_previous_bookings_not_canceled': no_of_previous_bookings_not_canceled,
        'avg_price_per_room': avg_price_per_room,
        'no_of_special_requests': no_of_special_requests,
        # additional dummy fields just for scaling purpose
        'no_of_children': 1 ,   #dummy value
        'no_of_previous_cancellations': 1,  #dummy value
        'type_of_meal_plan_Meal Plan 2': 1,  #dummy value
        'type_of_meal_plan_Meal Plan 3': 1,  #dummy value
        'type_of_meal_plan_Not Selected': 1,  #dummy value
        'market_segment_type_Complementary': 1, #dummy value
        'market_segment_type_Corporate': 1,   #dummy value
        'market_segment_type_Offline': 1,    #dummy value
        'market_segment_type_Online': 1     #dummy value
    }

    # Ensure all columns for features and cols_to_scale are present
    df = pd.DataFrame([input_data])

    # Ensure only required columns for scaling are scaled
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])

    # Ensure the DataFrame contains only the features expected by the model
    df = df[features]

    return df


def predict(no_of_adults,no_of_weekend_nights,no_of_week_nights,type_of_meal_plan,
                   required_car_parking_space,lead_time,market_segment_type,repeated_guest,
                     no_of_previous_bookings_not_canceled,avg_price_per_room,
                     no_of_special_requests):
    # Prepare input data
    input_df = prepare_input(no_of_adults,no_of_weekend_nights,no_of_week_nights,type_of_meal_plan,
                   required_car_parking_space,lead_time,market_segment_type,repeated_guest,
                     no_of_previous_bookings_not_canceled,avg_price_per_room,
                     no_of_special_requests)

    booking_status = find_booking_status(input_df)
    return booking_status

def find_booking_status(input_df):
    if model.predict(input_df) == 1:
            return "Canceled"
    else:
            return 'Not Canceled'

