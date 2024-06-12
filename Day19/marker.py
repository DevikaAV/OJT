import matplotlib.pyplot as plt
# dataset
x=[1,2,3,4,5]
y=[2,3,6,7,10]

# create a plot with marker
plt.plot(x,y,marker='*',linestyle='-.',color='b',markersize=6,markerfacecolor='r')

# add the label as wel as title 
plt.title("the line plot with markers")
plt.xlabel('x-axis')
plt.xlabel('y-axis')
plt.show()