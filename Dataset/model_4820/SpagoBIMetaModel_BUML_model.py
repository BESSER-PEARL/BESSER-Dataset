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
model_ModelPropertyCategory = Class(name="model_ModelPropertyCategory")
model_ModelPropertyType = Class(name="model_ModelPropertyType")
model_ModelProperty = Class(name="model_ModelProperty")
model_Model = Class(name="model_Model")
ModelObject = Class(name="ModelObject")
PhysicalModel = Class(name="PhysicalModel")
BusinessModel = Class(name="BusinessModel")
OlapModel = Class(name="OlapModel")
model_physical_PhysicalModel = Class(name="model_physical_PhysicalModel")
physical_model_Model = Class(name="physical_model_Model")
PhysicalTable = Class(name="PhysicalTable")
PhysicalPrimaryKey = Class(name="PhysicalPrimaryKey")
PhysicalForeignKey = Class(name="PhysicalForeignKey")
model_ModelPropertyMapEntry = Class(name="model_ModelPropertyMapEntry")
model_ModelObject = Class(name="model_ModelObject", is_abstract=True)
model_physical_PhysicalColumn = Class(name="model_physical_PhysicalColumn")
model_physical_PhysicalPrimaryKey = Class(name="model_physical_PhysicalPrimaryKey")
model_physical_PhysicalForeignKey = Class(name="model_physical_PhysicalForeignKey")
model_physical_PhysicalTable = Class(name="model_physical_PhysicalTable")
PhysicalColumn = Class(name="PhysicalColumn")
BusinessRelationship = Class(name="BusinessRelationship")
BusinessIdentifier = Class(name="BusinessIdentifier")
BusinessDomain = Class(name="BusinessDomain")
BusinessViewInnerJoinRelationship = Class(name="BusinessViewInnerJoinRelationship")
model_business_BusinessColumn = Class(name="model_business_BusinessColumn")
model_business_BusinessColumnSet = Class(name="model_business_BusinessColumnSet")
BusinessColumn = Class(name="BusinessColumn")
model_business_BusinessTable = Class(name="model_business_BusinessTable")
model_business_BusinessView = Class(name="model_business_BusinessView")
model_business_BusinessRelationship = Class(name="model_business_BusinessRelationship")
model_business_BusinessModel = Class(name="model_business_BusinessModel")
business_model_Model = Class(name="business_model_Model")
BusinessColumnSet = Class(name="BusinessColumnSet")
model_business_BusinessDomain = Class(name="model_business_BusinessDomain")
model_business_BusinessIdentifier = Class(name="model_business_BusinessIdentifier")
model_business_BusinessViewInnerJoinRelationship = Class(name="model_business_BusinessViewInnerJoinRelationship")
model_business_SimpleBusinessColumn = Class(name="model_business_SimpleBusinessColumn")
Cube = Class(name="Cube")
VirtualCube = Class(name="VirtualCube")
Dimension = Class(name="Dimension")
model_olap_Cube = Class(name="model_olap_Cube")
Measure = Class(name="Measure")
CalculatedMember = Class(name="CalculatedMember")
NamedSet = Class(name="NamedSet")
model_olap_Dimension = Class(name="model_olap_Dimension")
Hierarchy = Class(name="Hierarchy")
model_business_CalculatedBusinessColumn = Class(name="model_business_CalculatedBusinessColumn")
model_olap_OlapModel = Class(name="model_olap_OlapModel")
olap_model_Model = Class(name="olap_model_Model")
model_olap_Level = Class(name="model_olap_Level")
model_olap_Measure = Class(name="model_olap_Measure")
model_olap_CalculatedMember = Class(name="model_olap_CalculatedMember")
model_olap_Hierarchy = Class(name="model_olap_Hierarchy")
Level = Class(name="Level")
VirtualCubeMeasure = Class(name="VirtualCubeMeasure")
model_olap_VirtualCubeDimension = Class(name="model_olap_VirtualCubeDimension")
model_olap_VirtualCubeMeasure = Class(name="model_olap_VirtualCubeMeasure")
model_olap_NamedSet = Class(name="model_olap_NamedSet")
model_olap_VirtualCube = Class(name="model_olap_VirtualCube")
VirtualCubeDimension = Class(name="VirtualCubeDimension")
model_behavioural_BehaviouralModel = Class(name="model_behavioural_BehaviouralModel")
model_analytical_AnalyticalModel = Class(name="model_analytical_AnalyticalModel")

# model_ModelPropertyCategory class attributes and methods
model_ModelPropertyCategory_name: Property = Property(name="name", type=StringType)
model_ModelPropertyCategory_description: Property = Property(name="description", type=StringType)
model_ModelPropertyCategory.attributes={model_ModelPropertyCategory_name, model_ModelPropertyCategory_description}

