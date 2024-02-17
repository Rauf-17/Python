
# In[3]:


age = int(input("Please Enter age: "))
print(age)

if(age >= 18):
    print("Adult")
    print("Aged")
else:
    print("Underaged")


# In[7]:


#AIUB Grading System

marks = int(input("Please Enter Your Marks: "))

if(marks>= 90):
    print("A+")
elif(marks>=85 and marks<= 89):
    print("A")
elif(marks>=80 and marks<= 84):
    print("B+")
elif(marks>=75 and marks<= 79):
    print("B")
elif(marks>=70 and marks<= 74):
    print("C+")
elif(marks>=65 and marks<= 69):
    print("C")
elif(marks>=60 and marks<= 64):
    print("D+")
elif(marks>=50 and marks<= 59):
    print("D")
else:
    print("F")


# In[ ]:


#Loops(for, while, do while,do etc)
# break("to have lessTime Complexity") 1,2,3 
# continue()
#range(Starting Value,Range,Increament)


# In[19]:


for i in range(5,12,3):
    print(i, end = " ")


# In[23]:


i = 2
while i<12:
    print(i)
    i = i + 4


# In[26]:


for i in range(1,11):
    print(str(i)+ " Happy Rose Day")


# In[33]:


#break(Stops when condition matches)

for i in range(1,11):
    if(i==5):
        break
    print(i,end=" ")
        
    


# In[32]:


#continue(continue when condtion is matched and skip it)


for i in range(1,11):
    if(i==5):
        continue
    print(i,end=" ")


# In[47]:


#List(Mutable)
List1 = []
List1.append(10)
List1.append(30)
List1.append(20)
List1.append(40)

print(List1)





# In[48]:


#Tuple(Unmutable)
t1 = (10,20,30)
print(t1)
t1.count(10)


# In[55]:


#set{}

s = {10,20,30}

s.add(40)
s.pop()
print(s)


# In[58]:


#map

m ={1: "Rauf", 2: "21-45779-3", 3: "CS", 4: 5, 5: 5.6}
print(m)


# In[59]:


for i in m:
    print(i,m[i])


# In[ ]:


# Break until 12:30

