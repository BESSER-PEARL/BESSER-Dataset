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
PetriNet_Arc = Class(name="PetriNet::Arc", is_abstract=True)
PetriNet_PlaceToTransArc = Class(name="PetriNet::PlaceToTransArc")
Arc = Class(name="Arc")
PetriNet_TransToPlaceArc = Class(name="PetriNet::TransToPlaceArc")
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
PetriNet_Place = Class(name="PetriNet::Place")
PetriNet_Transition = Class(name="PetriNet::Transition")

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNet_Arc.attributes={PetriNet_Arc_weight}

# PetriNet_PlaceToTransArc class attributes and methods

# Arc class attributes and methods

# PetriNet_TransToPlaceArc class attributes and methods

# PetriNet_PetriNet class attributes and methods

# PetriNet_Place class attributes and methods

# PetriNet_Transition class attributes and methods

# Relationships
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="PetriNet_Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet4", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="PetriNet_Place6", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PlaceToTransArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="PetriNet_Transition9", type=PetriNet_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PlaceToTransArc8", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="PetriNet_Transition11", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_TransToPlaceArc", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="PetriNet_Place14", type=PetriNet_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_TransToPlaceArc13", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="PetriNet_Place", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="PetriNet_Transition", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet2", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PetriNet_PlaceToTransArc_Arc = Generalization(general=Arc, specific=PetriNet_PlaceToTransArc)
gen_PetriNet_TransToPlaceArc_Arc = Generalization(general=Arc, specific=PetriNet_TransToPlaceArc)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Arc, PetriNet_PlaceToTransArc, Arc, PetriNet_TransToPlaceArc, PetriNet_PetriNet, PetriNet_Place, PetriNet_Transition},
    associations={arcs3, source5, target7, source10, target12, places0, transitions1},
    generalizations={gen_PetriNet_PlaceToTransArc_Arc, gen_PetriNet_TransToPlaceArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)