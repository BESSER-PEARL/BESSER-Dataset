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

class rif11a_ExchangeFile_EmbeddedValue:

    def __init__(self, key: str, otherContent: str):
        self.key = key
        self.otherContent = otherContent
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def otherContent(self):
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
class DataTypes_XhtmlContent:

    pass
class ExchangeFile_AttributeDefinitionComplex:

    pass
class AttributeValueComplex:

    pass
class rif11a_ExchangeFile_AttributeValueEmbeddedFile(AttributeValueComplex):

    pass
class rif11a_ExchangeFile_AttributeValueEmbeddedDocument(AttributeValueComplex):

    pass
class ExchangeFile_AttributeDefinitionSimple:

    pass
class ExchangeFile_AttributeValueSimple:

    pass
class ExchangeFile_DatatypeDefinitionSimple:

    pass
class ExchangeFile_DatatypeDefinition:

    pass
class ExchangeFile_SpecGroup:

    pass
class AttributeValue:

    pass
class rif11a_ExchangeFile_AttributeValueSimple(AttributeValue):

    def __init__(self, theValue: str, rif11a_ExchangeFile_AttributeValueSimple: "ExchangeFile_AttributeDefinitionSimple" = None):
        self.theValue = theValue
        self.rif11a_ExchangeFile_AttributeValueSimple = rif11a_ExchangeFile_AttributeValueSimple
        
        pass
    @property
    def theValue(self):
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
        
        pass
    @property
    def embedded(self):
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
class rif11a_ExchangeFile_AttributeDefinitionEnumeration(AttributeDefinition):

    def __init__(self, multiValued: str, rif11a_ExchangeFile_AttributeDefinitionEnumeration: "ExchangeFile_DatatypeDefinitionEnumeration" = None, rif11a_ExchangeFile_AttributeDefinitionEnumeration52: "ExchangeFile_AttributeValueEnumeration" = None):
        self.multiValued = multiValued
        self.rif11a_ExchangeFile_AttributeDefinitionEnumeration = rif11a_ExchangeFile_AttributeDefinitionEnumeration
        self.rif11a_ExchangeFile_AttributeDefinitionEnumeration52 = rif11a_ExchangeFile_AttributeDefinitionEnumeration52
        
        pass
    @property
    def multiValued(self):
        return self.__multiValued

    @multiValued.setter
    def multiValued(self, multiValued: str):
        self.__multiValued = multiValued


    @property
    def rif11a_ExchangeFile_AttributeDefinitionEnumeration52(self):
        return self.__rif11a_ExchangeFile_AttributeDefinitionEnumeration52

    @rif11a_ExchangeFile_AttributeDefinitionEnumeration52.setter
    def rif11a_ExchangeFile_AttributeDefinitionEnumeration52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AttributeDefinitionEnumeration__rif11a_ExchangeFile_AttributeDefinitionEnumeration52", None)
        self.__rif11a_ExchangeFile_AttributeDefinitionEnumeration52 = value
        
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

class rif11a_ExchangeFile_AttributeDefinitionComplex(AttributeDefinition):

    pass
class ExchangeFile_SpecHierarchyRoot:

    pass
class ExchangeFile_AttributeDefinition:

    pass
