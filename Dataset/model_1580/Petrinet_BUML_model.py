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
ArcKindType: Enumeration = Enumeration(
    name="ArcKindType",
    literals={
            EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="read_arc")
    }
)

# Classes
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_Noeud = Class(name="petrinet::Noeud")
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_Transition = Class(name="petrinet::Transition")
Noeud = Class(name="Noeud")
petrinet_Place = Class(name="petrinet::Place")

# petrinet_PetriNet class attributes and methods
petrinet_PetriNet_name: Property = Property(name="name", type=StringType)
petrinet_PetriNet.attributes={petrinet_PetriNet_name}

# petrinet_Noeud class attributes and methods
petrinet_Noeud_name: Property = Property(name="name", type=StringType)
petrinet_Noeud.attributes={petrinet_Noeud_name}

# petrinet_Arc class attributes and methods
petrinet_Arc_name: Property = Property(name="name", type=StringType)
petrinet_Arc_arcType: Property = Property(name="arcType", type=StringType)
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc.attributes={petrinet_Arc_weight, petrinet_Arc_name, petrinet_Arc_arcType}

# petrinet_Transition class attributes and methods
petrinet_Transition_minTime: Property = Property(name="minTime", type=IntegerType)
petrinet_Transition_maxTime: Property = Property(name="maxTime", type=IntegerType)
petrinet_Transition.attributes={petrinet_Transition_minTime, petrinet_Transition_maxTime}

# Noeud class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_marking: Property = Property(name="marking", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_marking}

# Relationships
noeuds0: BinaryAssociation = BinaryAssociation(
    name="noeuds0",
    ends={
        Property(name="petrinet_Noeud", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Noeud, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="petrinet_Arc", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet2", type=petrinet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="petrinet_Noeud5", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc4", type=petrinet_Noeud, multiplicity=Multiplicity(0, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="petrinet_Noeud8", type=petrinet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Arc7", type=petrinet_Noeud, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_petrinet_Transition_Noeud = Generalization(general=Noeud, specific=petrinet_Transition)
gen_petrinet_Place_Noeud = Generalization(general=Noeud, specific=petrinet_Place)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_PetriNet, petrinet_Noeud, petrinet_Arc, petrinet_Transition, Noeud, petrinet_Place, ArcKindType},
    associations={noeuds0, arcs1, source3, target6},
    generalizations={gen_petrinet_Transition_Noeud, gen_petrinet_Place_Noeud},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)