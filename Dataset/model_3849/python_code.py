from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Table:

    pass
class SimpleRDBMS_FKey:

    pass
class SimpleRDBMS_Column:

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class FKey:

    pass
class Column:

    pass
class SimpleRDBMS_Table:

    def __init__(self, name: str, tipo: str, SimpleRDBMS_Table: set["FKey"] = None, SimpleRDBMS_Table2: set["Column"] = None, SimpleRDBMS_Table4: set["Column"] = None):
        self.name = name
        self.tipo = tipo
        self.SimpleRDBMS_Table = SimpleRDBMS_Table if SimpleRDBMS_Table is not None else set()
        self.SimpleRDBMS_Table2 = SimpleRDBMS_Table2 if SimpleRDBMS_Table2 is not None else set()
        self.SimpleRDBMS_Table4 = SimpleRDBMS_Table4 if SimpleRDBMS_Table4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def SimpleRDBMS_Table(self):
        return self.__SimpleRDBMS_Table

    @SimpleRDBMS_Table.setter
    def SimpleRDBMS_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Table__SimpleRDBMS_Table", None)
        self.__SimpleRDBMS_Table = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FKey"):
                    opp_val = getattr(item, "FKey", None)
                    
                    if opp_val == self:
                        setattr(item, "FKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FKey"):
                    opp_val = getattr(item, "FKey", None)
                    
                    setattr(item, "FKey", self)
                    

    @property
    def SimpleRDBMS_Table4(self):
        return self.__SimpleRDBMS_Table4

    @SimpleRDBMS_Table4.setter
    def SimpleRDBMS_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Table__SimpleRDBMS_Table4", None)
        self.__SimpleRDBMS_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column5"):
                    opp_val = getattr(item, "Column5", None)
                    
                    if opp_val == self:
                        setattr(item, "Column5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column5"):
                    opp_val = getattr(item, "Column5", None)
                    
                    setattr(item, "Column5", self)
                    

    @property
    def SimpleRDBMS_Table2(self):
        return self.__SimpleRDBMS_Table2

    @SimpleRDBMS_Table2.setter
    def SimpleRDBMS_Table2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Table__SimpleRDBMS_Table2", None)
        self.__SimpleRDBMS_Table2 = value if value is not None else set()
        
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
                    
