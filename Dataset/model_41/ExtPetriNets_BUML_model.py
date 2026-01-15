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
extendedPetriNets_Transition = Class(name="extendedPetriNets::Transition")
extendedPetriNets_InputArc = Class(name="extendedPetriNets::InputArc")
extendedPetriNets_PetriNet = Class(name="extendedPetriNets::PetriNet")
extendedPetriNets_GenericPlace = Class(name="extendedPetriNets::GenericPlace", is_abstract=True)
extendedPetriNets_OutputPort = Class(name="extendedPetriNets::OutputPort")
extendedPetriNets_OutputArc = Class(name="extendedPetriNets::OutputArc")
extendedPetriNets_Place = Class(name="extendedPetriNets::Place")
GenericPlace = Class(name="GenericPlace")
extendedPetriNets_InputPort = Class(name="extendedPetriNets::InputPort")

# extendedPetriNets_Transition class attributes and methods
extendedPetriNets_Transition_name: Property = Property(name="name", type=StringType)
extendedPetriNets_Transition.attributes={extendedPetriNets_Transition_name}

# extendedPetriNets_InputArc class attributes and methods
extendedPetriNets_InputArc_weight: Property = Property(name="weight", type=IntegerType)
extendedPetriNets_InputArc.attributes={extendedPetriNets_InputArc_weight}

# extendedPetriNets_PetriNet class attributes and methods
extendedPetriNets_PetriNet_name: Property = Property(name="name", type=StringType)
extendedPetriNets_PetriNet.attributes={extendedPetriNets_PetriNet_name}

# extendedPetriNets_GenericPlace class attributes and methods
extendedPetriNets_GenericPlace_name: Property = Property(name="name", type=StringType)
extendedPetriNets_GenericPlace_capacity: Property = Property(name="capacity", type=IntegerType)
extendedPetriNets_GenericPlace_numberOfTokens: Property = Property(name="numberOfTokens", type=IntegerType)
extendedPetriNets_GenericPlace.attributes={extendedPetriNets_GenericPlace_numberOfTokens, extendedPetriNets_GenericPlace_name, extendedPetriNets_GenericPlace_capacity}

# extendedPetriNets_OutputPort class attributes and methods

# extendedPetriNets_OutputArc class attributes and methods
extendedPetriNets_OutputArc_weight: Property = Property(name="weight", type=IntegerType)
extendedPetriNets_OutputArc.attributes={extendedPetriNets_OutputArc_weight}

# extendedPetriNets_Place class attributes and methods

# GenericPlace class attributes and methods

# extendedPetriNets_InputPort class attributes and methods

# Relationships
containsTransitions1: BinaryAssociation = BinaryAssociation(
    name="containsTransitions1",
    ends={
        Property(name="extendedPetriNets_Transition", type=extendedPetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_PetriNet2", type=extendedPetriNets_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsGenericPlaces0: BinaryAssociation = BinaryAssociation(
    name="containsGenericPlaces0",
    ends={
        Property(name="extendedPetriNets_GenericPlace", type=extendedPetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_PetriNet", type=extendedPetriNets_GenericPlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
OutputArcToPlace16: BinaryAssociation = BinaryAssociation(
    name="OutputArcToPlace16",
    ends={
        Property(name="extendedPetriNets_GenericPlace18", type=extendedPetriNets_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_OutputArc17", type=extendedPetriNets_GenericPlace, multiplicity=Multiplicity(0, 1))
    }
)
containsInputArcs3: BinaryAssociation = BinaryAssociation(
    name="containsInputArcs3",
    ends={
        Property(name="extendedPetriNets_InputArc", type=extendedPetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_PetriNet4", type=extendedPetriNets_InputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsOutputArcs5: BinaryAssociation = BinaryAssociation(
    name="containsOutputArcs5",
    ends={
        Property(name="extendedPetriNets_OutputArc", type=extendedPetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_PetriNet6", type=extendedPetriNets_OutputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InputArcToTransition7: BinaryAssociation = BinaryAssociation(
    name="InputArcToTransition7",
    ends={
        Property(name="extendedPetriNets_Transition9", type=extendedPetriNets_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_InputArc8", type=extendedPetriNets_Transition, multiplicity=Multiplicity(0, 1))
    }
)
InputArcFromPlace10: BinaryAssociation = BinaryAssociation(
    name="InputArcFromPlace10",
    ends={
        Property(name="extendedPetriNets_GenericPlace12", type=extendedPetriNets_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_InputArc11", type=extendedPetriNets_GenericPlace, multiplicity=Multiplicity(0, 1))
    }
)
OutputArcFromTransition13: BinaryAssociation = BinaryAssociation(
    name="OutputArcFromTransition13",
    ends={
        Property(name="extendedPetriNets_Transition15", type=extendedPetriNets_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_OutputArc14", type=extendedPetriNets_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_extendedPetriNets_OutputPort_GenericPlace = Generalization(general=GenericPlace, specific=extendedPetriNets_OutputPort)
gen_extendedPetriNets_Place_GenericPlace = Generalization(general=GenericPlace, specific=extendedPetriNets_Place)
gen_extendedPetriNets_InputPort_GenericPlace = Generalization(general=GenericPlace, specific=extendedPetriNets_InputPort)

# Domain Model
domain_model = DomainModel(
    name="extendedPetriNets",
    types={extendedPetriNets_Transition, extendedPetriNets_InputArc, extendedPetriNets_PetriNet, extendedPetriNets_GenericPlace, extendedPetriNets_OutputPort, extendedPetriNets_OutputArc, extendedPetriNets_Place, GenericPlace, extendedPetriNets_InputPort},
    associations={containsTransitions1, containsGenericPlaces0, OutputArcToPlace16, containsInputArcs3, containsOutputArcs5, InputArcToTransition7, InputArcFromPlace10, OutputArcFromTransition13},
    generalizations={gen_extendedPetriNets_OutputPort_GenericPlace, gen_extendedPetriNets_Place_GenericPlace, gen_extendedPetriNets_InputPort_GenericPlace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)