from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class databaseMetamodel_Relation:

    def __init__(self, name: str, isJoinTable: bool, isSelfJoinTable: bool, databaseMetamodel_Relation2: set["databaseMetamodel_Column"] = None, databaseMetamodel_Relation4: set["databaseMetamodel_Column"] = None, databaseMetamodel_Relation7: set["databaseMetamodel_Column"] = None, databaseMetamodel_Relation11: "databaseMetamodel_Relation" = None, databaseMetamodel_Relation9: set["databaseMetamodel_Relation"] = None, databaseMetamodel_Relation: "databaseMetamodel_Database" = None, databaseMetamodel_Relation17: "databaseMetamodel_Column" = None):
        self.name = name
        self.isJoinTable = isJoinTable
        self.isSelfJoinTable = isSelfJoinTable
        self.databaseMetamodel_Relation2 = databaseMetamodel_Relation2 if databaseMetamodel_Relation2 is not None else set()
        self.databaseMetamodel_Relation4 = databaseMetamodel_Relation4 if databaseMetamodel_Relation4 is not None else set()
        self.databaseMetamodel_Relation7 = databaseMetamodel_Relation7 if databaseMetamodel_Relation7 is not None else set()
        self.databaseMetamodel_Relation11 = databaseMetamodel_Relation11
        self.databaseMetamodel_Relation9 = databaseMetamodel_Relation9 if databaseMetamodel_Relation9 is not None else set()
        self.databaseMetamodel_Relation = databaseMetamodel_Relation
        self.databaseMetamodel_Relation17 = databaseMetamodel_Relation17
        
    @property
    def isSelfJoinTable(self) -> bool:
        return self.__isSelfJoinTable

    @isSelfJoinTable.setter
    def isSelfJoinTable(self, isSelfJoinTable: bool):
        self.__isSelfJoinTable = isSelfJoinTable

    @property
    def isJoinTable(self) -> bool:
        return self.__isJoinTable

    @isJoinTable.setter
    def isJoinTable(self, isJoinTable: bool):
        self.__isJoinTable = isJoinTable

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def databaseMetamodel_Relation4(self):
        return self.__databaseMetamodel_Relation4

    @databaseMetamodel_Relation4.setter
    def databaseMetamodel_Relation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Relation__databaseMetamodel_Relation4", None)
        self.__databaseMetamodel_Relation4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "databaseMetamodel_Column5"):
                    opp_val = getattr(item, "databaseMetamodel_Column5", None)
                    
                    if opp_val == self:
                        setattr(item, "databaseMetamodel_Column5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "databaseMetamodel_Column5"):
                    opp_val = getattr(item, "databaseMetamodel_Column5", None)
                    
                    setattr(item, "databaseMetamodel_Column5", self)
                    

    @property
    def databaseMetamodel_Relation11(self):
        return self.__databaseMetamodel_Relation11

    @databaseMetamodel_Relation11.setter
    def databaseMetamodel_Relation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Relation__databaseMetamodel_Relation11", None)
        self.__databaseMetamodel_Relation11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "databaseMetamodel_Relation9"):
                opp_val = getattr(old_value, "databaseMetamodel_Relation9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "databaseMetamodel_Relation9"):
                opp_val = getattr(value, "databaseMetamodel_Relation9", None)
                if opp_val is None:
                    setattr(value, "databaseMetamodel_Relation9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def databaseMetamodel_Relation7(self):
        return self.__databaseMetamodel_Relation7

    @databaseMetamodel_Relation7.setter
    def databaseMetamodel_Relation7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Relation__databaseMetamodel_Relation7", None)
        self.__databaseMetamodel_Relation7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "databaseMetamodel_Column8"):
                    opp_val = getattr(item, "databaseMetamodel_Column8", None)
                    
                    if opp_val == self:
                        setattr(item, "databaseMetamodel_Column8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "databaseMetamodel_Column8"):
                    opp_val = getattr(item, "databaseMetamodel_Column8", None)
                    
                    setattr(item, "databaseMetamodel_Column8", self)
                    

    @property
    def databaseMetamodel_Relation17(self):
        return self.__databaseMetamodel_Relation17

    @databaseMetamodel_Relation17.setter
    def databaseMetamodel_Relation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Relation__databaseMetamodel_Relation17", None)
        self.__databaseMetamodel_Relation17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "databaseMetamodel_Column16"):
                opp_val = getattr(old_value, "databaseMetamodel_Column16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "databaseMetamodel_Column16"):
                opp_val = getattr(value, "databaseMetamodel_Column16", None)
                if opp_val is None:
                    setattr(value, "databaseMetamodel_Column16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def databaseMetamodel_Relation2(self):
        return self.__databaseMetamodel_Relation2

    @databaseMetamodel_Relation2.setter
    def databaseMetamodel_Relation2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Relation__databaseMetamodel_Relation2", None)
        self.__databaseMetamodel_Relation2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "databaseMetamodel_Column"):
                    opp_val = getattr(item, "databaseMetamodel_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "databaseMetamodel_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "databaseMetamodel_Column"):
                    opp_val = getattr(item, "databaseMetamodel_Column", None)
                    
                    setattr(item, "databaseMetamodel_Column", self)
                    

    @property
    def databaseMetamodel_Relation9(self):
        return self.__databaseMetamodel_Relation9

    @databaseMetamodel_Relation9.setter
    def databaseMetamodel_Relation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Relation__databaseMetamodel_Relation9", None)
        self.__databaseMetamodel_Relation9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "databaseMetamodel_Relation11"):
                    opp_val = getattr(item, "databaseMetamodel_Relation11", None)
                    
                    if opp_val == self:
                        setattr(item, "databaseMetamodel_Relation11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "databaseMetamodel_Relation11"):
                    opp_val = getattr(item, "databaseMetamodel_Relation11", None)
                    
                    setattr(item, "databaseMetamodel_Relation11", self)
                    

    @property
    def databaseMetamodel_Relation(self):
        return self.__databaseMetamodel_Relation

    @databaseMetamodel_Relation.setter
    def databaseMetamodel_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Relation__databaseMetamodel_Relation", None)
        self.__databaseMetamodel_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "databaseMetamodel_Database"):
                opp_val = getattr(old_value, "databaseMetamodel_Database", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "databaseMetamodel_Database"):
                opp_val = getattr(value, "databaseMetamodel_Database", None)
                if opp_val is None:
                    setattr(value, "databaseMetamodel_Database", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class databaseMetamodel_Database:

    pass
class databaseMetamodel_Column:

    def __init__(self, hasFKOrder: int, name: str, type: str, hasPKOrder: int, databaseMetamodel_Column: "databaseMetamodel_Relation" = None, databaseMetamodel_Column5: "databaseMetamodel_Relation" = None, databaseMetamodel_Column8: "databaseMetamodel_Relation" = None, databaseMetamodel_Column14: "databaseMetamodel_Column" = None, databaseMetamodel_Column12: set["databaseMetamodel_Column"] = None, databaseMetamodel_Column16: set["databaseMetamodel_Relation"] = None):
        self.hasFKOrder = hasFKOrder
        self.name = name
        self.type = type
        self.hasPKOrder = hasPKOrder
        self.databaseMetamodel_Column = databaseMetamodel_Column
        self.databaseMetamodel_Column5 = databaseMetamodel_Column5
        self.databaseMetamodel_Column8 = databaseMetamodel_Column8
        self.databaseMetamodel_Column14 = databaseMetamodel_Column14
        self.databaseMetamodel_Column12 = databaseMetamodel_Column12 if databaseMetamodel_Column12 is not None else set()
        self.databaseMetamodel_Column16 = databaseMetamodel_Column16 if databaseMetamodel_Column16 is not None else set()
        
    @property
    def hasPKOrder(self) -> int:
        return self.__hasPKOrder

    @hasPKOrder.setter
    def hasPKOrder(self, hasPKOrder: int):
        self.__hasPKOrder = hasPKOrder

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def hasFKOrder(self) -> int:
        return self.__hasFKOrder

    @hasFKOrder.setter
    def hasFKOrder(self, hasFKOrder: int):
        self.__hasFKOrder = hasFKOrder

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def databaseMetamodel_Column5(self):
        return self.__databaseMetamodel_Column5

    @databaseMetamodel_Column5.setter
    def databaseMetamodel_Column5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Column__databaseMetamodel_Column5", None)
        self.__databaseMetamodel_Column5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "databaseMetamodel_Relation4"):
                opp_val = getattr(old_value, "databaseMetamodel_Relation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "databaseMetamodel_Relation4"):
                opp_val = getattr(value, "databaseMetamodel_Relation4", None)
                if opp_val is None:
                    setattr(value, "databaseMetamodel_Relation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def databaseMetamodel_Column14(self):
        return self.__databaseMetamodel_Column14

    @databaseMetamodel_Column14.setter
    def databaseMetamodel_Column14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Column__databaseMetamodel_Column14", None)
        self.__databaseMetamodel_Column14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "databaseMetamodel_Column12"):
                opp_val = getattr(old_value, "databaseMetamodel_Column12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "databaseMetamodel_Column12"):
                opp_val = getattr(value, "databaseMetamodel_Column12", None)
                if opp_val is None:
                    setattr(value, "databaseMetamodel_Column12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def databaseMetamodel_Column8(self):
        return self.__databaseMetamodel_Column8

    @databaseMetamodel_Column8.setter
    def databaseMetamodel_Column8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Column__databaseMetamodel_Column8", None)
        self.__databaseMetamodel_Column8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "databaseMetamodel_Relation7"):
                opp_val = getattr(old_value, "databaseMetamodel_Relation7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "databaseMetamodel_Relation7"):
                opp_val = getattr(value, "databaseMetamodel_Relation7", None)
                if opp_val is None:
                    setattr(value, "databaseMetamodel_Relation7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def databaseMetamodel_Column12(self):
        return self.__databaseMetamodel_Column12

    @databaseMetamodel_Column12.setter
    def databaseMetamodel_Column12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Column__databaseMetamodel_Column12", None)
        self.__databaseMetamodel_Column12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "databaseMetamodel_Column14"):
                    opp_val = getattr(item, "databaseMetamodel_Column14", None)
                    
                    if opp_val == self:
                        setattr(item, "databaseMetamodel_Column14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "databaseMetamodel_Column14"):
                    opp_val = getattr(item, "databaseMetamodel_Column14", None)
                    
                    setattr(item, "databaseMetamodel_Column14", self)
                    

    @property
    def databaseMetamodel_Column16(self):
        return self.__databaseMetamodel_Column16

    @databaseMetamodel_Column16.setter
    def databaseMetamodel_Column16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Column__databaseMetamodel_Column16", None)
        self.__databaseMetamodel_Column16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "databaseMetamodel_Relation17"):
                    opp_val = getattr(item, "databaseMetamodel_Relation17", None)
                    
                    if opp_val == self:
                        setattr(item, "databaseMetamodel_Relation17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "databaseMetamodel_Relation17"):
                    opp_val = getattr(item, "databaseMetamodel_Relation17", None)
                    
                    setattr(item, "databaseMetamodel_Relation17", self)
                    

    @property
    def databaseMetamodel_Column(self):
        return self.__databaseMetamodel_Column

    @databaseMetamodel_Column.setter
    def databaseMetamodel_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_databaseMetamodel_Column__databaseMetamodel_Column", None)
        self.__databaseMetamodel_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "databaseMetamodel_Relation2"):
                opp_val = getattr(old_value, "databaseMetamodel_Relation2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "databaseMetamodel_Relation2"):
                opp_val = getattr(value, "databaseMetamodel_Relation2", None)
                if opp_val is None:
                    setattr(value, "databaseMetamodel_Relation2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
