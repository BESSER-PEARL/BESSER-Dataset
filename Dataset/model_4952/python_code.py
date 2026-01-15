from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FieldType(Enum):
    TextBox = "TextBox"
    CheckBox = "CheckBox"
    RadioButton = "RadioButton"
    SubmitButton = "SubmitButton"
class ColumnType(Enum):
    String = "String"
    Boolean = "Boolean"
    Integer = "Integer"
    Float = "Float"
    Text = "Text"


############################################
# Definition of Classes
############################################

class Field:

    pass
class RelatedEntity:

    pass
class Column:

    pass
class Form:

    pass
class webApplication_content_CRUDForm(Form):

    pass
class Link:

    pass
class Content:

    pass
class webApplication_content_Menu(Content):

    def __init__(self, itemName: str, url: str, order: int, Content: "webApplication_content_Page"):
        self.itemName = itemName
        self.url = url
        self.order = order
        
    @property
    def itemName(self) -> str:
        return self.__itemName

    @itemName.setter
    def itemName(self, itemName: str):
        self.__itemName = itemName

    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

class webApplication_content_MultipleContent(Content):

    def __init__(self, paginated: bool, size: int, Content: "webApplication_content_Page"):
        self.paginated = paginated
        self.size = size
        
    @property
    def paginated(self) -> bool:
        return self.__paginated

    @paginated.setter
    def paginated(self, paginated: bool):
        self.__paginated = paginated

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class webApplication_content_SingleContent(Content):

    pass
class Page:

    pass
class DataSource:

    pass
class Entity:

    pass
class Named:

    pass
class webApplication_content_Page(Named):

    pass
class webApplication_content_Form(Named):

    pass
class webApplication_data_Column(Named):

    def __init__(self, type: str, lenght: int, PK: bool):
        self.type = type
        self.lenght = lenght
        self.PK = PK
        
    @property
    def PK(self) -> bool:
        return self.__PK

    @PK.setter
    def PK(self, PK: bool):
        self.__PK = PK

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def lenght(self) -> int:
        return self.__lenght

    @lenght.setter
    def lenght(self, lenght: int):
        self.__lenght = lenght

class webApplication_content_Field(Named):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class webApplication_content_Link(Named):

    pass
class webApplication_data_Entity(Named):

    def __init__(self, numberOfColumns: str, webApplication_data_Entity: set["Column"] = None, webApplication_data_Entity9: set["RelatedEntity"] = None, webApplication_data_Entity11: set["Entity"] = None):
        self.numberOfColumns = numberOfColumns
        self.webApplication_data_Entity = webApplication_data_Entity if webApplication_data_Entity is not None else set()
        self.webApplication_data_Entity9 = webApplication_data_Entity9 if webApplication_data_Entity9 is not None else set()
        self.webApplication_data_Entity11 = webApplication_data_Entity11 if webApplication_data_Entity11 is not None else set()
        
    @property
    def numberOfColumns(self) -> str:
        return self.__numberOfColumns

    @numberOfColumns.setter
    def numberOfColumns(self, numberOfColumns: str):
        self.__numberOfColumns = numberOfColumns

    @property
    def webApplication_data_Entity11(self):
        return self.__webApplication_data_Entity11

    @webApplication_data_Entity11.setter
    def webApplication_data_Entity11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webApplication_data_Entity__webApplication_data_Entity11", None)
        self.__webApplication_data_Entity11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Entity12"):
                    opp_val = getattr(item, "Entity12", None)
                    
                    if opp_val == self:
                        setattr(item, "Entity12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Entity12"):
                    opp_val = getattr(item, "Entity12", None)
                    
                    setattr(item, "Entity12", self)
                    

    @property
    def webApplication_data_Entity(self):
        return self.__webApplication_data_Entity

    @webApplication_data_Entity.setter
    def webApplication_data_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webApplication_data_Entity__webApplication_data_Entity", None)
        self.__webApplication_data_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    if opp_val == self:
                        setattr(item, "Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column"):
                    opp_val = getattr(item, "Column", None)
                    
                    setattr(item, "Column", self)
                    

    @property
    def webApplication_data_Entity9(self):
        return self.__webApplication_data_Entity9

    @webApplication_data_Entity9.setter
    def webApplication_data_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webApplication_data_Entity__webApplication_data_Entity9", None)
        self.__webApplication_data_Entity9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelatedEntity"):
                    opp_val = getattr(item, "RelatedEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "RelatedEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelatedEntity"):
                    opp_val = getattr(item, "RelatedEntity", None)
                    
                    setattr(item, "RelatedEntity", self)
                    

    def getPKRelated(self) -> str:
        # TODO: Implement getPKRelated method
        pass

    def getPK(self) -> str:
        # TODO: Implement getPK method
        pass

class webApplication_data_RelatedEntity(Named):

    pass
class webApplication_content_Content(Named):

    pass
class webApplication_WebApplicationModel(Named):

    pass
class webApplication_Named:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class webApplication_data_DataSource(Named):

    pass