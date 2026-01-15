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
GateType: Enumeration = Enumeration(
    name="GateType",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="PAND"),
			EnumerationLiteral(name="INHIBIT")
    }
)

PrimaryEventType: Enumeration = Enumeration(
    name="PrimaryEventType",
    literals={
            EnumerationLiteral(name="BASIC"),
			EnumerationLiteral(name="UNDEVELOPED"),
			EnumerationLiteral(name="EXTERNAL")
    }
)

# Classes
faultTree_FaultTree = Class(name="faultTree::FaultTree")
faultTree_Gate = Class(name="faultTree::Gate")
faultTree_Event = Class(name="faultTree::Event", is_abstract=True)
faultTree_IntermediateEvent = Class(name="faultTree::IntermediateEvent")
faultTree_PrimaryEvent = Class(name="faultTree::PrimaryEvent")
faultTree_ConditioningEvent = Class(name="faultTree::ConditioningEvent")
faultTree_TransferOut = Class(name="faultTree::TransferOut")
faultTree_TransferIn = Class(name="faultTree::TransferIn")
faultTree_Transfer = Class(name="faultTree::Transfer", is_abstract=True)
Event = Class(name="Event")
Transfer = Class(name="Transfer")

# faultTree_FaultTree class attributes and methods
faultTree_FaultTree_name: Property = Property(name="name", type=StringType)
faultTree_FaultTree.attributes={faultTree_FaultTree_name}

# faultTree_Gate class attributes and methods
faultTree_Gate_type: Property = Property(name="type", type=StringType)
faultTree_Gate_probability: Property = Property(name="probability", type=FloatType)
faultTree_Gate_name: Property = Property(name="name", type=StringType)
faultTree_Gate.attributes={faultTree_Gate_probability, faultTree_Gate_type, faultTree_Gate_name}

# faultTree_Event class attributes and methods
faultTree_Event_name: Property = Property(name="name", type=StringType)
faultTree_Event_description: Property = Property(name="description", type=StringType)
faultTree_Event.attributes={faultTree_Event_description, faultTree_Event_name}

# faultTree_IntermediateEvent class attributes and methods
faultTree_IntermediateEvent_probability: Property = Property(name="probability", type=FloatType)
faultTree_IntermediateEvent.attributes={faultTree_IntermediateEvent_probability}

# faultTree_PrimaryEvent class attributes and methods
faultTree_PrimaryEvent_type: Property = Property(name="type", type=StringType)
faultTree_PrimaryEvent_probability: Property = Property(name="probability", type=FloatType)
faultTree_PrimaryEvent.attributes={faultTree_PrimaryEvent_probability, faultTree_PrimaryEvent_type}

# faultTree_ConditioningEvent class attributes and methods
faultTree_ConditioningEvent_condition: Property = Property(name="condition", type=StringType)
faultTree_ConditioningEvent.attributes={faultTree_ConditioningEvent_condition}

# faultTree_TransferOut class attributes and methods

# faultTree_TransferIn class attributes and methods

# faultTree_Transfer class attributes and methods
faultTree_Transfer_name: Property = Property(name="name", type=StringType)
faultTree_Transfer.attributes={faultTree_Transfer_name}

# Event class attributes and methods

# Transfer class attributes and methods

