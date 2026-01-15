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
ArcKind: Enumeration = Enumeration(
    name="ArcKind",
    literals={
            EnumerationLiteral(name="INPUT"),
			EnumerationLiteral(name="OUTPUT")
    }
)

# Classes
stochasticpetrinet_PetriNet = Class(name="stochasticpetrinet::PetriNet")
stochasticpetrinet_Node = Class(name="stochasticpetrinet::Node", is_abstract=True)
stochasticpetrinet_Transition = Class(name="stochasticpetrinet::Transition", is_abstract=True)
Node = Class(name="Node")
stochasticpetrinet_Arc = Class(name="stochasticpetrinet::Arc")
stochasticpetrinet_Place = Class(name="stochasticpetrinet::Place")
stochasticpetrinet_TimedTransition = Class(name="stochasticpetrinet::TimedTransition")
Transition = Class(name="Transition")
stochasticpetrinet_ImmediateTransition = Class(name="stochasticpetrinet::ImmediateTransition")

# stochasticpetrinet_PetriNet class attributes and methods

# stochasticpetrinet_Node class attributes and methods

# stochasticpetrinet_Transition class attributes and methods

# Node class attributes and methods

# stochasticpetrinet_Arc class attributes and methods
stochasticpetrinet_Arc_kind: Property = Property(name="kind", type=StringType)
stochasticpetrinet_Arc.attributes={stochasticpetrinet_Arc_kind}

# stochasticpetrinet_Place class attributes and methods
stochasticpetrinet_Place_tokens: Property = Property(name="tokens", type=IntegerType)
stochasticpetrinet_Place.attributes={stochasticpetrinet_Place_tokens}

# stochasticpetrinet_TimedTransition class attributes and methods

# Transition class attributes and methods

# stochasticpetrinet_ImmediateTransition class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="Node", type=stochasticpetrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet", type=stochasticpetrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="Arc", type=stochasticpetrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=stochasticpetrinet_Arc, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transition2: BinaryAssociation = BinaryAssociation(
    name="transition2",
    ends={
        Property(name="Transition", type=stochasticpetrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=stochasticpetrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
place3: BinaryAssociation = BinaryAssociation(
    name="place3",
    ends={
        Property(name="stochasticpetrinet_Place", type=stochasticpetrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="stochasticpetrinet_Arc", type=stochasticpetrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
petriNet4: BinaryAssociation = BinaryAssociation(
    name="petriNet4",
    ends={
        Property(name="PetriNet", type=stochasticpetrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=stochasticpetrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_stochasticpetrinet_Transition_Node = Generalization(general=Node, specific=stochasticpetrinet_Transition)
gen_stochasticpetrinet_Place_Node = Generalization(general=Node, specific=stochasticpetrinet_Place)
gen_stochasticpetrinet_TimedTransition_Transition = Generalization(general=Transition, specific=stochasticpetrinet_TimedTransition)
gen_stochasticpetrinet_ImmediateTransition_Transition = Generalization(general=Transition, specific=stochasticpetrinet_ImmediateTransition)

# Domain Model
domain_model = DomainModel(
    name="stochasticpetrinet",
    types={stochasticpetrinet_PetriNet, stochasticpetrinet_Node, stochasticpetrinet_Transition, Node, stochasticpetrinet_Arc, stochasticpetrinet_Place, stochasticpetrinet_TimedTransition, Transition, stochasticpetrinet_ImmediateTransition, ArcKind},
    associations={nodes0, arcs1, transition2, place3, petriNet4},
    generalizations={gen_stochasticpetrinet_Transition_Node, gen_stochasticpetrinet_Place_Node, gen_stochasticpetrinet_TimedTransition_Transition, gen_stochasticpetrinet_ImmediateTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)