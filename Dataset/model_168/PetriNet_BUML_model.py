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
PetriNet_Element = Class(name="PetriNet::Element", is_abstract=True)
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
Element = Class(name="Element")
Place = Class(name="Place")
PetriNet_Place = Class(name="PetriNet::Place")
TransToPlaceArc = Class(name="TransToPlaceArc")
PlaceToTransArc = Class(name="PlaceToTransArc")
PetriNet = Class(name="PetriNet")
PetriNet_Transition = Class(name="PetriNet::Transition")
Transition = Class(name="Transition")
Arc = Class(name="Arc")
PetriNet_Arc = Class(name="PetriNet::Arc")
PetriNet_PlaceToTransArc = Class(name="PetriNet::PlaceToTransArc")
PetriNet_TransToPlaceArc = Class(name="PetriNet::TransToPlaceArc")
PetriNet_NonReferencedClass = Class(name="PetriNet::NonReferencedClass")
PetriNet_WeightedArc = Class(name="PetriNet::WeightedArc")

# PetriNet_Element class attributes and methods

# PetriNet_PetriNet class attributes and methods
PetriNet_PetriNet_name: Property = Property(name="name", type=StringType)
PetriNet_PetriNet.attributes={PetriNet_PetriNet_name}

# Element class attributes and methods

# Place class attributes and methods

# PetriNet_Place class attributes and methods
PetriNet_Place_name: Property = Property(name="name", type=StringType)
PetriNet_Place.attributes={PetriNet_Place_name}

# TransToPlaceArc class attributes and methods

# PlaceToTransArc class attributes and methods

# PetriNet class attributes and methods

# PetriNet_Transition class attributes and methods
PetriNet_Transition_name: Property = Property(name="name", type=StringType)
PetriNet_Transition.attributes={PetriNet_Transition_name}

# Transition class attributes and methods

# Arc class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=StringType)
PetriNet_Arc_name: Property = Property(name="name", type=StringType)
PetriNet_Arc.attributes={PetriNet_Arc_name, PetriNet_Arc_weight}

# PetriNet_PlaceToTransArc class attributes and methods

# PetriNet_TransToPlaceArc class attributes and methods

# PetriNet_NonReferencedClass class attributes and methods

# PetriNet_WeightedArc class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="#", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=TransToPlaceArc, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="#8", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="07", type=PlaceToTransArc, multiplicity=Multiplicity(0, 9999))
    }
)
net9: BinaryAssociation = BinaryAssociation(
    name="net9",
    ends={
        Property(name="PetriNet", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Place", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet2", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet4", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="#18", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="017", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="#21", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="020", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
incoming10: BinaryAssociation = BinaryAssociation(
    name="incoming10",
    ends={
        Property(name="#12", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="011", type=PlaceToTransArc, multiplicity=Multiplicity(1, 9999))
    }
)
outgoing13: BinaryAssociation = BinaryAssociation(
    name="outgoing13",
    ends={
        Property(name="#15", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="014", type=TransToPlaceArc, multiplicity=Multiplicity(1, 9999))
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="#24", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="023", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="#27", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="026", type=Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_PetriNet_Element = Generalization(general=Element, specific=PetriNet_PetriNet)
gen_PetriNet_Place_Element = Generalization(general=Element, specific=PetriNet_Place)
gen_PetriNet_Transition_Element = Generalization(general=Element, specific=PetriNet_Transition)
gen_PetriNet_PlaceToTransArc_Arc = Generalization(general=Arc, specific=PetriNet_PlaceToTransArc)
gen_PetriNet_TransToPlaceArc_Arc = Generalization(general=Arc, specific=PetriNet_TransToPlaceArc)
gen_PetriNet_WeightedArc_Arc = Generalization(general=Arc, specific=PetriNet_WeightedArc)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PetriNet_Element, PetriNet_PetriNet, Element, Place, PetriNet_Place, TransToPlaceArc, PlaceToTransArc, PetriNet, PetriNet_Transition, Transition, Arc, PetriNet_Arc, PetriNet_PlaceToTransArc, PetriNet_TransToPlaceArc, PetriNet_NonReferencedClass, PetriNet_WeightedArc},
    associations={places0, incoming5, outgoing6, net9, transitions1, arcs3, source16, target19, incoming10, outgoing13, source22, target25},
    generalizations={gen_PetriNet_PetriNet_Element, gen_PetriNet_Place_Element, gen_PetriNet_Transition_Element, gen_PetriNet_PlaceToTransArc_Arc, gen_PetriNet_TransToPlaceArc_Arc, gen_PetriNet_WeightedArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)