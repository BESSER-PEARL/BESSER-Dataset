from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CheckOption(Enum):
    NONE = "NONE"
    CASCADE = "CASCADE"
    LOCAL = "LOCAL"
class LanguageType(Enum):
    REXX = "REXX"
    RPG = "RPG"
    RPGLE = "RPGLE"
    PLSQL = "PLSQL"
    SQL = "SQL"
    JAVA = "JAVA"
    C = "C"
    OLE = "OLE"
    ASSEMBLY = "ASSEMBLY"
    COBOL = "COBOL"
    PLI = "PLI"
    CPLUSPLUS = "CPLUSPLUS"
    CL = "CL"
    COBOLLE = "COBOLLE"
    FORTRAN = "FORTRAN"
class LengthUnit(Enum):
    DECIMAL = "DECIMAL"
    BIT = "BIT"
    BYTE = "BYTE"
    DOUBLE_BYTE = "DOUBLE_BYTE"
class ParentUpdateDRIRuleType(Enum):
    NO_ACTION = "NO_ACTION"
    RESTRICT = "RESTRICT"
    CASCADE = "CASCADE"
    SET_NULL = "SET_NULL"
    SET_DEFAULT = "SET_DEFAULT"
class ProcedureType(Enum):
    PROCEDURE = "PROCEDURE"
    FUNCTION = "FUNCTION"
class ParentDeleteDRIRuleType(Enum):
    NO_ACTION = "NO_ACTION"
    RESTRICT = "RESTRICT"
    CASCADE = "CASCADE"
    SET_NULL = "SET_NULL"
    SET_DEFAULT = "SET_DEFAULT"
class PercentFreeTerminology(Enum):
    PERCENT_FREE = "PERCENT_FREE"
    FILL_FACTOR = "FILL_FACTOR"
    THRESHOLD = "THRESHOLD"
class ParameterStyle(Enum):
    DB2SQL = "DB2SQL"
    GENERAL = "GENERAL"
    GENERAL_WITH_NULLS = "GENERAL_WITH_NULLS"
    DB2GENRL = "DB2GENRL"
    DB2DARI = "DB2DARI"
    JAVA = "JAVA"
    SQL = "SQL"
class TableSpaceType(Enum):
    REGULAR = "REGULAR"
    LOB = "LOB"
    SYSTEM_TEMPORARY = "SYSTEM_TEMPORARY"
    USER_TEMPORARY = "USER_TEMPORARY"
    PERMANENT = "PERMANENT"
    TEMPORARY = "TEMPORARY"
    LONG = "LONG"
    LARGE = "LARGE"


############################################
# Definition of Classes
############################################

