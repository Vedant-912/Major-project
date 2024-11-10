import pandas as pd

# --- Combined EV data (4-wheelers and 2-wheelers) - CORRECTED ---
ev_data = {
    'Make & Model': [
        'BYD E6', 'BYD Seal', 'BYD Atto 3', 'Mahindra XUV400', 'Citroen eC3',
        'Hyundai Kona Electric', 'Hyundai Ioniq 5', 'Kia EV6',
        'Tata Punch EV Medium Range', 'Tata Punch EV Long Range', 'Tata Tiago EV',
        'Tata Tigor EV', 'Tata Nexon EV Medium Range', 'Tata Nexon EV Long Range',
        'Tata Curvv EV Medium Range', 'Tata Curvv Long Range', 'MG ZS EV',
        'MG Comet EV', 'MG Windsor EV', 'Mercedes-Benz EQS', 'Mercedes-Benz EQB',
        'Mercedes-Benz EQA', 'Mercedes-Benz EQE', 'Lotus Eletre', 'BMW iX',
        'BMW iX1', 'BMW i7', 'BMW i5', 'BMW i4', 'Rolls Royce Spectre',
        'Mini Cooper SE', 'Mini Cooper Countryman Electric', 'Jaguar I-Pace',
        'Volvo XC40 Recharge', 'Volvo C40 Recharge', 'Audi e-tron',
        'Audi e-tron GT', 'Audi Q8 e-tron', 'Porsche Taycan', 'Porsche Taycan GT',
        'Porsche Macan EV', 'Rivian R1S', 'Rivian R1T', 'Tesla Model S',
        'Tesla Model Y', 'Tesla Model 3', 'Tesla Model X', 'Tesla Cybertruck',
        'Hummer EV', 'Ford F150 Lightning', 'Mustang Mach-E', 'Lucid Air',
        'Volkswagen ID.4', 'Volkswagen ID.7', 'Volkswagen ID.Buzz',
        'Skoda Enyaq 4', 'Polestar 2', 'Nissan Leaf', 'Nissan Ariya',
        'Chevrolet Blazer EV', 'Chevrolet Silverado EV', 'Chevrolet Equinox EV',
        'Audi Q4 e-tron', 'BMW i3', 'BYD Dolphin',
        'Bajaj Chetak', 'Ola S1 2 kWh', 'Ola S1 3 kWh', 'TVS iQube',
        'Revolt RV400', 'Ultraviolette F77', 'Tork Kratos R',
        'Matter Aera', 'Hero Electric Optima', 'Ampere Magnus EX',
        'TVS X', 'Vida V1', 'Ather 450X', 'Ather 450',
        'Ola S1 Pro 4 kWh', 'Ola S1 Air 2 kWh', 'Ola S1 Air 3 kWh',
        'Ola S1 Air 4 kWh', 'Ola S1 X 2 kWh', 'Ola S1 X 3 kWh',
        'Ola S1 X 4 kWh', 'Ola S1 X+ 3 kWh'
    ],
    'kWh': [
        71.7, 82.5, 60.48, 34.5, 29.2, 39.2, 58, 77.4, 40, 60, 24, 26, 30, 40.5,
        40, 60, 50.3, 17.3, 60, 107.8, 66.5, 66.5, 90.6, 112, 76.6, 64.7,
        101.7, 80.7, 83.9, 120, 32.6, 60, 90, 78, 75, 95, 95, 106, 93.4, 100,
        75, 135, 135, 100, 75, 50, 100, 100, 200, 131, 98, 118, 82, 77, 62, 82,
        45, 62, 40, 65, 50, 107, 55, 77, 40, 3, 2, 3, 4.56, 3.24, 4.2,
        4, 5, 2.9, 2.6, 4.44, 3.94, 2.91, 2.41, 3.97, 2, 3, 4, 2, 3, 4, 3
    ],
    'Claimed Range (km)': [
        520, 700, 521, 456, 320, 452, 481, 528, 300, 400, 315, 315, 312, 453,
        400, 500, 461, 230, 450, 770, 419, 429, 590, 600, 600, 470, 600, 590,
        520, 650, 270, 400, 470, 423, 418, 488, 551, 582, 550, 600, 600, 500,
        700, 650, 400, 650, 650, 750, 550, 480, 700, 500, 520, 480, 550, 480,
        400, 500, 400, 480, 450, 600, 450, 550, 350, 90, 85, 127, 145,
        150, 150, 180, 125, 85, 120, 140, 143, 146, 108, 181, 85, 127, 169,
        85, 127, 169, 127
    ]
}


# --- Calculating the length of the data frame ---
len_make_model = len(ev_data['Make & Model'])
len_kwh = len(ev_data['kWh'])
len_range = len(ev_data['Claimed Range (km)'])

print("Length of Make & Model:", len_make_model)
print("Length of kWh:", len_kwh)
print("Length of Range:", len_range)

# --- Function to expand data ---
def expand_ev_data(df):
    new_data = []

    seasons = ['Summer', 'Monsoon', 'Winter', 'Spring']
    loads = ['Light', 'Heavy']
    battery_soc_values = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    terrains = ['City', 'Flat', 'Hilly']
    speed_modes = ['Normal', 'Eco', 'Power', 'Sports']  # Adjusted for broader applicability
    driving_styles = ['Normal', 'Aggressive', 'Eco']

    for index, row in df.iterrows():
        for season in seasons:
            for load in loads:
                for battery_soc in battery_soc_values:
                    for terrain in terrains:
                        for speed_mode in speed_modes:
                            for driving_style in driving_styles:

                                base_range = row['Claimed Range (km)']

                                # Apply adjustments based on factors
                                base_range = apply_adjustments(base_range, season, load, terrain, speed_mode,
                                                              driving_style)

                                # Battery SOC adjustment
                                actual_range = int(base_range * (battery_soc / 100))

                                new_data.append([
                                    row['Make & Model'], row['kWh'], row['Claimed Range (km)'],
                                    driving_style, season, load, battery_soc, terrain,
                                    speed_mode, actual_range
                                ])

    new_df = pd.DataFrame(new_data, columns=[
        'Make & Model', 'kWh', 'Claimed Range (km)', 'Driving Style', 'Season',
        'Vehicle Load', 'Battery SOC (%)', 'Terrain', 'Speed Mode', 'Actual Range (km)'
    ])

    return new_df

# --- Helper function to apply adjustments ---
def apply_adjustments(base_range, season, load, terrain, speed_mode, driving_style):
    # Season adjustment
    if season == 'Monsoon':
        base_range *= 0.90
    elif season == 'Winter':
        base_range *= 0.95
    elif season == 'Spring':
        base_range *= 0.98
    else:  # Summer
        base_range *= 0.92

    # Load adjustment
    if load == 'Heavy':
        base_range *= 0.95

    # Terrain adjustment
    if terrain == 'Hilly':
        base_range *= 0.80
    elif terrain == 'Flat':
        base_range *= 1.05

    # Speed mode adjustment
    if speed_mode == 'Eco':
        base_range *= 1.1
    elif speed_mode == 'Power':
        base_range *= 0.95
    elif speed_mode == 'Sports':
        base_range *= 0.80

    # Driving style adjustment
    if driving_style == 'Eco':
        base_range *= 1.05
    elif driving_style == 'Aggressive':
        base_range *= 0.90

    return base_range

# --- Create DataFrame (now only one) ---
df = pd.DataFrame(ev_data)

# --- Expand data  ---
expanded_df = expand_ev_data(df)

# --- Save to CSV ---
expanded_df.to_csv('indian_evs_data_expanded9.csv', index=False)

