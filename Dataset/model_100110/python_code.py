from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class SQLDistinctType:

    pass
class SQLSimpleType:

    pass
class CWMRelationalData_SQLDataType:

    def __init__(self, typeNumber: str, type: set["Column"] = None):
        self.typeNumber = typeNumber
        self.type = type if type is not None else set()
        
        pass
    @property
    def typeNumber(self):
        return self.__typeNumber

    @typeNumber.setter
    def typeNumber(self, typeNumber: str):
        self.__typeNumber = typeNumber


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CWMRelationalData_SQLDataType__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Column19"):
                    opp_val = getattr(item, "Column19", None)
                    
                    if opp_val == self:
                        setattr(item, "Column19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Column19"):
                    opp_val = getattr(item, "Column19", None)
                    
                    setattr(item, "Column19", self)
                    

class CWMRelationalData_Trigger:

    pass
class QueryExpression:

    pass
class Trigger:

    pass
class CWMRelationalData_ColumnSet:

    pass
class NamedColumnSet:

    pass
class ColumnSet:

    pass
class CWMRelationalData_QueryColumnSet(ColumnSet):

    pass
class CWMRelationalData_NamedColumnSet(ColumnSet):

    pass
class SQLDataType:

    pass
class CWMRelationalData_SQLDistinctType(SQLDataType):

    def __init__(self, length: str, precision: str, scale: str, sqlDistinctTypes: "SQLSimpleType" = None, SQLDataType: "CWMRelationalData_Column" = None):
        self.length = length
        self.precision = precision
        self.scale = scale
        self.sqlDistinctTypes = sqlDistinctTypes
        
        pass
    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length


    @property
    def sqlDistinctTypes(self):
        return self.__sqlDistinctTypes

    @sqlDistinctTypes.setter
    def sqlDistinctTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CWMRelationalData_SQLDistinctType__sqlDistinctTypes", None)
        self.__sqlDistinctTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQLSimpleType"):
                opp_val = getattr(old_value, "SQLSimpleType", None)
                if opp_val == self:
                    setattr(old_value, "SQLSimpleType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQLSimpleType"):
                opp_val = getattr(value, "SQLSimpleType", None)
                setattr(value, "SQLSimpleType", self)

class CWMRelationalData_SQLSimpleType(SQLDataType):

    def __init__(self, characterMaximumLength: str, characterOctetLength: str, numericPrecision: str, numericPrecisionRadix: str, numericScale: str, dateTimePrecision: str, sqlSimpleType: set["SQLDistinctType"] = None, SQLDataType: "CWMRelationalData_Column" = None):
        self.characterMaximumLength = characterMaximumLength
        self.characterOctetLength = characterOctetLength
        self.numericPrecision = numericPrecision
        self.numericPrecisionRadix = numericPrecisionRadix
        self.numericScale = numericScale
        self.dateTimePrecision = dateTimePrecision
        self.sqlSimpleType = sqlSimpleType if sqlSimpleType is not None else set()
        
        pass
    @property
    def characterOctetLength(self):
        return self.__characterOctetLength

    @characterOctetLength.setter
    def characterOctetLength(self, characterOctetLength: str):
        self.__characterOctetLength = characterOctetLength


    @property
    def characterMaximumLength(self):
        return self.__characterMaximumLength

    @characterMaximumLength.setter
    def characterMaximumLength(self, characterMaximumLength: str):
        self.__characterMaximumLength = characterMaximumLength


    @property
    def numericPrecisionRadix(self):
        return self.__numericPrecisionRadix

    @numericPrecisionRadix.setter
    def numericPrecisionRadix(self, numericPrecisionRadix: str):
        self.__numericPrecisionRadix = numericPrecisionRadix


    @property
    def dateTimePrecision(self):
        return self.__dateTimePrecision

    @dateTimePrecision.setter
    def dateTimePrecision(self, dateTimePrecision: str):
        self.__dateTimePrecision = dateTimePrecision


    @property
    def numericScale(self):
        return self.__numericScale

    @numericScale.setter
    def numericScale(self, numericScale: str):
        self.__numericScale = numericScale


    @property
    def numericPrecision(self):
        return self.__numericPrecision

    @numericPrecision.setter
    def numericPrecision(self, numericPrecision: str):
        self.__numericPrecision = numericPrecision


    @property
    def sqlSimpleType(self):
        return self.__sqlSimpleType

    @sqlSimpleType.setter
    def sqlSimpleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CWMRelationalData_SQLSimpleType__sqlSimpleType", None)
        self.__sqlSimpleType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SQLDistinctType"):
                    opp_val = getattr(item, "SQLDistinctType", None)
                    
                    if opp_val == self:
                        setattr(item, "SQLDistinctType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SQLDistinctType"):
                    opp_val = getattr(item, "SQLDistinctType", None)
                    
                    setattr(item, "SQLDistinctType", self)
                    

class CheckConstraint:

    pass
class CWMRelationalData_View(NamedColumnSet):

    def __init__(self, isReadOnly: str, checkOption: str, CWMRelationalData_View: "QueryExpression" = None, NamedColumnSet17: "CWMRelationalData_Trigger" = None, NamedColumnSet: "CWMRelationalData_Column" = None):
        self.isReadOnly = isReadOnly
        self.checkOption = checkOption
        self.CWMRelationalData_View = CWMRelationalData_View
        
        pass
    @property
    def checkOption(self):
        return self.__checkOption

    @checkOption.setter
    def checkOption(self, checkOption: str):
        self.__checkOption = checkOption


    @property
    def isReadOnly(self):
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: str):
        self.__isReadOnly = isReadOnly


    @property
    def CWMRelationalData_View(self):
        return self.__CWMRelationalData_View

    @CWMRelationalData_View.setter
    def CWMRelationalData_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CWMRelationalData_View__CWMRelationalData_View", None)
        self.__CWMRelationalData_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueryExpression15"):
                opp_val = getattr(old_value, "QueryExpression15", None)
                if opp_val == self:
                    setattr(old_value, "QueryExpression15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueryExpression15"):
                opp_val = getattr(value, "QueryExpression15", None)
                setattr(value, "QueryExpression15", self)

