def smallest_trailer(rooms):
    # Compute differences
    for i in range(len(rooms)):
        c, n, _ = rooms[i]
        rooms[i] = (c, n, n - c)
    
    # Sort descending by difference (greedy choice)
    rooms.sort(key=lambda x: x[2], reverse=True)

    total_kids = sum(r[0] for r in rooms)
    diff_sum = 0  # running total of difference for renovated rooms
    max_shortage = 0

    for c, n, diff in rooms:
        shortage = c - diff_sum #f ind the effective shortage
        if shortage > max_shortage:
            max_shortage = shortage
        diff_sum += diff  # renovate this room next (adds its difference)

    return max(0, max_shortage)


    

def main():
    # Read number of test cases
    T = int(input())
    
    # Process each test case
    test_cases = []
    for _ in range(T):
        # Read number of rooms for this test case
        number_of_rooms = int(input())
        
        # Read room capacities
        rooms = []
        for _ in range(number_of_rooms):
            current_cap, new_cap = map(int, input().split())
            rooms.append((current_cap, new_cap, 0)) #initilize difference to 0
        
        test_cases.append(rooms)
    
    for i in test_cases:
        print(smallest_trailer(i))

if __name__ == "__main__":
    main()