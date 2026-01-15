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
ecore_FSM = Class(name="ecore::FSM")
ecore_State = Class(name="ecore::State")
EClass = Class(name="EClass")
ecore_EClass = Class(name="ecore::EClass")
FSM = Class(name="FSM")
ecore_ENamedElement = Class(name="ecore::ENamedElement")
ecore_Transition = Class(name="ecore::Transition")

# ecore_FSM class attributes and methods

# ecore_State class attributes and methods
ecore_State_name: Property = Property(name="name", type=StringType)
ecore_State.attributes={ecore_State_name}

# EClass class attributes and methods

# ecore_EClass class attributes and methods

# FSM class attributes and methods

# ecore_ENamedElement class attributes and methods

# ecore_Transition class attributes and methods
ecore_Transition_input: Property = Property(name="input", type=StringType)
ecore_Transition_output: Property = Property(name="output", type=StringType)
ecore_Transition.attributes={ecore_Transition_input, ecore_Transition_output}

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="State", type=ecore_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="owningFSM", type=ecore_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="ecore_State", type=ecore_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_FSM", type=ecore_State, multiplicity=Multiplicity(1, 1))
    }
)
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="ecore_State4", type=ecore_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_FSM3", type=ecore_State, multiplicity=Multiplicity(1, 9999))
    }
)
incomingTransition7: BinaryAssociation = BinaryAssociation(
    name="incomingTransition7",
    ends={
        Property(name="target", type=ecore_Transition, multiplicity=Multiplicity(0, 9999)),
        Property(name="Transition8", type=ecore_State, multiplicity=Multiplicity(1, 1))
    }
)
myClasses9: BinaryAssociation = BinaryAssociation(
    name="myClasses9",
    ends={
        Property(name="ecore_EClass", type=ecore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_State10", type=ecore_EClass, multiplicity=Multiplicity(0, 9999))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="State12", type=ecore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=ecore_State, multiplicity=Multiplicity(1, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="State14", type=ecore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=ecore_State, multiplicity=Multiplicity(1, 1))
    }
)
myFSMs15: BinaryAssociation = BinaryAssociation(
    name="myFSMs15",
    ends={
        Property(name="ecore_FSM16", type=ecore_ENamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ecore_ENamedElement", type=ecore_FSM, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
owningFSM5: BinaryAssociation = BinaryAssociation(
    name="owningFSM5",
    ends={
        Property(name="FSM", type=ecore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=ecore_FSM, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition6",
    ends={
        Property(name="Transition", type=ecore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ecore_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_ecore_State_EClass = Generalization(general=EClass, specific=ecore_State)
gen_ecore_EClass_FSM = Generalization(general=FSM, specific=ecore_EClass)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={ecore_FSM, ecore_State, EClass, ecore_EClass, FSM, ecore_ENamedElement, ecore_Transition},
    associations={ownedState0, initialState1, finalState2, incomingTransition7, myClasses9, source11, target13, myFSMs15, owningFSM5, outgoingTransition6},
    generalizations={gen_ecore_State_EClass, gen_ecore_EClass_FSM},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)