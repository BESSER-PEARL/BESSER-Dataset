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
petri_PetriNet = Class(name="petri::PetriNet")
petri_EdgeToTransition = Class(name="petri::EdgeToTransition")
petri_EdgeToPlace = Class(name="petri::EdgeToPlace")
petri_Transition = Class(name="petri::Transition")
petri_Place = Class(name="petri::Place")
petri_Edge = Class(name="petri::Edge")
Edge = Class(name="Edge")

# petri_PetriNet class attributes and methods

# petri_EdgeToTransition class attributes and methods

# petri_EdgeToPlace class attributes and methods

# petri_Transition class attributes and methods
petri_Transition_token: Property = Property(name="token", type=IntegerType)
petri_Transition.attributes={petri_Transition_token}

# petri_Place class attributes and methods
petri_Place_token: Property = Property(name="token", type=IntegerType)
petri_Place.attributes={petri_Place_token}

# petri_Edge class attributes and methods
petri_Edge_weight: Property = Property(name="weight", type=IntegerType)
petri_Edge.attributes={petri_Edge_weight}

# Edge class attributes and methods

# Relationships
out3: BinaryAssociation = BinaryAssociation(
    name="out3",
    ends={
        Property(name="petri_EdgeToTransition", type=petri_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_Place4", type=petri_EdgeToTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out5: BinaryAssociation = BinaryAssociation(
    name="out5",
    ends={
        Property(name="petri_EdgeToPlace", type=petri_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_Transition6", type=petri_EdgeToPlace, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="petri_Transition", type=petri_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_PetriNet", type=petri_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places1: BinaryAssociation = BinaryAssociation(
    name="places1",
    ends={
        Property(name="petri_Place", type=petri_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_PetriNet2", type=petri_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in7: BinaryAssociation = BinaryAssociation(
    name="in7",
    ends={
        Property(name="petri_EdgeToPlace8", type=petri_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_Place9", type=petri_EdgeToPlace, multiplicity=Multiplicity(1, 1))
    }
)
in10: BinaryAssociation = BinaryAssociation(
    name="in10",
    ends={
        Property(name="petri_Transition12", type=petri_EdgeToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_EdgeToTransition11", type=petri_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_petri_EdgeToTransition_Edge = Generalization(general=Edge, specific=petri_EdgeToTransition)
gen_petri_EdgeToPlace_Edge = Generalization(general=Edge, specific=petri_EdgeToPlace)

# Domain Model
domain_model = DomainModel(
    name="petri",
    types={petri_PetriNet, petri_EdgeToTransition, petri_EdgeToPlace, petri_Transition, petri_Place, petri_Edge, Edge},
    associations={out3, out5, transitions0, places1, in7, in10},
    generalizations={gen_petri_EdgeToTransition_Edge, gen_petri_EdgeToPlace_Edge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)