
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler



def clean_data(num_fts, data):
    num_fts = data[['BMI', 'Glucose', 'BloodPressure', 'Insulin']]
    data = data.drop(['SkinThickness','BMI', 'Glucose', 'BloodPressure', 'Insulin'], axis=1)
    num_fts = num_fts.astype('float64')
    missing_vals = [0] 
    cleaned_ft = num_fts.replace(missing_vals, np.NaN)
    
    # we could've also used an imputer instead of doing so manually
    for feature in cleaned_ft:
        m = round(cleaned_ft[feature].median(), 2)
        cleaned_ft[feature] = cleaned_ft[feature].fillna(m)
    cleaned_df = pd.concat([data, cleaned_ft], axis=1)
    
    return cleaned_df


def scale_data(cleaned_df):
    scaler = StandardScaler()
    scaler.fit(cleaned_df.drop('Outcome',axis=1))
    scaled_feats = scaler.transform(cleaned_df.drop('Outcome', axis=1))
    scaled_df = pd.DataFrame(scaled_feats)
    
    return scaled_df
