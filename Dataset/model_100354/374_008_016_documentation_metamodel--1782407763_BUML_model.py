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
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate")
    }
)

# Classes
uml_StateMachine = Class(name="uml_StateMachine")
Behavior = Class(name="Behavior")
uml_Transition = Class(name="uml_Transition")
uml_Behavior = Class(name="uml_Behavior", is_abstract=True)
uml_Trigger = Class(name="uml_Trigger")
uml_Vertex = Class(name="uml_Vertex", is_abstract=True)
uml_Region = Class(name="uml_Region")
uml_Pseudostate = Class(name="uml_Pseudostate")
Vertex = Class(name="Vertex")
uml_FinalState = Class(name="uml_FinalState")
State = Class(name="State")
uml_Activity = Class(name="uml_Activity")
uml_State = Class(name="uml_State")

# uml_StateMachine class attributes and methods

# Behavior class attributes and methods

# uml_Transition class attributes and methods
uml_Transition_name: Property = Property(name="name", type=StringType)
uml_Transition.attributes={uml_Transition_name}

# uml_Behavior class attributes and methods
uml_Behavior_name: Property = Property(name="name", type=StringType)
uml_Behavior.attributes={uml_Behavior_name}

# uml_Trigger class attributes and methods
uml_Trigger_name: Property = Property(name="name", type=StringType)
uml_Trigger.attributes={uml_Trigger_name}

# uml_Vertex class attributes and methods
uml_Vertex_name: Property = Property(name="name", type=StringType)
uml_Vertex.attributes={uml_Vertex_name}

# uml_Region class attributes and methods

# uml_Pseudostate class attributes and methods
uml_Pseudostate_kind: Property = Property(name="kind", type=StringType)
uml_Pseudostate.attributes={uml_Pseudostate_kind}

# Vertex class attributes and methods

# uml_FinalState class attributes and methods

# State class attributes and methods

# uml_Activity class attributes and methods

# uml_State class attributes and methods

# Relationships
region0: BinaryAssociation = BinaryAssociation(
    name="region0",
    ends={
        Property(name="uml_StateMachine", type=uml_Region, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="uml_Region", type=uml_StateMachine, multiplicity=Multiplicity(1, 1))
    }
)
effect1: BinaryAssociation = BinaryAssociation(
    name="effect1",
    ends={
        Property(name="uml_Behavior", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Transition", type=uml_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger2: BinaryAssociation = BinaryAssociation(
    name="trigger2",
    ends={
        Property(name="uml_Trigger", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Transition3", type=uml_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="uml_Vertex", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Transition5", type=uml_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
subvertex9: BinaryAssociation = BinaryAssociation(
    name="subvertex9",
    ends={
        Property(name="Vertex", type=uml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=uml_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition10: BinaryAssociation = BinaryAssociation(
    name="transition10",
    ends={
        Property(name="uml_Transition12", type=uml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Region11", type=uml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="uml_Vertex8", type=uml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_Transition7", type=uml_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
entry14: BinaryAssociation = BinaryAssociation(
    name="entry14",
    ends={
        Property(name="uml_Behavior15", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_State", type=uml_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit16: BinaryAssociation = BinaryAssociation(
    name="exit16",
    ends={
        Property(name="uml_Behavior18", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_State17", type=uml_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container13: BinaryAssociation = BinaryAssociation(
    name="container13",
    ends={
        Property(name="Region", type=uml_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=uml_Region, multiplicity=Multiplicity(0, 1))
    }
)
doActivity19: BinaryAssociation = BinaryAssociation(
    name="doActivity19",
    ends={
        Property(name="uml_Behavior21", type=uml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="uml_State20", type=uml_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_uml_StateMachine_Behavior = Generalization(general=Behavior, specific=uml_StateMachine)
gen_uml_Pseudostate_Vertex = Generalization(general=Vertex, specific=uml_Pseudostate)
gen_uml_FinalState_State = Generalization(general=State, specific=uml_FinalState)
gen_uml_Activity_Behavior = Generalization(general=Behavior, specific=uml_Activity)
gen_uml_State_Vertex = Generalization(general=Vertex, specific=uml_State)

# Domain Model
domain_model = DomainModel(
    name="uml",
    types={uml_StateMachine, Behavior, uml_Transition, uml_Behavior, uml_Trigger, uml_Vertex, uml_Region, uml_Pseudostate, Vertex, uml_FinalState, State, uml_Activity, uml_State, PseudostateKind},
    associations={region0, effect1, trigger2, target4, subvertex9, transition10, source6, entry14, exit16, container13, doActivity19},
    generalizations={gen_uml_StateMachine_Behavior, gen_uml_Pseudostate_Vertex, gen_uml_FinalState_State, gen_uml_Activity_Behavior, gen_uml_State_Vertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)