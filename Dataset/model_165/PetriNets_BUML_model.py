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
PetriNets_Arc = Class(name="PetriNets::Arc", is_abstract=True)
PetriNets_Token = Class(name="PetriNets::Token")
PetriNets_ArcPT = Class(name="PetriNets::ArcPT")
Arc = Class(name="Arc")
PetriNets_ArcTP = Class(name="PetriNets::ArcTP")

# PetriNets_PetriNet class attributes and methods

# PetriNets_Place class attributes and methods
PetriNets_Place_itokens: Property = Property(name="itokens", type=IntegerType)
PetriNets_Place_bound: Property = Property(name="bound", type=IntegerType)
PetriNets_Place_m_tokens: Method = Method(name="tokens", parameters={}, type=IntegerType)
PetriNets_Place.attributes={PetriNets_Place_bound, PetriNets_Place_itokens}
PetriNets_Place.methods={PetriNets_Place_m_tokens}

# PetriNets_Transition class attributes and methods
PetriNets_Transition_priority: Property = Property(name="priority", type=FloatType)
PetriNets_Transition_m_inputs: Method = Method(name="inputs", parameters={}, type=StringType)
PetriNets_Transition_m_outputs: Method = Method(name="outputs", parameters={}, type=StringType)
PetriNets_Transition.attributes={PetriNets_Transition_priority}
PetriNets_Transition.methods={PetriNets_Transition_m_outputs, PetriNets_Transition_m_inputs}

# PetriNets_Arc class attributes and methods
PetriNets_Arc_weight: Property = Property(name="weight", type=IntegerType)
PetriNets_Arc.attributes={PetriNets_Arc_weight}

# PetriNets_Token class attributes and methods

# PetriNets_ArcPT class attributes and methods

# Arc class attributes and methods

# PetriNets_ArcTP class attributes and methods

# Relationships
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
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="PetriNets_Arc", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_PetriNet", type=PetriNets_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ctokens5: BinaryAssociation = BinaryAssociation(
    name="ctokens5",
    ends={
        Property(name="PetriNets_Token", type=PetriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Place", type=PetriNets_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from6: BinaryAssociation = BinaryAssociation(
    name="from6",
    ends={
        Property(name="PetriNets_Place7", type=PetriNets_ArcPT, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_ArcPT", type=PetriNets_Place, multiplicity=Multiplicity(1, 1))
    }
)
to8: BinaryAssociation = BinaryAssociation(
    name="to8",
    ends={
        Property(name="PetriNets_Transition", type=PetriNets_ArcPT, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_ArcPT9", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1))
    }
)
net4: BinaryAssociation = BinaryAssociation(
    name="net4",
    ends={
        Property(name="PetriNet", type=PetriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
net15: BinaryAssociation = BinaryAssociation(
    name="net15",
    ends={
        Property(name="PetriNet16", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="trans", type=PetriNets_PetriNet, multiplicity=Multiplicity(1, 1))
    }
)
ins17: BinaryAssociation = BinaryAssociation(
    name="ins17",
    ends={
        Property(name="PetriNets_Place19", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition18", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)
outs20: BinaryAssociation = BinaryAssociation(
    name="outs20",
    ends={
        Property(name="PetriNets_Place22", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition21", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)
inh23: BinaryAssociation = BinaryAssociation(
    name="inh23",
    ends={
        Property(name="PetriNets_Place25", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition24", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)
from10: BinaryAssociation = BinaryAssociation(
    name="from10",
    ends={
        Property(name="PetriNets_Transition11", type=PetriNets_ArcTP, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_ArcTP", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1))
    }
)
to12: BinaryAssociation = BinaryAssociation(
    name="to12",
    ends={
        Property(name="PetriNets_Place14", type=PetriNets_ArcTP, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_ArcTP13", type=PetriNets_Place, multiplicity=Multiplicity(1, 1))
    }
)
read26: BinaryAssociation = BinaryAssociation(
    name="read26",
    ends={
        Property(name="PetriNets_Place28", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition27", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)
reset29: BinaryAssociation = BinaryAssociation(
    name="reset29",
    ends={
        Property(name="PetriNets_Place31", type=PetriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNets_Transition30", type=PetriNets_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_PetriNets_ArcPT_Arc = Generalization(general=Arc, specific=PetriNets_ArcPT)
gen_PetriNets_ArcTP_Arc = Generalization(general=Arc, specific=PetriNets_ArcTP)

# Domain Model
domain_model = DomainModel(
    name="PetriNets",
    types={PetriNets_PetriNet, PetriNets_Place, PetriNets_Transition, PetriNets_Arc, PetriNets_Token, PetriNets_ArcPT, Arc, PetriNets_ArcTP},
    associations={places0, trans1, arcs3, ctokens5, from6, to8, net4, net15, ins17, outs20, inh23, from10, to12, read26, reset29},
    generalizations={gen_PetriNets_ArcPT_Arc, gen_PetriNets_ArcTP_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)