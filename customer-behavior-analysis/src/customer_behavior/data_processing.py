def load_data(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Remove duplicates
    data = data.drop_duplicates()
    # Fill missing values
    data = data.fillna(method='ffill')
    return data

def preprocess_data(file_path):
    data = load_data(file_path)
    cleaned_data = clean_data(data)
    return cleaned_data