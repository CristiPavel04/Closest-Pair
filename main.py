import matplotlib
matplotlib.use('TkAgg')
import math
import matplotlib.pyplot as plt

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    min_dist = float('inf')
    closest_pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    return min_dist, closest_pair

def strip_closest(strip, d):
    min_dist = d
    closest_pair = None
    strip.sort(key=lambda point: point[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (strip[i], strip[j])
    return min_dist, closest_pair

def closest_pair_recursive(points):
    if len(points) <= 3:
        return brute_force(points)
    mid = len(points) // 2
    mid_point = points[mid]
    dl, pair_l = closest_pair_recursive(points[:mid])
    dr, pair_r = closest_pair_recursive(points[mid:])
    if dl < dr:
        d, closest_pair = dl, pair_l
    else:
        d, closest_pair = dr, pair_r
    strip = [point for point in points if abs(point[0] - mid_point[0]) < d]
    strip_dist, strip_pair = strip_closest(strip, d)
    if strip_dist < d:
        return strip_dist, strip_pair
    return d, closest_pair

def closest_pair(points):
    points.sort(key=lambda point: point[0])
    return closest_pair_recursive(points)

def visualize(points, closest_pair):
    plt.scatter(*zip(*points), color='blue', label='Points')
    if closest_pair:
        p1, p2 = closest_pair
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='red', linewidth=2, label='Closest Pair')
        plt.scatter(*p1, color='red')
        plt.scatter(*p2, color='red')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Closest Pair of Points')
    plt.grid(True)
    plt.legend()
    plt.show()

points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
dist, closest_pair = closest_pair(points)

print(f"The smallest distance is: {dist}")
print(f"The closest pair is: {closest_pair}")

visualize(points, closest_pair)
