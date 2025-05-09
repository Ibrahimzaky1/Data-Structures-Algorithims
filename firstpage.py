################################# FIRST QUESTION #################################
arr = []

data = [
    "jan 1,27", "jan 2,31", "jan 3,23", "jan 4,34", "jan 5,37",
    "jan 6,38", "jan 7,29", "jan 8,30", "jan 9,35", "jan 10,30"
]

for line in data:
    try:
        tokens = line.split(",")
        temperature =int(tokens[1])
        arr.append(temperature)
    except Exception as e:
        print(f"Invaild temperature in row{line}: {e}. ingnoring this row.")

first_week_temps = arr[:7]
average_temp = sum(first_week_temps) / len(first_week_temps)

print(f"Average temperature is the first week if January: {average_temp:.2f}°f")

max_temp = max(arr[:10])
print(f"Maximum tempertaure in the first 10 days 10 of january: {max_temp}°f")

################################# SECOND QUESTION #################################

arr = []

data = [
    "jan 1,27", "jan 2,31", "jan 3,23", "jan 4,34", "jan 5,37",
    "jan 6,38", "jan 7,29", "jan 8,30", "jan 9,35", "jan 10,30"
]

for entry in data:
    data, temp = entry.split(",")
    try:
        temperature = int(temp)
        arr.append(temperature)
    except ValueError as e:
        print(f"Invalid temperature entry: {e}")

jan_9_temp = arr[8]
jan_4_temp = arr[3]

print(f"The temperature on jan 9 was: {jan_9_temp}°F")
print(f"The temperature on jan 4 was: {jan_4_temp}°F")

################################# THIRD QUESTION #################################

import string

# Step 1: Open the file and read its contents
with open(r"C:\Users\ibrahim\Downloads\Python\New Text Document.txt", "r", encoding="utf-8") as f:
    poem = f.read().lower()  # Convert to lowercase for case-insensitive counting

# Step 2: Remove punctuation and split the text into words
translator = str.maketrans('', '', string.punctuation)
poem = poem.translate(translator)

words = poem.split()  # Split the text into words

# Step 3: Count the frequency of each word using a dictionary
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 4: Print the results
for word, count in word_count.items():
    print(f"'{word}': {count}")

################################# FOURTH QUESTION #################################

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        
        # Linear probing to handle collisions
        while self.table[index] is not None:
            index = (index + 1) % self.size
        
        self.table[index] = (key, value)
    
    def display(self):
        for index, item in enumerate(self.table):
            if item is not None:
                print(f"Index {index}: {item}")

# Create hash table and insert months with the number of days
hash_table = HashTable()

hash_table.insert("January", 31)
hash_table.insert("February", 28)
hash_table.insert("March", 31)
hash_table.insert("April", 30)
hash_table.insert("May", 31)

# Display the hash table
hash_table.display()
