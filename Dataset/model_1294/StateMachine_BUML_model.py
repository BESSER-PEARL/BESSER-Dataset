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
TransitionKind: Enumeration = Enumeration(
    name="TransitionKind",
    literals={
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="local"),
			EnumerationLiteral(name="external")
    }
)

PseudoStateKind: Enumeration = Enumeration(
    name="PseudoStateKind",
    literals={
            EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice")
    }
)

# Classes
StateMachine_StateMachine = Class(name="StateMachine::StateMachine")
StateMachine_State = Class(name="StateMachine::State")
Vertex = Class(name="Vertex")
StateMachine_Region = Class(name="StateMachine::Region")
StateMachine_Behavior = Class(name="StateMachine::Behavior")
StateMachine_Trigger = Class(name="StateMachine::Trigger")
StateMachine_Constraint = Class(name="StateMachine::Constraint")
StateMachine_PseudoState = Class(name="StateMachine::PseudoState")
Behavior = Class(name="Behavior")
StateMachine_Vertex = Class(name="StateMachine::Vertex")
StateMachine_Transition = Class(name="StateMachine::Transition")
StateMachine_FinalState = Class(name="StateMachine::FinalState")
State = Class(name="State")
StateMachine_CodeBlock = Class(name="StateMachine::CodeBlock")

# StateMachine_StateMachine class attributes and methods
StateMachine_StateMachine_name: Property = Property(name="name", type=StringType)
StateMachine_StateMachine.attributes={StateMachine_StateMachine_name}

# StateMachine_State class attributes and methods
StateMachine_State_isComposite: Property = Property(name="isComposite", type=StringType)
StateMachine_State_isSimple: Property = Property(name="isSimple", type=StringType)
StateMachine_State_isSubmachineState: Property = Property(name="isSubmachineState", type=StringType)
StateMachine_State.attributes={StateMachine_State_isSimple, StateMachine_State_isSubmachineState, StateMachine_State_isComposite}

# Vertex class attributes and methods

# StateMachine_Region class attributes and methods
StateMachine_Region_name: Property = Property(name="name", type=StringType)
StateMachine_Region.attributes={StateMachine_Region_name}

# StateMachine_Behavior class attributes and methods

# StateMachine_Trigger class attributes and methods
StateMachine_Trigger_trigger: Property = Property(name="trigger", type=StringType)
StateMachine_Trigger.attributes={StateMachine_Trigger_trigger}

# StateMachine_Constraint class attributes and methods
StateMachine_Constraint_constraint: Property = Property(name="constraint", type=StringType)
StateMachine_Constraint.attributes={StateMachine_Constraint_constraint}

# StateMachine_PseudoState class attributes and methods
StateMachine_PseudoState_pseudoStateKind: Property = Property(name="pseudoStateKind", type=StringType)
StateMachine_PseudoState_returnValue: Property = Property(name="returnValue", type=StringType)
StateMachine_PseudoState.attributes={StateMachine_PseudoState_returnValue, StateMachine_PseudoState_pseudoStateKind}

# Behavior class attributes and methods

# StateMachine_Vertex class attributes and methods
StateMachine_Vertex_name: Property = Property(name="name", type=StringType)
StateMachine_Vertex.attributes={StateMachine_Vertex_name}

# StateMachine_Transition class attributes and methods
StateMachine_Transition_kind: Property = Property(name="kind", type=StringType)
StateMachine_Transition_name: Property = Property(name="name", type=StringType)
StateMachine_Transition.attributes={StateMachine_Transition_kind, StateMachine_Transition_name}

# StateMachine_FinalState class attributes and methods

# State class attributes and methods

# StateMachine_CodeBlock class attributes and methods
StateMachine_CodeBlock_desc: Property = Property(name="desc", type=StringType)
StateMachine_CodeBlock.attributes={StateMachine_CodeBlock_desc}

