import pandas as pd
import matplotlib.pyplot as plt


def get_data_set():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    df = pd.read_csv(url, header=None)
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    return df

def store_scatter_plot(df):
    for species in df['species'].unique():
        species_df = df[df['species'] == species]
    plt.scatter(species_df['sepal_length'], species_df['sepal_width'], label=species)
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.title('Iris Dataset: Sepal Length vs Sepal Width')
    plt.legend()
    plt.savefig('exec/scatter_plot.png')

if __name__ == '__main__':
    df = get_data_set()
    store_scatter_plot(df)