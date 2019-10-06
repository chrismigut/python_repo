donations = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200] 

 #find the range
def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest - lowest

    return lowest, highest, r

def print_range(numbers):
    lowest, highes, r = find_range(numbers)
    print('Lowest: {0} Highest: {1} Range: {2}'.format(lowest, highes, r))

#finding variance, low = values are clustered closer to the mean
"""
variance = sum(x(i) - x(mean))^2 / n
"""
def fine_mean(numbers):
    s = sum(numbers)
    n = len(numbers)
    mean = s / n
    print('mean: {0}'.format(mean))
    return mean

def find_difference(a, b):
    return a - b

def find_variance(numbers):
    mean = fine_mean(numbers)

    diff = []
    for num in numbers:
        diff.append(find_difference(num, mean)**2)
    
    n = len(numbers)
    v = sum(diff) /n
    
    return v

#finding SD, 
"""
    Sq.root the variance : 2-3 SD away from mean are viewed as outliers
"""
def find_SD(numbers):
   return find_variance(numbers)**0.5


if __name__ == '__main__':
    print_range(donations)
    print(find_variance(donations))
    print(find_SD(donations))