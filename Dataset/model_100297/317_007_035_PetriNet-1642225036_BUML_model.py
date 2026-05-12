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
PetriNet_PetriNet = Class(name="PetriNet_PetriNet")
EObject = Class(name="EObject")
Element = Class(name="Element")
Arc = Class(name="Arc")
PetriNet_Element = Class(name="PetriNet_Element", is_abstract=True)
PetriNet_Place = Class(name="PetriNet_Place")
PetriNet_Transition = Class(name="PetriNet_Transition")
PetriNet_Arc = Class(name="PetriNet_Arc", is_abstract=True)
PetriNet_PlaceToTransition = Class(name="PetriNet_PlaceToTransition")
Place = Class(name="Place")
Transition = Class(name="Transition")
PetriNet_TransitionToPlace = Class(name="PetriNet_TransitionToPlace")

# PetriNet_PetriNet class attributes and methods

# EObject class attributes and methods

# Element class attributes and methods

# Arc class attributes and methods

# PetriNet_Element class attributes and methods
PetriNet_Element_name: Property = Property(name="name", type=StringType)
PetriNet_Element.attributes={PetriNet_Element_name}

# PetriNet_Place class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Arc class attributes and methods
PetriNet_Arc_weight: Property = Property(name="weight", type=StringType)
PetriNet_Arc_name: Property = Property(name="name", type=StringType)
PetriNet_Arc.attributes={PetriNet_Arc_weight, PetriNet_Arc_name}

# PetriNet_PlaceToTransition class attributes and methods

# Place class attributes and methods

# Transition class attributes and methods

# PetriNet_TransitionToPlace class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="Element", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to8: BinaryAssociation = BinaryAssociation(
    name="to8",
    ends={
        Property(name="PetriNet_TransitionToPlace9", type=Place, multiplicity=Multiplicity(1, 1)),
        Property(name="Place10", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1))
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="Arc", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet2", type=Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from_3: BinaryAssociation = BinaryAssociation(
    name="from_3",
    ends={
        Property(name="Place", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PlaceToTransition", type=Place, multiplicity=Multiplicity(1, 1))
    }
)
to4: BinaryAssociation = BinaryAssociation(
    name="to4",
    ends={
        Property(name="Transition", type=PetriNet_PlaceToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PlaceToTransition5", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
from_6: BinaryAssociation = BinaryAssociation(
    name="from_6",
    ends={
        Property(name="Transition7", type=PetriNet_TransitionToPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_TransitionToPlace", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_PetriNet_EObject = Generalization(general=EObject, specific=PetriNet_PetriNet)
gen_PetriNet_Place_Element = Generalization(general=Element, specific=PetriNet_Place)
gen_PetriNet_Transition_Element = Generalization(general=Element, specific=PetriNet_Transition)
gen_PetriNet_PlaceToTransition_Arc = Generalization(general=Arc, specific=PetriNet_PlaceToTransition)
gen_PetriNet_TransitionToPlace_Arc = Generalization(general=Arc, specific=PetriNet_TransitionToPlace)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_PetriNet, EObject, Element, Arc, PetriNet_Element, PetriNet_Place, PetriNet_Transition, PetriNet_Arc, PetriNet_PlaceToTransition, Place, Transition, PetriNet_TransitionToPlace},
    associations={elements0, to8, arcs1, from_3, to4, from_6},
    generalizations={gen_PetriNet_PetriNet_EObject, gen_PetriNet_Place_Element, gen_PetriNet_Transition_Element, gen_PetriNet_PlaceToTransition_Arc, gen_PetriNet_TransitionToPlace_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)