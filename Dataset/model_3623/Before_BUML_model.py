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
PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="inital"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction")
    }
)

# Classes
ModelElement = Class(name="ModelElement")
minuml1_State = Class(name="minuml1::State")
minuml1_ModelElement = Class(name="minuml1::ModelElement")
minuml1_Partition = Class(name="minuml1::Partition")
minuml1_StateMachine = Class(name="minuml1::StateMachine")
minuml1_Transition = Class(name="minuml1::Transition")
minuml1_Activity = Class(name="minuml1::Activity")
StateMachine = Class(name="StateMachine")
minuml1_StateVertex = Class(name="minuml1::StateVertex", is_abstract=True)
StateVertex = Class(name="StateVertex")
minuml1_CompositeState = Class(name="minuml1::CompositeState")
State = Class(name="State")
minuml1_FinalState = Class(name="minuml1::FinalState")
minuml1_ActionState = Class(name="minuml1::ActionState")
minuml1_Pseudostate = Class(name="minuml1::Pseudostate")
minuml1_ObjectFlowState = Class(name="minuml1::ObjectFlowState")
minuml1_BooleanExpression = Class(name="minuml1::BooleanExpression")
minuml1_Guard = Class(name="minuml1::Guard")

# ModelElement class attributes and methods

# minuml1_State class attributes and methods

# minuml1_ModelElement class attributes and methods
minuml1_ModelElement_name: Property = Property(name="name", type=StringType)
minuml1_ModelElement.attributes={minuml1_ModelElement_name}

# minuml1_Partition class attributes and methods

# minuml1_StateMachine class attributes and methods

# minuml1_Transition class attributes and methods

# minuml1_Activity class attributes and methods

# StateMachine class attributes and methods

# minuml1_StateVertex class attributes and methods

# StateVertex class attributes and methods

# minuml1_CompositeState class attributes and methods

# State class attributes and methods

# minuml1_FinalState class attributes and methods

# minuml1_ActionState class attributes and methods
minuml1_ActionState_isDynamic: Property = Property(name="isDynamic", type=BooleanType)
minuml1_ActionState.attributes={minuml1_ActionState_isDynamic}

# minuml1_Pseudostate class attributes and methods
minuml1_Pseudostate_kind: Property = Property(name="kind", type=StringType)
minuml1_Pseudostate.attributes={minuml1_Pseudostate_kind}

# minuml1_ObjectFlowState class attributes and methods

# minuml1_BooleanExpression class attributes and methods
minuml1_BooleanExpression_language: Property = Property(name="language", type=StringType)
minuml1_BooleanExpression_body: Property = Property(name="body", type=StringType)
minuml1_BooleanExpression.attributes={minuml1_BooleanExpression_body, minuml1_BooleanExpression_language}

# minuml1_Guard class attributes and methods

# Relationships
top1: BinaryAssociation = BinaryAssociation(
    name="top1",
    ends={
        Property(name="minuml1_State", type=minuml1_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml1_StateMachine", type=minuml1_State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
partition0: BinaryAssociation = BinaryAssociation(
    name="partition0",
    ends={
        Property(name="Partition", type=minuml1_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="contents", type=minuml1_Partition, multiplicity=Multiplicity(1, 1))
    }
)
contents5: BinaryAssociation = BinaryAssociation(
    name="contents5",
    ends={
        Property(name="ModelElement", type=minuml1_Partition, multiplicity=Multiplicity(1, 1)),
        Property(name="partition", type=minuml1_ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
transitions2: BinaryAssociation = BinaryAssociation(
    name="transitions2",
    ends={
        Property(name="minuml1_Transition", type=minuml1_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml1_StateMachine3", type=minuml1_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parition4: BinaryAssociation = BinaryAssociation(
    name="parition4",
    ends={
        Property(name="minuml1_Partition", type=minuml1_Activity, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml1_Activity", type=minuml1_Partition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subvertex9: BinaryAssociation = BinaryAssociation(
    name="subvertex9",
    ends={
        Property(name="minuml1_StateVertex", type=minuml1_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml1_CompositeState", type=minuml1_StateVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Transition", type=minuml1_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=minuml1_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming7: BinaryAssociation = BinaryAssociation(
    name="incoming7",
    ends={
        Property(name="Transition8", type=minuml1_StateVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=minuml1_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="minuml1_ModelElement", type=minuml1_ObjectFlowState, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml1_ObjectFlowState", type=minuml1_ModelElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression16: BinaryAssociation = BinaryAssociation(
    name="expression16",
    ends={
        Property(name="minuml1_BooleanExpression", type=minuml1_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml1_Guard17", type=minuml1_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="StateVertex", type=minuml1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=minuml1_StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="StateVertex13", type=minuml1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=minuml1_StateVertex, multiplicity=Multiplicity(1, 1))
    }
)
guard14: BinaryAssociation = BinaryAssociation(
    name="guard14",
    ends={
        Property(name="minuml1_Guard", type=minuml1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="minuml1_Transition15", type=minuml1_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_minuml1_StateMachine_ModelElement = Generalization(general=ModelElement, specific=minuml1_StateMachine)
gen_minuml1_Activity_StateMachine = Generalization(general=StateMachine, specific=minuml1_Activity)
gen_minuml1_Partition_ModelElement = Generalization(general=ModelElement, specific=minuml1_Partition)
gen_minuml1_StateVertex_ModelElement = Generalization(general=ModelElement, specific=minuml1_StateVertex)
gen_minuml1_State_StateVertex = Generalization(general=StateVertex, specific=minuml1_State)
gen_minuml1_CompositeState_State = Generalization(general=State, specific=minuml1_CompositeState)
gen_minuml1_FinalState_State = Generalization(general=State, specific=minuml1_FinalState)
gen_minuml1_ActionState_State = Generalization(general=State, specific=minuml1_ActionState)
gen_minuml1_Pseudostate_StateVertex = Generalization(general=StateVertex, specific=minuml1_Pseudostate)
gen_minuml1_ObjectFlowState_State = Generalization(general=State, specific=minuml1_ObjectFlowState)
gen_minuml1_Transition_ModelElement = Generalization(general=ModelElement, specific=minuml1_Transition)
gen_minuml1_Guard_ModelElement = Generalization(general=ModelElement, specific=minuml1_Guard)

# Domain Model
domain_model = DomainModel(
    name="minuml1",
    types={ModelElement, minuml1_State, minuml1_ModelElement, minuml1_Partition, minuml1_StateMachine, minuml1_Transition, minuml1_Activity, StateMachine, minuml1_StateVertex, StateVertex, minuml1_CompositeState, State, minuml1_FinalState, minuml1_ActionState, minuml1_Pseudostate, minuml1_ObjectFlowState, minuml1_BooleanExpression, minuml1_Guard, PseudostateKind},
    associations={top1, partition0, contents5, transitions2, parition4, subvertex9, outgoing6, incoming7, type10, expression16, source11, target12, guard14},
    generalizations={gen_minuml1_StateMachine_ModelElement, gen_minuml1_Activity_StateMachine, gen_minuml1_Partition_ModelElement, gen_minuml1_StateVertex_ModelElement, gen_minuml1_State_StateVertex, gen_minuml1_CompositeState_State, gen_minuml1_FinalState_State, gen_minuml1_ActionState_State, gen_minuml1_Pseudostate_StateVertex, gen_minuml1_ObjectFlowState_State, gen_minuml1_Transition_ModelElement, gen_minuml1_Guard_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)