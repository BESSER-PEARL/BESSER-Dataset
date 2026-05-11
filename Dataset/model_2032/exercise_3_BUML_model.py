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
Pseudokind: Enumeration = Enumeration(
    name="Pseudokind",
    literals={
            EnumerationLiteral(name="Initial"),
			EnumerationLiteral(name="End"),
			EnumerationLiteral(name="Exit"),
			EnumerationLiteral(name="DeepHistory"),
			EnumerationLiteral(name="ShallowHistory")
    }
)

# Classes
MySM_Statemachine = Class(name="MySM_Statemachine")
Region = Class(name="Region")
MySM_Transition = Class(name="MySM_Transition")
MySM_Action = Class(name="MySM_Action")
MySM_ComplexSate = Class(name="MySM_ComplexSate")
State = Class(name="State")
MySM_LabeledTransition = Class(name="MySM_LabeledTransition")
Transition = Class(name="Transition")
MySM_Region = Class(name="MySM_Region")
MySM_State = Class(name="MySM_State")
MySM_Pseudostate = Class(name="MySM_Pseudostate")
MySM_Vertex = Class(name="MySM_Vertex")
Vertex = Class(name="Vertex")

# MySM_Statemachine class attributes and methods

# Region class attributes and methods

# MySM_Transition class attributes and methods
MySM_Transition_tId: Property = Property(name="tId", type=StringType)
MySM_Transition.attributes={MySM_Transition_tId}

# MySM_Action class attributes and methods
MySM_Action_name: Property = Property(name="name", type=StringType)
MySM_Action.attributes={MySM_Action_name}

# MySM_ComplexSate class attributes and methods

# State class attributes and methods

# MySM_LabeledTransition class attributes and methods

# Transition class attributes and methods

# MySM_Region class attributes and methods
MySM_Region_name: Property = Property(name="name", type=StringType)
MySM_Region.attributes={MySM_Region_name}

# MySM_State class attributes and methods
MySM_State_name: Property = Property(name="name", type=StringType)
MySM_State.attributes={MySM_State_name}

# MySM_Pseudostate class attributes and methods
MySM_Pseudostate_psId: Property = Property(name="psId", type=StringType)
MySM_Pseudostate_kind: Property = Property(name="kind", type=StringType)
MySM_Pseudostate.attributes={MySM_Pseudostate_kind, MySM_Pseudostate_psId}

# MySM_Vertex class attributes and methods

# Vertex class attributes and methods

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="MySM_Transition", type=MySM_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="MySM_Statemachine", type=MySM_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actions1: BinaryAssociation = BinaryAssociation(
    name="actions1",
    ends={
        Property(name="MySM_Action", type=MySM_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="MySM_Statemachine2", type=MySM_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
region8: BinaryAssociation = BinaryAssociation(
    name="region8",
    ends={
        Property(name="MySM_Region9", type=MySM_ComplexSate, multiplicity=Multiplicity(1, 1)),
        Property(name="MySM_ComplexSate", type=MySM_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="MySM_Vertex12", type=MySM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MySM_Transition11", type=MySM_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="MySM_Vertex15", type=MySM_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MySM_Transition14", type=MySM_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
action16: BinaryAssociation = BinaryAssociation(
    name="action16",
    ends={
        Property(name="MySM_Action17", type=MySM_LabeledTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="MySM_LabeledTransition", type=MySM_Action, multiplicity=Multiplicity(1, 1))
    }
)
states3: BinaryAssociation = BinaryAssociation(
    name="states3",
    ends={
        Property(name="MySM_State", type=MySM_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="MySM_Region", type=MySM_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initial4: BinaryAssociation = BinaryAssociation(
    name="initial4",
    ends={
        Property(name="MySM_Pseudostate", type=MySM_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="MySM_Region5", type=MySM_Pseudostate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outgoings6: BinaryAssociation = BinaryAssociation(
    name="outgoings6",
    ends={
        Property(name="MySM_Transition7", type=MySM_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="MySM_Vertex", type=MySM_Transition, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_MySM_Statemachine_Region = Generalization(general=Region, specific=MySM_Statemachine)
gen_MySM_ComplexSate_State = Generalization(general=State, specific=MySM_ComplexSate)
gen_MySM_LabeledTransition_Transition = Generalization(general=Transition, specific=MySM_LabeledTransition)
gen_MySM_Pseudostate_Vertex = Generalization(general=Vertex, specific=MySM_Pseudostate)
gen_MySM_State_Vertex = Generalization(general=Vertex, specific=MySM_State)

# Domain Model
domain_model = DomainModel(
    name="MySM",
    types={MySM_Statemachine, Region, MySM_Transition, MySM_Action, MySM_ComplexSate, State, MySM_LabeledTransition, Transition, MySM_Region, MySM_State, MySM_Pseudostate, MySM_Vertex, Vertex, Pseudokind},
    associations={transitions0, actions1, region8, source10, target13, action16, states3, initial4, outgoings6},
    generalizations={gen_MySM_Statemachine_Region, gen_MySM_ComplexSate_State, gen_MySM_LabeledTransition_Transition, gen_MySM_Pseudostate_Vertex, gen_MySM_State_Vertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)