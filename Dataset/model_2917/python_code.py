from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class isHasChoices(Enum):
    isA = "isA"
    hasA = "hasA"
class Cardinality(Enum):
    Optional = "Optional"
    Required = "Required"
    Many = "Many"
class DateDetails(Enum):
    DateOnly = "DateOnly"
    TimeOnly = "TimeOnly"
    DateAndTime = "DateAndTime"
class DatabaseTechnologies(Enum):
    MySql = "MySql"
    Oracle = "Oracle"
class OrmTechnologies(Enum):
    JPA = "JPA"
    DataMapper = "DataMapper"
    Idiorm = "Idiorm"
    Kohana = "Kohana"
    DoctrineORM = "DoctrineORM"
    DoctrineODM = "DoctrineODM"


############################################
# Definition of Classes
############################################

class EncapsulatedFeature:

    pass
class ViewFeature:

    pass
class persistence_EncapsulatedFeature(ViewFeature):

    def __init__(self, displayLabel: str, alias: str, columnName: str):
        self.displayLabel = displayLabel
        self.alias = alias
        self.columnName = columnName
        
    @property
    def displayLabel(self) -> str:
        return self.__displayLabel

    @displayLabel.setter
    def displayLabel(self, displayLabel: str):
        self.__displayLabel = displayLabel

    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def alias(self) -> str:
        return self.__alias

    @alias.setter
    def alias(self, alias: str):
        self.__alias = alias

class EntityAssociation:

    pass
class persistence_AssociationWithContainment(EntityAssociation):

    def __init__(self, sourceVisible: bool):
        self.sourceVisible = sourceVisible
        
    @property
    def sourceVisible(self) -> bool:
        return self.__sourceVisible

    @sourceVisible.setter
    def sourceVisible(self, sourceVisible: bool):
        self.__sourceVisible = sourceVisible

class persistence_AssociationWithoutContainment(EntityAssociation):

    def __init__(self, targetCardinality: str, targetUnique: bool):
        self.targetCardinality = targetCardinality
        self.targetUnique = targetUnique
        
    @property
    def targetCardinality(self) -> str:
        return self.__targetCardinality

    @targetCardinality.setter
    def targetCardinality(self, targetCardinality: str):
        self.__targetCardinality = targetCardinality

    @property
    def targetUnique(self) -> bool:
        return self.__targetUnique

    @targetUnique.setter
    def targetUnique(self, targetUnique: bool):
        self.__targetUnique = targetUnique

class persistence_AssociationKey:

    pass
class Association:

    pass
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
class EntityAttribute:

    pass
class persistence_LocationAttribute(EntityAttribute):

    pass
class persistence_DateAttribute(EntityAttribute):

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

class persistence_ResourceAttribute(EntityAttribute):

    def __init__(self, maximumUploadSize: int, validUploadMimeTypes: str, validUploadExtensions: str, uploadsWithinWebsite: bool, persistence_ResourceAttribute: set["persistence_PathElement"] = None):
        self.maximumUploadSize = maximumUploadSize
        self.validUploadMimeTypes = validUploadMimeTypes
        self.validUploadExtensions = validUploadExtensions
        self.uploadsWithinWebsite = uploadsWithinWebsite
        self.persistence_ResourceAttribute = persistence_ResourceAttribute if persistence_ResourceAttribute is not None else set()
        
    @property
    def uploadsWithinWebsite(self) -> bool:
        return self.__uploadsWithinWebsite

    @uploadsWithinWebsite.setter
    def uploadsWithinWebsite(self, uploadsWithinWebsite: bool):
        self.__uploadsWithinWebsite = uploadsWithinWebsite

    @property
    def validUploadMimeTypes(self) -> str:
        return self.__validUploadMimeTypes

    @validUploadMimeTypes.setter
    def validUploadMimeTypes(self, validUploadMimeTypes: str):
        self.__validUploadMimeTypes = validUploadMimeTypes

    @property
    def maximumUploadSize(self) -> int:
        return self.__maximumUploadSize

    @maximumUploadSize.setter
    def maximumUploadSize(self, maximumUploadSize: int):
        self.__maximumUploadSize = maximumUploadSize

    @property
    def validUploadExtensions(self) -> str:
        return self.__validUploadExtensions

    @validUploadExtensions.setter
    def validUploadExtensions(self, validUploadExtensions: str):
        self.__validUploadExtensions = validUploadExtensions

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
                    

class persistence_UrlAttribute(EntityAttribute):

    def __init__(self, displayValue: str):
        self.displayValue = displayValue
        
    @property
    def displayValue(self) -> str:
        return self.__displayValue

    @displayValue.setter
    def displayValue(self, displayValue: str):
        self.__displayValue = displayValue

class persistence_DataTypeAttribute(EntityAttribute):

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
            if hasattr(old_value, "persistence_DataType58"):
                opp_val = getattr(old_value, "persistence_DataType58", None)
                if opp_val == self:
                    setattr(old_value, "persistence_DataType58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_DataType58"):
                opp_val = getattr(value, "persistence_DataType58", None)
                setattr(value, "persistence_DataType58", self)

class Attribute:

    pass
class persistence_EncapsulatedAttribute(EncapsulatedFeature, Attribute):

    def __init__(self, name: str, cardinality: str, persistence_EncapsulatedAttribute: "persistence_Attribute" = None):
        self.name = name
        self.cardinality = cardinality
        self.persistence_EncapsulatedAttribute = persistence_EncapsulatedAttribute
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def persistence_EncapsulatedAttribute(self):
        return self.__persistence_EncapsulatedAttribute

    @persistence_EncapsulatedAttribute.setter
    def persistence_EncapsulatedAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EncapsulatedAttribute__persistence_EncapsulatedAttribute", None)
        self.__persistence_EncapsulatedAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Attribute75"):
                opp_val = getattr(old_value, "persistence_Attribute75", None)
                if opp_val == self:
                    setattr(old_value, "persistence_Attribute75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Attribute75"):
                opp_val = getattr(value, "persistence_Attribute75", None)
                setattr(value, "persistence_Attribute75", self)

class EntityFeature:

    pass
