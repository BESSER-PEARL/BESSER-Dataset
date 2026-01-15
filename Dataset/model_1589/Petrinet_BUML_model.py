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
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_PNGraph = Class(name="petrinet::PNGraph")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Node = Class(name="petrinet::Node", is_abstract=True)
Node = Class(name="Node")

# petrinet_Transition class attributes and methods
petrinet_Transition_id: Property = Property(name="id", type=StringType)
petrinet_Transition.attributes={petrinet_Transition_id}

# petrinet_PNGraph class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_id: Property = Property(name="id", type=StringType)
petrinet_Place_markings: Property = Property(name="markings", type=StringType)
petrinet_Place.attributes={petrinet_Place_id, petrinet_Place_markings}

# petrinet_Arc class attributes and methods
petrinet_Arc_w: Property = Property(name="w", type=StringType)
petrinet_Arc.attributes={petrinet_Arc_w}

# petrinet_Node class attributes and methods

# Node class attributes and methods

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinet_Transition", type=petrinet_PNGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PNGraph2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinet_Place", type=petrinet_PNGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PNGraph", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="petrinet_Arc", type=petrinet_PNGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PNGraph4", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from5: BinaryAssociation = BinaryAssociation(
    name="from5",
    ends={
        Property(name="petrinet_Node", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc6", type=petrinet_Node, multiplicity=Multiplicity(0, 1))
    }
)
to7: BinaryAssociation = BinaryAssociation(
    name="to7",
    ends={
        Property(name="petrinet_Node9", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc8", type=petrinet_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_petrinet_Place_Node = Generalization(general=Node, specific=petrinet_Place)
gen_petrinet_Transition_Node = Generalization(general=Node, specific=petrinet_Transition)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Transition, petrinet_PNGraph, petrinet_Place, petrinet_Arc, petrinet_Node, Node},
    associations={transitions1, places0, arcs3, from5, to7},
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