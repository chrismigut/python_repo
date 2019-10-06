#Finding the most common elements (mode)

from collections import Counter

elements = [4,2,1,3,2,4,5,2]
c = Counter(elements)

#Return the 2 most common elements
print(c.most_common(2))