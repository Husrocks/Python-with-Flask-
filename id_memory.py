x = 1000
y = 1000
print(id(x), id(y))  # Different IDs because large numbers are not cached

x = 5
y = 5
print(id(x), id(y))  # Same ID because small integers (-5 to 256) are cached

str1 = "hello"
str2 = "hello"
print(id(str1), id(str2))  # Same ID (string interning)
