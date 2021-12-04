import pandas as pd


def calculate_risk(val):
    if val < 18.4:
        return 'Malnutrition risk'
    elif 18.5 <= val <= 24.9:
        return 'Low risk'
    elif 25 <= val <= 29.9:
        return 'Low risk'
    elif 30 <= val <= 34.9:
        return 'Low risk'
    elif 35 <= val <= 39.9:
        return 'Low risk'
    else:
        return 'High Risk'


if __name__ == '__main__':
    df = pd.read_json('./patient_info.json')
    df['HeightMtr'] = df['HeightCm'].apply(float) / 100
    df['BMI'] = df['WeightKg'] / (df['HeightMtr'] ** 2)
    df['BMI'] = df['BMI'].apply(float)
    df['Health Risk'] = df['BMI'].apply(calculate_risk)
    print(df)
    df.to_csv('output_file.csv')
