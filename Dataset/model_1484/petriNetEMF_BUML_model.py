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
petriNetEMF_PlaceToTransitionArc = Class(name="petriNetEMF::PlaceToTransitionArc")
petriNetEMF_TransitionToPlaceArc = Class(name="petriNetEMF::TransitionToPlaceArc")
petriNetEMF_PetriNet = Class(name="petriNetEMF::PetriNet")
Identification = Class(name="Identification")
petriNetEMF_Place = Class(name="petriNetEMF::Place")
petriNetEMF_Transition = Class(name="petriNetEMF::Transition")
petriNetEMF_Arc = Class(name="petriNetEMF::Arc", is_abstract=True)
petriNetEMF_Identification = Class(name="petriNetEMF::Identification", is_abstract=True)
Arc = Class(name="Arc")

# petriNetEMF_PlaceToTransitionArc class attributes and methods

# petriNetEMF_TransitionToPlaceArc class attributes and methods

# petriNetEMF_PetriNet class attributes and methods

# Identification class attributes and methods

# petriNetEMF_Place class attributes and methods

# petriNetEMF_Transition class attributes and methods

# petriNetEMF_Arc class attributes and methods

# petriNetEMF_Identification class attributes and methods
petriNetEMF_Identification_ID: Property = Property(name="ID", type=StringType)
petriNetEMF_Identification_name: Property = Property(name="name", type=StringType)
petriNetEMF_Identification.attributes={petriNetEMF_Identification_name, petriNetEMF_Identification_ID}

# Arc class attributes and methods

# Relationships
outgoingArcs5: BinaryAssociation = BinaryAssociation(
    name="outgoingArcs5",
    ends={
        Property(name="PlaceToTransitionArc", type=petriNetEMF_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=petriNetEMF_PlaceToTransitionArc, multiplicity=Multiplicity(0, 9999))
    }
)
incomingArcs6: BinaryAssociation = BinaryAssociation(
    name="incomingArcs6",
    ends={
        Property(name="TransitionToPlaceArc", type=petriNetEMF_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=petriNetEMF_TransitionToPlaceArc, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingArcs7: BinaryAssociation = BinaryAssociation(
    name="outgoingArcs7",
    ends={
        Property(name="TransitionToPlaceArc9", type=petriNetEMF_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="from8", type=petriNetEMF_TransitionToPlaceArc, multiplicity=Multiplicity(0, 9999))
    }
)
Places0: BinaryAssociation = BinaryAssociation(
    name="Places0",
    ends={
        Property(name="petriNetEMF_Place", type=petriNetEMF_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetEMF_PetriNet", type=petriNetEMF_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Transitions1: BinaryAssociation = BinaryAssociation(
    name="Transitions1",
    ends={
        Property(name="petriNetEMF_Transition", type=petriNetEMF_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetEMF_PetriNet2", type=petriNetEMF_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Arcs3: BinaryAssociation = BinaryAssociation(
    name="Arcs3",
    ends={
        Property(name="petriNetEMF_Arc", type=petriNetEMF_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNetEMF_PetriNet4", type=petriNetEMF_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to18: BinaryAssociation = BinaryAssociation(
    name="to18",
    ends={
        Property(name="Place20", type=petriNetEMF_TransitionToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArcs19", type=petriNetEMF_Place, multiplicity=Multiplicity(1, 1))
    }
)
incomingArcs10: BinaryAssociation = BinaryAssociation(
    name="incomingArcs10",
    ends={
        Property(name="PlaceToTransitionArc12", type=petriNetEMF_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="to11", type=petriNetEMF_PlaceToTransitionArc, multiplicity=Multiplicity(0, 9999))
    }
)
to13: BinaryAssociation = BinaryAssociation(
    name="to13",
    ends={
        Property(name="Transition", type=petriNetEMF_PlaceToTransitionArc, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingArcs", type=petriNetEMF_Transition, multiplicity=Multiplicity(1, 1))
    }
)
from14: BinaryAssociation = BinaryAssociation(
    name="from14",
    ends={
        Property(name="Place", type=petriNetEMF_PlaceToTransitionArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArcs", type=petriNetEMF_Place, multiplicity=Multiplicity(1, 1))
    }
)
from15: BinaryAssociation = BinaryAssociation(
    name="from15",
    ends={
        Property(name="Transition17", type=petriNetEMF_TransitionToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingArcs16", type=petriNetEMF_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petriNetEMF_Place_Identification = Generalization(general=Identification, specific=petriNetEMF_Place)
gen_petriNetEMF_Transition_Identification = Generalization(general=Identification, specific=petriNetEMF_Transition)
gen_petriNetEMF_PetriNet_Identification = Generalization(general=Identification, specific=petriNetEMF_PetriNet)
gen_petriNetEMF_Arc_Identification = Generalization(general=Identification, specific=petriNetEMF_Arc)
gen_petriNetEMF_PlaceToTransitionArc_Arc = Generalization(general=Arc, specific=petriNetEMF_PlaceToTransitionArc)
gen_petriNetEMF_TransitionToPlaceArc_Arc = Generalization(general=Arc, specific=petriNetEMF_TransitionToPlaceArc)

# Domain Model
domain_model = DomainModel(
    name="petriNetEMF",
    types={petriNetEMF_PlaceToTransitionArc, petriNetEMF_TransitionToPlaceArc, petriNetEMF_PetriNet, Identification, petriNetEMF_Place, petriNetEMF_Transition, petriNetEMF_Arc, petriNetEMF_Identification, Arc},
    associations={outgoingArcs5, incomingArcs6, outgoingArcs7, Places0, Transitions1, Arcs3, to18, incomingArcs10, to13, from14, from15},
    generalizations={gen_petriNetEMF_Place_Identification, gen_petriNetEMF_Transition_Identification, gen_petriNetEMF_PetriNet_Identification, gen_petriNetEMF_Arc_Identification, gen_petriNetEMF_PlaceToTransitionArc_Arc, gen_petriNetEMF_TransitionToPlaceArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)