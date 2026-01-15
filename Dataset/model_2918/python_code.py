from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class isHasChoices(Enum):
    isA = "isA"
    hasA = "hasA"
class DatabaseTechnologies(Enum):
    MySql = "MySql"
    Oracle = "Oracle"
class OrmTechnologies(Enum):
    DataMapper = "DataMapper"
    Idiorm = "Idiorm"
    Kohana = "Kohana"
    DoctrineORM = "DoctrineORM"
    DoctrineODM = "DoctrineODM"
    JPA = "JPA"
class Cardinality(Enum):
    Optional = "Optional"
    Required = "Required"
    Many = "Many"
class DateDetails(Enum):
    DateOnly = "DateOnly"
    TimeOnly = "TimeOnly"
    DateAndTime = "DateAndTime"


############################################
# Definition of Classes
############################################

class Association:

    pass
class persistence_AssociationWithContainment(Association):

    def __init__(self, sourceVisible: bool):
        self.sourceVisible = sourceVisible
        
    @property
    def sourceVisible(self) -> bool:
        return self.__sourceVisible

    @sourceVisible.setter
    def sourceVisible(self, sourceVisible: bool):
        self.__sourceVisible = sourceVisible

class persistence_AssociationWithoutContainment(Association):

    def __init__(self, targetCardinality: str, targetUnique: bool):
        self.targetCardinality = targetCardinality
        self.targetUnique = targetUnique
        
    @property
    def targetUnique(self) -> bool:
        return self.__targetUnique

    @targetUnique.setter
    def targetUnique(self, targetUnique: bool):
        self.__targetUnique = targetUnique

    @property
    def targetCardinality(self) -> str:
        return self.__targetCardinality

    @targetCardinality.setter
    def targetCardinality(self, targetCardinality: str):
        self.__targetCardinality = targetCardinality

class Attribute:

    pass
