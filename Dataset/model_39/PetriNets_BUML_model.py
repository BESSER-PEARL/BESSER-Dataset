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
PetriNets_Place = Class(name="PetriNets::Place")
PetriNets_PetriNet = Class(name="PetriNets::PetriNet")
PetriNets_Transition = Class(name="PetriNets::Transition")
PetriNets_InputArc = Class(name="PetriNets::InputArc")
PetriNets_OutputArc = Class(name="PetriNets::OutputArc")

# PetriNets_Place class attributes and methods
PetriNets_Place_name: Property = Property(name="name", type=StringType)
PetriNets_Place_capacity: Property = Property(name="capacity", type=IntegerType)
PetriNets_Place_numberOfTokens: Property = Property(name="numberOfTokens", type=IntegerType)
PetriNets_Place.attributes={PetriNets_Place_name, PetriNets_Place_numberOfTokens, PetriNets_Place_capacity}

# PetriNets_PetriNet class attributes and methods
PetriNets_PetriNet_name: Property = Property(name="name", type=StringType)
PetriNets_PetriNet.attributes={PetriNets_PetriNet_name}

# PetriNets_Transition class attributes and methods
PetriNets_Transition_name: Property = Property(name="name", type=StringType)
PetriNets_Transition.attributes={PetriNets_Transition_name}

# PetriNets_InputArc class attributes and methods
PetriNets_InputArc_weight: Property = Property(name="weight", type=IntegerType)
PetriNets_InputArc.attributes={PetriNets_InputArc_weight}

# PetriNets_OutputArc class attributes and methods
PetriNets_OutputArc_weight: Property = Property(name="weight", type=IntegerType)
PetriNets_OutputArc.attributes={PetriNets_OutputArc_weight}

# Relationships
containsPlaces0: BinaryAssociation = BinaryAssociation(
    name="containsPlaces0",
    ends={
        Property(name="PetriNets_Place", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_PetriNet", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsTransitions1: BinaryAssociation = BinaryAssociation(
    name="containsTransitions1",
    ends={
        Property(name="PetriNets_Transition", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_PetriNet2", type=PetriNets_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsInputArcs3: BinaryAssociation = BinaryAssociation(
    name="containsInputArcs3",
    ends={
        Property(name="PetriNets_InputArc", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_PetriNet4", type=PetriNets_InputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsOutputArcs5: BinaryAssociation = BinaryAssociation(
    name="containsOutputArcs5",
    ends={
        Property(name="PetriNets_OutputArc", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_PetriNet6", type=PetriNets_OutputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
OutputArcFromTransition13: BinaryAssociation = BinaryAssociation(
    name="OutputArcFromTransition13",
    ends={
        Property(name="PetriNets_OutputArc14", type=PetriNets_Transition, multiplicity=Multiplicity(0, 1)),
        Property(name="PetriNets_Transition15", type=PetriNets_OutputArc, multiplicity=Multiplicity(1, 1))
    }
)
InputArcFromPlace7: BinaryAssociation = BinaryAssociation(
    name="InputArcFromPlace7",
    ends={
        Property(name="PetriNets_Place9", type=PetriNets_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_InputArc8", type=PetriNets_Place, multiplicity=Multiplicity(0, 1))
    }
)
InputArcToTransition10: BinaryAssociation = BinaryAssociation(
    name="InputArcToTransition10",
    ends={
        Property(name="PetriNets_Transition12", type=PetriNets_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_InputArc11", type=PetriNets_Transition, multiplicity=Multiplicity(0, 1))
    }
)
OutputArcToPlace16: BinaryAssociation = BinaryAssociation(
    name="OutputArcToPlace16",
    ends={
        Property(name="PetriNets_Place18", type=PetriNets_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_OutputArc17", type=PetriNets_Place, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PetriNets",
    types={PetriNets_Place, PetriNets_PetriNet, PetriNets_Transition, PetriNets_InputArc, PetriNets_OutputArc},
    associations={containsPlaces0, containsTransitions1, containsInputArcs3, containsOutputArcs5, OutputArcFromTransition13, InputArcFromPlace7, InputArcToTransition10, OutputArcToPlace16},
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