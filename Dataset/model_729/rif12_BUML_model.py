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
rif12_ExchangeFile_SpecHierarchyRoot = Class(name="rif12::ExchangeFile::SpecHierarchyRoot")
SpecElementWithUserDefinedAttributes = Class(name="SpecElementWithUserDefinedAttributes")
AttributeValue = Class(name="AttributeValue")
rif12_ExchangeFile_Identifiable = Class(name="rif12::ExchangeFile::Identifiable", is_abstract=True)
rif12_ExchangeFile_SpecType = Class(name="rif12::ExchangeFile::SpecType")
AttributeDefinition = Class(name="AttributeDefinition")
SpecHierarchy = Class(name="SpecHierarchy")
rif12_ExchangeFile_SpecElementWithUserDefinedAttributes = Class(name="rif12::ExchangeFile::SpecElementWithUserDefinedAttributes", is_abstract=True)
Identifiable = Class(name="Identifiable")
SpecType = Class(name="SpecType")
rif12_ExchangeFile_SpecHierarchy = Class(name="rif12::ExchangeFile::SpecHierarchy")
SpecObject = Class(name="SpecObject")
rif12_ExchangeFile_SpecObject = Class(name="rif12::ExchangeFile::SpecObject")
rif12_ExchangeFile_SpecGroup = Class(name="rif12::ExchangeFile::SpecGroup")
rif12_ExchangeFile_AttributeDefinition = Class(name="rif12::ExchangeFile::AttributeDefinition", is_abstract=True)
rif12_ExchangeFile_AttributeValue = Class(name="rif12::ExchangeFile::AttributeValue", is_abstract=True)
SpecRelation = Class(name="SpecRelation")
RelationGroup = Class(name="RelationGroup")
rif12_ExchangeFile_RelationGroup = Class(name="rif12::ExchangeFile::RelationGroup")
rif12_ExchangeFile_SpecRelation = Class(name="rif12::ExchangeFile::SpecRelation")
rif12_ExchangeFile_DatatypeDefinition = Class(name="rif12::ExchangeFile::DatatypeDefinition", is_abstract=True)
rif12_ExchangeFile_AccessPolicy = Class(name="rif12::ExchangeFile::AccessPolicy")
SpecGroupHierarchyRoot = Class(name="SpecGroupHierarchyRoot")
SpecGroup = Class(name="SpecGroup")
DatatypeDefinition = Class(name="DatatypeDefinition")
SpecHierarchyRoot = Class(name="SpecHierarchyRoot")
rif12_ExchangeFile_SpecGroupHierarchyRoot = Class(name="rif12::ExchangeFile::SpecGroupHierarchyRoot")
rif12_ExchangeFile_SpecGroupHierarchy = Class(name="rif12::ExchangeFile::SpecGroupHierarchy")
rif12_ExchangeFile_AttributeDefinitionComplex = Class(name="rif12::ExchangeFile::AttributeDefinitionComplex")
DatatypeDefinitionComplex = Class(name="DatatypeDefinitionComplex")
SpecGroupHierarchy = Class(name="SpecGroupHierarchy")
rif12_ExchangeFile_AttributeValueComplex = Class(name="rif12::ExchangeFile::AttributeValueComplex", is_abstract=True)
rif12_ExchangeFile_AttributeDefinitionEnumeration = Class(name="rif12::ExchangeFile::AttributeDefinitionEnumeration")
DatatypeDefinitionEnumeration = Class(name="DatatypeDefinitionEnumeration")
AttributeValueEnumeration = Class(name="AttributeValueEnumeration")
AttributeValueComplex = Class(name="AttributeValueComplex")
rif12_ExchangeFile_DatatypeDefinitionComplex = Class(name="rif12::ExchangeFile::DatatypeDefinitionComplex", is_abstract=True)
rif12_ExchangeFile_EnumValue = Class(name="rif12::ExchangeFile::EnumValue")
EmbeddedValue = Class(name="EmbeddedValue")
rif12_ExchangeFile_EmbeddedValue = Class(name="rif12::ExchangeFile::EmbeddedValue")
rif12_ExchangeFile_DatatypeDefinitionEnumeration = Class(name="rif12::ExchangeFile::DatatypeDefinitionEnumeration")
EnumValue = Class(name="EnumValue")
AttributeDefinitionEnumeration = Class(name="AttributeDefinitionEnumeration")
rif12_ExchangeFile_AttributeDefinitionSimple = Class(name="rif12::ExchangeFile::AttributeDefinitionSimple")
DatatypeDefinitionSimple = Class(name="DatatypeDefinitionSimple")
AttributeValueSimple = Class(name="AttributeValueSimple")
rif12_ExchangeFile_DatatypeDefinitionSimple = Class(name="rif12::ExchangeFile::DatatypeDefinitionSimple", is_abstract=True)
rif12_ExchangeFile_AttributeValueSimple = Class(name="rif12::ExchangeFile::AttributeValueSimple")
rif12_ExchangeFile_AttributeValueEnumeration = Class(name="rif12::ExchangeFile::AttributeValueEnumeration")
AttributeDefinitionComplex = Class(name="AttributeDefinitionComplex")
DataTypes_XhtmlContent = Class(name="DataTypes::XhtmlContent")
rif12_ExchangeFile_AttributeValueEmbeddedFile = Class(name="rif12::ExchangeFile::AttributeValueEmbeddedFile")
DataTypes_BinaryContent = Class(name="DataTypes::BinaryContent")
rif12_ExchangeFile_AttributeValueFileReference = Class(name="rif12::ExchangeFile::AttributeValueFileReference")
AttributeDefinitionSimple = Class(name="AttributeDefinitionSimple")
rif12_ExchangeFile_AttributeValueEmbeddedDocument = Class(name="rif12::ExchangeFile::AttributeValueEmbeddedDocument")
rif12_ExchangeFile_AttributeValueXmlData = Class(name="rif12::ExchangeFile::AttributeValueXmlData")
DataTypes_XmlContent = Class(name="DataTypes::XmlContent")
rif12_ExchangeFile_DatatypeDefinitionBinaryFile = Class(name="rif12::ExchangeFile::DatatypeDefinitionBinaryFile")
rif12_ExchangeFile_DatatypeDefinitionBoolean = Class(name="rif12::ExchangeFile::DatatypeDefinitionBoolean")
rif12_ExchangeFile_DatatypeDefinitionInteger = Class(name="rif12::ExchangeFile::DatatypeDefinitionInteger")
rif12_ExchangeFile_DatatypeDefinitionReal = Class(name="rif12::ExchangeFile::DatatypeDefinitionReal")
rif12_ExchangeFile_DatatypeDefinitionString = Class(name="rif12::ExchangeFile::DatatypeDefinitionString")
rif12_ExchangeFile_DatatypeDefinitionXmlData = Class(name="rif12::ExchangeFile::DatatypeDefinitionXmlData")
rif12_ExchangeFile_DatatypeDefinitionDate = Class(name="rif12::ExchangeFile::DatatypeDefinitionDate")
rif12_ExchangeFile_DatatypeDefinitionDocument = Class(name="rif12::ExchangeFile::DatatypeDefinitionDocument")
RIFContent = Class(name="RIFContent")
RIFToolExtension = Class(name="RIFToolExtension")
rif12_ExchangeFile_RIFHeader = Class(name="rif12::ExchangeFile::RIFHeader")
rif12_ExchangeFile_RIF = Class(name="rif12::ExchangeFile::RIF")
RIFHeader = Class(name="RIFHeader")
rif12_ExchangeFile_RIFContent = Class(name="rif12::ExchangeFile::RIFContent")
AccessPolicy = Class(name="AccessPolicy")
rif12_DataTypes_XhtmlContent = Class(name="rif12::DataTypes::XhtmlContent")
rif12_DataTypes_XmlContent = Class(name="rif12::DataTypes::XmlContent")
rif12_ExchangeFile_RIFToolExtension = Class(name="rif12::ExchangeFile::RIFToolExtension")
rif12_DataTypes_BinaryContent = Class(name="rif12::DataTypes::BinaryContent")

