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
PetriNets_Transition = Class(name="PetriNets::Transition")
PetriNets_PetriNet = Class(name="PetriNets::PetriNet")
PetriNets_Place = Class(name="PetriNets::Place")

# PetriNets_Transition class attributes and methods
PetriNets_Transition_m_net: Method = Method(name="net", parameters={}, type=StringType)
PetriNets_Transition_m_ins: Method = Method(name="ins", parameters={}, type=StringType)
PetriNets_Transition_m_outs: Method = Method(name="outs", parameters={}, type=StringType)
PetriNets_Transition.methods={PetriNets_Transition_m_net, PetriNets_Transition_m_outs, PetriNets_Transition_m_ins}

# PetriNets_PetriNet class attributes and methods
PetriNets_PetriNet_m_places: Method = Method(name="places", parameters={}, type=StringType)
PetriNets_PetriNet_m_trans: Method = Method(name="trans", parameters={}, type=StringType)
PetriNets_PetriNet.methods={PetriNets_PetriNet_m_places, PetriNets_PetriNet_m_trans}

# PetriNets_Place class attributes and methods
PetriNets_Place_m_tokens: Method = Method(name="tokens", parameters={}, type=IntegerType)
PetriNets_Place_m_net: Method = Method(name="net", parameters={}, type=StringType)
PetriNets_Place.methods={PetriNets_Place_m_net, PetriNets_Place_m_tokens}

# Domain Model
domain_model = DomainModel(
    name="PetriNets",
    types={PetriNets_Transition, PetriNets_PetriNet, PetriNets_Place},
    associations={},
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