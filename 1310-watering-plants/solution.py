class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water = capacity
        for i, need in enumerate(plants):
            if water < need:
                steps += 2 * i  # walk back to river (i steps) + walk back to plant i 
                water = capacity
            water -= need
            steps += 1            # the one step to move to this plant
        return steps

#plants = list(map(int, input().strip('[]').split(',')))
#capacity = int(input())
#print(Solution().wateringPlants(plants, capacity))

