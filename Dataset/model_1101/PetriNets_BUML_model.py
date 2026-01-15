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

# PetriNets_PetriNet class attributes and methods

# PetriNets_Place class attributes and methods
PetriNets_Place_itokens: Property = Property(name="itokens", type=IntegerType)
PetriNets_Place_bound: Property = Property(name="bound", type=IntegerType)
PetriNets_Place_m_tokens: Method = Method(name="tokens", parameters={}, type=IntegerType)
PetriNets_Place.attributes={PetriNets_Place_itokens, PetriNets_Place_bound}
PetriNets_Place.methods={PetriNets_Place_m_tokens}

# PetriNets_Transition class attributes and methods
PetriNets_Transition_priority: Property = Property(name="priority", type=FloatType)
PetriNets_Transition.attributes={PetriNets_Transition_priority}

# PetriNets_Token class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ctokens4: BinaryAssociation = BinaryAssociation(
    name="ctokens4",
    ends={
        Property(name="PetriNets_Token", type=PetriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Place", type=PetriNets_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net5: BinaryAssociation = BinaryAssociation(
    name="net5",
    ends={
        Property(name="PetriNet6", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="trans", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
ins7: BinaryAssociation = BinaryAssociation(
    name="ins7",
    ends={
        Property(name="PetriNets_Place8", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)
outs9: BinaryAssociation = BinaryAssociation(
    name="outs9",
    ends={
        Property(name="PetriNets_Place11", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition10", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)
inh12: BinaryAssociation = BinaryAssociation(
    name="inh12",
    ends={
        Property(name="PetriNets_Place14", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition13", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)
read15: BinaryAssociation = BinaryAssociation(
    name="read15",
    ends={
        Property(name="PetriNets_Place17", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition16", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
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

# Domain Model
domain_model = DomainModel(
    name="PetriNets",
    types={PetriNets_PetriNet, PetriNets_Place, PetriNets_Transition, PetriNets_Token},
    associations={places0, ctokens4, net5, ins7, outs9, inh12, read15, trans1, net3},
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