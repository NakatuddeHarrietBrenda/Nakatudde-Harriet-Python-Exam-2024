
#i)

class Book():
    def _init_(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def infoAboutBook(self):
            
        print(f'the book {self.title} was written by {self.author} with {self.pages} pages')

myBook = Book(title = "Great Expectations", author= "William Shake Spear", pages = 2556)

myBook.infoAboutBook()



#ii)
class Ebook(Book):
    def _init_(self, title, author, pages):
        return super()._init_(title, author, pages)
    
    
class EBook(Book):
    def _init_(self, title, author, pages, format):
        
        self.file_format = format
        return super()._init_(title, author, pages)
    
#iii)
    def titleAndAuthor(self):
         
        print(f'The book {self.title} was written by {self.author}')
myBook = Book(title = "Great Expectations", author= "William Shake Spear", pages = 2556)

myBook.titleAndAuthor()


#iv)
# a)
# A class is an OOP element that collects functions, variables 

#b)
# An object is an attribute of a class
