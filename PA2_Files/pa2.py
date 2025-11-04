# PA2 Skeleton Code
# DSA2, fall 2025

# This code will read in the input, and put the values into data structures.
# This skeleton code only reads in the input.
devices = {}
[num_devices,num_usages] = [int(x) for x in input().split(" ")]
for _ in range(num_devices):
    devices[input()] = []

for _ in range(num_usages):
    [device_name, start, finish, usage] = input().split(" ")
    devices[device_name].append([int(start), int(finish), int(usage)])

def merge(left, right):
    i, j = 0, 0
    left_h = right_h = 0
    left_device = right_device = None
    curr_h = 0
    curr_device = None
    merged = []

    while i < len(left) and j < len(right):
        #choose the smaller x
        if left[i][0] < right[j][0]:
            x, left_h, left_device = left[i]
            i += 1
        elif right[j][0] < left[i][0]:
            x, right_h, right_device = right[j]
            j += 1
        else:
            x = left[i][0]
            left_h, left_device = left[i][1], left[i][2]
            right_h, right_device = right[j][1], right[j][2]
            i += 1
            j += 1

        if left_h > right_h:
            max_h, max_device = left_h, left_device
        else:
            max_h, max_device = right_h, right_device

        if curr_h != max_h or curr_device != max_device:
            merged.append((x, max_h, max_device))
            curr_h, curr_device = max_h, max_device

    merged.extend(left[i:])
    merged.extend(right[j:])

    #remove redundant points
    clean_up = [merged[0]]
    for x, h, device in merged[1:]:
        if h != clean_up[-1][1] or device != clean_up[-1][2]:
            clean_up.append((x, h, device))

    return clean_up

def find_skyline(periods):
    #base case
    if len(periods) == 1:
        s, f, w, device = periods[0]
        return [(s, w, device), (f, 0, device)]
    
    mid = len(periods) // 2
    left_skyline = find_skyline(periods[:mid])
    right_skyline = find_skyline(periods[mid:])
    return merge(left_skyline, right_skyline)

def main():
    all_periods = []
    for d in devices:
        for (s, f, w) in devices[d]:
            all_periods.append((s, f, w, d))

    all_periods.sort(key=lambda x: x[0])
    silhouette = find_skyline(all_periods)

    durations = {d: 0 for d in devices}
    for i in range(len(silhouette) - 1):
        x1, h1, d1 = silhouette[i]
        x2, _, _ = silhouette[i + 1]
        durations[d1] += (x2 - x1)

    max_dev = max(durations.items(), key=lambda x: (x[1], -list(devices.keys()).index(x[0])))
    min_dev = min(durations.items(), key=lambda x: (x[1], list(devices.keys()).index(x[0])))

    # --- Output ---
    for (x, h, _) in silhouette:
        print(f"({x},{h})", end=" ")
    print()
    print(f"{max_dev[0]} {max_dev[1]}")
    print(f"{min_dev[0]} {min_dev[1]}")

if __name__ == "__main__":
    main()