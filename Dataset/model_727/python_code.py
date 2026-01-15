from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AccessPolicyAccessModeEnum(Enum):
    EDIT = "EDIT"
    DELETE = "DELETE"
    CREATE = "CREATE"
class DatatypeDefinitionDateFormatEnum(Enum):
    W3C = "W3C"
    CUSTOM = "CUSTOM"


############################################
# Definition of Classes
############################################

class rif11a_DataTypes_XhtmlContent:

    pass
class rif11a_DataTypes_XmlContent:

    pass
class rif11a_DataTypes_BinaryContent:

    pass
class ExchangeFile_AccessPolicy:

    pass
class rif11a_ExchangeFile_RIF:

    def __init__(self, author: str, comment: str, countryCode: str, creationTime: str, identifier: str, sourceToolId: str, title: str, version: str, rif11a_ExchangeFile_RIF: set["ExchangeFile_AccessPolicy"] = None, rif11a_ExchangeFile_RIF80: set["ExchangeFile_DatatypeDefinition"] = None, rif11a_ExchangeFile_RIF83: set["ExchangeFile_SpecHierarchyRoot"] = None, rif11a_ExchangeFile_RIF86: set["ExchangeFile_SpecObject"] = None, rif11a_ExchangeFile_RIF89: set["ExchangeFile_SpecGroup"] = None, rif11a_ExchangeFile_RIF92: set["ExchangeFile_SpecType"] = None, rif11a_ExchangeFile_RIF95: set["ExchangeFile_SpecRelation"] = None):
        self.author = author
        self.comment = comment
        self.countryCode = countryCode
        self.creationTime = creationTime
        self.identifier = identifier
        self.sourceToolId = sourceToolId
        self.title = title
        self.version = version
        self.rif11a_ExchangeFile_RIF = rif11a_ExchangeFile_RIF if rif11a_ExchangeFile_RIF is not None else set()
        self.rif11a_ExchangeFile_RIF80 = rif11a_ExchangeFile_RIF80 if rif11a_ExchangeFile_RIF80 is not None else set()
        self.rif11a_ExchangeFile_RIF83 = rif11a_ExchangeFile_RIF83 if rif11a_ExchangeFile_RIF83 is not None else set()
        self.rif11a_ExchangeFile_RIF86 = rif11a_ExchangeFile_RIF86 if rif11a_ExchangeFile_RIF86 is not None else set()
        self.rif11a_ExchangeFile_RIF89 = rif11a_ExchangeFile_RIF89 if rif11a_ExchangeFile_RIF89 is not None else set()
        self.rif11a_ExchangeFile_RIF92 = rif11a_ExchangeFile_RIF92 if rif11a_ExchangeFile_RIF92 is not None else set()
        self.rif11a_ExchangeFile_RIF95 = rif11a_ExchangeFile_RIF95 if rif11a_ExchangeFile_RIF95 is not None else set()
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def countryCode(self) -> str:
        return self.__countryCode

    @countryCode.setter
    def countryCode(self, countryCode: str):
        self.__countryCode = countryCode

    @property
    def creationTime(self) -> str:
        return self.__creationTime

    @creationTime.setter
    def creationTime(self, creationTime: str):
        self.__creationTime = creationTime

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def sourceToolId(self) -> str:
        return self.__sourceToolId

    @sourceToolId.setter
    def sourceToolId(self, sourceToolId: str):
        self.__sourceToolId = sourceToolId

    @property
    def rif11a_ExchangeFile_RIF(self):
        return self.__rif11a_ExchangeFile_RIF

    @rif11a_ExchangeFile_RIF.setter
    def rif11a_ExchangeFile_RIF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF", None)
        self.__rif11a_ExchangeFile_RIF = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_AccessPolicy"):
                    opp_val = getattr(item, "ExchangeFile_AccessPolicy", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_AccessPolicy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_AccessPolicy"):
                    opp_val = getattr(item, "ExchangeFile_AccessPolicy", None)
                    
                    setattr(item, "ExchangeFile_AccessPolicy", self)
                    

    @property
    def rif11a_ExchangeFile_RIF83(self):
        return self.__rif11a_ExchangeFile_RIF83

    @rif11a_ExchangeFile_RIF83.setter
    def rif11a_ExchangeFile_RIF83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF83", None)
        self.__rif11a_ExchangeFile_RIF83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecHierarchyRoot84"):
                    opp_val = getattr(item, "ExchangeFile_SpecHierarchyRoot84", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecHierarchyRoot84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecHierarchyRoot84"):
                    opp_val = getattr(item, "ExchangeFile_SpecHierarchyRoot84", None)
                    
                    setattr(item, "ExchangeFile_SpecHierarchyRoot84", self)
                    

    @property
    def rif11a_ExchangeFile_RIF89(self):
        return self.__rif11a_ExchangeFile_RIF89

    @rif11a_ExchangeFile_RIF89.setter
    def rif11a_ExchangeFile_RIF89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF89", None)
        self.__rif11a_ExchangeFile_RIF89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecGroup90"):
                    opp_val = getattr(item, "ExchangeFile_SpecGroup90", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecGroup90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecGroup90"):
                    opp_val = getattr(item, "ExchangeFile_SpecGroup90", None)
                    
                    setattr(item, "ExchangeFile_SpecGroup90", self)
                    

    @property
    def rif11a_ExchangeFile_RIF80(self):
        return self.__rif11a_ExchangeFile_RIF80

    @rif11a_ExchangeFile_RIF80.setter
    def rif11a_ExchangeFile_RIF80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF80", None)
        self.__rif11a_ExchangeFile_RIF80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_DatatypeDefinition81"):
                    opp_val = getattr(item, "ExchangeFile_DatatypeDefinition81", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_DatatypeDefinition81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_DatatypeDefinition81"):
                    opp_val = getattr(item, "ExchangeFile_DatatypeDefinition81", None)
                    
                    setattr(item, "ExchangeFile_DatatypeDefinition81", self)
                    

    @property
    def rif11a_ExchangeFile_RIF86(self):
        return self.__rif11a_ExchangeFile_RIF86

    @rif11a_ExchangeFile_RIF86.setter
    def rif11a_ExchangeFile_RIF86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF86", None)
        self.__rif11a_ExchangeFile_RIF86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecObject87"):
                    opp_val = getattr(item, "ExchangeFile_SpecObject87", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecObject87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecObject87"):
                    opp_val = getattr(item, "ExchangeFile_SpecObject87", None)
                    
                    setattr(item, "ExchangeFile_SpecObject87", self)
                    

    @property
    def rif11a_ExchangeFile_RIF92(self):
        return self.__rif11a_ExchangeFile_RIF92

    @rif11a_ExchangeFile_RIF92.setter
    def rif11a_ExchangeFile_RIF92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF92", None)
        self.__rif11a_ExchangeFile_RIF92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecType93"):
                    opp_val = getattr(item, "ExchangeFile_SpecType93", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecType93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecType93"):
                    opp_val = getattr(item, "ExchangeFile_SpecType93", None)
                    
                    setattr(item, "ExchangeFile_SpecType93", self)
                    

    @property
    def rif11a_ExchangeFile_RIF95(self):
        return self.__rif11a_ExchangeFile_RIF95

    @rif11a_ExchangeFile_RIF95.setter
    def rif11a_ExchangeFile_RIF95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF95", None)
        self.__rif11a_ExchangeFile_RIF95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecRelation96"):
                    opp_val = getattr(item, "ExchangeFile_SpecRelation96", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecRelation96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecRelation96"):
                    opp_val = getattr(item, "ExchangeFile_SpecRelation96", None)
                    
                    setattr(item, "ExchangeFile_SpecRelation96", self)
                    

class DatatypeDefinitionSimple:

    pass
class rif11a_ExchangeFile_DatatypeDefinitionDate(DatatypeDefinitionSimple):

    def __init__(self, format: str):
        self.format = format
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class rif11a_ExchangeFile_DatatypeDefinitionString(DatatypeDefinitionSimple):

    def __init__(self, maxLength: str):
        self.maxLength = maxLength
        
    @property
    def maxLength(self) -> str:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: str):
        self.__maxLength = maxLength

class rif11a_ExchangeFile_DatatypeDefinitionInteger(DatatypeDefinitionSimple):

    def __init__(self, max: str, min: str):
        self.max = max
        self.min = min
        
    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

class rif11a_ExchangeFile_DatatypeDefinitionReal(DatatypeDefinitionSimple):

    def __init__(self, accuracy: str, max: str, min: str):
        self.accuracy = accuracy
        self.max = max
        self.min = min
        
    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def accuracy(self) -> str:
        return self.__accuracy

    @accuracy.setter
    def accuracy(self, accuracy: str):
        self.__accuracy = accuracy

    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

class rif11a_ExchangeFile_DatatypeDefinitionBoolean(DatatypeDefinitionSimple):

    pass
class DatatypeDefinitionComplex:

    pass
class rif11a_ExchangeFile_DatatypeDefinitionXmlData(DatatypeDefinitionComplex):

    def __init__(self, nameSpaceURI: str, schemaLocation: str):
        self.nameSpaceURI = nameSpaceURI
        self.schemaLocation = schemaLocation
        
    @property
    def nameSpaceURI(self) -> str:
        return self.__nameSpaceURI

    @nameSpaceURI.setter
    def nameSpaceURI(self, nameSpaceURI: str):
        self.__nameSpaceURI = nameSpaceURI

    @property
    def schemaLocation(self) -> str:
        return self.__schemaLocation

    @schemaLocation.setter
    def schemaLocation(self, schemaLocation: str):
        self.__schemaLocation = schemaLocation

class rif11a_ExchangeFile_DatatypeDefinitionDocument(DatatypeDefinitionComplex):

    pass
class rif11a_ExchangeFile_DatatypeDefinitionBinaryFile(DatatypeDefinitionComplex):

    def __init__(self, application: str, filenameSuffix: str, formatName: str, mimeType: str):
        self.application = application
        self.filenameSuffix = filenameSuffix
        self.formatName = formatName
        self.mimeType = mimeType
        
    @property
    def mimeType(self) -> str:
        return self.__mimeType

    @mimeType.setter
    def mimeType(self, mimeType: str):
        self.__mimeType = mimeType

    @property
    def filenameSuffix(self) -> str:
        return self.__filenameSuffix

    @filenameSuffix.setter
    def filenameSuffix(self, filenameSuffix: str):
        self.__filenameSuffix = filenameSuffix

    @property
    def formatName(self) -> str:
        return self.__formatName

    @formatName.setter
    def formatName(self, formatName: str):
        self.__formatName = formatName

    @property
    def application(self) -> str:
        return self.__application

    @application.setter
    def application(self, application: str):
        self.__application = application

class DataTypes_XmlContent:

    pass
class DataTypes_BinaryContent:

    pass
class DataTypes_XhtmlContent:

    pass
class ExchangeFile_AttributeDefinitionComplex:

    pass
class AttributeValueComplex:

    pass
class rif11a_ExchangeFile_AttributeValueFileReference(AttributeValueComplex):

    def __init__(self, pathToFile: str, rif11a_ExchangeFile_AttributeValueFileReference: "ExchangeFile_AttributeDefinitionComplex" = None):
        self.pathToFile = pathToFile
        self.rif11a_ExchangeFile_AttributeValueFileReference = rif11a_ExchangeFile_AttributeValueFileReference
        
    @property
    def pathToFile(self) -> str:
        return self.__pathToFile

    @pathToFile.setter
    def pathToFile(self, pathToFile: str):
        self.__pathToFile = pathToFile

    @property
    def rif11a_ExchangeFile_AttributeValueFileReference(self):
        return self.__rif11a_ExchangeFile_AttributeValueFileReference

    @rif11a_ExchangeFile_AttributeValueFileReference.setter
    def rif11a_ExchangeFile_AttributeValueFileReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AttributeValueFileReference__rif11a_ExchangeFile_AttributeValueFileReference", None)
        self.__rif11a_ExchangeFile_AttributeValueFileReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExchangeFile_AttributeDefinitionComplex73"):
                opp_val = getattr(old_value, "ExchangeFile_AttributeDefinitionComplex73", None)
                if opp_val == self:
                    setattr(old_value, "ExchangeFile_AttributeDefinitionComplex73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExchangeFile_AttributeDefinitionComplex73"):
                opp_val = getattr(value, "ExchangeFile_AttributeDefinitionComplex73", None)
                setattr(value, "ExchangeFile_AttributeDefinitionComplex73", self)

class rif11a_ExchangeFile_AttributeValueXmlData(AttributeValueComplex):

    pass
class rif11a_ExchangeFile_AttributeValueEmbeddedFile(AttributeValueComplex):

    pass
class rif11a_ExchangeFile_AttributeValueEmbeddedDocument(AttributeValueComplex):

    pass
class ExchangeFile_AttributeDefinitionSimple:

    pass
class ExchangeFile_AttributeDefinitionEnumeration:

    pass
class ExchangeFile_AttributeValueSimple:

    pass
class ExchangeFile_DatatypeDefinitionSimple:

    pass
class rif11a_ExchangeFile_EmbeddedValue:

    def __init__(self, key: str, otherContent: str):
        self.key = key
        self.otherContent = otherContent
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def otherContent(self) -> str:
        return self.__otherContent

    @otherContent.setter
    def otherContent(self, otherContent: str):
        self.__otherContent = otherContent

class ExchangeFile_EmbeddedValue:

    pass
class ExchangeFile_EnumValue:

    pass
class ExchangeFile_AttributeValueEnumeration:

    pass
class ExchangeFile_DatatypeDefinitionEnumeration:

    pass
class AttributeValue:

    pass
class rif11a_ExchangeFile_AttributeValueSimple(AttributeValue):

    def __init__(self, theValue: str, rif11a_ExchangeFile_AttributeValueSimple: "ExchangeFile_AttributeDefinitionSimple" = None):
        self.theValue = theValue
        self.rif11a_ExchangeFile_AttributeValueSimple = rif11a_ExchangeFile_AttributeValueSimple
        
    @property
    def theValue(self) -> str:
        return self.__theValue

    @theValue.setter
    def theValue(self, theValue: str):
        self.__theValue = theValue

    @property
    def rif11a_ExchangeFile_AttributeValueSimple(self):
        return self.__rif11a_ExchangeFile_AttributeValueSimple

    @rif11a_ExchangeFile_AttributeValueSimple.setter
    def rif11a_ExchangeFile_AttributeValueSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AttributeValueSimple__rif11a_ExchangeFile_AttributeValueSimple", None)
        self.__rif11a_ExchangeFile_AttributeValueSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExchangeFile_AttributeDefinitionSimple"):
                opp_val = getattr(old_value, "ExchangeFile_AttributeDefinitionSimple", None)
                if opp_val == self:
                    setattr(old_value, "ExchangeFile_AttributeDefinitionSimple", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExchangeFile_AttributeDefinitionSimple"):
                opp_val = getattr(value, "ExchangeFile_AttributeDefinitionSimple", None)
                setattr(value, "ExchangeFile_AttributeDefinitionSimple", self)

class rif11a_ExchangeFile_AttributeValueEnumeration(AttributeValue):

    pass
class rif11a_ExchangeFile_AttributeValueComplex(AttributeValue):

    pass
class DatatypeDefinition:

    pass
class rif11a_ExchangeFile_DatatypeDefinitionEnumeration(DatatypeDefinition):

    pass
class rif11a_ExchangeFile_DatatypeDefinitionSimple(DatatypeDefinition):

    pass
class rif11a_ExchangeFile_DatatypeDefinitionComplex(DatatypeDefinition):

    def __init__(self, embedded: str):
        self.embedded = embedded
        
    @property
    def embedded(self) -> str:
        return self.__embedded

    @embedded.setter
    def embedded(self, embedded: str):
        self.__embedded = embedded

class ExchangeFile_AttributeValueComplex:

    pass
class ExchangeFile_DatatypeDefinitionComplex:

    pass
class AttributeDefinition:

    pass
class rif11a_ExchangeFile_AttributeDefinitionSimple(AttributeDefinition):

    pass
class rif11a_ExchangeFile_AttributeDefinitionEnumeration(AttributeDefinition):

    def __init__(self, multiValued: str, rif11a_ExchangeFile_AttributeDefinitionEnumeration: "ExchangeFile_DatatypeDefinitionEnumeration" = None, rif11a_ExchangeFile_AttributeDefinitionEnumeration54: "ExchangeFile_AttributeValueEnumeration" = None):
        self.multiValued = multiValued
        self.rif11a_ExchangeFile_AttributeDefinitionEnumeration = rif11a_ExchangeFile_AttributeDefinitionEnumeration
        self.rif11a_ExchangeFile_AttributeDefinitionEnumeration54 = rif11a_ExchangeFile_AttributeDefinitionEnumeration54
        
    @property
    def multiValued(self) -> str:
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: str):
        self.__multiValued = multiValued

    @property
    def rif11a_ExchangeFile_AttributeDefinitionEnumeration(self):
        return self.__rif11a_ExchangeFile_AttributeDefinitionEnumeration

    @rif11a_ExchangeFile_AttributeDefinitionEnumeration.setter
    def rif11a_ExchangeFile_AttributeDefinitionEnumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AttributeDefinitionEnumeration__rif11a_ExchangeFile_AttributeDefinitionEnumeration", None)
        self.__rif11a_ExchangeFile_AttributeDefinitionEnumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExchangeFile_DatatypeDefinitionEnumeration"):
                opp_val = getattr(old_value, "ExchangeFile_DatatypeDefinitionEnumeration", None)
                if opp_val == self:
                    setattr(old_value, "ExchangeFile_DatatypeDefinitionEnumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExchangeFile_DatatypeDefinitionEnumeration"):
                opp_val = getattr(value, "ExchangeFile_DatatypeDefinitionEnumeration", None)
                setattr(value, "ExchangeFile_DatatypeDefinitionEnumeration", self)

    @property
    def rif11a_ExchangeFile_AttributeDefinitionEnumeration54(self):
        return self.__rif11a_ExchangeFile_AttributeDefinitionEnumeration54

    @rif11a_ExchangeFile_AttributeDefinitionEnumeration54.setter
    def rif11a_ExchangeFile_AttributeDefinitionEnumeration54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AttributeDefinitionEnumeration__rif11a_ExchangeFile_AttributeDefinitionEnumeration54", None)
        self.__rif11a_ExchangeFile_AttributeDefinitionEnumeration54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExchangeFile_AttributeValueEnumeration"):
                opp_val = getattr(old_value, "ExchangeFile_AttributeValueEnumeration", None)
                if opp_val == self:
                    setattr(old_value, "ExchangeFile_AttributeValueEnumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExchangeFile_AttributeValueEnumeration"):
                opp_val = getattr(value, "ExchangeFile_AttributeValueEnumeration", None)
                setattr(value, "ExchangeFile_AttributeValueEnumeration", self)

class rif11a_ExchangeFile_AttributeDefinitionComplex(AttributeDefinition):

    pass
class ExchangeFile_SpecHierarchyRoot:

    pass
class ExchangeFile_DatatypeDefinition:

    pass
class ExchangeFile_SpecGroup:

    pass
class ExchangeFile_SpecRelation:

    pass
class ExchangeFile_RelationGroup:

    pass
class ExchangeFile_SpecObject:

    pass
class ExchangeFile_AttributeDefinition:

    pass
class rif11a_ExchangeFile_Identifiable(ABC):

    def __init__(self, desc: str, identifier: str, lastChange: str, longName: str):
        self.desc = desc
        self.identifier = identifier
        self.lastChange = lastChange
        self.longName = longName
        
    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

    @property
    def longName(self) -> str:
        return self.__longName

    @longName.setter
    def longName(self, longName: str):
        self.__longName = longName

    @property
    def lastChange(self) -> str:
        return self.__lastChange

    @lastChange.setter
    def lastChange(self, lastChange: str):
        self.__lastChange = lastChange

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

class ExchangeFile_AttributeValue:

    pass
class ExchangeFile_SpecType:

    pass
class Identifiable:

    pass
class rif11a_ExchangeFile_AttributeDefinition(Identifiable):

    pass
class rif11a_ExchangeFile_AttributeValue(Identifiable):

    pass
class rif11a_ExchangeFile_AccessPolicy(Identifiable):

    def __init__(self, accessMode: str, rif11a_ExchangeFile_AccessPolicy: set["ExchangeFile_SpecGroup"] = None, rif11a_ExchangeFile_AccessPolicy29: set["ExchangeFile_RelationGroup"] = None, rif11a_ExchangeFile_AccessPolicy31: set["ExchangeFile_DatatypeDefinition"] = None, rif11a_ExchangeFile_AccessPolicy33: set["ExchangeFile_SpecRelation"] = None, rif11a_ExchangeFile_AccessPolicy36: set["ExchangeFile_AttributeValue"] = None, rif11a_ExchangeFile_AccessPolicy39: set["ExchangeFile_SpecType"] = None, rif11a_ExchangeFile_AccessPolicy26: set["ExchangeFile_AttributeDefinition"] = None, rif11a_ExchangeFile_AccessPolicy42: set["ExchangeFile_SpecHierarchy"] = None, rif11a_ExchangeFile_AccessPolicy45: set["ExchangeFile_SpecObject"] = None, rif11a_ExchangeFile_AccessPolicy48: set["ExchangeFile_SpecHierarchyRoot"] = None):
        self.accessMode = accessMode
        self.rif11a_ExchangeFile_AccessPolicy = rif11a_ExchangeFile_AccessPolicy if rif11a_ExchangeFile_AccessPolicy is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy29 = rif11a_ExchangeFile_AccessPolicy29 if rif11a_ExchangeFile_AccessPolicy29 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy31 = rif11a_ExchangeFile_AccessPolicy31 if rif11a_ExchangeFile_AccessPolicy31 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy33 = rif11a_ExchangeFile_AccessPolicy33 if rif11a_ExchangeFile_AccessPolicy33 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy36 = rif11a_ExchangeFile_AccessPolicy36 if rif11a_ExchangeFile_AccessPolicy36 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy39 = rif11a_ExchangeFile_AccessPolicy39 if rif11a_ExchangeFile_AccessPolicy39 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy26 = rif11a_ExchangeFile_AccessPolicy26 if rif11a_ExchangeFile_AccessPolicy26 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy42 = rif11a_ExchangeFile_AccessPolicy42 if rif11a_ExchangeFile_AccessPolicy42 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy45 = rif11a_ExchangeFile_AccessPolicy45 if rif11a_ExchangeFile_AccessPolicy45 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy48 = rif11a_ExchangeFile_AccessPolicy48 if rif11a_ExchangeFile_AccessPolicy48 is not None else set()
        
    @property
    def accessMode(self) -> str:
        return self.__accessMode

    @accessMode.setter
    def accessMode(self, accessMode: str):
        self.__accessMode = accessMode

    @property
    def rif11a_ExchangeFile_AccessPolicy29(self):
        return self.__rif11a_ExchangeFile_AccessPolicy29

    @rif11a_ExchangeFile_AccessPolicy29.setter
    def rif11a_ExchangeFile_AccessPolicy29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy29", None)
        self.__rif11a_ExchangeFile_AccessPolicy29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_RelationGroup"):
                    opp_val = getattr(item, "ExchangeFile_RelationGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_RelationGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_RelationGroup"):
                    opp_val = getattr(item, "ExchangeFile_RelationGroup", None)
                    
                    setattr(item, "ExchangeFile_RelationGroup", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy39(self):
        return self.__rif11a_ExchangeFile_AccessPolicy39

    @rif11a_ExchangeFile_AccessPolicy39.setter
    def rif11a_ExchangeFile_AccessPolicy39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy39", None)
        self.__rif11a_ExchangeFile_AccessPolicy39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecType40"):
                    opp_val = getattr(item, "ExchangeFile_SpecType40", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecType40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecType40"):
                    opp_val = getattr(item, "ExchangeFile_SpecType40", None)
                    
                    setattr(item, "ExchangeFile_SpecType40", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy(self):
        return self.__rif11a_ExchangeFile_AccessPolicy

    @rif11a_ExchangeFile_AccessPolicy.setter
    def rif11a_ExchangeFile_AccessPolicy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy", None)
        self.__rif11a_ExchangeFile_AccessPolicy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecGroup"):
                    opp_val = getattr(item, "ExchangeFile_SpecGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecGroup"):
                    opp_val = getattr(item, "ExchangeFile_SpecGroup", None)
                    
                    setattr(item, "ExchangeFile_SpecGroup", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy48(self):
        return self.__rif11a_ExchangeFile_AccessPolicy48

    @rif11a_ExchangeFile_AccessPolicy48.setter
    def rif11a_ExchangeFile_AccessPolicy48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy48", None)
        self.__rif11a_ExchangeFile_AccessPolicy48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecHierarchyRoot"):
                    opp_val = getattr(item, "ExchangeFile_SpecHierarchyRoot", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecHierarchyRoot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecHierarchyRoot"):
                    opp_val = getattr(item, "ExchangeFile_SpecHierarchyRoot", None)
                    
                    setattr(item, "ExchangeFile_SpecHierarchyRoot", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy26(self):
        return self.__rif11a_ExchangeFile_AccessPolicy26

    @rif11a_ExchangeFile_AccessPolicy26.setter
    def rif11a_ExchangeFile_AccessPolicy26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy26", None)
        self.__rif11a_ExchangeFile_AccessPolicy26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_AttributeDefinition27"):
                    opp_val = getattr(item, "ExchangeFile_AttributeDefinition27", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_AttributeDefinition27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_AttributeDefinition27"):
                    opp_val = getattr(item, "ExchangeFile_AttributeDefinition27", None)
                    
                    setattr(item, "ExchangeFile_AttributeDefinition27", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy45(self):
        return self.__rif11a_ExchangeFile_AccessPolicy45

    @rif11a_ExchangeFile_AccessPolicy45.setter
    def rif11a_ExchangeFile_AccessPolicy45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy45", None)
        self.__rif11a_ExchangeFile_AccessPolicy45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecObject46"):
                    opp_val = getattr(item, "ExchangeFile_SpecObject46", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecObject46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecObject46"):
                    opp_val = getattr(item, "ExchangeFile_SpecObject46", None)
                    
                    setattr(item, "ExchangeFile_SpecObject46", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy31(self):
        return self.__rif11a_ExchangeFile_AccessPolicy31

    @rif11a_ExchangeFile_AccessPolicy31.setter
    def rif11a_ExchangeFile_AccessPolicy31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy31", None)
        self.__rif11a_ExchangeFile_AccessPolicy31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_DatatypeDefinition"):
                    opp_val = getattr(item, "ExchangeFile_DatatypeDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_DatatypeDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_DatatypeDefinition"):
                    opp_val = getattr(item, "ExchangeFile_DatatypeDefinition", None)
                    
                    setattr(item, "ExchangeFile_DatatypeDefinition", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy42(self):
        return self.__rif11a_ExchangeFile_AccessPolicy42

    @rif11a_ExchangeFile_AccessPolicy42.setter
    def rif11a_ExchangeFile_AccessPolicy42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy42", None)
        self.__rif11a_ExchangeFile_AccessPolicy42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecHierarchy43"):
                    opp_val = getattr(item, "ExchangeFile_SpecHierarchy43", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecHierarchy43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecHierarchy43"):
                    opp_val = getattr(item, "ExchangeFile_SpecHierarchy43", None)
                    
                    setattr(item, "ExchangeFile_SpecHierarchy43", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy36(self):
        return self.__rif11a_ExchangeFile_AccessPolicy36

    @rif11a_ExchangeFile_AccessPolicy36.setter
    def rif11a_ExchangeFile_AccessPolicy36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy36", None)
        self.__rif11a_ExchangeFile_AccessPolicy36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_AttributeValue37"):
                    opp_val = getattr(item, "ExchangeFile_AttributeValue37", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_AttributeValue37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_AttributeValue37"):
                    opp_val = getattr(item, "ExchangeFile_AttributeValue37", None)
                    
                    setattr(item, "ExchangeFile_AttributeValue37", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy33(self):
        return self.__rif11a_ExchangeFile_AccessPolicy33

    @rif11a_ExchangeFile_AccessPolicy33.setter
    def rif11a_ExchangeFile_AccessPolicy33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy33", None)
        self.__rif11a_ExchangeFile_AccessPolicy33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecRelation34"):
                    opp_val = getattr(item, "ExchangeFile_SpecRelation34", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecRelation34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecRelation34"):
                    opp_val = getattr(item, "ExchangeFile_SpecRelation34", None)
                    
                    setattr(item, "ExchangeFile_SpecRelation34", self)
                    

class rif11a_ExchangeFile_SpecType(Identifiable):

    pass
class rif11a_ExchangeFile_DatatypeDefinition(Identifiable):

    pass
class rif11a_ExchangeFile_SpecHierarchy(Identifiable):

    pass
class rif11a_ExchangeFile_EnumValue(Identifiable):

    pass
class rif11a_ExchangeFile_RelationGroup(Identifiable):

    pass
class rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes(Identifiable):

    pass
class ExchangeFile_SpecHierarchy:

    pass
class SpecElementWithUserDefinedAttributes:

    pass
class rif11a_ExchangeFile_SpecObject(SpecElementWithUserDefinedAttributes):

    pass
class rif11a_ExchangeFile_SpecGroup(SpecElementWithUserDefinedAttributes):

    pass
class rif11a_ExchangeFile_SpecRelation(SpecElementWithUserDefinedAttributes):

    pass
class rif11a_ExchangeFile_SpecHierarchyRoot(SpecElementWithUserDefinedAttributes):

    pass