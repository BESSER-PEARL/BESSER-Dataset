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
FSM_MgaObject = Class(name="FSM::MgaObject")
FSM_Transition = Class(name="FSM::Transition")
MgaObject = Class(name="MgaObject")
FSM_StateMachine = Class(name="FSM::StateMachine")
FSM_AssociationStateState = Class(name="FSM::AssociationStateState")
FSM_State = Class(name="FSM::State")
FSM_RootFolder = Class(name="FSM::RootFolder")

# FSM_MgaObject class attributes and methods
FSM_MgaObject_name: Property = Property(name="name", type=StringType)
FSM_MgaObject_position: Property = Property(name="position", type=StringType)
FSM_MgaObject.attributes={FSM_MgaObject_position, FSM_MgaObject_name}

# FSM_Transition class attributes and methods

# MgaObject class attributes and methods

# FSM_StateMachine class attributes and methods

# FSM_AssociationStateState class attributes and methods

# FSM_State class attributes and methods

# FSM_RootFolder class attributes and methods
FSM_RootFolder_name: Property = Property(name="name", type=StringType)
FSM_RootFolder.attributes={FSM_RootFolder_name}

# Relationships
stateMachine0: BinaryAssociation = BinaryAssociation(
    name="stateMachine0",
    ends={
        Property(name="StateMachine", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
associationStateState1: BinaryAssociation = BinaryAssociation(
    name="associationStateState1",
    ends={
        Property(name="AssociationStateState", type=FSM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition2", type=FSM_AssociationStateState, multiplicity=Multiplicity(1, 1))
    }
)
stateMachine3: BinaryAssociation = BinaryAssociation(
    name="stateMachine3",
    ends={
        Property(name="StateMachine4", type=FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
associationStateStatedst5: BinaryAssociation = BinaryAssociation(
    name="associationStateStatedst5",
    ends={
        Property(name="AssociationStateState6", type=FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dstTransition", type=FSM_AssociationStateState, multiplicity=Multiplicity(1, 9999))
    }
)
associationStateStatesrc7: BinaryAssociation = BinaryAssociation(
    name="associationStateStatesrc7",
    ends={
        Property(name="AssociationStateState8", type=FSM_State, multiplicity=Multiplicity(1, 1)),
        Property(name="srcTransition", type=FSM_AssociationStateState, multiplicity=Multiplicity(1, 9999))
    }
)
rootFolder9: BinaryAssociation = BinaryAssociation(
    name="rootFolder9",
    ends={
        Property(name="RootFolder", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=FSM_RootFolder, multiplicity=Multiplicity(1, 1))
    }
)
state10: BinaryAssociation = BinaryAssociation(
    name="state10",
    ends={
        Property(name="State", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine11", type=FSM_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition12: BinaryAssociation = BinaryAssociation(
    name="transition12",
    ends={
        Property(name="Transition", type=FSM_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine13", type=FSM_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootFolders15: BinaryAssociation = BinaryAssociation(
    name="rootFolders15",
    ends={
        Property(name="FSM_RootFolder", type=FSM_RootFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="FSM_RootFolder14", type=FSM_RootFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine16: BinaryAssociation = BinaryAssociation(
    name="stateMachine16",
    ends={
        Property(name="StateMachine17", type=FSM_RootFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="rootFolder", type=FSM_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition18: BinaryAssociation = BinaryAssociation(
    name="transition18",
    ends={
        Property(name="Transition19", type=FSM_AssociationStateState, multiplicity=Multiplicity(1, 1)),
        Property(name="associationStateState", type=FSM_Transition, multiplicity=Multiplicity(1, 1))
    }
)
dstTransition20: BinaryAssociation = BinaryAssociation(
    name="dstTransition20",
    ends={
        Property(name="State21", type=FSM_AssociationStateState, multiplicity=Multiplicity(1, 1)),
        Property(name="associationStateStatedst", type=FSM_State, multiplicity=Multiplicity(1, 9999))
    }
)
srcTransition22: BinaryAssociation = BinaryAssociation(
    name="srcTransition22",
    ends={
        Property(name="State23", type=FSM_AssociationStateState, multiplicity=Multiplicity(1, 1)),
        Property(name="associationStateStatesrc", type=FSM_State, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_FSM_Transition_MgaObject = Generalization(general=MgaObject, specific=FSM_Transition)
gen_FSM_State_MgaObject = Generalization(general=MgaObject, specific=FSM_State)
gen_FSM_StateMachine_MgaObject = Generalization(general=MgaObject, specific=FSM_StateMachine)

# Domain Model
domain_model = DomainModel(
    name="FSM",
    types={FSM_MgaObject, FSM_Transition, MgaObject, FSM_StateMachine, FSM_AssociationStateState, FSM_State, FSM_RootFolder},
    associations={stateMachine0, associationStateState1, stateMachine3, associationStateStatedst5, associationStateStatesrc7, rootFolder9, state10, transition12, rootFolders15, stateMachine16, transition18, dstTransition20, srcTransition22},
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