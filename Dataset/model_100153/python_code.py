from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FileFormat(Enum):
    UNIX = "UNIX"
    MAC = "MAC"
    WINDOWS = "WINDOWS"
class FieldSeparator(Enum):
    Space = "Space"
    Alt_65 = "Alt_65"
    Custom_ANSI = "Custom_ANSI"
    Custom_UTF8 = "Custom_UTF8"
    Custom_RegExp = "Custom_RegExp"
    Tabulation = "Tabulation"
    Semicolon = "Semicolon"
    Comma = "Comma"
class DevelopmentStatus(Enum):
    DRAFT = "DRAFT"
    PROD = "PROD"
class Escape(Enum):
    Delimited = "Delimited"
    CSV = "CSV"
class RowSeparator(Enum):
    Custom_String = "Custom_String"
    Standart_EOL = "Standart_EOL"


############################################
# Definition of Classes
############################################

class xml_TdXMLElement:

    pass
class connection_xml_TdXMLContent:

    pass
class xml_TdXMLContent:

    pass
class xml_TdXMLDocument:

    pass
class connection_xml_TdXMLElement:

    def __init__(self, javaType: str, connection_xml_TdXMLElement: "xml_TdXMLDocument" = None, connection_xml_TdXMLElement58: "xml_TdXMLContent" = None):
        self.javaType = javaType
        self.connection_xml_TdXMLElement = connection_xml_TdXMLElement
        self.connection_xml_TdXMLElement58 = connection_xml_TdXMLElement58
        
        pass
    @property
    def javaType(self):
        return self.__javaType

    @javaType.setter
    def javaType(self, javaType: str):
        self.__javaType = javaType


    @property
    def connection_xml_TdXMLElement(self):
        return self.__connection_xml_TdXMLElement

    @connection_xml_TdXMLElement.setter
    def connection_xml_TdXMLElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_xml_TdXMLElement__connection_xml_TdXMLElement", None)
        self.__connection_xml_TdXMLElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xml_TdXMLDocument"):
                opp_val = getattr(old_value, "xml_TdXMLDocument", None)
                if opp_val == self:
                    setattr(old_value, "xml_TdXMLDocument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xml_TdXMLDocument"):
                opp_val = getattr(value, "xml_TdXMLDocument", None)
                setattr(value, "xml_TdXMLDocument", self)

    @property
    def connection_xml_TdXMLElement58(self):
        return self.__connection_xml_TdXMLElement58

    @connection_xml_TdXMLElement58.setter
    def connection_xml_TdXMLElement58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_xml_TdXMLElement__connection_xml_TdXMLElement58", None)
        self.__connection_xml_TdXMLElement58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xml_TdXMLContent"):
                opp_val = getattr(old_value, "xml_TdXMLContent", None)
                if opp_val == self:
                    setattr(old_value, "xml_TdXMLContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xml_TdXMLContent"):
                opp_val = getattr(value, "xml_TdXMLContent", None)
                setattr(value, "xml_TdXMLContent", self)

    def setContentType(self, connection_contentType):
        # TODO: Implement setContentType method
        pass

    def getContentType(self):
        # TODO: Implement getContentType method
        pass

class connection_softwaredeployment_TdMachine:

    pass
class connection_softwaredeployment_TdSoftwareSystem:

    pass
class connection_softwaredeployment_TdDataManager:

    pass
class connection_relational_TdProcedure:

    pass
class connection_xml_TdXMLDocument:

    def __init__(self, xsdFilePath: str):
        self.xsdFilePath = xsdFilePath
        
        pass
    @property
    def xsdFilePath(self):
        return self.__xsdFilePath

    @xsdFilePath.setter
    def xsdFilePath(self, xsdFilePath: str):
        self.__xsdFilePath = xsdFilePath


class connection_relational_TdSqlDataType:

    def __init__(self, caseSensitive: str, autoIncrement: str, localTypeName: str, searchable: str, javaDataType: int, nullable: str, unsignedAttribute: str):
        self.caseSensitive = caseSensitive
        self.autoIncrement = autoIncrement
        self.localTypeName = localTypeName
        self.searchable = searchable
        self.javaDataType = javaDataType
        self.nullable = nullable
        self.unsignedAttribute = unsignedAttribute
        
        pass
    @property
    def localTypeName(self):
        return self.__localTypeName

    @localTypeName.setter
    def localTypeName(self, localTypeName: str):
        self.__localTypeName = localTypeName


    @property
    def unsignedAttribute(self):
        return self.__unsignedAttribute

    @unsignedAttribute.setter
    def unsignedAttribute(self, unsignedAttribute: str):
        self.__unsignedAttribute = unsignedAttribute


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: str):
        self.__nullable = nullable


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
    def autoIncrement(self):
        return self.__autoIncrement

    @autoIncrement.setter
    def autoIncrement(self, autoIncrement: str):
        self.__autoIncrement = autoIncrement


    @property
    def caseSensitive(self):
        return self.__caseSensitive

    @caseSensitive.setter
    def caseSensitive(self, caseSensitive: str):
        self.__caseSensitive = caseSensitive


class relational_TdSqlDataType:

    pass
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

    def getContentType(self):
        # TODO: Implement getContentType method
        pass

    def getJavaType(self):
        # TODO: Implement getJavaType method
        pass

    def setContentType(self, connection_contentType):
        # TODO: Implement setContentType method
        pass

class connection_relational_TdView:

    pass
class connection_relational_TdTable:

    pass
class connection_GenericPackage:

    pass
