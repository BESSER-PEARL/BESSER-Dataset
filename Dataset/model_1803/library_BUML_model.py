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
LevelKind: Enumeration = Enumeration(
    name="LevelKind",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="AMBER"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="YELLOW")
    }
)

RangeKind: Enumeration = Enumeration(
    name="RangeKind",
    literals={
            EnumerationLiteral(name="METRIC"),
			EnumerationLiteral(name="METRICREMOVE"),
			EnumerationLiteral(name="CAP"),
			EnumerationLiteral(name="DERIVED"),
			EnumerationLiteral(name="FORECAST"),
			EnumerationLiteral(name="FORECASTCAP"),
			EnumerationLiteral(name="TRENDED"),
			EnumerationLiteral(name="UTILIZATION"),
			EnumerationLiteral(name="TOLERANCE")
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

# Classes
library_BaseExpressionResult = Class(name="library::BaseExpressionResult")
library_BaseResource = Class(name="library::BaseResource")
Base = Class(name="Base")
library_Unit = Class(name="library::Unit")
library_Component = Class(name="library::Component")
library_Lifecycle = Class(name="library::Lifecycle")
library_NetXResource = Class(name="library::NetXResource")
library_Metric = Class(name="library::Metric")
library_Expression = Class(name="library::Expression")
library_Tolerance = Class(name="library::Tolerance")
library_Protocol = Class(name="library::Protocol")
library_Parameter = Class(name="library::Parameter")
library_DiagramInfo = Class(name="library::DiagramInfo")
library_MultiImage = Class(name="library::MultiImage")
library_Equipment = Class(name="library::Equipment")
Component = Class(name="Component")
library_EquipmentGroup = Class(name="library::EquipmentGroup")
library_EquipmentRelationship = Class(name="library::EquipmentRelationship")
library_ExpressionResult = Class(name="library::ExpressionResult")
BaseExpressionResult = Class(name="BaseExpressionResult")
library_EObject = Class(name="library::EObject")
library_Function = Class(name="library::Function")
library_Value = Class(name="library::Value")
library_FunctionRelationship = Class(name="library::FunctionRelationship")
library_LastEvaluationExpressionResult = Class(name="library::LastEvaluationExpressionResult")
library_Library = Class(name="library::Library")
library_MetricSource = Class(name="library::MetricSource")
library_NodeType = Class(name="library::NodeType")
library_Meta = Class(name="library::Meta")
BaseResource = Class(name="BaseResource")
library_MetricValueRange = Class(name="library::MetricValueRange")
library_ProductInfo = Class(name="library::ProductInfo")
library_Vendor = Class(name="library::Vendor")
Company = Class(name="Company")

# library_BaseExpressionResult class attributes and methods

# library_BaseResource class attributes and methods
library_BaseResource_detailDisplay: Property = Property(name="detailDisplay", type=StringType)
library_BaseResource_expressionName: Property = Property(name="expressionName", type=StringType)
library_BaseResource_longName: Property = Property(name="longName", type=StringType)
library_BaseResource_summaryDisplay: Property = Property(name="summaryDisplay", type=StringType)
library_BaseResource_shortName: Property = Property(name="shortName", type=StringType)
library_BaseResource.attributes={library_BaseResource_shortName, library_BaseResource_detailDisplay, library_BaseResource_expressionName, library_BaseResource_longName, library_BaseResource_summaryDisplay}

# Base class attributes and methods

# library_Unit class attributes and methods
library_Unit_code: Property = Property(name="code", type=StringType)
library_Unit_description: Property = Property(name="description", type=StringType)
library_Unit_name: Property = Property(name="name", type=StringType)
library_Unit.attributes={library_Unit_code, library_Unit_name, library_Unit_description}

# library_Component class attributes and methods
library_Component_description: Property = Property(name="description", type=StringType)
library_Component_duration: Property = Property(name="duration", type=StringType)
library_Component_name: Property = Property(name="name", type=StringType)
library_Component.attributes={library_Component_duration, library_Component_name, library_Component_description}

# library_Lifecycle class attributes and methods

# library_NetXResource class attributes and methods

# library_Metric class attributes and methods

# library_Expression class attributes and methods
library_Expression_expressionLines: Property = Property(name="expressionLines", type=StringType)
library_Expression_name: Property = Property(name="name", type=StringType)
library_Expression.attributes={library_Expression_name, library_Expression_expressionLines}

# library_Tolerance class attributes and methods
library_Tolerance_level: Property = Property(name="level", type=StringType)
library_Tolerance_name: Property = Property(name="name", type=StringType)
library_Tolerance.attributes={library_Tolerance_level, library_Tolerance_name}

# library_Protocol class attributes and methods

# library_Parameter class attributes and methods
library_Parameter_description: Property = Property(name="description", type=StringType)
library_Parameter_value: Property = Property(name="value", type=StringType)
library_Parameter_expressionName: Property = Property(name="expressionName", type=StringType)
library_Parameter_modifiable: Property = Property(name="modifiable", type=StringType)
library_Parameter_name: Property = Property(name="name", type=StringType)
library_Parameter.attributes={library_Parameter_description, library_Parameter_value, library_Parameter_expressionName, library_Parameter_name, library_Parameter_modifiable}

# library_DiagramInfo class attributes and methods

# library_MultiImage class attributes and methods

# library_Equipment class attributes and methods
library_Equipment_count: Property = Property(name="count", type=StringType)
library_Equipment_equipmentCode: Property = Property(name="equipmentCode", type=StringType)
library_Equipment_position: Property = Property(name="position", type=StringType)
library_Equipment_redundancy: Property = Property(name="redundancy", type=StringType)
library_Equipment_state: Property = Property(name="state", type=StringType)
library_Equipment.attributes={library_Equipment_redundancy, library_Equipment_count, library_Equipment_position, library_Equipment_state, library_Equipment_equipmentCode}

# Component class attributes and methods

# library_EquipmentGroup class attributes and methods
library_EquipmentGroup_count: Property = Property(name="count", type=StringType)
library_EquipmentGroup_description: Property = Property(name="description", type=StringType)
library_EquipmentGroup_name: Property = Property(name="name", type=StringType)
library_EquipmentGroup.attributes={library_EquipmentGroup_description, library_EquipmentGroup_name, library_EquipmentGroup_count}

# library_EquipmentRelationship class attributes and methods

# library_ExpressionResult class attributes and methods
library_ExpressionResult_targetIntervalHint: Property = Property(name="targetIntervalHint", type=StringType)
library_ExpressionResult_targetKindHint: Property = Property(name="targetKindHint", type=StringType)
library_ExpressionResult_targetRange: Property = Property(name="targetRange", type=StringType)
library_ExpressionResult.attributes={library_ExpressionResult_targetIntervalHint, library_ExpressionResult_targetRange, library_ExpressionResult_targetKindHint}

# BaseExpressionResult class attributes and methods

# library_EObject class attributes and methods

# library_Function class attributes and methods

# library_Value class attributes and methods

# library_FunctionRelationship class attributes and methods

# library_LastEvaluationExpressionResult class attributes and methods
library_LastEvaluationExpressionResult_lastEvalResult: Property = Property(name="lastEvalResult", type=StringType)
library_LastEvaluationExpressionResult.attributes={library_LastEvaluationExpressionResult_lastEvalResult}

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library_protocols: Property = Property(name="protocols", type=StringType)
library_Library.attributes={library_Library_name, library_Library_protocols}

# library_MetricSource class attributes and methods

# library_NodeType class attributes and methods
library_NodeType_leafNode: Property = Property(name="leafNode", type=StringType)
library_NodeType_name: Property = Property(name="name", type=StringType)
library_NodeType.attributes={library_NodeType_name, library_NodeType_leafNode}

# library_Meta class attributes and methods

# BaseResource class attributes and methods

# library_MetricValueRange class attributes and methods

# library_ProductInfo class attributes and methods
library_ProductInfo_availableDate: Property = Property(name="availableDate", type=StringType)
library_ProductInfo_salesCode: Property = Property(name="salesCode", type=StringType)
library_ProductInfo_underDevelopmentDate: Property = Property(name="underDevelopmentDate", type=StringType)
library_ProductInfo_endOfSalesDate: Property = Property(name="endOfSalesDate", type=StringType)
library_ProductInfo_endOfSupportDate: Property = Property(name="endOfSupportDate", type=StringType)
library_ProductInfo_productCode: Property = Property(name="productCode", type=StringType)
library_ProductInfo.attributes={library_ProductInfo_endOfSalesDate, library_ProductInfo_availableDate, library_ProductInfo_salesCode, library_ProductInfo_productCode, library_ProductInfo_underDevelopmentDate, library_ProductInfo_endOfSupportDate}

# library_Vendor class attributes and methods

# Company class attributes and methods

# Relationships
unitRef0: BinaryAssociation = BinaryAssociation(
    name="unitRef0",
    ends={
        Property(name="library_Unit", type=library_BaseResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_BaseResource", type=library_Unit, multiplicity=Multiplicity(0, 1))
    }
)
lifecycle1: BinaryAssociation = BinaryAssociation(
    name="lifecycle1",
    ends={
        Property(name="library_Lifecycle", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component", type=library_Lifecycle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceRefs2: BinaryAssociation = BinaryAssociation(
    name="resourceRefs2",
    ends={
        Property(name="NetXResource", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="componentRef", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
metricRefs3: BinaryAssociation = BinaryAssociation(
    name="metricRefs3",
    ends={
        Property(name="library_Metric", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component4", type=library_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
capacityExpressionRef5: BinaryAssociation = BinaryAssociation(
    name="capacityExpressionRef5",
    ends={
        Property(name="library_Expression", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component6", type=library_Expression, multiplicity=Multiplicity(0, 1))
    }
)
utilizationExpressionRef7: BinaryAssociation = BinaryAssociation(
    name="utilizationExpressionRef7",
    ends={
        Property(name="library_Expression9", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component8", type=library_Expression, multiplicity=Multiplicity(0, 1))
    }
)
toleranceRefs10: BinaryAssociation = BinaryAssociation(
    name="toleranceRefs10",
    ends={
        Property(name="library_Tolerance", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component11", type=library_Tolerance, multiplicity=Multiplicity(0, 9999))
    }
)
protocolRefs12: BinaryAssociation = BinaryAssociation(
    name="protocolRefs12",
    ends={
        Property(name="library_Protocol", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component13", type=library_Protocol, multiplicity=Multiplicity(0, 9999))
    }
)
parameterRefs14: BinaryAssociation = BinaryAssociation(
    name="parameterRefs14",
    ends={
        Property(name="library_Parameter", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component15", type=library_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
allResources16: BinaryAssociation = BinaryAssociation(
    name="allResources16",
    ends={
        Property(name="library_NetXResource", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component17", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
diagrams18: BinaryAssociation = BinaryAssociation(
    name="diagrams18",
    ends={
        Property(name="library_DiagramInfo", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component19", type=library_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icons20: BinaryAssociation = BinaryAssociation(
    name="icons20",
    ends={
        Property(name="library_MultiImage", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component21", type=library_MultiImage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equipments23: BinaryAssociation = BinaryAssociation(
    name="equipments23",
    ends={
        Property(name="library_Equipment", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment22", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentGroups24: BinaryAssociation = BinaryAssociation(
    name="equipmentGroups24",
    ends={
        Property(name="library_EquipmentGroup", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment25", type=library_EquipmentGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentRelationshipRefs26: BinaryAssociation = BinaryAssociation(
    name="equipmentRelationshipRefs26",
    ends={
        Property(name="library_EquipmentRelationship", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment27", type=library_EquipmentRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipments29: BinaryAssociation = BinaryAssociation(
    name="allEquipments29",
    ends={
        Property(name="library_Equipment30", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment28", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
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
        Property(name="library_Expression39", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup38", type=library_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentRefs40: BinaryAssociation = BinaryAssociation(
    name="equipmentRefs40",
    ends={
        Property(name="library_Equipment42", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup41", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
parameterRefs43: BinaryAssociation = BinaryAssociation(
    name="parameterRefs43",
    ends={
        Property(name="library_Parameter45", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup44", type=library_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipmentResources46: BinaryAssociation = BinaryAssociation(
    name="allEquipmentResources46",
    ends={
        Property(name="library_NetXResource48", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup47", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipments49: BinaryAssociation = BinaryAssociation(
    name="allEquipments49",
    ends={
        Property(name="library_Equipment51", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup50", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
targetResource54: BinaryAssociation = BinaryAssociation(
    name="targetResource54",
    ends={
        Property(name="library_BaseResource55", type=library_ExpressionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ExpressionResult", type=library_BaseResource, multiplicity=Multiplicity(0, 1))
    }
)
evaluationObject52: BinaryAssociation = BinaryAssociation(
    name="evaluationObject52",
    ends={
        Property(name="library_EObject", type=library_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Expression53", type=library_EObject, multiplicity=Multiplicity(0, 1))
    }
)
targetValues56: BinaryAssociation = BinaryAssociation(
    name="targetValues56",
    ends={
        Property(name="library_Value", type=library_ExpressionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ExpressionResult57", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionRelationshipRefs60: BinaryAssociation = BinaryAssociation(
    name="functionRelationshipRefs60",
    ends={
        Property(name="library_FunctionRelationship", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function61", type=library_FunctionRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
allFunctions63: BinaryAssociation = BinaryAssociation(
    name="allFunctions63",
    ends={
        Property(name="library_Function64", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function62", type=library_Function, multiplicity=Multiplicity(0, 9999))
    }
)
functions59: BinaryAssociation = BinaryAssociation(
    name="functions59",
    ends={
        Property(name="library_Function", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function58", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions65: BinaryAssociation = BinaryAssociation(
    name="functions65",
    ends={
        Property(name="library_Function66", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments69: BinaryAssociation = BinaryAssociation(
    name="equipments69",
    ends={
        Property(name="library_Equipment71", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library70", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metrics72: BinaryAssociation = BinaryAssociation(
    name="metrics72",
    ends={
        Property(name="library_Metric74", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library73", type=library_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricSources75: BinaryAssociation = BinaryAssociation(
    name="metricSources75",
    ends={
        Property(name="library_MetricSource", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library76", type=library_MetricSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters77: BinaryAssociation = BinaryAssociation(
    name="parameters77",
    ends={
        Property(name="library_Parameter79", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library78", type=library_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeTypes67: BinaryAssociation = BinaryAssociation(
    name="nodeTypes67",
    ends={
        Property(name="library_NodeType", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library68", type=library_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions83: BinaryAssociation = BinaryAssociation(
    name="expressions83",
    ends={
        Property(name="library_Library84", type=library_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="library_Expression85", type=library_Library, multiplicity=Multiplicity(1, 1))
    }
)
units86: BinaryAssociation = BinaryAssociation(
    name="units86",
    ends={
        Property(name="library_Unit88", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library87", type=library_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
version89: BinaryAssociation = BinaryAssociation(
    name="version89",
    ends={
        Property(name="library_Meta", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library90", type=library_Meta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tolerances80: BinaryAssociation = BinaryAssociation(
    name="tolerances80",
    ends={
        Property(name="library_Tolerance82", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library81", type=library_Tolerance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capacityValues97: BinaryAssociation = BinaryAssociation(
    name="capacityValues97",
    ends={
        Property(name="library_Value99", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource98", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilizationValues100: BinaryAssociation = BinaryAssociation(
    name="utilizationValues100",
    ends={
        Property(name="library_Value102", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource101", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forecastCapacityValues103: BinaryAssociation = BinaryAssociation(
    name="forecastCapacityValues103",
    ends={
        Property(name="library_Value105", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource104", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forecastValues106: BinaryAssociation = BinaryAssociation(
    name="forecastValues106",
    ends={
        Property(name="library_Value108", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource107", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentRef91: BinaryAssociation = BinaryAssociation(
    name="componentRef91",
    ends={
        Property(name="Component", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRefs", type=library_Component, multiplicity=Multiplicity(1, 1))
    }
)
metricRef92: BinaryAssociation = BinaryAssociation(
    name="metricRef92",
    ends={
        Property(name="library_Metric94", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource93", type=library_Metric, multiplicity=Multiplicity(0, 1))
    }
)
metricValueRanges95: BinaryAssociation = BinaryAssociation(
    name="metricValueRanges95",
    ends={
        Property(name="library_MetricValueRange", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource96", type=library_MetricValueRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions112: BinaryAssociation = BinaryAssociation(
    name="functions112",
    ends={
        Property(name="library_Function114", type=library_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NodeType113", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments115: BinaryAssociation = BinaryAssociation(
    name="equipments115",
    ends={
        Property(name="library_Equipment117", type=library_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NodeType116", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trendedValues109: BinaryAssociation = BinaryAssociation(
    name="trendedValues109",
    ends={
        Property(name="library_Value111", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource110", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentRef118: BinaryAssociation = BinaryAssociation(
    name="equipmentRef118",
    ends={
        Property(name="library_Equipment119", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
licensedFunctionRef120: BinaryAssociation = BinaryAssociation(
    name="licensedFunctionRef120",
    ends={
        Property(name="library_Function122", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo121", type=library_Function, multiplicity=Multiplicity(0, 9999))
    }
)
nodeTypeRef123: BinaryAssociation = BinaryAssociation(
    name="nodeTypeRef123",
    ends={
        Property(name="library_NodeType125", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo124", type=library_NodeType, multiplicity=Multiplicity(0, 9999))
    }
)
expressionRef126: BinaryAssociation = BinaryAssociation(
    name="expressionRef126",
    ends={
        Property(name="library_Expression128", type=library_Tolerance, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Tolerance127", type=library_Expression, multiplicity=Multiplicity(0, 1))
    }
)
icons129: BinaryAssociation = BinaryAssociation(
    name="icons129",
    ends={
        Property(name="library_MultiImage131", type=library_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Unit130", type=library_MultiImage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
products132: BinaryAssociation = BinaryAssociation(
    name="products132",
    ends={
        Property(name="library_ProductInfo133", type=library_Vendor, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Vendor", type=library_ProductInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_BaseResource_Base = Generalization(general=Base, specific=library_BaseResource)
gen_library_Component_Base = Generalization(general=Base, specific=library_Component)
gen_library_Equipment_Component = Generalization(general=Component, specific=library_Equipment)
gen_library_EquipmentGroup_Base = Generalization(general=Base, specific=library_EquipmentGroup)
gen_library_Expression_Base = Generalization(general=Base, specific=library_Expression)
gen_library_ExpressionResult_BaseExpressionResult = Generalization(general=BaseExpressionResult, specific=library_ExpressionResult)
gen_library_Function_Component = Generalization(general=Component, specific=library_Function)
gen_library_LastEvaluationExpressionResult_BaseExpressionResult = Generalization(general=BaseExpressionResult, specific=library_LastEvaluationExpressionResult)
gen_library_NetXResource_BaseResource = Generalization(general=BaseResource, specific=library_NetXResource)
gen_library_Parameter_Base = Generalization(general=Base, specific=library_Parameter)
gen_library_NodeType_Base = Generalization(general=Base, specific=library_NodeType)
gen_library_ProductInfo_Base = Generalization(general=Base, specific=library_ProductInfo)
gen_library_Unit_Base = Generalization(general=Base, specific=library_Unit)
gen_library_Tolerance_Base = Generalization(general=Base, specific=library_Tolerance)
gen_library_Vendor_Company = Generalization(general=Company, specific=library_Vendor)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_BaseExpressionResult, library_BaseResource, Base, library_Unit, library_Component, library_Lifecycle, library_NetXResource, library_Metric, library_Expression, library_Tolerance, library_Protocol, library_Parameter, library_DiagramInfo, library_MultiImage, library_Equipment, Component, library_EquipmentGroup, library_EquipmentRelationship, library_ExpressionResult, BaseExpressionResult, library_EObject, library_Function, library_Value, library_FunctionRelationship, library_LastEvaluationExpressionResult, library_Library, library_MetricSource, library_NodeType, library_Meta, BaseResource, library_MetricValueRange, library_ProductInfo, library_Vendor, Company, LevelKind, RangeKind, RedundancyType, StateType},
    associations={unitRef0, lifecycle1, resourceRefs2, metricRefs3, capacityExpressionRef5, utilizationExpressionRef7, toleranceRefs10, protocolRefs12, parameterRefs14, allResources16, diagrams18, icons20, equipments23, equipmentGroups24, equipmentRelationshipRefs26, allEquipments29, diagrams31, equipmentGroupResources34, expressionRefs37, equipmentRefs40, parameterRefs43, allEquipmentResources46, allEquipments49, targetResource54, evaluationObject52, targetValues56, functionRelationshipRefs60, allFunctions63, functions59, functions65, equipments69, metrics72, metricSources75, parameters77, nodeTypes67, expressions83, units86, version89, tolerances80, capacityValues97, utilizationValues100, forecastCapacityValues103, forecastValues106, componentRef91, metricRef92, metricValueRanges95, functions112, equipments115, trendedValues109, equipmentRef118, licensedFunctionRef120, nodeTypeRef123, expressionRef126, icons129, products132},
    generalizations={gen_library_BaseResource_Base, gen_library_Component_Base, gen_library_Equipment_Component, gen_library_EquipmentGroup_Base, gen_library_Expression_Base, gen_library_ExpressionResult_BaseExpressionResult, gen_library_Function_Component, gen_library_LastEvaluationExpressionResult_BaseExpressionResult, gen_library_NetXResource_BaseResource, gen_library_Parameter_Base, gen_library_NodeType_Base, gen_library_ProductInfo_Base, gen_library_Unit_Base, gen_library_Tolerance_Base, gen_library_Vendor_Company},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)