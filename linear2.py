import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Load the historical dataset
data = pd.read_csv('updated_custom_historical_ev_data.csv')

# Preprocess the dataset
data = data.dropna()  # Handle missing values

# Encode categorical features 
label_encoders = {}
for column in ['Username', 'Make & Model', 'Driving Style', 'Terrain', 'Speed Mode', 'Season', 'Tyre Pressure', 'Load']:
    le = LabelEncoder()
    if column != 'Username':
        data[column + '_encoded'] = le.fit_transform(data[column].str.capitalize())
    else:
        data[column + '_encoded'] = le.fit_transform(data[column])
    label_encoders[column] = le

# Split the data (including encoded tyre pressure and load)
X = data[['Username_encoded', 'Season_encoded', 'Battery SOC (%)', 'Battery Capacity (kWh)', 
          'Claimed Range (km)', 'Driving Style_encoded', 'Terrain_encoded', 'Speed Mode_encoded', 
          'Tyre Pressure_encoded', 'Load_encoded']]  # Include Tyre Pressure and Load
y = data['Actual Range (km)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)  # Make sure to use y_train here!

# Evaluate the model
y_pred = model.predict(X_test)
print('Mean Absolute Error (Linear Regression):', mean_absolute_error(y_test, y_pred))

# Function to predict range and display other information 
def predict_range(username):
    # Find the user's data from the historical dataset
    user_data = data[data['Username'] == username]

    # Handle case where username is not found
    if user_data.empty:
        print(f"Error: Username '{username}' not found in the historical data.")
        return  

    # Extract and display relevant information
    user_data = user_data.iloc[0]
    print("User:", username)
    print("Make & Model:", user_data['Make & Model'])
    print("Battery Capacity:", user_data['Battery Capacity (kWh)'], "kWh")
    print("Claimed Range:", user_data['Claimed Range (km)'], "km")
    print("Driving Style:", user_data['Driving Style'])
    print("Terrain:", user_data['Terrain'])
    print("Speed Mode:", user_data['Speed Mode'])

    # Get input from the user
    while True:
        try:
            soc = float(input("Enter the Battery SOC (%): "))
            if 0 <= soc <= 100:
                break
            else:
                print("Invalid SOC. Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value for SOC.")

    season = input("Enter the Season (Summer, Winter, Monsoon, Spring): ").capitalize()
    tyre_pressure = input("Enter Tyre Pressure (Normal, Under): ").capitalize()
    load = input("Enter Load (Light, Moderate, Heavy): ").capitalize()

    # Create input data for prediction (including encoded tyre pressure and load)
    input_data = pd.DataFrame([[label_encoders['Username'].transform([username])[0],
                               label_encoders['Season'].transform([season])[0],
                               soc, user_data['Battery Capacity (kWh)'], user_data['Claimed Range (km)'],
                               label_encoders['Driving Style'].transform([user_data['Driving Style']])[0],
                               label_encoders['Terrain'].transform([user_data['Terrain']])[0],
                               label_encoders['Speed Mode'].transform([user_data['Speed Mode']])[0],
                               label_encoders['Tyre Pressure'].transform([tyre_pressure])[0],  # Encoded Tyre Pressure
                               label_encoders['Load'].transform([load])[0]]],                  # Encoded Load
                             columns=['Username_encoded', 'Season_encoded', 'Battery SOC (%)',
                                      'Battery Capacity (kWh)', 'Claimed Range (km)',
                                      'Driving Style_encoded', 'Terrain_encoded', 'Speed Mode_encoded',
                                      'Tyre Pressure_encoded', 'Load_encoded'])  # Include Tyre Pressure and Load
    
    # Predict the range for the current SOC
    predicted_range = model.predict(input_data)[0] 
    print("Predicted Range:", predicted_range, "km")  

    # --- GRAPHING SECTION ---
    # Predict range for a range of SOC values (in reverse order)
    soc_values = list(range(0, 101, 10))  # SOC values from 0% to 100% 
    predicted_ranges = []
    for soc in soc_values:
        input_data['Battery SOC (%)'] = soc  # Update SOC in the input data
        predicted_range = model.predict(input_data)[0]
        predicted_ranges.append(predicted_range)

    # Create a curve graph (line plot)
    fig, ax = plt.subplots() # Create a figure and axes object
    ax.plot(soc_values, predicted_ranges, marker='o', linestyle='-') 
    ax.set_xlabel('Battery SOC (%)')
    ax.set_ylabel('Predicted Range (km)')
    ax.set_title('Predicted Range vs SOC')
    ax.grid(True)  # Add grid lines

    # Set x-axis ticks to show in descending order
    ax.set_xticks(soc_values) 

    # Set the limits of x and y axes to start from 0
    ax.set_xlim(100, 0)
    #ax.set_ylim(0, max(predicted_ranges)) # You may want to set the ylim based on your data

    plt.show()

# Example user input
username = input("Enter your username: ")
predict_range(username)