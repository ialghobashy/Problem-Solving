def count_alternating_sums_5(n, current_choices):
    if n == 0:
        print(current_choices)
        return 1
    elif n < 0:
        return 0
    count = 0
    for i in range(1, n + 1):
        # if i is even and the last number chosen is odd
        if i % 2 == 0 and (len(current_choices) == 0 or current_choices[-1] % 2 == 1):
            count += count_alternating_sums_5(n - i, [*current_choices, i])
        # if i is odd and the last number chosen is even
        elif i % 2 == 1 and (len(current_choices) == 0 or current_choices[-1] % 2 == 0):
            count += count_alternating_sums_5(n - i, [*current_choices, i])
    return count

for i in range(1,7):
    print(f"F({i})={count_alternating_sums_5(i, [])}") 