# Relationships
gates0: BinaryAssociation = BinaryAssociation(
    name="gates0",
    ends={
        Property(name="Gate", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree", type=faultTree_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topGates18: BinaryAssociation = BinaryAssociation(
    name="topGates18",
    ends={
        Property(name="Gate19", type=faultTree_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="inputs", type=faultTree_Gate, multiplicity=Multiplicity(0, 9999))
    }
)
faultTree20: BinaryAssociation = BinaryAssociation(
    name="faultTree20",
    ends={
        Property(name="faultTree_FaultTree22", type=faultTree_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree_Event21", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1))
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="faultTree_Event", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree_FaultTree", type=faultTree_Event, multiplicity=Multiplicity(0, 9999))
    }
)
intermediateEvents2: BinaryAssociation = BinaryAssociation(
    name="intermediateEvents2",
    ends={
        Property(name="faultTree_IntermediateEvent", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree_FaultTree3", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryEvents4: BinaryAssociation = BinaryAssociation(
    name="primaryEvents4",
    ends={
        Property(name="faultTree_PrimaryEvent", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree_FaultTree5", type=faultTree_PrimaryEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditioningEvents6: BinaryAssociation = BinaryAssociation(
    name="conditioningEvents6",
    ends={
        Property(name="faultTree_ConditioningEvent", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree_FaultTree7", type=faultTree_ConditioningEvent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transferOut8: BinaryAssociation = BinaryAssociation(
    name="transferOut8",
    ends={
        Property(name="TransferOut", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree9", type=faultTree_TransferOut, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transferIns10: BinaryAssociation = BinaryAssociation(
    name="transferIns10",
    ends={
        Property(name="TransferIn", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree11", type=faultTree_TransferIn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topEvent12: BinaryAssociation = BinaryAssociation(
    name="topEvent12",
    ends={
        Property(name="faultTree_IntermediateEvent14", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree_FaultTree13", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(0, 1))
    }
)
inputs15: BinaryAssociation = BinaryAssociation(
    name="inputs15",
    ends={
        Property(name="Event", type=faultTree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="topGates", type=faultTree_Event, multiplicity=Multiplicity(0, 9999))
    }
)
output16: BinaryAssociation = BinaryAssociation(
    name="output16",
    ends={
        Property(name="IntermediateEvent", type=faultTree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomGate", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(0, 1))
    }
)
faultTree17: BinaryAssociation = BinaryAssociation(
    name="faultTree17",
    ends={
        Property(name="FaultTree", type=faultTree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="gates", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1))
    }
)
faultTree38: BinaryAssociation = BinaryAssociation(
    name="faultTree38",
    ends={
        Property(name="FaultTree39", type=faultTree_TransferIn, multiplicity=Multiplicity(1, 1)),
        Property(name="transferIns", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1))
    }
)
event40: BinaryAssociation = BinaryAssociation(
    name="event40",
    ends={
        Property(name="IntermediateEvent41", type=faultTree_TransferOut, multiplicity=Multiplicity(1, 1)),
        Property(name="transferOut", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(0, 1))
    }
)
faultTree42: BinaryAssociation = BinaryAssociation(
    name="faultTree42",
    ends={
        Property(name="FaultTree44", type=faultTree_TransferOut, multiplicity=Multiplicity(1, 1)),
        Property(name="transferOut43", type=faultTree_FaultTree, multiplicity=Multiplicity(1, 1))
    }
)
bottomGate23: BinaryAssociation = BinaryAssociation(
    name="bottomGate23",
    ends={
        Property(name="Gate24", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="output", type=faultTree_Gate, multiplicity=Multiplicity(0, 1))
    }
)
topEvent26: BinaryAssociation = BinaryAssociation(
    name="topEvent26",
    ends={
        Property(name="IntermediateEvent27", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomEvent", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(0, 1))
    }
)
bottomEvent29: BinaryAssociation = BinaryAssociation(
    name="bottomEvent29",
    ends={
        Property(name="IntermediateEvent30", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="topEvent", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(0, 1))
    }
)
transferIn31: BinaryAssociation = BinaryAssociation(
    name="transferIn31",
    ends={
        Property(name="TransferIn32", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="event", type=faultTree_TransferIn, multiplicity=Multiplicity(0, 1))
    }
)
transferOut33: BinaryAssociation = BinaryAssociation(
    name="transferOut33",
    ends={
        Property(name="TransferOut35", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="event34", type=faultTree_TransferOut, multiplicity=Multiplicity(0, 1))
    }
)
event36: BinaryAssociation = BinaryAssociation(
    name="event36",
    ends={
        Property(name="IntermediateEvent37", type=faultTree_TransferIn, multiplicity=Multiplicity(1, 1)),
        Property(name="transferIn", type=faultTree_IntermediateEvent, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_faultTree_TransferOut_Transfer = Generalization(general=Transfer, specific=faultTree_TransferOut)
gen_faultTree_IntermediateEvent_Event = Generalization(general=Event, specific=faultTree_IntermediateEvent)
gen_faultTree_PrimaryEvent_Event = Generalization(general=Event, specific=faultTree_PrimaryEvent)
gen_faultTree_ConditioningEvent_Event = Generalization(general=Event, specific=faultTree_ConditioningEvent)
gen_faultTree_TransferIn_Transfer = Generalization(general=Transfer, specific=faultTree_TransferIn)

# Domain Model
domain_model = DomainModel(
    name="faultTree",
    types={faultTree_FaultTree, faultTree_Gate, faultTree_Event, faultTree_IntermediateEvent, faultTree_PrimaryEvent, faultTree_ConditioningEvent, faultTree_TransferOut, faultTree_TransferIn, faultTree_Transfer, Event, Transfer, GateType, PrimaryEventType},
    associations={gates0, topGates18, faultTree20, events1, intermediateEvents2, primaryEvents4, conditioningEvents6, transferOut8, transferIns10, topEvent12, inputs15, output16, faultTree17, faultTree38, event40, faultTree42, bottomGate23, topEvent26, bottomEvent29, transferIn31, transferOut33, event36},
    generalizations={gen_faultTree_TransferOut_Transfer, gen_faultTree_IntermediateEvent_Event, gen_faultTree_PrimaryEvent_Event, gen_faultTree_ConditioningEvent_Event, gen_faultTree_TransferIn_Transfer},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)