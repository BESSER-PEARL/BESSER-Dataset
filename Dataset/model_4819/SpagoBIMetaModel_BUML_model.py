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

# Classes
model_ModelPropertyCategory = Class(name="model::ModelPropertyCategory")
model_ModelPropertyType = Class(name="model::ModelPropertyType")
PhysicalModel = Class(name="PhysicalModel")
BusinessModel = Class(name="BusinessModel")
OlapModel = Class(name="OlapModel")
model_physical_PhysicalModel = Class(name="model::physical::PhysicalModel")
physical_model_Model = Class(name="physical::model::Model")
PhysicalTable = Class(name="PhysicalTable")
model_ModelProperty = Class(name="model::ModelProperty")
model_ModelPropertyMapEntry = Class(name="model::ModelPropertyMapEntry")
model_ModelObject = Class(name="model::ModelObject", is_abstract=True)
model_Model = Class(name="model::Model")
ModelObject = Class(name="ModelObject")
model_physical_PhysicalPrimaryKey = Class(name="model::physical::PhysicalPrimaryKey")
model_physical_PhysicalForeignKey = Class(name="model::physical::PhysicalForeignKey")
PhysicalPrimaryKey = Class(name="PhysicalPrimaryKey")
PhysicalForeignKey = Class(name="PhysicalForeignKey")
model_physical_PhysicalTable = Class(name="model::physical::PhysicalTable")
PhysicalColumn = Class(name="PhysicalColumn")
model_physical_PhysicalColumn = Class(name="model::physical::PhysicalColumn")
BusinessColumn = Class(name="BusinessColumn")
model_business_BusinessTable = Class(name="model::business::BusinessTable")
model_business_BusinessView = Class(name="model::business::BusinessView")
model_business_BusinessRelationship = Class(name="model::business::BusinessRelationship")
model_business_BusinessModel = Class(name="model::business::BusinessModel")
business_model_Model = Class(name="business::model::Model")
BusinessColumnSet = Class(name="BusinessColumnSet")
BusinessRelationship = Class(name="BusinessRelationship")
BusinessIdentifier = Class(name="BusinessIdentifier")
BusinessDomain = Class(name="BusinessDomain")
BusinessViewInnerJoinRelationship = Class(name="BusinessViewInnerJoinRelationship")
model_business_BusinessColumn = Class(name="model::business::BusinessColumn")
model_business_BusinessColumnSet = Class(name="model::business::BusinessColumnSet")
model_business_SimpleBusinessColumn = Class(name="model::business::SimpleBusinessColumn")
model_business_CalculatedBusinessColumn = Class(name="model::business::CalculatedBusinessColumn")
model_olap_OlapModel = Class(name="model::olap::OlapModel")
olap_model_Model = Class(name="olap::model::Model")
Cube = Class(name="Cube")
VirtualCube = Class(name="VirtualCube")
Dimension = Class(name="Dimension")
model_olap_Cube = Class(name="model::olap::Cube")
model_business_BusinessDomain = Class(name="model::business::BusinessDomain")
model_business_BusinessIdentifier = Class(name="model::business::BusinessIdentifier")
model_business_BusinessViewInnerJoinRelationship = Class(name="model::business::BusinessViewInnerJoinRelationship")
Level = Class(name="Level")
model_olap_Level = Class(name="model::olap::Level")
model_olap_Measure = Class(name="model::olap::Measure")
Measure = Class(name="Measure")
CalculatedMember = Class(name="CalculatedMember")
NamedSet = Class(name="NamedSet")
model_olap_Dimension = Class(name="model::olap::Dimension")
Hierarchy = Class(name="Hierarchy")
model_olap_Hierarchy = Class(name="model::olap::Hierarchy")
model_olap_VirtualCubeMeasure = Class(name="model::olap::VirtualCubeMeasure")
model_behavioural_BehaviouralModel = Class(name="model::behavioural::BehaviouralModel")
model_analytical_AnalyticalModel = Class(name="model::analytical::AnalyticalModel")
model_olap_CalculatedMember = Class(name="model::olap::CalculatedMember")
model_olap_NamedSet = Class(name="model::olap::NamedSet")
model_olap_VirtualCube = Class(name="model::olap::VirtualCube")
VirtualCubeDimension = Class(name="VirtualCubeDimension")
VirtualCubeMeasure = Class(name="VirtualCubeMeasure")
model_olap_VirtualCubeDimension = Class(name="model::olap::VirtualCubeDimension")

# model_ModelPropertyCategory class attributes and methods
model_ModelPropertyCategory_name: Property = Property(name="name", type=StringType)
model_ModelPropertyCategory_description: Property = Property(name="description", type=StringType)
model_ModelPropertyCategory.attributes={model_ModelPropertyCategory_description, model_ModelPropertyCategory_name}

# model_ModelPropertyType class attributes and methods
model_ModelPropertyType_id: Property = Property(name="id", type=StringType)
model_ModelPropertyType_name: Property = Property(name="name", type=StringType)
model_ModelPropertyType_description: Property = Property(name="description", type=StringType)
model_ModelPropertyType_admissibleValues: Property = Property(name="admissibleValues", type=StringType)
model_ModelPropertyType_defaultValue: Property = Property(name="defaultValue", type=StringType)
model_ModelPropertyType.attributes={model_ModelPropertyType_defaultValue, model_ModelPropertyType_description, model_ModelPropertyType_admissibleValues, model_ModelPropertyType_name, model_ModelPropertyType_id}

