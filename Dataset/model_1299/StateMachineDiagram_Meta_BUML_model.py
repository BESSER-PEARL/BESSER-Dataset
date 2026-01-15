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
StateMachineDiagram_meta_Vertex = Class(name="StateMachineDiagram::meta::Vertex", is_abstract=True)
StateMachineDiagram_meta_Transition = Class(name="StateMachineDiagram::meta::Transition")
StateMachineDiagram_meta_Application = Class(name="StateMachineDiagram::meta::Application")
StateMachineDiagram_meta_StateMachine = Class(name="StateMachineDiagram::meta::StateMachine")
StateMachineDiagram_meta_Pseudostate = Class(name="StateMachineDiagram::meta::Pseudostate")
Vertex = Class(name="Vertex")
StateMachineDiagram_meta_State = Class(name="StateMachineDiagram::meta::State", is_abstract=True)
StateMachineDiagram_meta_Activity = Class(name="StateMachineDiagram::meta::Activity")
State = Class(name="State")
StateMachineDiagram_meta_Fragment = Class(name="StateMachineDiagram::meta::Fragment")
StateMachineDiagram_meta_Event = Class(name="StateMachineDiagram::meta::Event")

# StateMachineDiagram_meta_Vertex class attributes and methods

# StateMachineDiagram_meta_Transition class attributes and methods
StateMachineDiagram_meta_Transition_name: Property = Property(name="name", type=StringType)
StateMachineDiagram_meta_Transition_trigger: Property = Property(name="trigger", type=StringType)
StateMachineDiagram_meta_Transition.attributes={StateMachineDiagram_meta_Transition_trigger, StateMachineDiagram_meta_Transition_name}

# StateMachineDiagram_meta_Application class attributes and methods
StateMachineDiagram_meta_Application_name: Property = Property(name="name", type=StringType)
StateMachineDiagram_meta_Application.attributes={StateMachineDiagram_meta_Application_name}

# StateMachineDiagram_meta_StateMachine class attributes and methods
StateMachineDiagram_meta_StateMachine_name: Property = Property(name="name", type=StringType)
StateMachineDiagram_meta_StateMachine.attributes={StateMachineDiagram_meta_StateMachine_name}

# StateMachineDiagram_meta_Pseudostate class attributes and methods

# Vertex class attributes and methods

# StateMachineDiagram_meta_State class attributes and methods
StateMachineDiagram_meta_State_name: Property = Property(name="name", type=StringType)
StateMachineDiagram_meta_State.attributes={StateMachineDiagram_meta_State_name}

# StateMachineDiagram_meta_Activity class attributes and methods

# State class attributes and methods

# StateMachineDiagram_meta_Fragment class attributes and methods

# StateMachineDiagram_meta_Event class attributes and methods

# Relationships
vertex1: BinaryAssociation = BinaryAssociation(
    name="vertex1",
    ends={
        Property(name="StateMachineDiagram_meta_Vertex", type=StateMachineDiagram_meta_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineDiagram_meta_StateMachine2", type=StateMachineDiagram_meta_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition3: BinaryAssociation = BinaryAssociation(
    name="transition3",
    ends={
        Property(name="StateMachineDiagram_meta_Transition", type=StateMachineDiagram_meta_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineDiagram_meta_StateMachine4", type=StateMachineDiagram_meta_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition", type=StateMachineDiagram_meta_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="souce", type=StateMachineDiagram_meta_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming6: BinaryAssociation = BinaryAssociation(
    name="incoming6",
    ends={
        Property(name="Transition7", type=StateMachineDiagram_meta_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=StateMachineDiagram_meta_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
statemachine0: BinaryAssociation = BinaryAssociation(
    name="statemachine0",
    ends={
        Property(name="StateMachineDiagram_meta_StateMachine", type=StateMachineDiagram_meta_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineDiagram_meta_Application", type=StateMachineDiagram_meta_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
souce8: BinaryAssociation = BinaryAssociation(
    name="souce8",
    ends={
        Property(name="Vertex", type=StateMachineDiagram_meta_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=StateMachineDiagram_meta_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="Vertex10", type=StateMachineDiagram_meta_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=StateMachineDiagram_meta_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
statemachine11: BinaryAssociation = BinaryAssociation(
    name="statemachine11",
    ends={
        Property(name="StateMachineDiagram_meta_StateMachine12", type=StateMachineDiagram_meta_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachineDiagram_meta_State", type=StateMachineDiagram_meta_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_StateMachineDiagram_meta_Pseudostate_Vertex = Generalization(general=Vertex, specific=StateMachineDiagram_meta_Pseudostate)
gen_StateMachineDiagram_meta_State_Vertex = Generalization(general=Vertex, specific=StateMachineDiagram_meta_State)
gen_StateMachineDiagram_meta_Activity_State = Generalization(general=State, specific=StateMachineDiagram_meta_Activity)
gen_StateMachineDiagram_meta_Fragment_State = Generalization(general=State, specific=StateMachineDiagram_meta_Fragment)
gen_StateMachineDiagram_meta_Event_State = Generalization(general=State, specific=StateMachineDiagram_meta_Event)

# Domain Model
domain_model = DomainModel(
    name="StateMachineDiagram_meta",
    types={StateMachineDiagram_meta_Vertex, StateMachineDiagram_meta_Transition, StateMachineDiagram_meta_Application, StateMachineDiagram_meta_StateMachine, StateMachineDiagram_meta_Pseudostate, Vertex, StateMachineDiagram_meta_State, StateMachineDiagram_meta_Activity, State, StateMachineDiagram_meta_Fragment, StateMachineDiagram_meta_Event},
    associations={vertex1, transition3, outgoing5, incoming6, statemachine0, souce8, target9, statemachine11},
    generalizations={gen_StateMachineDiagram_meta_Pseudostate_Vertex, gen_StateMachineDiagram_meta_State_Vertex, gen_StateMachineDiagram_meta_Activity_State, gen_StateMachineDiagram_meta_Fragment_State, gen_StateMachineDiagram_meta_Event_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)