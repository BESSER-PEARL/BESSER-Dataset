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

# Enumerations
SMACHStateOutcomes: Enumeration = Enumeration(
    name="SMACHStateOutcomes",
    literals={
            EnumerationLiteral(name="succeeded"),
			EnumerationLiteral(name="preempted"),
			EnumerationLiteral(name="aborted")
    }
)

SMACHGoalTypes: Enumeration = Enumeration(
    name="SMACHGoalTypes",
    literals={
            EnumerationLiteral(name="static_goal"),
			EnumerationLiteral(name="userdata_goal")
    }
)

# Classes
smach_SMACHTransition = Class(name="smach::SMACHTransition")
smach_SMACHStateMachine = Class(name="smach::SMACHStateMachine")
Node = Class(name="Node")
smach_SMACHState = Class(name="smach::SMACHState")
smach_FinalState = Class(name="smach::FinalState")
smach_InitActionState = Class(name="smach::InitActionState")
SMACHState = Class(name="SMACHState")
smach_ActionState = Class(name="smach::ActionState")
ActionClient = Class(name="ActionClient")
smach_ServiceState = Class(name="smach::ServiceState")
ServiceClient = Class(name="ServiceClient")
smach_InitStraightState = Class(name="smach::InitStraightState")

# smach_SMACHTransition class attributes and methods
smach_SMACHTransition_name: Property = Property(name="name", type=StringType)
smach_SMACHTransition.attributes={smach_SMACHTransition_name}

# smach_SMACHStateMachine class attributes and methods
smach_SMACHStateMachine_SkillInterface: Property = Property(name="SkillInterface", type=BooleanType)
smach_SMACHStateMachine.attributes={smach_SMACHStateMachine_SkillInterface}

# Node class attributes and methods

# smach_SMACHState class attributes and methods
smach_SMACHState_goal: Property = Property(name="goal", type=StringType)
smach_SMACHState_goal_type: Property = Property(name="goal_type", type=StringType)
smach_SMACHState_remap_overwrite: Property = Property(name="remap_overwrite", type=StringType)
smach_SMACHState.attributes={smach_SMACHState_goal, smach_SMACHState_goal_type, smach_SMACHState_remap_overwrite}

# smach_FinalState class attributes and methods
smach_FinalState_type: Property = Property(name="type", type=StringType)
smach_FinalState.attributes={smach_FinalState_type}

# smach_InitActionState class attributes and methods

# SMACHState class attributes and methods

# smach_ActionState class attributes and methods

# ActionClient class attributes and methods

# smach_ServiceState class attributes and methods

# ServiceClient class attributes and methods

# smach_InitStraightState class attributes and methods

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="smach_SMACHTransition", type=smach_SMACHStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="smach_SMACHStateMachine2", type=smach_SMACHTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="smach_SMACHState", type=smach_SMACHStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="smach_SMACHStateMachine", type=smach_SMACHState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalStates3: BinaryAssociation = BinaryAssociation(
    name="finalStates3",
    ends={
        Property(name="smach_FinalState", type=smach_SMACHStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="smach_SMACHStateMachine4", type=smach_FinalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialStates5: BinaryAssociation = BinaryAssociation(
    name="initialStates5",
    ends={
        Property(name="smach_InitActionState", type=smach_SMACHStateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="smach_SMACHStateMachine6", type=smach_InitActionState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Source7: BinaryAssociation = BinaryAssociation(
    name="Source7",
    ends={
        Property(name="smach_SMACHState9", type=smach_SMACHTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smach_SMACHTransition8", type=smach_SMACHState, multiplicity=Multiplicity(1, 1))
    }
)
Target10: BinaryAssociation = BinaryAssociation(
    name="Target10",
    ends={
        Property(name="smach_SMACHState12", type=smach_SMACHTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="smach_SMACHTransition11", type=smach_SMACHState, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_smach_SMACHStateMachine_Node = Generalization(general=Node, specific=smach_SMACHStateMachine)
gen_smach_ActionState_SMACHState = Generalization(general=SMACHState, specific=smach_ActionState)
gen_smach_ActionState_ActionClient = Generalization(general=ActionClient, specific=smach_ActionState)
gen_smach_ServiceState_ServiceClient = Generalization(general=ServiceClient, specific=smach_ServiceState)
gen_smach_ServiceState_SMACHState = Generalization(general=SMACHState, specific=smach_ServiceState)
gen_smach_FinalState_SMACHState = Generalization(general=SMACHState, specific=smach_FinalState)
gen_smach_InitStraightState_SMACHState = Generalization(general=SMACHState, specific=smach_InitStraightState)
gen_smach_InitActionState_SMACHState = Generalization(general=SMACHState, specific=smach_InitActionState)

# Domain Model
domain_model = DomainModel(
    name="smach",
    types={smach_SMACHTransition, smach_SMACHStateMachine, Node, smach_SMACHState, smach_FinalState, smach_InitActionState, SMACHState, smach_ActionState, ActionClient, smach_ServiceState, ServiceClient, smach_InitStraightState, SMACHStateOutcomes, SMACHGoalTypes},
    associations={transitions1, states0, finalStates3, initialStates5, Source7, Target10},
    generalizations={gen_smach_SMACHStateMachine_Node, gen_smach_ActionState_SMACHState, gen_smach_ActionState_ActionClient, gen_smach_ServiceState_ServiceClient, gen_smach_ServiceState_SMACHState, gen_smach_FinalState_SMACHState, gen_smach_InitStraightState_SMACHState, gen_smach_InitActionState_SMACHState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)