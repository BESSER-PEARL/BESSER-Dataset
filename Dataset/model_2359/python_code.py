from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SimpleRDBMS_RdbmsModelElement:

    def __init__(self, rdbmsName: str, rdbmsKind: str, id: str):
        self.rdbmsName = rdbmsName
        self.rdbmsKind = rdbmsKind
        self.id = id
        
    @property
    def rdbmsName(self) -> str:
        return self.__rdbmsName

    @rdbmsName.setter
    def rdbmsName(self, rdbmsName: str):
        self.__rdbmsName = rdbmsName

    @property
    def rdbmsKind(self) -> str:
        return self.__rdbmsKind

    @rdbmsKind.setter
    def rdbmsKind(self, rdbmsKind: str):
        self.__rdbmsKind = rdbmsKind

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class RdbmsModelElement:

    pass
class SimpleRDBMS_RdbmsKey(RdbmsModelElement):

    pass
class SimpleRDBMS_RdbmsTable(RdbmsModelElement):

    pass
class SimpleRDBMS_RdbmsSchema(RdbmsModelElement):

    pass
class SimpleRDBMS_RdbmsForeignKey(RdbmsModelElement):

    pass
class SimpleRDBMS_RdbmsColumn(RdbmsModelElement):

    def __init__(self, rdbmsType: str, rdbmsColumn: "SimpleRDBMS_RdbmsTable" = None, rdbmsColumn2: set["SimpleRDBMS_RdbmsKey"] = None, rdbmsColumn4: set["SimpleRDBMS_RdbmsForeignKey"] = None, RdbmsColumn: "SimpleRDBMS_RdbmsForeignKey" = None, RdbmsColumn12: "SimpleRDBMS_RdbmsKey" = None, RdbmsColumn21: "SimpleRDBMS_RdbmsTable" = None):
        self.rdbmsType = rdbmsType
        self.rdbmsColumn = rdbmsColumn
        self.rdbmsColumn2 = rdbmsColumn2 if rdbmsColumn2 is not None else set()
        self.rdbmsColumn4 = rdbmsColumn4 if rdbmsColumn4 is not None else set()
        self.RdbmsColumn = RdbmsColumn
        self.RdbmsColumn12 = RdbmsColumn12
        self.RdbmsColumn21 = RdbmsColumn21
        
    @property
    def rdbmsType(self) -> str:
        return self.__rdbmsType

    @rdbmsType.setter
    def rdbmsType(self, rdbmsType: str):
        self.__rdbmsType = rdbmsType

    @property
    def rdbmsColumn4(self):
        return self.__rdbmsColumn4

    @rdbmsColumn4.setter
    def rdbmsColumn4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_RdbmsColumn__rdbmsColumn4", None)
        self.__rdbmsColumn4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RdbmsForeignKey"):
                    opp_val = getattr(item, "RdbmsForeignKey", None)
                    
                    if opp_val == self:
                        setattr(item, "RdbmsForeignKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RdbmsForeignKey"):
                    opp_val = getattr(item, "RdbmsForeignKey", None)
                    
                    setattr(item, "RdbmsForeignKey", self)
                    

    @property
    def RdbmsColumn21(self):
        return self.__RdbmsColumn21

    @RdbmsColumn21.setter
    def RdbmsColumn21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_RdbmsColumn__RdbmsColumn21", None)
        self.__RdbmsColumn21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbmsOwner"):
                opp_val = getattr(old_value, "rdbmsOwner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbmsOwner"):
                opp_val = getattr(value, "rdbmsOwner", None)
                if opp_val is None:
                    setattr(value, "rdbmsOwner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbmsColumn2(self):
        return self.__rdbmsColumn2

    @rdbmsColumn2.setter
    def rdbmsColumn2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_RdbmsColumn__rdbmsColumn2", None)
        self.__rdbmsColumn2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RdbmsKey"):
                    opp_val = getattr(item, "RdbmsKey", None)
                    
                    if opp_val == self:
                        setattr(item, "RdbmsKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RdbmsKey"):
                    opp_val = getattr(item, "RdbmsKey", None)
                    
                    setattr(item, "RdbmsKey", self)
                    

    @property
    def RdbmsColumn(self):
        return self.__RdbmsColumn

    @RdbmsColumn.setter
    def RdbmsColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_RdbmsColumn__RdbmsColumn", None)
        self.__RdbmsColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbmsForeignKey10"):
                opp_val = getattr(old_value, "rdbmsForeignKey10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbmsForeignKey10"):
                opp_val = getattr(value, "rdbmsForeignKey10", None)
                if opp_val is None:
                    setattr(value, "rdbmsForeignKey10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RdbmsColumn12(self):
        return self.__RdbmsColumn12

    @RdbmsColumn12.setter
    def RdbmsColumn12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_RdbmsColumn__RdbmsColumn12", None)
        self.__RdbmsColumn12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rdbmsKey"):
                opp_val = getattr(old_value, "rdbmsKey", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rdbmsKey"):
                opp_val = getattr(value, "rdbmsKey", None)
                if opp_val is None:
                    setattr(value, "rdbmsKey", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rdbmsColumn(self):
        return self.__rdbmsColumn

    @rdbmsColumn.setter
    def rdbmsColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SimpleRDBMS_RdbmsColumn__rdbmsColumn", None)
        self.__rdbmsColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RdbmsTable"):
                opp_val = getattr(old_value, "RdbmsTable", None)
                if opp_val == self:
                    setattr(old_value, "RdbmsTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RdbmsTable"):
                opp_val = getattr(value, "RdbmsTable", None)
                setattr(value, "RdbmsTable", self)
