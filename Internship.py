import time
#To print a fibonacci series using a optimised algorithm.
def series(n): #Defining a function series
    if n > 0: #Using the if-else condition.
        a = 0 #Given
        b = 1 #Given
        for i in range(1, n + 1):
            c = a + b
            a = b
            b = c
        print(c)
        
    else:
        return n

srs = series(6) #Catching the value of the function in the variable, used 6 just to check how the output runs.
print(series) 

#To test the following cases in the optimised algorithm. I have used an Iterative method for the same for quick results.
list1 = [0,1,2,3,10,100,1000,10000]
for n in list1:
    start_time = time.time()
    srs = series(n)
    end_time = time.time()
    x = start_time - end_time
    pprint(srs,"\nExecution Time: ",x )


#To print the fibonacci series using a recursive approach.
list_val = []

def series(n): #Defining a function
    if n == 0 or n ==1 :
        if n == 1:
            series(n-1)
        list_val.append(n)
        
    else:
        series(n - 1)
        list_val.append(list_val[-1] + list_val[-2])
        
#To test the following cases using the recursive algorithm.
n = [0,1,2,3,10,100,1000,10000]
for i in n:
    start_time = time.time()
    list_val = []
    series(i)
    end_time = time.time()
    x = start_time - end_time
    print(list_val,"\nExecution Time: ",x )

series(n)
print(list_val)
