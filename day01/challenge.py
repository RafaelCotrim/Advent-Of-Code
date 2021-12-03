def read_file(filename):
    with open(filename) as f:
        return [int(line) for line in f]

def count_increment(nums):
    increment = 0
    previous = nums[0]

    for i in nums:
        if i > previous:
            increment += 1
        previous = i
    
    return increment

def sliding_window(data, size):
    slidind_data = []

    for i in range(len(data) - size + 1):

        slidind_data.append(sum(data[i:i+size]))

    return slidind_data


data = read_file('./input.txt')

print(f"Part one =  {count_increment(data)}")

print(f"Part two =  {count_increment(sliding_window(data, 3))}")
