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
resourcePetriNet_OutputArc = Class(name="resourcePetriNet::OutputArc")
resourcePetriNet_Place = Class(name="resourcePetriNet::Place")
GenericPlace = Class(name="GenericPlace")
resourcePetriNet_PetriNet = Class(name="resourcePetriNet::PetriNet")
resourcePetriNet_GenericPlace = Class(name="resourcePetriNet::GenericPlace", is_abstract=True)
resourcePetriNet_Transition = Class(name="resourcePetriNet::Transition")
resourcePetriNet_InputArc = Class(name="resourcePetriNet::InputArc")
resourcePetriNet_Resource = Class(name="resourcePetriNet::Resource")

# resourcePetriNet_OutputArc class attributes and methods
resourcePetriNet_OutputArc_weight: Property = Property(name="weight", type=IntegerType)
resourcePetriNet_OutputArc.attributes={resourcePetriNet_OutputArc_weight}

# resourcePetriNet_Place class attributes and methods
resourcePetriNet_Place_capacity: Property = Property(name="capacity", type=IntegerType)
resourcePetriNet_Place.attributes={resourcePetriNet_Place_capacity}

# GenericPlace class attributes and methods

# resourcePetriNet_PetriNet class attributes and methods
resourcePetriNet_PetriNet_name: Property = Property(name="name", type=StringType)
resourcePetriNet_PetriNet.attributes={resourcePetriNet_PetriNet_name}

# resourcePetriNet_GenericPlace class attributes and methods
resourcePetriNet_GenericPlace_name: Property = Property(name="name", type=StringType)
resourcePetriNet_GenericPlace_numberOfTokens: Property = Property(name="numberOfTokens", type=IntegerType)
resourcePetriNet_GenericPlace.attributes={resourcePetriNet_GenericPlace_numberOfTokens, resourcePetriNet_GenericPlace_name}

# resourcePetriNet_Transition class attributes and methods
resourcePetriNet_Transition_name: Property = Property(name="name", type=StringType)
resourcePetriNet_Transition.attributes={resourcePetriNet_Transition_name}

# resourcePetriNet_InputArc class attributes and methods
resourcePetriNet_InputArc_weight: Property = Property(name="weight", type=IntegerType)
resourcePetriNet_InputArc.attributes={resourcePetriNet_InputArc_weight}

# resourcePetriNet_Resource class attributes and methods

# Relationships
containsOutputArcs5: BinaryAssociation = BinaryAssociation(
    name="containsOutputArcs5",
    ends={
        Property(name="resourcePetriNet_OutputArc", type=resourcePetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="resourcePetriNet_PetriNet6", type=resourcePetriNet_OutputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InputArcFromPlace7: BinaryAssociation = BinaryAssociation(
    name="InputArcFromPlace7",
    ends={
        Property(name="resourcePetriNet_GenericPlace9", type=resourcePetriNet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="resourcePetriNet_InputArc8", type=resourcePetriNet_GenericPlace, multiplicity=Multiplicity(0, 1))
    }
)
containsGenericPlaces0: BinaryAssociation = BinaryAssociation(
    name="containsGenericPlaces0",
    ends={
        Property(name="resourcePetriNet_GenericPlace", type=resourcePetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="resourcePetriNet_PetriNet", type=resourcePetriNet_GenericPlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsTransitions1: BinaryAssociation = BinaryAssociation(
    name="containsTransitions1",
    ends={
        Property(name="resourcePetriNet_Transition", type=resourcePetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="resourcePetriNet_PetriNet2", type=resourcePetriNet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsInputArcs3: BinaryAssociation = BinaryAssociation(
    name="containsInputArcs3",
    ends={
        Property(name="resourcePetriNet_InputArc", type=resourcePetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="resourcePetriNet_PetriNet4", type=resourcePetriNet_InputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InputArcToTransition10: BinaryAssociation = BinaryAssociation(
    name="InputArcToTransition10",
    ends={
        Property(name="resourcePetriNet_Transition12", type=resourcePetriNet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="resourcePetriNet_InputArc11", type=resourcePetriNet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
OutputArcFromTransition13: BinaryAssociation = BinaryAssociation(
    name="OutputArcFromTransition13",
    ends={
        Property(name="resourcePetriNet_Transition15", type=resourcePetriNet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="resourcePetriNet_OutputArc14", type=resourcePetriNet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
OutputArcToPlace16: BinaryAssociation = BinaryAssociation(
    name="OutputArcToPlace16",
    ends={
        Property(name="resourcePetriNet_GenericPlace18", type=resourcePetriNet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="resourcePetriNet_OutputArc17", type=resourcePetriNet_GenericPlace, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_resourcePetriNet_Place_GenericPlace = Generalization(general=GenericPlace, specific=resourcePetriNet_Place)
gen_resourcePetriNet_Resource_GenericPlace = Generalization(general=GenericPlace, specific=resourcePetriNet_Resource)

# Domain Model
domain_model = DomainModel(
    name="resourcePetriNet",
    types={resourcePetriNet_OutputArc, resourcePetriNet_Place, GenericPlace, resourcePetriNet_PetriNet, resourcePetriNet_GenericPlace, resourcePetriNet_Transition, resourcePetriNet_InputArc, resourcePetriNet_Resource},
    associations={containsOutputArcs5, InputArcFromPlace7, containsGenericPlaces0, containsTransitions1, containsInputArcs3, InputArcToTransition10, OutputArcFromTransition13, OutputArcToPlace16},
    generalizations={gen_resourcePetriNet_Place_GenericPlace, gen_resourcePetriNet_Resource_GenericPlace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)