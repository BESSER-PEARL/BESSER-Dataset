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
Element = Class(name="Element")
PetriNet_Place = Class(name="PetriNet::Place")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Arc = Class(name="PetriNet::Arc")
PetriNet_Element = Class(name="PetriNet::Element", is_abstract=True)
PetriNet_TransToPlaceArc = Class(name="PetriNet::TransToPlaceArc")
PetriNet_PlaceToTransArc = Class(name="PetriNet::PlaceToTransArc")
Arc = Class(name="Arc")

# PetriNet_PetriNet class attributes and methods

# Element class attributes and methods

# PetriNet_Place class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNet_Arc.attributes={PetriNet_Arc_weight}

# PetriNet_Element class attributes and methods
PetriNet_Element_name: Property = Property(name="name", type=StringType)
PetriNet_Element.attributes={PetriNet_Element_name}

# PetriNet_TransToPlaceArc class attributes and methods

# PetriNet_PlaceToTransArc class attributes and methods

# Arc class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="PetriNet_Place", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=PetriNet_Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="PetriNet_Transition", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet2", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming7: BinaryAssociation = BinaryAssociation(
    name="incoming7",
    ends={
        Property(name="PlaceToTransArc9", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="target8", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 9999))
    }
)
outgoing10: BinaryAssociation = BinaryAssociation(
    name="outgoing10",
    ends={
        Property(name="TransToPlaceArc12", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="source11", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 9999))
    }
)
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="PetriNet_Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet4", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="TransToPlaceArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="PlaceToTransArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(0, 9999))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="Transition", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="Place", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="Place20", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming19", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="Transition17", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing16", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
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
    types={PetriNet_PetriNet, Element, PetriNet_Place, PetriNet_Transition, PetriNet_Arc, PetriNet_Element, PetriNet_TransToPlaceArc, PetriNet_PlaceToTransArc, Arc},
    associations={places0, transitions1, incoming7, outgoing10, arcs3, incoming5, outgoing6, target14, source13, target18, source15},
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