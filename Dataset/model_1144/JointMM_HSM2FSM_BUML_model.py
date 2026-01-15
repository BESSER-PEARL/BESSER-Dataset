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
jointPackage_HSM2FSM_JointMM = Class(name="jointPackage::HSM2FSM::JointMM")
SrcRoot = Class(name="SrcRoot")
TrgRoot = Class(name="TrgRoot")
jointPackage_HSM2FSM_SrcRoot = Class(name="jointPackage::HSM2FSM::SrcRoot")
SrcStateMachine = Class(name="SrcStateMachine")
jointPackage_HSM2FSM_SrcStateMachine = Class(name="jointPackage::HSM2FSM::SrcStateMachine")
SrcTransition = Class(name="SrcTransition")
SrcAbstractState = Class(name="SrcAbstractState")
jointPackage_HSM2FSM_SrcTransition = Class(name="jointPackage::HSM2FSM::SrcTransition")
jointPackage_HSM2FSM_SrcRegularState = Class(name="jointPackage::HSM2FSM::SrcRegularState")
jointPackage_HSM2FSM_SrcCompositeState = Class(name="jointPackage::HSM2FSM::SrcCompositeState")
jointPackage_HSM2FSM_TrgRoot = Class(name="jointPackage::HSM2FSM::TrgRoot")
TrgStateMachine = Class(name="TrgStateMachine")
jointPackage_HSM2FSM_TrgStateMachine = Class(name="jointPackage::HSM2FSM::TrgStateMachine")
TrgTransition = Class(name="TrgTransition")
TrgAbstractState = Class(name="TrgAbstractState")
jointPackage_HSM2FSM_TrgTransition = Class(name="jointPackage::HSM2FSM::TrgTransition")
jointPackage_HSM2FSM_TrgAbstractState = Class(name="jointPackage::HSM2FSM::TrgAbstractState", is_abstract=True)
TrgCompositeState = Class(name="TrgCompositeState")
jointPackage_HSM2FSM_SrcAbstractState = Class(name="jointPackage::HSM2FSM::SrcAbstractState", is_abstract=True)
SrcCompositeState = Class(name="SrcCompositeState")
jointPackage_HSM2FSM_SrcInitialState = Class(name="jointPackage::HSM2FSM::SrcInitialState")
jointPackage_HSM2FSM_TrgInitialState = Class(name="jointPackage::HSM2FSM::TrgInitialState")
jointPackage_HSM2FSM_TrgRegularState = Class(name="jointPackage::HSM2FSM::TrgRegularState")
jointPackage_HSM2FSM_TrgCompositeState = Class(name="jointPackage::HSM2FSM::TrgCompositeState")

# jointPackage_HSM2FSM_JointMM class attributes and methods

# SrcRoot class attributes and methods

# TrgRoot class attributes and methods

# jointPackage_HSM2FSM_SrcRoot class attributes and methods

# SrcStateMachine class attributes and methods

# jointPackage_HSM2FSM_SrcStateMachine class attributes and methods
jointPackage_HSM2FSM_SrcStateMachine_name: Property = Property(name="name", type=StringType)
jointPackage_HSM2FSM_SrcStateMachine.attributes={jointPackage_HSM2FSM_SrcStateMachine_name}

# SrcTransition class attributes and methods

# SrcAbstractState class attributes and methods

# jointPackage_HSM2FSM_SrcTransition class attributes and methods
jointPackage_HSM2FSM_SrcTransition_label: Property = Property(name="label", type=StringType)
jointPackage_HSM2FSM_SrcTransition.attributes={jointPackage_HSM2FSM_SrcTransition_label}

# jointPackage_HSM2FSM_SrcRegularState class attributes and methods

# jointPackage_HSM2FSM_SrcCompositeState class attributes and methods

# jointPackage_HSM2FSM_TrgRoot class attributes and methods

# TrgStateMachine class attributes and methods

