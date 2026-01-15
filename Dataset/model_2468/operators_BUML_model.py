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
MarkerKind: Enumeration = Enumeration(
    name="MarkerKind",
    literals={
            EnumerationLiteral(name="value"),
			EnumerationLiteral(name="INTERNALEVENT"),
			EnumerationLiteral(name="EXTERNALEVENT"),
			EnumerationLiteral(name="ACTIONNEEDED"),
			EnumerationLiteral(name="TOLERANCECROSSED")
    }
)

ToleranceMarkerDirectionKind: Enumeration = Enumeration(
    name="ToleranceMarkerDirectionKind",
    literals={
            EnumerationLiteral(name="START"),
			EnumerationLiteral(name="UP"),
			EnumerationLiteral(name="DOWN")
    }
)

# Classes
operators_Equipment = Class(name="operators::Equipment")
operators_EquipmentRelationship = Class(name="operators::EquipmentRelationship")
Relationship = Class(name="Relationship")
operators_Marker = Class(name="operators::Marker")
Base = Class(name="Base")
operators_Value = Class(name="operators::Value")
operators_FunctionRelationship = Class(name="operators::FunctionRelationship")
operators_Function = Class(name="operators::Function")
operators_NetXResource = Class(name="operators::NetXResource")
operators_Network = Class(name="operators::Network")
operators_DiagramInfo = Class(name="operators::DiagramInfo")
operators_Node = Class(name="operators::Node")
operators_MetricSource = Class(name="operators::MetricSource")
operators_Person = Class(name="operators::Person")
operators_Location = Class(name="operators::Location")
operators_Lifecycle = Class(name="operators::Lifecycle")
operators_NodeType = Class(name="operators::NodeType")
operators_Warehouse = Class(name="operators::Warehouse")
operators_Service = Class(name="operators::Service")
operators_Operator = Class(name="operators::Operator")
Company = Class(name="Company")
operators_ServiceUser = Class(name="operators::ServiceUser")
operators_ResourceExpansion = Class(name="operators::ResourceExpansion")
operators_Relationship = Class(name="operators::Relationship")
operators_Protocol = Class(name="operators::Protocol")
operators_DateTimeRange = Class(name="operators::DateTimeRange")
operators_ResourceForecast = Class(name="operators::ResourceForecast")
operators_ResourceMonitor = Class(name="operators::ResourceMonitor")
operators_ToleranceMarker = Class(name="operators::ToleranceMarker")
Marker = Class(name="Marker")

# operators_Equipment class attributes and methods

# operators_EquipmentRelationship class attributes and methods

# Relationship class attributes and methods

# operators_Marker class attributes and methods
operators_Marker_description: Property = Property(name="description", type=StringType)
operators_Marker_kind: Property = Property(name="kind", type=StringType)
operators_Marker.attributes={operators_Marker_kind, operators_Marker_description}

# Base class attributes and methods

# operators_Value class attributes and methods

# operators_FunctionRelationship class attributes and methods

# operators_Function class attributes and methods

# operators_NetXResource class attributes and methods

# operators_Network class attributes and methods
operators_Network_description: Property = Property(name="description", type=StringType)
operators_Network_name: Property = Property(name="name", type=StringType)
operators_Network_createdDate: Property = Property(name="createdDate", type=StringType)
operators_Network.attributes={operators_Network_createdDate, operators_Network_name, operators_Network_description}

# operators_DiagramInfo class attributes and methods

# operators_Node class attributes and methods
operators_Node_nodeID: Property = Property(name="nodeID", type=StringType)
operators_Node.attributes={operators_Node_nodeID}

# operators_MetricSource class attributes and methods

# operators_Person class attributes and methods

# operators_Location class attributes and methods

# operators_Lifecycle class attributes and methods

# operators_NodeType class attributes and methods

# operators_Warehouse class attributes and methods
operators_Warehouse_description: Property = Property(name="description", type=StringType)
operators_Warehouse_name: Property = Property(name="name", type=StringType)
operators_Warehouse.attributes={operators_Warehouse_description, operators_Warehouse_name}

