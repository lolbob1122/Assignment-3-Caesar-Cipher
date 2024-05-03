data = [["apple", 10], ["banana", 20], ["orange", 15], ["grape", 5]]

# Step 1: Sorting based on the first list alphabetically
data.sort(key=lambda x: x[0])

# Step 2: Normalizing the values of the second list
# First, find the maximum value in the second list
max_value = max(data, key=lambda x: x[1])[1]

# Then, normalize each value by dividing it by the maximum value
normalized_data = [[item[0], item[1] / max_value] for item in data]

# Print the normalized data
for item in normalized_data:
    print(item)