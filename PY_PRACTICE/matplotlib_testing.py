import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,160])
ypoints = np.array([0,200])

plt.plot(xpoints,ypoints)
plt.title("MATPLOTLIB GRAPH TESTING CREATED BY SOUMOBRATA MANNA")
plt.show()

xpoints = np.array([1,8,3,2,6,10,12,4,2])
plt.plot(xpoints, 'o:r')
plt.plot(xpoints, marker='p', ms=20, mec='b', mfc='g')
plt.title("MATPLOTLIB GRAPH TESTING  CREATED BY SOUMOBRATA MANNA")
plt.show()

xpoints = np.array([1,4,8,2])
ypoints = np.array([2,3,5,6])
plt.plot(xpoints,ypoints, linestyle='dotted', color = 'r')
plt.title("MATPLOTLIB GRAPH TESTING CREATED BY SOUMOBRATA MANNA")
plt.grid(axis='x')
plt.show()

xpoints = np.array([1,4,8,2])
ypoints = np.array([2,3,5,6])
plt.plot(xpoints ,linestyle='dotted', color = 'r')
plt.plot(ypoints,linestyle='dashed', color = 'g',linewidth=3)
# plt.figure(figsize=(3, 3))

font_1 = {'family':'serif','color':'red','size':20}
font_2 = {'family':'serif','color':'blue','size':20}


plt.title("MATPLOTLIB GRAPH TESTING CREATED BY SOUMOBRATA MANNA")
plt.xlabel("X-AXIS",fontdict=font_1)
plt.ylabel("Y-AXIS",fontdict=font_2)
plt.grid(color='green')
plt.show()

#BAR GRAPH
plt.title("MATPLOTLIB BAR GRAPH TESTING CREATED BY SOUMOBRATA MANNA")
x = np.array(["A","B","C","D","E"])
y = np.array([10,20,30,40,50])

plt.bar(x,y, color = "green")
plt.show()

#HISTOGRAM
plt.title("MATPLOTLIB HISTOGRAM GRAPH TESTING CREATED BY SOUMOBRATA MANNA")
x = np.random.normal([200,50,120,60])
plt.hist(x)
plt.show()

#PIECHARTS
x = np.array([12,22,45+10+5+6])
comp = ["Maruti", "Huyndai","Mercedes","VW","Mahindra","BMW"]

plt.pie(x, labels = comp)
plt.legend(title=" COMAPNIES ")
plt.show()