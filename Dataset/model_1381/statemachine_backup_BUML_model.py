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
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="final")
    }
)

# Classes
statemachine_Vertex = Class(name="statemachine::Vertex", is_abstract=True)
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_State = Class(name="statemachine::State")
Vertex = Class(name="Vertex")
statemachine_Pseudostate = Class(name="statemachine::Pseudostate")
State = Class(name="State")
statemachine_Region = Class(name="statemachine::Region")
statemachine_Statemachine = Class(name="statemachine::Statemachine")
Region = Class(name="Region")
statemachine_ComplexState = Class(name="statemachine::ComplexState")
statemachine_LabeledTransition = Class(name="statemachine::LabeledTransition")
Transition = Class(name="Transition")
statemachine_Action = Class(name="statemachine::Action")

# statemachine_Vertex class attributes and methods

# statemachine_Transition class attributes and methods
statemachine_Transition_id: Property = Property(name="id", type=StringType)
statemachine_Transition.attributes={statemachine_Transition_id}

# statemachine_State class attributes and methods
statemachine_State_name: Property = Property(name="name", type=StringType)
statemachine_State.attributes={statemachine_State_name}

# Vertex class attributes and methods

# statemachine_Pseudostate class attributes and methods
statemachine_Pseudostate_kind: Property = Property(name="kind", type=StringType)
statemachine_Pseudostate_id: Property = Property(name="id", type=StringType)
statemachine_Pseudostate.attributes={statemachine_Pseudostate_id, statemachine_Pseudostate_kind}

# State class attributes and methods

# statemachine_Region class attributes and methods

# statemachine_Statemachine class attributes and methods
statemachine_Statemachine_name: Property = Property(name="name", type=StringType)
statemachine_Statemachine.attributes={statemachine_Statemachine_name}

# Region class attributes and methods

# statemachine_ComplexState class attributes and methods

# statemachine_LabeledTransition class attributes and methods

# Transition class attributes and methods

# statemachine_Action class attributes and methods
statemachine_Action_name: Property = Property(name="name", type=StringType)
statemachine_Action.attributes={statemachine_Action_name}

# Relationships
outgoings0: BinaryAssociation = BinaryAssociation(
    name="outgoings0",
    ends={
        Property(name="statemachine_Transition", type=statemachine_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Vertex", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
region2: BinaryAssociation = BinaryAssociation(
    name="region2",
    ends={
        Property(name="statemachine_Region", type=statemachine_ComplexState, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_ComplexState3", type=statemachine_Region, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="statemachine_Vertex6", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition5", type=statemachine_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="statemachine_Vertex9", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition8", type=statemachine_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
super1: BinaryAssociation = BinaryAssociation(
    name="super1",
    ends={
        Property(name="statemachine_ComplexState", type=statemachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_State", type=statemachine_ComplexState, multiplicity=Multiplicity(0, 1))
    }
)
actions12: BinaryAssociation = BinaryAssociation(
    name="actions12",
    ends={
        Property(name="statemachine_Action", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine13", type=statemachine_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states14: BinaryAssociation = BinaryAssociation(
    name="states14",
    ends={
        Property(name="statemachine_State16", type=statemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Region15", type=statemachine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial17: BinaryAssociation = BinaryAssociation(
    name="initial17",
    ends={
        Property(name="statemachine_Pseudostate", type=statemachine_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Region18", type=statemachine_Pseudostate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action19: BinaryAssociation = BinaryAssociation(
    name="action19",
    ends={
        Property(name="statemachine_Action20", type=statemachine_LabeledTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_LabeledTransition", type=statemachine_Action, multiplicity=Multiplicity(1, 1))
    }
)
transitions10: BinaryAssociation = BinaryAssociation(
    name="transitions10",
    ends={
        Property(name="statemachine_Transition11", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statemachine_State_Vertex = Generalization(general=Vertex, specific=statemachine_State)
gen_statemachine_Pseudostate_Vertex = Generalization(general=Vertex, specific=statemachine_Pseudostate)
gen_statemachine_ComplexState_State = Generalization(general=State, specific=statemachine_ComplexState)
gen_statemachine_Statemachine_Region = Generalization(general=Region, specific=statemachine_Statemachine)
gen_statemachine_LabeledTransition_Transition = Generalization(general=Transition, specific=statemachine_LabeledTransition)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Vertex, statemachine_Transition, statemachine_State, Vertex, statemachine_Pseudostate, State, statemachine_Region, statemachine_Statemachine, Region, statemachine_ComplexState, statemachine_LabeledTransition, Transition, statemachine_Action, PseudostateKind},
    associations={outgoings0, region2, source4, target7, super1, actions12, states14, initial17, action19, transitions10},
    generalizations={gen_statemachine_State_Vertex, gen_statemachine_Pseudostate_Vertex, gen_statemachine_ComplexState_State, gen_statemachine_Statemachine_Region, gen_statemachine_LabeledTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)