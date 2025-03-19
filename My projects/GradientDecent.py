
#Gradient decent project (Line of the best fit)
#Students:
#1) Mohammed Ambusaidi

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np



data = [(2.9,4.0),(-1.5,-0.9)
        ,(0.1,0.0),(-1.0,-1.0),
        (2.1,3.0),(-4.0,-5.0),(-2.0,-3.5)
        ,(2.2,2.6),(0.2,1.0),(2.0,3.5)
        ,(1.5,1.0),(-2.5,-4.7)]


def lowest(m,b):
    def SSE_m(m,b):
        sum0 = 0
        for x,y in data:
            sum0 += (2*(y-(m*x+b))*(-x))
        return sum0
    def SSE_b(m,b):
        sum1 = 0
        for x,y in data:
            sum1 += (2*(y-(m*x+b))*(-1))
        return sum1
    def Gradient(m,b):
        xm = SSE_m(m,b)
        yb = SSE_b(m,b)
        return((-1*xm*0.001)+m,(-1*yb*0.001)+b)
    i,j = m,b
    while True:
        m,b = i,j
        i,j = Gradient(m,b)
        if abs(m-i) < 1e-9 and abs(b-j)<1e-9:
            break
    return (round(i,2),round(j,2))



M,B = lowest(-2,3)
#scatter visualization
x,y = zip(*data)
plt.scatter(x,y)

#line visualization
linex = range(-5,4)
liney = [M*x for x in linex]
plt.plot(linex, liney)
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('line of best fit (Gradient Decent Project)')
plt.show()
print(f"The Line of The Best Fit y = {M}x + {B}")


# Using scikit learning library to make sure everything is correct!.

def my_scikit_LR(data):
    x = np.array([x for x,y in data]).reshape(-1,1)
    y = np.array([y for x,y in data])
    model = LinearRegression()
    model.fit(x,y)
    m_hat = model.coef_[0]
    b_hat = model.intercept_
    return round(m_hat,2),round(b_hat,2)

print(lowest(-2,3))
print(my_scikit_LR(data))





