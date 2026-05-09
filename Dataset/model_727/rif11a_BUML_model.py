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
rif11a_ExchangeFile_SpecHierarchyRoot = Class(name="rif11a_ExchangeFile_SpecHierarchyRoot")
SpecElementWithUserDefinedAttributes = Class(name="SpecElementWithUserDefinedAttributes")
rif11a_ExchangeFile_SpecHierarchy = Class(name="rif11a_ExchangeFile_SpecHierarchy")
ExchangeFile_SpecObject = Class(name="ExchangeFile_SpecObject")
rif11a_ExchangeFile_SpecObject = Class(name="rif11a_ExchangeFile_SpecObject")
rif11a_ExchangeFile_SpecGroup = Class(name="rif11a_ExchangeFile_SpecGroup")
ExchangeFile_RelationGroup = Class(name="ExchangeFile_RelationGroup")
rif11a_ExchangeFile_RelationGroup = Class(name="rif11a_ExchangeFile_RelationGroup")
ExchangeFile_SpecRelation = Class(name="ExchangeFile_SpecRelation")
ExchangeFile_SpecHierarchy = Class(name="ExchangeFile_SpecHierarchy")
rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes = Class(name="rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes", is_abstract=True)
Identifiable = Class(name="Identifiable")
ExchangeFile_SpecType = Class(name="ExchangeFile_SpecType")
ExchangeFile_AttributeValue = Class(name="ExchangeFile_AttributeValue")
rif11a_ExchangeFile_Identifiable = Class(name="rif11a_ExchangeFile_Identifiable", is_abstract=True)
rif11a_ExchangeFile_SpecType = Class(name="rif11a_ExchangeFile_SpecType")
ExchangeFile_AttributeDefinition = Class(name="ExchangeFile_AttributeDefinition")
rif11a_ExchangeFile_AttributeDefinition = Class(name="rif11a_ExchangeFile_AttributeDefinition", is_abstract=True)
rif11a_ExchangeFile_AttributeValue = Class(name="rif11a_ExchangeFile_AttributeValue", is_abstract=True)
ExchangeFile_SpecHierarchyRoot = Class(name="ExchangeFile_SpecHierarchyRoot")
rif11a_ExchangeFile_AttributeDefinitionComplex = Class(name="rif11a_ExchangeFile_AttributeDefinitionComplex")
AttributeDefinition = Class(name="AttributeDefinition")
ExchangeFile_DatatypeDefinitionComplex = Class(name="ExchangeFile_DatatypeDefinitionComplex")
ExchangeFile_AttributeValueComplex = Class(name="ExchangeFile_AttributeValueComplex")
rif11a_ExchangeFile_DatatypeDefinitionComplex = Class(name="rif11a_ExchangeFile_DatatypeDefinitionComplex", is_abstract=True)
DatatypeDefinition = Class(name="DatatypeDefinition")
rif11a_ExchangeFile_AttributeValueComplex = Class(name="rif11a_ExchangeFile_AttributeValueComplex", is_abstract=True)
AttributeValue = Class(name="AttributeValue")
rif11a_ExchangeFile_AttributeDefinitionEnumeration = Class(name="rif11a_ExchangeFile_AttributeDefinitionEnumeration")
ExchangeFile_SpecGroup = Class(name="ExchangeFile_SpecGroup")
rif11a_ExchangeFile_SpecRelation = Class(name="rif11a_ExchangeFile_SpecRelation")
rif11a_ExchangeFile_DatatypeDefinition = Class(name="rif11a_ExchangeFile_DatatypeDefinition", is_abstract=True)
rif11a_ExchangeFile_AccessPolicy = Class(name="rif11a_ExchangeFile_AccessPolicy")
ExchangeFile_DatatypeDefinition = Class(name="ExchangeFile_DatatypeDefinition")
ExchangeFile_DatatypeDefinitionSimple = Class(name="ExchangeFile_DatatypeDefinitionSimple")
ExchangeFile_AttributeValueSimple = Class(name="ExchangeFile_AttributeValueSimple")
rif11a_ExchangeFile_DatatypeDefinitionSimple = Class(name="rif11a_ExchangeFile_DatatypeDefinitionSimple", is_abstract=True)
rif11a_ExchangeFile_AttributeValueSimple = Class(name="rif11a_ExchangeFile_AttributeValueSimple")
ExchangeFile_AttributeDefinitionSimple = Class(name="ExchangeFile_AttributeDefinitionSimple")
rif11a_ExchangeFile_AttributeValueEmbeddedDocument = Class(name="rif11a_ExchangeFile_AttributeValueEmbeddedDocument")
AttributeValueComplex = Class(name="AttributeValueComplex")
ExchangeFile_AttributeDefinitionComplex = Class(name="ExchangeFile_AttributeDefinitionComplex")
DataTypes_XhtmlContent = Class(name="DataTypes_XhtmlContent")
rif11a_ExchangeFile_AttributeValueEmbeddedFile = Class(name="rif11a_ExchangeFile_AttributeValueEmbeddedFile")
ExchangeFile_DatatypeDefinitionEnumeration = Class(name="ExchangeFile_DatatypeDefinitionEnumeration")
ExchangeFile_AttributeValueEnumeration = Class(name="ExchangeFile_AttributeValueEnumeration")
rif11a_ExchangeFile_DatatypeDefinitionEnumeration = Class(name="rif11a_ExchangeFile_DatatypeDefinitionEnumeration")
ExchangeFile_EnumValue = Class(name="ExchangeFile_EnumValue")
rif11a_ExchangeFile_EnumValue = Class(name="rif11a_ExchangeFile_EnumValue")
ExchangeFile_EmbeddedValue = Class(name="ExchangeFile_EmbeddedValue")
rif11a_ExchangeFile_EmbeddedValue = Class(name="rif11a_ExchangeFile_EmbeddedValue")
rif11a_ExchangeFile_AttributeValueEnumeration = Class(name="rif11a_ExchangeFile_AttributeValueEnumeration")
ExchangeFile_AttributeDefinitionEnumeration = Class(name="ExchangeFile_AttributeDefinitionEnumeration")
rif11a_ExchangeFile_AttributeDefinitionSimple = Class(name="rif11a_ExchangeFile_AttributeDefinitionSimple")
rif11a_ExchangeFile_DatatypeDefinitionInteger = Class(name="rif11a_ExchangeFile_DatatypeDefinitionInteger")
rif11a_ExchangeFile_DatatypeDefinitionReal = Class(name="rif11a_ExchangeFile_DatatypeDefinitionReal")
rif11a_ExchangeFile_DatatypeDefinitionString = Class(name="rif11a_ExchangeFile_DatatypeDefinitionString")
rif11a_ExchangeFile_DatatypeDefinitionXmlData = Class(name="rif11a_ExchangeFile_DatatypeDefinitionXmlData")
rif11a_ExchangeFile_RIF = Class(name="rif11a_ExchangeFile_RIF")
DataTypes_BinaryContent = Class(name="DataTypes_BinaryContent")
rif11a_ExchangeFile_AttributeValueFileReference = Class(name="rif11a_ExchangeFile_AttributeValueFileReference")
rif11a_ExchangeFile_AttributeValueXmlData = Class(name="rif11a_ExchangeFile_AttributeValueXmlData")
DataTypes_XmlContent = Class(name="DataTypes_XmlContent")
rif11a_ExchangeFile_DatatypeDefinitionBinaryFile = Class(name="rif11a_ExchangeFile_DatatypeDefinitionBinaryFile")
DatatypeDefinitionComplex = Class(name="DatatypeDefinitionComplex")
rif11a_ExchangeFile_DatatypeDefinitionBoolean = Class(name="rif11a_ExchangeFile_DatatypeDefinitionBoolean")
DatatypeDefinitionSimple = Class(name="DatatypeDefinitionSimple")
rif11a_ExchangeFile_DatatypeDefinitionDate = Class(name="rif11a_ExchangeFile_DatatypeDefinitionDate")
rif11a_ExchangeFile_DatatypeDefinitionDocument = Class(name="rif11a_ExchangeFile_DatatypeDefinitionDocument")
rif11a_DataTypes_XmlContent = Class(name="rif11a_DataTypes_XmlContent")
rif11a_DataTypes_XhtmlContent = Class(name="rif11a_DataTypes_XhtmlContent")
ExchangeFile_AccessPolicy = Class(name="ExchangeFile_AccessPolicy")
rif11a_DataTypes_BinaryContent = Class(name="rif11a_DataTypes_BinaryContent")

