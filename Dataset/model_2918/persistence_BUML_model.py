####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
Cardinality: Enumeration = Enumeration(
    name="Cardinality",
    literals={
            EnumerationLiteral(name="Optional"),
			EnumerationLiteral(name="Required"),
			EnumerationLiteral(name="Many")
    }
)

DatabaseTechnologies: Enumeration = Enumeration(
    name="DatabaseTechnologies",
    literals={
            EnumerationLiteral(name="MySql"),
			EnumerationLiteral(name="Oracle")
    }
)

OrmTechnologies: Enumeration = Enumeration(
    name="OrmTechnologies",
    literals={
            EnumerationLiteral(name="DataMapper"),
			EnumerationLiteral(name="Idiorm"),
			EnumerationLiteral(name="Kohana"),
			EnumerationLiteral(name="DoctrineORM"),
			EnumerationLiteral(name="DoctrineODM"),
			EnumerationLiteral(name="JPA")
    }
)

isHasChoices: Enumeration = Enumeration(
    name="isHasChoices",
    literals={
            EnumerationLiteral(name="isA"),
			EnumerationLiteral(name="hasA")
    }
)

DateDetails: Enumeration = Enumeration(
    name="DateDetails",
    literals={
            EnumerationLiteral(name="DateOnly"),
			EnumerationLiteral(name="TimeOnly"),
			EnumerationLiteral(name="DateAndTime")
    }
)

# Classes
persistence_Persistence = Class(name="persistence::Persistence")
NamedElement = Class(name="NamedElement")
persistence_SerializationGroup = Class(name="persistence::SerializationGroup")
persistence_DataType = Class(name="persistence::DataType")
persistence_Entity = Class(name="persistence::Entity")
persistence_Feature = Class(name="persistence::Feature", is_abstract=True)
NamedDisplayElement = Class(name="NamedDisplayElement")
persistence_Expression = Class(name="persistence::Expression")
persistence_Attribute = Class(name="persistence::Attribute", is_abstract=True)
Feature = Class(name="Feature")
Label = Class(name="Label")
persistence_Label = Class(name="persistence::Label", is_abstract=True)
persistence_ModelLabel = Class(name="persistence::ModelLabel")
persistence_Association = Class(name="persistence::Association", is_abstract=True)
persistence_AssociationKey = Class(name="persistence::AssociationKey")
Classifier = Class(name="Classifier")
persistence_ModelLabelFeature = Class(name="persistence::ModelLabelFeature", is_abstract=True)
persistence_ModelLabelAttribute = Class(name="persistence::ModelLabelAttribute")
ModelLabelFeature = Class(name="ModelLabelFeature")
persistence_ModelLabelAssociation = Class(name="persistence::ModelLabelAssociation")
persistence_PathElement = Class(name="persistence::PathElement", is_abstract=True)
persistence_StaticPathElement = Class(name="persistence::StaticPathElement")
PathElement = Class(name="PathElement")
persistence_DatePathElement = Class(name="persistence::DatePathElement")
persistence_FileAttribute = Class(name="persistence::FileAttribute")
ResourceAttribute = Class(name="ResourceAttribute")
persistence_ImageAttribute = Class(name="persistence::ImageAttribute")
persistence_DataTypeAttribute = Class(name="persistence::DataTypeAttribute")
Attribute = Class(name="Attribute")
persistence_DateAttribute = Class(name="persistence::DateAttribute")
persistence_UrlAttribute = Class(name="persistence::UrlAttribute")
persistence_ResourceAttribute = Class(name="persistence::ResourceAttribute", is_abstract=True)
persistence_LocationAttribute = Class(name="persistence::LocationAttribute")
persistence_AssociationWithoutContainment = Class(name="persistence::AssociationWithoutContainment")
Association = Class(name="Association")
persistence_AssociationWithContainment = Class(name="persistence::AssociationWithContainment")

