from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategoryType1(Enum):
    magazine = "magazine"
    novel = "novel"
    fiction = "fiction"
    other = "other"
class BookCategoryType(Enum):
    magazine = "magazine"
    novel = "novel"
    fiction = "fiction"
    other = "other"


############################################
# Definition of Classes
############################################

class sunBooks_EStringToStringMapEntry:

    pass
class sunBooks_DocumentRoot:

    def __init__(self, mixed: str, sunBooks_DocumentRoot: set["sunBooks_EStringToStringMapEntry"] = None, sunBooks_DocumentRoot9: set["sunBooks_EStringToStringMapEntry"] = None, sunBooks_DocumentRoot12: set["sunBooks_CollectionType"] = None):
        self.mixed = mixed
        self.sunBooks_DocumentRoot = sunBooks_DocumentRoot if sunBooks_DocumentRoot is not None else set()
        self.sunBooks_DocumentRoot9 = sunBooks_DocumentRoot9 if sunBooks_DocumentRoot9 is not None else set()
        self.sunBooks_DocumentRoot12 = sunBooks_DocumentRoot12 if sunBooks_DocumentRoot12 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def sunBooks_DocumentRoot(self):
        return self.__sunBooks_DocumentRoot

    @sunBooks_DocumentRoot.setter
    def sunBooks_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sunBooks_DocumentRoot__sunBooks_DocumentRoot", None)
        self.__sunBooks_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sunBooks_EStringToStringMapEntry"):
                    opp_val = getattr(item, "sunBooks_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "sunBooks_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sunBooks_EStringToStringMapEntry"):
                    opp_val = getattr(item, "sunBooks_EStringToStringMapEntry", None)
                    
                    setattr(item, "sunBooks_EStringToStringMapEntry", self)
                    

    @property
    def sunBooks_DocumentRoot9(self):
        return self.__sunBooks_DocumentRoot9

    @sunBooks_DocumentRoot9.setter
    def sunBooks_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sunBooks_DocumentRoot__sunBooks_DocumentRoot9", None)
        self.__sunBooks_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sunBooks_EStringToStringMapEntry10"):
                    opp_val = getattr(item, "sunBooks_EStringToStringMapEntry10", None)
                    
                    if opp_val == self:
                        setattr(item, "sunBooks_EStringToStringMapEntry10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sunBooks_EStringToStringMapEntry10"):
                    opp_val = getattr(item, "sunBooks_EStringToStringMapEntry10", None)
                    
                    setattr(item, "sunBooks_EStringToStringMapEntry10", self)
                    

    @property
    def sunBooks_DocumentRoot12(self):
        return self.__sunBooks_DocumentRoot12

    @sunBooks_DocumentRoot12.setter
    def sunBooks_DocumentRoot12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sunBooks_DocumentRoot__sunBooks_DocumentRoot12", None)
        self.__sunBooks_DocumentRoot12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sunBooks_CollectionType13"):
                    opp_val = getattr(item, "sunBooks_CollectionType13", None)
                    
                    if opp_val == self:
                        setattr(item, "sunBooks_CollectionType13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sunBooks_CollectionType13"):
                    opp_val = getattr(item, "sunBooks_CollectionType13", None)
                    
                    setattr(item, "sunBooks_CollectionType13", self)
                    

class sunBooks_CollectionType:

    pass
class sunBooks_PromotionType:

    def __init__(self, discount: str, none: str, sunBooks_PromotionType: "sunBooks_BookType" = None):
        self.discount = discount
        self.none = none
        self.sunBooks_PromotionType = sunBooks_PromotionType
        
    @property
    def none(self) -> str:
        return self.__none

    @none.setter
    def none(self, none: str):
        self.__none = none

    @property
    def discount(self) -> str:
        return self.__discount

    @discount.setter
    def discount(self, discount: str):
        self.__discount = discount

    @property
    def sunBooks_PromotionType(self):
        return self.__sunBooks_PromotionType

    @sunBooks_PromotionType.setter
    def sunBooks_PromotionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sunBooks_PromotionType__sunBooks_PromotionType", None)
        self.__sunBooks_PromotionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sunBooks_BookType4"):
                opp_val = getattr(old_value, "sunBooks_BookType4", None)
                if opp_val == self:
                    setattr(old_value, "sunBooks_BookType4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sunBooks_BookType4"):
                opp_val = getattr(value, "sunBooks_BookType4", None)
                setattr(value, "sunBooks_BookType4", self)

class sunBooks_BookType:

    def __init__(self, description: str, name: str, iSBN: str, price: str, publicationDate: str, bookCategory: str, itemId: str, sunBooks_BookType: "sunBooks_BooksType" = None, sunBooks_BookType2: "sunBooks_AuthorsType" = None, sunBooks_BookType4: "sunBooks_PromotionType" = None):
        self.description = description
        self.name = name
        self.iSBN = iSBN
        self.price = price
        self.publicationDate = publicationDate
        self.bookCategory = bookCategory
        self.itemId = itemId
        self.sunBooks_BookType = sunBooks_BookType
        self.sunBooks_BookType2 = sunBooks_BookType2
        self.sunBooks_BookType4 = sunBooks_BookType4
        
    @property
    def iSBN(self) -> str:
        return self.__iSBN

    @iSBN.setter
    def iSBN(self, iSBN: str):
        self.__iSBN = iSBN

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def bookCategory(self) -> str:
        return self.__bookCategory

    @bookCategory.setter
    def bookCategory(self, bookCategory: str):
        self.__bookCategory = bookCategory

    @property
    def publicationDate(self) -> str:
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate: str):
        self.__publicationDate = publicationDate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def itemId(self) -> str:
        return self.__itemId

    @itemId.setter
    def itemId(self, itemId: str):
        self.__itemId = itemId

    @property
    def sunBooks_BookType2(self):
        return self.__sunBooks_BookType2

    @sunBooks_BookType2.setter
    def sunBooks_BookType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sunBooks_BookType__sunBooks_BookType2", None)
        self.__sunBooks_BookType2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sunBooks_AuthorsType"):
                opp_val = getattr(old_value, "sunBooks_AuthorsType", None)
                if opp_val == self:
                    setattr(old_value, "sunBooks_AuthorsType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sunBooks_AuthorsType"):
                opp_val = getattr(value, "sunBooks_AuthorsType", None)
                setattr(value, "sunBooks_AuthorsType", self)

    @property
    def sunBooks_BookType(self):
        return self.__sunBooks_BookType

    @sunBooks_BookType.setter
    def sunBooks_BookType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sunBooks_BookType__sunBooks_BookType", None)
        self.__sunBooks_BookType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sunBooks_BooksType"):
                opp_val = getattr(old_value, "sunBooks_BooksType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sunBooks_BooksType"):
                opp_val = getattr(value, "sunBooks_BooksType", None)
                if opp_val is None:
                    setattr(value, "sunBooks_BooksType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sunBooks_BookType4(self):
        return self.__sunBooks_BookType4

    @sunBooks_BookType4.setter
    def sunBooks_BookType4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sunBooks_BookType__sunBooks_BookType4", None)
        self.__sunBooks_BookType4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sunBooks_PromotionType"):
                opp_val = getattr(old_value, "sunBooks_PromotionType", None)
                if opp_val == self:
                    setattr(old_value, "sunBooks_PromotionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sunBooks_PromotionType"):
                opp_val = getattr(value, "sunBooks_PromotionType", None)
                setattr(value, "sunBooks_PromotionType", self)

class sunBooks_BooksType:

    pass
class sunBooks_AuthorsType:

    def __init__(self, authorName: str, sunBooks_AuthorsType: "sunBooks_BookType" = None):
        self.authorName = authorName
        self.sunBooks_AuthorsType = sunBooks_AuthorsType
        
    @property
    def authorName(self) -> str:
        return self.__authorName

    @authorName.setter
    def authorName(self, authorName: str):
        self.__authorName = authorName

    @property
    def sunBooks_AuthorsType(self):
        return self.__sunBooks_AuthorsType

    @sunBooks_AuthorsType.setter
    def sunBooks_AuthorsType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sunBooks_AuthorsType__sunBooks_AuthorsType", None)
        self.__sunBooks_AuthorsType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sunBooks_BookType2"):
                opp_val = getattr(old_value, "sunBooks_BookType2", None)
                if opp_val == self:
                    setattr(old_value, "sunBooks_BookType2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sunBooks_BookType2"):
                opp_val = getattr(value, "sunBooks_BookType2", None)
                setattr(value, "sunBooks_BookType2", self)
