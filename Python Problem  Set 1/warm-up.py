# PURPOSE OF THIS CODE
# PROJECT
# DATE
# NAME

def sumList(nums):
    sum = 0
    for i in range(len(nums)):
       sum += nums[i]
    return sum

print("testing sumList")
print(sumList([]))              # expected output: 0
print(sumList([3]))             # expected output: 3
print(sumList([1., 4.5, -3.2])) # expected output: 2.3

def estimatePi(n):
    count = 0 
    denominator = 1
    pi = 0
    for i in range(n):
        if (count%2 == 0):
            pi += 4/(denominator) 
        else:
            pi -= 4/(denominator)
        denominator += 2
        count += 1
    return pi

print("testing estimatePi")
print(estimatePi(1))     # expected (approximate) output: 4.0
print(estimatePi(10))    # expected (approximate) output: 3.0418396189294032
print(estimatePi(100))   # expected (approximate) output: 3.1315929035585537
print(estimatePi(1000))  # expected (approximate) output: 3.140592653839794
print(estimatePi(10000)) # expected (approximate) output: 3.1414926535900345

def scaleVec(vec, scalar):
    newArray = []
    for i in range(len(vec)):
        newArray.append(vec[i])
    for i in range(len(newArray)):
        newArray[i] = newArray[i] * scalar
    return newArray

print("testing scaleVec")
vec = []
print(scaleVec(vec, 5)) # expected output: []
print(vec) # expected output: []
vec = [1]
print(scaleVec(vec, 5)) # expected output: [5]
print(vec) # expected output: [1]
vec = [-2, 1.5, 0.]
print(scaleVec(vec, 6)) # expected output: [-12., 9., 0.]
print(vec) # expected output: [-2, 1.5, 0.]
