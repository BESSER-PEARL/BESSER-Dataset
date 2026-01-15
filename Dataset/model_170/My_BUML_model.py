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
PetriNet_Token = Class(name="PetriNet::Token")
PetriNet_PetriNet = Class(name="PetriNet::PetriNet")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Place = Class(name="PetriNet::Place")

# PetriNet_Token class attributes and methods

# PetriNet_PetriNet class attributes and methods

# PetriNet_Transition class attributes and methods
PetriNet_Transition_name: Property = Property(name="name", type=StringType)
PetriNet_Transition.attributes={PetriNet_Transition_name}

# PetriNet_Place class attributes and methods
PetriNet_Place_name: Property = Property(name="name", type=StringType)
PetriNet_Place.attributes={PetriNet_Place_name}

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="PetriNet_Transition", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places1: BinaryAssociation = BinaryAssociation(
    name="places1",
    ends={
        Property(name="PetriNet_Place", type=PetriNet_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNet2", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tokens3: BinaryAssociation = BinaryAssociation(
    name="tokens3",
    ends={
        Property(name="PetriNet_Token", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Place4", type=PetriNet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input5: BinaryAssociation = BinaryAssociation(
    name="input5",
    ends={
        Property(name="PetriNet_Place7", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Transition6", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
output8: BinaryAssociation = BinaryAssociation(
    name="output8",
    ends={
        Property(name="PetriNet_Place10", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Transition9", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Token, PetriNet_PetriNet, PetriNet_Transition, PetriNet_Place},
    associations={transitions0, places1, tokens3, input5, output8},
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