# model_ModelPropertyType class attributes and methods
model_ModelPropertyType_id: Property = Property(name="id", type=StringType)
model_ModelPropertyType_name: Property = Property(name="name", type=StringType)
model_ModelPropertyType_description: Property = Property(name="description", type=StringType)
model_ModelPropertyType_admissibleValues: Property = Property(name="admissibleValues", type=StringType)
model_ModelPropertyType_defaultValue: Property = Property(name="defaultValue", type=StringType)
model_ModelPropertyType.attributes={model_ModelPropertyType_name, model_ModelPropertyType_id, model_ModelPropertyType_defaultValue, model_ModelPropertyType_description, model_ModelPropertyType_admissibleValues}

# model_ModelProperty class attributes and methods
model_ModelProperty_value: Property = Property(name="value", type=StringType)
model_ModelProperty.attributes={model_ModelProperty_value}

# model_Model class attributes and methods

# ModelObject class attributes and methods

# PhysicalModel class attributes and methods

# BusinessModel class attributes and methods

# OlapModel class attributes and methods

# model_physical_PhysicalModel class attributes and methods
model_physical_PhysicalModel_databaseName: Property = Property(name="databaseName", type=StringType)
model_physical_PhysicalModel_databaseVersion: Property = Property(name="databaseVersion", type=StringType)
model_physical_PhysicalModel_catalog: Property = Property(name="catalog", type=StringType)
model_physical_PhysicalModel_schema: Property = Property(name="schema", type=StringType)
model_physical_PhysicalModel.attributes={model_physical_PhysicalModel_catalog, model_physical_PhysicalModel_databaseVersion, model_physical_PhysicalModel_schema, model_physical_PhysicalModel_databaseName}

# physical_model_Model class attributes and methods

# PhysicalTable class attributes and methods

# PhysicalPrimaryKey class attributes and methods

# PhysicalForeignKey class attributes and methods

# model_ModelPropertyMapEntry class attributes and methods
model_ModelPropertyMapEntry_key: Property = Property(name="key", type=StringType)
model_ModelPropertyMapEntry.attributes={model_ModelPropertyMapEntry_key}

# model_ModelObject class attributes and methods
model_ModelObject_uniqueName: Property = Property(name="uniqueName", type=StringType)
model_ModelObject_description: Property = Property(name="description", type=StringType)
model_ModelObject_id: Property = Property(name="id", type=StringType)
model_ModelObject_name: Property = Property(name="name", type=StringType)
model_ModelObject.attributes={model_ModelObject_uniqueName, model_ModelObject_id, model_ModelObject_description, model_ModelObject_name}

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
model_physical_PhysicalColumn.attributes={model_physical_PhysicalColumn_position, model_physical_PhysicalColumn_comment, model_physical_PhysicalColumn_typeName, model_physical_PhysicalColumn_octectLength, model_physical_PhysicalColumn_dataType, model_physical_PhysicalColumn_decimalDigits, model_physical_PhysicalColumn_size, model_physical_PhysicalColumn_radix, model_physical_PhysicalColumn_nullable, model_physical_PhysicalColumn_defaultValue}

# model_physical_PhysicalPrimaryKey class attributes and methods

# model_physical_PhysicalForeignKey class attributes and methods
model_physical_PhysicalForeignKey_sourceName: Property = Property(name="sourceName", type=StringType)
model_physical_PhysicalForeignKey_destinationName: Property = Property(name="destinationName", type=StringType)
model_physical_PhysicalForeignKey.attributes={model_physical_PhysicalForeignKey_sourceName, model_physical_PhysicalForeignKey_destinationName}

# model_physical_PhysicalTable class attributes and methods
model_physical_PhysicalTable_comment: Property = Property(name="comment", type=StringType)
model_physical_PhysicalTable_type: Property = Property(name="type", type=StringType)
model_physical_PhysicalTable.attributes={model_physical_PhysicalTable_type, model_physical_PhysicalTable_comment}

# PhysicalColumn class attributes and methods

# BusinessRelationship class attributes and methods

# BusinessIdentifier class attributes and methods

# BusinessDomain class attributes and methods

# BusinessViewInnerJoinRelationship class attributes and methods

# model_business_BusinessColumn class attributes and methods

# model_business_BusinessColumnSet class attributes and methods

# BusinessColumn class attributes and methods

# model_business_BusinessTable class attributes and methods

# model_business_BusinessView class attributes and methods

# model_business_BusinessRelationship class attributes and methods

# model_business_BusinessModel class attributes and methods

# business_model_Model class attributes and methods

# BusinessColumnSet class attributes and methods

# model_business_BusinessDomain class attributes and methods

# model_business_BusinessIdentifier class attributes and methods

# model_business_BusinessViewInnerJoinRelationship class attributes and methods

# model_business_SimpleBusinessColumn class attributes and methods

# Cube class attributes and methods

# VirtualCube class attributes and methods

# Dimension class attributes and methods

# model_olap_Cube class attributes and methods

# Measure class attributes and methods

# CalculatedMember class attributes and methods

# NamedSet class attributes and methods

# model_olap_Dimension class attributes and methods

# Hierarchy class attributes and methods

# model_business_CalculatedBusinessColumn class attributes and methods

# model_olap_OlapModel class attributes and methods

