import streamlit as st
from prediction_helper import predict  # Ensure this is correctly linked to your prediction_helper.py

# Set the page configuration and title
st.set_page_config(page_title="Hotel Booking Status", page_icon="📊")
st.title("Hotel Booking Status")
# Create rows of three columns each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(2)

# Assign inputs to all rows with default values
with row1[0]:
    no_of_adults = st.number_input('no_of_adults', min_value=0, step=1, max_value=10, value=3)
with row1[1]:
     no_of_weekend_nights= st.number_input('no_of_weekend_nights', min_value=0, value=2)
with row1[2]:
    no_of_week_nights = st.number_input('no_of_week_nights', min_value=0, value=4)

with row2[0]:
    required_car_parking_space = st.selectbox('required_car_parking_space', [0, 1])
with row2[1]:
    lead_time = st.number_input('lead_time', min_value=0, value=5)
with row2[2]:
    repeated_guest = st.selectbox('repeated_guest', [0, 1])

with row3[0]:
    no_of_special_requests = st.number_input('no_of_special_requests', min_value=0, max_value=10, step=1, value=3)
with row3[1]:
    no_of_previous_bookings_not_canceled = st.number_input('no_of_previous_bookings_not_canceled', min_value=0, max_value=100, value=30)
with row3[2]:
    avg_price_per_room = st.number_input('avg_price_per_room', min_value=0)

with row4[0]:
    type_of_meal_plan = st.selectbox(' type_of_meal_plan', ['Not Selected', 'Meal plan 1', 'Meal plan 2', 'Meal plan 3'])
with row4[1]:
    market_segment_type = st.selectbox('market_segment_type', ['Online', 'Offline', 'Corporate', 'Complementary', 'Aviation'])



# Button to calculate risk
if st.button('Booking Status'):
    # Call the predict function from the helper module
    # print((age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
    #                                             delinquency_ratio, credit_utilization_ratio, num_open_accounts,
    #                                             residence_type, loan_purpose, loan_type))
    booking_status = predict(no_of_adults,no_of_weekend_nights,no_of_week_nights,type_of_meal_plan,
                   required_car_parking_space,lead_time,market_segment_type,repeated_guest,
                    no_of_previous_bookings_not_canceled,avg_price_per_room,no_of_special_requests)

    # Display the results
    st.write(f"Booking status : {booking_status}")

    # use 'print' option to view result values in Terminal' after clicking
    #  on  'Booking status' button in built_app using streamlit app
 #   print(f"Booking status : {y_pred}")


# Footer
# st.markdown('_Project From Codebasics ML Course_')



