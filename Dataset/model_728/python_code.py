from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DatatypeDefinitionDateFormatEnum(Enum):
    W3C = "W3C"
    CUSTOM = "CUSTOM"
class AccessPolicyAccessModeEnum(Enum):
    EDIT = "EDIT"
    DELETE = "DELETE"
    CREATE = "CREATE"


############################################
# Definition of Classes
############################################

class rif12_DataTypes_XmlContent:

    pass
class rif12_DataTypes_XhtmlContent:

    pass
class rif12_DataTypes_BinaryContent:

    pass
class rif12_ExchangeFile_RIFToolExtension:

    pass
class RIFContent:

    pass
class AccessPolicy:

    pass
class rif12_ExchangeFile_RIFContent:

    pass
class rif12_ExchangeFile_RIFHeader:

    def __init__(self, author: str, comment: str, creationTime: str, identifier: str, sourceToolId: str, title: str):
        self.author = author
        self.comment = comment
        self.creationTime = creationTime
        self.identifier = identifier
        self.sourceToolId = sourceToolId
        self.title = title
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def creationTime(self) -> str:
        return self.__creationTime

    @creationTime.setter
    def creationTime(self, creationTime: str):
        self.__creationTime = creationTime

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def sourceToolId(self) -> str:
        return self.__sourceToolId

    @sourceToolId.setter
    def sourceToolId(self, sourceToolId: str):
        self.__sourceToolId = sourceToolId

class RIFToolExtension:

    pass
class RIFHeader:

    pass
class rif12_ExchangeFile_RIF:

    pass
class DataTypes_XmlContent:

    pass
class DataTypes_BinaryContent:

    pass
class DataTypes_XhtmlContent:

    pass
class AttributeDefinitionComplex:

    pass
class AttributeDefinitionSimple:

    pass
class AttributeValueSimple:

    pass
class DatatypeDefinitionSimple:

    pass
class rif12_ExchangeFile_DatatypeDefinitionInteger(DatatypeDefinitionSimple):

    def __init__(self, max: str, min: str, DatatypeDefinitionSimple: "rif12_ExchangeFile_AttributeDefinitionSimple"):
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

class rif12_ExchangeFile_DatatypeDefinitionBoolean(DatatypeDefinitionSimple):

    pass
class rif12_ExchangeFile_DatatypeDefinitionString(DatatypeDefinitionSimple):

    def __init__(self, maxLength: str, DatatypeDefinitionSimple: "rif12_ExchangeFile_AttributeDefinitionSimple"):
        self.maxLength = maxLength
        
    @property
    def maxLength(self) -> str:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: str):
        self.__maxLength = maxLength

class rif12_ExchangeFile_DatatypeDefinitionDate(DatatypeDefinitionSimple):

    def __init__(self, format: str, DatatypeDefinitionSimple: "rif12_ExchangeFile_AttributeDefinitionSimple"):
        self.format = format
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class rif12_ExchangeFile_DatatypeDefinitionReal(DatatypeDefinitionSimple):

    def __init__(self, accuracy: str, max: str, min: str, DatatypeDefinitionSimple: "rif12_ExchangeFile_AttributeDefinitionSimple"):
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

class DatatypeDefinitionEnumeration:

    pass
class AttributeDefinitionEnumeration:

    pass
class rif12_ExchangeFile_EmbeddedValue:

    def __init__(self, key: str, otherContent: str):
        self.key = key
        self.otherContent = otherContent
        
    @property
    def otherContent(self) -> str:
        return self.__otherContent

    @otherContent.setter
    def otherContent(self, otherContent: str):
        self.__otherContent = otherContent

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class EmbeddedValue:

    pass
class EnumValue:

    pass
class AttributeValueEnumeration:

    pass
class AttributeValueComplex:

    pass
class rif12_ExchangeFile_AttributeValueXmlData(AttributeValueComplex):

    pass
class rif12_ExchangeFile_AttributeValueEmbeddedDocument(AttributeValueComplex):

    pass
class rif12_ExchangeFile_AttributeValueEmbeddedFile(AttributeValueComplex):

    pass
