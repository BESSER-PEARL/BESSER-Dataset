from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Operation:

    pass
class Trmodel_Update(Operation):

    def __init__(self, newName: str):
        self.newName = newName
        
    @property
    def newName(self) -> str:
        return self.__newName

    @newName.setter
    def newName(self, newName: str):
        self.__newName = newName

class Trmodel_Delete(Operation):

    pass
class Trmodel_Add(Operation):

    pass
class Trmodel_Column:

    def __init__(self, Name: str, tableName: str, Trmodel_Column: "Trmodel_Operation" = None):
        self.Name = Name
        self.tableName = tableName
        self.Trmodel_Column = Trmodel_Column
        
    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Trmodel_Column(self):
        return self.__Trmodel_Column

    @Trmodel_Column.setter
    def Trmodel_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trmodel_Column__Trmodel_Column", None)
        self.__Trmodel_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trmodel_Operation6"):
                opp_val = getattr(old_value, "Trmodel_Operation6", None)
                if opp_val == self:
                    setattr(old_value, "Trmodel_Operation6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trmodel_Operation6"):
                opp_val = getattr(value, "Trmodel_Operation6", None)
                setattr(value, "Trmodel_Operation6", self)

class Trmodel_Table:

    def __init__(self, Name: str, Trmodel_Table: "Trmodel_Operation" = None):
        self.Name = Name
        self.Trmodel_Table = Trmodel_Table
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Trmodel_Table(self):
        return self.__Trmodel_Table

    @Trmodel_Table.setter
    def Trmodel_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trmodel_Table__Trmodel_Table", None)
        self.__Trmodel_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trmodel_Operation4"):
                opp_val = getattr(old_value, "Trmodel_Operation4", None)
                if opp_val == self:
                    setattr(old_value, "Trmodel_Operation4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trmodel_Operation4"):
                opp_val = getattr(value, "Trmodel_Operation4", None)
                setattr(value, "Trmodel_Operation4", self)

class Trmodel_LoadModel:

    def __init__(self, url: str, Trmodel_LoadModel: "Trmodel_loader" = None):
        self.url = url
        self.Trmodel_LoadModel = Trmodel_LoadModel
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def Trmodel_LoadModel(self):
        return self.__Trmodel_LoadModel

    @Trmodel_LoadModel.setter
    def Trmodel_LoadModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Trmodel_LoadModel__Trmodel_LoadModel", None)
        self.__Trmodel_LoadModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trmodel_loader2"):
                opp_val = getattr(old_value, "Trmodel_loader2", None)
                if opp_val == self:
                    setattr(old_value, "Trmodel_loader2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trmodel_loader2"):
                opp_val = getattr(value, "Trmodel_loader2", None)
                setattr(value, "Trmodel_loader2", self)

class Trmodel_Operation(ABC):

    pass
class Trmodel_loader:

    pass