class persistence_DateAttribute(Attribute):

    def __init__(self, details: str, format: str):
        self.details = details
        self.format = format
        
    @property
    def details(self) -> str:
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class persistence_ResourceAttribute(Attribute):

    def __init__(self, maximumUploadSize: int, validUploadMimeTypes: str, validUploadExtensions: str, uploadsWithinWebsite: bool, persistence_ResourceAttribute: set["persistence_PathElement"] = None):
        self.maximumUploadSize = maximumUploadSize
        self.validUploadMimeTypes = validUploadMimeTypes
        self.validUploadExtensions = validUploadExtensions
        self.uploadsWithinWebsite = uploadsWithinWebsite
        self.persistence_ResourceAttribute = persistence_ResourceAttribute if persistence_ResourceAttribute is not None else set()
        
    @property
    def validUploadExtensions(self) -> str:
        return self.__validUploadExtensions

    @validUploadExtensions.setter
    def validUploadExtensions(self, validUploadExtensions: str):
        self.__validUploadExtensions = validUploadExtensions

    @property
    def validUploadMimeTypes(self) -> str:
        return self.__validUploadMimeTypes

    @validUploadMimeTypes.setter
    def validUploadMimeTypes(self, validUploadMimeTypes: str):
        self.__validUploadMimeTypes = validUploadMimeTypes

    @property
    def uploadsWithinWebsite(self) -> bool:
        return self.__uploadsWithinWebsite

    @uploadsWithinWebsite.setter
    def uploadsWithinWebsite(self, uploadsWithinWebsite: bool):
        self.__uploadsWithinWebsite = uploadsWithinWebsite

    @property
    def maximumUploadSize(self) -> int:
        return self.__maximumUploadSize

    @maximumUploadSize.setter
    def maximumUploadSize(self, maximumUploadSize: int):
        self.__maximumUploadSize = maximumUploadSize

    @property
    def persistence_ResourceAttribute(self):
        return self.__persistence_ResourceAttribute

    @persistence_ResourceAttribute.setter
    def persistence_ResourceAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ResourceAttribute__persistence_ResourceAttribute", None)
        self.__persistence_ResourceAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_PathElement"):
                    opp_val = getattr(item, "persistence_PathElement", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_PathElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_PathElement"):
                    opp_val = getattr(item, "persistence_PathElement", None)
                    
                    setattr(item, "persistence_PathElement", self)
                    

class persistence_LocationAttribute(Attribute):

    pass
class persistence_UrlAttribute(Attribute):

    def __init__(self, displayValue: str):
        self.displayValue = displayValue
        
    @property
    def displayValue(self) -> str:
        return self.__displayValue

    @displayValue.setter
    def displayValue(self, displayValue: str):
        self.__displayValue = displayValue

class persistence_DataTypeAttribute(Attribute):

    def __init__(self, obfuscateFormFields: bool, caseInsensitive: bool, encrypt: bool, persistence_DataTypeAttribute: "persistence_DataType" = None):
        self.obfuscateFormFields = obfuscateFormFields
        self.caseInsensitive = caseInsensitive
        self.encrypt = encrypt
        self.persistence_DataTypeAttribute = persistence_DataTypeAttribute
        
    @property
    def obfuscateFormFields(self) -> bool:
        return self.__obfuscateFormFields

    @obfuscateFormFields.setter
    def obfuscateFormFields(self, obfuscateFormFields: bool):
        self.__obfuscateFormFields = obfuscateFormFields

    @property
    def caseInsensitive(self) -> bool:
        return self.__caseInsensitive

    @caseInsensitive.setter
    def caseInsensitive(self, caseInsensitive: bool):
        self.__caseInsensitive = caseInsensitive

    @property
    def encrypt(self) -> bool:
        return self.__encrypt

    @encrypt.setter
    def encrypt(self, encrypt: bool):
        self.__encrypt = encrypt

    @property
    def persistence_DataTypeAttribute(self):
        return self.__persistence_DataTypeAttribute

    @persistence_DataTypeAttribute.setter
    def persistence_DataTypeAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_DataTypeAttribute__persistence_DataTypeAttribute", None)
        self.__persistence_DataTypeAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_DataType55"):
                opp_val = getattr(old_value, "persistence_DataType55", None)
                if opp_val == self:
                    setattr(old_value, "persistence_DataType55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_DataType55"):
                opp_val = getattr(value, "persistence_DataType55", None)
                setattr(value, "persistence_DataType55", self)

class ResourceAttribute:

    pass
class persistence_ImageAttribute(ResourceAttribute):

    pass
class persistence_FileAttribute(ResourceAttribute):

    pass
class PathElement:

    pass
class persistence_DatePathElement(PathElement):

    def __init__(self, format: str):
        self.format = format
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class persistence_StaticPathElement(PathElement):

    def __init__(self, element: str):
        self.element = element
        
    @property
    def element(self) -> str:
        return self.__element

    @element.setter
    def element(self, element: str):
        self.__element = element

class persistence_PathElement(ABC):

    pass
class ModelLabelFeature:

    pass
class persistence_ModelLabelAssociation(ModelLabelFeature):

    def __init__(self, isSourceAssociation: bool, persistence_ModelLabelAssociation26: "persistence_ModelLabel" = None, persistence_ModelLabelAssociation: "persistence_Association" = None):
        self.isSourceAssociation = isSourceAssociation
        self.persistence_ModelLabelAssociation26 = persistence_ModelLabelAssociation26
        self.persistence_ModelLabelAssociation = persistence_ModelLabelAssociation
        
    @property
    def isSourceAssociation(self) -> bool:
        return self.__isSourceAssociation

    @isSourceAssociation.setter
    def isSourceAssociation(self, isSourceAssociation: bool):
        self.__isSourceAssociation = isSourceAssociation

    @property
    def persistence_ModelLabelAssociation26(self):
        return self.__persistence_ModelLabelAssociation26

    @persistence_ModelLabelAssociation26.setter
    def persistence_ModelLabelAssociation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabelAssociation__persistence_ModelLabelAssociation26", None)
        self.__persistence_ModelLabelAssociation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_ModelLabel27"):
                opp_val = getattr(old_value, "persistence_ModelLabel27", None)
                if opp_val == self:
                    setattr(old_value, "persistence_ModelLabel27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_ModelLabel27"):
                opp_val = getattr(value, "persistence_ModelLabel27", None)
                setattr(value, "persistence_ModelLabel27", self)

    @property
    def persistence_ModelLabelAssociation(self):
        return self.__persistence_ModelLabelAssociation

    @persistence_ModelLabelAssociation.setter
    def persistence_ModelLabelAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabelAssociation__persistence_ModelLabelAssociation", None)
        self.__persistence_ModelLabelAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Association"):
                opp_val = getattr(old_value, "persistence_Association", None)
                if opp_val == self:
                    setattr(old_value, "persistence_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Association"):
                opp_val = getattr(value, "persistence_Association", None)
                setattr(value, "persistence_Association", self)

class persistence_ModelLabelAttribute(ModelLabelFeature):

    def __init__(self, dateFormat: str, persistence_ModelLabelAttribute: "persistence_Attribute" = None):
        self.dateFormat = dateFormat
        self.persistence_ModelLabelAttribute = persistence_ModelLabelAttribute
        
    @property
    def dateFormat(self) -> str:
        return self.__dateFormat

    @dateFormat.setter
    def dateFormat(self, dateFormat: str):
        self.__dateFormat = dateFormat

    @property
    def persistence_ModelLabelAttribute(self):
        return self.__persistence_ModelLabelAttribute

    @persistence_ModelLabelAttribute.setter
    def persistence_ModelLabelAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabelAttribute__persistence_ModelLabelAttribute", None)
        self.__persistence_ModelLabelAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Attribute23"):
                opp_val = getattr(old_value, "persistence_Attribute23", None)
                if opp_val == self:
                    setattr(old_value, "persistence_Attribute23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Attribute23"):
                opp_val = getattr(value, "persistence_Attribute23", None)
                setattr(value, "persistence_Attribute23", self)

class persistence_ModelLabelFeature(ABC):

    pass
class Classifier:

    pass
class persistence_AssociationKey:

    pass
class persistence_Label(ABC):

    pass
class Label:

    pass
class Feature:

    pass
class persistence_Association(Feature):

    def __init__(self, targetHeaderClass: str, targetInputClass: str, targetDisplayClass: str, targetFooterClass: str, pseudo: bool, inputColumnClass: str, inputElementClass: str, serializationMaxDepth: int, bidirectional: bool, unique: bool, pivotTableName: str, targetFeatureName: str, targetPrimaryKey: bool, targetColumnName: str, targetDisplayLabel: str, keyFor: set["persistence_AssociationKey"] = None, associationEnds: "persistence_Entity" = None, persistence_Association: "persistence_ModelLabelAssociation" = None, persistence_Association35: "persistence_Entity" = None, Association: "persistence_Entity" = None, persistence_Association42: "persistence_Entity" = None, Association58: "persistence_AssociationKey" = None):
        self.targetHeaderClass = targetHeaderClass
        self.targetInputClass = targetInputClass
        self.targetDisplayClass = targetDisplayClass
        self.targetFooterClass = targetFooterClass
        self.pseudo = pseudo
        self.inputColumnClass = inputColumnClass
        self.inputElementClass = inputElementClass
        self.serializationMaxDepth = serializationMaxDepth
        self.bidirectional = bidirectional
        self.unique = unique
        self.pivotTableName = pivotTableName
        self.targetFeatureName = targetFeatureName
        self.targetPrimaryKey = targetPrimaryKey
        self.targetColumnName = targetColumnName
        self.targetDisplayLabel = targetDisplayLabel
        self.keyFor = keyFor if keyFor is not None else set()
        self.associationEnds = associationEnds
        self.persistence_Association = persistence_Association
        self.persistence_Association35 = persistence_Association35
        self.Association = Association
        self.persistence_Association42 = persistence_Association42
        self.Association58 = Association58
        
    @property
    def targetFeatureName(self) -> str:
        return self.__targetFeatureName

    @targetFeatureName.setter
    def targetFeatureName(self, targetFeatureName: str):
        self.__targetFeatureName = targetFeatureName

    @property
    def targetDisplayLabel(self) -> str:
        return self.__targetDisplayLabel

    @targetDisplayLabel.setter
    def targetDisplayLabel(self, targetDisplayLabel: str):
        self.__targetDisplayLabel = targetDisplayLabel

    @property
    def targetColumnName(self) -> str:
        return self.__targetColumnName

    @targetColumnName.setter
    def targetColumnName(self, targetColumnName: str):
        self.__targetColumnName = targetColumnName

    @property
    def inputElementClass(self) -> str:
        return self.__inputElementClass

    @inputElementClass.setter
    def inputElementClass(self, inputElementClass: str):
        self.__inputElementClass = inputElementClass

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def pseudo(self) -> bool:
        return self.__pseudo

    @pseudo.setter
    def pseudo(self, pseudo: bool):
        self.__pseudo = pseudo

    @property
    def targetFooterClass(self) -> str:
        return self.__targetFooterClass

    @targetFooterClass.setter
    def targetFooterClass(self, targetFooterClass: str):
        self.__targetFooterClass = targetFooterClass

    @property
    def targetHeaderClass(self) -> str:
        return self.__targetHeaderClass

    @targetHeaderClass.setter
    def targetHeaderClass(self, targetHeaderClass: str):
        self.__targetHeaderClass = targetHeaderClass

    @property
    def targetInputClass(self) -> str:
        return self.__targetInputClass

    @targetInputClass.setter
    def targetInputClass(self, targetInputClass: str):
        self.__targetInputClass = targetInputClass

    @property
    def pivotTableName(self) -> str:
        return self.__pivotTableName

    @pivotTableName.setter
    def pivotTableName(self, pivotTableName: str):
        self.__pivotTableName = pivotTableName

    @property
    def serializationMaxDepth(self) -> int:
        return self.__serializationMaxDepth

    @serializationMaxDepth.setter
    def serializationMaxDepth(self, serializationMaxDepth: int):
        self.__serializationMaxDepth = serializationMaxDepth

    @property
    def targetDisplayClass(self) -> str:
        return self.__targetDisplayClass

    @targetDisplayClass.setter
    def targetDisplayClass(self, targetDisplayClass: str):
        self.__targetDisplayClass = targetDisplayClass

    @property
    def inputColumnClass(self) -> str:
        return self.__inputColumnClass

    @inputColumnClass.setter
    def inputColumnClass(self, inputColumnClass: str):
        self.__inputColumnClass = inputColumnClass

    @property
    def bidirectional(self) -> bool:
        return self.__bidirectional

    @bidirectional.setter
    def bidirectional(self, bidirectional: bool):
        self.__bidirectional = bidirectional

    @property
    def targetPrimaryKey(self) -> bool:
        return self.__targetPrimaryKey

    @targetPrimaryKey.setter
    def targetPrimaryKey(self, targetPrimaryKey: bool):
        self.__targetPrimaryKey = targetPrimaryKey

    @property
    def persistence_Association35(self):
        return self.__persistence_Association35

    @persistence_Association35.setter
    def persistence_Association35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__persistence_Association35", None)
        self.__persistence_Association35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Entity34"):
                opp_val = getattr(old_value, "persistence_Entity34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Entity34"):
                opp_val = getattr(value, "persistence_Entity34", None)
                if opp_val is None:
                    setattr(value, "persistence_Entity34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Association(self):
        return self.__persistence_Association

    @persistence_Association.setter
    def persistence_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__persistence_Association", None)
        self.__persistence_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_ModelLabelAssociation"):
                opp_val = getattr(old_value, "persistence_ModelLabelAssociation", None)
                if opp_val == self:
                    setattr(old_value, "persistence_ModelLabelAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_ModelLabelAssociation"):
                opp_val = getattr(value, "persistence_ModelLabelAssociation", None)
                setattr(value, "persistence_ModelLabelAssociation", self)

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetEntity"):
                opp_val = getattr(old_value, "targetEntity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetEntity"):
                opp_val = getattr(value, "targetEntity", None)
                if opp_val is None:
                    setattr(value, "targetEntity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Association58(self):
        return self.__Association58

    @Association58.setter
    def Association58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__Association58", None)
        self.__Association58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "keys"):
                opp_val = getattr(old_value, "keys", None)
                if opp_val == self:
                    setattr(old_value, "keys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "keys"):
                opp_val = getattr(value, "keys", None)
                setattr(value, "keys", self)

    @property
    def associationEnds(self):
        return self.__associationEnds

    @associationEnds.setter
    def associationEnds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__associationEnds", None)
        self.__associationEnds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity14"):
                opp_val = getattr(old_value, "Entity14", None)
                if opp_val == self:
                    setattr(old_value, "Entity14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity14"):
                opp_val = getattr(value, "Entity14", None)
                setattr(value, "Entity14", self)

    @property
    def keyFor(self):
        return self.__keyFor

    @keyFor.setter
    def keyFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__keyFor", None)
        self.__keyFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssociationKey"):
                    opp_val = getattr(item, "AssociationKey", None)
                    
                    if opp_val == self:
                        setattr(item, "AssociationKey", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssociationKey"):
                    opp_val = getattr(item, "AssociationKey", None)
                    
                    setattr(item, "AssociationKey", self)
                    

    @property
    def persistence_Association42(self):
        return self.__persistence_Association42

    @persistence_Association42.setter
    def persistence_Association42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__persistence_Association42", None)
        self.__persistence_Association42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Entity41"):
                opp_val = getattr(old_value, "persistence_Entity41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Entity41"):
                opp_val = getattr(value, "persistence_Entity41", None)
                if opp_val is None:
                    setattr(value, "persistence_Entity41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class persistence_Attribute(Feature, Label):

    def __init__(self, placeholder: str, validationPattern: str, inputColumnClass: str, inputElementClass: str, hidden: bool, containerUnique: bool, persistentType: str, ormType: str, interfaceType: str, unique: bool, persistence_Attribute11: "persistence_Expression" = None, persistence_Attribute: "persistence_Attribute" = None, persistence_Attribute8: set["persistence_Attribute"] = None, persistence_Attribute23: "persistence_ModelLabelAttribute" = None, persistence_Attribute32: "persistence_Entity" = None):
        self.placeholder = placeholder
        self.validationPattern = validationPattern
        self.inputColumnClass = inputColumnClass
        self.inputElementClass = inputElementClass
        self.hidden = hidden
        self.containerUnique = containerUnique
        self.persistentType = persistentType
        self.ormType = ormType
        self.interfaceType = interfaceType
        self.unique = unique
        self.persistence_Attribute11 = persistence_Attribute11
        self.persistence_Attribute = persistence_Attribute
        self.persistence_Attribute8 = persistence_Attribute8 if persistence_Attribute8 is not None else set()
        self.persistence_Attribute23 = persistence_Attribute23
        self.persistence_Attribute32 = persistence_Attribute32
        
    @property
    def containerUnique(self) -> bool:
        return self.__containerUnique

    @containerUnique.setter
    def containerUnique(self, containerUnique: bool):
        self.__containerUnique = containerUnique

    @property
    def inputElementClass(self) -> str:
        return self.__inputElementClass

    @inputElementClass.setter
    def inputElementClass(self, inputElementClass: str):
        self.__inputElementClass = inputElementClass

    @property
    def inputColumnClass(self) -> str:
        return self.__inputColumnClass

    @inputColumnClass.setter
    def inputColumnClass(self, inputColumnClass: str):
        self.__inputColumnClass = inputColumnClass

    @property
    def placeholder(self) -> str:
        return self.__placeholder

    @placeholder.setter
    def placeholder(self, placeholder: str):
        self.__placeholder = placeholder

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def interfaceType(self) -> str:
        return self.__interfaceType

    @interfaceType.setter
    def interfaceType(self, interfaceType: str):
        self.__interfaceType = interfaceType

    @property
    def hidden(self) -> bool:
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: bool):
        self.__hidden = hidden

    @property
    def persistentType(self) -> str:
        return self.__persistentType

    @persistentType.setter
    def persistentType(self, persistentType: str):
        self.__persistentType = persistentType

    @property
    def ormType(self) -> str:
        return self.__ormType

    @ormType.setter
    def ormType(self, ormType: str):
        self.__ormType = ormType

    @property
    def validationPattern(self) -> str:
        return self.__validationPattern

    @validationPattern.setter
    def validationPattern(self, validationPattern: str):
        self.__validationPattern = validationPattern

    @property
    def persistence_Attribute32(self):
        return self.__persistence_Attribute32

    @persistence_Attribute32.setter
    def persistence_Attribute32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Attribute__persistence_Attribute32", None)
        self.__persistence_Attribute32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Entity31"):
                opp_val = getattr(old_value, "persistence_Entity31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Entity31"):
                opp_val = getattr(value, "persistence_Entity31", None)
                if opp_val is None:
                    setattr(value, "persistence_Entity31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Attribute(self):
        return self.__persistence_Attribute

    @persistence_Attribute.setter
    def persistence_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Attribute__persistence_Attribute", None)
        self.__persistence_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Attribute8"):
                opp_val = getattr(old_value, "persistence_Attribute8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Attribute8"):
                opp_val = getattr(value, "persistence_Attribute8", None)
                if opp_val is None:
                    setattr(value, "persistence_Attribute8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Attribute8(self):
        return self.__persistence_Attribute8

    @persistence_Attribute8.setter
    def persistence_Attribute8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Attribute__persistence_Attribute8", None)
        self.__persistence_Attribute8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Attribute"):
                    opp_val = getattr(item, "persistence_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Attribute"):
                    opp_val = getattr(item, "persistence_Attribute", None)
                    
                    setattr(item, "persistence_Attribute", self)
                    

    @property
    def persistence_Attribute11(self):
        return self.__persistence_Attribute11

    @persistence_Attribute11.setter
    def persistence_Attribute11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Attribute__persistence_Attribute11", None)
        self.__persistence_Attribute11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Expression"):
                opp_val = getattr(old_value, "persistence_Expression", None)
                if opp_val == self:
                    setattr(old_value, "persistence_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Expression"):
                opp_val = getattr(value, "persistence_Expression", None)
                setattr(value, "persistence_Expression", self)

    @property
    def persistence_Attribute23(self):
        return self.__persistence_Attribute23

    @persistence_Attribute23.setter
    def persistence_Attribute23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Attribute__persistence_Attribute23", None)
        self.__persistence_Attribute23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_ModelLabelAttribute"):
                opp_val = getattr(old_value, "persistence_ModelLabelAttribute", None)
                if opp_val == self:
                    setattr(old_value, "persistence_ModelLabelAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_ModelLabelAttribute"):
                opp_val = getattr(value, "persistence_ModelLabelAttribute", None)
                setattr(value, "persistence_ModelLabelAttribute", self)

class persistence_Expression:

    pass
class NamedDisplayElement:

    pass
class persistence_Feature(NamedDisplayElement):

    def __init__(self, collectionOrmAllowRemove: bool, defaultDisplayValue: str, emptyDisplayValue: str, encodeUriKey: bool, singletonName: str, pluralisedName: str, columnName: str, cardinality: str, ordered: bool, primaryKey: bool, derived: bool, customiseSet: bool, booleanIsHasChoice: str, title: str, collectionOrmAllowAdd: bool, headerClass: str, displayClass: str, footerClass: str, features: "persistence_Entity" = None, persistence_Feature: set["persistence_SerializationGroup"] = None, persistence_Feature45: "persistence_Entity" = None, persistence_Feature50: "persistence_Entity" = None, persistence_Feature53: "persistence_Entity" = None, Feature: "persistence_Entity" = None, persistence_Feature39: "persistence_Entity" = None, persistence_Feature60: "persistence_AssociationKey" = None, persistence_Feature63: "persistence_AssociationKey" = None):
        self.collectionOrmAllowRemove = collectionOrmAllowRemove
        self.defaultDisplayValue = defaultDisplayValue
        self.emptyDisplayValue = emptyDisplayValue
        self.encodeUriKey = encodeUriKey
        self.singletonName = singletonName
        self.pluralisedName = pluralisedName
        self.columnName = columnName
        self.cardinality = cardinality
        self.ordered = ordered
        self.primaryKey = primaryKey
        self.derived = derived
        self.customiseSet = customiseSet
        self.booleanIsHasChoice = booleanIsHasChoice
        self.title = title
        self.collectionOrmAllowAdd = collectionOrmAllowAdd
        self.headerClass = headerClass
        self.displayClass = displayClass
        self.footerClass = footerClass
        self.features = features
        self.persistence_Feature = persistence_Feature if persistence_Feature is not None else set()
        self.persistence_Feature45 = persistence_Feature45
        self.persistence_Feature50 = persistence_Feature50
        self.persistence_Feature53 = persistence_Feature53
        self.Feature = Feature
        self.persistence_Feature39 = persistence_Feature39
        self.persistence_Feature60 = persistence_Feature60
        self.persistence_Feature63 = persistence_Feature63
        
    @property
    def emptyDisplayValue(self) -> str:
        return self.__emptyDisplayValue

    @emptyDisplayValue.setter
    def emptyDisplayValue(self, emptyDisplayValue: str):
        self.__emptyDisplayValue = emptyDisplayValue

    @property
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def primaryKey(self) -> bool:
        return self.__primaryKey

    @primaryKey.setter
    def primaryKey(self, primaryKey: bool):
        self.__primaryKey = primaryKey

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def encodeUriKey(self) -> bool:
        return self.__encodeUriKey

    @encodeUriKey.setter
    def encodeUriKey(self, encodeUriKey: bool):
        self.__encodeUriKey = encodeUriKey

    @property
    def customiseSet(self) -> bool:
        return self.__customiseSet

    @customiseSet.setter
    def customiseSet(self, customiseSet: bool):
        self.__customiseSet = customiseSet

    @property
    def collectionOrmAllowRemove(self) -> bool:
        return self.__collectionOrmAllowRemove

    @collectionOrmAllowRemove.setter
    def collectionOrmAllowRemove(self, collectionOrmAllowRemove: bool):
        self.__collectionOrmAllowRemove = collectionOrmAllowRemove

    @property
    def defaultDisplayValue(self) -> str:
        return self.__defaultDisplayValue

    @defaultDisplayValue.setter
    def defaultDisplayValue(self, defaultDisplayValue: str):
        self.__defaultDisplayValue = defaultDisplayValue

    @property
    def headerClass(self) -> str:
        return self.__headerClass

    @headerClass.setter
    def headerClass(self, headerClass: str):
        self.__headerClass = headerClass

    @property
    def footerClass(self) -> str:
        return self.__footerClass

    @footerClass.setter
    def footerClass(self, footerClass: str):
        self.__footerClass = footerClass

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def collectionOrmAllowAdd(self) -> bool:
        return self.__collectionOrmAllowAdd

    @collectionOrmAllowAdd.setter
    def collectionOrmAllowAdd(self, collectionOrmAllowAdd: bool):
        self.__collectionOrmAllowAdd = collectionOrmAllowAdd

    @property
    def singletonName(self) -> str:
        return self.__singletonName

    @singletonName.setter
    def singletonName(self, singletonName: str):
        self.__singletonName = singletonName

    @property
    def displayClass(self) -> str:
        return self.__displayClass

    @displayClass.setter
    def displayClass(self, displayClass: str):
        self.__displayClass = displayClass

    @property
    def booleanIsHasChoice(self) -> str:
        return self.__booleanIsHasChoice

    @booleanIsHasChoice.setter
    def booleanIsHasChoice(self, booleanIsHasChoice: str):
        self.__booleanIsHasChoice = booleanIsHasChoice

    @property
    def pluralisedName(self) -> str:
        return self.__pluralisedName

    @pluralisedName.setter
    def pluralisedName(self, pluralisedName: str):
        self.__pluralisedName = pluralisedName

    @property
    def Feature(self):
        return self.__Feature

    @Feature.setter
    def Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__Feature", None)
        self.__Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partOf29"):
                opp_val = getattr(old_value, "partOf29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partOf29"):
                opp_val = getattr(value, "partOf29", None)
                if opp_val is None:
                    setattr(value, "partOf29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Feature39(self):
        return self.__persistence_Feature39

    @persistence_Feature39.setter
    def persistence_Feature39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature39", None)
        self.__persistence_Feature39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Entity38"):
                opp_val = getattr(old_value, "persistence_Entity38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Entity38"):
                opp_val = getattr(value, "persistence_Entity38", None)
                if opp_val is None:
                    setattr(value, "persistence_Entity38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Feature(self):
        return self.__persistence_Feature

    @persistence_Feature.setter
    def persistence_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature", None)
        self.__persistence_Feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_SerializationGroup7"):
                    opp_val = getattr(item, "persistence_SerializationGroup7", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_SerializationGroup7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_SerializationGroup7"):
                    opp_val = getattr(item, "persistence_SerializationGroup7", None)
                    
                    setattr(item, "persistence_SerializationGroup7", self)
                    

    @property
    def persistence_Feature53(self):
        return self.__persistence_Feature53

    @persistence_Feature53.setter
    def persistence_Feature53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature53", None)
        self.__persistence_Feature53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Entity52"):
                opp_val = getattr(old_value, "persistence_Entity52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Entity52"):
                opp_val = getattr(value, "persistence_Entity52", None)
                if opp_val is None:
                    setattr(value, "persistence_Entity52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Feature45(self):
        return self.__persistence_Feature45

    @persistence_Feature45.setter
    def persistence_Feature45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature45", None)
        self.__persistence_Feature45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Entity44"):
                opp_val = getattr(old_value, "persistence_Entity44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Entity44"):
                opp_val = getattr(value, "persistence_Entity44", None)
                if opp_val is None:
                    setattr(value, "persistence_Entity44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def features(self):
        return self.__features

    @features.setter
    def features(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__features", None)
        self.__features = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity"):
                opp_val = getattr(old_value, "Entity", None)
                if opp_val == self:
                    setattr(old_value, "Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity"):
                opp_val = getattr(value, "Entity", None)
                setattr(value, "Entity", self)

    @property
    def persistence_Feature63(self):
        return self.__persistence_Feature63

    @persistence_Feature63.setter
    def persistence_Feature63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature63", None)
        self.__persistence_Feature63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_AssociationKey62"):
                opp_val = getattr(old_value, "persistence_AssociationKey62", None)
                if opp_val == self:
                    setattr(old_value, "persistence_AssociationKey62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_AssociationKey62"):
                opp_val = getattr(value, "persistence_AssociationKey62", None)
                setattr(value, "persistence_AssociationKey62", self)

    @property
    def persistence_Feature50(self):
        return self.__persistence_Feature50

    @persistence_Feature50.setter
    def persistence_Feature50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature50", None)
        self.__persistence_Feature50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Entity49"):
                opp_val = getattr(old_value, "persistence_Entity49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Entity49"):
                opp_val = getattr(value, "persistence_Entity49", None)
                if opp_val is None:
                    setattr(value, "persistence_Entity49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Feature60(self):
        return self.__persistence_Feature60

    @persistence_Feature60.setter
    def persistence_Feature60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature60", None)
        self.__persistence_Feature60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_AssociationKey"):
                opp_val = getattr(old_value, "persistence_AssociationKey", None)
                if opp_val == self:
                    setattr(old_value, "persistence_AssociationKey", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_AssociationKey"):
                opp_val = getattr(value, "persistence_AssociationKey", None)
                setattr(value, "persistence_AssociationKey", self)

class persistence_Entity(Classifier):

    def __init__(self, tableName: str, autoKeyName: str, singletonName: str, pluralisedName: str, autoKeyPersistentType: str, autoKeyGenerationStrategy: str, implementsUserInterface: bool, allowFormTypeCustomisation: bool, persistence_Entity: "persistence_Persistence" = None, Entity: "persistence_Feature" = None, Entity14: "persistence_Association" = None, Entity16: "persistence_ModelLabel" = None, persistence_Entity44: set["persistence_Feature"] = None, labelFor: set["persistence_ModelLabel"] = None, persistence_Entity49: set["persistence_Feature"] = None, persistence_Entity52: set["persistence_Feature"] = None, partOf29: set["persistence_Feature"] = None, persistence_Entity31: set["persistence_Attribute"] = None, persistence_Entity34: set["persistence_Association"] = None, targetEntity: set["persistence_Association"] = None, persistence_Entity38: set["persistence_Feature"] = None, persistence_Entity41: set["persistence_Association"] = None):
        self.tableName = tableName
        self.autoKeyName = autoKeyName
        self.singletonName = singletonName
        self.pluralisedName = pluralisedName
        self.autoKeyPersistentType = autoKeyPersistentType
        self.autoKeyGenerationStrategy = autoKeyGenerationStrategy
        self.implementsUserInterface = implementsUserInterface
        self.allowFormTypeCustomisation = allowFormTypeCustomisation
        self.persistence_Entity = persistence_Entity
        self.Entity = Entity
        self.Entity14 = Entity14
        self.Entity16 = Entity16
        self.persistence_Entity44 = persistence_Entity44 if persistence_Entity44 is not None else set()
        self.labelFor = labelFor if labelFor is not None else set()
        self.persistence_Entity49 = persistence_Entity49 if persistence_Entity49 is not None else set()
        self.persistence_Entity52 = persistence_Entity52 if persistence_Entity52 is not None else set()
        self.partOf29 = partOf29 if partOf29 is not None else set()
        self.persistence_Entity31 = persistence_Entity31 if persistence_Entity31 is not None else set()
        self.persistence_Entity34 = persistence_Entity34 if persistence_Entity34 is not None else set()
        self.targetEntity = targetEntity if targetEntity is not None else set()
        self.persistence_Entity38 = persistence_Entity38 if persistence_Entity38 is not None else set()
        self.persistence_Entity41 = persistence_Entity41 if persistence_Entity41 is not None else set()
        
    @property
    def implementsUserInterface(self) -> bool:
        return self.__implementsUserInterface

    @implementsUserInterface.setter
    def implementsUserInterface(self, implementsUserInterface: bool):
        self.__implementsUserInterface = implementsUserInterface

    @property
    def autoKeyPersistentType(self) -> str:
        return self.__autoKeyPersistentType

    @autoKeyPersistentType.setter
    def autoKeyPersistentType(self, autoKeyPersistentType: str):
        self.__autoKeyPersistentType = autoKeyPersistentType

    @property
    def autoKeyName(self) -> str:
        return self.__autoKeyName

    @autoKeyName.setter
    def autoKeyName(self, autoKeyName: str):
        self.__autoKeyName = autoKeyName

    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def autoKeyGenerationStrategy(self) -> str:
        return self.__autoKeyGenerationStrategy

    @autoKeyGenerationStrategy.setter
    def autoKeyGenerationStrategy(self, autoKeyGenerationStrategy: str):
        self.__autoKeyGenerationStrategy = autoKeyGenerationStrategy

    @property
    def allowFormTypeCustomisation(self) -> bool:
        return self.__allowFormTypeCustomisation

    @allowFormTypeCustomisation.setter
    def allowFormTypeCustomisation(self, allowFormTypeCustomisation: bool):
        self.__allowFormTypeCustomisation = allowFormTypeCustomisation

    @property
    def singletonName(self) -> str:
        return self.__singletonName

    @singletonName.setter
    def singletonName(self, singletonName: str):
        self.__singletonName = singletonName

    @property
    def pluralisedName(self) -> str:
        return self.__pluralisedName

    @pluralisedName.setter
    def pluralisedName(self, pluralisedName: str):
        self.__pluralisedName = pluralisedName

    @property
    def targetEntity(self):
        return self.__targetEntity

    @targetEntity.setter
    def targetEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__targetEntity", None)
        self.__targetEntity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Association"):
                    opp_val = getattr(item, "Association", None)
                    
                    if opp_val == self:
                        setattr(item, "Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Association"):
                    opp_val = getattr(item, "Association", None)
                    
                    setattr(item, "Association", self)
                    

    @property
    def Entity(self):
        return self.__Entity

    @Entity.setter
    def Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__Entity", None)
        self.__Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features"):
                opp_val = getattr(old_value, "features", None)
                if opp_val == self:
                    setattr(old_value, "features", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features"):
                opp_val = getattr(value, "features", None)
                setattr(value, "features", self)

    @property
    def persistence_Entity44(self):
        return self.__persistence_Entity44

    @persistence_Entity44.setter
    def persistence_Entity44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__persistence_Entity44", None)
        self.__persistence_Entity44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Feature45"):
                    opp_val = getattr(item, "persistence_Feature45", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Feature45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Feature45"):
                    opp_val = getattr(item, "persistence_Feature45", None)
                    
                    setattr(item, "persistence_Feature45", self)
                    

    @property
    def persistence_Entity31(self):
        return self.__persistence_Entity31

    @persistence_Entity31.setter
    def persistence_Entity31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__persistence_Entity31", None)
        self.__persistence_Entity31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Attribute32"):
                    opp_val = getattr(item, "persistence_Attribute32", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Attribute32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Attribute32"):
                    opp_val = getattr(item, "persistence_Attribute32", None)
                    
                    setattr(item, "persistence_Attribute32", self)
                    

    @property
    def Entity16(self):
        return self.__Entity16

    @Entity16.setter
    def Entity16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__Entity16", None)
        self.__Entity16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "labels"):
                opp_val = getattr(old_value, "labels", None)
                if opp_val == self:
                    setattr(old_value, "labels", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "labels"):
                opp_val = getattr(value, "labels", None)
                setattr(value, "labels", self)

    @property
    def persistence_Entity34(self):
        return self.__persistence_Entity34

    @persistence_Entity34.setter
    def persistence_Entity34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__persistence_Entity34", None)
        self.__persistence_Entity34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Association35"):
                    opp_val = getattr(item, "persistence_Association35", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Association35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Association35"):
                    opp_val = getattr(item, "persistence_Association35", None)
                    
                    setattr(item, "persistence_Association35", self)
                    

    @property
    def persistence_Entity52(self):
        return self.__persistence_Entity52

    @persistence_Entity52.setter
    def persistence_Entity52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__persistence_Entity52", None)
        self.__persistence_Entity52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Feature53"):
                    opp_val = getattr(item, "persistence_Feature53", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Feature53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Feature53"):
                    opp_val = getattr(item, "persistence_Feature53", None)
                    
                    setattr(item, "persistence_Feature53", self)
                    

    @property
    def Entity14(self):
        return self.__Entity14

    @Entity14.setter
    def Entity14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__Entity14", None)
        self.__Entity14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associationEnds"):
                opp_val = getattr(old_value, "associationEnds", None)
                if opp_val == self:
                    setattr(old_value, "associationEnds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associationEnds"):
                opp_val = getattr(value, "associationEnds", None)
                setattr(value, "associationEnds", self)

    @property
    def persistence_Entity41(self):
        return self.__persistence_Entity41

    @persistence_Entity41.setter
    def persistence_Entity41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__persistence_Entity41", None)
        self.__persistence_Entity41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Association42"):
                    opp_val = getattr(item, "persistence_Association42", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Association42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Association42"):
                    opp_val = getattr(item, "persistence_Association42", None)
                    
                    setattr(item, "persistence_Association42", self)
                    

    @property
    def persistence_Entity49(self):
        return self.__persistence_Entity49

    @persistence_Entity49.setter
    def persistence_Entity49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__persistence_Entity49", None)
        self.__persistence_Entity49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Feature50"):
                    opp_val = getattr(item, "persistence_Feature50", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Feature50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Feature50"):
                    opp_val = getattr(item, "persistence_Feature50", None)
                    
                    setattr(item, "persistence_Feature50", self)
                    

    @property
    def partOf29(self):
        return self.__partOf29

    @partOf29.setter
    def partOf29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__partOf29", None)
        self.__partOf29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Feature"):
                    opp_val = getattr(item, "Feature", None)
                    
                    setattr(item, "Feature", self)
                    

    @property
    def persistence_Entity38(self):
        return self.__persistence_Entity38

    @persistence_Entity38.setter
    def persistence_Entity38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__persistence_Entity38", None)
        self.__persistence_Entity38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Feature39"):
                    opp_val = getattr(item, "persistence_Feature39", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Feature39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Feature39"):
                    opp_val = getattr(item, "persistence_Feature39", None)
                    
                    setattr(item, "persistence_Feature39", self)
                    

    @property
    def persistence_Entity(self):
        return self.__persistence_Entity

    @persistence_Entity.setter
    def persistence_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__persistence_Entity", None)
        self.__persistence_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Persistence4"):
                opp_val = getattr(old_value, "persistence_Persistence4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Persistence4"):
                opp_val = getattr(value, "persistence_Persistence4", None)
                if opp_val is None:
                    setattr(value, "persistence_Persistence4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def labelFor(self):
        return self.__labelFor

    @labelFor.setter
    def labelFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Entity__labelFor", None)
        self.__labelFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelLabel47"):
                    opp_val = getattr(item, "ModelLabel47", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelLabel47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelLabel47"):
                    opp_val = getattr(item, "ModelLabel47", None)
                    
                    setattr(item, "ModelLabel47", self)
                    

class persistence_DataType:

    pass
class NamedElement:

    pass
class persistence_ModelLabel(NamedElement, Label):

    def __init__(self, format: str, customise: bool, persistence_ModelLabel27: "persistence_ModelLabelAssociation" = None, labels: "persistence_Entity" = None, partOf: set["persistence_ModelLabelFeature"] = None, persistence_ModelLabel: set["persistence_SerializationGroup"] = None, ModelLabel: "persistence_ModelLabelFeature" = None, ModelLabel47: "persistence_Entity" = None):
        self.format = format
        self.customise = customise
        self.persistence_ModelLabel27 = persistence_ModelLabel27
        self.labels = labels
        self.partOf = partOf if partOf is not None else set()
        self.persistence_ModelLabel = persistence_ModelLabel if persistence_ModelLabel is not None else set()
        self.ModelLabel = ModelLabel
        self.ModelLabel47 = ModelLabel47
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def customise(self) -> bool:
        return self.__customise

    @customise.setter
    def customise(self, customise: bool):
        self.__customise = customise

    @property
    def labels(self):
        return self.__labels

    @labels.setter
    def labels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabel__labels", None)
        self.__labels = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity16"):
                opp_val = getattr(old_value, "Entity16", None)
                if opp_val == self:
                    setattr(old_value, "Entity16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity16"):
                opp_val = getattr(value, "Entity16", None)
                setattr(value, "Entity16", self)

    @property
    def partOf(self):
        return self.__partOf

    @partOf.setter
    def partOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabel__partOf", None)
        self.__partOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelLabelFeature"):
                    opp_val = getattr(item, "ModelLabelFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelLabelFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelLabelFeature"):
                    opp_val = getattr(item, "ModelLabelFeature", None)
                    
                    setattr(item, "ModelLabelFeature", self)
                    

    @property
    def ModelLabel47(self):
        return self.__ModelLabel47

    @ModelLabel47.setter
    def ModelLabel47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabel__ModelLabel47", None)
        self.__ModelLabel47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "labelFor"):
                opp_val = getattr(old_value, "labelFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "labelFor"):
                opp_val = getattr(value, "labelFor", None)
                if opp_val is None:
                    setattr(value, "labelFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_ModelLabel(self):
        return self.__persistence_ModelLabel

    @persistence_ModelLabel.setter
    def persistence_ModelLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabel__persistence_ModelLabel", None)
        self.__persistence_ModelLabel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_SerializationGroup19"):
                    opp_val = getattr(item, "persistence_SerializationGroup19", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_SerializationGroup19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_SerializationGroup19"):
                    opp_val = getattr(item, "persistence_SerializationGroup19", None)
                    
                    setattr(item, "persistence_SerializationGroup19", self)
                    

    @property
    def ModelLabel(self):
        return self.__ModelLabel

    @ModelLabel.setter
    def ModelLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabel__ModelLabel", None)
        self.__ModelLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "features21"):
                opp_val = getattr(old_value, "features21", None)
                if opp_val == self:
                    setattr(old_value, "features21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "features21"):
                opp_val = getattr(value, "features21", None)
                setattr(value, "features21", self)

    @property
    def persistence_ModelLabel27(self):
        return self.__persistence_ModelLabel27

    @persistence_ModelLabel27.setter
    def persistence_ModelLabel27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabel__persistence_ModelLabel27", None)
        self.__persistence_ModelLabel27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_ModelLabelAssociation26"):
                opp_val = getattr(old_value, "persistence_ModelLabelAssociation26", None)
                if opp_val == self:
                    setattr(old_value, "persistence_ModelLabelAssociation26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_ModelLabelAssociation26"):
                opp_val = getattr(value, "persistence_ModelLabelAssociation26", None)
                setattr(value, "persistence_ModelLabelAssociation26", self)

class persistence_SerializationGroup(NamedElement):

    pass
class persistence_Persistence:

    def __init__(self, ormTechnology: str, databaseTechnology: str, timestampCreation: bool, timestampUpdates: bool, persistence_Persistence: set["persistence_SerializationGroup"] = None, persistence_Persistence2: set["persistence_DataType"] = None, persistence_Persistence4: set["persistence_Entity"] = None):
        self.ormTechnology = ormTechnology
        self.databaseTechnology = databaseTechnology
        self.timestampCreation = timestampCreation
        self.timestampUpdates = timestampUpdates
        self.persistence_Persistence = persistence_Persistence if persistence_Persistence is not None else set()
        self.persistence_Persistence2 = persistence_Persistence2 if persistence_Persistence2 is not None else set()
        self.persistence_Persistence4 = persistence_Persistence4 if persistence_Persistence4 is not None else set()
        
    @property
    def ormTechnology(self) -> str:
        return self.__ormTechnology

    @ormTechnology.setter
    def ormTechnology(self, ormTechnology: str):
        self.__ormTechnology = ormTechnology

    @property
    def timestampCreation(self) -> bool:
        return self.__timestampCreation

    @timestampCreation.setter
    def timestampCreation(self, timestampCreation: bool):
        self.__timestampCreation = timestampCreation

    @property
    def timestampUpdates(self) -> bool:
        return self.__timestampUpdates

    @timestampUpdates.setter
    def timestampUpdates(self, timestampUpdates: bool):
        self.__timestampUpdates = timestampUpdates

    @property
    def databaseTechnology(self) -> str:
        return self.__databaseTechnology

    @databaseTechnology.setter
    def databaseTechnology(self, databaseTechnology: str):
        self.__databaseTechnology = databaseTechnology

    @property
    def persistence_Persistence4(self):
        return self.__persistence_Persistence4

    @persistence_Persistence4.setter
    def persistence_Persistence4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Persistence__persistence_Persistence4", None)
        self.__persistence_Persistence4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Entity"):
                    opp_val = getattr(item, "persistence_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Entity"):
                    opp_val = getattr(item, "persistence_Entity", None)
                    
                    setattr(item, "persistence_Entity", self)
                    

    @property
    def persistence_Persistence(self):
        return self.__persistence_Persistence

    @persistence_Persistence.setter
    def persistence_Persistence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Persistence__persistence_Persistence", None)
        self.__persistence_Persistence = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_SerializationGroup"):
                    opp_val = getattr(item, "persistence_SerializationGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_SerializationGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_SerializationGroup"):
                    opp_val = getattr(item, "persistence_SerializationGroup", None)
                    
                    setattr(item, "persistence_SerializationGroup", self)
                    

    @property
    def persistence_Persistence2(self):
        return self.__persistence_Persistence2

    @persistence_Persistence2.setter
    def persistence_Persistence2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Persistence__persistence_Persistence2", None)
        self.__persistence_Persistence2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_DataType"):
                    opp_val = getattr(item, "persistence_DataType", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_DataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_DataType"):
                    opp_val = getattr(item, "persistence_DataType", None)
                    
                    setattr(item, "persistence_DataType", self)
                    