class rif12_ExchangeFile_AttributeValueFileReference(AttributeValueComplex):

    def __init__(self, pathToFile: str, rif12_ExchangeFile_AttributeValueFileReference: "AttributeDefinitionComplex" = None, AttributeValueComplex: "rif12_ExchangeFile_AttributeDefinitionComplex"):
        self.pathToFile = pathToFile
        self.rif12_ExchangeFile_AttributeValueFileReference = rif12_ExchangeFile_AttributeValueFileReference
        
    @property
    def pathToFile(self) -> str:
        return self.__pathToFile

    @pathToFile.setter
    def pathToFile(self, pathToFile: str):
        self.__pathToFile = pathToFile

    @property
    def rif12_ExchangeFile_AttributeValueFileReference(self):
        return self.__rif12_ExchangeFile_AttributeValueFileReference

    @rif12_ExchangeFile_AttributeValueFileReference.setter
    def rif12_ExchangeFile_AttributeValueFileReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AttributeValueFileReference__rif12_ExchangeFile_AttributeValueFileReference", None)
        self.__rif12_ExchangeFile_AttributeValueFileReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributeDefinitionComplex80"):
                opp_val = getattr(old_value, "AttributeDefinitionComplex80", None)
                if opp_val == self:
                    setattr(old_value, "AttributeDefinitionComplex80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributeDefinitionComplex80"):
                opp_val = getattr(value, "AttributeDefinitionComplex80", None)
                setattr(value, "AttributeDefinitionComplex80", self)

class DatatypeDefinitionComplex:

    pass
class rif12_ExchangeFile_DatatypeDefinitionXmlData(DatatypeDefinitionComplex):

    def __init__(self, nameSpaceURI: str, schemaLocation: str, DatatypeDefinitionComplex: "rif12_ExchangeFile_AttributeDefinitionComplex"):
        self.nameSpaceURI = nameSpaceURI
        self.schemaLocation = schemaLocation
        
    @property
    def schemaLocation(self) -> str:
        return self.__schemaLocation

    @schemaLocation.setter
    def schemaLocation(self, schemaLocation: str):
        self.__schemaLocation = schemaLocation

    @property
    def nameSpaceURI(self) -> str:
        return self.__nameSpaceURI

    @nameSpaceURI.setter
    def nameSpaceURI(self, nameSpaceURI: str):
        self.__nameSpaceURI = nameSpaceURI

class rif12_ExchangeFile_DatatypeDefinitionBinaryFile(DatatypeDefinitionComplex):

    def __init__(self, application: str, filenameSuffix: str, formatName: str, mimeType: str, DatatypeDefinitionComplex: "rif12_ExchangeFile_AttributeDefinitionComplex"):
        self.application = application
        self.filenameSuffix = filenameSuffix
        self.formatName = formatName
        self.mimeType = mimeType
        
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

    @property
    def filenameSuffix(self) -> str:
        return self.__filenameSuffix

    @filenameSuffix.setter
    def filenameSuffix(self, filenameSuffix: str):
        self.__filenameSuffix = filenameSuffix

    @property
    def mimeType(self) -> str:
        return self.__mimeType

    @mimeType.setter
    def mimeType(self, mimeType: str):
        self.__mimeType = mimeType

class rif12_ExchangeFile_DatatypeDefinitionDocument(DatatypeDefinitionComplex):

    pass
class SpecGroupHierarchy:

    pass
class SpecHierarchyRoot:

    pass
class SpecGroup:

    pass
class DatatypeDefinition:

    pass
class rif12_ExchangeFile_DatatypeDefinitionSimple(DatatypeDefinition):

    pass
class rif12_ExchangeFile_DatatypeDefinitionComplex(DatatypeDefinition):

    def __init__(self, embedded: str, DatatypeDefinition: "rif12_ExchangeFile_AccessPolicy", DatatypeDefinition93: "rif12_ExchangeFile_RIFContent"):
        self.embedded = embedded
        
    @property
    def embedded(self) -> str:
        return self.__embedded

    @embedded.setter
    def embedded(self, embedded: str):
        self.__embedded = embedded

class rif12_ExchangeFile_DatatypeDefinitionEnumeration(DatatypeDefinition):

    pass
class SpecGroupHierarchyRoot:

    pass
class SpecRelation:

    pass
class RelationGroup:

    pass
