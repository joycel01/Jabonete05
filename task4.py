class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    
    def describe(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}"

# Create three book objects
book1 = Book("Moby-Dick", "Herman Melville", 1851)
book2 = Book("Crime and Punishment", "Fyodor Dostoevsky", 1866)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

print("Book 1")
print(book1.describe())
print("\n")
print("Book 2")
print(book2.describe())
print("\n")
print("Book 3")
print(book3.describe())