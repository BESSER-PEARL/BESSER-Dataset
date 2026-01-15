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
petri_PetriNet = Class(name="petri::PetriNet")
petri_Node = Class(name="petri::Node", is_abstract=True)
petri_Arc = Class(name="petri::Arc", is_abstract=True)
petri_Place = Class(name="petri::Place")
Node = Class(name="Node")
petri_Transition = Class(name="petri::Transition")
petri_TPArc = Class(name="petri::TPArc")
Arc = Class(name="Arc")
petri_PTArc = Class(name="petri::PTArc")

# petri_PetriNet class attributes and methods

# petri_Node class attributes and methods
petri_Node_name: Property = Property(name="name", type=StringType)
petri_Node.attributes={petri_Node_name}

# petri_Arc class attributes and methods

# petri_Place class attributes and methods
petri_Place_tokens: Property = Property(name="tokens", type=IntegerType)
petri_Place.attributes={petri_Place_tokens}

# Node class attributes and methods

# petri_Transition class attributes and methods

# petri_TPArc class attributes and methods

# Arc class attributes and methods

# petri_PTArc class attributes and methods

# Relationships
elems0: BinaryAssociation = BinaryAssociation(
    name="elems0",
    ends={
        Property(name="petri_Node", type=petri_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_PetriNet", type=petri_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="petri_Arc", type=petri_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_PetriNet2", type=petri_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input3: BinaryAssociation = BinaryAssociation(
    name="input3",
    ends={
        Property(name="petri_Transition", type=petri_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_TPArc", type=petri_Transition, multiplicity=Multiplicity(1, 1))
    }
)
output4: BinaryAssociation = BinaryAssociation(
    name="output4",
    ends={
        Property(name="petri_Place", type=petri_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_TPArc5", type=petri_Place, multiplicity=Multiplicity(1, 1))
    }
)
input6: BinaryAssociation = BinaryAssociation(
    name="input6",
    ends={
        Property(name="petri_Place7", type=petri_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_PTArc", type=petri_Place, multiplicity=Multiplicity(1, 1))
    }
)
output8: BinaryAssociation = BinaryAssociation(
    name="output8",
    ends={
        Property(name="petri_Transition10", type=petri_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_PTArc9", type=petri_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petri_Place_Node = Generalization(general=Node, specific=petri_Place)
gen_petri_Transition_Node = Generalization(general=Node, specific=petri_Transition)
gen_petri_TPArc_Arc = Generalization(general=Arc, specific=petri_TPArc)
gen_petri_PTArc_Arc = Generalization(general=Arc, specific=petri_PTArc)

# Domain Model
domain_model = DomainModel(
    name="petri",
    types={petri_PetriNet, petri_Node, petri_Arc, petri_Place, Node, petri_Transition, petri_TPArc, Arc, petri_PTArc},
    associations={elems0, arcs1, input3, output4, input6, output8},
    generalizations={gen_petri_Place_Node, gen_petri_Transition_Node, gen_petri_TPArc_Arc, gen_petri_PTArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)