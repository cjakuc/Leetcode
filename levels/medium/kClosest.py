# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq

# My solution: applying the heap to the end is just sorting at the end so not the optimal time complexity
# def kClosest(points, k):
#     def euclid_dist(x1, y1, y2=0, x2=0):
#         distance = ((x1 - x2)**2 + (y1 -y2)**2)**(1/2)
#         return distance
#     def sortKey(point_tup):
#         return point_tup[0]

#     for idx, point in enumerate(points):
#         x1 = point[0]
#         y1 = point[1]
#         point_tup = (euclid_dist(x1=x1, y1=y1), point)
#         points[idx] = point_tup

#     closest_points = heapq.nsmallest(k, points, key = sortKey)
#     closest_points = [point_tup[1] for point_tup in closest_points]
    
#     return closest_points

# Optimal solution sorts as it goes so has better time complexity
def kClosest(points, k):
        # Time Complexity : O(Nlogk), where N is the number of elements in the array and k is 
        # the number of closest elements we need to find. Since there are a max of O(k) elements 
        # at any point in the heap, the push and pop operation only take O(logk) and this happens 
        # O(N) times leading to total time complexity of O(Nlogk)
        # Space Complexity : O(k), for maintain heap
        heap, euclidean = [], lambda x, y : x*x + y*y
        for i, (x, y) in enumerate(points):
            d = euclidean(x, y)
            if len(heap) == k:
                heapq.heappushpop(heap, (-d, i))     # -d to convert to max-heap (default is min)
            else: 
                heapq.heappush(heap, (-d, i))
        
        return [points[i] for d, i in heap]

# Another way to do it
def kClosest(points, k):
    # Time Complexity : O(N + klogN), constructing the heap from given array of points P can be 
    # done in O(N) time. Then each heap pop operation would take O(logN) time which will be called 
    # for k times. Thus overall time will be O(N + klogN)
    # Space Complexity : O(1), we are doing it in-place. If input modification is not allowed, use a copy of P and that would take O(N) space
    euclidean = lambda x, y : x*x + y*y
    for p in points:
        p.insert(0, euclidean(p[0], p[1]))
    heapq.heapify(points)
    return [heapq.heappop(points)[1:] for i in range(k)]
    

# One liner that does it all
def kClosest(points, k):
        return heapq.nsmallest(k, points,  lambda x: x[0] ** 2 + x[1] ** 2)

assert kClosest(points = [[1,3],[-2,2]], k = 1) == [[-2, 2]]
assert kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2) == ([[3,3],[-2,4]]) or ([[-2,4],[3,3]])