class AttributeDefinition:

    pass
class rif12_ExchangeFile_AttributeDefinitionComplex(AttributeDefinition):

    pass
class rif12_ExchangeFile_AttributeDefinitionSimple(AttributeDefinition):

    pass
class rif12_ExchangeFile_AttributeDefinitionEnumeration(AttributeDefinition):

    def __init__(self, multiValued: str, rif12_ExchangeFile_AttributeDefinitionEnumeration61: "AttributeValueEnumeration" = None, rif12_ExchangeFile_AttributeDefinitionEnumeration: "DatatypeDefinitionEnumeration" = None, AttributeDefinition: "rif12_ExchangeFile_SpecType", AttributeDefinition30: "rif12_ExchangeFile_AccessPolicy"):
        self.multiValued = multiValued
        self.rif12_ExchangeFile_AttributeDefinitionEnumeration61 = rif12_ExchangeFile_AttributeDefinitionEnumeration61
        self.rif12_ExchangeFile_AttributeDefinitionEnumeration = rif12_ExchangeFile_AttributeDefinitionEnumeration
        
    @property
    def multiValued(self) -> str:
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: str):
        self.__multiValued = multiValued

    @property
    def rif12_ExchangeFile_AttributeDefinitionEnumeration61(self):
        return self.__rif12_ExchangeFile_AttributeDefinitionEnumeration61

    @rif12_ExchangeFile_AttributeDefinitionEnumeration61.setter
    def rif12_ExchangeFile_AttributeDefinitionEnumeration61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AttributeDefinitionEnumeration__rif12_ExchangeFile_AttributeDefinitionEnumeration61", None)
        self.__rif12_ExchangeFile_AttributeDefinitionEnumeration61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributeValueEnumeration"):
                opp_val = getattr(old_value, "AttributeValueEnumeration", None)
                if opp_val == self:
                    setattr(old_value, "AttributeValueEnumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributeValueEnumeration"):
                opp_val = getattr(value, "AttributeValueEnumeration", None)
                setattr(value, "AttributeValueEnumeration", self)

    @property
    def rif12_ExchangeFile_AttributeDefinitionEnumeration(self):
        return self.__rif12_ExchangeFile_AttributeDefinitionEnumeration

    @rif12_ExchangeFile_AttributeDefinitionEnumeration.setter
    def rif12_ExchangeFile_AttributeDefinitionEnumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AttributeDefinitionEnumeration__rif12_ExchangeFile_AttributeDefinitionEnumeration", None)
        self.__rif12_ExchangeFile_AttributeDefinitionEnumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DatatypeDefinitionEnumeration"):
                opp_val = getattr(old_value, "DatatypeDefinitionEnumeration", None)
                if opp_val == self:
                    setattr(old_value, "DatatypeDefinitionEnumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DatatypeDefinitionEnumeration"):
                opp_val = getattr(value, "DatatypeDefinitionEnumeration", None)
                setattr(value, "DatatypeDefinitionEnumeration", self)

class SpecObject:

    pass
class Identifiable:

    pass
