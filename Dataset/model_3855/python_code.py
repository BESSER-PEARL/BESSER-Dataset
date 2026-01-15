from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class FKeyType(Enum):
    PKEY = "PKEY"


############################################
# Definition of Classes
############################################

class SimpleRDBMS_Column:

    def __init__(self, name: str, type: str, id: int, SimpleRDBMS_Column: "SimpleRDBMS_Table" = None, SimpleRDBMS_Column5: "SimpleRDBMS_Table" = None, SimpleRDBMS_Column11: "SimpleRDBMS_FKey" = None):
        self.name = name
        self.type = type
        self.id = id
        self.SimpleRDBMS_Column = SimpleRDBMS_Column
        self.SimpleRDBMS_Column5 = SimpleRDBMS_Column5
        self.SimpleRDBMS_Column11 = SimpleRDBMS_Column11
        
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

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def SimpleRDBMS_Column5(self):
        return self.__SimpleRDBMS_Column5

    @SimpleRDBMS_Column5.setter
    def SimpleRDBMS_Column5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__SimpleRDBMS_Column5", None)
        self.__SimpleRDBMS_Column5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleRDBMS_Table4"):
                opp_val = getattr(old_value, "SimpleRDBMS_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleRDBMS_Table4"):
                opp_val = getattr(value, "SimpleRDBMS_Table4", None)
                if opp_val is None:
                    setattr(value, "SimpleRDBMS_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleRDBMS_Column(self):
        return self.__SimpleRDBMS_Column

    @SimpleRDBMS_Column.setter
    def SimpleRDBMS_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__SimpleRDBMS_Column", None)
        self.__SimpleRDBMS_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleRDBMS_Table2"):
                opp_val = getattr(old_value, "SimpleRDBMS_Table2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleRDBMS_Table2"):
                opp_val = getattr(value, "SimpleRDBMS_Table2", None)
                if opp_val is None:
                    setattr(value, "SimpleRDBMS_Table2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleRDBMS_Column11(self):
        return self.__SimpleRDBMS_Column11

    @SimpleRDBMS_Column11.setter
    def SimpleRDBMS_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Column__SimpleRDBMS_Column11", None)
        self.__SimpleRDBMS_Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleRDBMS_FKey10"):
                opp_val = getattr(old_value, "SimpleRDBMS_FKey10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleRDBMS_FKey10"):
                opp_val = getattr(value, "SimpleRDBMS_FKey10", None)
                if opp_val is None:
                    setattr(value, "SimpleRDBMS_FKey10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SimpleRDBMS_FKey:

    def __init__(self, fkeyType: str, SimpleRDBMS_FKey: "SimpleRDBMS_Table" = None, SimpleRDBMS_FKey7: "SimpleRDBMS_Table" = None, SimpleRDBMS_FKey10: set["SimpleRDBMS_Column"] = None):
        self.fkeyType = fkeyType
        self.SimpleRDBMS_FKey = SimpleRDBMS_FKey
        self.SimpleRDBMS_FKey7 = SimpleRDBMS_FKey7
        self.SimpleRDBMS_FKey10 = SimpleRDBMS_FKey10 if SimpleRDBMS_FKey10 is not None else set()
        
    @property
    def fkeyType(self) -> str:
        return self.__fkeyType

    @fkeyType.setter
    def fkeyType(self, fkeyType: str):
        self.__fkeyType = fkeyType

    @property
    def SimpleRDBMS_FKey7(self):
        return self.__SimpleRDBMS_FKey7

    @SimpleRDBMS_FKey7.setter
    def SimpleRDBMS_FKey7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_FKey__SimpleRDBMS_FKey7", None)
        self.__SimpleRDBMS_FKey7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleRDBMS_Table8"):
                opp_val = getattr(old_value, "SimpleRDBMS_Table8", None)
                if opp_val == self:
                    setattr(old_value, "SimpleRDBMS_Table8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleRDBMS_Table8"):
                opp_val = getattr(value, "SimpleRDBMS_Table8", None)
                setattr(value, "SimpleRDBMS_Table8", self)

    @property
    def SimpleRDBMS_FKey(self):
        return self.__SimpleRDBMS_FKey

    @SimpleRDBMS_FKey.setter
    def SimpleRDBMS_FKey(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_FKey__SimpleRDBMS_FKey", None)
        self.__SimpleRDBMS_FKey = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleRDBMS_Table"):
                opp_val = getattr(old_value, "SimpleRDBMS_Table", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleRDBMS_Table"):
                opp_val = getattr(value, "SimpleRDBMS_Table", None)
                if opp_val is None:
                    setattr(value, "SimpleRDBMS_Table", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SimpleRDBMS_FKey10(self):
        return self.__SimpleRDBMS_FKey10

    @SimpleRDBMS_FKey10.setter
    def SimpleRDBMS_FKey10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_FKey__SimpleRDBMS_FKey10", None)
        self.__SimpleRDBMS_FKey10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SimpleRDBMS_Column11"):
                    opp_val = getattr(item, "SimpleRDBMS_Column11", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleRDBMS_Column11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleRDBMS_Column11"):
                    opp_val = getattr(item, "SimpleRDBMS_Column11", None)
                    
                    setattr(item, "SimpleRDBMS_Column11", self)
                    

class SimpleRDBMS_Table:

    def __init__(self, name: str, id: int, SimpleRDBMS_Table: set["SimpleRDBMS_FKey"] = None, SimpleRDBMS_Table2: set["SimpleRDBMS_Column"] = None, SimpleRDBMS_Table4: set["SimpleRDBMS_Column"] = None, SimpleRDBMS_Table8: "SimpleRDBMS_FKey" = None):
        self.name = name
        self.id = id
        self.SimpleRDBMS_Table = SimpleRDBMS_Table if SimpleRDBMS_Table is not None else set()
        self.SimpleRDBMS_Table2 = SimpleRDBMS_Table2 if SimpleRDBMS_Table2 is not None else set()
        self.SimpleRDBMS_Table4 = SimpleRDBMS_Table4 if SimpleRDBMS_Table4 is not None else set()
        self.SimpleRDBMS_Table8 = SimpleRDBMS_Table8
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SimpleRDBMS_Table8(self):
        return self.__SimpleRDBMS_Table8

    @SimpleRDBMS_Table8.setter
    def SimpleRDBMS_Table8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_Table__SimpleRDBMS_Table8", None)
        self.__SimpleRDBMS_Table8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimpleRDBMS_FKey7"):
                opp_val = getattr(old_value, "SimpleRDBMS_FKey7", None)
                if opp_val == self:
                    setattr(old_value, "SimpleRDBMS_FKey7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimpleRDBMS_FKey7"):
                opp_val = getattr(value, "SimpleRDBMS_FKey7", None)
                setattr(value, "SimpleRDBMS_FKey7", self)

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
                if hasattr(item, "SimpleRDBMS_Column"):
                    opp_val = getattr(item, "SimpleRDBMS_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleRDBMS_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleRDBMS_Column"):
                    opp_val = getattr(item, "SimpleRDBMS_Column", None)
                    
                    setattr(item, "SimpleRDBMS_Column", self)
                    

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
                if hasattr(item, "SimpleRDBMS_Column5"):
                    opp_val = getattr(item, "SimpleRDBMS_Column5", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleRDBMS_Column5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleRDBMS_Column5"):
                    opp_val = getattr(item, "SimpleRDBMS_Column5", None)
                    
                    setattr(item, "SimpleRDBMS_Column5", self)
                    

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
                if hasattr(item, "SimpleRDBMS_FKey"):
                    opp_val = getattr(item, "SimpleRDBMS_FKey", None)
                    
                    if opp_val == self:
                        setattr(item, "SimpleRDBMS_FKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SimpleRDBMS_FKey"):
                    opp_val = getattr(item, "SimpleRDBMS_FKey", None)
                    
                    setattr(item, "SimpleRDBMS_FKey", self)
                    