# rif12_ExchangeFile_SpecHierarchyRoot class attributes and methods

# SpecElementWithUserDefinedAttributes class attributes and methods

# AttributeValue class attributes and methods

# rif12_ExchangeFile_Identifiable class attributes and methods
rif12_ExchangeFile_Identifiable_desc: Property = Property(name="desc", type=StringType)
rif12_ExchangeFile_Identifiable_identifier: Property = Property(name="identifier", type=StringType)
rif12_ExchangeFile_Identifiable_lastChange: Property = Property(name="lastChange", type=StringType)
rif12_ExchangeFile_Identifiable_longName: Property = Property(name="longName", type=StringType)
rif12_ExchangeFile_Identifiable.attributes={rif12_ExchangeFile_Identifiable_longName, rif12_ExchangeFile_Identifiable_identifier, rif12_ExchangeFile_Identifiable_lastChange, rif12_ExchangeFile_Identifiable_desc}

# rif12_ExchangeFile_SpecType class attributes and methods

# AttributeDefinition class attributes and methods

# SpecHierarchy class attributes and methods

# rif12_ExchangeFile_SpecElementWithUserDefinedAttributes class attributes and methods

# Identifiable class attributes and methods

# SpecType class attributes and methods

# rif12_ExchangeFile_SpecHierarchy class attributes and methods

# SpecObject class attributes and methods

# rif12_ExchangeFile_SpecObject class attributes and methods

# rif12_ExchangeFile_SpecGroup class attributes and methods

# rif12_ExchangeFile_AttributeDefinition class attributes and methods

# rif12_ExchangeFile_AttributeValue class attributes and methods

# SpecRelation class attributes and methods

# RelationGroup class attributes and methods

# rif12_ExchangeFile_RelationGroup class attributes and methods

# rif12_ExchangeFile_SpecRelation class attributes and methods

# rif12_ExchangeFile_DatatypeDefinition class attributes and methods

# rif12_ExchangeFile_AccessPolicy class attributes and methods
rif12_ExchangeFile_AccessPolicy_accessMode: Property = Property(name="accessMode", type=StringType)
rif12_ExchangeFile_AccessPolicy.attributes={rif12_ExchangeFile_AccessPolicy_accessMode}

# SpecGroupHierarchyRoot class attributes and methods

# SpecGroup class attributes and methods

# DatatypeDefinition class attributes and methods

# SpecHierarchyRoot class attributes and methods

# rif12_ExchangeFile_SpecGroupHierarchyRoot class attributes and methods

# rif12_ExchangeFile_SpecGroupHierarchy class attributes and methods

# rif12_ExchangeFile_AttributeDefinitionComplex class attributes and methods

# DatatypeDefinitionComplex class attributes and methods

# SpecGroupHierarchy class attributes and methods

# rif12_ExchangeFile_AttributeValueComplex class attributes and methods

# rif12_ExchangeFile_AttributeDefinitionEnumeration class attributes and methods
rif12_ExchangeFile_AttributeDefinitionEnumeration_multiValued: Property = Property(name="multiValued", type=StringType)
rif12_ExchangeFile_AttributeDefinitionEnumeration.attributes={rif12_ExchangeFile_AttributeDefinitionEnumeration_multiValued}

# DatatypeDefinitionEnumeration class attributes and methods

# AttributeValueEnumeration class attributes and methods

# AttributeValueComplex class attributes and methods

