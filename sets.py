'''Set
Set.add(ele)
Set.discard(ele)
Len
Max
Min
Sorted
Sum
Union() ex. A.Union(B) or A|B
Intersection A&B
Difference A-B
Difference A^B
Clear
Copy
Isdisjoint
Pop'''
# Creating sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Adding elements
A.add(9)
print("After adding 9 to A:", A)

# Discarding elements
A.discard(2)
print("After discarding 2 from A:", A)

# Getting length
print("Length of A:", len(A))

# Getting maximum and minimum
print("Maximum in A:", max(A))
print("Minimum in A:", min(A))

# Sorting the set
print("Sorted A:", sorted(A))

# Summing elements
print("Sum of elements in A:", sum(A))

# Union
print("Union of A and B:", A.union(B))
print("Union of A and B using |:", A | B)

# Intersection
print("Intersection of A and B:", A.intersection(B))
print("Intersection of A and B using &:", A & B)

# Difference
print("Difference of A and B:", A.difference(B))
print("Difference of A and B using -:", A - B)

# Symmetric difference
print("Symmetric difference of A and B:", A.symmetric_difference(B))
print("Symmetric difference of A and B using ^:", A ^ B)

# Clearing the set
A.clear()
print("After clearing A:", A)

# Copying the set
A = {1, 2, 3, 4, 5}
C = A.copy()
print("Copy of A:", C)

# Checking disjoint sets
print("Are A and B disjoint?", A.isdisjoint(B))

# Popping an element
popped_element = A.pop()
print("Popped element from A:", popped_element)
print("A after popping an element:", A)


