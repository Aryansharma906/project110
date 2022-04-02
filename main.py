from typing import Counter
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
import statistics
import random

df = pd.read_csv('medium_data.csv')
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)

 ## finding mean of 30 random data points
def sampleData_mean(counter):
     sample_dataset = []
     for i in range(0, counter):
          random_index = random.randint(0,len(data))
          value = data[random_index]
          sample_dataset.append(value)

     sample_mean = statistics.mean(sample_dataset)
     return sample_mean
     
def plot_graph(mean_list):
     df = mean_list
     mean = statistics.mean(df)
     fig = ff.create_distplot([df], ['reading time'], show_hist =False)
     fig.add_trace(go.Scatter(x =[mean,mean], y =[0,1], mode ='lines', name ='Mean'))
     fig.show()
     
def setup():
     mean_list =[]
     for i in range(0,100):
          set_of_means = sampleData_mean(30)
          mean_list.append(set_of_means)
     
     plot_graph(mean_list)
     mean = statistics.mean(mean_list)
     print("Mean of sampling distribution -: ", mean)

setup()

population_mean = statistics.mean(data)
print("mean of population data -: ", population_mean)
