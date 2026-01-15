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
myFirstEditorCustom_State = Class(name="myFirstEditorCustom::State")
myFirstEditorCustom_Transition = Class(name="myFirstEditorCustom::Transition")
myFirstEditorCustom_StateMachine = Class(name="myFirstEditorCustom::StateMachine")
myFirstEditorCustom_StartState = Class(name="myFirstEditorCustom::StartState")
State = Class(name="State")
myFirstEditorCustom_EndState = Class(name="myFirstEditorCustom::EndState")

# myFirstEditorCustom_State class attributes and methods
myFirstEditorCustom_State_name: Property = Property(name="name", type=StringType)
myFirstEditorCustom_State_type: Property = Property(name="type", type=StringType)
myFirstEditorCustom_State.attributes={myFirstEditorCustom_State_name, myFirstEditorCustom_State_type}

# myFirstEditorCustom_Transition class attributes and methods
myFirstEditorCustom_Transition_name: Property = Property(name="name", type=StringType)
myFirstEditorCustom_Transition.attributes={myFirstEditorCustom_Transition_name}

# myFirstEditorCustom_StateMachine class attributes and methods
myFirstEditorCustom_StateMachine_name: Property = Property(name="name", type=StringType)
myFirstEditorCustom_StateMachine.attributes={myFirstEditorCustom_StateMachine_name}

# myFirstEditorCustom_StartState class attributes and methods

# State class attributes and methods

# myFirstEditorCustom_EndState class attributes and methods

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="myFirstEditorCustom_State", type=myFirstEditorCustom_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="myFirstEditorCustom_StateMachine", type=myFirstEditorCustom_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="myFirstEditorCustom_Transition", type=myFirstEditorCustom_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="myFirstEditorCustom_StateMachine2", type=myFirstEditorCustom_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out3: BinaryAssociation = BinaryAssociation(
    name="out3",
    ends={
        Property(name="Transition", type=myFirstEditorCustom_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=myFirstEditorCustom_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
in4: BinaryAssociation = BinaryAssociation(
    name="in4",
    ends={
        Property(name="Transition5", type=myFirstEditorCustom_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=myFirstEditorCustom_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="State", type=myFirstEditorCustom_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=myFirstEditorCustom_State, multiplicity=Multiplicity(0, 1))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="State8", type=myFirstEditorCustom_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=myFirstEditorCustom_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myFirstEditorCustom_StartState_State = Generalization(general=State, specific=myFirstEditorCustom_StartState)
gen_myFirstEditorCustom_EndState_State = Generalization(general=State, specific=myFirstEditorCustom_EndState)

# Domain Model
domain_model = DomainModel(
    name="myFirstEditorCustom",
    types={myFirstEditorCustom_State, myFirstEditorCustom_Transition, myFirstEditorCustom_StateMachine, myFirstEditorCustom_StartState, State, myFirstEditorCustom_EndState},
    associations={state0, transition1, out3, in4, target6, source7},
    generalizations={gen_myFirstEditorCustom_StartState_State, gen_myFirstEditorCustom_EndState_State},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)