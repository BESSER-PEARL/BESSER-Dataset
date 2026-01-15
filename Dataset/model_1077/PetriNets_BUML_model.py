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
PetriNets_PetriNet = Class(name="PetriNets::PetriNet")
PetriNets_Place = Class(name="PetriNets::Place")
PetriNets_Transition = Class(name="PetriNets::Transition")
PetriNets_Token = Class(name="PetriNets::Token")
PetriNet = Class(name="PetriNet")

# PetriNets_PetriNet class attributes and methods

# PetriNets_Place class attributes and methods
PetriNets_Place_itokens: Property = Property(name="itokens", type=IntegerType)
PetriNets_Place.attributes={PetriNets_Place_itokens}

# PetriNets_Transition class attributes and methods

# PetriNets_Token class attributes and methods

# PetriNet class attributes and methods

# Relationships
net7: BinaryAssociation = BinaryAssociation(
    name="net7",
    ends={
        Property(name="PetriNet8", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="trans", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
input9: BinaryAssociation = BinaryAssociation(
    name="input9",
    ends={
        Property(name="PetriNets_Place", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trans1: BinaryAssociation = BinaryAssociation(
    name="trans1",
    ends={
        Property(name="Transition", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=PetriNets_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="PetriNet", type=PetriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
tokens4: BinaryAssociation = BinaryAssociation(
    name="tokens4",
    ends={
        Property(name="Token", type=PetriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=PetriNets_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place5: BinaryAssociation = BinaryAssociation(
    name="place5",
    ends={
        Property(name="Place6", type=PetriNets_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="tokens", type=PetriNets_Place, multiplicity=Multiplicity(1, 1))
    }
)
output10: BinaryAssociation = BinaryAssociation(
    name="output10",
    ends={
        Property(name="PetriNets_Place12", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition11", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_PetriNets_Transition_PetriNet = Generalization(general=PetriNet, specific=PetriNets_Transition)

# Domain Model
domain_model = DomainModel(
    name="PetriNets",
    types={PetriNets_PetriNet, PetriNets_Place, PetriNets_Transition, PetriNets_Token, PetriNet},
    associations={net7, input9, places0, trans1, net3, tokens4, place5, output10},
    generalizations={gen_PetriNets_Transition_PetriNet},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)