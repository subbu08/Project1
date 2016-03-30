import graphlab
def get_residual_sum_of_squares(model, data, outcome):
    # First get the predictions
    
    y_hat = model.predict( data )

    # Then compute the residuals/errors
    error_y = outcome - y_hat 

    # Then square and add them up
    error_y2 = error_y * error_y
    RSS = error_y2.sum()

    return(RSS)    
    
model_1_features = ['sqft_living', 'bedrooms', 'bathrooms', 'lat', 'long']
model_2_features = model_1_features + ['bed_bath_rooms']
model_3_features = model_2_features + ['bedrooms_squared', 'log_sqft_living', 'lat_plus_long']