class dbdefinition_PrivilegeDefinition:

    def __init__(self, name: str, dbdefinition_PrivilegeDefinition: "dbdefinition_PrivilegedElementDefinition" = None, dbdefinition_PrivilegeDefinition66: set["dbdefinition_PrivilegedElementDefinition"] = None):
        self.name = name
        self.dbdefinition_PrivilegeDefinition = dbdefinition_PrivilegeDefinition
        self.dbdefinition_PrivilegeDefinition66 = dbdefinition_PrivilegeDefinition66 if dbdefinition_PrivilegeDefinition66 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dbdefinition_PrivilegeDefinition(self):
        return self.__dbdefinition_PrivilegeDefinition

    @dbdefinition_PrivilegeDefinition.setter
    def dbdefinition_PrivilegeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PrivilegeDefinition__dbdefinition_PrivilegeDefinition", None)
        self.__dbdefinition_PrivilegeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_PrivilegedElementDefinition64"):
                opp_val = getattr(old_value, "dbdefinition_PrivilegedElementDefinition64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_PrivilegedElementDefinition64"):
                opp_val = getattr(value, "dbdefinition_PrivilegedElementDefinition64", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_PrivilegedElementDefinition64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbdefinition_PrivilegeDefinition66(self):
        return self.__dbdefinition_PrivilegeDefinition66

    @dbdefinition_PrivilegeDefinition66.setter
    def dbdefinition_PrivilegeDefinition66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PrivilegeDefinition__dbdefinition_PrivilegeDefinition66", None)
        self.__dbdefinition_PrivilegeDefinition66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_PrivilegedElementDefinition67"):
                    opp_val = getattr(item, "dbdefinition_PrivilegedElementDefinition67", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_PrivilegedElementDefinition67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_PrivilegedElementDefinition67"):
                    opp_val = getattr(item, "dbdefinition_PrivilegedElementDefinition67", None)
                    
                    setattr(item, "dbdefinition_PrivilegedElementDefinition67", self)
                    

class dbdefinition_FieldQualifierDefinition:

    def __init__(self, name: str, maximumPrecision: int, defaultPrecision: int, precisionSupported: bool, maximumScale: int, defaultScale: int, scaleSupported: bool, dbdefinition_FieldQualifierDefinition: "dbdefinition_PredefinedDataTypeDefinition" = None, dbdefinition_FieldQualifierDefinition41: "dbdefinition_PredefinedDataTypeDefinition" = None, dbdefinition_FieldQualifierDefinition44: "dbdefinition_PredefinedDataTypeDefinition" = None, dbdefinition_FieldQualifierDefinition47: "dbdefinition_PredefinedDataTypeDefinition" = None, dbdefinition_FieldQualifierDefinition62: "dbdefinition_FieldQualifierDefinition" = None, dbdefinition_FieldQualifierDefinition60: set["dbdefinition_FieldQualifierDefinition"] = None):
        self.name = name
        self.maximumPrecision = maximumPrecision
        self.defaultPrecision = defaultPrecision
        self.precisionSupported = precisionSupported
        self.maximumScale = maximumScale
        self.defaultScale = defaultScale
        self.scaleSupported = scaleSupported
        self.dbdefinition_FieldQualifierDefinition = dbdefinition_FieldQualifierDefinition
        self.dbdefinition_FieldQualifierDefinition41 = dbdefinition_FieldQualifierDefinition41
        self.dbdefinition_FieldQualifierDefinition44 = dbdefinition_FieldQualifierDefinition44
        self.dbdefinition_FieldQualifierDefinition47 = dbdefinition_FieldQualifierDefinition47
        self.dbdefinition_FieldQualifierDefinition62 = dbdefinition_FieldQualifierDefinition62
        self.dbdefinition_FieldQualifierDefinition60 = dbdefinition_FieldQualifierDefinition60 if dbdefinition_FieldQualifierDefinition60 is not None else set()
        
        pass
    @property
    def defaultScale(self):
        return self.__defaultScale

    @defaultScale.setter
    def defaultScale(self, defaultScale: int):
        self.__defaultScale = defaultScale


    @property
    def maximumScale(self):
        return self.__maximumScale

    @maximumScale.setter
    def maximumScale(self, maximumScale: int):
        self.__maximumScale = maximumScale


    @property
    def scaleSupported(self):
        return self.__scaleSupported

    @scaleSupported.setter
    def scaleSupported(self, scaleSupported: bool):
        self.__scaleSupported = scaleSupported


    @property
    def maximumPrecision(self):
        return self.__maximumPrecision

    @maximumPrecision.setter
    def maximumPrecision(self, maximumPrecision: int):
        self.__maximumPrecision = maximumPrecision


    @property
    def defaultPrecision(self):
        return self.__defaultPrecision

    @defaultPrecision.setter
    def defaultPrecision(self, defaultPrecision: int):
        self.__defaultPrecision = defaultPrecision


    @property
    def precisionSupported(self):
        return self.__precisionSupported

    @precisionSupported.setter
    def precisionSupported(self, precisionSupported: bool):
        self.__precisionSupported = precisionSupported


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dbdefinition_FieldQualifierDefinition47(self):
        return self.__dbdefinition_FieldQualifierDefinition47

    @dbdefinition_FieldQualifierDefinition47.setter
    def dbdefinition_FieldQualifierDefinition47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_FieldQualifierDefinition__dbdefinition_FieldQualifierDefinition47", None)
        self.__dbdefinition_FieldQualifierDefinition47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_PredefinedDataTypeDefinition46"):
                opp_val = getattr(old_value, "dbdefinition_PredefinedDataTypeDefinition46", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_PredefinedDataTypeDefinition46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_PredefinedDataTypeDefinition46"):
                opp_val = getattr(value, "dbdefinition_PredefinedDataTypeDefinition46", None)
                setattr(value, "dbdefinition_PredefinedDataTypeDefinition46", self)

    @property
    def dbdefinition_FieldQualifierDefinition60(self):
        return self.__dbdefinition_FieldQualifierDefinition60

    @dbdefinition_FieldQualifierDefinition60.setter
    def dbdefinition_FieldQualifierDefinition60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_FieldQualifierDefinition__dbdefinition_FieldQualifierDefinition60", None)
        self.__dbdefinition_FieldQualifierDefinition60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_FieldQualifierDefinition62"):
                    opp_val = getattr(item, "dbdefinition_FieldQualifierDefinition62", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_FieldQualifierDefinition62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_FieldQualifierDefinition62"):
                    opp_val = getattr(item, "dbdefinition_FieldQualifierDefinition62", None)
                    
                    setattr(item, "dbdefinition_FieldQualifierDefinition62", self)
                    

    @property
    def dbdefinition_FieldQualifierDefinition62(self):
        return self.__dbdefinition_FieldQualifierDefinition62

    @dbdefinition_FieldQualifierDefinition62.setter
    def dbdefinition_FieldQualifierDefinition62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_FieldQualifierDefinition__dbdefinition_FieldQualifierDefinition62", None)
        self.__dbdefinition_FieldQualifierDefinition62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_FieldQualifierDefinition60"):
                opp_val = getattr(old_value, "dbdefinition_FieldQualifierDefinition60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_FieldQualifierDefinition60"):
                opp_val = getattr(value, "dbdefinition_FieldQualifierDefinition60", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_FieldQualifierDefinition60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbdefinition_FieldQualifierDefinition41(self):
        return self.__dbdefinition_FieldQualifierDefinition41

    @dbdefinition_FieldQualifierDefinition41.setter
    def dbdefinition_FieldQualifierDefinition41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_FieldQualifierDefinition__dbdefinition_FieldQualifierDefinition41", None)
        self.__dbdefinition_FieldQualifierDefinition41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_PredefinedDataTypeDefinition40"):
                opp_val = getattr(old_value, "dbdefinition_PredefinedDataTypeDefinition40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_PredefinedDataTypeDefinition40"):
                opp_val = getattr(value, "dbdefinition_PredefinedDataTypeDefinition40", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_PredefinedDataTypeDefinition40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbdefinition_FieldQualifierDefinition44(self):
        return self.__dbdefinition_FieldQualifierDefinition44

    @dbdefinition_FieldQualifierDefinition44.setter
    def dbdefinition_FieldQualifierDefinition44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_FieldQualifierDefinition__dbdefinition_FieldQualifierDefinition44", None)
        self.__dbdefinition_FieldQualifierDefinition44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_PredefinedDataTypeDefinition43"):
                opp_val = getattr(old_value, "dbdefinition_PredefinedDataTypeDefinition43", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_PredefinedDataTypeDefinition43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_PredefinedDataTypeDefinition43"):
                opp_val = getattr(value, "dbdefinition_PredefinedDataTypeDefinition43", None)
                setattr(value, "dbdefinition_PredefinedDataTypeDefinition43", self)

    @property
    def dbdefinition_FieldQualifierDefinition(self):
        return self.__dbdefinition_FieldQualifierDefinition

    @dbdefinition_FieldQualifierDefinition.setter
    def dbdefinition_FieldQualifierDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_FieldQualifierDefinition__dbdefinition_FieldQualifierDefinition", None)
        self.__dbdefinition_FieldQualifierDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_PredefinedDataTypeDefinition38"):
                opp_val = getattr(old_value, "dbdefinition_PredefinedDataTypeDefinition38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_PredefinedDataTypeDefinition38"):
                opp_val = getattr(value, "dbdefinition_PredefinedDataTypeDefinition38", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_PredefinedDataTypeDefinition38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbdefinition_ConstructedDataTypeDefinition:

    def __init__(self, arrayDatatypeSupported: bool, multisetDatatypeSupported: bool, rowDatatypeSupported: bool, referenceDatatypeSupported: bool, cursorDatatypeSupported: bool, dbdefinition_ConstructedDataTypeDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.arrayDatatypeSupported = arrayDatatypeSupported
        self.multisetDatatypeSupported = multisetDatatypeSupported
        self.rowDatatypeSupported = rowDatatypeSupported
        self.referenceDatatypeSupported = referenceDatatypeSupported
        self.cursorDatatypeSupported = cursorDatatypeSupported
        self.dbdefinition_ConstructedDataTypeDefinition = dbdefinition_ConstructedDataTypeDefinition
        
        pass
    @property
    def referenceDatatypeSupported(self):
        return self.__referenceDatatypeSupported

    @referenceDatatypeSupported.setter
    def referenceDatatypeSupported(self, referenceDatatypeSupported: bool):
        self.__referenceDatatypeSupported = referenceDatatypeSupported


    @property
    def multisetDatatypeSupported(self):
        return self.__multisetDatatypeSupported

    @multisetDatatypeSupported.setter
    def multisetDatatypeSupported(self, multisetDatatypeSupported: bool):
        self.__multisetDatatypeSupported = multisetDatatypeSupported


    @property
    def cursorDatatypeSupported(self):
        return self.__cursorDatatypeSupported

    @cursorDatatypeSupported.setter
    def cursorDatatypeSupported(self, cursorDatatypeSupported: bool):
        self.__cursorDatatypeSupported = cursorDatatypeSupported


    @property
    def rowDatatypeSupported(self):
        return self.__rowDatatypeSupported

    @rowDatatypeSupported.setter
    def rowDatatypeSupported(self, rowDatatypeSupported: bool):
        self.__rowDatatypeSupported = rowDatatypeSupported


    @property
    def arrayDatatypeSupported(self):
        return self.__arrayDatatypeSupported

    @arrayDatatypeSupported.setter
    def arrayDatatypeSupported(self, arrayDatatypeSupported: bool):
        self.__arrayDatatypeSupported = arrayDatatypeSupported


    @property
    def dbdefinition_ConstructedDataTypeDefinition(self):
        return self.__dbdefinition_ConstructedDataTypeDefinition

    @dbdefinition_ConstructedDataTypeDefinition.setter
    def dbdefinition_ConstructedDataTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_ConstructedDataTypeDefinition__dbdefinition_ConstructedDataTypeDefinition", None)
        self.__dbdefinition_ConstructedDataTypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition36"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition36", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition36"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition36", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition36", self)

class dbdefinition_PrivilegedElementDefinition:

    def __init__(self, name: str, dbdefinition_PrivilegedElementDefinition: "dbdefinition_DatabaseVendorDefinition" = None, dbdefinition_PrivilegedElementDefinition64: set["dbdefinition_PrivilegeDefinition"] = None, dbdefinition_PrivilegedElementDefinition67: "dbdefinition_PrivilegeDefinition" = None):
        self.name = name
        self.dbdefinition_PrivilegedElementDefinition = dbdefinition_PrivilegedElementDefinition
        self.dbdefinition_PrivilegedElementDefinition64 = dbdefinition_PrivilegedElementDefinition64 if dbdefinition_PrivilegedElementDefinition64 is not None else set()
        self.dbdefinition_PrivilegedElementDefinition67 = dbdefinition_PrivilegedElementDefinition67
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def dbdefinition_PrivilegedElementDefinition67(self):
        return self.__dbdefinition_PrivilegedElementDefinition67

    @dbdefinition_PrivilegedElementDefinition67.setter
    def dbdefinition_PrivilegedElementDefinition67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PrivilegedElementDefinition__dbdefinition_PrivilegedElementDefinition67", None)
        self.__dbdefinition_PrivilegedElementDefinition67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_PrivilegeDefinition66"):
                opp_val = getattr(old_value, "dbdefinition_PrivilegeDefinition66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_PrivilegeDefinition66"):
                opp_val = getattr(value, "dbdefinition_PrivilegeDefinition66", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_PrivilegeDefinition66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbdefinition_PrivilegedElementDefinition64(self):
        return self.__dbdefinition_PrivilegedElementDefinition64

    @dbdefinition_PrivilegedElementDefinition64.setter
    def dbdefinition_PrivilegedElementDefinition64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PrivilegedElementDefinition__dbdefinition_PrivilegedElementDefinition64", None)
        self.__dbdefinition_PrivilegedElementDefinition64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_PrivilegeDefinition"):
                    opp_val = getattr(item, "dbdefinition_PrivilegeDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_PrivilegeDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_PrivilegeDefinition"):
                    opp_val = getattr(item, "dbdefinition_PrivilegeDefinition", None)
                    
                    setattr(item, "dbdefinition_PrivilegeDefinition", self)
                    

    @property
    def dbdefinition_PrivilegedElementDefinition(self):
        return self.__dbdefinition_PrivilegedElementDefinition

    @dbdefinition_PrivilegedElementDefinition.setter
    def dbdefinition_PrivilegedElementDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PrivilegedElementDefinition__dbdefinition_PrivilegedElementDefinition", None)
        self.__dbdefinition_PrivilegedElementDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition34"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition34"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition34", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_DatabaseVendorDefinition34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbdefinition_DebuggerDefinition:

    def __init__(self, conditionSupported: bool, dbdefinition_DebuggerDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.conditionSupported = conditionSupported
        self.dbdefinition_DebuggerDefinition = dbdefinition_DebuggerDefinition
        
        pass
    @property
    def conditionSupported(self):
        return self.__conditionSupported

    @conditionSupported.setter
    def conditionSupported(self, conditionSupported: bool):
        self.__conditionSupported = conditionSupported


    @property
    def dbdefinition_DebuggerDefinition(self):
        return self.__dbdefinition_DebuggerDefinition

    @dbdefinition_DebuggerDefinition.setter
    def dbdefinition_DebuggerDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DebuggerDefinition__dbdefinition_DebuggerDefinition", None)
        self.__dbdefinition_DebuggerDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition32"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition32", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition32"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition32", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition32", self)

class dbdefinition_ViewDefinition:

    def __init__(self, maximumIdentifierLength: int, indexSupported: bool, checkOptionSupported: bool, checkOptionLevelsSupported: bool, dbdefinition_ViewDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.maximumIdentifierLength = maximumIdentifierLength
        self.indexSupported = indexSupported
        self.checkOptionSupported = checkOptionSupported
        self.checkOptionLevelsSupported = checkOptionLevelsSupported
        self.dbdefinition_ViewDefinition = dbdefinition_ViewDefinition
        
        pass
    @property
    def checkOptionLevelsSupported(self):
        return self.__checkOptionLevelsSupported

    @checkOptionLevelsSupported.setter
    def checkOptionLevelsSupported(self, checkOptionLevelsSupported: bool):
        self.__checkOptionLevelsSupported = checkOptionLevelsSupported


    @property
    def indexSupported(self):
        return self.__indexSupported

    @indexSupported.setter
    def indexSupported(self, indexSupported: bool):
        self.__indexSupported = indexSupported


    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def checkOptionSupported(self):
        return self.__checkOptionSupported

    @checkOptionSupported.setter
    def checkOptionSupported(self, checkOptionSupported: bool):
        self.__checkOptionSupported = checkOptionSupported


    @property
    def dbdefinition_ViewDefinition(self):
        return self.__dbdefinition_ViewDefinition

    @dbdefinition_ViewDefinition.setter
    def dbdefinition_ViewDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_ViewDefinition__dbdefinition_ViewDefinition", None)
        self.__dbdefinition_ViewDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition30"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition30", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition30"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition30", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition30", self)

class dbdefinition_SchemaDefinition:

    def __init__(self, maximumIdentifierLength: int, dbdefinition_SchemaDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.maximumIdentifierLength = maximumIdentifierLength
        self.dbdefinition_SchemaDefinition = dbdefinition_SchemaDefinition
        
        pass
    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def dbdefinition_SchemaDefinition(self):
        return self.__dbdefinition_SchemaDefinition

    @dbdefinition_SchemaDefinition.setter
    def dbdefinition_SchemaDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_SchemaDefinition__dbdefinition_SchemaDefinition", None)
        self.__dbdefinition_SchemaDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition28"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition28", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition28"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition28", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition28", self)

class dbdefinition_SequenceDefinition:

    def __init__(self, typeEnumerationSupported: bool, cacheSupported: bool, orderSupported: bool, noMaximumValueString: str, noMinimumValueString: str, noCacheString: str, cacheDefaultValue: int, dbdefinition_SequenceDefinition: "dbdefinition_DatabaseVendorDefinition" = None, dbdefinition_SequenceDefinition55: set["dbdefinition_PredefinedDataTypeDefinition"] = None, dbdefinition_SequenceDefinition58: "dbdefinition_PredefinedDataTypeDefinition" = None):
        self.typeEnumerationSupported = typeEnumerationSupported
        self.cacheSupported = cacheSupported
        self.orderSupported = orderSupported
        self.noMaximumValueString = noMaximumValueString
        self.noMinimumValueString = noMinimumValueString
        self.noCacheString = noCacheString
        self.cacheDefaultValue = cacheDefaultValue
        self.dbdefinition_SequenceDefinition = dbdefinition_SequenceDefinition
        self.dbdefinition_SequenceDefinition55 = dbdefinition_SequenceDefinition55 if dbdefinition_SequenceDefinition55 is not None else set()
        self.dbdefinition_SequenceDefinition58 = dbdefinition_SequenceDefinition58
        
        pass
    @property
    def noCacheString(self):
        return self.__noCacheString

    @noCacheString.setter
    def noCacheString(self, noCacheString: str):
        self.__noCacheString = noCacheString


    @property
    def cacheSupported(self):
        return self.__cacheSupported

    @cacheSupported.setter
    def cacheSupported(self, cacheSupported: bool):
        self.__cacheSupported = cacheSupported


    @property
    def noMaximumValueString(self):
        return self.__noMaximumValueString

    @noMaximumValueString.setter
    def noMaximumValueString(self, noMaximumValueString: str):
        self.__noMaximumValueString = noMaximumValueString


    @property
    def noMinimumValueString(self):
        return self.__noMinimumValueString

    @noMinimumValueString.setter
    def noMinimumValueString(self, noMinimumValueString: str):
        self.__noMinimumValueString = noMinimumValueString


    @property
    def cacheDefaultValue(self):
        return self.__cacheDefaultValue

    @cacheDefaultValue.setter
    def cacheDefaultValue(self, cacheDefaultValue: int):
        self.__cacheDefaultValue = cacheDefaultValue


    @property
    def typeEnumerationSupported(self):
        return self.__typeEnumerationSupported

    @typeEnumerationSupported.setter
    def typeEnumerationSupported(self, typeEnumerationSupported: bool):
        self.__typeEnumerationSupported = typeEnumerationSupported


    @property
    def orderSupported(self):
        return self.__orderSupported

    @orderSupported.setter
    def orderSupported(self, orderSupported: bool):
        self.__orderSupported = orderSupported


    @property
    def dbdefinition_SequenceDefinition(self):
        return self.__dbdefinition_SequenceDefinition

    @dbdefinition_SequenceDefinition.setter
    def dbdefinition_SequenceDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_SequenceDefinition__dbdefinition_SequenceDefinition", None)
        self.__dbdefinition_SequenceDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition18"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition18", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition18"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition18", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition18", self)

    @property
    def dbdefinition_SequenceDefinition55(self):
        return self.__dbdefinition_SequenceDefinition55

    @dbdefinition_SequenceDefinition55.setter
    def dbdefinition_SequenceDefinition55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_SequenceDefinition__dbdefinition_SequenceDefinition55", None)
        self.__dbdefinition_SequenceDefinition55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_PredefinedDataTypeDefinition56"):
                    opp_val = getattr(item, "dbdefinition_PredefinedDataTypeDefinition56", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_PredefinedDataTypeDefinition56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_PredefinedDataTypeDefinition56"):
                    opp_val = getattr(item, "dbdefinition_PredefinedDataTypeDefinition56", None)
                    
                    setattr(item, "dbdefinition_PredefinedDataTypeDefinition56", self)
                    

    @property
    def dbdefinition_SequenceDefinition58(self):
        return self.__dbdefinition_SequenceDefinition58

    @dbdefinition_SequenceDefinition58.setter
    def dbdefinition_SequenceDefinition58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_SequenceDefinition__dbdefinition_SequenceDefinition58", None)
        self.__dbdefinition_SequenceDefinition58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_PredefinedDataTypeDefinition59"):
                opp_val = getattr(old_value, "dbdefinition_PredefinedDataTypeDefinition59", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_PredefinedDataTypeDefinition59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_PredefinedDataTypeDefinition59"):
                opp_val = getattr(value, "dbdefinition_PredefinedDataTypeDefinition59", None)
                setattr(value, "dbdefinition_PredefinedDataTypeDefinition59", self)

class dbdefinition_TableDefinition:

    def __init__(self, maximumIdentifierLength: int, auditSupported: bool, dataCaptureSupported: bool, editProcSupported: bool, encodingSupported: bool, validProcSupported: bool, dbdefinition_TableDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.maximumIdentifierLength = maximumIdentifierLength
        self.auditSupported = auditSupported
        self.dataCaptureSupported = dataCaptureSupported
        self.editProcSupported = editProcSupported
        self.encodingSupported = encodingSupported
        self.validProcSupported = validProcSupported
        self.dbdefinition_TableDefinition = dbdefinition_TableDefinition
        
        pass
    @property
    def validProcSupported(self):
        return self.__validProcSupported

    @validProcSupported.setter
    def validProcSupported(self, validProcSupported: bool):
        self.__validProcSupported = validProcSupported


    @property
    def dataCaptureSupported(self):
        return self.__dataCaptureSupported

    @dataCaptureSupported.setter
    def dataCaptureSupported(self, dataCaptureSupported: bool):
        self.__dataCaptureSupported = dataCaptureSupported


    @property
    def editProcSupported(self):
        return self.__editProcSupported

    @editProcSupported.setter
    def editProcSupported(self, editProcSupported: bool):
        self.__editProcSupported = editProcSupported


    @property
    def encodingSupported(self):
        return self.__encodingSupported

    @encodingSupported.setter
    def encodingSupported(self, encodingSupported: bool):
        self.__encodingSupported = encodingSupported


    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def auditSupported(self):
        return self.__auditSupported

    @auditSupported.setter
    def auditSupported(self, auditSupported: bool):
        self.__auditSupported = auditSupported


    @property
    def dbdefinition_TableDefinition(self):
        return self.__dbdefinition_TableDefinition

    @dbdefinition_TableDefinition.setter
    def dbdefinition_TableDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_TableDefinition__dbdefinition_TableDefinition", None)
        self.__dbdefinition_TableDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition16"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition16", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition16"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition16", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition16", self)

class dbdefinition_IndexDefinition:

    def __init__(self, percentFreeTerminology: str, percentFreeChangeable: bool, clusteringSupported: bool, clusterChangeable: bool, fillFactorSupported: bool, includedColumnsSupported: bool, maximumIdentifierLength: int, dbdefinition_IndexDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.percentFreeTerminology = percentFreeTerminology
        self.percentFreeChangeable = percentFreeChangeable
        self.clusteringSupported = clusteringSupported
        self.clusterChangeable = clusterChangeable
        self.fillFactorSupported = fillFactorSupported
        self.includedColumnsSupported = includedColumnsSupported
        self.maximumIdentifierLength = maximumIdentifierLength
        self.dbdefinition_IndexDefinition = dbdefinition_IndexDefinition
        
        pass
    @property
    def clusterChangeable(self):
        return self.__clusterChangeable

    @clusterChangeable.setter
    def clusterChangeable(self, clusterChangeable: bool):
        self.__clusterChangeable = clusterChangeable


    @property
    def clusteringSupported(self):
        return self.__clusteringSupported

    @clusteringSupported.setter
    def clusteringSupported(self, clusteringSupported: bool):
        self.__clusteringSupported = clusteringSupported


    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def fillFactorSupported(self):
        return self.__fillFactorSupported

    @fillFactorSupported.setter
    def fillFactorSupported(self, fillFactorSupported: bool):
        self.__fillFactorSupported = fillFactorSupported


    @property
    def percentFreeChangeable(self):
        return self.__percentFreeChangeable

    @percentFreeChangeable.setter
    def percentFreeChangeable(self, percentFreeChangeable: bool):
        self.__percentFreeChangeable = percentFreeChangeable


    @property
    def includedColumnsSupported(self):
        return self.__includedColumnsSupported

    @includedColumnsSupported.setter
    def includedColumnsSupported(self, includedColumnsSupported: bool):
        self.__includedColumnsSupported = includedColumnsSupported


    @property
    def percentFreeTerminology(self):
        return self.__percentFreeTerminology

    @percentFreeTerminology.setter
    def percentFreeTerminology(self, percentFreeTerminology: str):
        self.__percentFreeTerminology = percentFreeTerminology


    @property
    def dbdefinition_IndexDefinition(self):
        return self.__dbdefinition_IndexDefinition

    @dbdefinition_IndexDefinition.setter
    def dbdefinition_IndexDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_IndexDefinition__dbdefinition_IndexDefinition", None)
        self.__dbdefinition_IndexDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition14"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition14", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition14"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition14", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition14", self)

class dbdefinition_ExtendedDefinition:

    def __init__(self, name: str, value: str, dbdefinition_ExtendedDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.name = name
        self.value = value
        self.dbdefinition_ExtendedDefinition = dbdefinition_ExtendedDefinition
        
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
    def value(self, value: str):
        self.__value = value


    @property
    def dbdefinition_ExtendedDefinition(self):
        return self.__dbdefinition_ExtendedDefinition

    @dbdefinition_ExtendedDefinition.setter
    def dbdefinition_ExtendedDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_ExtendedDefinition__dbdefinition_ExtendedDefinition", None)
        self.__dbdefinition_ExtendedDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition12"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition12"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition12", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_DatabaseVendorDefinition12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dbdefinition_ConstraintDefinition:

    def __init__(self, deferrableConstraintSupported: bool, informationalConstraintSupported: bool, clusteredPrimaryKeySupported: bool, clusteredUniqueConstraintSupported: bool, primaryKeyNullable: bool, uniqueKeyNullable: bool, maximumCheckExpressionLength: int, parentUpdateDRIRuleType: str, parentDeleteDRIRuleType: str, checkOption: str, maximumPrimaryKeyIdentifierLength: int, maximumForeignKeyIdentifierLength: int, maximumCheckConstraintIdentifierLength: int, dbdefinition_ConstraintDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.deferrableConstraintSupported = deferrableConstraintSupported
        self.informationalConstraintSupported = informationalConstraintSupported
        self.clusteredPrimaryKeySupported = clusteredPrimaryKeySupported
        self.clusteredUniqueConstraintSupported = clusteredUniqueConstraintSupported
        self.primaryKeyNullable = primaryKeyNullable
        self.uniqueKeyNullable = uniqueKeyNullable
        self.maximumCheckExpressionLength = maximumCheckExpressionLength
        self.parentUpdateDRIRuleType = parentUpdateDRIRuleType
        self.parentDeleteDRIRuleType = parentDeleteDRIRuleType
        self.checkOption = checkOption
        self.maximumPrimaryKeyIdentifierLength = maximumPrimaryKeyIdentifierLength
        self.maximumForeignKeyIdentifierLength = maximumForeignKeyIdentifierLength
        self.maximumCheckConstraintIdentifierLength = maximumCheckConstraintIdentifierLength
        self.dbdefinition_ConstraintDefinition = dbdefinition_ConstraintDefinition
        
        pass
    @property
    def checkOption(self):
        return self.__checkOption

    @checkOption.setter
    def checkOption(self, checkOption: str):
        self.__checkOption = checkOption


    @property
    def informationalConstraintSupported(self):
        return self.__informationalConstraintSupported

    @informationalConstraintSupported.setter
    def informationalConstraintSupported(self, informationalConstraintSupported: bool):
        self.__informationalConstraintSupported = informationalConstraintSupported


    @property
    def clusteredUniqueConstraintSupported(self):
        return self.__clusteredUniqueConstraintSupported

    @clusteredUniqueConstraintSupported.setter
    def clusteredUniqueConstraintSupported(self, clusteredUniqueConstraintSupported: bool):
        self.__clusteredUniqueConstraintSupported = clusteredUniqueConstraintSupported


    @property
    def maximumCheckExpressionLength(self):
        return self.__maximumCheckExpressionLength

    @maximumCheckExpressionLength.setter
    def maximumCheckExpressionLength(self, maximumCheckExpressionLength: int):
        self.__maximumCheckExpressionLength = maximumCheckExpressionLength


    @property
    def maximumPrimaryKeyIdentifierLength(self):
        return self.__maximumPrimaryKeyIdentifierLength

    @maximumPrimaryKeyIdentifierLength.setter
    def maximumPrimaryKeyIdentifierLength(self, maximumPrimaryKeyIdentifierLength: int):
        self.__maximumPrimaryKeyIdentifierLength = maximumPrimaryKeyIdentifierLength


    @property
    def parentDeleteDRIRuleType(self):
        return self.__parentDeleteDRIRuleType

    @parentDeleteDRIRuleType.setter
    def parentDeleteDRIRuleType(self, parentDeleteDRIRuleType: str):
        self.__parentDeleteDRIRuleType = parentDeleteDRIRuleType


    @property
    def parentUpdateDRIRuleType(self):
        return self.__parentUpdateDRIRuleType

    @parentUpdateDRIRuleType.setter
    def parentUpdateDRIRuleType(self, parentUpdateDRIRuleType: str):
        self.__parentUpdateDRIRuleType = parentUpdateDRIRuleType


    @property
    def maximumCheckConstraintIdentifierLength(self):
        return self.__maximumCheckConstraintIdentifierLength

    @maximumCheckConstraintIdentifierLength.setter
    def maximumCheckConstraintIdentifierLength(self, maximumCheckConstraintIdentifierLength: int):
        self.__maximumCheckConstraintIdentifierLength = maximumCheckConstraintIdentifierLength


    @property
    def maximumForeignKeyIdentifierLength(self):
        return self.__maximumForeignKeyIdentifierLength

    @maximumForeignKeyIdentifierLength.setter
    def maximumForeignKeyIdentifierLength(self, maximumForeignKeyIdentifierLength: int):
        self.__maximumForeignKeyIdentifierLength = maximumForeignKeyIdentifierLength


    @property
    def deferrableConstraintSupported(self):
        return self.__deferrableConstraintSupported

    @deferrableConstraintSupported.setter
    def deferrableConstraintSupported(self, deferrableConstraintSupported: bool):
        self.__deferrableConstraintSupported = deferrableConstraintSupported


    @property
    def clusteredPrimaryKeySupported(self):
        return self.__clusteredPrimaryKeySupported

    @clusteredPrimaryKeySupported.setter
    def clusteredPrimaryKeySupported(self, clusteredPrimaryKeySupported: bool):
        self.__clusteredPrimaryKeySupported = clusteredPrimaryKeySupported


    @property
    def uniqueKeyNullable(self):
        return self.__uniqueKeyNullable

    @uniqueKeyNullable.setter
    def uniqueKeyNullable(self, uniqueKeyNullable: bool):
        self.__uniqueKeyNullable = uniqueKeyNullable


    @property
    def primaryKeyNullable(self):
        return self.__primaryKeyNullable

    @primaryKeyNullable.setter
    def primaryKeyNullable(self, primaryKeyNullable: bool):
        self.__primaryKeyNullable = primaryKeyNullable


    @property
    def dbdefinition_ConstraintDefinition(self):
        return self.__dbdefinition_ConstraintDefinition

    @dbdefinition_ConstraintDefinition.setter
    def dbdefinition_ConstraintDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_ConstraintDefinition__dbdefinition_ConstraintDefinition", None)
        self.__dbdefinition_ConstraintDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition10"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition10", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition10"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition10", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition10", self)

class dbdefinition_ColumnDefinition:

    def __init__(self, identityStartValueSupported: bool, identityIncrementSupported: bool, identityMinimumSupported: bool, identityMaximumSupported: bool, identityCycleSupported: bool, maximumIdentifierLength: int, identitySupported: bool, computedSupported: bool, dbdefinition_ColumnDefinition: "dbdefinition_DatabaseVendorDefinition" = None, dbdefinition_ColumnDefinition52: set["dbdefinition_PredefinedDataTypeDefinition"] = None):
        self.identityStartValueSupported = identityStartValueSupported
        self.identityIncrementSupported = identityIncrementSupported
        self.identityMinimumSupported = identityMinimumSupported
        self.identityMaximumSupported = identityMaximumSupported
        self.identityCycleSupported = identityCycleSupported
        self.maximumIdentifierLength = maximumIdentifierLength
        self.identitySupported = identitySupported
        self.computedSupported = computedSupported
        self.dbdefinition_ColumnDefinition = dbdefinition_ColumnDefinition
        self.dbdefinition_ColumnDefinition52 = dbdefinition_ColumnDefinition52 if dbdefinition_ColumnDefinition52 is not None else set()
        
        pass
    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def computedSupported(self):
        return self.__computedSupported

    @computedSupported.setter
    def computedSupported(self, computedSupported: bool):
        self.__computedSupported = computedSupported


    @property
    def identityMinimumSupported(self):
        return self.__identityMinimumSupported

    @identityMinimumSupported.setter
    def identityMinimumSupported(self, identityMinimumSupported: bool):
        self.__identityMinimumSupported = identityMinimumSupported


    @property
    def identityStartValueSupported(self):
        return self.__identityStartValueSupported

    @identityStartValueSupported.setter
    def identityStartValueSupported(self, identityStartValueSupported: bool):
        self.__identityStartValueSupported = identityStartValueSupported


    @property
    def identityMaximumSupported(self):
        return self.__identityMaximumSupported

    @identityMaximumSupported.setter
    def identityMaximumSupported(self, identityMaximumSupported: bool):
        self.__identityMaximumSupported = identityMaximumSupported


    @property
    def identitySupported(self):
        return self.__identitySupported

    @identitySupported.setter
    def identitySupported(self, identitySupported: bool):
        self.__identitySupported = identitySupported


    @property
    def identityCycleSupported(self):
        return self.__identityCycleSupported

    @identityCycleSupported.setter
    def identityCycleSupported(self, identityCycleSupported: bool):
        self.__identityCycleSupported = identityCycleSupported


    @property
    def identityIncrementSupported(self):
        return self.__identityIncrementSupported

    @identityIncrementSupported.setter
    def identityIncrementSupported(self, identityIncrementSupported: bool):
        self.__identityIncrementSupported = identityIncrementSupported


    @property
    def dbdefinition_ColumnDefinition52(self):
        return self.__dbdefinition_ColumnDefinition52

    @dbdefinition_ColumnDefinition52.setter
    def dbdefinition_ColumnDefinition52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_ColumnDefinition__dbdefinition_ColumnDefinition52", None)
        self.__dbdefinition_ColumnDefinition52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_PredefinedDataTypeDefinition53"):
                    opp_val = getattr(item, "dbdefinition_PredefinedDataTypeDefinition53", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_PredefinedDataTypeDefinition53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_PredefinedDataTypeDefinition53"):
                    opp_val = getattr(item, "dbdefinition_PredefinedDataTypeDefinition53", None)
                    
                    setattr(item, "dbdefinition_PredefinedDataTypeDefinition53", self)
                    

    @property
    def dbdefinition_ColumnDefinition(self):
        return self.__dbdefinition_ColumnDefinition

    @dbdefinition_ColumnDefinition.setter
    def dbdefinition_ColumnDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_ColumnDefinition__dbdefinition_ColumnDefinition", None)
        self.__dbdefinition_ColumnDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition8"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition8", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition8"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition8", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition8", self)

class dbdefinition_TriggerDefinition:

    def __init__(self, maximumReferencePartLength: int, maximumActionBodyLength: int, typeSupported: bool, whenClauseSupported: bool, granularitySupported: bool, referencesClauseSupported: bool, perColumnUpdateTriggerSupported: bool, insteadOfTriggerSupported: bool, rowTriggerReferenceSupported: bool, tableTriggerReferenceSupported: bool, maximumIdentifierLength: int, dbdefinition_TriggerDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.maximumReferencePartLength = maximumReferencePartLength
        self.maximumActionBodyLength = maximumActionBodyLength
        self.typeSupported = typeSupported
        self.whenClauseSupported = whenClauseSupported
        self.granularitySupported = granularitySupported
        self.referencesClauseSupported = referencesClauseSupported
        self.perColumnUpdateTriggerSupported = perColumnUpdateTriggerSupported
        self.insteadOfTriggerSupported = insteadOfTriggerSupported
        self.rowTriggerReferenceSupported = rowTriggerReferenceSupported
        self.tableTriggerReferenceSupported = tableTriggerReferenceSupported
        self.maximumIdentifierLength = maximumIdentifierLength
        self.dbdefinition_TriggerDefinition = dbdefinition_TriggerDefinition
        
        pass
    @property
    def whenClauseSupported(self):
        return self.__whenClauseSupported

    @whenClauseSupported.setter
    def whenClauseSupported(self, whenClauseSupported: bool):
        self.__whenClauseSupported = whenClauseSupported


    @property
    def insteadOfTriggerSupported(self):
        return self.__insteadOfTriggerSupported

    @insteadOfTriggerSupported.setter
    def insteadOfTriggerSupported(self, insteadOfTriggerSupported: bool):
        self.__insteadOfTriggerSupported = insteadOfTriggerSupported


    @property
    def tableTriggerReferenceSupported(self):
        return self.__tableTriggerReferenceSupported

    @tableTriggerReferenceSupported.setter
    def tableTriggerReferenceSupported(self, tableTriggerReferenceSupported: bool):
        self.__tableTriggerReferenceSupported = tableTriggerReferenceSupported


    @property
    def rowTriggerReferenceSupported(self):
        return self.__rowTriggerReferenceSupported

    @rowTriggerReferenceSupported.setter
    def rowTriggerReferenceSupported(self, rowTriggerReferenceSupported: bool):
        self.__rowTriggerReferenceSupported = rowTriggerReferenceSupported


    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def maximumActionBodyLength(self):
        return self.__maximumActionBodyLength

    @maximumActionBodyLength.setter
    def maximumActionBodyLength(self, maximumActionBodyLength: int):
        self.__maximumActionBodyLength = maximumActionBodyLength


    @property
    def referencesClauseSupported(self):
        return self.__referencesClauseSupported

    @referencesClauseSupported.setter
    def referencesClauseSupported(self, referencesClauseSupported: bool):
        self.__referencesClauseSupported = referencesClauseSupported


    @property
    def maximumReferencePartLength(self):
        return self.__maximumReferencePartLength

    @maximumReferencePartLength.setter
    def maximumReferencePartLength(self, maximumReferencePartLength: int):
        self.__maximumReferencePartLength = maximumReferencePartLength


    @property
    def perColumnUpdateTriggerSupported(self):
        return self.__perColumnUpdateTriggerSupported

    @perColumnUpdateTriggerSupported.setter
    def perColumnUpdateTriggerSupported(self, perColumnUpdateTriggerSupported: bool):
        self.__perColumnUpdateTriggerSupported = perColumnUpdateTriggerSupported


    @property
    def typeSupported(self):
        return self.__typeSupported

    @typeSupported.setter
    def typeSupported(self, typeSupported: bool):
        self.__typeSupported = typeSupported


    @property
    def granularitySupported(self):
        return self.__granularitySupported

    @granularitySupported.setter
    def granularitySupported(self, granularitySupported: bool):
        self.__granularitySupported = granularitySupported


    @property
    def dbdefinition_TriggerDefinition(self):
        return self.__dbdefinition_TriggerDefinition

    @dbdefinition_TriggerDefinition.setter
    def dbdefinition_TriggerDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_TriggerDefinition__dbdefinition_TriggerDefinition", None)
        self.__dbdefinition_TriggerDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition6"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition6", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition6"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition6", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition6", self)

class dbdefinition_StoredProcedureDefinition:

    def __init__(self, nullInputActionSupported: bool, packageGenerationSupported: bool, determininsticSupported: bool, returnedNullSupported: bool, returnedTypeDeclarationConstraintSupported: bool, parameterInitValueSupported: bool, parameterStyleSupported: bool, returnTypeSupported: bool, parameterDeclarationConstraintSupported: bool, maximumActionBodyLength: int, parameterStyle: str, languageType: str, functionLanguageType: str, procedureType: str, maximumIdentifierLength: int, dbdefinition_StoredProcedureDefinition: "dbdefinition_DatabaseVendorDefinition" = None, dbdefinition_StoredProcedureDefinition49: set["dbdefinition_PredefinedDataTypeDefinition"] = None):
        self.nullInputActionSupported = nullInputActionSupported
        self.packageGenerationSupported = packageGenerationSupported
        self.determininsticSupported = determininsticSupported
        self.returnedNullSupported = returnedNullSupported
        self.returnedTypeDeclarationConstraintSupported = returnedTypeDeclarationConstraintSupported
        self.parameterInitValueSupported = parameterInitValueSupported
        self.parameterStyleSupported = parameterStyleSupported
        self.returnTypeSupported = returnTypeSupported
        self.parameterDeclarationConstraintSupported = parameterDeclarationConstraintSupported
        self.maximumActionBodyLength = maximumActionBodyLength
        self.parameterStyle = parameterStyle
        self.languageType = languageType
        self.functionLanguageType = functionLanguageType
        self.procedureType = procedureType
        self.maximumIdentifierLength = maximumIdentifierLength
        self.dbdefinition_StoredProcedureDefinition = dbdefinition_StoredProcedureDefinition
        self.dbdefinition_StoredProcedureDefinition49 = dbdefinition_StoredProcedureDefinition49 if dbdefinition_StoredProcedureDefinition49 is not None else set()
        
        pass
    @property
    def parameterInitValueSupported(self):
        return self.__parameterInitValueSupported

    @parameterInitValueSupported.setter
    def parameterInitValueSupported(self, parameterInitValueSupported: bool):
        self.__parameterInitValueSupported = parameterInitValueSupported


    @property
    def nullInputActionSupported(self):
        return self.__nullInputActionSupported

    @nullInputActionSupported.setter
    def nullInputActionSupported(self, nullInputActionSupported: bool):
        self.__nullInputActionSupported = nullInputActionSupported


    @property
    def returnTypeSupported(self):
        return self.__returnTypeSupported

    @returnTypeSupported.setter
    def returnTypeSupported(self, returnTypeSupported: bool):
        self.__returnTypeSupported = returnTypeSupported


    @property
    def determininsticSupported(self):
        return self.__determininsticSupported

    @determininsticSupported.setter
    def determininsticSupported(self, determininsticSupported: bool):
        self.__determininsticSupported = determininsticSupported


    @property
    def maximumActionBodyLength(self):
        return self.__maximumActionBodyLength

    @maximumActionBodyLength.setter
    def maximumActionBodyLength(self, maximumActionBodyLength: int):
        self.__maximumActionBodyLength = maximumActionBodyLength


    @property
    def languageType(self):
        return self.__languageType

    @languageType.setter
    def languageType(self, languageType: str):
        self.__languageType = languageType


    @property
    def parameterDeclarationConstraintSupported(self):
        return self.__parameterDeclarationConstraintSupported

    @parameterDeclarationConstraintSupported.setter
    def parameterDeclarationConstraintSupported(self, parameterDeclarationConstraintSupported: bool):
        self.__parameterDeclarationConstraintSupported = parameterDeclarationConstraintSupported


    @property
    def parameterStyleSupported(self):
        return self.__parameterStyleSupported

    @parameterStyleSupported.setter
    def parameterStyleSupported(self, parameterStyleSupported: bool):
        self.__parameterStyleSupported = parameterStyleSupported


    @property
    def returnedTypeDeclarationConstraintSupported(self):
        return self.__returnedTypeDeclarationConstraintSupported

    @returnedTypeDeclarationConstraintSupported.setter
    def returnedTypeDeclarationConstraintSupported(self, returnedTypeDeclarationConstraintSupported: bool):
        self.__returnedTypeDeclarationConstraintSupported = returnedTypeDeclarationConstraintSupported


    @property
    def functionLanguageType(self):
        return self.__functionLanguageType

    @functionLanguageType.setter
    def functionLanguageType(self, functionLanguageType: str):
        self.__functionLanguageType = functionLanguageType


    @property
    def returnedNullSupported(self):
        return self.__returnedNullSupported

    @returnedNullSupported.setter
    def returnedNullSupported(self, returnedNullSupported: bool):
        self.__returnedNullSupported = returnedNullSupported


    @property
    def procedureType(self):
        return self.__procedureType

    @procedureType.setter
    def procedureType(self, procedureType: str):
        self.__procedureType = procedureType


    @property
    def packageGenerationSupported(self):
        return self.__packageGenerationSupported

    @packageGenerationSupported.setter
    def packageGenerationSupported(self, packageGenerationSupported: bool):
        self.__packageGenerationSupported = packageGenerationSupported


    @property
    def parameterStyle(self):
        return self.__parameterStyle

    @parameterStyle.setter
    def parameterStyle(self, parameterStyle: str):
        self.__parameterStyle = parameterStyle


    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def dbdefinition_StoredProcedureDefinition(self):
        return self.__dbdefinition_StoredProcedureDefinition

    @dbdefinition_StoredProcedureDefinition.setter
    def dbdefinition_StoredProcedureDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_StoredProcedureDefinition__dbdefinition_StoredProcedureDefinition", None)
        self.__dbdefinition_StoredProcedureDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition4"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition4", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition4"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition4", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition4", self)

    @property
    def dbdefinition_StoredProcedureDefinition49(self):
        return self.__dbdefinition_StoredProcedureDefinition49

    @dbdefinition_StoredProcedureDefinition49.setter
    def dbdefinition_StoredProcedureDefinition49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_StoredProcedureDefinition__dbdefinition_StoredProcedureDefinition49", None)
        self.__dbdefinition_StoredProcedureDefinition49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_PredefinedDataTypeDefinition50"):
                    opp_val = getattr(item, "dbdefinition_PredefinedDataTypeDefinition50", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_PredefinedDataTypeDefinition50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_PredefinedDataTypeDefinition50"):
                    opp_val = getattr(item, "dbdefinition_PredefinedDataTypeDefinition50", None)
                    
                    setattr(item, "dbdefinition_PredefinedDataTypeDefinition50", self)
                    

class dbdefinition_TableSpaceDefinition:

    def __init__(self, typeSupported: bool, extentSizeSupported: bool, prefetchSizeSupported: bool, managedBySupported: bool, pageSizeSupported: bool, bufferPoolSupported: bool, defaultSupported: bool, containerMaximumSizeSupported: bool, containerInitialSizeSupported: bool, containerExtentSizeSupported: bool, tableSpaceType: str, maximumIdentifierLength: int, dbdefinition_TableSpaceDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.typeSupported = typeSupported
        self.extentSizeSupported = extentSizeSupported
        self.prefetchSizeSupported = prefetchSizeSupported
        self.managedBySupported = managedBySupported
        self.pageSizeSupported = pageSizeSupported
        self.bufferPoolSupported = bufferPoolSupported
        self.defaultSupported = defaultSupported
        self.containerMaximumSizeSupported = containerMaximumSizeSupported
        self.containerInitialSizeSupported = containerInitialSizeSupported
        self.containerExtentSizeSupported = containerExtentSizeSupported
        self.tableSpaceType = tableSpaceType
        self.maximumIdentifierLength = maximumIdentifierLength
        self.dbdefinition_TableSpaceDefinition = dbdefinition_TableSpaceDefinition
        
        pass
    @property
    def defaultSupported(self):
        return self.__defaultSupported

    @defaultSupported.setter
    def defaultSupported(self, defaultSupported: bool):
        self.__defaultSupported = defaultSupported


    @property
    def extentSizeSupported(self):
        return self.__extentSizeSupported

    @extentSizeSupported.setter
    def extentSizeSupported(self, extentSizeSupported: bool):
        self.__extentSizeSupported = extentSizeSupported


    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def containerInitialSizeSupported(self):
        return self.__containerInitialSizeSupported

    @containerInitialSizeSupported.setter
    def containerInitialSizeSupported(self, containerInitialSizeSupported: bool):
        self.__containerInitialSizeSupported = containerInitialSizeSupported


    @property
    def typeSupported(self):
        return self.__typeSupported

    @typeSupported.setter
    def typeSupported(self, typeSupported: bool):
        self.__typeSupported = typeSupported


    @property
    def managedBySupported(self):
        return self.__managedBySupported

    @managedBySupported.setter
    def managedBySupported(self, managedBySupported: bool):
        self.__managedBySupported = managedBySupported


    @property
    def containerMaximumSizeSupported(self):
        return self.__containerMaximumSizeSupported

    @containerMaximumSizeSupported.setter
    def containerMaximumSizeSupported(self, containerMaximumSizeSupported: bool):
        self.__containerMaximumSizeSupported = containerMaximumSizeSupported


    @property
    def containerExtentSizeSupported(self):
        return self.__containerExtentSizeSupported

    @containerExtentSizeSupported.setter
    def containerExtentSizeSupported(self, containerExtentSizeSupported: bool):
        self.__containerExtentSizeSupported = containerExtentSizeSupported


    @property
    def pageSizeSupported(self):
        return self.__pageSizeSupported

    @pageSizeSupported.setter
    def pageSizeSupported(self, pageSizeSupported: bool):
        self.__pageSizeSupported = pageSizeSupported


    @property
    def tableSpaceType(self):
        return self.__tableSpaceType

    @tableSpaceType.setter
    def tableSpaceType(self, tableSpaceType: str):
        self.__tableSpaceType = tableSpaceType


    @property
    def prefetchSizeSupported(self):
        return self.__prefetchSizeSupported

    @prefetchSizeSupported.setter
    def prefetchSizeSupported(self, prefetchSizeSupported: bool):
        self.__prefetchSizeSupported = prefetchSizeSupported


    @property
    def bufferPoolSupported(self):
        return self.__bufferPoolSupported

    @bufferPoolSupported.setter
    def bufferPoolSupported(self, bufferPoolSupported: bool):
        self.__bufferPoolSupported = bufferPoolSupported


    @property
    def dbdefinition_TableSpaceDefinition(self):
        return self.__dbdefinition_TableSpaceDefinition

    @dbdefinition_TableSpaceDefinition.setter
    def dbdefinition_TableSpaceDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_TableSpaceDefinition__dbdefinition_TableSpaceDefinition", None)
        self.__dbdefinition_TableSpaceDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition2"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition2", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition2"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition2", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition2", self)

class dbdefinition_NicknameDefinition:

    def __init__(self, constraintSupported: bool, indexSupported: bool, maximumIdentifierLength: int, dbdefinition_NicknameDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.constraintSupported = constraintSupported
        self.indexSupported = indexSupported
        self.maximumIdentifierLength = maximumIdentifierLength
        self.dbdefinition_NicknameDefinition = dbdefinition_NicknameDefinition
        
        pass
    @property
    def indexSupported(self):
        return self.__indexSupported

    @indexSupported.setter
    def indexSupported(self, indexSupported: bool):
        self.__indexSupported = indexSupported


    @property
    def constraintSupported(self):
        return self.__constraintSupported

    @constraintSupported.setter
    def constraintSupported(self, constraintSupported: bool):
        self.__constraintSupported = constraintSupported


    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def dbdefinition_NicknameDefinition(self):
        return self.__dbdefinition_NicknameDefinition

    @dbdefinition_NicknameDefinition.setter
    def dbdefinition_NicknameDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_NicknameDefinition__dbdefinition_NicknameDefinition", None)
        self.__dbdefinition_NicknameDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition26"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition26", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition26"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition26", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition26", self)

class dbdefinition_SQLSyntaxDefinition:

    def __init__(self, keywords: str, operators: str, terminationCharacter: str, dbdefinition_SQLSyntaxDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.keywords = keywords
        self.operators = operators
        self.terminationCharacter = terminationCharacter
        self.dbdefinition_SQLSyntaxDefinition = dbdefinition_SQLSyntaxDefinition
        
        pass
    @property
    def terminationCharacter(self):
        return self.__terminationCharacter

    @terminationCharacter.setter
    def terminationCharacter(self, terminationCharacter: str):
        self.__terminationCharacter = terminationCharacter


    @property
    def operators(self):
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators


    @property
    def keywords(self):
        return self.__keywords

    @keywords.setter
    def keywords(self, keywords: str):
        self.__keywords = keywords


    @property
    def dbdefinition_SQLSyntaxDefinition(self):
        return self.__dbdefinition_SQLSyntaxDefinition

    @dbdefinition_SQLSyntaxDefinition.setter
    def dbdefinition_SQLSyntaxDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_SQLSyntaxDefinition__dbdefinition_SQLSyntaxDefinition", None)
        self.__dbdefinition_SQLSyntaxDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition24"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition24", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition24"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition24", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition24", self)

class dbdefinition_QueryDefinition:

    def __init__(self, identifierQuoteString: str, hostVariableMarker: str, hostVariableMarkerSupported: bool, castExpressionSupported: bool, defaultKeywordForInsertValueSupported: bool, extendedGroupingSupported: bool, tableAliasInDeleteSupported: bool, dbdefinition_QueryDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.identifierQuoteString = identifierQuoteString
        self.hostVariableMarker = hostVariableMarker
        self.hostVariableMarkerSupported = hostVariableMarkerSupported
        self.castExpressionSupported = castExpressionSupported
        self.defaultKeywordForInsertValueSupported = defaultKeywordForInsertValueSupported
        self.extendedGroupingSupported = extendedGroupingSupported
        self.tableAliasInDeleteSupported = tableAliasInDeleteSupported
        self.dbdefinition_QueryDefinition = dbdefinition_QueryDefinition
        
        pass
    @property
    def tableAliasInDeleteSupported(self):
        return self.__tableAliasInDeleteSupported

    @tableAliasInDeleteSupported.setter
    def tableAliasInDeleteSupported(self, tableAliasInDeleteSupported: bool):
        self.__tableAliasInDeleteSupported = tableAliasInDeleteSupported


    @property
    def castExpressionSupported(self):
        return self.__castExpressionSupported

    @castExpressionSupported.setter
    def castExpressionSupported(self, castExpressionSupported: bool):
        self.__castExpressionSupported = castExpressionSupported


    @property
    def extendedGroupingSupported(self):
        return self.__extendedGroupingSupported

    @extendedGroupingSupported.setter
    def extendedGroupingSupported(self, extendedGroupingSupported: bool):
        self.__extendedGroupingSupported = extendedGroupingSupported


    @property
    def identifierQuoteString(self):
        return self.__identifierQuoteString

    @identifierQuoteString.setter
    def identifierQuoteString(self, identifierQuoteString: str):
        self.__identifierQuoteString = identifierQuoteString


    @property
    def hostVariableMarker(self):
        return self.__hostVariableMarker

    @hostVariableMarker.setter
    def hostVariableMarker(self, hostVariableMarker: str):
        self.__hostVariableMarker = hostVariableMarker


    @property
    def defaultKeywordForInsertValueSupported(self):
        return self.__defaultKeywordForInsertValueSupported

    @defaultKeywordForInsertValueSupported.setter
    def defaultKeywordForInsertValueSupported(self, defaultKeywordForInsertValueSupported: bool):
        self.__defaultKeywordForInsertValueSupported = defaultKeywordForInsertValueSupported


    @property
    def hostVariableMarkerSupported(self):
        return self.__hostVariableMarkerSupported

    @hostVariableMarkerSupported.setter
    def hostVariableMarkerSupported(self, hostVariableMarkerSupported: bool):
        self.__hostVariableMarkerSupported = hostVariableMarkerSupported


    @property
    def dbdefinition_QueryDefinition(self):
        return self.__dbdefinition_QueryDefinition

    @dbdefinition_QueryDefinition.setter
    def dbdefinition_QueryDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_QueryDefinition__dbdefinition_QueryDefinition", None)
        self.__dbdefinition_QueryDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition22"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition22", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition22"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition22", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition22", self)

class dbdefinition_UserDefinedTypeDefinition:

    def __init__(self, defaultValueSupported: bool, distinctTypeSupported: bool, structuredTypeSupported: bool, maximumIdentifierLength: int, dbdefinition_UserDefinedTypeDefinition: "dbdefinition_DatabaseVendorDefinition" = None):
        self.defaultValueSupported = defaultValueSupported
        self.distinctTypeSupported = distinctTypeSupported
        self.structuredTypeSupported = structuredTypeSupported
        self.maximumIdentifierLength = maximumIdentifierLength
        self.dbdefinition_UserDefinedTypeDefinition = dbdefinition_UserDefinedTypeDefinition
        
        pass
    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def structuredTypeSupported(self):
        return self.__structuredTypeSupported

    @structuredTypeSupported.setter
    def structuredTypeSupported(self, structuredTypeSupported: bool):
        self.__structuredTypeSupported = structuredTypeSupported


    @property
    def defaultValueSupported(self):
        return self.__defaultValueSupported

    @defaultValueSupported.setter
    def defaultValueSupported(self, defaultValueSupported: bool):
        self.__defaultValueSupported = defaultValueSupported


    @property
    def distinctTypeSupported(self):
        return self.__distinctTypeSupported

    @distinctTypeSupported.setter
    def distinctTypeSupported(self, distinctTypeSupported: bool):
        self.__distinctTypeSupported = distinctTypeSupported


    @property
    def dbdefinition_UserDefinedTypeDefinition(self):
        return self.__dbdefinition_UserDefinedTypeDefinition

    @dbdefinition_UserDefinedTypeDefinition.setter
    def dbdefinition_UserDefinedTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_UserDefinedTypeDefinition__dbdefinition_UserDefinedTypeDefinition", None)
        self.__dbdefinition_UserDefinedTypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition20"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition20", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DatabaseVendorDefinition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition20"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition20", None)
                setattr(value, "dbdefinition_DatabaseVendorDefinition20", self)

class dbdefinition_PredefinedDataTypeDefinition:

    def __init__(self, maximumScale: int, minimumScale: int, defaultValueTypes: str, primitiveType: str, name: str, jdbcEnumType: int, characterSet: str, encodingScheme: str, characterSetSuffix: str, encodingSchemeSuffix: str, javaClassName: str, defaultLength: int, lengthSupported: bool, scaleSupported: bool, precisionSupported: bool, keyConstraintSupported: bool, identitySupported: bool, multipleColumnsSupported: bool, nullableSupported: bool, defaultSupported: bool, clusteringSupported: bool, fillFactorSupported: bool, bitDataSupported: bool, maximumValue: str, minimumValue: str, maximumLength: int, maximumPrecision: int, defaultPrecision: int, defaultScale: int, cutoffPrecision: int, lengthUnit: str, orderingSupported: bool, groupingSupported: bool, displayName: str, displayNameSupported: bool, leadingFieldQualifierSupported: bool, trailingFieldQualifierSupported: bool, fieldQualifierSeparator: str, largeValueSpecifierSupported: bool, largeValueSpecifierName: str, largeValueSpecifierLength: int, lengthSemanticSupported: bool, lengthSemantic: str, languageType: str, dbdefinition_PredefinedDataTypeDefinition: "dbdefinition_DatabaseVendorDefinition" = None, dbdefinition_PredefinedDataTypeDefinition38: set["dbdefinition_FieldQualifierDefinition"] = None, dbdefinition_PredefinedDataTypeDefinition40: set["dbdefinition_FieldQualifierDefinition"] = None, dbdefinition_PredefinedDataTypeDefinition43: "dbdefinition_FieldQualifierDefinition" = None, dbdefinition_PredefinedDataTypeDefinition46: "dbdefinition_FieldQualifierDefinition" = None, dbdefinition_PredefinedDataTypeDefinition50: "dbdefinition_StoredProcedureDefinition" = None, dbdefinition_PredefinedDataTypeDefinition53: "dbdefinition_ColumnDefinition" = None, dbdefinition_PredefinedDataTypeDefinition56: "dbdefinition_SequenceDefinition" = None, dbdefinition_PredefinedDataTypeDefinition59: "dbdefinition_SequenceDefinition" = None):
        self.maximumScale = maximumScale
        self.minimumScale = minimumScale
        self.defaultValueTypes = defaultValueTypes
        self.primitiveType = primitiveType
        self.name = name
        self.jdbcEnumType = jdbcEnumType
        self.characterSet = characterSet
        self.encodingScheme = encodingScheme
        self.characterSetSuffix = characterSetSuffix
        self.encodingSchemeSuffix = encodingSchemeSuffix
        self.javaClassName = javaClassName
        self.defaultLength = defaultLength
        self.lengthSupported = lengthSupported
        self.scaleSupported = scaleSupported
        self.precisionSupported = precisionSupported
        self.keyConstraintSupported = keyConstraintSupported
        self.identitySupported = identitySupported
        self.multipleColumnsSupported = multipleColumnsSupported
        self.nullableSupported = nullableSupported
        self.defaultSupported = defaultSupported
        self.clusteringSupported = clusteringSupported
        self.fillFactorSupported = fillFactorSupported
        self.bitDataSupported = bitDataSupported
        self.maximumValue = maximumValue
        self.minimumValue = minimumValue
        self.maximumLength = maximumLength
        self.maximumPrecision = maximumPrecision
        self.defaultPrecision = defaultPrecision
        self.defaultScale = defaultScale
        self.cutoffPrecision = cutoffPrecision
        self.lengthUnit = lengthUnit
        self.orderingSupported = orderingSupported
        self.groupingSupported = groupingSupported
        self.displayName = displayName
        self.displayNameSupported = displayNameSupported
        self.leadingFieldQualifierSupported = leadingFieldQualifierSupported
        self.trailingFieldQualifierSupported = trailingFieldQualifierSupported
        self.fieldQualifierSeparator = fieldQualifierSeparator
        self.largeValueSpecifierSupported = largeValueSpecifierSupported
        self.largeValueSpecifierName = largeValueSpecifierName
        self.largeValueSpecifierLength = largeValueSpecifierLength
        self.lengthSemanticSupported = lengthSemanticSupported
        self.lengthSemantic = lengthSemantic
        self.languageType = languageType
        self.dbdefinition_PredefinedDataTypeDefinition = dbdefinition_PredefinedDataTypeDefinition
        self.dbdefinition_PredefinedDataTypeDefinition38 = dbdefinition_PredefinedDataTypeDefinition38 if dbdefinition_PredefinedDataTypeDefinition38 is not None else set()
        self.dbdefinition_PredefinedDataTypeDefinition40 = dbdefinition_PredefinedDataTypeDefinition40 if dbdefinition_PredefinedDataTypeDefinition40 is not None else set()
        self.dbdefinition_PredefinedDataTypeDefinition43 = dbdefinition_PredefinedDataTypeDefinition43
        self.dbdefinition_PredefinedDataTypeDefinition46 = dbdefinition_PredefinedDataTypeDefinition46
        self.dbdefinition_PredefinedDataTypeDefinition50 = dbdefinition_PredefinedDataTypeDefinition50
        self.dbdefinition_PredefinedDataTypeDefinition53 = dbdefinition_PredefinedDataTypeDefinition53
        self.dbdefinition_PredefinedDataTypeDefinition56 = dbdefinition_PredefinedDataTypeDefinition56
        self.dbdefinition_PredefinedDataTypeDefinition59 = dbdefinition_PredefinedDataTypeDefinition59
        
        pass
    @property
    def lengthSupported(self):
        return self.__lengthSupported

    @lengthSupported.setter
    def lengthSupported(self, lengthSupported: bool):
        self.__lengthSupported = lengthSupported


    @property
    def cutoffPrecision(self):
        return self.__cutoffPrecision

    @cutoffPrecision.setter
    def cutoffPrecision(self, cutoffPrecision: int):
        self.__cutoffPrecision = cutoffPrecision


    @property
    def primitiveType(self):
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType


    @property
    def groupingSupported(self):
        return self.__groupingSupported

    @groupingSupported.setter
    def groupingSupported(self, groupingSupported: bool):
        self.__groupingSupported = groupingSupported


    @property
    def clusteringSupported(self):
        return self.__clusteringSupported

    @clusteringSupported.setter
    def clusteringSupported(self, clusteringSupported: bool):
        self.__clusteringSupported = clusteringSupported


    @property
    def defaultLength(self):
        return self.__defaultLength

    @defaultLength.setter
    def defaultLength(self, defaultLength: int):
        self.__defaultLength = defaultLength


    @property
    def keyConstraintSupported(self):
        return self.__keyConstraintSupported

    @keyConstraintSupported.setter
    def keyConstraintSupported(self, keyConstraintSupported: bool):
        self.__keyConstraintSupported = keyConstraintSupported


    @property
    def defaultSupported(self):
        return self.__defaultSupported

    @defaultSupported.setter
    def defaultSupported(self, defaultSupported: bool):
        self.__defaultSupported = defaultSupported


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def maximumValue(self):
        return self.__maximumValue

    @maximumValue.setter
    def maximumValue(self, maximumValue: str):
        self.__maximumValue = maximumValue


    @property
    def lengthSemantic(self):
        return self.__lengthSemantic

    @lengthSemantic.setter
    def lengthSemantic(self, lengthSemantic: str):
        self.__lengthSemantic = lengthSemantic


    @property
    def minimumValue(self):
        return self.__minimumValue

    @minimumValue.setter
    def minimumValue(self, minimumValue: str):
        self.__minimumValue = minimumValue


    @property
    def largeValueSpecifierSupported(self):
        return self.__largeValueSpecifierSupported

    @largeValueSpecifierSupported.setter
    def largeValueSpecifierSupported(self, largeValueSpecifierSupported: bool):
        self.__largeValueSpecifierSupported = largeValueSpecifierSupported


    @property
    def bitDataSupported(self):
        return self.__bitDataSupported

    @bitDataSupported.setter
    def bitDataSupported(self, bitDataSupported: bool):
        self.__bitDataSupported = bitDataSupported


    @property
    def displayNameSupported(self):
        return self.__displayNameSupported

    @displayNameSupported.setter
    def displayNameSupported(self, displayNameSupported: bool):
        self.__displayNameSupported = displayNameSupported


    @property
    def maximumLength(self):
        return self.__maximumLength

    @maximumLength.setter
    def maximumLength(self, maximumLength: int):
        self.__maximumLength = maximumLength


    @property
    def defaultScale(self):
        return self.__defaultScale

    @defaultScale.setter
    def defaultScale(self, defaultScale: int):
        self.__defaultScale = defaultScale


    @property
    def precisionSupported(self):
        return self.__precisionSupported

    @precisionSupported.setter
    def precisionSupported(self, precisionSupported: bool):
        self.__precisionSupported = precisionSupported


    @property
    def largeValueSpecifierLength(self):
        return self.__largeValueSpecifierLength

    @largeValueSpecifierLength.setter
    def largeValueSpecifierLength(self, largeValueSpecifierLength: int):
        self.__largeValueSpecifierLength = largeValueSpecifierLength


    @property
    def scaleSupported(self):
        return self.__scaleSupported

    @scaleSupported.setter
    def scaleSupported(self, scaleSupported: bool):
        self.__scaleSupported = scaleSupported


    @property
    def encodingScheme(self):
        return self.__encodingScheme

    @encodingScheme.setter
    def encodingScheme(self, encodingScheme: str):
        self.__encodingScheme = encodingScheme


    @property
    def jdbcEnumType(self):
        return self.__jdbcEnumType

    @jdbcEnumType.setter
    def jdbcEnumType(self, jdbcEnumType: int):
        self.__jdbcEnumType = jdbcEnumType


    @property
    def orderingSupported(self):
        return self.__orderingSupported

    @orderingSupported.setter
    def orderingSupported(self, orderingSupported: bool):
        self.__orderingSupported = orderingSupported


    @property
    def defaultValueTypes(self):
        return self.__defaultValueTypes

    @defaultValueTypes.setter
    def defaultValueTypes(self, defaultValueTypes: str):
        self.__defaultValueTypes = defaultValueTypes


    @property
    def characterSet(self):
        return self.__characterSet

    @characterSet.setter
    def characterSet(self, characterSet: str):
        self.__characterSet = characterSet


    @property
    def defaultPrecision(self):
        return self.__defaultPrecision

    @defaultPrecision.setter
    def defaultPrecision(self, defaultPrecision: int):
        self.__defaultPrecision = defaultPrecision


    @property
    def displayName(self):
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName


    @property
    def trailingFieldQualifierSupported(self):
        return self.__trailingFieldQualifierSupported

    @trailingFieldQualifierSupported.setter
    def trailingFieldQualifierSupported(self, trailingFieldQualifierSupported: bool):
        self.__trailingFieldQualifierSupported = trailingFieldQualifierSupported


    @property
    def languageType(self):
        return self.__languageType

    @languageType.setter
    def languageType(self, languageType: str):
        self.__languageType = languageType


    @property
    def lengthSemanticSupported(self):
        return self.__lengthSemanticSupported

    @lengthSemanticSupported.setter
    def lengthSemanticSupported(self, lengthSemanticSupported: bool):
        self.__lengthSemanticSupported = lengthSemanticSupported


    @property
    def fillFactorSupported(self):
        return self.__fillFactorSupported

    @fillFactorSupported.setter
    def fillFactorSupported(self, fillFactorSupported: bool):
        self.__fillFactorSupported = fillFactorSupported


    @property
    def fieldQualifierSeparator(self):
        return self.__fieldQualifierSeparator

    @fieldQualifierSeparator.setter
    def fieldQualifierSeparator(self, fieldQualifierSeparator: str):
        self.__fieldQualifierSeparator = fieldQualifierSeparator


    @property
    def maximumPrecision(self):
        return self.__maximumPrecision

    @maximumPrecision.setter
    def maximumPrecision(self, maximumPrecision: int):
        self.__maximumPrecision = maximumPrecision


    @property
    def leadingFieldQualifierSupported(self):
        return self.__leadingFieldQualifierSupported

    @leadingFieldQualifierSupported.setter
    def leadingFieldQualifierSupported(self, leadingFieldQualifierSupported: bool):
        self.__leadingFieldQualifierSupported = leadingFieldQualifierSupported


    @property
    def maximumScale(self):
        return self.__maximumScale

    @maximumScale.setter
    def maximumScale(self, maximumScale: int):
        self.__maximumScale = maximumScale


    @property
    def lengthUnit(self):
        return self.__lengthUnit

    @lengthUnit.setter
    def lengthUnit(self, lengthUnit: str):
        self.__lengthUnit = lengthUnit


    @property
    def multipleColumnsSupported(self):
        return self.__multipleColumnsSupported

    @multipleColumnsSupported.setter
    def multipleColumnsSupported(self, multipleColumnsSupported: bool):
        self.__multipleColumnsSupported = multipleColumnsSupported


    @property
    def minimumScale(self):
        return self.__minimumScale

    @minimumScale.setter
    def minimumScale(self, minimumScale: int):
        self.__minimumScale = minimumScale


    @property
    def javaClassName(self):
        return self.__javaClassName

    @javaClassName.setter
    def javaClassName(self, javaClassName: str):
        self.__javaClassName = javaClassName


    @property
    def nullableSupported(self):
        return self.__nullableSupported

    @nullableSupported.setter
    def nullableSupported(self, nullableSupported: bool):
        self.__nullableSupported = nullableSupported


    @property
    def characterSetSuffix(self):
        return self.__characterSetSuffix

    @characterSetSuffix.setter
    def characterSetSuffix(self, characterSetSuffix: str):
        self.__characterSetSuffix = characterSetSuffix


    @property
    def identitySupported(self):
        return self.__identitySupported

    @identitySupported.setter
    def identitySupported(self, identitySupported: bool):
        self.__identitySupported = identitySupported


    @property
    def encodingSchemeSuffix(self):
        return self.__encodingSchemeSuffix

    @encodingSchemeSuffix.setter
    def encodingSchemeSuffix(self, encodingSchemeSuffix: str):
        self.__encodingSchemeSuffix = encodingSchemeSuffix


    @property
    def largeValueSpecifierName(self):
        return self.__largeValueSpecifierName

    @largeValueSpecifierName.setter
    def largeValueSpecifierName(self, largeValueSpecifierName: str):
        self.__largeValueSpecifierName = largeValueSpecifierName


    @property
    def dbdefinition_PredefinedDataTypeDefinition56(self):
        return self.__dbdefinition_PredefinedDataTypeDefinition56

    @dbdefinition_PredefinedDataTypeDefinition56.setter
    def dbdefinition_PredefinedDataTypeDefinition56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PredefinedDataTypeDefinition__dbdefinition_PredefinedDataTypeDefinition56", None)
        self.__dbdefinition_PredefinedDataTypeDefinition56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_SequenceDefinition55"):
                opp_val = getattr(old_value, "dbdefinition_SequenceDefinition55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_SequenceDefinition55"):
                opp_val = getattr(value, "dbdefinition_SequenceDefinition55", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_SequenceDefinition55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbdefinition_PredefinedDataTypeDefinition46(self):
        return self.__dbdefinition_PredefinedDataTypeDefinition46

    @dbdefinition_PredefinedDataTypeDefinition46.setter
    def dbdefinition_PredefinedDataTypeDefinition46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PredefinedDataTypeDefinition__dbdefinition_PredefinedDataTypeDefinition46", None)
        self.__dbdefinition_PredefinedDataTypeDefinition46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_FieldQualifierDefinition47"):
                opp_val = getattr(old_value, "dbdefinition_FieldQualifierDefinition47", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_FieldQualifierDefinition47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_FieldQualifierDefinition47"):
                opp_val = getattr(value, "dbdefinition_FieldQualifierDefinition47", None)
                setattr(value, "dbdefinition_FieldQualifierDefinition47", self)

    @property
    def dbdefinition_PredefinedDataTypeDefinition40(self):
        return self.__dbdefinition_PredefinedDataTypeDefinition40

    @dbdefinition_PredefinedDataTypeDefinition40.setter
    def dbdefinition_PredefinedDataTypeDefinition40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PredefinedDataTypeDefinition__dbdefinition_PredefinedDataTypeDefinition40", None)
        self.__dbdefinition_PredefinedDataTypeDefinition40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_FieldQualifierDefinition41"):
                    opp_val = getattr(item, "dbdefinition_FieldQualifierDefinition41", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_FieldQualifierDefinition41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_FieldQualifierDefinition41"):
                    opp_val = getattr(item, "dbdefinition_FieldQualifierDefinition41", None)
                    
                    setattr(item, "dbdefinition_FieldQualifierDefinition41", self)
                    

    @property
    def dbdefinition_PredefinedDataTypeDefinition38(self):
        return self.__dbdefinition_PredefinedDataTypeDefinition38

    @dbdefinition_PredefinedDataTypeDefinition38.setter
    def dbdefinition_PredefinedDataTypeDefinition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PredefinedDataTypeDefinition__dbdefinition_PredefinedDataTypeDefinition38", None)
        self.__dbdefinition_PredefinedDataTypeDefinition38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_FieldQualifierDefinition"):
                    opp_val = getattr(item, "dbdefinition_FieldQualifierDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_FieldQualifierDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_FieldQualifierDefinition"):
                    opp_val = getattr(item, "dbdefinition_FieldQualifierDefinition", None)
                    
                    setattr(item, "dbdefinition_FieldQualifierDefinition", self)
                    

    @property
    def dbdefinition_PredefinedDataTypeDefinition(self):
        return self.__dbdefinition_PredefinedDataTypeDefinition

    @dbdefinition_PredefinedDataTypeDefinition.setter
    def dbdefinition_PredefinedDataTypeDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PredefinedDataTypeDefinition__dbdefinition_PredefinedDataTypeDefinition", None)
        self.__dbdefinition_PredefinedDataTypeDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DatabaseVendorDefinition"):
                opp_val = getattr(old_value, "dbdefinition_DatabaseVendorDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DatabaseVendorDefinition"):
                opp_val = getattr(value, "dbdefinition_DatabaseVendorDefinition", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_DatabaseVendorDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbdefinition_PredefinedDataTypeDefinition50(self):
        return self.__dbdefinition_PredefinedDataTypeDefinition50

    @dbdefinition_PredefinedDataTypeDefinition50.setter
    def dbdefinition_PredefinedDataTypeDefinition50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PredefinedDataTypeDefinition__dbdefinition_PredefinedDataTypeDefinition50", None)
        self.__dbdefinition_PredefinedDataTypeDefinition50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_StoredProcedureDefinition49"):
                opp_val = getattr(old_value, "dbdefinition_StoredProcedureDefinition49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_StoredProcedureDefinition49"):
                opp_val = getattr(value, "dbdefinition_StoredProcedureDefinition49", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_StoredProcedureDefinition49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbdefinition_PredefinedDataTypeDefinition53(self):
        return self.__dbdefinition_PredefinedDataTypeDefinition53

    @dbdefinition_PredefinedDataTypeDefinition53.setter
    def dbdefinition_PredefinedDataTypeDefinition53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PredefinedDataTypeDefinition__dbdefinition_PredefinedDataTypeDefinition53", None)
        self.__dbdefinition_PredefinedDataTypeDefinition53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_ColumnDefinition52"):
                opp_val = getattr(old_value, "dbdefinition_ColumnDefinition52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_ColumnDefinition52"):
                opp_val = getattr(value, "dbdefinition_ColumnDefinition52", None)
                if opp_val is None:
                    setattr(value, "dbdefinition_ColumnDefinition52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dbdefinition_PredefinedDataTypeDefinition43(self):
        return self.__dbdefinition_PredefinedDataTypeDefinition43

    @dbdefinition_PredefinedDataTypeDefinition43.setter
    def dbdefinition_PredefinedDataTypeDefinition43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PredefinedDataTypeDefinition__dbdefinition_PredefinedDataTypeDefinition43", None)
        self.__dbdefinition_PredefinedDataTypeDefinition43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_FieldQualifierDefinition44"):
                opp_val = getattr(old_value, "dbdefinition_FieldQualifierDefinition44", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_FieldQualifierDefinition44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_FieldQualifierDefinition44"):
                opp_val = getattr(value, "dbdefinition_FieldQualifierDefinition44", None)
                setattr(value, "dbdefinition_FieldQualifierDefinition44", self)

    @property
    def dbdefinition_PredefinedDataTypeDefinition59(self):
        return self.__dbdefinition_PredefinedDataTypeDefinition59

    @dbdefinition_PredefinedDataTypeDefinition59.setter
    def dbdefinition_PredefinedDataTypeDefinition59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_PredefinedDataTypeDefinition__dbdefinition_PredefinedDataTypeDefinition59", None)
        self.__dbdefinition_PredefinedDataTypeDefinition59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_SequenceDefinition58"):
                opp_val = getattr(old_value, "dbdefinition_SequenceDefinition58", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_SequenceDefinition58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_SequenceDefinition58"):
                opp_val = getattr(value, "dbdefinition_SequenceDefinition58", None)
                setattr(value, "dbdefinition_SequenceDefinition58", self)

class dbdefinition_DatabaseVendorDefinition:

    def __init__(self, domainSupported: bool, SQLStatementSupported: bool, nicknameSupported: bool, quotedDMLSupported: bool, quotedDDLSupported: bool, xmlSupported: bool, mQTIndexSupported: bool, eventSupported: bool, sqlUDFSupported: bool, storedProcedureSupported: bool, packageSupported: bool, authorizationIdentifierSupported: bool, vendor: str, version: str, constraintsSupported: bool, maximumIdentifierLength: int, triggerSupported: bool, snapshotViewSupported: bool, joinSupported: bool, viewTriggerSupported: bool, tablespacesSupported: bool, maximumCommentLength: int, sequenceSupported: bool, mQTSupported: bool, schemaSupported: bool, aliasSupported: bool, synonymSupported: bool, userDefinedTypeSupported: bool, roleSupported: bool, groupSupported: bool, userSupported: bool, roleAuthorizationSupported: bool, constructedDataTypeSupported: bool, uDFSupported: bool, dbdefinition_DatabaseVendorDefinition20: "dbdefinition_UserDefinedTypeDefinition" = None, dbdefinition_DatabaseVendorDefinition22: "dbdefinition_QueryDefinition" = None, dbdefinition_DatabaseVendorDefinition24: "dbdefinition_SQLSyntaxDefinition" = None, dbdefinition_DatabaseVendorDefinition26: "dbdefinition_NicknameDefinition" = None, dbdefinition_DatabaseVendorDefinition: set["dbdefinition_PredefinedDataTypeDefinition"] = None, dbdefinition_DatabaseVendorDefinition2: "dbdefinition_TableSpaceDefinition" = None, dbdefinition_DatabaseVendorDefinition4: "dbdefinition_StoredProcedureDefinition" = None, dbdefinition_DatabaseVendorDefinition6: "dbdefinition_TriggerDefinition" = None, dbdefinition_DatabaseVendorDefinition8: "dbdefinition_ColumnDefinition" = None, dbdefinition_DatabaseVendorDefinition10: "dbdefinition_ConstraintDefinition" = None, dbdefinition_DatabaseVendorDefinition12: set["dbdefinition_ExtendedDefinition"] = None, dbdefinition_DatabaseVendorDefinition14: "dbdefinition_IndexDefinition" = None, dbdefinition_DatabaseVendorDefinition16: "dbdefinition_TableDefinition" = None, dbdefinition_DatabaseVendorDefinition18: "dbdefinition_SequenceDefinition" = None, dbdefinition_DatabaseVendorDefinition28: "dbdefinition_SchemaDefinition" = None, dbdefinition_DatabaseVendorDefinition30: "dbdefinition_ViewDefinition" = None, dbdefinition_DatabaseVendorDefinition32: "dbdefinition_DebuggerDefinition" = None, dbdefinition_DatabaseVendorDefinition34: set["dbdefinition_PrivilegedElementDefinition"] = None, dbdefinition_DatabaseVendorDefinition36: "dbdefinition_ConstructedDataTypeDefinition" = None):
        self.domainSupported = domainSupported
        self.SQLStatementSupported = SQLStatementSupported
        self.nicknameSupported = nicknameSupported
        self.quotedDMLSupported = quotedDMLSupported
        self.quotedDDLSupported = quotedDDLSupported
        self.xmlSupported = xmlSupported
        self.mQTIndexSupported = mQTIndexSupported
        self.eventSupported = eventSupported
        self.sqlUDFSupported = sqlUDFSupported
        self.storedProcedureSupported = storedProcedureSupported
        self.packageSupported = packageSupported
        self.authorizationIdentifierSupported = authorizationIdentifierSupported
        self.vendor = vendor
        self.version = version
        self.constraintsSupported = constraintsSupported
        self.maximumIdentifierLength = maximumIdentifierLength
        self.triggerSupported = triggerSupported
        self.snapshotViewSupported = snapshotViewSupported
        self.joinSupported = joinSupported
        self.viewTriggerSupported = viewTriggerSupported
        self.tablespacesSupported = tablespacesSupported
        self.maximumCommentLength = maximumCommentLength
        self.sequenceSupported = sequenceSupported
        self.mQTSupported = mQTSupported
        self.schemaSupported = schemaSupported
        self.aliasSupported = aliasSupported
        self.synonymSupported = synonymSupported
        self.userDefinedTypeSupported = userDefinedTypeSupported
        self.roleSupported = roleSupported
        self.groupSupported = groupSupported
        self.userSupported = userSupported
        self.roleAuthorizationSupported = roleAuthorizationSupported
        self.constructedDataTypeSupported = constructedDataTypeSupported
        self.uDFSupported = uDFSupported
        self.dbdefinition_DatabaseVendorDefinition20 = dbdefinition_DatabaseVendorDefinition20
        self.dbdefinition_DatabaseVendorDefinition22 = dbdefinition_DatabaseVendorDefinition22
        self.dbdefinition_DatabaseVendorDefinition24 = dbdefinition_DatabaseVendorDefinition24
        self.dbdefinition_DatabaseVendorDefinition26 = dbdefinition_DatabaseVendorDefinition26
        self.dbdefinition_DatabaseVendorDefinition = dbdefinition_DatabaseVendorDefinition if dbdefinition_DatabaseVendorDefinition is not None else set()
        self.dbdefinition_DatabaseVendorDefinition2 = dbdefinition_DatabaseVendorDefinition2
        self.dbdefinition_DatabaseVendorDefinition4 = dbdefinition_DatabaseVendorDefinition4
        self.dbdefinition_DatabaseVendorDefinition6 = dbdefinition_DatabaseVendorDefinition6
        self.dbdefinition_DatabaseVendorDefinition8 = dbdefinition_DatabaseVendorDefinition8
        self.dbdefinition_DatabaseVendorDefinition10 = dbdefinition_DatabaseVendorDefinition10
        self.dbdefinition_DatabaseVendorDefinition12 = dbdefinition_DatabaseVendorDefinition12 if dbdefinition_DatabaseVendorDefinition12 is not None else set()
        self.dbdefinition_DatabaseVendorDefinition14 = dbdefinition_DatabaseVendorDefinition14
        self.dbdefinition_DatabaseVendorDefinition16 = dbdefinition_DatabaseVendorDefinition16
        self.dbdefinition_DatabaseVendorDefinition18 = dbdefinition_DatabaseVendorDefinition18
        self.dbdefinition_DatabaseVendorDefinition28 = dbdefinition_DatabaseVendorDefinition28
        self.dbdefinition_DatabaseVendorDefinition30 = dbdefinition_DatabaseVendorDefinition30
        self.dbdefinition_DatabaseVendorDefinition32 = dbdefinition_DatabaseVendorDefinition32
        self.dbdefinition_DatabaseVendorDefinition34 = dbdefinition_DatabaseVendorDefinition34 if dbdefinition_DatabaseVendorDefinition34 is not None else set()
        self.dbdefinition_DatabaseVendorDefinition36 = dbdefinition_DatabaseVendorDefinition36
        
        pass
    @property
    def quotedDDLSupported(self):
        return self.__quotedDDLSupported

    @quotedDDLSupported.setter
    def quotedDDLSupported(self, quotedDDLSupported: bool):
        self.__quotedDDLSupported = quotedDDLSupported


    @property
    def roleSupported(self):
        return self.__roleSupported

    @roleSupported.setter
    def roleSupported(self, roleSupported: bool):
        self.__roleSupported = roleSupported


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def tablespacesSupported(self):
        return self.__tablespacesSupported

    @tablespacesSupported.setter
    def tablespacesSupported(self, tablespacesSupported: bool):
        self.__tablespacesSupported = tablespacesSupported


    @property
    def userDefinedTypeSupported(self):
        return self.__userDefinedTypeSupported

    @userDefinedTypeSupported.setter
    def userDefinedTypeSupported(self, userDefinedTypeSupported: bool):
        self.__userDefinedTypeSupported = userDefinedTypeSupported


    @property
    def sqlUDFSupported(self):
        return self.__sqlUDFSupported

    @sqlUDFSupported.setter
    def sqlUDFSupported(self, sqlUDFSupported: bool):
        self.__sqlUDFSupported = sqlUDFSupported


    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor


    @property
    def userSupported(self):
        return self.__userSupported

    @userSupported.setter
    def userSupported(self, userSupported: bool):
        self.__userSupported = userSupported


    @property
    def sequenceSupported(self):
        return self.__sequenceSupported

    @sequenceSupported.setter
    def sequenceSupported(self, sequenceSupported: bool):
        self.__sequenceSupported = sequenceSupported


    @property
    def triggerSupported(self):
        return self.__triggerSupported

    @triggerSupported.setter
    def triggerSupported(self, triggerSupported: bool):
        self.__triggerSupported = triggerSupported


    @property
    def joinSupported(self):
        return self.__joinSupported

    @joinSupported.setter
    def joinSupported(self, joinSupported: bool):
        self.__joinSupported = joinSupported


    @property
    def constraintsSupported(self):
        return self.__constraintsSupported

    @constraintsSupported.setter
    def constraintsSupported(self, constraintsSupported: bool):
        self.__constraintsSupported = constraintsSupported


    @property
    def uDFSupported(self):
        return self.__uDFSupported

    @uDFSupported.setter
    def uDFSupported(self, uDFSupported: bool):
        self.__uDFSupported = uDFSupported


    @property
    def snapshotViewSupported(self):
        return self.__snapshotViewSupported

    @snapshotViewSupported.setter
    def snapshotViewSupported(self, snapshotViewSupported: bool):
        self.__snapshotViewSupported = snapshotViewSupported


    @property
    def domainSupported(self):
        return self.__domainSupported

    @domainSupported.setter
    def domainSupported(self, domainSupported: bool):
        self.__domainSupported = domainSupported


    @property
    def maximumCommentLength(self):
        return self.__maximumCommentLength

    @maximumCommentLength.setter
    def maximumCommentLength(self, maximumCommentLength: int):
        self.__maximumCommentLength = maximumCommentLength


    @property
    def nicknameSupported(self):
        return self.__nicknameSupported

    @nicknameSupported.setter
    def nicknameSupported(self, nicknameSupported: bool):
        self.__nicknameSupported = nicknameSupported


    @property
    def mQTSupported(self):
        return self.__mQTSupported

    @mQTSupported.setter
    def mQTSupported(self, mQTSupported: bool):
        self.__mQTSupported = mQTSupported


    @property
    def viewTriggerSupported(self):
        return self.__viewTriggerSupported

    @viewTriggerSupported.setter
    def viewTriggerSupported(self, viewTriggerSupported: bool):
        self.__viewTriggerSupported = viewTriggerSupported


    @property
    def SQLStatementSupported(self):
        return self.__SQLStatementSupported

    @SQLStatementSupported.setter
    def SQLStatementSupported(self, SQLStatementSupported: bool):
        self.__SQLStatementSupported = SQLStatementSupported


    @property
    def storedProcedureSupported(self):
        return self.__storedProcedureSupported

    @storedProcedureSupported.setter
    def storedProcedureSupported(self, storedProcedureSupported: bool):
        self.__storedProcedureSupported = storedProcedureSupported


    @property
    def schemaSupported(self):
        return self.__schemaSupported

    @schemaSupported.setter
    def schemaSupported(self, schemaSupported: bool):
        self.__schemaSupported = schemaSupported


    @property
    def maximumIdentifierLength(self):
        return self.__maximumIdentifierLength

    @maximumIdentifierLength.setter
    def maximumIdentifierLength(self, maximumIdentifierLength: int):
        self.__maximumIdentifierLength = maximumIdentifierLength


    @property
    def constructedDataTypeSupported(self):
        return self.__constructedDataTypeSupported

    @constructedDataTypeSupported.setter
    def constructedDataTypeSupported(self, constructedDataTypeSupported: bool):
        self.__constructedDataTypeSupported = constructedDataTypeSupported


    @property
    def eventSupported(self):
        return self.__eventSupported

    @eventSupported.setter
    def eventSupported(self, eventSupported: bool):
        self.__eventSupported = eventSupported


    @property
    def groupSupported(self):
        return self.__groupSupported

    @groupSupported.setter
    def groupSupported(self, groupSupported: bool):
        self.__groupSupported = groupSupported


    @property
    def mQTIndexSupported(self):
        return self.__mQTIndexSupported

    @mQTIndexSupported.setter
    def mQTIndexSupported(self, mQTIndexSupported: bool):
        self.__mQTIndexSupported = mQTIndexSupported


    @property
    def packageSupported(self):
        return self.__packageSupported

    @packageSupported.setter
    def packageSupported(self, packageSupported: bool):
        self.__packageSupported = packageSupported


    @property
    def quotedDMLSupported(self):
        return self.__quotedDMLSupported

    @quotedDMLSupported.setter
    def quotedDMLSupported(self, quotedDMLSupported: bool):
        self.__quotedDMLSupported = quotedDMLSupported


    @property
    def synonymSupported(self):
        return self.__synonymSupported

    @synonymSupported.setter
    def synonymSupported(self, synonymSupported: bool):
        self.__synonymSupported = synonymSupported


    @property
    def aliasSupported(self):
        return self.__aliasSupported

    @aliasSupported.setter
    def aliasSupported(self, aliasSupported: bool):
        self.__aliasSupported = aliasSupported


    @property
    def xmlSupported(self):
        return self.__xmlSupported

    @xmlSupported.setter
    def xmlSupported(self, xmlSupported: bool):
        self.__xmlSupported = xmlSupported


    @property
    def roleAuthorizationSupported(self):
        return self.__roleAuthorizationSupported

    @roleAuthorizationSupported.setter
    def roleAuthorizationSupported(self, roleAuthorizationSupported: bool):
        self.__roleAuthorizationSupported = roleAuthorizationSupported


    @property
    def authorizationIdentifierSupported(self):
        return self.__authorizationIdentifierSupported

    @authorizationIdentifierSupported.setter
    def authorizationIdentifierSupported(self, authorizationIdentifierSupported: bool):
        self.__authorizationIdentifierSupported = authorizationIdentifierSupported


    @property
    def dbdefinition_DatabaseVendorDefinition12(self):
        return self.__dbdefinition_DatabaseVendorDefinition12

    @dbdefinition_DatabaseVendorDefinition12.setter
    def dbdefinition_DatabaseVendorDefinition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition12", None)
        self.__dbdefinition_DatabaseVendorDefinition12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_ExtendedDefinition"):
                    opp_val = getattr(item, "dbdefinition_ExtendedDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_ExtendedDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_ExtendedDefinition"):
                    opp_val = getattr(item, "dbdefinition_ExtendedDefinition", None)
                    
                    setattr(item, "dbdefinition_ExtendedDefinition", self)
                    

    @property
    def dbdefinition_DatabaseVendorDefinition28(self):
        return self.__dbdefinition_DatabaseVendorDefinition28

    @dbdefinition_DatabaseVendorDefinition28.setter
    def dbdefinition_DatabaseVendorDefinition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition28", None)
        self.__dbdefinition_DatabaseVendorDefinition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_SchemaDefinition"):
                opp_val = getattr(old_value, "dbdefinition_SchemaDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_SchemaDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_SchemaDefinition"):
                opp_val = getattr(value, "dbdefinition_SchemaDefinition", None)
                setattr(value, "dbdefinition_SchemaDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition8(self):
        return self.__dbdefinition_DatabaseVendorDefinition8

    @dbdefinition_DatabaseVendorDefinition8.setter
    def dbdefinition_DatabaseVendorDefinition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition8", None)
        self.__dbdefinition_DatabaseVendorDefinition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_ColumnDefinition"):
                opp_val = getattr(old_value, "dbdefinition_ColumnDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_ColumnDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_ColumnDefinition"):
                opp_val = getattr(value, "dbdefinition_ColumnDefinition", None)
                setattr(value, "dbdefinition_ColumnDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition6(self):
        return self.__dbdefinition_DatabaseVendorDefinition6

    @dbdefinition_DatabaseVendorDefinition6.setter
    def dbdefinition_DatabaseVendorDefinition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition6", None)
        self.__dbdefinition_DatabaseVendorDefinition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_TriggerDefinition"):
                opp_val = getattr(old_value, "dbdefinition_TriggerDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_TriggerDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_TriggerDefinition"):
                opp_val = getattr(value, "dbdefinition_TriggerDefinition", None)
                setattr(value, "dbdefinition_TriggerDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition20(self):
        return self.__dbdefinition_DatabaseVendorDefinition20

    @dbdefinition_DatabaseVendorDefinition20.setter
    def dbdefinition_DatabaseVendorDefinition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition20", None)
        self.__dbdefinition_DatabaseVendorDefinition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_UserDefinedTypeDefinition"):
                opp_val = getattr(old_value, "dbdefinition_UserDefinedTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_UserDefinedTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_UserDefinedTypeDefinition"):
                opp_val = getattr(value, "dbdefinition_UserDefinedTypeDefinition", None)
                setattr(value, "dbdefinition_UserDefinedTypeDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition26(self):
        return self.__dbdefinition_DatabaseVendorDefinition26

    @dbdefinition_DatabaseVendorDefinition26.setter
    def dbdefinition_DatabaseVendorDefinition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition26", None)
        self.__dbdefinition_DatabaseVendorDefinition26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_NicknameDefinition"):
                opp_val = getattr(old_value, "dbdefinition_NicknameDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_NicknameDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_NicknameDefinition"):
                opp_val = getattr(value, "dbdefinition_NicknameDefinition", None)
                setattr(value, "dbdefinition_NicknameDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition2(self):
        return self.__dbdefinition_DatabaseVendorDefinition2

    @dbdefinition_DatabaseVendorDefinition2.setter
    def dbdefinition_DatabaseVendorDefinition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition2", None)
        self.__dbdefinition_DatabaseVendorDefinition2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_TableSpaceDefinition"):
                opp_val = getattr(old_value, "dbdefinition_TableSpaceDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_TableSpaceDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_TableSpaceDefinition"):
                opp_val = getattr(value, "dbdefinition_TableSpaceDefinition", None)
                setattr(value, "dbdefinition_TableSpaceDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition16(self):
        return self.__dbdefinition_DatabaseVendorDefinition16

    @dbdefinition_DatabaseVendorDefinition16.setter
    def dbdefinition_DatabaseVendorDefinition16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition16", None)
        self.__dbdefinition_DatabaseVendorDefinition16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_TableDefinition"):
                opp_val = getattr(old_value, "dbdefinition_TableDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_TableDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_TableDefinition"):
                opp_val = getattr(value, "dbdefinition_TableDefinition", None)
                setattr(value, "dbdefinition_TableDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition10(self):
        return self.__dbdefinition_DatabaseVendorDefinition10

    @dbdefinition_DatabaseVendorDefinition10.setter
    def dbdefinition_DatabaseVendorDefinition10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition10", None)
        self.__dbdefinition_DatabaseVendorDefinition10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_ConstraintDefinition"):
                opp_val = getattr(old_value, "dbdefinition_ConstraintDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_ConstraintDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_ConstraintDefinition"):
                opp_val = getattr(value, "dbdefinition_ConstraintDefinition", None)
                setattr(value, "dbdefinition_ConstraintDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition4(self):
        return self.__dbdefinition_DatabaseVendorDefinition4

    @dbdefinition_DatabaseVendorDefinition4.setter
    def dbdefinition_DatabaseVendorDefinition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition4", None)
        self.__dbdefinition_DatabaseVendorDefinition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_StoredProcedureDefinition"):
                opp_val = getattr(old_value, "dbdefinition_StoredProcedureDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_StoredProcedureDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_StoredProcedureDefinition"):
                opp_val = getattr(value, "dbdefinition_StoredProcedureDefinition", None)
                setattr(value, "dbdefinition_StoredProcedureDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition22(self):
        return self.__dbdefinition_DatabaseVendorDefinition22

    @dbdefinition_DatabaseVendorDefinition22.setter
    def dbdefinition_DatabaseVendorDefinition22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition22", None)
        self.__dbdefinition_DatabaseVendorDefinition22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_QueryDefinition"):
                opp_val = getattr(old_value, "dbdefinition_QueryDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_QueryDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_QueryDefinition"):
                opp_val = getattr(value, "dbdefinition_QueryDefinition", None)
                setattr(value, "dbdefinition_QueryDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition14(self):
        return self.__dbdefinition_DatabaseVendorDefinition14

    @dbdefinition_DatabaseVendorDefinition14.setter
    def dbdefinition_DatabaseVendorDefinition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition14", None)
        self.__dbdefinition_DatabaseVendorDefinition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_IndexDefinition"):
                opp_val = getattr(old_value, "dbdefinition_IndexDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_IndexDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_IndexDefinition"):
                opp_val = getattr(value, "dbdefinition_IndexDefinition", None)
                setattr(value, "dbdefinition_IndexDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition(self):
        return self.__dbdefinition_DatabaseVendorDefinition

    @dbdefinition_DatabaseVendorDefinition.setter
    def dbdefinition_DatabaseVendorDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition", None)
        self.__dbdefinition_DatabaseVendorDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_PredefinedDataTypeDefinition"):
                    opp_val = getattr(item, "dbdefinition_PredefinedDataTypeDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_PredefinedDataTypeDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_PredefinedDataTypeDefinition"):
                    opp_val = getattr(item, "dbdefinition_PredefinedDataTypeDefinition", None)
                    
                    setattr(item, "dbdefinition_PredefinedDataTypeDefinition", self)
                    

    @property
    def dbdefinition_DatabaseVendorDefinition32(self):
        return self.__dbdefinition_DatabaseVendorDefinition32

    @dbdefinition_DatabaseVendorDefinition32.setter
    def dbdefinition_DatabaseVendorDefinition32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition32", None)
        self.__dbdefinition_DatabaseVendorDefinition32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_DebuggerDefinition"):
                opp_val = getattr(old_value, "dbdefinition_DebuggerDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_DebuggerDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_DebuggerDefinition"):
                opp_val = getattr(value, "dbdefinition_DebuggerDefinition", None)
                setattr(value, "dbdefinition_DebuggerDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition30(self):
        return self.__dbdefinition_DatabaseVendorDefinition30

    @dbdefinition_DatabaseVendorDefinition30.setter
    def dbdefinition_DatabaseVendorDefinition30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition30", None)
        self.__dbdefinition_DatabaseVendorDefinition30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_ViewDefinition"):
                opp_val = getattr(old_value, "dbdefinition_ViewDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_ViewDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_ViewDefinition"):
                opp_val = getattr(value, "dbdefinition_ViewDefinition", None)
                setattr(value, "dbdefinition_ViewDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition34(self):
        return self.__dbdefinition_DatabaseVendorDefinition34

    @dbdefinition_DatabaseVendorDefinition34.setter
    def dbdefinition_DatabaseVendorDefinition34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition34", None)
        self.__dbdefinition_DatabaseVendorDefinition34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dbdefinition_PrivilegedElementDefinition"):
                    opp_val = getattr(item, "dbdefinition_PrivilegedElementDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "dbdefinition_PrivilegedElementDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dbdefinition_PrivilegedElementDefinition"):
                    opp_val = getattr(item, "dbdefinition_PrivilegedElementDefinition", None)
                    
                    setattr(item, "dbdefinition_PrivilegedElementDefinition", self)
                    

    @property
    def dbdefinition_DatabaseVendorDefinition18(self):
        return self.__dbdefinition_DatabaseVendorDefinition18

    @dbdefinition_DatabaseVendorDefinition18.setter
    def dbdefinition_DatabaseVendorDefinition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition18", None)
        self.__dbdefinition_DatabaseVendorDefinition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_SequenceDefinition"):
                opp_val = getattr(old_value, "dbdefinition_SequenceDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_SequenceDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_SequenceDefinition"):
                opp_val = getattr(value, "dbdefinition_SequenceDefinition", None)
                setattr(value, "dbdefinition_SequenceDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition36(self):
        return self.__dbdefinition_DatabaseVendorDefinition36

    @dbdefinition_DatabaseVendorDefinition36.setter
    def dbdefinition_DatabaseVendorDefinition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition36", None)
        self.__dbdefinition_DatabaseVendorDefinition36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_ConstructedDataTypeDefinition"):
                opp_val = getattr(old_value, "dbdefinition_ConstructedDataTypeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_ConstructedDataTypeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_ConstructedDataTypeDefinition"):
                opp_val = getattr(value, "dbdefinition_ConstructedDataTypeDefinition", None)
                setattr(value, "dbdefinition_ConstructedDataTypeDefinition", self)

    @property
    def dbdefinition_DatabaseVendorDefinition24(self):
        return self.__dbdefinition_DatabaseVendorDefinition24

    @dbdefinition_DatabaseVendorDefinition24.setter
    def dbdefinition_DatabaseVendorDefinition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dbdefinition_DatabaseVendorDefinition__dbdefinition_DatabaseVendorDefinition24", None)
        self.__dbdefinition_DatabaseVendorDefinition24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dbdefinition_SQLSyntaxDefinition"):
                opp_val = getattr(old_value, "dbdefinition_SQLSyntaxDefinition", None)
                if opp_val == self:
                    setattr(old_value, "dbdefinition_SQLSyntaxDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dbdefinition_SQLSyntaxDefinition"):
                opp_val = getattr(value, "dbdefinition_SQLSyntaxDefinition", None)
                setattr(value, "dbdefinition_SQLSyntaxDefinition", self)
