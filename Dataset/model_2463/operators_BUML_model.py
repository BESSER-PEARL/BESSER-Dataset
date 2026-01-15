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
			EnumerationLiteral(name="THRESHOLDREACHED")
    }
)

# Classes
operators_EquipmentRelationship = Class(name="operators::EquipmentRelationship")
Relationship = Class(name="Relationship")
operators_Equipment = Class(name="operators::Equipment")
operators_ExpansionExperience = Class(name="operators::ExpansionExperience")
operators_Marker = Class(name="operators::Marker")
operators_FunctionRelationship = Class(name="operators::FunctionRelationship")
operators_Function = Class(name="operators::Function")
operators_Value = Class(name="operators::Value")
operators_Node = Class(name="operators::Node")
operators_Network = Class(name="operators::Network")
operators_DiagramInfo = Class(name="operators::DiagramInfo")
operators_MetricSource = Class(name="operators::MetricSource")
operators_Person = Class(name="operators::Person")
operators_Lifecycle = Class(name="operators::Lifecycle")
operators_Warehouse = Class(name="operators::Warehouse")
operators_Room = Class(name="operators::Room")
operators_Operator = Class(name="operators::Operator")
Company = Class(name="Company")
operators_ResourceExpansion = Class(name="operators::ResourceExpansion")
operators_Service = Class(name="operators::Service")
operators_ServiceUser = Class(name="operators::ServiceUser")
operators_Protocol = Class(name="operators::Protocol")
operators_Relationship = Class(name="operators::Relationship")
operators_ResourceForecast = Class(name="operators::ResourceForecast")
operators_ResourceMonitor = Class(name="operators::ResourceMonitor")

# operators_EquipmentRelationship class attributes and methods

# Relationship class attributes and methods

# operators_Equipment class attributes and methods

# operators_ExpansionExperience class attributes and methods
operators_ExpansionExperience_duration: Property = Property(name="duration", type=StringType)
operators_ExpansionExperience.attributes={operators_ExpansionExperience_duration}

# operators_Marker class attributes and methods
operators_Marker_kind: Property = Property(name="kind", type=StringType)
operators_Marker_description: Property = Property(name="description", type=StringType)
operators_Marker.attributes={operators_Marker_kind, operators_Marker_description}

# operators_FunctionRelationship class attributes and methods

# operators_Function class attributes and methods

# operators_Value class attributes and methods

# operators_Node class attributes and methods
operators_Node_nodeID: Property = Property(name="nodeID", type=StringType)
operators_Node.attributes={operators_Node_nodeID}

# operators_Network class attributes and methods
operators_Network_createdDate: Property = Property(name="createdDate", type=StringType)
operators_Network_description: Property = Property(name="description", type=StringType)
operators_Network_name: Property = Property(name="name", type=StringType)
operators_Network.attributes={operators_Network_description, operators_Network_createdDate, operators_Network_name}

# operators_DiagramInfo class attributes and methods

# operators_MetricSource class attributes and methods

# operators_Person class attributes and methods

# operators_Lifecycle class attributes and methods

# operators_Warehouse class attributes and methods
operators_Warehouse_equipments: Property = Property(name="equipments", type=StringType)
operators_Warehouse_description: Property = Property(name="description", type=StringType)
operators_Warehouse_name: Property = Property(name="name", type=StringType)
operators_Warehouse.attributes={operators_Warehouse_name, operators_Warehouse_description, operators_Warehouse_equipments}

# operators_Room class attributes and methods

# operators_Operator class attributes and methods

# Company class attributes and methods

# operators_ResourceExpansion class attributes and methods

# operators_Service class attributes and methods

# operators_ServiceUser class attributes and methods

# operators_Protocol class attributes and methods

# operators_Relationship class attributes and methods
operators_Relationship_name: Property = Property(name="name", type=StringType)
operators_Relationship.attributes={operators_Relationship_name}

# operators_ResourceForecast class attributes and methods

# operators_ResourceMonitor class attributes and methods

