import numpy as np
import matplotlib.pyplot as plt

data = [(2.9,4.0),(-1.5,-0.9), (0.1,0.0),(-1.0,-1.0), (2.1,3.0),(-4.0,-5.0),
        (-2.0,-3.5), (2.2,2.6), (0.2,1.0), (2.0,3.5), (1.5,1.0), (-2.5,-4.7)]


def matrix(data):
    y = [y for x,y in data]
    x = [x for x,y in data]
    x_matrix = np.array([[1, xi] for xi in x]) #X
    x_trans = x_matrix.T                       #XT
    x_mul = x_trans @ x_matrix                 #(XT*X)
    x_inv = np.linalg.inv(x_mul)               #(XT*X)^-1
    y_matrix = np.array(y).reshape(-1, 1)      #(Y)
    y_mul = x_trans @ y_matrix                 #(XT*Y)
    ans = x_inv @ y_mul                        #(XT*X)^-1 * (XT*Y)

                                               #[[b0]
    return ans                                 # [b1]]


def bestfit(data):

    n = len(data)
    sum_x = sum([x for x,y in data])       
    sum_y = sum([y for x,y in data])           
    sum_xy = sum([x*y for x,y in data])        
    sum_x2 = sum([x**2 for x,y in data])       
    avx = sum_x/n
    avy = sum_y/n


    b1 = (sum_xy-(avy*sum_x)-avx*sum_y+(n*avx*avy))/(sum_x2-(2*avx*sum_x)+(n*(avx**2)))
    b0 = avy-b1*avx


    return(round(b1,2),round(b0,2))

    
print(matrix(data))
print(bestfit(data))

b1,b0 = bestfit(data)
#scatter visualization
x,y = zip(*data)
plt.scatter(x,y)

#line visualization
linex = range(-5,4)
liney = [b1*x for x in linex]
plt.plot(linex, liney)
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('line of best fit (matrix Project)')
plt.show()
print(f"The Line of The Best Fit y = {b1}x{b0}")
