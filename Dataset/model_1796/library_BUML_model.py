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
LevelType: Enumeration = Enumeration(
    name="LevelType",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="AMBER"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="YELLOW")
    }
)

StateType: Enumeration = Enumeration(
    name="StateType",
    literals={
            EnumerationLiteral(name="ACTIVE"),
			EnumerationLiteral(name="STANDBY"),
			EnumerationLiteral(name="IDLE"),
			EnumerationLiteral(name="DEFECT"),
			EnumerationLiteral(name="RESERVED")
    }
)

RedundancyType: Enumeration = Enumeration(
    name="RedundancyType",
    literals={
            EnumerationLiteral(name="n"),
			EnumerationLiteral(name="n1"),
			EnumerationLiteral(name="_11")
    }
)

# Classes
library_Equipment = Class(name="library::Equipment")
library_Lifecycle = Class(name="library::Lifecycle")
library_DiagramInfo = Class(name="library::DiagramInfo")
library_EquipmentGroup = Class(name="library::EquipmentGroup")
library_NetXResource = Class(name="library::NetXResource")
library_Metric = Class(name="library::Metric")
library_EquipmentRelationship = Class(name="library::EquipmentRelationship")
library_Expression = Class(name="library::Expression")
library_Tolerance = Class(name="library::Tolerance")
library_Protocol = Class(name="library::Protocol")
library_Parameter = Class(name="library::Parameter")
library_MultiImage = Class(name="library::MultiImage")
library_EObject = Class(name="library::EObject")
library_Function = Class(name="library::Function")
library_ServiceProfile = Class(name="library::ServiceProfile")
library_ExpressionResult = Class(name="library::ExpressionResult")
library_FunctionRelationship = Class(name="library::FunctionRelationship")
library_Library = Class(name="library::Library")
library_NodeType = Class(name="library::NodeType")
library_MetricSource = Class(name="library::MetricSource")
library_Unit = Class(name="library::Unit")
library_Meta = Class(name="library::Meta")
library_MetricValueRange = Class(name="library::MetricValueRange")
library_Value = Class(name="library::Value")
library_ProductInfo = Class(name="library::ProductInfo")
library_Vendor = Class(name="library::Vendor")
Company = Class(name="Company")

# library_Equipment class attributes and methods
library_Equipment_count: Property = Property(name="count", type=StringType)
library_Equipment_description: Property = Property(name="description", type=StringType)
library_Equipment_equipmentCode: Property = Property(name="equipmentCode", type=StringType)
library_Equipment_equipmentName: Property = Property(name="equipmentName", type=StringType)
library_Equipment_position: Property = Property(name="position", type=StringType)
library_Equipment_redundancy: Property = Property(name="redundancy", type=StringType)
library_Equipment_state: Property = Property(name="state", type=StringType)
library_Equipment.attributes={library_Equipment_count, library_Equipment_equipmentCode, library_Equipment_redundancy, library_Equipment_equipmentName, library_Equipment_state, library_Equipment_position, library_Equipment_description}

# library_Lifecycle class attributes and methods

# library_DiagramInfo class attributes and methods

# library_EquipmentGroup class attributes and methods
library_EquipmentGroup_count: Property = Property(name="count", type=StringType)
library_EquipmentGroup_description: Property = Property(name="description", type=StringType)
library_EquipmentGroup_name: Property = Property(name="name", type=StringType)
library_EquipmentGroup.attributes={library_EquipmentGroup_count, library_EquipmentGroup_name, library_EquipmentGroup_description}

# library_NetXResource class attributes and methods
library_NetXResource_detailDisplay: Property = Property(name="detailDisplay", type=StringType)
library_NetXResource_expressionName: Property = Property(name="expressionName", type=StringType)
library_NetXResource_longName: Property = Property(name="longName", type=StringType)
library_NetXResource_shortName: Property = Property(name="shortName", type=StringType)
library_NetXResource_summaryDisplay: Property = Property(name="summaryDisplay", type=StringType)
library_NetXResource.attributes={library_NetXResource_longName, library_NetXResource_detailDisplay, library_NetXResource_expressionName, library_NetXResource_summaryDisplay, library_NetXResource_shortName}

# library_Metric class attributes and methods

# library_EquipmentRelationship class attributes and methods

