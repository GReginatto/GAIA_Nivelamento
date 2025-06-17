import pandas as pd
import math
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
import tensorflow_decision_forests as tfdf
from google.colab import drive
drive.mount('/content/drive', force_remount=True)



caminho = 'caminho pro arquivo'

df = pd.read_csv(caminho)

df.head()
colunas_numericas = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
colunas_categoricas = df.select_dtypes(include=['object', 'category', 'string']).columns.tolist()





