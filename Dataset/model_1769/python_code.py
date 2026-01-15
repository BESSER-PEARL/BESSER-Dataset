from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class book_Article:

    def __init__(self, title: str, Article: "book_Book" = None, articles: "book_Book" = None, articles10: set["book_Person"] = None, Article18: "book_Person" = None):
        self.title = title
        self.Article = Article
        self.articles = articles
        self.articles10 = articles10 if articles10 is not None else set()
        self.Article18 = Article18
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def articles10(self):
        return self.__articles10

    @articles10.setter
    def articles10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Article__articles10", None)
        self.__articles10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person11"):
                    opp_val = getattr(item, "Person11", None)
                    
                    if opp_val == self:
                        setattr(item, "Person11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person11"):
                    opp_val = getattr(item, "Person11", None)
                    
                    setattr(item, "Person11", self)
                    

    @property
    def Article18(self):
        return self.__Article18

    @Article18.setter
    def Article18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Article__Article18", None)
        self.__Article18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author17"):
                opp_val = getattr(old_value, "author17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author17"):
                opp_val = getattr(value, "author17", None)
                if opp_val is None:
                    setattr(value, "author17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def articles(self):
        return self.__articles

    @articles.setter
    def articles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Article__articles", None)
        self.__articles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book8"):
                opp_val = getattr(old_value, "Book8", None)
                if opp_val == self:
                    setattr(old_value, "Book8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book8"):
                opp_val = getattr(value, "Book8", None)
                setattr(value, "Book8", self)

    @property
    def Article(self):
        return self.__Article

    @Article.setter
    def Article(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Article__Article", None)
        self.__Article = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book6"):
                opp_val = getattr(old_value, "book6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book6"):
                opp_val = getattr(value, "book6", None)
                if opp_val is None:
                    setattr(value, "book6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class book_Person:

    def __init__(self, name: str, Person: "book_Book" = None, Person4: "book_Book" = None, Person11: "book_Article" = None, editor: set["book_Book"] = None, author: set["book_Book"] = None, author17: set["book_Article"] = None):
        self.name = name
        self.Person = Person
        self.Person4 = Person4
        self.Person11 = Person11
        self.editor = editor if editor is not None else set()
        self.author = author if author is not None else set()
        self.author17 = author17 if author17 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Person11(self):
        return self.__Person11

    @Person11.setter
    def Person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Person__Person11", None)
        self.__Person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articles10"):
                opp_val = getattr(old_value, "articles10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articles10"):
                opp_val = getattr(value, "articles10", None)
                if opp_val is None:
                    setattr(value, "articles10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def author17(self):
        return self.__author17

    @author17.setter
    def author17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Person__author17", None)
        self.__author17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Article18"):
                    opp_val = getattr(item, "Article18", None)
                    
                    if opp_val == self:
                        setattr(item, "Article18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Article18"):
                    opp_val = getattr(item, "Article18", None)
                    
                    setattr(item, "Article18", self)
                    

    @property
    def editor(self):
        return self.__editor

    @editor.setter
    def editor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Person__editor", None)
        self.__editor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book13"):
                    opp_val = getattr(item, "Book13", None)
                    
                    if opp_val == self:
                        setattr(item, "Book13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book13"):
                    opp_val = getattr(item, "Book13", None)
                    
                    setattr(item, "Book13", self)
                    

    @property
    def Person4(self):
        return self.__Person4

    @Person4.setter
    def Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Person__Person4", None)
        self.__Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authored"):
                opp_val = getattr(old_value, "authored", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authored"):
                opp_val = getattr(value, "authored", None)
                if opp_val is None:
                    setattr(value, "authored", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edited"):
                opp_val = getattr(old_value, "edited", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edited"):
                opp_val = getattr(value, "edited", None)
                if opp_val is None:
                    setattr(value, "edited", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Person__author", None)
        self.__author = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book15"):
                    opp_val = getattr(item, "Book15", None)
                    
                    if opp_val == self:
                        setattr(item, "Book15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book15"):
                    opp_val = getattr(item, "Book15", None)
                    
                    setattr(item, "Book15", self)
                    

class book_Book:

    def __init__(self, title: str, Book: "book_DocBook" = None, book: "book_DocBook" = None, edited: set["book_Person"] = None, authored: set["book_Person"] = None, book6: set["book_Article"] = None, Book8: "book_Article" = None, Book13: "book_Person" = None, Book15: "book_Person" = None):
        self.title = title
        self.Book = Book
        self.book = book
        self.edited = edited if edited is not None else set()
        self.authored = authored if authored is not None else set()
        self.book6 = book6 if book6 is not None else set()
        self.Book8 = Book8
        self.Book13 = Book13
        self.Book15 = Book15
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def edited(self):
        return self.__edited

    @edited.setter
    def edited(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__edited", None)
        self.__edited = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def Book8(self):
        return self.__Book8

    @Book8.setter
    def Book8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__Book8", None)
        self.__Book8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articles"):
                opp_val = getattr(old_value, "articles", None)
                if opp_val == self:
                    setattr(old_value, "articles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articles"):
                opp_val = getattr(value, "articles", None)
                setattr(value, "articles", self)

    @property
    def authored(self):
        return self.__authored

    @authored.setter
    def authored(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__authored", None)
        self.__authored = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person4"):
                    opp_val = getattr(item, "Person4", None)
                    
                    if opp_val == self:
                        setattr(item, "Person4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person4"):
                    opp_val = getattr(item, "Person4", None)
                    
                    setattr(item, "Person4", self)
                    

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__book", None)
        self.__book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DocBook"):
                opp_val = getattr(old_value, "DocBook", None)
                if opp_val == self:
                    setattr(old_value, "DocBook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DocBook"):
                opp_val = getattr(value, "DocBook", None)
                setattr(value, "DocBook", self)

    @property
    def book6(self):
        return self.__book6

    @book6.setter
    def book6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__book6", None)
        self.__book6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Article"):
                    opp_val = getattr(item, "Article", None)
                    
                    if opp_val == self:
                        setattr(item, "Article", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Article"):
                    opp_val = getattr(item, "Article", None)
                    
                    setattr(item, "Article", self)
                    

    @property
    def Book13(self):
        return self.__Book13

    @Book13.setter
    def Book13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__Book13", None)
        self.__Book13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "editor"):
                opp_val = getattr(old_value, "editor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "editor"):
                opp_val = getattr(value, "editor", None)
                if opp_val is None:
                    setattr(value, "editor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docBook"):
                opp_val = getattr(old_value, "docBook", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docBook"):
                opp_val = getattr(value, "docBook", None)
                if opp_val is None:
                    setattr(value, "docBook", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book15(self):
        return self.__Book15

    @Book15.setter
    def Book15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_book_Book__Book15", None)
        self.__Book15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author"):
                opp_val = getattr(old_value, "author", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author"):
                opp_val = getattr(value, "author", None)
                if opp_val is None:
                    setattr(value, "author", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class book_DocBook:

    pass