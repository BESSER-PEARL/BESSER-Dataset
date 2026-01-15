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
mngr_Manager = Class(name="mngr::Manager")
NamedElement = Class(name="NamedElement")
mngr_ManagerState = Class(name="mngr::ManagerState")
mngr_ManagerParameter = Class(name="mngr::ManagerParameter")
mngr_ManagedElement = Class(name="mngr::ManagedElement")
mngr_ManagerTransition = Class(name="mngr::ManagerTransition")
mngr_OpaqueExpression = Class(name="mngr::OpaqueExpression")

# mngr_Manager class attributes and methods

# NamedElement class attributes and methods

# mngr_ManagerState class attributes and methods
mngr_ManagerState_isStart: Property = Property(name="isStart", type=BooleanType)
mngr_ManagerState_isEnd: Property = Property(name="isEnd", type=BooleanType)
mngr_ManagerState_Prob: Property = Property(name="Prob", type=FloatType)
mngr_ManagerState.attributes={mngr_ManagerState_Prob, mngr_ManagerState_isStart, mngr_ManagerState_isEnd}

# mngr_ManagerParameter class attributes and methods
mngr_ManagerParameter_isInput: Property = Property(name="isInput", type=BooleanType)
mngr_ManagerParameter_LitteralInteger: Property = Property(name="LitteralInteger", type=IntegerType)
mngr_ManagerParameter_LitteralString: Property = Property(name="LitteralString", type=StringType)
mngr_ManagerParameter_LitteralBoolean: Property = Property(name="LitteralBoolean", type=BooleanType)
mngr_ManagerParameter_LitteralUnlimitedNatural: Property = Property(name="LitteralUnlimitedNatural", type=FloatType)
mngr_ManagerParameter.attributes={mngr_ManagerParameter_LitteralBoolean, mngr_ManagerParameter_LitteralInteger, mngr_ManagerParameter_LitteralString, mngr_ManagerParameter_isInput, mngr_ManagerParameter_LitteralUnlimitedNatural}

# mngr_ManagedElement class attributes and methods
mngr_ManagedElement_description: Property = Property(name="description", type=StringType)
mngr_ManagedElement.attributes={mngr_ManagedElement_description}

# mngr_ManagerTransition class attributes and methods
mngr_ManagerTransition_Event: Property = Property(name="Event", type=StringType)
mngr_ManagerTransition_Condition: Property = Property(name="Condition", type=StringType)
mngr_ManagerTransition_Action: Property = Property(name="Action", type=StringType)
mngr_ManagerTransition_input: Property = Property(name="input", type=StringType)
mngr_ManagerTransition_output: Property = Property(name="output", type=StringType)
mngr_ManagerTransition_transProb: Property = Property(name="transProb", type=FloatType)
mngr_ManagerTransition_transRate: Property = Property(name="transRate", type=FloatType)
mngr_ManagerTransition.attributes={mngr_ManagerTransition_output, mngr_ManagerTransition_input, mngr_ManagerTransition_Event, mngr_ManagerTransition_Action, mngr_ManagerTransition_transProb, mngr_ManagerTransition_transRate, mngr_ManagerTransition_Condition}