# rif12_ExchangeFile_DatatypeDefinitionComplex class attributes and methods
rif12_ExchangeFile_DatatypeDefinitionComplex_embedded: Property = Property(name="embedded", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionComplex.attributes={rif12_ExchangeFile_DatatypeDefinitionComplex_embedded}

# rif12_ExchangeFile_EnumValue class attributes and methods

# EmbeddedValue class attributes and methods

# rif12_ExchangeFile_EmbeddedValue class attributes and methods
rif12_ExchangeFile_EmbeddedValue_key: Property = Property(name="key", type=StringType)
rif12_ExchangeFile_EmbeddedValue_otherContent: Property = Property(name="otherContent", type=StringType)
rif12_ExchangeFile_EmbeddedValue.attributes={rif12_ExchangeFile_EmbeddedValue_otherContent, rif12_ExchangeFile_EmbeddedValue_key}

# rif12_ExchangeFile_DatatypeDefinitionEnumeration class attributes and methods

# EnumValue class attributes and methods

# AttributeDefinitionEnumeration class attributes and methods

# rif12_ExchangeFile_AttributeDefinitionSimple class attributes and methods

# DatatypeDefinitionSimple class attributes and methods

# AttributeValueSimple class attributes and methods

# rif12_ExchangeFile_DatatypeDefinitionSimple class attributes and methods

# rif12_ExchangeFile_AttributeValueSimple class attributes and methods
rif12_ExchangeFile_AttributeValueSimple_theValue: Property = Property(name="theValue", type=StringType)
rif12_ExchangeFile_AttributeValueSimple.attributes={rif12_ExchangeFile_AttributeValueSimple_theValue}

# rif12_ExchangeFile_AttributeValueEnumeration class attributes and methods

# AttributeDefinitionComplex class attributes and methods

# DataTypes_XhtmlContent class attributes and methods

# rif12_ExchangeFile_AttributeValueEmbeddedFile class attributes and methods

# DataTypes_BinaryContent class attributes and methods

# rif12_ExchangeFile_AttributeValueFileReference class attributes and methods
rif12_ExchangeFile_AttributeValueFileReference_pathToFile: Property = Property(name="pathToFile", type=StringType)
rif12_ExchangeFile_AttributeValueFileReference.attributes={rif12_ExchangeFile_AttributeValueFileReference_pathToFile}

# AttributeDefinitionSimple class attributes and methods

# rif12_ExchangeFile_AttributeValueEmbeddedDocument class attributes and methods

# rif12_ExchangeFile_AttributeValueXmlData class attributes and methods

# DataTypes_XmlContent class attributes and methods

# rif12_ExchangeFile_DatatypeDefinitionBinaryFile class attributes and methods
rif12_ExchangeFile_DatatypeDefinitionBinaryFile_application: Property = Property(name="application", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionBinaryFile_filenameSuffix: Property = Property(name="filenameSuffix", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionBinaryFile_formatName: Property = Property(name="formatName", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionBinaryFile_mimeType: Property = Property(name="mimeType", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionBinaryFile.attributes={rif12_ExchangeFile_DatatypeDefinitionBinaryFile_application, rif12_ExchangeFile_DatatypeDefinitionBinaryFile_filenameSuffix, rif12_ExchangeFile_DatatypeDefinitionBinaryFile_formatName, rif12_ExchangeFile_DatatypeDefinitionBinaryFile_mimeType}

# rif12_ExchangeFile_DatatypeDefinitionBoolean class attributes and methods

# rif12_ExchangeFile_DatatypeDefinitionInteger class attributes and methods
rif12_ExchangeFile_DatatypeDefinitionInteger_max: Property = Property(name="max", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionInteger_min: Property = Property(name="min", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionInteger.attributes={rif12_ExchangeFile_DatatypeDefinitionInteger_max, rif12_ExchangeFile_DatatypeDefinitionInteger_min}

# rif12_ExchangeFile_DatatypeDefinitionReal class attributes and methods
rif12_ExchangeFile_DatatypeDefinitionReal_accuracy: Property = Property(name="accuracy", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionReal_max: Property = Property(name="max", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionReal_min: Property = Property(name="min", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionReal.attributes={rif12_ExchangeFile_DatatypeDefinitionReal_accuracy, rif12_ExchangeFile_DatatypeDefinitionReal_min, rif12_ExchangeFile_DatatypeDefinitionReal_max}

# rif12_ExchangeFile_DatatypeDefinitionString class attributes and methods
rif12_ExchangeFile_DatatypeDefinitionString_maxLength: Property = Property(name="maxLength", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionString.attributes={rif12_ExchangeFile_DatatypeDefinitionString_maxLength}

# rif12_ExchangeFile_DatatypeDefinitionXmlData class attributes and methods
rif12_ExchangeFile_DatatypeDefinitionXmlData_nameSpaceURI: Property = Property(name="nameSpaceURI", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionXmlData_schemaLocation: Property = Property(name="schemaLocation", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionXmlData.attributes={rif12_ExchangeFile_DatatypeDefinitionXmlData_schemaLocation, rif12_ExchangeFile_DatatypeDefinitionXmlData_nameSpaceURI}

# rif12_ExchangeFile_DatatypeDefinitionDate class attributes and methods
rif12_ExchangeFile_DatatypeDefinitionDate_format: Property = Property(name="format", type=StringType)
rif12_ExchangeFile_DatatypeDefinitionDate.attributes={rif12_ExchangeFile_DatatypeDefinitionDate_format}

# rif12_ExchangeFile_DatatypeDefinitionDocument class attributes and methods

# RIFContent class attributes and methods

# RIFToolExtension class attributes and methods

# rif12_ExchangeFile_RIFHeader class attributes and methods
rif12_ExchangeFile_RIFHeader_author: Property = Property(name="author", type=StringType)
rif12_ExchangeFile_RIFHeader_comment: Property = Property(name="comment", type=StringType)
rif12_ExchangeFile_RIFHeader_creationTime: Property = Property(name="creationTime", type=StringType)
rif12_ExchangeFile_RIFHeader_identifier: Property = Property(name="identifier", type=StringType)
rif12_ExchangeFile_RIFHeader_sourceToolId: Property = Property(name="sourceToolId", type=StringType)
rif12_ExchangeFile_RIFHeader_title: Property = Property(name="title", type=StringType)
rif12_ExchangeFile_RIFHeader.attributes={rif12_ExchangeFile_RIFHeader_title, rif12_ExchangeFile_RIFHeader_comment, rif12_ExchangeFile_RIFHeader_creationTime, rif12_ExchangeFile_RIFHeader_author, rif12_ExchangeFile_RIFHeader_identifier, rif12_ExchangeFile_RIFHeader_sourceToolId}

# rif12_ExchangeFile_RIF class attributes and methods

# RIFHeader class attributes and methods

# rif12_ExchangeFile_RIFContent class attributes and methods

# AccessPolicy class attributes and methods

# rif12_DataTypes_XhtmlContent class attributes and methods

# rif12_DataTypes_XmlContent class attributes and methods

# rif12_ExchangeFile_RIFToolExtension class attributes and methods

# rif12_DataTypes_BinaryContent class attributes and methods

# Relationships
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="SpecType", type=rif12_ExchangeFile_SpecElementWithUserDefinedAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecElementWithUserDefinedAttributes", type=SpecType, multiplicity=Multiplicity(1, 1))
    }
)
values2: BinaryAssociation = BinaryAssociation(
    name="values2",
    ends={
        Property(name="AttributeValue", type=rif12_ExchangeFile_SpecElementWithUserDefinedAttributes, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecElementWithUserDefinedAttributes3", type=AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specAttributes4: BinaryAssociation = BinaryAssociation(
    name="specAttributes4",
    ends={
        Property(name="AttributeDefinition", type=rif12_ExchangeFile_SpecType, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecType", type=AttributeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="SpecHierarchy", type=rif12_ExchangeFile_SpecHierarchyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecHierarchyRoot", type=SpecHierarchy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
object5: BinaryAssociation = BinaryAssociation(
    name="object5",
    ends={
        Property(name="SpecObject", type=rif12_ExchangeFile_SpecHierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecHierarchy", type=SpecObject, multiplicity=Multiplicity(1, 1))
    }
)
values6: BinaryAssociation = BinaryAssociation(
    name="values6",
    ends={
        Property(name="AttributeValue8", type=rif12_ExchangeFile_SpecHierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecHierarchy7", type=AttributeValue, multiplicity=Multiplicity(0, 9999))
    }
)
children9: BinaryAssociation = BinaryAssociation(
    name="children9",
    ends={
        Property(name="SpecHierarchy11", type=rif12_ExchangeFile_SpecHierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecHierarchy10", type=SpecHierarchy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specObjects12: BinaryAssociation = BinaryAssociation(
    name="specObjects12",
    ends={
        Property(name="SpecObject13", type=rif12_ExchangeFile_SpecGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecGroup", type=SpecObject, multiplicity=Multiplicity(0, 9999))
    }
)
specRelations16: BinaryAssociation = BinaryAssociation(
    name="specRelations16",
    ends={
        Property(name="SpecRelation", type=rif12_ExchangeFile_RelationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RelationGroup", type=SpecRelation, multiplicity=Multiplicity(0, 9999))
    }
)
relationType17: BinaryAssociation = BinaryAssociation(
    name="relationType17",
    ends={
        Property(name="SpecType19", type=rif12_ExchangeFile_RelationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RelationGroup18", type=SpecType, multiplicity=Multiplicity(0, 1))
    }
)
relationGroups14: BinaryAssociation = BinaryAssociation(
    name="relationGroups14",
    ends={
        Property(name="RelationGroup", type=rif12_ExchangeFile_SpecGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecGroup15", type=RelationGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="rif12_ExchangeFile_SpecRelation", type=SpecObject, multiplicity=Multiplicity(1, 1)),
        Property(name="SpecObject21", type=rif12_ExchangeFile_SpecRelation, multiplicity=Multiplicity(1, 1))
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="SpecObject24", type=rif12_ExchangeFile_SpecRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecRelation23", type=SpecObject, multiplicity=Multiplicity(1, 1))
    }
)
specGroupHierarchyRoots25: BinaryAssociation = BinaryAssociation(
    name="specGroupHierarchyRoots25",
    ends={
        Property(name="SpecGroupHierarchyRoot", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy", type=SpecGroupHierarchyRoot, multiplicity=Multiplicity(0, 9999))
    }
)
attributeDefinitions28: BinaryAssociation = BinaryAssociation(
    name="attributeDefinitions28",
    ends={
        Property(name="AttributeDefinition30", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy29", type=AttributeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
specGroups26: BinaryAssociation = BinaryAssociation(
    name="specGroups26",
    ends={
        Property(name="SpecGroup", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy27", type=SpecGroup, multiplicity=Multiplicity(0, 9999))
    }
)
relationGroups31: BinaryAssociation = BinaryAssociation(
    name="relationGroups31",
    ends={
        Property(name="RelationGroup33", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy32", type=RelationGroup, multiplicity=Multiplicity(0, 9999))
    }
)
datatypeDefinitions34: BinaryAssociation = BinaryAssociation(
    name="datatypeDefinitions34",
    ends={
        Property(name="DatatypeDefinition", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy35", type=DatatypeDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
attributeValues39: BinaryAssociation = BinaryAssociation(
    name="attributeValues39",
    ends={
        Property(name="AttributeValue41", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy40", type=AttributeValue, multiplicity=Multiplicity(0, 9999))
    }
)
specRelations36: BinaryAssociation = BinaryAssociation(
    name="specRelations36",
    ends={
        Property(name="SpecRelation38", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy37", type=SpecRelation, multiplicity=Multiplicity(0, 9999))
    }
)
specTypes42: BinaryAssociation = BinaryAssociation(
    name="specTypes42",
    ends={
        Property(name="SpecType44", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy43", type=SpecType, multiplicity=Multiplicity(0, 9999))
    }
)
specHierarchies45: BinaryAssociation = BinaryAssociation(
    name="specHierarchies45",
    ends={
        Property(name="SpecHierarchy47", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy46", type=SpecHierarchy, multiplicity=Multiplicity(0, 9999))
    }
)
specObjects48: BinaryAssociation = BinaryAssociation(
    name="specObjects48",
    ends={
        Property(name="SpecObject50", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy49", type=SpecObject, multiplicity=Multiplicity(0, 9999))
    }
)
specHierarchyRoots51: BinaryAssociation = BinaryAssociation(
    name="specHierarchyRoots51",
    ends={
        Property(name="SpecHierarchyRoot", type=rif12_ExchangeFile_AccessPolicy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AccessPolicy52", type=SpecHierarchyRoot, multiplicity=Multiplicity(0, 9999))
    }
)
group54: BinaryAssociation = BinaryAssociation(
    name="group54",
    ends={
        Property(name="SpecGroup55", type=rif12_ExchangeFile_SpecGroupHierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecGroupHierarchy", type=SpecGroup, multiplicity=Multiplicity(1, 1))
    }
)
type56: BinaryAssociation = BinaryAssociation(
    name="type56",
    ends={
        Property(name="DatatypeDefinitionComplex", type=rif12_ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeDefinitionComplex", type=DatatypeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
children53: BinaryAssociation = BinaryAssociation(
    name="children53",
    ends={
        Property(name="SpecGroupHierarchy", type=rif12_ExchangeFile_SpecGroupHierarchyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_SpecGroupHierarchyRoot", type=SpecGroupHierarchy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type59: BinaryAssociation = BinaryAssociation(
    name="type59",
    ends={
        Property(name="DatatypeDefinitionEnumeration", type=rif12_ExchangeFile_AttributeDefinitionEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeDefinitionEnumeration", type=DatatypeDefinitionEnumeration, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue60: BinaryAssociation = BinaryAssociation(
    name="defaultValue60",
    ends={
        Property(name="AttributeValueEnumeration", type=rif12_ExchangeFile_AttributeDefinitionEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeDefinitionEnumeration61", type=AttributeValueEnumeration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue57: BinaryAssociation = BinaryAssociation(
    name="defaultValue57",
    ends={
        Property(name="AttributeValueComplex", type=rif12_ExchangeFile_AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeDefinitionComplex58", type=AttributeValueComplex, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties63: BinaryAssociation = BinaryAssociation(
    name="properties63",
    ends={
        Property(name="EmbeddedValue", type=rif12_ExchangeFile_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_EnumValue", type=EmbeddedValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
specifiedValues62: BinaryAssociation = BinaryAssociation(
    name="specifiedValues62",
    ends={
        Property(name="EnumValue", type=rif12_ExchangeFile_DatatypeDefinitionEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_DatatypeDefinitionEnumeration", type=EnumValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition66: BinaryAssociation = BinaryAssociation(
    name="definition66",
    ends={
        Property(name="AttributeDefinitionEnumeration", type=rif12_ExchangeFile_AttributeValueEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeValueEnumeration67", type=AttributeDefinitionEnumeration, multiplicity=Multiplicity(1, 1))
    }
)
type68: BinaryAssociation = BinaryAssociation(
    name="type68",
    ends={
        Property(name="DatatypeDefinitionSimple", type=rif12_ExchangeFile_AttributeDefinitionSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeDefinitionSimple", type=DatatypeDefinitionSimple, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue69: BinaryAssociation = BinaryAssociation(
    name="defaultValue69",
    ends={
        Property(name="AttributeValueSimple", type=rif12_ExchangeFile_AttributeDefinitionSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeDefinitionSimple70", type=AttributeValueSimple, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values64: BinaryAssociation = BinaryAssociation(
    name="values64",
    ends={
        Property(name="EnumValue65", type=rif12_ExchangeFile_AttributeValueEnumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeValueEnumeration", type=EnumValue, multiplicity=Multiplicity(0, 9999))
    }
)
definition72: BinaryAssociation = BinaryAssociation(
    name="definition72",
    ends={
        Property(name="AttributeDefinitionComplex", type=rif12_ExchangeFile_AttributeValueEmbeddedDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeValueEmbeddedDocument", type=AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
xhtmlContent73: BinaryAssociation = BinaryAssociation(
    name="xhtmlContent73",
    ends={
        Property(name="DataTypes_XhtmlContent", type=rif12_ExchangeFile_AttributeValueEmbeddedDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeValueEmbeddedDocument74", type=DataTypes_XhtmlContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition75: BinaryAssociation = BinaryAssociation(
    name="definition75",
    ends={
        Property(name="AttributeDefinitionComplex76", type=rif12_ExchangeFile_AttributeValueEmbeddedFile, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeValueEmbeddedFile", type=AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
binaryContent77: BinaryAssociation = BinaryAssociation(
    name="binaryContent77",
    ends={
        Property(name="DataTypes_BinaryContent", type=rif12_ExchangeFile_AttributeValueEmbeddedFile, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeValueEmbeddedFile78", type=DataTypes_BinaryContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition71: BinaryAssociation = BinaryAssociation(
    name="definition71",
    ends={
        Property(name="AttributeDefinitionSimple", type=rif12_ExchangeFile_AttributeValueSimple, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeValueSimple", type=AttributeDefinitionSimple, multiplicity=Multiplicity(1, 1))
    }
)
definition81: BinaryAssociation = BinaryAssociation(
    name="definition81",
    ends={
        Property(name="AttributeDefinitionComplex82", type=rif12_ExchangeFile_AttributeValueXmlData, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeValueXmlData", type=AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
xmlContent83: BinaryAssociation = BinaryAssociation(
    name="xmlContent83",
    ends={
        Property(name="DataTypes_XmlContent", type=rif12_ExchangeFile_AttributeValueXmlData, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeValueXmlData84", type=DataTypes_XmlContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definition79: BinaryAssociation = BinaryAssociation(
    name="definition79",
    ends={
        Property(name="AttributeDefinitionComplex80", type=rif12_ExchangeFile_AttributeValueFileReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_AttributeValueFileReference", type=AttributeDefinitionComplex, multiplicity=Multiplicity(1, 1))
    }
)
coreContent86: BinaryAssociation = BinaryAssociation(
    name="coreContent86",
    ends={
        Property(name="RIFContent", type=rif12_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIF87", type=RIFContent, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
toolExtensions88: BinaryAssociation = BinaryAssociation(
    name="toolExtensions88",
    ends={
        Property(name="RIFToolExtension", type=rif12_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIF89", type=RIFToolExtension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
header85: BinaryAssociation = BinaryAssociation(
    name="header85",
    ends={
        Property(name="RIFHeader", type=rif12_ExchangeFile_RIF, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIF", type=RIFHeader, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SpecHierarchyRoots94: BinaryAssociation = BinaryAssociation(
    name="SpecHierarchyRoots94",
    ends={
        Property(name="SpecHierarchyRoot96", type=rif12_ExchangeFile_RIFContent, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIFContent95", type=SpecHierarchyRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specObjects97: BinaryAssociation = BinaryAssociation(
    name="specObjects97",
    ends={
        Property(name="SpecObject99", type=rif12_ExchangeFile_RIFContent, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIFContent98", type=SpecObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specGroups100: BinaryAssociation = BinaryAssociation(
    name="specGroups100",
    ends={
        Property(name="SpecGroup102", type=rif12_ExchangeFile_RIFContent, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIFContent101", type=SpecGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
SpecGroupHierarchyRoots103: BinaryAssociation = BinaryAssociation(
    name="SpecGroupHierarchyRoots103",
    ends={
        Property(name="SpecGroupHierarchyRoot105", type=rif12_ExchangeFile_RIFContent, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIFContent104", type=SpecGroupHierarchyRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specTypes106: BinaryAssociation = BinaryAssociation(
    name="specTypes106",
    ends={
        Property(name="SpecType108", type=rif12_ExchangeFile_RIFContent, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIFContent107", type=SpecType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessPolicies90: BinaryAssociation = BinaryAssociation(
    name="accessPolicies90",
    ends={
        Property(name="AccessPolicy", type=rif12_ExchangeFile_RIFContent, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIFContent", type=AccessPolicy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datatypes91: BinaryAssociation = BinaryAssociation(
    name="datatypes91",
    ends={
        Property(name="DatatypeDefinition93", type=rif12_ExchangeFile_RIFContent, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIFContent92", type=DatatypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specRelations109: BinaryAssociation = BinaryAssociation(
    name="specRelations109",
    ends={
        Property(name="SpecRelation111", type=rif12_ExchangeFile_RIFContent, multiplicity=Multiplicity(1, 1)),
        Property(name="rif12_ExchangeFile_RIFContent110", type=SpecRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_rif12_ExchangeFile_SpecHierarchyRoot_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif12_ExchangeFile_SpecHierarchyRoot)
gen_rif12_ExchangeFile_SpecType_Identifiable = Generalization(general=Identifiable, specific=rif12_ExchangeFile_SpecType)
gen_rif12_ExchangeFile_SpecElementWithUserDefinedAttributes_Identifiable = Generalization(general=Identifiable, specific=rif12_ExchangeFile_SpecElementWithUserDefinedAttributes)
gen_rif12_ExchangeFile_SpecHierarchy_Identifiable = Generalization(general=Identifiable, specific=rif12_ExchangeFile_SpecHierarchy)
gen_rif12_ExchangeFile_SpecObject_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif12_ExchangeFile_SpecObject)
gen_rif12_ExchangeFile_SpecGroup_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif12_ExchangeFile_SpecGroup)
gen_rif12_ExchangeFile_AttributeDefinition_Identifiable = Generalization(general=Identifiable, specific=rif12_ExchangeFile_AttributeDefinition)
gen_rif12_ExchangeFile_AttributeValue_Identifiable = Generalization(general=Identifiable, specific=rif12_ExchangeFile_AttributeValue)
gen_rif12_ExchangeFile_RelationGroup_Identifiable = Generalization(general=Identifiable, specific=rif12_ExchangeFile_RelationGroup)
gen_rif12_ExchangeFile_SpecRelation_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif12_ExchangeFile_SpecRelation)
gen_rif12_ExchangeFile_DatatypeDefinition_Identifiable = Generalization(general=Identifiable, specific=rif12_ExchangeFile_DatatypeDefinition)
gen_rif12_ExchangeFile_AccessPolicy_Identifiable = Generalization(general=Identifiable, specific=rif12_ExchangeFile_AccessPolicy)
gen_rif12_ExchangeFile_SpecGroupHierarchyRoot_SpecElementWithUserDefinedAttributes = Generalization(general=SpecElementWithUserDefinedAttributes, specific=rif12_ExchangeFile_SpecGroupHierarchyRoot)
gen_rif12_ExchangeFile_SpecGroupHierarchy_Identifiable = Generalization(general=Identifiable, specific=rif12_ExchangeFile_SpecGroupHierarchy)
gen_rif12_ExchangeFile_AttributeDefinitionComplex_AttributeDefinition = Generalization(general=AttributeDefinition, specific=rif12_ExchangeFile_AttributeDefinitionComplex)
gen_rif12_ExchangeFile_AttributeValueComplex_AttributeValue = Generalization(general=AttributeValue, specific=rif12_ExchangeFile_AttributeValueComplex)
gen_rif12_ExchangeFile_AttributeDefinitionEnumeration_AttributeDefinition = Generalization(general=AttributeDefinition, specific=rif12_ExchangeFile_AttributeDefinitionEnumeration)
gen_rif12_ExchangeFile_DatatypeDefinitionComplex_DatatypeDefinition = Generalization(general=DatatypeDefinition, specific=rif12_ExchangeFile_DatatypeDefinitionComplex)
gen_rif12_ExchangeFile_EnumValue_Identifiable = Generalization(general=Identifiable, specific=rif12_ExchangeFile_EnumValue)
gen_rif12_ExchangeFile_DatatypeDefinitionEnumeration_DatatypeDefinition = Generalization(general=DatatypeDefinition, specific=rif12_ExchangeFile_DatatypeDefinitionEnumeration)
gen_rif12_ExchangeFile_AttributeDefinitionSimple_AttributeDefinition = Generalization(general=AttributeDefinition, specific=rif12_ExchangeFile_AttributeDefinitionSimple)
gen_rif12_ExchangeFile_DatatypeDefinitionSimple_DatatypeDefinition = Generalization(general=DatatypeDefinition, specific=rif12_ExchangeFile_DatatypeDefinitionSimple)
gen_rif12_ExchangeFile_AttributeValueSimple_AttributeValue = Generalization(general=AttributeValue, specific=rif12_ExchangeFile_AttributeValueSimple)
gen_rif12_ExchangeFile_AttributeValueEnumeration_AttributeValue = Generalization(general=AttributeValue, specific=rif12_ExchangeFile_AttributeValueEnumeration)
gen_rif12_ExchangeFile_AttributeValueEmbeddedDocument_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif12_ExchangeFile_AttributeValueEmbeddedDocument)
gen_rif12_ExchangeFile_AttributeValueEmbeddedFile_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif12_ExchangeFile_AttributeValueEmbeddedFile)
gen_rif12_ExchangeFile_AttributeValueXmlData_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif12_ExchangeFile_AttributeValueXmlData)
gen_rif12_ExchangeFile_DatatypeDefinitionBinaryFile_DatatypeDefinitionComplex = Generalization(general=DatatypeDefinitionComplex, specific=rif12_ExchangeFile_DatatypeDefinitionBinaryFile)
gen_rif12_ExchangeFile_AttributeValueFileReference_AttributeValueComplex = Generalization(general=AttributeValueComplex, specific=rif12_ExchangeFile_AttributeValueFileReference)
gen_rif12_ExchangeFile_DatatypeDefinitionInteger_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif12_ExchangeFile_DatatypeDefinitionInteger)
gen_rif12_ExchangeFile_DatatypeDefinitionReal_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif12_ExchangeFile_DatatypeDefinitionReal)
gen_rif12_ExchangeFile_DatatypeDefinitionString_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif12_ExchangeFile_DatatypeDefinitionString)
gen_rif12_ExchangeFile_DatatypeDefinitionXmlData_DatatypeDefinitionComplex = Generalization(general=DatatypeDefinitionComplex, specific=rif12_ExchangeFile_DatatypeDefinitionXmlData)
gen_rif12_ExchangeFile_DatatypeDefinitionBoolean_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif12_ExchangeFile_DatatypeDefinitionBoolean)
gen_rif12_ExchangeFile_DatatypeDefinitionDate_DatatypeDefinitionSimple = Generalization(general=DatatypeDefinitionSimple, specific=rif12_ExchangeFile_DatatypeDefinitionDate)
gen_rif12_ExchangeFile_DatatypeDefinitionDocument_DatatypeDefinitionComplex = Generalization(general=DatatypeDefinitionComplex, specific=rif12_ExchangeFile_DatatypeDefinitionDocument)

# Domain Model
domain_model = DomainModel(
    name="rif12",
    types={rif12_ExchangeFile_SpecHierarchyRoot, SpecElementWithUserDefinedAttributes, AttributeValue, rif12_ExchangeFile_Identifiable, rif12_ExchangeFile_SpecType, AttributeDefinition, SpecHierarchy, rif12_ExchangeFile_SpecElementWithUserDefinedAttributes, Identifiable, SpecType, rif12_ExchangeFile_SpecHierarchy, SpecObject, rif12_ExchangeFile_SpecObject, rif12_ExchangeFile_SpecGroup, rif12_ExchangeFile_AttributeDefinition, rif12_ExchangeFile_AttributeValue, SpecRelation, RelationGroup, rif12_ExchangeFile_RelationGroup, rif12_ExchangeFile_SpecRelation, rif12_ExchangeFile_DatatypeDefinition, rif12_ExchangeFile_AccessPolicy, SpecGroupHierarchyRoot, SpecGroup, DatatypeDefinition, SpecHierarchyRoot, rif12_ExchangeFile_SpecGroupHierarchyRoot, rif12_ExchangeFile_SpecGroupHierarchy, rif12_ExchangeFile_AttributeDefinitionComplex, DatatypeDefinitionComplex, SpecGroupHierarchy, rif12_ExchangeFile_AttributeValueComplex, rif12_ExchangeFile_AttributeDefinitionEnumeration, DatatypeDefinitionEnumeration, AttributeValueEnumeration, AttributeValueComplex, rif12_ExchangeFile_DatatypeDefinitionComplex, rif12_ExchangeFile_EnumValue, EmbeddedValue, rif12_ExchangeFile_EmbeddedValue, rif12_ExchangeFile_DatatypeDefinitionEnumeration, EnumValue, AttributeDefinitionEnumeration, rif12_ExchangeFile_AttributeDefinitionSimple, DatatypeDefinitionSimple, AttributeValueSimple, rif12_ExchangeFile_DatatypeDefinitionSimple, rif12_ExchangeFile_AttributeValueSimple, rif12_ExchangeFile_AttributeValueEnumeration, AttributeDefinitionComplex, DataTypes_XhtmlContent, rif12_ExchangeFile_AttributeValueEmbeddedFile, DataTypes_BinaryContent, rif12_ExchangeFile_AttributeValueFileReference, AttributeDefinitionSimple, rif12_ExchangeFile_AttributeValueEmbeddedDocument, rif12_ExchangeFile_AttributeValueXmlData, DataTypes_XmlContent, rif12_ExchangeFile_DatatypeDefinitionBinaryFile, rif12_ExchangeFile_DatatypeDefinitionBoolean, rif12_ExchangeFile_DatatypeDefinitionInteger, rif12_ExchangeFile_DatatypeDefinitionReal, rif12_ExchangeFile_DatatypeDefinitionString, rif12_ExchangeFile_DatatypeDefinitionXmlData, rif12_ExchangeFile_DatatypeDefinitionDate, rif12_ExchangeFile_DatatypeDefinitionDocument, RIFContent, RIFToolExtension, rif12_ExchangeFile_RIFHeader, rif12_ExchangeFile_RIF, RIFHeader, rif12_ExchangeFile_RIFContent, AccessPolicy, rif12_DataTypes_XhtmlContent, rif12_DataTypes_XmlContent, rif12_ExchangeFile_RIFToolExtension, rif12_DataTypes_BinaryContent, AccessPolicyAccessModeEnum, DatatypeDefinitionDateFormatEnum},
    associations={type1, values2, specAttributes4, children0, object5, values6, children9, specObjects12, specRelations16, relationType17, relationGroups14, target20, source22, specGroupHierarchyRoots25, attributeDefinitions28, specGroups26, relationGroups31, datatypeDefinitions34, attributeValues39, specRelations36, specTypes42, specHierarchies45, specObjects48, specHierarchyRoots51, group54, type56, children53, type59, defaultValue60, defaultValue57, properties63, specifiedValues62, definition66, type68, defaultValue69, values64, definition72, xhtmlContent73, definition75, binaryContent77, definition71, definition81, xmlContent83, definition79, coreContent86, toolExtensions88, header85, SpecHierarchyRoots94, specObjects97, specGroups100, SpecGroupHierarchyRoots103, specTypes106, accessPolicies90, datatypes91, specRelations109},
    generalizations={gen_rif12_ExchangeFile_SpecHierarchyRoot_SpecElementWithUserDefinedAttributes, gen_rif12_ExchangeFile_SpecType_Identifiable, gen_rif12_ExchangeFile_SpecElementWithUserDefinedAttributes_Identifiable, gen_rif12_ExchangeFile_SpecHierarchy_Identifiable, gen_rif12_ExchangeFile_SpecObject_SpecElementWithUserDefinedAttributes, gen_rif12_ExchangeFile_SpecGroup_SpecElementWithUserDefinedAttributes, gen_rif12_ExchangeFile_AttributeDefinition_Identifiable, gen_rif12_ExchangeFile_AttributeValue_Identifiable, gen_rif12_ExchangeFile_RelationGroup_Identifiable, gen_rif12_ExchangeFile_SpecRelation_SpecElementWithUserDefinedAttributes, gen_rif12_ExchangeFile_DatatypeDefinition_Identifiable, gen_rif12_ExchangeFile_AccessPolicy_Identifiable, gen_rif12_ExchangeFile_SpecGroupHierarchyRoot_SpecElementWithUserDefinedAttributes, gen_rif12_ExchangeFile_SpecGroupHierarchy_Identifiable, gen_rif12_ExchangeFile_AttributeDefinitionComplex_AttributeDefinition, gen_rif12_ExchangeFile_AttributeValueComplex_AttributeValue, gen_rif12_ExchangeFile_AttributeDefinitionEnumeration_AttributeDefinition, gen_rif12_ExchangeFile_DatatypeDefinitionComplex_DatatypeDefinition, gen_rif12_ExchangeFile_EnumValue_Identifiable, gen_rif12_ExchangeFile_DatatypeDefinitionEnumeration_DatatypeDefinition, gen_rif12_ExchangeFile_AttributeDefinitionSimple_AttributeDefinition, gen_rif12_ExchangeFile_DatatypeDefinitionSimple_DatatypeDefinition, gen_rif12_ExchangeFile_AttributeValueSimple_AttributeValue, gen_rif12_ExchangeFile_AttributeValueEnumeration_AttributeValue, gen_rif12_ExchangeFile_AttributeValueEmbeddedDocument_AttributeValueComplex, gen_rif12_ExchangeFile_AttributeValueEmbeddedFile_AttributeValueComplex, gen_rif12_ExchangeFile_AttributeValueXmlData_AttributeValueComplex, gen_rif12_ExchangeFile_DatatypeDefinitionBinaryFile_DatatypeDefinitionComplex, gen_rif12_ExchangeFile_AttributeValueFileReference_AttributeValueComplex, gen_rif12_ExchangeFile_DatatypeDefinitionInteger_DatatypeDefinitionSimple, gen_rif12_ExchangeFile_DatatypeDefinitionReal_DatatypeDefinitionSimple, gen_rif12_ExchangeFile_DatatypeDefinitionString_DatatypeDefinitionSimple, gen_rif12_ExchangeFile_DatatypeDefinitionXmlData_DatatypeDefinitionComplex, gen_rif12_ExchangeFile_DatatypeDefinitionBoolean_DatatypeDefinitionSimple, gen_rif12_ExchangeFile_DatatypeDefinitionDate_DatatypeDefinitionSimple, gen_rif12_ExchangeFile_DatatypeDefinitionDocument_DatatypeDefinitionComplex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)