class persistence_EntityAttribute(EntityFeature, Attribute):

    def __init__(self, hidden: bool, containerUnique: bool, persistentType: str, ormType: str, interfaceType: str, unique: bool, persistence_EntityAttribute: set["persistence_Attribute"] = None):
        self.hidden = hidden
        self.containerUnique = containerUnique
        self.persistentType = persistentType
        self.ormType = ormType
        self.interfaceType = interfaceType
        self.unique = unique
        self.persistence_EntityAttribute = persistence_EntityAttribute if persistence_EntityAttribute is not None else set()
        
    @property
    def persistentType(self) -> str:
        return self.__persistentType

    @persistentType.setter
    def persistentType(self, persistentType: str):
        self.__persistentType = persistentType

    @property
    def containerUnique(self) -> bool:
        return self.__containerUnique

    @containerUnique.setter
    def containerUnique(self, containerUnique: bool):
        self.__containerUnique = containerUnique

    @property
    def hidden(self) -> bool:
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: bool):
        self.__hidden = hidden

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def ormType(self) -> str:
        return self.__ormType

    @ormType.setter
    def ormType(self, ormType: str):
        self.__ormType = ormType

    @property
    def interfaceType(self) -> str:
        return self.__interfaceType

    @interfaceType.setter
    def interfaceType(self, interfaceType: str):
        self.__interfaceType = interfaceType

    @property
    def persistence_EntityAttribute(self):
        return self.__persistence_EntityAttribute

    @persistence_EntityAttribute.setter
    def persistence_EntityAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityAttribute__persistence_EntityAttribute", None)
        self.__persistence_EntityAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Attribute56"):
                    opp_val = getattr(item, "persistence_Attribute56", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Attribute56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Attribute56"):
                    opp_val = getattr(item, "persistence_Attribute56", None)
                    
                    setattr(item, "persistence_Attribute56", self)
                    

class NamedDisplayElement:

    pass
class persistence_ViewAssociation(ViewFeature, Association, NamedDisplayElement):

    def __init__(self, cardinality: str, persistence_ViewAssociation: "persistence_EncapsulatedAssociation" = None):
        self.cardinality = cardinality
        self.persistence_ViewAssociation = persistence_ViewAssociation
        
    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def persistence_ViewAssociation(self):
        return self.__persistence_ViewAssociation

    @persistence_ViewAssociation.setter
    def persistence_ViewAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ViewAssociation__persistence_ViewAssociation", None)
        self.__persistence_ViewAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EncapsulatedAssociation85"):
                opp_val = getattr(old_value, "persistence_EncapsulatedAssociation85", None)
                if opp_val == self:
                    setattr(old_value, "persistence_EncapsulatedAssociation85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EncapsulatedAssociation85"):
                opp_val = getattr(value, "persistence_EncapsulatedAssociation85", None)
                setattr(value, "persistence_EncapsulatedAssociation85", self)

class EntityOrView:

    pass
class persistence_View(EntityOrView):

    pass
class persistence_Entity(EntityOrView):

    pass
class persistence_EntityAssociation(EntityFeature, Association):

    def __init__(self, bidirectional: bool, unique: bool, pivotTableName: str, targetFeatureName: str, targetPrimaryKey: bool, targetColumnName: str, targetDisplayLabel: str, targetHeaderClass: str, targetInputClass: str, targetDisplayClass: str, targetFooterClass: str, persistence_EntityAssociation: "persistence_ModelLabelAssociation" = None, EntityAssociation: "persistence_Entity" = None, keyFor: set["persistence_AssociationKey"] = None, associationEnds: "persistence_Entity" = None, EntityAssociation64: "persistence_AssociationKey" = None):
        self.bidirectional = bidirectional
        self.unique = unique
        self.pivotTableName = pivotTableName
        self.targetFeatureName = targetFeatureName
        self.targetPrimaryKey = targetPrimaryKey
        self.targetColumnName = targetColumnName
        self.targetDisplayLabel = targetDisplayLabel
        self.targetHeaderClass = targetHeaderClass
        self.targetInputClass = targetInputClass
        self.targetDisplayClass = targetDisplayClass
        self.targetFooterClass = targetFooterClass
        self.persistence_EntityAssociation = persistence_EntityAssociation
        self.EntityAssociation = EntityAssociation
        self.keyFor = keyFor if keyFor is not None else set()
        self.associationEnds = associationEnds
        self.EntityAssociation64 = EntityAssociation64
        
    @property
    def targetInputClass(self) -> str:
        return self.__targetInputClass

    @targetInputClass.setter
    def targetInputClass(self, targetInputClass: str):
        self.__targetInputClass = targetInputClass

    @property
    def targetHeaderClass(self) -> str:
        return self.__targetHeaderClass

    @targetHeaderClass.setter
    def targetHeaderClass(self, targetHeaderClass: str):
        self.__targetHeaderClass = targetHeaderClass

    @property
    def targetDisplayClass(self) -> str:
        return self.__targetDisplayClass

    @targetDisplayClass.setter
    def targetDisplayClass(self, targetDisplayClass: str):
        self.__targetDisplayClass = targetDisplayClass

    @property
    def unique(self) -> bool:
        return self.__unique

    @unique.setter
    def unique(self, unique: bool):
        self.__unique = unique

    @property
    def targetFooterClass(self) -> str:
        return self.__targetFooterClass

    @targetFooterClass.setter
    def targetFooterClass(self, targetFooterClass: str):
        self.__targetFooterClass = targetFooterClass

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
    def targetFeatureName(self) -> str:
        return self.__targetFeatureName

    @targetFeatureName.setter
    def targetFeatureName(self, targetFeatureName: str):
        self.__targetFeatureName = targetFeatureName

    @property
    def pivotTableName(self) -> str:
        return self.__pivotTableName

    @pivotTableName.setter
    def pivotTableName(self, pivotTableName: str):
        self.__pivotTableName = pivotTableName

    @property
    def associationEnds(self):
        return self.__associationEnds

    @associationEnds.setter
    def associationEnds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityAssociation__associationEnds", None)
        self.__associationEnds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity62"):
                opp_val = getattr(old_value, "Entity62", None)
                if opp_val == self:
                    setattr(old_value, "Entity62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity62"):
                opp_val = getattr(value, "Entity62", None)
                setattr(value, "Entity62", self)

    @property
    def EntityAssociation(self):
        return self.__EntityAssociation

    @EntityAssociation.setter
    def EntityAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityAssociation__EntityAssociation", None)
        self.__EntityAssociation = value
        
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
    def keyFor(self):
        return self.__keyFor

    @keyFor.setter
    def keyFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityAssociation__keyFor", None)
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
    def persistence_EntityAssociation(self):
        return self.__persistence_EntityAssociation

    @persistence_EntityAssociation.setter
    def persistence_EntityAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityAssociation__persistence_EntityAssociation", None)
        self.__persistence_EntityAssociation = value
        
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
    def EntityAssociation64(self):
        return self.__EntityAssociation64

    @EntityAssociation64.setter
    def EntityAssociation64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityAssociation__EntityAssociation64", None)
        self.__EntityAssociation64 = value
        
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

class ModelLabelFeature:

    pass
class persistence_ModelLabelAssociation(ModelLabelFeature):

    def __init__(self, isSourceAssociation: bool, persistence_ModelLabelAssociation: "persistence_EntityAssociation" = None, persistence_ModelLabelAssociation49: "persistence_ModelLabel" = None):
        self.isSourceAssociation = isSourceAssociation
        self.persistence_ModelLabelAssociation = persistence_ModelLabelAssociation
        self.persistence_ModelLabelAssociation49 = persistence_ModelLabelAssociation49
        
    @property
    def isSourceAssociation(self) -> bool:
        return self.__isSourceAssociation

    @isSourceAssociation.setter
    def isSourceAssociation(self, isSourceAssociation: bool):
        self.__isSourceAssociation = isSourceAssociation

    @property
    def persistence_ModelLabelAssociation49(self):
        return self.__persistence_ModelLabelAssociation49

    @persistence_ModelLabelAssociation49.setter
    def persistence_ModelLabelAssociation49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabelAssociation__persistence_ModelLabelAssociation49", None)
        self.__persistence_ModelLabelAssociation49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_ModelLabel50"):
                opp_val = getattr(old_value, "persistence_ModelLabel50", None)
                if opp_val == self:
                    setattr(old_value, "persistence_ModelLabel50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_ModelLabel50"):
                opp_val = getattr(value, "persistence_ModelLabel50", None)
                setattr(value, "persistence_ModelLabel50", self)

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
            if hasattr(old_value, "persistence_EntityAssociation"):
                opp_val = getattr(old_value, "persistence_EntityAssociation", None)
                if opp_val == self:
                    setattr(old_value, "persistence_EntityAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityAssociation"):
                opp_val = getattr(value, "persistence_EntityAssociation", None)
                setattr(value, "persistence_EntityAssociation", self)

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
            if hasattr(old_value, "persistence_Attribute46"):
                opp_val = getattr(old_value, "persistence_Attribute46", None)
                if opp_val == self:
                    setattr(old_value, "persistence_Attribute46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Attribute46"):
                opp_val = getattr(value, "persistence_Attribute46", None)
                setattr(value, "persistence_Attribute46", self)

class persistence_ModelLabelFeature(ABC):

    pass
class persistence_Label(ABC):

    pass
class persistence_EncapsulatedAssociation(EncapsulatedFeature, Association):

    def __init__(self, name: str, isSourceAssociation: bool, cardinality: str, EncapsulatedAssociation: "persistence_Association" = None, encapsulatedBy: "persistence_Association" = None, persistence_EncapsulatedAssociation: "persistence_EncapsulatedAssociation" = None, persistence_EncapsulatedAssociation77: "persistence_EncapsulatedAssociation" = None, persistence_EncapsulatedAssociation80: "persistence_Entity" = None, persistence_EncapsulatedAssociation82: "persistence_Entity" = None, persistence_EncapsulatedAssociation85: "persistence_ViewAssociation" = None):
        self.name = name
        self.isSourceAssociation = isSourceAssociation
        self.cardinality = cardinality
        self.EncapsulatedAssociation = EncapsulatedAssociation
        self.encapsulatedBy = encapsulatedBy
        self.persistence_EncapsulatedAssociation = persistence_EncapsulatedAssociation
        self.persistence_EncapsulatedAssociation77 = persistence_EncapsulatedAssociation77
        self.persistence_EncapsulatedAssociation80 = persistence_EncapsulatedAssociation80
        self.persistence_EncapsulatedAssociation82 = persistence_EncapsulatedAssociation82
        self.persistence_EncapsulatedAssociation85 = persistence_EncapsulatedAssociation85
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def isSourceAssociation(self) -> bool:
        return self.__isSourceAssociation

    @isSourceAssociation.setter
    def isSourceAssociation(self, isSourceAssociation: bool):
        self.__isSourceAssociation = isSourceAssociation

    @property
    def persistence_EncapsulatedAssociation80(self):
        return self.__persistence_EncapsulatedAssociation80

    @persistence_EncapsulatedAssociation80.setter
    def persistence_EncapsulatedAssociation80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EncapsulatedAssociation__persistence_EncapsulatedAssociation80", None)
        self.__persistence_EncapsulatedAssociation80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Entity"):
                opp_val = getattr(old_value, "persistence_Entity", None)
                if opp_val == self:
                    setattr(old_value, "persistence_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Entity"):
                opp_val = getattr(value, "persistence_Entity", None)
                setattr(value, "persistence_Entity", self)

    @property
    def persistence_EncapsulatedAssociation82(self):
        return self.__persistence_EncapsulatedAssociation82

    @persistence_EncapsulatedAssociation82.setter
    def persistence_EncapsulatedAssociation82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EncapsulatedAssociation__persistence_EncapsulatedAssociation82", None)
        self.__persistence_EncapsulatedAssociation82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Entity83"):
                opp_val = getattr(old_value, "persistence_Entity83", None)
                if opp_val == self:
                    setattr(old_value, "persistence_Entity83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Entity83"):
                opp_val = getattr(value, "persistence_Entity83", None)
                setattr(value, "persistence_Entity83", self)

    @property
    def encapsulatedBy(self):
        return self.__encapsulatedBy

    @encapsulatedBy.setter
    def encapsulatedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EncapsulatedAssociation__encapsulatedBy", None)
        self.__encapsulatedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Association"):
                opp_val = getattr(old_value, "Association", None)
                if opp_val == self:
                    setattr(old_value, "Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Association"):
                opp_val = getattr(value, "Association", None)
                setattr(value, "Association", self)

    @property
    def persistence_EncapsulatedAssociation77(self):
        return self.__persistence_EncapsulatedAssociation77

    @persistence_EncapsulatedAssociation77.setter
    def persistence_EncapsulatedAssociation77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EncapsulatedAssociation__persistence_EncapsulatedAssociation77", None)
        self.__persistence_EncapsulatedAssociation77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EncapsulatedAssociation"):
                opp_val = getattr(old_value, "persistence_EncapsulatedAssociation", None)
                if opp_val == self:
                    setattr(old_value, "persistence_EncapsulatedAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EncapsulatedAssociation"):
                opp_val = getattr(value, "persistence_EncapsulatedAssociation", None)
                setattr(value, "persistence_EncapsulatedAssociation", self)

    @property
    def EncapsulatedAssociation(self):
        return self.__EncapsulatedAssociation

    @EncapsulatedAssociation.setter
    def EncapsulatedAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EncapsulatedAssociation__EncapsulatedAssociation", None)
        self.__EncapsulatedAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "association"):
                opp_val = getattr(old_value, "association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "association"):
                opp_val = getattr(value, "association", None)
                if opp_val is None:
                    setattr(value, "association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_EncapsulatedAssociation(self):
        return self.__persistence_EncapsulatedAssociation

    @persistence_EncapsulatedAssociation.setter
    def persistence_EncapsulatedAssociation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EncapsulatedAssociation__persistence_EncapsulatedAssociation", None)
        self.__persistence_EncapsulatedAssociation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EncapsulatedAssociation77"):
                opp_val = getattr(old_value, "persistence_EncapsulatedAssociation77", None)
                if opp_val == self:
                    setattr(old_value, "persistence_EncapsulatedAssociation77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EncapsulatedAssociation77"):
                opp_val = getattr(value, "persistence_EncapsulatedAssociation77", None)
                setattr(value, "persistence_EncapsulatedAssociation77", self)

    @property
    def persistence_EncapsulatedAssociation85(self):
        return self.__persistence_EncapsulatedAssociation85

    @persistence_EncapsulatedAssociation85.setter
    def persistence_EncapsulatedAssociation85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EncapsulatedAssociation__persistence_EncapsulatedAssociation85", None)
        self.__persistence_EncapsulatedAssociation85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_ViewAssociation"):
                opp_val = getattr(old_value, "persistence_ViewAssociation", None)
                if opp_val == self:
                    setattr(old_value, "persistence_ViewAssociation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_ViewAssociation"):
                opp_val = getattr(value, "persistence_ViewAssociation", None)
                setattr(value, "persistence_ViewAssociation", self)

class persistence_Expression:

    pass
class Label:

    pass
class Feature:

    pass
class persistence_EntityFeature(Feature, NamedDisplayElement):

    def __init__(self, cardinality: str, ordered: bool, primaryKey: bool, derived: bool, customiseSet: bool, booleanIsHasChoice: str, singletonName: str, pluralisedName: str, columnName: str, EntityFeature: "persistence_Entity" = None, entityFeatures: "persistence_Entity" = None, persistence_EntityFeature68: "persistence_AssociationKey" = None, persistence_EntityFeature: "persistence_AssociationKey" = None):
        self.cardinality = cardinality
        self.ordered = ordered
        self.primaryKey = primaryKey
        self.derived = derived
        self.customiseSet = customiseSet
        self.booleanIsHasChoice = booleanIsHasChoice
        self.singletonName = singletonName
        self.pluralisedName = pluralisedName
        self.columnName = columnName
        self.EntityFeature = EntityFeature
        self.entityFeatures = entityFeatures
        self.persistence_EntityFeature68 = persistence_EntityFeature68
        self.persistence_EntityFeature = persistence_EntityFeature
        
    @property
    def columnName(self) -> str:
        return self.__columnName

    @columnName.setter
    def columnName(self, columnName: str):
        self.__columnName = columnName

    @property
    def cardinality(self) -> str:
        return self.__cardinality

    @cardinality.setter
    def cardinality(self, cardinality: str):
        self.__cardinality = cardinality

    @property
    def primaryKey(self) -> bool:
        return self.__primaryKey

    @primaryKey.setter
    def primaryKey(self, primaryKey: bool):
        self.__primaryKey = primaryKey

    @property
    def booleanIsHasChoice(self) -> str:
        return self.__booleanIsHasChoice

    @booleanIsHasChoice.setter
    def booleanIsHasChoice(self, booleanIsHasChoice: str):
        self.__booleanIsHasChoice = booleanIsHasChoice

    @property
    def customiseSet(self) -> bool:
        return self.__customiseSet

    @customiseSet.setter
    def customiseSet(self, customiseSet: bool):
        self.__customiseSet = customiseSet

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
    def derived(self) -> bool:
        return self.__derived

    @derived.setter
    def derived(self, derived: bool):
        self.__derived = derived

    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def persistence_EntityFeature68(self):
        return self.__persistence_EntityFeature68

    @persistence_EntityFeature68.setter
    def persistence_EntityFeature68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityFeature__persistence_EntityFeature68", None)
        self.__persistence_EntityFeature68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_AssociationKey67"):
                opp_val = getattr(old_value, "persistence_AssociationKey67", None)
                if opp_val == self:
                    setattr(old_value, "persistence_AssociationKey67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_AssociationKey67"):
                opp_val = getattr(value, "persistence_AssociationKey67", None)
                setattr(value, "persistence_AssociationKey67", self)

    @property
    def persistence_EntityFeature(self):
        return self.__persistence_EntityFeature

    @persistence_EntityFeature.setter
    def persistence_EntityFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityFeature__persistence_EntityFeature", None)
        self.__persistence_EntityFeature = value
        
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

    @property
    def EntityFeature(self):
        return self.__EntityFeature

    @EntityFeature.setter
    def EntityFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityFeature__EntityFeature", None)
        self.__EntityFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partOf52"):
                opp_val = getattr(old_value, "partOf52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partOf52"):
                opp_val = getattr(value, "partOf52", None)
                if opp_val is None:
                    setattr(value, "partOf52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def entityFeatures(self):
        return self.__entityFeatures

    @entityFeatures.setter
    def entityFeatures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityFeature__entityFeatures", None)
        self.__entityFeatures = value
        
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

class persistence_ViewFeature(Feature):

    pass
class persistence_Association(Feature):

    def __init__(self, inputClass: str, serializationMaxDepth: int, pseudo: bool, persistence_Association: "persistence_EntityOrView" = None, persistence_Association26: "persistence_EntityOrView" = None, association: set["persistence_EncapsulatedAssociation"] = None, persistence_Association34: "persistence_EntityOrView" = None, persistence_Association37: "persistence_EntityOrView" = None, Association: "persistence_EncapsulatedAssociation" = None):
        self.inputClass = inputClass
        self.serializationMaxDepth = serializationMaxDepth
        self.pseudo = pseudo
        self.persistence_Association = persistence_Association
        self.persistence_Association26 = persistence_Association26
        self.association = association if association is not None else set()
        self.persistence_Association34 = persistence_Association34
        self.persistence_Association37 = persistence_Association37
        self.Association = Association
        
    @property
    def serializationMaxDepth(self) -> int:
        return self.__serializationMaxDepth

    @serializationMaxDepth.setter
    def serializationMaxDepth(self, serializationMaxDepth: int):
        self.__serializationMaxDepth = serializationMaxDepth

    @property
    def pseudo(self) -> bool:
        return self.__pseudo

    @pseudo.setter
    def pseudo(self, pseudo: bool):
        self.__pseudo = pseudo

    @property
    def inputClass(self) -> str:
        return self.__inputClass

    @inputClass.setter
    def inputClass(self, inputClass: str):
        self.__inputClass = inputClass

    @property
    def association(self):
        return self.__association

    @association.setter
    def association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__association", None)
        self.__association = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EncapsulatedAssociation"):
                    opp_val = getattr(item, "EncapsulatedAssociation", None)
                    
                    if opp_val == self:
                        setattr(item, "EncapsulatedAssociation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EncapsulatedAssociation"):
                    opp_val = getattr(item, "EncapsulatedAssociation", None)
                    
                    setattr(item, "EncapsulatedAssociation", self)
                    

    @property
    def persistence_Association26(self):
        return self.__persistence_Association26

    @persistence_Association26.setter
    def persistence_Association26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__persistence_Association26", None)
        self.__persistence_Association26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EntityOrView25"):
                opp_val = getattr(old_value, "persistence_EntityOrView25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityOrView25"):
                opp_val = getattr(value, "persistence_EntityOrView25", None)
                if opp_val is None:
                    setattr(value, "persistence_EntityOrView25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Association34(self):
        return self.__persistence_Association34

    @persistence_Association34.setter
    def persistence_Association34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__persistence_Association34", None)
        self.__persistence_Association34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EntityOrView35"):
                opp_val = getattr(old_value, "persistence_EntityOrView35", None)
                if opp_val == self:
                    setattr(old_value, "persistence_EntityOrView35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityOrView35"):
                opp_val = getattr(value, "persistence_EntityOrView35", None)
                setattr(value, "persistence_EntityOrView35", self)

    @property
    def persistence_Association37(self):
        return self.__persistence_Association37

    @persistence_Association37.setter
    def persistence_Association37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Association__persistence_Association37", None)
        self.__persistence_Association37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EntityOrView38"):
                opp_val = getattr(old_value, "persistence_EntityOrView38", None)
                if opp_val == self:
                    setattr(old_value, "persistence_EntityOrView38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityOrView38"):
                opp_val = getattr(value, "persistence_EntityOrView38", None)
                setattr(value, "persistence_EntityOrView38", self)

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
            if hasattr(old_value, "persistence_EntityOrView23"):
                opp_val = getattr(old_value, "persistence_EntityOrView23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityOrView23"):
                opp_val = getattr(value, "persistence_EntityOrView23", None)
                if opp_val is None:
                    setattr(value, "persistence_EntityOrView23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "encapsulatedBy"):
                opp_val = getattr(old_value, "encapsulatedBy", None)
                if opp_val == self:
                    setattr(old_value, "encapsulatedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "encapsulatedBy"):
                opp_val = getattr(value, "encapsulatedBy", None)
                setattr(value, "encapsulatedBy", self)

class persistence_Attribute(Feature, Label):

    def __init__(self, validationPattern: str, inputClass: str, persistence_Attribute: "persistence_EntityOrView" = None, persistence_Attribute31: "persistence_Expression" = None, persistence_Attribute46: "persistence_ModelLabelAttribute" = None, persistence_Attribute56: "persistence_EntityAttribute" = None, persistence_Attribute75: "persistence_EncapsulatedAttribute" = None):
        self.validationPattern = validationPattern
        self.inputClass = inputClass
        self.persistence_Attribute = persistence_Attribute
        self.persistence_Attribute31 = persistence_Attribute31
        self.persistence_Attribute46 = persistence_Attribute46
        self.persistence_Attribute56 = persistence_Attribute56
        self.persistence_Attribute75 = persistence_Attribute75
        
    @property
    def validationPattern(self) -> str:
        return self.__validationPattern

    @validationPattern.setter
    def validationPattern(self, validationPattern: str):
        self.__validationPattern = validationPattern

    @property
    def inputClass(self) -> str:
        return self.__inputClass

    @inputClass.setter
    def inputClass(self, inputClass: str):
        self.__inputClass = inputClass

    @property
    def persistence_Attribute46(self):
        return self.__persistence_Attribute46

    @persistence_Attribute46.setter
    def persistence_Attribute46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Attribute__persistence_Attribute46", None)
        self.__persistence_Attribute46 = value
        
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
            if hasattr(old_value, "persistence_EntityOrView21"):
                opp_val = getattr(old_value, "persistence_EntityOrView21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityOrView21"):
                opp_val = getattr(value, "persistence_EntityOrView21", None)
                if opp_val is None:
                    setattr(value, "persistence_EntityOrView21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Attribute31(self):
        return self.__persistence_Attribute31

    @persistence_Attribute31.setter
    def persistence_Attribute31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Attribute__persistence_Attribute31", None)
        self.__persistence_Attribute31 = value
        
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
    def persistence_Attribute75(self):
        return self.__persistence_Attribute75

    @persistence_Attribute75.setter
    def persistence_Attribute75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Attribute__persistence_Attribute75", None)
        self.__persistence_Attribute75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EncapsulatedAttribute"):
                opp_val = getattr(old_value, "persistence_EncapsulatedAttribute", None)
                if opp_val == self:
                    setattr(old_value, "persistence_EncapsulatedAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EncapsulatedAttribute"):
                opp_val = getattr(value, "persistence_EncapsulatedAttribute", None)
                setattr(value, "persistence_EncapsulatedAttribute", self)

    @property
    def persistence_Attribute56(self):
        return self.__persistence_Attribute56

    @persistence_Attribute56.setter
    def persistence_Attribute56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Attribute__persistence_Attribute56", None)
        self.__persistence_Attribute56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EntityAttribute"):
                opp_val = getattr(old_value, "persistence_EntityAttribute", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityAttribute"):
                opp_val = getattr(value, "persistence_EntityAttribute", None)
                if opp_val is None:
                    setattr(value, "persistence_EntityAttribute", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class persistence_Feature(ABC):

    def __init__(self, title: str, collectionOrmAllowAdd: bool, collectionOrmAllowRemove: bool, placeholder: str, nullDisplayValue: str, encodeUriKey: bool, headerClass: str, displayClass: str, footerClass: str, persistence_Feature: "persistence_EntityOrView" = None, persistence_Feature9: "persistence_EntityOrView" = None, persistence_Feature12: "persistence_EntityOrView" = None, persistence_Feature16: "persistence_EntityOrView" = None, persistence_Feature19: "persistence_EntityOrView" = None, persistence_Feature28: set["persistence_SerializationGroup"] = None):
        self.title = title
        self.collectionOrmAllowAdd = collectionOrmAllowAdd
        self.collectionOrmAllowRemove = collectionOrmAllowRemove
        self.placeholder = placeholder
        self.nullDisplayValue = nullDisplayValue
        self.encodeUriKey = encodeUriKey
        self.headerClass = headerClass
        self.displayClass = displayClass
        self.footerClass = footerClass
        self.persistence_Feature = persistence_Feature
        self.persistence_Feature9 = persistence_Feature9
        self.persistence_Feature12 = persistence_Feature12
        self.persistence_Feature16 = persistence_Feature16
        self.persistence_Feature19 = persistence_Feature19
        self.persistence_Feature28 = persistence_Feature28 if persistence_Feature28 is not None else set()
        
    @property
    def headerClass(self) -> str:
        return self.__headerClass

    @headerClass.setter
    def headerClass(self, headerClass: str):
        self.__headerClass = headerClass

    @property
    def nullDisplayValue(self) -> str:
        return self.__nullDisplayValue

    @nullDisplayValue.setter
    def nullDisplayValue(self, nullDisplayValue: str):
        self.__nullDisplayValue = nullDisplayValue

    @property
    def encodeUriKey(self) -> bool:
        return self.__encodeUriKey

    @encodeUriKey.setter
    def encodeUriKey(self, encodeUriKey: bool):
        self.__encodeUriKey = encodeUriKey

    @property
    def placeholder(self) -> str:
        return self.__placeholder

    @placeholder.setter
    def placeholder(self, placeholder: str):
        self.__placeholder = placeholder

    @property
    def footerClass(self) -> str:
        return self.__footerClass

    @footerClass.setter
    def footerClass(self, footerClass: str):
        self.__footerClass = footerClass

    @property
    def collectionOrmAllowRemove(self) -> bool:
        return self.__collectionOrmAllowRemove

    @collectionOrmAllowRemove.setter
    def collectionOrmAllowRemove(self, collectionOrmAllowRemove: bool):
        self.__collectionOrmAllowRemove = collectionOrmAllowRemove

    @property
    def collectionOrmAllowAdd(self) -> bool:
        return self.__collectionOrmAllowAdd

    @collectionOrmAllowAdd.setter
    def collectionOrmAllowAdd(self, collectionOrmAllowAdd: bool):
        self.__collectionOrmAllowAdd = collectionOrmAllowAdd

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def displayClass(self) -> str:
        return self.__displayClass

    @displayClass.setter
    def displayClass(self, displayClass: str):
        self.__displayClass = displayClass

    @property
    def persistence_Feature16(self):
        return self.__persistence_Feature16

    @persistence_Feature16.setter
    def persistence_Feature16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature16", None)
        self.__persistence_Feature16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EntityOrView15"):
                opp_val = getattr(old_value, "persistence_EntityOrView15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityOrView15"):
                opp_val = getattr(value, "persistence_EntityOrView15", None)
                if opp_val is None:
                    setattr(value, "persistence_EntityOrView15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Feature12(self):
        return self.__persistence_Feature12

    @persistence_Feature12.setter
    def persistence_Feature12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature12", None)
        self.__persistence_Feature12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EntityOrView11"):
                opp_val = getattr(old_value, "persistence_EntityOrView11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityOrView11"):
                opp_val = getattr(value, "persistence_EntityOrView11", None)
                if opp_val is None:
                    setattr(value, "persistence_EntityOrView11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Feature(self):
        return self.__persistence_Feature

    @persistence_Feature.setter
    def persistence_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature", None)
        self.__persistence_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EntityOrView6"):
                opp_val = getattr(old_value, "persistence_EntityOrView6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityOrView6"):
                opp_val = getattr(value, "persistence_EntityOrView6", None)
                if opp_val is None:
                    setattr(value, "persistence_EntityOrView6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Feature28(self):
        return self.__persistence_Feature28

    @persistence_Feature28.setter
    def persistence_Feature28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature28", None)
        self.__persistence_Feature28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_SerializationGroup29"):
                    opp_val = getattr(item, "persistence_SerializationGroup29", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_SerializationGroup29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_SerializationGroup29"):
                    opp_val = getattr(item, "persistence_SerializationGroup29", None)
                    
                    setattr(item, "persistence_SerializationGroup29", self)
                    

    @property
    def persistence_Feature19(self):
        return self.__persistence_Feature19

    @persistence_Feature19.setter
    def persistence_Feature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature19", None)
        self.__persistence_Feature19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EntityOrView18"):
                opp_val = getattr(old_value, "persistence_EntityOrView18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityOrView18"):
                opp_val = getattr(value, "persistence_EntityOrView18", None)
                if opp_val is None:
                    setattr(value, "persistence_EntityOrView18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_Feature9(self):
        return self.__persistence_Feature9

    @persistence_Feature9.setter
    def persistence_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_Feature__persistence_Feature9", None)
        self.__persistence_Feature9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_EntityOrView8"):
                opp_val = getattr(old_value, "persistence_EntityOrView8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_EntityOrView8"):
                opp_val = getattr(value, "persistence_EntityOrView8", None)
                if opp_val is None:
                    setattr(value, "persistence_EntityOrView8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Classifier:

    pass
class NamedElement:

    pass
class persistence_ModelLabel(NamedElement, Label):

    def __init__(self, format: str, customise: bool, ModelLabel: "persistence_EntityOrView" = None, labels: "persistence_EntityOrView" = None, partOf: set["persistence_ModelLabelFeature"] = None, persistence_ModelLabel: set["persistence_SerializationGroup"] = None, ModelLabel44: "persistence_ModelLabelFeature" = None, persistence_ModelLabel50: "persistence_ModelLabelAssociation" = None):
        self.format = format
        self.customise = customise
        self.ModelLabel = ModelLabel
        self.labels = labels
        self.partOf = partOf if partOf is not None else set()
        self.persistence_ModelLabel = persistence_ModelLabel if persistence_ModelLabel is not None else set()
        self.ModelLabel44 = ModelLabel44
        self.persistence_ModelLabel50 = persistence_ModelLabel50
        
    @property
    def customise(self) -> bool:
        return self.__customise

    @customise.setter
    def customise(self, customise: bool):
        self.__customise = customise

    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def ModelLabel44(self):
        return self.__ModelLabel44

    @ModelLabel44.setter
    def ModelLabel44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabel__ModelLabel44", None)
        self.__ModelLabel44 = value
        
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
    def labels(self):
        return self.__labels

    @labels.setter
    def labels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabel__labels", None)
        self.__labels = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntityOrView"):
                opp_val = getattr(old_value, "EntityOrView", None)
                if opp_val == self:
                    setattr(old_value, "EntityOrView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntityOrView"):
                opp_val = getattr(value, "EntityOrView", None)
                setattr(value, "EntityOrView", self)

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
                if hasattr(item, "persistence_SerializationGroup42"):
                    opp_val = getattr(item, "persistence_SerializationGroup42", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_SerializationGroup42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_SerializationGroup42"):
                    opp_val = getattr(item, "persistence_SerializationGroup42", None)
                    
                    setattr(item, "persistence_SerializationGroup42", self)
                    

    @property
    def persistence_ModelLabel50(self):
        return self.__persistence_ModelLabel50

    @persistence_ModelLabel50.setter
    def persistence_ModelLabel50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabel__persistence_ModelLabel50", None)
        self.__persistence_ModelLabel50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_ModelLabelAssociation49"):
                opp_val = getattr(old_value, "persistence_ModelLabelAssociation49", None)
                if opp_val == self:
                    setattr(old_value, "persistence_ModelLabelAssociation49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_ModelLabelAssociation49"):
                opp_val = getattr(value, "persistence_ModelLabelAssociation49", None)
                setattr(value, "persistence_ModelLabelAssociation49", self)

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
    def ModelLabel(self):
        return self.__ModelLabel

    @ModelLabel.setter
    def ModelLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_ModelLabel__ModelLabel", None)
        self.__ModelLabel = value
        
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

class persistence_EntityOrView(Classifier):

    def __init__(self, singletonName: str, pluralisedName: str, tableName: str, autoKeyName: str, autoKeyPersistentType: str, autoKeyGenerationStrategy: str, implementsUserInterface: bool, allowFormTypeCustomisation: bool, persistence_EntityOrView: "persistence_Persistence" = None, persistence_EntityOrView6: set["persistence_Feature"] = None, persistence_EntityOrView8: set["persistence_Feature"] = None, persistence_EntityOrView11: set["persistence_Feature"] = None, labelFor: set["persistence_ModelLabel"] = None, persistence_EntityOrView15: set["persistence_Feature"] = None, persistence_EntityOrView18: set["persistence_Feature"] = None, persistence_EntityOrView21: set["persistence_Attribute"] = None, persistence_EntityOrView23: set["persistence_Association"] = None, persistence_EntityOrView25: set["persistence_Association"] = None, persistence_EntityOrView35: "persistence_Association" = None, persistence_EntityOrView38: "persistence_Association" = None, EntityOrView: "persistence_ModelLabel" = None, persistence_EntityOrView70: "persistence_View" = None):
        self.singletonName = singletonName
        self.pluralisedName = pluralisedName
        self.tableName = tableName
        self.autoKeyName = autoKeyName
        self.autoKeyPersistentType = autoKeyPersistentType
        self.autoKeyGenerationStrategy = autoKeyGenerationStrategy
        self.implementsUserInterface = implementsUserInterface
        self.allowFormTypeCustomisation = allowFormTypeCustomisation
        self.persistence_EntityOrView = persistence_EntityOrView
        self.persistence_EntityOrView6 = persistence_EntityOrView6 if persistence_EntityOrView6 is not None else set()
        self.persistence_EntityOrView8 = persistence_EntityOrView8 if persistence_EntityOrView8 is not None else set()
        self.persistence_EntityOrView11 = persistence_EntityOrView11 if persistence_EntityOrView11 is not None else set()
        self.labelFor = labelFor if labelFor is not None else set()
        self.persistence_EntityOrView15 = persistence_EntityOrView15 if persistence_EntityOrView15 is not None else set()
        self.persistence_EntityOrView18 = persistence_EntityOrView18 if persistence_EntityOrView18 is not None else set()
        self.persistence_EntityOrView21 = persistence_EntityOrView21 if persistence_EntityOrView21 is not None else set()
        self.persistence_EntityOrView23 = persistence_EntityOrView23 if persistence_EntityOrView23 is not None else set()
        self.persistence_EntityOrView25 = persistence_EntityOrView25 if persistence_EntityOrView25 is not None else set()
        self.persistence_EntityOrView35 = persistence_EntityOrView35
        self.persistence_EntityOrView38 = persistence_EntityOrView38
        self.EntityOrView = EntityOrView
        self.persistence_EntityOrView70 = persistence_EntityOrView70
        
    @property
    def tableName(self) -> str:
        return self.__tableName

    @tableName.setter
    def tableName(self, tableName: str):
        self.__tableName = tableName

    @property
    def autoKeyPersistentType(self) -> str:
        return self.__autoKeyPersistentType

    @autoKeyPersistentType.setter
    def autoKeyPersistentType(self, autoKeyPersistentType: str):
        self.__autoKeyPersistentType = autoKeyPersistentType

    @property
    def allowFormTypeCustomisation(self) -> bool:
        return self.__allowFormTypeCustomisation

    @allowFormTypeCustomisation.setter
    def allowFormTypeCustomisation(self, allowFormTypeCustomisation: bool):
        self.__allowFormTypeCustomisation = allowFormTypeCustomisation

    @property
    def pluralisedName(self) -> str:
        return self.__pluralisedName

    @pluralisedName.setter
    def pluralisedName(self, pluralisedName: str):
        self.__pluralisedName = pluralisedName

    @property
    def autoKeyGenerationStrategy(self) -> str:
        return self.__autoKeyGenerationStrategy

    @autoKeyGenerationStrategy.setter
    def autoKeyGenerationStrategy(self, autoKeyGenerationStrategy: str):
        self.__autoKeyGenerationStrategy = autoKeyGenerationStrategy

    @property
    def autoKeyName(self) -> str:
        return self.__autoKeyName

    @autoKeyName.setter
    def autoKeyName(self, autoKeyName: str):
        self.__autoKeyName = autoKeyName

    @property
    def singletonName(self) -> str:
        return self.__singletonName

    @singletonName.setter
    def singletonName(self, singletonName: str):
        self.__singletonName = singletonName

    @property
    def implementsUserInterface(self) -> bool:
        return self.__implementsUserInterface

    @implementsUserInterface.setter
    def implementsUserInterface(self, implementsUserInterface: bool):
        self.__implementsUserInterface = implementsUserInterface

    @property
    def persistence_EntityOrView21(self):
        return self.__persistence_EntityOrView21

    @persistence_EntityOrView21.setter
    def persistence_EntityOrView21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView21", None)
        self.__persistence_EntityOrView21 = value if value is not None else set()
        
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
    def persistence_EntityOrView23(self):
        return self.__persistence_EntityOrView23

    @persistence_EntityOrView23.setter
    def persistence_EntityOrView23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView23", None)
        self.__persistence_EntityOrView23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Association"):
                    opp_val = getattr(item, "persistence_Association", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Association"):
                    opp_val = getattr(item, "persistence_Association", None)
                    
                    setattr(item, "persistence_Association", self)
                    

    @property
    def persistence_EntityOrView70(self):
        return self.__persistence_EntityOrView70

    @persistence_EntityOrView70.setter
    def persistence_EntityOrView70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView70", None)
        self.__persistence_EntityOrView70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_View"):
                opp_val = getattr(old_value, "persistence_View", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_View"):
                opp_val = getattr(value, "persistence_View", None)
                if opp_val is None:
                    setattr(value, "persistence_View", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persistence_EntityOrView11(self):
        return self.__persistence_EntityOrView11

    @persistence_EntityOrView11.setter
    def persistence_EntityOrView11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView11", None)
        self.__persistence_EntityOrView11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Feature12"):
                    opp_val = getattr(item, "persistence_Feature12", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Feature12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Feature12"):
                    opp_val = getattr(item, "persistence_Feature12", None)
                    
                    setattr(item, "persistence_Feature12", self)
                    

    @property
    def persistence_EntityOrView8(self):
        return self.__persistence_EntityOrView8

    @persistence_EntityOrView8.setter
    def persistence_EntityOrView8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView8", None)
        self.__persistence_EntityOrView8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Feature9"):
                    opp_val = getattr(item, "persistence_Feature9", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Feature9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Feature9"):
                    opp_val = getattr(item, "persistence_Feature9", None)
                    
                    setattr(item, "persistence_Feature9", self)
                    

    @property
    def persistence_EntityOrView25(self):
        return self.__persistence_EntityOrView25

    @persistence_EntityOrView25.setter
    def persistence_EntityOrView25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView25", None)
        self.__persistence_EntityOrView25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Association26"):
                    opp_val = getattr(item, "persistence_Association26", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Association26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Association26"):
                    opp_val = getattr(item, "persistence_Association26", None)
                    
                    setattr(item, "persistence_Association26", self)
                    

    @property
    def persistence_EntityOrView38(self):
        return self.__persistence_EntityOrView38

    @persistence_EntityOrView38.setter
    def persistence_EntityOrView38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView38", None)
        self.__persistence_EntityOrView38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Association37"):
                opp_val = getattr(old_value, "persistence_Association37", None)
                if opp_val == self:
                    setattr(old_value, "persistence_Association37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Association37"):
                opp_val = getattr(value, "persistence_Association37", None)
                setattr(value, "persistence_Association37", self)

    @property
    def persistence_EntityOrView6(self):
        return self.__persistence_EntityOrView6

    @persistence_EntityOrView6.setter
    def persistence_EntityOrView6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView6", None)
        self.__persistence_EntityOrView6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Feature"):
                    opp_val = getattr(item, "persistence_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Feature"):
                    opp_val = getattr(item, "persistence_Feature", None)
                    
                    setattr(item, "persistence_Feature", self)
                    

    @property
    def persistence_EntityOrView18(self):
        return self.__persistence_EntityOrView18

    @persistence_EntityOrView18.setter
    def persistence_EntityOrView18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView18", None)
        self.__persistence_EntityOrView18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Feature19"):
                    opp_val = getattr(item, "persistence_Feature19", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Feature19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Feature19"):
                    opp_val = getattr(item, "persistence_Feature19", None)
                    
                    setattr(item, "persistence_Feature19", self)
                    

    @property
    def EntityOrView(self):
        return self.__EntityOrView

    @EntityOrView.setter
    def EntityOrView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__EntityOrView", None)
        self.__EntityOrView = value
        
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
    def persistence_EntityOrView(self):
        return self.__persistence_EntityOrView

    @persistence_EntityOrView.setter
    def persistence_EntityOrView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView", None)
        self.__persistence_EntityOrView = value
        
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
    def persistence_EntityOrView35(self):
        return self.__persistence_EntityOrView35

    @persistence_EntityOrView35.setter
    def persistence_EntityOrView35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView35", None)
        self.__persistence_EntityOrView35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persistence_Association34"):
                opp_val = getattr(old_value, "persistence_Association34", None)
                if opp_val == self:
                    setattr(old_value, "persistence_Association34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persistence_Association34"):
                opp_val = getattr(value, "persistence_Association34", None)
                setattr(value, "persistence_Association34", self)

    @property
    def labelFor(self):
        return self.__labelFor

    @labelFor.setter
    def labelFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__labelFor", None)
        self.__labelFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelLabel"):
                    opp_val = getattr(item, "ModelLabel", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelLabel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelLabel"):
                    opp_val = getattr(item, "ModelLabel", None)
                    
                    setattr(item, "ModelLabel", self)
                    

    @property
    def persistence_EntityOrView15(self):
        return self.__persistence_EntityOrView15

    @persistence_EntityOrView15.setter
    def persistence_EntityOrView15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persistence_EntityOrView__persistence_EntityOrView15", None)
        self.__persistence_EntityOrView15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persistence_Feature16"):
                    opp_val = getattr(item, "persistence_Feature16", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_Feature16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_Feature16"):
                    opp_val = getattr(item, "persistence_Feature16", None)
                    
                    setattr(item, "persistence_Feature16", self)
                    

class persistence_DataType:

    pass
class persistence_SerializationGroup(NamedElement):

    pass
class persistence_Persistence:

    def __init__(self, ormTechnology: str, databaseTechnology: str, timestampCreation: bool, timestampUpdates: bool, persistence_Persistence: set["persistence_SerializationGroup"] = None, persistence_Persistence2: set["persistence_DataType"] = None, persistence_Persistence4: set["persistence_EntityOrView"] = None):
        self.ormTechnology = ormTechnology
        self.databaseTechnology = databaseTechnology
        self.timestampCreation = timestampCreation
        self.timestampUpdates = timestampUpdates
        self.persistence_Persistence = persistence_Persistence if persistence_Persistence is not None else set()
        self.persistence_Persistence2 = persistence_Persistence2 if persistence_Persistence2 is not None else set()
        self.persistence_Persistence4 = persistence_Persistence4 if persistence_Persistence4 is not None else set()
        
    @property
    def timestampCreation(self) -> bool:
        return self.__timestampCreation

    @timestampCreation.setter
    def timestampCreation(self, timestampCreation: bool):
        self.__timestampCreation = timestampCreation

    @property
    def databaseTechnology(self) -> str:
        return self.__databaseTechnology

    @databaseTechnology.setter
    def databaseTechnology(self, databaseTechnology: str):
        self.__databaseTechnology = databaseTechnology

    @property
    def ormTechnology(self) -> str:
        return self.__ormTechnology

    @ormTechnology.setter
    def ormTechnology(self, ormTechnology: str):
        self.__ormTechnology = ormTechnology

    @property
    def timestampUpdates(self) -> bool:
        return self.__timestampUpdates

    @timestampUpdates.setter
    def timestampUpdates(self, timestampUpdates: bool):
        self.__timestampUpdates = timestampUpdates

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
                if hasattr(item, "persistence_EntityOrView"):
                    opp_val = getattr(item, "persistence_EntityOrView", None)
                    
                    if opp_val == self:
                        setattr(item, "persistence_EntityOrView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persistence_EntityOrView"):
                    opp_val = getattr(item, "persistence_EntityOrView", None)
                    
                    setattr(item, "persistence_EntityOrView", self)
                    

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
                    
