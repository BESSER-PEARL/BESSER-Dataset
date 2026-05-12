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
FSM_MgaObject = Class(name="FSM_MgaObject")
FSM_Transition = Class(name="FSM_Transition")
MgaObject = Class(name="MgaObject")
StateMachine = Class(name="StateMachine")
AssociationStateState = Class(name="AssociationStateState")
FSM_State = Class(name="FSM_State")
FSM_StateMachine = Class(name="FSM_StateMachine")
RootFolder = Class(name="RootFolder")
State = Class(name="State")
Transition = Class(name="Transition")
FSM_RootFolder = Class(name="FSM_RootFolder")
FSM_AssociationStateState = Class(name="FSM_AssociationStateState")

# FSM_MgaObject class attributes and methods
FSM_MgaObject_name: Property = Property(name="name", type=StringType)
FSM_MgaObject_position: Property = Property(name="position", type=StringType)
FSM_MgaObject.attributes={FSM_MgaObject_position, FSM_MgaObject_name}

# FSM_Transition class attributes and methods

# MgaObject class attributes and methods

# StateMachine class attributes and methods

# AssociationStateState class attributes and methods

# FSM_State class attributes and methods

# FSM_StateMachine class attributes and methods

# RootFolder class attributes and methods

# State class attributes and methods

# Transition class attributes and methods

# FSM_RootFolder class attributes and methods
FSM_RootFolder_name: Property = Property(name="name", type=StringType)
FSM_RootFolder.attributes={FSM_RootFolder_name}

# FSM_AssociationStateState class attributes and methods

# Relationships
stateMachine0: BinaryAssociation = BinaryAssociation(
    name="stateMachine0",
    ends={
        Property(name="StateMachine", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
associationStateState1: BinaryAssociation = BinaryAssociation(
    name="associationStateState1",
    ends={
        Property(name="AssociationStateState", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition2", type=AssociationStateState, multiplicity=Multiplicity(1, 1))
    }
)
stateMachine3: BinaryAssociation = BinaryAssociation(
    name="stateMachine3",
    ends={
        Property(name="StateMachine4", type=FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
associationStateStatedst5: BinaryAssociation = BinaryAssociation(
    name="associationStateStatedst5",
    ends={
        Property(name="AssociationStateState6", type=FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dstTransition", type=AssociationStateState, multiplicity=Multiplicity(1, 9999))
    }
)
associationStateStatesrc7: BinaryAssociation = BinaryAssociation(
    name="associationStateStatesrc7",
    ends={
        Property(name="AssociationStateState8", type=FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="srcTransition", type=AssociationStateState, multiplicity=Multiplicity(1, 9999))
    }
)
rootFolder9: BinaryAssociation = BinaryAssociation(
    name="rootFolder9",
    ends={
        Property(name="RootFolder", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=RootFolder, multiplicity=Multiplicity(1, 1))
    }
)
state10: BinaryAssociation = BinaryAssociation(
    name="state10",
    ends={
        Property(name="State", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine11", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition12: BinaryAssociation = BinaryAssociation(
    name="transition12",
    ends={
        Property(name="Transition", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine13", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootFolders14: BinaryAssociation = BinaryAssociation(
    name="rootFolders14",
    ends={
        Property(name="RootFolder15", type=FSM_RootFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_RootFolder", type=RootFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine16: BinaryAssociation = BinaryAssociation(
    name="stateMachine16",
    ends={
        Property(name="StateMachine17", type=FSM_RootFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="rootFolder", type=StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition18: BinaryAssociation = BinaryAssociation(
    name="transition18",
    ends={
        Property(name="Transition19", type=FSM_AssociationStateState, multiplicity=Multiplicity(1, 1)),
        Property(name="associationStateState", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
dstTransition20: BinaryAssociation = BinaryAssociation(
    name="dstTransition20",
    ends={
        Property(name="State21", type=FSM_AssociationStateState, multiplicity=Multiplicity(1, 1)),
        Property(name="associationStateStatedst", type=State, multiplicity=Multiplicity(1, 9999))
    }
)
srcTransition22: BinaryAssociation = BinaryAssociation(
    name="srcTransition22",
    ends={
        Property(name="State23", type=FSM_AssociationStateState, multiplicity=Multiplicity(1, 1)),
        Property(name="associationStateStatesrc", type=State, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_FSM_Transition_MgaObject = Generalization(general=MgaObject, specific=FSM_Transition)
gen_FSM_State_MgaObject = Generalization(general=MgaObject, specific=FSM_State)
gen_FSM_StateMachine_MgaObject = Generalization(general=MgaObject, specific=FSM_StateMachine)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={FSM_MgaObject, FSM_Transition, MgaObject, StateMachine, AssociationStateState, FSM_State, FSM_StateMachine, RootFolder, State, Transition, FSM_RootFolder, FSM_AssociationStateState},
    associations={stateMachine0, associationStateState1, stateMachine3, associationStateStatedst5, associationStateStatesrc7, rootFolder9, state10, transition12, rootFolders14, stateMachine16, transition18, dstTransition20, srcTransition22},
    generalizations={gen_FSM_Transition_MgaObject, gen_FSM_State_MgaObject, gen_FSM_StateMachine_MgaObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)