# persistence_Persistence class attributes and methods
persistence_Persistence_ormTechnology: Property = Property(name="ormTechnology", type=StringType)
persistence_Persistence_databaseTechnology: Property = Property(name="databaseTechnology", type=StringType)
persistence_Persistence_timestampCreation: Property = Property(name="timestampCreation", type=BooleanType)
persistence_Persistence_timestampUpdates: Property = Property(name="timestampUpdates", type=BooleanType)
persistence_Persistence.attributes={persistence_Persistence_ormTechnology, persistence_Persistence_timestampCreation, persistence_Persistence_timestampUpdates, persistence_Persistence_databaseTechnology}

# NamedElement class attributes and methods

# persistence_SerializationGroup class attributes and methods

# persistence_DataType class attributes and methods

# persistence_Entity class attributes and methods
persistence_Entity_tableName: Property = Property(name="tableName", type=StringType)
persistence_Entity_autoKeyName: Property = Property(name="autoKeyName", type=StringType)
persistence_Entity_singletonName: Property = Property(name="singletonName", type=StringType)
persistence_Entity_pluralisedName: Property = Property(name="pluralisedName", type=StringType)
persistence_Entity_autoKeyPersistentType: Property = Property(name="autoKeyPersistentType", type=StringType)
persistence_Entity_autoKeyGenerationStrategy: Property = Property(name="autoKeyGenerationStrategy", type=StringType)
persistence_Entity_implementsUserInterface: Property = Property(name="implementsUserInterface", type=BooleanType)
persistence_Entity_allowFormTypeCustomisation: Property = Property(name="allowFormTypeCustomisation", type=BooleanType)
persistence_Entity.attributes={persistence_Entity_implementsUserInterface, persistence_Entity_autoKeyPersistentType, persistence_Entity_autoKeyName, persistence_Entity_tableName, persistence_Entity_autoKeyGenerationStrategy, persistence_Entity_allowFormTypeCustomisation, persistence_Entity_singletonName, persistence_Entity_pluralisedName}

# persistence_Feature class attributes and methods
persistence_Feature_collectionOrmAllowRemove: Property = Property(name="collectionOrmAllowRemove", type=BooleanType)
persistence_Feature_defaultDisplayValue: Property = Property(name="defaultDisplayValue", type=StringType)
persistence_Feature_emptyDisplayValue: Property = Property(name="emptyDisplayValue", type=StringType)
persistence_Feature_encodeUriKey: Property = Property(name="encodeUriKey", type=BooleanType)
persistence_Feature_singletonName: Property = Property(name="singletonName", type=StringType)
persistence_Feature_pluralisedName: Property = Property(name="pluralisedName", type=StringType)
persistence_Feature_columnName: Property = Property(name="columnName", type=StringType)
persistence_Feature_cardinality: Property = Property(name="cardinality", type=StringType)
persistence_Feature_ordered: Property = Property(name="ordered", type=BooleanType)
persistence_Feature_primaryKey: Property = Property(name="primaryKey", type=BooleanType)
persistence_Feature_derived: Property = Property(name="derived", type=BooleanType)
persistence_Feature_customiseSet: Property = Property(name="customiseSet", type=BooleanType)
persistence_Feature_booleanIsHasChoice: Property = Property(name="booleanIsHasChoice", type=StringType)
persistence_Feature_title: Property = Property(name="title", type=StringType)
persistence_Feature_collectionOrmAllowAdd: Property = Property(name="collectionOrmAllowAdd", type=BooleanType)
persistence_Feature_headerClass: Property = Property(name="headerClass", type=StringType)
persistence_Feature_displayClass: Property = Property(name="displayClass", type=StringType)
persistence_Feature_footerClass: Property = Property(name="footerClass", type=StringType)
persistence_Feature.attributes={persistence_Feature_emptyDisplayValue, persistence_Feature_derived, persistence_Feature_title, persistence_Feature_primaryKey, persistence_Feature_cardinality, persistence_Feature_columnName, persistence_Feature_encodeUriKey, persistence_Feature_customiseSet, persistence_Feature_collectionOrmAllowRemove, persistence_Feature_defaultDisplayValue, persistence_Feature_headerClass, persistence_Feature_footerClass, persistence_Feature_ordered, persistence_Feature_collectionOrmAllowAdd, persistence_Feature_singletonName, persistence_Feature_displayClass, persistence_Feature_booleanIsHasChoice, persistence_Feature_pluralisedName}

