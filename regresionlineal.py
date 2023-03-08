import numpy as np
import pandas as pd
import asyncio
from matplotlib import pyplot as plt
from pyodide.http import open_url
      
from js import document, FileReader
from pyodide import create_proxy

df = pd.DataFrame(columns=['X','Y'])

async def process_file(event):
    fileList = event.target.files.to_py()
    i = 0
    for f in fileList:
        data = await f.text()
        dat = str(data).split("\r\n")
        
        for item in dat:
            s = item.split(',')
            if len(s) == 2:
                new_row = [ s[0], s[1] ]
                df.loc[len(df)] = new_row

    processData()
    return

def main():
    file_event = create_proxy(process_file)
    e = document.getElementById("myfile")
    e.addEventListener("change", file_event, False)
    return

def processData():
    xl = df.iloc[:,0].tolist()
    yl = df.iloc[:,1].tolist()

    x = np.array(xl).astype(np.single)
    y = np.array(yl).astype(np.single)      
    xm = x.mean()
    ym = y.mean()

    m = sum( (x - xm) * (y - ym) ) / sum((x - xm)**2)
    b = ym - m*xm

    xlinea = np.linspace(x.min(), x.max(), 30)
    ylinea = m*xlinea + b
    ley = "y = " + str(m) + "x + " + str(b)
    #print(ley)
    plt.figure(figsize=(6,6))
    plt.title(label="Regresión Lineal. García Bautista Jorge Armando", fontsize=12 )
    plt.scatter(x,y, label = "Datos")
    plt.plot(xlinea, ylinea, label = ley, color = 'salmon')
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("Y")
    #document.getElementById("content").deleteRow(0);
    #document.getElementById("graph-area").deleteRow(0);
    element = document.getElementById("content")
    for xdat,ydat in zip(x,y):
    	element.append( create_html_element(xdat,ydat) )
    #display(df, target="content", append=True)
    display(plt, target="graph-area", append=True)
    return
 
def create_html_element(xd,yd):
    tr_element = document.createElement('tr')
    first_name_element = document.createElement('td')
    last_name_element = document.createElement('td')
    first_name_element.innerText = xd
    last_name_element.innerText = yd
    tr_element.append(first_name_element)
    tr_element.append(last_name_element)
    return tr_element

main()
