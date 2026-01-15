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
AccessPolicyAccessModeEnum: Enumeration = Enumeration(
    name="AccessPolicyAccessModeEnum",
    literals={
            EnumerationLiteral(name="EDIT"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="CREATE")
    }
)

DatatypeDefinitionDateFormatEnum: Enumeration = Enumeration(
    name="DatatypeDefinitionDateFormatEnum",
    literals={
            EnumerationLiteral(name="W3C"),
			EnumerationLiteral(name="CUSTOM")
    }
)

# Classes
rif11a_ExchangeFile_SpecHierarchyRoot = Class(name="rif11a::ExchangeFile::SpecHierarchyRoot")
SpecElementWithUserDefinedAttributes = Class(name="SpecElementWithUserDefinedAttributes")
ExchangeFile_SpecHierarchy = Class(name="ExchangeFile::SpecHierarchy")
rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes = Class(name="rif11a::ExchangeFile::SpecElementWithUserDefinedAttributes", is_abstract=True)
Identifiable = Class(name="Identifiable")
ExchangeFile_SpecType = Class(name="ExchangeFile::SpecType")
ExchangeFile_AttributeValue = Class(name="ExchangeFile::AttributeValue")
rif11a_ExchangeFile_Identifiable = Class(name="rif11a::ExchangeFile::Identifiable", is_abstract=True)
rif11a_ExchangeFile_SpecType = Class(name="rif11a::ExchangeFile::SpecType")
ExchangeFile_AttributeDefinition = Class(name="ExchangeFile::AttributeDefinition")
rif11a_ExchangeFile_AttributeDefinition = Class(name="rif11a::ExchangeFile::AttributeDefinition", is_abstract=True)
rif11a_ExchangeFile_AttributeValue = Class(name="rif11a::ExchangeFile::AttributeValue", is_abstract=True)
rif11a_ExchangeFile_SpecHierarchy = Class(name="rif11a::ExchangeFile::SpecHierarchy")
ExchangeFile_SpecObject = Class(name="ExchangeFile::SpecObject")
rif11a_ExchangeFile_SpecObject = Class(name="rif11a::ExchangeFile::SpecObject")
rif11a_ExchangeFile_SpecGroup = Class(name="rif11a::ExchangeFile::SpecGroup")
ExchangeFile_RelationGroup = Class(name="ExchangeFile::RelationGroup")
rif11a_ExchangeFile_RelationGroup = Class(name="rif11a::ExchangeFile::RelationGroup")
ExchangeFile_SpecRelation = Class(name="ExchangeFile::SpecRelation")
ExchangeFile_SpecGroup = Class(name="ExchangeFile::SpecGroup")
rif11a_ExchangeFile_SpecRelation = Class(name="rif11a::ExchangeFile::SpecRelation")
rif11a_ExchangeFile_DatatypeDefinition = Class(name="rif11a::ExchangeFile::DatatypeDefinition", is_abstract=True)
rif11a_ExchangeFile_AccessPolicy = Class(name="rif11a::ExchangeFile::AccessPolicy")
ExchangeFile_DatatypeDefinition = Class(name="ExchangeFile::DatatypeDefinition")
ExchangeFile_SpecHierarchyRoot = Class(name="ExchangeFile::SpecHierarchyRoot")
rif11a_ExchangeFile_AttributeDefinitionComplex = Class(name="rif11a::ExchangeFile::AttributeDefinitionComplex")
AttributeDefinition = Class(name="AttributeDefinition")
ExchangeFile_DatatypeDefinitionComplex = Class(name="ExchangeFile::DatatypeDefinitionComplex")
ExchangeFile_AttributeValueComplex = Class(name="ExchangeFile::AttributeValueComplex")
rif11a_ExchangeFile_DatatypeDefinitionComplex = Class(name="rif11a::ExchangeFile::DatatypeDefinitionComplex", is_abstract=True)
DatatypeDefinition = Class(name="DatatypeDefinition")
rif11a_ExchangeFile_AttributeValueComplex = Class(name="rif11a::ExchangeFile::AttributeValueComplex", is_abstract=True)
AttributeValue = Class(name="AttributeValue")
rif11a_ExchangeFile_AttributeDefinitionEnumeration = Class(name="rif11a::ExchangeFile::AttributeDefinitionEnumeration")
ExchangeFile_DatatypeDefinitionEnumeration = Class(name="ExchangeFile::DatatypeDefinitionEnumeration")
ExchangeFile_AttributeValueEnumeration = Class(name="ExchangeFile::AttributeValueEnumeration")
rif11a_ExchangeFile_DatatypeDefinitionEnumeration = Class(name="rif11a::ExchangeFile::DatatypeDefinitionEnumeration")
ExchangeFile_EnumValue = Class(name="ExchangeFile::EnumValue")
rif11a_ExchangeFile_EnumValue = Class(name="rif11a::ExchangeFile::EnumValue")
ExchangeFile_EmbeddedValue = Class(name="ExchangeFile::EmbeddedValue")
rif11a_ExchangeFile_EmbeddedValue = Class(name="rif11a::ExchangeFile::EmbeddedValue")
rif11a_ExchangeFile_AttributeValueEnumeration = Class(name="rif11a::ExchangeFile::AttributeValueEnumeration")
rif11a_ExchangeFile_AttributeDefinitionSimple = Class(name="rif11a::ExchangeFile::AttributeDefinitionSimple")
ExchangeFile_DatatypeDefinitionSimple = Class(name="ExchangeFile::DatatypeDefinitionSimple")
ExchangeFile_AttributeValueSimple = Class(name="ExchangeFile::AttributeValueSimple")
rif11a_ExchangeFile_DatatypeDefinitionSimple = Class(name="rif11a::ExchangeFile::DatatypeDefinitionSimple", is_abstract=True)
rif11a_ExchangeFile_AttributeValueSimple = Class(name="rif11a::ExchangeFile::AttributeValueSimple")
ExchangeFile_AttributeDefinitionEnumeration = Class(name="ExchangeFile::AttributeDefinitionEnumeration")
ExchangeFile_AttributeDefinitionSimple = Class(name="ExchangeFile::AttributeDefinitionSimple")
rif11a_ExchangeFile_AttributeValueEmbeddedDocument = Class(name="rif11a::ExchangeFile::AttributeValueEmbeddedDocument")
AttributeValueComplex = Class(name="AttributeValueComplex")
ExchangeFile_AttributeDefinitionComplex = Class(name="ExchangeFile::AttributeDefinitionComplex")
DataTypes_XhtmlContent = Class(name="DataTypes::XhtmlContent")
rif11a_ExchangeFile_AttributeValueEmbeddedFile = Class(name="rif11a::ExchangeFile::AttributeValueEmbeddedFile")
DataTypes_BinaryContent = Class(name="DataTypes::BinaryContent")
rif11a_ExchangeFile_AttributeValueFileReference = Class(name="rif11a::ExchangeFile::AttributeValueFileReference")
rif11a_ExchangeFile_AttributeValueXmlData = Class(name="rif11a::ExchangeFile::AttributeValueXmlData")
DataTypes_XmlContent = Class(name="DataTypes::XmlContent")
rif11a_ExchangeFile_DatatypeDefinitionBinaryFile = Class(name="rif11a::ExchangeFile::DatatypeDefinitionBinaryFile")
DatatypeDefinitionComplex = Class(name="DatatypeDefinitionComplex")
rif11a_ExchangeFile_DatatypeDefinitionBoolean = Class(name="rif11a::ExchangeFile::DatatypeDefinitionBoolean")
DatatypeDefinitionSimple = Class(name="DatatypeDefinitionSimple")
rif11a_ExchangeFile_DatatypeDefinitionDate = Class(name="rif11a::ExchangeFile::DatatypeDefinitionDate")
rif11a_ExchangeFile_DatatypeDefinitionDocument = Class(name="rif11a::ExchangeFile::DatatypeDefinitionDocument")
rif11a_ExchangeFile_DatatypeDefinitionInteger = Class(name="rif11a::ExchangeFile::DatatypeDefinitionInteger")
rif11a_ExchangeFile_DatatypeDefinitionReal = Class(name="rif11a::ExchangeFile::DatatypeDefinitionReal")
rif11a_ExchangeFile_DatatypeDefinitionString = Class(name="rif11a::ExchangeFile::DatatypeDefinitionString")
rif11a_ExchangeFile_DatatypeDefinitionXmlData = Class(name="rif11a::ExchangeFile::DatatypeDefinitionXmlData")
rif11a_ExchangeFile_RIF = Class(name="rif11a::ExchangeFile::RIF")
ExchangeFile_AccessPolicy = Class(name="ExchangeFile::AccessPolicy")
rif11a_DataTypes_BinaryContent = Class(name="rif11a::DataTypes::BinaryContent")
rif11a_DataTypes_XmlContent = Class(name="rif11a::DataTypes::XmlContent")
rif11a_DataTypes_XhtmlContent = Class(name="rif11a::DataTypes::XhtmlContent")