# library_Expression class attributes and methods
library_Expression_expressionLines: Property = Property(name="expressionLines", type=StringType)
library_Expression_name: Property = Property(name="name", type=StringType)
library_Expression.attributes={library_Expression_expressionLines, library_Expression_name}

# library_Tolerance class attributes and methods
library_Tolerance_expression: Property = Property(name="expression", type=StringType)
library_Tolerance_level: Property = Property(name="level", type=StringType)
library_Tolerance_name: Property = Property(name="name", type=StringType)
library_Tolerance.attributes={library_Tolerance_level, library_Tolerance_name, library_Tolerance_expression}

# library_Protocol class attributes and methods

# library_Parameter class attributes and methods
library_Parameter_modifiable: Property = Property(name="modifiable", type=StringType)
library_Parameter_name: Property = Property(name="name", type=StringType)
library_Parameter_value: Property = Property(name="value", type=StringType)
library_Parameter_description: Property = Property(name="description", type=StringType)
library_Parameter_expressionName: Property = Property(name="expressionName", type=StringType)
library_Parameter.attributes={library_Parameter_expressionName, library_Parameter_value, library_Parameter_description, library_Parameter_name, library_Parameter_modifiable}

# library_MultiImage class attributes and methods

# library_EObject class attributes and methods

# library_Function class attributes and methods
library_Function_description: Property = Property(name="description", type=StringType)
library_Function_functionName: Property = Property(name="functionName", type=StringType)
library_Function.attributes={library_Function_functionName, library_Function_description}

# library_ServiceProfile class attributes and methods

# library_ExpressionResult class attributes and methods

# library_FunctionRelationship class attributes and methods

# library_Library class attributes and methods
library_Library_protocols: Property = Property(name="protocols", type=StringType)
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name, library_Library_protocols}

# library_NodeType class attributes and methods
library_NodeType_leafNode: Property = Property(name="leafNode", type=StringType)
library_NodeType.attributes={library_NodeType_leafNode}

# library_MetricSource class attributes and methods

# library_Unit class attributes and methods
library_Unit_code: Property = Property(name="code", type=StringType)
library_Unit_description: Property = Property(name="description", type=StringType)
library_Unit_name: Property = Property(name="name", type=StringType)
library_Unit.attributes={library_Unit_name, library_Unit_description, library_Unit_code}

# library_Meta class attributes and methods

# library_MetricValueRange class attributes and methods

# library_Value class attributes and methods

# library_ProductInfo class attributes and methods
library_ProductInfo_availableDate: Property = Property(name="availableDate", type=StringType)
library_ProductInfo_endOfSalesDate: Property = Property(name="endOfSalesDate", type=StringType)
library_ProductInfo_endOfSupportDate: Property = Property(name="endOfSupportDate", type=StringType)
library_ProductInfo_productCode: Property = Property(name="productCode", type=StringType)
library_ProductInfo_salesCode: Property = Property(name="salesCode", type=StringType)
library_ProductInfo_underDevelopmentDate: Property = Property(name="underDevelopmentDate", type=StringType)
library_ProductInfo.attributes={library_ProductInfo_availableDate, library_ProductInfo_endOfSalesDate, library_ProductInfo_salesCode, library_ProductInfo_endOfSupportDate, library_ProductInfo_productCode, library_ProductInfo_underDevelopmentDate}

# library_Vendor class attributes and methods

# Company class attributes and methods

