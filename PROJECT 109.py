from numpy.lib.function_base import median
import plotly.graph_objects as go
import statistics
import random 
import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("PROJECT 109.csv")
data = df["reading score"].tolist()
mean=sum(data)/len(data)
std_deviation=statistics.stdev(data)
median=statistics.median(data)
mode=statistics.mode(data)                                                                    
first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
fig=ff.create_distplot([data],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.70],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.70],mode="lines",name="STANDERD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.70],mode="lines",name="STANDERD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.70],mode="lines",name="STANDERD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.70],mode="lines",name="STANDERD DEVIATION 2"))

fig.show()
thin_1_std_deviation=[result for result in data if result > first_std_deviation_start and result<first_std_deviation_end]
thin_2_std_deviation=[result for result in data if result > second_std_deviation_start and result<second_std_deviation_end]
thin_3_std_deviation=[result for result in data if result > third_std_deviation_start and result<third_std_deviation_end]
print("mean {}".format(mean))
print("median {}".format(median))
print("mode {}".format(mode))
print("standard deviation{}".format(std_deviation))
print("{}% first standard deviation".format(len(thin_1_std_deviation)*100/len(data)))
print("{}% second standard deviation".format(len(thin_2_std_deviation)*100/len(data)))
print("{}% third standard deviation".format(len(thin_3_std_deviation)*100/len(data)))