class connection_relational_TdTrigger:

    pass
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
            if hasattr(old_value, "connection_CDCType46"):
                opp_val = getattr(old_value, "connection_CDCType46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_CDCType46"):
                opp_val = getattr(value, "connection_CDCType46", None)
                if opp_val is None:
                    setattr(value, "connection_CDCType46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_ConceptTarget:

    def __init__(self, targetName: str, RelativeLoopExpression: str, ConceptTarget: "connection_Concept" = None, conceptTargets: "connection_Concept" = None):
        self.targetName = targetName
        self.RelativeLoopExpression = RelativeLoopExpression
        self.ConceptTarget = ConceptTarget
        self.conceptTargets = conceptTargets
        
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
            if hasattr(old_value, "schema53"):
                opp_val = getattr(old_value, "schema53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema53"):
                opp_val = getattr(value, "schema53", None)
                if opp_val is None:
                    setattr(value, "schema53", set([self]))
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
    def SchemaTarget(self):
        return self.__SchemaTarget

    @SchemaTarget.setter
    def SchemaTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SchemaTarget__SchemaTarget", None)
        self.__SchemaTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema42"):
                opp_val = getattr(old_value, "schema42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema42"):
                opp_val = getattr(value, "schema42", None)
                if opp_val is None:
                    setattr(value, "schema42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "XmlXPathLoopDescriptor34"):
                opp_val = getattr(old_value, "XmlXPathLoopDescriptor34", None)
                if opp_val == self:
                    setattr(old_value, "XmlXPathLoopDescriptor34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XmlXPathLoopDescriptor34"):
                opp_val = getattr(value, "XmlXPathLoopDescriptor34", None)
                setattr(value, "XmlXPathLoopDescriptor34", self)

class connection_XmlXPathLoopDescriptor:

    def __init__(self, LimitBoucle: str, AbsoluteXPathQuery: str, XmlXPathLoopDescriptor: "connection_XmlFileConnection" = None, XmlXPathLoopDescriptor34: "connection_SchemaTarget" = None, schema: "connection_XmlFileConnection" = None, schema42: set["connection_SchemaTarget"] = None):
        self.LimitBoucle = LimitBoucle
        self.AbsoluteXPathQuery = AbsoluteXPathQuery
        self.XmlXPathLoopDescriptor = XmlXPathLoopDescriptor
        self.XmlXPathLoopDescriptor34 = XmlXPathLoopDescriptor34
        self.schema = schema
        self.schema42 = schema42 if schema42 is not None else set()
        
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
    def XmlXPathLoopDescriptor34(self):
        return self.__XmlXPathLoopDescriptor34

    @XmlXPathLoopDescriptor34.setter
    def XmlXPathLoopDescriptor34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlXPathLoopDescriptor__XmlXPathLoopDescriptor34", None)
        self.__XmlXPathLoopDescriptor34 = value
        
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
    def schema42(self):
        return self.__schema42

    @schema42.setter
    def schema42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlXPathLoopDescriptor__schema42", None)
        self.__schema42 = value if value is not None else set()
        
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
    def XmlXPathLoopDescriptor(self):
        return self.__XmlXPathLoopDescriptor

    @XmlXPathLoopDescriptor.setter
    def XmlXPathLoopDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlXPathLoopDescriptor__XmlXPathLoopDescriptor", None)
        self.__XmlXPathLoopDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection32"):
                opp_val = getattr(old_value, "connection32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection32"):
                opp_val = getattr(value, "connection32", None)
                if opp_val is None:
                    setattr(value, "connection32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_OutputSAPFunctionParameterTable(SAPFunctionParameterTable):

    pass
class connection_InputSAPFunctionParameterTable(SAPFunctionParameterTable):

    pass
class connection_SAPTestInputParameterTable(SAPFunctionParameterTable):

    pass
class connection_CDCConnection:

    pass
class FileConnection:

    pass
class connection_EbcdicConnection(FileConnection):

    def __init__(self, MidFile: str, DataFile: str):
        self.MidFile = MidFile
        self.DataFile = DataFile
        
        pass
    @property
    def DataFile(self):
        return self.__DataFile

    @DataFile.setter
    def DataFile(self, DataFile: str):
        self.__DataFile = DataFile


    @property
    def MidFile(self):
        return self.__MidFile

    @MidFile.setter
    def MidFile(self, MidFile: str):
        self.__MidFile = MidFile


class connection_FileExcelConnection(FileConnection):

    def __init__(self, SheetName: str, sheetColumns: str, firstColumn: str, lastColumn: str, thousandSeparator: str, decimalSeparator: str, advancedSpearator: bool, selectAllSheets: bool, sheetList: str):
        self.SheetName = SheetName
        self.sheetColumns = sheetColumns
        self.firstColumn = firstColumn
        self.lastColumn = lastColumn
        self.thousandSeparator = thousandSeparator
        self.decimalSeparator = decimalSeparator
        self.advancedSpearator = advancedSpearator
        self.selectAllSheets = selectAllSheets
        self.sheetList = sheetList
        
        pass
    @property
    def sheetList(self):
        return self.__sheetList

    @sheetList.setter
    def sheetList(self, sheetList: str):
        self.__sheetList = sheetList


    @property
    def SheetName(self):
        return self.__SheetName

    @SheetName.setter
    def SheetName(self, SheetName: str):
        self.__SheetName = SheetName


    @property
    def selectAllSheets(self):
        return self.__selectAllSheets

    @selectAllSheets.setter
    def selectAllSheets(self, selectAllSheets: bool):
        self.__selectAllSheets = selectAllSheets


    @property
    def lastColumn(self):
        return self.__lastColumn

    @lastColumn.setter
    def lastColumn(self, lastColumn: str):
        self.__lastColumn = lastColumn


    @property
    def firstColumn(self):
        return self.__firstColumn

    @firstColumn.setter
    def firstColumn(self, firstColumn: str):
        self.__firstColumn = firstColumn


    @property
    def advancedSpearator(self):
        return self.__advancedSpearator

    @advancedSpearator.setter
    def advancedSpearator(self, advancedSpearator: bool):
        self.__advancedSpearator = advancedSpearator


    @property
    def thousandSeparator(self):
        return self.__thousandSeparator

    @thousandSeparator.setter
    def thousandSeparator(self, thousandSeparator: str):
        self.__thousandSeparator = thousandSeparator


    @property
    def decimalSeparator(self):
        return self.__decimalSeparator

    @decimalSeparator.setter
    def decimalSeparator(self, decimalSeparator: str):
        self.__decimalSeparator = decimalSeparator


    @property
    def sheetColumns(self):
        return self.__sheetColumns

    @sheetColumns.setter
    def sheetColumns(self, sheetColumns: str):
        self.__sheetColumns = sheetColumns


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


class connection_PositionalFileConnection(FileConnection):

    pass
class connection_HL7Connection(FileConnection):

    def __init__(self, StartChar: str, EndChar: int):
        self.StartChar = StartChar
        self.EndChar = EndChar
        
        pass
    @property
    def StartChar(self):
        return self.__StartChar

    @StartChar.setter
    def StartChar(self, StartChar: str):
        self.__StartChar = StartChar


    @property
    def EndChar(self):
        return self.__EndChar

    @EndChar.setter
    def EndChar(self, EndChar: int):
        self.__EndChar = EndChar


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


class connection_Concept(TdTable):

    def __init__(self, LoopExpression: str, LoopLimit: str, schema53: set["connection_ConceptTarget"] = None, Concept: "connection_ConceptTarget" = None, connection_Concept: "connection_MDMConnection" = None):
        self.LoopExpression = LoopExpression
        self.LoopLimit = LoopLimit
        self.schema53 = schema53 if schema53 is not None else set()
        self.Concept = Concept
        self.connection_Concept = connection_Concept
        
        pass
    @property
    def LoopLimit(self):
        return self.__LoopLimit

    @LoopLimit.setter
    def LoopLimit(self, LoopLimit: str):
        self.__LoopLimit = LoopLimit


    @property
    def LoopExpression(self):
        return self.__LoopExpression

    @LoopExpression.setter
    def LoopExpression(self, LoopExpression: str):
        self.__LoopExpression = LoopExpression


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
    def schema53(self):
        return self.__schema53

    @schema53.setter
    def schema53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__schema53", None)
        self.__schema53 = value if value is not None else set()
        
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
class connection_XmlFileConnection(Connection):

    def __init__(self, XsdFilePath: str, XmlFilePath: str, Guess: bool, MaskXPattern: str, Encoding: str, connection32: set["connection_XmlXPathLoopDescriptor"] = None, XmlFileConnection: "connection_XmlXPathLoopDescriptor" = None):
        self.XsdFilePath = XsdFilePath
        self.XmlFilePath = XmlFilePath
        self.Guess = Guess
        self.MaskXPattern = MaskXPattern
        self.Encoding = Encoding
        self.connection32 = connection32 if connection32 is not None else set()
        self.XmlFileConnection = XmlFileConnection
        
        pass
    @property
    def XsdFilePath(self):
        return self.__XsdFilePath

    @XsdFilePath.setter
    def XsdFilePath(self, XsdFilePath: str):
        self.__XsdFilePath = XsdFilePath


    @property
    def XmlFilePath(self):
        return self.__XmlFilePath

    @XmlFilePath.setter
    def XmlFilePath(self, XmlFilePath: str):
        self.__XmlFilePath = XmlFilePath


    @property
    def Guess(self):
        return self.__Guess

    @Guess.setter
    def Guess(self, Guess: bool):
        self.__Guess = Guess


    @property
    def Encoding(self):
        return self.__Encoding

    @Encoding.setter
    def Encoding(self, Encoding: str):
        self.__Encoding = Encoding


    @property
    def MaskXPattern(self):
        return self.__MaskXPattern

    @MaskXPattern.setter
    def MaskXPattern(self, MaskXPattern: str):
        self.__MaskXPattern = MaskXPattern


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
    def connection32(self):
        return self.__connection32

    @connection32.setter
    def connection32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlFileConnection__connection32", None)
        self.__connection32 = value if value is not None else set()
        
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
                    

class connection_SalesforceSchemaConnection(Connection):

    def __init__(self, proxyPort: str, proxyUsername: str, proxyPassword: str, batchSize: str, useHttpProxy: bool, useAlphbet: bool, timeOut: str, webServiceUrl: str, userName: str, password: str, moduleName: str, queryCondition: str, useCustomModuleName: bool, useProxy: bool, proxyHost: str):
        self.proxyPort = proxyPort
        self.proxyUsername = proxyUsername
        self.proxyPassword = proxyPassword
        self.batchSize = batchSize
        self.useHttpProxy = useHttpProxy
        self.useAlphbet = useAlphbet
        self.timeOut = timeOut
        self.webServiceUrl = webServiceUrl
        self.userName = userName
        self.password = password
        self.moduleName = moduleName
        self.queryCondition = queryCondition
        self.useCustomModuleName = useCustomModuleName
        self.useProxy = useProxy
        self.proxyHost = proxyHost
        
        pass
    @property
    def useHttpProxy(self):
        return self.__useHttpProxy

    @useHttpProxy.setter
    def useHttpProxy(self, useHttpProxy: bool):
        self.__useHttpProxy = useHttpProxy


    @property
    def proxyPassword(self):
        return self.__proxyPassword

    @proxyPassword.setter
    def proxyPassword(self, proxyPassword: str):
        self.__proxyPassword = proxyPassword


    @property
    def useProxy(self):
        return self.__useProxy

    @useProxy.setter
    def useProxy(self, useProxy: bool):
        self.__useProxy = useProxy


    @property
    def useCustomModuleName(self):
        return self.__useCustomModuleName

    @useCustomModuleName.setter
    def useCustomModuleName(self, useCustomModuleName: bool):
        self.__useCustomModuleName = useCustomModuleName


    @property
    def queryCondition(self):
        return self.__queryCondition

    @queryCondition.setter
    def queryCondition(self, queryCondition: str):
        self.__queryCondition = queryCondition


    @property
    def timeOut(self):
        return self.__timeOut

    @timeOut.setter
    def timeOut(self, timeOut: str):
        self.__timeOut = timeOut


    @property
    def userName(self):
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName


    @property
    def webServiceUrl(self):
        return self.__webServiceUrl

    @webServiceUrl.setter
    def webServiceUrl(self, webServiceUrl: str):
        self.__webServiceUrl = webServiceUrl


    @property
    def batchSize(self):
        return self.__batchSize

    @batchSize.setter
    def batchSize(self, batchSize: str):
        self.__batchSize = batchSize


    @property
    def proxyUsername(self):
        return self.__proxyUsername

    @proxyUsername.setter
    def proxyUsername(self, proxyUsername: str):
        self.__proxyUsername = proxyUsername


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
    def proxyPort(self):
        return self.__proxyPort

    @proxyPort.setter
    def proxyPort(self, proxyPort: str):
        self.__proxyPort = proxyPort


    @property
    def moduleName(self):
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName


    @property
    def proxyHost(self):
        return self.__proxyHost

    @proxyHost.setter
    def proxyHost(self, proxyHost: str):
        self.__proxyHost = proxyHost


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


class connection_MDMConnection(Connection):

    def __init__(self, Username: str, Password: str, Port: str, Server: str, Universe: str, Datamodel: str, Datacluster: str, connection_MDMConnection: set["connection_Concept"] = None):
        self.Username = Username
        self.Password = Password
        self.Port = Port
        self.Server = Server
        self.Universe = Universe
        self.Datamodel = Datamodel
        self.Datacluster = Datacluster
        self.connection_MDMConnection = connection_MDMConnection if connection_MDMConnection is not None else set()
        
        pass
    @property
    def Datamodel(self):
        return self.__Datamodel

    @Datamodel.setter
    def Datamodel(self, Datamodel: str):
        self.__Datamodel = Datamodel


    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def Datacluster(self):
        return self.__Datacluster

    @Datacluster.setter
    def Datacluster(self, Datacluster: str):
        self.__Datacluster = Datacluster


    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, Port: str):
        self.__Port = Port


    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username


    @property
    def Server(self):
        return self.__Server

    @Server.setter
    def Server(self, Server: str):
        self.__Server = Server


    @property
    def Universe(self):
        return self.__Universe

    @Universe.setter
    def Universe(self, Universe: str):
        self.__Universe = Universe


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
                    

class connection_DatabaseConnection(Connection):

    def __init__(self, URL: str, dbVersionString: str, Port: str, DatabaseType: str, SystemSQL: bool, DriverJarPath: str, DriverClass: str, cdcTypeMode: str, SQLMode: bool, UiSchema: str, Username: str, Password: str, ServerName: str, DatasourceName: str, FileFieldName: str, SID: str, SqlSynthax: str, StringQuote: str, NullChar: str, DbmsId: str, ProductId: str, DBRootPath: str, AdditionalParams: str, StandardSQL: bool, DatabaseConnection: "connection_CDCConnection" = None, connection11: "connection_CDCConnection" = None):
        self.URL = URL
        self.dbVersionString = dbVersionString
        self.Port = Port
        self.DatabaseType = DatabaseType
        self.SystemSQL = SystemSQL
        self.DriverJarPath = DriverJarPath
        self.DriverClass = DriverClass
        self.cdcTypeMode = cdcTypeMode
        self.SQLMode = SQLMode
        self.UiSchema = UiSchema
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
        self.DBRootPath = DBRootPath
        self.AdditionalParams = AdditionalParams
        self.StandardSQL = StandardSQL
        self.DatabaseConnection = DatabaseConnection
        self.connection11 = connection11
        
        pass
    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


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
    def DbmsId(self):
        return self.__DbmsId

    @DbmsId.setter
    def DbmsId(self, DbmsId: str):
        self.__DbmsId = DbmsId


    @property
    def AdditionalParams(self):
        return self.__AdditionalParams

    @AdditionalParams.setter
    def AdditionalParams(self, AdditionalParams: str):
        self.__AdditionalParams = AdditionalParams


    @property
    def cdcTypeMode(self):
        return self.__cdcTypeMode

    @cdcTypeMode.setter
    def cdcTypeMode(self, cdcTypeMode: str):
        self.__cdcTypeMode = cdcTypeMode


    @property
    def DBRootPath(self):
        return self.__DBRootPath

    @DBRootPath.setter
    def DBRootPath(self, DBRootPath: str):
        self.__DBRootPath = DBRootPath


    @property
    def SID(self):
        return self.__SID

    @SID.setter
    def SID(self, SID: str):
        self.__SID = SID


    @property
    def dbVersionString(self):
        return self.__dbVersionString

    @dbVersionString.setter
    def dbVersionString(self, dbVersionString: str):
        self.__dbVersionString = dbVersionString


    @property
    def SystemSQL(self):
        return self.__SystemSQL

    @SystemSQL.setter
    def SystemSQL(self, SystemSQL: bool):
        self.__SystemSQL = SystemSQL


    @property
    def DriverClass(self):
        return self.__DriverClass

    @DriverClass.setter
    def DriverClass(self, DriverClass: str):
        self.__DriverClass = DriverClass


    @property
    def NullChar(self):
        return self.__NullChar

    @NullChar.setter
    def NullChar(self, NullChar: str):
        self.__NullChar = NullChar


    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username


    @property
    def DriverJarPath(self):
        return self.__DriverJarPath

    @DriverJarPath.setter
    def DriverJarPath(self, DriverJarPath: str):
        self.__DriverJarPath = DriverJarPath


    @property
    def URL(self):
        return self.__URL

    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL


    @property
    def ServerName(self):
        return self.__ServerName

    @ServerName.setter
    def ServerName(self, ServerName: str):
        self.__ServerName = ServerName


    @property
    def StringQuote(self):
        return self.__StringQuote

    @StringQuote.setter
    def StringQuote(self, StringQuote: str):
        self.__StringQuote = StringQuote


    @property
    def ProductId(self):
        return self.__ProductId

    @ProductId.setter
    def ProductId(self, ProductId: str):
        self.__ProductId = ProductId


    @property
    def UiSchema(self):
        return self.__UiSchema

    @UiSchema.setter
    def UiSchema(self, UiSchema: str):
        self.__UiSchema = UiSchema


    @property
    def FileFieldName(self):
        return self.__FileFieldName

    @FileFieldName.setter
    def FileFieldName(self, FileFieldName: str):
        self.__FileFieldName = FileFieldName


    @property
    def StandardSQL(self):
        return self.__StandardSQL

    @StandardSQL.setter
    def StandardSQL(self, StandardSQL: bool):
        self.__StandardSQL = StandardSQL


    @property
    def DatabaseType(self):
        return self.__DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType: str):
        self.__DatabaseType = DatabaseType


    @property
    def DatasourceName(self):
        return self.__DatasourceName

    @DatasourceName.setter
    def DatasourceName(self, DatasourceName: str):
        self.__DatasourceName = DatasourceName


    @property
    def SQLMode(self):
        return self.__SQLMode

    @SQLMode.setter
    def SQLMode(self, SQLMode: bool):
        self.__SQLMode = SQLMode


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

    @property
    def connection11(self):
        return self.__connection11

    @connection11.setter
    def connection11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_DatabaseConnection__connection11", None)
        self.__connection11 = value
        
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

class connection_LDAPSchemaConnection(Connection):

    def __init__(self, Host: str, Port: str, Protocol: str, Filter: str, SelectedDN: str, Separator: str, UseAdvanced: bool, StorePath: str, UseLimit: bool, UseAuthen: bool, BindPrincipal: str, BindPassword: str, LimitValue: int, EncryptionMethodName: str, Value: str, SavePassword: bool, Aliases: str, Referrals: str, CountLimit: str, TimeOutLimit: str, BaseDNs: str, GetBaseDNsFromRoot: bool, ReturnAttributes: str):
        self.Host = Host
        self.Port = Port
        self.Protocol = Protocol
        self.Filter = Filter
        self.SelectedDN = SelectedDN
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
        
        pass
    @property
    def Separator(self):
        return self.__Separator

    @Separator.setter
    def Separator(self, Separator: str):
        self.__Separator = Separator


    @property
    def Aliases(self):
        return self.__Aliases

    @Aliases.setter
    def Aliases(self, Aliases: str):
        self.__Aliases = Aliases


    @property
    def TimeOutLimit(self):
        return self.__TimeOutLimit

    @TimeOutLimit.setter
    def TimeOutLimit(self, TimeOutLimit: str):
        self.__TimeOutLimit = TimeOutLimit


    @property
    def UseAuthen(self):
        return self.__UseAuthen

    @UseAuthen.setter
    def UseAuthen(self, UseAuthen: bool):
        self.__UseAuthen = UseAuthen


    @property
    def Filter(self):
        return self.__Filter

    @Filter.setter
    def Filter(self, Filter: str):
        self.__Filter = Filter


    @property
    def BindPassword(self):
        return self.__BindPassword

    @BindPassword.setter
    def BindPassword(self, BindPassword: str):
        self.__BindPassword = BindPassword


    @property
    def BaseDNs(self):
        return self.__BaseDNs

    @BaseDNs.setter
    def BaseDNs(self, BaseDNs: str):
        self.__BaseDNs = BaseDNs


    @property
    def BindPrincipal(self):
        return self.__BindPrincipal

    @BindPrincipal.setter
    def BindPrincipal(self, BindPrincipal: str):
        self.__BindPrincipal = BindPrincipal


    @property
    def SavePassword(self):
        return self.__SavePassword

    @SavePassword.setter
    def SavePassword(self, SavePassword: bool):
        self.__SavePassword = SavePassword


    @property
    def SelectedDN(self):
        return self.__SelectedDN

    @SelectedDN.setter
    def SelectedDN(self, SelectedDN: str):
        self.__SelectedDN = SelectedDN


    @property
    def Host(self):
        return self.__Host

    @Host.setter
    def Host(self, Host: str):
        self.__Host = Host


    @property
    def Protocol(self):
        return self.__Protocol

    @Protocol.setter
    def Protocol(self, Protocol: str):
        self.__Protocol = Protocol


    @property
    def StorePath(self):
        return self.__StorePath

    @StorePath.setter
    def StorePath(self, StorePath: str):
        self.__StorePath = StorePath


    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value


    @property
    def EncryptionMethodName(self):
        return self.__EncryptionMethodName

    @EncryptionMethodName.setter
    def EncryptionMethodName(self, EncryptionMethodName: str):
        self.__EncryptionMethodName = EncryptionMethodName


    @property
    def CountLimit(self):
        return self.__CountLimit

    @CountLimit.setter
    def CountLimit(self, CountLimit: str):
        self.__CountLimit = CountLimit


    @property
    def Referrals(self):
        return self.__Referrals

    @Referrals.setter
    def Referrals(self, Referrals: str):
        self.__Referrals = Referrals


    @property
    def UseLimit(self):
        return self.__UseLimit

    @UseLimit.setter
    def UseLimit(self, UseLimit: bool):
        self.__UseLimit = UseLimit


    @property
    def ReturnAttributes(self):
        return self.__ReturnAttributes

    @ReturnAttributes.setter
    def ReturnAttributes(self, ReturnAttributes: str):
        self.__ReturnAttributes = ReturnAttributes


    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, Port: str):
        self.__Port = Port


    @property
    def UseAdvanced(self):
        return self.__UseAdvanced

    @UseAdvanced.setter
    def UseAdvanced(self, UseAdvanced: bool):
        self.__UseAdvanced = UseAdvanced


    @property
    def GetBaseDNsFromRoot(self):
        return self.__GetBaseDNsFromRoot

    @GetBaseDNsFromRoot.setter
    def GetBaseDNsFromRoot(self, GetBaseDNsFromRoot: bool):
        self.__GetBaseDNsFromRoot = GetBaseDNsFromRoot


    @property
    def LimitValue(self):
        return self.__LimitValue

    @LimitValue.setter
    def LimitValue(self, LimitValue: int):
        self.__LimitValue = LimitValue