# NamedDisplayElement class attributes and methods

# persistence_Expression class attributes and methods

# persistence_Attribute class attributes and methods
persistence_Attribute_placeholder: Property = Property(name="placeholder", type=StringType)
persistence_Attribute_validationPattern: Property = Property(name="validationPattern", type=StringType)
persistence_Attribute_inputColumnClass: Property = Property(name="inputColumnClass", type=StringType)
persistence_Attribute_inputElementClass: Property = Property(name="inputElementClass", type=StringType)
persistence_Attribute_hidden: Property = Property(name="hidden", type=BooleanType)
persistence_Attribute_containerUnique: Property = Property(name="containerUnique", type=BooleanType)
persistence_Attribute_persistentType: Property = Property(name="persistentType", type=StringType)
persistence_Attribute_ormType: Property = Property(name="ormType", type=StringType)
persistence_Attribute_interfaceType: Property = Property(name="interfaceType", type=StringType)
persistence_Attribute_unique: Property = Property(name="unique", type=BooleanType)
persistence_Attribute.attributes={persistence_Attribute_containerUnique, persistence_Attribute_inputElementClass, persistence_Attribute_inputColumnClass, persistence_Attribute_placeholder, persistence_Attribute_unique, persistence_Attribute_interfaceType, persistence_Attribute_hidden, persistence_Attribute_persistentType, persistence_Attribute_ormType, persistence_Attribute_validationPattern}

# Feature class attributes and methods

# Label class attributes and methods

# persistence_Label class attributes and methods

# persistence_ModelLabel class attributes and methods
persistence_ModelLabel_format: Property = Property(name="format", type=StringType)
persistence_ModelLabel_customise: Property = Property(name="customise", type=BooleanType)
persistence_ModelLabel.attributes={persistence_ModelLabel_format, persistence_ModelLabel_customise}

# persistence_Association class attributes and methods
persistence_Association_targetHeaderClass: Property = Property(name="targetHeaderClass", type=StringType)
persistence_Association_targetInputClass: Property = Property(name="targetInputClass", type=StringType)
persistence_Association_targetDisplayClass: Property = Property(name="targetDisplayClass", type=StringType)
persistence_Association_targetFooterClass: Property = Property(name="targetFooterClass", type=StringType)
persistence_Association_pseudo: Property = Property(name="pseudo", type=BooleanType)
persistence_Association_inputColumnClass: Property = Property(name="inputColumnClass", type=StringType)
persistence_Association_inputElementClass: Property = Property(name="inputElementClass", type=StringType)
persistence_Association_serializationMaxDepth: Property = Property(name="serializationMaxDepth", type=IntegerType)
persistence_Association_bidirectional: Property = Property(name="bidirectional", type=BooleanType)
persistence_Association_unique: Property = Property(name="unique", type=BooleanType)
persistence_Association_pivotTableName: Property = Property(name="pivotTableName", type=StringType)
persistence_Association_targetFeatureName: Property = Property(name="targetFeatureName", type=StringType)
persistence_Association_targetPrimaryKey: Property = Property(name="targetPrimaryKey", type=BooleanType)
persistence_Association_targetColumnName: Property = Property(name="targetColumnName", type=StringType)
persistence_Association_targetDisplayLabel: Property = Property(name="targetDisplayLabel", type=StringType)
persistence_Association.attributes={persistence_Association_targetFeatureName, persistence_Association_targetDisplayLabel, persistence_Association_targetColumnName, persistence_Association_inputElementClass, persistence_Association_unique, persistence_Association_pseudo, persistence_Association_targetFooterClass, persistence_Association_targetHeaderClass, persistence_Association_targetInputClass, persistence_Association_pivotTableName, persistence_Association_serializationMaxDepth, persistence_Association_targetDisplayClass, persistence_Association_inputColumnClass, persistence_Association_bidirectional, persistence_Association_targetPrimaryKey}