class CWMRelationalData_Table(NamedColumnSet):

    def __init__(self, isTemporary: str, temporaryScope: str, isSystem: str, constrainedElements: set["CheckConstraint"] = None, NamedColumnSet17: "CWMRelationalData_Trigger" = None, NamedColumnSet: "CWMRelationalData_Column" = None):
        self.isTemporary = isTemporary
        self.temporaryScope = temporaryScope
        self.isSystem = isSystem
        self.constrainedElements = constrainedElements if constrainedElements is not None else set()
        
        pass
    @property
    def isTemporary(self):
        return self.__isTemporary

    @isTemporary.setter
    def isTemporary(self, isTemporary: str):
        self.__isTemporary = isTemporary


    @property
    def isSystem(self):
        return self.__isSystem

    @isSystem.setter
    def isSystem(self, isSystem: str):
        self.__isSystem = isSystem


    @property
    def temporaryScope(self):
        return self.__temporaryScope

    @temporaryScope.setter
    def temporaryScope(self, temporaryScope: str):
        self.__temporaryScope = temporaryScope


    @property
    def constrainedElements(self):
        return self.__constrainedElements

    @constrainedElements.setter
    def constrainedElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CWMRelationalData_Table__constrainedElements", None)
        self.__constrainedElements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CheckConstraint13"):
                    opp_val = getattr(item, "CheckConstraint13", None)
                    
                    if opp_val == self:
                        setattr(item, "CheckConstraint13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CheckConstraint13"):
                    opp_val = getattr(item, "CheckConstraint13", None)
                    
                    setattr(item, "CheckConstraint13", self)
                    

class CWMRelationalData_CheckConstraint:

    pass
class CWMRelationalData_QueryExpression:

    def __init__(self, expresssion: str):
        self.expresssion = expresssion
        
        pass
    @property
    def expresssion(self):
        return self.__expresssion

    @expresssion.setter
    def expresssion(self, expresssion: str):
        self.__expresssion = expresssion


class CWMRelationalData_Column:

    def __init__(self, precision: str, scale: str, isNullable: str, length: str, collectionName: str, characterSetName: str, constraintElements: set["CheckConstraint"] = None, structuralFeatures: "SQLDataType" = None, features: "ColumnSet" = None, optionScopeColumn: "NamedColumnSet" = None):
        self.precision = precision
        self.scale = scale
        self.isNullable = isNullable
        self.length = length
        self.collectionName = collectionName
        self.characterSetName = characterSetName
        self.constraintElements = constraintElements if constraintElements is not None else set()
        self.structuralFeatures = structuralFeatures
        self.features = features
        self.optionScopeColumn = optionScopeColumn
        
        pass
    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length


    @property
    def isNullable(self):
        return self.__isNullable

    @isNullable.setter
    def isNullable(self, isNullable: str):
        self.__isNullable = isNullable


    @property
    def characterSetName(self):
        return self.__characterSetName

    @characterSetName.setter
    def characterSetName(self, characterSetName: str):
        self.__characterSetName = characterSetName


    @property
    def scale(self):
        return self.__scale

    @scale.setter
    def scale(self, scale: str):
        self.__scale = scale


    @property
    def precision(self):
        return self.__precision

    @precision.setter
    def precision(self, precision: str):
        self.__precision = precision


    @property
    def collectionName(self):
        return self.__collectionName

    @collectionName.setter
    def collectionName(self, collectionName: str):
        self.__collectionName = collectionName


    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CWMRelationalData_Column__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColumnSet"):
                opp_val = getattr(old_value, "ColumnSet", None)
                if opp_val == self:
                    setattr(old_value, "ColumnSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColumnSet"):
                opp_val = getattr(value, "ColumnSet", None)
                setattr(value, "ColumnSet", self)

    @property
    def optionScopeColumn(self):
        return self.__optionScopeColumn

    @optionScopeColumn.setter
    def optionScopeColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CWMRelationalData_Column__optionScopeColumn", None)
        self.__optionScopeColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NamedColumnSet"):
                opp_val = getattr(old_value, "NamedColumnSet", None)
                if opp_val == self:
                    setattr(old_value, "NamedColumnSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NamedColumnSet"):
                opp_val = getattr(value, "NamedColumnSet", None)
                setattr(value, "NamedColumnSet", self)

    @property
    def constraintElements(self):
        return self.__constraintElements

    @constraintElements.setter
    def constraintElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CWMRelationalData_Column__constraintElements", None)
        self.__constraintElements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CheckConstraint"):
                    opp_val = getattr(item, "CheckConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "CheckConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CheckConstraint"):
                    opp_val = getattr(item, "CheckConstraint", None)
                    
                    setattr(item, "CheckConstraint", self)
                    

    @property
    def structuralFeatures(self):
        return self.__structuralFeatures

    @structuralFeatures.setter
    def structuralFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CWMRelationalData_Column__structuralFeatures", None)
        self.__structuralFeatures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SQLDataType"):
                opp_val = getattr(old_value, "SQLDataType", None)
                if opp_val == self:
                    setattr(old_value, "SQLDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SQLDataType"):
                opp_val = getattr(value, "SQLDataType", None)
                setattr(value, "SQLDataType", self)

class Table:

    pass
class Column:

    pass