# Relationships
equipmentRef4: BinaryAssociation = BinaryAssociation(
    name="equipmentRef4",
    ends={
        Property(name="operators_Equipment5", type=operators_ExpansionExperience, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ExpansionExperience", type=operators_Equipment, multiplicity=Multiplicity(0, 1))
    }
)
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
equipmentRef10: BinaryAssociation = BinaryAssociation(
    name="equipmentRef10",
    ends={
        Property(name="operators_Equipment11", type=operators_Marker, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Marker", type=operators_Equipment, multiplicity=Multiplicity(0, 1))
    }
)
function1Ref6: BinaryAssociation = BinaryAssociation(
    name="function1Ref6",
    ends={
        Property(name="operators_Function", type=operators_FunctionRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_FunctionRelationship", type=operators_Function, multiplicity=Multiplicity(0, 1))
    }
)
function2Ref7: BinaryAssociation = BinaryAssociation(
    name="function2Ref7",
    ends={
        Property(name="operators_Function9", type=operators_FunctionRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_FunctionRelationship8", type=operators_Function, multiplicity=Multiplicity(0, 1))
    }
)
functionRef12: BinaryAssociation = BinaryAssociation(
    name="functionRef12",
    ends={
        Property(name="operators_Function14", type=operators_Marker, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Marker13", type=operators_Function, multiplicity=Multiplicity(0, 1))
    }
)
markerValueRef15: BinaryAssociation = BinaryAssociation(
    name="markerValueRef15",
    ends={
        Property(name="operators_Value", type=operators_Marker, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Marker16", type=operators_Value, multiplicity=Multiplicity(0, 1))
    }
)
nodes18: BinaryAssociation = BinaryAssociation(
    name="nodes18",
    ends={
        Property(name="operators_Node", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network19", type=operators_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
networks21: BinaryAssociation = BinaryAssociation(
    name="networks21",
    ends={
        Property(name="operators_Network22", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network20", type=operators_Network, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
diagrams17: BinaryAssociation = BinaryAssociation(
    name="diagrams17",
    ends={
        Property(name="operators_DiagramInfo", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network", type=operators_DiagramInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricSources29: BinaryAssociation = BinaryAssociation(
    name="metricSources29",
    ends={
        Property(name="operators_MetricSource", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network30", type=operators_MetricSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createdByRef31: BinaryAssociation = BinaryAssociation(
    name="createdByRef31",
    ends={
        Property(name="operators_Person", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network32", type=operators_Person, multiplicity=Multiplicity(0, 1))
    }
)
functionRelationships23: BinaryAssociation = BinaryAssociation(
    name="functionRelationships23",
    ends={
        Property(name="operators_FunctionRelationship25", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network24", type=operators_FunctionRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipmentRelationships26: BinaryAssociation = BinaryAssociation(
    name="equipmentRelationships26",
    ends={
        Property(name="operators_EquipmentRelationship28", type=operators_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Network27", type=operators_EquipmentRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lifecycle33: BinaryAssociation = BinaryAssociation(
    name="lifecycle33",
    ends={
        Property(name="operators_Lifecycle", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node34", type=operators_Lifecycle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions35: BinaryAssociation = BinaryAssociation(
    name="functions35",
    ends={
        Property(name="operators_Function37", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node36", type=operators_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalEquipmentRef44: BinaryAssociation = BinaryAssociation(
    name="originalEquipmentRef44",
    ends={
        Property(name="operators_Equipment46", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node45", type=operators_Equipment, multiplicity=Multiplicity(0, 1))
    }
)
originalFunctionRef47: BinaryAssociation = BinaryAssociation(
    name="originalFunctionRef47",
    ends={
        Property(name="operators_Function49", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node48", type=operators_Function, multiplicity=Multiplicity(0, 1))
    }
)
equipments38: BinaryAssociation = BinaryAssociation(
    name="equipments38",
    ends={
        Property(name="operators_Equipment40", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node39", type=operators_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createdByRef41: BinaryAssociation = BinaryAssociation(
    name="createdByRef41",
    ends={
        Property(name="operators_Person43", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node42", type=operators_Person, multiplicity=Multiplicity(0, 1))
    }
)
networks52: BinaryAssociation = BinaryAssociation(
    name="networks52",
    ends={
        Property(name="operators_Network53", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator", type=operators_Network, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
warehouses54: BinaryAssociation = BinaryAssociation(
    name="warehouses54",
    ends={
        Property(name="operators_Warehouse", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator55", type=operators_Warehouse, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
roomRef50: BinaryAssociation = BinaryAssociation(
    name="roomRef50",
    ends={
        Property(name="operators_Room", type=operators_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Node51", type=operators_Room, multiplicity=Multiplicity(0, 1))
    }
)
resourceExpansions60: BinaryAssociation = BinaryAssociation(
    name="resourceExpansions60",
    ends={
        Property(name="operators_ResourceExpansion", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator61", type=operators_ResourceExpansion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expansionExperiences62: BinaryAssociation = BinaryAssociation(
    name="expansionExperiences62",
    ends={
        Property(name="operators_ExpansionExperience64", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator63", type=operators_ExpansionExperience, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services56: BinaryAssociation = BinaryAssociation(
    name="services56",
    ends={
        Property(name="operators_Service", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator57", type=operators_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceUsers58: BinaryAssociation = BinaryAssociation(
    name="serviceUsers58",
    ends={
        Property(name="operators_ServiceUser", type=operators_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Operator59", type=operators_ServiceUser, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodeID2Ref67: BinaryAssociation = BinaryAssociation(
    name="nodeID2Ref67",
    ends={
        Property(name="operators_Node69", type=operators_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Relationship68", type=operators_Node, multiplicity=Multiplicity(0, 1))
    }
)
protocolRef70: BinaryAssociation = BinaryAssociation(
    name="protocolRef70",
    ends={
        Property(name="operators_Protocol", type=operators_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Relationship71", type=operators_Protocol, multiplicity=Multiplicity(0, 1))
    }
)
nodeID1Ref65: BinaryAssociation = BinaryAssociation(
    name="nodeID1Ref65",
    ends={
        Property(name="operators_Node66", type=operators_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Relationship", type=operators_Node, multiplicity=Multiplicity(0, 1))
    }
)
functionRefs78: BinaryAssociation = BinaryAssociation(
    name="functionRefs78",
    ends={
        Property(name="operators_Function80", type=operators_ResourceExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceExpansion79", type=operators_Function, multiplicity=Multiplicity(0, 9999))
    }
)
nodeRefs72: BinaryAssociation = BinaryAssociation(
    name="nodeRefs72",
    ends={
        Property(name="operators_Node74", type=operators_ResourceExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceExpansion73", type=operators_Node, multiplicity=Multiplicity(0, 9999))
    }
)
equipmentRefs75: BinaryAssociation = BinaryAssociation(
    name="equipmentRefs75",
    ends={
        Property(name="operators_Equipment77", type=operators_ResourceExpansion, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceExpansion76", type=operators_Equipment, multiplicity=Multiplicity(0, 9999))
    }
)
nodes85: BinaryAssociation = BinaryAssociation(
    name="nodes85",
    ends={
        Property(name="operators_Node87", type=operators_Warehouse, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_Warehouse86", type=operators_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
markers81: BinaryAssociation = BinaryAssociation(
    name="markers81",
    ends={
        Property(name="operators_Marker82", type=operators_ResourceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceForecast", type=operators_Marker, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
markers83: BinaryAssociation = BinaryAssociation(
    name="markers83",
    ends={
        Property(name="operators_Marker84", type=operators_ResourceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_ResourceMonitor", type=operators_Marker, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_operators_EquipmentRelationship_Relationship = Generalization(general=Relationship, specific=operators_EquipmentRelationship)
gen_operators_FunctionRelationship_Relationship = Generalization(general=Relationship, specific=operators_FunctionRelationship)
gen_operators_Operator_Company = Generalization(general=Company, specific=operators_Operator)

# Domain Model
domain_model = DomainModel(
    name="operators",
    types={operators_EquipmentRelationship, Relationship, operators_Equipment, operators_ExpansionExperience, operators_Marker, operators_FunctionRelationship, operators_Function, operators_Value, operators_Node, operators_Network, operators_DiagramInfo, operators_MetricSource, operators_Person, operators_Lifecycle, operators_Warehouse, operators_Room, operators_Operator, Company, operators_ResourceExpansion, operators_Service, operators_ServiceUser, operators_Protocol, operators_Relationship, operators_ResourceForecast, operators_ResourceMonitor, MarkerKind},
    associations={equipmentRef4, equipment1Ref0, equipment2Ref1, equipmentRef10, function1Ref6, function2Ref7, functionRef12, markerValueRef15, nodes18, networks21, diagrams17, metricSources29, createdByRef31, functionRelationships23, equipmentRelationships26, lifecycle33, functions35, originalEquipmentRef44, originalFunctionRef47, equipments38, createdByRef41, networks52, warehouses54, roomRef50, resourceExpansions60, expansionExperiences62, services56, serviceUsers58, nodeID2Ref67, protocolRef70, nodeID1Ref65, functionRefs78, nodeRefs72, equipmentRefs75, nodes85, markers81, markers83},
    generalizations={gen_operators_EquipmentRelationship_Relationship, gen_operators_FunctionRelationship_Relationship, gen_operators_Operator_Company},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)