# rif11a_ExchangeFile_SpecHierarchyRoot class attributes and methods

# SpecElementWithUserDefinedAttributes class attributes and methods

# ExchangeFile_SpecHierarchy class attributes and methods

# rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes class attributes and methods

# Identifiable class attributes and methods

# ExchangeFile_SpecType class attributes and methods

# ExchangeFile_AttributeValue class attributes and methods

# rif11a_ExchangeFile_Identifiable class attributes and methods
rif11a_ExchangeFile_Identifiable_desc: Property = Property(name="desc", type=StringType)
rif11a_ExchangeFile_Identifiable_identifier: Property = Property(name="identifier", type=StringType)
rif11a_ExchangeFile_Identifiable_lastChange: Property = Property(name="lastChange", type=StringType)
rif11a_ExchangeFile_Identifiable_longName: Property = Property(name="longName", type=StringType)
rif11a_ExchangeFile_Identifiable.attributes={rif11a_ExchangeFile_Identifiable_desc, rif11a_ExchangeFile_Identifiable_longName, rif11a_ExchangeFile_Identifiable_lastChange, rif11a_ExchangeFile_Identifiable_identifier}

# rif11a_ExchangeFile_SpecType class attributes and methods

# ExchangeFile_AttributeDefinition class attributes and methods

# rif11a_ExchangeFile_AttributeDefinition class attributes and methods

# rif11a_ExchangeFile_AttributeValue class attributes and methods

# rif11a_ExchangeFile_SpecHierarchy class attributes and methods

# ExchangeFile_SpecObject class attributes and methods

# rif11a_ExchangeFile_SpecObject class attributes and methods

# rif11a_ExchangeFile_SpecGroup class attributes and methods

# ExchangeFile_RelationGroup class attributes and methods

