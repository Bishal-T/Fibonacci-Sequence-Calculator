#Worked with Alex, Submehs, Emre, Melvin 

from random import *
import time 

first_term = 0
second_term = 1
nth_term = randint(15,35)

count = 0

start_time = time.time()

while count <= nth_term:

    next_term = first_term + second_term
    first_term = second_term 
    second_term = next_term
    count += 1


end_time = time.time()

total_time = (end_time - start_time) 

print(f'fib({nth_term})= {first_term}')

print(f'fib({nth_term}) took {total_time} seconds')

