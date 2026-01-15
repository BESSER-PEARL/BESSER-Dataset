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
StateMachineDiagram_Meta_Application = Class(name="StateMachineDiagram::Meta::Application")
StateMachineDiagram_Meta_Pseudostate = Class(name="StateMachineDiagram::Meta::Pseudostate")
Vertex = Class(name="Vertex")
StateMachineDiagram_Meta_State = Class(name="StateMachineDiagram::Meta::State", is_abstract=True)
StateMachineDiagram_Meta_StateMachine = Class(name="StateMachineDiagram::Meta::StateMachine")
StateMachineDiagram_Meta_Vertex = Class(name="StateMachineDiagram::Meta::Vertex", is_abstract=True)
StateMachineDiagram_Meta_Transition = Class(name="StateMachineDiagram::Meta::Transition")
StateMachineDiagram_Meta_ViewController = Class(name="StateMachineDiagram::Meta::ViewController")
State = Class(name="State")
StateMachineDiagram_Meta_Event = Class(name="StateMachineDiagram::Meta::Event")

# StateMachineDiagram_Meta_Application class attributes and methods
StateMachineDiagram_Meta_Application_name: Property = Property(name="name", type=StringType)
StateMachineDiagram_Meta_Application.attributes={StateMachineDiagram_Meta_Application_name}

# StateMachineDiagram_Meta_Pseudostate class attributes and methods

# Vertex class attributes and methods

# StateMachineDiagram_Meta_State class attributes and methods
StateMachineDiagram_Meta_State_name: Property = Property(name="name", type=StringType)
StateMachineDiagram_Meta_State.attributes={StateMachineDiagram_Meta_State_name}

# StateMachineDiagram_Meta_StateMachine class attributes and methods
StateMachineDiagram_Meta_StateMachine_name: Property = Property(name="name", type=StringType)
StateMachineDiagram_Meta_StateMachine.attributes={StateMachineDiagram_Meta_StateMachine_name}

# StateMachineDiagram_Meta_Vertex class attributes and methods

# StateMachineDiagram_Meta_Transition class attributes and methods
StateMachineDiagram_Meta_Transition_name: Property = Property(name="name", type=StringType)
StateMachineDiagram_Meta_Transition_trigger: Property = Property(name="trigger", type=StringType)
StateMachineDiagram_Meta_Transition.attributes={StateMachineDiagram_Meta_Transition_trigger, StateMachineDiagram_Meta_Transition_name}

# StateMachineDiagram_Meta_ViewController class attributes and methods

# State class attributes and methods

# StateMachineDiagram_Meta_Event class attributes and methods

# Relationships
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="Vertex", type=StateMachineDiagram_Meta_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=StateMachineDiagram_Meta_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="Vertex10", type=StateMachineDiagram_Meta_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=StateMachineDiagram_Meta_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
statemachine11: BinaryAssociation = BinaryAssociation(
    name="statemachine11",
    ends={
        Property(name="StateMachineDiagram_Meta_StateMachine12", type=StateMachineDiagram_Meta_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineDiagram_Meta_State", type=StateMachineDiagram_Meta_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statemachine0: BinaryAssociation = BinaryAssociation(
    name="statemachine0",
    ends={
        Property(name="StateMachineDiagram_Meta_StateMachine", type=StateMachineDiagram_Meta_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineDiagram_Meta_Application", type=StateMachineDiagram_Meta_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertex1: BinaryAssociation = BinaryAssociation(
    name="vertex1",
    ends={
        Property(name="StateMachineDiagram_Meta_Vertex", type=StateMachineDiagram_Meta_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineDiagram_Meta_StateMachine2", type=StateMachineDiagram_Meta_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition3: BinaryAssociation = BinaryAssociation(
    name="transition3",
    ends={
        Property(name="StateMachineDiagram_Meta_Transition", type=StateMachineDiagram_Meta_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineDiagram_Meta_StateMachine4", type=StateMachineDiagram_Meta_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition", type=StateMachineDiagram_Meta_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=StateMachineDiagram_Meta_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition7", type=StateMachineDiagram_Meta_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=StateMachineDiagram_Meta_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_StateMachineDiagram_Meta_Pseudostate_Vertex = Generalization(general=Vertex, specific=StateMachineDiagram_Meta_Pseudostate)
gen_StateMachineDiagram_Meta_State_Vertex = Generalization(general=Vertex, specific=StateMachineDiagram_Meta_State)
gen_StateMachineDiagram_Meta_ViewController_State = Generalization(general=State, specific=StateMachineDiagram_Meta_ViewController)
gen_StateMachineDiagram_Meta_Event_State = Generalization(general=State, specific=StateMachineDiagram_Meta_Event)

# Domain Model
domain_model = DomainModel(
    name="StateMachineDiagram_Meta",
    types={StateMachineDiagram_Meta_Application, StateMachineDiagram_Meta_Pseudostate, Vertex, StateMachineDiagram_Meta_State, StateMachineDiagram_Meta_StateMachine, StateMachineDiagram_Meta_Vertex, StateMachineDiagram_Meta_Transition, StateMachineDiagram_Meta_ViewController, State, StateMachineDiagram_Meta_Event},
    associations={source8, target9, statemachine11, statemachine0, vertex1, transition3, outgoing5, incoming6},
    generalizations={gen_StateMachineDiagram_Meta_Pseudostate_Vertex, gen_StateMachineDiagram_Meta_State_Vertex, gen_StateMachineDiagram_Meta_ViewController_State, gen_StateMachineDiagram_Meta_Event_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)