# operators_Service class attributes and methods

# operators_Operator class attributes and methods

# Company class attributes and methods

# operators_ServiceUser class attributes and methods

# operators_ResourceExpansion class attributes and methods

# operators_Relationship class attributes and methods
operators_Relationship_name: Property = Property(name="name", type=StringType)
operators_Relationship.attributes={operators_Relationship_name}

# operators_Protocol class attributes and methods

# operators_DateTimeRange class attributes and methods

# operators_ResourceForecast class attributes and methods

# operators_ResourceMonitor class attributes and methods

# operators_ToleranceMarker class attributes and methods
operators_ToleranceMarker_direction: Property = Property(name="direction", type=StringType)
operators_ToleranceMarker_level: Property = Property(name="level", type=StringType)
operators_ToleranceMarker.attributes={operators_ToleranceMarker_direction, operators_ToleranceMarker_level}

# Marker class attributes and methods

# Relationships
equipment1Ref0: BinaryAssociation = BinaryAssociation(
    name="equipment1Ref0",
    ends={
        Property(name="operators_Equipment", type=operators_EquipmentRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_EquipmentRelationship", type=operators_Equipment, multiplicity=Multiplicity(0, 1))
    }
)
equipment2Ref1: BinaryAssociation = BinaryAssociation(
    name="equipment2Ref1",
    ends={
        Property(name="operators_Equipment3", type=operators_EquipmentRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_EquipmentRelationship2", type=operators_Equipment, multiplicity=Multiplicity(0, 1))
    }
)
function1Ref4: BinaryAssociation = BinaryAssociation(
    name="function1Ref4",
    ends={
        Property(name="operators_Function", type=operators_FunctionRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_FunctionRelationship", type=operators_Function, multiplicity=Multiplicity(0, 1))
    }
)
function2Ref5: BinaryAssociation = BinaryAssociation(
    name="function2Ref5",
    ends={
        Property(name="operators_Function7", type=operators_FunctionRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_FunctionRelationship6", type=operators_Function, multiplicity=Multiplicity(0, 1))
    }
)
valueRef8: BinaryAssociation = BinaryAssociation(
    name="valueRef8",
    ends={
        Property(name="operators_Value", type=operators_Marker, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Marker", type=operators_Value, multiplicity=Multiplicity(0, 1))
    }
)
markerResourceRef9: BinaryAssociation = BinaryAssociation(
    name="markerResourceRef9",
    ends={
        Property(name="operators_NetXResource", type=operators_Marker, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Marker10", type=operators_NetXResource, multiplicity=Multiplicity(0, 1))
    }
)
functionRelationships17: BinaryAssociation = BinaryAssociation(
    name="functionRelationships17",
    ends={
        Property(name="operators_FunctionRelationship19", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network18", type=operators_FunctionRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagrams11: BinaryAssociation = BinaryAssociation(
    name="diagrams11",
    ends={
        Property(name="operators_DiagramInfo", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network", type=operators_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes12: BinaryAssociation = BinaryAssociation(
    name="nodes12",
    ends={
        Property(name="operators_Node", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network13", type=operators_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
networks15: BinaryAssociation = BinaryAssociation(
    name="networks15",
    ends={
        Property(name="operators_Network16", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network14", type=operators_Network, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentRelationships20: BinaryAssociation = BinaryAssociation(
    name="equipmentRelationships20",
    ends={
        Property(name="operators_EquipmentRelationship22", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network21", type=operators_EquipmentRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricSources23: BinaryAssociation = BinaryAssociation(
    name="metricSources23",
    ends={
        Property(name="operators_MetricSource", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network24", type=operators_MetricSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createdByRef25: BinaryAssociation = BinaryAssociation(
    name="createdByRef25",
    ends={
        Property(name="operators_Person", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network26", type=operators_Person, multiplicity=Multiplicity(0, 1))
    }
)
createdByRef31: BinaryAssociation = BinaryAssociation(
    name="createdByRef31",
    ends={
        Property(name="operators_Person33", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node32", type=operators_Person, multiplicity=Multiplicity(0, 1))
    }
)
locationRef34: BinaryAssociation = BinaryAssociation(
    name="locationRef34",
    ends={
        Property(name="operators_Location", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node35", type=operators_Location, multiplicity=Multiplicity(0, 1))
    }
)
lifecycle27: BinaryAssociation = BinaryAssociation(
    name="lifecycle27",
    ends={
        Property(name="operators_Lifecycle", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node28", type=operators_Lifecycle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodeType29: BinaryAssociation = BinaryAssociation(
    name="nodeType29",
    ends={
        Property(name="operators_NodeType", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node30", type=operators_NodeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
warehouses41: BinaryAssociation = BinaryAssociation(
    name="warehouses41",
    ends={
        Property(name="operators_Warehouse", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator42", type=operators_Warehouse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalNodeTypeRef36: BinaryAssociation = BinaryAssociation(
    name="originalNodeTypeRef36",
    ends={
        Property(name="operators_NodeType38", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node37", type=operators_NodeType, multiplicity=Multiplicity(0, 1))
    }
)
networks39: BinaryAssociation = BinaryAssociation(
    name="networks39",
    ends={
        Property(name="operators_Network40", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator", type=operators_Network, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeID1Ref49: BinaryAssociation = BinaryAssociation(
    name="nodeID1Ref49",
    ends={
        Property(name="operators_Node50", type=operators_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Relationship", type=operators_Node, multiplicity=Multiplicity(0, 1))
    }
)
services43: BinaryAssociation = BinaryAssociation(
    name="services43",
    ends={
        Property(name="operators_Service", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator44", type=operators_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceUsers45: BinaryAssociation = BinaryAssociation(
    name="serviceUsers45",
    ends={
        Property(name="operators_ServiceUser", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator46", type=operators_ServiceUser, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceExpansions47: BinaryAssociation = BinaryAssociation(
    name="resourceExpansions47",
    ends={
        Property(name="operators_ResourceExpansion", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator48", type=operators_ResourceExpansion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeRefs56: BinaryAssociation = BinaryAssociation(
    name="nodeRefs56",
    ends={
        Property(name="operators_Node58", type=operators_ResourceExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceExpansion57", type=operators_Node, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentRefs59: BinaryAssociation = BinaryAssociation(
    name="equipmentRefs59",
    ends={
        Property(name="operators_Equipment61", type=operators_ResourceExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceExpansion60", type=operators_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
nodeID2Ref51: BinaryAssociation = BinaryAssociation(
    name="nodeID2Ref51",
    ends={
        Property(name="operators_Node53", type=operators_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Relationship52", type=operators_Node, multiplicity=Multiplicity(0, 1))
    }
)
protocolRef54: BinaryAssociation = BinaryAssociation(
    name="protocolRef54",
    ends={
        Property(name="operators_Protocol", type=operators_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Relationship55", type=operators_Protocol, multiplicity=Multiplicity(0, 1))
    }
)
resourceRef72: BinaryAssociation = BinaryAssociation(
    name="resourceRef72",
    ends={
        Property(name="operators_NetXResource74", type=operators_ResourceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceMonitor73", type=operators_NetXResource, multiplicity=Multiplicity(0, 1))
    }
)
period75: BinaryAssociation = BinaryAssociation(
    name="period75",
    ends={
        Property(name="operators_DateTimeRange", type=operators_ResourceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceMonitor76", type=operators_DateTimeRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionRefs62: BinaryAssociation = BinaryAssociation(
    name="functionRefs62",
    ends={
        Property(name="operators_Function64", type=operators_ResourceExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceExpansion63", type=operators_Function, multiplicity=Multiplicity(0, 9999))
    }
)
markers65: BinaryAssociation = BinaryAssociation(
    name="markers65",
    ends={
        Property(name="operators_Marker66", type=operators_ResourceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceForecast", type=operators_Marker, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
markers67: BinaryAssociation = BinaryAssociation(
    name="markers67",
    ends={
        Property(name="operators_Marker68", type=operators_ResourceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceMonitor", type=operators_Marker, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeRef69: BinaryAssociation = BinaryAssociation(
    name="nodeRef69",
    ends={
        Property(name="operators_Node71", type=operators_ResourceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceMonitor70", type=operators_Node, multiplicity=Multiplicity(0, 1))
    }
)
nodes77: BinaryAssociation = BinaryAssociation(
    name="nodes77",
    ends={
        Property(name="operators_Node79", type=operators_Warehouse, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Warehouse78", type=operators_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments80: BinaryAssociation = BinaryAssociation(
    name="equipments80",
    ends={
        Property(name="operators_Equipment82", type=operators_Warehouse, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Warehouse81", type=operators_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_operators_EquipmentRelationship_Relationship = Generalization(general=Relationship, specific=operators_EquipmentRelationship)
gen_operators_Marker_Base = Generalization(general=Base, specific=operators_Marker)
gen_operators_FunctionRelationship_Relationship = Generalization(general=Relationship, specific=operators_FunctionRelationship)
gen_operators_Network_Base = Generalization(general=Base, specific=operators_Network)
gen_operators_Node_Base = Generalization(general=Base, specific=operators_Node)
gen_operators_Operator_Company = Generalization(general=Company, specific=operators_Operator)
gen_operators_Relationship_Base = Generalization(general=Base, specific=operators_Relationship)
gen_operators_ResourceExpansion_Base = Generalization(general=Base, specific=operators_ResourceExpansion)
gen_operators_ResourceForecast_Base = Generalization(general=Base, specific=operators_ResourceForecast)
gen_operators_ResourceMonitor_Base = Generalization(general=Base, specific=operators_ResourceMonitor)
gen_operators_ToleranceMarker_Marker = Generalization(general=Marker, specific=operators_ToleranceMarker)
gen_operators_Warehouse_Base = Generalization(general=Base, specific=operators_Warehouse)

# Domain Model
domain_model = DomainModel(
    name="operators",
    types={operators_Equipment, operators_EquipmentRelationship, Relationship, operators_Marker, Base, operators_Value, operators_FunctionRelationship, operators_Function, operators_NetXResource, operators_Network, operators_DiagramInfo, operators_Node, operators_MetricSource, operators_Person, operators_Location, operators_Lifecycle, operators_NodeType, operators_Warehouse, operators_Service, operators_Operator, Company, operators_ServiceUser, operators_ResourceExpansion, operators_Relationship, operators_Protocol, operators_DateTimeRange, operators_ResourceForecast, operators_ResourceMonitor, operators_ToleranceMarker, Marker, MarkerKind, ToleranceMarkerDirectionKind},
    associations={equipment1Ref0, equipment2Ref1, function1Ref4, function2Ref5, valueRef8, markerResourceRef9, functionRelationships17, diagrams11, nodes12, networks15, equipmentRelationships20, metricSources23, createdByRef25, createdByRef31, locationRef34, lifecycle27, nodeType29, warehouses41, originalNodeTypeRef36, networks39, nodeID1Ref49, services43, serviceUsers45, resourceExpansions47, nodeRefs56, equipmentRefs59, nodeID2Ref51, protocolRef54, resourceRef72, period75, functionRefs62, markers65, markers67, nodeRef69, nodes77, equipments80},
    generalizations={gen_operators_EquipmentRelationship_Relationship, gen_operators_Marker_Base, gen_operators_FunctionRelationship_Relationship, gen_operators_Network_Base, gen_operators_Node_Base, gen_operators_Operator_Company, gen_operators_Relationship_Base, gen_operators_ResourceExpansion_Base, gen_operators_ResourceForecast_Base, gen_operators_ResourceMonitor_Base, gen_operators_ToleranceMarker_Marker, gen_operators_Warehouse_Base},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)