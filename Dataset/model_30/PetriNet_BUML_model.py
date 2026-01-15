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
Arc = Class(name="Arc")
PetriNet_Place = Class(name="PetriNet::Place")
TransToPlaceArc = Class(name="TransToPlaceArc")
PlaceToTransArc = Class(name="PlaceToTransArc")
PetriNet = Class(name="PetriNet")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
Element = Class(name="Element")
PetriNet_Arc = Class(name="PetriNet::Arc", is_abstract=True)
Place = Class(name="Place")
Transition = Class(name="Transition")
PetriNet_TransToPlaceArc = Class(name="PetriNet::TransToPlaceArc")
PetriNet_PlaceToTransArc = Class(name="PetriNet::PlaceToTransArc")

# PetriNet_Element class attributes and methods

# Arc class attributes and methods

# PetriNet_Place class attributes and methods

# TransToPlaceArc class attributes and methods

# PlaceToTransArc class attributes and methods

# PetriNet class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_PetriNet class attributes and methods

# Element class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=StringType)
PetriNet_Arc.attributes={PetriNet_Arc_weight}

# Place class attributes and methods

# Transition class attributes and methods

# PetriNet_TransToPlaceArc class attributes and methods

# PetriNet_PlaceToTransArc class attributes and methods

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs2: BinaryAssociation = BinaryAssociation(
    name="arcs2",
    ends={
        Property(name="Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet3", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="#6", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="05", type=TransToPlaceArc, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing7: BinaryAssociation = BinaryAssociation(
    name="outgoing7",
    ends={
        Property(name="#9", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="08", type=PlaceToTransArc, multiplicity=Multiplicity(0, 9999))
    }
)
net10: BinaryAssociation = BinaryAssociation(
    name="net10",
    ends={
        Property(name="#12", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="011", type=PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
incoming13: BinaryAssociation = BinaryAssociation(
    name="incoming13",
    ends={
        Property(name="#15", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="014", type=PlaceToTransArc, multiplicity=Multiplicity(1, 9999))
    }
)
outgoing16: BinaryAssociation = BinaryAssociation(
    name="outgoing16",
    ends={
        Property(name="#18", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="017", type=TransToPlaceArc, multiplicity=Multiplicity(1, 9999))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="#", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="023", type=Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="#24", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1))
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="#27", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="026", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="#30", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="029", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="#21", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="020", type=Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_Place_Element = Generalization(general=Element, specific=PetriNet_Place)
gen_PetriNet_Transition_Element = Generalization(general=Element, specific=PetriNet_Transition)
gen_PetriNet_PetriNet_Element = Generalization(general=Element, specific=PetriNet_PetriNet)
gen_PetriNet_TransToPlaceArc_Arc = Generalization(general=Arc, specific=PetriNet_TransToPlaceArc)
gen_PetriNet_PlaceToTransArc_Arc = Generalization(general=Arc, specific=PetriNet_PlaceToTransArc)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={PetriNet_Element, Arc, PetriNet_Place, TransToPlaceArc, PlaceToTransArc, PetriNet, PetriNet_Transition, PetriNet_PetriNet, Element, PetriNet_Arc, Place, Transition, PetriNet_TransToPlaceArc, PetriNet_PlaceToTransArc},
    associations={transitions1, arcs2, incoming4, outgoing7, net10, incoming13, outgoing16, places0, target22, source25, target28, source19},
    generalizations={gen_PetriNet_Place_Element, gen_PetriNet_Transition_Element, gen_PetriNet_PetriNet_Element, gen_PetriNet_TransToPlaceArc_Arc, gen_PetriNet_PlaceToTransArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)