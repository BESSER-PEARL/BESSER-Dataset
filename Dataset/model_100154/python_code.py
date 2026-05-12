from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FieldSeparator(Enum):
    Tabulation = "Tabulation"
    Semicolon = "Semicolon"
    Comma = "Comma"
    Space = "Space"
    Alt_65 = "Alt_65"
    Custom_ANSI = "Custom_ANSI"
    Custom_UTF8 = "Custom_UTF8"
    Custom_RegExp = "Custom_RegExp"
class DevelopmentStatus(Enum):
    DRAFT = "DRAFT"
    PROD = "PROD"
class MDMConnectionProtocol(Enum):
    HTTP = "HTTP"
class RowSeparator(Enum):
    Custom_String = "Custom_String"
    Standart_EOL = "Standart_EOL"
class FileFormat(Enum):
    UNIX = "UNIX"
    MAC = "MAC"
    WINDOWS = "WINDOWS"
class Escape(Enum):
    Delimited = "Delimited"
    CSV = "CSV"


############################################
# Definition of Classes
############################################

class xml_TdXmlContent:

    pass
class SoftwareSystem:

    pass
class connection_softwaredeployment_TdSoftwareSystem(SoftwareSystem):

    pass
class DataManager:

    pass
class connection_softwaredeployment_TdDataManager(DataManager):

    pass
class Procedure:

    pass
class connection_relational_TdProcedure(Procedure):

    pass
class Trigger:

    pass
class connection_relational_TdTrigger(Trigger):

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
    def unsignedAttribute(self):
        return self.__unsignedAttribute

    @unsignedAttribute.setter
    def unsignedAttribute(self, unsignedAttribute: str):
        self.__unsignedAttribute = unsignedAttribute


    @property
    def localTypeName(self):
        return self.__localTypeName

    @localTypeName.setter
    def localTypeName(self, localTypeName: str):
        self.__localTypeName = localTypeName


    @property
    def autoIncrement(self):
        return self.__autoIncrement

    @autoIncrement.setter
    def autoIncrement(self, autoIncrement: str):
        self.__autoIncrement = autoIncrement


    @property
    def javaDataType(self):
        return self.__javaDataType

    @javaDataType.setter
    def javaDataType(self, javaDataType: int):
        self.__javaDataType = javaDataType


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
    def searchable(self):
        return self.__searchable

    @searchable.setter
    def searchable(self, searchable: str):
        self.__searchable = searchable


class relational_TdSqlDataType:

    pass
class xml_TdXmlSchema:

    pass
class xml_connection_EObject:

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

    def setContentType(self, connection_contentType):
        # TODO: Implement setContentType method
        pass

    def getContentType(self) :
        # TODO: Implement getContentType method
        pass

    def getJavaType(self) :
        # TODO: Implement getJavaType method
        pass

class ElementType:

    pass
class relational_View:

    pass
class connection_xml_TdXmlElementType(ElementType):

    def __init__(self, javaType: str, connection_xml_TdXmlElementType: "xml_connection_EObject" = None, connection_xml_TdXmlElementType83: "xml_TdXmlSchema" = None, connection_xml_TdXmlElementType85: "xml_TdXmlContent" = None):
        self.javaType = javaType
        self.connection_xml_TdXmlElementType = connection_xml_TdXmlElementType
        self.connection_xml_TdXmlElementType83 = connection_xml_TdXmlElementType83
        self.connection_xml_TdXmlElementType85 = connection_xml_TdXmlElementType85
        
        pass
    @property
    def javaType(self):
        return self.__javaType

    @javaType.setter
    def javaType(self, javaType: str):
        self.__javaType = javaType


    @property
    def connection_xml_TdXmlElementType85(self):
        return self.__connection_xml_TdXmlElementType85

    @connection_xml_TdXmlElementType85.setter
    def connection_xml_TdXmlElementType85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_xml_TdXmlElementType__connection_xml_TdXmlElementType85", None)
        self.__connection_xml_TdXmlElementType85 = value
        
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
    def connection_xml_TdXmlElementType83(self):
        return self.__connection_xml_TdXmlElementType83

    @connection_xml_TdXmlElementType83.setter
    def connection_xml_TdXmlElementType83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_xml_TdXmlElementType__connection_xml_TdXmlElementType83", None)
        self.__connection_xml_TdXmlElementType83 = value
        
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

    def getContentType(self) :
        # TODO: Implement getContentType method
        pass

    def setContentType(self, connection_contentType):
        # TODO: Implement setContentType method
        pass

class relational_Table:

    pass
class MetadataTable:

    pass
class connection_relational_TdView(MetadataTable, relational_View):

    pass
class connection_relational_TdTable(MetadataTable, relational_Table):

    pass
class Machine:

    pass
class connection_softwaredeployment_TdMachine(Machine):

    pass
class Package:

    pass
class connection_GenericPackage(Package):

    pass