# persistence_AssociationKey class attributes and methods

# Classifier class attributes and methods

# persistence_ModelLabelFeature class attributes and methods

# persistence_ModelLabelAttribute class attributes and methods
persistence_ModelLabelAttribute_dateFormat: Property = Property(name="dateFormat", type=StringType)
persistence_ModelLabelAttribute.attributes={persistence_ModelLabelAttribute_dateFormat}

# ModelLabelFeature class attributes and methods

# persistence_ModelLabelAssociation class attributes and methods
persistence_ModelLabelAssociation_isSourceAssociation: Property = Property(name="isSourceAssociation", type=BooleanType)
persistence_ModelLabelAssociation.attributes={persistence_ModelLabelAssociation_isSourceAssociation}

# persistence_PathElement class attributes and methods

# persistence_StaticPathElement class attributes and methods
persistence_StaticPathElement_element: Property = Property(name="element", type=StringType)
persistence_StaticPathElement.attributes={persistence_StaticPathElement_element}

# PathElement class attributes and methods

# persistence_DatePathElement class attributes and methods
persistence_DatePathElement_format: Property = Property(name="format", type=StringType)
persistence_DatePathElement.attributes={persistence_DatePathElement_format}

# persistence_FileAttribute class attributes and methods

# ResourceAttribute class attributes and methods

# persistence_ImageAttribute class attributes and methods

# persistence_DataTypeAttribute class attributes and methods
persistence_DataTypeAttribute_obfuscateFormFields: Property = Property(name="obfuscateFormFields", type=BooleanType)
persistence_DataTypeAttribute_caseInsensitive: Property = Property(name="caseInsensitive", type=BooleanType)
persistence_DataTypeAttribute_encrypt: Property = Property(name="encrypt", type=BooleanType)
persistence_DataTypeAttribute.attributes={persistence_DataTypeAttribute_obfuscateFormFields, persistence_DataTypeAttribute_caseInsensitive, persistence_DataTypeAttribute_encrypt}

# Attribute class attributes and methods

# persistence_DateAttribute class attributes and methods
persistence_DateAttribute_details: Property = Property(name="details", type=StringType)
persistence_DateAttribute_format: Property = Property(name="format", type=StringType)
persistence_DateAttribute.attributes={persistence_DateAttribute_details, persistence_DateAttribute_format}

# persistence_UrlAttribute class attributes and methods
persistence_UrlAttribute_displayValue: Property = Property(name="displayValue", type=StringType)
persistence_UrlAttribute.attributes={persistence_UrlAttribute_displayValue}

# persistence_ResourceAttribute class attributes and methods
persistence_ResourceAttribute_maximumUploadSize: Property = Property(name="maximumUploadSize", type=IntegerType)
persistence_ResourceAttribute_validUploadMimeTypes: Property = Property(name="validUploadMimeTypes", type=StringType)
persistence_ResourceAttribute_validUploadExtensions: Property = Property(name="validUploadExtensions", type=StringType)
persistence_ResourceAttribute_uploadsWithinWebsite: Property = Property(name="uploadsWithinWebsite", type=BooleanType)
persistence_ResourceAttribute.attributes={persistence_ResourceAttribute_validUploadExtensions, persistence_ResourceAttribute_validUploadMimeTypes, persistence_ResourceAttribute_uploadsWithinWebsite, persistence_ResourceAttribute_maximumUploadSize}

# persistence_LocationAttribute class attributes and methods

# persistence_AssociationWithoutContainment class attributes and methods
persistence_AssociationWithoutContainment_targetCardinality: Property = Property(name="targetCardinality", type=StringType)
persistence_AssociationWithoutContainment_targetUnique: Property = Property(name="targetUnique", type=BooleanType)
persistence_AssociationWithoutContainment.attributes={persistence_AssociationWithoutContainment_targetUnique, persistence_AssociationWithoutContainment_targetCardinality}

# Association class attributes and methods

