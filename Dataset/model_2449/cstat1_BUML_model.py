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
StateType: Enumeration = Enumeration(
    name="StateType",
    literals={
            EnumerationLiteral(name="SIMPLE"),
			EnumerationLiteral(name="INITIAL"),
			EnumerationLiteral(name="FINAL")
    }
)

ActionMode: Enumeration = Enumeration(
    name="ActionMode",
    literals={
            EnumerationLiteral(name="ENTRY"),
			EnumerationLiteral(name="EXIT")
    }
)

# Classes
cstat1_SubState1 = Class(name="cstat1::SubState1")
AbstractState = Class(name="AbstractState")
cstat1_SubState2 = Class(name="cstat1::SubState2")
cstat1_StateChart = Class(name="cstat1::StateChart")
cstat1_State = Class(name="cstat1::State")
cstat1_Action = Class(name="cstat1::Action")
cstat1_Transition = Class(name="cstat1::Transition")
cstat1_AbstractState = Class(name="cstat1::AbstractState", is_abstract=True)
cstat1_EClass0 = Class(name="cstat1::EClass0")

# cstat1_SubState1 class attributes and methods

# AbstractState class attributes and methods

# cstat1_SubState2 class attributes and methods

# cstat1_StateChart class attributes and methods

# cstat1_State class attributes and methods

# cstat1_Action class attributes and methods
cstat1_Action_expression: Property = Property(name="expression", type=StringType)
cstat1_Action_mode: Property = Property(name="mode", type=StringType)
cstat1_Action.attributes={cstat1_Action_mode, cstat1_Action_expression}

# cstat1_Transition class attributes and methods
cstat1_Transition_guard: Property = Property(name="guard", type=StringType)
cstat1_Transition_event: Property = Property(name="event", type=StringType)
cstat1_Transition.attributes={cstat1_Transition_event, cstat1_Transition_guard}

# cstat1_AbstractState class attributes and methods
cstat1_AbstractState_type: Property = Property(name="type", type=StringType)
cstat1_AbstractState_id: Property = Property(name="id", type=StringType)
cstat1_AbstractState.attributes={cstat1_AbstractState_id, cstat1_AbstractState_type}

# cstat1_EClass0 class attributes and methods

# Relationships
sub2s0: BinaryAssociation = BinaryAssociation(
    name="sub2s0",
    ends={
        Property(name="cstat1_SubState2", type=cstat1_SubState1, multiplicity=Multiplicity(1, 1)),
        Property(name="cstat1_SubState1", type=cstat1_SubState2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="cstat1_State", type=cstat1_StateChart, multiplicity=Multiplicity(1, 1)),
        Property(name="cstat1_StateChart", type=cstat1_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actions12: BinaryAssociation = BinaryAssociation(
    name="actions12",
    ends={
        Property(name="cstat1_Action", type=cstat1_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="cstat1_AbstractState13", type=cstat1_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sub1s2: BinaryAssociation = BinaryAssociation(
    name="sub1s2",
    ends={
        Property(name="cstat1_SubState14", type=cstat1_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cstat1_State3", type=cstat1_SubState1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromState5: BinaryAssociation = BinaryAssociation(
    name="fromState5",
    ends={
        Property(name="cstat1_AbstractState", type=cstat1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cstat1_Transition", type=cstat1_AbstractState, multiplicity=Multiplicity(0, 1))
    }
)
toState6: BinaryAssociation = BinaryAssociation(
    name="toState6",
    ends={
        Property(name="cstat1_AbstractState8", type=cstat1_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cstat1_Transition7", type=cstat1_AbstractState, multiplicity=Multiplicity(0, 1))
    }
)
transitions9: BinaryAssociation = BinaryAssociation(
    name="transitions9",
    ends={
        Property(name="cstat1_Transition11", type=cstat1_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="cstat1_AbstractState10", type=cstat1_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cstat1_State_AbstractState = Generalization(general=AbstractState, specific=cstat1_State)
gen_cstat1_SubState1_AbstractState = Generalization(general=AbstractState, specific=cstat1_SubState1)
gen_cstat1_SubState2_AbstractState = Generalization(general=AbstractState, specific=cstat1_SubState2)

# Domain Model
domain_model = DomainModel(
    name="cstat1",
    types={cstat1_SubState1, AbstractState, cstat1_SubState2, cstat1_StateChart, cstat1_State, cstat1_Action, cstat1_Transition, cstat1_AbstractState, cstat1_EClass0, StateType, ActionMode},
    associations={sub2s0, states1, actions12, sub1s2, fromState5, toState6, transitions9},
    generalizations={gen_cstat1_State_AbstractState, gen_cstat1_SubState1_AbstractState, gen_cstat1_SubState2_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)