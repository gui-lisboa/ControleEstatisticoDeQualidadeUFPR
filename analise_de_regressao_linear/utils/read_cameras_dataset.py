import pandas
import warnings

def read_cameras_dataset():
    warnings.filterwarnings('ignore')
    colunas_data = ['last_update', 'release_date', 'release_month']
    dataset = pandas.read_table("http://leg.ufpr.br/~walmes/data/digital-cameras.txt", comment="#", parse_dates=colunas_data)
    dataset = dataset.convert_dtypes()
    return dataset