# persistence_AssociationWithContainment class attributes and methods
persistence_AssociationWithContainment_sourceVisible: Property = Property(name="sourceVisible", type=BooleanType)
persistence_AssociationWithContainment.attributes={persistence_AssociationWithContainment_sourceVisible}

# Relationships
serializationGroups0: BinaryAssociation = BinaryAssociation(
    name="serializationGroups0",
    ends={
        Property(name="persistence_SerializationGroup", type=persistence_Persistence, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Persistence", type=persistence_SerializationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes1: BinaryAssociation = BinaryAssociation(
    name="dataTypes1",
    ends={
        Property(name="persistence_DataType", type=persistence_Persistence, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Persistence2", type=persistence_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities3: BinaryAssociation = BinaryAssociation(
    name="entities3",
    ends={
        Property(name="persistence_Entity", type=persistence_Persistence, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Persistence4", type=persistence_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partOf5: BinaryAssociation = BinaryAssociation(
    name="partOf5",
    ends={
        Property(name="Entity", type=persistence_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=persistence_Entity, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue10: BinaryAssociation = BinaryAssociation(
    name="defaultValue10",
    ends={
        Property(name="persistence_Expression", type=persistence_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Attribute11", type=persistence_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serializationGroups6: BinaryAssociation = BinaryAssociation(
    name="serializationGroups6",
    ends={
        Property(name="persistence_SerializationGroup7", type=persistence_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Feature", type=persistence_SerializationGroup, multiplicity=Multiplicity(0, 9999))
    }
)
slugFields9: BinaryAssociation = BinaryAssociation(
    name="slugFields9",
    ends={
        Property(name="persistence_Attribute", type=persistence_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Attribute8", type=persistence_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
keys12: BinaryAssociation = BinaryAssociation(
    name="keys12",
    ends={
        Property(name="AssociationKey", type=persistence_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="keyFor", type=persistence_AssociationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetEntity13: BinaryAssociation = BinaryAssociation(
    name="targetEntity13",
    ends={
        Property(name="Entity14", type=persistence_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnds", type=persistence_Entity, multiplicity=Multiplicity(1, 1))
    }
)
dynamicLabel25: BinaryAssociation = BinaryAssociation(
    name="dynamicLabel25",
    ends={
        Property(name="persistence_ModelLabel27", type=persistence_ModelLabelAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ModelLabelAssociation26", type=persistence_ModelLabel, multiplicity=Multiplicity(0, 1))
    }
)
labelFor15: BinaryAssociation = BinaryAssociation(
    name="labelFor15",
    ends={
        Property(name="Entity16", type=persistence_ModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=persistence_Entity, multiplicity=Multiplicity(1, 1))
    }
)
features17: BinaryAssociation = BinaryAssociation(
    name="features17",
    ends={
        Property(name="ModelLabelFeature", type=persistence_ModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf", type=persistence_ModelLabelFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serializationGroups18: BinaryAssociation = BinaryAssociation(
    name="serializationGroups18",
    ends={
        Property(name="persistence_SerializationGroup19", type=persistence_ModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ModelLabel", type=persistence_SerializationGroup, multiplicity=Multiplicity(0, 9999))
    }
)
partOf20: BinaryAssociation = BinaryAssociation(
    name="partOf20",
    ends={
        Property(name="ModelLabel", type=persistence_ModelLabelFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="features21", type=persistence_ModelLabel, multiplicity=Multiplicity(1, 1))
    }
)
attribute22: BinaryAssociation = BinaryAssociation(
    name="attribute22",
    ends={
        Property(name="persistence_Attribute23", type=persistence_ModelLabelAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ModelLabelAttribute", type=persistence_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
association24: BinaryAssociation = BinaryAssociation(
    name="association24",
    ends={
        Property(name="persistence_Association", type=persistence_ModelLabelAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ModelLabelAssociation", type=persistence_Association, multiplicity=Multiplicity(1, 1))
    }
)
keys43: BinaryAssociation = BinaryAssociation(
    name="keys43",
    ends={
        Property(name="persistence_Feature45", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Entity44", type=persistence_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
labels46: BinaryAssociation = BinaryAssociation(
    name="labels46",
    ends={
        Property(name="ModelLabel47", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="labelFor", type=persistence_ModelLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unique48: BinaryAssociation = BinaryAssociation(
    name="unique48",
    ends={
        Property(name="persistence_Feature50", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Entity49", type=persistence_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
containerUnique51: BinaryAssociation = BinaryAssociation(
    name="containerUnique51",
    ends={
        Property(name="persistence_Feature53", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Entity52", type=persistence_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
features28: BinaryAssociation = BinaryAssociation(
    name="features28",
    ends={
        Property(name="Feature", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf29", type=persistence_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes30: BinaryAssociation = BinaryAssociation(
    name="attributes30",
    ends={
        Property(name="persistence_Attribute32", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Entity31", type=persistence_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
associations33: BinaryAssociation = BinaryAssociation(
    name="associations33",
    ends={
        Property(name="persistence_Association35", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Entity34", type=persistence_Association, multiplicity=Multiplicity(0, 9999))
    }
)
associationEnds36: BinaryAssociation = BinaryAssociation(
    name="associationEnds36",
    ends={
        Property(name="Association", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="targetEntity", type=persistence_Association, multiplicity=Multiplicity(0, 9999))
    }
)
allFeatures37: BinaryAssociation = BinaryAssociation(
    name="allFeatures37",
    ends={
        Property(name="persistence_Feature39", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Entity38", type=persistence_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
allAssociations40: BinaryAssociation = BinaryAssociation(
    name="allAssociations40",
    ends={
        Property(name="persistence_Association42", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Entity41", type=persistence_Association, multiplicity=Multiplicity(0, 9999))
    }
)
uploadPath56: BinaryAssociation = BinaryAssociation(
    name="uploadPath56",
    ends={
        Property(name="persistence_PathElement", type=persistence_ResourceAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ResourceAttribute", type=persistence_PathElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType54: BinaryAssociation = BinaryAssociation(
    name="dataType54",
    ends={
        Property(name="persistence_DataType55", type=persistence_DataTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_DataTypeAttribute", type=persistence_DataType, multiplicity=Multiplicity(1, 1))
    }
)
keyFor57: BinaryAssociation = BinaryAssociation(
    name="keyFor57",
    ends={
        Property(name="Association58", type=persistence_AssociationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="keys", type=persistence_Association, multiplicity=Multiplicity(1, 1))
    }
)
sourceFeature59: BinaryAssociation = BinaryAssociation(
    name="sourceFeature59",
    ends={
        Property(name="persistence_Feature60", type=persistence_AssociationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_AssociationKey", type=persistence_Feature, multiplicity=Multiplicity(1, 1))
    }
)
targetFeature61: BinaryAssociation = BinaryAssociation(
    name="targetFeature61",
    ends={
        Property(name="persistence_Feature63", type=persistence_AssociationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_AssociationKey62", type=persistence_Feature, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_persistence_SerializationGroup_NamedElement = Generalization(general=NamedElement, specific=persistence_SerializationGroup)
gen_persistence_Feature_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=persistence_Feature)
gen_persistence_Attribute_Feature = Generalization(general=Feature, specific=persistence_Attribute)
gen_persistence_Attribute_Label = Generalization(general=Label, specific=persistence_Attribute)
gen_persistence_ModelLabel_NamedElement = Generalization(general=NamedElement, specific=persistence_ModelLabel)
gen_persistence_ModelLabel_Label = Generalization(general=Label, specific=persistence_ModelLabel)
gen_persistence_Association_Feature = Generalization(general=Feature, specific=persistence_Association)
gen_persistence_Entity_Classifier = Generalization(general=Classifier, specific=persistence_Entity)
gen_persistence_ModelLabelAttribute_ModelLabelFeature = Generalization(general=ModelLabelFeature, specific=persistence_ModelLabelAttribute)
gen_persistence_ModelLabelAssociation_ModelLabelFeature = Generalization(general=ModelLabelFeature, specific=persistence_ModelLabelAssociation)
gen_persistence_StaticPathElement_PathElement = Generalization(general=PathElement, specific=persistence_StaticPathElement)
gen_persistence_DatePathElement_PathElement = Generalization(general=PathElement, specific=persistence_DatePathElement)
gen_persistence_FileAttribute_ResourceAttribute = Generalization(general=ResourceAttribute, specific=persistence_FileAttribute)
gen_persistence_ImageAttribute_ResourceAttribute = Generalization(general=ResourceAttribute, specific=persistence_ImageAttribute)
gen_persistence_DataTypeAttribute_Attribute = Generalization(general=Attribute, specific=persistence_DataTypeAttribute)
gen_persistence_DateAttribute_Attribute = Generalization(general=Attribute, specific=persistence_DateAttribute)
gen_persistence_UrlAttribute_Attribute = Generalization(general=Attribute, specific=persistence_UrlAttribute)
gen_persistence_ResourceAttribute_Attribute = Generalization(general=Attribute, specific=persistence_ResourceAttribute)
gen_persistence_LocationAttribute_Attribute = Generalization(general=Attribute, specific=persistence_LocationAttribute)
gen_persistence_AssociationWithoutContainment_Association = Generalization(general=Association, specific=persistence_AssociationWithoutContainment)
gen_persistence_AssociationWithContainment_Association = Generalization(general=Association, specific=persistence_AssociationWithContainment)

# Domain Model
domain_model = DomainModel(
    name="persistence",
    types={persistence_Persistence, NamedElement, persistence_SerializationGroup, persistence_DataType, persistence_Entity, persistence_Feature, NamedDisplayElement, persistence_Expression, persistence_Attribute, Feature, Label, persistence_Label, persistence_ModelLabel, persistence_Association, persistence_AssociationKey, Classifier, persistence_ModelLabelFeature, persistence_ModelLabelAttribute, ModelLabelFeature, persistence_ModelLabelAssociation, persistence_PathElement, persistence_StaticPathElement, PathElement, persistence_DatePathElement, persistence_FileAttribute, ResourceAttribute, persistence_ImageAttribute, persistence_DataTypeAttribute, Attribute, persistence_DateAttribute, persistence_UrlAttribute, persistence_ResourceAttribute, persistence_LocationAttribute, persistence_AssociationWithoutContainment, Association, persistence_AssociationWithContainment, Cardinality, DatabaseTechnologies, OrmTechnologies, isHasChoices, DateDetails},
    associations={serializationGroups0, dataTypes1, entities3, partOf5, defaultValue10, serializationGroups6, slugFields9, keys12, targetEntity13, dynamicLabel25, labelFor15, features17, serializationGroups18, partOf20, attribute22, association24, keys43, labels46, unique48, containerUnique51, features28, attributes30, associations33, associationEnds36, allFeatures37, allAssociations40, uploadPath56, dataType54, keyFor57, sourceFeature59, targetFeature61},
    generalizations={gen_persistence_SerializationGroup_NamedElement, gen_persistence_Feature_NamedDisplayElement, gen_persistence_Attribute_Feature, gen_persistence_Attribute_Label, gen_persistence_ModelLabel_NamedElement, gen_persistence_ModelLabel_Label, gen_persistence_Association_Feature, gen_persistence_Entity_Classifier, gen_persistence_ModelLabelAttribute_ModelLabelFeature, gen_persistence_ModelLabelAssociation_ModelLabelFeature, gen_persistence_StaticPathElement_PathElement, gen_persistence_DatePathElement_PathElement, gen_persistence_FileAttribute_ResourceAttribute, gen_persistence_ImageAttribute_ResourceAttribute, gen_persistence_DataTypeAttribute_Attribute, gen_persistence_DateAttribute_Attribute, gen_persistence_UrlAttribute_Attribute, gen_persistence_ResourceAttribute_Attribute, gen_persistence_LocationAttribute_Attribute, gen_persistence_AssociationWithoutContainment_Association, gen_persistence_AssociationWithContainment_Association},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)