# mngr_OpaqueExpression class attributes and methods

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="ManagerState", type=mngr_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="owningManager", type=mngr_ManagerState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="mngr_ManagerState", type=mngr_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="mngr_Manager", type=mngr_ManagerState, multiplicity=Multiplicity(1, 1))
    }
)
owningManager11: BinaryAssociation = BinaryAssociation(
    name="owningManager11",
    ends={
        Property(name="Manager", type=mngr_ManagerState, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=mngr_Manager, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition12: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition12",
    ends={
        Property(name="ManagerTransition13", type=mngr_ManagerState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=mngr_ManagerTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransition14: BinaryAssociation = BinaryAssociation(
    name="incomingTransition14",
    ends={
        Property(name="ManagerTransition15", type=mngr_ManagerState, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=mngr_ManagerTransition, multiplicity=Multiplicity(0, 9999))
    }
)
contextParameters16: BinaryAssociation = BinaryAssociation(
    name="contextParameters16",
    ends={
        Property(name="ManagerParameter17", type=mngr_ManagerState, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=mngr_ManagerParameter, multiplicity=Multiplicity(0, 9999))
    }
)
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="mngr_ManagerState4", type=mngr_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="mngr_Manager3", type=mngr_ManagerState, multiplicity=Multiplicity(0, 9999))
    }
)
contextParameters5: BinaryAssociation = BinaryAssociation(
    name="contextParameters5",
    ends={
        Property(name="ManagerParameter", type=mngr_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="owningManager6", type=mngr_ManagerParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
managedElement7: BinaryAssociation = BinaryAssociation(
    name="managedElement7",
    ends={
        Property(name="ManagedElement", type=mngr_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="owningManager8", type=mngr_ManagedElement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedTransition9: BinaryAssociation = BinaryAssociation(
    name="ownedTransition9",
    ends={
        Property(name="ManagerTransition", type=mngr_Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="owningManager10", type=mngr_ManagerTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state24: BinaryAssociation = BinaryAssociation(
    name="state24",
    ends={
        Property(name="ManagerState25", type=mngr_ManagerParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="contextParameters", type=mngr_ManagerState, multiplicity=Multiplicity(0, 9999))
    }
)
opaqueExpressions26: BinaryAssociation = BinaryAssociation(
    name="opaqueExpressions26",
    ends={
        Property(name="mngr_OpaqueExpression", type=mngr_ManagerParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="mngr_ManagerParameter", type=mngr_OpaqueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningManager18: BinaryAssociation = BinaryAssociation(
    name="owningManager18",
    ends={
        Property(name="Manager19", type=mngr_ManagerTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTransition", type=mngr_Manager, multiplicity=Multiplicity(1, 1))
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="ManagerState21", type=mngr_ManagerTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=mngr_ManagerState, multiplicity=Multiplicity(1, 1))
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="ManagerState23", type=mngr_ManagerTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=mngr_ManagerState, multiplicity=Multiplicity(1, 1))
    }
)
owningManager27: BinaryAssociation = BinaryAssociation(
    name="owningManager27",
    ends={
        Property(name="Manager29", type=mngr_ManagerParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="contextParameters28", type=mngr_Manager, multiplicity=Multiplicity(1, 1))
    }
)
owningManager30: BinaryAssociation = BinaryAssociation(
    name="owningManager30",
    ends={
        Property(name="Manager31", type=mngr_ManagedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="managedElement", type=mngr_Manager, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mngr_Manager_NamedElement = Generalization(general=NamedElement, specific=mngr_Manager)
gen_mngr_ManagerState_NamedElement = Generalization(general=NamedElement, specific=mngr_ManagerState)
gen_mngr_ManagerParameter_NamedElement = Generalization(general=NamedElement, specific=mngr_ManagerParameter)
gen_mngr_ManagerTransition_NamedElement = Generalization(general=NamedElement, specific=mngr_ManagerTransition)
gen_mngr_ManagedElement_NamedElement = Generalization(general=NamedElement, specific=mngr_ManagedElement)

# Domain Model
domain_model = DomainModel(
    name="mngr",
    types={mngr_Manager, NamedElement, mngr_ManagerState, mngr_ManagerParameter, mngr_ManagedElement, mngr_ManagerTransition, mngr_OpaqueExpression},
    associations={ownedState0, initialState1, owningManager11, outgoingTransition12, incomingTransition14, contextParameters16, finalState2, contextParameters5, managedElement7, ownedTransition9, state24, opaqueExpressions26, owningManager18, source20, target22, owningManager27, owningManager30},
    generalizations={gen_mngr_Manager_NamedElement, gen_mngr_ManagerState_NamedElement, gen_mngr_ManagerParameter_NamedElement, gen_mngr_ManagerTransition_NamedElement, gen_mngr_ManagedElement_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)