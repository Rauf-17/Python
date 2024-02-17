

# In[1]:#Function is python. 1, Default Function(), Parameterized Function= def function(x,y,z)
# def

def f():
    print("AIUB")
f()


# In[8]:


def g(name):
    print("Hi " + name)
g("AIUB")


# In[11]:


def N(Fname,Lname):
    print(Fname+ " "+ Lname)
N("Raufull","Islam")



# In[12]:


def func(*Name):
    print("My name is: "+ Name[2])
func("Rauf","X","Y","Z","A")


# In[15]:


def dp(country = "Bangladesh"):
    print("I'm From: " +country)
dp("India")
dp("Pakistan")
dp()
dp("SriLanka")
dp()


# In[18]:


def function(food):
    for i in food:
        print(i)
dish = ["Biriany","Kacchi","X"]
function(dish)


# In[19]:


# f(x)= 3*x**2+32

def f(x):
    return 3*x**2+32
y = f(2)
print(y)



# In[21]:


#Listed function
# f(x)= 3*x**2+32

def f(x):
    return 3*x**2+32
List1 = [2,3,4,5]
List2 = []

for i in range(len(List1)):
    List2.append(f(List1[i]))
print(List1)
print(List2)


# In[23]:


# List values sum

def sum1(List1):
    sum = 0
    for i in range(len(List1)):
        sum += List1[i]
    return sum
List1 = [10,20,30,40]
print(sum1(List1))


# In[25]:


# [10,20,30] = [20,40,60]

def doublevalue(L):
    List1 = []
    for i in range(len(L)):
        List1.append(L[i]*2)
    return List1
    
    
L = [10,20,30]
print(L)
print(doublevalue(L))


# In[29]:


#derivation

#f(x)= 3*x**2+32

def f(x):
    return 3*x**2+32
def derivative(x):
    return 6*x
x = [-1,0,1]
y = []
z = []

for i in range(len(x)):
    y.append(f(i))
    z.append(derivative(i))
print(x)
print(y)
print(z)


# In[32]:


# Distance between two vector
# distance = math.sqrt((x1-x2)^2 + (y1-y2)^2.......)

import math

def distance(u,v):
    dis = 0
    for i in range(len(u)):
        dis += (u[i]-v[i])**2
    return math.sqrt(dis)
u = [10,4,7]
v = [2,5,9]

print(distance(u,v))


# In[40]:


# range(starting value, range, increament)
# linspace

import math
def linspace(lower,upper,steps):
    L = []
    h = (upper-lower)/steps
    L.append(lower)
    
    for i in range(1,steps):
        L.append(L[i-1]+h)
    L.append(upper)
    return L
print(linspace(0,1,5))


# In[ ]:




