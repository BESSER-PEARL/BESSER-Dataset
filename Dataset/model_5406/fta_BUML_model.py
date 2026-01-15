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
faultTree_FTElement = Class(name="faultTree::FTElement", is_abstract=True)
faultTree_Connector = Class(name="faultTree::Connector")
FTElement = Class(name="FTElement")
faultTree_FaultTree = Class(name="faultTree::FaultTree")
faultTree_Event = Class(name="faultTree::Event")
faultTree_IntermediateEvent = Class(name="faultTree::IntermediateEvent")
faultTree_Gate = Class(name="faultTree::Gate", is_abstract=True)
faultTree_AND_Gate = Class(name="faultTree::AND::Gate")
Gate = Class(name="Gate")
faultTree_OR_Gate = Class(name="faultTree::OR::Gate")
faultTree_ProbabalisticEvent = Class(name="faultTree::ProbabalisticEvent", is_abstract=True)
Event = Class(name="Event")
faultTree_BasicEvent = Class(name="faultTree::BasicEvent")
ProbabalisticEvent = Class(name="ProbabalisticEvent")
faultTree_UndevelopedEvent = Class(name="faultTree::UndevelopedEvent")
faultTree_ExternalEvent = Class(name="faultTree::ExternalEvent")

# faultTree_FTElement class attributes and methods

# faultTree_Connector class attributes and methods

# FTElement class attributes and methods

# faultTree_FaultTree class attributes and methods

# faultTree_Event class attributes and methods
faultTree_Event_title: Property = Property(name="title", type=StringType)
faultTree_Event_description: Property = Property(name="description", type=StringType)
faultTree_Event.attributes={faultTree_Event_title, faultTree_Event_description}

# faultTree_IntermediateEvent class attributes and methods

# faultTree_Gate class attributes and methods

# faultTree_AND_Gate class attributes and methods

# Gate class attributes and methods

# faultTree_OR_Gate class attributes and methods

# faultTree_ProbabalisticEvent class attributes and methods
faultTree_ProbabalisticEvent_probability: Property = Property(name="probability", type=FloatType)
faultTree_ProbabalisticEvent.attributes={faultTree_ProbabalisticEvent_probability}

# Event class attributes and methods

# faultTree_BasicEvent class attributes and methods

# ProbabalisticEvent class attributes and methods

# faultTree_UndevelopedEvent class attributes and methods

# faultTree_ExternalEvent class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="faultTree_FTElement", type=faultTree_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree_Connector", type=faultTree_FTElement, multiplicity=Multiplicity(0, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="faultTree_FTElement3", type=faultTree_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="faultTree_Connector2", type=faultTree_FTElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_faultTree_Connector_FTElement = Generalization(general=FTElement, specific=faultTree_Connector)
gen_faultTree_FaultTree_FTElement = Generalization(general=FTElement, specific=faultTree_FaultTree)
gen_faultTree_Event_FTElement = Generalization(general=FTElement, specific=faultTree_Event)
gen_faultTree_IntermediateEvent_Event = Generalization(general=Event, specific=faultTree_IntermediateEvent)
gen_faultTree_Gate_FTElement = Generalization(general=FTElement, specific=faultTree_Gate)
gen_faultTree_AND_Gate_Gate = Generalization(general=Gate, specific=faultTree_AND_Gate)
gen_faultTree_OR_Gate_Gate = Generalization(general=Gate, specific=faultTree_OR_Gate)
gen_faultTree_ProbabalisticEvent_Event = Generalization(general=Event, specific=faultTree_ProbabalisticEvent)
gen_faultTree_BasicEvent_ProbabalisticEvent = Generalization(general=ProbabalisticEvent, specific=faultTree_BasicEvent)
gen_faultTree_UndevelopedEvent_ProbabalisticEvent = Generalization(general=ProbabalisticEvent, specific=faultTree_UndevelopedEvent)
gen_faultTree_ExternalEvent_ProbabalisticEvent = Generalization(general=ProbabalisticEvent, specific=faultTree_ExternalEvent)

# Domain Model
domain_model = DomainModel(
    name="faultTree",
    types={faultTree_FTElement, faultTree_Connector, FTElement, faultTree_FaultTree, faultTree_Event, faultTree_IntermediateEvent, faultTree_Gate, faultTree_AND_Gate, Gate, faultTree_OR_Gate, faultTree_ProbabalisticEvent, Event, faultTree_BasicEvent, ProbabalisticEvent, faultTree_UndevelopedEvent, faultTree_ExternalEvent},
    associations={source0, target1},
    generalizations={gen_faultTree_Connector_FTElement, gen_faultTree_FaultTree_FTElement, gen_faultTree_Event_FTElement, gen_faultTree_IntermediateEvent_Event, gen_faultTree_Gate_FTElement, gen_faultTree_AND_Gate_Gate, gen_faultTree_OR_Gate_Gate, gen_faultTree_ProbabalisticEvent_Event, gen_faultTree_BasicEvent_ProbabalisticEvent, gen_faultTree_UndevelopedEvent_ProbabalisticEvent, gen_faultTree_ExternalEvent_ProbabalisticEvent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)