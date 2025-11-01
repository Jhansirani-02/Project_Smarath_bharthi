import pandas as pd

def load_local_data():
    rainfall = pd.read_csv('rainfall.csv')
    crops = pd.read_csv('crops.csv')
    # basic type cast
    rainfall['Year'] = rainfall['Year'].astype(int)
    crops['Year'] = crops['Year'].astype(int)
    return rainfall, crops
