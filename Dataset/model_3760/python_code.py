from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class GenreTypes(Enum):
    NewRelease = "NewRelease"
    Action = "Action"
    Animation = "Animation"
    Family = "Family"
    Classics = "Classics"
    Comedy = "Comedy"
    Documentary = "Documentary"
    Drama = "Drama"
    Horror = "Horror"
    Romance = "Romance"
    SciFi = "SciFi"
    Thriller = "Thriller"


############################################
# Definition of Classes
############################################

class db_MovieType:

    def __init__(self, title: str, actors: str, director: str, genre: str, summary: str, criticsReviewGroup: str, any: str, iD: str, db_MovieType: "db_MovieDBType" = None, db_MovieType18: "db_CustomerType" = None, db_MovieType15: set["db_CriticsReviewType"] = None):
        self.title = title
        self.actors = actors
        self.director = director
        self.genre = genre
        self.summary = summary
        self.criticsReviewGroup = criticsReviewGroup
        self.any = any
        self.iD = iD
        self.db_MovieType = db_MovieType
        self.db_MovieType18 = db_MovieType18
        self.db_MovieType15 = db_MovieType15 if db_MovieType15 is not None else set()
        
    @property
    def director(self) -> str:
        return self.__director

    @director.setter
    def director(self, director: str):
        self.__director = director

    @property
    def summary(self) -> str:
        return self.__summary

    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def criticsReviewGroup(self) -> str:
        return self.__criticsReviewGroup

    @criticsReviewGroup.setter
    def criticsReviewGroup(self, criticsReviewGroup: str):
        self.__criticsReviewGroup = criticsReviewGroup

    @property
    def actors(self) -> str:
        return self.__actors

    @actors.setter
    def actors(self, actors: str):
        self.__actors = actors

    @property
    def iD(self) -> str:
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD

    @property
    def genre(self) -> str:
        return self.__genre

    @genre.setter
    def genre(self, genre: str):
        self.__genre = genre

    @property
    def db_MovieType15(self):
        return self.__db_MovieType15

    @db_MovieType15.setter
    def db_MovieType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_MovieType__db_MovieType15", None)
        self.__db_MovieType15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "db_CriticsReviewType16"):
                    opp_val = getattr(item, "db_CriticsReviewType16", None)
                    
                    if opp_val == self:
                        setattr(item, "db_CriticsReviewType16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "db_CriticsReviewType16"):
                    opp_val = getattr(item, "db_CriticsReviewType16", None)
                    
                    setattr(item, "db_CriticsReviewType16", self)
                    

    @property
    def db_MovieType18(self):
        return self.__db_MovieType18

    @db_MovieType18.setter
    def db_MovieType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_MovieType__db_MovieType18", None)
        self.__db_MovieType18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_CustomerType19"):
                opp_val = getattr(old_value, "db_CustomerType19", None)
                if opp_val == self:
                    setattr(old_value, "db_CustomerType19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_CustomerType19"):
                opp_val = getattr(value, "db_CustomerType19", None)
                setattr(value, "db_CustomerType19", self)

    @property
    def db_MovieType(self):
        return self.__db_MovieType

    @db_MovieType.setter
    def db_MovieType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_MovieType__db_MovieType", None)
        self.__db_MovieType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_MovieDBType13"):
                opp_val = getattr(old_value, "db_MovieDBType13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_MovieDBType13"):
                opp_val = getattr(value, "db_MovieDBType13", None)
                if opp_val is None:
                    setattr(value, "db_MovieDBType13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class db_MovieDBType:

    def __init__(self, movieDBFeatureMap: str, comment: str, db_MovieDBType: "db_DocumentRoot" = None, db_MovieDBType13: set["db_MovieType"] = None):
        self.movieDBFeatureMap = movieDBFeatureMap
        self.comment = comment
        self.db_MovieDBType = db_MovieDBType
        self.db_MovieDBType13 = db_MovieDBType13 if db_MovieDBType13 is not None else set()
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def movieDBFeatureMap(self) -> str:
        return self.__movieDBFeatureMap

    @movieDBFeatureMap.setter
    def movieDBFeatureMap(self, movieDBFeatureMap: str):
        self.__movieDBFeatureMap = movieDBFeatureMap

    @property
    def db_MovieDBType13(self):
        return self.__db_MovieDBType13

    @db_MovieDBType13.setter
    def db_MovieDBType13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_MovieDBType__db_MovieDBType13", None)
        self.__db_MovieDBType13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "db_MovieType"):
                    opp_val = getattr(item, "db_MovieType", None)
                    
                    if opp_val == self:
                        setattr(item, "db_MovieType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "db_MovieType"):
                    opp_val = getattr(item, "db_MovieType", None)
                    
                    setattr(item, "db_MovieType", self)
                    

    @property
    def db_MovieDBType(self):
        return self.__db_MovieDBType

    @db_MovieDBType.setter
    def db_MovieDBType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_MovieDBType__db_MovieDBType", None)
        self.__db_MovieDBType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_DocumentRoot11"):
                opp_val = getattr(old_value, "db_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_DocumentRoot11"):
                opp_val = getattr(value, "db_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "db_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class db_CustomerType:

    pass
class db_EStringToStringMapEntry:

    pass
class db_DocumentRoot:

    def __init__(self, mixed: str, language: str, specialFeatures: str, db_DocumentRoot: set["db_EStringToStringMapEntry"] = None, db_DocumentRoot2: set["db_EStringToStringMapEntry"] = None, db_DocumentRoot5: set["db_CustomerType"] = None, db_DocumentRoot9: set["db_CustomerReviewType"] = None, db_DocumentRoot11: set["db_MovieDBType"] = None, db_DocumentRoot7: set["db_CriticsReviewType"] = None):
        self.mixed = mixed
        self.language = language
        self.specialFeatures = specialFeatures
        self.db_DocumentRoot = db_DocumentRoot if db_DocumentRoot is not None else set()
        self.db_DocumentRoot2 = db_DocumentRoot2 if db_DocumentRoot2 is not None else set()
        self.db_DocumentRoot5 = db_DocumentRoot5 if db_DocumentRoot5 is not None else set()
        self.db_DocumentRoot9 = db_DocumentRoot9 if db_DocumentRoot9 is not None else set()
        self.db_DocumentRoot11 = db_DocumentRoot11 if db_DocumentRoot11 is not None else set()
        self.db_DocumentRoot7 = db_DocumentRoot7 if db_DocumentRoot7 is not None else set()
        
    @property
    def specialFeatures(self) -> str:
        return self.__specialFeatures

    @specialFeatures.setter
    def specialFeatures(self, specialFeatures: str):
        self.__specialFeatures = specialFeatures

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def db_DocumentRoot9(self):
        return self.__db_DocumentRoot9

    @db_DocumentRoot9.setter
    def db_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DocumentRoot__db_DocumentRoot9", None)
        self.__db_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "db_CustomerReviewType"):
                    opp_val = getattr(item, "db_CustomerReviewType", None)
                    
                    if opp_val == self:
                        setattr(item, "db_CustomerReviewType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "db_CustomerReviewType"):
                    opp_val = getattr(item, "db_CustomerReviewType", None)
                    
                    setattr(item, "db_CustomerReviewType", self)
                    

    @property
    def db_DocumentRoot5(self):
        return self.__db_DocumentRoot5

    @db_DocumentRoot5.setter
    def db_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DocumentRoot__db_DocumentRoot5", None)
        self.__db_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "db_CustomerType"):
                    opp_val = getattr(item, "db_CustomerType", None)
                    
                    if opp_val == self:
                        setattr(item, "db_CustomerType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "db_CustomerType"):
                    opp_val = getattr(item, "db_CustomerType", None)
                    
                    setattr(item, "db_CustomerType", self)
                    

    @property
    def db_DocumentRoot7(self):
        return self.__db_DocumentRoot7

    @db_DocumentRoot7.setter
    def db_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DocumentRoot__db_DocumentRoot7", None)
        self.__db_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "db_CriticsReviewType"):
                    opp_val = getattr(item, "db_CriticsReviewType", None)
                    
                    if opp_val == self:
                        setattr(item, "db_CriticsReviewType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "db_CriticsReviewType"):
                    opp_val = getattr(item, "db_CriticsReviewType", None)
                    
                    setattr(item, "db_CriticsReviewType", self)
                    

    @property
    def db_DocumentRoot11(self):
        return self.__db_DocumentRoot11

    @db_DocumentRoot11.setter
    def db_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DocumentRoot__db_DocumentRoot11", None)
        self.__db_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "db_MovieDBType"):
                    opp_val = getattr(item, "db_MovieDBType", None)
                    
                    if opp_val == self:
                        setattr(item, "db_MovieDBType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "db_MovieDBType"):
                    opp_val = getattr(item, "db_MovieDBType", None)
                    
                    setattr(item, "db_MovieDBType", self)
                    

    @property
    def db_DocumentRoot2(self):
        return self.__db_DocumentRoot2

    @db_DocumentRoot2.setter
    def db_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DocumentRoot__db_DocumentRoot2", None)
        self.__db_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "db_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "db_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "db_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "db_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "db_EStringToStringMapEntry3", None)
                    
                    setattr(item, "db_EStringToStringMapEntry3", self)
                    

    @property
    def db_DocumentRoot(self):
        return self.__db_DocumentRoot

    @db_DocumentRoot.setter
    def db_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_DocumentRoot__db_DocumentRoot", None)
        self.__db_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "db_EStringToStringMapEntry"):
                    opp_val = getattr(item, "db_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "db_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "db_EStringToStringMapEntry"):
                    opp_val = getattr(item, "db_EStringToStringMapEntry", None)
                    
                    setattr(item, "db_EStringToStringMapEntry", self)
                    

class CriticsReviewType:

    pass
class db_CustomerReviewType(CriticsReviewType):

    def __init__(self, comment: str, db_CustomerReviewType: "db_DocumentRoot" = None):
        self.comment = comment
        self.db_CustomerReviewType = db_CustomerReviewType
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def db_CustomerReviewType(self):
        return self.__db_CustomerReviewType

    @db_CustomerReviewType.setter
    def db_CustomerReviewType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_CustomerReviewType__db_CustomerReviewType", None)
        self.__db_CustomerReviewType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_DocumentRoot9"):
                opp_val = getattr(old_value, "db_DocumentRoot9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_DocumentRoot9"):
                opp_val = getattr(value, "db_DocumentRoot9", None)
                if opp_val is None:
                    setattr(value, "db_DocumentRoot9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class db_CriticsReviewType:

    def __init__(self, rating: str, reviewedBy: str, db_CriticsReviewType: "db_DocumentRoot" = None, db_CriticsReviewType16: "db_MovieType" = None):
        self.rating = rating
        self.reviewedBy = reviewedBy
        self.db_CriticsReviewType = db_CriticsReviewType
        self.db_CriticsReviewType16 = db_CriticsReviewType16
        
    @property
    def rating(self) -> str:
        return self.__rating

    @rating.setter
    def rating(self, rating: str):
        self.__rating = rating

    @property
    def reviewedBy(self) -> str:
        return self.__reviewedBy

    @reviewedBy.setter
    def reviewedBy(self, reviewedBy: str):
        self.__reviewedBy = reviewedBy

    @property
    def db_CriticsReviewType(self):
        return self.__db_CriticsReviewType

    @db_CriticsReviewType.setter
    def db_CriticsReviewType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_CriticsReviewType__db_CriticsReviewType", None)
        self.__db_CriticsReviewType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_DocumentRoot7"):
                opp_val = getattr(old_value, "db_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_DocumentRoot7"):
                opp_val = getattr(value, "db_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "db_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def db_CriticsReviewType16(self):
        return self.__db_CriticsReviewType16

    @db_CriticsReviewType16.setter
    def db_CriticsReviewType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_db_CriticsReviewType__db_CriticsReviewType16", None)
        self.__db_CriticsReviewType16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "db_MovieType15"):
                opp_val = getattr(old_value, "db_MovieType15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "db_MovieType15"):
                opp_val = getattr(value, "db_MovieType15", None)
                if opp_val is None:
                    setattr(value, "db_MovieType15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