# jointPackage_HSM2FSM_TrgStateMachine class attributes and methods
jointPackage_HSM2FSM_TrgStateMachine_name: Property = Property(name="name", type=StringType)
jointPackage_HSM2FSM_TrgStateMachine.attributes={jointPackage_HSM2FSM_TrgStateMachine_name}

# TrgTransition class attributes and methods

# TrgAbstractState class attributes and methods

# jointPackage_HSM2FSM_TrgTransition class attributes and methods
jointPackage_HSM2FSM_TrgTransition_label: Property = Property(name="label", type=StringType)
jointPackage_HSM2FSM_TrgTransition.attributes={jointPackage_HSM2FSM_TrgTransition_label}

# jointPackage_HSM2FSM_TrgAbstractState class attributes and methods
jointPackage_HSM2FSM_TrgAbstractState_name: Property = Property(name="name", type=StringType)
jointPackage_HSM2FSM_TrgAbstractState.attributes={jointPackage_HSM2FSM_TrgAbstractState_name}

# TrgCompositeState class attributes and methods

# jointPackage_HSM2FSM_SrcAbstractState class attributes and methods
jointPackage_HSM2FSM_SrcAbstractState_name: Property = Property(name="name", type=StringType)
jointPackage_HSM2FSM_SrcAbstractState.attributes={jointPackage_HSM2FSM_SrcAbstractState_name}

# SrcCompositeState class attributes and methods

