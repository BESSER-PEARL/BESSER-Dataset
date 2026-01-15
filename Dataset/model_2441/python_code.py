from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ddl_DataElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class DataElement:

    pass
class ddl_DataType(DataElement):

    pass
class ddl_Column(DataElement):

    pass
class ddl_Table(DataElement):

    pass
class ddl_Schema(DataElement):

    def __init__(self, version: int, conformite: bool, prix: float, ddl_Schema: set["ddl_Table"] = None, ddl_Schema2: set["ddl_DataType"] = None):
        self.version = version
        self.conformite = conformite
        self.prix = prix
        self.ddl_Schema = ddl_Schema if ddl_Schema is not None else set()
        self.ddl_Schema2 = ddl_Schema2 if ddl_Schema2 is not None else set()
        
    @property
    def version(self) -> int:
        return self.__version

    @version.setter
    def version(self, version: int):
        self.__version = version

    @property
    def conformite(self) -> bool:
        return self.__conformite

    @conformite.setter
    def conformite(self, conformite: bool):
        self.__conformite = conformite

    @property
    def prix(self) -> float:
        return self.__prix

    @prix.setter
    def prix(self, prix: float):
        self.__prix = prix

    @property
    def ddl_Schema2(self):
        return self.__ddl_Schema2

    @ddl_Schema2.setter
    def ddl_Schema2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddl_Schema__ddl_Schema2", None)
        self.__ddl_Schema2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddl_DataType"):
                    opp_val = getattr(item, "ddl_DataType", None)
                    
                    if opp_val == self:
                        setattr(item, "ddl_DataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddl_DataType"):
                    opp_val = getattr(item, "ddl_DataType", None)
                    
                    setattr(item, "ddl_DataType", self)
                    

    @property
    def ddl_Schema(self):
        return self.__ddl_Schema

    @ddl_Schema.setter
    def ddl_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ddl_Schema__ddl_Schema", None)
        self.__ddl_Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ddl_Table"):
                    opp_val = getattr(item, "ddl_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "ddl_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ddl_Table"):
                    opp_val = getattr(item, "ddl_Table", None)
                    
                    setattr(item, "ddl_Table", self)
                    
