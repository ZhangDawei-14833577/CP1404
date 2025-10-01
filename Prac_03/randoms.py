import random

print(random.randint(5, 20))  # line 1
# In lin 1, I see any integer between 5 and 20. The smallest number I can see is 5 and the largest is 20.
print(random.randrange(3, 10, 2))  # line 2
#On the second row, I can see a number from 3, 5, 7, or 9. The maximum number I can get is 9,
# and the minimum is 3. I can't get 4 because the numbers start at 3 and the step size is 2.
print(random.uniform(2.5, 5.5))  # line 3
#In the third row you can see random floating point numbers between 2.5 and 5.5.
# The maximum value is 5.5 and the minimum is 2.5.

random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)



