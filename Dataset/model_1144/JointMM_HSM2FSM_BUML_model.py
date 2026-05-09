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
SrcRoot = Class(name="SrcRoot")
TrgRoot = Class(name="TrgRoot")
jointPackage_HSM2FSM_SrcRoot = Class(name="jointPackage_HSM2FSM_SrcRoot")
SrcStateMachine = Class(name="SrcStateMachine")
jointPackage_HSM2FSM_JointMM = Class(name="jointPackage_HSM2FSM_JointMM")
TrgAbstractState = Class(name="TrgAbstractState")
jointPackage_HSM2FSM_TrgTransition = Class(name="jointPackage_HSM2FSM_TrgTransition")
jointPackage_HSM2FSM_TrgAbstractState = Class(name="jointPackage_HSM2FSM_TrgAbstractState", is_abstract=True)
jointPackage_HSM2FSM_SrcStateMachine = Class(name="jointPackage_HSM2FSM_SrcStateMachine")
SrcTransition = Class(name="SrcTransition")
SrcAbstractState = Class(name="SrcAbstractState")
jointPackage_HSM2FSM_SrcTransition = Class(name="jointPackage_HSM2FSM_SrcTransition")
jointPackage_HSM2FSM_SrcAbstractState = Class(name="jointPackage_HSM2FSM_SrcAbstractState", is_abstract=True)
SrcCompositeState = Class(name="SrcCompositeState")
jointPackage_HSM2FSM_SrcInitialState = Class(name="jointPackage_HSM2FSM_SrcInitialState")
jointPackage_HSM2FSM_SrcRegularState = Class(name="jointPackage_HSM2FSM_SrcRegularState")
jointPackage_HSM2FSM_SrcCompositeState = Class(name="jointPackage_HSM2FSM_SrcCompositeState")
jointPackage_HSM2FSM_TrgRoot = Class(name="jointPackage_HSM2FSM_TrgRoot")
TrgStateMachine = Class(name="TrgStateMachine")
jointPackage_HSM2FSM_TrgStateMachine = Class(name="jointPackage_HSM2FSM_TrgStateMachine")
TrgTransition = Class(name="TrgTransition")
TrgCompositeState = Class(name="TrgCompositeState")
jointPackage_HSM2FSM_TrgInitialState = Class(name="jointPackage_HSM2FSM_TrgInitialState")
jointPackage_HSM2FSM_TrgRegularState = Class(name="jointPackage_HSM2FSM_TrgRegularState")
jointPackage_HSM2FSM_TrgCompositeState = Class(name="jointPackage_HSM2FSM_TrgCompositeState")

# SrcRoot class attributes and methods

# TrgRoot class attributes and methods

# jointPackage_HSM2FSM_SrcRoot class attributes and methods

# SrcStateMachine class attributes and methods

# jointPackage_HSM2FSM_JointMM class attributes and methods

# TrgAbstractState class attributes and methods

# jointPackage_HSM2FSM_TrgTransition class attributes and methods
jointPackage_HSM2FSM_TrgTransition_label: Property = Property(name="label", type=StringType)
jointPackage_HSM2FSM_TrgTransition.attributes={jointPackage_HSM2FSM_TrgTransition_label}

# jointPackage_HSM2FSM_TrgAbstractState class attributes and methods
jointPackage_HSM2FSM_TrgAbstractState_name: Property = Property(name="name", type=StringType)
jointPackage_HSM2FSM_TrgAbstractState.attributes={jointPackage_HSM2FSM_TrgAbstractState_name}

# jointPackage_HSM2FSM_SrcStateMachine class attributes and methods
jointPackage_HSM2FSM_SrcStateMachine_name: Property = Property(name="name", type=StringType)
jointPackage_HSM2FSM_SrcStateMachine.attributes={jointPackage_HSM2FSM_SrcStateMachine_name}

# SrcTransition class attributes and methods

# SrcAbstractState class attributes and methods

# jointPackage_HSM2FSM_SrcTransition class attributes and methods
jointPackage_HSM2FSM_SrcTransition_label: Property = Property(name="label", type=StringType)
jointPackage_HSM2FSM_SrcTransition.attributes={jointPackage_HSM2FSM_SrcTransition_label}

