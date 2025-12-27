# This file includes solutions for Recursion Problem Set


# 1. The Classic Staircase


def count_ways(n):
    def count_ways_in(n):
        if n in calculateds:
            return calculateds[n]
        else:
            calculated = count_ways_in(n-1) + count_ways_in(n-2)
            calculateds[n] = calculated
            return calculateds[n]
    calculateds = {0:1, 1:1}
    return count_ways_in(n)
    
print("Testing for the first function with n = 50: ")
print(count_ways(50))      # By default in python recursion limit is 1000 but you can increase more
    
# 2. The Abstract Sum Architect

def count_sum_strings(n):
    def count_sum_strings_in(n):
        if n in calculateds:
            return calculateds[n]
        else:
            calculated = count_sum_strings_in(n-1) + count_sum_strings_in(n-3)
            calculateds[n] = calculated
            return calculateds[n]
    calculateds = {0:1, 1:1, 2:1}
    return count_sum_strings_in(n)

print("Testing for the second function with n = 50: ")
print(count_sum_strings(50))


# 3. The 2D Dungeon Crawler

def count_paths_2d(m, n):
    def count_paths_2d_in(m, n):
        if m ==0 or n == 0:
            return 1
        else:
            if (m, n) in calculateds:
                return calculateds[(m, n)]
            else:
                calculated = (count_paths_2d_in(m-1, n-1) + 
                            count_paths_2d_in(m-1, n) + 
                            count_paths_2d_in(m, n-1))
                calculateds[(m, n)] = calculated
                return calculateds[(m, n)]
    calculateds = {}
    return count_paths_2d_in(m, n)

print("Testing for the third function with n = 50, m = 30: ")
print(count_paths_2d(30, 50)) 

# 4. The 3D Space Architect

def count_paths_3d(x, y, z):
    def count_paths_3d_in(x, y, z):
        if x ==0 or y ==0 or z ==0:
            return 1
        else:
            if (x, y, z) in calculateds:
                return calculateds[(x, y, z)]
            else:     
                calculated =  (
                    count_paths_3d_in(x-1, y, z) +
                    count_paths_3d_in(x, y-1, z) +
                    count_paths_3d_in(x, y, z-1) 
                )
                calculateds[(x, y, z)] = calculated
                return calculateds[(x, y, z)]
            
    calculateds = {}
    return count_paths_3d_in(x, y, z)

print("Testing for the fourth function with x = 20, y = 30, z = 20: ")
print(count_paths_3d(20, 30, 20)) 

# 5. Advanced: The Restricted Path

def count_advanced_ways(n, broken_steps):
    def calc_ways(n, stamina):
        if n in broken_steps: # enough to handle broken steps
            return 0
        elif n in calculateds: # base case
            return calculateds[n]
        elif stamina:   # handle stamina 
            calculated = calc_ways(n-1, True) + calc_ways(n-2, False)
            calculateds[n] = calculated
            return calculateds[n]
        elif not stamina:
            calculated = calc_ways(n-1, True)
            calculateds[n] = calculated
            return calculateds[n]
    
    calculateds = {0:1, 1:1}
    return calc_ways(n, True)

print("Testing for the fifth function with n = 20, broken_steps =[5, 8, 12, 17] ")
print(count_advanced_ways(20, [5, 8, 12, 17])) 

