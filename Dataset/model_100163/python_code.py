from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DevelopmentStatus(Enum):
    DRAFT = "DRAFT"
    PROD = "PROD"


############################################
# Definition of Classes
############################################

class Element:

    pass
class cwm_xml_TdXMLElement(Element):

    def __init__(self, javaType: str, cwm_xml_TdXMLElement: "xml_cwm_EObject" = None, cwm_xml_TdXMLElement3: "TdXMLDocument" = None, cwm_xml_TdXMLElement5: "TdXMLContent" = None):
        self.javaType = javaType
        self.cwm_xml_TdXMLElement = cwm_xml_TdXMLElement
        self.cwm_xml_TdXMLElement3 = cwm_xml_TdXMLElement3
        self.cwm_xml_TdXMLElement5 = cwm_xml_TdXMLElement5
        
        pass
    @property
    def javaType(self):
        return self.__javaType

    @javaType.setter
    def javaType(self, javaType: str):
        self.__javaType = javaType


    @property
    def cwm_xml_TdXMLElement5(self):
        return self.__cwm_xml_TdXMLElement5

    @cwm_xml_TdXMLElement5.setter
    def cwm_xml_TdXMLElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cwm_xml_TdXMLElement__cwm_xml_TdXMLElement5", None)
        self.__cwm_xml_TdXMLElement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TdXMLContent"):
                opp_val = getattr(old_value, "TdXMLContent", None)
                if opp_val == self:
                    setattr(old_value, "TdXMLContent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TdXMLContent"):
                opp_val = getattr(value, "TdXMLContent", None)
                setattr(value, "TdXMLContent", self)

    @property
    def cwm_xml_TdXMLElement(self):
        return self.__cwm_xml_TdXMLElement

    @cwm_xml_TdXMLElement.setter
    def cwm_xml_TdXMLElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cwm_xml_TdXMLElement__cwm_xml_TdXMLElement", None)
        self.__cwm_xml_TdXMLElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xml_cwm_EObject"):
                opp_val = getattr(old_value, "xml_cwm_EObject", None)
                if opp_val == self:
                    setattr(old_value, "xml_cwm_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xml_cwm_EObject"):
                opp_val = getattr(value, "xml_cwm_EObject", None)
                setattr(value, "xml_cwm_EObject", self)

    @property
    def cwm_xml_TdXMLElement3(self):
        return self.__cwm_xml_TdXMLElement3

    @cwm_xml_TdXMLElement3.setter
    def cwm_xml_TdXMLElement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cwm_xml_TdXMLElement__cwm_xml_TdXMLElement3", None)
        self.__cwm_xml_TdXMLElement3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TdXMLDocument"):
                opp_val = getattr(old_value, "TdXMLDocument", None)
                if opp_val == self:
                    setattr(old_value, "TdXMLDocument", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TdXMLDocument"):
                opp_val = getattr(value, "TdXMLDocument", None)
                setattr(value, "TdXMLDocument", self)

    def setContentType(self, cwm_contentType):
        # TODO: Implement setContentType method
        pass

    def getContentType(self) :
        # TODO: Implement getContentType method
        pass

class Machine:

    pass
class cwm_softwaredeployment_TdMachine(Machine):

    pass
class SoftwareSystem:

    pass
class cwm_softwaredeployment_TdSoftwareSystem(SoftwareSystem):

    pass
class Document:

    pass
class cwm_xml_TdXMLDocument(Document):

    def __init__(self, xsdFilePath: str):
        self.xsdFilePath = xsdFilePath
        
        pass
    @property
    def xsdFilePath(self):
        return self.__xsdFilePath

    @xsdFilePath.setter
    def xsdFilePath(self, xsdFilePath: str):
        self.__xsdFilePath = xsdFilePath


class TdXMLElement:

    pass
class Content:

    pass
class cwm_xml_TdXMLContent(Content):

    pass
class TdXMLContent:

    pass
class TdXMLDocument:

    pass
class xml_cwm_EObject:

    pass
class DataProvider:

    pass
class cwm_softwaredeployment_TdDataProvider(DataProvider):

    pass
class DataManager:

    pass
class cwm_softwaredeployment_TdDataManager(DataManager):

    pass
class ProviderConnection:

    pass
class cwm_softwaredeployment_TdProviderConnection(ProviderConnection):

    def __init__(self, login: str, password: str, connectionString: str, driverClassName: str):
        self.login = login
        self.password = password
        self.connectionString = connectionString
        self.driverClassName = driverClassName
        
        pass
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def connectionString(self):
        return self.__connectionString

    @connectionString.setter
    def connectionString(self, connectionString: str):
        self.__connectionString = connectionString


    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login: str):
        self.__login = login


    @property
    def driverClassName(self):
        return self.__driverClassName

    @driverClassName.setter
    def driverClassName(self, driverClassName: str):
        self.__driverClassName = driverClassName


