import math

def obtainMagnitude(vector):
    magnitude = 0
    for i in range(len(vector)):
        magnitude += vector[i]**2
    return math.sqrt(magnitude)

def obtainDotProduct(vector1, vector2):
    dotProduct = 0
    for i in range(len(vector1)):
        dotProduct += vector1[i] * vector2[i]
    return dotProduct

def obtainCrossProduct(Vector3D1, Vector3D2):
    xElement = Vector3D1[1] * Vector3D2[2] - Vector3D1[2] * Vector3D2[1]
    yElement = Vector3D1[2] * Vector3D2[0] - Vector3D1[0] * Vector3D2[2]
    zElement = Vector3D1[0] * Vector3D2[1] - Vector3D1[1] * Vector3D2[0]
    #Credit: http://mechanicsmap.psu.edu/websites/A1_vector_math/crossproduct/crossproduct.html
    return [xElement, yElement, zElement]

print(obtainMagnitude([]))
print(obtainMagnitude([3]))
print(obtainMagnitude([1,-1]))
print(obtainMagnitude([1,1,1,1]))


print(obtainDotProduct([], []))
print(obtainDotProduct([2,5,6], [3,7,8]))
print(obtainDotProduct([1,-1,0], [-1,-1,5]))
print(obtainDotProduct([1,0,1,0], [2,2,0,2]))

print(obtainCrossProduct([1,0,0],[0,1,0]))
print(obtainCrossProduct([1,0,0],[0,0,1]))
print(obtainCrossProduct([2,5,6],[3,7,8]))