# rif11a_ExchangeFile_RelationGroup class attributes and methods

# ExchangeFile_SpecRelation class attributes and methods

# ExchangeFile_SpecGroup class attributes and methods

# rif11a_ExchangeFile_SpecRelation class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinition class attributes and methods

# rif11a_ExchangeFile_AccessPolicy class attributes and methods
rif11a_ExchangeFile_AccessPolicy_accessMode: Property = Property(name="accessMode", type=StringType)
rif11a_ExchangeFile_AccessPolicy.attributes={rif11a_ExchangeFile_AccessPolicy_accessMode}

# ExchangeFile_DatatypeDefinition class attributes and methods

# ExchangeFile_SpecHierarchyRoot class attributes and methods

# rif11a_ExchangeFile_AttributeDefinitionComplex class attributes and methods

# AttributeDefinition class attributes and methods

# ExchangeFile_DatatypeDefinitionComplex class attributes and methods

# ExchangeFile_AttributeValueComplex class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionComplex class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionComplex_embedded: Property = Property(name="embedded", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionComplex.attributes={rif11a_ExchangeFile_DatatypeDefinitionComplex_embedded}

# DatatypeDefinition class attributes and methods

# rif11a_ExchangeFile_AttributeValueComplex class attributes and methods

# AttributeValue class attributes and methods

# rif11a_ExchangeFile_AttributeDefinitionEnumeration class attributes and methods
rif11a_ExchangeFile_AttributeDefinitionEnumeration_multiValued: Property = Property(name="multiValued", type=StringType)
rif11a_ExchangeFile_AttributeDefinitionEnumeration.attributes={rif11a_ExchangeFile_AttributeDefinitionEnumeration_multiValued}

# ExchangeFile_DatatypeDefinitionEnumeration class attributes and methods

# ExchangeFile_AttributeValueEnumeration class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionEnumeration class attributes and methods

# ExchangeFile_EnumValue class attributes and methods

# rif11a_ExchangeFile_EnumValue class attributes and methods

# ExchangeFile_EmbeddedValue class attributes and methods

# rif11a_ExchangeFile_EmbeddedValue class attributes and methods
rif11a_ExchangeFile_EmbeddedValue_key: Property = Property(name="key", type=StringType)
rif11a_ExchangeFile_EmbeddedValue_otherContent: Property = Property(name="otherContent", type=StringType)
rif11a_ExchangeFile_EmbeddedValue.attributes={rif11a_ExchangeFile_EmbeddedValue_key, rif11a_ExchangeFile_EmbeddedValue_otherContent}

# rif11a_ExchangeFile_AttributeValueEnumeration class attributes and methods

# rif11a_ExchangeFile_AttributeDefinitionSimple class attributes and methods

# ExchangeFile_DatatypeDefinitionSimple class attributes and methods

# ExchangeFile_AttributeValueSimple class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionSimple class attributes and methods

# rif11a_ExchangeFile_AttributeValueSimple class attributes and methods
rif11a_ExchangeFile_AttributeValueSimple_theValue: Property = Property(name="theValue", type=StringType)
rif11a_ExchangeFile_AttributeValueSimple.attributes={rif11a_ExchangeFile_AttributeValueSimple_theValue}

# ExchangeFile_AttributeDefinitionEnumeration class attributes and methods

# ExchangeFile_AttributeDefinitionSimple class attributes and methods

# rif11a_ExchangeFile_AttributeValueEmbeddedDocument class attributes and methods

# AttributeValueComplex class attributes and methods

# ExchangeFile_AttributeDefinitionComplex class attributes and methods

# DataTypes_XhtmlContent class attributes and methods

# rif11a_ExchangeFile_AttributeValueEmbeddedFile class attributes and methods

# DataTypes_BinaryContent class attributes and methods

# rif11a_ExchangeFile_AttributeValueFileReference class attributes and methods
rif11a_ExchangeFile_AttributeValueFileReference_pathToFile: Property = Property(name="pathToFile", type=StringType)
rif11a_ExchangeFile_AttributeValueFileReference.attributes={rif11a_ExchangeFile_AttributeValueFileReference_pathToFile}

# rif11a_ExchangeFile_AttributeValueXmlData class attributes and methods

# DataTypes_XmlContent class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionBinaryFile class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_application: Property = Property(name="application", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_filenameSuffix: Property = Property(name="filenameSuffix", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_formatName: Property = Property(name="formatName", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_mimeType: Property = Property(name="mimeType", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionBinaryFile.attributes={rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_mimeType, rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_filenameSuffix, rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_formatName, rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_application}

# DatatypeDefinitionComplex class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionBoolean class attributes and methods

# DatatypeDefinitionSimple class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionDate class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionDate_format: Property = Property(name="format", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionDate.attributes={rif11a_ExchangeFile_DatatypeDefinitionDate_format}

# rif11a_ExchangeFile_DatatypeDefinitionDocument class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionInteger class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionInteger_max: Property = Property(name="max", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionInteger_min: Property = Property(name="min", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionInteger.attributes={rif11a_ExchangeFile_DatatypeDefinitionInteger_max, rif11a_ExchangeFile_DatatypeDefinitionInteger_min}

# rif11a_ExchangeFile_DatatypeDefinitionReal class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionReal_accuracy: Property = Property(name="accuracy", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionReal_max: Property = Property(name="max", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionReal_min: Property = Property(name="min", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionReal.attributes={rif11a_ExchangeFile_DatatypeDefinitionReal_min, rif11a_ExchangeFile_DatatypeDefinitionReal_accuracy, rif11a_ExchangeFile_DatatypeDefinitionReal_max}

