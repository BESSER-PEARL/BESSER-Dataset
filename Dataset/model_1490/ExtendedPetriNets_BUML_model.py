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
extendedPetriNets_PetriNet = Class(name="extendedPetriNets::PetriNet")
extendedPetriNets_GenericPlace = Class(name="extendedPetriNets::GenericPlace", is_abstract=True)
extendedPetriNets_Transition = Class(name="extendedPetriNets::Transition")
extendedPetriNets_InputArc = Class(name="extendedPetriNets::InputArc")
extendedPetriNets_OutputArc = Class(name="extendedPetriNets::OutputArc")
extendedPetriNets_Place = Class(name="extendedPetriNets::Place")
extendedPetriNets_InputPort = Class(name="extendedPetriNets::InputPort")
extendedPetriNets_OutputPort = Class(name="extendedPetriNets::OutputPort")
GenericPlace = Class(name="GenericPlace")

# extendedPetriNets_PetriNet class attributes and methods
extendedPetriNets_PetriNet_name: Property = Property(name="name", type=StringType)
extendedPetriNets_PetriNet.attributes={extendedPetriNets_PetriNet_name}

# extendedPetriNets_GenericPlace class attributes and methods
extendedPetriNets_GenericPlace_name: Property = Property(name="name", type=StringType)
extendedPetriNets_GenericPlace_capacity: Property = Property(name="capacity", type=IntegerType)
extendedPetriNets_GenericPlace_numberOfTokens: Property = Property(name="numberOfTokens", type=IntegerType)
extendedPetriNets_GenericPlace.attributes={extendedPetriNets_GenericPlace_name, extendedPetriNets_GenericPlace_numberOfTokens, extendedPetriNets_GenericPlace_capacity}

# extendedPetriNets_Transition class attributes and methods
extendedPetriNets_Transition_name: Property = Property(name="name", type=StringType)
extendedPetriNets_Transition.attributes={extendedPetriNets_Transition_name}

# extendedPetriNets_InputArc class attributes and methods
extendedPetriNets_InputArc_weight: Property = Property(name="weight", type=IntegerType)
extendedPetriNets_InputArc.attributes={extendedPetriNets_InputArc_weight}

# extendedPetriNets_OutputArc class attributes and methods
extendedPetriNets_OutputArc_weight: Property = Property(name="weight", type=IntegerType)
extendedPetriNets_OutputArc.attributes={extendedPetriNets_OutputArc_weight}

# extendedPetriNets_Place class attributes and methods

# extendedPetriNets_InputPort class attributes and methods

# extendedPetriNets_OutputPort class attributes and methods

# GenericPlace class attributes and methods

# Relationships
containsGenericPlaces0: BinaryAssociation = BinaryAssociation(
    name="containsGenericPlaces0",
    ends={
        Property(name="extendedPetriNets_GenericPlace", type=extendedPetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_PetriNet", type=extendedPetriNets_GenericPlace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsTransitions1: BinaryAssociation = BinaryAssociation(
    name="containsTransitions1",
    ends={
        Property(name="extendedPetriNets_Transition", type=extendedPetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_PetriNet2", type=extendedPetriNets_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
        Property(name="extendedPetriNets_Place", type=extendedPetriNets_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_InputArc11", type=extendedPetriNets_Place, multiplicity=Multiplicity(0, 1))
    }
)
InputArcFromInputPort12: BinaryAssociation = BinaryAssociation(
    name="InputArcFromInputPort12",
    ends={
        Property(name="extendedPetriNets_InputPort", type=extendedPetriNets_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_InputArc13", type=extendedPetriNets_InputPort, multiplicity=Multiplicity(0, 1))
    }
)
OutputArcFromTransition14: BinaryAssociation = BinaryAssociation(
    name="OutputArcFromTransition14",
    ends={
        Property(name="extendedPetriNets_Transition16", type=extendedPetriNets_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_OutputArc15", type=extendedPetriNets_Transition, multiplicity=Multiplicity(0, 1))
    }
)
OutputArcToPlace17: BinaryAssociation = BinaryAssociation(
    name="OutputArcToPlace17",
    ends={
        Property(name="extendedPetriNets_Place19", type=extendedPetriNets_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_OutputArc18", type=extendedPetriNets_Place, multiplicity=Multiplicity(0, 1))
    }
)
OutputArcToOutputPort20: BinaryAssociation = BinaryAssociation(
    name="OutputArcToOutputPort20",
    ends={
        Property(name="extendedPetriNets_OutputPort", type=extendedPetriNets_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedPetriNets_OutputArc21", type=extendedPetriNets_OutputPort, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_extendedPetriNets_OutputPort_GenericPlace = Generalization(general=GenericPlace, specific=extendedPetriNets_OutputPort)
gen_extendedPetriNets_InputPort_GenericPlace = Generalization(general=GenericPlace, specific=extendedPetriNets_InputPort)
gen_extendedPetriNets_Place_GenericPlace = Generalization(general=GenericPlace, specific=extendedPetriNets_Place)

# Domain Model
domain_model = DomainModel(
    name="extendedPetriNets",
    types={extendedPetriNets_PetriNet, extendedPetriNets_GenericPlace, extendedPetriNets_Transition, extendedPetriNets_InputArc, extendedPetriNets_OutputArc, extendedPetriNets_Place, extendedPetriNets_InputPort, extendedPetriNets_OutputPort, GenericPlace},
    associations={containsGenericPlaces0, containsTransitions1, containsInputArcs3, containsOutputArcs5, InputArcToTransition7, InputArcFromPlace10, InputArcFromInputPort12, OutputArcFromTransition14, OutputArcToPlace17, OutputArcToOutputPort20},
    generalizations={gen_extendedPetriNets_OutputPort_GenericPlace, gen_extendedPetriNets_InputPort_GenericPlace, gen_extendedPetriNets_Place_GenericPlace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)