# jointPackage_HSM2FSM_SrcInitialState class attributes and methods

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
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="#", type=jointPackage_HSM2FSM_SrcStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=SrcTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states5: BinaryAssociation = BinaryAssociation(
    name="states5",
    ends={
        Property(name="#7", type=jointPackage_HSM2FSM_SrcStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="06", type=SrcAbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine8: BinaryAssociation = BinaryAssociation(
    name="stateMachine8",
    ends={
        Property(name="#10", type=jointPackage_HSM2FSM_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="09", type=SrcStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="SrcAbstractState", type=jointPackage_HSM2FSM_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_SrcTransition", type=SrcAbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="SrcAbstractState14", type=jointPackage_HSM2FSM_SrcTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_SrcTransition13", type=SrcAbstractState, multiplicity=Multiplicity(1, 1))
    }
)
states21: BinaryAssociation = BinaryAssociation(
    name="states21",
    ends={
        Property(name="#23", type=jointPackage_HSM2FSM_SrcCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="022", type=SrcAbstractState, multiplicity=Multiplicity(0, 9999))
    }
)
stateMachines24: BinaryAssociation = BinaryAssociation(
    name="stateMachines24",
    ends={
        Property(name="TrgStateMachine", type=jointPackage_HSM2FSM_TrgRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_TrgRoot", type=TrgStateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions25: BinaryAssociation = BinaryAssociation(
    name="transitions25",
    ends={
        Property(name="#27", type=jointPackage_HSM2FSM_TrgStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="026", type=TrgTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states28: BinaryAssociation = BinaryAssociation(
    name="states28",
    ends={
        Property(name="#30", type=jointPackage_HSM2FSM_TrgStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="029", type=TrgAbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine31: BinaryAssociation = BinaryAssociation(
    name="stateMachine31",
    ends={
        Property(name="#33", type=jointPackage_HSM2FSM_TrgTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="032", type=TrgStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
source34: BinaryAssociation = BinaryAssociation(
    name="source34",
    ends={
        Property(name="TrgAbstractState", type=jointPackage_HSM2FSM_TrgTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_TrgTransition", type=TrgAbstractState, multiplicity=Multiplicity(1, 1))
    }
)
target35: BinaryAssociation = BinaryAssociation(
    name="target35",
    ends={
        Property(name="TrgAbstractState37", type=jointPackage_HSM2FSM_TrgTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_HSM2FSM_TrgTransition36", type=TrgAbstractState, multiplicity=Multiplicity(1, 1))
    }
)
stateMachine38: BinaryAssociation = BinaryAssociation(
    name="stateMachine38",
    ends={
        Property(name="#40", type=jointPackage_HSM2FSM_TrgAbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="039", type=TrgStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
compositeStates41: BinaryAssociation = BinaryAssociation(
    name="compositeStates41",
    ends={
        Property(name="#43", type=jointPackage_HSM2FSM_TrgAbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="042", type=TrgCompositeState, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine15: BinaryAssociation = BinaryAssociation(
    name="stateMachine15",
    ends={
        Property(name="#17", type=jointPackage_HSM2FSM_SrcAbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="016", type=SrcStateMachine, multiplicity=Multiplicity(1, 1))
    }
)
compositeStates18: BinaryAssociation = BinaryAssociation(
    name="compositeStates18",
    ends={
        Property(name="#20", type=jointPackage_HSM2FSM_SrcAbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="019", type=SrcCompositeState, multiplicity=Multiplicity(0, 1))
    }
)
states44: BinaryAssociation = BinaryAssociation(
    name="states44",
    ends={
        Property(name="#46", type=jointPackage_HSM2FSM_TrgCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="045", type=TrgAbstractState, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_jointPackage_HSM2FSM_SrcRegularState_SrcAbstractState = Generalization(general=SrcAbstractState, specific=jointPackage_HSM2FSM_SrcRegularState)
gen_jointPackage_HSM2FSM_SrcCompositeState_SrcAbstractState = Generalization(general=SrcAbstractState, specific=jointPackage_HSM2FSM_SrcCompositeState)
gen_jointPackage_HSM2FSM_SrcInitialState_SrcAbstractState = Generalization(general=SrcAbstractState, specific=jointPackage_HSM2FSM_SrcInitialState)
gen_jointPackage_HSM2FSM_TrgInitialState_TrgAbstractState = Generalization(general=TrgAbstractState, specific=jointPackage_HSM2FSM_TrgInitialState)
gen_jointPackage_HSM2FSM_TrgRegularState_TrgAbstractState = Generalization(general=TrgAbstractState, specific=jointPackage_HSM2FSM_TrgRegularState)
gen_jointPackage_HSM2FSM_TrgCompositeState_TrgAbstractState = Generalization(general=TrgAbstractState, specific=jointPackage_HSM2FSM_TrgCompositeState)

# Domain Model
domain_model = DomainModel(
    name="jointPackage_HSM2FSM",
    types={jointPackage_HSM2FSM_JointMM, SrcRoot, TrgRoot, jointPackage_HSM2FSM_SrcRoot, SrcStateMachine, jointPackage_HSM2FSM_SrcStateMachine, SrcTransition, SrcAbstractState, jointPackage_HSM2FSM_SrcTransition, jointPackage_HSM2FSM_SrcRegularState, jointPackage_HSM2FSM_SrcCompositeState, jointPackage_HSM2FSM_TrgRoot, TrgStateMachine, jointPackage_HSM2FSM_TrgStateMachine, TrgTransition, TrgAbstractState, jointPackage_HSM2FSM_TrgTransition, jointPackage_HSM2FSM_TrgAbstractState, TrgCompositeState, jointPackage_HSM2FSM_SrcAbstractState, SrcCompositeState, jointPackage_HSM2FSM_SrcInitialState, jointPackage_HSM2FSM_TrgInitialState, jointPackage_HSM2FSM_TrgRegularState, jointPackage_HSM2FSM_TrgCompositeState},
    associations={sourceRoot0, targetRoot1, statemachines3, transitions4, states5, stateMachine8, source11, target12, states21, stateMachines24, transitions25, states28, stateMachine31, source34, target35, stateMachine38, compositeStates41, stateMachine15, compositeStates18, states44},
    generalizations={gen_jointPackage_HSM2FSM_SrcRegularState_SrcAbstractState, gen_jointPackage_HSM2FSM_SrcCompositeState_SrcAbstractState, gen_jointPackage_HSM2FSM_SrcInitialState_SrcAbstractState, gen_jointPackage_HSM2FSM_TrgInitialState_TrgAbstractState, gen_jointPackage_HSM2FSM_TrgRegularState_TrgAbstractState, gen_jointPackage_HSM2FSM_TrgCompositeState_TrgAbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)