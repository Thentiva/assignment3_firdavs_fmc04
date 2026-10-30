def replace_value(values, index, new_value):
    values[index] = new_value
    return None

def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def summarize(values):
    stats_record = (min(values), max(values), sum(values))
    return stats_record

def main():
    num_days = int(input("Enter the number of days: "))
    
    original = []
    for _ in range(num_days):
        calls = int(input("Enter the number of calls: "))
        original.append(calls)
        
    # Copy original to updated using slicing
    updated = original[:]
    
    index_to_correct = int(input("Enter the index to correct: "))
    new_calls = int(input("Enter the new number of calls: "))
    replace_value(updated, index_to_correct, new_calls)
    
    target = int(input("Enter the number of calls to search for: "))
    
    first_index = find_first(updated, target)
    match_count = updated.count(target)
    
    minimum, maximum, total = summarize(updated)
    sorted_list = sorted(updated)
    
    print(f"Original: {original}")
    print(f"Updated: {updated}")
    print(f"Sorted: {sorted_list}")
    print(f"Minimum number of calls: {minimum}")
    print(f"Maximum number of calls: {maximum}")
    print(f"Total number of calls: {total}")
    
    if first_index != -1:
        print(f"First matching index: {first_index}")
    else:
        print("Target not found")
        
    print(f"Matching values: {match_count}")

if __name__ == "__main__":
    main()