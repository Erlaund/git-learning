#!/usr/bin/env python
# coding: utf-8

# In[15]:


from itertools import *
import math

# подстановка значений в формулу
def length_counter(a,b):
    length = ((b[0]-a[0])**2 + (b[1]-a[1])**2) **0.5
    return length

def point_finder(x):
    b = (2,5)
    c = (5,2)
    d = (6,6)
    e = (8,3)
    
    if x == 'b':
        point = b
    elif x == 'c':
        point = c
    elif x == 'd':
        point = d
    elif x == 'e':
        point = e
        
    return point

def way_counter(massive):
    a = (0,2)
    points_massive = []
    
    for i in massive:
        i = [point_finder(i)]
        points_massive.extend(i)
        
    w1 = length_counter(a, points_massive[0])
    w2 = length_counter(points_massive[0], points_massive[1])
    w3 = length_counter(points_massive[1], points_massive[2])
    w4 = length_counter(points_massive[2], points_massive[3])
    w5 = length_counter(points_massive[3], a)
    
 
    
    full_way = w1 + w2 + w3 + w4 + w5
    
    return full_way, w1, w2, w3, w4, w5, massive

    
massive = []
way_values = []
a = (0,2)

for i in permutations('bcde'):
    i = [i]
    #print(i)
    massive.extend(i)

for i in massive:
    way, w1, w2, w3, w4, w5, point_way = way_counter(i)    
    #print(way)
    way_values.append(way)

min_way = min(way_values)
answer_index = way_values.index(min_way)

way, w1, w2, w3, w4, w5, point_way = way_counter(massive[answer_index])


print()
print()

#print(f"Последовательность: a -> {point_way[0]} -> {point_way[1]} -> {point_way[2]} -> {point_way[3]} -> a  ")
#print(f"Путь из a -> {point_way[0]} равен: {w1}")
#print(f"Путь из {point_way[0]} -> {point_way[1]} равен: {w2}")
#print(f"Путь из {point_way[1]} -> {point_way[2]} равен: {w3}")
#print(f"Путь из {point_way[2]} -> {point_way[3]} равен: {w4}")
#print(f"Путь из {point_way[3]} -> a равен: {w5}")
#print(f"По итогу обход всех точек равен: {way}")


print(f"Последовательность: a -> {point_way[0]} [{w1}] -> {point_way[1]}[{w2 + w1}] -> {point_way[2]}[{w3 + w2 + w1}] -> {point_way[3]}[{w4 + w3 + w2 + w1}] -> a [{w5 + w4 + w3 + w2 + w1}] = {way}  ")


# In[ ]:





# In[ ]:




