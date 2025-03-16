numbers = [1, 2, 3, 4 , "ji"]  # Iterable
iterator = iter(numbers)  # Convert to iterator

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
print(next(iterator))  # Output: 4
print(next(iterator))  # Error: StopIteration (No more items)

class Counter:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self  # Iterator object

    def __next__(self):
        if self.num > 5:
            raise StopIteration # Stop when reaching 5
        value = self.num
        self.num += 1
        return value

# Using the iterator
count = Counter()
for num in count:
    print(num)
