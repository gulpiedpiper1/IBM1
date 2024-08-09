import math
points = [(1, 2), (4, 6), (5, 8), (2, 1)]
def euclideanDistance(point1, point2):
    print(f"Hesaplanıyor: {point1} ve {point2}")
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        print(f"Mesafe: {dist}")
        distances.append(dist)
if distances:  
    min_distance = min(distances)
    print(f"Minimum Mesafe: {min_distance}")
else:
    print("Mesafeler listesi boş, mesafeler hesaplanamadı.")