# Relationships
lifecycle0: BinaryAssociation = BinaryAssociation(
    name="lifecycle0",
    ends={
        Property(name="library_Lifecycle", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment", type=library_Lifecycle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagrams1: BinaryAssociation = BinaryAssociation(
    name="diagrams1",
    ends={
        Property(name="library_DiagramInfo", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment2", type=library_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments4: BinaryAssociation = BinaryAssociation(
    name="equipments4",
    ends={
        Property(name="library_Equipment5", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment3", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentGroups6: BinaryAssociation = BinaryAssociation(
    name="equipmentGroups6",
    ends={
        Property(name="library_EquipmentGroup", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment7", type=library_EquipmentGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentResources8: BinaryAssociation = BinaryAssociation(
    name="equipmentResources8",
    ends={
        Property(name="library_NetXResource", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment9", type=library_NetXResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentMetricRefs10: BinaryAssociation = BinaryAssociation(
    name="equipmentMetricRefs10",
    ends={
        Property(name="library_Metric", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment11", type=library_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentRelationshipRefs12: BinaryAssociation = BinaryAssociation(
    name="equipmentRelationshipRefs12",
    ends={
        Property(name="library_EquipmentRelationship", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment13", type=library_EquipmentRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentExpressionRefs14: BinaryAssociation = BinaryAssociation(
    name="equipmentExpressionRefs14",
    ends={
        Property(name="Expression", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="equipmentRefs", type=library_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
capacityExpressionRef15: BinaryAssociation = BinaryAssociation(
    name="capacityExpressionRef15",
    ends={
        Property(name="library_Expression", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment16", type=library_Expression, multiplicity=Multiplicity(0, 1))
    }
)
toleranceRefs17: BinaryAssociation = BinaryAssociation(
    name="toleranceRefs17",
    ends={
        Property(name="library_Tolerance", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment18", type=library_Tolerance, multiplicity=Multiplicity(0, 9999))
    }
)
protocolRefs19: BinaryAssociation = BinaryAssociation(
    name="protocolRefs19",
    ends={
        Property(name="library_Protocol", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment20", type=library_Protocol, multiplicity=Multiplicity(0, 9999))
    }
)
parameterRefs21: BinaryAssociation = BinaryAssociation(
    name="parameterRefs21",
    ends={
        Property(name="library_Parameter", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment22", type=library_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipmentResources23: BinaryAssociation = BinaryAssociation(
    name="allEquipmentResources23",
    ends={
        Property(name="library_NetXResource25", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment24", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipments27: BinaryAssociation = BinaryAssociation(
    name="allEquipments27",
    ends={
        Property(name="library_Equipment28", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment26", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
icons29: BinaryAssociation = BinaryAssociation(
    name="icons29",
    ends={
        Property(name="library_MultiImage", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment30", type=library_MultiImage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
diagrams31: BinaryAssociation = BinaryAssociation(
    name="diagrams31",
    ends={
        Property(name="library_DiagramInfo33", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup32", type=library_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentGroupResources34: BinaryAssociation = BinaryAssociation(
    name="equipmentGroupResources34",
    ends={
        Property(name="library_NetXResource36", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup35", type=library_NetXResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionRefs37: BinaryAssociation = BinaryAssociation(
    name="expressionRefs37",
    ends={
        Property(name="Expression38", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="equipmentGroupRefs", type=library_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentRefs39: BinaryAssociation = BinaryAssociation(
    name="equipmentRefs39",
    ends={
        Property(name="library_Equipment41", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup40", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
parameterRefs42: BinaryAssociation = BinaryAssociation(
    name="parameterRefs42",
    ends={
        Property(name="library_Parameter44", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup43", type=library_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipmentResources45: BinaryAssociation = BinaryAssociation(
    name="allEquipmentResources45",
    ends={
        Property(name="library_NetXResource47", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup46", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
evaluationObject51: BinaryAssociation = BinaryAssociation(
    name="evaluationObject51",
    ends={
        Property(name="library_Expression52", type=library_EObject, multiplicity=Multiplicity(0, 1)),
        Property(name="library_EObject", type=library_Expression, multiplicity=Multiplicity(1, 1))
    }
)
allEquipments48: BinaryAssociation = BinaryAssociation(
    name="allEquipments48",
    ends={
        Property(name="library_Equipment50", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup49", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentRefs53: BinaryAssociation = BinaryAssociation(
    name="equipmentRefs53",
    ends={
        Property(name="Equipment", type=library_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="equipmentExpressionRefs", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
functionRefs54: BinaryAssociation = BinaryAssociation(
    name="functionRefs54",
    ends={
        Property(name="Function", type=library_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="functionExpressionRefs", type=library_Function, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentGroupRefs55: BinaryAssociation = BinaryAssociation(
    name="equipmentGroupRefs55",
    ends={
        Property(name="EquipmentGroup", type=library_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionRefs", type=library_EquipmentGroup, multiplicity=Multiplicity(0, 9999))
    }
)
serviceProfileRefs56: BinaryAssociation = BinaryAssociation(
    name="serviceProfileRefs56",
    ends={
        Property(name="library_ServiceProfile", type=library_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Expression57", type=library_ServiceProfile, multiplicity=Multiplicity(0, 9999))
    }
)
diagrams58: BinaryAssociation = BinaryAssociation(
    name="diagrams58",
    ends={
        Property(name="library_DiagramInfo59", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function", type=library_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icons60: BinaryAssociation = BinaryAssociation(
    name="icons60",
    ends={
        Property(name="library_MultiImage62", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function61", type=library_MultiImage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions64: BinaryAssociation = BinaryAssociation(
    name="functions64",
    ends={
        Property(name="library_Function65", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function63", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionResources66: BinaryAssociation = BinaryAssociation(
    name="functionResources66",
    ends={
        Property(name="library_NetXResource68", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function67", type=library_NetXResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMetricRefs69: BinaryAssociation = BinaryAssociation(
    name="functionMetricRefs69",
    ends={
        Property(name="library_Metric71", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function70", type=library_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
functionRelationshipRefs72: BinaryAssociation = BinaryAssociation(
    name="functionRelationshipRefs72",
    ends={
        Property(name="library_FunctionRelationship", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function73", type=library_FunctionRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
functionExpressionRefs74: BinaryAssociation = BinaryAssociation(
    name="functionExpressionRefs74",
    ends={
        Property(name="Expression75", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="functionRefs", type=library_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
capacityExpressionRef76: BinaryAssociation = BinaryAssociation(
    name="capacityExpressionRef76",
    ends={
        Property(name="library_Expression78", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function77", type=library_Expression, multiplicity=Multiplicity(0, 1))
    }
)
toleranceRefs79: BinaryAssociation = BinaryAssociation(
    name="toleranceRefs79",
    ends={
        Property(name="library_Tolerance81", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function80", type=library_Tolerance, multiplicity=Multiplicity(0, 9999))
    }
)
protocolRefs82: BinaryAssociation = BinaryAssociation(
    name="protocolRefs82",
    ends={
        Property(name="library_Protocol84", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function83", type=library_Protocol, multiplicity=Multiplicity(0, 9999))
    }
)
parameterRefs85: BinaryAssociation = BinaryAssociation(
    name="parameterRefs85",
    ends={
        Property(name="library_Parameter87", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function86", type=library_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
allFunctionResources88: BinaryAssociation = BinaryAssociation(
    name="allFunctionResources88",
    ends={
        Property(name="library_NetXResource90", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function89", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
allFunctions92: BinaryAssociation = BinaryAssociation(
    name="allFunctions92",
    ends={
        Property(name="library_Function93", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function91", type=library_Function, multiplicity=Multiplicity(0, 9999))
    }
)
nodeTypes96: BinaryAssociation = BinaryAssociation(
    name="nodeTypes96",
    ends={
        Property(name="library_Library97", type=library_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="library_NodeType", type=library_Library, multiplicity=Multiplicity(1, 1))
    }
)
functions94: BinaryAssociation = BinaryAssociation(
    name="functions94",
    ends={
        Property(name="library_Function95", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments98: BinaryAssociation = BinaryAssociation(
    name="equipments98",
    ends={
        Property(name="library_Equipment100", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library99", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metrics101: BinaryAssociation = BinaryAssociation(
    name="metrics101",
    ends={
        Property(name="library_Metric103", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library102", type=library_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricSources104: BinaryAssociation = BinaryAssociation(
    name="metricSources104",
    ends={
        Property(name="library_MetricSource", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library105", type=library_MetricSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters106: BinaryAssociation = BinaryAssociation(
    name="parameters106",
    ends={
        Property(name="library_Parameter108", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library107", type=library_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tolerances109: BinaryAssociation = BinaryAssociation(
    name="tolerances109",
    ends={
        Property(name="library_Tolerance111", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library110", type=library_Tolerance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions112: BinaryAssociation = BinaryAssociation(
    name="expressions112",
    ends={
        Property(name="library_Expression114", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library113", type=library_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units115: BinaryAssociation = BinaryAssociation(
    name="units115",
    ends={
        Property(name="library_Unit", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library116", type=library_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
version117: BinaryAssociation = BinaryAssociation(
    name="version117",
    ends={
        Property(name="library_Meta", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library118", type=library_Meta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metricRef119: BinaryAssociation = BinaryAssociation(
    name="metricRef119",
    ends={
        Property(name="library_Metric121", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource120", type=library_Metric, multiplicity=Multiplicity(0, 1))
    }
)
metricValueRanges122: BinaryAssociation = BinaryAssociation(
    name="metricValueRanges122",
    ends={
        Property(name="library_MetricValueRange", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource123", type=library_MetricValueRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capacityValues124: BinaryAssociation = BinaryAssociation(
    name="capacityValues124",
    ends={
        Property(name="library_Value", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource125", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilizationValues126: BinaryAssociation = BinaryAssociation(
    name="utilizationValues126",
    ends={
        Property(name="library_Value128", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource127", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forecastCapacityValues129: BinaryAssociation = BinaryAssociation(
    name="forecastCapacityValues129",
    ends={
        Property(name="library_Value131", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource130", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forecastValues132: BinaryAssociation = BinaryAssociation(
    name="forecastValues132",
    ends={
        Property(name="library_Value134", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource133", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trendedValues135: BinaryAssociation = BinaryAssociation(
    name="trendedValues135",
    ends={
        Property(name="library_Value137", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource136", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unitRef138: BinaryAssociation = BinaryAssociation(
    name="unitRef138",
    ends={
        Property(name="library_Unit140", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource139", type=library_Unit, multiplicity=Multiplicity(0, 1))
    }
)
functions141: BinaryAssociation = BinaryAssociation(
    name="functions141",
    ends={
        Property(name="library_Function143", type=library_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NodeType142", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments144: BinaryAssociation = BinaryAssociation(
    name="equipments144",
    ends={
        Property(name="library_Equipment146", type=library_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NodeType145", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeTypeRef152: BinaryAssociation = BinaryAssociation(
    name="nodeTypeRef152",
    ends={
        Property(name="library_NodeType154", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo153", type=library_NodeType, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentRef147: BinaryAssociation = BinaryAssociation(
    name="equipmentRef147",
    ends={
        Property(name="library_Equipment148", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
licensedFunctionRef149: BinaryAssociation = BinaryAssociation(
    name="licensedFunctionRef149",
    ends={
        Property(name="library_Function151", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo150", type=library_Function, multiplicity=Multiplicity(0, 9999))
    }
)
icons155: BinaryAssociation = BinaryAssociation(
    name="icons155",
    ends={
        Property(name="library_MultiImage157", type=library_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Unit156", type=library_MultiImage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
products158: BinaryAssociation = BinaryAssociation(
    name="products158",
    ends={
        Property(name="library_ProductInfo159", type=library_Vendor, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Vendor", type=library_ProductInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_Vendor_Company = Generalization(general=Company, specific=library_Vendor)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Equipment, library_Lifecycle, library_DiagramInfo, library_EquipmentGroup, library_NetXResource, library_Metric, library_EquipmentRelationship, library_Expression, library_Tolerance, library_Protocol, library_Parameter, library_MultiImage, library_EObject, library_Function, library_ServiceProfile, library_ExpressionResult, library_FunctionRelationship, library_Library, library_NodeType, library_MetricSource, library_Unit, library_Meta, library_MetricValueRange, library_Value, library_ProductInfo, library_Vendor, Company, LevelType, StateType, RedundancyType},
    associations={lifecycle0, diagrams1, equipments4, equipmentGroups6, equipmentResources8, equipmentMetricRefs10, equipmentRelationshipRefs12, equipmentExpressionRefs14, capacityExpressionRef15, toleranceRefs17, protocolRefs19, parameterRefs21, allEquipmentResources23, allEquipments27, icons29, diagrams31, equipmentGroupResources34, expressionRefs37, equipmentRefs39, parameterRefs42, allEquipmentResources45, evaluationObject51, allEquipments48, equipmentRefs53, functionRefs54, equipmentGroupRefs55, serviceProfileRefs56, diagrams58, icons60, functions64, functionResources66, functionMetricRefs69, functionRelationshipRefs72, functionExpressionRefs74, capacityExpressionRef76, toleranceRefs79, protocolRefs82, parameterRefs85, allFunctionResources88, allFunctions92, nodeTypes96, functions94, equipments98, metrics101, metricSources104, parameters106, tolerances109, expressions112, units115, version117, metricRef119, metricValueRanges122, capacityValues124, utilizationValues126, forecastCapacityValues129, forecastValues132, trendedValues135, unitRef138, functions141, equipments144, nodeTypeRef152, equipmentRef147, licensedFunctionRef149, icons155, products158},
    generalizations={gen_library_Vendor_Company},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)