class connection_LdifFileConnection(Connection):

    def __init__(self, value: str, FilePath: str, LimitEntry: int, UseLimit: bool, Server: str):
        self.value = value
        self.FilePath = FilePath
        self.LimitEntry = LimitEntry
        self.UseLimit = UseLimit
        self.Server = Server
        
        pass
    @property
    def LimitEntry(self):
        return self.__LimitEntry

    @LimitEntry.setter
    def LimitEntry(self, LimitEntry: int):
        self.__LimitEntry = LimitEntry


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
    def Server(self):
        return self.__Server

    @Server.setter
    def Server(self, Server: str):
        self.__Server = Server


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class connection_WSDLSchemaConnection(Connection):

    def __init__(self, WSDL: str, needAuth: bool, methodName: str, parameters: str, UserName: str, Password: str, useProxy: bool, proxyHost: str, proxyPort: str, proxyUser: str, proxyPassword: str, Value: str, EndpointURI: str, Encoding: str, timeOut: int):
        self.WSDL = WSDL
        self.needAuth = needAuth
        self.methodName = methodName
        self.parameters = parameters
        self.UserName = UserName
        self.Password = Password
        self.useProxy = useProxy
        self.proxyHost = proxyHost
        self.proxyPort = proxyPort
        self.proxyUser = proxyUser
        self.proxyPassword = proxyPassword
        self.Value = Value
        self.EndpointURI = EndpointURI
        self.Encoding = Encoding
        self.timeOut = timeOut
        
        pass
    @property
    def useProxy(self):
        return self.__useProxy

    @useProxy.setter
    def useProxy(self, useProxy: bool):
        self.__useProxy = useProxy


    @property
    def proxyHost(self):
        return self.__proxyHost

    @proxyHost.setter
    def proxyHost(self, proxyHost: str):
        self.__proxyHost = proxyHost


    @property
    def Encoding(self):
        return self.__Encoding

    @Encoding.setter
    def Encoding(self, Encoding: str):
        self.__Encoding = Encoding


    @property
    def EndpointURI(self):
        return self.__EndpointURI

    @EndpointURI.setter
    def EndpointURI(self, EndpointURI: str):
        self.__EndpointURI = EndpointURI


    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def proxyPort(self):
        return self.__proxyPort

    @proxyPort.setter
    def proxyPort(self, proxyPort: str):
        self.__proxyPort = proxyPort


    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters


    @property
    def needAuth(self):
        return self.__needAuth

    @needAuth.setter
    def needAuth(self, needAuth: bool):
        self.__needAuth = needAuth


    @property
    def methodName(self):
        return self.__methodName

    @methodName.setter
    def methodName(self, methodName: str):
        self.__methodName = methodName


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
    def timeOut(self):
        return self.__timeOut

    @timeOut.setter
    def timeOut(self, timeOut: int):
        self.__timeOut = timeOut


    @property
    def proxyUser(self):
        return self.__proxyUser

    @proxyUser.setter
    def proxyUser(self, proxyUser: str):
        self.__proxyUser = proxyUser


    @property
    def proxyPassword(self):
        return self.__proxyPassword

    @proxyPassword.setter
    def proxyPassword(self, proxyPassword: str):
        self.__proxyPassword = proxyPassword


    @property
    def UserName(self):
        return self.__UserName

    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName


