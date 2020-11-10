import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    excel_name = 'textmining.xlsx'
    df = pd.read_excel(excel_name)
    print(df)

    df
    df.std()
    df.head()
    df.tail()
    df.describe()
    df['Clothing ID']
    df.groupby('Clothing ID')['Age'].mean()
    df.groupby('Clothing ID')['Age'].max()
    min_age = df['Age'].min()
    max_age = df['Age'].max()
    df.groupby('Clothing ID')['Age'].std()
    df.groupby('Clothing ID')['Rating'].mean()
    df.groupby('Clothing ID')['Rating'].std()
    df['Clothing ID'].unique()
    pd.unique(df['Clothing ID']).tolist()
    x = df['Clothing ID']
    y = df['Age']

    plt.plot(x, y, 'bo')
    plt.title('Età per prodotto')
    plt.xlabel('IdProdotto')
    plt.ylabel('Età')

    plt.show()

    df.groupby('Clothing ID')['Rating'].std()

    df['Age'].plot(kind='hist', color='teal')
