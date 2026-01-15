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
tP1_IDM_State = Class(name="tP1::IDM::State")
tP1_IDM_Transition = Class(name="tP1::IDM::Transition")
tP1_IDM_StateMachine = Class(name="tP1::IDM::StateMachine")

# tP1_IDM_State class attributes and methods
tP1_IDM_State_name: Property = Property(name="name", type=StringType)
tP1_IDM_State.attributes={tP1_IDM_State_name}

# tP1_IDM_Transition class attributes and methods
tP1_IDM_Transition_name: Property = Property(name="name", type=StringType)
tP1_IDM_Transition.attributes={tP1_IDM_Transition_name}

# tP1_IDM_StateMachine class attributes and methods
tP1_IDM_StateMachine_name: Property = Property(name="name", type=StringType)
tP1_IDM_StateMachine_m_execute: Method = Method(name="execute", parameters={})
tP1_IDM_StateMachine.attributes={tP1_IDM_StateMachine_name}
tP1_IDM_StateMachine.methods={tP1_IDM_StateMachine_m_execute}

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="tP1_IDM_State", type=tP1_IDM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tP1_IDM_StateMachine", type=tP1_IDM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="tP1_IDM_Transition", type=tP1_IDM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tP1_IDM_StateMachine2", type=tP1_IDM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomming6: BinaryAssociation = BinaryAssociation(
    name="incomming6",
    ends={
        Property(name="Transition", type=tP1_IDM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=tP1_IDM_Transition, multiplicity=Multiplicity(0, 1))
    }
)
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="Transition8", type=tP1_IDM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=tP1_IDM_Transition, multiplicity=Multiplicity(0, 1))
    }
)
stateStart3: BinaryAssociation = BinaryAssociation(
    name="stateStart3",
    ends={
        Property(name="tP1_IDM_State5", type=tP1_IDM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="tP1_IDM_StateMachine4", type=tP1_IDM_State, multiplicity=Multiplicity(0, 1))
    }
)
to9: BinaryAssociation = BinaryAssociation(
    name="to9",
    ends={
        Property(name="State", type=tP1_IDM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomming", type=tP1_IDM_State, multiplicity=Multiplicity(0, 1))
    }
)
from10: BinaryAssociation = BinaryAssociation(
    name="from10",
    ends={
        Property(name="State11", type=tP1_IDM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=tP1_IDM_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="tP1_IDM",
    types={tP1_IDM_State, tP1_IDM_Transition, tP1_IDM_StateMachine},
    associations={state0, transition1, incomming6, outgoing7, stateStart3, to9, from10},
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