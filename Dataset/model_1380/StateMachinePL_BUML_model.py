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
statemachine_FSM = Class(name="statemachine::FSM")
statemachine_State = Class(name="statemachine::State")
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_Initial = Class(name="statemachine::Initial")
State = Class(name="State")
statemachine_Final = Class(name="statemachine::Final")

# statemachine_FSM class attributes and methods

# statemachine_State class attributes and methods
statemachine_State_time: Property = Property(name="time", type=StringType)
statemachine_State.attributes={statemachine_State_time}

# statemachine_Transition class attributes and methods

# statemachine_Initial class attributes and methods

# State class attributes and methods

# statemachine_Final class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_State", type=statemachine_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_FSM", type=statemachine_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="statemachine_Transition", type=statemachine_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_FSM2", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
current3: BinaryAssociation = BinaryAssociation(
    name="current3",
    ends={
        Property(name="statemachine_State5", type=statemachine_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_FSM4", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
src9: BinaryAssociation = BinaryAssociation(
    name="src9",
    ends={
        Property(name="statemachine_State11", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition10", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
tar12: BinaryAssociation = BinaryAssociation(
    name="tar12",
    ends={
        Property(name="statemachine_State14", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition13", type=statemachine_State, multiplicity=Multiplicity(1, 1))
    }
)
nested7: BinaryAssociation = BinaryAssociation(
    name="nested7",
    ends={
        Property(name="statemachine_State8", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State6", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statemachine_Initial_State = Generalization(general=State, specific=statemachine_Initial)
gen_statemachine_Final_State = Generalization(general=State, specific=statemachine_Final)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_FSM, statemachine_State, statemachine_Transition, statemachine_Initial, State, statemachine_Final},
    associations={states0, transitions1, current3, src9, tar12, nested7},
    generalizations={gen_statemachine_Initial_State, gen_statemachine_Final_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)