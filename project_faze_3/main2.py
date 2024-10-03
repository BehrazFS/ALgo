def weighted_class_scheduling(classes):
    classes.sort(key=lambda x: x[1][1])
    n = len(classes)
    dp = [0] * (n + 1)
    selected_classes = [[] for _ in range(n + 1)]

    def latest_non_conflicting(j):
        low, high = 0, j - 1
        while low <= high:
            mid = (low + high) // 2
            if classes[mid][1][1] <= classes[j][1][0]:
                if mid + 1 <= high and classes[mid + 1][1][1] <= classes[j][1][0]:
                    low = mid + 1
                else:
                    return mid
            else:
                high = mid - 1
        return -1

    for j in range(1, n + 1):
        include_class = classes[j - 1][0]
        l = latest_non_conflicting(j - 1)
        if l != -1:
            include_class += dp[l + 1]
        exclude_class = dp[j - 1]

        if include_class > exclude_class:
            dp[j] = include_class
            selected_classes[j] = selected_classes[l + 1] + [j - 1]  # Include the current class
        else:
            dp[j] = exclude_class
            selected_classes[j] = selected_classes[j - 1]  # Exclude the current class
    return dp[n], [classes[i] for i in selected_classes[n]]


days = {
    "Sunday": [],
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": []
}
classes = [
    (5, (1, 3), 'Monday'),
    (6, (2, 5), 'Tuesday'),
    (5, (4, 6), 'Wednesday'),
    (4, (6, 7), 'Thursday'),
    (11, (5, 8), 'Friday'),
    (2, (7, 9), 'Saturday'),
    (16, (1, 4), 'Monday'),
    (3, (0, 2), 'Sunday'),
    (10, (3, 5), 'Monday'),
    (8, (3, 6), 'Tuesday'),
    (15, (4, 7), 'Wednesday'),
    (7, (2, 4), 'Thursday'),
    (9, (6, 9), 'Friday'),
    (4, (5, 7), 'Saturday'),
    (12, (7, 10), 'Sunday'),
    (10, (0, 3), 'Monday'),
    (6, (4, 8), 'Tuesday'),
    (11, (3, 6), 'Wednesday'),
    (13, (5, 9), 'Thursday'),
    (8, (1, 4), 'Friday')
]

for i in classes:
    days[i[2]].append(i)
all_units = 0
for day, arr in days.items():
    max_weight, picked_classes = weighted_class_scheduling(arr)
    all_units += max_weight
    print(f"Maximum units on {day!s}: {max_weight!s}")
    print(f"Picked classes on {day!s}: {picked_classes!s}")
    print()
print(f"max taken units : {all_units!s}")
# todo : online and exam date problem