class connection_SAPConnection(Connection):

    def __init__(self, Host: str, Username: str, Password: str, Client: str, SystemNumber: str, Language: str, currentFucntion: str, SAPConnection: "connection_SAPFunctionUnit" = None, connection13: set["connection_SAPFunctionUnit"] = None):
        self.Host = Host
        self.Username = Username
        self.Password = Password
        self.Client = Client
        self.SystemNumber = SystemNumber
        self.Language = Language
        self.currentFucntion = currentFucntion
        self.SAPConnection = SAPConnection
        self.connection13 = connection13 if connection13 is not None else set()
        
        pass
    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username


    @property
    def SystemNumber(self):
        return self.__SystemNumber

    @SystemNumber.setter
    def SystemNumber(self, SystemNumber: str):
        self.__SystemNumber = SystemNumber


    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def Host(self):
        return self.__Host

    @Host.setter
    def Host(self, Host: str):
        self.__Host = Host


    @property
    def currentFucntion(self):
        return self.__currentFucntion

    @currentFucntion.setter
    def currentFucntion(self, currentFucntion: str):
        self.__currentFucntion = currentFucntion


    @property
    def Language(self):
        return self.__Language

    @Language.setter
    def Language(self, Language: str):
        self.__Language = Language


    @property
    def Client(self):
        return self.__Client

    @Client.setter
    def Client(self, Client: str):
        self.__Client = Client


    @property
    def connection13(self):
        return self.__connection13

    @connection13.setter
    def connection13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__connection13", None)
        self.__connection13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SAPFunctionUnit"):
                    opp_val = getattr(item, "SAPFunctionUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "SAPFunctionUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SAPFunctionUnit"):
                    opp_val = getattr(item, "SAPFunctionUnit", None)
                    
                    setattr(item, "SAPFunctionUnit", self)
                    

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
            if hasattr(old_value, "Funtions"):
                opp_val = getattr(old_value, "Funtions", None)
                if opp_val == self:
                    setattr(old_value, "Funtions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Funtions"):
                opp_val = getattr(value, "Funtions", None)
                setattr(value, "Funtions", self)

class connection_FileConnection(Connection):

    def __init__(self, Server: str, FilePath: str, Format: str, Encoding: str, FieldSeparatorValue: str, RowSeparatorType: str, RowSeparatorValue: str, TextIdentifier: str, UseHeader: bool, HeaderValue: str, UseFooter: bool, FooterValue: str, UseLimit: bool, LimitValue: str, FirstLineCaption: bool, RemoveEmptyRow: bool, EscapeType: str, EscapeChar: str, TextEnclosure: str, CsvOption: bool):
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
        self.FirstLineCaption = FirstLineCaption
        self.RemoveEmptyRow = RemoveEmptyRow
        self.EscapeType = EscapeType
        self.EscapeChar = EscapeChar
        self.TextEnclosure = TextEnclosure
        self.CsvOption = CsvOption
        
        pass
    @property
    def CsvOption(self):
        return self.__CsvOption

    @CsvOption.setter
    def CsvOption(self, CsvOption: bool):
        self.__CsvOption = CsvOption


    @property
    def FilePath(self):
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath


    @property
    def TextIdentifier(self):
        return self.__TextIdentifier

    @TextIdentifier.setter
    def TextIdentifier(self, TextIdentifier: str):
        self.__TextIdentifier = TextIdentifier


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
    def RemoveEmptyRow(self):
        return self.__RemoveEmptyRow

    @RemoveEmptyRow.setter
    def RemoveEmptyRow(self, RemoveEmptyRow: bool):
        self.__RemoveEmptyRow = RemoveEmptyRow


    @property
    def Format(self):
        return self.__Format

    @Format.setter
    def Format(self, Format: str):
        self.__Format = Format


    @property
    def FirstLineCaption(self):
        return self.__FirstLineCaption

    @FirstLineCaption.setter
    def FirstLineCaption(self, FirstLineCaption: bool):
        self.__FirstLineCaption = FirstLineCaption


    @property
    def TextEnclosure(self):
        return self.__TextEnclosure

    @TextEnclosure.setter
    def TextEnclosure(self, TextEnclosure: str):
        self.__TextEnclosure = TextEnclosure


    @property
    def EscapeChar(self):
        return self.__EscapeChar

    @EscapeChar.setter
    def EscapeChar(self, EscapeChar: str):
        self.__EscapeChar = EscapeChar


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
    def FieldSeparatorValue(self):
        return self.__FieldSeparatorValue

    @FieldSeparatorValue.setter
    def FieldSeparatorValue(self, FieldSeparatorValue: str):
        self.__FieldSeparatorValue = FieldSeparatorValue


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
    def UseFooter(self):
        return self.__UseFooter

    @UseFooter.setter
    def UseFooter(self, UseFooter: bool):
        self.__UseFooter = UseFooter


    @property
    def HeaderValue(self):
        return self.__HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue: str):
        self.__HeaderValue = HeaderValue


    @property
    def EscapeType(self):
        return self.__EscapeType

    @EscapeType.setter
    def EscapeType(self, EscapeType: str):
        self.__EscapeType = EscapeType


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


