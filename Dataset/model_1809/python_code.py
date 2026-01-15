from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class sistedesMM_SistedesMember(Person):

    pass
class sistedesMM_Publisher:

    def __init__(self, name: str, address: str, sistedesMM_Publisher: "sistedesMM_InProceedings" = None, sistedesMM_Publisher9: "sistedesMM_Book" = None):
        self.name = name
        self.address = address
        self.sistedesMM_Publisher = sistedesMM_Publisher
        self.sistedesMM_Publisher9 = sistedesMM_Publisher9
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sistedesMM_Publisher(self):
        return self.__sistedesMM_Publisher

    @sistedesMM_Publisher.setter
    def sistedesMM_Publisher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Publisher__sistedesMM_Publisher", None)
        self.__sistedesMM_Publisher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistedesMM_InProceedings"):
                opp_val = getattr(old_value, "sistedesMM_InProceedings", None)
                if opp_val == self:
                    setattr(old_value, "sistedesMM_InProceedings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistedesMM_InProceedings"):
                opp_val = getattr(value, "sistedesMM_InProceedings", None)
                setattr(value, "sistedesMM_InProceedings", self)

    @property
    def sistedesMM_Publisher9(self):
        return self.__sistedesMM_Publisher9

    @sistedesMM_Publisher9.setter
    def sistedesMM_Publisher9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Publisher__sistedesMM_Publisher9", None)
        self.__sistedesMM_Publisher9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistedesMM_Book"):
                opp_val = getattr(old_value, "sistedesMM_Book", None)
                if opp_val == self:
                    setattr(old_value, "sistedesMM_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistedesMM_Book"):
                opp_val = getattr(value, "sistedesMM_Book", None)
                setattr(value, "sistedesMM_Book", self)

