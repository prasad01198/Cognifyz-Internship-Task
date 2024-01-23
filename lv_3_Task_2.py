import pandas as pd
import plotly.express as px

def visualization(dataset):
    # Handling exception for reading a file efficiently
    try:
        df = pd.read_csv(dataset, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(dataset, encoding='latin1')

    # checking statistics report for dataset
    print("Dataset Statistics:")
    print(df.describe())

    # Reading no of columns
    cols = df.columns

    # Plotting bar chart
    barChart = px.bar(df, x=cols[0], y=cols[1], color=cols[2],
                       barmode='group', title='Bar Chart',
                       color_discrete_sequence=px.colors.qualitative.Plotly)
    barChart.show()
    
    # plotting scatter chart
    scatterPlot = px.scatter(df, x=cols[0], y=cols[1], color=cols[2],
                              title='Scatter Plot',
                              color_discrete_sequence=px.colors.qualitative.Set1)
    scatterPlot.show()

    # plotting line chart
    lineChart = px.line(df, x=cols[0], y=cols[1],
                         color=cols[2], line_group=cols[2],
                         title='Line Chart',
                         color_discrete_sequence=px.colors.qualitative.Plotly)
    lineChart.show()

if __name__ == "__main__":
    
    # defining dataset of the dataset
    dataset = r'D:\\Programs\\Python\\Cognifyz\Book1.csv'
    
    # calling a function
    visualization(dataset)