# rif11a_ExchangeFile_SpecHierarchyRoot class attributes and methods

# SpecElementWithUserDefinedAttributes class attributes and methods

# rif11a_ExchangeFile_SpecHierarchy class attributes and methods

# ExchangeFile_SpecObject class attributes and methods

# rif11a_ExchangeFile_SpecObject class attributes and methods

# rif11a_ExchangeFile_SpecGroup class attributes and methods

# ExchangeFile_RelationGroup class attributes and methods

# rif11a_ExchangeFile_RelationGroup class attributes and methods

# ExchangeFile_SpecRelation class attributes and methods

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
rif11a_ExchangeFile_Identifiable.attributes={rif11a_ExchangeFile_Identifiable_identifier, rif11a_ExchangeFile_Identifiable_desc, rif11a_ExchangeFile_Identifiable_lastChange, rif11a_ExchangeFile_Identifiable_longName}

# rif11a_ExchangeFile_SpecType class attributes and methods

# ExchangeFile_AttributeDefinition class attributes and methods

# rif11a_ExchangeFile_AttributeDefinition class attributes and methods

# rif11a_ExchangeFile_AttributeValue class attributes and methods

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

# ExchangeFile_SpecGroup class attributes and methods

# rif11a_ExchangeFile_SpecRelation class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinition class attributes and methods

