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
            EnumerationLiteral(name="JPA"),
			EnumerationLiteral(name="DataMapper"),
			EnumerationLiteral(name="Idiorm"),
			EnumerationLiteral(name="Kohana"),
			EnumerationLiteral(name="DoctrineORM"),
			EnumerationLiteral(name="DoctrineODM")
    }
)

Cardinality: Enumeration = Enumeration(
    name="Cardinality",
    literals={
            EnumerationLiteral(name="Optional"),
			EnumerationLiteral(name="Required"),
			EnumerationLiteral(name="Many")
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
persistence_EntityOrView = Class(name="persistence::EntityOrView", is_abstract=True)
persistence_SerializationGroup = Class(name="persistence::SerializationGroup")
persistence_DataType = Class(name="persistence::DataType")
persistence_Feature = Class(name="persistence::Feature", is_abstract=True)
persistence_ModelLabel = Class(name="persistence::ModelLabel")
NamedElement = Class(name="NamedElement")
Classifier = Class(name="Classifier")
persistence_Attribute = Class(name="persistence::Attribute", is_abstract=True)
persistence_Association = Class(name="persistence::Association", is_abstract=True)
Feature = Class(name="Feature")
Label = Class(name="Label")
persistence_Expression = Class(name="persistence::Expression")
persistence_EncapsulatedAssociation = Class(name="persistence::EncapsulatedAssociation")
persistence_ModelLabelFeature = Class(name="persistence::ModelLabelFeature", is_abstract=True)
persistence_ModelLabelAttribute = Class(name="persistence::ModelLabelAttribute")
ModelLabelFeature = Class(name="ModelLabelFeature")
persistence_ModelLabelAssociation = Class(name="persistence::ModelLabelAssociation")
persistence_Label = Class(name="persistence::Label", is_abstract=True)
persistence_Entity = Class(name="persistence::Entity")
EntityOrView = Class(name="EntityOrView")
persistence_EntityFeature = Class(name="persistence::EntityFeature", is_abstract=True)
NamedDisplayElement = Class(name="NamedDisplayElement")
persistence_EntityAssociation = Class(name="persistence::EntityAssociation", is_abstract=True)
persistence_EntityAttribute = Class(name="persistence::EntityAttribute", is_abstract=True)
EntityFeature = Class(name="EntityFeature")
Attribute = Class(name="Attribute")
persistence_DataTypeAttribute = Class(name="persistence::DataTypeAttribute")
EntityAttribute = Class(name="EntityAttribute")
persistence_UrlAttribute = Class(name="persistence::UrlAttribute")
persistence_ResourceAttribute = Class(name="persistence::ResourceAttribute", is_abstract=True)
persistence_PathElement = Class(name="persistence::PathElement", is_abstract=True)
persistence_StaticPathElement = Class(name="persistence::StaticPathElement")
PathElement = Class(name="PathElement")
persistence_DatePathElement = Class(name="persistence::DatePathElement")
persistence_FileAttribute = Class(name="persistence::FileAttribute")
ResourceAttribute = Class(name="ResourceAttribute")
persistence_DateAttribute = Class(name="persistence::DateAttribute")
persistence_AssociationKey = Class(name="persistence::AssociationKey")
persistence_AssociationWithoutContainment = Class(name="persistence::AssociationWithoutContainment")
EntityAssociation = Class(name="EntityAssociation")
persistence_ImageAttribute = Class(name="persistence::ImageAttribute")
persistence_LocationAttribute = Class(name="persistence::LocationAttribute")
Association = Class(name="Association")
persistence_View = Class(name="persistence::View")
persistence_ViewFeature = Class(name="persistence::ViewFeature", is_abstract=True)
persistence_EncapsulatedFeature = Class(name="persistence::EncapsulatedFeature")
ViewFeature = Class(name="ViewFeature")
persistence_AssociationWithContainment = Class(name="persistence::AssociationWithContainment")
persistence_EncapsulatedAttribute = Class(name="persistence::EncapsulatedAttribute")
EncapsulatedFeature = Class(name="EncapsulatedFeature")
persistence_ViewAssociation = Class(name="persistence::ViewAssociation")

# persistence_Persistence class attributes and methods
persistence_Persistence_ormTechnology: Property = Property(name="ormTechnology", type=StringType)
persistence_Persistence_databaseTechnology: Property = Property(name="databaseTechnology", type=StringType)
persistence_Persistence_databasePrefix: Property = Property(name="databasePrefix", type=StringType)
persistence_Persistence_databaseHost: Property = Property(name="databaseHost", type=StringType)
persistence_Persistence_databaseName: Property = Property(name="databaseName", type=StringType)
persistence_Persistence_databasePort: Property = Property(name="databasePort", type=StringType)
persistence_Persistence_databaseUsername: Property = Property(name="databaseUsername", type=StringType)
persistence_Persistence_databasePassword: Property = Property(name="databasePassword", type=StringType)
persistence_Persistence_timestampCreation: Property = Property(name="timestampCreation", type=BooleanType)
persistence_Persistence_timestampUpdates: Property = Property(name="timestampUpdates", type=BooleanType)
persistence_Persistence.attributes={persistence_Persistence_ormTechnology, persistence_Persistence_databasePort, persistence_Persistence_databaseUsername, persistence_Persistence_databaseTechnology, persistence_Persistence_timestampCreation, persistence_Persistence_databasePrefix, persistence_Persistence_databaseHost, persistence_Persistence_databaseName, persistence_Persistence_databasePassword, persistence_Persistence_timestampUpdates}

# persistence_EntityOrView class attributes and methods
persistence_EntityOrView_singletonName: Property = Property(name="singletonName", type=StringType)
persistence_EntityOrView_pluralisedName: Property = Property(name="pluralisedName", type=StringType)
persistence_EntityOrView_tableName: Property = Property(name="tableName", type=StringType)
persistence_EntityOrView_autoKeyName: Property = Property(name="autoKeyName", type=StringType)
persistence_EntityOrView_autoKeyPersistentType: Property = Property(name="autoKeyPersistentType", type=StringType)
persistence_EntityOrView_autoKeyGenerationStrategy: Property = Property(name="autoKeyGenerationStrategy", type=StringType)
persistence_EntityOrView_implementsUserInterface: Property = Property(name="implementsUserInterface", type=BooleanType)
persistence_EntityOrView.attributes={persistence_EntityOrView_autoKeyPersistentType, persistence_EntityOrView_autoKeyGenerationStrategy, persistence_EntityOrView_pluralisedName, persistence_EntityOrView_singletonName, persistence_EntityOrView_implementsUserInterface, persistence_EntityOrView_tableName, persistence_EntityOrView_autoKeyName}

# persistence_SerializationGroup class attributes and methods

# persistence_DataType class attributes and methods

# persistence_Feature class attributes and methods
persistence_Feature_title: Property = Property(name="title", type=StringType)
persistence_Feature_collectionAllowAdd: Property = Property(name="collectionAllowAdd", type=BooleanType)
persistence_Feature_collectionAllowRemove: Property = Property(name="collectionAllowRemove", type=BooleanType)
persistence_Feature_nullDisplayValue: Property = Property(name="nullDisplayValue", type=StringType)
persistence_Feature_footerClass: Property = Property(name="footerClass", type=StringType)
persistence_Feature_encodeUriKey: Property = Property(name="encodeUriKey", type=BooleanType)
persistence_Feature_headerClass: Property = Property(name="headerClass", type=StringType)
persistence_Feature_displayClass: Property = Property(name="displayClass", type=StringType)
persistence_Feature.attributes={persistence_Feature_title, persistence_Feature_collectionAllowAdd, persistence_Feature_encodeUriKey, persistence_Feature_headerClass, persistence_Feature_displayClass, persistence_Feature_nullDisplayValue, persistence_Feature_footerClass, persistence_Feature_collectionAllowRemove}

# persistence_ModelLabel class attributes and methods
persistence_ModelLabel_format: Property = Property(name="format", type=StringType)
persistence_ModelLabel.attributes={persistence_ModelLabel_format}

# NamedElement class attributes and methods

# Classifier class attributes and methods

# persistence_Attribute class attributes and methods
persistence_Attribute_placeholder: Property = Property(name="placeholder", type=StringType)
persistence_Attribute_validationPattern: Property = Property(name="validationPattern", type=StringType)
persistence_Attribute_inputClass: Property = Property(name="inputClass", type=StringType)
persistence_Attribute.attributes={persistence_Attribute_placeholder, persistence_Attribute_inputClass, persistence_Attribute_validationPattern}

# persistence_Association class attributes and methods
persistence_Association_pseudo: Property = Property(name="pseudo", type=BooleanType)
persistence_Association_inputClass: Property = Property(name="inputClass", type=StringType)
persistence_Association_serializationMaxDepth: Property = Property(name="serializationMaxDepth", type=IntegerType)
persistence_Association.attributes={persistence_Association_inputClass, persistence_Association_pseudo, persistence_Association_serializationMaxDepth}

# Feature class attributes and methods

# Label class attributes and methods

# persistence_Expression class attributes and methods

# persistence_EncapsulatedAssociation class attributes and methods
persistence_EncapsulatedAssociation_name: Property = Property(name="name", type=StringType)
persistence_EncapsulatedAssociation_isSourceAssociation: Property = Property(name="isSourceAssociation", type=BooleanType)
persistence_EncapsulatedAssociation_cardinality: Property = Property(name="cardinality", type=StringType)
persistence_EncapsulatedAssociation.attributes={persistence_EncapsulatedAssociation_name, persistence_EncapsulatedAssociation_cardinality, persistence_EncapsulatedAssociation_isSourceAssociation}

# persistence_ModelLabelFeature class attributes and methods

# persistence_ModelLabelAttribute class attributes and methods
persistence_ModelLabelAttribute_dateFormat: Property = Property(name="dateFormat", type=StringType)
persistence_ModelLabelAttribute.attributes={persistence_ModelLabelAttribute_dateFormat}

# ModelLabelFeature class attributes and methods

# persistence_ModelLabelAssociation class attributes and methods
persistence_ModelLabelAssociation_isSourceAssociation: Property = Property(name="isSourceAssociation", type=BooleanType)
persistence_ModelLabelAssociation.attributes={persistence_ModelLabelAssociation_isSourceAssociation}

# persistence_Label class attributes and methods

# persistence_Entity class attributes and methods

# EntityOrView class attributes and methods

# persistence_EntityFeature class attributes and methods
persistence_EntityFeature_cardinality: Property = Property(name="cardinality", type=StringType)
persistence_EntityFeature_singletonName: Property = Property(name="singletonName", type=StringType)
persistence_EntityFeature_pluralisedName: Property = Property(name="pluralisedName", type=StringType)
persistence_EntityFeature_columnName: Property = Property(name="columnName", type=StringType)
persistence_EntityFeature_unique: Property = Property(name="unique", type=BooleanType)
persistence_EntityFeature_ordered: Property = Property(name="ordered", type=BooleanType)
persistence_EntityFeature_booleanIsHasChoice: Property = Property(name="booleanIsHasChoice", type=StringType)
persistence_EntityFeature.attributes={persistence_EntityFeature_columnName, persistence_EntityFeature_cardinality, persistence_EntityFeature_singletonName, persistence_EntityFeature_booleanIsHasChoice, persistence_EntityFeature_pluralisedName, persistence_EntityFeature_unique, persistence_EntityFeature_ordered}

# NamedDisplayElement class attributes and methods

# persistence_EntityAssociation class attributes and methods
persistence_EntityAssociation_bidirectional: Property = Property(name="bidirectional", type=BooleanType)
persistence_EntityAssociation_pivotTableName: Property = Property(name="pivotTableName", type=StringType)
persistence_EntityAssociation_targetFeatureName: Property = Property(name="targetFeatureName", type=StringType)
persistence_EntityAssociation_targetPrimaryKey: Property = Property(name="targetPrimaryKey", type=BooleanType)
persistence_EntityAssociation_targetDisplayLabel: Property = Property(name="targetDisplayLabel", type=StringType)
persistence_EntityAssociation_targetHeaderClass: Property = Property(name="targetHeaderClass", type=StringType)
persistence_EntityAssociation_targetInputClass: Property = Property(name="targetInputClass", type=StringType)
persistence_EntityAssociation_targetDisplayClass: Property = Property(name="targetDisplayClass", type=StringType)
persistence_EntityAssociation_targetFooterClass: Property = Property(name="targetFooterClass", type=StringType)
persistence_EntityAssociation.attributes={persistence_EntityAssociation_pivotTableName, persistence_EntityAssociation_targetDisplayLabel, persistence_EntityAssociation_targetFooterClass, persistence_EntityAssociation_targetInputClass, persistence_EntityAssociation_targetHeaderClass, persistence_EntityAssociation_targetDisplayClass, persistence_EntityAssociation_targetPrimaryKey, persistence_EntityAssociation_targetFeatureName, persistence_EntityAssociation_bidirectional}

# persistence_EntityAttribute class attributes and methods
persistence_EntityAttribute_primaryKey: Property = Property(name="primaryKey", type=BooleanType)
persistence_EntityAttribute_containerUnique: Property = Property(name="containerUnique", type=BooleanType)
persistence_EntityAttribute_persistentType: Property = Property(name="persistentType", type=StringType)
persistence_EntityAttribute_ormType: Property = Property(name="ormType", type=StringType)
persistence_EntityAttribute_interfaceType: Property = Property(name="interfaceType", type=StringType)
persistence_EntityAttribute.attributes={persistence_EntityAttribute_ormType, persistence_EntityAttribute_primaryKey, persistence_EntityAttribute_containerUnique, persistence_EntityAttribute_persistentType, persistence_EntityAttribute_interfaceType}

# EntityFeature class attributes and methods

# Attribute class attributes and methods

# persistence_DataTypeAttribute class attributes and methods
persistence_DataTypeAttribute_obfuscateFormFields: Property = Property(name="obfuscateFormFields", type=BooleanType)
persistence_DataTypeAttribute_caseInsensitive: Property = Property(name="caseInsensitive", type=BooleanType)
persistence_DataTypeAttribute_encrypt: Property = Property(name="encrypt", type=BooleanType)
persistence_DataTypeAttribute.attributes={persistence_DataTypeAttribute_caseInsensitive, persistence_DataTypeAttribute_obfuscateFormFields, persistence_DataTypeAttribute_encrypt}

# EntityAttribute class attributes and methods

# persistence_UrlAttribute class attributes and methods
persistence_UrlAttribute_displayValue: Property = Property(name="displayValue", type=StringType)
persistence_UrlAttribute.attributes={persistence_UrlAttribute_displayValue}

# persistence_ResourceAttribute class attributes and methods
persistence_ResourceAttribute_maximumUploadSize: Property = Property(name="maximumUploadSize", type=IntegerType)
persistence_ResourceAttribute_validUploadMimeTypes: Property = Property(name="validUploadMimeTypes", type=StringType)
persistence_ResourceAttribute_validUploadExtensions: Property = Property(name="validUploadExtensions", type=StringType)
persistence_ResourceAttribute_uploadsWithinWebsite: Property = Property(name="uploadsWithinWebsite", type=BooleanType)
persistence_ResourceAttribute.attributes={persistence_ResourceAttribute_validUploadExtensions, persistence_ResourceAttribute_validUploadMimeTypes, persistence_ResourceAttribute_uploadsWithinWebsite, persistence_ResourceAttribute_maximumUploadSize}

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

# persistence_DateAttribute class attributes and methods
persistence_DateAttribute_format: Property = Property(name="format", type=StringType)
persistence_DateAttribute_details: Property = Property(name="details", type=StringType)
persistence_DateAttribute.attributes={persistence_DateAttribute_details, persistence_DateAttribute_format}

# persistence_AssociationKey class attributes and methods
persistence_AssociationKey_targetColumnName: Property = Property(name="targetColumnName", type=StringType)
persistence_AssociationKey.attributes={persistence_AssociationKey_targetColumnName}

# persistence_AssociationWithoutContainment class attributes and methods
persistence_AssociationWithoutContainment_targetCardinality: Property = Property(name="targetCardinality", type=StringType)
persistence_AssociationWithoutContainment_targetUnique: Property = Property(name="targetUnique", type=BooleanType)
persistence_AssociationWithoutContainment.attributes={persistence_AssociationWithoutContainment_targetUnique, persistence_AssociationWithoutContainment_targetCardinality}

# EntityAssociation class attributes and methods

# persistence_ImageAttribute class attributes and methods

# persistence_LocationAttribute class attributes and methods

# Association class attributes and methods

# persistence_View class attributes and methods

# persistence_ViewFeature class attributes and methods

# persistence_EncapsulatedFeature class attributes and methods
persistence_EncapsulatedFeature_displayLabel: Property = Property(name="displayLabel", type=StringType)
persistence_EncapsulatedFeature_alias: Property = Property(name="alias", type=StringType)
persistence_EncapsulatedFeature_columnName: Property = Property(name="columnName", type=StringType)
persistence_EncapsulatedFeature.attributes={persistence_EncapsulatedFeature_columnName, persistence_EncapsulatedFeature_displayLabel, persistence_EncapsulatedFeature_alias}

# ViewFeature class attributes and methods

# persistence_AssociationWithContainment class attributes and methods
persistence_AssociationWithContainment_sourceVisible: Property = Property(name="sourceVisible", type=BooleanType)
persistence_AssociationWithContainment.attributes={persistence_AssociationWithContainment_sourceVisible}

# persistence_EncapsulatedAttribute class attributes and methods
persistence_EncapsulatedAttribute_name: Property = Property(name="name", type=StringType)
persistence_EncapsulatedAttribute_cardinality: Property = Property(name="cardinality", type=StringType)
persistence_EncapsulatedAttribute.attributes={persistence_EncapsulatedAttribute_name, persistence_EncapsulatedAttribute_cardinality}

# EncapsulatedFeature class attributes and methods

# persistence_ViewAssociation class attributes and methods
persistence_ViewAssociation_cardinality: Property = Property(name="cardinality", type=StringType)
persistence_ViewAssociation.attributes={persistence_ViewAssociation_cardinality}

# Relationships
dataTypes1: BinaryAssociation = BinaryAssociation(
    name="dataTypes1",
    ends={
        Property(name="persistence_Persistence2", type=persistence_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="persistence_DataType", type=persistence_Persistence, multiplicity=Multiplicity(1, 1))
    }
)
entities3: BinaryAssociation = BinaryAssociation(
    name="entities3",
    ends={
        Property(name="persistence_EntityOrView", type=persistence_Persistence, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Persistence4", type=persistence_EntityOrView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serializationGroups0: BinaryAssociation = BinaryAssociation(
    name="serializationGroups0",
    ends={
        Property(name="persistence_SerializationGroup", type=persistence_Persistence, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Persistence", type=persistence_SerializationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys5: BinaryAssociation = BinaryAssociation(
    name="keys5",
    ends={
        Property(name="persistence_Feature", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EntityOrView6", type=persistence_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
unique7: BinaryAssociation = BinaryAssociation(
    name="unique7",
    ends={
        Property(name="persistence_Feature9", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EntityOrView8", type=persistence_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
containerUnique10: BinaryAssociation = BinaryAssociation(
    name="containerUnique10",
    ends={
        Property(name="persistence_Feature12", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EntityOrView11", type=persistence_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
labels13: BinaryAssociation = BinaryAssociation(
    name="labels13",
    ends={
        Property(name="ModelLabel", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="labelFor", type=persistence_ModelLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features14: BinaryAssociation = BinaryAssociation(
    name="features14",
    ends={
        Property(name="persistence_Feature16", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EntityOrView15", type=persistence_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
attributes20: BinaryAssociation = BinaryAssociation(
    name="attributes20",
    ends={
        Property(name="persistence_Attribute", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EntityOrView21", type=persistence_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
associations22: BinaryAssociation = BinaryAssociation(
    name="associations22",
    ends={
        Property(name="persistence_Association", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EntityOrView23", type=persistence_Association, multiplicity=Multiplicity(0, 9999))
    }
)
allAssociations24: BinaryAssociation = BinaryAssociation(
    name="allAssociations24",
    ends={
        Property(name="persistence_Association26", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EntityOrView25", type=persistence_Association, multiplicity=Multiplicity(0, 9999))
    }
)
allFeatures17: BinaryAssociation = BinaryAssociation(
    name="allFeatures17",
    ends={
        Property(name="persistence_Feature19", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EntityOrView18", type=persistence_Feature, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue30: BinaryAssociation = BinaryAssociation(
    name="defaultValue30",
    ends={
        Property(name="persistence_Expression", type=persistence_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Attribute31", type=persistence_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
encapsulatedBy32: BinaryAssociation = BinaryAssociation(
    name="encapsulatedBy32",
    ends={
        Property(name="EncapsulatedAssociation", type=persistence_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=persistence_EncapsulatedAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
sourceEntityX33: BinaryAssociation = BinaryAssociation(
    name="sourceEntityX33",
    ends={
        Property(name="persistence_EntityOrView35", type=persistence_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Association34", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
serializationGroups27: BinaryAssociation = BinaryAssociation(
    name="serializationGroups27",
    ends={
        Property(name="persistence_SerializationGroup29", type=persistence_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Feature28", type=persistence_SerializationGroup, multiplicity=Multiplicity(0, 9999))
    }
)
labelFor39: BinaryAssociation = BinaryAssociation(
    name="labelFor39",
    ends={
        Property(name="EntityOrView", type=persistence_ModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
features40: BinaryAssociation = BinaryAssociation(
    name="features40",
    ends={
        Property(name="ModelLabelFeature", type=persistence_ModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf", type=persistence_ModelLabelFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serializationGroups41: BinaryAssociation = BinaryAssociation(
    name="serializationGroups41",
    ends={
        Property(name="persistence_SerializationGroup42", type=persistence_ModelLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ModelLabel", type=persistence_SerializationGroup, multiplicity=Multiplicity(0, 9999))
    }
)
partOf43: BinaryAssociation = BinaryAssociation(
    name="partOf43",
    ends={
        Property(name="ModelLabel44", type=persistence_ModelLabelFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=persistence_ModelLabel, multiplicity=Multiplicity(1, 1))
    }
)
attribute45: BinaryAssociation = BinaryAssociation(
    name="attribute45",
    ends={
        Property(name="persistence_Attribute46", type=persistence_ModelLabelAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ModelLabelAttribute", type=persistence_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
targetEntityX36: BinaryAssociation = BinaryAssociation(
    name="targetEntityX36",
    ends={
        Property(name="persistence_EntityOrView38", type=persistence_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_Association37", type=persistence_EntityOrView, multiplicity=Multiplicity(1, 1))
    }
)
entityFeatures51: BinaryAssociation = BinaryAssociation(
    name="entityFeatures51",
    ends={
        Property(name="EntityFeature", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf52", type=persistence_EntityFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationEnds53: BinaryAssociation = BinaryAssociation(
    name="associationEnds53",
    ends={
        Property(name="EntityAssociation", type=persistence_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="targetEntity", type=persistence_EntityAssociation, multiplicity=Multiplicity(0, 9999))
    }
)
partOf54: BinaryAssociation = BinaryAssociation(
    name="partOf54",
    ends={
        Property(name="Entity", type=persistence_EntityFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="entityFeatures", type=persistence_Entity, multiplicity=Multiplicity(1, 1))
    }
)
association47: BinaryAssociation = BinaryAssociation(
    name="association47",
    ends={
        Property(name="persistence_EntityAssociation", type=persistence_ModelLabelAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ModelLabelAssociation", type=persistence_EntityAssociation, multiplicity=Multiplicity(1, 1))
    }
)
dynamicLabel48: BinaryAssociation = BinaryAssociation(
    name="dynamicLabel48",
    ends={
        Property(name="persistence_ModelLabel50", type=persistence_ModelLabelAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ModelLabelAssociation49", type=persistence_ModelLabel, multiplicity=Multiplicity(0, 1))
    }
)
dataType55: BinaryAssociation = BinaryAssociation(
    name="dataType55",
    ends={
        Property(name="persistence_DataType56", type=persistence_DataTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_DataTypeAttribute", type=persistence_DataType, multiplicity=Multiplicity(1, 1))
    }
)
uploadPath57: BinaryAssociation = BinaryAssociation(
    name="uploadPath57",
    ends={
        Property(name="persistence_PathElement", type=persistence_ResourceAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ResourceAttribute", type=persistence_PathElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys58: BinaryAssociation = BinaryAssociation(
    name="keys58",
    ends={
        Property(name="AssociationKey", type=persistence_EntityAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="keyFor", type=persistence_AssociationKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetEntity59: BinaryAssociation = BinaryAssociation(
    name="targetEntity59",
    ends={
        Property(name="Entity60", type=persistence_EntityAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="associationEnds", type=persistence_Entity, multiplicity=Multiplicity(1, 1))
    }
)
sourceFeature63: BinaryAssociation = BinaryAssociation(
    name="sourceFeature63",
    ends={
        Property(name="persistence_EntityFeature", type=persistence_AssociationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_AssociationKey", type=persistence_EntityFeature, multiplicity=Multiplicity(1, 1))
    }
)
targetFeature64: BinaryAssociation = BinaryAssociation(
    name="targetFeature64",
    ends={
        Property(name="persistence_EntityFeature66", type=persistence_AssociationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_AssociationKey65", type=persistence_EntityFeature, multiplicity=Multiplicity(0, 1))
    }
)
encapsulates67: BinaryAssociation = BinaryAssociation(
    name="encapsulates67",
    ends={
        Property(name="persistence_EntityOrView68", type=persistence_View, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_View", type=persistence_EntityOrView, multiplicity=Multiplicity(0, 9999))
    }
)
viewFeatures69: BinaryAssociation = BinaryAssociation(
    name="viewFeatures69",
    ends={
        Property(name="ViewFeature", type=persistence_View, multiplicity=Multiplicity(1, 1)),
        Property(name="partOf70", type=persistence_ViewFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partOf71: BinaryAssociation = BinaryAssociation(
    name="partOf71",
    ends={
        Property(name="View", type=persistence_ViewFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="viewFeatures", type=persistence_View, multiplicity=Multiplicity(1, 1))
    }
)
keyFor61: BinaryAssociation = BinaryAssociation(
    name="keyFor61",
    ends={
        Property(name="EntityAssociation62", type=persistence_AssociationKey, multiplicity=Multiplicity(1, 1)),
        Property(name="keys", type=persistence_EntityAssociation, multiplicity=Multiplicity(1, 1))
    }
)
attribute72: BinaryAssociation = BinaryAssociation(
    name="attribute72",
    ends={
        Property(name="persistence_Attribute73", type=persistence_EncapsulatedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EncapsulatedAttribute", type=persistence_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
encapsulatedTarget76: BinaryAssociation = BinaryAssociation(
    name="encapsulatedTarget76",
    ends={
        Property(name="persistence_EncapsulatedAssociation75", type=persistence_EncapsulatedAssociation, multiplicity=Multiplicity(0, 1)),
        Property(name="persistence_EncapsulatedAssociation", type=persistence_EncapsulatedAssociation, multiplicity=Multiplicity(1, 1))
    }
)
sourceEntity77: BinaryAssociation = BinaryAssociation(
    name="sourceEntity77",
    ends={
        Property(name="persistence_Entity", type=persistence_EncapsulatedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EncapsulatedAssociation78", type=persistence_Entity, multiplicity=Multiplicity(1, 1))
    }
)
targetEntity79: BinaryAssociation = BinaryAssociation(
    name="targetEntity79",
    ends={
        Property(name="persistence_Entity81", type=persistence_EncapsulatedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_EncapsulatedAssociation80", type=persistence_Entity, multiplicity=Multiplicity(1, 1))
    }
)
association74: BinaryAssociation = BinaryAssociation(
    name="association74",
    ends={
        Property(name="Association", type=persistence_EncapsulatedAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="encapsulatedBy", type=persistence_Association, multiplicity=Multiplicity(1, 1))
    }
)
opposite82: BinaryAssociation = BinaryAssociation(
    name="opposite82",
    ends={
        Property(name="persistence_EncapsulatedAssociation83", type=persistence_ViewAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="persistence_ViewAssociation", type=persistence_EncapsulatedAssociation, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_persistence_SerializationGroup_NamedElement = Generalization(general=NamedElement, specific=persistence_SerializationGroup)
gen_persistence_EntityOrView_Classifier = Generalization(general=Classifier, specific=persistence_EntityOrView)
gen_persistence_Attribute_Feature = Generalization(general=Feature, specific=persistence_Attribute)
gen_persistence_Attribute_Label = Generalization(general=Label, specific=persistence_Attribute)
gen_persistence_Association_Feature = Generalization(general=Feature, specific=persistence_Association)
gen_persistence_ModelLabel_NamedElement = Generalization(general=NamedElement, specific=persistence_ModelLabel)
gen_persistence_ModelLabel_Label = Generalization(general=Label, specific=persistence_ModelLabel)
gen_persistence_ModelLabelAttribute_ModelLabelFeature = Generalization(general=ModelLabelFeature, specific=persistence_ModelLabelAttribute)
gen_persistence_ModelLabelAssociation_ModelLabelFeature = Generalization(general=ModelLabelFeature, specific=persistence_ModelLabelAssociation)
gen_persistence_Entity_EntityOrView = Generalization(general=EntityOrView, specific=persistence_Entity)
gen_persistence_EntityFeature_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=persistence_EntityFeature)
gen_persistence_EntityFeature_Feature = Generalization(general=Feature, specific=persistence_EntityFeature)
gen_persistence_EntityAttribute_EntityFeature = Generalization(general=EntityFeature, specific=persistence_EntityAttribute)
gen_persistence_EntityAttribute_Attribute = Generalization(general=Attribute, specific=persistence_EntityAttribute)
gen_persistence_DataTypeAttribute_EntityAttribute = Generalization(general=EntityAttribute, specific=persistence_DataTypeAttribute)
gen_persistence_UrlAttribute_EntityAttribute = Generalization(general=EntityAttribute, specific=persistence_UrlAttribute)
gen_persistence_ResourceAttribute_EntityAttribute = Generalization(general=EntityAttribute, specific=persistence_ResourceAttribute)
gen_persistence_StaticPathElement_PathElement = Generalization(general=PathElement, specific=persistence_StaticPathElement)
gen_persistence_DatePathElement_PathElement = Generalization(general=PathElement, specific=persistence_DatePathElement)
gen_persistence_FileAttribute_ResourceAttribute = Generalization(general=ResourceAttribute, specific=persistence_FileAttribute)
gen_persistence_DateAttribute_EntityAttribute = Generalization(general=EntityAttribute, specific=persistence_DateAttribute)
gen_persistence_AssociationWithoutContainment_EntityAssociation = Generalization(general=EntityAssociation, specific=persistence_AssociationWithoutContainment)
gen_persistence_ImageAttribute_ResourceAttribute = Generalization(general=ResourceAttribute, specific=persistence_ImageAttribute)
gen_persistence_LocationAttribute_EntityAttribute = Generalization(general=EntityAttribute, specific=persistence_LocationAttribute)
gen_persistence_EntityAssociation_EntityFeature = Generalization(general=EntityFeature, specific=persistence_EntityAssociation)
gen_persistence_EntityAssociation_Association = Generalization(general=Association, specific=persistence_EntityAssociation)
gen_persistence_View_EntityOrView = Generalization(general=EntityOrView, specific=persistence_View)
gen_persistence_ViewFeature_Feature = Generalization(general=Feature, specific=persistence_ViewFeature)
gen_persistence_EncapsulatedFeature_ViewFeature = Generalization(general=ViewFeature, specific=persistence_EncapsulatedFeature)
gen_persistence_AssociationWithContainment_EntityAssociation = Generalization(general=EntityAssociation, specific=persistence_AssociationWithContainment)
gen_persistence_EncapsulatedAttribute_EncapsulatedFeature = Generalization(general=EncapsulatedFeature, specific=persistence_EncapsulatedAttribute)
gen_persistence_EncapsulatedAttribute_Attribute = Generalization(general=Attribute, specific=persistence_EncapsulatedAttribute)
gen_persistence_EncapsulatedAssociation_EncapsulatedFeature = Generalization(general=EncapsulatedFeature, specific=persistence_EncapsulatedAssociation)
gen_persistence_EncapsulatedAssociation_Association = Generalization(general=Association, specific=persistence_EncapsulatedAssociation)
gen_persistence_ViewAssociation_NamedDisplayElement = Generalization(general=NamedDisplayElement, specific=persistence_ViewAssociation)
gen_persistence_ViewAssociation_ViewFeature = Generalization(general=ViewFeature, specific=persistence_ViewAssociation)
gen_persistence_ViewAssociation_Association = Generalization(general=Association, specific=persistence_ViewAssociation)

# Domain Model
domain_model = DomainModel(
    name="persistence",
    types={persistence_Persistence, persistence_EntityOrView, persistence_SerializationGroup, persistence_DataType, persistence_Feature, persistence_ModelLabel, NamedElement, Classifier, persistence_Attribute, persistence_Association, Feature, Label, persistence_Expression, persistence_EncapsulatedAssociation, persistence_ModelLabelFeature, persistence_ModelLabelAttribute, ModelLabelFeature, persistence_ModelLabelAssociation, persistence_Label, persistence_Entity, EntityOrView, persistence_EntityFeature, NamedDisplayElement, persistence_EntityAssociation, persistence_EntityAttribute, EntityFeature, Attribute, persistence_DataTypeAttribute, EntityAttribute, persistence_UrlAttribute, persistence_ResourceAttribute, persistence_PathElement, persistence_StaticPathElement, PathElement, persistence_DatePathElement, persistence_FileAttribute, ResourceAttribute, persistence_DateAttribute, persistence_AssociationKey, persistence_AssociationWithoutContainment, EntityAssociation, persistence_ImageAttribute, persistence_LocationAttribute, Association, persistence_View, persistence_ViewFeature, persistence_EncapsulatedFeature, ViewFeature, persistence_AssociationWithContainment, persistence_EncapsulatedAttribute, EncapsulatedFeature, persistence_ViewAssociation, DatabaseTechnologies, OrmTechnologies, Cardinality, isHasChoices, DateDetails},
    associations={dataTypes1, entities3, serializationGroups0, keys5, unique7, containerUnique10, labels13, features14, attributes20, associations22, allAssociations24, allFeatures17, defaultValue30, encapsulatedBy32, sourceEntityX33, serializationGroups27, labelFor39, features40, serializationGroups41, partOf43, attribute45, targetEntityX36, entityFeatures51, associationEnds53, partOf54, association47, dynamicLabel48, dataType55, uploadPath57, keys58, targetEntity59, sourceFeature63, targetFeature64, encapsulates67, viewFeatures69, partOf71, keyFor61, attribute72, encapsulatedTarget76, sourceEntity77, targetEntity79, association74, opposite82},
    generalizations={gen_persistence_SerializationGroup_NamedElement, gen_persistence_EntityOrView_Classifier, gen_persistence_Attribute_Feature, gen_persistence_Attribute_Label, gen_persistence_Association_Feature, gen_persistence_ModelLabel_NamedElement, gen_persistence_ModelLabel_Label, gen_persistence_ModelLabelAttribute_ModelLabelFeature, gen_persistence_ModelLabelAssociation_ModelLabelFeature, gen_persistence_Entity_EntityOrView, gen_persistence_EntityFeature_NamedDisplayElement, gen_persistence_EntityFeature_Feature, gen_persistence_EntityAttribute_EntityFeature, gen_persistence_EntityAttribute_Attribute, gen_persistence_DataTypeAttribute_EntityAttribute, gen_persistence_UrlAttribute_EntityAttribute, gen_persistence_ResourceAttribute_EntityAttribute, gen_persistence_StaticPathElement_PathElement, gen_persistence_DatePathElement_PathElement, gen_persistence_FileAttribute_ResourceAttribute, gen_persistence_DateAttribute_EntityAttribute, gen_persistence_AssociationWithoutContainment_EntityAssociation, gen_persistence_ImageAttribute_ResourceAttribute, gen_persistence_LocationAttribute_EntityAttribute, gen_persistence_EntityAssociation_EntityFeature, gen_persistence_EntityAssociation_Association, gen_persistence_View_EntityOrView, gen_persistence_ViewFeature_Feature, gen_persistence_EncapsulatedFeature_ViewFeature, gen_persistence_AssociationWithContainment_EntityAssociation, gen_persistence_EncapsulatedAttribute_EncapsulatedFeature, gen_persistence_EncapsulatedAttribute_Attribute, gen_persistence_EncapsulatedAssociation_EncapsulatedFeature, gen_persistence_EncapsulatedAssociation_Association, gen_persistence_ViewAssociation_NamedDisplayElement, gen_persistence_ViewAssociation_ViewFeature, gen_persistence_ViewAssociation_Association},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)