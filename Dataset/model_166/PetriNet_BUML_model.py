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
petrinet_metamodel_Element = Class(name="petrinet::metamodel::Element", is_abstract=True)
petrinet_metamodel_PetriNet = Class(name="petrinet::metamodel::PetriNet")
Element = Class(name="Element")
petrinet_metamodel_Place = Class(name="petrinet::metamodel::Place")
petrinet_metamodel_Transition = Class(name="petrinet::metamodel::Transition")
petrinet_metamodel_Arc = Class(name="petrinet::metamodel::Arc", is_abstract=True)
petrinet_metamodel_TransToPlaceArc = Class(name="petrinet::metamodel::TransToPlaceArc")
petrinet_metamodel_PlaceToTransArc = Class(name="petrinet::metamodel::PlaceToTransArc")
petrinet_metamodel_Rectangle = Class(name="petrinet::metamodel::Rectangle")
Arc = Class(name="Arc")

# petrinet_metamodel_Element class attributes and methods
petrinet_metamodel_Element_comments: Property = Property(name="comments", type=StringType)
petrinet_metamodel_Element_name: Property = Property(name="name", type=StringType)
petrinet_metamodel_Element.attributes={petrinet_metamodel_Element_name, petrinet_metamodel_Element_comments}

# petrinet_metamodel_PetriNet class attributes and methods

# Element class attributes and methods

# petrinet_metamodel_Place class attributes and methods
petrinet_metamodel_Place_radius: Property = Property(name="radius", type=IntegerType)
petrinet_metamodel_Place_fill_colour: Property = Property(name="fill_colour", type=StringType)
petrinet_metamodel_Place_coordinates: Property = Property(name="coordinates", type=IntegerType)
petrinet_metamodel_Place.attributes={petrinet_metamodel_Place_coordinates, petrinet_metamodel_Place_fill_colour, petrinet_metamodel_Place_radius}

# petrinet_metamodel_Transition class attributes and methods

# petrinet_metamodel_Arc class attributes and methods
petrinet_metamodel_Arc_weight: Property = Property(name="weight", type=IntegerType)
petrinet_metamodel_Arc.attributes={petrinet_metamodel_Arc_weight}

# petrinet_metamodel_TransToPlaceArc class attributes and methods

# petrinet_metamodel_PlaceToTransArc class attributes and methods

# petrinet_metamodel_Rectangle class attributes and methods
petrinet_metamodel_Rectangle_start_end_coordinates: Property = Property(name="start_end_coordinates", type=IntegerType)
petrinet_metamodel_Rectangle.attributes={petrinet_metamodel_Rectangle_start_end_coordinates}

# Arc class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=petrinet_metamodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet", type=petrinet_metamodel_Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=petrinet_metamodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2", type=petrinet_metamodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="petrinet_metamodel_Arc", type=petrinet_metamodel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_metamodel_PetriNet", type=petrinet_metamodel_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="TransToPlaceArc", type=petrinet_metamodel_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=petrinet_metamodel_TransToPlaceArc, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="PlaceToTransArc", type=petrinet_metamodel_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=petrinet_metamodel_PlaceToTransArc, multiplicity=Multiplicity(0, 9999))
    }
)
petrinet6: BinaryAssociation = BinaryAssociation(
    name="petrinet6",
    ends={
        Property(name="PetriNet", type=petrinet_metamodel_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=petrinet_metamodel_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
petrinet7: BinaryAssociation = BinaryAssociation(
    name="petrinet7",
    ends={
        Property(name="PetriNet8", type=petrinet_metamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=petrinet_metamodel_PetriNet, multiplicity=Multiplicity(0, 1))
    }
)
incoming9: BinaryAssociation = BinaryAssociation(
    name="incoming9",
    ends={
        Property(name="PlaceToTransArc11", type=petrinet_metamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="target10", type=petrinet_metamodel_PlaceToTransArc, multiplicity=Multiplicity(1, 9999))
    }
)
outgoing12: BinaryAssociation = BinaryAssociation(
    name="outgoing12",
    ends={
        Property(name="TransToPlaceArc14", type=petrinet_metamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="source13", type=petrinet_metamodel_TransToPlaceArc, multiplicity=Multiplicity(1, 9999))
    }
)
rectangle15: BinaryAssociation = BinaryAssociation(
    name="rectangle15",
    ends={
        Property(name="Rectangle", type=petrinet_metamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="belongs_to", type=petrinet_metamodel_Rectangle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="Place17", type=petrinet_metamodel_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=petrinet_metamodel_Place, multiplicity=Multiplicity(1, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="Transition19", type=petrinet_metamodel_PlaceToTransArc, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=petrinet_metamodel_Transition, multiplicity=Multiplicity(1, 1))
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="Transition22", type=petrinet_metamodel_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing21", type=petrinet_metamodel_Transition, multiplicity=Multiplicity(1, 1))
    }
)
target23: BinaryAssociation = BinaryAssociation(
    name="target23",
    ends={
        Property(name="Place25", type=petrinet_metamodel_TransToPlaceArc, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming24", type=petrinet_metamodel_Place, multiplicity=Multiplicity(1, 1))
    }
)
belongs_to26: BinaryAssociation = BinaryAssociation(
    name="belongs_to26",
    ends={
        Property(name="Transition27", type=petrinet_metamodel_Rectangle, multiplicity=Multiplicity(1, 1)),
        Property(name="rectangle", type=petrinet_metamodel_Transition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_petrinet_metamodel_PetriNet_Element = Generalization(general=Element, specific=petrinet_metamodel_PetriNet)
gen_petrinet_metamodel_Place_Element = Generalization(general=Element, specific=petrinet_metamodel_Place)
gen_petrinet_metamodel_Transition_Element = Generalization(general=Element, specific=petrinet_metamodel_Transition)
gen_petrinet_metamodel_PlaceToTransArc_Arc = Generalization(general=Arc, specific=petrinet_metamodel_PlaceToTransArc)
gen_petrinet_metamodel_TransToPlaceArc_Arc = Generalization(general=Arc, specific=petrinet_metamodel_TransToPlaceArc)

# Domain Model
domain_model = DomainModel(
    name="petrinet_metamodel",
    types={petrinet_metamodel_Element, petrinet_metamodel_PetriNet, Element, petrinet_metamodel_Place, petrinet_metamodel_Transition, petrinet_metamodel_Arc, petrinet_metamodel_TransToPlaceArc, petrinet_metamodel_PlaceToTransArc, petrinet_metamodel_Rectangle, Arc},
    associations={places0, transitions1, arcs3, incoming4, outgoing5, petrinet6, petrinet7, incoming9, outgoing12, rectangle15, source16, target18, source20, target23, belongs_to26},
    generalizations={gen_petrinet_metamodel_PetriNet_Element, gen_petrinet_metamodel_Place_Element, gen_petrinet_metamodel_Transition_Element, gen_petrinet_metamodel_PlaceToTransArc_Arc, gen_petrinet_metamodel_TransToPlaceArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)