class rif11a_ExchangeFile_Identifiable(ABC):

    def __init__(self, desc: str, identifier: str, lastChange: str, longName: str):
        self.desc = desc
        self.identifier = identifier
        self.lastChange = lastChange
        self.longName = longName
        
        pass
    @property
    def longName(self):
        return self.__longName

    @longName.setter
    def longName(self, longName: str):
        self.__longName = longName


    @property
    def lastChange(self):
        return self.__lastChange

    @lastChange.setter
    def lastChange(self, lastChange: str):
        self.__lastChange = lastChange


    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc


    @property
    def identifier(self):
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
class rif11a_ExchangeFile_AccessPolicy(Identifiable):

    def __init__(self, accessMode: str, rif11a_ExchangeFile_AccessPolicy40: set["ExchangeFile_SpecHierarchy"] = None, rif11a_ExchangeFile_AccessPolicy43: set["ExchangeFile_SpecObject"] = None, rif11a_ExchangeFile_AccessPolicy46: set["ExchangeFile_SpecHierarchyRoot"] = None, rif11a_ExchangeFile_AccessPolicy: set["ExchangeFile_SpecGroup"] = None, rif11a_ExchangeFile_AccessPolicy24: set["ExchangeFile_AttributeDefinition"] = None, rif11a_ExchangeFile_AccessPolicy27: set["ExchangeFile_RelationGroup"] = None, rif11a_ExchangeFile_AccessPolicy29: set["ExchangeFile_DatatypeDefinition"] = None, rif11a_ExchangeFile_AccessPolicy31: set["ExchangeFile_SpecRelation"] = None, rif11a_ExchangeFile_AccessPolicy34: set["ExchangeFile_AttributeValue"] = None, rif11a_ExchangeFile_AccessPolicy37: set["ExchangeFile_SpecType"] = None):
        self.accessMode = accessMode
        self.rif11a_ExchangeFile_AccessPolicy40 = rif11a_ExchangeFile_AccessPolicy40 if rif11a_ExchangeFile_AccessPolicy40 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy43 = rif11a_ExchangeFile_AccessPolicy43 if rif11a_ExchangeFile_AccessPolicy43 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy46 = rif11a_ExchangeFile_AccessPolicy46 if rif11a_ExchangeFile_AccessPolicy46 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy = rif11a_ExchangeFile_AccessPolicy if rif11a_ExchangeFile_AccessPolicy is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy24 = rif11a_ExchangeFile_AccessPolicy24 if rif11a_ExchangeFile_AccessPolicy24 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy27 = rif11a_ExchangeFile_AccessPolicy27 if rif11a_ExchangeFile_AccessPolicy27 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy29 = rif11a_ExchangeFile_AccessPolicy29 if rif11a_ExchangeFile_AccessPolicy29 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy31 = rif11a_ExchangeFile_AccessPolicy31 if rif11a_ExchangeFile_AccessPolicy31 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy34 = rif11a_ExchangeFile_AccessPolicy34 if rif11a_ExchangeFile_AccessPolicy34 is not None else set()
        self.rif11a_ExchangeFile_AccessPolicy37 = rif11a_ExchangeFile_AccessPolicy37 if rif11a_ExchangeFile_AccessPolicy37 is not None else set()
        
        pass
    @property
    def accessMode(self):
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
    def rif11a_ExchangeFile_AccessPolicy40(self):
        return self.__rif11a_ExchangeFile_AccessPolicy40

    @rif11a_ExchangeFile_AccessPolicy40.setter
    def rif11a_ExchangeFile_AccessPolicy40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy40", None)
        self.__rif11a_ExchangeFile_AccessPolicy40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecHierarchy41"):
                    opp_val = getattr(item, "ExchangeFile_SpecHierarchy41", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecHierarchy41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecHierarchy41"):
                    opp_val = getattr(item, "ExchangeFile_SpecHierarchy41", None)
                    
                    setattr(item, "ExchangeFile_SpecHierarchy41", self)
                    

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
                if hasattr(item, "ExchangeFile_SpecRelation32"):
                    opp_val = getattr(item, "ExchangeFile_SpecRelation32", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecRelation32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecRelation32"):
                    opp_val = getattr(item, "ExchangeFile_SpecRelation32", None)
                    
                    setattr(item, "ExchangeFile_SpecRelation32", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy34(self):
        return self.__rif11a_ExchangeFile_AccessPolicy34

    @rif11a_ExchangeFile_AccessPolicy34.setter
    def rif11a_ExchangeFile_AccessPolicy34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy34", None)
        self.__rif11a_ExchangeFile_AccessPolicy34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_AttributeValue35"):
                    opp_val = getattr(item, "ExchangeFile_AttributeValue35", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_AttributeValue35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_AttributeValue35"):
                    opp_val = getattr(item, "ExchangeFile_AttributeValue35", None)
                    
                    setattr(item, "ExchangeFile_AttributeValue35", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy37(self):
        return self.__rif11a_ExchangeFile_AccessPolicy37

    @rif11a_ExchangeFile_AccessPolicy37.setter
    def rif11a_ExchangeFile_AccessPolicy37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy37", None)
        self.__rif11a_ExchangeFile_AccessPolicy37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecType38"):
                    opp_val = getattr(item, "ExchangeFile_SpecType38", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecType38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecType38"):
                    opp_val = getattr(item, "ExchangeFile_SpecType38", None)
                    
                    setattr(item, "ExchangeFile_SpecType38", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy43(self):
        return self.__rif11a_ExchangeFile_AccessPolicy43

    @rif11a_ExchangeFile_AccessPolicy43.setter
    def rif11a_ExchangeFile_AccessPolicy43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy43", None)
        self.__rif11a_ExchangeFile_AccessPolicy43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecObject44"):
                    opp_val = getattr(item, "ExchangeFile_SpecObject44", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecObject44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecObject44"):
                    opp_val = getattr(item, "ExchangeFile_SpecObject44", None)
                    
                    setattr(item, "ExchangeFile_SpecObject44", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy24(self):
        return self.__rif11a_ExchangeFile_AccessPolicy24

    @rif11a_ExchangeFile_AccessPolicy24.setter
    def rif11a_ExchangeFile_AccessPolicy24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy24", None)
        self.__rif11a_ExchangeFile_AccessPolicy24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_AttributeDefinition25"):
                    opp_val = getattr(item, "ExchangeFile_AttributeDefinition25", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_AttributeDefinition25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_AttributeDefinition25"):
                    opp_val = getattr(item, "ExchangeFile_AttributeDefinition25", None)
                    
                    setattr(item, "ExchangeFile_AttributeDefinition25", self)
                    

    @property
    def rif11a_ExchangeFile_AccessPolicy46(self):
        return self.__rif11a_ExchangeFile_AccessPolicy46

    @rif11a_ExchangeFile_AccessPolicy46.setter
    def rif11a_ExchangeFile_AccessPolicy46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy46", None)
        self.__rif11a_ExchangeFile_AccessPolicy46 = value if value is not None else set()
        
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
    def rif11a_ExchangeFile_AccessPolicy27(self):
        return self.__rif11a_ExchangeFile_AccessPolicy27

    @rif11a_ExchangeFile_AccessPolicy27.setter
    def rif11a_ExchangeFile_AccessPolicy27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_AccessPolicy__rif11a_ExchangeFile_AccessPolicy27", None)
        self.__rif11a_ExchangeFile_AccessPolicy27 = value if value is not None else set()
        
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
                    

class rif11a_ExchangeFile_SpecType(Identifiable):

    pass
class rif11a_ExchangeFile_AttributeValue(Identifiable):

    pass
class rif11a_ExchangeFile_AttributeDefinition(Identifiable):

    pass
class rif11a_ExchangeFile_EnumValue(Identifiable):

    pass
class rif11a_ExchangeFile_DatatypeDefinition(Identifiable):

    pass
class rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes(Identifiable):

    pass
class ExchangeFile_SpecHierarchy:

    pass
class ExchangeFile_SpecRelation:

    pass
class rif11a_ExchangeFile_RelationGroup(Identifiable):

    pass
class ExchangeFile_RelationGroup:

    pass
class ExchangeFile_SpecObject:

    pass
class rif11a_ExchangeFile_SpecHierarchy(Identifiable):

    pass
class SpecElementWithUserDefinedAttributes:

    pass
class rif11a_ExchangeFile_SpecObject(SpecElementWithUserDefinedAttributes):

    pass
class rif11a_ExchangeFile_SpecRelation(SpecElementWithUserDefinedAttributes):

    pass
class rif11a_ExchangeFile_SpecGroup(SpecElementWithUserDefinedAttributes):

    pass
class rif11a_ExchangeFile_SpecHierarchyRoot(SpecElementWithUserDefinedAttributes):

    pass
class rif11a_DataTypes_BinaryContent:

    pass
class ExchangeFile_AccessPolicy:

    pass
class rif11a_DataTypes_XhtmlContent:

    pass
class rif11a_DataTypes_XmlContent:

    pass
class DatatypeDefinitionSimple:

    pass
class rif11a_ExchangeFile_DatatypeDefinitionDate(DatatypeDefinitionSimple):

    def __init__(self, format: str):
        self.format = format
        
        pass
    @property
    def format(self):
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format


class rif11a_ExchangeFile_DatatypeDefinitionBoolean(DatatypeDefinitionSimple):

    pass
class DatatypeDefinitionComplex:

    pass
class rif11a_ExchangeFile_DatatypeDefinitionDocument(DatatypeDefinitionComplex):

    pass
class rif11a_ExchangeFile_DatatypeDefinitionBinaryFile(DatatypeDefinitionComplex):

    def __init__(self, application: str, filenameSuffix: str, formatName: str, mimeType: str):
        self.application = application
        self.filenameSuffix = filenameSuffix
        self.formatName = formatName
        self.mimeType = mimeType
        
        pass
    @property
    def formatName(self):
        return self.__formatName

    @formatName.setter
    def formatName(self, formatName: str):
        self.__formatName = formatName


    @property
    def application(self):
        return self.__application

    @application.setter
    def application(self, application: str):
        self.__application = application


    @property
    def mimeType(self):
        return self.__mimeType

    @mimeType.setter
    def mimeType(self, mimeType: str):
        self.__mimeType = mimeType


    @property
    def filenameSuffix(self):
        return self.__filenameSuffix

    @filenameSuffix.setter
    def filenameSuffix(self, filenameSuffix: str):
        self.__filenameSuffix = filenameSuffix


class DataTypes_XmlContent:

    pass
class rif11a_ExchangeFile_AttributeValueXmlData(AttributeValueComplex):

    pass
class rif11a_ExchangeFile_AttributeValueFileReference(AttributeValueComplex):

    def __init__(self, pathToFile: str, rif11a_ExchangeFile_AttributeValueFileReference: "ExchangeFile_AttributeDefinitionComplex" = None):
        self.pathToFile = pathToFile
        self.rif11a_ExchangeFile_AttributeValueFileReference = rif11a_ExchangeFile_AttributeValueFileReference
        
        pass
    @property
    def pathToFile(self):
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
            if hasattr(old_value, "ExchangeFile_AttributeDefinitionComplex71"):
                opp_val = getattr(old_value, "ExchangeFile_AttributeDefinitionComplex71", None)
                if opp_val == self:
                    setattr(old_value, "ExchangeFile_AttributeDefinitionComplex71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExchangeFile_AttributeDefinitionComplex71"):
                opp_val = getattr(value, "ExchangeFile_AttributeDefinitionComplex71", None)
                setattr(value, "ExchangeFile_AttributeDefinitionComplex71", self)

class DataTypes_BinaryContent:

    pass
class rif11a_ExchangeFile_RIF:

    def __init__(self, author: str, comment: str, countryCode: str, creationTime: str, identifier: str, sourceToolId: str, title: str, version: str, rif11a_ExchangeFile_RIF: set["ExchangeFile_AccessPolicy"] = None, rif11a_ExchangeFile_RIF78: set["ExchangeFile_DatatypeDefinition"] = None, rif11a_ExchangeFile_RIF81: set["ExchangeFile_SpecHierarchyRoot"] = None, rif11a_ExchangeFile_RIF84: set["ExchangeFile_SpecObject"] = None, rif11a_ExchangeFile_RIF87: set["ExchangeFile_SpecGroup"] = None, rif11a_ExchangeFile_RIF90: set["ExchangeFile_SpecType"] = None, rif11a_ExchangeFile_RIF93: set["ExchangeFile_SpecRelation"] = None):
        self.author = author
        self.comment = comment
        self.countryCode = countryCode
        self.creationTime = creationTime
        self.identifier = identifier
        self.sourceToolId = sourceToolId
        self.title = title
        self.version = version
        self.rif11a_ExchangeFile_RIF = rif11a_ExchangeFile_RIF if rif11a_ExchangeFile_RIF is not None else set()
        self.rif11a_ExchangeFile_RIF78 = rif11a_ExchangeFile_RIF78 if rif11a_ExchangeFile_RIF78 is not None else set()
        self.rif11a_ExchangeFile_RIF81 = rif11a_ExchangeFile_RIF81 if rif11a_ExchangeFile_RIF81 is not None else set()
        self.rif11a_ExchangeFile_RIF84 = rif11a_ExchangeFile_RIF84 if rif11a_ExchangeFile_RIF84 is not None else set()
        self.rif11a_ExchangeFile_RIF87 = rif11a_ExchangeFile_RIF87 if rif11a_ExchangeFile_RIF87 is not None else set()
        self.rif11a_ExchangeFile_RIF90 = rif11a_ExchangeFile_RIF90 if rif11a_ExchangeFile_RIF90 is not None else set()
        self.rif11a_ExchangeFile_RIF93 = rif11a_ExchangeFile_RIF93 if rif11a_ExchangeFile_RIF93 is not None else set()
        
        pass
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def creationTime(self):
        return self.__creationTime

    @creationTime.setter
    def creationTime(self, creationTime: str):
        self.__creationTime = creationTime


    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def countryCode(self):
        return self.__countryCode

    @countryCode.setter
    def countryCode(self, countryCode: str):
        self.__countryCode = countryCode


    @property
    def sourceToolId(self):
        return self.__sourceToolId

    @sourceToolId.setter
    def sourceToolId(self, sourceToolId: str):
        self.__sourceToolId = sourceToolId


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


    @property
    def rif11a_ExchangeFile_RIF90(self):
        return self.__rif11a_ExchangeFile_RIF90

    @rif11a_ExchangeFile_RIF90.setter
    def rif11a_ExchangeFile_RIF90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF90", None)
        self.__rif11a_ExchangeFile_RIF90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecType91"):
                    opp_val = getattr(item, "ExchangeFile_SpecType91", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecType91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecType91"):
                    opp_val = getattr(item, "ExchangeFile_SpecType91", None)
                    
                    setattr(item, "ExchangeFile_SpecType91", self)
                    

    @property
    def rif11a_ExchangeFile_RIF78(self):
        return self.__rif11a_ExchangeFile_RIF78

    @rif11a_ExchangeFile_RIF78.setter
    def rif11a_ExchangeFile_RIF78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF78", None)
        self.__rif11a_ExchangeFile_RIF78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_DatatypeDefinition79"):
                    opp_val = getattr(item, "ExchangeFile_DatatypeDefinition79", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_DatatypeDefinition79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_DatatypeDefinition79"):
                    opp_val = getattr(item, "ExchangeFile_DatatypeDefinition79", None)
                    
                    setattr(item, "ExchangeFile_DatatypeDefinition79", self)
                    

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
    def rif11a_ExchangeFile_RIF93(self):
        return self.__rif11a_ExchangeFile_RIF93

    @rif11a_ExchangeFile_RIF93.setter
    def rif11a_ExchangeFile_RIF93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF93", None)
        self.__rif11a_ExchangeFile_RIF93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecRelation94"):
                    opp_val = getattr(item, "ExchangeFile_SpecRelation94", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecRelation94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecRelation94"):
                    opp_val = getattr(item, "ExchangeFile_SpecRelation94", None)
                    
                    setattr(item, "ExchangeFile_SpecRelation94", self)
                    

    @property
    def rif11a_ExchangeFile_RIF87(self):
        return self.__rif11a_ExchangeFile_RIF87

    @rif11a_ExchangeFile_RIF87.setter
    def rif11a_ExchangeFile_RIF87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF87", None)
        self.__rif11a_ExchangeFile_RIF87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecGroup88"):
                    opp_val = getattr(item, "ExchangeFile_SpecGroup88", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecGroup88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecGroup88"):
                    opp_val = getattr(item, "ExchangeFile_SpecGroup88", None)
                    
                    setattr(item, "ExchangeFile_SpecGroup88", self)
                    

    @property
    def rif11a_ExchangeFile_RIF84(self):
        return self.__rif11a_ExchangeFile_RIF84

    @rif11a_ExchangeFile_RIF84.setter
    def rif11a_ExchangeFile_RIF84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF84", None)
        self.__rif11a_ExchangeFile_RIF84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecObject85"):
                    opp_val = getattr(item, "ExchangeFile_SpecObject85", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecObject85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecObject85"):
                    opp_val = getattr(item, "ExchangeFile_SpecObject85", None)
                    
                    setattr(item, "ExchangeFile_SpecObject85", self)
                    

    @property
    def rif11a_ExchangeFile_RIF81(self):
        return self.__rif11a_ExchangeFile_RIF81

    @rif11a_ExchangeFile_RIF81.setter
    def rif11a_ExchangeFile_RIF81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rif11a_ExchangeFile_RIF__rif11a_ExchangeFile_RIF81", None)
        self.__rif11a_ExchangeFile_RIF81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExchangeFile_SpecHierarchyRoot82"):
                    opp_val = getattr(item, "ExchangeFile_SpecHierarchyRoot82", None)
                    
                    if opp_val == self:
                        setattr(item, "ExchangeFile_SpecHierarchyRoot82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExchangeFile_SpecHierarchyRoot82"):
                    opp_val = getattr(item, "ExchangeFile_SpecHierarchyRoot82", None)
                    
                    setattr(item, "ExchangeFile_SpecHierarchyRoot82", self)
                    

class rif11a_ExchangeFile_DatatypeDefinitionXmlData(DatatypeDefinitionComplex):

    def __init__(self, nameSpaceURI: str, schemaLocation: str):
        self.nameSpaceURI = nameSpaceURI
        self.schemaLocation = schemaLocation
        
        pass
    @property
    def nameSpaceURI(self):
        return self.__nameSpaceURI

    @nameSpaceURI.setter
    def nameSpaceURI(self, nameSpaceURI: str):
        self.__nameSpaceURI = nameSpaceURI


    @property
    def schemaLocation(self):
        return self.__schemaLocation

    @schemaLocation.setter
    def schemaLocation(self, schemaLocation: str):
        self.__schemaLocation = schemaLocation


class rif11a_ExchangeFile_DatatypeDefinitionString(DatatypeDefinitionSimple):

    def __init__(self, maxLength: str):
        self.maxLength = maxLength
        
        pass
    @property
    def maxLength(self):
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: str):
        self.__maxLength = maxLength


class rif11a_ExchangeFile_DatatypeDefinitionReal(DatatypeDefinitionSimple):

    def __init__(self, accuracy: str, max: str, min: str):
        self.accuracy = accuracy
        self.max = max
        self.min = min
        
        pass
    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max


    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min


    @property
    def accuracy(self):
        return self.__accuracy

    @accuracy.setter
    def accuracy(self, accuracy: str):
        self.__accuracy = accuracy


class rif11a_ExchangeFile_DatatypeDefinitionInteger(DatatypeDefinitionSimple):

    def __init__(self, max: str, min: str):
        self.max = max
        self.min = min
        
        pass
    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max


    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min


class rif11a_ExchangeFile_AttributeDefinitionSimple(AttributeDefinition):

    pass
class ExchangeFile_AttributeDefinitionEnumeration:

    pass