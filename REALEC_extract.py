import pandas as pd
from pathlib import Path
import zipfile

# text = '/home/daria/Downloads/REALEC_texts.zip'
# preds = '/home/daria/Downloads/REALEC_predictions.csv'

# insert your path to the files


with zipfile.ZipFile(text) as file:
  file.extractall('files')


files = list(Path('files').iterdir())


def read_text(path):
    with open(path) as file:
        txt = file.readlines()
    return txt, path.name


txt = {name: ' '.join(txt) for txt, name in map(read_text, files)}


levels = pd.read_csv(preds, index_col=0)

# query('CEFR=="A2-B1").text.iloc[any number]
# query('CEFR=="B1-B2").text.iloc[any number]
# query('CEFR=="B2-C1").text.iloc[any number]

levels.assign(text=pd.DataFrame(txt.values(), index=txt.keys()))[['CEFR', 'text']].query('CEFR=="B2-C1"').text.iloc[0]

