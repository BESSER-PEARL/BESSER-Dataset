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
NamedElement = Class(name="NamedElement")
petrinet_Place = Class(name="petrinet::Place")
petrinet_PetriNet = Class(name="petrinet::PetriNet")
petrinet_PTArc = Class(name="petrinet::PTArc")
petrinet_TPArc = Class(name="petrinet::TPArc")
petrinet_Token = Class(name="petrinet::Token")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_Arc = Class(name="petrinet::Arc", is_abstract=True)
petrinet_NamedElement = Class(name="petrinet::NamedElement")
Arc = Class(name="Arc")

# NamedElement class attributes and methods

# petrinet_Place class attributes and methods

# petrinet_PetriNet class attributes and methods

# petrinet_PTArc class attributes and methods

# petrinet_TPArc class attributes and methods

# petrinet_Token class attributes and methods

# petrinet_Transition class attributes and methods

# petrinet_Arc class attributes and methods
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc.attributes={petrinet_Arc_weight}

# petrinet_NamedElement class attributes and methods
petrinet_NamedElement_name: Property = Property(name="name", type=StringType)
petrinet_NamedElement.attributes={petrinet_NamedElement_name}

# Arc class attributes and methods

# Relationships
net0: BinaryAssociation = BinaryAssociation(
    name="net0",
    ends={
        Property(name="PetriNet", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
outArcs1: BinaryAssociation = BinaryAssociation(
    name="outArcs1",
    ends={
        Property(name="PTArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petrinet_PTArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inArcs2: BinaryAssociation = BinaryAssociation(
    name="inArcs2",
    ends={
        Property(name="TPArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petrinet_TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
tokens3: BinaryAssociation = BinaryAssociation(
    name="tokens3",
    ends={
        Property(name="Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inArcs6: BinaryAssociation = BinaryAssociation(
    name="inArcs6",
    ends={
        Property(name="PTArc8", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="target7", type=petrinet_PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
outArcs9: BinaryAssociation = BinaryAssociation(
    name="outArcs9",
    ends={
        Property(name="TPArc11", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="source10", type=petrinet_TPArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places12: BinaryAssociation = BinaryAssociation(
    name="places12",
    ends={
        Property(name="Place", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions13: BinaryAssociation = BinaryAssociation(
    name="transitions13",
    ends={
        Property(name="Transition", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net14", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="Place16", type=petrinet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outArcs", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
net4: BinaryAssociation = BinaryAssociation(
    name="net4",
    ends={
        Property(name="PetriNet5", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="Transition21", type=petrinet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outArcs20", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="Place24", type=petrinet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="inArcs23", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
place25: BinaryAssociation = BinaryAssociation(
    name="place25",
    ends={
        Property(name="Place26", type=petrinet_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="tokens", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="Transition18", type=petrinet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="inArcs", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_Place_NamedElement = Generalization(general=NamedElement, specific=petrinet_Place)
gen_petrinet_Transition_NamedElement = Generalization(general=NamedElement, specific=petrinet_Transition)
gen_petrinet_PTArc_Arc = Generalization(general=Arc, specific=petrinet_PTArc)
gen_petrinet_TPArc_Arc = Generalization(general=Arc, specific=petrinet_TPArc)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={NamedElement, petrinet_Place, petrinet_PetriNet, petrinet_PTArc, petrinet_TPArc, petrinet_Token, petrinet_Transition, petrinet_Arc, petrinet_NamedElement, Arc},
    associations={net0, outArcs1, inArcs2, tokens3, inArcs6, outArcs9, places12, transitions13, source15, net4, source19, target22, place25, target17},
    generalizations={gen_petrinet_Place_NamedElement, gen_petrinet_Transition_NamedElement, gen_petrinet_PTArc_Arc, gen_petrinet_TPArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)