class Procedure:

    pass
class cwm_relational_TdProcedure(Procedure):

    pass
class Trigger:

    pass
class cwm_relational_TdTrigger(Trigger):

    pass
class SQLSimpleType:

    pass
class cwm_relational_TdSqlDataType(SQLSimpleType):

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
    def searchable(self):
        return self.__searchable

    @searchable.setter
    def searchable(self, searchable: str):
        self.__searchable = searchable


    @property
    def nullable(self):
        return self.__nullable

    @nullable.setter
    def nullable(self, nullable: str):
        self.__nullable = nullable


    @property
    def caseSensitive(self):
        return self.__caseSensitive

    @caseSensitive.setter
    def caseSensitive(self, caseSensitive: str):
        self.__caseSensitive = caseSensitive


    @property
    def javaDataType(self):
        return self.__javaDataType

    @javaDataType.setter
    def javaDataType(self, javaDataType: int):
        self.__javaDataType = javaDataType


    @property
    def autoIncrement(self):
        return self.__autoIncrement

    @autoIncrement.setter
    def autoIncrement(self, autoIncrement: str):
        self.__autoIncrement = autoIncrement


    @property
    def localTypeName(self):
        return self.__localTypeName

    @localTypeName.setter
    def localTypeName(self, localTypeName: str):
        self.__localTypeName = localTypeName


class TdSqlDataType:

    pass
class Column:

    pass
class cwm_relational_TdColumn(Column):

    def __init__(self, javaType: int, cwm_relational_TdColumn: "TdSqlDataType" = None):
        self.javaType = javaType
        self.cwm_relational_TdColumn = cwm_relational_TdColumn
        
        pass
    @property
    def javaType(self):
        return self.__javaType

    @javaType.setter
    def javaType(self, javaType: int):
        self.__javaType = javaType


    @property
    def cwm_relational_TdColumn(self):
        return self.__cwm_relational_TdColumn

    @cwm_relational_TdColumn.setter
    def cwm_relational_TdColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cwm_relational_TdColumn__cwm_relational_TdColumn", None)
        self.__cwm_relational_TdColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TdSqlDataType"):
                opp_val = getattr(old_value, "TdSqlDataType", None)
                if opp_val == self:
                    setattr(old_value, "TdSqlDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TdSqlDataType"):
                opp_val = getattr(value, "TdSqlDataType", None)
                setattr(value, "TdSqlDataType", self)

    def setContentType(self, cwm_contentType):
        # TODO: Implement setContentType method
        pass

    def getContentType(self) :
        # TODO: Implement getContentType method
        pass

class Schema:

    pass
class cwm_relational_TdSchema(Schema):

    pass
class Catalog:

    pass
class cwm_relational_TdCatalog(Catalog):

    def __init__(self):
        
        pass
    def addSchema(self, cwm_schema) :
        # TODO: Implement addSchema method
        pass

class View:

    pass
class cwm_relational_TdView(View):

    pass
class Table:

    pass
class cwm_relational_TdTable(Table):

    pass