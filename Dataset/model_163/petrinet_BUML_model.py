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
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_Arc = Class(name="petrinet::Arc")
petrinet_TPArc = Class(name="petrinet::TPArc")
petrinet_PTArc = Class(name="petrinet::PTArc")
Arc = Class(name="Arc")

# petrinet_PetriNet class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_name: Property = Property(name="name", type=StringType)
petrinet_Place_token: Property = Property(name="token", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_token, petrinet_Place_name}

# petrinet_Transition class attributes and methods
petrinet_Transition_name: Property = Property(name="name", type=StringType)
petrinet_Transition.attributes={petrinet_Transition_name}

# petrinet_Arc class attributes and methods
petrinet_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_Arc.attributes={petrinet_Arc_weight}

# petrinet_TPArc class attributes and methods

# petrinet_PTArc class attributes and methods

# Arc class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinet_Place", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinet_Transition", type=petrinet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PetriNet2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing3: BinaryAssociation = BinaryAssociation(
    name="outgoing3",
    ends={
        Property(name="TPArc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petrinet_TPArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="PTArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="source5", type=petrinet_PTArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="petrinet_Transition7", type=petrinet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_PTArc", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="Place", type=petrinet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="petrinet_Place10", type=petrinet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_TPArc", type=petrinet_Place, multiplicity=Multiplicity(1, 1))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="Transition", type=petrinet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing12", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petrinet_PTArc_Arc = Generalization(general=Arc, specific=petrinet_PTArc)
gen_petrinet_TPArc_Arc = Generalization(general=Arc, specific=petrinet_TPArc)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_PetriNet, petrinet_Place, petrinet_Transition, petrinet_Arc, petrinet_TPArc, petrinet_PTArc, Arc},
    associations={places0, transitions1, outgoing3, outgoing4, target6, source8, target9, source11},
    generalizations={gen_petrinet_PTArc_Arc, gen_petrinet_TPArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)