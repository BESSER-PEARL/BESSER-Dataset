from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SDBEngine(Enum):
    INNODB = "INNODB"
    MYISAM = "MYISAM"
class SIndex(Enum):
    NO = "NO"
    YES = "YES"
    UNIQUE = "UNIQUE"
    SPATIAL = "SPATIAL"
class SSimpleTypes(Enum):
    INT = "INT"
    TINY_INT = "TINY_INT"
    SMALL_INT = "SMALL_INT"
    FOTO = "FOTO"
    Currency = "Currency"
    Coordinate = "Coordinate"
    MEDIUM_INT = "MEDIUM_INT"
    BOOLEAN = "BOOLEAN"
    BLOB = "BLOB"
    DATETIME = "DATETIME"
    DATE = "DATE"
    TIME = "TIME"
    POLYGON = "POLYGON"
    POINT = "POINT"


############################################
# Definition of Classes
############################################

class SInlinedSQLType:

    pass
class sqlDSL_SDecimal(SInlinedSQLType):

    pass
class sqlDSL_SString(SInlinedSQLType):

    pass
class sqlDSL_SEnumLiteral:

    def __init__(self, name: str, value: int, sqlDSL_SEnumLiteral: "sqlDSL_SEnum" = None):
        self.name = name
        self.value = value
        self.sqlDSL_SEnumLiteral = sqlDSL_SEnumLiteral
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


    @property
    def sqlDSL_SEnumLiteral(self):
        return self.__sqlDSL_SEnumLiteral

    @sqlDSL_SEnumLiteral.setter
    def sqlDSL_SEnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_SEnumLiteral__sqlDSL_SEnumLiteral", None)
        self.__sqlDSL_SEnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_SEnum"):
                opp_val = getattr(old_value, "sqlDSL_SEnum", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_SEnum"):
                opp_val = getattr(value, "sqlDSL_SEnum", None)
                if opp_val is None:
                    setattr(value, "sqlDSL_SEnum", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SExtDeclaredSQLType:

    pass
class sqlDSL_SInlinedSQLType:

    def __init__(self, value: int, sqlDSL_SInlinedSQLType: "sqlDSL_SColumn" = None):
        self.value = value
        self.sqlDSL_SInlinedSQLType = sqlDSL_SInlinedSQLType
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


    @property
    def sqlDSL_SInlinedSQLType(self):
        return self.__sqlDSL_SInlinedSQLType

    @sqlDSL_SInlinedSQLType.setter
    def sqlDSL_SInlinedSQLType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_SInlinedSQLType__sqlDSL_SInlinedSQLType", None)
        self.__sqlDSL_SInlinedSQLType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_SColumn11"):
                opp_val = getattr(old_value, "sqlDSL_SColumn11", None)
                if opp_val == self:
                    setattr(old_value, "sqlDSL_SColumn11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_SColumn11"):
                opp_val = getattr(value, "sqlDSL_SColumn11", None)
                setattr(value, "sqlDSL_SColumn11", self)

class SArtifact:

    pass
class sqlDSL_SEnum(SArtifact, SExtDeclaredSQLType):

    pass
class sqlDSL_STable(SArtifact):

    def __init__(self, cached: bool, prefix: str, entityname: str, sqlDSL_STable6: set["sqlDSL_STableMember"] = None, sqlDSL_STable: "sqlDSL_SSettings" = None, sqlDSL_STable13: "sqlDSL_SJoinColumn" = None):
        self.cached = cached
        self.prefix = prefix
        self.entityname = entityname
        self.sqlDSL_STable6 = sqlDSL_STable6 if sqlDSL_STable6 is not None else set()
        self.sqlDSL_STable = sqlDSL_STable
        self.sqlDSL_STable13 = sqlDSL_STable13
        
        pass
    @property
    def cached(self):
        return self.__cached

    @cached.setter
    def cached(self, cached: bool):
        self.__cached = cached


    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix


    @property
    def entityname(self):
        return self.__entityname

    @entityname.setter
    def entityname(self, entityname: str):
        self.__entityname = entityname


    @property
    def sqlDSL_STable6(self):
        return self.__sqlDSL_STable6

    @sqlDSL_STable6.setter
    def sqlDSL_STable6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_STable__sqlDSL_STable6", None)
        self.__sqlDSL_STable6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlDSL_STableMember"):
                    opp_val = getattr(item, "sqlDSL_STableMember", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlDSL_STableMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlDSL_STableMember"):
                    opp_val = getattr(item, "sqlDSL_STableMember", None)
                    
                    setattr(item, "sqlDSL_STableMember", self)
                    

    @property
    def sqlDSL_STable(self):
        return self.__sqlDSL_STable

    @sqlDSL_STable.setter
    def sqlDSL_STable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_STable__sqlDSL_STable", None)
        self.__sqlDSL_STable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_SSettings4"):
                opp_val = getattr(old_value, "sqlDSL_SSettings4", None)
                if opp_val == self:
                    setattr(old_value, "sqlDSL_SSettings4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_SSettings4"):
                opp_val = getattr(value, "sqlDSL_SSettings4", None)
                setattr(value, "sqlDSL_SSettings4", self)

    @property
    def sqlDSL_STable13(self):
        return self.__sqlDSL_STable13

    @sqlDSL_STable13.setter
    def sqlDSL_STable13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_STable__sqlDSL_STable13", None)
        self.__sqlDSL_STable13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_SJoinColumn"):
                opp_val = getattr(old_value, "sqlDSL_SJoinColumn", None)
                if opp_val == self:
                    setattr(old_value, "sqlDSL_SJoinColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_SJoinColumn"):
                opp_val = getattr(value, "sqlDSL_SJoinColumn", None)
                setattr(value, "sqlDSL_SJoinColumn", self)

class sqlDSL_SExtDeclaredSQLType:

    pass
class STableMember:

    pass
class sqlDSL_SJoinColumn(STableMember):

    pass
class sqlDSL_SColumn(STableMember):

    def __init__(self, simpleType: str, sqlDSL_SColumn: "sqlDSL_SExtDeclaredSQLType" = None, sqlDSL_SColumn11: "sqlDSL_SInlinedSQLType" = None):
        self.simpleType = simpleType
        self.sqlDSL_SColumn = sqlDSL_SColumn
        self.sqlDSL_SColumn11 = sqlDSL_SColumn11
        
        pass
    @property
    def simpleType(self):
        return self.__simpleType

    @simpleType.setter
    def simpleType(self, simpleType: str):
        self.__simpleType = simpleType


    @property
    def sqlDSL_SColumn(self):
        return self.__sqlDSL_SColumn

    @sqlDSL_SColumn.setter
    def sqlDSL_SColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_SColumn__sqlDSL_SColumn", None)
        self.__sqlDSL_SColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_SExtDeclaredSQLType"):
                opp_val = getattr(old_value, "sqlDSL_SExtDeclaredSQLType", None)
                if opp_val == self:
                    setattr(old_value, "sqlDSL_SExtDeclaredSQLType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_SExtDeclaredSQLType"):
                opp_val = getattr(value, "sqlDSL_SExtDeclaredSQLType", None)
                setattr(value, "sqlDSL_SExtDeclaredSQLType", self)

    @property
    def sqlDSL_SColumn11(self):
        return self.__sqlDSL_SColumn11

    @sqlDSL_SColumn11.setter
    def sqlDSL_SColumn11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_SColumn__sqlDSL_SColumn11", None)
        self.__sqlDSL_SColumn11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_SInlinedSQLType"):
                opp_val = getattr(old_value, "sqlDSL_SInlinedSQLType", None)
                if opp_val == self:
                    setattr(old_value, "sqlDSL_SInlinedSQLType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_SInlinedSQLType"):
                opp_val = getattr(value, "sqlDSL_SInlinedSQLType", None)
                setattr(value, "sqlDSL_SInlinedSQLType", self)

class sqlDSL_SColumnProps:

    def __init__(self, nullable: bool, aes: bool, index: str, javacolumn: str, sqlDSL_SColumnProps: "sqlDSL_STableMember" = None):
        self.nullable = nullable
        self.aes = aes
        self.index = index
        self.javacolumn = javacolumn
        self.sqlDSL_SColumnProps = sqlDSL_SColumnProps
        
        pass
    @property
    def javacolumn(self):
        return self.__javacolumn

    @javacolumn.setter
    def javacolumn(self, javacolumn: str):
        self.__javacolumn = javacolumn


    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def aes(self):
        return self.__aes

    @aes.setter
    def aes(self, aes: bool):
        self.__aes = aes


    @property
    def sqlDSL_SColumnProps(self):
        return self.__sqlDSL_SColumnProps

    @sqlDSL_SColumnProps.setter
    def sqlDSL_SColumnProps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_SColumnProps__sqlDSL_SColumnProps", None)
        self.__sqlDSL_SColumnProps = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_STableMember8"):
                opp_val = getattr(old_value, "sqlDSL_STableMember8", None)
                if opp_val == self:
                    setattr(old_value, "sqlDSL_STableMember8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_STableMember8"):
                opp_val = getattr(value, "sqlDSL_STableMember8", None)
                setattr(value, "sqlDSL_STableMember8", self)

class sqlDSL_STableMember:

    def __init__(self, name: str, sqlDSL_STableMember: "sqlDSL_STable" = None, sqlDSL_STableMember8: "sqlDSL_SColumnProps" = None):
        self.name = name
        self.sqlDSL_STableMember = sqlDSL_STableMember
        self.sqlDSL_STableMember8 = sqlDSL_STableMember8
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqlDSL_STableMember8(self):
        return self.__sqlDSL_STableMember8

    @sqlDSL_STableMember8.setter
    def sqlDSL_STableMember8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_STableMember__sqlDSL_STableMember8", None)
        self.__sqlDSL_STableMember8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_SColumnProps"):
                opp_val = getattr(old_value, "sqlDSL_SColumnProps", None)
                if opp_val == self:
                    setattr(old_value, "sqlDSL_SColumnProps", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_SColumnProps"):
                opp_val = getattr(value, "sqlDSL_SColumnProps", None)
                setattr(value, "sqlDSL_SColumnProps", self)

    @property
    def sqlDSL_STableMember(self):
        return self.__sqlDSL_STableMember

    @sqlDSL_STableMember.setter
    def sqlDSL_STableMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_STableMember__sqlDSL_STableMember", None)
        self.__sqlDSL_STableMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_STable6"):
                opp_val = getattr(old_value, "sqlDSL_STable6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_STable6"):
                opp_val = getattr(value, "sqlDSL_STable6", None)
                if opp_val is None:
                    setattr(value, "sqlDSL_STable6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sqlDSL_SSettings:

    def __init__(self, schema: str, javapackage: str, engine: str, sqlDSL_SSettings: "sqlDSL_SModel" = None, sqlDSL_SSettings4: "sqlDSL_STable" = None):
        self.schema = schema
        self.javapackage = javapackage
        self.engine = engine
        self.sqlDSL_SSettings = sqlDSL_SSettings
        self.sqlDSL_SSettings4 = sqlDSL_SSettings4
        
        pass
    @property
    def javapackage(self):
        return self.__javapackage

    @javapackage.setter
    def javapackage(self, javapackage: str):
        self.__javapackage = javapackage


    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine: str):
        self.__engine = engine


    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, schema: str):
        self.__schema = schema


    @property
    def sqlDSL_SSettings(self):
        return self.__sqlDSL_SSettings

    @sqlDSL_SSettings.setter
    def sqlDSL_SSettings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_SSettings__sqlDSL_SSettings", None)
        self.__sqlDSL_SSettings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_SModel"):
                opp_val = getattr(old_value, "sqlDSL_SModel", None)
                if opp_val == self:
                    setattr(old_value, "sqlDSL_SModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_SModel"):
                opp_val = getattr(value, "sqlDSL_SModel", None)
                setattr(value, "sqlDSL_SModel", self)

    @property
    def sqlDSL_SSettings4(self):
        return self.__sqlDSL_SSettings4

    @sqlDSL_SSettings4.setter
    def sqlDSL_SSettings4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_SSettings__sqlDSL_SSettings4", None)
        self.__sqlDSL_SSettings4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_STable"):
                opp_val = getattr(old_value, "sqlDSL_STable", None)
                if opp_val == self:
                    setattr(old_value, "sqlDSL_STable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_STable"):
                opp_val = getattr(value, "sqlDSL_STable", None)
                setattr(value, "sqlDSL_STable", self)

class sqlDSL_SModel:

    def __init__(self, generatedFile: str, sqlDSL_SModel: "sqlDSL_SSettings" = None, sqlDSL_SModel2: set["sqlDSL_SArtifact"] = None):
        self.generatedFile = generatedFile
        self.sqlDSL_SModel = sqlDSL_SModel
        self.sqlDSL_SModel2 = sqlDSL_SModel2 if sqlDSL_SModel2 is not None else set()
        
        pass
    @property
    def generatedFile(self):
        return self.__generatedFile

    @generatedFile.setter
    def generatedFile(self, generatedFile: str):
        self.__generatedFile = generatedFile


    @property
    def sqlDSL_SModel(self):
        return self.__sqlDSL_SModel

    @sqlDSL_SModel.setter
    def sqlDSL_SModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_SModel__sqlDSL_SModel", None)
        self.__sqlDSL_SModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_SSettings"):
                opp_val = getattr(old_value, "sqlDSL_SSettings", None)
                if opp_val == self:
                    setattr(old_value, "sqlDSL_SSettings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_SSettings"):
                opp_val = getattr(value, "sqlDSL_SSettings", None)
                setattr(value, "sqlDSL_SSettings", self)

    @property
    def sqlDSL_SModel2(self):
        return self.__sqlDSL_SModel2

    @sqlDSL_SModel2.setter
    def sqlDSL_SModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_SModel__sqlDSL_SModel2", None)
        self.__sqlDSL_SModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sqlDSL_SArtifact"):
                    opp_val = getattr(item, "sqlDSL_SArtifact", None)
                    
                    if opp_val == self:
                        setattr(item, "sqlDSL_SArtifact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sqlDSL_SArtifact"):
                    opp_val = getattr(item, "sqlDSL_SArtifact", None)
                    
                    setattr(item, "sqlDSL_SArtifact", self)
                    

class sqlDSL_SArtifact:

    def __init__(self, name: str, sqlDSL_SArtifact: "sqlDSL_SModel" = None):
        self.name = name
        self.sqlDSL_SArtifact = sqlDSL_SArtifact
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sqlDSL_SArtifact(self):
        return self.__sqlDSL_SArtifact

    @sqlDSL_SArtifact.setter
    def sqlDSL_SArtifact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sqlDSL_SArtifact__sqlDSL_SArtifact", None)
        self.__sqlDSL_SArtifact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sqlDSL_SModel2"):
                opp_val = getattr(old_value, "sqlDSL_SModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sqlDSL_SModel2"):
                opp_val = getattr(value, "sqlDSL_SModel2", None)
                if opp_val is None:
                    setattr(value, "sqlDSL_SModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
