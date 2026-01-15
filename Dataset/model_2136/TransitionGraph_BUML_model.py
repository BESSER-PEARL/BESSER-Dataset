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
transitiongraph_TransitionGraph = Class(name="transitiongraph::TransitionGraph")
transitiongraph_State = Class(name="transitiongraph::State")
transitiongraph_Transition = Class(name="transitiongraph::Transition")

# transitiongraph_TransitionGraph class attributes and methods

# transitiongraph_State class attributes and methods
transitiongraph_State_isFinal: Property = Property(name="isFinal", type=BooleanType)
transitiongraph_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
transitiongraph_State_id: Property = Property(name="id", type=IntegerType)
transitiongraph_State.attributes={transitiongraph_State_isInitial, transitiongraph_State_isFinal, transitiongraph_State_id}

# transitiongraph_Transition class attributes and methods
transitiongraph_Transition_label: Property = Property(name="label", type=StringType)
transitiongraph_Transition_probability: Property = Property(name="probability", type=FloatType)
transitiongraph_Transition.attributes={transitiongraph_Transition_probability, transitiongraph_Transition_label}

# Relationships
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition5", type=transitiongraph_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=transitiongraph_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="State", type=transitiongraph_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=transitiongraph_State, multiplicity=Multiplicity(1, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="State8", type=transitiongraph_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=transitiongraph_State, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="transitiongraph_State", type=transitiongraph_TransitionGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="transitiongraph_TransitionGraph", type=transitiongraph_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="transitiongraph_Transition", type=transitiongraph_TransitionGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="transitiongraph_TransitionGraph2", type=transitiongraph_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing3: BinaryAssociation = BinaryAssociation(
    name="outgoing3",
    ends={
        Property(name="Transition", type=transitiongraph_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=transitiongraph_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="transitiongraph",
    types={transitiongraph_TransitionGraph, transitiongraph_State, transitiongraph_Transition},
    associations={incoming4, source6, target7, states0, transitions1, outgoing3},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)