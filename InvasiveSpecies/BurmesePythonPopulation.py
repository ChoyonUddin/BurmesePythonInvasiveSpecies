import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn as scy

df = pd.read_csv("FL Specimen Management Database Pre-2022PYMO.csv")

years = df['Year'].value_counts().sort_index()
y = years.values
x = years.index


plt.figure(figsize=(10, 6))

#Line Graph
plt.plot(x, y, marker=',', linestyle='solid',markersize =7)
plt.xticks(x, rotation=45)
plt.xlabel('Year')
plt.ylabel('Sightings')
plt.title('Number of Burmese Pythons Documented Each Year')
plt.savefig('Python_Population_Line_Graph.jpeg')

#Bar Graph
plt.bar(years.index, years.values)
plt.xticks(x, rotation=45)
plt.xlabel('Year')
plt.ylabel('Sightings')
plt.title('Number of Burmese Pythons Documented Each Year')
plt.savefig("Python_Population_Bar_Graph.jpeg")