# rif11a_ExchangeFile_DatatypeDefinitionString class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionString_maxLength: Property = Property(name="maxLength", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionString.attributes={rif11a_ExchangeFile_DatatypeDefinitionString_maxLength}

# rif11a_ExchangeFile_DatatypeDefinitionXmlData class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionXmlData_nameSpaceURI: Property = Property(name="nameSpaceURI", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionXmlData_schemaLocation: Property = Property(name="schemaLocation", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionXmlData.attributes={rif11a_ExchangeFile_DatatypeDefinitionXmlData_nameSpaceURI, rif11a_ExchangeFile_DatatypeDefinitionXmlData_schemaLocation}

# rif11a_ExchangeFile_RIF class attributes and methods
rif11a_ExchangeFile_RIF_author: Property = Property(name="author", type=StringType)
rif11a_ExchangeFile_RIF_comment: Property = Property(name="comment", type=StringType)
rif11a_ExchangeFile_RIF_countryCode: Property = Property(name="countryCode", type=StringType)
rif11a_ExchangeFile_RIF_creationTime: Property = Property(name="creationTime", type=StringType)
rif11a_ExchangeFile_RIF_identifier: Property = Property(name="identifier", type=StringType)
rif11a_ExchangeFile_RIF_sourceToolId: Property = Property(name="sourceToolId", type=StringType)
rif11a_ExchangeFile_RIF_title: Property = Property(name="title", type=StringType)
rif11a_ExchangeFile_RIF_version: Property = Property(name="version", type=StringType)
rif11a_ExchangeFile_RIF.attributes={rif11a_ExchangeFile_RIF_identifier, rif11a_ExchangeFile_RIF_comment, rif11a_ExchangeFile_RIF_countryCode, rif11a_ExchangeFile_RIF_creationTime, rif11a_ExchangeFile_RIF_author, rif11a_ExchangeFile_RIF_title, rif11a_ExchangeFile_RIF_version, rif11a_ExchangeFile_RIF_sourceToolId}

# ExchangeFile_AccessPolicy class attributes and methods

# rif11a_DataTypes_BinaryContent class attributes and methods

# rif11a_DataTypes_XmlContent class attributes and methods

# rif11a_DataTypes_XhtmlContent class attributes and methods

