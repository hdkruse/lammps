from numpy import *
import matplotlib.pyplot as plt

with open("calc0085","r") as ifile:
    print(ifile.readline())
    i=0
    data=ifile.readlines
    print(data) 
    area=[]
    step=[]
    for line in ifile:
       words=line.split()
       area.append(words[0])
       step.append(words[1])
       i+=1



plt.plot(array(step),array(area))
plt.show()

    
