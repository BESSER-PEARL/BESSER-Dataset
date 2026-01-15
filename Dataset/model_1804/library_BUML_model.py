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

RedundancyType: Enumeration = Enumeration(
    name="RedundancyType",
    literals={
            EnumerationLiteral(name="n"),
			EnumerationLiteral(name="n1"),
			EnumerationLiteral(name="_11")
    }
)

RangeKind: Enumeration = Enumeration(
    name="RangeKind",
    literals={
            EnumerationLiteral(name="METRICREMOVE"),
			EnumerationLiteral(name="CAP"),
			EnumerationLiteral(name="DERIVED"),
			EnumerationLiteral(name="FORECAST"),
			EnumerationLiteral(name="FORECASTCAP"),
			EnumerationLiteral(name="TRENDED"),
			EnumerationLiteral(name="UTILIZATION"),
			EnumerationLiteral(name="TOLERANCE"),
			EnumerationLiteral(name="METRIC")
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
library_Expression = Class(name="library::Expression")
library_Unit = Class(name="library::Unit")
library_Tolerance = Class(name="library::Tolerance")
library_Protocol = Class(name="library::Protocol")
library_Component = Class(name="library::Component")
library_Parameter = Class(name="library::Parameter")
library_Lifecycle = Class(name="library::Lifecycle")
library_NetXResource = Class(name="library::NetXResource")
library_ConfigAttribute = Class(name="library::ConfigAttribute")
library_Metric = Class(name="library::Metric")
library_Equipment = Class(name="library::Equipment")
Component = Class(name="Component")
library_DiagramInfo = Class(name="library::DiagramInfo")
library_MultiImage = Class(name="library::MultiImage")
library_EquipmentGroup = Class(name="library::EquipmentGroup")
library_EquipmentRelationship = Class(name="library::EquipmentRelationship")
library_EObject = Class(name="library::EObject")
library_ExpressionResult = Class(name="library::ExpressionResult")
BaseExpressionResult = Class(name="BaseExpressionResult")
library_Value = Class(name="library::Value")
library_Function = Class(name="library::Function")
library_FunctionRelationship = Class(name="library::FunctionRelationship")
library_LastEvaluationExpressionResult = Class(name="library::LastEvaluationExpressionResult")
library_Library = Class(name="library::Library")
library_NodeType = Class(name="library::NodeType")
library_MetricSource = Class(name="library::MetricSource")
library_Meta = Class(name="library::Meta")
library_MetricValueRange = Class(name="library::MetricValueRange")
BaseResource = Class(name="BaseResource")
library_ProductInfo = Class(name="library::ProductInfo")
library_ReferenceRelationship = Class(name="library::ReferenceRelationship")
library_ReferenceNetwork = Class(name="library::ReferenceNetwork")
library_Vendor = Class(name="library::Vendor")
Company = Class(name="Company")

# library_BaseExpressionResult class attributes and methods

# library_BaseResource class attributes and methods
library_BaseResource_longName: Property = Property(name="longName", type=StringType)
library_BaseResource_detailDisplay: Property = Property(name="detailDisplay", type=StringType)
library_BaseResource_expressionName: Property = Property(name="expressionName", type=StringType)
library_BaseResource_shortName: Property = Property(name="shortName", type=StringType)
library_BaseResource_summaryDisplay: Property = Property(name="summaryDisplay", type=StringType)
library_BaseResource.attributes={library_BaseResource_shortName, library_BaseResource_summaryDisplay, library_BaseResource_longName, library_BaseResource_detailDisplay, library_BaseResource_expressionName}

# Base class attributes and methods

# library_Expression class attributes and methods
library_Expression_expressionLines: Property = Property(name="expressionLines", type=StringType)
library_Expression_name: Property = Property(name="name", type=StringType)
library_Expression.attributes={library_Expression_name, library_Expression_expressionLines}

# library_Unit class attributes and methods
library_Unit_code: Property = Property(name="code", type=StringType)
library_Unit_description: Property = Property(name="description", type=StringType)
library_Unit_name: Property = Property(name="name", type=StringType)
library_Unit.attributes={library_Unit_description, library_Unit_name, library_Unit_code}

# library_Tolerance class attributes and methods
library_Tolerance_level: Property = Property(name="level", type=StringType)
library_Tolerance_name: Property = Property(name="name", type=StringType)
library_Tolerance.attributes={library_Tolerance_name, library_Tolerance_level}

# library_Protocol class attributes and methods

# library_Component class attributes and methods
library_Component_description: Property = Property(name="description", type=StringType)
library_Component_duration: Property = Property(name="duration", type=StringType)
library_Component_name: Property = Property(name="name", type=StringType)
library_Component.attributes={library_Component_description, library_Component_name, library_Component_duration}

# library_Parameter class attributes and methods
library_Parameter_description: Property = Property(name="description", type=StringType)
library_Parameter_expressionName: Property = Property(name="expressionName", type=StringType)
library_Parameter_modifiable: Property = Property(name="modifiable", type=StringType)
library_Parameter_name: Property = Property(name="name", type=StringType)
library_Parameter_value: Property = Property(name="value", type=StringType)
library_Parameter.attributes={library_Parameter_description, library_Parameter_expressionName, library_Parameter_modifiable, library_Parameter_value, library_Parameter_name}

# library_Lifecycle class attributes and methods

# library_NetXResource class attributes and methods

# library_ConfigAttribute class attributes and methods

# library_Metric class attributes and methods

# library_Equipment class attributes and methods
library_Equipment_count: Property = Property(name="count", type=StringType)
library_Equipment_equipmentCode: Property = Property(name="equipmentCode", type=StringType)
library_Equipment_state: Property = Property(name="state", type=StringType)
library_Equipment_position: Property = Property(name="position", type=StringType)
library_Equipment_redundancy: Property = Property(name="redundancy", type=StringType)
library_Equipment.attributes={library_Equipment_count, library_Equipment_redundancy, library_Equipment_position, library_Equipment_state, library_Equipment_equipmentCode}

# Component class attributes and methods

# library_DiagramInfo class attributes and methods

# library_MultiImage class attributes and methods

# library_EquipmentGroup class attributes and methods
library_EquipmentGroup_count: Property = Property(name="count", type=StringType)
library_EquipmentGroup_description: Property = Property(name="description", type=StringType)
library_EquipmentGroup_name: Property = Property(name="name", type=StringType)
library_EquipmentGroup.attributes={library_EquipmentGroup_count, library_EquipmentGroup_description, library_EquipmentGroup_name}

# library_EquipmentRelationship class attributes and methods

# library_EObject class attributes and methods

# library_ExpressionResult class attributes and methods
library_ExpressionResult_targetRange: Property = Property(name="targetRange", type=StringType)
library_ExpressionResult_targetIntervalHint: Property = Property(name="targetIntervalHint", type=StringType)
library_ExpressionResult_targetKindHint: Property = Property(name="targetKindHint", type=StringType)
library_ExpressionResult.attributes={library_ExpressionResult_targetIntervalHint, library_ExpressionResult_targetRange, library_ExpressionResult_targetKindHint}

# BaseExpressionResult class attributes and methods

# library_Value class attributes and methods

# library_Function class attributes and methods

# library_FunctionRelationship class attributes and methods

# library_LastEvaluationExpressionResult class attributes and methods
library_LastEvaluationExpressionResult_lastEvalResult: Property = Property(name="lastEvalResult", type=StringType)
library_LastEvaluationExpressionResult.attributes={library_LastEvaluationExpressionResult_lastEvalResult}

# library_Library class attributes and methods
library_Library_protocols: Property = Property(name="protocols", type=StringType)
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_protocols, library_Library_name}

# library_NodeType class attributes and methods
library_NodeType_leafNode: Property = Property(name="leafNode", type=StringType)
library_NodeType_name: Property = Property(name="name", type=StringType)
library_NodeType.attributes={library_NodeType_name, library_NodeType_leafNode}

# library_MetricSource class attributes and methods

# library_Meta class attributes and methods

# library_MetricValueRange class attributes and methods

# BaseResource class attributes and methods

# library_ProductInfo class attributes and methods
library_ProductInfo_endOfSalesDate: Property = Property(name="endOfSalesDate", type=StringType)
library_ProductInfo_endOfSupportDate: Property = Property(name="endOfSupportDate", type=StringType)
library_ProductInfo_productCode: Property = Property(name="productCode", type=StringType)
library_ProductInfo_availableDate: Property = Property(name="availableDate", type=StringType)
library_ProductInfo_salesCode: Property = Property(name="salesCode", type=StringType)
library_ProductInfo_underDevelopmentDate: Property = Property(name="underDevelopmentDate", type=StringType)
library_ProductInfo.attributes={library_ProductInfo_endOfSalesDate, library_ProductInfo_endOfSupportDate, library_ProductInfo_availableDate, library_ProductInfo_salesCode, library_ProductInfo_productCode, library_ProductInfo_underDevelopmentDate}

# library_ReferenceRelationship class attributes and methods
library_ReferenceRelationship_name: Property = Property(name="name", type=StringType)
library_ReferenceRelationship.attributes={library_ReferenceRelationship_name}

# library_ReferenceNetwork class attributes and methods
library_ReferenceNetwork_description: Property = Property(name="description", type=StringType)
library_ReferenceNetwork_name: Property = Property(name="name", type=StringType)
library_ReferenceNetwork.attributes={library_ReferenceNetwork_description, library_ReferenceNetwork_name}

# library_Vendor class attributes and methods

# Company class attributes and methods

# Relationships
capacityExpressionRef7: BinaryAssociation = BinaryAssociation(
    name="capacityExpressionRef7",
    ends={
        Property(name="library_Expression", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component8", type=library_Expression, multiplicity=Multiplicity(0, 1))
    }
)
utilizationExpressionRef9: BinaryAssociation = BinaryAssociation(
    name="utilizationExpressionRef9",
    ends={
        Property(name="library_Expression11", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component10", type=library_Expression, multiplicity=Multiplicity(0, 1))
    }
)
unitRef0: BinaryAssociation = BinaryAssociation(
    name="unitRef0",
    ends={
        Property(name="library_Unit", type=library_BaseResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_BaseResource", type=library_Unit, multiplicity=Multiplicity(0, 1))
    }
)
toleranceRefs12: BinaryAssociation = BinaryAssociation(
    name="toleranceRefs12",
    ends={
        Property(name="library_Tolerance", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component13", type=library_Tolerance, multiplicity=Multiplicity(0, 9999))
    }
)
protocolRefs14: BinaryAssociation = BinaryAssociation(
    name="protocolRefs14",
    ends={
        Property(name="library_Protocol", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component15", type=library_Protocol, multiplicity=Multiplicity(0, 9999))
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
configAttributes3: BinaryAssociation = BinaryAssociation(
    name="configAttributes3",
    ends={
        Property(name="library_ConfigAttribute", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component4", type=library_ConfigAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricRefs5: BinaryAssociation = BinaryAssociation(
    name="metricRefs5",
    ends={
        Property(name="library_Metric", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component6", type=library_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
equipments25: BinaryAssociation = BinaryAssociation(
    name="equipments25",
    ends={
        Property(name="library_Equipment", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment24", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterRefs16: BinaryAssociation = BinaryAssociation(
    name="parameterRefs16",
    ends={
        Property(name="library_Parameter", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component17", type=library_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
allResources18: BinaryAssociation = BinaryAssociation(
    name="allResources18",
    ends={
        Property(name="library_NetXResource", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component19", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
diagrams20: BinaryAssociation = BinaryAssociation(
    name="diagrams20",
    ends={
        Property(name="library_DiagramInfo", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component21", type=library_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icons22: BinaryAssociation = BinaryAssociation(
    name="icons22",
    ends={
        Property(name="library_MultiImage", type=library_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Component23", type=library_MultiImage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allEquipments31: BinaryAssociation = BinaryAssociation(
    name="allEquipments31",
    ends={
        Property(name="library_Equipment32", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment30", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentGroups26: BinaryAssociation = BinaryAssociation(
    name="equipmentGroups26",
    ends={
        Property(name="library_EquipmentGroup", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment27", type=library_EquipmentGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentRelationshipRefs28: BinaryAssociation = BinaryAssociation(
    name="equipmentRelationshipRefs28",
    ends={
        Property(name="library_EquipmentRelationship", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment29", type=library_EquipmentRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
diagrams33: BinaryAssociation = BinaryAssociation(
    name="diagrams33",
    ends={
        Property(name="library_DiagramInfo35", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup34", type=library_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentRefs42: BinaryAssociation = BinaryAssociation(
    name="equipmentRefs42",
    ends={
        Property(name="library_Equipment44", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup43", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
parameterRefs45: BinaryAssociation = BinaryAssociation(
    name="parameterRefs45",
    ends={
        Property(name="library_Parameter47", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup46", type=library_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentGroupResources36: BinaryAssociation = BinaryAssociation(
    name="equipmentGroupResources36",
    ends={
        Property(name="library_NetXResource38", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup37", type=library_NetXResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionRefs39: BinaryAssociation = BinaryAssociation(
    name="expressionRefs39",
    ends={
        Property(name="library_Expression41", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup40", type=library_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipments51: BinaryAssociation = BinaryAssociation(
    name="allEquipments51",
    ends={
        Property(name="library_Equipment53", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup52", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipmentResources48: BinaryAssociation = BinaryAssociation(
    name="allEquipmentResources48",
    ends={
        Property(name="library_NetXResource50", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup49", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
evaluationObject54: BinaryAssociation = BinaryAssociation(
    name="evaluationObject54",
    ends={
        Property(name="library_EObject", type=library_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Expression55", type=library_EObject, multiplicity=Multiplicity(0, 1))
    }
)
targetResource56: BinaryAssociation = BinaryAssociation(
    name="targetResource56",
    ends={
        Property(name="library_BaseResource57", type=library_ExpressionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ExpressionResult", type=library_BaseResource, multiplicity=Multiplicity(0, 1))
    }
)
targetValues58: BinaryAssociation = BinaryAssociation(
    name="targetValues58",
    ends={
        Property(name="library_Value", type=library_ExpressionResult, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ExpressionResult59", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions61: BinaryAssociation = BinaryAssociation(
    name="functions61",
    ends={
        Property(name="library_Function", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function60", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionRelationshipRefs62: BinaryAssociation = BinaryAssociation(
    name="functionRelationshipRefs62",
    ends={
        Property(name="library_FunctionRelationship", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function63", type=library_FunctionRelationship, multiplicity=Multiplicity(0, 9999))
    }
)
allFunctions65: BinaryAssociation = BinaryAssociation(
    name="allFunctions65",
    ends={
        Property(name="library_Function66", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function64", type=library_Function, multiplicity=Multiplicity(0, 9999))
    }
)
equipments71: BinaryAssociation = BinaryAssociation(
    name="equipments71",
    ends={
        Property(name="library_Equipment73", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library72", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions67: BinaryAssociation = BinaryAssociation(
    name="functions67",
    ends={
        Property(name="library_Function68", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeTypes69: BinaryAssociation = BinaryAssociation(
    name="nodeTypes69",
    ends={
        Property(name="library_NodeType", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library70", type=library_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metrics74: BinaryAssociation = BinaryAssociation(
    name="metrics74",
    ends={
        Property(name="library_Metric76", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library75", type=library_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricSources77: BinaryAssociation = BinaryAssociation(
    name="metricSources77",
    ends={
        Property(name="library_MetricSource", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library78", type=library_MetricSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters79: BinaryAssociation = BinaryAssociation(
    name="parameters79",
    ends={
        Property(name="library_Parameter81", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library80", type=library_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
version91: BinaryAssociation = BinaryAssociation(
    name="version91",
    ends={
        Property(name="library_Meta", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library92", type=library_Meta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tolerances82: BinaryAssociation = BinaryAssociation(
    name="tolerances82",
    ends={
        Property(name="library_Tolerance84", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library83", type=library_Tolerance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions85: BinaryAssociation = BinaryAssociation(
    name="expressions85",
    ends={
        Property(name="library_Expression87", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library86", type=library_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units88: BinaryAssociation = BinaryAssociation(
    name="units88",
    ends={
        Property(name="library_Unit90", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library89", type=library_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricValueRanges97: BinaryAssociation = BinaryAssociation(
    name="metricValueRanges97",
    ends={
        Property(name="library_MetricValueRange", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource98", type=library_MetricValueRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentRef93: BinaryAssociation = BinaryAssociation(
    name="componentRef93",
    ends={
        Property(name="Component", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="resourceRefs", type=library_Component, multiplicity=Multiplicity(1, 1))
    }
)
metricRef94: BinaryAssociation = BinaryAssociation(
    name="metricRef94",
    ends={
        Property(name="library_Metric96", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource95", type=library_Metric, multiplicity=Multiplicity(0, 1))
    }
)
forecastValues108: BinaryAssociation = BinaryAssociation(
    name="forecastValues108",
    ends={
        Property(name="library_Value110", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource109", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trendedValues111: BinaryAssociation = BinaryAssociation(
    name="trendedValues111",
    ends={
        Property(name="library_Value113", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource112", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
capacityValues99: BinaryAssociation = BinaryAssociation(
    name="capacityValues99",
    ends={
        Property(name="library_Value101", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource100", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions114: BinaryAssociation = BinaryAssociation(
    name="functions114",
    ends={
        Property(name="library_Function116", type=library_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NodeType115", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
utilizationValues102: BinaryAssociation = BinaryAssociation(
    name="utilizationValues102",
    ends={
        Property(name="library_Value104", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource103", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forecastCapacityValues105: BinaryAssociation = BinaryAssociation(
    name="forecastCapacityValues105",
    ends={
        Property(name="library_Value107", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource106", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments117: BinaryAssociation = BinaryAssociation(
    name="equipments117",
    ends={
        Property(name="library_Equipment119", type=library_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NodeType118", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentRef120: BinaryAssociation = BinaryAssociation(
    name="equipmentRef120",
    ends={
        Property(name="library_Equipment121", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
licensedFunctionRef122: BinaryAssociation = BinaryAssociation(
    name="licensedFunctionRef122",
    ends={
        Property(name="library_Function124", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo123", type=library_Function, multiplicity=Multiplicity(0, 9999))
    }
)
nodeTypeRef125: BinaryAssociation = BinaryAssociation(
    name="nodeTypeRef125",
    ends={
        Property(name="library_NodeType127", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo126", type=library_NodeType, multiplicity=Multiplicity(0, 9999))
    }
)
nodeTypes130: BinaryAssociation = BinaryAssociation(
    name="nodeTypes130",
    ends={
        Property(name="library_NodeType132", type=library_ReferenceNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ReferenceNetwork131", type=library_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceNetworks134: BinaryAssociation = BinaryAssociation(
    name="referenceNetworks134",
    ends={
        Property(name="library_ReferenceNetwork135", type=library_ReferenceNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ReferenceNetwork133", type=library_ReferenceNetwork, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagrams128: BinaryAssociation = BinaryAssociation(
    name="diagrams128",
    ends={
        Property(name="library_DiagramInfo129", type=library_ReferenceNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ReferenceNetwork", type=library_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocolRef138: BinaryAssociation = BinaryAssociation(
    name="protocolRef138",
    ends={
        Property(name="library_Protocol140", type=library_ReferenceRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ReferenceRelationship139", type=library_Protocol, multiplicity=Multiplicity(0, 1))
    }
)
refRelationships136: BinaryAssociation = BinaryAssociation(
    name="refRelationships136",
    ends={
        Property(name="library_ReferenceRelationship", type=library_ReferenceNetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ReferenceNetwork137", type=library_ReferenceRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refInterface1Ref141: BinaryAssociation = BinaryAssociation(
    name="refInterface1Ref141",
    ends={
        Property(name="library_NodeType143", type=library_ReferenceRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ReferenceRelationship142", type=library_NodeType, multiplicity=Multiplicity(0, 1))
    }
)
refInterface2Ref144: BinaryAssociation = BinaryAssociation(
    name="refInterface2Ref144",
    ends={
        Property(name="library_NodeType146", type=library_ReferenceRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ReferenceRelationship145", type=library_NodeType, multiplicity=Multiplicity(0, 1))
    }
)
icons150: BinaryAssociation = BinaryAssociation(
    name="icons150",
    ends={
        Property(name="library_MultiImage152", type=library_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Unit151", type=library_MultiImage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionRef147: BinaryAssociation = BinaryAssociation(
    name="expressionRef147",
    ends={
        Property(name="library_Expression149", type=library_Tolerance, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Tolerance148", type=library_Expression, multiplicity=Multiplicity(0, 1))
    }
)
products153: BinaryAssociation = BinaryAssociation(
    name="products153",
    ends={
        Property(name="library_ProductInfo154", type=library_Vendor, multiplicity=Multiplicity(1, 1)),
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
gen_library_NodeType_Base = Generalization(general=Base, specific=library_NodeType)
gen_library_Parameter_Base = Generalization(general=Base, specific=library_Parameter)
gen_library_ProductInfo_Base = Generalization(general=Base, specific=library_ProductInfo)
gen_library_ReferenceNetwork_Base = Generalization(general=Base, specific=library_ReferenceNetwork)
gen_library_ReferenceRelationship_Base = Generalization(general=Base, specific=library_ReferenceRelationship)
gen_library_Tolerance_Base = Generalization(general=Base, specific=library_Tolerance)
gen_library_Unit_Base = Generalization(general=Base, specific=library_Unit)
gen_library_Vendor_Company = Generalization(general=Company, specific=library_Vendor)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_BaseExpressionResult, library_BaseResource, Base, library_Expression, library_Unit, library_Tolerance, library_Protocol, library_Component, library_Parameter, library_Lifecycle, library_NetXResource, library_ConfigAttribute, library_Metric, library_Equipment, Component, library_DiagramInfo, library_MultiImage, library_EquipmentGroup, library_EquipmentRelationship, library_EObject, library_ExpressionResult, BaseExpressionResult, library_Value, library_Function, library_FunctionRelationship, library_LastEvaluationExpressionResult, library_Library, library_NodeType, library_MetricSource, library_Meta, library_MetricValueRange, BaseResource, library_ProductInfo, library_ReferenceRelationship, library_ReferenceNetwork, library_Vendor, Company, LevelKind, RedundancyType, RangeKind, StateType},
    associations={capacityExpressionRef7, utilizationExpressionRef9, unitRef0, toleranceRefs12, protocolRefs14, lifecycle1, resourceRefs2, configAttributes3, metricRefs5, equipments25, parameterRefs16, allResources18, diagrams20, icons22, allEquipments31, equipmentGroups26, equipmentRelationshipRefs28, diagrams33, equipmentRefs42, parameterRefs45, equipmentGroupResources36, expressionRefs39, allEquipments51, allEquipmentResources48, evaluationObject54, targetResource56, targetValues58, functions61, functionRelationshipRefs62, allFunctions65, equipments71, functions67, nodeTypes69, metrics74, metricSources77, parameters79, version91, tolerances82, expressions85, units88, metricValueRanges97, componentRef93, metricRef94, forecastValues108, trendedValues111, capacityValues99, functions114, utilizationValues102, forecastCapacityValues105, equipments117, equipmentRef120, licensedFunctionRef122, nodeTypeRef125, nodeTypes130, referenceNetworks134, diagrams128, protocolRef138, refRelationships136, refInterface1Ref141, refInterface2Ref144, icons150, expressionRef147, products153},
    generalizations={gen_library_BaseResource_Base, gen_library_Component_Base, gen_library_Equipment_Component, gen_library_EquipmentGroup_Base, gen_library_Expression_Base, gen_library_ExpressionResult_BaseExpressionResult, gen_library_Function_Component, gen_library_LastEvaluationExpressionResult_BaseExpressionResult, gen_library_NetXResource_BaseResource, gen_library_NodeType_Base, gen_library_Parameter_Base, gen_library_ProductInfo_Base, gen_library_ReferenceNetwork_Base, gen_library_ReferenceRelationship_Base, gen_library_Tolerance_Base, gen_library_Unit_Base, gen_library_Vendor_Company},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)