# olap_model_Model class attributes and methods

# model_olap_Level class attributes and methods

# model_olap_Measure class attributes and methods

# model_olap_CalculatedMember class attributes and methods

# model_olap_Hierarchy class attributes and methods

# Level class attributes and methods

# VirtualCubeMeasure class attributes and methods

# model_olap_VirtualCubeDimension class attributes and methods

# model_olap_VirtualCubeMeasure class attributes and methods

# model_olap_NamedSet class attributes and methods

# model_olap_VirtualCube class attributes and methods

# VirtualCubeDimension class attributes and methods

# model_behavioural_BehaviouralModel class attributes and methods

# model_analytical_AnalyticalModel class attributes and methods

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
properties10: BinaryAssociation = BinaryAssociation(
    name="properties10",
    ends={
        Property(name="model_ModelPropertyMapEntry11", type=model_ModelObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ModelObject", type=model_ModelPropertyMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalModels12: BinaryAssociation = BinaryAssociation(
    name="physicalModels12",
    ends={
        Property(name="PhysicalModel", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="parentModel", type=PhysicalModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
businessModels13: BinaryAssociation = BinaryAssociation(
    name="businessModels13",
    ends={
        Property(name="BusinessModel", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="parentModel14", type=BusinessModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
olapModels15: BinaryAssociation = BinaryAssociation(
    name="olapModels15",
    ends={
        Property(name="OlapModel", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="parentModel16", type=OlapModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyTypes17: BinaryAssociation = BinaryAssociation(
    name="propertyTypes17",
    ends={
        Property(name="model_ModelPropertyType18", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Model", type=model_ModelPropertyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propertyCategories19: BinaryAssociation = BinaryAssociation(
    name="propertyCategories19",
    ends={
        Property(name="model_ModelPropertyCategory21", type=model_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Model20", type=model_ModelPropertyCategory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentModel22: BinaryAssociation = BinaryAssociation(
    name="parentModel22",
    ends={
        Property(name="Model", type=model_physical_PhysicalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="physicalModels", type=physical_model_Model, multiplicity=Multiplicity(1, 1))
    }
)
tables23: BinaryAssociation = BinaryAssociation(
    name="tables23",
    ends={
        Property(name="PhysicalTable", type=model_physical_PhysicalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=PhysicalTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKeys24: BinaryAssociation = BinaryAssociation(
    name="primaryKeys24",
    ends={
        Property(name="PhysicalPrimaryKey", type=model_physical_PhysicalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model25", type=PhysicalPrimaryKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeys26: BinaryAssociation = BinaryAssociation(
    name="foreignKeys26",
    ends={
        Property(name="PhysicalForeignKey", type=model_physical_PhysicalModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model27", type=PhysicalForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
table31: BinaryAssociation = BinaryAssociation(
    name="table31",
    ends={
        Property(name="PhysicalTable32", type=model_physical_PhysicalColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
model33: BinaryAssociation = BinaryAssociation(
    name="model33",
    ends={
        Property(name="PhysicalModel34", type=model_physical_PhysicalPrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="primaryKeys", type=PhysicalModel, multiplicity=Multiplicity(1, 1))
    }
)
table35: BinaryAssociation = BinaryAssociation(
    name="table35",
    ends={
        Property(name="PhysicalTable36", type=model_physical_PhysicalPrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalPrimaryKey", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
columns37: BinaryAssociation = BinaryAssociation(
    name="columns37",
    ends={
        Property(name="PhysicalColumn39", type=model_physical_PhysicalPrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalPrimaryKey38", type=PhysicalColumn, multiplicity=Multiplicity(1, 9999))
    }
)
sourceTable40: BinaryAssociation = BinaryAssociation(
    name="sourceTable40",
    ends={
        Property(name="PhysicalTable41", type=model_physical_PhysicalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalForeignKey", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
sourceColumns42: BinaryAssociation = BinaryAssociation(
    name="sourceColumns42",
    ends={
        Property(name="PhysicalColumn44", type=model_physical_PhysicalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalForeignKey43", type=PhysicalColumn, multiplicity=Multiplicity(1, 9999))
    }
)
destinationTable45: BinaryAssociation = BinaryAssociation(
    name="destinationTable45",
    ends={
        Property(name="PhysicalTable47", type=model_physical_PhysicalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalForeignKey46", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
destinationColumns48: BinaryAssociation = BinaryAssociation(
    name="destinationColumns48",
    ends={
        Property(name="PhysicalColumn50", type=model_physical_PhysicalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="model_physical_PhysicalForeignKey49", type=PhysicalColumn, multiplicity=Multiplicity(1, 9999))
    }
)
model51: BinaryAssociation = BinaryAssociation(
    name="model51",
    ends={
        Property(name="PhysicalModel52", type=model_physical_PhysicalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=PhysicalModel, multiplicity=Multiplicity(0, 1))
    }
)
model28: BinaryAssociation = BinaryAssociation(
    name="model28",
    ends={
        Property(name="PhysicalModel29", type=model_physical_PhysicalTable, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=PhysicalModel, multiplicity=Multiplicity(1, 1))
    }
)
columns30: BinaryAssociation = BinaryAssociation(
    name="columns30",
    ends={
        Property(name="PhysicalColumn", type=model_physical_PhysicalTable, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=PhysicalColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables57: BinaryAssociation = BinaryAssociation(
    name="tables57",
    ends={
        Property(name="model58", type=BusinessColumnSet, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="BusinessColumnSet", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1))
    }
)
relationships59: BinaryAssociation = BinaryAssociation(
    name="relationships59",
    ends={
        Property(name="BusinessRelationship", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model60", type=BusinessRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifiers61: BinaryAssociation = BinaryAssociation(
    name="identifiers61",
    ends={
        Property(name="BusinessIdentifier", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model62", type=BusinessIdentifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domains63: BinaryAssociation = BinaryAssociation(
    name="domains63",
    ends={
        Property(name="BusinessDomain", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model64", type=BusinessDomain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
joinRelationships65: BinaryAssociation = BinaryAssociation(
    name="joinRelationships65",
    ends={
        Property(name="BusinessViewInnerJoinRelationship", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model66", type=BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table67: BinaryAssociation = BinaryAssociation(
    name="table67",
    ends={
        Property(name="BusinessColumnSet69", type=model_business_BusinessColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="columns68", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
model70: BinaryAssociation = BinaryAssociation(
    name="model70",
    ends={
        Property(name="BusinessModel72", type=model_business_BusinessColumnSet, multiplicity=Multiplicity(1, 1)),
        Property(name="tables71", type=BusinessModel, multiplicity=Multiplicity(1, 1))
    }
)
columns73: BinaryAssociation = BinaryAssociation(
    name="columns73",
    ends={
        Property(name="BusinessColumn", type=model_business_BusinessColumnSet, multiplicity=Multiplicity(1, 1)),
        Property(name="table74", type=BusinessColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
physicalTable75: BinaryAssociation = BinaryAssociation(
    name="physicalTable75",
    ends={
        Property(name="PhysicalTable76", type=model_business_BusinessTable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessTable", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
joinRelationships77: BinaryAssociation = BinaryAssociation(
    name="joinRelationships77",
    ends={
        Property(name="BusinessViewInnerJoinRelationship78", type=model_business_BusinessView, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessView", type=BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
model79: BinaryAssociation = BinaryAssociation(
    name="model79",
    ends={
        Property(name="BusinessModel80", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="relationships", type=BusinessModel, multiplicity=Multiplicity(1, 1))
    }
)
sourceTable81: BinaryAssociation = BinaryAssociation(
    name="sourceTable81",
    ends={
        Property(name="BusinessColumnSet82", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessRelationship", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
parentModel53: BinaryAssociation = BinaryAssociation(
    name="parentModel53",
    ends={
        Property(name="Model54", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="businessModels", type=business_model_Model, multiplicity=Multiplicity(1, 1))
    }
)
physicalModel55: BinaryAssociation = BinaryAssociation(
    name="physicalModel55",
    ends={
        Property(name="PhysicalModel56", type=model_business_BusinessModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessModel", type=PhysicalModel, multiplicity=Multiplicity(1, 1))
    }
)
model95: BinaryAssociation = BinaryAssociation(
    name="model95",
    ends={
        Property(name="BusinessModel96", type=model_business_BusinessDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="domains", type=BusinessModel, multiplicity=Multiplicity(1, 1))
    }
)
tables97: BinaryAssociation = BinaryAssociation(
    name="tables97",
    ends={
        Property(name="BusinessColumnSet98", type=model_business_BusinessDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessDomain", type=BusinessColumnSet, multiplicity=Multiplicity(0, 9999))
    }
)
relationships99: BinaryAssociation = BinaryAssociation(
    name="relationships99",
    ends={
        Property(name="BusinessRelationship101", type=model_business_BusinessDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessDomain100", type=BusinessRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
model102: BinaryAssociation = BinaryAssociation(
    name="model102",
    ends={
        Property(name="BusinessModel103", type=model_business_BusinessIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="identifiers", type=BusinessModel, multiplicity=Multiplicity(0, 1))
    }
)
table104: BinaryAssociation = BinaryAssociation(
    name="table104",
    ends={
        Property(name="BusinessColumnSet105", type=model_business_BusinessIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessIdentifier", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
columns106: BinaryAssociation = BinaryAssociation(
    name="columns106",
    ends={
        Property(name="BusinessColumn108", type=model_business_BusinessIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessIdentifier107", type=BusinessColumn, multiplicity=Multiplicity(1, 9999))
    }
)
physicalPrimaryKey109: BinaryAssociation = BinaryAssociation(
    name="physicalPrimaryKey109",
    ends={
        Property(name="PhysicalPrimaryKey111", type=model_business_BusinessIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessIdentifier110", type=PhysicalPrimaryKey, multiplicity=Multiplicity(0, 1))
    }
)
model112: BinaryAssociation = BinaryAssociation(
    name="model112",
    ends={
        Property(name="BusinessModel113", type=model_business_BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="joinRelationships", type=BusinessModel, multiplicity=Multiplicity(1, 1))
    }
)
sourceTable114: BinaryAssociation = BinaryAssociation(
    name="sourceTable114",
    ends={
        Property(name="PhysicalTable115", type=model_business_BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessViewInnerJoinRelationship", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
destinationTable116: BinaryAssociation = BinaryAssociation(
    name="destinationTable116",
    ends={
        Property(name="PhysicalTable118", type=model_business_BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessViewInnerJoinRelationship117", type=PhysicalTable, multiplicity=Multiplicity(1, 1))
    }
)
sourceColumns119: BinaryAssociation = BinaryAssociation(
    name="sourceColumns119",
    ends={
        Property(name="PhysicalColumn121", type=model_business_BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessViewInnerJoinRelationship120", type=PhysicalColumn, multiplicity=Multiplicity(0, 9999))
    }
)
destinationColumns122: BinaryAssociation = BinaryAssociation(
    name="destinationColumns122",
    ends={
        Property(name="PhysicalColumn124", type=model_business_BusinessViewInnerJoinRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessViewInnerJoinRelationship123", type=PhysicalColumn, multiplicity=Multiplicity(0, 9999))
    }
)
physicalColumn125: BinaryAssociation = BinaryAssociation(
    name="physicalColumn125",
    ends={
        Property(name="PhysicalColumn126", type=model_business_SimpleBusinessColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_SimpleBusinessColumn", type=PhysicalColumn, multiplicity=Multiplicity(1, 1))
    }
)
destinationTable83: BinaryAssociation = BinaryAssociation(
    name="destinationTable83",
    ends={
        Property(name="BusinessColumnSet85", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessRelationship84", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
sourceColumns86: BinaryAssociation = BinaryAssociation(
    name="sourceColumns86",
    ends={
        Property(name="BusinessColumn88", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessRelationship87", type=BusinessColumn, multiplicity=Multiplicity(0, 9999))
    }
)
destinationColumns89: BinaryAssociation = BinaryAssociation(
    name="destinationColumns89",
    ends={
        Property(name="BusinessColumn91", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessRelationship90", type=BusinessColumn, multiplicity=Multiplicity(0, 9999))
    }
)
physicalForeignKey92: BinaryAssociation = BinaryAssociation(
    name="physicalForeignKey92",
    ends={
        Property(name="PhysicalForeignKey94", type=model_business_BusinessRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="model_business_BusinessRelationship93", type=PhysicalForeignKey, multiplicity=Multiplicity(0, 1))
    }
)
cubes129: BinaryAssociation = BinaryAssociation(
    name="cubes129",
    ends={
        Property(name="Cube", type=model_olap_OlapModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model130", type=Cube, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
virtualCubes131: BinaryAssociation = BinaryAssociation(
    name="virtualCubes131",
    ends={
        Property(name="VirtualCube", type=model_olap_OlapModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model132", type=VirtualCube, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dimensions133: BinaryAssociation = BinaryAssociation(
    name="dimensions133",
    ends={
        Property(name="Dimension", type=model_olap_OlapModel, multiplicity=Multiplicity(1, 1)),
        Property(name="model134", type=Dimension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model135: BinaryAssociation = BinaryAssociation(
    name="model135",
    ends={
        Property(name="OlapModel136", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="cubes", type=OlapModel, multiplicity=Multiplicity(0, 1))
    }
)
table137: BinaryAssociation = BinaryAssociation(
    name="table137",
    ends={
        Property(name="BusinessColumnSet138", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Cube", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
dimensions139: BinaryAssociation = BinaryAssociation(
    name="dimensions139",
    ends={
        Property(name="Dimension141", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Cube140", type=Dimension, multiplicity=Multiplicity(1, 9999))
    }
)
measures142: BinaryAssociation = BinaryAssociation(
    name="measures142",
    ends={
        Property(name="Measure", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="cube", type=Measure, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
calculatedMembers143: BinaryAssociation = BinaryAssociation(
    name="calculatedMembers143",
    ends={
        Property(name="CalculatedMember", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="cube144", type=CalculatedMember, multiplicity=Multiplicity(0, 1))
    }
)
namedSets145: BinaryAssociation = BinaryAssociation(
    name="namedSets145",
    ends={
        Property(name="NamedSet", type=model_olap_Cube, multiplicity=Multiplicity(1, 1)),
        Property(name="cube146", type=NamedSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table147: BinaryAssociation = BinaryAssociation(
    name="table147",
    ends={
        Property(name="BusinessColumnSet148", type=model_olap_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Dimension", type=BusinessColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
hierarchies149: BinaryAssociation = BinaryAssociation(
    name="hierarchies149",
    ends={
        Property(name="Hierarchy", type=model_olap_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dimension", type=Hierarchy, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
model150: BinaryAssociation = BinaryAssociation(
    name="model150",
    ends={
        Property(name="OlapModel151", type=model_olap_Dimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dimensions", type=OlapModel, multiplicity=Multiplicity(0, 1))
    }
)
parentModel127: BinaryAssociation = BinaryAssociation(
    name="parentModel127",
    ends={
        Property(name="Model128", type=model_olap_OlapModel, multiplicity=Multiplicity(1, 1)),
        Property(name="olapModels", type=olap_model_Model, multiplicity=Multiplicity(1, 1))
    }
)
hierarchy157: BinaryAssociation = BinaryAssociation(
    name="hierarchy157",
    ends={
        Property(name="Hierarchy158", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="levels", type=Hierarchy, multiplicity=Multiplicity(0, 1))
    }
)
column159: BinaryAssociation = BinaryAssociation(
    name="column159",
    ends={
        Property(name="BusinessColumn160", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Level", type=BusinessColumn, multiplicity=Multiplicity(0, 1))
    }
)
ordinalColumn161: BinaryAssociation = BinaryAssociation(
    name="ordinalColumn161",
    ends={
        Property(name="BusinessColumn163", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Level162", type=BusinessColumn, multiplicity=Multiplicity(0, 1))
    }
)
nameColumn164: BinaryAssociation = BinaryAssociation(
    name="nameColumn164",
    ends={
        Property(name="BusinessColumn166", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Level165", type=BusinessColumn, multiplicity=Multiplicity(0, 1))
    }
)
captionColumn167: BinaryAssociation = BinaryAssociation(
    name="captionColumn167",
    ends={
        Property(name="BusinessColumn169", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Level168", type=BusinessColumn, multiplicity=Multiplicity(0, 1))
    }
)
propertyColumns170: BinaryAssociation = BinaryAssociation(
    name="propertyColumns170",
    ends={
        Property(name="BusinessColumn172", type=model_olap_Level, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Level171", type=BusinessColumn, multiplicity=Multiplicity(0, 9999))
    }
)
cube173: BinaryAssociation = BinaryAssociation(
    name="cube173",
    ends={
        Property(name="Cube174", type=model_olap_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="measures", type=Cube, multiplicity=Multiplicity(0, 1))
    }
)
column175: BinaryAssociation = BinaryAssociation(
    name="column175",
    ends={
        Property(name="BusinessColumn176", type=model_olap_Measure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Measure", type=BusinessColumn, multiplicity=Multiplicity(0, 1))
    }
)
cube177: BinaryAssociation = BinaryAssociation(
    name="cube177",
    ends={
        Property(name="Cube178", type=model_olap_CalculatedMember, multiplicity=Multiplicity(1, 1)),
        Property(name="calculatedMembers", type=Cube, multiplicity=Multiplicity(0, 1))
    }
)
hierarchy179: BinaryAssociation = BinaryAssociation(
    name="hierarchy179",
    ends={
        Property(name="Hierarchy180", type=model_olap_CalculatedMember, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_CalculatedMember", type=Hierarchy, multiplicity=Multiplicity(0, 1))
    }
)
table152: BinaryAssociation = BinaryAssociation(
    name="table152",
    ends={
        Property(name="BusinessColumnSet153", type=model_olap_Hierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_Hierarchy", type=BusinessColumnSet, multiplicity=Multiplicity(0, 1))
    }
)
dimension154: BinaryAssociation = BinaryAssociation(
    name="dimension154",
    ends={
        Property(name="Dimension155", type=model_olap_Hierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="hierarchies", type=Dimension, multiplicity=Multiplicity(0, 1))
    }
)
levels156: BinaryAssociation = BinaryAssociation(
    name="levels156",
    ends={
        Property(name="Level", type=model_olap_Hierarchy, multiplicity=Multiplicity(1, 1)),
        Property(name="hierarchy", type=Level, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
measures186: BinaryAssociation = BinaryAssociation(
    name="measures186",
    ends={
        Property(name="VirtualCubeMeasure", type=model_olap_VirtualCube, multiplicity=Multiplicity(1, 1)),
        Property(name="virtualCube187", type=VirtualCubeMeasure, multiplicity=Multiplicity(0, 9999))
    }
)
calculatedMembers188: BinaryAssociation = BinaryAssociation(
    name="calculatedMembers188",
    ends={
        Property(name="CalculatedMember190", type=model_olap_VirtualCube, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCube189", type=CalculatedMember, multiplicity=Multiplicity(0, 9999))
    }
)
model191: BinaryAssociation = BinaryAssociation(
    name="model191",
    ends={
        Property(name="OlapModel192", type=model_olap_VirtualCube, multiplicity=Multiplicity(1, 1)),
        Property(name="virtualCubes", type=OlapModel, multiplicity=Multiplicity(0, 1))
    }
)
virtualCube193: BinaryAssociation = BinaryAssociation(
    name="virtualCube193",
    ends={
        Property(name="VirtualCube195", type=model_olap_VirtualCubeDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="dimensions194", type=VirtualCube, multiplicity=Multiplicity(0, 1))
    }
)
cube196: BinaryAssociation = BinaryAssociation(
    name="cube196",
    ends={
        Property(name="Cube197", type=model_olap_VirtualCubeDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCubeDimension", type=Cube, multiplicity=Multiplicity(0, 1))
    }
)
dimension198: BinaryAssociation = BinaryAssociation(
    name="dimension198",
    ends={
        Property(name="Dimension200", type=model_olap_VirtualCubeDimension, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCubeDimension199", type=Dimension, multiplicity=Multiplicity(0, 1))
    }
)
virtualCube201: BinaryAssociation = BinaryAssociation(
    name="virtualCube201",
    ends={
        Property(name="VirtualCube203", type=model_olap_VirtualCubeMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="measures202", type=VirtualCube, multiplicity=Multiplicity(0, 1))
    }
)
cube204: BinaryAssociation = BinaryAssociation(
    name="cube204",
    ends={
        Property(name="Cube205", type=model_olap_VirtualCubeMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCubeMeasure", type=Cube, multiplicity=Multiplicity(0, 1))
    }
)
cube181: BinaryAssociation = BinaryAssociation(
    name="cube181",
    ends={
        Property(name="Cube182", type=model_olap_NamedSet, multiplicity=Multiplicity(1, 1)),
        Property(name="namedSets", type=Cube, multiplicity=Multiplicity(0, 1))
    }
)
cubes183: BinaryAssociation = BinaryAssociation(
    name="cubes183",
    ends={
        Property(name="Cube184", type=model_olap_VirtualCube, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCube", type=Cube, multiplicity=Multiplicity(0, 9999))
    }
)
dimensions185: BinaryAssociation = BinaryAssociation(
    name="dimensions185",
    ends={
        Property(name="VirtualCubeDimension", type=model_olap_VirtualCube, multiplicity=Multiplicity(1, 1)),
        Property(name="virtualCube", type=VirtualCubeDimension, multiplicity=Multiplicity(0, 1))
    }
)
measure206: BinaryAssociation = BinaryAssociation(
    name="measure206",
    ends={
        Property(name="Measure208", type=model_olap_VirtualCubeMeasure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_olap_VirtualCubeMeasure207", type=Measure, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model_Model_ModelObject = Generalization(general=ModelObject, specific=model_Model)
gen_model_physical_PhysicalModel_ModelObject = Generalization(general=ModelObject, specific=model_physical_PhysicalModel)
gen_model_physical_PhysicalColumn_ModelObject = Generalization(general=ModelObject, specific=model_physical_PhysicalColumn)
gen_model_physical_PhysicalPrimaryKey_ModelObject = Generalization(general=ModelObject, specific=model_physical_PhysicalPrimaryKey)
gen_model_physical_PhysicalForeignKey_ModelObject = Generalization(general=ModelObject, specific=model_physical_PhysicalForeignKey)
gen_model_physical_PhysicalTable_ModelObject = Generalization(general=ModelObject, specific=model_physical_PhysicalTable)
gen_model_business_BusinessColumn_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessColumn)
gen_model_business_BusinessColumnSet_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessColumnSet)
gen_model_business_BusinessTable_BusinessColumnSet = Generalization(general=BusinessColumnSet, specific=model_business_BusinessTable)
gen_model_business_BusinessView_BusinessColumnSet = Generalization(general=BusinessColumnSet, specific=model_business_BusinessView)
gen_model_business_BusinessRelationship_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessRelationship)
gen_model_business_BusinessModel_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessModel)
gen_model_business_BusinessDomain_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessDomain)
gen_model_business_BusinessIdentifier_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessIdentifier)
gen_model_business_BusinessViewInnerJoinRelationship_ModelObject = Generalization(general=ModelObject, specific=model_business_BusinessViewInnerJoinRelationship)
gen_model_business_SimpleBusinessColumn_BusinessColumn = Generalization(general=BusinessColumn, specific=model_business_SimpleBusinessColumn)
gen_model_olap_Cube_ModelObject = Generalization(general=ModelObject, specific=model_olap_Cube)
gen_model_olap_Dimension_ModelObject = Generalization(general=ModelObject, specific=model_olap_Dimension)
gen_model_business_CalculatedBusinessColumn_BusinessColumn = Generalization(general=BusinessColumn, specific=model_business_CalculatedBusinessColumn)
gen_model_olap_OlapModel_ModelObject = Generalization(general=ModelObject, specific=model_olap_OlapModel)
gen_model_olap_Level_ModelObject = Generalization(general=ModelObject, specific=model_olap_Level)
gen_model_olap_Measure_ModelObject = Generalization(general=ModelObject, specific=model_olap_Measure)
gen_model_olap_CalculatedMember_ModelObject = Generalization(general=ModelObject, specific=model_olap_CalculatedMember)
gen_model_olap_Hierarchy_ModelObject = Generalization(general=ModelObject, specific=model_olap_Hierarchy)
gen_model_olap_VirtualCubeDimension_ModelObject = Generalization(general=ModelObject, specific=model_olap_VirtualCubeDimension)
gen_model_olap_VirtualCubeMeasure_ModelObject = Generalization(general=ModelObject, specific=model_olap_VirtualCubeMeasure)
gen_model_olap_NamedSet_ModelObject = Generalization(general=ModelObject, specific=model_olap_NamedSet)
gen_model_olap_VirtualCube_ModelObject = Generalization(general=ModelObject, specific=model_olap_VirtualCube)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_ModelPropertyCategory, model_ModelPropertyType, model_ModelProperty, model_Model, ModelObject, PhysicalModel, BusinessModel, OlapModel, model_physical_PhysicalModel, physical_model_Model, PhysicalTable, PhysicalPrimaryKey, PhysicalForeignKey, model_ModelPropertyMapEntry, model_ModelObject, model_physical_PhysicalColumn, model_physical_PhysicalPrimaryKey, model_physical_PhysicalForeignKey, model_physical_PhysicalTable, PhysicalColumn, BusinessRelationship, BusinessIdentifier, BusinessDomain, BusinessViewInnerJoinRelationship, model_business_BusinessColumn, model_business_BusinessColumnSet, BusinessColumn, model_business_BusinessTable, model_business_BusinessView, model_business_BusinessRelationship, model_business_BusinessModel, business_model_Model, BusinessColumnSet, model_business_BusinessDomain, model_business_BusinessIdentifier, model_business_BusinessViewInnerJoinRelationship, model_business_SimpleBusinessColumn, Cube, VirtualCube, Dimension, model_olap_Cube, Measure, CalculatedMember, NamedSet, model_olap_Dimension, Hierarchy, model_business_CalculatedBusinessColumn, model_olap_OlapModel, olap_model_Model, model_olap_Level, model_olap_Measure, model_olap_CalculatedMember, model_olap_Hierarchy, Level, VirtualCubeMeasure, model_olap_VirtualCubeDimension, model_olap_VirtualCubeMeasure, model_olap_NamedSet, model_olap_VirtualCube, VirtualCubeDimension, model_behavioural_BehaviouralModel, model_analytical_AnalyticalModel},
    associations={parentCategory1, subCategories3, propertyTypes5, category6, properties10, physicalModels12, businessModels13, olapModels15, propertyTypes17, propertyCategories19, parentModel22, tables23, primaryKeys24, foreignKeys26, propertyType7, value8, table31, model33, table35, columns37, sourceTable40, sourceColumns42, destinationTable45, destinationColumns48, model51, model28, columns30, tables57, relationships59, identifiers61, domains63, joinRelationships65, table67, model70, columns73, physicalTable75, joinRelationships77, model79, sourceTable81, parentModel53, physicalModel55, model95, tables97, relationships99, model102, table104, columns106, physicalPrimaryKey109, model112, sourceTable114, destinationTable116, sourceColumns119, destinationColumns122, physicalColumn125, destinationTable83, sourceColumns86, destinationColumns89, physicalForeignKey92, cubes129, virtualCubes131, dimensions133, model135, table137, dimensions139, measures142, calculatedMembers143, namedSets145, table147, hierarchies149, model150, parentModel127, hierarchy157, column159, ordinalColumn161, nameColumn164, captionColumn167, propertyColumns170, cube173, column175, cube177, hierarchy179, table152, dimension154, levels156, measures186, calculatedMembers188, model191, virtualCube193, cube196, dimension198, virtualCube201, cube204, cube181, cubes183, dimensions185, measure206},
    generalizations={gen_model_Model_ModelObject, gen_model_physical_PhysicalModel_ModelObject, gen_model_physical_PhysicalColumn_ModelObject, gen_model_physical_PhysicalPrimaryKey_ModelObject, gen_model_physical_PhysicalForeignKey_ModelObject, gen_model_physical_PhysicalTable_ModelObject, gen_model_business_BusinessColumn_ModelObject, gen_model_business_BusinessColumnSet_ModelObject, gen_model_business_BusinessTable_BusinessColumnSet, gen_model_business_BusinessView_BusinessColumnSet, gen_model_business_BusinessRelationship_ModelObject, gen_model_business_BusinessModel_ModelObject, gen_model_business_BusinessDomain_ModelObject, gen_model_business_BusinessIdentifier_ModelObject, gen_model_business_BusinessViewInnerJoinRelationship_ModelObject, gen_model_business_SimpleBusinessColumn_BusinessColumn, gen_model_olap_Cube_ModelObject, gen_model_olap_Dimension_ModelObject, gen_model_business_CalculatedBusinessColumn_BusinessColumn, gen_model_olap_OlapModel_ModelObject, gen_model_olap_Level_ModelObject, gen_model_olap_Measure_ModelObject, gen_model_olap_CalculatedMember_ModelObject, gen_model_olap_Hierarchy_ModelObject, gen_model_olap_VirtualCubeDimension_ModelObject, gen_model_olap_VirtualCubeMeasure_ModelObject, gen_model_olap_NamedSet_ModelObject, gen_model_olap_VirtualCube_ModelObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)