class sistedesMM_Journal:

    def __init__(self, name: str, jcrIndexed: bool, acronym: str, Journal: "sistedesMM_Article" = None, journal: "sistedesMM_Article" = None):
        self.name = name
        self.jcrIndexed = jcrIndexed
        self.acronym = acronym
        self.Journal = Journal
        self.journal = journal
        
    @property
    def jcrIndexed(self) -> bool:
        return self.__jcrIndexed

    @jcrIndexed.setter
    def jcrIndexed(self, jcrIndexed: bool):
        self.__jcrIndexed = jcrIndexed

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def acronym(self) -> str:
        return self.__acronym

    @acronym.setter
    def acronym(self, acronym: str):
        self.__acronym = acronym

    @property
    def Journal(self):
        return self.__Journal

    @Journal.setter
    def Journal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Journal__Journal", None)
        self.__Journal = value
        
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
    def journal(self):
        return self.__journal

    @journal.setter
    def journal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Journal__journal", None)
        self.__journal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Article"):
                opp_val = getattr(old_value, "Article", None)
                if opp_val == self:
                    setattr(old_value, "Article", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Article"):
                opp_val = getattr(value, "Article", None)
                setattr(value, "Article", self)

class sistedesMM_Editor:

    def __init__(self, name: str, sistedesMM_Editor: "sistedesMM_InProceedings" = None):
        self.name = name
        self.sistedesMM_Editor = sistedesMM_Editor
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sistedesMM_Editor(self):
        return self.__sistedesMM_Editor

    @sistedesMM_Editor.setter
    def sistedesMM_Editor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Editor__sistedesMM_Editor", None)
        self.__sistedesMM_Editor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistedesMM_InProceedings6"):
                opp_val = getattr(old_value, "sistedesMM_InProceedings6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistedesMM_InProceedings6"):
                opp_val = getattr(value, "sistedesMM_InProceedings6", None)
                if opp_val is None:
                    setattr(value, "sistedesMM_InProceedings6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sistedesMM_Edition:

    def __init__(self, year: int, location: str, sistedesMM_Edition: "sistedesMM_SistedesMember" = None):
        self.year = year
        self.location = location
        self.sistedesMM_Edition = sistedesMM_Edition
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def sistedesMM_Edition(self):
        return self.__sistedesMM_Edition

    @sistedesMM_Edition.setter
    def sistedesMM_Edition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Edition__sistedesMM_Edition", None)
        self.__sistedesMM_Edition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistedesMM_SistedesMember"):
                opp_val = getattr(old_value, "sistedesMM_SistedesMember", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistedesMM_SistedesMember"):
                opp_val = getattr(value, "sistedesMM_SistedesMember", None)
                if opp_val is None:
                    setattr(value, "sistedesMM_SistedesMember", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sistedesMM_Publication(ABC):

    pass
class sistedesMM_University:

    def __init__(self, name: str, city: str, provinceOrState: str, country: str, sistedesMM_University: "sistedesMM_Person" = None):
        self.name = name
        self.city = city
        self.provinceOrState = provinceOrState
        self.country = country
        self.sistedesMM_University = sistedesMM_University
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def provinceOrState(self) -> str:
        return self.__provinceOrState

    @provinceOrState.setter
    def provinceOrState(self, provinceOrState: str):
        self.__provinceOrState = provinceOrState

    @property
    def sistedesMM_University(self):
        return self.__sistedesMM_University

    @sistedesMM_University.setter
    def sistedesMM_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_University__sistedesMM_University", None)
        self.__sistedesMM_University = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistedesMM_Person"):
                opp_val = getattr(old_value, "sistedesMM_Person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistedesMM_Person"):
                opp_val = getattr(value, "sistedesMM_Person", None)
                if opp_val is None:
                    setattr(value, "sistedesMM_Person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Publication:

    pass
class sistedesMM_InProceedings(Publication):

    def __init__(self, title: str, bookTitle: str, year: int, fromPage: str, toPage: str, month: str, sistedesMM_InProceedings6: set["sistedesMM_Editor"] = None, sistedesMM_InProceedings: "sistedesMM_Publisher" = None):
        self.title = title
        self.bookTitle = bookTitle
        self.year = year
        self.fromPage = fromPage
        self.toPage = toPage
        self.month = month
        self.sistedesMM_InProceedings6 = sistedesMM_InProceedings6 if sistedesMM_InProceedings6 is not None else set()
        self.sistedesMM_InProceedings = sistedesMM_InProceedings
        
    @property
    def toPage(self) -> str:
        return self.__toPage

    @toPage.setter
    def toPage(self, toPage: str):
        self.__toPage = toPage

    @property
    def bookTitle(self) -> str:
        return self.__bookTitle

    @bookTitle.setter
    def bookTitle(self, bookTitle: str):
        self.__bookTitle = bookTitle

    @property
    def fromPage(self) -> str:
        return self.__fromPage

    @fromPage.setter
    def fromPage(self, fromPage: str):
        self.__fromPage = fromPage

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def sistedesMM_InProceedings6(self):
        return self.__sistedesMM_InProceedings6

    @sistedesMM_InProceedings6.setter
    def sistedesMM_InProceedings6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_InProceedings__sistedesMM_InProceedings6", None)
        self.__sistedesMM_InProceedings6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sistedesMM_Editor"):
                    opp_val = getattr(item, "sistedesMM_Editor", None)
                    
                    if opp_val == self:
                        setattr(item, "sistedesMM_Editor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sistedesMM_Editor"):
                    opp_val = getattr(item, "sistedesMM_Editor", None)
                    
                    setattr(item, "sistedesMM_Editor", self)
                    

    @property
    def sistedesMM_InProceedings(self):
        return self.__sistedesMM_InProceedings

    @sistedesMM_InProceedings.setter
    def sistedesMM_InProceedings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_InProceedings__sistedesMM_InProceedings", None)
        self.__sistedesMM_InProceedings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistedesMM_Publisher"):
                opp_val = getattr(old_value, "sistedesMM_Publisher", None)
                if opp_val == self:
                    setattr(old_value, "sistedesMM_Publisher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistedesMM_Publisher"):
                opp_val = getattr(value, "sistedesMM_Publisher", None)
                setattr(value, "sistedesMM_Publisher", self)

class sistedesMM_Book(Publication):

    def __init__(self, title: str, year: int, month: str, volume: str, series: str, edition: int, isbn: str, sistedesMM_Book: "sistedesMM_Publisher" = None):
        self.title = title
        self.year = year
        self.month = month
        self.volume = volume
        self.series = series
        self.edition = edition
        self.isbn = isbn
        self.sistedesMM_Book = sistedesMM_Book
        
    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def edition(self) -> int:
        return self.__edition

    @edition.setter
    def edition(self, edition: int):
        self.__edition = edition

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def series(self) -> str:
        return self.__series

    @series.setter
    def series(self, series: str):
        self.__series = series

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def sistedesMM_Book(self):
        return self.__sistedesMM_Book

    @sistedesMM_Book.setter
    def sistedesMM_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Book__sistedesMM_Book", None)
        self.__sistedesMM_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistedesMM_Publisher9"):
                opp_val = getattr(old_value, "sistedesMM_Publisher9", None)
                if opp_val == self:
                    setattr(old_value, "sistedesMM_Publisher9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistedesMM_Publisher9"):
                opp_val = getattr(value, "sistedesMM_Publisher9", None)
                setattr(value, "sistedesMM_Publisher9", self)

class sistedesMM_Article(Publication):

    def __init__(self, title: str, fromPage: int, toPage: int, number: int, volume: str, month: str, year: int, articles: "sistedesMM_Journal" = None, Article: "sistedesMM_Journal" = None):
        self.title = title
        self.fromPage = fromPage
        self.toPage = toPage
        self.number = number
        self.volume = volume
        self.month = month
        self.year = year
        self.articles = articles
        self.Article = Article
        
    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def toPage(self) -> int:
        return self.__toPage

    @toPage.setter
    def toPage(self, toPage: int):
        self.__toPage = toPage

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def fromPage(self) -> int:
        return self.__fromPage

    @fromPage.setter
    def fromPage(self, fromPage: int):
        self.__fromPage = fromPage

    @property
    def volume(self) -> str:
        return self.__volume

    @volume.setter
    def volume(self, volume: str):
        self.__volume = volume

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Article(self):
        return self.__Article

    @Article.setter
    def Article(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Article__Article", None)
        self.__Article = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "journal"):
                opp_val = getattr(old_value, "journal", None)
                if opp_val == self:
                    setattr(old_value, "journal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "journal"):
                opp_val = getattr(value, "journal", None)
                setattr(value, "journal", self)

    @property
    def articles(self):
        return self.__articles

    @articles.setter
    def articles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Article__articles", None)
        self.__articles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Journal"):
                opp_val = getattr(old_value, "Journal", None)
                if opp_val == self:
                    setattr(old_value, "Journal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Journal"):
                opp_val = getattr(value, "Journal", None)
                setattr(value, "Journal", self)

class sistedesMM_Person:

    def __init__(self, name: str, surname: str, email: str, nationality: str, Person: "sistedesMM_Publication" = None, sistedesMM_Person: set["sistedesMM_University"] = None, authors: set["sistedesMM_Publication"] = None):
        self.name = name
        self.surname = surname
        self.email = email
        self.nationality = nationality
        self.Person = Person
        self.sistedesMM_Person = sistedesMM_Person if sistedesMM_Person is not None else set()
        self.authors = authors if authors is not None else set()
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nationality(self) -> str:
        return self.__nationality

    @nationality.setter
    def nationality(self, nationality: str):
        self.__nationality = nationality

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "publications"):
                opp_val = getattr(old_value, "publications", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "publications"):
                opp_val = getattr(value, "publications", None)
                if opp_val is None:
                    setattr(value, "publications", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sistedesMM_Person(self):
        return self.__sistedesMM_Person

    @sistedesMM_Person.setter
    def sistedesMM_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Person__sistedesMM_Person", None)
        self.__sistedesMM_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sistedesMM_University"):
                    opp_val = getattr(item, "sistedesMM_University", None)
                    
                    if opp_val == self:
                        setattr(item, "sistedesMM_University", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sistedesMM_University"):
                    opp_val = getattr(item, "sistedesMM_University", None)
                    
                    setattr(item, "sistedesMM_University", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistedesMM_Person__authors", None)
        self.__authors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Publication"):
                    opp_val = getattr(item, "Publication", None)
                    
                    if opp_val == self:
                        setattr(item, "Publication", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Publication"):
                    opp_val = getattr(item, "Publication", None)
                    
                    setattr(item, "Publication", self)
                    
