from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DevelopmentStatus(Enum):
    DRAFT = "DRAFT"
    PROD = "PROD"
class Escape(Enum):
    Delimited = "Delimited"
    CSV = "CSV"
class MDMConnectionProtocol(Enum):
    HTTP = "HTTP"
class RowSeparator(Enum):
    Custom_String = "Custom_String"
    Standart_EOL = "Standart_EOL"
class Operator(Enum):
    Lower = "Lower"
    Greater_or_equals = "Greater_or_equals"
    Lower_or_equals = "Lower_or_equals"
    Equals = "Equals"
    Not_equals = "Not_equals"
    Greater = "Greater"
class MdmConceptType(Enum):
    OUTPUT = "OUTPUT"
    RECEIVE = "RECEIVE"
    INPUT = "INPUT"
class RuleType(Enum):
    REFERENCE = "REFERENCE"
    BASIC = "BASIC"
    CUSTOM = "CUSTOM"
class FileFormat(Enum):
    UNIX = "UNIX"
    MAC = "MAC"
    WINDOWS = "WINDOWS"
class LogicalOperator(Enum):
    And = "And"
    Or = "Or"
class FieldSeparator(Enum):
    Space = "Space"
    Alt_65 = "Alt_65"
    Custom_ANSI = "Custom_ANSI"
    Custom_UTF8 = "Custom_UTF8"
    Custom_RegExp = "Custom_RegExp"
    Tabulation = "Tabulation"
    Semicolon = "Semicolon"
    Comma = "Comma"
class Function(Enum):
    Empty = "Empty"
    Lower_case = "Lower_case"
    Upper_case = "Upper_case"
    Lower_case_first = "Lower_case_first"
    Upper_case_first = "Upper_case_first"
    Length = "Length"
    Match = "Match"


############################################
# Definition of Classes
############################################

class Schema:

    pass
class ElementType:

    pass
class connection_xml_TdXmlElementType(ElementType):

    def __init__(self, javaType: str, connection_xml_TdXmlElementType: "xml_connection_EObject" = None, connection_xml_TdXmlElementType132: "xml_TdXmlSchema" = None, connection_xml_TdXmlElementType134: "xml_TdXmlContent" = None):
        self.javaType = javaType
        self.connection_xml_TdXmlElementType = connection_xml_TdXmlElementType
        self.connection_xml_TdXmlElementType132 = connection_xml_TdXmlElementType132
        self.connection_xml_TdXmlElementType134 = connection_xml_TdXmlElementType134
        
        pass
    @property
    def javaType(self):
        return self.__javaType

    @javaType.setter
    def javaType(self, javaType: str):
        self.__javaType = javaType


    @property
    def connection_xml_TdXmlElementType132(self):
        return self.__connection_xml_TdXmlElementType132

    @connection_xml_TdXmlElementType132.setter
    def connection_xml_TdXmlElementType132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_xml_TdXmlElementType__connection_xml_TdXmlElementType132", None)
        self.__connection_xml_TdXmlElementType132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xml_TdXmlSchema"):
                opp_val = getattr(old_value, "xml_TdXmlSchema", None)
                if opp_val == self:
                    setattr(old_value, "xml_TdXmlSchema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xml_TdXmlSchema"):
                opp_val = getattr(value, "xml_TdXmlSchema", None)
                setattr(value, "xml_TdXmlSchema", self)

    @property
    def connection_xml_TdXmlElementType(self):
        return self.__connection_xml_TdXmlElementType

    @connection_xml_TdXmlElementType.setter
    def connection_xml_TdXmlElementType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_xml_TdXmlElementType__connection_xml_TdXmlElementType", None)
        self.__connection_xml_TdXmlElementType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xml_connection_EObject"):
                opp_val = getattr(old_value, "xml_connection_EObject", None)
                if opp_val == self:
                    setattr(old_value, "xml_connection_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xml_connection_EObject"):
                opp_val = getattr(value, "xml_connection_EObject", None)
                setattr(value, "xml_connection_EObject", self)

    @property
    def connection_xml_TdXmlElementType134(self):
        return self.__connection_xml_TdXmlElementType134

    @connection_xml_TdXmlElementType134.setter
    def connection_xml_TdXmlElementType134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_xml_TdXmlElementType__connection_xml_TdXmlElementType134", None)
        self.__connection_xml_TdXmlElementType134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xml_TdXmlContent"):
                opp_val = getattr(old_value, "xml_TdXmlContent", None)
                if opp_val == self:
                    setattr(old_value, "xml_TdXmlContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xml_TdXmlContent"):
                opp_val = getattr(value, "xml_TdXmlContent", None)
                setattr(value, "xml_TdXmlContent", self)

    def setContentType(self, connection_contentType):
        # TODO: Implement setContentType method
        pass

    def getContentType(self) :
        # TODO: Implement getContentType method
        pass

class Machine:

    pass
class connection_softwaredeployment_TdMachine(Machine):

    pass
class SoftwareSystem:

    pass
class connection_softwaredeployment_TdSoftwareSystem(SoftwareSystem):

    pass
class DataManager:

    pass
class connection_softwaredeployment_TdDataManager(DataManager):

    pass
class Expression:

    pass
class connection_relational_TdExpression(Expression):

    def __init__(self, version: str, modificationDate: str, name: str, expressionVariableMap: str):
        self.version = version
        self.modificationDate = modificationDate
        self.name = name
        self.expressionVariableMap = expressionVariableMap
        
        pass
    @property
    def modificationDate(self):
        return self.__modificationDate

    @modificationDate.setter
    def modificationDate(self, modificationDate: str):
        self.__modificationDate = modificationDate


    @property
    def expressionVariableMap(self):
        return self.__expressionVariableMap

    @expressionVariableMap.setter
    def expressionVariableMap(self, expressionVariableMap: str):
        self.__expressionVariableMap = expressionVariableMap


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


class Procedure:

    pass
class connection_relational_TdProcedure(Procedure):

    pass
class Trigger:

    pass
class connection_relational_TdTrigger(Trigger):

    pass
class connection_xml_TdXmlSchema(Schema):

    def __init__(self, xsdFilePath: str):
        self.xsdFilePath = xsdFilePath
        
        pass
    @property
    def xsdFilePath(self):
        return self.__xsdFilePath

    @xsdFilePath.setter
    def xsdFilePath(self, xsdFilePath: str):
        self.__xsdFilePath = xsdFilePath


class xml_TdXmlElementType:

    pass
class Content:

    pass
class connection_xml_TdXmlContent(Content):

    pass
class xml_TdXmlContent:

    pass
class xml_TdXmlSchema:

    pass
class xml_connection_EObject:

    pass
class relational_TdSqlDataType:

    pass
class relational_View:

    pass
class relational_Table:

    pass
class SAPTableField:

    pass
class connection_SAPBWTableField(SAPTableField):

    def __init__(self, logicalName: str):
        self.logicalName = logicalName
        
        pass
    @property
    def logicalName(self):
        return self.__logicalName

    @logicalName.setter
    def logicalName(self, logicalName: str):
        self.__logicalName = logicalName


class SAPTable:

    pass
class SQLSimpleType:

    pass
class connection_relational_TdSqlDataType(SQLSimpleType):

    def __init__(self, javaDataType: int, nullable: str, unsignedAttribute: str, caseSensitive: str, autoIncrement: str, localTypeName: str, searchable: str):
        self.javaDataType = javaDataType
        self.nullable = nullable
        self.unsignedAttribute = unsignedAttribute
        self.caseSensitive = caseSensitive
        self.autoIncrement = autoIncrement
        self.localTypeName = localTypeName
        self.searchable = searchable
        
        pass
    @property
    def localTypeName(self):
        return self.__localTypeName

    @localTypeName.setter
    def localTypeName(self, localTypeName: str):
        self.__localTypeName = localTypeName


    @property
    def javaDataType(self):
        return self.__javaDataType

    @javaDataType.setter
    def javaDataType(self, javaDataType: int):
        self.__javaDataType = javaDataType


    @property
    def searchable(self):
        return self.__searchable

    @searchable.setter
    def searchable(self, searchable: str):
        self.__searchable = searchable


    @property
    def caseSensitive(self):
        return self.__caseSensitive

    @caseSensitive.setter
    def caseSensitive(self, caseSensitive: str):
        self.__caseSensitive = caseSensitive


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: str):
        self.__nullable = nullable


    @property
    def autoIncrement(self):
        return self.__autoIncrement

    @autoIncrement.setter
    def autoIncrement(self, autoIncrement: str):
        self.__autoIncrement = autoIncrement


    @property
    def unsignedAttribute(self):
        return self.__unsignedAttribute

    @unsignedAttribute.setter
    def unsignedAttribute(self, unsignedAttribute: str):
        self.__unsignedAttribute = unsignedAttribute


