import pandas as pd
import matplotlib.pyplot as plt

def visualization(path):
    try:
        df = pd.read_csv(path, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding='latin1')

    print("Dataset Statistics:")
    print(df.describe())

    cols = df.columns
    
        # Bar Chart with Matplotlib
    plt.figure(figsize=(10, 6))
    for color_value, group_df in df.groupby(cols[2]):
        plt.bar(group_df[cols[0]], group_df[cols[1]], label=color_value, alpha=0.7)
    plt.title('Bar Chart')
    plt.xlabel(cols[0])
    plt.ylabel(cols[1])
    plt.legend(title=cols[2])
    plt.show()

    # Scatter Plot with Matplotlib
    plt.figure(figsize=(10, 6))
    plt.scatter(df[cols[0]], df[cols[1]], c=df[cols[2]], cmap='Set1')
    plt.title('Scatter Plot')
    plt.xlabel(cols[0])
    plt.ylabel(cols[1])
    plt.colorbar(label=cols[2])
    plt.show()

    # Line Chart with Matplotlib
    plt.figure(figsize=(10, 6))
    for color_value, group_df in df.groupby(cols[2]):
        plt.plot(group_df[cols[0]], group_df[cols[1]], label=color_value)
    plt.title('Line Chart')
    plt.xlabel(cols[0])
    plt.ylabel(cols[1])
    plt.legend(title=cols[2])
    plt.show()

if __name__ == "__main__":
    path = r'D:\\Programs\\Python\\Cognifyz\Book1.csv'
    visualization(path)