class connection_MetadataTable:

    def __init__(self, sourceName: str, tableType: str, attachedCDC: bool, activatedCDC: bool, connection_MetadataTable18: "connection_SAPFunctionUnit" = None, connection_MetadataTable22: "connection_SAPFunctionUnit" = None, connection_MetadataTable: "connection_MetadataColumn" = None, connection_MetadataTable4: set["connection_MetadataColumn"] = None, connection_MetadataTable7: "connection_Connection" = None):
        self.sourceName = sourceName
        self.tableType = tableType
        self.attachedCDC = attachedCDC
        self.activatedCDC = activatedCDC
        self.connection_MetadataTable18 = connection_MetadataTable18
        self.connection_MetadataTable22 = connection_MetadataTable22
        self.connection_MetadataTable = connection_MetadataTable
        self.connection_MetadataTable4 = connection_MetadataTable4 if connection_MetadataTable4 is not None else set()
        self.connection_MetadataTable7 = connection_MetadataTable7
        
        pass
    @property
    def tableType(self):
        return self.__tableType

    @tableType.setter
    def tableType(self, tableType: str):
        self.__tableType = tableType


    @property
    def activatedCDC(self):
        return self.__activatedCDC

    @activatedCDC.setter
    def activatedCDC(self, activatedCDC: bool):
        self.__activatedCDC = activatedCDC


    @property
    def sourceName(self):
        return self.__sourceName

    @sourceName.setter
    def sourceName(self, sourceName: str):
        self.__sourceName = sourceName


    @property
    def attachedCDC(self):
        return self.__attachedCDC

    @attachedCDC.setter
    def attachedCDC(self, attachedCDC: bool):
        self.__attachedCDC = attachedCDC


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
                    

    @property
    def connection_MetadataTable22(self):
        return self.__connection_MetadataTable22

    @connection_MetadataTable22.setter
    def connection_MetadataTable22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable22", None)
        self.__connection_MetadataTable22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionUnit21"):
                opp_val = getattr(old_value, "connection_SAPFunctionUnit21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionUnit21"):
                opp_val = getattr(value, "connection_SAPFunctionUnit21", None)
                if opp_val is None:
                    setattr(value, "connection_SAPFunctionUnit21", set([self]))
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
    def connection_MetadataTable18(self):
        return self.__connection_MetadataTable18

    @connection_MetadataTable18.setter
    def connection_MetadataTable18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable18", None)
        self.__connection_MetadataTable18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionUnit"):
                opp_val = getattr(old_value, "connection_SAPFunctionUnit", None)
                if opp_val == self:
                    setattr(old_value, "connection_SAPFunctionUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionUnit"):
                opp_val = getattr(value, "connection_SAPFunctionUnit", None)
                setattr(value, "connection_SAPFunctionUnit", self)

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

