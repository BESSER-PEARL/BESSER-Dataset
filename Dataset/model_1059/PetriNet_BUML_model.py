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
PetriNet_Element = Class(name="PetriNet_Element", is_abstract=True)
PetriNet_PetriNet = Class(name="PetriNet_PetriNet")
Element = Class(name="Element")
Place = Class(name="Place")
Transition = Class(name="Transition")
PetriNet_Place = Class(name="PetriNet_Place")
TransToPlaceArc = Class(name="TransToPlaceArc")
PlaceToTransArc = Class(name="PlaceToTransArc")
PetriNet = Class(name="PetriNet")
PetriNet_Transition = Class(name="PetriNet_Transition")
PetriNet_Arc = Class(name="PetriNet_Arc")
PetriNet_PlaceToTransArc = Class(name="PetriNet_PlaceToTransArc")
PetriNet_TransToPlaceArc = Class(name="PetriNet_TransToPlaceArc")
Arc = Class(name="Arc")

# PetriNet_Element class attributes and methods

# PetriNet_PetriNet class attributes and methods

# Element class attributes and methods

# Place class attributes and methods

# Transition class attributes and methods

# PetriNet_Place class attributes and methods

# TransToPlaceArc class attributes and methods

# PlaceToTransArc class attributes and methods

# PetriNet class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=StringType)
PetriNet_Arc.attributes={PetriNet_Arc_weight}

# PetriNet_PlaceToTransArc class attributes and methods

# PetriNet_TransToPlaceArc class attributes and methods

# Arc class attributes and methods

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
        Property(name="TransToPlaceArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=TransToPlaceArc, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="PlaceToTransArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PlaceToTransArc, multiplicity=Multiplicity(0, 9999))
    }
)
net7: BinaryAssociation = BinaryAssociation(
    name="net7",
    ends={
        Property(name="PetriNet", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Place", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
incoming8: BinaryAssociation = BinaryAssociation(
    name="incoming8",
    ends={
        Property(name="PlaceToTransArc10", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="target9", type=PlaceToTransArc, multiplicity=Multiplicity(1, 9999))
    }
)
outgoing11: BinaryAssociation = BinaryAssociation(
    name="outgoing11",
    ends={
        Property(name="TransToPlaceArc13", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="source12", type=TransToPlaceArc, multiplicity=Multiplicity(1, 9999))
    }
)
source14: BinaryAssociation = BinaryAssociation(
    name="source14",
    ends={
        Property(name="Place15", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="Transition17", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=Transition, multiplicity=Multiplicity(1, 1))
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
source18: BinaryAssociation = BinaryAssociation(
    name="source18",
    ends={
        Property(name="Transition20", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing19", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="Place23", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming22", type=Place, multiplicity=Multiplicity(1, 1))
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
    name="PrimitiveTypes",
    types={PetriNet_Element, PetriNet_PetriNet, Element, Place, Transition, PetriNet_Place, TransToPlaceArc, PlaceToTransArc, PetriNet, PetriNet_Transition, PetriNet_Arc, PetriNet_PlaceToTransArc, PetriNet_TransToPlaceArc, Arc},
    associations={places0, incoming5, outgoing6, net7, incoming8, outgoing11, source14, target16, transitions1, arcs3, source18, target21},
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