# jointPackage_HSM2FSM_SrcAbstractState class attributes and methods
jointPackage_HSM2FSM_SrcAbstractState_name: Property = Property(name="name", type=StringType)
jointPackage_HSM2FSM_SrcAbstractState.attributes={jointPackage_HSM2FSM_SrcAbstractState_name}

# SrcCompositeState class attributes and methods

# jointPackage_HSM2FSM_SrcInitialState class attributes and methods

# jointPackage_HSM2FSM_SrcRegularState class attributes and methods

# jointPackage_HSM2FSM_SrcCompositeState class attributes and methods

# jointPackage_HSM2FSM_TrgRoot class attributes and methods

# TrgStateMachine class attributes and methods

# jointPackage_HSM2FSM_TrgStateMachine class attributes and methods
jointPackage_HSM2FSM_TrgStateMachine_name: Property = Property(name="name", type=StringType)
jointPackage_HSM2FSM_TrgStateMachine.attributes={jointPackage_HSM2FSM_TrgStateMachine_name}

# TrgTransition class attributes and methods

# TrgCompositeState class attributes and methods

# jointPackage_HSM2FSM_TrgInitialState class attributes and methods

# jointPackage_HSM2FSM_TrgRegularState class attributes and methods

# jointPackage_HSM2FSM_TrgCompositeState class attributes and methods

