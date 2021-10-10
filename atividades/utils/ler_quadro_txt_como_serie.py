import pandas

def ler_quadro_txt_como_serie(nome_arquivo: str):
    data_frame = pandas.read_csv(nome_arquivo, sep='\s+', header=None, decimal=",")
    return pandas.Series([valor for linha in data_frame.values for valor in linha])