# Relationships
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="ExchangeFile_SpecHierarchy", type=rif11a_ExchangeFile_SpecHierarchyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecHierarchyRoot", type=ExchangeFile_SpecHierarchy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="ExchangeFile_SpecType", type=rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes", type=ExchangeFile_SpecType, multiplicity=Multiplicity(1, 1))
    }
)
values2: BinaryAssociation = BinaryAssociation(
    name="values2",
    ends={
        Property(name="ExchangeFile_AttributeValue", type=rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes3", type=ExchangeFile_AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specAttributes4: BinaryAssociation = BinaryAssociation(
    name="specAttributes4",
    ends={
        Property(name="ExchangeFile_AttributeDefinition", type=rif11a_ExchangeFile_SpecType, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecType", type=ExchangeFile_AttributeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationGroups11: BinaryAssociation = BinaryAssociation(
    name="relationGroups11",
    ends={
        Property(name="rif", type=rif11a_ExchangeFile_SpecGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ExchangeFile", type=ExchangeFile_RelationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object5: BinaryAssociation = BinaryAssociation(
    name="object5",
    ends={
        Property(name="ExchangeFile_SpecObject", type=rif11a_ExchangeFile_SpecHierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecHierarchy", type=ExchangeFile_SpecObject, multiplicity=Multiplicity(1, 1))
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="ExchangeFile_SpecHierarchy8", type=rif11a_ExchangeFile_SpecHierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecHierarchy7", type=ExchangeFile_SpecHierarchy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specObjects9: BinaryAssociation = BinaryAssociation(
    name="specObjects9",
    ends={
        Property(name="ExchangeFile_SpecObject10", type=rif11a_ExchangeFile_SpecGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecGroup", type=ExchangeFile_SpecObject, multiplicity=Multiplicity(0, 9999))
    }
)
specRelations12: BinaryAssociation = BinaryAssociation(
    name="specRelations12",
    ends={
        Property(name="ExchangeFile_SpecRelation", type=rif11a_ExchangeFile_RelationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RelationGroup", type=ExchangeFile_SpecRelation, multiplicity=Multiplicity(0, 9999))
    }
)
relationType13: BinaryAssociation = BinaryAssociation(
    name="relationType13",
    ends={
        Property(name="ExchangeFile_SpecType15", type=rif11a_ExchangeFile_RelationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RelationGroup14", type=ExchangeFile_SpecType, multiplicity=Multiplicity(0, 1))
    }
)
sourceGroup16: BinaryAssociation = BinaryAssociation(
    name="sourceGroup16",
    ends={
        Property(name="rif18", type=rif11a_ExchangeFile_RelationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="ExchangeFile17", type=ExchangeFile_SpecGroup, multiplicity=Multiplicity(1, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="ExchangeFile_SpecObject20", type=rif11a_ExchangeFile_SpecRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecRelation", type=ExchangeFile_SpecObject, multiplicity=Multiplicity(1, 1))
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="ExchangeFile_SpecObject23", type=rif11a_ExchangeFile_SpecRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecRelation22", type=ExchangeFile_SpecObject, multiplicity=Multiplicity(1, 1))
    }
)
specGroups24: BinaryAssociation = BinaryAssociation(
    name="specGroups24",
    ends={
        Property(name="ExchangeFile_SpecGroup", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy", type=ExchangeFile_SpecGroup, multiplicity=Multiplicity(0, 9999))
    }
)
attributeDefinitions25: BinaryAssociation = BinaryAssociation(
    name="attributeDefinitions25",
    ends={
        Property(name="ExchangeFile_AttributeDefinition27", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy26", type=ExchangeFile_AttributeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
relationGroups28: BinaryAssociation = BinaryAssociation(
    name="relationGroups28",
    ends={
        Property(name="ExchangeFile_RelationGroup", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy29", type=ExchangeFile_RelationGroup, multiplicity=Multiplicity(0, 9999))
    }
)
datatypeDefinitions30: BinaryAssociation = BinaryAssociation(
    name="datatypeDefinitions30",
    ends={
        Property(name="ExchangeFile_DatatypeDefinition", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy31", type=ExchangeFile_DatatypeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
specRelations32: BinaryAssociation = BinaryAssociation(
    name="specRelations32",
    ends={
        Property(name="ExchangeFile_SpecRelation34", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy33", type=ExchangeFile_SpecRelation, multiplicity=Multiplicity(0, 9999))
    }
)
attributeValues35: BinaryAssociation = BinaryAssociation(
    name="attributeValues35",
    ends={
        Property(name="ExchangeFile_AttributeValue37", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy36", type=ExchangeFile_AttributeValue, multiplicity=Multiplicity(0, 9999))
    }
)
specTypes38: BinaryAssociation = BinaryAssociation(
    name="specTypes38",
    ends={
        Property(name="ExchangeFile_SpecType40", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy39", type=ExchangeFile_SpecType, multiplicity=Multiplicity(0, 9999))
    }
)
specHierarchies41: BinaryAssociation = BinaryAssociation(
    name="specHierarchies41",
    ends={
        Property(name="ExchangeFile_SpecHierarchy43", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy42", type=ExchangeFile_SpecHierarchy, multiplicity=Multiplicity(0, 9999))
    }
)
specObjects44: BinaryAssociation = BinaryAssociation(
    name="specObjects44",
    ends={
        Property(name="ExchangeFile_SpecObject46", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy45", type=ExchangeFile_SpecObject, multiplicity=Multiplicity(0, 9999))
    }
)
specHierarchyRoots47: BinaryAssociation = BinaryAssociation(
    name="specHierarchyRoots47",
    ends={
        Property(name="ExchangeFile_SpecHierarchyRoot", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy48", type=ExchangeFile_SpecHierarchyRoot, multiplicity=Multiplicity(0, 9999))
    }
)
defaultValue50: BinaryAssociation = BinaryAssociation(
    name="defaultValue50",
    ends={
        Property(name="ExchangeFile_AttributeValueComplex", type=rif11a_ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionComplex51", type=ExchangeFile_AttributeValueComplex, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="ExchangeFile_DatatypeDefinitionComplex", type=rif11a_ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionComplex", type=ExchangeFile_DatatypeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="ExchangeFile_DatatypeDefinitionEnumeration", type=rif11a_ExchangeFile_AttributeDefinitionEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionEnumeration", type=ExchangeFile_DatatypeDefinitionEnumeration, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue53: BinaryAssociation = BinaryAssociation(
    name="defaultValue53",
    ends={
        Property(name="ExchangeFile_AttributeValueEnumeration", type=rif11a_ExchangeFile_AttributeDefinitionEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionEnumeration54", type=ExchangeFile_AttributeValueEnumeration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifiedValues55: BinaryAssociation = BinaryAssociation(
    name="specifiedValues55",
    ends={
        Property(name="ExchangeFile_EnumValue", type=rif11a_ExchangeFile_DatatypeDefinitionEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_DatatypeDefinitionEnumeration", type=ExchangeFile_EnumValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties56: BinaryAssociation = BinaryAssociation(
    name="properties56",
    ends={
        Property(name="ExchangeFile_EmbeddedValue", type=rif11a_ExchangeFile_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_EnumValue", type=ExchangeFile_EmbeddedValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values57: BinaryAssociation = BinaryAssociation(
    name="values57",
    ends={
        Property(name="ExchangeFile_EnumValue58", type=rif11a_ExchangeFile_AttributeValueEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEnumeration", type=ExchangeFile_EnumValue, multiplicity=Multiplicity(0, 9999))
    }
)
definition59: BinaryAssociation = BinaryAssociation(
    name="definition59",
    ends={
        Property(name="rif11a_ExchangeFile_AttributeValueEnumeration60", type=ExchangeFile_AttributeDefinitionEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="ExchangeFile_AttributeDefinitionEnumeration", type=rif11a_ExchangeFile_AttributeValueEnumeration, multiplicity=Multiplicity(1, 1))
    }
)
type61: BinaryAssociation = BinaryAssociation(
    name="type61",
    ends={
        Property(name="ExchangeFile_DatatypeDefinitionSimple", type=rif11a_ExchangeFile_AttributeDefinitionSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionSimple", type=ExchangeFile_DatatypeDefinitionSimple, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue62: BinaryAssociation = BinaryAssociation(
    name="defaultValue62",
    ends={
        Property(name="ExchangeFile_AttributeValueSimple", type=rif11a_ExchangeFile_AttributeDefinitionSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionSimple63", type=ExchangeFile_AttributeValueSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition64: BinaryAssociation = BinaryAssociation(
    name="definition64",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionSimple", type=rif11a_ExchangeFile_AttributeValueSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueSimple", type=ExchangeFile_AttributeDefinitionSimple, multiplicity=Multiplicity(1, 1))
    }
)
definition65: BinaryAssociation = BinaryAssociation(
    name="definition65",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionComplex", type=rif11a_ExchangeFile_AttributeValueEmbeddedDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEmbeddedDocument", type=ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
xhtmlContent66: BinaryAssociation = BinaryAssociation(
    name="xhtmlContent66",
    ends={
        Property(name="DataTypes_XhtmlContent", type=rif11a_ExchangeFile_AttributeValueEmbeddedDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEmbeddedDocument67", type=DataTypes_XhtmlContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition68: BinaryAssociation = BinaryAssociation(
    name="definition68",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionComplex69", type=rif11a_ExchangeFile_AttributeValueEmbeddedFile, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEmbeddedFile", type=ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
binaryContent70: BinaryAssociation = BinaryAssociation(
    name="binaryContent70",
    ends={
        Property(name="DataTypes_BinaryContent", type=rif11a_ExchangeFile_AttributeValueEmbeddedFile, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEmbeddedFile71", type=DataTypes_BinaryContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition72: BinaryAssociation = BinaryAssociation(
    name="definition72",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionComplex73", type=rif11a_ExchangeFile_AttributeValueFileReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueFileReference", type=ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
definition74: BinaryAssociation = BinaryAssociation(
    name="definition74",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionComplex75", type=rif11a_ExchangeFile_AttributeValueXmlData, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueXmlData", type=ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
xmlContent76: BinaryAssociation = BinaryAssociation(
    name="xmlContent76",
    ends={
        Property(name="DataTypes_XmlContent", type=rif11a_ExchangeFile_AttributeValueXmlData, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueXmlData77", type=DataTypes_XmlContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accessPolicies78: BinaryAssociation = BinaryAssociation(
    name="accessPolicies78",
    ends={
        Property(name="ExchangeFile_AccessPolicy", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF", type=ExchangeFile_AccessPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes79: BinaryAssociation = BinaryAssociation(
    name="datatypes79",
    ends={
        Property(name="ExchangeFile_DatatypeDefinition81", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF80", type=ExchangeFile_DatatypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
SpecHierarchyRoots82: BinaryAssociation = BinaryAssociation(
    name="SpecHierarchyRoots82",
    ends={
        Property(name="ExchangeFile_SpecHierarchyRoot84", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF83", type=ExchangeFile_SpecHierarchyRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specObjects85: BinaryAssociation = BinaryAssociation(
    name="specObjects85",
    ends={
        Property(name="ExchangeFile_SpecObject87", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF86", type=ExchangeFile_SpecObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specGroups88: BinaryAssociation = BinaryAssociation(
    name="specGroups88",
    ends={
        Property(name="ExchangeFile_SpecGroup90", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF89", type=ExchangeFile_SpecGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specTypes91: BinaryAssociation = BinaryAssociation(
    name="specTypes91",
    ends={
        Property(name="ExchangeFile_SpecType93", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF92", type=ExchangeFile_SpecType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specRelations94: BinaryAssociation = BinaryAssociation(
    name="specRelations94",
    ends={
        Property(name="ExchangeFile_SpecRelation96", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF95", type=ExchangeFile_SpecRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_rif11a_ExchangeFile_SpecHierarchyRoot_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif11a_ExchangeFile_SpecHierarchyRoot)
gen_rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes)
gen_rif11a_ExchangeFile_SpecType_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_SpecType)
gen_rif11a_ExchangeFile_AttributeDefinition_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_AttributeDefinition)
gen_rif11a_ExchangeFile_AttributeValue_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_AttributeValue)
gen_rif11a_ExchangeFile_SpecHierarchy_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_SpecHierarchy)
gen_rif11a_ExchangeFile_SpecObject_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif11a_ExchangeFile_SpecObject)
gen_rif11a_ExchangeFile_SpecGroup_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif11a_ExchangeFile_SpecGroup)
gen_rif11a_ExchangeFile_RelationGroup_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_RelationGroup)
gen_rif11a_ExchangeFile_SpecRelation_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif11a_ExchangeFile_SpecRelation)
gen_rif11a_ExchangeFile_DatatypeDefinition_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_DatatypeDefinition)
gen_rif11a_ExchangeFile_AccessPolicy_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_AccessPolicy)
gen_rif11a_ExchangeFile_AttributeDefinitionComplex_AttributeDefinition = Generalization(general=AttributeDefinition, specific=rif11a_ExchangeFile_AttributeDefinitionComplex)
gen_rif11a_ExchangeFile_DatatypeDefinitionComplex_DatatypeDefinition = Generalization(general=DatatypeDefinition, specific=rif11a_ExchangeFile_DatatypeDefinitionComplex)
gen_rif11a_ExchangeFile_AttributeValueComplex_AttributeValue = Generalization(general=AttributeValue, specific=rif11a_ExchangeFile_AttributeValueComplex)
gen_rif11a_ExchangeFile_AttributeDefinitionEnumeration_AttributeDefinition = Generalization(general=AttributeDefinition, specific=rif11a_ExchangeFile_AttributeDefinitionEnumeration)
gen_rif11a_ExchangeFile_DatatypeDefinitionEnumeration_DatatypeDefinition = Generalization(general=DatatypeDefinition, specific=rif11a_ExchangeFile_DatatypeDefinitionEnumeration)
gen_rif11a_ExchangeFile_EnumValue_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_EnumValue)
gen_rif11a_ExchangeFile_AttributeValueEnumeration_AttributeValue = Generalization(general=AttributeValue, specific=rif11a_ExchangeFile_AttributeValueEnumeration)
gen_rif11a_ExchangeFile_AttributeDefinitionSimple_AttributeDefinition = Generalization(general=AttributeDefinition, specific=rif11a_ExchangeFile_AttributeDefinitionSimple)
gen_rif11a_ExchangeFile_DatatypeDefinitionSimple_DatatypeDefinition = Generalization(general=DatatypeDefinition, specific=rif11a_ExchangeFile_DatatypeDefinitionSimple)
gen_rif11a_ExchangeFile_AttributeValueSimple_AttributeValue = Generalization(general=AttributeValue, specific=rif11a_ExchangeFile_AttributeValueSimple)
gen_rif11a_ExchangeFile_AttributeValueEmbeddedDocument_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif11a_ExchangeFile_AttributeValueEmbeddedDocument)
gen_rif11a_ExchangeFile_AttributeValueEmbeddedFile_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif11a_ExchangeFile_AttributeValueEmbeddedFile)
gen_rif11a_ExchangeFile_AttributeValueFileReference_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif11a_ExchangeFile_AttributeValueFileReference)
gen_rif11a_ExchangeFile_AttributeValueXmlData_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif11a_ExchangeFile_AttributeValueXmlData)
gen_rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_DatatypeDefinitionComplex = Generalization(general=DatatypeDefinitionComplex, specific=rif11a_ExchangeFile_DatatypeDefinitionBinaryFile)
gen_rif11a_ExchangeFile_DatatypeDefinitionBoolean_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif11a_ExchangeFile_DatatypeDefinitionBoolean)
gen_rif11a_ExchangeFile_DatatypeDefinitionDate_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif11a_ExchangeFile_DatatypeDefinitionDate)
gen_rif11a_ExchangeFile_DatatypeDefinitionDocument_DatatypeDefinitionComplex = Generalization(general=DatatypeDefinitionComplex, specific=rif11a_ExchangeFile_DatatypeDefinitionDocument)
gen_rif11a_ExchangeFile_DatatypeDefinitionInteger_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif11a_ExchangeFile_DatatypeDefinitionInteger)
gen_rif11a_ExchangeFile_DatatypeDefinitionReal_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif11a_ExchangeFile_DatatypeDefinitionReal)
gen_rif11a_ExchangeFile_DatatypeDefinitionString_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif11a_ExchangeFile_DatatypeDefinitionString)
gen_rif11a_ExchangeFile_DatatypeDefinitionXmlData_DatatypeDefinitionComplex = Generalization(general=DatatypeDefinitionComplex, specific=rif11a_ExchangeFile_DatatypeDefinitionXmlData)

# Domain Model
domain_model = DomainModel(
    name="rif11a",
    types={rif11a_ExchangeFile_SpecHierarchyRoot, SpecElementWithUserDefinedAttributes, ExchangeFile_SpecHierarchy, rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes, Identifiable, ExchangeFile_SpecType, ExchangeFile_AttributeValue, rif11a_ExchangeFile_Identifiable, rif11a_ExchangeFile_SpecType, ExchangeFile_AttributeDefinition, rif11a_ExchangeFile_AttributeDefinition, rif11a_ExchangeFile_AttributeValue, rif11a_ExchangeFile_SpecHierarchy, ExchangeFile_SpecObject, rif11a_ExchangeFile_SpecObject, rif11a_ExchangeFile_SpecGroup, ExchangeFile_RelationGroup, rif11a_ExchangeFile_RelationGroup, ExchangeFile_SpecRelation, ExchangeFile_SpecGroup, rif11a_ExchangeFile_SpecRelation, rif11a_ExchangeFile_DatatypeDefinition, rif11a_ExchangeFile_AccessPolicy, ExchangeFile_DatatypeDefinition, ExchangeFile_SpecHierarchyRoot, rif11a_ExchangeFile_AttributeDefinitionComplex, AttributeDefinition, ExchangeFile_DatatypeDefinitionComplex, ExchangeFile_AttributeValueComplex, rif11a_ExchangeFile_DatatypeDefinitionComplex, DatatypeDefinition, rif11a_ExchangeFile_AttributeValueComplex, AttributeValue, rif11a_ExchangeFile_AttributeDefinitionEnumeration, ExchangeFile_DatatypeDefinitionEnumeration, ExchangeFile_AttributeValueEnumeration, rif11a_ExchangeFile_DatatypeDefinitionEnumeration, ExchangeFile_EnumValue, rif11a_ExchangeFile_EnumValue, ExchangeFile_EmbeddedValue, rif11a_ExchangeFile_EmbeddedValue, rif11a_ExchangeFile_AttributeValueEnumeration, rif11a_ExchangeFile_AttributeDefinitionSimple, ExchangeFile_DatatypeDefinitionSimple, ExchangeFile_AttributeValueSimple, rif11a_ExchangeFile_DatatypeDefinitionSimple, rif11a_ExchangeFile_AttributeValueSimple, ExchangeFile_AttributeDefinitionEnumeration, ExchangeFile_AttributeDefinitionSimple, rif11a_ExchangeFile_AttributeValueEmbeddedDocument, AttributeValueComplex, ExchangeFile_AttributeDefinitionComplex, DataTypes_XhtmlContent, rif11a_ExchangeFile_AttributeValueEmbeddedFile, DataTypes_BinaryContent, rif11a_ExchangeFile_AttributeValueFileReference, rif11a_ExchangeFile_AttributeValueXmlData, DataTypes_XmlContent, rif11a_ExchangeFile_DatatypeDefinitionBinaryFile, DatatypeDefinitionComplex, rif11a_ExchangeFile_DatatypeDefinitionBoolean, DatatypeDefinitionSimple, rif11a_ExchangeFile_DatatypeDefinitionDate, rif11a_ExchangeFile_DatatypeDefinitionDocument, rif11a_ExchangeFile_DatatypeDefinitionInteger, rif11a_ExchangeFile_DatatypeDefinitionReal, rif11a_ExchangeFile_DatatypeDefinitionString, rif11a_ExchangeFile_DatatypeDefinitionXmlData, rif11a_ExchangeFile_RIF, ExchangeFile_AccessPolicy, rif11a_DataTypes_BinaryContent, rif11a_DataTypes_XmlContent, rif11a_DataTypes_XhtmlContent, AccessPolicyAccessModeEnum, DatatypeDefinitionDateFormatEnum},
    associations={children0, type1, values2, specAttributes4, relationGroups11, object5, children6, specObjects9, specRelations12, relationType13, sourceGroup16, target19, source21, specGroups24, attributeDefinitions25, relationGroups28, datatypeDefinitions30, specRelations32, attributeValues35, specTypes38, specHierarchies41, specObjects44, specHierarchyRoots47, defaultValue50, type49, type52, defaultValue53, specifiedValues55, properties56, values57, definition59, type61, defaultValue62, definition64, definition65, xhtmlContent66, definition68, binaryContent70, definition72, definition74, xmlContent76, accessPolicies78, datatypes79, SpecHierarchyRoots82, specObjects85, specGroups88, specTypes91, specRelations94},
    generalizations={gen_rif11a_ExchangeFile_SpecHierarchyRoot_SpecElementWithUserDefinedAttributes, gen_rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes_Identifiable, gen_rif11a_ExchangeFile_SpecType_Identifiable, gen_rif11a_ExchangeFile_AttributeDefinition_Identifiable, gen_rif11a_ExchangeFile_AttributeValue_Identifiable, gen_rif11a_ExchangeFile_SpecHierarchy_Identifiable, gen_rif11a_ExchangeFile_SpecObject_SpecElementWithUserDefinedAttributes, gen_rif11a_ExchangeFile_SpecGroup_SpecElementWithUserDefinedAttributes, gen_rif11a_ExchangeFile_RelationGroup_Identifiable, gen_rif11a_ExchangeFile_SpecRelation_SpecElementWithUserDefinedAttributes, gen_rif11a_ExchangeFile_DatatypeDefinition_Identifiable, gen_rif11a_ExchangeFile_AccessPolicy_Identifiable, gen_rif11a_ExchangeFile_AttributeDefinitionComplex_AttributeDefinition, gen_rif11a_ExchangeFile_DatatypeDefinitionComplex_DatatypeDefinition, gen_rif11a_ExchangeFile_AttributeValueComplex_AttributeValue, gen_rif11a_ExchangeFile_AttributeDefinitionEnumeration_AttributeDefinition, gen_rif11a_ExchangeFile_DatatypeDefinitionEnumeration_DatatypeDefinition, gen_rif11a_ExchangeFile_EnumValue_Identifiable, gen_rif11a_ExchangeFile_AttributeValueEnumeration_AttributeValue, gen_rif11a_ExchangeFile_AttributeDefinitionSimple_AttributeDefinition, gen_rif11a_ExchangeFile_DatatypeDefinitionSimple_DatatypeDefinition, gen_rif11a_ExchangeFile_AttributeValueSimple_AttributeValue, gen_rif11a_ExchangeFile_AttributeValueEmbeddedDocument_AttributeValueComplex, gen_rif11a_ExchangeFile_AttributeValueEmbeddedFile_AttributeValueComplex, gen_rif11a_ExchangeFile_AttributeValueFileReference_AttributeValueComplex, gen_rif11a_ExchangeFile_AttributeValueXmlData_AttributeValueComplex, gen_rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_DatatypeDefinitionComplex, gen_rif11a_ExchangeFile_DatatypeDefinitionBoolean_DatatypeDefinitionSimple, gen_rif11a_ExchangeFile_DatatypeDefinitionDate_DatatypeDefinitionSimple, gen_rif11a_ExchangeFile_DatatypeDefinitionDocument_DatatypeDefinitionComplex, gen_rif11a_ExchangeFile_DatatypeDefinitionInteger_DatatypeDefinitionSimple, gen_rif11a_ExchangeFile_DatatypeDefinitionReal_DatatypeDefinitionSimple, gen_rif11a_ExchangeFile_DatatypeDefinitionString_DatatypeDefinitionSimple, gen_rif11a_ExchangeFile_DatatypeDefinitionXmlData_DatatypeDefinitionComplex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)