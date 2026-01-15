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
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_PetriNetElement = Class(name="petrinet::PetriNetElement", is_abstract=True)
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
PetriNetElement = Class(name="PetriNetElement")
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Place = Class(name="petrinet::Place")
Node = Class(name="Node")
petrinet_Transition = Class(name="petrinet::Transition")

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# petrinet_PetriNetElement class attributes and methods

# petrinet_Node class attributes and methods
petrinet_Node_name: Property = Property(name="name", type=StringType)
petrinet_Node.attributes={petrinet_Node_name}

# PetriNetElement class attributes and methods

# petrinet_Arc class attributes and methods
petrinet_Arc_multiplicity: Property = Property(name="multiplicity", type=IntegerType)
petrinet_Arc_readOnly: Property = Property(name="readOnly", type=BooleanType)
petrinet_Arc.attributes={petrinet_Arc_multiplicity, petrinet_Arc_readOnly}

# petrinet_Place class attributes and methods
petrinet_Place_marking: Property = Property(name="marking", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_marking}

# Node class attributes and methods

# petrinet_Transition class attributes and methods

# Relationships
linksToPredecessor3: BinaryAssociation = BinaryAssociation(
    name="linksToPredecessor3",
    ends={
        Property(name="Arc4", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="successor", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
petriNetElements0: BinaryAssociation = BinaryAssociation(
    name="petriNetElements0",
    ends={
        Property(name="PetriNetElement", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet", type=petrinet_PetriNetElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
petriNet1: BinaryAssociation = BinaryAssociation(
    name="petriNet1",
    ends={
        Property(name="PetriNet", type=petrinet_PetriNetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetElements", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
linksToSuccessor2: BinaryAssociation = BinaryAssociation(
    name="linksToSuccessor2",
    ends={
        Property(name="Arc", type=petrinet_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="predecessor", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
predecessor5: BinaryAssociation = BinaryAssociation(
    name="predecessor5",
    ends={
        Property(name="Node", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToSuccessor", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)
successor6: BinaryAssociation = BinaryAssociation(
    name="successor6",
    ends={
        Property(name="Node7", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="linksToPredecessor", type=petrinet_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Arc_PetriNetElement = Generalization(general=PetriNetElement, specific=petrinet_Arc)
gen_petrinet_Node_PetriNetElement = Generalization(general=PetriNetElement, specific=petrinet_Node)
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_PetriNet, petrinet_PetriNetElement, petrinet_Node, PetriNetElement, petrinet_Arc, petrinet_Place, Node, petrinet_Transition},
    associations={linksToPredecessor3, petriNetElements0, petriNet1, linksToSuccessor2, predecessor5, successor6},
    generalizations={gen_petrinet_Arc_PetriNetElement, gen_petrinet_Node_PetriNetElement, gen_petrinet_Place_Node, gen_petrinet_Transition_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)