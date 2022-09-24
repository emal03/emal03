#Machie learning is subset of Artificial intellgence mainly they focus on the designing of system 

#Mean : Average value are called mean 
#Median : the mid pont value or intermadete number
#Mode : the most common value 


#mean 
#median 
#mode 

# pip install numpy 
# pip install scipy 
#conda install numpy
# conda install scipy


# first we have to declare number that you want to find the mean
value = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# To calculate the mean, find the sum of all values, and divide the sum by the number of values
# value = (99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77
import numpy as np

value = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print("mean is ",np.mean(value))#Use the NumPy mean() method to find the average  or mean value 

#finding the Median value or number 
#The median value is the value in the middle, after you have sorted all the values:
#77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111  Meadian  is ? 
import numpy as np

value = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print("Median number is value is ",np.median(value))
#It is important that the numbers are sorted before you can find the median.
#If there are two numbers in the middle, divide the sum of those numbers by two.
#77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103
#(86 + 87) / 2 = 86.5 Example
import numpy

value = [99,86,87,88,86,103,87,94,78,77,85,86]

x = numpy.median(value)
print("the median of two number is ",x)

#Mode : The Mode value is the value that appears the most number of times:
#99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86 like 86 coming two time 

from scipy import stats

value = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(value)


print(x)