# Relationships
submachine13: BinaryAssociation = BinaryAssociation(
    name="submachine13",
    ends={
        Property(name="StateMachine", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="submachineState", type=StateMachine_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
region0: BinaryAssociation = BinaryAssociation(
    name="region0",
    ends={
        Property(name="StateMachine_Region", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_State", type=StateMachine_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
doActivity1: BinaryAssociation = BinaryAssociation(
    name="doActivity1",
    ends={
        Property(name="StateMachine_Behavior", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_State2", type=StateMachine_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deferrableTrigger3: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger3",
    ends={
        Property(name="StateMachine_Trigger", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_State4", type=StateMachine_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateInvariant5: BinaryAssociation = BinaryAssociation(
    name="stateInvariant5",
    ends={
        Property(name="StateMachine_Constraint", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_State6", type=StateMachine_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit7: BinaryAssociation = BinaryAssociation(
    name="exit7",
    ends={
        Property(name="StateMachine_Behavior9", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_State8", type=StateMachine_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry10: BinaryAssociation = BinaryAssociation(
    name="entry10",
    ends={
        Property(name="StateMachine_Behavior12", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_State11", type=StateMachine_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryPoint14: BinaryAssociation = BinaryAssociation(
    name="entryPoint14",
    ends={
        Property(name="StateMachine_PseudoState", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_State15", type=StateMachine_PseudoState, multiplicity=Multiplicity(0, 1))
    }
)
region26: BinaryAssociation = BinaryAssociation(
    name="region26",
    ends={
        Property(name="StateMachine_Region27", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_StateMachine", type=StateMachine_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
exitPoint16: BinaryAssociation = BinaryAssociation(
    name="exitPoint16",
    ends={
        Property(name="StateMachine_PseudoState18", type=StateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_State17", type=StateMachine_PseudoState, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing19: BinaryAssociation = BinaryAssociation(
    name="outgoing19",
    ends={
        Property(name="Transition", type=StateMachine_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming20: BinaryAssociation = BinaryAssociation(
    name="incoming20",
    ends={
        Property(name="Transition21", type=StateMachine_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
subvertex22: BinaryAssociation = BinaryAssociation(
    name="subvertex22",
    ends={
        Property(name="StateMachine_Vertex", type=StateMachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Region23", type=StateMachine_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition24: BinaryAssociation = BinaryAssociation(
    name="transition24",
    ends={
        Property(name="StateMachine_Transition", type=StateMachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Region25", type=StateMachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachineState28: BinaryAssociation = BinaryAssociation(
    name="submachineState28",
    ends={
        Property(name="State", type=StateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="submachine", type=StateMachine_State, multiplicity=Multiplicity(0, 9999))
    }
)
source29: BinaryAssociation = BinaryAssociation(
    name="source29",
    ends={
        Property(name="Vertex", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=StateMachine_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target30: BinaryAssociation = BinaryAssociation(
    name="target30",
    ends={
        Property(name="Vertex31", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=StateMachine_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
effect32: BinaryAssociation = BinaryAssociation(
    name="effect32",
    ends={
        Property(name="StateMachine_Behavior34", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Transition33", type=StateMachine_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger35: BinaryAssociation = BinaryAssociation(
    name="trigger35",
    ends={
        Property(name="StateMachine_Trigger37", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Transition36", type=StateMachine_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard38: BinaryAssociation = BinaryAssociation(
    name="guard38",
    ends={
        Property(name="StateMachine_Constraint40", type=StateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachine_Transition39", type=StateMachine_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_StateMachine_State_Vertex = Generalization(general=Vertex, specific=StateMachine_State)
gen_StateMachine_PseudoState_Vertex = Generalization(general=Vertex, specific=StateMachine_PseudoState)
gen_StateMachine_StateMachine_Behavior = Generalization(general=Behavior, specific=StateMachine_StateMachine)
gen_StateMachine_FinalState_State = Generalization(general=State, specific=StateMachine_FinalState)
gen_StateMachine_CodeBlock_Behavior = Generalization(general=Behavior, specific=StateMachine_CodeBlock)

# Domain Model
domain_model = DomainModel(
    name="StateMachine",
    types={StateMachine_StateMachine, StateMachine_State, Vertex, StateMachine_Region, StateMachine_Behavior, StateMachine_Trigger, StateMachine_Constraint, StateMachine_PseudoState, Behavior, StateMachine_Vertex, StateMachine_Transition, StateMachine_FinalState, State, StateMachine_CodeBlock, TransitionKind, PseudoStateKind},
    associations={submachine13, region0, doActivity1, deferrableTrigger3, stateInvariant5, exit7, entry10, entryPoint14, region26, exitPoint16, outgoing19, incoming20, subvertex22, transition24, submachineState28, source29, target30, effect32, trigger35, guard38},
    generalizations={gen_StateMachine_State_Vertex, gen_StateMachine_PseudoState_Vertex, gen_StateMachine_StateMachine_Behavior, gen_StateMachine_FinalState_State, gen_StateMachine_CodeBlock_Behavior},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)