class rif12_ExchangeFile_AccessPolicy(Identifiable):

    def __init__(self, accessMode: str, rif12_ExchangeFile_AccessPolicy29: set["AttributeDefinition"] = None, rif12_ExchangeFile_AccessPolicy32: set["RelationGroup"] = None, rif12_ExchangeFile_AccessPolicy: set["SpecGroupHierarchyRoot"] = None, rif12_ExchangeFile_AccessPolicy35: set["DatatypeDefinition"] = None, rif12_ExchangeFile_AccessPolicy27: set["SpecGroup"] = None, rif12_ExchangeFile_AccessPolicy37: set["SpecRelation"] = None, rif12_ExchangeFile_AccessPolicy40: set["AttributeValue"] = None, rif12_ExchangeFile_AccessPolicy43: set["SpecType"] = None, rif12_ExchangeFile_AccessPolicy46: set["SpecHierarchy"] = None, rif12_ExchangeFile_AccessPolicy49: set["SpecObject"] = None, rif12_ExchangeFile_AccessPolicy52: set["SpecHierarchyRoot"] = None):
        self.accessMode = accessMode
        self.rif12_ExchangeFile_AccessPolicy29 = rif12_ExchangeFile_AccessPolicy29 if rif12_ExchangeFile_AccessPolicy29 is not None else set()
        self.rif12_ExchangeFile_AccessPolicy32 = rif12_ExchangeFile_AccessPolicy32 if rif12_ExchangeFile_AccessPolicy32 is not None else set()
        self.rif12_ExchangeFile_AccessPolicy = rif12_ExchangeFile_AccessPolicy if rif12_ExchangeFile_AccessPolicy is not None else set()
        self.rif12_ExchangeFile_AccessPolicy35 = rif12_ExchangeFile_AccessPolicy35 if rif12_ExchangeFile_AccessPolicy35 is not None else set()
        self.rif12_ExchangeFile_AccessPolicy27 = rif12_ExchangeFile_AccessPolicy27 if rif12_ExchangeFile_AccessPolicy27 is not None else set()
        self.rif12_ExchangeFile_AccessPolicy37 = rif12_ExchangeFile_AccessPolicy37 if rif12_ExchangeFile_AccessPolicy37 is not None else set()
        self.rif12_ExchangeFile_AccessPolicy40 = rif12_ExchangeFile_AccessPolicy40 if rif12_ExchangeFile_AccessPolicy40 is not None else set()
        self.rif12_ExchangeFile_AccessPolicy43 = rif12_ExchangeFile_AccessPolicy43 if rif12_ExchangeFile_AccessPolicy43 is not None else set()
        self.rif12_ExchangeFile_AccessPolicy46 = rif12_ExchangeFile_AccessPolicy46 if rif12_ExchangeFile_AccessPolicy46 is not None else set()
        self.rif12_ExchangeFile_AccessPolicy49 = rif12_ExchangeFile_AccessPolicy49 if rif12_ExchangeFile_AccessPolicy49 is not None else set()
        self.rif12_ExchangeFile_AccessPolicy52 = rif12_ExchangeFile_AccessPolicy52 if rif12_ExchangeFile_AccessPolicy52 is not None else set()
        
    @property
    def accessMode(self) -> str:
        return self.__accessMode

    @accessMode.setter
    def accessMode(self, accessMode: str):
        self.__accessMode = accessMode

    @property
    def rif12_ExchangeFile_AccessPolicy49(self):
        return self.__rif12_ExchangeFile_AccessPolicy49

    @rif12_ExchangeFile_AccessPolicy49.setter
    def rif12_ExchangeFile_AccessPolicy49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy49", None)
        self.__rif12_ExchangeFile_AccessPolicy49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecObject50"):
                    opp_val = getattr(item, "SpecObject50", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecObject50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecObject50"):
                    opp_val = getattr(item, "SpecObject50", None)
                    
                    setattr(item, "SpecObject50", self)
                    

    @property
    def rif12_ExchangeFile_AccessPolicy46(self):
        return self.__rif12_ExchangeFile_AccessPolicy46

    @rif12_ExchangeFile_AccessPolicy46.setter
    def rif12_ExchangeFile_AccessPolicy46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy46", None)
        self.__rif12_ExchangeFile_AccessPolicy46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecHierarchy47"):
                    opp_val = getattr(item, "SpecHierarchy47", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecHierarchy47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecHierarchy47"):
                    opp_val = getattr(item, "SpecHierarchy47", None)
                    
                    setattr(item, "SpecHierarchy47", self)
                    

    @property
    def rif12_ExchangeFile_AccessPolicy29(self):
        return self.__rif12_ExchangeFile_AccessPolicy29

    @rif12_ExchangeFile_AccessPolicy29.setter
    def rif12_ExchangeFile_AccessPolicy29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy29", None)
        self.__rif12_ExchangeFile_AccessPolicy29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeDefinition30"):
                    opp_val = getattr(item, "AttributeDefinition30", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeDefinition30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeDefinition30"):
                    opp_val = getattr(item, "AttributeDefinition30", None)
                    
                    setattr(item, "AttributeDefinition30", self)
                    

    @property
    def rif12_ExchangeFile_AccessPolicy27(self):
        return self.__rif12_ExchangeFile_AccessPolicy27

    @rif12_ExchangeFile_AccessPolicy27.setter
    def rif12_ExchangeFile_AccessPolicy27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy27", None)
        self.__rif12_ExchangeFile_AccessPolicy27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecGroup"):
                    opp_val = getattr(item, "SpecGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecGroup"):
                    opp_val = getattr(item, "SpecGroup", None)
                    
                    setattr(item, "SpecGroup", self)
                    

    @property
    def rif12_ExchangeFile_AccessPolicy(self):
        return self.__rif12_ExchangeFile_AccessPolicy

    @rif12_ExchangeFile_AccessPolicy.setter
    def rif12_ExchangeFile_AccessPolicy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy", None)
        self.__rif12_ExchangeFile_AccessPolicy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecGroupHierarchyRoot"):
                    opp_val = getattr(item, "SpecGroupHierarchyRoot", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecGroupHierarchyRoot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecGroupHierarchyRoot"):
                    opp_val = getattr(item, "SpecGroupHierarchyRoot", None)
                    
                    setattr(item, "SpecGroupHierarchyRoot", self)
                    

    @property
    def rif12_ExchangeFile_AccessPolicy35(self):
        return self.__rif12_ExchangeFile_AccessPolicy35

    @rif12_ExchangeFile_AccessPolicy35.setter
    def rif12_ExchangeFile_AccessPolicy35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy35", None)
        self.__rif12_ExchangeFile_AccessPolicy35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DatatypeDefinition"):
                    opp_val = getattr(item, "DatatypeDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "DatatypeDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DatatypeDefinition"):
                    opp_val = getattr(item, "DatatypeDefinition", None)
                    
                    setattr(item, "DatatypeDefinition", self)
                    

    @property
    def rif12_ExchangeFile_AccessPolicy32(self):
        return self.__rif12_ExchangeFile_AccessPolicy32

    @rif12_ExchangeFile_AccessPolicy32.setter
    def rif12_ExchangeFile_AccessPolicy32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy32", None)
        self.__rif12_ExchangeFile_AccessPolicy32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RelationGroup33"):
                    opp_val = getattr(item, "RelationGroup33", None)
                    
                    if opp_val == self:
                        setattr(item, "RelationGroup33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RelationGroup33"):
                    opp_val = getattr(item, "RelationGroup33", None)
                    
                    setattr(item, "RelationGroup33", self)
                    

    @property
    def rif12_ExchangeFile_AccessPolicy52(self):
        return self.__rif12_ExchangeFile_AccessPolicy52

    @rif12_ExchangeFile_AccessPolicy52.setter
    def rif12_ExchangeFile_AccessPolicy52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy52", None)
        self.__rif12_ExchangeFile_AccessPolicy52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecHierarchyRoot"):
                    opp_val = getattr(item, "SpecHierarchyRoot", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecHierarchyRoot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecHierarchyRoot"):
                    opp_val = getattr(item, "SpecHierarchyRoot", None)
                    
                    setattr(item, "SpecHierarchyRoot", self)
                    

    @property
    def rif12_ExchangeFile_AccessPolicy40(self):
        return self.__rif12_ExchangeFile_AccessPolicy40

    @rif12_ExchangeFile_AccessPolicy40.setter
    def rif12_ExchangeFile_AccessPolicy40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy40", None)
        self.__rif12_ExchangeFile_AccessPolicy40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AttributeValue41"):
                    opp_val = getattr(item, "AttributeValue41", None)
                    
                    if opp_val == self:
                        setattr(item, "AttributeValue41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AttributeValue41"):
                    opp_val = getattr(item, "AttributeValue41", None)
                    
                    setattr(item, "AttributeValue41", self)
                    

    @property
    def rif12_ExchangeFile_AccessPolicy43(self):
        return self.__rif12_ExchangeFile_AccessPolicy43

    @rif12_ExchangeFile_AccessPolicy43.setter
    def rif12_ExchangeFile_AccessPolicy43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy43", None)
        self.__rif12_ExchangeFile_AccessPolicy43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecType44"):
                    opp_val = getattr(item, "SpecType44", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecType44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecType44"):
                    opp_val = getattr(item, "SpecType44", None)
                    
                    setattr(item, "SpecType44", self)
                    

    @property
    def rif12_ExchangeFile_AccessPolicy37(self):
        return self.__rif12_ExchangeFile_AccessPolicy37

    @rif12_ExchangeFile_AccessPolicy37.setter
    def rif12_ExchangeFile_AccessPolicy37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AccessPolicy__rif12_ExchangeFile_AccessPolicy37", None)
        self.__rif12_ExchangeFile_AccessPolicy37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SpecRelation38"):
                    opp_val = getattr(item, "SpecRelation38", None)
                    
                    if opp_val == self:
                        setattr(item, "SpecRelation38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SpecRelation38"):
                    opp_val = getattr(item, "SpecRelation38", None)
                    
                    setattr(item, "SpecRelation38", self)
                    

class rif12_ExchangeFile_AttributeValue(Identifiable):

    pass
class rif12_ExchangeFile_SpecGroupHierarchy(Identifiable):

    pass
class rif12_ExchangeFile_SpecHierarchy(Identifiable):

    pass
class rif12_ExchangeFile_EnumValue(Identifiable):

    pass
class rif12_ExchangeFile_DatatypeDefinition(Identifiable):

    pass
class rif12_ExchangeFile_SpecType(Identifiable):

    pass
class rif12_ExchangeFile_RelationGroup(Identifiable):

    pass
class rif12_ExchangeFile_AttributeDefinition(Identifiable):

    pass
class rif12_ExchangeFile_SpecElementWithUserDefinedAttributes(Identifiable):

    pass
class SpecHierarchy:

    pass
class SpecElementWithUserDefinedAttributes:

    pass
class rif12_ExchangeFile_SpecObject(SpecElementWithUserDefinedAttributes):

    pass
class rif12_ExchangeFile_SpecGroup(SpecElementWithUserDefinedAttributes):

    pass
class rif12_ExchangeFile_SpecGroupHierarchyRoot(SpecElementWithUserDefinedAttributes):

    pass
class rif12_ExchangeFile_SpecRelation(SpecElementWithUserDefinedAttributes):

    pass
class rif12_ExchangeFile_SpecHierarchyRoot(SpecElementWithUserDefinedAttributes):

    pass
class rif12_ExchangeFile_Identifiable(ABC):

    def __init__(self, desc: str, identifier: str, lastChange: str, longName: str):
        self.desc = desc
        self.identifier = identifier
        self.lastChange = lastChange
        self.longName = longName
        
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

    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

class AttributeValue:

    pass
class rif12_ExchangeFile_AttributeValueComplex(AttributeValue):

    pass
class rif12_ExchangeFile_AttributeValueEnumeration(AttributeValue):

    pass
class rif12_ExchangeFile_AttributeValueSimple(AttributeValue):

    def __init__(self, theValue: str, rif12_ExchangeFile_AttributeValueSimple: "AttributeDefinitionSimple" = None, AttributeValue: "rif12_ExchangeFile_SpecElementWithUserDefinedAttributes", AttributeValue8: "rif12_ExchangeFile_SpecHierarchy", AttributeValue41: "rif12_ExchangeFile_AccessPolicy"):
        self.theValue = theValue
        self.rif12_ExchangeFile_AttributeValueSimple = rif12_ExchangeFile_AttributeValueSimple
        
    @property
    def theValue(self) -> str:
        return self.__theValue

    @theValue.setter
    def theValue(self, theValue: str):
        self.__theValue = theValue

    @property
    def rif12_ExchangeFile_AttributeValueSimple(self):
        return self.__rif12_ExchangeFile_AttributeValueSimple

    @rif12_ExchangeFile_AttributeValueSimple.setter
    def rif12_ExchangeFile_AttributeValueSimple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif12_ExchangeFile_AttributeValueSimple__rif12_ExchangeFile_AttributeValueSimple", None)
        self.__rif12_ExchangeFile_AttributeValueSimple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AttributeDefinitionSimple"):
                opp_val = getattr(old_value, "AttributeDefinitionSimple", None)
                if opp_val == self:
                    setattr(old_value, "AttributeDefinitionSimple", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AttributeDefinitionSimple"):
                opp_val = getattr(value, "AttributeDefinitionSimple", None)
                setattr(value, "AttributeDefinitionSimple", self)

class SpecType:

    pass