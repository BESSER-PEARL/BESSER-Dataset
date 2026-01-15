from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BasicType(Enum):
    BOOL = "BOOL"
    INT = "INT"
    CHAR = "CHAR"
    REAL = "REAL"


############################################
# Definition of Classes
############################################

class rdpl_RecordElement:

    def __init__(self, value: str, rdpl_RecordElement21: "rdpl_Column" = None, rdpl_RecordElement: "rdpl_Record" = None):
        self.value = value
        self.rdpl_RecordElement21 = rdpl_RecordElement21
        self.rdpl_RecordElement = rdpl_RecordElement
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def rdpl_RecordElement(self):
        return self.__rdpl_RecordElement

    @rdpl_RecordElement.setter
    def rdpl_RecordElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_RecordElement__rdpl_RecordElement", None)
        self.__rdpl_RecordElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_Record19"):
                opp_val = getattr(old_value, "rdpl_Record19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_Record19"):
                opp_val = getattr(value, "rdpl_Record19", None)
                if opp_val is None:
                    setattr(value, "rdpl_Record19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdpl_RecordElement21(self):
        return self.__rdpl_RecordElement21

    @rdpl_RecordElement21.setter
    def rdpl_RecordElement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_RecordElement__rdpl_RecordElement21", None)
        self.__rdpl_RecordElement21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_Column22"):
                opp_val = getattr(old_value, "rdpl_Column22", None)
                if opp_val == self:
                    setattr(old_value, "rdpl_Column22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_Column22"):
                opp_val = getattr(value, "rdpl_Column22", None)
                setattr(value, "rdpl_Column22", self)

class rdpl_ForeignKey:

    pass
class rdpl_Type:

    def __init__(self, name: str, rdpl_Type: "rdpl_Schema" = None, rdpl_Type25: "rdpl_Column" = None):
        self.name = name
        self.rdpl_Type = rdpl_Type
        self.rdpl_Type25 = rdpl_Type25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rdpl_Type(self):
        return self.__rdpl_Type

    @rdpl_Type.setter
    def rdpl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Type__rdpl_Type", None)
        self.__rdpl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_Schema2"):
                opp_val = getattr(old_value, "rdpl_Schema2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_Schema2"):
                opp_val = getattr(value, "rdpl_Schema2", None)
                if opp_val is None:
                    setattr(value, "rdpl_Schema2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdpl_Type25(self):
        return self.__rdpl_Type25

    @rdpl_Type25.setter
    def rdpl_Type25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Type__rdpl_Type25", None)
        self.__rdpl_Type25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_Column24"):
                opp_val = getattr(old_value, "rdpl_Column24", None)
                if opp_val == self:
                    setattr(old_value, "rdpl_Column24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_Column24"):
                opp_val = getattr(value, "rdpl_Column24", None)
                setattr(value, "rdpl_Column24", self)

class rdpl_Record:

    pass
class rdpl_Column:

    def __init__(self, name: str, stype: str, ctype: str, rdpl_Column: "rdpl_Table" = None, rdpl_Column7: "rdpl_Table" = None, rdpl_Column17: "rdpl_ForeignKey" = None, rdpl_Column22: "rdpl_RecordElement" = None, rdpl_Column24: "rdpl_Type" = None):
        self.name = name
        self.stype = stype
        self.ctype = ctype
        self.rdpl_Column = rdpl_Column
        self.rdpl_Column7 = rdpl_Column7
        self.rdpl_Column17 = rdpl_Column17
        self.rdpl_Column22 = rdpl_Column22
        self.rdpl_Column24 = rdpl_Column24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ctype(self) -> str:
        return self.__ctype

    @ctype.setter
    def ctype(self, ctype: str):
        self.__ctype = ctype

    @property
    def stype(self) -> str:
        return self.__stype

    @stype.setter
    def stype(self, stype: str):
        self.__stype = stype

    @property
    def rdpl_Column17(self):
        return self.__rdpl_Column17

    @rdpl_Column17.setter
    def rdpl_Column17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Column__rdpl_Column17", None)
        self.__rdpl_Column17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_ForeignKey16"):
                opp_val = getattr(old_value, "rdpl_ForeignKey16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_ForeignKey16"):
                opp_val = getattr(value, "rdpl_ForeignKey16", None)
                if opp_val is None:
                    setattr(value, "rdpl_ForeignKey16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdpl_Column7(self):
        return self.__rdpl_Column7

    @rdpl_Column7.setter
    def rdpl_Column7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Column__rdpl_Column7", None)
        self.__rdpl_Column7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_Table6"):
                opp_val = getattr(old_value, "rdpl_Table6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_Table6"):
                opp_val = getattr(value, "rdpl_Table6", None)
                if opp_val is None:
                    setattr(value, "rdpl_Table6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdpl_Column(self):
        return self.__rdpl_Column

    @rdpl_Column.setter
    def rdpl_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Column__rdpl_Column", None)
        self.__rdpl_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_Table4"):
                opp_val = getattr(old_value, "rdpl_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_Table4"):
                opp_val = getattr(value, "rdpl_Table4", None)
                if opp_val is None:
                    setattr(value, "rdpl_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdpl_Column24(self):
        return self.__rdpl_Column24

    @rdpl_Column24.setter
    def rdpl_Column24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Column__rdpl_Column24", None)
        self.__rdpl_Column24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_Type25"):
                opp_val = getattr(old_value, "rdpl_Type25", None)
                if opp_val == self:
                    setattr(old_value, "rdpl_Type25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_Type25"):
                opp_val = getattr(value, "rdpl_Type25", None)
                setattr(value, "rdpl_Type25", self)

    @property
    def rdpl_Column22(self):
        return self.__rdpl_Column22

    @rdpl_Column22.setter
    def rdpl_Column22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Column__rdpl_Column22", None)
        self.__rdpl_Column22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_RecordElement21"):
                opp_val = getattr(old_value, "rdpl_RecordElement21", None)
                if opp_val == self:
                    setattr(old_value, "rdpl_RecordElement21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_RecordElement21"):
                opp_val = getattr(value, "rdpl_RecordElement21", None)
                setattr(value, "rdpl_RecordElement21", self)

class rdpl_Table:

    def __init__(self, name: str, rdpl_Table4: set["rdpl_Column"] = None, rdpl_Table6: set["rdpl_Column"] = None, rdpl_Table9: set["rdpl_Record"] = None, rdpl_Table: "rdpl_Schema" = None, rdpl_Table14: "rdpl_ForeignKey" = None, rdpl_Table11: set["rdpl_ForeignKey"] = None):
        self.name = name
        self.rdpl_Table4 = rdpl_Table4 if rdpl_Table4 is not None else set()
        self.rdpl_Table6 = rdpl_Table6 if rdpl_Table6 is not None else set()
        self.rdpl_Table9 = rdpl_Table9 if rdpl_Table9 is not None else set()
        self.rdpl_Table = rdpl_Table
        self.rdpl_Table14 = rdpl_Table14
        self.rdpl_Table11 = rdpl_Table11 if rdpl_Table11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rdpl_Table11(self):
        return self.__rdpl_Table11

    @rdpl_Table11.setter
    def rdpl_Table11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Table__rdpl_Table11", None)
        self.__rdpl_Table11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdpl_ForeignKey"):
                    opp_val = getattr(item, "rdpl_ForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "rdpl_ForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdpl_ForeignKey"):
                    opp_val = getattr(item, "rdpl_ForeignKey", None)
                    
                    setattr(item, "rdpl_ForeignKey", self)
                    

    @property
    def rdpl_Table9(self):
        return self.__rdpl_Table9

    @rdpl_Table9.setter
    def rdpl_Table9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Table__rdpl_Table9", None)
        self.__rdpl_Table9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdpl_Record"):
                    opp_val = getattr(item, "rdpl_Record", None)
                    
                    if opp_val == self:
                        setattr(item, "rdpl_Record", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdpl_Record"):
                    opp_val = getattr(item, "rdpl_Record", None)
                    
                    setattr(item, "rdpl_Record", self)
                    

    @property
    def rdpl_Table(self):
        return self.__rdpl_Table

    @rdpl_Table.setter
    def rdpl_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Table__rdpl_Table", None)
        self.__rdpl_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_Schema"):
                opp_val = getattr(old_value, "rdpl_Schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_Schema"):
                opp_val = getattr(value, "rdpl_Schema", None)
                if opp_val is None:
                    setattr(value, "rdpl_Schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdpl_Table14(self):
        return self.__rdpl_Table14

    @rdpl_Table14.setter
    def rdpl_Table14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Table__rdpl_Table14", None)
        self.__rdpl_Table14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdpl_ForeignKey13"):
                opp_val = getattr(old_value, "rdpl_ForeignKey13", None)
                if opp_val == self:
                    setattr(old_value, "rdpl_ForeignKey13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdpl_ForeignKey13"):
                opp_val = getattr(value, "rdpl_ForeignKey13", None)
                setattr(value, "rdpl_ForeignKey13", self)

    @property
    def rdpl_Table6(self):
        return self.__rdpl_Table6

    @rdpl_Table6.setter
    def rdpl_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Table__rdpl_Table6", None)
        self.__rdpl_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdpl_Column7"):
                    opp_val = getattr(item, "rdpl_Column7", None)
                    
                    if opp_val == self:
                        setattr(item, "rdpl_Column7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdpl_Column7"):
                    opp_val = getattr(item, "rdpl_Column7", None)
                    
                    setattr(item, "rdpl_Column7", self)
                    

    @property
    def rdpl_Table4(self):
        return self.__rdpl_Table4

    @rdpl_Table4.setter
    def rdpl_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Table__rdpl_Table4", None)
        self.__rdpl_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdpl_Column"):
                    opp_val = getattr(item, "rdpl_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "rdpl_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdpl_Column"):
                    opp_val = getattr(item, "rdpl_Column", None)
                    
                    setattr(item, "rdpl_Column", self)
                    

class rdpl_Schema:

    def __init__(self, name: str, rdpl_Schema: set["rdpl_Table"] = None, rdpl_Schema2: set["rdpl_Type"] = None):
        self.name = name
        self.rdpl_Schema = rdpl_Schema if rdpl_Schema is not None else set()
        self.rdpl_Schema2 = rdpl_Schema2 if rdpl_Schema2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rdpl_Schema2(self):
        return self.__rdpl_Schema2

    @rdpl_Schema2.setter
    def rdpl_Schema2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Schema__rdpl_Schema2", None)
        self.__rdpl_Schema2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdpl_Type"):
                    opp_val = getattr(item, "rdpl_Type", None)
                    
                    if opp_val == self:
                        setattr(item, "rdpl_Type", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdpl_Type"):
                    opp_val = getattr(item, "rdpl_Type", None)
                    
                    setattr(item, "rdpl_Type", self)
                    

    @property
    def rdpl_Schema(self):
        return self.__rdpl_Schema

    @rdpl_Schema.setter
    def rdpl_Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rdpl_Schema__rdpl_Schema", None)
        self.__rdpl_Schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rdpl_Table"):
                    opp_val = getattr(item, "rdpl_Table", None)
                    
                    if opp_val == self:
                        setattr(item, "rdpl_Table", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rdpl_Table"):
                    opp_val = getattr(item, "rdpl_Table", None)
                    
                    setattr(item, "rdpl_Table", self)
                    
