
with open('books_url.txt') as f:
    books_url = f.readlines()

for i in books_url:
    print(i.replace('\n', ''))

# print(books_url)