class connection_MetadataColumn:

    def __init__(self, pattern: str, displayField: str, sourceType: str, defaultValue: str, talendType: str, key: bool, nullable: bool, originalField: str, connection_MetadataColumn: "connection_MetadataTable" = None, connection_MetadataColumn5: "connection_MetadataTable" = None):
        self.pattern = pattern
        self.displayField = displayField
        self.sourceType = sourceType
        self.defaultValue = defaultValue
        self.talendType = talendType
        self.key = key
        self.nullable = nullable
        self.originalField = originalField
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
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


    @property
    def defaultValue(self):
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: bool):
        self.__key = key


    @property
    def originalField(self):
        return self.__originalField

    @originalField.setter
    def originalField(self, originalField: str):
        self.__originalField = originalField


    @property
    def talendType(self):
        return self.__talendType

    @talendType.setter
    def talendType(self, talendType: str):
        self.__talendType = talendType


    @property
    def displayField(self):
        return self.__displayField

    @displayField.setter
    def displayField(self, displayField: str):
        self.__displayField = displayField


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


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

class connection_AbstractMetadataObject(ABC):

    def __init__(self, properties: str, id: str, comment: str, label: str, readOnly: bool, synchronised: bool, divergency: bool):
        self.properties = properties
        self.id = id
        self.comment = comment
        self.label = label
        self.readOnly = readOnly
        self.synchronised = synchronised
        self.divergency = divergency
        
        pass
    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def synchronised(self):
        return self.__synchronised

    @synchronised.setter
    def synchronised(self, synchronised: bool):
        self.__synchronised = synchronised


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def divergency(self):
        return self.__divergency

    @divergency.setter
    def divergency(self, divergency: bool):
        self.__divergency = divergency


