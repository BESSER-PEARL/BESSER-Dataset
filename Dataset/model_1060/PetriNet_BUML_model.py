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
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
PetriNet_Element = Class(name="PetriNet::Element", is_abstract=True)
Element = Class(name="Element")
Place = Class(name="Place")
Transition = Class(name="Transition")
Arc = Class(name="Arc")
PetriNet_Place = Class(name="PetriNet::Place")
TransToPlaceArc = Class(name="TransToPlaceArc")
PlaceToTransArc = Class(name="PlaceToTransArc")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Arc = Class(name="PetriNet::Arc")
PetriNet_PlaceToTransArc = Class(name="PetriNet::PlaceToTransArc")
PetriNet_TransToPlaceArc = Class(name="PetriNet::TransToPlaceArc")

# PetriNet_PetriNet class attributes and methods

# PetriNet_Element class attributes and methods
PetriNet_Element_name: Property = Property(name="name", type=StringType)
PetriNet_Element.attributes={PetriNet_Element_name}

# Element class attributes and methods

# Place class attributes and methods

# Transition class attributes and methods

# Arc class attributes and methods

# PetriNet_Place class attributes and methods

# TransToPlaceArc class attributes and methods

# PlaceToTransArc class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNet_Arc.attributes={PetriNet_Arc_weight}

# PetriNet_PlaceToTransArc class attributes and methods

# PetriNet_TransToPlaceArc class attributes and methods

# Relationships
outgoing12: BinaryAssociation = BinaryAssociation(
    name="outgoing12",
    ends={
        Property(name="14", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="013", type=TransToPlaceArc, multiplicity=Multiplicity(1, 9999))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
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
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=TransToPlaceArc, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="8", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="07", type=PlaceToTransArc, multiplicity=Multiplicity(0, 9999))
    }
)
incoming9: BinaryAssociation = BinaryAssociation(
    name="incoming9",
    ends={
        Property(name="11", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="010", type=PlaceToTransArc, multiplicity=Multiplicity(1, 9999))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="17", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="016", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="20", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="019", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
source21: BinaryAssociation = BinaryAssociation(
    name="source21",
    ends={
        Property(name="23", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="022", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="26", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="025", type=Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_PetriNet_Element = Generalization(general=Element, specific=PetriNet_PetriNet)
gen_PetriNet_Place_Element = Generalization(general=Element, specific=PetriNet_Place)
gen_PetriNet_Transition_Element = Generalization(general=Element, specific=PetriNet_Transition)
gen_PetriNet_PlaceToTransArc_Arc = Generalization(general=Arc, specific=PetriNet_PlaceToTransArc)
gen_PetriNet_TransToPlaceArc_Arc = Generalization(general=Arc, specific=PetriNet_TransToPlaceArc)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_PetriNet, PetriNet_Element, Element, Place, Transition, Arc, PetriNet_Place, TransToPlaceArc, PlaceToTransArc, PetriNet_Transition, PetriNet_Arc, PetriNet_PlaceToTransArc, PetriNet_TransToPlaceArc},
    associations={outgoing12, places0, transitions1, arcs3, incoming5, outgoing6, incoming9, source15, target18, source21, target24},
    generalizations={gen_PetriNet_PetriNet_Element, gen_PetriNet_Place_Element, gen_PetriNet_Transition_Element, gen_PetriNet_PlaceToTransArc_Arc, gen_PetriNet_TransToPlaceArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)