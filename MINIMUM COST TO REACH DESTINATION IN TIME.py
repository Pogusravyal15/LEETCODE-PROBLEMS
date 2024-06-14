from typing import List
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        # Create adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))
            # Dijkstra's Algorithm
            pq = [(passingFees[0], 0, 0)]
            # (total fees, time, city)
            dist = {(0, 0): passingFees[0]}
            # (time, city): total fees
            while pq:
                total_fees, time, city = heapq.heappop(pq)
                if city == n - 1:
                    return total_fees
                for neighbor, travel_time in graph[city]:
                    new_time = time + travel_time
                    if new_time <= maxTime:
                        new_fees = total_fees + passingFees[neighbor]
                        if (new_time, neighbor) not in dist or new_fees < dist[(new_time, neighbor)]:
                            dist[(new_time, neighbor)] = new_fees
                            heapq.heappush(pq, (new_fees, new_time, neighbor))
                            return -1 # If destination is unreachable within maxTime 