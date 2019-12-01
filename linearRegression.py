import numpy as np 
import drawPlot as dp

def linearRegression(x, y): 
    
    avgX, avgY = np.mean(x), np.mean(y) 
    
    a = np.sum( y * (x - avgX) ) / np.sum((x - avgX) * (x - avgX)) 

    b = avgY - a * avgX 
  
    return(a, b)
   
def main(): 
    x = np.array([40,  43,  139, 182,  240]) 
    y = np.array([149, 157, 350, 367,  423]) 
  
    f = linearRegression(x, y) 
    print("f(x) = {}x  {}".format(f[0], f[1]))
    
    price = float(input("Price $: "))

    size = (price-f[1]) / f[0]
    print("Size {}".format(size))

    dp.drawPlot(x, y, f)

if __name__ == "__main__": 
    main()