# rif11a_ExchangeFile_AccessPolicy class attributes and methods
rif11a_ExchangeFile_AccessPolicy_accessMode: Property = Property(name="accessMode", type=StringType)
rif11a_ExchangeFile_AccessPolicy.attributes={rif11a_ExchangeFile_AccessPolicy_accessMode}

# ExchangeFile_DatatypeDefinition class attributes and methods

# ExchangeFile_DatatypeDefinitionSimple class attributes and methods

# ExchangeFile_AttributeValueSimple class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionSimple class attributes and methods

# rif11a_ExchangeFile_AttributeValueSimple class attributes and methods
rif11a_ExchangeFile_AttributeValueSimple_theValue: Property = Property(name="theValue", type=StringType)
rif11a_ExchangeFile_AttributeValueSimple.attributes={rif11a_ExchangeFile_AttributeValueSimple_theValue}

# ExchangeFile_AttributeDefinitionSimple class attributes and methods

# rif11a_ExchangeFile_AttributeValueEmbeddedDocument class attributes and methods

# AttributeValueComplex class attributes and methods

# ExchangeFile_AttributeDefinitionComplex class attributes and methods

# DataTypes_XhtmlContent class attributes and methods

# rif11a_ExchangeFile_AttributeValueEmbeddedFile class attributes and methods

# ExchangeFile_DatatypeDefinitionEnumeration class attributes and methods

# ExchangeFile_AttributeValueEnumeration class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionEnumeration class attributes and methods

# ExchangeFile_EnumValue class attributes and methods

# rif11a_ExchangeFile_EnumValue class attributes and methods

# ExchangeFile_EmbeddedValue class attributes and methods

# rif11a_ExchangeFile_EmbeddedValue class attributes and methods
rif11a_ExchangeFile_EmbeddedValue_key: Property = Property(name="key", type=StringType)
rif11a_ExchangeFile_EmbeddedValue_otherContent: Property = Property(name="otherContent", type=StringType)
rif11a_ExchangeFile_EmbeddedValue.attributes={rif11a_ExchangeFile_EmbeddedValue_otherContent, rif11a_ExchangeFile_EmbeddedValue_key}

# rif11a_ExchangeFile_AttributeValueEnumeration class attributes and methods

# ExchangeFile_AttributeDefinitionEnumeration class attributes and methods

# rif11a_ExchangeFile_AttributeDefinitionSimple class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionInteger class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionInteger_max: Property = Property(name="max", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionInteger_min: Property = Property(name="min", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionInteger.attributes={rif11a_ExchangeFile_DatatypeDefinitionInteger_max, rif11a_ExchangeFile_DatatypeDefinitionInteger_min}

# rif11a_ExchangeFile_DatatypeDefinitionReal class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionReal_accuracy: Property = Property(name="accuracy", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionReal_max: Property = Property(name="max", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionReal_min: Property = Property(name="min", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionReal.attributes={rif11a_ExchangeFile_DatatypeDefinitionReal_min, rif11a_ExchangeFile_DatatypeDefinitionReal_max, rif11a_ExchangeFile_DatatypeDefinitionReal_accuracy}

# rif11a_ExchangeFile_DatatypeDefinitionString class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionString_maxLength: Property = Property(name="maxLength", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionString.attributes={rif11a_ExchangeFile_DatatypeDefinitionString_maxLength}

# rif11a_ExchangeFile_DatatypeDefinitionXmlData class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionXmlData_nameSpaceURI: Property = Property(name="nameSpaceURI", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionXmlData_schemaLocation: Property = Property(name="schemaLocation", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionXmlData.attributes={rif11a_ExchangeFile_DatatypeDefinitionXmlData_schemaLocation, rif11a_ExchangeFile_DatatypeDefinitionXmlData_nameSpaceURI}

# rif11a_ExchangeFile_RIF class attributes and methods
rif11a_ExchangeFile_RIF_author: Property = Property(name="author", type=StringType)
rif11a_ExchangeFile_RIF_comment: Property = Property(name="comment", type=StringType)
rif11a_ExchangeFile_RIF_countryCode: Property = Property(name="countryCode", type=StringType)
rif11a_ExchangeFile_RIF_creationTime: Property = Property(name="creationTime", type=StringType)
rif11a_ExchangeFile_RIF_identifier: Property = Property(name="identifier", type=StringType)
rif11a_ExchangeFile_RIF_sourceToolId: Property = Property(name="sourceToolId", type=StringType)
rif11a_ExchangeFile_RIF_title: Property = Property(name="title", type=StringType)
rif11a_ExchangeFile_RIF_version: Property = Property(name="version", type=StringType)
rif11a_ExchangeFile_RIF.attributes={rif11a_ExchangeFile_RIF_title, rif11a_ExchangeFile_RIF_creationTime, rif11a_ExchangeFile_RIF_identifier, rif11a_ExchangeFile_RIF_comment, rif11a_ExchangeFile_RIF_author, rif11a_ExchangeFile_RIF_sourceToolId, rif11a_ExchangeFile_RIF_countryCode, rif11a_ExchangeFile_RIF_version}

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
rif11a_ExchangeFile_DatatypeDefinitionBinaryFile.attributes={rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_filenameSuffix, rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_formatName, rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_mimeType, rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_application}

