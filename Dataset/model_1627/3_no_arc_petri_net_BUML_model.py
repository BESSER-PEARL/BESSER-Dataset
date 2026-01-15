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
petri_NamedElement = Class(name="petri::NamedElement", is_abstract=True)
petri_Place = Class(name="petri::Place")
NamedElement = Class(name="NamedElement")
petri_Transition = Class(name="petri::Transition")

# petri_PetriNet class attributes and methods

# petri_NamedElement class attributes and methods
petri_NamedElement_name: Property = Property(name="name", type=StringType)
petri_NamedElement.attributes={petri_NamedElement_name}

# petri_Place class attributes and methods
petri_Place_tokens: Property = Property(name="tokens", type=IntegerType)
petri_Place.attributes={petri_Place_tokens}

# NamedElement class attributes and methods

# petri_Transition class attributes and methods

# Relationships
elems0: BinaryAssociation = BinaryAssociation(
    name="elems0",
    ends={
        Property(name="petri_NamedElement", type=petri_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_PetriNet", type=petri_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in1: BinaryAssociation = BinaryAssociation(
    name="in1",
    ends={
        Property(name="petri_Place", type=petri_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_Transition", type=petri_Place, multiplicity=Multiplicity(0, 9999))
    }
)
out2: BinaryAssociation = BinaryAssociation(
    name="out2",
    ends={
        Property(name="petri_Place4", type=petri_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_Transition3", type=petri_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_petri_Place_NamedElement = Generalization(general=NamedElement, specific=petri_Place)
gen_petri_Transition_NamedElement = Generalization(general=NamedElement, specific=petri_Transition)

# Domain Model
domain_model = DomainModel(
    name="petri",
    types={petri_PetriNet, petri_NamedElement, petri_Place, NamedElement, petri_Transition},
    associations={elems0, in1, out2},
    generalizations={gen_petri_Place_NamedElement, gen_petri_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)