from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Genre(Enum):
    Adventure = "Adventure"
    SciFi = "SciFi"
class StaffListType(Enum):
    titles = "titles"
    characters = "characters"


############################################
# Definition of Classes
############################################

class imdb_User:

    def __init__(self, username: str, watchlist: str, imdb_User: "imdb_db" = None, imdb_User24: "imdb_StaffList" = None):
        self.username = username
        self.watchlist = watchlist
        self.imdb_User = imdb_User
        self.imdb_User24 = imdb_User24
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def watchlist(self) -> str:
        return self.__watchlist

    @watchlist.setter
    def watchlist(self, watchlist: str):
        self.__watchlist = watchlist

    @property
    def imdb_User(self):
        return self.__imdb_User

    @imdb_User.setter
    def imdb_User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_User__imdb_User", None)
        self.__imdb_User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_db21"):
                opp_val = getattr(old_value, "imdb_db21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_db21"):
                opp_val = getattr(value, "imdb_db21", None)
                if opp_val is None:
                    setattr(value, "imdb_db21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imdb_User24(self):
        return self.__imdb_User24

    @imdb_User24.setter
    def imdb_User24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_User__imdb_User24", None)
        self.__imdb_User24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_StaffList23"):
                opp_val = getattr(old_value, "imdb_StaffList23", None)
                if opp_val == self:
                    setattr(old_value, "imdb_StaffList23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_StaffList23"):
                opp_val = getattr(value, "imdb_StaffList23", None)
                setattr(value, "imdb_StaffList23", self)

class imdb_StaffList:

    def __init__(self, coverPhoto: str, name: str, elements: str, elementType: str, createdDate: date, imdb_StaffList: "imdb_db" = None, imdb_StaffList23: "imdb_User" = None):
        self.coverPhoto = coverPhoto
        self.name = name
        self.elements = elements
        self.elementType = elementType
        self.createdDate = createdDate
        self.imdb_StaffList = imdb_StaffList
        self.imdb_StaffList23 = imdb_StaffList23
        
    @property
    def elementType(self) -> str:
        return self.__elementType

    @elementType.setter
    def elementType(self, elementType: str):
        self.__elementType = elementType

    @property
    def coverPhoto(self) -> str:
        return self.__coverPhoto

    @coverPhoto.setter
    def coverPhoto(self, coverPhoto: str):
        self.__coverPhoto = coverPhoto

    @property
    def elements(self) -> str:
        return self.__elements

    @elements.setter
    def elements(self, elements: str):
        self.__elements = elements

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def createdDate(self) -> date:
        return self.__createdDate

    @createdDate.setter
    def createdDate(self, createdDate: date):
        self.__createdDate = createdDate

    @property
    def imdb_StaffList(self):
        return self.__imdb_StaffList

    @imdb_StaffList.setter
    def imdb_StaffList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_StaffList__imdb_StaffList", None)
        self.__imdb_StaffList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_db19"):
                opp_val = getattr(old_value, "imdb_db19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_db19"):
                opp_val = getattr(value, "imdb_db19", None)
                if opp_val is None:
                    setattr(value, "imdb_db19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imdb_StaffList23(self):
        return self.__imdb_StaffList23

    @imdb_StaffList23.setter
    def imdb_StaffList23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_StaffList__imdb_StaffList23", None)
        self.__imdb_StaffList23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_User24"):
                opp_val = getattr(old_value, "imdb_User24", None)
                if opp_val == self:
                    setattr(old_value, "imdb_User24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_User24"):
                opp_val = getattr(value, "imdb_User24", None)
                setattr(value, "imdb_User24", self)

class imdb_Movie:

    def __init__(self, age: int, title: str, releaseDate: date, runtime: int, poster: str, rating: float, userReviews: int, criticReviews: int, userRatings: int, synopsis: str, metaScore: int, metacriticReviews: int, genres: str, imdb_Movie17: "imdb_db" = None, imdb_Movie: "imdb_Person" = None, imdb_Movie2: set["imdb_Person"] = None, imdb_Movie5: set["imdb_Person"] = None):
        self.age = age
        self.title = title
        self.releaseDate = releaseDate
        self.runtime = runtime
        self.poster = poster
        self.rating = rating
        self.userReviews = userReviews
        self.criticReviews = criticReviews
        self.userRatings = userRatings
        self.synopsis = synopsis
        self.metaScore = metaScore
        self.metacriticReviews = metacriticReviews
        self.genres = genres
        self.imdb_Movie17 = imdb_Movie17
        self.imdb_Movie = imdb_Movie
        self.imdb_Movie2 = imdb_Movie2 if imdb_Movie2 is not None else set()
        self.imdb_Movie5 = imdb_Movie5 if imdb_Movie5 is not None else set()
        
    @property
    def runtime(self) -> int:
        return self.__runtime

    @runtime.setter
    def runtime(self, runtime: int):
        self.__runtime = runtime

    @property
    def releaseDate(self) -> date:
        return self.__releaseDate

    @releaseDate.setter
    def releaseDate(self, releaseDate: date):
        self.__releaseDate = releaseDate

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def criticReviews(self) -> int:
        return self.__criticReviews

    @criticReviews.setter
    def criticReviews(self, criticReviews: int):
        self.__criticReviews = criticReviews

    @property
    def userRatings(self) -> int:
        return self.__userRatings

    @userRatings.setter
    def userRatings(self, userRatings: int):
        self.__userRatings = userRatings

    @property
    def rating(self) -> float:
        return self.__rating

    @rating.setter
    def rating(self, rating: float):
        self.__rating = rating

    @property
    def userReviews(self) -> int:
        return self.__userReviews

    @userReviews.setter
    def userReviews(self, userReviews: int):
        self.__userReviews = userReviews

    @property
    def genres(self) -> str:
        return self.__genres

    @genres.setter
    def genres(self, genres: str):
        self.__genres = genres

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def synopsis(self) -> str:
        return self.__synopsis

    @synopsis.setter
    def synopsis(self, synopsis: str):
        self.__synopsis = synopsis

    @property
    def metaScore(self) -> int:
        return self.__metaScore

    @metaScore.setter
    def metaScore(self, metaScore: int):
        self.__metaScore = metaScore

    @property
    def poster(self) -> str:
        return self.__poster

    @poster.setter
    def poster(self, poster: str):
        self.__poster = poster

    @property
    def metacriticReviews(self) -> int:
        return self.__metacriticReviews

    @metacriticReviews.setter
    def metacriticReviews(self, metacriticReviews: int):
        self.__metacriticReviews = metacriticReviews

    @property
    def imdb_Movie2(self):
        return self.__imdb_Movie2

    @imdb_Movie2.setter
    def imdb_Movie2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_Movie__imdb_Movie2", None)
        self.__imdb_Movie2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imdb_Person3"):
                    opp_val = getattr(item, "imdb_Person3", None)
                    
                    if opp_val == self:
                        setattr(item, "imdb_Person3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imdb_Person3"):
                    opp_val = getattr(item, "imdb_Person3", None)
                    
                    setattr(item, "imdb_Person3", self)
                    

    @property
    def imdb_Movie(self):
        return self.__imdb_Movie

    @imdb_Movie.setter
    def imdb_Movie(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_Movie__imdb_Movie", None)
        self.__imdb_Movie = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_Person"):
                opp_val = getattr(old_value, "imdb_Person", None)
                if opp_val == self:
                    setattr(old_value, "imdb_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_Person"):
                opp_val = getattr(value, "imdb_Person", None)
                setattr(value, "imdb_Person", self)

    @property
    def imdb_Movie17(self):
        return self.__imdb_Movie17

    @imdb_Movie17.setter
    def imdb_Movie17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_Movie__imdb_Movie17", None)
        self.__imdb_Movie17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_db16"):
                opp_val = getattr(old_value, "imdb_db16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_db16"):
                opp_val = getattr(value, "imdb_db16", None)
                if opp_val is None:
                    setattr(value, "imdb_db16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imdb_Movie5(self):
        return self.__imdb_Movie5

    @imdb_Movie5.setter
    def imdb_Movie5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_Movie__imdb_Movie5", None)
        self.__imdb_Movie5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imdb_Person6"):
                    opp_val = getattr(item, "imdb_Person6", None)
                    
                    if opp_val == self:
                        setattr(item, "imdb_Person6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imdb_Person6"):
                    opp_val = getattr(item, "imdb_Person6", None)
                    
                    setattr(item, "imdb_Person6", self)
                    

class imdb_Person:

    def __init__(self, name: str, imdb_Person8: "imdb_db" = None, imdb_Person11: "imdb_db" = None, imdb_Person14: "imdb_db" = None, imdb_Person: "imdb_Movie" = None, imdb_Person3: "imdb_Movie" = None, imdb_Person6: "imdb_Movie" = None):
        self.name = name
        self.imdb_Person8 = imdb_Person8
        self.imdb_Person11 = imdb_Person11
        self.imdb_Person14 = imdb_Person14
        self.imdb_Person = imdb_Person
        self.imdb_Person3 = imdb_Person3
        self.imdb_Person6 = imdb_Person6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def imdb_Person6(self):
        return self.__imdb_Person6

    @imdb_Person6.setter
    def imdb_Person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_Person__imdb_Person6", None)
        self.__imdb_Person6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_Movie5"):
                opp_val = getattr(old_value, "imdb_Movie5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_Movie5"):
                opp_val = getattr(value, "imdb_Movie5", None)
                if opp_val is None:
                    setattr(value, "imdb_Movie5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imdb_Person(self):
        return self.__imdb_Person

    @imdb_Person.setter
    def imdb_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_Person__imdb_Person", None)
        self.__imdb_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_Movie"):
                opp_val = getattr(old_value, "imdb_Movie", None)
                if opp_val == self:
                    setattr(old_value, "imdb_Movie", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_Movie"):
                opp_val = getattr(value, "imdb_Movie", None)
                setattr(value, "imdb_Movie", self)

    @property
    def imdb_Person14(self):
        return self.__imdb_Person14

    @imdb_Person14.setter
    def imdb_Person14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_Person__imdb_Person14", None)
        self.__imdb_Person14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_db13"):
                opp_val = getattr(old_value, "imdb_db13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_db13"):
                opp_val = getattr(value, "imdb_db13", None)
                if opp_val is None:
                    setattr(value, "imdb_db13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imdb_Person11(self):
        return self.__imdb_Person11

    @imdb_Person11.setter
    def imdb_Person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_Person__imdb_Person11", None)
        self.__imdb_Person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_db10"):
                opp_val = getattr(old_value, "imdb_db10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_db10"):
                opp_val = getattr(value, "imdb_db10", None)
                if opp_val is None:
                    setattr(value, "imdb_db10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imdb_Person8(self):
        return self.__imdb_Person8

    @imdb_Person8.setter
    def imdb_Person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_Person__imdb_Person8", None)
        self.__imdb_Person8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_db"):
                opp_val = getattr(old_value, "imdb_db", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_db"):
                opp_val = getattr(value, "imdb_db", None)
                if opp_val is None:
                    setattr(value, "imdb_db", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def imdb_Person3(self):
        return self.__imdb_Person3

    @imdb_Person3.setter
    def imdb_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_Person__imdb_Person3", None)
        self.__imdb_Person3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "imdb_Movie2"):
                opp_val = getattr(old_value, "imdb_Movie2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "imdb_Movie2"):
                opp_val = getattr(value, "imdb_Movie2", None)
                if opp_val is None:
                    setattr(value, "imdb_Movie2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class imdb_db:

    def __init__(self, bestOf2014: str, imdb_db: set["imdb_Person"] = None, imdb_db10: set["imdb_Person"] = None, imdb_db13: set["imdb_Person"] = None, imdb_db16: set["imdb_Movie"] = None, imdb_db19: set["imdb_StaffList"] = None, imdb_db21: set["imdb_User"] = None):
        self.bestOf2014 = bestOf2014
        self.imdb_db = imdb_db if imdb_db is not None else set()
        self.imdb_db10 = imdb_db10 if imdb_db10 is not None else set()
        self.imdb_db13 = imdb_db13 if imdb_db13 is not None else set()
        self.imdb_db16 = imdb_db16 if imdb_db16 is not None else set()
        self.imdb_db19 = imdb_db19 if imdb_db19 is not None else set()
        self.imdb_db21 = imdb_db21 if imdb_db21 is not None else set()
        
    @property
    def bestOf2014(self) -> str:
        return self.__bestOf2014

    @bestOf2014.setter
    def bestOf2014(self, bestOf2014: str):
        self.__bestOf2014 = bestOf2014

    @property
    def imdb_db21(self):
        return self.__imdb_db21

    @imdb_db21.setter
    def imdb_db21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_db__imdb_db21", None)
        self.__imdb_db21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imdb_User"):
                    opp_val = getattr(item, "imdb_User", None)
                    
                    if opp_val == self:
                        setattr(item, "imdb_User", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imdb_User"):
                    opp_val = getattr(item, "imdb_User", None)
                    
                    setattr(item, "imdb_User", self)
                    

    @property
    def imdb_db10(self):
        return self.__imdb_db10

    @imdb_db10.setter
    def imdb_db10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_db__imdb_db10", None)
        self.__imdb_db10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imdb_Person11"):
                    opp_val = getattr(item, "imdb_Person11", None)
                    
                    if opp_val == self:
                        setattr(item, "imdb_Person11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imdb_Person11"):
                    opp_val = getattr(item, "imdb_Person11", None)
                    
                    setattr(item, "imdb_Person11", self)
                    

    @property
    def imdb_db19(self):
        return self.__imdb_db19

    @imdb_db19.setter
    def imdb_db19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_db__imdb_db19", None)
        self.__imdb_db19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imdb_StaffList"):
                    opp_val = getattr(item, "imdb_StaffList", None)
                    
                    if opp_val == self:
                        setattr(item, "imdb_StaffList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imdb_StaffList"):
                    opp_val = getattr(item, "imdb_StaffList", None)
                    
                    setattr(item, "imdb_StaffList", self)
                    

    @property
    def imdb_db(self):
        return self.__imdb_db

    @imdb_db.setter
    def imdb_db(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_db__imdb_db", None)
        self.__imdb_db = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imdb_Person8"):
                    opp_val = getattr(item, "imdb_Person8", None)
                    
                    if opp_val == self:
                        setattr(item, "imdb_Person8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imdb_Person8"):
                    opp_val = getattr(item, "imdb_Person8", None)
                    
                    setattr(item, "imdb_Person8", self)
                    

    @property
    def imdb_db16(self):
        return self.__imdb_db16

    @imdb_db16.setter
    def imdb_db16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_db__imdb_db16", None)
        self.__imdb_db16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imdb_Movie17"):
                    opp_val = getattr(item, "imdb_Movie17", None)
                    
                    if opp_val == self:
                        setattr(item, "imdb_Movie17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imdb_Movie17"):
                    opp_val = getattr(item, "imdb_Movie17", None)
                    
                    setattr(item, "imdb_Movie17", self)
                    

    @property
    def imdb_db13(self):
        return self.__imdb_db13

    @imdb_db13.setter
    def imdb_db13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_imdb_db__imdb_db13", None)
        self.__imdb_db13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "imdb_Person14"):
                    opp_val = getattr(item, "imdb_Person14", None)
                    
                    if opp_val == self:
                        setattr(item, "imdb_Person14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "imdb_Person14"):
                    opp_val = getattr(item, "imdb_Person14", None)
                    
                    setattr(item, "imdb_Person14", self)
                    

    def sam(self) -> str:
        # TODO: Implement sam method
        pass