class connection_HL7FileNode:

    def __init__(self, FilePath: str, Order: int, Attribute: str, DefaultValue: str, RelatedColumn: str, Repeatable: bool, connection_HL7FileNode: "connection_HL7Connection" = None):
        self.FilePath = FilePath
        self.Order = Order
        self.Attribute = Attribute
        self.DefaultValue = DefaultValue
        self.RelatedColumn = RelatedColumn
        self.Repeatable = Repeatable
        self.connection_HL7FileNode = connection_HL7FileNode
        
        pass
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
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, Attribute: str):
        self.__Attribute = Attribute


    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, Order: int):
        self.__Order = Order


    @property
    def FilePath(self):
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath


    @property
    def DefaultValue(self):
        return self.__DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue: str):
        self.__DefaultValue = DefaultValue


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
    def ConceptTarget(self):
        return self.__ConceptTarget

    @ConceptTarget.setter
    def ConceptTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_ConceptTarget__ConceptTarget", None)
        self.__ConceptTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema68"):
                opp_val = getattr(old_value, "schema68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema68"):
                opp_val = getattr(value, "schema68", None)
                if opp_val is None:
                    setattr(value, "schema68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "connection_CDCType61"):
                opp_val = getattr(old_value, "connection_CDCType61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_CDCType61"):
                opp_val = getattr(value, "connection_CDCType61", None)
                if opp_val is None:
                    setattr(value, "connection_CDCType61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_WSDLParameter:

    def __init__(self, Element: str, source: str, Column: str, Expression: str, ParameterInfo: str, ParameterInfoParent: str, connection_WSDLParameter: "connection_WSDLSchemaConnection" = None, connection_WSDLParameter57: "connection_WSDLSchemaConnection" = None):
        self.Element = Element
        self.source = source
        self.Column = Column
        self.Expression = Expression
        self.ParameterInfo = ParameterInfo
        self.ParameterInfoParent = ParameterInfoParent
        self.connection_WSDLParameter = connection_WSDLParameter
        self.connection_WSDLParameter57 = connection_WSDLParameter57
        
        pass
    @property
    def Element(self):
        return self.__Element

    @Element.setter
    def Element(self, Element: str):
        self.__Element = Element


    @property
    def ParameterInfo(self):
        return self.__ParameterInfo

    @ParameterInfo.setter
    def ParameterInfo(self, ParameterInfo: str):
        self.__ParameterInfo = ParameterInfo


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
    def Expression(self):
        return self.__Expression

    @Expression.setter
    def Expression(self, Expression: str):
        self.__Expression = Expression


    @property
    def connection_WSDLParameter57(self):
        return self.__connection_WSDLParameter57

    @connection_WSDLParameter57.setter
    def connection_WSDLParameter57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_WSDLParameter__connection_WSDLParameter57", None)
        self.__connection_WSDLParameter57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_WSDLSchemaConnection56"):
                opp_val = getattr(old_value, "connection_WSDLSchemaConnection56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_WSDLSchemaConnection56"):
                opp_val = getattr(value, "connection_WSDLSchemaConnection56", None)
                if opp_val is None:
                    setattr(value, "connection_WSDLSchemaConnection56", set([self]))
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

class connection_SchemaTarget:

    def __init__(self, RelativeXPathQuery: str, TagName: str, schemaTargets: "connection_XmlXPathLoopDescriptor" = None, SchemaTarget: "connection_XmlXPathLoopDescriptor" = None):
        self.RelativeXPathQuery = RelativeXPathQuery
        self.TagName = TagName
        self.schemaTargets = schemaTargets
        self.SchemaTarget = SchemaTarget
        
        pass
    @property
    def TagName(self):
        return self.__TagName

    @TagName.setter
    def TagName(self, TagName: str):
        self.__TagName = TagName


    @property
    def RelativeXPathQuery(self):
        return self.__RelativeXPathQuery

    @RelativeXPathQuery.setter
    def RelativeXPathQuery(self, RelativeXPathQuery: str):
        self.__RelativeXPathQuery = RelativeXPathQuery


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
            if hasattr(old_value, "XmlXPathLoopDescriptor45"):
                opp_val = getattr(old_value, "XmlXPathLoopDescriptor45", None)
                if opp_val == self:
                    setattr(old_value, "XmlXPathLoopDescriptor45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "XmlXPathLoopDescriptor45"):
                opp_val = getattr(value, "XmlXPathLoopDescriptor45", None)
                setattr(value, "XmlXPathLoopDescriptor45", self)

class connection_XMLFileNode:

    def __init__(self, XMLPath: str, RelatedColumn: str, DefaultValue: str, Attribute: str, Order: int, Type: str, connection_XMLFileNode: "connection_XmlFileConnection" = None, connection_XMLFileNode40: "connection_XmlFileConnection" = None, connection_XMLFileNode43: "connection_XmlFileConnection" = None, connection_XMLFileNode71: "connection_Concept" = None, connection_XMLFileNode74: "connection_Concept" = None, connection_XMLFileNode77: "connection_Concept" = None):
        self.XMLPath = XMLPath
        self.RelatedColumn = RelatedColumn
        self.DefaultValue = DefaultValue
        self.Attribute = Attribute
        self.Order = Order
        self.Type = Type
        self.connection_XMLFileNode = connection_XMLFileNode
        self.connection_XMLFileNode40 = connection_XMLFileNode40
        self.connection_XMLFileNode43 = connection_XMLFileNode43
        self.connection_XMLFileNode71 = connection_XMLFileNode71
        self.connection_XMLFileNode74 = connection_XMLFileNode74
        self.connection_XMLFileNode77 = connection_XMLFileNode77
        
        pass
    @property
    def Order(self):
        return self.__Order

    @Order.setter
    def Order(self, Order: int):
        self.__Order = Order


    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, Attribute: str):
        self.__Attribute = Attribute


    @property
    def RelatedColumn(self):
        return self.__RelatedColumn

    @RelatedColumn.setter
    def RelatedColumn(self, RelatedColumn: str):
        self.__RelatedColumn = RelatedColumn


    @property
    def XMLPath(self):
        return self.__XMLPath

    @XMLPath.setter
    def XMLPath(self, XMLPath: str):
        self.__XMLPath = XMLPath


    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type


    @property
    def DefaultValue(self):
        return self.__DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue: str):
        self.__DefaultValue = DefaultValue


    @property
    def connection_XMLFileNode43(self):
        return self.__connection_XMLFileNode43

    @connection_XMLFileNode43.setter
    def connection_XMLFileNode43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode43", None)
        self.__connection_XMLFileNode43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_XmlFileConnection42"):
                opp_val = getattr(old_value, "connection_XmlFileConnection42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_XmlFileConnection42"):
                opp_val = getattr(value, "connection_XmlFileConnection42", None)
                if opp_val is None:
                    setattr(value, "connection_XmlFileConnection42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode77(self):
        return self.__connection_XMLFileNode77

    @connection_XMLFileNode77.setter
    def connection_XMLFileNode77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode77", None)
        self.__connection_XMLFileNode77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_Concept76"):
                opp_val = getattr(old_value, "connection_Concept76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_Concept76"):
                opp_val = getattr(value, "connection_Concept76", None)
                if opp_val is None:
                    setattr(value, "connection_Concept76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode71(self):
        return self.__connection_XMLFileNode71

    @connection_XMLFileNode71.setter
    def connection_XMLFileNode71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode71", None)
        self.__connection_XMLFileNode71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_Concept70"):
                opp_val = getattr(old_value, "connection_Concept70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_Concept70"):
                opp_val = getattr(value, "connection_Concept70", None)
                if opp_val is None:
                    setattr(value, "connection_Concept70", set([self]))
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
    def connection_XMLFileNode40(self):
        return self.__connection_XMLFileNode40

    @connection_XMLFileNode40.setter
    def connection_XMLFileNode40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode40", None)
        self.__connection_XMLFileNode40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_XmlFileConnection39"):
                opp_val = getattr(old_value, "connection_XmlFileConnection39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_XmlFileConnection39"):
                opp_val = getattr(value, "connection_XmlFileConnection39", None)
                if opp_val is None:
                    setattr(value, "connection_XmlFileConnection39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def connection_XMLFileNode74(self):
        return self.__connection_XMLFileNode74

    @connection_XMLFileNode74.setter
    def connection_XMLFileNode74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XMLFileNode__connection_XMLFileNode74", None)
        self.__connection_XMLFileNode74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_Concept73"):
                opp_val = getattr(old_value, "connection_Concept73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_Concept73"):
                opp_val = getattr(value, "connection_Concept73", None)
                if opp_val is None:
                    setattr(value, "connection_Concept73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_XmlXPathLoopDescriptor:

    def __init__(self, LimitBoucle: str, AbsoluteXPathQuery: str, XmlXPathLoopDescriptor: "connection_XmlFileConnection" = None, XmlXPathLoopDescriptor45: "connection_SchemaTarget" = None, schema: "connection_XmlFileConnection" = None, schema53: set["connection_SchemaTarget"] = None):
        self.LimitBoucle = LimitBoucle
        self.AbsoluteXPathQuery = AbsoluteXPathQuery
        self.XmlXPathLoopDescriptor = XmlXPathLoopDescriptor
        self.XmlXPathLoopDescriptor45 = XmlXPathLoopDescriptor45
        self.schema = schema
        self.schema53 = schema53 if schema53 is not None else set()
        
        pass
    @property
    def AbsoluteXPathQuery(self):
        return self.__AbsoluteXPathQuery

    @AbsoluteXPathQuery.setter
    def AbsoluteXPathQuery(self, AbsoluteXPathQuery: str):
        self.__AbsoluteXPathQuery = AbsoluteXPathQuery


    @property
    def LimitBoucle(self):
        return self.__LimitBoucle

    @LimitBoucle.setter
    def LimitBoucle(self, LimitBoucle: str):
        self.__LimitBoucle = LimitBoucle


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
            if hasattr(old_value, "connection36"):
                opp_val = getattr(old_value, "connection36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection36"):
                opp_val = getattr(value, "connection36", None)
                if opp_val is None:
                    setattr(value, "connection36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def XmlXPathLoopDescriptor45(self):
        return self.__XmlXPathLoopDescriptor45

    @XmlXPathLoopDescriptor45.setter
    def XmlXPathLoopDescriptor45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlXPathLoopDescriptor__XmlXPathLoopDescriptor45", None)
        self.__XmlXPathLoopDescriptor45 = value
        
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
    def schema53(self):
        return self.__schema53

    @schema53.setter
    def schema53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlXPathLoopDescriptor__schema53", None)
        self.__schema53 = value if value is not None else set()
        
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
                    

class SAPFunctionParameterTable:

    pass
class connection_SAPTestInputParameterTable(SAPFunctionParameterTable):

    pass
class connection_OutputSAPFunctionParameterTable(SAPFunctionParameterTable):

    pass
class connection_InputSAPFunctionParameterTable(SAPFunctionParameterTable):

    pass
class connection_CDCConnection:

    pass
class Connection:

    pass
class connection_GenericSchemaConnection(Connection):

    def __init__(self, mappingTypeId: str, mappingTypeUsed: bool):
        self.mappingTypeId = mappingTypeId
        self.mappingTypeUsed = mappingTypeUsed
        
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


class connection_SalesforceSchemaConnection(Connection):

    def __init__(self, webServiceUrl: str, userName: str, password: str, moduleName: str, queryCondition: str, useCustomModuleName: bool, useProxy: bool, proxyHost: str, proxyPort: str, proxyUsername: str, proxyPassword: str, batchSize: str, useHttpProxy: bool, useAlphbet: bool, timeOut: str):
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
        
        pass
    @property
    def batchSize(self):
        return self.__batchSize

    @batchSize.setter
    def batchSize(self, batchSize: str):
        self.__batchSize = batchSize


    @property
    def moduleName(self):
        return self.__moduleName

    @moduleName.setter
    def moduleName(self, moduleName: str):
        self.__moduleName = moduleName


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
    def useProxy(self):
        return self.__useProxy

    @useProxy.setter
    def useProxy(self, useProxy: bool):
        self.__useProxy = useProxy


    @property
    def proxyUsername(self):
        return self.__proxyUsername

    @proxyUsername.setter
    def proxyUsername(self, proxyUsername: str):
        self.__proxyUsername = proxyUsername


    @property
    def useCustomModuleName(self):
        return self.__useCustomModuleName

    @useCustomModuleName.setter
    def useCustomModuleName(self, useCustomModuleName: bool):
        self.__useCustomModuleName = useCustomModuleName


    @property
    def webServiceUrl(self):
        return self.__webServiceUrl

    @webServiceUrl.setter
    def webServiceUrl(self, webServiceUrl: str):
        self.__webServiceUrl = webServiceUrl


    @property
    def useHttpProxy(self):
        return self.__useHttpProxy

    @useHttpProxy.setter
    def useHttpProxy(self, useHttpProxy: bool):
        self.__useHttpProxy = useHttpProxy


    @property
    def timeOut(self):
        return self.__timeOut

    @timeOut.setter
    def timeOut(self, timeOut: str):
        self.__timeOut = timeOut


    @property
    def proxyHost(self):
        return self.__proxyHost

    @proxyHost.setter
    def proxyHost(self, proxyHost: str):
        self.__proxyHost = proxyHost


    @property
    def queryCondition(self):
        return self.__queryCondition

    @queryCondition.setter
    def queryCondition(self, queryCondition: str):
        self.__queryCondition = queryCondition


    @property
    def proxyPassword(self):
        return self.__proxyPassword

    @proxyPassword.setter
    def proxyPassword(self, proxyPassword: str):
        self.__proxyPassword = proxyPassword


    @property
    def userName(self):
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


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
    def LimitEntry(self):
        return self.__LimitEntry

    @LimitEntry.setter
    def LimitEntry(self, LimitEntry: int):
        self.__LimitEntry = LimitEntry


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
    def FilePath(self):
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath


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
    def BindPassword(self):
        return self.__BindPassword

    @BindPassword.setter
    def BindPassword(self, BindPassword: str):
        self.__BindPassword = BindPassword


    @property
    def ReturnAttributes(self):
        return self.__ReturnAttributes

    @ReturnAttributes.setter
    def ReturnAttributes(self, ReturnAttributes: str):
        self.__ReturnAttributes = ReturnAttributes


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


    @property
    def Referrals(self):
        return self.__Referrals

    @Referrals.setter
    def Referrals(self, Referrals: str):
        self.__Referrals = Referrals


    @property
    def Separator(self):
        return self.__Separator

    @Separator.setter
    def Separator(self, Separator: str):
        self.__Separator = Separator


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
    def Protocol(self):
        return self.__Protocol

    @Protocol.setter
    def Protocol(self, Protocol: str):
        self.__Protocol = Protocol


    @property
    def Aliases(self):
        return self.__Aliases

    @Aliases.setter
    def Aliases(self, Aliases: str):
        self.__Aliases = Aliases


    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value


    @property
    def UseAuthen(self):
        return self.__UseAuthen

    @UseAuthen.setter
    def UseAuthen(self, UseAuthen: bool):
        self.__UseAuthen = UseAuthen


    @property
    def EncryptionMethodName(self):
        return self.__EncryptionMethodName

    @EncryptionMethodName.setter
    def EncryptionMethodName(self, EncryptionMethodName: str):
        self.__EncryptionMethodName = EncryptionMethodName


    @property
    def UseLimit(self):
        return self.__UseLimit

    @UseLimit.setter
    def UseLimit(self, UseLimit: bool):
        self.__UseLimit = UseLimit


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
    def TimeOutLimit(self):
        return self.__TimeOutLimit

    @TimeOutLimit.setter
    def TimeOutLimit(self, TimeOutLimit: str):
        self.__TimeOutLimit = TimeOutLimit


    @property
    def Filter(self):
        return self.__Filter

    @Filter.setter
    def Filter(self, Filter: str):
        self.__Filter = Filter


    @property
    def SavePassword(self):
        return self.__SavePassword

    @SavePassword.setter
    def SavePassword(self, SavePassword: bool):
        self.__SavePassword = SavePassword


    @property
    def StorePath(self):
        return self.__StorePath

    @StorePath.setter
    def StorePath(self, StorePath: str):
        self.__StorePath = StorePath


    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, Port: str):
        self.__Port = Port


class connection_WSDLSchemaConnection(Connection):

    def __init__(self, WSDL: str, needAuth: bool, methodName: str, parameters: str, UserName: str, Password: str, useProxy: bool, proxyHost: str, proxyPort: str, proxyUser: str, Encoding: str, timeOut: int, isInputModel: bool, serverNameSpace: str, serverName: str, portNameSpace: str, portName: str, proxyPassword: str, Value: str, EndpointURI: str, connection_WSDLSchemaConnection: set["connection_WSDLParameter"] = None, connection_WSDLSchemaConnection56: set["connection_WSDLParameter"] = None):
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
        self.Encoding = Encoding
        self.timeOut = timeOut
        self.isInputModel = isInputModel
        self.serverNameSpace = serverNameSpace
        self.serverName = serverName
        self.portNameSpace = portNameSpace
        self.portName = portName
        self.proxyPassword = proxyPassword
        self.Value = Value
        self.EndpointURI = EndpointURI
        self.connection_WSDLSchemaConnection = connection_WSDLSchemaConnection if connection_WSDLSchemaConnection is not None else set()
        self.connection_WSDLSchemaConnection56 = connection_WSDLSchemaConnection56 if connection_WSDLSchemaConnection56 is not None else set()
        
        pass
    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def proxyPassword(self):
        return self.__proxyPassword

    @proxyPassword.setter
    def proxyPassword(self, proxyPassword: str):
        self.__proxyPassword = proxyPassword


    @property
    def portName(self):
        return self.__portName

    @portName.setter
    def portName(self, portName: str):
        self.__portName = portName


    @property
    def Encoding(self):
        return self.__Encoding

    @Encoding.setter
    def Encoding(self, Encoding: str):
        self.__Encoding = Encoding


    @property
    def proxyUser(self):
        return self.__proxyUser

    @proxyUser.setter
    def proxyUser(self, proxyUser: str):
        self.__proxyUser = proxyUser


    @property
    def needAuth(self):
        return self.__needAuth

    @needAuth.setter
    def needAuth(self, needAuth: bool):
        self.__needAuth = needAuth


    @property
    def serverName(self):
        return self.__serverName

    @serverName.setter
    def serverName(self, serverName: str):
        self.__serverName = serverName


    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters


    @property
    def timeOut(self):
        return self.__timeOut

    @timeOut.setter
    def timeOut(self, timeOut: int):
        self.__timeOut = timeOut


    @property
    def EndpointURI(self):
        return self.__EndpointURI

    @EndpointURI.setter
    def EndpointURI(self, EndpointURI: str):
        self.__EndpointURI = EndpointURI


    @property
    def portNameSpace(self):
        return self.__portNameSpace

    @portNameSpace.setter
    def portNameSpace(self, portNameSpace: str):
        self.__portNameSpace = portNameSpace


    @property
    def isInputModel(self):
        return self.__isInputModel

    @isInputModel.setter
    def isInputModel(self, isInputModel: bool):
        self.__isInputModel = isInputModel


    @property
    def WSDL(self):
        return self.__WSDL

    @WSDL.setter
    def WSDL(self, WSDL: str):
        self.__WSDL = WSDL


    @property
    def proxyHost(self):
        return self.__proxyHost

    @proxyHost.setter
    def proxyHost(self, proxyHost: str):
        self.__proxyHost = proxyHost


    @property
    def serverNameSpace(self):
        return self.__serverNameSpace

    @serverNameSpace.setter
    def serverNameSpace(self, serverNameSpace: str):
        self.__serverNameSpace = serverNameSpace


    @property
    def useProxy(self):
        return self.__useProxy

    @useProxy.setter
    def useProxy(self, useProxy: bool):
        self.__useProxy = useProxy


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
    def UserName(self):
        return self.__UserName

    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName


    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value


    @property
    def connection_WSDLSchemaConnection56(self):
        return self.__connection_WSDLSchemaConnection56

    @connection_WSDLSchemaConnection56.setter
    def connection_WSDLSchemaConnection56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_WSDLSchemaConnection__connection_WSDLSchemaConnection56", None)
        self.__connection_WSDLSchemaConnection56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_WSDLParameter57"):
                    opp_val = getattr(item, "connection_WSDLParameter57", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_WSDLParameter57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_WSDLParameter57"):
                    opp_val = getattr(item, "connection_WSDLParameter57", None)
                    
                    setattr(item, "connection_WSDLParameter57", self)
                    

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
                    

class connection_SAPConnection(Connection):

    def __init__(self, Host: str, Username: str, Password: str, Client: str, SystemNumber: str, Language: str, currentFucntion: str, connection13: set["connection_SAPFunctionUnit"] = None, connection15: set["connection_SAPIDocUnit"] = None, SAPConnection: "connection_SAPFunctionUnit" = None, SAPConnection28: "connection_SAPIDocUnit" = None):
        self.Host = Host
        self.Username = Username
        self.Password = Password
        self.Client = Client
        self.SystemNumber = SystemNumber
        self.Language = Language
        self.currentFucntion = currentFucntion
        self.connection13 = connection13 if connection13 is not None else set()
        self.connection15 = connection15 if connection15 is not None else set()
        self.SAPConnection = SAPConnection
        self.SAPConnection28 = SAPConnection28
        
        pass
    @property
    def Language(self):
        return self.__Language

    @Language.setter
    def Language(self, Language: str):
        self.__Language = Language


    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username


    @property
    def Client(self):
        return self.__Client

    @Client.setter
    def Client(self, Client: str):
        self.__Client = Client


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
    def SAPConnection28(self):
        return self.__SAPConnection28

    @SAPConnection28.setter
    def SAPConnection28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__SAPConnection28", None)
        self.__SAPConnection28 = value
        
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
    def connection15(self):
        return self.__connection15

    @connection15.setter
    def connection15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPConnection__connection15", None)
        self.__connection15 = value if value is not None else set()
        
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
                    

class connection_FTPConnection(Connection):

    def __init__(self, Host: str, Port: str, Username: str, Password: str, Mode: str, Ecoding: str, SFTP: bool, FTPS: bool, Method: str, KeystoreFile: str, KeystorePassword: str, Usesocks: bool, CustomEncode: str, Proxyhost: str, Proxyport: str, Proxyuser: str, Proxypassword: str):
        self.Host = Host
        self.Port = Port
        self.Username = Username
        self.Password = Password
        self.Mode = Mode
        self.Ecoding = Ecoding
        self.SFTP = SFTP
        self.FTPS = FTPS
        self.Method = Method
        self.KeystoreFile = KeystoreFile
        self.KeystorePassword = KeystorePassword
        self.Usesocks = Usesocks
        self.CustomEncode = CustomEncode
        self.Proxyhost = Proxyhost
        self.Proxyport = Proxyport
        self.Proxyuser = Proxyuser
        self.Proxypassword = Proxypassword
        
        pass
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
    def Proxyport(self):
        return self.__Proxyport

    @Proxyport.setter
    def Proxyport(self, Proxyport: str):
        self.__Proxyport = Proxyport


    @property
    def Usesocks(self):
        return self.__Usesocks

    @Usesocks.setter
    def Usesocks(self, Usesocks: bool):
        self.__Usesocks = Usesocks


    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username


    @property
    def KeystoreFile(self):
        return self.__KeystoreFile

    @KeystoreFile.setter
    def KeystoreFile(self, KeystoreFile: str):
        self.__KeystoreFile = KeystoreFile


    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, Port: str):
        self.__Port = Port


    @property
    def Ecoding(self):
        return self.__Ecoding

    @Ecoding.setter
    def Ecoding(self, Ecoding: str):
        self.__Ecoding = Ecoding


    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, Method: str):
        self.__Method = Method


    @property
    def FTPS(self):
        return self.__FTPS

    @FTPS.setter
    def FTPS(self, FTPS: bool):
        self.__FTPS = FTPS


    @property
    def Proxypassword(self):
        return self.__Proxypassword

    @Proxypassword.setter
    def Proxypassword(self, Proxypassword: str):
        self.__Proxypassword = Proxypassword


    @property
    def KeystorePassword(self):
        return self.__KeystorePassword

    @KeystorePassword.setter
    def KeystorePassword(self, KeystorePassword: str):
        self.__KeystorePassword = KeystorePassword


    @property
    def CustomEncode(self):
        return self.__CustomEncode

    @CustomEncode.setter
    def CustomEncode(self, CustomEncode: str):
        self.__CustomEncode = CustomEncode


    @property
    def SFTP(self):
        return self.__SFTP

    @SFTP.setter
    def SFTP(self, SFTP: bool):
        self.__SFTP = SFTP


    @property
    def Mode(self):
        return self.__Mode

    @Mode.setter
    def Mode(self, Mode: str):
        self.__Mode = Mode


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


class connection_HeaderFooterConnection(Connection):

    def __init__(self, isHeader: bool, imports: str, mainCode: str, libraries: str):
        self.isHeader = isHeader
        self.imports = imports
        self.mainCode = mainCode
        self.libraries = libraries
        
        pass
    @property
    def libraries(self):
        return self.__libraries

    @libraries.setter
    def libraries(self, libraries: str):
        self.__libraries = libraries


    @property
    def mainCode(self):
        return self.__mainCode

    @mainCode.setter
    def mainCode(self, mainCode: str):
        self.__mainCode = mainCode


    @property
    def isHeader(self):
        return self.__isHeader

    @isHeader.setter
    def isHeader(self, isHeader: bool):
        self.__isHeader = isHeader


    @property
    def imports(self):
        return self.__imports

    @imports.setter
    def imports(self, imports: str):
        self.__imports = imports


class connection_DatabaseConnection(Connection):

    def __init__(self, DatabaseType: str, DriverJarPath: str, DriverClass: str, URL: str, dbVersionString: str, Port: str, Username: str, Password: str, FileFieldName: str, SID: str, SqlSynthax: str, StringQuote: str, NullChar: str, DbmsId: str, ProductId: str, DBRootPath: str, AdditionalParams: str, StandardSQL: bool, SystemSQL: bool, cdcTypeMode: str, SQLMode: bool, UiSchema: str, ServerName: str, DatasourceName: str, connection11: "connection_CDCConnection" = None, DatabaseConnection: "connection_CDCConnection" = None):
        self.DatabaseType = DatabaseType
        self.DriverJarPath = DriverJarPath
        self.DriverClass = DriverClass
        self.URL = URL
        self.dbVersionString = dbVersionString
        self.Port = Port
        self.Username = Username
        self.Password = Password
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
        self.SystemSQL = SystemSQL
        self.cdcTypeMode = cdcTypeMode
        self.SQLMode = SQLMode
        self.UiSchema = UiSchema
        self.ServerName = ServerName
        self.DatasourceName = DatasourceName
        self.connection11 = connection11
        self.DatabaseConnection = DatabaseConnection
        
        pass
    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, Port: str):
        self.__Port = Port


    @property
    def ServerName(self):
        return self.__ServerName

    @ServerName.setter
    def ServerName(self, ServerName: str):
        self.__ServerName = ServerName


    @property
    def UiSchema(self):
        return self.__UiSchema

    @UiSchema.setter
    def UiSchema(self, UiSchema: str):
        self.__UiSchema = UiSchema


    @property
    def DatabaseType(self):
        return self.__DatabaseType

    @DatabaseType.setter
    def DatabaseType(self, DatabaseType: str):
        self.__DatabaseType = DatabaseType


    @property
    def DriverJarPath(self):
        return self.__DriverJarPath

    @DriverJarPath.setter
    def DriverJarPath(self, DriverJarPath: str):
        self.__DriverJarPath = DriverJarPath


    @property
    def cdcTypeMode(self):
        return self.__cdcTypeMode

    @cdcTypeMode.setter
    def cdcTypeMode(self, cdcTypeMode: str):
        self.__cdcTypeMode = cdcTypeMode


    @property
    def AdditionalParams(self):
        return self.__AdditionalParams

    @AdditionalParams.setter
    def AdditionalParams(self, AdditionalParams: str):
        self.__AdditionalParams = AdditionalParams


    @property
    def Username(self):
        return self.__Username

    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username


    @property
    def dbVersionString(self):
        return self.__dbVersionString

    @dbVersionString.setter
    def dbVersionString(self, dbVersionString: str):
        self.__dbVersionString = dbVersionString


    @property
    def FileFieldName(self):
        return self.__FileFieldName

    @FileFieldName.setter
    def FileFieldName(self, FileFieldName: str):
        self.__FileFieldName = FileFieldName


    @property
    def URL(self):
        return self.__URL

    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL


    @property
    def DBRootPath(self):
        return self.__DBRootPath

    @DBRootPath.setter
    def DBRootPath(self, DBRootPath: str):
        self.__DBRootPath = DBRootPath


    @property
    def ProductId(self):
        return self.__ProductId

    @ProductId.setter
    def ProductId(self, ProductId: str):
        self.__ProductId = ProductId


    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def SqlSynthax(self):
        return self.__SqlSynthax

    @SqlSynthax.setter
    def SqlSynthax(self, SqlSynthax: str):
        self.__SqlSynthax = SqlSynthax


    @property
    def StandardSQL(self):
        return self.__StandardSQL

    @StandardSQL.setter
    def StandardSQL(self, StandardSQL: bool):
        self.__StandardSQL = StandardSQL


    @property
    def DriverClass(self):
        return self.__DriverClass

    @DriverClass.setter
    def DriverClass(self, DriverClass: str):
        self.__DriverClass = DriverClass


    @property
    def DbmsId(self):
        return self.__DbmsId

    @DbmsId.setter
    def DbmsId(self, DbmsId: str):
        self.__DbmsId = DbmsId


    @property
    def SystemSQL(self):
        return self.__SystemSQL

    @SystemSQL.setter
    def SystemSQL(self, SystemSQL: bool):
        self.__SystemSQL = SystemSQL


    @property
    def StringQuote(self):
        return self.__StringQuote

    @StringQuote.setter
    def StringQuote(self, StringQuote: str):
        self.__StringQuote = StringQuote


    @property
    def NullChar(self):
        return self.__NullChar

    @NullChar.setter
    def NullChar(self, NullChar: str):
        self.__NullChar = NullChar


    @property
    def SQLMode(self):
        return self.__SQLMode

    @SQLMode.setter
    def SQLMode(self, SQLMode: bool):
        self.__SQLMode = SQLMode


    @property
    def DatasourceName(self):
        return self.__DatasourceName

    @DatasourceName.setter
    def DatasourceName(self, DatasourceName: str):
        self.__DatasourceName = DatasourceName


    @property
    def SID(self):
        return self.__SID

    @SID.setter
    def SID(self, SID: str):
        self.__SID = SID


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

class connection_XmlFileConnection(Connection):

    def __init__(self, XsdFilePath: str, XmlFilePath: str, Guess: bool, MaskXPattern: str, Encoding: str, inputModel: bool, outputFilePath: str, connection36: set["connection_XmlXPathLoopDescriptor"] = None, connection_XmlFileConnection: set["connection_XMLFileNode"] = None, connection_XmlFileConnection39: set["connection_XMLFileNode"] = None, connection_XmlFileConnection42: set["connection_XMLFileNode"] = None, XmlFileConnection: "connection_XmlXPathLoopDescriptor" = None):
        self.XsdFilePath = XsdFilePath
        self.XmlFilePath = XmlFilePath
        self.Guess = Guess
        self.MaskXPattern = MaskXPattern
        self.Encoding = Encoding
        self.inputModel = inputModel
        self.outputFilePath = outputFilePath
        self.connection36 = connection36 if connection36 is not None else set()
        self.connection_XmlFileConnection = connection_XmlFileConnection if connection_XmlFileConnection is not None else set()
        self.connection_XmlFileConnection39 = connection_XmlFileConnection39 if connection_XmlFileConnection39 is not None else set()
        self.connection_XmlFileConnection42 = connection_XmlFileConnection42 if connection_XmlFileConnection42 is not None else set()
        self.XmlFileConnection = XmlFileConnection
        
        pass
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
    def outputFilePath(self):
        return self.__outputFilePath

    @outputFilePath.setter
    def outputFilePath(self, outputFilePath: str):
        self.__outputFilePath = outputFilePath


    @property
    def XmlFilePath(self):
        return self.__XmlFilePath

    @XmlFilePath.setter
    def XmlFilePath(self, XmlFilePath: str):
        self.__XmlFilePath = XmlFilePath


    @property
    def inputModel(self):
        return self.__inputModel

    @inputModel.setter
    def inputModel(self, inputModel: bool):
        self.__inputModel = inputModel


    @property
    def MaskXPattern(self):
        return self.__MaskXPattern

    @MaskXPattern.setter
    def MaskXPattern(self, MaskXPattern: str):
        self.__MaskXPattern = MaskXPattern


    @property
    def XsdFilePath(self):
        return self.__XsdFilePath

    @XsdFilePath.setter
    def XsdFilePath(self, XsdFilePath: str):
        self.__XsdFilePath = XsdFilePath


    @property
    def connection36(self):
        return self.__connection36

    @connection36.setter
    def connection36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlFileConnection__connection36", None)
        self.__connection36 = value if value is not None else set()
        
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
                    

    @property
    def connection_XmlFileConnection39(self):
        return self.__connection_XmlFileConnection39

    @connection_XmlFileConnection39.setter
    def connection_XmlFileConnection39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlFileConnection__connection_XmlFileConnection39", None)
        self.__connection_XmlFileConnection39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode40"):
                    opp_val = getattr(item, "connection_XMLFileNode40", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode40"):
                    opp_val = getattr(item, "connection_XMLFileNode40", None)
                    
                    setattr(item, "connection_XMLFileNode40", self)
                    

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
    def connection_XmlFileConnection42(self):
        return self.__connection_XmlFileConnection42

    @connection_XmlFileConnection42.setter
    def connection_XmlFileConnection42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_XmlFileConnection__connection_XmlFileConnection42", None)
        self.__connection_XmlFileConnection42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode43"):
                    opp_val = getattr(item, "connection_XMLFileNode43", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode43"):
                    opp_val = getattr(item, "connection_XMLFileNode43", None)
                    
                    setattr(item, "connection_XMLFileNode43", self)
                    

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

class connection_FileConnection(Connection):

    def __init__(self, FilePath: str, Format: str, Encoding: str, FieldSeparatorValue: str, RowSeparatorType: str, RowSeparatorValue: str, TextIdentifier: str, UseHeader: bool, HeaderValue: str, UseFooter: bool, FooterValue: str, UseLimit: bool, LimitValue: str, FirstLineCaption: bool, RemoveEmptyRow: bool, EscapeType: str, EscapeChar: str, TextEnclosure: str, CsvOption: bool, Server: str):
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
        self.Server = Server
        
        pass
    @property
    def FilePath(self):
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath


    @property
    def EscapeType(self):
        return self.__EscapeType

    @EscapeType.setter
    def EscapeType(self, EscapeType: str):
        self.__EscapeType = EscapeType


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
    def HeaderValue(self):
        return self.__HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue: str):
        self.__HeaderValue = HeaderValue


    @property
    def UseLimit(self):
        return self.__UseLimit

    @UseLimit.setter
    def UseLimit(self, UseLimit: bool):
        self.__UseLimit = UseLimit


    @property
    def CsvOption(self):
        return self.__CsvOption

    @CsvOption.setter
    def CsvOption(self, CsvOption: bool):
        self.__CsvOption = CsvOption


    @property
    def RowSeparatorType(self):
        return self.__RowSeparatorType

    @RowSeparatorType.setter
    def RowSeparatorType(self, RowSeparatorType: str):
        self.__RowSeparatorType = RowSeparatorType


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
    def Format(self):
        return self.__Format

    @Format.setter
    def Format(self, Format: str):
        self.__Format = Format


    @property
    def LimitValue(self):
        return self.__LimitValue

    @LimitValue.setter
    def LimitValue(self, LimitValue: str):
        self.__LimitValue = LimitValue


    @property
    def Encoding(self):
        return self.__Encoding

    @Encoding.setter
    def Encoding(self, Encoding: str):
        self.__Encoding = Encoding


    @property
    def FooterValue(self):
        return self.__FooterValue

    @FooterValue.setter
    def FooterValue(self, FooterValue: str):
        self.__FooterValue = FooterValue


    @property
    def UseHeader(self):
        return self.__UseHeader

    @UseHeader.setter
    def UseHeader(self, UseHeader: bool):
        self.__UseHeader = UseHeader


    @property
    def UseFooter(self):
        return self.__UseFooter

    @UseFooter.setter
    def UseFooter(self, UseFooter: bool):
        self.__UseFooter = UseFooter


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


class connection_Concept(TdTable):

    def __init__(self, LoopExpression: str, LoopLimit: str, inputModel: bool, connection_Concept: "connection_MDMConnection" = None, schema68: set["connection_ConceptTarget"] = None, connection_Concept70: set["connection_XMLFileNode"] = None, connection_Concept73: set["connection_XMLFileNode"] = None, connection_Concept76: set["connection_XMLFileNode"] = None, Concept: "connection_ConceptTarget" = None):
        self.LoopExpression = LoopExpression
        self.LoopLimit = LoopLimit
        self.inputModel = inputModel
        self.connection_Concept = connection_Concept
        self.schema68 = schema68 if schema68 is not None else set()
        self.connection_Concept70 = connection_Concept70 if connection_Concept70 is not None else set()
        self.connection_Concept73 = connection_Concept73 if connection_Concept73 is not None else set()
        self.connection_Concept76 = connection_Concept76 if connection_Concept76 is not None else set()
        self.Concept = Concept
        
        pass
    @property
    def LoopExpression(self):
        return self.__LoopExpression

    @LoopExpression.setter
    def LoopExpression(self, LoopExpression: str):
        self.__LoopExpression = LoopExpression


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
    def connection_Concept73(self):
        return self.__connection_Concept73

    @connection_Concept73.setter
    def connection_Concept73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__connection_Concept73", None)
        self.__connection_Concept73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode74"):
                    opp_val = getattr(item, "connection_XMLFileNode74", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode74"):
                    opp_val = getattr(item, "connection_XMLFileNode74", None)
                    
                    setattr(item, "connection_XMLFileNode74", self)
                    

    @property
    def connection_Concept70(self):
        return self.__connection_Concept70

    @connection_Concept70.setter
    def connection_Concept70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__connection_Concept70", None)
        self.__connection_Concept70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode71"):
                    opp_val = getattr(item, "connection_XMLFileNode71", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode71"):
                    opp_val = getattr(item, "connection_XMLFileNode71", None)
                    
                    setattr(item, "connection_XMLFileNode71", self)
                    

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

    @property
    def schema68(self):
        return self.__schema68

    @schema68.setter
    def schema68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__schema68", None)
        self.__schema68 = value if value is not None else set()
        
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
    def connection_Concept76(self):
        return self.__connection_Concept76

    @connection_Concept76.setter
    def connection_Concept76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_Concept__connection_Concept76", None)
        self.__connection_Concept76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_XMLFileNode77"):
                    opp_val = getattr(item, "connection_XMLFileNode77", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_XMLFileNode77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_XMLFileNode77"):
                    opp_val = getattr(item, "connection_XMLFileNode77", None)
                    
                    setattr(item, "connection_XMLFileNode77", self)
                    

class connection_MDMConnection(Connection):

    def __init__(self, Username: str, Password: str, Port: str, Server: str, Universe: str, Datamodel: str, Datacluster: str, context: str, protocol: str, connection_MDMConnection: set["connection_Concept"] = None):
        self.Username = Username
        self.Password = Password
        self.Port = Port
        self.Server = Server
        self.Universe = Universe
        self.Datamodel = Datamodel
        self.Datacluster = Datacluster
        self.context = context
        self.protocol = protocol
        self.connection_MDMConnection = connection_MDMConnection if connection_MDMConnection is not None else set()
        
        pass
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
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password


    @property
    def Datamodel(self):
        return self.__Datamodel

    @Datamodel.setter
    def Datamodel(self, Datamodel: str):
        self.__Datamodel = Datamodel


    @property
    def Universe(self):
        return self.__Universe

    @Universe.setter
    def Universe(self, Universe: str):
        self.__Universe = Universe


    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context


    @property
    def Port(self):
        return self.__Port

    @Port.setter
    def Port(self, Port: str):
        self.__Port = Port


    @property
    def Server(self):
        return self.__Server

    @Server.setter
    def Server(self, Server: str):
        self.__Server = Server


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


class connection_PositionalFileConnection(FileConnection):

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


class connection_HL7Connection(FileConnection):

    def __init__(self, StartChar: str, EndChar: str, outputFilePath: str, connection_HL7Connection: set["connection_HL7FileNode"] = None):
        self.StartChar = StartChar
        self.EndChar = EndChar
        self.outputFilePath = outputFilePath
        self.connection_HL7Connection = connection_HL7Connection if connection_HL7Connection is not None else set()
        
        pass
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
    def EndChar(self):
        return self.__EndChar

    @EndChar.setter
    def EndChar(self, EndChar: str):
        self.__EndChar = EndChar


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
    def lastColumn(self):
        return self.__lastColumn

    @lastColumn.setter
    def lastColumn(self, lastColumn: str):
        self.__lastColumn = lastColumn


    @property
    def sheetList(self):
        return self.__sheetList

    @sheetList.setter
    def sheetList(self, sheetList: str):
        self.__sheetList = sheetList


    @property
    def selectAllSheets(self):
        return self.__selectAllSheets

    @selectAllSheets.setter
    def selectAllSheets(self, selectAllSheets: bool):
        self.__selectAllSheets = selectAllSheets


    @property
    def sheetColumns(self):
        return self.__sheetColumns

    @sheetColumns.setter
    def sheetColumns(self, sheetColumns: str):
        self.__sheetColumns = sheetColumns


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
    def decimalSeparator(self):
        return self.__decimalSeparator

    @decimalSeparator.setter
    def decimalSeparator(self, decimalSeparator: str):
        self.__decimalSeparator = decimalSeparator


    @property
    def thousandSeparator(self):
        return self.__thousandSeparator

    @thousandSeparator.setter
    def thousandSeparator(self, thousandSeparator: str):
        self.__thousandSeparator = thousandSeparator


    @property
    def SheetName(self):
        return self.__SheetName

    @SheetName.setter
    def SheetName(self, SheetName: str):
        self.__SheetName = SheetName


class connection_DelimitedFileConnection(FileConnection):

    def __init__(self, FieldSeparatorType: str, splitRecord: bool):
        self.FieldSeparatorType = FieldSeparatorType
        self.splitRecord = splitRecord
        
        pass
    @property
    def FieldSeparatorType(self):
        return self.__FieldSeparatorType

    @FieldSeparatorType.setter
    def FieldSeparatorType(self, FieldSeparatorType: str):
        self.__FieldSeparatorType = FieldSeparatorType


    @property
    def splitRecord(self):
        return self.__splitRecord

    @splitRecord.setter
    def splitRecord(self, splitRecord: bool):
        self.__splitRecord = splitRecord


class core_Class:

    pass
class ModelElement:

    pass
class connection_AbstractMetadataObject(ModelElement):

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
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def divergency(self):
        return self.__divergency

    @divergency.setter
    def divergency(self, divergency: bool):
        self.__divergency = divergency


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
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, properties: str):
        self.__properties = properties


class record_Field:

    pass
class connection_QueriesConnection:

    pass
class softwaredeployment_DataProvider:

    pass
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
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def contextMode(self):
        return self.__contextMode

    @contextMode.setter
    def contextMode(self, contextMode: bool):
        self.__contextMode = contextMode


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
            if hasattr(old_value, "QueriesConnection50"):
                opp_val = getattr(old_value, "QueriesConnection50", None)
                if opp_val == self:
                    setattr(old_value, "QueriesConnection50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QueriesConnection50"):
                opp_val = getattr(value, "QueriesConnection50", None)
                setattr(value, "QueriesConnection50", self)

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
            if hasattr(old_value, "queries48"):
                opp_val = getattr(old_value, "queries48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queries48"):
                opp_val = getattr(value, "queries48", None)
                if opp_val is None:
                    setattr(value, "queries48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class connection_MetadataTable(AbstractMetadataObject, core_Class):

    def __init__(self, sourceName: str, tableType: str, attachedCDC: bool, activatedCDC: bool, connection_MetadataTable7: "connection_Connection" = None, connection_MetadataTable20: "connection_SAPFunctionUnit" = None, connection_MetadataTable24: "connection_SAPFunctionUnit" = None, connection_MetadataTable: "connection_MetadataColumn" = None, connection_MetadataTable4: set["connection_MetadataColumn"] = None):
        self.sourceName = sourceName
        self.tableType = tableType
        self.attachedCDC = attachedCDC
        self.activatedCDC = activatedCDC
        self.connection_MetadataTable7 = connection_MetadataTable7
        self.connection_MetadataTable20 = connection_MetadataTable20
        self.connection_MetadataTable24 = connection_MetadataTable24
        self.connection_MetadataTable = connection_MetadataTable
        self.connection_MetadataTable4 = connection_MetadataTable4 if connection_MetadataTable4 is not None else set()
        
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
    def connection_MetadataTable20(self):
        return self.__connection_MetadataTable20

    @connection_MetadataTable20.setter
    def connection_MetadataTable20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable20", None)
        self.__connection_MetadataTable20 = value
        
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

    @property
    def connection_MetadataTable24(self):
        return self.__connection_MetadataTable24

    @connection_MetadataTable24.setter
    def connection_MetadataTable24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_MetadataTable__connection_MetadataTable24", None)
        self.__connection_MetadataTable24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_SAPFunctionUnit23"):
                opp_val = getattr(old_value, "connection_SAPFunctionUnit23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_SAPFunctionUnit23"):
                opp_val = getattr(value, "connection_SAPFunctionUnit23", None)
                if opp_val is None:
                    setattr(value, "connection_SAPFunctionUnit23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def Length(self):
        return self.__Length

    @Length.setter
    def Length(self, Length: str):
        self.__Length = Length


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
    def DataType(self):
        return self.__DataType

    @DataType.setter
    def DataType(self, DataType: str):
        self.__DataType = DataType


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

    def setDescription(self, connection_description):
        # TODO: Implement setDescription method
        pass

class connection_SAPFunctionParameterTable(AbstractMetadataObject):

    pass
class connection_Connection(softwaredeployment_DataProvider, AbstractMetadataObject):

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
    def ContextId(self):
        return self.__ContextId

    @ContextId.setter
    def ContextId(self, ContextId: str):
        self.__ContextId = ContextId


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

class connection_MetadataColumn(record_Field, AbstractMetadataObject):

    def __init__(self, sourceType: str, defaultValue: str, talendType: str, key: bool, nullable: bool, displayField: str, originalField: str, pattern: str, connection_MetadataColumn: "connection_MetadataTable" = None, connection_MetadataColumn5: "connection_MetadataTable" = None):
        self.sourceType = sourceType
        self.defaultValue = defaultValue
        self.talendType = talendType
        self.key = key
        self.nullable = nullable
        self.displayField = displayField
        self.originalField = originalField
        self.pattern = pattern
        self.connection_MetadataColumn = connection_MetadataColumn
        self.connection_MetadataColumn5 = connection_MetadataColumn5
        
        pass
    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: bool):
        self.__nullable = nullable


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
    def sourceType(self):
        return self.__sourceType

    @sourceType.setter
    def sourceType(self, sourceType: str):
        self.__sourceType = sourceType


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
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: bool):
        self.__key = key


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

class connection_SAPFunctionUnit(AbstractMetadataObject):

    def __init__(self, OutputTableName: str, OutputType: str, SAPFunctionUnit: "connection_SAPConnection" = None, functionUnit: "connection_InputSAPFunctionParameterTable" = None, functionUnit18: "connection_OutputSAPFunctionParameterTable" = None, connection_SAPFunctionUnit: "connection_MetadataTable" = None, Funtions: "connection_SAPConnection" = None, connection_SAPFunctionUnit23: set["connection_MetadataTable"] = None, functionUnit26: "connection_SAPTestInputParameterTable" = None, SAPFunctionUnit32: "connection_InputSAPFunctionParameterTable" = None, SAPFunctionUnit34: "connection_OutputSAPFunctionParameterTable" = None, SAPFunctionUnit66: "connection_SAPTestInputParameterTable" = None):
        self.OutputTableName = OutputTableName
        self.OutputType = OutputType
        self.SAPFunctionUnit = SAPFunctionUnit
        self.functionUnit = functionUnit
        self.functionUnit18 = functionUnit18
        self.connection_SAPFunctionUnit = connection_SAPFunctionUnit
        self.Funtions = Funtions
        self.connection_SAPFunctionUnit23 = connection_SAPFunctionUnit23 if connection_SAPFunctionUnit23 is not None else set()
        self.functionUnit26 = functionUnit26
        self.SAPFunctionUnit32 = SAPFunctionUnit32
        self.SAPFunctionUnit34 = SAPFunctionUnit34
        self.SAPFunctionUnit66 = SAPFunctionUnit66
        
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
    def functionUnit18(self):
        return self.__functionUnit18

    @functionUnit18.setter
    def functionUnit18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__functionUnit18", None)
        self.__functionUnit18 = value
        
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
    def SAPFunctionUnit34(self):
        return self.__SAPFunctionUnit34

    @SAPFunctionUnit34.setter
    def SAPFunctionUnit34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__SAPFunctionUnit34", None)
        self.__SAPFunctionUnit34 = value
        
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
    def SAPFunctionUnit32(self):
        return self.__SAPFunctionUnit32

    @SAPFunctionUnit32.setter
    def SAPFunctionUnit32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__SAPFunctionUnit32", None)
        self.__SAPFunctionUnit32 = value
        
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
    def connection_SAPFunctionUnit23(self):
        return self.__connection_SAPFunctionUnit23

    @connection_SAPFunctionUnit23.setter
    def connection_SAPFunctionUnit23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__connection_SAPFunctionUnit23", None)
        self.__connection_SAPFunctionUnit23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection_MetadataTable24"):
                    opp_val = getattr(item, "connection_MetadataTable24", None)
                    
                    if opp_val == self:
                        setattr(item, "connection_MetadataTable24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection_MetadataTable24"):
                    opp_val = getattr(item, "connection_MetadataTable24", None)
                    
                    setattr(item, "connection_MetadataTable24", self)
                    

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
    def SAPFunctionUnit66(self):
        return self.__SAPFunctionUnit66

    @SAPFunctionUnit66.setter
    def SAPFunctionUnit66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__SAPFunctionUnit66", None)
        self.__SAPFunctionUnit66 = value
        
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
    def functionUnit26(self):
        return self.__functionUnit26

    @functionUnit26.setter
    def functionUnit26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__functionUnit26", None)
        self.__functionUnit26 = value
        
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
    def connection_SAPFunctionUnit(self):
        return self.__connection_SAPFunctionUnit

    @connection_SAPFunctionUnit.setter
    def connection_SAPFunctionUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_SAPFunctionUnit__connection_SAPFunctionUnit", None)
        self.__connection_SAPFunctionUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_MetadataTable20"):
                opp_val = getattr(old_value, "connection_MetadataTable20", None)
                if opp_val == self:
                    setattr(old_value, "connection_MetadataTable20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_MetadataTable20"):
                opp_val = getattr(value, "connection_MetadataTable20", None)
                setattr(value, "connection_MetadataTable20", self)

    def setDocument(self, connection_document):
        # TODO: Implement setDocument method
        pass

class connection_CDCType(AbstractMetadataObject):

    def __init__(self, linkDB: str, journalName: str, connection_CDCType: "connection_CDCConnection" = None, connection_CDCType63: "connection_CDCConnection" = None, connection_CDCType61: set["connection_SubscriberTable"] = None):
        self.linkDB = linkDB
        self.journalName = journalName
        self.connection_CDCType = connection_CDCType
        self.connection_CDCType63 = connection_CDCType63
        self.connection_CDCType61 = connection_CDCType61 if connection_CDCType61 is not None else set()
        
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
    def connection_CDCType63(self):
        return self.__connection_CDCType63

    @connection_CDCType63.setter
    def connection_CDCType63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_CDCType__connection_CDCType63", None)
        self.__connection_CDCType63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connection_CDCConnection64"):
                opp_val = getattr(old_value, "connection_CDCConnection64", None)
                if opp_val == self:
                    setattr(old_value, "connection_CDCConnection64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection_CDCConnection64"):
                opp_val = getattr(value, "connection_CDCConnection64", None)
                setattr(value, "connection_CDCConnection64", self)

    @property
    def connection_CDCType61(self):
        return self.__connection_CDCType61

    @connection_CDCType61.setter
    def connection_CDCType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_connection_CDCType__connection_CDCType61", None)
        self.__connection_CDCType61 = value if value is not None else set()
        
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
    def htmlFile(self):
        return self.__htmlFile

    @htmlFile.setter
    def htmlFile(self, htmlFile: str):
        self.__htmlFile = htmlFile


    @property
    def useHtmlOutput(self):
        return self.__useHtmlOutput

    @useHtmlOutput.setter
    def useHtmlOutput(self, useHtmlOutput: bool):
        self.__useHtmlOutput = useHtmlOutput


    @property
    def gatewayService(self):
        return self.__gatewayService

    @gatewayService.setter
    def gatewayService(self, gatewayService: str):
        self.__gatewayService = gatewayService


    @property
    def programId(self):
        return self.__programId

    @programId.setter
    def programId(self, programId: str):
        self.__programId = programId


    @property
    def useXmlOutput(self):
        return self.__useXmlOutput

    @useXmlOutput.setter
    def useXmlOutput(self, useXmlOutput: bool):
        self.__useXmlOutput = useXmlOutput


    @property
    def xmlFile(self):
        return self.__xmlFile

    @xmlFile.setter
    def xmlFile(self, xmlFile: str):
        self.__xmlFile = xmlFile


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
            if hasattr(old_value, "connection15"):
                opp_val = getattr(old_value, "connection15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connection15"):
                opp_val = getattr(value, "connection15", None)
                if opp_val is None:
                    setattr(value, "connection15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "SAPConnection28"):
                opp_val = getattr(old_value, "SAPConnection28", None)
                if opp_val == self:
                    setattr(old_value, "SAPConnection28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SAPConnection28"):
                opp_val = getattr(value, "SAPConnection28", None)
                setattr(value, "SAPConnection28", self)

class connection_Metadata(AbstractMetadataObject):

    pass
class Schema:

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