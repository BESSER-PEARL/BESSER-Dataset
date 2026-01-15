from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class GenreTypes(Enum):
    Comedy = "Comedy"
    Documentary = "Documentary"
    Drama = "Drama"
    Horror = "Horror"
    Romance = "Romance"
    SciFi = "SciFi"
    Thriller = "Thriller"
    NewRelease = "NewRelease"
    Action = "Action"
    Animation = "Animation"
    Family = "Family"
    Classics = "Classics"


############################################
# Definition of Classes
############################################

class movies_Place:

    def __init__(self, id: str, name: str, movies_Place9: "movies_Copy" = None, movies_Place: "movies_MoviesDB" = None):
        self.id = id
        self.name = name
        self.movies_Place9 = movies_Place9
        self.movies_Place = movies_Place
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def movies_Place(self):
        return self.__movies_Place

    @movies_Place.setter
    def movies_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_movies_Place__movies_Place", None)
        self.__movies_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "movies_MoviesDB6"):
                opp_val = getattr(old_value, "movies_MoviesDB6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "movies_MoviesDB6"):
                opp_val = getattr(value, "movies_MoviesDB6", None)
                if opp_val is None:
                    setattr(value, "movies_MoviesDB6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def movies_Place9(self):
        return self.__movies_Place9

    @movies_Place9.setter
    def movies_Place9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_movies_Place__movies_Place9", None)
        self.__movies_Place9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "movies_Copy8"):
                opp_val = getattr(old_value, "movies_Copy8", None)
                if opp_val == self:
                    setattr(old_value, "movies_Copy8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "movies_Copy8"):
                opp_val = getattr(value, "movies_Copy8", None)
                setattr(value, "movies_Copy8", self)

class movies_MoviesDB:

    def __init__(self, comment: str, movies_MoviesDB: set["movies_Movie"] = None, movies_MoviesDB6: set["movies_Place"] = None):
        self.comment = comment
        self.movies_MoviesDB = movies_MoviesDB if movies_MoviesDB is not None else set()
        self.movies_MoviesDB6 = movies_MoviesDB6 if movies_MoviesDB6 is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def movies_MoviesDB(self):
        return self.__movies_MoviesDB

    @movies_MoviesDB.setter
    def movies_MoviesDB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_movies_MoviesDB__movies_MoviesDB", None)
        self.__movies_MoviesDB = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "movies_Movie4"):
                    opp_val = getattr(item, "movies_Movie4", None)
                    
                    if opp_val == self:
                        setattr(item, "movies_Movie4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "movies_Movie4"):
                    opp_val = getattr(item, "movies_Movie4", None)
                    
                    setattr(item, "movies_Movie4", self)
                    

    @property
    def movies_MoviesDB6(self):
        return self.__movies_MoviesDB6

    @movies_MoviesDB6.setter
    def movies_MoviesDB6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_movies_MoviesDB__movies_MoviesDB6", None)
        self.__movies_MoviesDB6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "movies_Place"):
                    opp_val = getattr(item, "movies_Place", None)
                    
                    if opp_val == self:
                        setattr(item, "movies_Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "movies_Place"):
                    opp_val = getattr(item, "movies_Place", None)
                    
                    setattr(item, "movies_Place", self)
                    

class CriticsReview:

    pass
class movies_CustomerReview(CriticsReview):

    def __init__(self, comment: str):
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

class movies_CriticsReview:

    def __init__(self, rating: str, reviewedBy: str, movies_CriticsReview: "movies_Movie" = None):
        self.rating = rating
        self.reviewedBy = reviewedBy
        self.movies_CriticsReview = movies_CriticsReview
        
    @property
    def reviewedBy(self) -> str:
        return self.__reviewedBy

    @reviewedBy.setter
    def reviewedBy(self, reviewedBy: str):
        self.__reviewedBy = reviewedBy

    @property
    def rating(self) -> str:
        return self.__rating

    @rating.setter
    def rating(self, rating: str):
        self.__rating = rating

    @property
    def movies_CriticsReview(self):
        return self.__movies_CriticsReview

    @movies_CriticsReview.setter
    def movies_CriticsReview(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_movies_CriticsReview__movies_CriticsReview", None)
        self.__movies_CriticsReview = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "movies_Movie2"):
                opp_val = getattr(old_value, "movies_Movie2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "movies_Movie2"):
                opp_val = getattr(value, "movies_Movie2", None)
                if opp_val is None:
                    setattr(value, "movies_Movie2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class movies_Copy:

    def __init__(self, id: str, movies_Copy: "movies_Movie" = None, movies_Copy8: "movies_Place" = None):
        self.id = id
        self.movies_Copy = movies_Copy
        self.movies_Copy8 = movies_Copy8
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def movies_Copy8(self):
        return self.__movies_Copy8

    @movies_Copy8.setter
    def movies_Copy8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_movies_Copy__movies_Copy8", None)
        self.__movies_Copy8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "movies_Place9"):
                opp_val = getattr(old_value, "movies_Place9", None)
                if opp_val == self:
                    setattr(old_value, "movies_Place9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "movies_Place9"):
                opp_val = getattr(value, "movies_Place9", None)
                setattr(value, "movies_Place9", self)

    @property
    def movies_Copy(self):
        return self.__movies_Copy

    @movies_Copy.setter
    def movies_Copy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_movies_Copy__movies_Copy", None)
        self.__movies_Copy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "movies_Movie"):
                opp_val = getattr(old_value, "movies_Movie", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "movies_Movie"):
                opp_val = getattr(value, "movies_Movie", None)
                if opp_val is None:
                    setattr(value, "movies_Movie", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class movies_Movie:

    def __init__(self, actors: str, title: str, director: str, genre: str, summary: str, movies_Movie: set["movies_Copy"] = None, movies_Movie2: set["movies_CriticsReview"] = None, movies_Movie4: "movies_MoviesDB" = None):
        self.actors = actors
        self.title = title
        self.director = director
        self.genre = genre
        self.summary = summary
        self.movies_Movie = movies_Movie if movies_Movie is not None else set()
        self.movies_Movie2 = movies_Movie2 if movies_Movie2 is not None else set()
        self.movies_Movie4 = movies_Movie4
        
    @property
    def actors(self) -> str:
        return self.__actors

    @actors.setter
    def actors(self, actors: str):
        self.__actors = actors

    @property
    def summary(self) -> str:
        return self.__summary

    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary

    @property
    def genre(self) -> str:
        return self.__genre

    @genre.setter
    def genre(self, genre: str):
        self.__genre = genre

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def director(self) -> str:
        return self.__director

    @director.setter
    def director(self, director: str):
        self.__director = director

    @property
    def movies_Movie(self):
        return self.__movies_Movie

    @movies_Movie.setter
    def movies_Movie(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_movies_Movie__movies_Movie", None)
        self.__movies_Movie = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "movies_Copy"):
                    opp_val = getattr(item, "movies_Copy", None)
                    
                    if opp_val == self:
                        setattr(item, "movies_Copy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "movies_Copy"):
                    opp_val = getattr(item, "movies_Copy", None)
                    
                    setattr(item, "movies_Copy", self)
                    

    @property
    def movies_Movie4(self):
        return self.__movies_Movie4

    @movies_Movie4.setter
    def movies_Movie4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_movies_Movie__movies_Movie4", None)
        self.__movies_Movie4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "movies_MoviesDB"):
                opp_val = getattr(old_value, "movies_MoviesDB", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "movies_MoviesDB"):
                opp_val = getattr(value, "movies_MoviesDB", None)
                if opp_val is None:
                    setattr(value, "movies_MoviesDB", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def movies_Movie2(self):
        return self.__movies_Movie2

    @movies_Movie2.setter
    def movies_Movie2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_movies_Movie__movies_Movie2", None)
        self.__movies_Movie2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "movies_CriticsReview"):
                    opp_val = getattr(item, "movies_CriticsReview", None)
                    
                    if opp_val == self:
                        setattr(item, "movies_CriticsReview", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "movies_CriticsReview"):
                    opp_val = getattr(item, "movies_CriticsReview", None)
                    
                    setattr(item, "movies_CriticsReview", self)
                    