# Relationships
sourceRoot0: BinaryAssociation = BinaryAssociation(
    name="sourceRoot0",
    ends={
        Property(name="SrcRoot", type=jointPackage_HSM2FSM_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_JointMM", type=SrcRoot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetRoot1: BinaryAssociation = BinaryAssociation(
    name="targetRoot1",
    ends={
        Property(name="TrgRoot", type=jointPackage_HSM2FSM_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_JointMM2", type=TrgRoot, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statemachines3: BinaryAssociation = BinaryAssociation(
    name="statemachines3",
    ends={
        Property(name="SrcStateMachine", type=jointPackage_HSM2FSM_SrcRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_SrcRoot", type=SrcStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions21: BinaryAssociation = BinaryAssociation(
    name="transitions21",
    ends={
        Property(name="stateMachine22", type=TrgTransition, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="TrgTransition", type=jointPackage_HSM2FSM_TrgStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
states23: BinaryAssociation = BinaryAssociation(
    name="states23",
    ends={
        Property(name="TrgAbstractState", type=jointPackage_HSM2FSM_TrgStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine24", type=TrgAbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine25: BinaryAssociation = BinaryAssociation(
    name="stateMachine25",
    ends={
        Property(name="TrgStateMachine27", type=jointPackage_HSM2FSM_TrgTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions26", type=TrgStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
source28: BinaryAssociation = BinaryAssociation(
    name="source28",
    ends={
        Property(name="TrgAbstractState29", type=jointPackage_HSM2FSM_TrgTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_TrgTransition", type=TrgAbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target30: BinaryAssociation = BinaryAssociation(
    name="target30",
    ends={
        Property(name="TrgAbstractState32", type=jointPackage_HSM2FSM_TrgTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_TrgTransition31", type=TrgAbstractState, multiplicity=Multiplicity(1, 1))
    }
)
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="SrcTransition", type=jointPackage_HSM2FSM_SrcStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=SrcTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states5: BinaryAssociation = BinaryAssociation(
    name="states5",
    ends={
        Property(name="SrcAbstractState", type=jointPackage_HSM2FSM_SrcStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine6", type=SrcAbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine7: BinaryAssociation = BinaryAssociation(
    name="stateMachine7",
    ends={
        Property(name="SrcStateMachine8", type=jointPackage_HSM2FSM_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=SrcStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="SrcAbstractState10", type=jointPackage_HSM2FSM_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_SrcTransition", type=SrcAbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="SrcAbstractState13", type=jointPackage_HSM2FSM_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_SrcTransition12", type=SrcAbstractState, multiplicity=Multiplicity(1, 1))
    }
)
stateMachine14: BinaryAssociation = BinaryAssociation(
    name="stateMachine14",
    ends={
        Property(name="SrcStateMachine15", type=jointPackage_HSM2FSM_SrcAbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=SrcStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
compositeStates16: BinaryAssociation = BinaryAssociation(
    name="compositeStates16",
    ends={
        Property(name="SrcCompositeState", type=jointPackage_HSM2FSM_SrcAbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states17", type=SrcCompositeState, multiplicity=Multiplicity(0, 1))
    }
)
states18: BinaryAssociation = BinaryAssociation(
    name="states18",
    ends={
        Property(name="SrcAbstractState19", type=jointPackage_HSM2FSM_SrcCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeStates", type=SrcAbstractState, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachines20: BinaryAssociation = BinaryAssociation(
    name="stateMachines20",
    ends={
        Property(name="TrgStateMachine", type=jointPackage_HSM2FSM_TrgRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_TrgRoot", type=TrgStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine33: BinaryAssociation = BinaryAssociation(
    name="stateMachine33",
    ends={
        Property(name="TrgStateMachine35", type=jointPackage_HSM2FSM_TrgAbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states34", type=TrgStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
compositeStates36: BinaryAssociation = BinaryAssociation(
    name="compositeStates36",
    ends={
        Property(name="TrgCompositeState", type=jointPackage_HSM2FSM_TrgAbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="states37", type=TrgCompositeState, multiplicity=Multiplicity(0, 1))
    }
)
states38: BinaryAssociation = BinaryAssociation(
    name="states38",
    ends={
        Property(name="TrgAbstractState40", type=jointPackage_HSM2FSM_TrgCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="compositeStates39", type=TrgAbstractState, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_jointPackage_HSM2FSM_SrcInitialState_SrcAbstractState = Generalization(general=SrcAbstractState, specific=jointPackage_HSM2FSM_SrcInitialState)
gen_jointPackage_HSM2FSM_SrcRegularState_SrcAbstractState = Generalization(general=SrcAbstractState, specific=jointPackage_HSM2FSM_SrcRegularState)
gen_jointPackage_HSM2FSM_SrcCompositeState_SrcAbstractState = Generalization(general=SrcAbstractState, specific=jointPackage_HSM2FSM_SrcCompositeState)
gen_jointPackage_HSM2FSM_TrgInitialState_TrgAbstractState = Generalization(general=TrgAbstractState, specific=jointPackage_HSM2FSM_TrgInitialState)
gen_jointPackage_HSM2FSM_TrgRegularState_TrgAbstractState = Generalization(general=TrgAbstractState, specific=jointPackage_HSM2FSM_TrgRegularState)
gen_jointPackage_HSM2FSM_TrgCompositeState_TrgAbstractState = Generalization(general=TrgAbstractState, specific=jointPackage_HSM2FSM_TrgCompositeState)

# Domain Model
domain_model = DomainModel(
    name="jointPackage_HSM2FSM",
    types={SrcRoot, TrgRoot, jointPackage_HSM2FSM_SrcRoot, SrcStateMachine, jointPackage_HSM2FSM_JointMM, TrgAbstractState, jointPackage_HSM2FSM_TrgTransition, jointPackage_HSM2FSM_TrgAbstractState, jointPackage_HSM2FSM_SrcStateMachine, SrcTransition, SrcAbstractState, jointPackage_HSM2FSM_SrcTransition, jointPackage_HSM2FSM_SrcAbstractState, SrcCompositeState, jointPackage_HSM2FSM_SrcInitialState, jointPackage_HSM2FSM_SrcRegularState, jointPackage_HSM2FSM_SrcCompositeState, jointPackage_HSM2FSM_TrgRoot, TrgStateMachine, jointPackage_HSM2FSM_TrgStateMachine, TrgTransition, TrgCompositeState, jointPackage_HSM2FSM_TrgInitialState, jointPackage_HSM2FSM_TrgRegularState, jointPackage_HSM2FSM_TrgCompositeState},
    associations={sourceRoot0, targetRoot1, statemachines3, transitions21, states23, stateMachine25, source28, target30, transitions4, states5, stateMachine7, source9, target11, stateMachine14, compositeStates16, states18, stateMachines20, stateMachine33, compositeStates36, states38},
    generalizations={gen_jointPackage_HSM2FSM_SrcInitialState_SrcAbstractState, gen_jointPackage_HSM2FSM_SrcRegularState_SrcAbstractState, gen_jointPackage_HSM2FSM_SrcCompositeState_SrcAbstractState, gen_jointPackage_HSM2FSM_TrgInitialState_TrgAbstractState, gen_jointPackage_HSM2FSM_TrgRegularState_TrgAbstractState, gen_jointPackage_HSM2FSM_TrgCompositeState_TrgAbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)