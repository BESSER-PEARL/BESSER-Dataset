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
petrinet101_Place = Class(name="petrinet101::Place")
Node = Class(name="Node")
petrinet101_Token = Class(name="petrinet101::Token")
petrinet101_Petrinet = Class(name="petrinet101::Petrinet")
petrinet101_Node = Class(name="petrinet101::Node", is_abstract=True)
petrinet101_Arc = Class(name="petrinet101::Arc")
petrinet101_Transition = Class(name="petrinet101::Transition")

# petrinet101_Place class attributes and methods

# Node class attributes and methods

# petrinet101_Token class attributes and methods

# petrinet101_Petrinet class attributes and methods

# petrinet101_Node class attributes and methods

# petrinet101_Arc class attributes and methods

# petrinet101_Transition class attributes and methods

# Relationships
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="petrinet101_Arc", type=petrinet101_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet101_Petrinet2", type=petrinet101_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens3: BinaryAssociation = BinaryAssociation(
    name="tokens3",
    ends={
        Property(name="petrinet101_Token", type=petrinet101_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet101_Place", type=petrinet101_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="petrinet101_Node", type=petrinet101_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet101_Petrinet", type=petrinet101_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="petrinet101_Node6", type=petrinet101_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet101_Arc5", type=petrinet101_Node, multiplicity=Multiplicity(1, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="petrinet101_Node9", type=petrinet101_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet101_Arc8", type=petrinet101_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet101_Place_Node = Generalization(general=Node, specific=petrinet101_Place)
gen_petrinet101_Transition_Node = Generalization(general=Node, specific=petrinet101_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet101",
    types={petrinet101_Place, Node, petrinet101_Token, petrinet101_Petrinet, petrinet101_Node, petrinet101_Arc, petrinet101_Transition},
    associations={arcs1, tokens3, nodes0, source4, target7},
    generalizations={gen_petrinet101_Place_Node, gen_petrinet101_Transition_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)