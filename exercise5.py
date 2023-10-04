#Create a class that describes a book. It should have a name, author, and price

class Book:
    def __init__ (self, name, author, price):
        self.name = name
        self.author = author
        self.__price = price
       
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price 
        
    def __str__(self):
        return (f"Name: {self.name} \n"
                f" Author: {self.author} \n"
                f" Price: £{self.price} \n")  
       
        
b1 = Book(f'Harry Potter and The Chamber of Secrets', 'JK Rowling', '£10.00')
b2 = Book(f'Harry Potter and The Half Blood Prince', 'JK Rowling', '£15.00')
b3 = Book(f'Harry Potter and The Prisoner of Azkaban', 'JK Rowling', '£10.00')

print(f'{b1.name} by {b1.author} is {b1.price}')
print(f'{b2.name} by {b2.author} is {b2.price}')
print(f'{b3.name} by {b3.author} is {b3.price}')


# Declare a list and add objects 

book_list = []

b1 = Book(f'Harry Potter and The Chamber of Secrets', 'JK Rowling', '10.00')
b2 = Book(f'Harry Potter and The Half Blood Prince', 'JK Rowling', '15.00')
b3 = Book(f'Harry Potter and The Prisoner of Azkaban', 'JK Rowling', '10.00')

book_list.append(b1)
book_list.append(b2)
book_list.append(b3)


#Play around with various loops to iterate though loops.

 print("\nBooks in the list:")
    for book in book_list:
        print("Name:", book.name)
        print("Author:", book.author)
        print("Price:", book.price)
        print()

    if __name__ == "Book":
    Book()

#creating my own object class

class nflx_shows:
    def __init__(self, name, language, genre):
        self.name = name
        self.language = language
        self.genre = genre

    def __str__(self):
        return (f"Name: {self.name} \n"
                f"Language: {self.language} \n"
                f"Genre: {self.genre} \n")

n1 = nflx_shows(f'Crash Landing On You', 'Korean', 'Romance')
n2 = nflx_shows(f'La Casa De Papel', 'Spanish', 'Crime')
n3 = nflx_shows(f"Grey's Anatomy", "American-English", "Drama")
n4 = nflx_shows(f"Kara Sevda", "Turkish", "Romance")

print(f"- N E T F L I X  S H O W S -\n")

print(f"{n1.name} is a {n1.language} show based on {n1.genre}")
print(f"{n2.name} is a {n2.language} show based on {n2.genre}")
print(f"{n3.name} is a {n3.language} show based on {n3.genre}")
print(f"{n4.name} is a {n4.language} show based on {n4.genre}")

nflx_show_list = [n1, n2, n3, n4]

nflx_show_list = [n1, n2, n3, n4]

print("\n Netflix Show Information :\n")

for nflx_shows in nflx_show_list:
        print("Name:", nflx_shows.name)
        print("Language:", nflx_shows.language)
        print("Genre:", nflx_shows.genre)
        print()

if __name__ == "Netflix Shows":
    nflx_shows()