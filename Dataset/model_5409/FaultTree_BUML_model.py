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
fault_tree_Hazard = Class(name="fault::tree::Hazard")
Event = Class(name="Event")
fault_tree_IntermediateEvent = Class(name="fault::tree::IntermediateEvent")
fault_tree_Gate = Class(name="fault::tree::Gate", is_abstract=True)
IDBase = Class(name="IDBase")
fault_tree_Event = Class(name="fault::tree::Event", is_abstract=True)
fault_tree_FailureInstance = Class(name="fault::tree::FailureInstance")
fault_tree_FailureType = Class(name="fault::tree::FailureType")
fault_tree_FaultTree = Class(name="fault::tree::FaultTree")
fault_tree_OR = Class(name="fault::tree::OR")
Gate = Class(name="Gate")
fault_tree_AND = Class(name="fault::tree::AND")
fault_tree_XOR = Class(name="fault::tree::XOR")
fault_tree_PriorAND = Class(name="fault::tree::PriorAND")
fault_tree_Inhibit = Class(name="fault::tree::Inhibit")
fault_tree_ErrorInstance = Class(name="fault::tree::ErrorInstance")
fault_tree_BasicEvent = Class(name="fault::tree::BasicEvent")
fault_tree_UndevelopedEvent = Class(name="fault::tree::UndevelopedEvent")
fault_tree_ErrorType = Class(name="fault::tree::ErrorType")

# fault_tree_Hazard class attributes and methods

# Event class attributes and methods

# fault_tree_IntermediateEvent class attributes and methods

# fault_tree_Gate class attributes and methods

# IDBase class attributes and methods

# fault_tree_Event class attributes and methods
fault_tree_Event_description: Property = Property(name="description", type=StringType)
fault_tree_Event_name: Property = Property(name="name", type=StringType)
fault_tree_Event.attributes={fault_tree_Event_description, fault_tree_Event_name}

# fault_tree_FailureInstance class attributes and methods
fault_tree_FailureInstance_name: Property = Property(name="name", type=StringType)
fault_tree_FailureInstance.attributes={fault_tree_FailureInstance_name}

# fault_tree_FailureType class attributes and methods
fault_tree_FailureType_name: Property = Property(name="name", type=StringType)
fault_tree_FailureType.attributes={fault_tree_FailureType_name}

# fault_tree_FaultTree class attributes and methods

# fault_tree_OR class attributes and methods

# Gate class attributes and methods

# fault_tree_AND class attributes and methods

# fault_tree_XOR class attributes and methods

# fault_tree_PriorAND class attributes and methods

# fault_tree_Inhibit class attributes and methods

# fault_tree_ErrorInstance class attributes and methods
fault_tree_ErrorInstance_name: Property = Property(name="name", type=StringType)
fault_tree_ErrorInstance.attributes={fault_tree_ErrorInstance_name}

# fault_tree_BasicEvent class attributes and methods
fault_tree_BasicEvent_probability: Property = Property(name="probability", type=FloatType)
fault_tree_BasicEvent.attributes={fault_tree_BasicEvent_probability}

# fault_tree_UndevelopedEvent class attributes and methods

# fault_tree_ErrorType class attributes and methods
fault_tree_ErrorType_name: Property = Property(name="name", type=StringType)
fault_tree_ErrorType.attributes={fault_tree_ErrorType_name}

