import pandas as pd
import sys

def bmi_calculation():
    df_weight_height_data = pd.read_json('data/weight_height_data.json', chunksize=1000)

    bmi_category = {
        'category': ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese', 'Severely obese', 'Very severely obese'],
        'min_bmi': [0, 18.5, 25, 30, 35, 40],
        'max_bmi': [18.4, 24.9, 29.9, 34.9, 39.9, 999],
        'health_risk': ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 'High risk', 'Very high risk']
    }

    df_bmi_category = pd.DataFrame(bmi_category)

    print(df_weight_height_data.to_string())
    print(df_bmi_category.to_string())
