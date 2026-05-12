from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dbmap_DBMapperTableEntry:

    def __init__(self, name: str, expression: str, type: str, nullable: bool, join: bool, operator: str, dbmap_DBMapperTableEntry: "dbmap_AbstractDBDataMapTable" = None):
        self.name = name
        self.expression = expression
        self.type = type
        self.nullable = nullable
        self.join = join
        self.operator = operator
        self.dbmap_DBMapperTableEntry = dbmap_DBMapperTableEntry
        
        pass
    @property
    def join(self):
        return self.__join

    @join.setter
    def join(self, join: bool):
        self.__join = join


    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


    @property
    def dbmap_DBMapperTableEntry(self):
        return self.__dbmap_DBMapperTableEntry

    @dbmap_DBMapperTableEntry.setter
    def dbmap_DBMapperTableEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmap_DBMapperTableEntry__dbmap_DBMapperTableEntry", None)
        self.__dbmap_DBMapperTableEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmap_AbstractDBDataMapTable"):
                opp_val = getattr(old_value, "dbmap_AbstractDBDataMapTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmap_AbstractDBDataMapTable"):
                opp_val = getattr(value, "dbmap_AbstractDBDataMapTable", None)
                if opp_val is None:
                    setattr(value, "dbmap_AbstractDBDataMapTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbmap_FilterEntry:

    def __init__(self, name: str, expression: str, dbmap_FilterEntry: "dbmap_OutputTable" = None):
        self.name = name
        self.expression = expression
        self.dbmap_FilterEntry = dbmap_FilterEntry
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dbmap_FilterEntry(self):
        return self.__dbmap_FilterEntry

    @dbmap_FilterEntry.setter
    def dbmap_FilterEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmap_FilterEntry__dbmap_FilterEntry", None)
        self.__dbmap_FilterEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmap_OutputTable7"):
                opp_val = getattr(old_value, "dbmap_OutputTable7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmap_OutputTable7"):
                opp_val = getattr(value, "dbmap_OutputTable7", None)
                if opp_val is None:
                    setattr(value, "dbmap_OutputTable7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstaceDBInOutTable:

    pass
class dbmap_InputTable(AbstaceDBInOutTable):

    def __init__(self, joinType: str, alias: str, dbmap_InputTable: "dbmap_DBMapData" = None):
        self.joinType = joinType
        self.alias = alias
        self.dbmap_InputTable = dbmap_InputTable
        
        pass
    @property
    def joinType(self):
        return self.__joinType

    @joinType.setter
    def joinType(self, joinType: str):
        self.__joinType = joinType


    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias


    @property
    def dbmap_InputTable(self):
        return self.__dbmap_InputTable

    @dbmap_InputTable.setter
    def dbmap_InputTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmap_InputTable__dbmap_InputTable", None)
        self.__dbmap_InputTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbmap_DBMapData2"):
                opp_val = getattr(old_value, "dbmap_DBMapData2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbmap_DBMapData2"):
                opp_val = getattr(value, "dbmap_DBMapData2", None)
                if opp_val is None:
                    setattr(value, "dbmap_DBMapData2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbmap_OutputTable(AbstaceDBInOutTable):

    pass
class AbstractDBDataMapTable:

    pass
class dbmap_AbstaceDBInOutTable(AbstractDBDataMapTable):

    pass
class dbmap_AbstractDBDataMapTable:

    def __init__(self, name: str, minimized: bool, readonly: bool, tableName: str, dbmap_AbstractDBDataMapTable: set["dbmap_DBMapperTableEntry"] = None):
        self.name = name
        self.minimized = minimized
        self.readonly = readonly
        self.tableName = tableName
        self.dbmap_AbstractDBDataMapTable = dbmap_AbstractDBDataMapTable if dbmap_AbstractDBDataMapTable is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def readonly(self):
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly


    @property
    def minimized(self):
        return self.__minimized

    @minimized.setter
    def minimized(self, minimized: bool):
        self.__minimized = minimized


    @property
    def tableName(self):
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName


    @property
    def dbmap_AbstractDBDataMapTable(self):
        return self.__dbmap_AbstractDBDataMapTable

    @dbmap_AbstractDBDataMapTable.setter
    def dbmap_AbstractDBDataMapTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbmap_AbstractDBDataMapTable__dbmap_AbstractDBDataMapTable", None)
        self.__dbmap_AbstractDBDataMapTable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbmap_DBMapperTableEntry"):
                    opp_val = getattr(item, "dbmap_DBMapperTableEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "dbmap_DBMapperTableEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbmap_DBMapperTableEntry"):
                    opp_val = getattr(item, "dbmap_DBMapperTableEntry", None)
                    
                    setattr(item, "dbmap_DBMapperTableEntry", self)
                    

class dbmap_VarTable(AbstractDBDataMapTable):

    pass
class AbstractExternalData:

    pass
class dbmap_DBMapData(AbstractExternalData):

    pass