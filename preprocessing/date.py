import pandas as pd

def extract_first_active_year(month: str) -> int:
    return int(str(month)[:4])

def extract_first_active_month(month: str) -> int:
    return int(str(month)[2:])

def create_date_features(data: pd.DataFrame) -> pd.DataFrame:
    data['first_active_year'] = data['first_active_month'].apply(extract_first_active_year)
    data['first_active_month'] = data['first_active_month'].apply(extract_first_active_month)
    return data