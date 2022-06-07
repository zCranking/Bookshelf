class bookshelf():
    def __init__(self, name, author, price, pub_year):
        self.name = name
        self.author = author
        self.price = price
        self.pub_year = pub_year
        
    def name():
        return self.name
    
    def author():
        return self.author
    
    def price():
        return self.price
    
    def pub_year():
        return self.pub_year
    
    def add_book(self):
        print("Book Name: " + self.name)
        print("Book Author: " + self.author)
        print("Book Price: " + str(self.price))
        print("Book Year Published: " + str(self.pub_year))
    
    def year_since_published(self):
        ysp = 2022 - int(self.pub_year)
        print(self.name + " was published " + str(ysp) + " years ago") 

Maze_Runner = bookshelf("Maze Runnner", "James Dashner", 5, 2009)
Maze_Runner.add_book()
Maze_Runner.year_since_published()

RNGDS= bookshelf("Renegades", "Marissa Meyer", 15, 2015)
RNGDS.add_book()
RNGDS.year_since_published()