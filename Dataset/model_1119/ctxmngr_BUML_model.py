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
ctxmngr_ContextManager = Class(name="ctxmngr::ContextManager")
NamedElement = Class(name="NamedElement")
ctxmngr_CtxState = Class(name="ctxmngr::CtxState")
ctxmngr_ManagerState = Class(name="ctxmngr::ManagerState")
ctxmngr_ContextParameter = Class(name="ctxmngr::ContextParameter")
ctxmngr_Manager = Class(name="ctxmngr::Manager")
ctxmngr_RemoteFiringDependency = Class(name="ctxmngr::RemoteFiringDependency")
ctxmngr_CtxTransition = Class(name="ctxmngr::CtxTransition")
ctxmngr_ManagerTransition = Class(name="ctxmngr::ManagerTransition")
ctxmngr_OpaqueExpression = Class(name="ctxmngr::OpaqueExpression")

# ctxmngr_ContextManager class attributes and methods

# NamedElement class attributes and methods

# ctxmngr_CtxState class attributes and methods
ctxmngr_CtxState_isStart: Property = Property(name="isStart", type=BooleanType)
ctxmngr_CtxState_isEnd: Property = Property(name="isEnd", type=BooleanType)
ctxmngr_CtxState.attributes={ctxmngr_CtxState_isStart, ctxmngr_CtxState_isEnd}

# ctxmngr_ManagerState class attributes and methods

# ctxmngr_ContextParameter class attributes and methods
ctxmngr_ContextParameter_LitteralInteger: Property = Property(name="LitteralInteger", type=IntegerType)
ctxmngr_ContextParameter_LitteralString: Property = Property(name="LitteralString", type=StringType)
ctxmngr_ContextParameter_LitteralBoolean: Property = Property(name="LitteralBoolean", type=BooleanType)
ctxmngr_ContextParameter_LitteralUnlimitedNatural: Property = Property(name="LitteralUnlimitedNatural", type=FloatType)
ctxmngr_ContextParameter_isInput: Property = Property(name="isInput", type=BooleanType)
ctxmngr_ContextParameter.attributes={ctxmngr_ContextParameter_LitteralString, ctxmngr_ContextParameter_LitteralInteger, ctxmngr_ContextParameter_isInput, ctxmngr_ContextParameter_LitteralBoolean, ctxmngr_ContextParameter_LitteralUnlimitedNatural}

# ctxmngr_Manager class attributes and methods

# ctxmngr_RemoteFiringDependency class attributes and methods

# ctxmngr_CtxTransition class attributes and methods
ctxmngr_CtxTransition_input: Property = Property(name="input", type=StringType)
ctxmngr_CtxTransition_output: Property = Property(name="output", type=StringType)
ctxmngr_CtxTransition_transProb: Property = Property(name="transProb", type=FloatType)
ctxmngr_CtxTransition_Action: Property = Property(name="Action", type=StringType)
ctxmngr_CtxTransition_Event: Property = Property(name="Event", type=StringType)
ctxmngr_CtxTransition_Condition: Property = Property(name="Condition", type=StringType)
ctxmngr_CtxTransition_transRate: Property = Property(name="transRate", type=FloatType)
ctxmngr_CtxTransition_isRemote: Property = Property(name="isRemote", type=BooleanType)
ctxmngr_CtxTransition.attributes={ctxmngr_CtxTransition_Condition, ctxmngr_CtxTransition_input, ctxmngr_CtxTransition_isRemote, ctxmngr_CtxTransition_transRate, ctxmngr_CtxTransition_transProb, ctxmngr_CtxTransition_Action, ctxmngr_CtxTransition_Event, ctxmngr_CtxTransition_output}

# ctxmngr_ManagerTransition class attributes and methods

# ctxmngr_OpaqueExpression class attributes and methods