class connection_QueriesConnection:

    pass
class connection_Connection:

    def __init__(self, version: str, ContextMode: bool, ContextId: str, Connection: "connection_QueriesConnection" = None, connection_Connection: "connection_Metadata" = None, connection: "connection_QueriesConnection" = None, connection_Connection8: "connection_MetadataTable" = None):
        self.version = version
        self.ContextMode = ContextMode
        self.ContextId = ContextId
        self.Connection = Connection
        self.connection_Connection = connection_Connection
        self.connection = connection
        self.connection_Connection8 = connection_Connection8
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def ContextId(self):
        return self.__ContextId

    @ContextId.setter
    def ContextId(self, ContextId: str):
        self.__ContextId = ContextId


    @property
    def ContextMode(self):
        return self.__ContextMode

    @ContextMode.setter
    def ContextMode(self, ContextMode: bool):
        self.__ContextMode = ContextMode


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

class AbstractMetadataObject:

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
    def Query(self):
        return self.__Query

    @Query.setter
    def Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Query__Query", None)
        self.__Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queries37"):
                opp_val = getattr(old_value, "queries37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queries37"):
                opp_val = getattr(value, "queries37", None)
                if opp_val is None:
                    setattr(value, "queries37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "QueriesConnection39"):
                opp_val = getattr(old_value, "QueriesConnection39", None)
                if opp_val == self:
                    setattr(old_value, "QueriesConnection39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueriesConnection39"):
                opp_val = getattr(value, "QueriesConnection39", None)
                setattr(value, "QueriesConnection39", self)

class connection_SAPFunctionUnit(AbstractMetadataObject):

    def __init__(self, OutputType: str, OutputTableName: str, connection_SAPFunctionUnit: "connection_MetadataTable" = None, Funtions: "connection_SAPConnection" = None, connection_SAPFunctionUnit21: set["connection_MetadataTable"] = None, SAPFunctionUnit: "connection_SAPConnection" = None, functionUnit: "connection_InputSAPFunctionParameterTable" = None, functionUnit16: "connection_OutputSAPFunctionParameterTable" = None, functionUnit24: "connection_SAPTestInputParameterTable" = None, SAPFunctionUnit28: "connection_InputSAPFunctionParameterTable" = None, SAPFunctionUnit30: "connection_OutputSAPFunctionParameterTable" = None, SAPFunctionUnit51: "connection_SAPTestInputParameterTable" = None):
        self.OutputType = OutputType
        self.OutputTableName = OutputTableName
        self.connection_SAPFunctionUnit = connection_SAPFunctionUnit
        self.Funtions = Funtions
        self.connection_SAPFunctionUnit21 = connection_SAPFunctionUnit21 if connection_SAPFunctionUnit21 is not None else set()
        self.SAPFunctionUnit = SAPFunctionUnit
        self.functionUnit = functionUnit
        self.functionUnit16 = functionUnit16
        self.functionUnit24 = functionUnit24
        self.SAPFunctionUnit28 = SAPFunctionUnit28
        self.SAPFunctionUnit30 = SAPFunctionUnit30
        self.SAPFunctionUnit51 = SAPFunctionUnit51
        
        pass
    @property
    def OutputTableName(self):
        return self.__OutputTableName

    @OutputTableName.setter
    def OutputTableName(self, OutputTableName: str):
        self.__OutputTableName = OutputTableName


    @property
    def OutputType(self):
        return self.__OutputType

    @OutputType.setter
    def OutputType(self, OutputType: str):
        self.__OutputType = OutputType


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
            if hasattr(old_value, "connection13"):
                opp_val = getattr(old_value, "connection13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection13"):
                opp_val = getattr(value, "connection13", None)
                if opp_val is None:
                    setattr(value, "connection13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SAPFunctionUnit51(self):
        return self.__SAPFunctionUnit51

    @SAPFunctionUnit51.setter
    def SAPFunctionUnit51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__SAPFunctionUnit51", None)
        self.__SAPFunctionUnit51 = value
        
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
    def functionUnit24(self):
        return self.__functionUnit24

    @functionUnit24.setter
    def functionUnit24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__functionUnit24", None)
        self.__functionUnit24 = value
        
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
    def SAPFunctionUnit30(self):
        return self.__SAPFunctionUnit30

    @SAPFunctionUnit30.setter
    def SAPFunctionUnit30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__SAPFunctionUnit30", None)
        self.__SAPFunctionUnit30 = value
        
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
    def SAPFunctionUnit28(self):
        return self.__SAPFunctionUnit28

    @SAPFunctionUnit28.setter
    def SAPFunctionUnit28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__SAPFunctionUnit28", None)
        self.__SAPFunctionUnit28 = value
        
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
    def connection_SAPFunctionUnit(self):
        return self.__connection_SAPFunctionUnit

    @connection_SAPFunctionUnit.setter
    def connection_SAPFunctionUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__connection_SAPFunctionUnit", None)
        self.__connection_SAPFunctionUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_MetadataTable18"):
                opp_val = getattr(old_value, "connection_MetadataTable18", None)
                if opp_val == self:
                    setattr(old_value, "connection_MetadataTable18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_MetadataTable18"):
                opp_val = getattr(value, "connection_MetadataTable18", None)
                setattr(value, "connection_MetadataTable18", self)

    @property
    def functionUnit16(self):
        return self.__functionUnit16

    @functionUnit16.setter
    def functionUnit16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__functionUnit16", None)
        self.__functionUnit16 = value
        
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
    def Funtions(self):
        return self.__Funtions

    @Funtions.setter
    def Funtions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__Funtions", None)
        self.__Funtions = value
        
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
    def connection_SAPFunctionUnit21(self):
        return self.__connection_SAPFunctionUnit21

    @connection_SAPFunctionUnit21.setter
    def connection_SAPFunctionUnit21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__connection_SAPFunctionUnit21", None)
        self.__connection_SAPFunctionUnit21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_MetadataTable22"):
                    opp_val = getattr(item, "connection_MetadataTable22", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_MetadataTable22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_MetadataTable22"):
                    opp_val = getattr(item, "connection_MetadataTable22", None)
                    
                    setattr(item, "connection_MetadataTable22", self)
                    

    def setDocument(self, connection_document):
        # TODO: Implement setDocument method
        pass

class connection_SAPFunctionParameterTable(AbstractMetadataObject):

    pass
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
    def StructureOrTableName(self):
        return self.__StructureOrTableName

    @StructureOrTableName.setter
    def StructureOrTableName(self, StructureOrTableName: str):
        self.__StructureOrTableName = StructureOrTableName


    @property
    def DataType(self):
        return self.__DataType

    @DataType.setter
    def DataType(self, DataType: str):
        self.__DataType = DataType


    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value


    @property
    def ParameterType(self):
        return self.__ParameterType

    @ParameterType.setter
    def ParameterType(self, ParameterType: str):
        self.__ParameterType = ParameterType


    @property
    def Length(self):
        return self.__Length

    @Length.setter
    def Length(self, Length: str):
        self.__Length = Length


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

class connection_CDCType(AbstractMetadataObject):

    def __init__(self, linkDB: str, journalName: str, connection_CDCType: "connection_CDCConnection" = None, connection_CDCType46: set["connection_SubscriberTable"] = None, connection_CDCType48: "connection_CDCConnection" = None):
        self.linkDB = linkDB
        self.journalName = journalName
        self.connection_CDCType = connection_CDCType
        self.connection_CDCType46 = connection_CDCType46 if connection_CDCType46 is not None else set()
        self.connection_CDCType48 = connection_CDCType48
        
        pass
    @property
    def journalName(self):
        return self.__journalName

    @journalName.setter
    def journalName(self, journalName: str):
        self.__journalName = journalName


    @property
    def linkDB(self):
        return self.__linkDB

    @linkDB.setter
    def linkDB(self, linkDB: str):
        self.__linkDB = linkDB


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
    def connection_CDCType46(self):
        return self.__connection_CDCType46

    @connection_CDCType46.setter
    def connection_CDCType46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_CDCType__connection_CDCType46", None)
        self.__connection_CDCType46 = value if value is not None else set()
        
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
    def connection_CDCType48(self):
        return self.__connection_CDCType48

    @connection_CDCType48.setter
    def connection_CDCType48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_CDCType__connection_CDCType48", None)
        self.__connection_CDCType48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_CDCConnection49"):
                opp_val = getattr(old_value, "connection_CDCConnection49", None)
                if opp_val == self:
                    setattr(old_value, "connection_CDCConnection49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_CDCConnection49"):
                opp_val = getattr(value, "connection_CDCConnection49", None)
                setattr(value, "connection_CDCConnection49", self)

class connection_Metadata(AbstractMetadataObject):

    pass