# Relationships
inEvent0: BinaryAssociation = BinaryAssociation(
    name="inEvent0",
    ends={
        Property(name="fault_tree_IntermediateEvent", type=fault_tree_Hazard, multiplicity=Multiplicity(1, 1)),
        Property(name="fault_tree_Hazard", type=fault_tree_IntermediateEvent, multiplicity=Multiplicity(0, 1))
    }
)
inputGates2: BinaryAssociation = BinaryAssociation(
    name="inputGates2",
    ends={
        Property(name="fault_tree_Gate", type=fault_tree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="fault_tree_Gate1", type=fault_tree_Gate, multiplicity=Multiplicity(0, 9999))
    }
)
instance15: BinaryAssociation = BinaryAssociation(
    name="instance15",
    ends={
        Property(name="FailureInstance", type=fault_tree_IntermediateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="event16", type=fault_tree_FailureInstance, multiplicity=Multiplicity(0, 9999))
    }
)
inEvent17: BinaryAssociation = BinaryAssociation(
    name="inEvent17",
    ends={
        Property(name="fault_tree_Event", type=fault_tree_IntermediateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="fault_tree_IntermediateEvent18", type=fault_tree_Event, multiplicity=Multiplicity(0, 1))
    }
)
outEvent19: BinaryAssociation = BinaryAssociation(
    name="outEvent19",
    ends={
        Property(name="fault_tree_Event21", type=fault_tree_IntermediateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="fault_tree_IntermediateEvent20", type=fault_tree_Event, multiplicity=Multiplicity(0, 1))
    }
)
instance22: BinaryAssociation = BinaryAssociation(
    name="instance22",
    ends={
        Property(name="FailureInstance23", type=fault_tree_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=fault_tree_FailureInstance, multiplicity=Multiplicity(1, 9999))
    }
)
root24: BinaryAssociation = BinaryAssociation(
    name="root24",
    ends={
        Property(name="FaultTree25", type=fault_tree_FailureType, multiplicity=Multiplicity(1, 1)),
        Property(name="failure_type", type=fault_tree_FaultTree, multiplicity=Multiplicity(0, 1))
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="FailureType", type=fault_tree_FailureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance", type=fault_tree_FailureType, multiplicity=Multiplicity(1, 1))
    }
)
inputEvents3: BinaryAssociation = BinaryAssociation(
    name="inputEvents3",
    ends={
        Property(name="Event", type=fault_tree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="outputGate", type=fault_tree_Event, multiplicity=Multiplicity(0, 9999))
    }
)
outputGate5: BinaryAssociation = BinaryAssociation(
    name="outputGate5",
    ends={
        Property(name="fault_tree_Gate6", type=fault_tree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="fault_tree_Gate4", type=fault_tree_Gate, multiplicity=Multiplicity(0, 1))
    }
)
outputEvent7: BinaryAssociation = BinaryAssociation(
    name="outputEvent7",
    ends={
        Property(name="Event8", type=fault_tree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="inputGate", type=fault_tree_Event, multiplicity=Multiplicity(0, 1))
    }
)
root9: BinaryAssociation = BinaryAssociation(
    name="root9",
    ends={
        Property(name="FaultTree", type=fault_tree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="gate", type=fault_tree_FaultTree, multiplicity=Multiplicity(0, 1))
    }
)
inputGate10: BinaryAssociation = BinaryAssociation(
    name="inputGate10",
    ends={
        Property(name="Gate", type=fault_tree_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="outputEvent", type=fault_tree_Gate, multiplicity=Multiplicity(0, 1))
    }
)
outputGate11: BinaryAssociation = BinaryAssociation(
    name="outputGate11",
    ends={
        Property(name="Gate12", type=fault_tree_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="inputEvents", type=fault_tree_Gate, multiplicity=Multiplicity(0, 1))
    }
)
root13: BinaryAssociation = BinaryAssociation(
    name="root13",
    ends={
        Property(name="FaultTree14", type=fault_tree_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="event", type=fault_tree_FaultTree, multiplicity=Multiplicity(0, 1))
    }
)
root27: BinaryAssociation = BinaryAssociation(
    name="root27",
    ends={
        Property(name="FaultTree28", type=fault_tree_FailureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="failure_instance", type=fault_tree_FaultTree, multiplicity=Multiplicity(0, 1))
    }
)
root41: BinaryAssociation = BinaryAssociation(
    name="root41",
    ends={
        Property(name="FaultTree42", type=fault_tree_ErrorType, multiplicity=Multiplicity(1, 1)),
        Property(name="error_type", type=fault_tree_FaultTree, multiplicity=Multiplicity(0, 1))
    }
)
error43: BinaryAssociation = BinaryAssociation(
    name="error43",
    ends={
        Property(name="BasicEvent", type=fault_tree_ErrorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance44", type=fault_tree_BasicEvent, multiplicity=Multiplicity(0, 1))
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="ErrorType", type=fault_tree_ErrorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="error46", type=fault_tree_ErrorType, multiplicity=Multiplicity(1, 1))
    }
)
root47: BinaryAssociation = BinaryAssociation(
    name="root47",
    ends={
        Property(name="FaultTree48", type=fault_tree_ErrorInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="error_instance", type=fault_tree_FaultTree, multiplicity=Multiplicity(0, 1))
    }
)
previousFailure30: BinaryAssociation = BinaryAssociation(
    name="previousFailure30",
    ends={
        Property(name="fault_tree_FailureInstance", type=fault_tree_FailureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="fault_tree_FailureInstance29", type=fault_tree_FailureInstance, multiplicity=Multiplicity(0, 1))
    }
)
previousError31: BinaryAssociation = BinaryAssociation(
    name="previousError31",
    ends={
        Property(name="fault_tree_ErrorInstance", type=fault_tree_FailureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="fault_tree_FailureInstance32", type=fault_tree_ErrorInstance, multiplicity=Multiplicity(0, 1))
    }
)
event33: BinaryAssociation = BinaryAssociation(
    name="event33",
    ends={
        Property(name="IntermediateEvent", type=fault_tree_FailureInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance34", type=fault_tree_IntermediateEvent, multiplicity=Multiplicity(0, 1))
    }
)
instance35: BinaryAssociation = BinaryAssociation(
    name="instance35",
    ends={
        Property(name="ErrorInstance", type=fault_tree_BasicEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="error", type=fault_tree_ErrorInstance, multiplicity=Multiplicity(0, 9999))
    }
)
outEvent36: BinaryAssociation = BinaryAssociation(
    name="outEvent36",
    ends={
        Property(name="fault_tree_IntermediateEvent37", type=fault_tree_BasicEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="fault_tree_BasicEvent", type=fault_tree_IntermediateEvent, multiplicity=Multiplicity(0, 1))
    }
)
error38: BinaryAssociation = BinaryAssociation(
    name="error38",
    ends={
        Property(name="ErrorInstance40", type=fault_tree_ErrorType, multiplicity=Multiplicity(1, 1)),
        Property(name="type39", type=fault_tree_ErrorInstance, multiplicity=Multiplicity(1, 9999))
    }
)
hazard49: BinaryAssociation = BinaryAssociation(
    name="hazard49",
    ends={
        Property(name="fault_tree_Hazard50", type=fault_tree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="fault_tree_FaultTree", type=fault_tree_Hazard, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
gate51: BinaryAssociation = BinaryAssociation(
    name="gate51",
    ends={
        Property(name="Gate52", type=fault_tree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="root", type=fault_tree_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event53: BinaryAssociation = BinaryAssociation(
    name="event53",
    ends={
        Property(name="Event55", type=fault_tree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="root54", type=fault_tree_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failure_instance56: BinaryAssociation = BinaryAssociation(
    name="failure_instance56",
    ends={
        Property(name="FailureInstance58", type=fault_tree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="root57", type=fault_tree_FailureInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failure_type59: BinaryAssociation = BinaryAssociation(
    name="failure_type59",
    ends={
        Property(name="FailureType61", type=fault_tree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="root60", type=fault_tree_FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
error_instance62: BinaryAssociation = BinaryAssociation(
    name="error_instance62",
    ends={
        Property(name="ErrorInstance64", type=fault_tree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="root63", type=fault_tree_ErrorInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
error_type65: BinaryAssociation = BinaryAssociation(
    name="error_type65",
    ends={
        Property(name="ErrorType67", type=fault_tree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="root66", type=fault_tree_ErrorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_fault_tree_Hazard_Event = Generalization(general=Event, specific=fault_tree_Hazard)
gen_fault_tree_Gate_IDBase = Generalization(general=IDBase, specific=fault_tree_Gate)
gen_fault_tree_FailureType_IDBase = Generalization(general=IDBase, specific=fault_tree_FailureType)
gen_fault_tree_FailureInstance_IDBase = Generalization(general=IDBase, specific=fault_tree_FailureInstance)
gen_fault_tree_Event_IDBase = Generalization(general=IDBase, specific=fault_tree_Event)
gen_fault_tree_IntermediateEvent_Event = Generalization(general=Event, specific=fault_tree_IntermediateEvent)
gen_fault_tree_ErrorInstance_IDBase = Generalization(general=IDBase, specific=fault_tree_ErrorInstance)
gen_fault_tree_OR_Gate = Generalization(general=Gate, specific=fault_tree_OR)
gen_fault_tree_AND_Gate = Generalization(general=Gate, specific=fault_tree_AND)
gen_fault_tree_XOR_Gate = Generalization(general=Gate, specific=fault_tree_XOR)
gen_fault_tree_PriorAND_Gate = Generalization(general=Gate, specific=fault_tree_PriorAND)
gen_fault_tree_Inhibit_Gate = Generalization(general=Gate, specific=fault_tree_Inhibit)
gen_fault_tree_FaultTree_IDBase = Generalization(general=IDBase, specific=fault_tree_FaultTree)
gen_fault_tree_BasicEvent_Event = Generalization(general=Event, specific=fault_tree_BasicEvent)
gen_fault_tree_UndevelopedEvent_Event = Generalization(general=Event, specific=fault_tree_UndevelopedEvent)
gen_fault_tree_ErrorType_IDBase = Generalization(general=IDBase, specific=fault_tree_ErrorType)

# Domain Model
domain_model = DomainModel(
    name="fault_tree",
    types={fault_tree_Hazard, Event, fault_tree_IntermediateEvent, fault_tree_Gate, IDBase, fault_tree_Event, fault_tree_FailureInstance, fault_tree_FailureType, fault_tree_FaultTree, fault_tree_OR, Gate, fault_tree_AND, fault_tree_XOR, fault_tree_PriorAND, fault_tree_Inhibit, fault_tree_ErrorInstance, fault_tree_BasicEvent, fault_tree_UndevelopedEvent, fault_tree_ErrorType},
    associations={inEvent0, inputGates2, instance15, inEvent17, outEvent19, instance22, root24, type26, inputEvents3, outputGate5, outputEvent7, root9, inputGate10, outputGate11, root13, root27, root41, error43, type45, root47, previousFailure30, previousError31, event33, instance35, outEvent36, error38, hazard49, gate51, event53, failure_instance56, failure_type59, error_instance62, error_type65},
    generalizations={gen_fault_tree_Hazard_Event, gen_fault_tree_Gate_IDBase, gen_fault_tree_FailureType_IDBase, gen_fault_tree_FailureInstance_IDBase, gen_fault_tree_Event_IDBase, gen_fault_tree_IntermediateEvent_Event, gen_fault_tree_ErrorInstance_IDBase, gen_fault_tree_OR_Gate, gen_fault_tree_AND_Gate, gen_fault_tree_XOR_Gate, gen_fault_tree_PriorAND_Gate, gen_fault_tree_Inhibit_Gate, gen_fault_tree_FaultTree_IDBase, gen_fault_tree_BasicEvent_Event, gen_fault_tree_UndevelopedEvent_Event, gen_fault_tree_ErrorType_IDBase},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)