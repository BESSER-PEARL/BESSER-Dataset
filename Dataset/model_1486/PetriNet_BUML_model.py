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
petriNet_Place = Class(name="petriNet::Place")
GenericPlace = Class(name="GenericPlace")
petriNet_PetriNet = Class(name="petriNet::PetriNet")
petriNet_GenericPlace = Class(name="petriNet::GenericPlace", is_abstract=True)
petriNet_Transition = Class(name="petriNet::Transition")
petriNet_InputArc = Class(name="petriNet::InputArc")
petriNet_OutputArc = Class(name="petriNet::OutputArc")
petriNet_Resource = Class(name="petriNet::Resource")

# petriNet_Place class attributes and methods
petriNet_Place_capacity: Property = Property(name="capacity", type=IntegerType)
petriNet_Place.attributes={petriNet_Place_capacity}

# GenericPlace class attributes and methods

# petriNet_PetriNet class attributes and methods
petriNet_PetriNet_name: Property = Property(name="name", type=StringType)
petriNet_PetriNet.attributes={petriNet_PetriNet_name}

# petriNet_GenericPlace class attributes and methods
petriNet_GenericPlace_name: Property = Property(name="name", type=StringType)
petriNet_GenericPlace_numberOfTokens: Property = Property(name="numberOfTokens", type=IntegerType)
petriNet_GenericPlace.attributes={petriNet_GenericPlace_name, petriNet_GenericPlace_numberOfTokens}

# petriNet_Transition class attributes and methods
petriNet_Transition_name: Property = Property(name="name", type=StringType)
petriNet_Transition.attributes={petriNet_Transition_name}

# petriNet_InputArc class attributes and methods
petriNet_InputArc_weight: Property = Property(name="weight", type=IntegerType)
petriNet_InputArc.attributes={petriNet_InputArc_weight}

# petriNet_OutputArc class attributes and methods
petriNet_OutputArc_weight: Property = Property(name="weight", type=IntegerType)
petriNet_OutputArc.attributes={petriNet_OutputArc_weight}

# petriNet_Resource class attributes and methods

# Relationships
containsGenericPlaces0: BinaryAssociation = BinaryAssociation(
    name="containsGenericPlaces0",
    ends={
        Property(name="petriNet_GenericPlace", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_PetriNet", type=petriNet_GenericPlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsTransitions1: BinaryAssociation = BinaryAssociation(
    name="containsTransitions1",
    ends={
        Property(name="petriNet_Transition", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_PetriNet2", type=petriNet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsInputArcs3: BinaryAssociation = BinaryAssociation(
    name="containsInputArcs3",
    ends={
        Property(name="petriNet_InputArc", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_PetriNet4", type=petriNet_InputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsOutputArcs5: BinaryAssociation = BinaryAssociation(
    name="containsOutputArcs5",
    ends={
        Property(name="petriNet_OutputArc", type=petriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_PetriNet6", type=petriNet_OutputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InputArcFromPlace7: BinaryAssociation = BinaryAssociation(
    name="InputArcFromPlace7",
    ends={
        Property(name="petriNet_InputArc8", type=petriNet_GenericPlace, multiplicity=Multiplicity(0, 1)),
        Property(name="petriNet_GenericPlace9", type=petriNet_InputArc, multiplicity=Multiplicity(1, 1))
    }
)
InputArcToTransition10: BinaryAssociation = BinaryAssociation(
    name="InputArcToTransition10",
    ends={
        Property(name="petriNet_Transition12", type=petriNet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_InputArc11", type=petriNet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
OutputArcFromTransition13: BinaryAssociation = BinaryAssociation(
    name="OutputArcFromTransition13",
    ends={
        Property(name="petriNet_Transition15", type=petriNet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_OutputArc14", type=petriNet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
OutputArcToPlace16: BinaryAssociation = BinaryAssociation(
    name="OutputArcToPlace16",
    ends={
        Property(name="petriNet_GenericPlace18", type=petriNet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="petriNet_OutputArc17", type=petriNet_GenericPlace, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_petriNet_Place_GenericPlace = Generalization(general=GenericPlace, specific=petriNet_Place)
gen_petriNet_Resource_GenericPlace = Generalization(general=GenericPlace, specific=petriNet_Resource)

# Domain Model
domain_model = DomainModel(
    name="petriNet",
    types={petriNet_Place, GenericPlace, petriNet_PetriNet, petriNet_GenericPlace, petriNet_Transition, petriNet_InputArc, petriNet_OutputArc, petriNet_Resource},
    associations={containsGenericPlaces0, containsTransitions1, containsInputArcs3, containsOutputArcs5, InputArcFromPlace7, InputArcToTransition10, OutputArcFromTransition13, OutputArcToPlace16},
    generalizations={gen_petriNet_Place_GenericPlace, gen_petriNet_Resource_GenericPlace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)