# PhysicalModel class attributes and methods

# BusinessModel class attributes and methods

# OlapModel class attributes and methods

# model_physical_PhysicalModel class attributes and methods
model_physical_PhysicalModel_databaseName: Property = Property(name="databaseName", type=StringType)
model_physical_PhysicalModel_databaseVersion: Property = Property(name="databaseVersion", type=StringType)
model_physical_PhysicalModel_catalog: Property = Property(name="catalog", type=StringType)
model_physical_PhysicalModel_schema: Property = Property(name="schema", type=StringType)
model_physical_PhysicalModel.attributes={model_physical_PhysicalModel_databaseVersion, model_physical_PhysicalModel_catalog, model_physical_PhysicalModel_databaseName, model_physical_PhysicalModel_schema}

# physical_model_Model class attributes and methods

# PhysicalTable class attributes and methods

# model_ModelProperty class attributes and methods
model_ModelProperty_value: Property = Property(name="value", type=StringType)
model_ModelProperty.attributes={model_ModelProperty_value}

# model_ModelPropertyMapEntry class attributes and methods
model_ModelPropertyMapEntry_key: Property = Property(name="key", type=StringType)
model_ModelPropertyMapEntry.attributes={model_ModelPropertyMapEntry_key}

# model_ModelObject class attributes and methods
model_ModelObject_id: Property = Property(name="id", type=StringType)
model_ModelObject_name: Property = Property(name="name", type=StringType)
model_ModelObject_uniqueName: Property = Property(name="uniqueName", type=StringType)
model_ModelObject_description: Property = Property(name="description", type=StringType)
model_ModelObject.attributes={model_ModelObject_uniqueName, model_ModelObject_description, model_ModelObject_id, model_ModelObject_name}

# model_Model class attributes and methods

# ModelObject class attributes and methods

# model_physical_PhysicalPrimaryKey class attributes and methods

# model_physical_PhysicalForeignKey class attributes and methods
model_physical_PhysicalForeignKey_sourceName: Property = Property(name="sourceName", type=StringType)
model_physical_PhysicalForeignKey_destinationName: Property = Property(name="destinationName", type=StringType)
model_physical_PhysicalForeignKey.attributes={model_physical_PhysicalForeignKey_sourceName, model_physical_PhysicalForeignKey_destinationName}

# PhysicalPrimaryKey class attributes and methods

# PhysicalForeignKey class attributes and methods

# model_physical_PhysicalTable class attributes and methods
model_physical_PhysicalTable_comment: Property = Property(name="comment", type=StringType)
model_physical_PhysicalTable_type: Property = Property(name="type", type=StringType)
model_physical_PhysicalTable.attributes={model_physical_PhysicalTable_comment, model_physical_PhysicalTable_type}

# PhysicalColumn class attributes and methods

# model_physical_PhysicalColumn class attributes and methods
model_physical_PhysicalColumn_comment: Property = Property(name="comment", type=StringType)
model_physical_PhysicalColumn_dataType: Property = Property(name="dataType", type=StringType)
model_physical_PhysicalColumn_typeName: Property = Property(name="typeName", type=StringType)
model_physical_PhysicalColumn_size: Property = Property(name="size", type=IntegerType)
model_physical_PhysicalColumn_octectLength: Property = Property(name="octectLength", type=IntegerType)
model_physical_PhysicalColumn_decimalDigits: Property = Property(name="decimalDigits", type=IntegerType)
model_physical_PhysicalColumn_radix: Property = Property(name="radix", type=IntegerType)
model_physical_PhysicalColumn_defaultValue: Property = Property(name="defaultValue", type=StringType)
model_physical_PhysicalColumn_nullable: Property = Property(name="nullable", type=BooleanType)
model_physical_PhysicalColumn_position: Property = Property(name="position", type=IntegerType)
model_physical_PhysicalColumn.attributes={model_physical_PhysicalColumn_size, model_physical_PhysicalColumn_dataType, model_physical_PhysicalColumn_position, model_physical_PhysicalColumn_comment, model_physical_PhysicalColumn_nullable, model_physical_PhysicalColumn_decimalDigits, model_physical_PhysicalColumn_defaultValue, model_physical_PhysicalColumn_octectLength, model_physical_PhysicalColumn_radix, model_physical_PhysicalColumn_typeName}

# BusinessColumn class attributes and methods

# model_business_BusinessTable class attributes and methods

# model_business_BusinessView class attributes and methods

# model_business_BusinessRelationship class attributes and methods

# model_business_BusinessModel class attributes and methods

# business_model_Model class attributes and methods

# BusinessColumnSet class attributes and methods

# BusinessRelationship class attributes and methods

# BusinessIdentifier class attributes and methods

# BusinessDomain class attributes and methods

# BusinessViewInnerJoinRelationship class attributes and methods

# model_business_BusinessColumn class attributes and methods

# model_business_BusinessColumnSet class attributes and methods

# model_business_SimpleBusinessColumn class attributes and methods

# model_business_CalculatedBusinessColumn class attributes and methods

# model_olap_OlapModel class attributes and methods