# Relationships
ownedState0: BinaryAssociation = BinaryAssociation(
    name="ownedState0",
    ends={
        Property(name="CtxState", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="owningManager", type=ctxmngr_CtxState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextParameters18: BinaryAssociation = BinaryAssociation(
    name="contextParameters18",
    ends={
        Property(name="ContextParameter19", type=ctxmngr_CtxState, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=ctxmngr_ContextParameter, multiplicity=Multiplicity(0, 9999))
    }
)
managerStates20: BinaryAssociation = BinaryAssociation(
    name="managerStates20",
    ends={
        Property(name="ctxmngr_ManagerState", type=ctxmngr_CtxState, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxmngr_CtxState21", type=ctxmngr_ManagerState, multiplicity=Multiplicity(0, 9999))
    }
)
owningManager22: BinaryAssociation = BinaryAssociation(
    name="owningManager22",
    ends={
        Property(name="ContextManager23", type=ctxmngr_CtxTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTransition", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1))
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="CtxState25", type=ctxmngr_CtxTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransition", type=ctxmngr_CtxState, multiplicity=Multiplicity(1, 1))
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="CtxState27", type=ctxmngr_CtxTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransition", type=ctxmngr_CtxState, multiplicity=Multiplicity(1, 1))
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="ctxmngr_CtxState", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxmngr_ContextManager", type=ctxmngr_CtxState, multiplicity=Multiplicity(1, 1))
    }
)
finalState2: BinaryAssociation = BinaryAssociation(
    name="finalState2",
    ends={
        Property(name="ctxmngr_CtxState4", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxmngr_ContextManager3", type=ctxmngr_CtxState, multiplicity=Multiplicity(0, 9999))
    }
)
contextParameters5: BinaryAssociation = BinaryAssociation(
    name="contextParameters5",
    ends={
        Property(name="ContextParameter", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="owningManager6", type=ctxmngr_ContextParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
combinedManager7: BinaryAssociation = BinaryAssociation(
    name="combinedManager7",
    ends={
        Property(name="ctxmngr_Manager", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxmngr_ContextManager8", type=ctxmngr_Manager, multiplicity=Multiplicity(0, 9999))
    }
)
remoteFirings9: BinaryAssociation = BinaryAssociation(
    name="remoteFirings9",
    ends={
        Property(name="RemoteFiringDependency", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="owningManager10", type=ctxmngr_RemoteFiringDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransition11: BinaryAssociation = BinaryAssociation(
    name="ownedTransition11",
    ends={
        Property(name="CtxTransition", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1)),
        Property(name="owningManager12", type=ctxmngr_CtxTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningManager13: BinaryAssociation = BinaryAssociation(
    name="owningManager13",
    ends={
        Property(name="ContextManager", type=ctxmngr_CtxState, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedState", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransition14: BinaryAssociation = BinaryAssociation(
    name="outgoingTransition14",
    ends={
        Property(name="CtxTransition15", type=ctxmngr_CtxState, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=ctxmngr_CtxTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransition16: BinaryAssociation = BinaryAssociation(
    name="incomingTransition16",
    ends={
        Property(name="CtxTransition17", type=ctxmngr_CtxState, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=ctxmngr_CtxTransition, multiplicity=Multiplicity(0, 9999))
    }
)
fired35: BinaryAssociation = BinaryAssociation(
    name="fired35",
    ends={
        Property(name="ctxmngr_ManagerTransition36", type=ctxmngr_RemoteFiringDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxmngr_RemoteFiringDependency", type=ctxmngr_ManagerTransition, multiplicity=Multiplicity(1, 9999))
    }
)
firing37: BinaryAssociation = BinaryAssociation(
    name="firing37",
    ends={
        Property(name="ctxmngr_ManagerTransition39", type=ctxmngr_RemoteFiringDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxmngr_RemoteFiringDependency38", type=ctxmngr_ManagerTransition, multiplicity=Multiplicity(1, 9999))
    }
)
owningManager40: BinaryAssociation = BinaryAssociation(
    name="owningManager40",
    ends={
        Property(name="ContextManager41", type=ctxmngr_RemoteFiringDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="remoteFirings", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1))
    }
)
represents42: BinaryAssociation = BinaryAssociation(
    name="represents42",
    ends={
        Property(name="ctxmngr_CtxTransition44", type=ctxmngr_RemoteFiringDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxmngr_RemoteFiringDependency43", type=ctxmngr_CtxTransition, multiplicity=Multiplicity(1, 9999))
    }
)
managerTransition28: BinaryAssociation = BinaryAssociation(
    name="managerTransition28",
    ends={
        Property(name="ctxmngr_ManagerTransition", type=ctxmngr_CtxTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxmngr_CtxTransition", type=ctxmngr_ManagerTransition, multiplicity=Multiplicity(0, 9999))
    }
)
state29: BinaryAssociation = BinaryAssociation(
    name="state29",
    ends={
        Property(name="CtxState30", type=ctxmngr_ContextParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="contextParameters", type=ctxmngr_CtxState, multiplicity=Multiplicity(0, 9999))
    }
)
opaqueExpressions31: BinaryAssociation = BinaryAssociation(
    name="opaqueExpressions31",
    ends={
        Property(name="ctxmngr_OpaqueExpression", type=ctxmngr_ContextParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxmngr_ContextParameter", type=ctxmngr_OpaqueExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningManager32: BinaryAssociation = BinaryAssociation(
    name="owningManager32",
    ends={
        Property(name="ContextManager34", type=ctxmngr_ContextParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="contextParameters33", type=ctxmngr_ContextManager, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_ctxmngr_ContextManager_NamedElement = Generalization(general=NamedElement, specific=ctxmngr_ContextManager)
gen_ctxmngr_CtxTransition_NamedElement = Generalization(general=NamedElement, specific=ctxmngr_CtxTransition)
gen_ctxmngr_CtxState_NamedElement = Generalization(general=NamedElement, specific=ctxmngr_CtxState)
gen_ctxmngr_ContextParameter_NamedElement = Generalization(general=NamedElement, specific=ctxmngr_ContextParameter)
gen_ctxmngr_RemoteFiringDependency_NamedElement = Generalization(general=NamedElement, specific=ctxmngr_RemoteFiringDependency)

# Domain Model
domain_model = DomainModel(
    name="ctxmngr",
    types={ctxmngr_ContextManager, NamedElement, ctxmngr_CtxState, ctxmngr_ManagerState, ctxmngr_ContextParameter, ctxmngr_Manager, ctxmngr_RemoteFiringDependency, ctxmngr_CtxTransition, ctxmngr_ManagerTransition, ctxmngr_OpaqueExpression},
    associations={ownedState0, contextParameters18, managerStates20, owningManager22, source24, target26, initialState1, finalState2, contextParameters5, combinedManager7, remoteFirings9, ownedTransition11, owningManager13, outgoingTransition14, incomingTransition16, fired35, firing37, owningManager40, represents42, managerTransition28, state29, opaqueExpressions31, owningManager32},
    generalizations={gen_ctxmngr_ContextManager_NamedElement, gen_ctxmngr_CtxTransition_NamedElement, gen_ctxmngr_CtxState_NamedElement, gen_ctxmngr_ContextParameter_NamedElement, gen_ctxmngr_RemoteFiringDependency_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)