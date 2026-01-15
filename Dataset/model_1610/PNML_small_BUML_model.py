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
pnml_PNMLDocument = Class(name="pnml::PNMLDocument")
pnml_NetElement = Class(name="pnml::NetElement")
pnml_PlaceElement = Class(name="pnml::PlaceElement")
Element = Class(name="Element")
pnml_ArcTransition2Place = Class(name="pnml::ArcTransition2Place")
pnml_Element = Class(name="pnml::Element", is_abstract=True)
pnml_TransitionElement = Class(name="pnml::TransitionElement")
pnml_ArcPlace2Transition = Class(name="pnml::ArcPlace2Transition")

# pnml_PNMLDocument class attributes and methods
pnml_PNMLDocument_location: Property = Property(name="location", type=StringType)
pnml_PNMLDocument.attributes={pnml_PNMLDocument_location}

# pnml_NetElement class attributes and methods
pnml_NetElement_name: Property = Property(name="name", type=StringType)
pnml_NetElement.attributes={pnml_NetElement_name}

# pnml_PlaceElement class attributes and methods
pnml_PlaceElement_name: Property = Property(name="name", type=StringType)
pnml_PlaceElement_tokens: Property = Property(name="tokens", type=IntegerType)
pnml_PlaceElement.attributes={pnml_PlaceElement_tokens, pnml_PlaceElement_name}

# Element class attributes and methods

# pnml_ArcTransition2Place class attributes and methods

# pnml_Element class attributes and methods
pnml_Element_id: Property = Property(name="id", type=StringType)
pnml_Element_location: Property = Property(name="location", type=StringType)
pnml_Element.attributes={pnml_Element_location, pnml_Element_id}

# pnml_TransitionElement class attributes and methods
pnml_TransitionElement_name: Property = Property(name="name", type=StringType)
pnml_TransitionElement.attributes={pnml_TransitionElement_name}

# pnml_ArcPlace2Transition class attributes and methods

# Relationships
nets0: BinaryAssociation = BinaryAssociation(
    name="nets0",
    ends={
        Property(name="pnml_NetElement", type=pnml_PNMLDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="pnml_PNMLDocument", type=pnml_NetElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target2: BinaryAssociation = BinaryAssociation(
    name="target2",
    ends={
        Property(name="pnml_TransitionElement", type=pnml_ArcPlace2Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="pnml_ArcPlace2Transition3", type=pnml_TransitionElement, multiplicity=Multiplicity(0, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="pnml_PlaceElement5", type=pnml_ArcTransition2Place, multiplicity=Multiplicity(1, 1)),
        Property(name="pnml_ArcTransition2Place", type=pnml_PlaceElement, multiplicity=Multiplicity(0, 1))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="pnml_TransitionElement8", type=pnml_ArcTransition2Place, multiplicity=Multiplicity(1, 1)),
        Property(name="pnml_ArcTransition2Place7", type=pnml_TransitionElement, multiplicity=Multiplicity(0, 1))
    }
)
contents9: BinaryAssociation = BinaryAssociation(
    name="contents9",
    ends={
        Property(name="pnml_Element", type=pnml_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pnml_NetElement10", type=pnml_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="pnml_PlaceElement", type=pnml_ArcPlace2Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="pnml_ArcPlace2Transition", type=pnml_PlaceElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pnml_PlaceElement_Element = Generalization(general=Element, specific=pnml_PlaceElement)
gen_pnml_ArcTransition2Place_Element = Generalization(general=Element, specific=pnml_ArcTransition2Place)
gen_pnml_NetElement_Element = Generalization(general=Element, specific=pnml_NetElement)
gen_pnml_TransitionElement_Element = Generalization(general=Element, specific=pnml_TransitionElement)
gen_pnml_ArcPlace2Transition_Element = Generalization(general=Element, specific=pnml_ArcPlace2Transition)

# Domain Model
domain_model = DomainModel(
    name="pnml",
    types={pnml_PNMLDocument, pnml_NetElement, pnml_PlaceElement, Element, pnml_ArcTransition2Place, pnml_Element, pnml_TransitionElement, pnml_ArcPlace2Transition},
    associations={nets0, target2, target4, source6, contents9, source1},
    generalizations={gen_pnml_PlaceElement_Element, gen_pnml_ArcTransition2Place_Element, gen_pnml_NetElement_Element, gen_pnml_TransitionElement_Element, gen_pnml_ArcPlace2Transition_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)