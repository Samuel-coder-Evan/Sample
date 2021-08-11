import pandas as pd
import statistics
import csv
import random
from pandas.io.stata import StataReader
import plotly.figure_factory as ff
df = pd.read_csv('distribution.csv')
data = df['reading_time'].tolist()
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
print(mean,median,mode)
def randomset(count):
    dataset = []
    for i in range(0,100):
        index = random.randint(0,len(data) - 1)
        value = data[index]
        dataset.append(value)
    mean1 = statistics.mean(dataset)
    return mean1
def showfig(meanlist):
    fig = ff.create_distplot([meanlist],['avg'],show_hist=False)
    fig.show()
def setup():
    meanlist = []
    for i in range(0,1000):
        means = randomset(100)
        meanlist.append(means)
    showfig(meanlist)
    mean = statistics.mean(meanlist)
    median = statistics.median(meanlist)
    mode = statistics.mode(meanlist)
    print(mean,median,mode)
setup()