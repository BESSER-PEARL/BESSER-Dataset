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

OSIType: Enumeration = Enumeration(
    name="OSIType",
    literals={
            EnumerationLiteral(name="Application"),
			EnumerationLiteral(name="Presentation"),
			EnumerationLiteral(name="Session"),
			EnumerationLiteral(name="Transport"),
			EnumerationLiteral(name="Network"),
			EnumerationLiteral(name="DataLink"),
			EnumerationLiteral(name="Physiscal")
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
library_Equipment = Class(name="library_Equipment")
library_Lifecycle = Class(name="library_Lifecycle")
library_EquipmentRelationship = Class(name="library_EquipmentRelationship")
library_Expression = Class(name="library_Expression")
library_Tolerance = Class(name="library_Tolerance")
library_DiagramInfo = Class(name="library_DiagramInfo")
library_EquipmentGroup = Class(name="library_EquipmentGroup")
library_NetXResource = Class(name="library_NetXResource")
library_Metric = Class(name="library_Metric")
library_Protocol = Class(name="library_Protocol")
library_Parameter = Class(name="library_Parameter")
library_MultiImage = Class(name="library_MultiImage")
library_Function = Class(name="library_Function")
library_ServiceProfile = Class(name="library_ServiceProfile")
library_FunctionRelationship = Class(name="library_FunctionRelationship")
library_Library = Class(name="library_Library")
library_NodeType = Class(name="library_NodeType")
library_Message = Class(name="library_Message")
library_Unit = Class(name="library_Unit")
library_Meta = Class(name="library_Meta")
library_Value = Class(name="library_Value")
library_MetricValueRange = Class(name="library_MetricValueRange")
library_Procedure = Class(name="library_Procedure")
library_ProductInfo = Class(name="library_ProductInfo")
library_Company = Class(name="library_Company")
library_Vendor = Class(name="library_Vendor")
Company = Class(name="Company")

# library_Equipment class attributes and methods
library_Equipment_count: Property = Property(name="count", type=StringType)
library_Equipment_description: Property = Property(name="description", type=StringType)
library_Equipment_equipmentCode: Property = Property(name="equipmentCode", type=StringType)
library_Equipment_equipmentName: Property = Property(name="equipmentName", type=StringType)
library_Equipment_position: Property = Property(name="position", type=StringType)
library_Equipment_redundancy: Property = Property(name="redundancy", type=StringType)
library_Equipment_state: Property = Property(name="state", type=StringType)
library_Equipment.attributes={library_Equipment_state, library_Equipment_description, library_Equipment_equipmentName, library_Equipment_equipmentCode, library_Equipment_position, library_Equipment_redundancy, library_Equipment_count}

# library_Lifecycle class attributes and methods

# library_EquipmentRelationship class attributes and methods

# library_Expression class attributes and methods
library_Expression_expressionLines: Property = Property(name="expressionLines", type=StringType)
library_Expression_name: Property = Property(name="name", type=StringType)
library_Expression.attributes={library_Expression_name, library_Expression_expressionLines}

# library_Tolerance class attributes and methods
library_Tolerance_expression: Property = Property(name="expression", type=StringType)
library_Tolerance_level: Property = Property(name="level", type=StringType)
library_Tolerance_name: Property = Property(name="name", type=StringType)
library_Tolerance.attributes={library_Tolerance_name, library_Tolerance_level, library_Tolerance_expression}

# library_DiagramInfo class attributes and methods

# library_EquipmentGroup class attributes and methods
library_EquipmentGroup_description: Property = Property(name="description", type=StringType)
library_EquipmentGroup_name: Property = Property(name="name", type=StringType)
library_EquipmentGroup_count: Property = Property(name="count", type=StringType)
library_EquipmentGroup.attributes={library_EquipmentGroup_description, library_EquipmentGroup_count, library_EquipmentGroup_name}

# library_NetXResource class attributes and methods
library_NetXResource_detailDisplay: Property = Property(name="detailDisplay", type=StringType)
library_NetXResource_expressionName: Property = Property(name="expressionName", type=StringType)
library_NetXResource_longName: Property = Property(name="longName", type=StringType)
library_NetXResource_shortName: Property = Property(name="shortName", type=StringType)
library_NetXResource_summaryDisplay: Property = Property(name="summaryDisplay", type=StringType)
library_NetXResource.attributes={library_NetXResource_detailDisplay, library_NetXResource_longName, library_NetXResource_shortName, library_NetXResource_summaryDisplay, library_NetXResource_expressionName}

# library_Metric class attributes and methods

# library_Protocol class attributes and methods
library_Protocol_name: Property = Property(name="name", type=StringType)
library_Protocol_oSI: Property = Property(name="oSI", type=StringType)
library_Protocol_specification: Property = Property(name="specification", type=StringType)
library_Protocol_description: Property = Property(name="description", type=StringType)
library_Protocol.attributes={library_Protocol_oSI, library_Protocol_specification, library_Protocol_description, library_Protocol_name}

# library_Parameter class attributes and methods
library_Parameter_modifiable: Property = Property(name="modifiable", type=StringType)
library_Parameter_name: Property = Property(name="name", type=StringType)
library_Parameter_value: Property = Property(name="value", type=StringType)
library_Parameter_description: Property = Property(name="description", type=StringType)
library_Parameter_expressionName: Property = Property(name="expressionName", type=StringType)
library_Parameter.attributes={library_Parameter_value, library_Parameter_name, library_Parameter_description, library_Parameter_expressionName, library_Parameter_modifiable}

# library_MultiImage class attributes and methods

# library_Function class attributes and methods
library_Function_functionName: Property = Property(name="functionName", type=StringType)
library_Function_description: Property = Property(name="description", type=StringType)
library_Function.attributes={library_Function_functionName, library_Function_description}

# library_ServiceProfile class attributes and methods

# library_FunctionRelationship class attributes and methods

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_NodeType class attributes and methods

# library_Message class attributes and methods
library_Message_name: Property = Property(name="name", type=StringType)
library_Message.attributes={library_Message_name}

# library_Unit class attributes and methods
library_Unit_code: Property = Property(name="code", type=StringType)
library_Unit_description: Property = Property(name="description", type=StringType)
library_Unit_name: Property = Property(name="name", type=StringType)
library_Unit.attributes={library_Unit_code, library_Unit_description, library_Unit_name}

# library_Meta class attributes and methods
library_Meta_author: Property = Property(name="author", type=StringType)
library_Meta_description: Property = Property(name="description", type=StringType)
library_Meta_version: Property = Property(name="version", type=StringType)
library_Meta.attributes={library_Meta_version, library_Meta_description, library_Meta_author}

# library_Value class attributes and methods

# library_MetricValueRange class attributes and methods

# library_Procedure class attributes and methods
library_Procedure_name: Property = Property(name="name", type=StringType)
library_Procedure.attributes={library_Procedure_name}

# library_ProductInfo class attributes and methods
library_ProductInfo_availableDate: Property = Property(name="availableDate", type=StringType)
library_ProductInfo_endOfSalesDate: Property = Property(name="endOfSalesDate", type=StringType)
library_ProductInfo_endOfSupportDate: Property = Property(name="endOfSupportDate", type=StringType)
library_ProductInfo_productCode: Property = Property(name="productCode", type=StringType)
library_ProductInfo_salesCode: Property = Property(name="salesCode", type=StringType)
library_ProductInfo_underDevelopmentDate: Property = Property(name="underDevelopmentDate", type=StringType)
library_ProductInfo.attributes={library_ProductInfo_endOfSupportDate, library_ProductInfo_underDevelopmentDate, library_ProductInfo_endOfSalesDate, library_ProductInfo_salesCode, library_ProductInfo_productCode, library_ProductInfo_availableDate}

# library_Company class attributes and methods

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
toleranceRefs15: BinaryAssociation = BinaryAssociation(
    name="toleranceRefs15",
    ends={
        Property(name="library_Tolerance", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment16", type=library_Tolerance, multiplicity=Multiplicity(0, 9999))
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
protocolRefs17: BinaryAssociation = BinaryAssociation(
    name="protocolRefs17",
    ends={
        Property(name="library_Protocol", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment18", type=library_Protocol, multiplicity=Multiplicity(0, 9999))
    }
)
parameterRefs19: BinaryAssociation = BinaryAssociation(
    name="parameterRefs19",
    ends={
        Property(name="library_Parameter", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment20", type=library_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipmentResources21: BinaryAssociation = BinaryAssociation(
    name="allEquipmentResources21",
    ends={
        Property(name="library_NetXResource23", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment22", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipments25: BinaryAssociation = BinaryAssociation(
    name="allEquipments25",
    ends={
        Property(name="library_Equipment26", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment24", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
icons27: BinaryAssociation = BinaryAssociation(
    name="icons27",
    ends={
        Property(name="library_MultiImage", type=library_Equipment, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Equipment28", type=library_MultiImage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equipmentGroupResources32: BinaryAssociation = BinaryAssociation(
    name="equipmentGroupResources32",
    ends={
        Property(name="library_NetXResource34", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup33", type=library_NetXResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionRefs35: BinaryAssociation = BinaryAssociation(
    name="expressionRefs35",
    ends={
        Property(name="Expression36", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="equipmentGroupRefs", type=library_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentRefs37: BinaryAssociation = BinaryAssociation(
    name="equipmentRefs37",
    ends={
        Property(name="library_Equipment39", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup38", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
diagrams29: BinaryAssociation = BinaryAssociation(
    name="diagrams29",
    ends={
        Property(name="library_DiagramInfo31", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup30", type=library_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterRefs40: BinaryAssociation = BinaryAssociation(
    name="parameterRefs40",
    ends={
        Property(name="library_Parameter42", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup41", type=library_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipmentResources43: BinaryAssociation = BinaryAssociation(
    name="allEquipmentResources43",
    ends={
        Property(name="library_NetXResource45", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup44", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
allEquipments46: BinaryAssociation = BinaryAssociation(
    name="allEquipments46",
    ends={
        Property(name="library_Equipment48", type=library_EquipmentGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EquipmentGroup47", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
diagrams53: BinaryAssociation = BinaryAssociation(
    name="diagrams53",
    ends={
        Property(name="library_DiagramInfo54", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function", type=library_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
icons55: BinaryAssociation = BinaryAssociation(
    name="icons55",
    ends={
        Property(name="library_MultiImage57", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function56", type=library_MultiImage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equipmentRefs49: BinaryAssociation = BinaryAssociation(
    name="equipmentRefs49",
    ends={
        Property(name="Equipment", type=library_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="equipmentExpressionRefs", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
functionRefs50: BinaryAssociation = BinaryAssociation(
    name="functionRefs50",
    ends={
        Property(name="Function", type=library_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="functionExpressionRefs", type=library_Function, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentGroupRefs51: BinaryAssociation = BinaryAssociation(
    name="equipmentGroupRefs51",
    ends={
        Property(name="EquipmentGroup", type=library_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionRefs", type=library_EquipmentGroup, multiplicity=Multiplicity(0, 9999))
    }
)
serviceProfileRefs52: BinaryAssociation = BinaryAssociation(
    name="serviceProfileRefs52",
    ends={
        Property(name="library_ServiceProfile", type=library_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Expression", type=library_ServiceProfile, multiplicity=Multiplicity(0, 9999))
    }
)
functionRelationshipRefs67: BinaryAssociation = BinaryAssociation(
    name="functionRelationshipRefs67",
    ends={
        Property(name="library_Function68", type=library_FunctionRelationship, multiplicity=Multiplicity(0, 9999)),
        Property(name="library_FunctionRelationship", type=library_Function, multiplicity=Multiplicity(1, 1))
    }
)
functionExpressionRefs69: BinaryAssociation = BinaryAssociation(
    name="functionExpressionRefs69",
    ends={
        Property(name="Expression70", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="functionRefs", type=library_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
toleranceRefs71: BinaryAssociation = BinaryAssociation(
    name="toleranceRefs71",
    ends={
        Property(name="library_Tolerance73", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function72", type=library_Tolerance, multiplicity=Multiplicity(0, 9999))
    }
)
functions59: BinaryAssociation = BinaryAssociation(
    name="functions59",
    ends={
        Property(name="library_Function60", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function58", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionResources61: BinaryAssociation = BinaryAssociation(
    name="functionResources61",
    ends={
        Property(name="library_NetXResource63", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function62", type=library_NetXResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionMetricRefs64: BinaryAssociation = BinaryAssociation(
    name="functionMetricRefs64",
    ends={
        Property(name="library_Metric66", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function65", type=library_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
protocolRefs74: BinaryAssociation = BinaryAssociation(
    name="protocolRefs74",
    ends={
        Property(name="library_Protocol76", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function75", type=library_Protocol, multiplicity=Multiplicity(0, 9999))
    }
)
parameterRefs77: BinaryAssociation = BinaryAssociation(
    name="parameterRefs77",
    ends={
        Property(name="library_Parameter79", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function78", type=library_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
allFunctionResources80: BinaryAssociation = BinaryAssociation(
    name="allFunctionResources80",
    ends={
        Property(name="library_NetXResource82", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function81", type=library_NetXResource, multiplicity=Multiplicity(0, 9999))
    }
)
allFunctions84: BinaryAssociation = BinaryAssociation(
    name="allFunctions84",
    ends={
        Property(name="library_Function85", type=library_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Function83", type=library_Function, multiplicity=Multiplicity(0, 9999))
    }
)
functions86: BinaryAssociation = BinaryAssociation(
    name="functions86",
    ends={
        Property(name="library_Function87", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeTypes88: BinaryAssociation = BinaryAssociation(
    name="nodeTypes88",
    ends={
        Property(name="library_NodeType", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library89", type=library_NodeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments90: BinaryAssociation = BinaryAssociation(
    name="equipments90",
    ends={
        Property(name="library_Equipment92", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library91", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metrics93: BinaryAssociation = BinaryAssociation(
    name="metrics93",
    ends={
        Property(name="library_Metric95", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library94", type=library_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocols99: BinaryAssociation = BinaryAssociation(
    name="protocols99",
    ends={
        Property(name="library_Protocol101", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library100", type=library_Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tolerances102: BinaryAssociation = BinaryAssociation(
    name="tolerances102",
    ends={
        Property(name="library_Tolerance104", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library103", type=library_Tolerance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters96: BinaryAssociation = BinaryAssociation(
    name="parameters96",
    ends={
        Property(name="library_Parameter98", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library97", type=library_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions105: BinaryAssociation = BinaryAssociation(
    name="expressions105",
    ends={
        Property(name="library_Expression107", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library106", type=library_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units108: BinaryAssociation = BinaryAssociation(
    name="units108",
    ends={
        Property(name="library_Unit", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library109", type=library_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
version110: BinaryAssociation = BinaryAssociation(
    name="version110",
    ends={
        Property(name="library_Meta", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library111", type=library_Meta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
capacityValues114: BinaryAssociation = BinaryAssociation(
    name="capacityValues114",
    ends={
        Property(name="library_Value", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource115", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forecastCapacityValues116: BinaryAssociation = BinaryAssociation(
    name="forecastCapacityValues116",
    ends={
        Property(name="library_Value118", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource117", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forecastValues119: BinaryAssociation = BinaryAssociation(
    name="forecastValues119",
    ends={
        Property(name="library_Value121", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource120", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricValueRanges112: BinaryAssociation = BinaryAssociation(
    name="metricValueRanges112",
    ends={
        Property(name="library_MetricValueRange", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource113", type=library_MetricValueRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unitRef125: BinaryAssociation = BinaryAssociation(
    name="unitRef125",
    ends={
        Property(name="library_Unit127", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource126", type=library_Unit, multiplicity=Multiplicity(0, 1))
    }
)
trendedValues122: BinaryAssociation = BinaryAssociation(
    name="trendedValues122",
    ends={
        Property(name="library_Value124", type=library_NetXResource, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NetXResource123", type=library_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions128: BinaryAssociation = BinaryAssociation(
    name="functions128",
    ends={
        Property(name="library_Function130", type=library_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NodeType129", type=library_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments131: BinaryAssociation = BinaryAssociation(
    name="equipments131",
    ends={
        Property(name="library_Equipment133", type=library_NodeType, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NodeType132", type=library_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messages134: BinaryAssociation = BinaryAssociation(
    name="messages134",
    ends={
        Property(name="library_Message", type=library_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Procedure", type=library_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentRef135: BinaryAssociation = BinaryAssociation(
    name="equipmentRef135",
    ends={
        Property(name="library_Equipment136", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo", type=library_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
licensedFunctionRef137: BinaryAssociation = BinaryAssociation(
    name="licensedFunctionRef137",
    ends={
        Property(name="library_Function139", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo138", type=library_Function, multiplicity=Multiplicity(0, 9999))
    }
)
nodeTypeRef140: BinaryAssociation = BinaryAssociation(
    name="nodeTypeRef140",
    ends={
        Property(name="library_NodeType142", type=library_ProductInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="library_ProductInfo141", type=library_NodeType, multiplicity=Multiplicity(0, 9999))
    }
)
procedures143: BinaryAssociation = BinaryAssociation(
    name="procedures143",
    ends={
        Property(name="library_Procedure145", type=library_Protocol, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Protocol144", type=library_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyRef146: BinaryAssociation = BinaryAssociation(
    name="bodyRef146",
    ends={
        Property(name="library_Company", type=library_Protocol, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Protocol147", type=library_Company, multiplicity=Multiplicity(0, 1))
    }
)
icons148: BinaryAssociation = BinaryAssociation(
    name="icons148",
    ends={
        Property(name="library_MultiImage150", type=library_Unit, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Unit149", type=library_MultiImage, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
products151: BinaryAssociation = BinaryAssociation(
    name="products151",
    ends={
        Property(name="library_ProductInfo152", type=library_Vendor, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Vendor", type=library_ProductInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_Vendor_Company = Generalization(general=Company, specific=library_Vendor)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Equipment, library_Lifecycle, library_EquipmentRelationship, library_Expression, library_Tolerance, library_DiagramInfo, library_EquipmentGroup, library_NetXResource, library_Metric, library_Protocol, library_Parameter, library_MultiImage, library_Function, library_ServiceProfile, library_FunctionRelationship, library_Library, library_NodeType, library_Message, library_Unit, library_Meta, library_Value, library_MetricValueRange, library_Procedure, library_ProductInfo, library_Company, library_Vendor, Company, LevelType, OSIType, RedundancyType, StateType},
    associations={lifecycle0, equipmentRelationshipRefs12, equipmentExpressionRefs14, toleranceRefs15, diagrams1, equipments4, equipmentGroups6, equipmentResources8, equipmentMetricRefs10, protocolRefs17, parameterRefs19, allEquipmentResources21, allEquipments25, icons27, equipmentGroupResources32, expressionRefs35, equipmentRefs37, diagrams29, parameterRefs40, allEquipmentResources43, allEquipments46, diagrams53, icons55, equipmentRefs49, functionRefs50, equipmentGroupRefs51, serviceProfileRefs52, functionRelationshipRefs67, functionExpressionRefs69, toleranceRefs71, functions59, functionResources61, functionMetricRefs64, protocolRefs74, parameterRefs77, allFunctionResources80, allFunctions84, functions86, nodeTypes88, equipments90, metrics93, protocols99, tolerances102, parameters96, expressions105, units108, version110, capacityValues114, forecastCapacityValues116, forecastValues119, metricValueRanges112, unitRef125, trendedValues122, functions128, equipments131, messages134, equipmentRef135, licensedFunctionRef137, nodeTypeRef140, procedures143, bodyRef146, icons148, products151},
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