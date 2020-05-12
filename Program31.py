# stack -> append(), pop() LIFO and queue FIFO
from collections import deque
books = []
books.append("Learn c")
books.append("Learn C++")
books.append("Learn Java")
print(books)

books.pop()
print("Now the last book is : ", books[-1])

books.pop()
print("Now the last book is : ", books[-1])

books.pop()

if not books:
    print("No books left")


# queue example -> FIFO
bank = deque(["x", "y", "z"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()

if not bank:
    print("No person left")