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
petrinet_Place = Class(name="petrinet_Place")
Node = Class(name="Node")
petrinet_PetriNet = Class(name="petrinet_PetriNet")
petrinet_Node = Class(name="petrinet_Node")
petrinet_Arc = Class(name="petrinet_Arc")
petrinet_Transition = Class(name="petrinet_Transition")

# petrinet_Place class attributes and methods
petrinet_Place_nbJetons: Property = Property(name="nbJetons", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_nbJetons}

# Node class attributes and methods

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# petrinet_Arc class attributes and methods
petrinet_Arc_poids: Property = Property(name="poids", type=IntegerType)
petrinet_Arc_readArc: Property = Property(name="readArc", type=BooleanType)
petrinet_Arc.attributes={petrinet_Arc_poids, petrinet_Arc_readArc}

# petrinet_Transition class attributes and methods

# Relationships
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="petrinet_Node8", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc7", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="petrinet_Node", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arc1: BinaryAssociation = BinaryAssociation(
    name="arc1",
    ends={
        Property(name="petrinet_Arc", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet2", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="petrinet_Node5", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc4", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Place, Node, petrinet_PetriNet, petrinet_Node, petrinet_Arc, petrinet_Transition},
    associations={source6, node0, arc1, target3},
    generalizations={gen_petrinet_Place_Node, gen_petrinet_Transition_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)