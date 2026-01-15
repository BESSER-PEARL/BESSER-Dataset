from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):
    Mystery = "Mystery"
    ScienceFiction = "ScienceFiction"
    Biography = "Biography"


############################################
# Definition of Classes
############################################

class library_Chapter:

    def __init__(self, name: str, library_Chapter: "library_Book" = None):
        self.name = name
        self.library_Chapter = library_Chapter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Chapter(self):
        return self.__library_Chapter

    @library_Chapter.setter
    def library_Chapter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Chapter__library_Chapter", None)
        self.__library_Chapter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book13"):
                opp_val = getattr(old_value, "library_Book13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book13"):
                opp_val = getattr(value, "library_Book13", None)
                if opp_val is None:
                    setattr(value, "library_Book13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Review:

    def __init__(self, title: str, positive: bool, Review: "library_Book" = None, reviews: "library_Book" = None):
        self.title = title
        self.positive = positive
        self.Review = Review
        self.reviews = reviews
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def positive(self) -> bool:
        return self.__positive

    @positive.setter
    def positive(self, positive: bool):
        self.__positive = positive

    @property
    def Review(self):
        return self.__Review

    @Review.setter
    def Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Review__Review", None)
        self.__Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book"):
                opp_val = getattr(old_value, "book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book"):
                opp_val = getattr(value, "book", None)
                if opp_val is None:
                    setattr(value, "book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Review__reviews", None)
        self.__reviews = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book18"):
                opp_val = getattr(old_value, "Book18", None)
                if opp_val == self:
                    setattr(old_value, "Book18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book18"):
                opp_val = getattr(value, "Book18", None)
                setattr(value, "Book18", self)

class library_CommunityRole:

    def __init__(self, role: str, CommunityRole: "library_Writer" = None, roles: "library_Community" = None, participates: set["library_Writer"] = None, CommunityRole25: "library_Community" = None):
        self.role = role
        self.CommunityRole = CommunityRole
        self.roles = roles
        self.participates = participates if participates is not None else set()
        self.CommunityRole25 = CommunityRole25
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def participates(self):
        return self.__participates

    @participates.setter
    def participates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_CommunityRole__participates", None)
        self.__participates = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Writer30"):
                    opp_val = getattr(item, "Writer30", None)
                    
                    if opp_val == self:
                        setattr(item, "Writer30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Writer30"):
                    opp_val = getattr(item, "Writer30", None)
                    
                    setattr(item, "Writer30", self)
                    

    @property
    def CommunityRole(self):
        return self.__CommunityRole

    @CommunityRole.setter
    def CommunityRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_CommunityRole__CommunityRole", None)
        self.__CommunityRole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participants"):
                opp_val = getattr(old_value, "participants", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participants"):
                opp_val = getattr(value, "participants", None)
                if opp_val is None:
                    setattr(value, "participants", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CommunityRole25(self):
        return self.__CommunityRole25

    @CommunityRole25.setter
    def CommunityRole25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_CommunityRole__CommunityRole25", None)
        self.__CommunityRole25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "community"):
                opp_val = getattr(old_value, "community", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "community"):
                opp_val = getattr(value, "community", None)
                if opp_val is None:
                    setattr(value, "community", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def roles(self):
        return self.__roles

    @roles.setter
    def roles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_CommunityRole__roles", None)
        self.__roles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Community28"):
                opp_val = getattr(old_value, "Community28", None)
                if opp_val == self:
                    setattr(old_value, "Community28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Community28"):
                opp_val = getattr(value, "Community28", None)
                setattr(value, "Community28", self)

class library_Opinion:

    def __init__(self, text: str, context: str, Opinion: "library_Writer" = None, Opinion16: "library_Book" = None, opinions: "library_Writer" = None, opinions22: "library_Book" = None):
        self.text = text
        self.context = context
        self.Opinion = Opinion
        self.Opinion16 = Opinion16
        self.opinions = opinions
        self.opinions22 = opinions22
        
    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def opinions(self):
        return self.__opinions

    @opinions.setter
    def opinions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Opinion__opinions", None)
        self.__opinions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Writer20"):
                opp_val = getattr(old_value, "Writer20", None)
                if opp_val == self:
                    setattr(old_value, "Writer20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Writer20"):
                opp_val = getattr(value, "Writer20", None)
                setattr(value, "Writer20", self)

    @property
    def opinions22(self):
        return self.__opinions22

    @opinions22.setter
    def opinions22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Opinion__opinions22", None)
        self.__opinions22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book23"):
                opp_val = getattr(old_value, "Book23", None)
                if opp_val == self:
                    setattr(old_value, "Book23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book23"):
                opp_val = getattr(value, "Book23", None)
                setattr(value, "Book23", self)

    @property
    def Opinion(self):
        return self.__Opinion

    @Opinion.setter
    def Opinion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Opinion__Opinion", None)
        self.__Opinion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writer"):
                opp_val = getattr(old_value, "writer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writer"):
                opp_val = getattr(value, "writer", None)
                if opp_val is None:
                    setattr(value, "writer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Opinion16(self):
        return self.__Opinion16

    @Opinion16.setter
    def Opinion16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Opinion__Opinion16", None)
        self.__Opinion16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book15"):
                opp_val = getattr(old_value, "book15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book15"):
                opp_val = getattr(value, "book15", None)
                if opp_val is None:
                    setattr(value, "book15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Community:

    def __init__(self, name: str, Community: "library_Library" = None, Community28: "library_CommunityRole" = None, community: set["library_CommunityRole"] = None, communities: "library_Library" = None):
        self.name = name
        self.Community = Community
        self.Community28 = Community28
        self.community = community if community is not None else set()
        self.communities = communities
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Community(self):
        return self.__Community

    @Community.setter
    def Community(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Community__Community", None)
        self.__Community = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library"):
                opp_val = getattr(old_value, "library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library"):
                opp_val = getattr(value, "library", None)
                if opp_val is None:
                    setattr(value, "library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Community28(self):
        return self.__Community28

    @Community28.setter
    def Community28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Community__Community28", None)
        self.__Community28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roles"):
                opp_val = getattr(old_value, "roles", None)
                if opp_val == self:
                    setattr(old_value, "roles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roles"):
                opp_val = getattr(value, "roles", None)
                setattr(value, "roles", self)

    @property
    def community(self):
        return self.__community

    @community.setter
    def community(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Community__community", None)
        self.__community = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CommunityRole25"):
                    opp_val = getattr(item, "CommunityRole25", None)
                    
                    if opp_val == self:
                        setattr(item, "CommunityRole25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CommunityRole25"):
                    opp_val = getattr(item, "CommunityRole25", None)
                    
                    setattr(item, "CommunityRole25", self)
                    

    @property
    def communities(self):
        return self.__communities

    @communities.setter
    def communities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Community__communities", None)
        self.__communities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library"):
                opp_val = getattr(old_value, "Library", None)
                if opp_val == self:
                    setattr(old_value, "Library", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library"):
                opp_val = getattr(value, "Library", None)
                setattr(value, "Library", self)

class library_Book:

    def __init__(self, category: str, title: str, pages: int, library_Book: "library_Library" = None, Book: "library_Writer" = None, library_Book7: "library_Writer" = None, books: "library_Writer" = None, book: set["library_Review"] = None, library_Book13: set["library_Chapter"] = None, book15: set["library_Opinion"] = None, Book18: "library_Review" = None, Book23: "library_Opinion" = None):
        self.category = category
        self.title = title
        self.pages = pages
        self.library_Book = library_Book
        self.Book = Book
        self.library_Book7 = library_Book7
        self.books = books
        self.book = book if book is not None else set()
        self.library_Book13 = library_Book13 if library_Book13 is not None else set()
        self.book15 = book15 if book15 is not None else set()
        self.Book18 = Book18
        self.Book23 = Book23
        
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def library_Book(self):
        return self.__library_Book

    @library_Book.setter
    def library_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book", None)
        self.__library_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library2"):
                opp_val = getattr(old_value, "library_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library2"):
                opp_val = getattr(value, "library_Library2", None)
                if opp_val is None:
                    setattr(value, "library_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book18(self):
        return self.__Book18

    @Book18.setter
    def Book18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__Book18", None)
        self.__Book18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews"):
                opp_val = getattr(old_value, "reviews", None)
                if opp_val == self:
                    setattr(old_value, "reviews", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews"):
                opp_val = getattr(value, "reviews", None)
                setattr(value, "reviews", self)

    @property
    def book15(self):
        return self.__book15

    @book15.setter
    def book15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__book15", None)
        self.__book15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Opinion16"):
                    opp_val = getattr(item, "Opinion16", None)
                    
                    if opp_val == self:
                        setattr(item, "Opinion16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Opinion16"):
                    opp_val = getattr(item, "Opinion16", None)
                    
                    setattr(item, "Opinion16", self)
                    

    @property
    def library_Book13(self):
        return self.__library_Book13

    @library_Book13.setter
    def library_Book13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book13", None)
        self.__library_Book13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Chapter"):
                    opp_val = getattr(item, "library_Chapter", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Chapter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Chapter"):
                    opp_val = getattr(item, "library_Chapter", None)
                    
                    setattr(item, "library_Chapter", self)
                    

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__Book", None)
        self.__Book = value
        
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

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__book", None)
        self.__book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Review"):
                    opp_val = getattr(item, "Review", None)
                    
                    if opp_val == self:
                        setattr(item, "Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Review"):
                    opp_val = getattr(item, "Review", None)
                    
                    setattr(item, "Review", self)
                    

    @property
    def Book23(self):
        return self.__Book23

    @Book23.setter
    def Book23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__Book23", None)
        self.__Book23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opinions22"):
                opp_val = getattr(old_value, "opinions22", None)
                if opp_val == self:
                    setattr(old_value, "opinions22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opinions22"):
                opp_val = getattr(value, "opinions22", None)
                setattr(value, "opinions22", self)

    @property
    def library_Book7(self):
        return self.__library_Book7

    @library_Book7.setter
    def library_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book7", None)
        self.__library_Book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Writer6"):
                opp_val = getattr(old_value, "library_Writer6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Writer6"):
                opp_val = getattr(value, "library_Writer6", None)
                if opp_val is None:
                    setattr(value, "library_Writer6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__books", None)
        self.__books = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Writer"):
                opp_val = getattr(old_value, "Writer", None)
                if opp_val == self:
                    setattr(old_value, "Writer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Writer"):
                opp_val = getattr(value, "Writer", None)
                setattr(value, "Writer", self)

class library_Writer:

    def __init__(self, name: str, library_Writer: "library_Library" = None, author: set["library_Book"] = None, library_Writer6: set["library_Book"] = None, writer: set["library_Opinion"] = None, participants: set["library_CommunityRole"] = None, Writer: "library_Book" = None, Writer20: "library_Opinion" = None, Writer30: "library_CommunityRole" = None):
        self.name = name
        self.library_Writer = library_Writer
        self.author = author if author is not None else set()
        self.library_Writer6 = library_Writer6 if library_Writer6 is not None else set()
        self.writer = writer if writer is not None else set()
        self.participants = participants if participants is not None else set()
        self.Writer = Writer
        self.Writer20 = Writer20
        self.Writer30 = Writer30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Writer6(self):
        return self.__library_Writer6

    @library_Writer6.setter
    def library_Writer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer6", None)
        self.__library_Writer6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book7"):
                    opp_val = getattr(item, "library_Book7", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book7"):
                    opp_val = getattr(item, "library_Book7", None)
                    
                    setattr(item, "library_Book7", self)
                    

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__author", None)
        self.__author = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    setattr(item, "Book", self)
                    

    @property
    def Writer20(self):
        return self.__Writer20

    @Writer20.setter
    def Writer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__Writer20", None)
        self.__Writer20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opinions"):
                opp_val = getattr(old_value, "opinions", None)
                if opp_val == self:
                    setattr(old_value, "opinions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opinions"):
                opp_val = getattr(value, "opinions", None)
                setattr(value, "opinions", self)

    @property
    def Writer30(self):
        return self.__Writer30

    @Writer30.setter
    def Writer30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__Writer30", None)
        self.__Writer30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participates"):
                opp_val = getattr(old_value, "participates", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participates"):
                opp_val = getattr(value, "participates", None)
                if opp_val is None:
                    setattr(value, "participates", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__participants", None)
        self.__participants = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CommunityRole"):
                    opp_val = getattr(item, "CommunityRole", None)
                    
                    if opp_val == self:
                        setattr(item, "CommunityRole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CommunityRole"):
                    opp_val = getattr(item, "CommunityRole", None)
                    
                    setattr(item, "CommunityRole", self)
                    

    @property
    def writer(self):
        return self.__writer

    @writer.setter
    def writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__writer", None)
        self.__writer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Opinion"):
                    opp_val = getattr(item, "Opinion", None)
                    
                    if opp_val == self:
                        setattr(item, "Opinion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Opinion"):
                    opp_val = getattr(item, "Opinion", None)
                    
                    setattr(item, "Opinion", self)
                    

    @property
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__Writer", None)
        self.__Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books"):
                opp_val = getattr(old_value, "books", None)
                if opp_val == self:
                    setattr(old_value, "books", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books"):
                opp_val = getattr(value, "books", None)
                setattr(value, "books", self)

    @property
    def library_Writer(self):
        return self.__library_Writer

    @library_Writer.setter
    def library_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer", None)
        self.__library_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library"):
                opp_val = getattr(old_value, "library_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library"):
                opp_val = getattr(value, "library_Library", None)
                if opp_val is None:
                    setattr(value, "library_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Library:

    def __init__(self, name: str, library_Library: set["library_Writer"] = None, library_Library2: set["library_Book"] = None, library: set["library_Community"] = None, Library: "library_Community" = None):
        self.name = name
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library2 = library_Library2 if library_Library2 is not None else set()
        self.library = library if library is not None else set()
        self.Library = Library
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "communities"):
                opp_val = getattr(old_value, "communities", None)
                if opp_val == self:
                    setattr(old_value, "communities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "communities"):
                opp_val = getattr(value, "communities", None)
                setattr(value, "communities", self)

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library", None)
        self.__library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Community"):
                    opp_val = getattr(item, "Community", None)
                    
                    if opp_val == self:
                        setattr(item, "Community", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Community"):
                    opp_val = getattr(item, "Community", None)
                    
                    setattr(item, "Community", self)
                    

    @property
    def library_Library2(self):
        return self.__library_Library2

    @library_Library2.setter
    def library_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library2", None)
        self.__library_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book"):
                    opp_val = getattr(item, "library_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book"):
                    opp_val = getattr(item, "library_Book", None)
                    
                    setattr(item, "library_Book", self)
                    

    @property
    def library_Library(self):
        return self.__library_Library

    @library_Library.setter
    def library_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library", None)
        self.__library_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Writer"):
                    opp_val = getattr(item, "library_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Writer"):
                    opp_val = getattr(item, "library_Writer", None)
                    
                    setattr(item, "library_Writer", self)
                    
