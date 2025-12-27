# This file includes solutions for Recursion Problem Set


# 1. The Classic Staircase

def count_ways(n):
    calculateds = {0:1, 1:1}
    if n == 0 or n == 1:
        return 1
    else:
        if n in calculateds:
            return calculateds[n]
        else:
            calculated = count_ways(n-1) + count_ways(n-2)
            calculateds[n] = calculated
            return calculateds[n]
    
# 2. The Abstract Sum Architect

def count_sum_strings(n):
    if n < 3:
        return 1
    else:
        return count_sum_strings(n-1) + count_sum_strings(n-3)

# 3. The 2D Dungeon Crawler

def count_paths_2d(m, n):
    if m ==0 or n == 0:
        return 1
    else:
        return count_paths_2d(m-1, n-1) + count_paths_2d(m-1, n) + count_paths_2d(m, n-1)

# 4. The 3D Space Architect

def count_paths_3d(x, y, z):
    if x ==0 or y ==0 or z ==0:
        return 1
    else:
        return (
            count_paths_3d(x-1, y, z) +
            count_paths_3d(x, y-1, z) +
            count_paths_3d(x, y, z-1) +
            count_paths_3d(x-1, y-1, z) +
            count_paths_3d(x-1, y, z-1) +
            count_paths_3d(x, y-1, z-1) + 
            count_paths_3d(x-1, y-1, z-1)
        )


#Testing
print(count_ways(0))
print(count_ways(1))
print(count_ways(2))
print(count_ways(7))