# DatatypeDefinitionComplex class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionBoolean class attributes and methods

# DatatypeDefinitionSimple class attributes and methods

# rif11a_ExchangeFile_DatatypeDefinitionDate class attributes and methods
rif11a_ExchangeFile_DatatypeDefinitionDate_format: Property = Property(name="format", type=StringType)
rif11a_ExchangeFile_DatatypeDefinitionDate.attributes={rif11a_ExchangeFile_DatatypeDefinitionDate_format}

# rif11a_ExchangeFile_DatatypeDefinitionDocument class attributes and methods

# rif11a_DataTypes_XmlContent class attributes and methods

# rif11a_DataTypes_XhtmlContent class attributes and methods

# ExchangeFile_AccessPolicy class attributes and methods

# rif11a_DataTypes_BinaryContent class attributes and methods

# Relationships
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
relationGroups11: BinaryAssociation = BinaryAssociation(
    name="relationGroups11",
    ends={
        Property(name="RelationGroup", type=rif11a_ExchangeFile_SpecGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceGroup", type=ExchangeFile_RelationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
specHierarchies39: BinaryAssociation = BinaryAssociation(
    name="specHierarchies39",
    ends={
        Property(name="ExchangeFile_SpecHierarchy41", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy40", type=ExchangeFile_SpecHierarchy, multiplicity=Multiplicity(0, 9999))
    }
)
specObjects42: BinaryAssociation = BinaryAssociation(
    name="specObjects42",
    ends={
        Property(name="ExchangeFile_SpecObject44", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy43", type=ExchangeFile_SpecObject, multiplicity=Multiplicity(0, 9999))
    }
)
specHierarchyRoots45: BinaryAssociation = BinaryAssociation(
    name="specHierarchyRoots45",
    ends={
        Property(name="ExchangeFile_SpecHierarchyRoot", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy46", type=ExchangeFile_SpecHierarchyRoot, multiplicity=Multiplicity(0, 9999))
    }
)
type47: BinaryAssociation = BinaryAssociation(
    name="type47",
    ends={
        Property(name="ExchangeFile_DatatypeDefinitionComplex", type=rif11a_ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionComplex", type=ExchangeFile_DatatypeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue48: BinaryAssociation = BinaryAssociation(
    name="defaultValue48",
    ends={
        Property(name="ExchangeFile_AttributeValueComplex", type=rif11a_ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionComplex49", type=ExchangeFile_AttributeValueComplex, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sourceGroup16: BinaryAssociation = BinaryAssociation(
    name="sourceGroup16",
    ends={
        Property(name="SpecGroup", type=rif11a_ExchangeFile_RelationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="relationGroups", type=ExchangeFile_SpecGroup, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="ExchangeFile_SpecObject18", type=rif11a_ExchangeFile_SpecRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecRelation", type=ExchangeFile_SpecObject, multiplicity=Multiplicity(1, 1))
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="ExchangeFile_SpecObject21", type=rif11a_ExchangeFile_SpecRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_SpecRelation20", type=ExchangeFile_SpecObject, multiplicity=Multiplicity(1, 1))
    }
)
specGroups22: BinaryAssociation = BinaryAssociation(
    name="specGroups22",
    ends={
        Property(name="ExchangeFile_SpecGroup", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy", type=ExchangeFile_SpecGroup, multiplicity=Multiplicity(0, 9999))
    }
)
attributeDefinitions23: BinaryAssociation = BinaryAssociation(
    name="attributeDefinitions23",
    ends={
        Property(name="ExchangeFile_AttributeDefinition25", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy24", type=ExchangeFile_AttributeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
relationGroups26: BinaryAssociation = BinaryAssociation(
    name="relationGroups26",
    ends={
        Property(name="ExchangeFile_RelationGroup", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy27", type=ExchangeFile_RelationGroup, multiplicity=Multiplicity(0, 9999))
    }
)
datatypeDefinitions28: BinaryAssociation = BinaryAssociation(
    name="datatypeDefinitions28",
    ends={
        Property(name="ExchangeFile_DatatypeDefinition", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy29", type=ExchangeFile_DatatypeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
specRelations30: BinaryAssociation = BinaryAssociation(
    name="specRelations30",
    ends={
        Property(name="ExchangeFile_SpecRelation32", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy31", type=ExchangeFile_SpecRelation, multiplicity=Multiplicity(0, 9999))
    }
)
attributeValues33: BinaryAssociation = BinaryAssociation(
    name="attributeValues33",
    ends={
        Property(name="ExchangeFile_AttributeValue35", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy34", type=ExchangeFile_AttributeValue, multiplicity=Multiplicity(0, 9999))
    }
)
specTypes36: BinaryAssociation = BinaryAssociation(
    name="specTypes36",
    ends={
        Property(name="ExchangeFile_SpecType38", type=rif11a_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AccessPolicy37", type=ExchangeFile_SpecType, multiplicity=Multiplicity(0, 9999))
    }
)
type59: BinaryAssociation = BinaryAssociation(
    name="type59",
    ends={
        Property(name="ExchangeFile_DatatypeDefinitionSimple", type=rif11a_ExchangeFile_AttributeDefinitionSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionSimple", type=ExchangeFile_DatatypeDefinitionSimple, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue60: BinaryAssociation = BinaryAssociation(
    name="defaultValue60",
    ends={
        Property(name="ExchangeFile_AttributeValueSimple", type=rif11a_ExchangeFile_AttributeDefinitionSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionSimple61", type=ExchangeFile_AttributeValueSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definition62: BinaryAssociation = BinaryAssociation(
    name="definition62",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionSimple", type=rif11a_ExchangeFile_AttributeValueSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueSimple", type=ExchangeFile_AttributeDefinitionSimple, multiplicity=Multiplicity(1, 1))
    }
)
definition63: BinaryAssociation = BinaryAssociation(
    name="definition63",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionComplex", type=rif11a_ExchangeFile_AttributeValueEmbeddedDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEmbeddedDocument", type=ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
xhtmlContent64: BinaryAssociation = BinaryAssociation(
    name="xhtmlContent64",
    ends={
        Property(name="DataTypes_XhtmlContent", type=rif11a_ExchangeFile_AttributeValueEmbeddedDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEmbeddedDocument65", type=DataTypes_XhtmlContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition66: BinaryAssociation = BinaryAssociation(
    name="definition66",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionComplex67", type=rif11a_ExchangeFile_AttributeValueEmbeddedFile, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEmbeddedFile", type=ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
type50: BinaryAssociation = BinaryAssociation(
    name="type50",
    ends={
        Property(name="ExchangeFile_DatatypeDefinitionEnumeration", type=rif11a_ExchangeFile_AttributeDefinitionEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionEnumeration", type=ExchangeFile_DatatypeDefinitionEnumeration, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue51: BinaryAssociation = BinaryAssociation(
    name="defaultValue51",
    ends={
        Property(name="ExchangeFile_AttributeValueEnumeration", type=rif11a_ExchangeFile_AttributeDefinitionEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeDefinitionEnumeration52", type=ExchangeFile_AttributeValueEnumeration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specifiedValues53: BinaryAssociation = BinaryAssociation(
    name="specifiedValues53",
    ends={
        Property(name="ExchangeFile_EnumValue", type=rif11a_ExchangeFile_DatatypeDefinitionEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_DatatypeDefinitionEnumeration", type=ExchangeFile_EnumValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties54: BinaryAssociation = BinaryAssociation(
    name="properties54",
    ends={
        Property(name="ExchangeFile_EmbeddedValue", type=rif11a_ExchangeFile_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_EnumValue", type=ExchangeFile_EmbeddedValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values55: BinaryAssociation = BinaryAssociation(
    name="values55",
    ends={
        Property(name="ExchangeFile_EnumValue56", type=rif11a_ExchangeFile_AttributeValueEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEnumeration", type=ExchangeFile_EnumValue, multiplicity=Multiplicity(0, 9999))
    }
)
definition57: BinaryAssociation = BinaryAssociation(
    name="definition57",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionEnumeration", type=rif11a_ExchangeFile_AttributeValueEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEnumeration58", type=ExchangeFile_AttributeDefinitionEnumeration, multiplicity=Multiplicity(1, 1))
    }
)
binaryContent68: BinaryAssociation = BinaryAssociation(
    name="binaryContent68",
    ends={
        Property(name="DataTypes_BinaryContent", type=rif11a_ExchangeFile_AttributeValueEmbeddedFile, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueEmbeddedFile69", type=DataTypes_BinaryContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition70: BinaryAssociation = BinaryAssociation(
    name="definition70",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionComplex71", type=rif11a_ExchangeFile_AttributeValueFileReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueFileReference", type=ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
definition72: BinaryAssociation = BinaryAssociation(
    name="definition72",
    ends={
        Property(name="ExchangeFile_AttributeDefinitionComplex73", type=rif11a_ExchangeFile_AttributeValueXmlData, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueXmlData", type=ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
xmlContent74: BinaryAssociation = BinaryAssociation(
    name="xmlContent74",
    ends={
        Property(name="DataTypes_XmlContent", type=rif11a_ExchangeFile_AttributeValueXmlData, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_AttributeValueXmlData75", type=DataTypes_XmlContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
accessPolicies76: BinaryAssociation = BinaryAssociation(
    name="accessPolicies76",
    ends={
        Property(name="ExchangeFile_AccessPolicy", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF", type=ExchangeFile_AccessPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes77: BinaryAssociation = BinaryAssociation(
    name="datatypes77",
    ends={
        Property(name="ExchangeFile_DatatypeDefinition79", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF78", type=ExchangeFile_DatatypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
SpecHierarchyRoots80: BinaryAssociation = BinaryAssociation(
    name="SpecHierarchyRoots80",
    ends={
        Property(name="ExchangeFile_SpecHierarchyRoot82", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF81", type=ExchangeFile_SpecHierarchyRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specObjects83: BinaryAssociation = BinaryAssociation(
    name="specObjects83",
    ends={
        Property(name="ExchangeFile_SpecObject85", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF84", type=ExchangeFile_SpecObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specGroups86: BinaryAssociation = BinaryAssociation(
    name="specGroups86",
    ends={
        Property(name="ExchangeFile_SpecGroup88", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF87", type=ExchangeFile_SpecGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specTypes89: BinaryAssociation = BinaryAssociation(
    name="specTypes89",
    ends={
        Property(name="ExchangeFile_SpecType91", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF90", type=ExchangeFile_SpecType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specRelations92: BinaryAssociation = BinaryAssociation(
    name="specRelations92",
    ends={
        Property(name="ExchangeFile_SpecRelation94", type=rif11a_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif11a_ExchangeFile_RIF93", type=ExchangeFile_SpecRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_rif11a_ExchangeFile_SpecHierarchyRoot_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif11a_ExchangeFile_SpecHierarchyRoot)
gen_rif11a_ExchangeFile_SpecHierarchy_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_SpecHierarchy)
gen_rif11a_ExchangeFile_SpecObject_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif11a_ExchangeFile_SpecObject)
gen_rif11a_ExchangeFile_SpecGroup_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif11a_ExchangeFile_SpecGroup)
gen_rif11a_ExchangeFile_RelationGroup_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_RelationGroup)
gen_rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes)
gen_rif11a_ExchangeFile_SpecType_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_SpecType)
gen_rif11a_ExchangeFile_AttributeDefinition_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_AttributeDefinition)
gen_rif11a_ExchangeFile_AttributeValue_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_AttributeValue)
gen_rif11a_ExchangeFile_AttributeDefinitionComplex_AttributeDefinition = Generalization(general=AttributeDefinition, specific=rif11a_ExchangeFile_AttributeDefinitionComplex)
gen_rif11a_ExchangeFile_DatatypeDefinitionComplex_DatatypeDefinition = Generalization(general=DatatypeDefinition, specific=rif11a_ExchangeFile_DatatypeDefinitionComplex)
gen_rif11a_ExchangeFile_AttributeValueComplex_AttributeValue = Generalization(general=AttributeValue, specific=rif11a_ExchangeFile_AttributeValueComplex)
gen_rif11a_ExchangeFile_AttributeDefinitionEnumeration_AttributeDefinition = Generalization(general=AttributeDefinition, specific=rif11a_ExchangeFile_AttributeDefinitionEnumeration)
gen_rif11a_ExchangeFile_SpecRelation_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif11a_ExchangeFile_SpecRelation)
gen_rif11a_ExchangeFile_DatatypeDefinition_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_DatatypeDefinition)
gen_rif11a_ExchangeFile_AccessPolicy_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_AccessPolicy)
gen_rif11a_ExchangeFile_DatatypeDefinitionSimple_DatatypeDefinition = Generalization(general=DatatypeDefinition, specific=rif11a_ExchangeFile_DatatypeDefinitionSimple)
gen_rif11a_ExchangeFile_AttributeValueSimple_AttributeValue = Generalization(general=AttributeValue, specific=rif11a_ExchangeFile_AttributeValueSimple)
gen_rif11a_ExchangeFile_AttributeValueEmbeddedDocument_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif11a_ExchangeFile_AttributeValueEmbeddedDocument)
gen_rif11a_ExchangeFile_AttributeValueEmbeddedFile_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif11a_ExchangeFile_AttributeValueEmbeddedFile)
gen_rif11a_ExchangeFile_DatatypeDefinitionEnumeration_DatatypeDefinition = Generalization(general=DatatypeDefinition, specific=rif11a_ExchangeFile_DatatypeDefinitionEnumeration)
gen_rif11a_ExchangeFile_EnumValue_Identifiable = Generalization(general=Identifiable, specific=rif11a_ExchangeFile_EnumValue)
gen_rif11a_ExchangeFile_AttributeValueEnumeration_AttributeValue = Generalization(general=AttributeValue, specific=rif11a_ExchangeFile_AttributeValueEnumeration)
gen_rif11a_ExchangeFile_AttributeDefinitionSimple_AttributeDefinition = Generalization(general=AttributeDefinition, specific=rif11a_ExchangeFile_AttributeDefinitionSimple)
gen_rif11a_ExchangeFile_DatatypeDefinitionInteger_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif11a_ExchangeFile_DatatypeDefinitionInteger)
gen_rif11a_ExchangeFile_DatatypeDefinitionReal_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif11a_ExchangeFile_DatatypeDefinitionReal)
gen_rif11a_ExchangeFile_DatatypeDefinitionString_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif11a_ExchangeFile_DatatypeDefinitionString)
gen_rif11a_ExchangeFile_DatatypeDefinitionXmlData_DatatypeDefinitionComplex = Generalization(general=DatatypeDefinitionComplex, specific=rif11a_ExchangeFile_DatatypeDefinitionXmlData)
gen_rif11a_ExchangeFile_AttributeValueFileReference_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif11a_ExchangeFile_AttributeValueFileReference)
gen_rif11a_ExchangeFile_AttributeValueXmlData_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif11a_ExchangeFile_AttributeValueXmlData)
gen_rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_DatatypeDefinitionComplex = Generalization(general=DatatypeDefinitionComplex, specific=rif11a_ExchangeFile_DatatypeDefinitionBinaryFile)
gen_rif11a_ExchangeFile_DatatypeDefinitionBoolean_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif11a_ExchangeFile_DatatypeDefinitionBoolean)
gen_rif11a_ExchangeFile_DatatypeDefinitionDate_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif11a_ExchangeFile_DatatypeDefinitionDate)
gen_rif11a_ExchangeFile_DatatypeDefinitionDocument_DatatypeDefinitionComplex = Generalization(general=DatatypeDefinitionComplex, specific=rif11a_ExchangeFile_DatatypeDefinitionDocument)

# Domain Model
domain_model = DomainModel(
    name="rif11a",
    types={rif11a_ExchangeFile_SpecHierarchyRoot, SpecElementWithUserDefinedAttributes, rif11a_ExchangeFile_SpecHierarchy, ExchangeFile_SpecObject, rif11a_ExchangeFile_SpecObject, rif11a_ExchangeFile_SpecGroup, ExchangeFile_RelationGroup, rif11a_ExchangeFile_RelationGroup, ExchangeFile_SpecRelation, ExchangeFile_SpecHierarchy, rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes, Identifiable, ExchangeFile_SpecType, ExchangeFile_AttributeValue, rif11a_ExchangeFile_Identifiable, rif11a_ExchangeFile_SpecType, ExchangeFile_AttributeDefinition, rif11a_ExchangeFile_AttributeDefinition, rif11a_ExchangeFile_AttributeValue, ExchangeFile_SpecHierarchyRoot, rif11a_ExchangeFile_AttributeDefinitionComplex, AttributeDefinition, ExchangeFile_DatatypeDefinitionComplex, ExchangeFile_AttributeValueComplex, rif11a_ExchangeFile_DatatypeDefinitionComplex, DatatypeDefinition, rif11a_ExchangeFile_AttributeValueComplex, AttributeValue, rif11a_ExchangeFile_AttributeDefinitionEnumeration, ExchangeFile_SpecGroup, rif11a_ExchangeFile_SpecRelation, rif11a_ExchangeFile_DatatypeDefinition, rif11a_ExchangeFile_AccessPolicy, ExchangeFile_DatatypeDefinition, ExchangeFile_DatatypeDefinitionSimple, ExchangeFile_AttributeValueSimple, rif11a_ExchangeFile_DatatypeDefinitionSimple, rif11a_ExchangeFile_AttributeValueSimple, ExchangeFile_AttributeDefinitionSimple, rif11a_ExchangeFile_AttributeValueEmbeddedDocument, AttributeValueComplex, ExchangeFile_AttributeDefinitionComplex, DataTypes_XhtmlContent, rif11a_ExchangeFile_AttributeValueEmbeddedFile, ExchangeFile_DatatypeDefinitionEnumeration, ExchangeFile_AttributeValueEnumeration, rif11a_ExchangeFile_DatatypeDefinitionEnumeration, ExchangeFile_EnumValue, rif11a_ExchangeFile_EnumValue, ExchangeFile_EmbeddedValue, rif11a_ExchangeFile_EmbeddedValue, rif11a_ExchangeFile_AttributeValueEnumeration, ExchangeFile_AttributeDefinitionEnumeration, rif11a_ExchangeFile_AttributeDefinitionSimple, rif11a_ExchangeFile_DatatypeDefinitionInteger, rif11a_ExchangeFile_DatatypeDefinitionReal, rif11a_ExchangeFile_DatatypeDefinitionString, rif11a_ExchangeFile_DatatypeDefinitionXmlData, rif11a_ExchangeFile_RIF, DataTypes_BinaryContent, rif11a_ExchangeFile_AttributeValueFileReference, rif11a_ExchangeFile_AttributeValueXmlData, DataTypes_XmlContent, rif11a_ExchangeFile_DatatypeDefinitionBinaryFile, DatatypeDefinitionComplex, rif11a_ExchangeFile_DatatypeDefinitionBoolean, DatatypeDefinitionSimple, rif11a_ExchangeFile_DatatypeDefinitionDate, rif11a_ExchangeFile_DatatypeDefinitionDocument, rif11a_DataTypes_XmlContent, rif11a_DataTypes_XhtmlContent, ExchangeFile_AccessPolicy, rif11a_DataTypes_BinaryContent, AccessPolicyAccessModeEnum, DatatypeDefinitionDateFormatEnum},
    associations={object5, children6, specObjects9, relationGroups11, specRelations12, relationType13, children0, type1, values2, specAttributes4, specHierarchies39, specObjects42, specHierarchyRoots45, type47, defaultValue48, sourceGroup16, target17, source19, specGroups22, attributeDefinitions23, relationGroups26, datatypeDefinitions28, specRelations30, attributeValues33, specTypes36, type59, defaultValue60, definition62, definition63, xhtmlContent64, definition66, type50, defaultValue51, specifiedValues53, properties54, values55, definition57, binaryContent68, definition70, definition72, xmlContent74, accessPolicies76, datatypes77, SpecHierarchyRoots80, specObjects83, specGroups86, specTypes89, specRelations92},
    generalizations={gen_rif11a_ExchangeFile_SpecHierarchyRoot_SpecElementWithUserDefinedAttributes, gen_rif11a_ExchangeFile_SpecHierarchy_Identifiable, gen_rif11a_ExchangeFile_SpecObject_SpecElementWithUserDefinedAttributes, gen_rif11a_ExchangeFile_SpecGroup_SpecElementWithUserDefinedAttributes, gen_rif11a_ExchangeFile_RelationGroup_Identifiable, gen_rif11a_ExchangeFile_SpecElementWithUserDefinedAttributes_Identifiable, gen_rif11a_ExchangeFile_SpecType_Identifiable, gen_rif11a_ExchangeFile_AttributeDefinition_Identifiable, gen_rif11a_ExchangeFile_AttributeValue_Identifiable, gen_rif11a_ExchangeFile_AttributeDefinitionComplex_AttributeDefinition, gen_rif11a_ExchangeFile_DatatypeDefinitionComplex_DatatypeDefinition, gen_rif11a_ExchangeFile_AttributeValueComplex_AttributeValue, gen_rif11a_ExchangeFile_AttributeDefinitionEnumeration_AttributeDefinition, gen_rif11a_ExchangeFile_SpecRelation_SpecElementWithUserDefinedAttributes, gen_rif11a_ExchangeFile_DatatypeDefinition_Identifiable, gen_rif11a_ExchangeFile_AccessPolicy_Identifiable, gen_rif11a_ExchangeFile_DatatypeDefinitionSimple_DatatypeDefinition, gen_rif11a_ExchangeFile_AttributeValueSimple_AttributeValue, gen_rif11a_ExchangeFile_AttributeValueEmbeddedDocument_AttributeValueComplex, gen_rif11a_ExchangeFile_AttributeValueEmbeddedFile_AttributeValueComplex, gen_rif11a_ExchangeFile_DatatypeDefinitionEnumeration_DatatypeDefinition, gen_rif11a_ExchangeFile_EnumValue_Identifiable, gen_rif11a_ExchangeFile_AttributeValueEnumeration_AttributeValue, gen_rif11a_ExchangeFile_AttributeDefinitionSimple_AttributeDefinition, gen_rif11a_ExchangeFile_DatatypeDefinitionInteger_DatatypeDefinitionSimple, gen_rif11a_ExchangeFile_DatatypeDefinitionReal_DatatypeDefinitionSimple, gen_rif11a_ExchangeFile_DatatypeDefinitionString_DatatypeDefinitionSimple, gen_rif11a_ExchangeFile_DatatypeDefinitionXmlData_DatatypeDefinitionComplex, gen_rif11a_ExchangeFile_AttributeValueFileReference_AttributeValueComplex, gen_rif11a_ExchangeFile_AttributeValueXmlData_AttributeValueComplex, gen_rif11a_ExchangeFile_DatatypeDefinitionBinaryFile_DatatypeDefinitionComplex, gen_rif11a_ExchangeFile_DatatypeDefinitionBoolean_DatatypeDefinitionSimple, gen_rif11a_ExchangeFile_DatatypeDefinitionDate_DatatypeDefinitionSimple, gen_rif11a_ExchangeFile_DatatypeDefinitionDocument_DatatypeDefinitionComplex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)