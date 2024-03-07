import panel as pn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pyscript import display

xdata = np.array( [2.1,2.7,2.8,3.2,3.2,4.5,4.6,7.2,8.3,8.9,10,11.5,11.7,12.8,13.8,14.6,14.9] )
ydata = np.array( [2.94,4.32,1.12,0.64,1.92,3.6,8.28,1.44,9.96,3.56,20,11.5,11.7,17.92,22.08,23.36,17.88] )

data = np.column_stack((xdata, ydata))
df = pd.DataFrame(data, columns = ['x','y'])

df_pane = pn.pane.DataFrame(df, width=400)

x = np.linspace(xdata.min()-2, xdata.max()+2, 20)
b = 0
m = 0
y = m*x + b

fig, ax = plt.subplots()
ax.scatter(xdata,ydata)
ax.plot(x,y,color='red')
plt.grid()
display(plt, target="graph-area", append=False)

sliderM = pn.widgets.FloatSlider(start=-5, end=5, value=0, name='m')
sliderB = pn.widgets.FloatSlider(start=-15, end=25, value=0, name='b')

def callbackM(m, b):
    y = m*x + b
    ax.clear()
    ax.scatter(xdata,ydata)
    ax.plot(x,y,color='red')
    plt.xlim(0, 16)
    plt.ylim(-5, 25)
    plt.grid()
    display(plt, target="graph-area", append=False)
    return f'y: {round(m,2)} x + {round(b,2)}'

def callbackB(m, b):
    y = m*x + b
    ax.clear()
    ax.scatter(xdata,ydata)
    ax.plot(x,y,color='red')
    plt.xlim(0, 16)
    plt.ylim(-5, 25)
    plt.grid()
    display(plt, target="graph-area", append=False)
    return f'y: {round(m,2)} x + {round(b,2)}'

binderM = pn.bind(callbackM, m=sliderM, b=sliderB)
pn.Row(sliderM, binderM).servable(target='simple_app');

binderB = pn.bind(callbackB, m=sliderM, b=sliderB)
pn.Row(sliderB, binderB).servable(target='simple_app');

dataTable = pn.widgets.Tabulator(df_pane, width=650)
pn.Row(dataTable).servable(target='simple_app');
