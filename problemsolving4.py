# 1. Multiplication tables from 1 to 10 using nested loops

for i in range(1, 11):          # Outer loop for numbers 1 to 10
    print(f"\nTable of {i}:")
    
    for j in range(1, 11):      # Inner loop for multiples 1 to 10
        print(f"{i} x {j} = {i * j}")
        
'''Output:
Table of 10:
10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
10 x 4 = 40
10 x 5 = 50
10 x 6 = 60
10 x 7 = 70
10 x 8 = 80
10 x 9 = 90
10 x 10 = 100'''

# 2.  Adding two 2D lists (matrices) using nested loops

# Matrix A
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matrix B
B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Result matrix (initialize with zeros)
result = []

# Nested loops for matrix addition
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

# Display result
print("Resultant Matrix:")
for r in result:
    print(r)

'''Output:
Resultant Matrix:
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]'''

# 3. Counting even and odd numbers in a nested list

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

even_count = 0
odd_count = 0

# Nested loops to traverse the list
for i in nested_list:
    for j in i:
        if j % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

# Display results
print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)

'''Output:
Even numbers count: 5
Odd numbers count: 4'''

# 4. Print prime numbers between 2 and 50 using nested loops

for num in range(2, 51):   # Numbers from 2 to 50
    is_prime = True
    
    for i in range(2, num):   # Check divisibility
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
'''Output:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 '''

# 5. Transpose of a 2D matrix using nested loops

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Initialize transpose matrix with zeros
rows = len(matrix)
cols = len(matrix[0])

transpose = []

for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)

# Display result
print("Transpose Matrix:")
for r in transpose:
    print(r)
    
'''Output:
Transpose Matrix:
[1, 4]
[2, 5]
[3, 6]'''

# 6. Display unique pair combinations

lst = [1, 2, 3, 4]

# Nested loops for unique pairs
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        print(f"({lst[i]}, {lst[j]})")
        
'''Output:
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)'''

# 7. Find common characters between two strings

str1 = "hello"
str2 = "world"

common_chars = []

# Nested loops to compare characters
for i in str1:
    for j in str2:
        if i == j and i not in common_chars:
            common_chars.append(i)

# Display result
print("Common characters:", common_chars)

'''Output:
Common characters: ['o', 'l']'''

# 8. Count vowels in each word from a list

words = ["hello", "world", "python", "programming"]

vowels = "aeiouAEIOU"

# Loop through each word
for word in words:
    count = 0
    
    # Loop through each character in the word
    for ch in word:
        if ch in vowels:
            count += 1
    
    print(f"{word} -> {count} vowels")
    
'''Output: 
hello -> 2 vowels
world -> 1 vowels
python -> 1 vowels
programming -> 3 vowels'''

# 9. Find common elements between two lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = []

# Nested loops to compare elements
for i in list1:
    for j in list2:
        if i == j and i not in common_elements:
            common_elements.append(i)

# Display result
print("Common elements:", common_elements)

'''Output:
Common elements: [3, 4, 5]'''

# 10. Sum of elements in each row of a 2D list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Loop through each row
for i in range(len(matrix)):
    row_sum = 0
    
    # Loop through each element in the row
    for j in range(len(matrix[i])):
        row_sum += matrix[i][j]
    
    print(f"Sum of row {i+1}: {row_sum}")
    
'''Output:
Sum of row 1: 6
Sum of row 2: 15
Sum of row 3: 24
'''