# olap_model_Model class attributes and methods

# Cube class attributes and methods

# VirtualCube class attributes and methods

# Dimension class attributes and methods

# model_olap_Cube class attributes and methods

# model_business_BusinessDomain class attributes and methods

# model_business_BusinessIdentifier class attributes and methods

# model_business_BusinessViewInnerJoinRelationship class attributes and methods

# Level class attributes and methods

# model_olap_Level class attributes and methods

# model_olap_Measure class attributes and methods

# Measure class attributes and methods

# CalculatedMember class attributes and methods

# NamedSet class attributes and methods

# model_olap_Dimension class attributes and methods

# Hierarchy class attributes and methods

# model_olap_Hierarchy class attributes and methods

# model_olap_VirtualCubeMeasure class attributes and methods

# model_behavioural_BehaviouralModel class attributes and methods

# model_analytical_AnalyticalModel class attributes and methods

# model_olap_CalculatedMember class attributes and methods

# model_olap_NamedSet class attributes and methods

# model_olap_VirtualCube class attributes and methods

# VirtualCubeDimension class attributes and methods

# VirtualCubeMeasure class attributes and methods

# model_olap_VirtualCubeDimension class attributes and methods

# Relationships
parentCategory1: BinaryAssociation = BinaryAssociation(
    name="parentCategory1",
    ends={
        Property(name="model_ModelPropertyCategory", type=model_ModelPropertyCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ModelPropertyCategory0", type=model_ModelPropertyCategory, multiplicity=Multiplicity(0, 1))
    }
)
subCategories3: BinaryAssociation = BinaryAssociation(
    name="subCategories3",
    ends={
        Property(name="model_ModelPropertyCategory4", type=model_ModelPropertyCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ModelPropertyCategory2", type=model_ModelPropertyCategory, multiplicity=Multiplicity(0, 9999))
    }
)
physicalModels12: BinaryAssociation = BinaryAssociation(
    name="physicalModels12",
    ends={
        Property(name="physical", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="PhysicalModel", type=PhysicalModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessModels13: BinaryAssociation = BinaryAssociation(
    name="businessModels13",
    ends={
        Property(name="business", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessModel", type=BusinessModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
olapModels14: BinaryAssociation = BinaryAssociation(
    name="olapModels14",
    ends={
        Property(name="olap", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="OlapModel", type=OlapModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyTypes15: BinaryAssociation = BinaryAssociation(
    name="propertyTypes15",
    ends={
        Property(name="model_ModelPropertyType16", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Model", type=model_ModelPropertyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyCategories17: BinaryAssociation = BinaryAssociation(
    name="propertyCategories17",
    ends={
        Property(name="model_ModelPropertyCategory19", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Model18", type=model_ModelPropertyCategory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentModel20: BinaryAssociation = BinaryAssociation(
    name="parentModel20",
    ends={
        Property(name="Model", type=model_physical_PhysicalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="physicalModels", type=physical_model_Model, multiplicity=Multiplicity(1, 1))
    }
)
tables21: BinaryAssociation = BinaryAssociation(
    name="tables21",
    ends={
        Property(name="physical22", type=model_physical_PhysicalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="PhysicalTable", type=PhysicalTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyTypes5: BinaryAssociation = BinaryAssociation(
    name="propertyTypes5",
    ends={
        Property(name="ModelPropertyType", type=model_ModelPropertyCategory, multiplicity=Multiplicity(1, 1)),
        Property(name="category", type=model_ModelPropertyType, multiplicity=Multiplicity(0, 9999))
    }
)
category6: BinaryAssociation = BinaryAssociation(
    name="category6",
    ends={
        Property(name="ModelPropertyCategory", type=model_ModelPropertyType, multiplicity=Multiplicity(1, 1)),
        Property(name="propertyTypes", type=model_ModelPropertyCategory, multiplicity=Multiplicity(1, 1))
    }
)
propertyType7: BinaryAssociation = BinaryAssociation(
    name="propertyType7",
    ends={
        Property(name="model_ModelPropertyType", type=model_ModelProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ModelProperty", type=model_ModelPropertyType, multiplicity=Multiplicity(1, 1))
    }
)
value8: BinaryAssociation = BinaryAssociation(
    name="value8",
    ends={
        Property(name="model_ModelProperty9", type=model_ModelPropertyMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ModelPropertyMapEntry", type=model_ModelProperty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties10: BinaryAssociation = BinaryAssociation(
    name="properties10",
    ends={
        Property(name="model_ModelPropertyMapEntry11", type=model_ModelObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ModelObject", type=model_ModelPropertyMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model35: BinaryAssociation = BinaryAssociation(
    name="model35",
    ends={
        Property(name="physical37", type=model_physical_PhysicalPrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="PhysicalModel36", type=PhysicalModel, multiplicity=Multiplicity(1, 1))
    }
)
table38: BinaryAssociation = BinaryAssociation(
    name="table38",
    ends={
        Property(name="PhysicalTable39", type=model_physical_PhysicalPrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalPrimaryKey", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
columns40: BinaryAssociation = BinaryAssociation(
    name="columns40",
    ends={
        Property(name="PhysicalColumn42", type=model_physical_PhysicalPrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalPrimaryKey41", type=PhysicalColumn, multiplicity=Multiplicity(1, 9999))
    }
)
sourceTable43: BinaryAssociation = BinaryAssociation(
    name="sourceTable43",
    ends={
        Property(name="PhysicalTable44", type=model_physical_PhysicalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalForeignKey", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
sourceColumns45: BinaryAssociation = BinaryAssociation(
    name="sourceColumns45",
    ends={
        Property(name="PhysicalColumn47", type=model_physical_PhysicalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalForeignKey46", type=PhysicalColumn, multiplicity=Multiplicity(1, 9999))
    }
)
destinationTable48: BinaryAssociation = BinaryAssociation(
    name="destinationTable48",
    ends={
        Property(name="PhysicalTable50", type=model_physical_PhysicalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalForeignKey49", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
destinationColumns51: BinaryAssociation = BinaryAssociation(
    name="destinationColumns51",
    ends={
        Property(name="PhysicalColumn53", type=model_physical_PhysicalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalForeignKey52", type=PhysicalColumn, multiplicity=Multiplicity(1, 9999))
    }
)
primaryKeys23: BinaryAssociation = BinaryAssociation(
    name="primaryKeys23",
    ends={
        Property(name="physical24", type=model_physical_PhysicalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="PhysicalPrimaryKey", type=PhysicalPrimaryKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeys25: BinaryAssociation = BinaryAssociation(
    name="foreignKeys25",
    ends={
        Property(name="physical26", type=model_physical_PhysicalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="PhysicalForeignKey", type=PhysicalForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model27: BinaryAssociation = BinaryAssociation(
    name="model27",
    ends={
        Property(name="physical29", type=model_physical_PhysicalTable, multiplicity=Multiplicity(1, 1)),
        Property(name="PhysicalModel28", type=PhysicalModel, multiplicity=Multiplicity(1, 1))
    }
)
columns30: BinaryAssociation = BinaryAssociation(
    name="columns30",
    ends={
        Property(name="physical31", type=model_physical_PhysicalTable, multiplicity=Multiplicity(1, 1)),
        Property(name="PhysicalColumn", type=PhysicalColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table32: BinaryAssociation = BinaryAssociation(
    name="table32",
    ends={
        Property(name="physical34", type=model_physical_PhysicalColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="PhysicalTable33", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
columns77: BinaryAssociation = BinaryAssociation(
    name="columns77",
    ends={
        Property(name="business78", type=model_business_BusinessColumnSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessColumn", type=BusinessColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalTable79: BinaryAssociation = BinaryAssociation(
    name="physicalTable79",
    ends={
        Property(name="PhysicalTable80", type=model_business_BusinessTable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessTable", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
joinRelationships81: BinaryAssociation = BinaryAssociation(
    name="joinRelationships81",
    ends={
        Property(name="BusinessViewInnerJoinRelationship82", type=model_business_BusinessView, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessView", type=BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
model83: BinaryAssociation = BinaryAssociation(
    name="model83",
    ends={
        Property(name="business85", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessModel84", type=BusinessModel, multiplicity=Multiplicity(1, 1))
    }
)
sourceTable86: BinaryAssociation = BinaryAssociation(
    name="sourceTable86",
    ends={
        Property(name="BusinessColumnSet87", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessRelationship", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
destinationTable88: BinaryAssociation = BinaryAssociation(
    name="destinationTable88",
    ends={
        Property(name="BusinessColumnSet90", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessRelationship89", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
sourceColumns91: BinaryAssociation = BinaryAssociation(
    name="sourceColumns91",
    ends={
        Property(name="BusinessColumn93", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessRelationship92", type=BusinessColumn, multiplicity=Multiplicity(0, 9999))
    }
)
destinationColumns94: BinaryAssociation = BinaryAssociation(
    name="destinationColumns94",
    ends={
        Property(name="BusinessColumn96", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessRelationship95", type=BusinessColumn, multiplicity=Multiplicity(0, 9999))
    }
)
model54: BinaryAssociation = BinaryAssociation(
    name="model54",
    ends={
        Property(name="physical56", type=model_physical_PhysicalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="PhysicalModel55", type=PhysicalModel, multiplicity=Multiplicity(0, 1))
    }
)
parentModel57: BinaryAssociation = BinaryAssociation(
    name="parentModel57",
    ends={
        Property(name="Model58", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="businessModels", type=business_model_Model, multiplicity=Multiplicity(1, 1))
    }
)
physicalModel59: BinaryAssociation = BinaryAssociation(
    name="physicalModel59",
    ends={
        Property(name="PhysicalModel60", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessModel", type=PhysicalModel, multiplicity=Multiplicity(1, 1))
    }
)
tables61: BinaryAssociation = BinaryAssociation(
    name="tables61",
    ends={
        Property(name="business62", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessColumnSet", type=BusinessColumnSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships63: BinaryAssociation = BinaryAssociation(
    name="relationships63",
    ends={
        Property(name="business64", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessRelationship", type=BusinessRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiers65: BinaryAssociation = BinaryAssociation(
    name="identifiers65",
    ends={
        Property(name="business66", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessIdentifier", type=BusinessIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domains67: BinaryAssociation = BinaryAssociation(
    name="domains67",
    ends={
        Property(name="business68", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessDomain", type=BusinessDomain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
joinRelationships69: BinaryAssociation = BinaryAssociation(
    name="joinRelationships69",
    ends={
        Property(name="business70", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessViewInnerJoinRelationship", type=BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table71: BinaryAssociation = BinaryAssociation(
    name="table71",
    ends={
        Property(name="business73", type=model_business_BusinessColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessColumnSet72", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
model74: BinaryAssociation = BinaryAssociation(
    name="model74",
    ends={
        Property(name="business76", type=model_business_BusinessColumnSet, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessModel75", type=BusinessModel, multiplicity=Multiplicity(1, 1))
    }
)
sourceColumns127: BinaryAssociation = BinaryAssociation(
    name="sourceColumns127",
    ends={
        Property(name="PhysicalColumn129", type=model_business_BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessViewInnerJoinRelationship128", type=PhysicalColumn, multiplicity=Multiplicity(0, 9999))
    }
)
destinationColumns130: BinaryAssociation = BinaryAssociation(
    name="destinationColumns130",
    ends={
        Property(name="PhysicalColumn132", type=model_business_BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessViewInnerJoinRelationship131", type=PhysicalColumn, multiplicity=Multiplicity(0, 9999))
    }
)
physicalColumn133: BinaryAssociation = BinaryAssociation(
    name="physicalColumn133",
    ends={
        Property(name="PhysicalColumn134", type=model_business_SimpleBusinessColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_SimpleBusinessColumn", type=PhysicalColumn, multiplicity=Multiplicity(1, 1))
    }
)
parentModel135: BinaryAssociation = BinaryAssociation(
    name="parentModel135",
    ends={
        Property(name="Model136", type=model_olap_OlapModel, multiplicity=Multiplicity(1, 1)),
        Property(name="olapModels", type=olap_model_Model, multiplicity=Multiplicity(1, 1))
    }
)
cubes137: BinaryAssociation = BinaryAssociation(
    name="cubes137",
    ends={
        Property(name="olap138", type=model_olap_OlapModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Cube", type=Cube, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
virtualCubes139: BinaryAssociation = BinaryAssociation(
    name="virtualCubes139",
    ends={
        Property(name="olap140", type=model_olap_OlapModel, multiplicity=Multiplicity(1, 1)),
        Property(name="VirtualCube", type=VirtualCube, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimensions141: BinaryAssociation = BinaryAssociation(
    name="dimensions141",
    ends={
        Property(name="olap142", type=model_olap_OlapModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Dimension", type=Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalForeignKey97: BinaryAssociation = BinaryAssociation(
    name="physicalForeignKey97",
    ends={
        Property(name="PhysicalForeignKey99", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessRelationship98", type=PhysicalForeignKey, multiplicity=Multiplicity(0, 1))
    }
)
model100: BinaryAssociation = BinaryAssociation(
    name="model100",
    ends={
        Property(name="business102", type=model_business_BusinessDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessModel101", type=BusinessModel, multiplicity=Multiplicity(1, 1))
    }
)
tables103: BinaryAssociation = BinaryAssociation(
    name="tables103",
    ends={
        Property(name="BusinessColumnSet104", type=model_business_BusinessDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessDomain", type=BusinessColumnSet, multiplicity=Multiplicity(0, 9999))
    }
)
relationships105: BinaryAssociation = BinaryAssociation(
    name="relationships105",
    ends={
        Property(name="BusinessRelationship107", type=model_business_BusinessDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessDomain106", type=BusinessRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
model108: BinaryAssociation = BinaryAssociation(
    name="model108",
    ends={
        Property(name="business110", type=model_business_BusinessIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessModel109", type=BusinessModel, multiplicity=Multiplicity(0, 1))
    }
)
table111: BinaryAssociation = BinaryAssociation(
    name="table111",
    ends={
        Property(name="BusinessColumnSet112", type=model_business_BusinessIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessIdentifier", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
columns113: BinaryAssociation = BinaryAssociation(
    name="columns113",
    ends={
        Property(name="BusinessColumn115", type=model_business_BusinessIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessIdentifier114", type=BusinessColumn, multiplicity=Multiplicity(1, 9999))
    }
)
physicalPrimaryKey116: BinaryAssociation = BinaryAssociation(
    name="physicalPrimaryKey116",
    ends={
        Property(name="PhysicalPrimaryKey118", type=model_business_BusinessIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessIdentifier117", type=PhysicalPrimaryKey, multiplicity=Multiplicity(0, 1))
    }
)
model119: BinaryAssociation = BinaryAssociation(
    name="model119",
    ends={
        Property(name="business121", type=model_business_BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="BusinessModel120", type=BusinessModel, multiplicity=Multiplicity(1, 1))
    }
)
sourceTable122: BinaryAssociation = BinaryAssociation(
    name="sourceTable122",
    ends={
        Property(name="PhysicalTable123", type=model_business_BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessViewInnerJoinRelationship", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
destinationTable124: BinaryAssociation = BinaryAssociation(
    name="destinationTable124",
    ends={
        Property(name="PhysicalTable126", type=model_business_BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessViewInnerJoinRelationship125", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
levels169: BinaryAssociation = BinaryAssociation(
    name="levels169",
    ends={
        Property(name="olap170", type=model_olap_Hierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="Level", type=Level, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
hierarchy171: BinaryAssociation = BinaryAssociation(
    name="hierarchy171",
    ends={
        Property(name="olap173", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="Hierarchy172", type=Hierarchy, multiplicity=Multiplicity(0, 1))
    }
)
column174: BinaryAssociation = BinaryAssociation(
    name="column174",
    ends={
        Property(name="BusinessColumn175", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Level", type=BusinessColumn, multiplicity=Multiplicity(0, 1))
    }
)
ordinalColumn176: BinaryAssociation = BinaryAssociation(
    name="ordinalColumn176",
    ends={
        Property(name="BusinessColumn178", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Level177", type=BusinessColumn, multiplicity=Multiplicity(0, 1))
    }
)
nameColumn179: BinaryAssociation = BinaryAssociation(
    name="nameColumn179",
    ends={
        Property(name="BusinessColumn181", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Level180", type=BusinessColumn, multiplicity=Multiplicity(0, 1))
    }
)
captionColumn182: BinaryAssociation = BinaryAssociation(
    name="captionColumn182",
    ends={
        Property(name="BusinessColumn184", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Level183", type=BusinessColumn, multiplicity=Multiplicity(0, 1))
    }
)
propertyColumns185: BinaryAssociation = BinaryAssociation(
    name="propertyColumns185",
    ends={
        Property(name="BusinessColumn187", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Level186", type=BusinessColumn, multiplicity=Multiplicity(0, 9999))
    }
)
cube188: BinaryAssociation = BinaryAssociation(
    name="cube188",
    ends={
        Property(name="olap190", type=model_olap_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="Cube189", type=Cube, multiplicity=Multiplicity(0, 1))
    }
)
model143: BinaryAssociation = BinaryAssociation(
    name="model143",
    ends={
        Property(name="olap145", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="OlapModel144", type=OlapModel, multiplicity=Multiplicity(0, 1))
    }
)
table146: BinaryAssociation = BinaryAssociation(
    name="table146",
    ends={
        Property(name="BusinessColumnSet147", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Cube", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
dimensions148: BinaryAssociation = BinaryAssociation(
    name="dimensions148",
    ends={
        Property(name="Dimension150", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Cube149", type=Dimension, multiplicity=Multiplicity(1, 9999))
    }
)
measures151: BinaryAssociation = BinaryAssociation(
    name="measures151",
    ends={
        Property(name="olap152", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="Measure", type=Measure, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
calculatedMembers153: BinaryAssociation = BinaryAssociation(
    name="calculatedMembers153",
    ends={
        Property(name="olap154", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="CalculatedMember", type=CalculatedMember, multiplicity=Multiplicity(0, 1))
    }
)
namedSets155: BinaryAssociation = BinaryAssociation(
    name="namedSets155",
    ends={
        Property(name="olap156", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedSet", type=NamedSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table157: BinaryAssociation = BinaryAssociation(
    name="table157",
    ends={
        Property(name="BusinessColumnSet158", type=model_olap_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Dimension", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
hierarchies159: BinaryAssociation = BinaryAssociation(
    name="hierarchies159",
    ends={
        Property(name="olap160", type=model_olap_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="Hierarchy", type=Hierarchy, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
model161: BinaryAssociation = BinaryAssociation(
    name="model161",
    ends={
        Property(name="olap163", type=model_olap_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="OlapModel162", type=OlapModel, multiplicity=Multiplicity(0, 1))
    }
)
table164: BinaryAssociation = BinaryAssociation(
    name="table164",
    ends={
        Property(name="BusinessColumnSet165", type=model_olap_Hierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Hierarchy", type=BusinessColumnSet, multiplicity=Multiplicity(0, 1))
    }
)
dimension166: BinaryAssociation = BinaryAssociation(
    name="dimension166",
    ends={
        Property(name="olap168", type=model_olap_Hierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="Dimension167", type=Dimension, multiplicity=Multiplicity(0, 1))
    }
)
dimension218: BinaryAssociation = BinaryAssociation(
    name="dimension218",
    ends={
        Property(name="Dimension220", type=model_olap_VirtualCubeDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCubeDimension219", type=Dimension, multiplicity=Multiplicity(0, 1))
    }
)
virtualCube221: BinaryAssociation = BinaryAssociation(
    name="virtualCube221",
    ends={
        Property(name="olap223", type=model_olap_VirtualCubeMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="VirtualCube222", type=VirtualCube, multiplicity=Multiplicity(0, 1))
    }
)
cube224: BinaryAssociation = BinaryAssociation(
    name="cube224",
    ends={
        Property(name="Cube225", type=model_olap_VirtualCubeMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCubeMeasure", type=Cube, multiplicity=Multiplicity(0, 1))
    }
)
measure226: BinaryAssociation = BinaryAssociation(
    name="measure226",
    ends={
        Property(name="Measure228", type=model_olap_VirtualCubeMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCubeMeasure227", type=Measure, multiplicity=Multiplicity(0, 1))
    }
)
column191: BinaryAssociation = BinaryAssociation(
    name="column191",
    ends={
        Property(name="BusinessColumn192", type=model_olap_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Measure", type=BusinessColumn, multiplicity=Multiplicity(0, 1))
    }
)
cube193: BinaryAssociation = BinaryAssociation(
    name="cube193",
    ends={
        Property(name="olap195", type=model_olap_CalculatedMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Cube194", type=Cube, multiplicity=Multiplicity(0, 1))
    }
)
hierarchy196: BinaryAssociation = BinaryAssociation(
    name="hierarchy196",
    ends={
        Property(name="Hierarchy197", type=model_olap_CalculatedMember, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_CalculatedMember", type=Hierarchy, multiplicity=Multiplicity(0, 1))
    }
)
cube198: BinaryAssociation = BinaryAssociation(
    name="cube198",
    ends={
        Property(name="olap200", type=model_olap_NamedSet, multiplicity=Multiplicity(1, 1)),
        Property(name="Cube199", type=Cube, multiplicity=Multiplicity(0, 1))
    }
)
cubes201: BinaryAssociation = BinaryAssociation(
    name="cubes201",
    ends={
        Property(name="Cube202", type=model_olap_VirtualCube, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCube", type=Cube, multiplicity=Multiplicity(0, 9999))
    }
)
dimensions203: BinaryAssociation = BinaryAssociation(
    name="dimensions203",
    ends={
        Property(name="olap204", type=model_olap_VirtualCube, multiplicity=Multiplicity(1, 1)),
        Property(name="VirtualCubeDimension", type=VirtualCubeDimension, multiplicity=Multiplicity(0, 1))
    }
)
measures205: BinaryAssociation = BinaryAssociation(
    name="measures205",
    ends={
        Property(name="olap206", type=model_olap_VirtualCube, multiplicity=Multiplicity(1, 1)),
        Property(name="VirtualCubeMeasure", type=VirtualCubeMeasure, multiplicity=Multiplicity(0, 9999))
    }
)
calculatedMembers207: BinaryAssociation = BinaryAssociation(
    name="calculatedMembers207",
    ends={
        Property(name="CalculatedMember209", type=model_olap_VirtualCube, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCube208", type=CalculatedMember, multiplicity=Multiplicity(0, 9999))
    }
)
model210: BinaryAssociation = BinaryAssociation(
    name="model210",
    ends={
        Property(name="olap212", type=model_olap_VirtualCube, multiplicity=Multiplicity(1, 1)),
        Property(name="OlapModel211", type=OlapModel, multiplicity=Multiplicity(0, 1))
    }
)
virtualCube213: BinaryAssociation = BinaryAssociation(
    name="virtualCube213",
    ends={
        Property(name="olap215", type=model_olap_VirtualCubeDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="VirtualCube214", type=VirtualCube, multiplicity=Multiplicity(0, 1))
    }
)
cube216: BinaryAssociation = BinaryAssociation(
    name="cube216",
    ends={
        Property(name="Cube217", type=model_olap_VirtualCubeDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCubeDimension", type=Cube, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model_physical_PhysicalModel_ModelObject = Generalization(general=ModelObject, specific=model_physical_PhysicalModel)
gen_model_Model_ModelObject = Generalization(general=ModelObject, specific=model_Model)
gen_model_physical_PhysicalPrimaryKey_ModelObject = Generalization(general=ModelObject, specific=model_physical_PhysicalPrimaryKey)
gen_model_physical_PhysicalForeignKey_ModelObject = Generalization(general=ModelObject, specific=model_physical_PhysicalForeignKey)
gen_model_physical_PhysicalTable_ModelObject = Generalization(general=ModelObject, specific=model_physical_PhysicalTable)
gen_model_physical_PhysicalColumn_ModelObject = Generalization(general=ModelObject, specific=model_physical_PhysicalColumn)
gen_model_business_BusinessTable_BusinessColumnSet = Generalization(general=BusinessColumnSet, specific=model_business_BusinessTable)
gen_model_business_BusinessView_BusinessColumnSet = Generalization(general=BusinessColumnSet, specific=model_business_BusinessView)
gen_model_business_BusinessRelationship_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessRelationship)
gen_model_business_BusinessModel_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessModel)
gen_model_business_BusinessColumn_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessColumn)
gen_model_business_BusinessColumnSet_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessColumnSet)
gen_model_business_SimpleBusinessColumn_BusinessColumn = Generalization(general=BusinessColumn, specific=model_business_SimpleBusinessColumn)
gen_model_business_CalculatedBusinessColumn_BusinessColumn = Generalization(general=BusinessColumn, specific=model_business_CalculatedBusinessColumn)
gen_model_olap_OlapModel_ModelObject = Generalization(general=ModelObject, specific=model_olap_OlapModel)
gen_model_olap_Cube_ModelObject = Generalization(general=ModelObject, specific=model_olap_Cube)
gen_model_business_BusinessDomain_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessDomain)
gen_model_business_BusinessIdentifier_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessIdentifier)
gen_model_business_BusinessViewInnerJoinRelationship_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessViewInnerJoinRelationship)
gen_model_olap_Level_ModelObject = Generalization(general=ModelObject, specific=model_olap_Level)
gen_model_olap_Measure_ModelObject = Generalization(general=ModelObject, specific=model_olap_Measure)
gen_model_olap_Dimension_ModelObject = Generalization(general=ModelObject, specific=model_olap_Dimension)
gen_model_olap_Hierarchy_ModelObject = Generalization(general=ModelObject, specific=model_olap_Hierarchy)
gen_model_olap_VirtualCubeMeasure_ModelObject = Generalization(general=ModelObject, specific=model_olap_VirtualCubeMeasure)
gen_model_olap_CalculatedMember_ModelObject = Generalization(general=ModelObject, specific=model_olap_CalculatedMember)
gen_model_olap_NamedSet_ModelObject = Generalization(general=ModelObject, specific=model_olap_NamedSet)
gen_model_olap_VirtualCube_ModelObject = Generalization(general=ModelObject, specific=model_olap_VirtualCube)
gen_model_olap_VirtualCubeDimension_ModelObject = Generalization(general=ModelObject, specific=model_olap_VirtualCubeDimension)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_ModelPropertyCategory, model_ModelPropertyType, PhysicalModel, BusinessModel, OlapModel, model_physical_PhysicalModel, physical_model_Model, PhysicalTable, model_ModelProperty, model_ModelPropertyMapEntry, model_ModelObject, model_Model, ModelObject, model_physical_PhysicalPrimaryKey, model_physical_PhysicalForeignKey, PhysicalPrimaryKey, PhysicalForeignKey, model_physical_PhysicalTable, PhysicalColumn, model_physical_PhysicalColumn, BusinessColumn, model_business_BusinessTable, model_business_BusinessView, model_business_BusinessRelationship, model_business_BusinessModel, business_model_Model, BusinessColumnSet, BusinessRelationship, BusinessIdentifier, BusinessDomain, BusinessViewInnerJoinRelationship, model_business_BusinessColumn, model_business_BusinessColumnSet, model_business_SimpleBusinessColumn, model_business_CalculatedBusinessColumn, model_olap_OlapModel, olap_model_Model, Cube, VirtualCube, Dimension, model_olap_Cube, model_business_BusinessDomain, model_business_BusinessIdentifier, model_business_BusinessViewInnerJoinRelationship, Level, model_olap_Level, model_olap_Measure, Measure, CalculatedMember, NamedSet, model_olap_Dimension, Hierarchy, model_olap_Hierarchy, model_olap_VirtualCubeMeasure, model_behavioural_BehaviouralModel, model_analytical_AnalyticalModel, model_olap_CalculatedMember, model_olap_NamedSet, model_olap_VirtualCube, VirtualCubeDimension, VirtualCubeMeasure, model_olap_VirtualCubeDimension},
    associations={parentCategory1, subCategories3, physicalModels12, businessModels13, olapModels14, propertyTypes15, propertyCategories17, parentModel20, tables21, propertyTypes5, category6, propertyType7, value8, properties10, model35, table38, columns40, sourceTable43, sourceColumns45, destinationTable48, destinationColumns51, primaryKeys23, foreignKeys25, model27, columns30, table32, columns77, physicalTable79, joinRelationships81, model83, sourceTable86, destinationTable88, sourceColumns91, destinationColumns94, model54, parentModel57, physicalModel59, tables61, relationships63, identifiers65, domains67, joinRelationships69, table71, model74, sourceColumns127, destinationColumns130, physicalColumn133, parentModel135, cubes137, virtualCubes139, dimensions141, physicalForeignKey97, model100, tables103, relationships105, model108, table111, columns113, physicalPrimaryKey116, model119, sourceTable122, destinationTable124, levels169, hierarchy171, column174, ordinalColumn176, nameColumn179, captionColumn182, propertyColumns185, cube188, model143, table146, dimensions148, measures151, calculatedMembers153, namedSets155, table157, hierarchies159, model161, table164, dimension166, dimension218, virtualCube221, cube224, measure226, column191, cube193, hierarchy196, cube198, cubes201, dimensions203, measures205, calculatedMembers207, model210, virtualCube213, cube216},
    generalizations={gen_model_physical_PhysicalModel_ModelObject, gen_model_Model_ModelObject, gen_model_physical_PhysicalPrimaryKey_ModelObject, gen_model_physical_PhysicalForeignKey_ModelObject, gen_model_physical_PhysicalTable_ModelObject, gen_model_physical_PhysicalColumn_ModelObject, gen_model_business_BusinessTable_BusinessColumnSet, gen_model_business_BusinessView_BusinessColumnSet, gen_model_business_BusinessRelationship_ModelObject, gen_model_business_BusinessModel_ModelObject, gen_model_business_BusinessColumn_ModelObject, gen_model_business_BusinessColumnSet_ModelObject, gen_model_business_SimpleBusinessColumn_BusinessColumn, gen_model_business_CalculatedBusinessColumn_BusinessColumn, gen_model_olap_OlapModel_ModelObject, gen_model_olap_Cube_ModelObject, gen_model_business_BusinessDomain_ModelObject, gen_model_business_BusinessIdentifier_ModelObject, gen_model_business_BusinessViewInnerJoinRelationship_ModelObject, gen_model_olap_Level_ModelObject, gen_model_olap_Measure_ModelObject, gen_model_olap_Dimension_ModelObject, gen_model_olap_Hierarchy_ModelObject, gen_model_olap_VirtualCubeMeasure_ModelObject, gen_model_olap_CalculatedMember_ModelObject, gen_model_olap_NamedSet_ModelObject, gen_model_olap_VirtualCube_ModelObject, gen_model_olap_VirtualCubeDimension_ModelObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)