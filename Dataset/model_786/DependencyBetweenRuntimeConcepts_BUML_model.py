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
fsm_FSM = Class(name="fsm_FSM")
fsm_State = Class(name="fsm_State")
fsm_RuntimeConcept1 = Class(name="fsm_RuntimeConcept1")
fsm_Transition = Class(name="fsm_Transition")
fsm_RuntimeConcept2 = Class(name="fsm_RuntimeConcept2")

# fsm_FSM class attributes and methods

# fsm_State class attributes and methods
fsm_State_name: Property = Property(name="name", type=StringType)
fsm_State.attributes={fsm_State_name}

# fsm_RuntimeConcept1 class attributes and methods
fsm_RuntimeConcept1_foo: Property = Property(name="foo", type=IntegerType)
fsm_RuntimeConcept1.attributes={fsm_RuntimeConcept1_foo}

# fsm_Transition class attributes and methods
fsm_Transition_input: Property = Property(name="input", type=StringType)
fsm_Transition_output: Property = Property(name="output", type=StringType)
fsm_Transition.attributes={fsm_Transition_input, fsm_Transition_output}

# fsm_RuntimeConcept2 class attributes and methods
fsm_RuntimeConcept2_bar: Property = Property(name="bar", type=StringType)
fsm_RuntimeConcept2.attributes={fsm_RuntimeConcept2_bar}

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="fsm_State", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="fsm_State4", type=fsm_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_FSM3", type=fsm_State, multiplicity=Multiplicity(1, 9999))
    }
)
myFoos5: BinaryAssociation = BinaryAssociation(
    name="myFoos5",
    ends={
        Property(name="fsm_RuntimeConcept1", type=fsm_RuntimeConcept2, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RuntimeConcept2", type=fsm_RuntimeConcept1, multiplicity=Multiplicity(0, 9999))
    }
)
owningFSM6: BinaryAssociation = BinaryAssociation(
    name="owningFSM6",
    ends={
        Property(name="FSM", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=fsm_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition7: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition7",
    ends={
        Property(name="Transition", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsm_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransition8: BinaryAssociation = BinaryAssociation(
    name="incomingTransition8",
    ends={
        Property(name="Transition9", type=fsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsm_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="State11", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="State13", type=fsm_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=fsm_State, multiplicity=Multiplicity(1, 1))
    }
)
myState14: BinaryAssociation = BinaryAssociation(
    name="myState14",
    ends={
        Property(name="fsm_State16", type=fsm_RuntimeConcept1, multiplicity=Multiplicity(1, 1)),
        Property(name="fsm_RuntimeConcept115", type=fsm_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_FSM, fsm_State, fsm_RuntimeConcept1, fsm_Transition, fsm_RuntimeConcept2},
    associations={ownedState0, initialState1, finalState2, myFoos5, owningFSM6, outgoingTransition7, incomingTransition8, source10, target12, myState14},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)