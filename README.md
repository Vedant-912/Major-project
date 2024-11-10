# Major-project
# Electric Vehicle (EV) Range Prediction using Machine Learning

This project addresses one of the key challenges in electric vehicle (EV) adoption — range anxiety. By leveraging machine learning techniques, this project aims to predict the range of EVs based on various factors like battery capacity, driving style, terrain, and weather conditions.

## Table of Contents
- [Background](#background)
- [Project Goals](#project-goals)
- [Data Sources](#data-sources)
- [Models Implemented](#models-implemented)
- [Evaluation Metrics](#evaluation-metrics)
- [Results](#results)
- [Future Work](#future-work)
- [Setup and Usage](#setup-and-usage)

## Background
As EVs gain popularity due to environmental concerns, accurately predicting their driving range is crucial for user confidence and planning. This project explores machine learning methods to provide dependable range estimates, potentially enhancing EV usability and reducing range anxiety.

## Project Goals
The main objectives are:
1. Develop and test machine learning models to predict EV range under various conditions.
2. Compare model performances to identify the most accurate and reliable approach.
3. Offer insights into how factors like driving behavior, SOC (State of Charge), and battery health impact range.

## Data Sources
The project utilizes a comprehensive dataset containing both real-world and simulated data. Key sources include:
- Public EV performance datasets
- Simulated data reflecting diverse driving scenarios
- Real-world data where available

The dataset includes features such as battery capacity, driving style, terrain, weather conditions, SOC, and actual range.

## Models Implemented
Three machine learning models were implemented for range prediction:
- **Linear Regression**: Establishes a baseline and captures linear relationships.
- **Support Vector Regression (SVR)**: Effective in high-dimensional spaces, modeling complex relationships.
- **Random Forest Regression**: An ensemble method capturing non-linear patterns, known for robustness.

## Evaluation Metrics
Mean Absolute Error (MAE) was selected as the primary evaluation metric, as it provides an interpretable error value in distance units, which aligns with user expectations for range accuracy.

## Results
The Random Forest Regression model achieved the best performance with the lowest MAE, making it the preferred model for EV range prediction:
- **Linear Regression**: MAE = 20 km
- **SVR**: MAE = 15 km
- **Random Forest Regression**: MAE = 5 km

## Future Work
- **Enhanced Feature Set**: Include additional variables like real-time traffic and battery degradation.
- **Data Quality Improvement**: Gather more diverse and high-quality EV data.
- **Additional Model Exploration**: Explore advanced models like deep learning and gradient boosting.
- **User Interface**: Develop a user-friendly interface for drivers to input conditions and receive accurate range predictions.

## Setup and Usage

### Requirements
- Python 3.x
- Pandas
- NumPy
- Scikit-learn

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ev-range-prediction.git
    cd ev-range-prediction
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. Prepare the dataset (`ev_range_data.csv`) with features like battery capacity, driving style, terrain, and SOC.
2. Run the main script to train and test models:
    ```bash
    python main.py
    ```

### Example Code
An example of the model training and evaluation is available in `example.py`.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- Contributors and dataset providers
- Research and public datasets on EV performance

---

By providing reliable EV range estimates, this project aims to support broader EV adoption by enhancing driver confidence and journey planning.