class connection_SAPFunctionParameter:

    def __init__(self, description: str, length: str, changing: bool, testValue: str, tableResideInTables: bool, name: str, type: str, connection_SAPFunctionParameter: "connection_SAPFunctionParameter" = None, connection_SAPFunctionParameter121: set["connection_SAPFunctionParameter"] = None, connection_SAPFunctionParameter125: "connection_SAPFunctionParamData" = None, connection_SAPFunctionParameter128: "connection_SAPFunctionParamData" = None):
        self.description = description
        self.length = length
        self.changing = changing
        self.testValue = testValue
        self.tableResideInTables = tableResideInTables
        self.name = name
        self.type = type
        self.connection_SAPFunctionParameter = connection_SAPFunctionParameter
        self.connection_SAPFunctionParameter121 = connection_SAPFunctionParameter121 if connection_SAPFunctionParameter121 is not None else set()
        self.connection_SAPFunctionParameter125 = connection_SAPFunctionParameter125
        self.connection_SAPFunctionParameter128 = connection_SAPFunctionParameter128
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def changing(self):
        return self.__changing

    @changing.setter
    def changing(self, changing: bool):
        self.__changing = changing


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def testValue(self):
        return self.__testValue

    @testValue.setter
    def testValue(self, testValue: str):
        self.__testValue = testValue


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def tableResideInTables(self):
        return self.__tableResideInTables

    @tableResideInTables.setter
    def tableResideInTables(self, tableResideInTables: bool):
        self.__tableResideInTables = tableResideInTables


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length


    @property
    def connection_SAPFunctionParameter(self):
        return self.__connection_SAPFunctionParameter

    @connection_SAPFunctionParameter.setter
    def connection_SAPFunctionParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionParameter__connection_SAPFunctionParameter", None)
        self.__connection_SAPFunctionParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionParameter121"):
                opp_val = getattr(old_value, "connection_SAPFunctionParameter121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionParameter121"):
                opp_val = getattr(value, "connection_SAPFunctionParameter121", None)
                if opp_val is None:
                    setattr(value, "connection_SAPFunctionParameter121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_SAPFunctionParameter121(self):
        return self.__connection_SAPFunctionParameter121

    @connection_SAPFunctionParameter121.setter
    def connection_SAPFunctionParameter121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionParameter__connection_SAPFunctionParameter121", None)
        self.__connection_SAPFunctionParameter121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_SAPFunctionParameter"):
                    opp_val = getattr(item, "connection_SAPFunctionParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_SAPFunctionParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_SAPFunctionParameter"):
                    opp_val = getattr(item, "connection_SAPFunctionParameter", None)
                    
                    setattr(item, "connection_SAPFunctionParameter", self)
                    

    @property
    def connection_SAPFunctionParameter125(self):
        return self.__connection_SAPFunctionParameter125

    @connection_SAPFunctionParameter125.setter
    def connection_SAPFunctionParameter125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionParameter__connection_SAPFunctionParameter125", None)
        self.__connection_SAPFunctionParameter125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionParamData124"):
                opp_val = getattr(old_value, "connection_SAPFunctionParamData124", None)
                if opp_val == self:
                    setattr(old_value, "connection_SAPFunctionParamData124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionParamData124"):
                opp_val = getattr(value, "connection_SAPFunctionParamData124", None)
                setattr(value, "connection_SAPFunctionParamData124", self)

    @property
    def connection_SAPFunctionParameter128(self):
        return self.__connection_SAPFunctionParameter128

    @connection_SAPFunctionParameter128.setter
    def connection_SAPFunctionParameter128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionParameter__connection_SAPFunctionParameter128", None)
        self.__connection_SAPFunctionParameter128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionParamData127"):
                opp_val = getattr(old_value, "connection_SAPFunctionParamData127", None)
                if opp_val == self:
                    setattr(old_value, "connection_SAPFunctionParamData127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionParamData127"):
                opp_val = getattr(value, "connection_SAPFunctionParamData127", None)
                setattr(value, "connection_SAPFunctionParamData127", self)

class MetadataTable:

    pass
class connection_relational_TdTable(relational_Table, MetadataTable):

    pass
class connection_relational_TdView(relational_View, MetadataTable):

    pass
class connection_SAPTable(MetadataTable):

    def __init__(self, tableSearchType: str):
        self.tableSearchType = tableSearchType
        
        pass
    @property
    def tableSearchType(self):
        return self.__tableSearchType

    @tableSearchType.setter
    def tableSearchType(self, tableSearchType: str):
        self.__tableSearchType = tableSearchType


class connection_InnerJoinMap:

    def __init__(self, key: str, value: str, connection_InnerJoinMap: "connection_ValidationRulesConnection" = None):
        self.key = key
        self.value = value
        self.connection_InnerJoinMap = connection_InnerJoinMap
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def connection_InnerJoinMap(self):
        return self.__connection_InnerJoinMap

    @connection_InnerJoinMap.setter
    def connection_InnerJoinMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_InnerJoinMap__connection_InnerJoinMap", None)
        self.__connection_InnerJoinMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_ValidationRulesConnection114"):
                opp_val = getattr(old_value, "connection_ValidationRulesConnection114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_ValidationRulesConnection114"):
                opp_val = getattr(value, "connection_ValidationRulesConnection114", None)
                if opp_val is None:
                    setattr(value, "connection_ValidationRulesConnection114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_ConditionType:

    def __init__(self, inputColumn: str, function: str, operator: str, value: str, connection_ConditionType: "connection_ValidationRulesConnection" = None):
        self.inputColumn = inputColumn
        self.function = function
        self.operator = operator
        self.value = value
        self.connection_ConditionType = connection_ConditionType
        
        pass
    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def inputColumn(self):
        return self.__inputColumn

    @inputColumn.setter
    def inputColumn(self, inputColumn: str):
        self.__inputColumn = inputColumn


    @property
    def connection_ConditionType(self):
        return self.__connection_ConditionType

    @connection_ConditionType.setter
    def connection_ConditionType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_ConditionType__connection_ConditionType", None)
        self.__connection_ConditionType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_ValidationRulesConnection"):
                opp_val = getattr(old_value, "connection_ValidationRulesConnection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_ValidationRulesConnection"):
                opp_val = getattr(value, "connection_ValidationRulesConnection", None)
                if opp_val is None:
                    setattr(value, "connection_ValidationRulesConnection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MetadataColumn:

    pass
class connection_relational_TdColumn(MetadataColumn):

    def __init__(self, connection_relational_TdColumn: "relational_TdSqlDataType" = None):
        self.connection_relational_TdColumn = connection_relational_TdColumn
        
        pass
    @property
    def connection_relational_TdColumn(self):
        return self.__connection_relational_TdColumn

    @connection_relational_TdColumn.setter
    def connection_relational_TdColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_relational_TdColumn__connection_relational_TdColumn", None)
        self.__connection_relational_TdColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relational_TdSqlDataType"):
                opp_val = getattr(old_value, "relational_TdSqlDataType", None)
                if opp_val == self:
                    setattr(old_value, "relational_TdSqlDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relational_TdSqlDataType"):
                opp_val = getattr(value, "relational_TdSqlDataType", None)
                setattr(value, "relational_TdSqlDataType", self)

    def getContentType(self) :
        # TODO: Implement getContentType method
        pass

    def setContentType(self, connection_contentType):
        # TODO: Implement setContentType method
        pass

    def getJavaType(self) :
        # TODO: Implement getJavaType method
        pass

class connection_SAPTableField(MetadataColumn):

    def __init__(self, businessName: str, refTable: str):
        self.businessName = businessName
        self.refTable = refTable
        
        pass
    @property
    def businessName(self):
        return self.__businessName

    @businessName.setter
    def businessName(self, businessName: str):
        self.__businessName = businessName


    @property
    def refTable(self):
        return self.__refTable

    @refTable.setter
    def refTable(self, refTable: str):
        self.__refTable = refTable


class connection_EDIFACTColumn(MetadataColumn):

    def __init__(self, EDIColumnName: str, EDIXpath: str):
        self.EDIColumnName = EDIColumnName
        self.EDIXpath = EDIXpath
        
        pass
    @property
    def EDIColumnName(self):
        return self.__EDIColumnName

    @EDIColumnName.setter
    def EDIColumnName(self, EDIColumnName: str):
        self.__EDIColumnName = EDIColumnName


    @property
    def EDIXpath(self):
        return self.__EDIXpath

    @EDIXpath.setter
    def EDIXpath(self, EDIXpath: str):
        self.__EDIXpath = EDIXpath


class Package:

    pass
class connection_GenericPackage(Package):

    pass
class connection_ConceptTarget:

    def __init__(self, targetName: str, RelativeLoopExpression: str, conceptTargets: "connection_Concept" = None, ConceptTarget: "connection_Concept" = None):
        self.targetName = targetName
        self.RelativeLoopExpression = RelativeLoopExpression
        self.conceptTargets = conceptTargets
        self.ConceptTarget = ConceptTarget
        
        pass
    @property
    def RelativeLoopExpression(self):
        return self.__RelativeLoopExpression

    @RelativeLoopExpression.setter
    def RelativeLoopExpression(self, RelativeLoopExpression: str):
        self.__RelativeLoopExpression = RelativeLoopExpression


    @property
    def targetName(self):
        return self.__targetName

    @targetName.setter
    def targetName(self, targetName: str):
        self.__targetName = targetName


    @property
    def conceptTargets(self):
        return self.__conceptTargets

    @conceptTargets.setter
    def conceptTargets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_ConceptTarget__conceptTargets", None)
        self.__conceptTargets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Concept"):
                opp_val = getattr(old_value, "Concept", None)
                if opp_val == self:
                    setattr(old_value, "Concept", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Concept"):
                opp_val = getattr(value, "Concept", None)
                setattr(value, "Concept", self)

    @property
    def ConceptTarget(self):
        return self.__ConceptTarget

    @ConceptTarget.setter
    def ConceptTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_ConceptTarget__ConceptTarget", None)
        self.__ConceptTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema92"):
                opp_val = getattr(old_value, "schema92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema92"):
                opp_val = getattr(value, "schema92", None)
                if opp_val is None:
                    setattr(value, "schema92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TdTable:

    pass
class connection_SubscriberTable(TdTable):

    def __init__(self, system: bool, connection_SubscriberTable: "connection_CDCType" = None):
        self.system = system
        self.connection_SubscriberTable = connection_SubscriberTable
        
        pass
    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system: bool):
        self.__system = system


    @property
    def connection_SubscriberTable(self):
        return self.__connection_SubscriberTable

    @connection_SubscriberTable.setter
    def connection_SubscriberTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SubscriberTable__connection_SubscriberTable", None)
        self.__connection_SubscriberTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_CDCType85"):
                opp_val = getattr(old_value, "connection_CDCType85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_CDCType85"):
                opp_val = getattr(value, "connection_CDCType85", None)
                if opp_val is None:
                    setattr(value, "connection_CDCType85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_HL7FileNode:

    def __init__(self, Order: int, Attribute: str, DefaultValue: str, RelatedColumn: str, Repeatable: bool, FilePath: str, connection_HL7FileNode: "connection_HL7Connection" = None):
        self.Order = Order
        self.Attribute = Attribute
        self.DefaultValue = DefaultValue
        self.RelatedColumn = RelatedColumn
        self.Repeatable = Repeatable
        self.FilePath = FilePath
        self.connection_HL7FileNode = connection_HL7FileNode
        
        pass
    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, Attribute: str):
        self.__Attribute = Attribute


    @property
    def DefaultValue(self):
        return self.__DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue: str):
        self.__DefaultValue = DefaultValue


    @property
    def FilePath(self):
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath


    @property
    def Repeatable(self):
        return self.__Repeatable

    @Repeatable.setter
    def Repeatable(self, Repeatable: bool):
        self.__Repeatable = Repeatable


    @property
    def RelatedColumn(self):
        return self.__RelatedColumn

    @RelatedColumn.setter
    def RelatedColumn(self, RelatedColumn: str):
        self.__RelatedColumn = RelatedColumn


    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, Order: int):
        self.__Order = Order


    @property
    def connection_HL7FileNode(self):
        return self.__connection_HL7FileNode

    @connection_HL7FileNode.setter
    def connection_HL7FileNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_HL7FileNode__connection_HL7FileNode", None)
        self.__connection_HL7FileNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_HL7Connection"):
                opp_val = getattr(old_value, "connection_HL7Connection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_HL7Connection"):
                opp_val = getattr(value, "connection_HL7Connection", None)
                if opp_val is None:
                    setattr(value, "connection_HL7Connection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_WSDLParameter:

    def __init__(self, Element: str, source: str, Column: str, Expression: str, ParameterInfo: str, ParameterInfoParent: str, connection_WSDLParameter: "connection_WSDLSchemaConnection" = None, connection_WSDLParameter79: "connection_WSDLSchemaConnection" = None):
        self.Element = Element
        self.source = source
        self.Column = Column
        self.Expression = Expression
        self.ParameterInfo = ParameterInfo
        self.ParameterInfoParent = ParameterInfoParent
        self.connection_WSDLParameter = connection_WSDLParameter
        self.connection_WSDLParameter79 = connection_WSDLParameter79
        
        pass
    @property
    def Expression(self):
        return self.__Expression

    @Expression.setter
    def Expression(self, Expression: str):
        self.__Expression = Expression


    @property
    def Column(self):
        return self.__Column

    @Column.setter
    def Column(self, Column: str):
        self.__Column = Column


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def ParameterInfoParent(self):
        return self.__ParameterInfoParent

    @ParameterInfoParent.setter
    def ParameterInfoParent(self, ParameterInfoParent: str):
        self.__ParameterInfoParent = ParameterInfoParent


    @property
    def ParameterInfo(self):
        return self.__ParameterInfo

    @ParameterInfo.setter
    def ParameterInfo(self, ParameterInfo: str):
        self.__ParameterInfo = ParameterInfo


    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, Element: str):
        self.__Element = Element


    @property
    def connection_WSDLParameter79(self):
        return self.__connection_WSDLParameter79

    @connection_WSDLParameter79.setter
    def connection_WSDLParameter79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_WSDLParameter__connection_WSDLParameter79", None)
        self.__connection_WSDLParameter79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_WSDLSchemaConnection78"):
                opp_val = getattr(old_value, "connection_WSDLSchemaConnection78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_WSDLSchemaConnection78"):
                opp_val = getattr(value, "connection_WSDLSchemaConnection78", None)
                if opp_val is None:
                    setattr(value, "connection_WSDLSchemaConnection78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_WSDLParameter(self):
        return self.__connection_WSDLParameter

    @connection_WSDLParameter.setter
    def connection_WSDLParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_WSDLParameter__connection_WSDLParameter", None)
        self.__connection_WSDLParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_WSDLSchemaConnection"):
                opp_val = getattr(old_value, "connection_WSDLSchemaConnection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_WSDLSchemaConnection"):
                opp_val = getattr(value, "connection_WSDLSchemaConnection", None)
                if opp_val is None:
                    setattr(value, "connection_WSDLSchemaConnection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_XMLFileNode:

    def __init__(self, XMLPath: str, RelatedColumn: str, DefaultValue: str, Attribute: str, Order: int, Type: str, connection_XMLFileNode65: "connection_XmlFileConnection" = None, connection_XMLFileNode: "connection_XmlFileConnection" = None, connection_XMLFileNode111: "connection_BRMSConnection" = None, connection_XMLFileNode62: "connection_XmlFileConnection" = None, connection_XMLFileNode101: "connection_Concept" = None, connection_XMLFileNode95: "connection_Concept" = None, connection_XMLFileNode98: "connection_Concept" = None, connection_XMLFileNode105: "connection_BRMSConnection" = None, connection_XMLFileNode108: "connection_BRMSConnection" = None):
        self.XMLPath = XMLPath
        self.RelatedColumn = RelatedColumn
        self.DefaultValue = DefaultValue
        self.Attribute = Attribute
        self.Order = Order
        self.Type = Type
        self.connection_XMLFileNode65 = connection_XMLFileNode65
        self.connection_XMLFileNode = connection_XMLFileNode
        self.connection_XMLFileNode111 = connection_XMLFileNode111
        self.connection_XMLFileNode62 = connection_XMLFileNode62
        self.connection_XMLFileNode101 = connection_XMLFileNode101
        self.connection_XMLFileNode95 = connection_XMLFileNode95
        self.connection_XMLFileNode98 = connection_XMLFileNode98
        self.connection_XMLFileNode105 = connection_XMLFileNode105
        self.connection_XMLFileNode108 = connection_XMLFileNode108
        
        pass
    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, Order: int):
        self.__Order = Order


    @property
    def RelatedColumn(self):
        return self.__RelatedColumn

    @RelatedColumn.setter
    def RelatedColumn(self, RelatedColumn: str):
        self.__RelatedColumn = RelatedColumn


    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type


    @property
    def XMLPath(self):
        return self.__XMLPath

    @XMLPath.setter
    def XMLPath(self, XMLPath: str):
        self.__XMLPath = XMLPath


    @property
    def DefaultValue(self):
        return self.__DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue: str):
        self.__DefaultValue = DefaultValue


    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, Attribute: str):
        self.__Attribute = Attribute


    @property
    def connection_XMLFileNode95(self):
        return self.__connection_XMLFileNode95

    @connection_XMLFileNode95.setter
    def connection_XMLFileNode95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode95", None)
        self.__connection_XMLFileNode95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_Concept94"):
                opp_val = getattr(old_value, "connection_Concept94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_Concept94"):
                opp_val = getattr(value, "connection_Concept94", None)
                if opp_val is None:
                    setattr(value, "connection_Concept94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode98(self):
        return self.__connection_XMLFileNode98

    @connection_XMLFileNode98.setter
    def connection_XMLFileNode98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode98", None)
        self.__connection_XMLFileNode98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_Concept97"):
                opp_val = getattr(old_value, "connection_Concept97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_Concept97"):
                opp_val = getattr(value, "connection_Concept97", None)
                if opp_val is None:
                    setattr(value, "connection_Concept97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode(self):
        return self.__connection_XMLFileNode

    @connection_XMLFileNode.setter
    def connection_XMLFileNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode", None)
        self.__connection_XMLFileNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_XmlFileConnection"):
                opp_val = getattr(old_value, "connection_XmlFileConnection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_XmlFileConnection"):
                opp_val = getattr(value, "connection_XmlFileConnection", None)
                if opp_val is None:
                    setattr(value, "connection_XmlFileConnection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode101(self):
        return self.__connection_XMLFileNode101

    @connection_XMLFileNode101.setter
    def connection_XMLFileNode101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode101", None)
        self.__connection_XMLFileNode101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_Concept100"):
                opp_val = getattr(old_value, "connection_Concept100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_Concept100"):
                opp_val = getattr(value, "connection_Concept100", None)
                if opp_val is None:
                    setattr(value, "connection_Concept100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode65(self):
        return self.__connection_XMLFileNode65

    @connection_XMLFileNode65.setter
    def connection_XMLFileNode65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode65", None)
        self.__connection_XMLFileNode65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_XmlFileConnection64"):
                opp_val = getattr(old_value, "connection_XmlFileConnection64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_XmlFileConnection64"):
                opp_val = getattr(value, "connection_XmlFileConnection64", None)
                if opp_val is None:
                    setattr(value, "connection_XmlFileConnection64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode111(self):
        return self.__connection_XMLFileNode111

    @connection_XMLFileNode111.setter
    def connection_XMLFileNode111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode111", None)
        self.__connection_XMLFileNode111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_BRMSConnection110"):
                opp_val = getattr(old_value, "connection_BRMSConnection110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_BRMSConnection110"):
                opp_val = getattr(value, "connection_BRMSConnection110", None)
                if opp_val is None:
                    setattr(value, "connection_BRMSConnection110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode62(self):
        return self.__connection_XMLFileNode62

    @connection_XMLFileNode62.setter
    def connection_XMLFileNode62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode62", None)
        self.__connection_XMLFileNode62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_XmlFileConnection61"):
                opp_val = getattr(old_value, "connection_XmlFileConnection61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_XmlFileConnection61"):
                opp_val = getattr(value, "connection_XmlFileConnection61", None)
                if opp_val is None:
                    setattr(value, "connection_XmlFileConnection61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode108(self):
        return self.__connection_XMLFileNode108

    @connection_XMLFileNode108.setter
    def connection_XMLFileNode108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode108", None)
        self.__connection_XMLFileNode108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_BRMSConnection107"):
                opp_val = getattr(old_value, "connection_BRMSConnection107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_BRMSConnection107"):
                opp_val = getattr(value, "connection_BRMSConnection107", None)
                if opp_val is None:
                    setattr(value, "connection_BRMSConnection107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode105(self):
        return self.__connection_XMLFileNode105

    @connection_XMLFileNode105.setter
    def connection_XMLFileNode105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode105", None)
        self.__connection_XMLFileNode105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_BRMSConnection"):
                opp_val = getattr(old_value, "connection_BRMSConnection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_BRMSConnection"):
                opp_val = getattr(value, "connection_BRMSConnection", None)
                if opp_val is None:
                    setattr(value, "connection_BRMSConnection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_XmlXPathLoopDescriptor:

    def __init__(self, AbsoluteXPathQuery: str, LimitBoucle: str, XmlXPathLoopDescriptor67: "connection_SchemaTarget" = None, XmlXPathLoopDescriptor: "connection_XmlFileConnection" = None, schema: "connection_XmlFileConnection" = None, schema75: set["connection_SchemaTarget"] = None):
        self.AbsoluteXPathQuery = AbsoluteXPathQuery
        self.LimitBoucle = LimitBoucle
        self.XmlXPathLoopDescriptor67 = XmlXPathLoopDescriptor67
        self.XmlXPathLoopDescriptor = XmlXPathLoopDescriptor
        self.schema = schema
        self.schema75 = schema75 if schema75 is not None else set()
        
        pass
    @property
    def LimitBoucle(self):
        return self.__LimitBoucle

    @LimitBoucle.setter
    def LimitBoucle(self, LimitBoucle: str):
        self.__LimitBoucle = LimitBoucle


    @property
    def AbsoluteXPathQuery(self):
        return self.__AbsoluteXPathQuery

    @AbsoluteXPathQuery.setter
    def AbsoluteXPathQuery(self, AbsoluteXPathQuery: str):
        self.__AbsoluteXPathQuery = AbsoluteXPathQuery


    @property
    def XmlXPathLoopDescriptor67(self):
        return self.__XmlXPathLoopDescriptor67

    @XmlXPathLoopDescriptor67.setter
    def XmlXPathLoopDescriptor67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlXPathLoopDescriptor__XmlXPathLoopDescriptor67", None)
        self.__XmlXPathLoopDescriptor67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schemaTargets"):
                opp_val = getattr(old_value, "schemaTargets", None)
                if opp_val == self:
                    setattr(old_value, "schemaTargets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schemaTargets"):
                opp_val = getattr(value, "schemaTargets", None)
                setattr(value, "schemaTargets", self)

    @property
    def schema75(self):
        return self.__schema75

    @schema75.setter
    def schema75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlXPathLoopDescriptor__schema75", None)
        self.__schema75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SchemaTarget"):
                    opp_val = getattr(item, "SchemaTarget", None)
                    
                    if opp_val == self:
                        setattr(item, "SchemaTarget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SchemaTarget"):
                    opp_val = getattr(item, "SchemaTarget", None)
                    
                    setattr(item, "SchemaTarget", self)
                    

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlXPathLoopDescriptor__schema", None)
        self.__schema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XmlFileConnection"):
                opp_val = getattr(old_value, "XmlFileConnection", None)
                if opp_val == self:
                    setattr(old_value, "XmlFileConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XmlFileConnection"):
                opp_val = getattr(value, "XmlFileConnection", None)
                setattr(value, "XmlFileConnection", self)

    @property
    def XmlXPathLoopDescriptor(self):
        return self.__XmlXPathLoopDescriptor

    @XmlXPathLoopDescriptor.setter
    def XmlXPathLoopDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlXPathLoopDescriptor__XmlXPathLoopDescriptor", None)
        self.__XmlXPathLoopDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection58"):
                opp_val = getattr(old_value, "connection58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection58"):
                opp_val = getattr(value, "connection58", None)
                if opp_val is None:
                    setattr(value, "connection58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SAPFunctionParameterTable:

    pass
class connection_SchemaTarget:

    def __init__(self, RelativeXPathQuery: str, TagName: str, schemaTargets: "connection_XmlXPathLoopDescriptor" = None, SchemaTarget: "connection_XmlXPathLoopDescriptor" = None):
        self.RelativeXPathQuery = RelativeXPathQuery
        self.TagName = TagName
        self.schemaTargets = schemaTargets
        self.SchemaTarget = SchemaTarget
        
        pass
    @property
    def RelativeXPathQuery(self):
        return self.__RelativeXPathQuery

    @RelativeXPathQuery.setter
    def RelativeXPathQuery(self, RelativeXPathQuery: str):
        self.__RelativeXPathQuery = RelativeXPathQuery


    @property
    def TagName(self):
        return self.__TagName

    @TagName.setter
    def TagName(self, TagName: str):
        self.__TagName = TagName


    @property
    def schemaTargets(self):
        return self.__schemaTargets

    @schemaTargets.setter
    def schemaTargets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SchemaTarget__schemaTargets", None)
        self.__schemaTargets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "XmlXPathLoopDescriptor67"):
                opp_val = getattr(old_value, "XmlXPathLoopDescriptor67", None)
                if opp_val == self:
                    setattr(old_value, "XmlXPathLoopDescriptor67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XmlXPathLoopDescriptor67"):
                opp_val = getattr(value, "XmlXPathLoopDescriptor67", None)
                setattr(value, "XmlXPathLoopDescriptor67", self)

    @property
    def SchemaTarget(self):
        return self.__SchemaTarget

    @SchemaTarget.setter
    def SchemaTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SchemaTarget__SchemaTarget", None)
        self.__SchemaTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema75"):
                opp_val = getattr(old_value, "schema75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema75"):
                opp_val = getattr(value, "schema75", None)
                if opp_val is None:
                    setattr(value, "schema75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_SAPFunctionParamData:

    pass
class connection_SAPTestInputParameterTable(SAPFunctionParameterTable):

    pass
class connection_SAPBWTable(SAPTable):

    def __init__(self, modelType: str, active: bool, sourceSystemName: str, infoAreaName: str, innerIOType: str, connection_SAPBWTable: "connection_SAPConnection" = None, connection_SAPBWTable25: "connection_SAPConnection" = None, connection_SAPBWTable28: "connection_SAPConnection" = None, connection_SAPBWTable31: "connection_SAPConnection" = None):
        self.modelType = modelType
        self.active = active
        self.sourceSystemName = sourceSystemName
        self.infoAreaName = infoAreaName
        self.innerIOType = innerIOType
        self.connection_SAPBWTable = connection_SAPBWTable
        self.connection_SAPBWTable25 = connection_SAPBWTable25
        self.connection_SAPBWTable28 = connection_SAPBWTable28
        self.connection_SAPBWTable31 = connection_SAPBWTable31
        
        pass
    @property
    def innerIOType(self):
        return self.__innerIOType

    @innerIOType.setter
    def innerIOType(self, innerIOType: str):
        self.__innerIOType = innerIOType


    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active


    @property
    def infoAreaName(self):
        return self.__infoAreaName

    @infoAreaName.setter
    def infoAreaName(self, infoAreaName: str):
        self.__infoAreaName = infoAreaName


    @property
    def sourceSystemName(self):
        return self.__sourceSystemName

    @sourceSystemName.setter
    def sourceSystemName(self, sourceSystemName: str):
        self.__sourceSystemName = sourceSystemName


    @property
    def modelType(self):
        return self.__modelType

    @modelType.setter
    def modelType(self, modelType: str):
        self.__modelType = modelType


    @property
    def connection_SAPBWTable31(self):
        return self.__connection_SAPBWTable31

    @connection_SAPBWTable31.setter
    def connection_SAPBWTable31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPBWTable__connection_SAPBWTable31", None)
        self.__connection_SAPBWTable31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPConnection30"):
                opp_val = getattr(old_value, "connection_SAPConnection30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPConnection30"):
                opp_val = getattr(value, "connection_SAPConnection30", None)
                if opp_val is None:
                    setattr(value, "connection_SAPConnection30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_SAPBWTable25(self):
        return self.__connection_SAPBWTable25

    @connection_SAPBWTable25.setter
    def connection_SAPBWTable25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPBWTable__connection_SAPBWTable25", None)
        self.__connection_SAPBWTable25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPConnection24"):
                opp_val = getattr(old_value, "connection_SAPConnection24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPConnection24"):
                opp_val = getattr(value, "connection_SAPConnection24", None)
                if opp_val is None:
                    setattr(value, "connection_SAPConnection24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_SAPBWTable(self):
        return self.__connection_SAPBWTable

    @connection_SAPBWTable.setter
    def connection_SAPBWTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPBWTable__connection_SAPBWTable", None)
        self.__connection_SAPBWTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPConnection22"):
                opp_val = getattr(old_value, "connection_SAPConnection22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPConnection22"):
                opp_val = getattr(value, "connection_SAPConnection22", None)
                if opp_val is None:
                    setattr(value, "connection_SAPConnection22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_SAPBWTable28(self):
        return self.__connection_SAPBWTable28

    @connection_SAPBWTable28.setter
    def connection_SAPBWTable28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPBWTable__connection_SAPBWTable28", None)
        self.__connection_SAPBWTable28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPConnection27"):
                opp_val = getattr(old_value, "connection_SAPConnection27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPConnection27"):
                opp_val = getattr(value, "connection_SAPConnection27", None)
                if opp_val is None:
                    setattr(value, "connection_SAPConnection27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_AdditionalConnectionProperty:

    def __init__(self, propertyName: str, Value: str, connection_AdditionalConnectionProperty: "connection_SAPConnection" = None):
        self.propertyName = propertyName
        self.Value = Value
        self.connection_AdditionalConnectionProperty = connection_AdditionalConnectionProperty
        
        pass
    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value


    @property
    def propertyName(self):
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName


    @property
    def connection_AdditionalConnectionProperty(self):
        return self.__connection_AdditionalConnectionProperty

    @connection_AdditionalConnectionProperty.setter
    def connection_AdditionalConnectionProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_AdditionalConnectionProperty__connection_AdditionalConnectionProperty", None)
        self.__connection_AdditionalConnectionProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPConnection20"):
                opp_val = getattr(old_value, "connection_SAPConnection20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPConnection20"):
                opp_val = getattr(value, "connection_SAPConnection20", None)
                if opp_val is None:
                    setattr(value, "connection_SAPConnection20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_OutputSAPFunctionParameterTable(SAPFunctionParameterTable):

    pass
class connection_InputSAPFunctionParameterTable(SAPFunctionParameterTable):

    pass
class connection_CDCConnection:

    pass
class connection_Concept(TdTable):

    def __init__(self, conceptType: str, xPathPrefix: str, LoopExpression: str, LoopLimit: str, inputModel: bool, connection_Concept: "connection_MDMConnection" = None, connection_Concept100: set["connection_XMLFileNode"] = None, Concept: "connection_ConceptTarget" = None, schema92: set["connection_ConceptTarget"] = None, connection_Concept94: set["connection_XMLFileNode"] = None, connection_Concept97: set["connection_XMLFileNode"] = None):
        self.conceptType = conceptType
        self.xPathPrefix = xPathPrefix
        self.LoopExpression = LoopExpression
        self.LoopLimit = LoopLimit
        self.inputModel = inputModel
        self.connection_Concept = connection_Concept
        self.connection_Concept100 = connection_Concept100 if connection_Concept100 is not None else set()
        self.Concept = Concept
        self.schema92 = schema92 if schema92 is not None else set()
        self.connection_Concept94 = connection_Concept94 if connection_Concept94 is not None else set()
        self.connection_Concept97 = connection_Concept97 if connection_Concept97 is not None else set()
        
        pass
    @property
    def LoopExpression(self):
        return self.__LoopExpression

    @LoopExpression.setter
    def LoopExpression(self, LoopExpression: str):
        self.__LoopExpression = LoopExpression


    @property
    def conceptType(self):
        return self.__conceptType

    @conceptType.setter
    def conceptType(self, conceptType: str):
        self.__conceptType = conceptType


    @property
    def xPathPrefix(self):
        return self.__xPathPrefix

    @xPathPrefix.setter
    def xPathPrefix(self, xPathPrefix: str):
        self.__xPathPrefix = xPathPrefix


    @property
    def inputModel(self):
        return self.__inputModel

    @inputModel.setter
    def inputModel(self, inputModel: bool):
        self.__inputModel = inputModel


    @property
    def LoopLimit(self):
        return self.__LoopLimit

    @LoopLimit.setter
    def LoopLimit(self, LoopLimit: str):
        self.__LoopLimit = LoopLimit


    @property
    def connection_Concept94(self):
        return self.__connection_Concept94

    @connection_Concept94.setter
    def connection_Concept94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__connection_Concept94", None)
        self.__connection_Concept94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode95"):
                    opp_val = getattr(item, "connection_XMLFileNode95", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode95"):
                    opp_val = getattr(item, "connection_XMLFileNode95", None)
                    
                    setattr(item, "connection_XMLFileNode95", self)
                    

    @property
    def connection_Concept97(self):
        return self.__connection_Concept97

    @connection_Concept97.setter
    def connection_Concept97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__connection_Concept97", None)
        self.__connection_Concept97 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode98"):
                    opp_val = getattr(item, "connection_XMLFileNode98", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode98"):
                    opp_val = getattr(item, "connection_XMLFileNode98", None)
                    
                    setattr(item, "connection_XMLFileNode98", self)
                    

    @property
    def schema92(self):
        return self.__schema92

    @schema92.setter
    def schema92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__schema92", None)
        self.__schema92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConceptTarget"):
                    opp_val = getattr(item, "ConceptTarget", None)
                    
                    if opp_val == self:
                        setattr(item, "ConceptTarget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConceptTarget"):
                    opp_val = getattr(item, "ConceptTarget", None)
                    
                    setattr(item, "ConceptTarget", self)
                    

    @property
    def connection_Concept100(self):
        return self.__connection_Concept100

    @connection_Concept100.setter
    def connection_Concept100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__connection_Concept100", None)
        self.__connection_Concept100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode101"):
                    opp_val = getattr(item, "connection_XMLFileNode101", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode101", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode101"):
                    opp_val = getattr(item, "connection_XMLFileNode101", None)
                    
                    setattr(item, "connection_XMLFileNode101", self)
                    

    @property
    def connection_Concept(self):
        return self.__connection_Concept

    @connection_Concept.setter
    def connection_Concept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__connection_Concept", None)
        self.__connection_Concept = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_MDMConnection"):
                opp_val = getattr(old_value, "connection_MDMConnection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_MDMConnection"):
                opp_val = getattr(value, "connection_MDMConnection", None)
                if opp_val is None:
                    setattr(value, "connection_MDMConnection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Concept(self):
        return self.__Concept

    @Concept.setter
    def Concept(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__Concept", None)
        self.__Concept = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conceptTargets"):
                opp_val = getattr(old_value, "conceptTargets", None)
                if opp_val == self:
                    setattr(old_value, "conceptTargets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conceptTargets"):
                opp_val = getattr(value, "conceptTargets", None)
                setattr(value, "conceptTargets", self)

class Connection:

    pass
class connection_BRMSConnection(Connection):

    def __init__(self, xmlField: str, urlName: str, tacWebappName: str, className: str, moduleUsed: str, package: str, connection_BRMSConnection110: set["connection_XMLFileNode"] = None, connection_BRMSConnection: set["connection_XMLFileNode"] = None, connection_BRMSConnection107: set["connection_XMLFileNode"] = None):
        self.xmlField = xmlField
        self.urlName = urlName
        self.tacWebappName = tacWebappName
        self.className = className
        self.moduleUsed = moduleUsed
        self.package = package
        self.connection_BRMSConnection110 = connection_BRMSConnection110 if connection_BRMSConnection110 is not None else set()
        self.connection_BRMSConnection = connection_BRMSConnection if connection_BRMSConnection is not None else set()
        self.connection_BRMSConnection107 = connection_BRMSConnection107 if connection_BRMSConnection107 is not None else set()
        
        pass
    @property
    def urlName(self):
        return self.__urlName

    @urlName.setter
    def urlName(self, urlName: str):
        self.__urlName = urlName


    @property
    def tacWebappName(self):
        return self.__tacWebappName

    @tacWebappName.setter
    def tacWebappName(self, tacWebappName: str):
        self.__tacWebappName = tacWebappName


    @property
    def className(self):
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className


    @property
    def xmlField(self):
        return self.__xmlField

    @xmlField.setter
    def xmlField(self, xmlField: str):
        self.__xmlField = xmlField


    @property
    def moduleUsed(self):
        return self.__moduleUsed

    @moduleUsed.setter
    def moduleUsed(self, moduleUsed: str):
        self.__moduleUsed = moduleUsed


    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package


    @property
    def connection_BRMSConnection110(self):
        return self.__connection_BRMSConnection110

    @connection_BRMSConnection110.setter
    def connection_BRMSConnection110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_BRMSConnection__connection_BRMSConnection110", None)
        self.__connection_BRMSConnection110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode111"):
                    opp_val = getattr(item, "connection_XMLFileNode111", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode111"):
                    opp_val = getattr(item, "connection_XMLFileNode111", None)
                    
                    setattr(item, "connection_XMLFileNode111", self)
                    

    @property
    def connection_BRMSConnection(self):
        return self.__connection_BRMSConnection

    @connection_BRMSConnection.setter
    def connection_BRMSConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_BRMSConnection__connection_BRMSConnection", None)
        self.__connection_BRMSConnection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode105"):
                    opp_val = getattr(item, "connection_XMLFileNode105", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode105"):
                    opp_val = getattr(item, "connection_XMLFileNode105", None)
                    
                    setattr(item, "connection_XMLFileNode105", self)
                    

    @property
    def connection_BRMSConnection107(self):
        return self.__connection_BRMSConnection107

    @connection_BRMSConnection107.setter
    def connection_BRMSConnection107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_BRMSConnection__connection_BRMSConnection107", None)
        self.__connection_BRMSConnection107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode108"):
                    opp_val = getattr(item, "connection_XMLFileNode108", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode108"):
                    opp_val = getattr(item, "connection_XMLFileNode108", None)
                    
                    setattr(item, "connection_XMLFileNode108", self)
                    

class connection_MDMConnection(Connection):

    def __init__(self, Username: str, Password: str, Port: str, Server: str, Universe: str, Datamodel: str, Datacluster: str, protocol: str, context: str, serverUrl: str, connection_MDMConnection: set["connection_Concept"] = None):
        self.Username = Username
        self.Password = Password
        self.Port = Port
        self.Server = Server
        self.Universe = Universe
        self.Datamodel = Datamodel
        self.Datacluster = Datacluster
        self.protocol = protocol
        self.context = context
        self.serverUrl = serverUrl
        self.connection_MDMConnection = connection_MDMConnection if connection_MDMConnection is not None else set()
        
        pass
    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, Port: str):
        self.__Port = Port


    @property
    def Universe(self):
        return self.__Universe

    @Universe.setter
    def Universe(self, Universe: str):
        self.__Universe = Universe


    @property
    def Server(self):
        return self.__Server

    @Server.setter
    def Server(self, Server: str):
        self.__Server = Server


    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def serverUrl(self):
        return self.__serverUrl

    @serverUrl.setter
    def serverUrl(self, serverUrl: str):
        self.__serverUrl = serverUrl


    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context


    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: str):
        self.__protocol = protocol


    @property
    def Datacluster(self):
        return self.__Datacluster

    @Datacluster.setter
    def Datacluster(self, Datacluster: str):
        self.__Datacluster = Datacluster


    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username


    @property
    def Datamodel(self):
        return self.__Datamodel

    @Datamodel.setter
    def Datamodel(self, Datamodel: str):
        self.__Datamodel = Datamodel


    @property
    def connection_MDMConnection(self):
        return self.__connection_MDMConnection

    @connection_MDMConnection.setter
    def connection_MDMConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MDMConnection__connection_MDMConnection", None)
        self.__connection_MDMConnection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_Concept"):
                    opp_val = getattr(item, "connection_Concept", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_Concept", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_Concept"):
                    opp_val = getattr(item, "connection_Concept", None)
                    
                    setattr(item, "connection_Concept", self)
                    

    def getConnectionString(self) :
        # TODO: Implement getConnectionString method
        pass

class connection_XmlFileConnection(Connection):

    def __init__(self, inputModel: bool, outputFilePath: str, fileContent: str, XsdFilePath: str, XmlFilePath: str, Guess: bool, MaskXPattern: str, Encoding: str, connection_XmlFileConnection64: set["connection_XMLFileNode"] = None, connection58: set["connection_XmlXPathLoopDescriptor"] = None, connection_XmlFileConnection: set["connection_XMLFileNode"] = None, connection_XmlFileConnection61: set["connection_XMLFileNode"] = None, XmlFileConnection: "connection_XmlXPathLoopDescriptor" = None):
        self.inputModel = inputModel
        self.outputFilePath = outputFilePath
        self.fileContent = fileContent
        self.XsdFilePath = XsdFilePath
        self.XmlFilePath = XmlFilePath
        self.Guess = Guess
        self.MaskXPattern = MaskXPattern
        self.Encoding = Encoding
        self.connection_XmlFileConnection64 = connection_XmlFileConnection64 if connection_XmlFileConnection64 is not None else set()
        self.connection58 = connection58 if connection58 is not None else set()
        self.connection_XmlFileConnection = connection_XmlFileConnection if connection_XmlFileConnection is not None else set()
        self.connection_XmlFileConnection61 = connection_XmlFileConnection61 if connection_XmlFileConnection61 is not None else set()
        self.XmlFileConnection = XmlFileConnection
        
        pass
    @property
    def MaskXPattern(self):
        return self.__MaskXPattern

    @MaskXPattern.setter
    def MaskXPattern(self, MaskXPattern: str):
        self.__MaskXPattern = MaskXPattern


    @property
    def inputModel(self):
        return self.__inputModel

    @inputModel.setter
    def inputModel(self, inputModel: bool):
        self.__inputModel = inputModel


    @property
    def XsdFilePath(self):
        return self.__XsdFilePath

    @XsdFilePath.setter
    def XsdFilePath(self, XsdFilePath: str):
        self.__XsdFilePath = XsdFilePath


    @property
    def outputFilePath(self):
        return self.__outputFilePath

    @outputFilePath.setter
    def outputFilePath(self, outputFilePath: str):
        self.__outputFilePath = outputFilePath


    @property
    def fileContent(self):
        return self.__fileContent

    @fileContent.setter
    def fileContent(self, fileContent: str):
        self.__fileContent = fileContent


    @property
    def XmlFilePath(self):
        return self.__XmlFilePath

    @XmlFilePath.setter
    def XmlFilePath(self, XmlFilePath: str):
        self.__XmlFilePath = XmlFilePath


    @property
    def Encoding(self):
        return self.__Encoding

    @Encoding.setter
    def Encoding(self, Encoding: str):
        self.__Encoding = Encoding


    @property
    def Guess(self):
        return self.__Guess

    @Guess.setter
    def Guess(self, Guess: bool):
        self.__Guess = Guess


    @property
    def XmlFileConnection(self):
        return self.__XmlFileConnection

    @XmlFileConnection.setter
    def XmlFileConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlFileConnection__XmlFileConnection", None)
        self.__XmlFileConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema"):
                opp_val = getattr(old_value, "schema", None)
                if opp_val == self:
                    setattr(old_value, "schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema"):
                opp_val = getattr(value, "schema", None)
                setattr(value, "schema", self)

    @property
    def connection_XmlFileConnection64(self):
        return self.__connection_XmlFileConnection64

    @connection_XmlFileConnection64.setter
    def connection_XmlFileConnection64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlFileConnection__connection_XmlFileConnection64", None)
        self.__connection_XmlFileConnection64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode65"):
                    opp_val = getattr(item, "connection_XMLFileNode65", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode65"):
                    opp_val = getattr(item, "connection_XMLFileNode65", None)
                    
                    setattr(item, "connection_XMLFileNode65", self)
                    

    @property
    def connection_XmlFileConnection61(self):
        return self.__connection_XmlFileConnection61

    @connection_XmlFileConnection61.setter
    def connection_XmlFileConnection61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlFileConnection__connection_XmlFileConnection61", None)
        self.__connection_XmlFileConnection61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode62"):
                    opp_val = getattr(item, "connection_XMLFileNode62", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode62"):
                    opp_val = getattr(item, "connection_XMLFileNode62", None)
                    
                    setattr(item, "connection_XMLFileNode62", self)
                    

    @property
    def connection_XmlFileConnection(self):
        return self.__connection_XmlFileConnection

    @connection_XmlFileConnection.setter
    def connection_XmlFileConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlFileConnection__connection_XmlFileConnection", None)
        self.__connection_XmlFileConnection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode"):
                    opp_val = getattr(item, "connection_XMLFileNode", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode"):
                    opp_val = getattr(item, "connection_XMLFileNode", None)
                    
                    setattr(item, "connection_XMLFileNode", self)
                    

    @property
    def connection58(self):
        return self.__connection58

    @connection58.setter
    def connection58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlFileConnection__connection58", None)
        self.__connection58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "XmlXPathLoopDescriptor"):
                    opp_val = getattr(item, "XmlXPathLoopDescriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "XmlXPathLoopDescriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "XmlXPathLoopDescriptor"):
                    opp_val = getattr(item, "XmlXPathLoopDescriptor", None)
                    
                    setattr(item, "XmlXPathLoopDescriptor", self)
                    

class connection_WSDLSchemaConnection(Connection):

    def __init__(self, proxyHost: str, proxyPort: str, proxyUser: str, proxyPassword: str, Value: str, EndpointURI: str, Encoding: str, timeOut: int, isInputModel: bool, serverNameSpace: str, serverName: str, portNameSpace: str, portName: str, WSDL: str, needAuth: bool, methodName: str, parameters: str, UserName: str, Password: str, useProxy: bool, connection_WSDLSchemaConnection: set["connection_WSDLParameter"] = None, connection_WSDLSchemaConnection78: set["connection_WSDLParameter"] = None):
        self.proxyHost = proxyHost
        self.proxyPort = proxyPort
        self.proxyUser = proxyUser
        self.proxyPassword = proxyPassword
        self.Value = Value
        self.EndpointURI = EndpointURI
        self.Encoding = Encoding
        self.timeOut = timeOut
        self.isInputModel = isInputModel
        self.serverNameSpace = serverNameSpace
        self.serverName = serverName
        self.portNameSpace = portNameSpace
        self.portName = portName
        self.WSDL = WSDL
        self.needAuth = needAuth
        self.methodName = methodName
        self.parameters = parameters
        self.UserName = UserName
        self.Password = Password
        self.useProxy = useProxy
        self.connection_WSDLSchemaConnection = connection_WSDLSchemaConnection if connection_WSDLSchemaConnection is not None else set()
        self.connection_WSDLSchemaConnection78 = connection_WSDLSchemaConnection78 if connection_WSDLSchemaConnection78 is not None else set()
        
        pass
    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value


    @property
    def WSDL(self):
        return self.__WSDL

    @WSDL.setter
    def WSDL(self, WSDL: str):
        self.__WSDL = WSDL


    @property
    def UserName(self):
        return self.__UserName

    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName


    @property
    def proxyPort(self):
        return self.__proxyPort

    @proxyPort.setter
    def proxyPort(self, proxyPort: str):
        self.__proxyPort = proxyPort


    @property
    def methodName(self):
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName


    @property
    def timeOut(self):
        return self.__timeOut

    @timeOut.setter
    def timeOut(self, timeOut: int):
        self.__timeOut = timeOut


    @property
    def isInputModel(self):
        return self.__isInputModel

    @isInputModel.setter
    def isInputModel(self, isInputModel: bool):
        self.__isInputModel = isInputModel


    @property
    def useProxy(self):
        return self.__useProxy

    @useProxy.setter
    def useProxy(self, useProxy: bool):
        self.__useProxy = useProxy


    @property
    def proxyUser(self):
        return self.__proxyUser

    @proxyUser.setter
    def proxyUser(self, proxyUser: str):
        self.__proxyUser = proxyUser


    @property
    def EndpointURI(self):
        return self.__EndpointURI

    @EndpointURI.setter
    def EndpointURI(self, EndpointURI: str):
        self.__EndpointURI = EndpointURI


    @property
    def needAuth(self):
        return self.__needAuth

    @needAuth.setter
    def needAuth(self, needAuth: bool):
        self.__needAuth = needAuth


    @property
    def Encoding(self):
        return self.__Encoding

    @Encoding.setter
    def Encoding(self, Encoding: str):
        self.__Encoding = Encoding


    @property
    def proxyPassword(self):
        return self.__proxyPassword

    @proxyPassword.setter
    def proxyPassword(self, proxyPassword: str):
        self.__proxyPassword = proxyPassword


    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def serverName(self):
        return self.__serverName

    @serverName.setter
    def serverName(self, serverName: str):
        self.__serverName = serverName


    @property
    def portNameSpace(self):
        return self.__portNameSpace

    @portNameSpace.setter
    def portNameSpace(self, portNameSpace: str):
        self.__portNameSpace = portNameSpace


    @property
    def serverNameSpace(self):
        return self.__serverNameSpace

    @serverNameSpace.setter
    def serverNameSpace(self, serverNameSpace: str):
        self.__serverNameSpace = serverNameSpace


    @property
    def proxyHost(self):
        return self.__proxyHost

    @proxyHost.setter
    def proxyHost(self, proxyHost: str):
        self.__proxyHost = proxyHost


    @property
    def portName(self):
        return self.__portName

    @portName.setter
    def portName(self, portName: str):
        self.__portName = portName


    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters


    @property
    def connection_WSDLSchemaConnection(self):
        return self.__connection_WSDLSchemaConnection

    @connection_WSDLSchemaConnection.setter
    def connection_WSDLSchemaConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_WSDLSchemaConnection__connection_WSDLSchemaConnection", None)
        self.__connection_WSDLSchemaConnection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_WSDLParameter"):
                    opp_val = getattr(item, "connection_WSDLParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_WSDLParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_WSDLParameter"):
                    opp_val = getattr(item, "connection_WSDLParameter", None)
                    
                    setattr(item, "connection_WSDLParameter", self)
                    

    @property
    def connection_WSDLSchemaConnection78(self):
        return self.__connection_WSDLSchemaConnection78

    @connection_WSDLSchemaConnection78.setter
    def connection_WSDLSchemaConnection78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_WSDLSchemaConnection__connection_WSDLSchemaConnection78", None)
        self.__connection_WSDLSchemaConnection78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_WSDLParameter79"):
                    opp_val = getattr(item, "connection_WSDLParameter79", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_WSDLParameter79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_WSDLParameter79"):
                    opp_val = getattr(item, "connection_WSDLParameter79", None)
                    
                    setattr(item, "connection_WSDLParameter79", self)
                    

class connection_DatabaseConnection(Connection):

    def __init__(self, DatabaseType: str, DBRootPath: str, AdditionalParams: str, StandardSQL: bool, SystemSQL: bool, cdcTypeMode: str, SQLMode: bool, DriverJarPath: str, DriverClass: str, URL: str, dbVersionString: str, Port: str, Username: str, Password: str, ServerName: str, DatasourceName: str, FileFieldName: str, SID: str, SqlSynthax: str, StringQuote: str, NullChar: str, DbmsId: str, ProductId: str, UiSchema: str, connection_DatabaseConnection: set["connection_AdditionalProperties"] = None, connection13: "connection_CDCConnection" = None, DatabaseConnection: "connection_CDCConnection" = None):
        self.DatabaseType = DatabaseType
        self.DBRootPath = DBRootPath
        self.AdditionalParams = AdditionalParams
        self.StandardSQL = StandardSQL
        self.SystemSQL = SystemSQL
        self.cdcTypeMode = cdcTypeMode
        self.SQLMode = SQLMode
        self.DriverJarPath = DriverJarPath
        self.DriverClass = DriverClass
        self.URL = URL
        self.dbVersionString = dbVersionString
        self.Port = Port
        self.Username = Username
        self.Password = Password
        self.ServerName = ServerName
        self.DatasourceName = DatasourceName
        self.FileFieldName = FileFieldName
        self.SID = SID
        self.SqlSynthax = SqlSynthax
        self.StringQuote = StringQuote
        self.NullChar = NullChar
        self.DbmsId = DbmsId
        self.ProductId = ProductId
        self.UiSchema = UiSchema
        self.connection_DatabaseConnection = connection_DatabaseConnection if connection_DatabaseConnection is not None else set()
        self.connection13 = connection13
        self.DatabaseConnection = DatabaseConnection
        
        pass
    @property
    def AdditionalParams(self):
        return self.__AdditionalParams

    @AdditionalParams.setter
    def AdditionalParams(self, AdditionalParams: str):
        self.__AdditionalParams = AdditionalParams


    @property
    def FileFieldName(self):
        return self.__FileFieldName

    @FileFieldName.setter
    def FileFieldName(self, FileFieldName: str):
        self.__FileFieldName = FileFieldName


    @property
    def DriverJarPath(self):
        return self.__DriverJarPath

    @DriverJarPath.setter
    def DriverJarPath(self, DriverJarPath: str):
        self.__DriverJarPath = DriverJarPath


    @property
    def DatasourceName(self):
        return self.__DatasourceName

    @DatasourceName.setter
    def DatasourceName(self, DatasourceName: str):
        self.__DatasourceName = DatasourceName


    @property
    def dbVersionString(self):
        return self.__dbVersionString

    @dbVersionString.setter
    def dbVersionString(self, dbVersionString: str):
        self.__dbVersionString = dbVersionString


    @property
    def SQLMode(self):
        return self.__SQLMode

    @SQLMode.setter
    def SQLMode(self, SQLMode: bool):
        self.__SQLMode = SQLMode


    @property
    def ProductId(self):
        return self.__ProductId

    @ProductId.setter
    def ProductId(self, ProductId: str):
        self.__ProductId = ProductId


    @property
    def DBRootPath(self):
        return self.__DBRootPath

    @DBRootPath.setter
    def DBRootPath(self, DBRootPath: str):
        self.__DBRootPath = DBRootPath


    @property
    def DriverClass(self):
        return self.__DriverClass

    @DriverClass.setter
    def DriverClass(self, DriverClass: str):
        self.__DriverClass = DriverClass


    @property
    def ServerName(self):
        return self.__ServerName

    @ServerName.setter
    def ServerName(self, ServerName: str):
        self.__ServerName = ServerName


    @property
    def URL(self):
        return self.__URL

    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL


    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, Port: str):
        self.__Port = Port


    @property
    def SqlSynthax(self):
        return self.__SqlSynthax

    @SqlSynthax.setter
    def SqlSynthax(self, SqlSynthax: str):
        self.__SqlSynthax = SqlSynthax


    @property
    def DatabaseType(self):
        return self.__DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType: str):
        self.__DatabaseType = DatabaseType


    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def DbmsId(self):
        return self.__DbmsId

    @DbmsId.setter
    def DbmsId(self, DbmsId: str):
        self.__DbmsId = DbmsId


    @property
    def StandardSQL(self):
        return self.__StandardSQL

    @StandardSQL.setter
    def StandardSQL(self, StandardSQL: bool):
        self.__StandardSQL = StandardSQL


    @property
    def SystemSQL(self):
        return self.__SystemSQL

    @SystemSQL.setter
    def SystemSQL(self, SystemSQL: bool):
        self.__SystemSQL = SystemSQL


    @property
    def SID(self):
        return self.__SID

    @SID.setter
    def SID(self, SID: str):
        self.__SID = SID


    @property
    def cdcTypeMode(self):
        return self.__cdcTypeMode

    @cdcTypeMode.setter
    def cdcTypeMode(self, cdcTypeMode: str):
        self.__cdcTypeMode = cdcTypeMode


    @property
    def NullChar(self):
        return self.__NullChar

    @NullChar.setter
    def NullChar(self, NullChar: str):
        self.__NullChar = NullChar


    @property
    def StringQuote(self):
        return self.__StringQuote

    @StringQuote.setter
    def StringQuote(self, StringQuote: str):
        self.__StringQuote = StringQuote


    @property
    def UiSchema(self):
        return self.__UiSchema

    @UiSchema.setter
    def UiSchema(self, UiSchema: str):
        self.__UiSchema = UiSchema


    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username


    @property
    def connection_DatabaseConnection(self):
        return self.__connection_DatabaseConnection

    @connection_DatabaseConnection.setter
    def connection_DatabaseConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_DatabaseConnection__connection_DatabaseConnection", None)
        self.__connection_DatabaseConnection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_AdditionalProperties15"):
                    opp_val = getattr(item, "connection_AdditionalProperties15", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_AdditionalProperties15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_AdditionalProperties15"):
                    opp_val = getattr(item, "connection_AdditionalProperties15", None)
                    
                    setattr(item, "connection_AdditionalProperties15", self)
                    

    @property
    def connection13(self):
        return self.__connection13

    @connection13.setter
    def connection13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_DatabaseConnection__connection13", None)
        self.__connection13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CDCConnection"):
                opp_val = getattr(old_value, "CDCConnection", None)
                if opp_val == self:
                    setattr(old_value, "CDCConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CDCConnection"):
                opp_val = getattr(value, "CDCConnection", None)
                setattr(value, "CDCConnection", self)

    @property
    def DatabaseConnection(self):
        return self.__DatabaseConnection

    @DatabaseConnection.setter
    def DatabaseConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_DatabaseConnection__DatabaseConnection", None)
        self.__DatabaseConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cdcConns"):
                opp_val = getattr(old_value, "cdcConns", None)
                if opp_val == self:
                    setattr(old_value, "cdcConns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cdcConns"):
                opp_val = getattr(value, "cdcConns", None)
                setattr(value, "cdcConns", self)

class connection_SAPConnection(Connection):

    def __init__(self, Host: str, Username: str, Password: str, Client: str, SystemNumber: str, Language: str, currentFucntion: str, jcoVersion: str, connection_SAPConnection: set["connection_SAPFunctionUnit"] = None, connection18: set["connection_SAPIDocUnit"] = None, connection_SAPConnection20: set["connection_AdditionalConnectionProperty"] = None, connection_SAPConnection22: set["connection_SAPBWTable"] = None, connection_SAPConnection24: set["connection_SAPBWTable"] = None, connection_SAPConnection27: set["connection_SAPBWTable"] = None, connection_SAPConnection30: set["connection_SAPBWTable"] = None, connection_SAPConnection40: "connection_SAPFunctionUnit" = None, SAPConnection: "connection_SAPIDocUnit" = None):
        self.Host = Host
        self.Username = Username
        self.Password = Password
        self.Client = Client
        self.SystemNumber = SystemNumber
        self.Language = Language
        self.currentFucntion = currentFucntion
        self.jcoVersion = jcoVersion
        self.connection_SAPConnection = connection_SAPConnection if connection_SAPConnection is not None else set()
        self.connection18 = connection18 if connection18 is not None else set()
        self.connection_SAPConnection20 = connection_SAPConnection20 if connection_SAPConnection20 is not None else set()
        self.connection_SAPConnection22 = connection_SAPConnection22 if connection_SAPConnection22 is not None else set()
        self.connection_SAPConnection24 = connection_SAPConnection24 if connection_SAPConnection24 is not None else set()
        self.connection_SAPConnection27 = connection_SAPConnection27 if connection_SAPConnection27 is not None else set()
        self.connection_SAPConnection30 = connection_SAPConnection30 if connection_SAPConnection30 is not None else set()
        self.connection_SAPConnection40 = connection_SAPConnection40
        self.SAPConnection = SAPConnection
        
        pass
    @property
    def Client(self):
        return self.__Client

    @Client.setter
    def Client(self, Client: str):
        self.__Client = Client


    @property
    def Host(self):
        return self.__Host

    @Host.setter
    def Host(self, Host: str):
        self.__Host = Host


    @property
    def SystemNumber(self):
        return self.__SystemNumber

    @SystemNumber.setter
    def SystemNumber(self, SystemNumber: str):
        self.__SystemNumber = SystemNumber


    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username


    @property
    def Language(self):
        return self.__Language

    @Language.setter
    def Language(self, Language: str):
        self.__Language = Language


    @property
    def currentFucntion(self):
        return self.__currentFucntion

    @currentFucntion.setter
    def currentFucntion(self, currentFucntion: str):
        self.__currentFucntion = currentFucntion


    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def jcoVersion(self):
        return self.__jcoVersion

    @jcoVersion.setter
    def jcoVersion(self, jcoVersion: str):
        self.__jcoVersion = jcoVersion


    @property
    def connection_SAPConnection30(self):
        return self.__connection_SAPConnection30

    @connection_SAPConnection30.setter
    def connection_SAPConnection30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__connection_SAPConnection30", None)
        self.__connection_SAPConnection30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_SAPBWTable31"):
                    opp_val = getattr(item, "connection_SAPBWTable31", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_SAPBWTable31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_SAPBWTable31"):
                    opp_val = getattr(item, "connection_SAPBWTable31", None)
                    
                    setattr(item, "connection_SAPBWTable31", self)
                    

    @property
    def connection_SAPConnection40(self):
        return self.__connection_SAPConnection40

    @connection_SAPConnection40.setter
    def connection_SAPConnection40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__connection_SAPConnection40", None)
        self.__connection_SAPConnection40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionUnit39"):
                opp_val = getattr(old_value, "connection_SAPFunctionUnit39", None)
                if opp_val == self:
                    setattr(old_value, "connection_SAPFunctionUnit39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionUnit39"):
                opp_val = getattr(value, "connection_SAPFunctionUnit39", None)
                setattr(value, "connection_SAPFunctionUnit39", self)

    @property
    def connection_SAPConnection20(self):
        return self.__connection_SAPConnection20

    @connection_SAPConnection20.setter
    def connection_SAPConnection20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__connection_SAPConnection20", None)
        self.__connection_SAPConnection20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_AdditionalConnectionProperty"):
                    opp_val = getattr(item, "connection_AdditionalConnectionProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_AdditionalConnectionProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_AdditionalConnectionProperty"):
                    opp_val = getattr(item, "connection_AdditionalConnectionProperty", None)
                    
                    setattr(item, "connection_AdditionalConnectionProperty", self)
                    

    @property
    def connection_SAPConnection24(self):
        return self.__connection_SAPConnection24

    @connection_SAPConnection24.setter
    def connection_SAPConnection24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__connection_SAPConnection24", None)
        self.__connection_SAPConnection24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_SAPBWTable25"):
                    opp_val = getattr(item, "connection_SAPBWTable25", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_SAPBWTable25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_SAPBWTable25"):
                    opp_val = getattr(item, "connection_SAPBWTable25", None)
                    
                    setattr(item, "connection_SAPBWTable25", self)
                    

    @property
    def connection_SAPConnection22(self):
        return self.__connection_SAPConnection22

    @connection_SAPConnection22.setter
    def connection_SAPConnection22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__connection_SAPConnection22", None)
        self.__connection_SAPConnection22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_SAPBWTable"):
                    opp_val = getattr(item, "connection_SAPBWTable", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_SAPBWTable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_SAPBWTable"):
                    opp_val = getattr(item, "connection_SAPBWTable", None)
                    
                    setattr(item, "connection_SAPBWTable", self)
                    

    @property
    def connection_SAPConnection(self):
        return self.__connection_SAPConnection

    @connection_SAPConnection.setter
    def connection_SAPConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__connection_SAPConnection", None)
        self.__connection_SAPConnection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_SAPFunctionUnit"):
                    opp_val = getattr(item, "connection_SAPFunctionUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_SAPFunctionUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_SAPFunctionUnit"):
                    opp_val = getattr(item, "connection_SAPFunctionUnit", None)
                    
                    setattr(item, "connection_SAPFunctionUnit", self)
                    

    @property
    def SAPConnection(self):
        return self.__SAPConnection

    @SAPConnection.setter
    def SAPConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__SAPConnection", None)
        self.__SAPConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IDocs"):
                opp_val = getattr(old_value, "IDocs", None)
                if opp_val == self:
                    setattr(old_value, "IDocs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IDocs"):
                opp_val = getattr(value, "IDocs", None)
                setattr(value, "IDocs", self)

    @property
    def connection18(self):
        return self.__connection18

    @connection18.setter
    def connection18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__connection18", None)
        self.__connection18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAPIDocUnit"):
                    opp_val = getattr(item, "SAPIDocUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "SAPIDocUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAPIDocUnit"):
                    opp_val = getattr(item, "SAPIDocUnit", None)
                    
                    setattr(item, "SAPIDocUnit", self)
                    

    @property
    def connection_SAPConnection27(self):
        return self.__connection_SAPConnection27

    @connection_SAPConnection27.setter
    def connection_SAPConnection27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__connection_SAPConnection27", None)
        self.__connection_SAPConnection27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_SAPBWTable28"):
                    opp_val = getattr(item, "connection_SAPBWTable28", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_SAPBWTable28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_SAPBWTable28"):
                    opp_val = getattr(item, "connection_SAPBWTable28", None)
                    
                    setattr(item, "connection_SAPBWTable28", self)
                    

class connection_EDIFACTConnection(Connection):

    def __init__(self, XmlName: str, FileName: str, XmlPath: str):
        self.XmlName = XmlName
        self.FileName = FileName
        self.XmlPath = XmlPath
        
        pass
    @property
    def XmlName(self):
        return self.__XmlName

    @XmlName.setter
    def XmlName(self, XmlName: str):
        self.__XmlName = XmlName


    @property
    def FileName(self):
        return self.__FileName

    @FileName.setter
    def FileName(self, FileName: str):
        self.__FileName = FileName


    @property
    def XmlPath(self):
        return self.__XmlPath

    @XmlPath.setter
    def XmlPath(self, XmlPath: str):
        self.__XmlPath = XmlPath


class connection_LdifFileConnection(Connection):

    def __init__(self, value: str, FilePath: str, LimitEntry: int, UseLimit: bool, Server: str):
        self.value = value
        self.FilePath = FilePath
        self.LimitEntry = LimitEntry
        self.UseLimit = UseLimit
        self.Server = Server
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def FilePath(self):
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath


    @property
    def UseLimit(self):
        return self.__UseLimit

    @UseLimit.setter
    def UseLimit(self, UseLimit: bool):
        self.__UseLimit = UseLimit


    @property
    def LimitEntry(self):
        return self.__LimitEntry

    @LimitEntry.setter
    def LimitEntry(self, LimitEntry: int):
        self.__LimitEntry = LimitEntry


    @property
    def Server(self):
        return self.__Server

    @Server.setter
    def Server(self, Server: str):
        self.__Server = Server


class connection_GenericSchemaConnection(Connection):

    def __init__(self, mappingTypeUsed: bool, mappingTypeId: str):
        self.mappingTypeUsed = mappingTypeUsed
        self.mappingTypeId = mappingTypeId
        
        pass
    @property
    def mappingTypeId(self):
        return self.__mappingTypeId

    @mappingTypeId.setter
    def mappingTypeId(self, mappingTypeId: str):
        self.__mappingTypeId = mappingTypeId


    @property
    def mappingTypeUsed(self):
        return self.__mappingTypeUsed

    @mappingTypeUsed.setter
    def mappingTypeUsed(self, mappingTypeUsed: bool):
        self.__mappingTypeUsed = mappingTypeUsed


class connection_HeaderFooterConnection(Connection):

    def __init__(self, isHeader: bool, imports: str, mainCode: str, libraries: str):
        self.isHeader = isHeader
        self.imports = imports
        self.mainCode = mainCode
        self.libraries = libraries
        
        pass
    @property
    def imports(self):
        return self.__imports

    @imports.setter
    def imports(self, imports: str):
        self.__imports = imports


    @property
    def libraries(self):
        return self.__libraries

    @libraries.setter
    def libraries(self, libraries: str):
        self.__libraries = libraries


    @property
    def isHeader(self):
        return self.__isHeader

    @isHeader.setter
    def isHeader(self, isHeader: bool):
        self.__isHeader = isHeader


    @property
    def mainCode(self):
        return self.__mainCode

    @mainCode.setter
    def mainCode(self, mainCode: str):
        self.__mainCode = mainCode


class connection_FTPConnection(Connection):

    def __init__(self, Host: str, Port: str, Username: str, Password: str, Mode: str, Ecoding: str, SFTP: bool, FTPS: bool, Method: str, Privatekey: str, Passphrase: str, KeystoreFile: str, KeystorePassword: str, Usesocks: bool, Proxyhost: str, Proxyport: str, Proxyuser: str, Proxypassword: str, CustomEncode: str):
        self.Host = Host
        self.Port = Port
        self.Username = Username
        self.Password = Password
        self.Mode = Mode
        self.Ecoding = Ecoding
        self.SFTP = SFTP
        self.FTPS = FTPS
        self.Method = Method
        self.Privatekey = Privatekey
        self.Passphrase = Passphrase
        self.KeystoreFile = KeystoreFile
        self.KeystorePassword = KeystorePassword
        self.Usesocks = Usesocks
        self.Proxyhost = Proxyhost
        self.Proxyport = Proxyport
        self.Proxyuser = Proxyuser
        self.Proxypassword = Proxypassword
        self.CustomEncode = CustomEncode
        
        pass
    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, Method: str):
        self.__Method = Method


    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def FTPS(self):
        return self.__FTPS

    @FTPS.setter
    def FTPS(self, FTPS: bool):
        self.__FTPS = FTPS


    @property
    def Usesocks(self):
        return self.__Usesocks

    @Usesocks.setter
    def Usesocks(self, Usesocks: bool):
        self.__Usesocks = Usesocks


    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, Port: str):
        self.__Port = Port


    @property
    def Proxyhost(self):
        return self.__Proxyhost

    @Proxyhost.setter
    def Proxyhost(self, Proxyhost: str):
        self.__Proxyhost = Proxyhost


    @property
    def Proxyuser(self):
        return self.__Proxyuser

    @Proxyuser.setter
    def Proxyuser(self, Proxyuser: str):
        self.__Proxyuser = Proxyuser


    @property
    def Passphrase(self):
        return self.__Passphrase

    @Passphrase.setter
    def Passphrase(self, Passphrase: str):
        self.__Passphrase = Passphrase


    @property
    def Host(self):
        return self.__Host

    @Host.setter
    def Host(self, Host: str):
        self.__Host = Host


    @property
    def SFTP(self):
        return self.__SFTP

    @SFTP.setter
    def SFTP(self, SFTP: bool):
        self.__SFTP = SFTP


    @property
    def Proxypassword(self):
        return self.__Proxypassword

    @Proxypassword.setter
    def Proxypassword(self, Proxypassword: str):
        self.__Proxypassword = Proxypassword


    @property
    def Mode(self):
        return self.__Mode

    @Mode.setter
    def Mode(self, Mode: str):
        self.__Mode = Mode


    @property
    def Privatekey(self):
        return self.__Privatekey

    @Privatekey.setter
    def Privatekey(self, Privatekey: str):
        self.__Privatekey = Privatekey


    @property
    def CustomEncode(self):
        return self.__CustomEncode

    @CustomEncode.setter
    def CustomEncode(self, CustomEncode: str):
        self.__CustomEncode = CustomEncode


    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username


    @property
    def KeystorePassword(self):
        return self.__KeystorePassword

    @KeystorePassword.setter
    def KeystorePassword(self, KeystorePassword: str):
        self.__KeystorePassword = KeystorePassword


    @property
    def Proxyport(self):
        return self.__Proxyport

    @Proxyport.setter
    def Proxyport(self, Proxyport: str):
        self.__Proxyport = Proxyport


    @property
    def KeystoreFile(self):
        return self.__KeystoreFile

    @KeystoreFile.setter
    def KeystoreFile(self, KeystoreFile: str):
        self.__KeystoreFile = KeystoreFile


    @property
    def Ecoding(self):
        return self.__Ecoding

    @Ecoding.setter
    def Ecoding(self, Ecoding: str):
        self.__Ecoding = Ecoding


class connection_SalesforceSchemaConnection(Connection):

    def __init__(self, callbackPort: str, salesforceVersion: str, token: str, loginType: str, webServiceUrl: str, userName: str, password: str, moduleName: str, queryCondition: str, useCustomModuleName: bool, useProxy: bool, proxyHost: str, proxyPort: str, proxyUsername: str, proxyPassword: str, batchSize: str, useHttpProxy: bool, useAlphbet: bool, timeOut: str, webServiceUrlTextForOAuth: str, consumeKey: str, consumeSecret: str, callbackHost: str, SalesforceSchemaConnection: "connection_SalesforceModuleUnit" = None, connection81: set["connection_SalesforceModuleUnit"] = None):
        self.callbackPort = callbackPort
        self.salesforceVersion = salesforceVersion
        self.token = token
        self.loginType = loginType
        self.webServiceUrl = webServiceUrl
        self.userName = userName
        self.password = password
        self.moduleName = moduleName
        self.queryCondition = queryCondition
        self.useCustomModuleName = useCustomModuleName
        self.useProxy = useProxy
        self.proxyHost = proxyHost
        self.proxyPort = proxyPort
        self.proxyUsername = proxyUsername
        self.proxyPassword = proxyPassword
        self.batchSize = batchSize
        self.useHttpProxy = useHttpProxy
        self.useAlphbet = useAlphbet
        self.timeOut = timeOut
        self.webServiceUrlTextForOAuth = webServiceUrlTextForOAuth
        self.consumeKey = consumeKey
        self.consumeSecret = consumeSecret
        self.callbackHost = callbackHost
        self.SalesforceSchemaConnection = SalesforceSchemaConnection
        self.connection81 = connection81 if connection81 is not None else set()
        
        pass
    @property
    def queryCondition(self):
        return self.__queryCondition

    @queryCondition.setter
    def queryCondition(self, queryCondition: str):
        self.__queryCondition = queryCondition


    @property
    def useHttpProxy(self):
        return self.__useHttpProxy

    @useHttpProxy.setter
    def useHttpProxy(self, useHttpProxy: bool):
        self.__useHttpProxy = useHttpProxy


    @property
    def callbackHost(self):
        return self.__callbackHost

    @callbackHost.setter
    def callbackHost(self, callbackHost: str):
        self.__callbackHost = callbackHost


    @property
    def batchSize(self):
        return self.__batchSize

    @batchSize.setter
    def batchSize(self, batchSize: str):
        self.__batchSize = batchSize


    @property
    def loginType(self):
        return self.__loginType

    @loginType.setter
    def loginType(self, loginType: str):
        self.__loginType = loginType


    @property
    def salesforceVersion(self):
        return self.__salesforceVersion

    @salesforceVersion.setter
    def salesforceVersion(self, salesforceVersion: str):
        self.__salesforceVersion = salesforceVersion


    @property
    def proxyPort(self):
        return self.__proxyPort

    @proxyPort.setter
    def proxyPort(self, proxyPort: str):
        self.__proxyPort = proxyPort


    @property
    def proxyHost(self):
        return self.__proxyHost

    @proxyHost.setter
    def proxyHost(self, proxyHost: str):
        self.__proxyHost = proxyHost


    @property
    def callbackPort(self):
        return self.__callbackPort

    @callbackPort.setter
    def callbackPort(self, callbackPort: str):
        self.__callbackPort = callbackPort


    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token


    @property
    def moduleName(self):
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName


    @property
    def webServiceUrlTextForOAuth(self):
        return self.__webServiceUrlTextForOAuth

    @webServiceUrlTextForOAuth.setter
    def webServiceUrlTextForOAuth(self, webServiceUrlTextForOAuth: str):
        self.__webServiceUrlTextForOAuth = webServiceUrlTextForOAuth


    @property
    def timeOut(self):
        return self.__timeOut

    @timeOut.setter
    def timeOut(self, timeOut: str):
        self.__timeOut = timeOut


    @property
    def useCustomModuleName(self):
        return self.__useCustomModuleName

    @useCustomModuleName.setter
    def useCustomModuleName(self, useCustomModuleName: bool):
        self.__useCustomModuleName = useCustomModuleName


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def useAlphbet(self):
        return self.__useAlphbet

    @useAlphbet.setter
    def useAlphbet(self, useAlphbet: bool):
        self.__useAlphbet = useAlphbet


    @property
    def consumeKey(self):
        return self.__consumeKey

    @consumeKey.setter
    def consumeKey(self, consumeKey: str):
        self.__consumeKey = consumeKey


    @property
    def useProxy(self):
        return self.__useProxy

    @useProxy.setter
    def useProxy(self, useProxy: bool):
        self.__useProxy = useProxy


    @property
    def proxyPassword(self):
        return self.__proxyPassword

    @proxyPassword.setter
    def proxyPassword(self, proxyPassword: str):
        self.__proxyPassword = proxyPassword


    @property
    def consumeSecret(self):
        return self.__consumeSecret

    @consumeSecret.setter
    def consumeSecret(self, consumeSecret: str):
        self.__consumeSecret = consumeSecret


    @property
    def proxyUsername(self):
        return self.__proxyUsername

    @proxyUsername.setter
    def proxyUsername(self, proxyUsername: str):
        self.__proxyUsername = proxyUsername


    @property
    def webServiceUrl(self):
        return self.__webServiceUrl

    @webServiceUrl.setter
    def webServiceUrl(self, webServiceUrl: str):
        self.__webServiceUrl = webServiceUrl


    @property
    def userName(self):
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName


    @property
    def connection81(self):
        return self.__connection81

    @connection81.setter
    def connection81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SalesforceSchemaConnection__connection81", None)
        self.__connection81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SalesforceModuleUnit"):
                    opp_val = getattr(item, "SalesforceModuleUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "SalesforceModuleUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SalesforceModuleUnit"):
                    opp_val = getattr(item, "SalesforceModuleUnit", None)
                    
                    setattr(item, "SalesforceModuleUnit", self)
                    

    @property
    def SalesforceSchemaConnection(self):
        return self.__SalesforceSchemaConnection

    @SalesforceSchemaConnection.setter
    def SalesforceSchemaConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SalesforceSchemaConnection__SalesforceSchemaConnection", None)
        self.__SalesforceSchemaConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modules"):
                opp_val = getattr(old_value, "modules", None)
                if opp_val == self:
                    setattr(old_value, "modules", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modules"):
                opp_val = getattr(value, "modules", None)
                setattr(value, "modules", self)

class connection_LDAPSchemaConnection(Connection):

    def __init__(self, Host: str, Port: str, Protocol: str, Filter: str, Separator: str, UseAdvanced: bool, StorePath: str, UseLimit: bool, UseAuthen: bool, BindPrincipal: str, BindPassword: str, LimitValue: int, EncryptionMethodName: str, Value: str, SavePassword: bool, Aliases: str, Referrals: str, CountLimit: str, TimeOutLimit: str, BaseDNs: str, GetBaseDNsFromRoot: bool, ReturnAttributes: str, SelectedDN: str):
        self.Host = Host
        self.Port = Port
        self.Protocol = Protocol
        self.Filter = Filter
        self.Separator = Separator
        self.UseAdvanced = UseAdvanced
        self.StorePath = StorePath
        self.UseLimit = UseLimit
        self.UseAuthen = UseAuthen
        self.BindPrincipal = BindPrincipal
        self.BindPassword = BindPassword
        self.LimitValue = LimitValue
        self.EncryptionMethodName = EncryptionMethodName
        self.Value = Value
        self.SavePassword = SavePassword
        self.Aliases = Aliases
        self.Referrals = Referrals
        self.CountLimit = CountLimit
        self.TimeOutLimit = TimeOutLimit
        self.BaseDNs = BaseDNs
        self.GetBaseDNsFromRoot = GetBaseDNsFromRoot
        self.ReturnAttributes = ReturnAttributes
        self.SelectedDN = SelectedDN
        
        pass
    @property
    def Protocol(self):
        return self.__Protocol

    @Protocol.setter
    def Protocol(self, Protocol: str):
        self.__Protocol = Protocol


    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value


    @property
    def Referrals(self):
        return self.__Referrals

    @Referrals.setter
    def Referrals(self, Referrals: str):
        self.__Referrals = Referrals


    @property
    def LimitValue(self):
        return self.__LimitValue

    @LimitValue.setter
    def LimitValue(self, LimitValue: int):
        self.__LimitValue = LimitValue


    @property
    def Host(self):
        return self.__Host

    @Host.setter
    def Host(self, Host: str):
        self.__Host = Host


    @property
    def EncryptionMethodName(self):
        return self.__EncryptionMethodName

    @EncryptionMethodName.setter
    def EncryptionMethodName(self, EncryptionMethodName: str):
        self.__EncryptionMethodName = EncryptionMethodName


    @property
    def Separator(self):
        return self.__Separator

    @Separator.setter
    def Separator(self, Separator: str):
        self.__Separator = Separator


    @property
    def Filter(self):
        return self.__Filter

    @Filter.setter
    def Filter(self, Filter: str):
        self.__Filter = Filter


    @property
    def UseLimit(self):
        return self.__UseLimit

    @UseLimit.setter
    def UseLimit(self, UseLimit: bool):
        self.__UseLimit = UseLimit


    @property
    def StorePath(self):
        return self.__StorePath

    @StorePath.setter
    def StorePath(self, StorePath: str):
        self.__StorePath = StorePath


    @property
    def Aliases(self):
        return self.__Aliases

    @Aliases.setter
    def Aliases(self, Aliases: str):
        self.__Aliases = Aliases


    @property
    def SelectedDN(self):
        return self.__SelectedDN

    @SelectedDN.setter
    def SelectedDN(self, SelectedDN: str):
        self.__SelectedDN = SelectedDN


    @property
    def UseAdvanced(self):
        return self.__UseAdvanced

    @UseAdvanced.setter
    def UseAdvanced(self, UseAdvanced: bool):
        self.__UseAdvanced = UseAdvanced


    @property
    def CountLimit(self):
        return self.__CountLimit

    @CountLimit.setter
    def CountLimit(self, CountLimit: str):
        self.__CountLimit = CountLimit


    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, Port: str):
        self.__Port = Port


    @property
    def BindPassword(self):
        return self.__BindPassword

    @BindPassword.setter
    def BindPassword(self, BindPassword: str):
        self.__BindPassword = BindPassword


    @property
    def SavePassword(self):
        return self.__SavePassword

    @SavePassword.setter
    def SavePassword(self, SavePassword: bool):
        self.__SavePassword = SavePassword


    @property
    def BaseDNs(self):
        return self.__BaseDNs

    @BaseDNs.setter
    def BaseDNs(self, BaseDNs: str):
        self.__BaseDNs = BaseDNs


    @property
    def ReturnAttributes(self):
        return self.__ReturnAttributes

    @ReturnAttributes.setter
    def ReturnAttributes(self, ReturnAttributes: str):
        self.__ReturnAttributes = ReturnAttributes


    @property
    def UseAuthen(self):
        return self.__UseAuthen

    @UseAuthen.setter
    def UseAuthen(self, UseAuthen: bool):
        self.__UseAuthen = UseAuthen


    @property
    def GetBaseDNsFromRoot(self):
        return self.__GetBaseDNsFromRoot

    @GetBaseDNsFromRoot.setter
    def GetBaseDNsFromRoot(self, GetBaseDNsFromRoot: bool):
        self.__GetBaseDNsFromRoot = GetBaseDNsFromRoot


    @property
    def TimeOutLimit(self):
        return self.__TimeOutLimit

    @TimeOutLimit.setter
    def TimeOutLimit(self, TimeOutLimit: str):
        self.__TimeOutLimit = TimeOutLimit


    @property
    def BindPrincipal(self):
        return self.__BindPrincipal

    @BindPrincipal.setter
    def BindPrincipal(self, BindPrincipal: str):
        self.__BindPrincipal = BindPrincipal


class connection_ValidationRulesConnection(Connection):

    def __init__(self, isSelect: bool, isInsert: bool, isUpdate: bool, isDelete: bool, type: str, baseSchema: str, baseColumnNames: str, refSchema: str, refColumnNames: str, javaCondition: str, sqlCondition: str, logicalOperator: str, isDisallow: bool, isRejectLink: bool, connection_ValidationRulesConnection: set["connection_ConditionType"] = None, connection_ValidationRulesConnection114: set["connection_InnerJoinMap"] = None):
        self.isSelect = isSelect
        self.isInsert = isInsert
        self.isUpdate = isUpdate
        self.isDelete = isDelete
        self.type = type
        self.baseSchema = baseSchema
        self.baseColumnNames = baseColumnNames
        self.refSchema = refSchema
        self.refColumnNames = refColumnNames
        self.javaCondition = javaCondition
        self.sqlCondition = sqlCondition
        self.logicalOperator = logicalOperator
        self.isDisallow = isDisallow
        self.isRejectLink = isRejectLink
        self.connection_ValidationRulesConnection = connection_ValidationRulesConnection if connection_ValidationRulesConnection is not None else set()
        self.connection_ValidationRulesConnection114 = connection_ValidationRulesConnection114 if connection_ValidationRulesConnection114 is not None else set()
        
        pass
    @property
    def logicalOperator(self):
        return self.__logicalOperator

    @logicalOperator.setter
    def logicalOperator(self, logicalOperator: str):
        self.__logicalOperator = logicalOperator


    @property
    def refSchema(self):
        return self.__refSchema

    @refSchema.setter
    def refSchema(self, refSchema: str):
        self.__refSchema = refSchema


    @property
    def isDelete(self):
        return self.__isDelete

    @isDelete.setter
    def isDelete(self, isDelete: bool):
        self.__isDelete = isDelete


    @property
    def baseColumnNames(self):
        return self.__baseColumnNames

    @baseColumnNames.setter
    def baseColumnNames(self, baseColumnNames: str):
        self.__baseColumnNames = baseColumnNames


    @property
    def refColumnNames(self):
        return self.__refColumnNames

    @refColumnNames.setter
    def refColumnNames(self, refColumnNames: str):
        self.__refColumnNames = refColumnNames


    @property
    def isInsert(self):
        return self.__isInsert

    @isInsert.setter
    def isInsert(self, isInsert: bool):
        self.__isInsert = isInsert


    @property
    def baseSchema(self):
        return self.__baseSchema

    @baseSchema.setter
    def baseSchema(self, baseSchema: str):
        self.__baseSchema = baseSchema


    @property
    def javaCondition(self):
        return self.__javaCondition

    @javaCondition.setter
    def javaCondition(self, javaCondition: str):
        self.__javaCondition = javaCondition


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def isUpdate(self):
        return self.__isUpdate

    @isUpdate.setter
    def isUpdate(self, isUpdate: bool):
        self.__isUpdate = isUpdate


    @property
    def isRejectLink(self):
        return self.__isRejectLink

    @isRejectLink.setter
    def isRejectLink(self, isRejectLink: bool):
        self.__isRejectLink = isRejectLink


    @property
    def isDisallow(self):
        return self.__isDisallow

    @isDisallow.setter
    def isDisallow(self, isDisallow: bool):
        self.__isDisallow = isDisallow


    @property
    def isSelect(self):
        return self.__isSelect

    @isSelect.setter
    def isSelect(self, isSelect: bool):
        self.__isSelect = isSelect


    @property
    def sqlCondition(self):
        return self.__sqlCondition

    @sqlCondition.setter
    def sqlCondition(self, sqlCondition: str):
        self.__sqlCondition = sqlCondition


    @property
    def connection_ValidationRulesConnection114(self):
        return self.__connection_ValidationRulesConnection114

    @connection_ValidationRulesConnection114.setter
    def connection_ValidationRulesConnection114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_ValidationRulesConnection__connection_ValidationRulesConnection114", None)
        self.__connection_ValidationRulesConnection114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_InnerJoinMap"):
                    opp_val = getattr(item, "connection_InnerJoinMap", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_InnerJoinMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_InnerJoinMap"):
                    opp_val = getattr(item, "connection_InnerJoinMap", None)
                    
                    setattr(item, "connection_InnerJoinMap", self)
                    

    @property
    def connection_ValidationRulesConnection(self):
        return self.__connection_ValidationRulesConnection

    @connection_ValidationRulesConnection.setter
    def connection_ValidationRulesConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_ValidationRulesConnection__connection_ValidationRulesConnection", None)
        self.__connection_ValidationRulesConnection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_ConditionType"):
                    opp_val = getattr(item, "connection_ConditionType", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_ConditionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_ConditionType"):
                    opp_val = getattr(item, "connection_ConditionType", None)
                    
                    setattr(item, "connection_ConditionType", self)
                    

class connection_FileConnection(Connection):

    def __init__(self, FirstLineCaption: bool, RemoveEmptyRow: bool, EscapeType: str, EscapeChar: str, TextEnclosure: str, CsvOption: bool, Server: str, FilePath: str, Format: str, Encoding: str, FieldSeparatorValue: str, RowSeparatorType: str, RowSeparatorValue: str, TextIdentifier: str, UseHeader: bool, HeaderValue: str, UseFooter: bool, FooterValue: str, UseLimit: bool, LimitValue: str):
        self.FirstLineCaption = FirstLineCaption
        self.RemoveEmptyRow = RemoveEmptyRow
        self.EscapeType = EscapeType
        self.EscapeChar = EscapeChar
        self.TextEnclosure = TextEnclosure
        self.CsvOption = CsvOption
        self.Server = Server
        self.FilePath = FilePath
        self.Format = Format
        self.Encoding = Encoding
        self.FieldSeparatorValue = FieldSeparatorValue
        self.RowSeparatorType = RowSeparatorType
        self.RowSeparatorValue = RowSeparatorValue
        self.TextIdentifier = TextIdentifier
        self.UseHeader = UseHeader
        self.HeaderValue = HeaderValue
        self.UseFooter = UseFooter
        self.FooterValue = FooterValue
        self.UseLimit = UseLimit
        self.LimitValue = LimitValue
        
        pass
    @property
    def FooterValue(self):
        return self.__FooterValue

    @FooterValue.setter
    def FooterValue(self, FooterValue: str):
        self.__FooterValue = FooterValue


    @property
    def UseLimit(self):
        return self.__UseLimit

    @UseLimit.setter
    def UseLimit(self, UseLimit: bool):
        self.__UseLimit = UseLimit


    @property
    def HeaderValue(self):
        return self.__HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue: str):
        self.__HeaderValue = HeaderValue


    @property
    def FieldSeparatorValue(self):
        return self.__FieldSeparatorValue

    @FieldSeparatorValue.setter
    def FieldSeparatorValue(self, FieldSeparatorValue: str):
        self.__FieldSeparatorValue = FieldSeparatorValue


    @property
    def EscapeChar(self):
        return self.__EscapeChar

    @EscapeChar.setter
    def EscapeChar(self, EscapeChar: str):
        self.__EscapeChar = EscapeChar


    @property
    def TextEnclosure(self):
        return self.__TextEnclosure

    @TextEnclosure.setter
    def TextEnclosure(self, TextEnclosure: str):
        self.__TextEnclosure = TextEnclosure


    @property
    def UseFooter(self):
        return self.__UseFooter

    @UseFooter.setter
    def UseFooter(self, UseFooter: bool):
        self.__UseFooter = UseFooter


    @property
    def LimitValue(self):
        return self.__LimitValue

    @LimitValue.setter
    def LimitValue(self, LimitValue: str):
        self.__LimitValue = LimitValue


    @property
    def UseHeader(self):
        return self.__UseHeader

    @UseHeader.setter
    def UseHeader(self, UseHeader: bool):
        self.__UseHeader = UseHeader


    @property
    def FilePath(self):
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath


    @property
    def Encoding(self):
        return self.__Encoding

    @Encoding.setter
    def Encoding(self, Encoding: str):
        self.__Encoding = Encoding


    @property
    def RowSeparatorType(self):
        return self.__RowSeparatorType

    @RowSeparatorType.setter
    def RowSeparatorType(self, RowSeparatorType: str):
        self.__RowSeparatorType = RowSeparatorType


    @property
    def CsvOption(self):
        return self.__CsvOption

    @CsvOption.setter
    def CsvOption(self, CsvOption: bool):
        self.__CsvOption = CsvOption


    @property
    def EscapeType(self):
        return self.__EscapeType

    @EscapeType.setter
    def EscapeType(self, EscapeType: str):
        self.__EscapeType = EscapeType


    @property
    def Format(self):
        return self.__Format

    @Format.setter
    def Format(self, Format: str):
        self.__Format = Format


    @property
    def Server(self):
        return self.__Server

    @Server.setter
    def Server(self, Server: str):
        self.__Server = Server


    @property
    def RowSeparatorValue(self):
        return self.__RowSeparatorValue

    @RowSeparatorValue.setter
    def RowSeparatorValue(self, RowSeparatorValue: str):
        self.__RowSeparatorValue = RowSeparatorValue


    @property
    def TextIdentifier(self):
        return self.__TextIdentifier

    @TextIdentifier.setter
    def TextIdentifier(self, TextIdentifier: str):
        self.__TextIdentifier = TextIdentifier


    @property
    def RemoveEmptyRow(self):
        return self.__RemoveEmptyRow

    @RemoveEmptyRow.setter
    def RemoveEmptyRow(self, RemoveEmptyRow: bool):
        self.__RemoveEmptyRow = RemoveEmptyRow


    @property
    def FirstLineCaption(self):
        return self.__FirstLineCaption

    @FirstLineCaption.setter
    def FirstLineCaption(self, FirstLineCaption: bool):
        self.__FirstLineCaption = FirstLineCaption


class connection_AdditionalProperties:

    def __init__(self, key: str, value: str, connection_AdditionalProperties15: "connection_DatabaseConnection" = None, connection_AdditionalProperties: "connection_MetadataTable" = None):
        self.key = key
        self.value = value
        self.connection_AdditionalProperties15 = connection_AdditionalProperties15
        self.connection_AdditionalProperties = connection_AdditionalProperties
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def connection_AdditionalProperties(self):
        return self.__connection_AdditionalProperties

    @connection_AdditionalProperties.setter
    def connection_AdditionalProperties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_AdditionalProperties__connection_AdditionalProperties", None)
        self.__connection_AdditionalProperties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_MetadataTable10"):
                opp_val = getattr(old_value, "connection_MetadataTable10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_MetadataTable10"):
                opp_val = getattr(value, "connection_MetadataTable10", None)
                if opp_val is None:
                    setattr(value, "connection_MetadataTable10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_AdditionalProperties15(self):
        return self.__connection_AdditionalProperties15

    @connection_AdditionalProperties15.setter
    def connection_AdditionalProperties15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_AdditionalProperties__connection_AdditionalProperties15", None)
        self.__connection_AdditionalProperties15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_DatabaseConnection"):
                opp_val = getattr(old_value, "connection_DatabaseConnection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_DatabaseConnection"):
                opp_val = getattr(value, "connection_DatabaseConnection", None)
                if opp_val is None:
                    setattr(value, "connection_DatabaseConnection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class FileConnection:

    pass
class connection_RegexpFileConnection(FileConnection):

    def __init__(self, FieldSeparatorType: str):
        self.FieldSeparatorType = FieldSeparatorType
        
        pass
    @property
    def FieldSeparatorType(self):
        return self.__FieldSeparatorType

    @FieldSeparatorType.setter
    def FieldSeparatorType(self, FieldSeparatorType: str):
        self.__FieldSeparatorType = FieldSeparatorType


class connection_EbcdicConnection(FileConnection):

    def __init__(self, MidFile: str, DataFile: str, CodePage: str, SourceFileStart: str, SourceFileEnd: str):
        self.MidFile = MidFile
        self.DataFile = DataFile
        self.CodePage = CodePage
        self.SourceFileStart = SourceFileStart
        self.SourceFileEnd = SourceFileEnd
        
        pass
    @property
    def DataFile(self):
        return self.__DataFile

    @DataFile.setter
    def DataFile(self, DataFile: str):
        self.__DataFile = DataFile


    @property
    def SourceFileEnd(self):
        return self.__SourceFileEnd

    @SourceFileEnd.setter
    def SourceFileEnd(self, SourceFileEnd: str):
        self.__SourceFileEnd = SourceFileEnd


    @property
    def CodePage(self):
        return self.__CodePage

    @CodePage.setter
    def CodePage(self, CodePage: str):
        self.__CodePage = CodePage


    @property
    def SourceFileStart(self):
        return self.__SourceFileStart

    @SourceFileStart.setter
    def SourceFileStart(self, SourceFileStart: str):
        self.__SourceFileStart = SourceFileStart


    @property
    def MidFile(self):
        return self.__MidFile

    @MidFile.setter
    def MidFile(self, MidFile: str):
        self.__MidFile = MidFile


class connection_HL7Connection(FileConnection):

    def __init__(self, StartChar: str, EndChar: str, outputFilePath: str, connection_HL7Connection: set["connection_HL7FileNode"] = None):
        self.StartChar = StartChar
        self.EndChar = EndChar
        self.outputFilePath = outputFilePath
        self.connection_HL7Connection = connection_HL7Connection if connection_HL7Connection is not None else set()
        
        pass
    @property
    def EndChar(self):
        return self.__EndChar

    @EndChar.setter
    def EndChar(self, EndChar: str):
        self.__EndChar = EndChar


    @property
    def outputFilePath(self):
        return self.__outputFilePath

    @outputFilePath.setter
    def outputFilePath(self, outputFilePath: str):
        self.__outputFilePath = outputFilePath


    @property
    def StartChar(self):
        return self.__StartChar

    @StartChar.setter
    def StartChar(self, StartChar: str):
        self.__StartChar = StartChar


    @property
    def connection_HL7Connection(self):
        return self.__connection_HL7Connection

    @connection_HL7Connection.setter
    def connection_HL7Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_HL7Connection__connection_HL7Connection", None)
        self.__connection_HL7Connection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_HL7FileNode"):
                    opp_val = getattr(item, "connection_HL7FileNode", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_HL7FileNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_HL7FileNode"):
                    opp_val = getattr(item, "connection_HL7FileNode", None)
                    
                    setattr(item, "connection_HL7FileNode", self)
                    

class connection_FileExcelConnection(FileConnection):

    def __init__(self, SheetName: str, sheetColumns: str, firstColumn: str, lastColumn: str, thousandSeparator: str, decimalSeparator: str, advancedSpearator: bool, selectAllSheets: bool, sheetList: str, generationMode: str):
        self.SheetName = SheetName
        self.sheetColumns = sheetColumns
        self.firstColumn = firstColumn
        self.lastColumn = lastColumn
        self.thousandSeparator = thousandSeparator
        self.decimalSeparator = decimalSeparator
        self.advancedSpearator = advancedSpearator
        self.selectAllSheets = selectAllSheets
        self.sheetList = sheetList
        self.generationMode = generationMode
        
        pass
    @property
    def advancedSpearator(self):
        return self.__advancedSpearator

    @advancedSpearator.setter
    def advancedSpearator(self, advancedSpearator: bool):
        self.__advancedSpearator = advancedSpearator


    @property
    def decimalSeparator(self):
        return self.__decimalSeparator

    @decimalSeparator.setter
    def decimalSeparator(self, decimalSeparator: str):
        self.__decimalSeparator = decimalSeparator


    @property
    def sheetList(self):
        return self.__sheetList

    @sheetList.setter
    def sheetList(self, sheetList: str):
        self.__sheetList = sheetList


    @property
    def firstColumn(self):
        return self.__firstColumn

    @firstColumn.setter
    def firstColumn(self, firstColumn: str):
        self.__firstColumn = firstColumn


    @property
    def generationMode(self):
        return self.__generationMode

    @generationMode.setter
    def generationMode(self, generationMode: str):
        self.__generationMode = generationMode


    @property
    def selectAllSheets(self):
        return self.__selectAllSheets

    @selectAllSheets.setter
    def selectAllSheets(self, selectAllSheets: bool):
        self.__selectAllSheets = selectAllSheets


    @property
    def SheetName(self):
        return self.__SheetName

    @SheetName.setter
    def SheetName(self, SheetName: str):
        self.__SheetName = SheetName


    @property
    def thousandSeparator(self):
        return self.__thousandSeparator

    @thousandSeparator.setter
    def thousandSeparator(self, thousandSeparator: str):
        self.__thousandSeparator = thousandSeparator


    @property
    def lastColumn(self):
        return self.__lastColumn

    @lastColumn.setter
    def lastColumn(self, lastColumn: str):
        self.__lastColumn = lastColumn


    @property
    def sheetColumns(self):
        return self.__sheetColumns

    @sheetColumns.setter
    def sheetColumns(self, sheetColumns: str):
        self.__sheetColumns = sheetColumns


class connection_PositionalFileConnection(FileConnection):

    pass
class connection_DelimitedFileConnection(FileConnection):

    def __init__(self, FieldSeparatorType: str, splitRecord: bool):
        self.FieldSeparatorType = FieldSeparatorType
        self.splitRecord = splitRecord
        
        pass
    @property
    def splitRecord(self):
        return self.__splitRecord

    @splitRecord.setter
    def splitRecord(self, splitRecord: bool):
        self.__splitRecord = splitRecord


    @property
    def FieldSeparatorType(self):
        return self.__FieldSeparatorType

    @FieldSeparatorType.setter
    def FieldSeparatorType(self, FieldSeparatorType: str):
        self.__FieldSeparatorType = FieldSeparatorType


class ModelElement:

    pass
class connection_AbstractMetadataObject(ModelElement):

    def __init__(self, divergency: bool, properties: str, id: str, comment: str, label: str, readOnly: bool, synchronised: bool):
        self.divergency = divergency
        self.properties = properties
        self.id = id
        self.comment = comment
        self.label = label
        self.readOnly = readOnly
        self.synchronised = synchronised
        
        pass
    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def synchronised(self):
        return self.__synchronised

    @synchronised.setter
    def synchronised(self, synchronised: bool):
        self.__synchronised = synchronised


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties


    @property
    def divergency(self):
        return self.__divergency

    @divergency.setter
    def divergency(self, divergency: bool):
        self.__divergency = divergency


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


class core_Class:

    pass
class record_Field:

    pass
class connection_QueriesConnection:

    pass
class softwaredeployment_DataProvider:

    pass
class AbstractMetadataObject:

    pass
class connection_MetadataColumn(record_Field, AbstractMetadataObject):

    def __init__(self, defaultValue: str, talendType: str, key: bool, nullable: bool, sourceType: str, originalField: str, pattern: str, displayField: str, originalLength: str, relatedEntity: str, relationshipType: str, connection_MetadataColumn: "connection_MetadataTable" = None, connection_MetadataColumn5: "connection_MetadataTable" = None):
        self.defaultValue = defaultValue
        self.talendType = talendType
        self.key = key
        self.nullable = nullable
        self.sourceType = sourceType
        self.originalField = originalField
        self.pattern = pattern
        self.displayField = displayField
        self.originalLength = originalLength
        self.relatedEntity = relatedEntity
        self.relationshipType = relationshipType
        self.connection_MetadataColumn = connection_MetadataColumn
        self.connection_MetadataColumn5 = connection_MetadataColumn5
        
        pass
    @property
    def sourceType(self):
        return self.__sourceType

    @sourceType.setter
    def sourceType(self, sourceType: str):
        self.__sourceType = sourceType


    @property
    def originalField(self):
        return self.__originalField

    @originalField.setter
    def originalField(self, originalField: str):
        self.__originalField = originalField


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


    @property
    def displayField(self):
        return self.__displayField

    @displayField.setter
    def displayField(self, displayField: str):
        self.__displayField = displayField


    @property
    def talendType(self):
        return self.__talendType

    @talendType.setter
    def talendType(self, talendType: str):
        self.__talendType = talendType


    @property
    def originalLength(self):
        return self.__originalLength

    @originalLength.setter
    def originalLength(self, originalLength: str):
        self.__originalLength = originalLength


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: bool):
        self.__key = key


    @property
    def relationshipType(self):
        return self.__relationshipType

    @relationshipType.setter
    def relationshipType(self, relationshipType: str):
        self.__relationshipType = relationshipType


    @property
    def relatedEntity(self):
        return self.__relatedEntity

    @relatedEntity.setter
    def relatedEntity(self, relatedEntity: str):
        self.__relatedEntity = relatedEntity


    @property
    def connection_MetadataColumn(self):
        return self.__connection_MetadataColumn

    @connection_MetadataColumn.setter
    def connection_MetadataColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataColumn__connection_MetadataColumn", None)
        self.__connection_MetadataColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_MetadataTable"):
                opp_val = getattr(old_value, "connection_MetadataTable", None)
                if opp_val == self:
                    setattr(old_value, "connection_MetadataTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_MetadataTable"):
                opp_val = getattr(value, "connection_MetadataTable", None)
                setattr(value, "connection_MetadataTable", self)

    @property
    def connection_MetadataColumn5(self):
        return self.__connection_MetadataColumn5

    @connection_MetadataColumn5.setter
    def connection_MetadataColumn5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataColumn__connection_MetadataColumn5", None)
        self.__connection_MetadataColumn5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_MetadataTable4"):
                opp_val = getattr(old_value, "connection_MetadataTable4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_MetadataTable4"):
                opp_val = getattr(value, "connection_MetadataTable4", None)
                if opp_val is None:
                    setattr(value, "connection_MetadataTable4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_CDCType(AbstractMetadataObject):

    def __init__(self, linkDB: str, journalName: str, connection_CDCType: "connection_CDCConnection" = None, connection_CDCType85: set["connection_SubscriberTable"] = None, connection_CDCType87: "connection_CDCConnection" = None):
        self.linkDB = linkDB
        self.journalName = journalName
        self.connection_CDCType = connection_CDCType
        self.connection_CDCType85 = connection_CDCType85 if connection_CDCType85 is not None else set()
        self.connection_CDCType87 = connection_CDCType87
        
        pass
    @property
    def linkDB(self):
        return self.__linkDB

    @linkDB.setter
    def linkDB(self, linkDB: str):
        self.__linkDB = linkDB


    @property
    def journalName(self):
        return self.__journalName

    @journalName.setter
    def journalName(self, journalName: str):
        self.__journalName = journalName


    @property
    def connection_CDCType85(self):
        return self.__connection_CDCType85

    @connection_CDCType85.setter
    def connection_CDCType85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_CDCType__connection_CDCType85", None)
        self.__connection_CDCType85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_SubscriberTable"):
                    opp_val = getattr(item, "connection_SubscriberTable", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_SubscriberTable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_SubscriberTable"):
                    opp_val = getattr(item, "connection_SubscriberTable", None)
                    
                    setattr(item, "connection_SubscriberTable", self)
                    

    @property
    def connection_CDCType(self):
        return self.__connection_CDCType

    @connection_CDCType.setter
    def connection_CDCType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_CDCType__connection_CDCType", None)
        self.__connection_CDCType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_CDCConnection"):
                opp_val = getattr(old_value, "connection_CDCConnection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_CDCConnection"):
                opp_val = getattr(value, "connection_CDCConnection", None)
                if opp_val is None:
                    setattr(value, "connection_CDCConnection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_CDCType87(self):
        return self.__connection_CDCType87

    @connection_CDCType87.setter
    def connection_CDCType87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_CDCType__connection_CDCType87", None)
        self.__connection_CDCType87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_CDCConnection88"):
                opp_val = getattr(old_value, "connection_CDCConnection88", None)
                if opp_val == self:
                    setattr(old_value, "connection_CDCConnection88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_CDCConnection88"):
                opp_val = getattr(value, "connection_CDCConnection88", None)
                setattr(value, "connection_CDCConnection88", self)

class connection_SAPFunctionParameterColumn(AbstractMetadataObject):

    def __init__(self, ParameterType: str, StructureOrTableName: str, DataType: str, Length: str, Value: str, columns: "connection_SAPFunctionParameterTable" = None, SAPFunctionParameterColumn: "connection_SAPFunctionParameterTable" = None):
        self.ParameterType = ParameterType
        self.StructureOrTableName = StructureOrTableName
        self.DataType = DataType
        self.Length = Length
        self.Value = Value
        self.columns = columns
        self.SAPFunctionParameterColumn = SAPFunctionParameterColumn
        
        pass
    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value


    @property
    def DataType(self):
        return self.__DataType

    @DataType.setter
    def DataType(self, DataType: str):
        self.__DataType = DataType


    @property
    def Length(self):
        return self.__Length

    @Length.setter
    def Length(self, Length: str):
        self.__Length = Length


    @property
    def ParameterType(self):
        return self.__ParameterType

    @ParameterType.setter
    def ParameterType(self, ParameterType: str):
        self.__ParameterType = ParameterType


    @property
    def StructureOrTableName(self):
        return self.__StructureOrTableName

    @StructureOrTableName.setter
    def StructureOrTableName(self, StructureOrTableName: str):
        self.__StructureOrTableName = StructureOrTableName


    @property
    def columns(self):
        return self.__columns

    @columns.setter
    def columns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionParameterColumn__columns", None)
        self.__columns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAPFunctionParameterTable"):
                opp_val = getattr(old_value, "SAPFunctionParameterTable", None)
                if opp_val == self:
                    setattr(old_value, "SAPFunctionParameterTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAPFunctionParameterTable"):
                opp_val = getattr(value, "SAPFunctionParameterTable", None)
                setattr(value, "SAPFunctionParameterTable", self)

    @property
    def SAPFunctionParameterColumn(self):
        return self.__SAPFunctionParameterColumn

    @SAPFunctionParameterColumn.setter
    def SAPFunctionParameterColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionParameterColumn__SAPFunctionParameterColumn", None)
        self.__SAPFunctionParameterColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ParameterTable"):
                opp_val = getattr(old_value, "ParameterTable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ParameterTable"):
                opp_val = getattr(value, "ParameterTable", None)
                if opp_val is None:
                    setattr(value, "ParameterTable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def setDescription(self, connection_description):
        # TODO: Implement setDescription method
        pass

class connection_Query(AbstractMetadataObject):

    def __init__(self, value: str, contextMode: bool, Query: "connection_QueriesConnection" = None, query: "connection_QueriesConnection" = None):
        self.value = value
        self.contextMode = contextMode
        self.Query = Query
        self.query = query
        
        pass
    @property
    def contextMode(self):
        return self.__contextMode

    @contextMode.setter
    def contextMode(self, contextMode: bool):
        self.__contextMode = contextMode


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Query__query", None)
        self.__query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueriesConnection72"):
                opp_val = getattr(old_value, "QueriesConnection72", None)
                if opp_val == self:
                    setattr(old_value, "QueriesConnection72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueriesConnection72"):
                opp_val = getattr(value, "QueriesConnection72", None)
                setattr(value, "QueriesConnection72", self)

    @property
    def Query(self):
        return self.__Query

    @Query.setter
    def Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Query__Query", None)
        self.__Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queries70"):
                opp_val = getattr(old_value, "queries70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queries70"):
                opp_val = getattr(value, "queries70", None)
                if opp_val is None:
                    setattr(value, "queries70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_SAPFunctionParameterTable(AbstractMetadataObject):

    pass
class connection_MetadataTable(core_Class, AbstractMetadataObject):

    def __init__(self, sourceName: str, tableType: str, attachedCDC: bool, activatedCDC: bool, connection_MetadataTable37: "connection_SAPFunctionUnit" = None, connection_MetadataTable43: "connection_SAPFunctionUnit" = None, connection_MetadataTable46: "connection_SAPFunctionUnit" = None, connection_MetadataTable: "connection_MetadataColumn" = None, connection_MetadataTable4: set["connection_MetadataColumn"] = None, connection_MetadataTable7: "connection_Connection" = None, connection_MetadataTable10: set["connection_AdditionalProperties"] = None, connection_MetadataTable116: "connection_SalesforceModuleUnit" = None, connection_MetadataTable120: "connection_SalesforceModuleUnit" = None):
        self.sourceName = sourceName
        self.tableType = tableType
        self.attachedCDC = attachedCDC
        self.activatedCDC = activatedCDC
        self.connection_MetadataTable37 = connection_MetadataTable37
        self.connection_MetadataTable43 = connection_MetadataTable43
        self.connection_MetadataTable46 = connection_MetadataTable46
        self.connection_MetadataTable = connection_MetadataTable
        self.connection_MetadataTable4 = connection_MetadataTable4 if connection_MetadataTable4 is not None else set()
        self.connection_MetadataTable7 = connection_MetadataTable7
        self.connection_MetadataTable10 = connection_MetadataTable10 if connection_MetadataTable10 is not None else set()
        self.connection_MetadataTable116 = connection_MetadataTable116
        self.connection_MetadataTable120 = connection_MetadataTable120
        
        pass
    @property
    def attachedCDC(self):
        return self.__attachedCDC

    @attachedCDC.setter
    def attachedCDC(self, attachedCDC: bool):
        self.__attachedCDC = attachedCDC


    @property
    def activatedCDC(self):
        return self.__activatedCDC

    @activatedCDC.setter
    def activatedCDC(self, activatedCDC: bool):
        self.__activatedCDC = activatedCDC


    @property
    def tableType(self):
        return self.__tableType

    @tableType.setter
    def tableType(self, tableType: str):
        self.__tableType = tableType


    @property
    def sourceName(self):
        return self.__sourceName

    @sourceName.setter
    def sourceName(self, sourceName: str):
        self.__sourceName = sourceName


    @property
    def connection_MetadataTable120(self):
        return self.__connection_MetadataTable120

    @connection_MetadataTable120.setter
    def connection_MetadataTable120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable120", None)
        self.__connection_MetadataTable120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SalesforceModuleUnit119"):
                opp_val = getattr(old_value, "connection_SalesforceModuleUnit119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SalesforceModuleUnit119"):
                opp_val = getattr(value, "connection_SalesforceModuleUnit119", None)
                if opp_val is None:
                    setattr(value, "connection_SalesforceModuleUnit119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_MetadataTable43(self):
        return self.__connection_MetadataTable43

    @connection_MetadataTable43.setter
    def connection_MetadataTable43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable43", None)
        self.__connection_MetadataTable43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionUnit42"):
                opp_val = getattr(old_value, "connection_SAPFunctionUnit42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionUnit42"):
                opp_val = getattr(value, "connection_SAPFunctionUnit42", None)
                if opp_val is None:
                    setattr(value, "connection_SAPFunctionUnit42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_MetadataTable(self):
        return self.__connection_MetadataTable

    @connection_MetadataTable.setter
    def connection_MetadataTable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable", None)
        self.__connection_MetadataTable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_MetadataColumn"):
                opp_val = getattr(old_value, "connection_MetadataColumn", None)
                if opp_val == self:
                    setattr(old_value, "connection_MetadataColumn", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_MetadataColumn"):
                opp_val = getattr(value, "connection_MetadataColumn", None)
                setattr(value, "connection_MetadataColumn", self)

    @property
    def connection_MetadataTable10(self):
        return self.__connection_MetadataTable10

    @connection_MetadataTable10.setter
    def connection_MetadataTable10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable10", None)
        self.__connection_MetadataTable10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_AdditionalProperties"):
                    opp_val = getattr(item, "connection_AdditionalProperties", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_AdditionalProperties", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_AdditionalProperties"):
                    opp_val = getattr(item, "connection_AdditionalProperties", None)
                    
                    setattr(item, "connection_AdditionalProperties", self)
                    

    @property
    def connection_MetadataTable116(self):
        return self.__connection_MetadataTable116

    @connection_MetadataTable116.setter
    def connection_MetadataTable116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable116", None)
        self.__connection_MetadataTable116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SalesforceModuleUnit"):
                opp_val = getattr(old_value, "connection_SalesforceModuleUnit", None)
                if opp_val == self:
                    setattr(old_value, "connection_SalesforceModuleUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SalesforceModuleUnit"):
                opp_val = getattr(value, "connection_SalesforceModuleUnit", None)
                setattr(value, "connection_SalesforceModuleUnit", self)

    @property
    def connection_MetadataTable46(self):
        return self.__connection_MetadataTable46

    @connection_MetadataTable46.setter
    def connection_MetadataTable46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable46", None)
        self.__connection_MetadataTable46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionUnit45"):
                opp_val = getattr(old_value, "connection_SAPFunctionUnit45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionUnit45"):
                opp_val = getattr(value, "connection_SAPFunctionUnit45", None)
                if opp_val is None:
                    setattr(value, "connection_SAPFunctionUnit45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_MetadataTable37(self):
        return self.__connection_MetadataTable37

    @connection_MetadataTable37.setter
    def connection_MetadataTable37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable37", None)
        self.__connection_MetadataTable37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionUnit36"):
                opp_val = getattr(old_value, "connection_SAPFunctionUnit36", None)
                if opp_val == self:
                    setattr(old_value, "connection_SAPFunctionUnit36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionUnit36"):
                opp_val = getattr(value, "connection_SAPFunctionUnit36", None)
                setattr(value, "connection_SAPFunctionUnit36", self)

    @property
    def connection_MetadataTable7(self):
        return self.__connection_MetadataTable7

    @connection_MetadataTable7.setter
    def connection_MetadataTable7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable7", None)
        self.__connection_MetadataTable7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_Connection8"):
                opp_val = getattr(old_value, "connection_Connection8", None)
                if opp_val == self:
                    setattr(old_value, "connection_Connection8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_Connection8"):
                opp_val = getattr(value, "connection_Connection8", None)
                setattr(value, "connection_Connection8", self)

    @property
    def connection_MetadataTable4(self):
        return self.__connection_MetadataTable4

    @connection_MetadataTable4.setter
    def connection_MetadataTable4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable4", None)
        self.__connection_MetadataTable4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_MetadataColumn5"):
                    opp_val = getattr(item, "connection_MetadataColumn5", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_MetadataColumn5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_MetadataColumn5"):
                    opp_val = getattr(item, "connection_MetadataColumn5", None)
                    
                    setattr(item, "connection_MetadataColumn5", self)
                    

class connection_SAPIDocUnit(AbstractMetadataObject):

    def __init__(self, programId: str, gatewayService: str, useXmlOutput: bool, xmlFile: str, useHtmlOutput: bool, htmlFile: str, SAPIDocUnit: "connection_SAPConnection" = None, IDocs: "connection_SAPConnection" = None):
        self.programId = programId
        self.gatewayService = gatewayService
        self.useXmlOutput = useXmlOutput
        self.xmlFile = xmlFile
        self.useHtmlOutput = useHtmlOutput
        self.htmlFile = htmlFile
        self.SAPIDocUnit = SAPIDocUnit
        self.IDocs = IDocs
        
        pass
    @property
    def programId(self):
        return self.__programId

    @programId.setter
    def programId(self, programId: str):
        self.__programId = programId


    @property
    def gatewayService(self):
        return self.__gatewayService

    @gatewayService.setter
    def gatewayService(self, gatewayService: str):
        self.__gatewayService = gatewayService


    @property
    def useHtmlOutput(self):
        return self.__useHtmlOutput

    @useHtmlOutput.setter
    def useHtmlOutput(self, useHtmlOutput: bool):
        self.__useHtmlOutput = useHtmlOutput


    @property
    def htmlFile(self):
        return self.__htmlFile

    @htmlFile.setter
    def htmlFile(self, htmlFile: str):
        self.__htmlFile = htmlFile


    @property
    def xmlFile(self):
        return self.__xmlFile

    @xmlFile.setter
    def xmlFile(self, xmlFile: str):
        self.__xmlFile = xmlFile


    @property
    def useXmlOutput(self):
        return self.__useXmlOutput

    @useXmlOutput.setter
    def useXmlOutput(self, useXmlOutput: bool):
        self.__useXmlOutput = useXmlOutput


    @property
    def IDocs(self):
        return self.__IDocs

    @IDocs.setter
    def IDocs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPIDocUnit__IDocs", None)
        self.__IDocs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAPConnection"):
                opp_val = getattr(old_value, "SAPConnection", None)
                if opp_val == self:
                    setattr(old_value, "SAPConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAPConnection"):
                opp_val = getattr(value, "SAPConnection", None)
                setattr(value, "SAPConnection", self)

    @property
    def SAPIDocUnit(self):
        return self.__SAPIDocUnit

    @SAPIDocUnit.setter
    def SAPIDocUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPIDocUnit__SAPIDocUnit", None)
        self.__SAPIDocUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection18"):
                opp_val = getattr(old_value, "connection18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection18"):
                opp_val = getattr(value, "connection18", None)
                if opp_val is None:
                    setattr(value, "connection18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_SalesforceModuleUnit(AbstractMetadataObject):

    def __init__(self, moduleName: str, connection_SalesforceModuleUnit: "connection_MetadataTable" = None, modules: "connection_SalesforceSchemaConnection" = None, connection_SalesforceModuleUnit119: set["connection_MetadataTable"] = None, SalesforceModuleUnit: "connection_SalesforceSchemaConnection" = None):
        self.moduleName = moduleName
        self.connection_SalesforceModuleUnit = connection_SalesforceModuleUnit
        self.modules = modules
        self.connection_SalesforceModuleUnit119 = connection_SalesforceModuleUnit119 if connection_SalesforceModuleUnit119 is not None else set()
        self.SalesforceModuleUnit = SalesforceModuleUnit
        
        pass
    @property
    def moduleName(self):
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName


    @property
    def modules(self):
        return self.__modules

    @modules.setter
    def modules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SalesforceModuleUnit__modules", None)
        self.__modules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SalesforceSchemaConnection"):
                opp_val = getattr(old_value, "SalesforceSchemaConnection", None)
                if opp_val == self:
                    setattr(old_value, "SalesforceSchemaConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SalesforceSchemaConnection"):
                opp_val = getattr(value, "SalesforceSchemaConnection", None)
                setattr(value, "SalesforceSchemaConnection", self)

    @property
    def connection_SalesforceModuleUnit(self):
        return self.__connection_SalesforceModuleUnit

    @connection_SalesforceModuleUnit.setter
    def connection_SalesforceModuleUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SalesforceModuleUnit__connection_SalesforceModuleUnit", None)
        self.__connection_SalesforceModuleUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_MetadataTable116"):
                opp_val = getattr(old_value, "connection_MetadataTable116", None)
                if opp_val == self:
                    setattr(old_value, "connection_MetadataTable116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_MetadataTable116"):
                opp_val = getattr(value, "connection_MetadataTable116", None)
                setattr(value, "connection_MetadataTable116", self)

    @property
    def SalesforceModuleUnit(self):
        return self.__SalesforceModuleUnit

    @SalesforceModuleUnit.setter
    def SalesforceModuleUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SalesforceModuleUnit__SalesforceModuleUnit", None)
        self.__SalesforceModuleUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection81"):
                opp_val = getattr(old_value, "connection81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection81"):
                opp_val = getattr(value, "connection81", None)
                if opp_val is None:
                    setattr(value, "connection81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_SalesforceModuleUnit119(self):
        return self.__connection_SalesforceModuleUnit119

    @connection_SalesforceModuleUnit119.setter
    def connection_SalesforceModuleUnit119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SalesforceModuleUnit__connection_SalesforceModuleUnit119", None)
        self.__connection_SalesforceModuleUnit119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_MetadataTable120"):
                    opp_val = getattr(item, "connection_MetadataTable120", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_MetadataTable120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_MetadataTable120"):
                    opp_val = getattr(item, "connection_MetadataTable120", None)
                    
                    setattr(item, "connection_MetadataTable120", self)
                    

class connection_Connection(softwaredeployment_DataProvider, AbstractMetadataObject):

    def __init__(self, version: str, ContextMode: bool, ContextId: str, contextName: str, connection_Connection: "connection_Metadata" = None, connection: "connection_QueriesConnection" = None, connection_Connection8: "connection_MetadataTable" = None, Connection: "connection_QueriesConnection" = None):
        self.version = version
        self.ContextMode = ContextMode
        self.ContextId = ContextId
        self.contextName = contextName
        self.connection_Connection = connection_Connection
        self.connection = connection
        self.connection_Connection8 = connection_Connection8
        self.Connection = Connection
        
        pass
    @property
    def ContextId(self):
        return self.__ContextId

    @ContextId.setter
    def ContextId(self, ContextId: str):
        self.__ContextId = ContextId


    @property
    def contextName(self):
        return self.__contextName

    @contextName.setter
    def contextName(self, contextName: str):
        self.__contextName = contextName


    @property
    def ContextMode(self):
        return self.__ContextMode

    @ContextMode.setter
    def ContextMode(self, ContextMode: bool):
        self.__ContextMode = ContextMode


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def connection_Connection(self):
        return self.__connection_Connection

    @connection_Connection.setter
    def connection_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Connection__connection_Connection", None)
        self.__connection_Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_Metadata"):
                opp_val = getattr(old_value, "connection_Metadata", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_Metadata"):
                opp_val = getattr(value, "connection_Metadata", None)
                if opp_val is None:
                    setattr(value, "connection_Metadata", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_Connection8(self):
        return self.__connection_Connection8

    @connection_Connection8.setter
    def connection_Connection8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Connection__connection_Connection8", None)
        self.__connection_Connection8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_MetadataTable7"):
                opp_val = getattr(old_value, "connection_MetadataTable7", None)
                if opp_val == self:
                    setattr(old_value, "connection_MetadataTable7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_MetadataTable7"):
                opp_val = getattr(value, "connection_MetadataTable7", None)
                setattr(value, "connection_MetadataTable7", self)

    @property
    def Connection(self):
        return self.__Connection

    @Connection.setter
    def Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Connection__Connection", None)
        self.__Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queries"):
                opp_val = getattr(old_value, "queries", None)
                if opp_val == self:
                    setattr(old_value, "queries", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queries"):
                opp_val = getattr(value, "queries", None)
                setattr(value, "queries", self)

    @property
    def connection(self):
        return self.__connection

    @connection.setter
    def connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Connection__connection", None)
        self.__connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QueriesConnection"):
                opp_val = getattr(old_value, "QueriesConnection", None)
                if opp_val == self:
                    setattr(old_value, "QueriesConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueriesConnection"):
                opp_val = getattr(value, "QueriesConnection", None)
                setattr(value, "QueriesConnection", self)

    def getConnectionTypeName(self) :
        # TODO: Implement getConnectionTypeName method
        pass

class connection_SAPFunctionUnit(AbstractMetadataObject):

    def __init__(self, OutputType: str, OutputTableName: str, asXmlSchema: bool, functionUnit: "connection_InputSAPFunctionParameterTable" = None, connection_SAPFunctionUnit: "connection_SAPConnection" = None, functionUnit34: "connection_OutputSAPFunctionParameterTable" = None, connection_SAPFunctionUnit36: "connection_MetadataTable" = None, connection_SAPFunctionUnit39: "connection_SAPConnection" = None, connection_SAPFunctionUnit42: set["connection_MetadataTable"] = None, connection_SAPFunctionUnit45: set["connection_MetadataTable"] = None, functionUnit48: "connection_SAPTestInputParameterTable" = None, connection_SAPFunctionUnit50: "connection_SAPFunctionParamData" = None, SAPFunctionUnit: "connection_InputSAPFunctionParameterTable" = None, SAPFunctionUnit56: "connection_OutputSAPFunctionParameterTable" = None, SAPFunctionUnit90: "connection_SAPTestInputParameterTable" = None):
        self.OutputType = OutputType
        self.OutputTableName = OutputTableName
        self.asXmlSchema = asXmlSchema
        self.functionUnit = functionUnit
        self.connection_SAPFunctionUnit = connection_SAPFunctionUnit
        self.functionUnit34 = functionUnit34
        self.connection_SAPFunctionUnit36 = connection_SAPFunctionUnit36
        self.connection_SAPFunctionUnit39 = connection_SAPFunctionUnit39
        self.connection_SAPFunctionUnit42 = connection_SAPFunctionUnit42 if connection_SAPFunctionUnit42 is not None else set()
        self.connection_SAPFunctionUnit45 = connection_SAPFunctionUnit45 if connection_SAPFunctionUnit45 is not None else set()
        self.functionUnit48 = functionUnit48
        self.connection_SAPFunctionUnit50 = connection_SAPFunctionUnit50
        self.SAPFunctionUnit = SAPFunctionUnit
        self.SAPFunctionUnit56 = SAPFunctionUnit56
        self.SAPFunctionUnit90 = SAPFunctionUnit90
        
        pass
    @property
    def OutputType(self):
        return self.__OutputType

    @OutputType.setter
    def OutputType(self, OutputType: str):
        self.__OutputType = OutputType


    @property
    def asXmlSchema(self):
        return self.__asXmlSchema

    @asXmlSchema.setter
    def asXmlSchema(self, asXmlSchema: bool):
        self.__asXmlSchema = asXmlSchema


    @property
    def OutputTableName(self):
        return self.__OutputTableName

    @OutputTableName.setter
    def OutputTableName(self, OutputTableName: str):
        self.__OutputTableName = OutputTableName


    @property
    def functionUnit48(self):
        return self.__functionUnit48

    @functionUnit48.setter
    def functionUnit48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__functionUnit48", None)
        self.__functionUnit48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SAPTestInputParameterTable"):
                opp_val = getattr(old_value, "SAPTestInputParameterTable", None)
                if opp_val == self:
                    setattr(old_value, "SAPTestInputParameterTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAPTestInputParameterTable"):
                opp_val = getattr(value, "SAPTestInputParameterTable", None)
                setattr(value, "SAPTestInputParameterTable", self)

    @property
    def connection_SAPFunctionUnit42(self):
        return self.__connection_SAPFunctionUnit42

    @connection_SAPFunctionUnit42.setter
    def connection_SAPFunctionUnit42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__connection_SAPFunctionUnit42", None)
        self.__connection_SAPFunctionUnit42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_MetadataTable43"):
                    opp_val = getattr(item, "connection_MetadataTable43", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_MetadataTable43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_MetadataTable43"):
                    opp_val = getattr(item, "connection_MetadataTable43", None)
                    
                    setattr(item, "connection_MetadataTable43", self)
                    

    @property
    def connection_SAPFunctionUnit(self):
        return self.__connection_SAPFunctionUnit

    @connection_SAPFunctionUnit.setter
    def connection_SAPFunctionUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__connection_SAPFunctionUnit", None)
        self.__connection_SAPFunctionUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPConnection"):
                opp_val = getattr(old_value, "connection_SAPConnection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPConnection"):
                opp_val = getattr(value, "connection_SAPConnection", None)
                if opp_val is None:
                    setattr(value, "connection_SAPConnection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_SAPFunctionUnit36(self):
        return self.__connection_SAPFunctionUnit36

    @connection_SAPFunctionUnit36.setter
    def connection_SAPFunctionUnit36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__connection_SAPFunctionUnit36", None)
        self.__connection_SAPFunctionUnit36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_MetadataTable37"):
                opp_val = getattr(old_value, "connection_MetadataTable37", None)
                if opp_val == self:
                    setattr(old_value, "connection_MetadataTable37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_MetadataTable37"):
                opp_val = getattr(value, "connection_MetadataTable37", None)
                setattr(value, "connection_MetadataTable37", self)

    @property
    def functionUnit(self):
        return self.__functionUnit

    @functionUnit.setter
    def functionUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__functionUnit", None)
        self.__functionUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InputSAPFunctionParameterTable"):
                opp_val = getattr(old_value, "InputSAPFunctionParameterTable", None)
                if opp_val == self:
                    setattr(old_value, "InputSAPFunctionParameterTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InputSAPFunctionParameterTable"):
                opp_val = getattr(value, "InputSAPFunctionParameterTable", None)
                setattr(value, "InputSAPFunctionParameterTable", self)

    @property
    def SAPFunctionUnit56(self):
        return self.__SAPFunctionUnit56

    @SAPFunctionUnit56.setter
    def SAPFunctionUnit56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__SAPFunctionUnit56", None)
        self.__SAPFunctionUnit56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutputParameterTable"):
                opp_val = getattr(old_value, "OutputParameterTable", None)
                if opp_val == self:
                    setattr(old_value, "OutputParameterTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutputParameterTable"):
                opp_val = getattr(value, "OutputParameterTable", None)
                setattr(value, "OutputParameterTable", self)

    @property
    def SAPFunctionUnit(self):
        return self.__SAPFunctionUnit

    @SAPFunctionUnit.setter
    def SAPFunctionUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__SAPFunctionUnit", None)
        self.__SAPFunctionUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InputParameterTable"):
                opp_val = getattr(old_value, "InputParameterTable", None)
                if opp_val == self:
                    setattr(old_value, "InputParameterTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InputParameterTable"):
                opp_val = getattr(value, "InputParameterTable", None)
                setattr(value, "InputParameterTable", self)

    @property
    def functionUnit34(self):
        return self.__functionUnit34

    @functionUnit34.setter
    def functionUnit34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__functionUnit34", None)
        self.__functionUnit34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OutputSAPFunctionParameterTable"):
                opp_val = getattr(old_value, "OutputSAPFunctionParameterTable", None)
                if opp_val == self:
                    setattr(old_value, "OutputSAPFunctionParameterTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OutputSAPFunctionParameterTable"):
                opp_val = getattr(value, "OutputSAPFunctionParameterTable", None)
                setattr(value, "OutputSAPFunctionParameterTable", self)

    @property
    def SAPFunctionUnit90(self):
        return self.__SAPFunctionUnit90

    @SAPFunctionUnit90.setter
    def SAPFunctionUnit90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__SAPFunctionUnit90", None)
        self.__SAPFunctionUnit90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TestInputParameterTable"):
                opp_val = getattr(old_value, "TestInputParameterTable", None)
                if opp_val == self:
                    setattr(old_value, "TestInputParameterTable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TestInputParameterTable"):
                opp_val = getattr(value, "TestInputParameterTable", None)
                setattr(value, "TestInputParameterTable", self)

    @property
    def connection_SAPFunctionUnit39(self):
        return self.__connection_SAPFunctionUnit39

    @connection_SAPFunctionUnit39.setter
    def connection_SAPFunctionUnit39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__connection_SAPFunctionUnit39", None)
        self.__connection_SAPFunctionUnit39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPConnection40"):
                opp_val = getattr(old_value, "connection_SAPConnection40", None)
                if opp_val == self:
                    setattr(old_value, "connection_SAPConnection40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPConnection40"):
                opp_val = getattr(value, "connection_SAPConnection40", None)
                setattr(value, "connection_SAPConnection40", self)

    @property
    def connection_SAPFunctionUnit50(self):
        return self.__connection_SAPFunctionUnit50

    @connection_SAPFunctionUnit50.setter
    def connection_SAPFunctionUnit50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__connection_SAPFunctionUnit50", None)
        self.__connection_SAPFunctionUnit50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionParamData"):
                opp_val = getattr(old_value, "connection_SAPFunctionParamData", None)
                if opp_val == self:
                    setattr(old_value, "connection_SAPFunctionParamData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionParamData"):
                opp_val = getattr(value, "connection_SAPFunctionParamData", None)
                setattr(value, "connection_SAPFunctionParamData", self)

    @property
    def connection_SAPFunctionUnit45(self):
        return self.__connection_SAPFunctionUnit45

    @connection_SAPFunctionUnit45.setter
    def connection_SAPFunctionUnit45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__connection_SAPFunctionUnit45", None)
        self.__connection_SAPFunctionUnit45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_MetadataTable46"):
                    opp_val = getattr(item, "connection_MetadataTable46", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_MetadataTable46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_MetadataTable46"):
                    opp_val = getattr(item, "connection_MetadataTable46", None)
                    
                    setattr(item, "connection_MetadataTable46", self)
                    

    def setDocument(self, connection_document):
        # TODO: Implement setDocument method
        pass

class connection_Metadata(AbstractMetadataObject):

    pass