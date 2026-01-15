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
standardPetriNets_Transition = Class(name="standardPetriNets::Transition")
standardPetriNets_InputArc = Class(name="standardPetriNets::InputArc")
standardPetriNets_Place = Class(name="standardPetriNets::Place")
standardPetriNets_OutputArc = Class(name="standardPetriNets::OutputArc")
standardPetriNets_PetriNet = Class(name="standardPetriNets::PetriNet")

# standardPetriNets_Transition class attributes and methods
standardPetriNets_Transition_name: Property = Property(name="name", type=StringType)
standardPetriNets_Transition.attributes={standardPetriNets_Transition_name}

# standardPetriNets_InputArc class attributes and methods
standardPetriNets_InputArc_weight: Property = Property(name="weight", type=IntegerType)
standardPetriNets_InputArc.attributes={standardPetriNets_InputArc_weight}

# standardPetriNets_Place class attributes and methods
standardPetriNets_Place_numOfTokens: Property = Property(name="numOfTokens", type=IntegerType)
standardPetriNets_Place_capacity: Property = Property(name="capacity", type=IntegerType)
standardPetriNets_Place_name: Property = Property(name="name", type=StringType)
standardPetriNets_Place.attributes={standardPetriNets_Place_capacity, standardPetriNets_Place_numOfTokens, standardPetriNets_Place_name}

# standardPetriNets_OutputArc class attributes and methods
standardPetriNets_OutputArc_weight: Property = Property(name="weight", type=IntegerType)
standardPetriNets_OutputArc.attributes={standardPetriNets_OutputArc_weight}

# standardPetriNets_PetriNet class attributes and methods
standardPetriNets_PetriNet_name: Property = Property(name="name", type=StringType)
standardPetriNets_PetriNet.attributes={standardPetriNets_PetriNet_name}

# Relationships
inputArcFromPlace0: BinaryAssociation = BinaryAssociation(
    name="inputArcFromPlace0",
    ends={
        Property(name="standardPetriNets_Place", type=standardPetriNets_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="standardPetriNets_InputArc", type=standardPetriNets_Place, multiplicity=Multiplicity(0, 1))
    }
)
containsTransitions10: BinaryAssociation = BinaryAssociation(
    name="containsTransitions10",
    ends={
        Property(name="standardPetriNets_Transition12", type=standardPetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="standardPetriNets_PetriNet11", type=standardPetriNets_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsInputArcs13: BinaryAssociation = BinaryAssociation(
    name="containsInputArcs13",
    ends={
        Property(name="standardPetriNets_InputArc15", type=standardPetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="standardPetriNets_PetriNet14", type=standardPetriNets_InputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsOutputArcs16: BinaryAssociation = BinaryAssociation(
    name="containsOutputArcs16",
    ends={
        Property(name="standardPetriNets_OutputArc18", type=standardPetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="standardPetriNets_PetriNet17", type=standardPetriNets_OutputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputArcToTransition1: BinaryAssociation = BinaryAssociation(
    name="inputArcToTransition1",
    ends={
        Property(name="standardPetriNets_Transition", type=standardPetriNets_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="standardPetriNets_InputArc2", type=standardPetriNets_Transition, multiplicity=Multiplicity(0, 1))
    }
)
outputArcFromTransition3: BinaryAssociation = BinaryAssociation(
    name="outputArcFromTransition3",
    ends={
        Property(name="standardPetriNets_Transition4", type=standardPetriNets_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="standardPetriNets_OutputArc", type=standardPetriNets_Transition, multiplicity=Multiplicity(0, 1))
    }
)
outputArcToPlace5: BinaryAssociation = BinaryAssociation(
    name="outputArcToPlace5",
    ends={
        Property(name="standardPetriNets_Place7", type=standardPetriNets_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="standardPetriNets_OutputArc6", type=standardPetriNets_Place, multiplicity=Multiplicity(0, 1))
    }
)
containsPlaces8: BinaryAssociation = BinaryAssociation(
    name="containsPlaces8",
    ends={
        Property(name="standardPetriNets_Place9", type=standardPetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="standardPetriNets_PetriNet", type=standardPetriNets_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="standardPetriNets",
    types={standardPetriNets_Transition, standardPetriNets_InputArc, standardPetriNets_Place, standardPetriNets_OutputArc, standardPetriNets_PetriNet},
    associations={inputArcFromPlace0, containsTransitions10, containsInputArcs13, containsOutputArcs16, inputArcToTransition1, outputArcFromTransition3, outputArcToPlace5, containsPlaces8},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)