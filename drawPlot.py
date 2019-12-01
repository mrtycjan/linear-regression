import matplotlib.pyplot as plt

def drawPlot(x, y, f): 
    plt.style.use('dark_background')
    plt.scatter(x, y, color = "m",marker = "o", s = 30)
    
    linearFunction = f[0]*x + f[1]
    
    plt.plot(x, linearFunction, color = "g")
    
    plt.xlabel('Size') 
    plt.ylabel('Price') 
  
    plt.show()