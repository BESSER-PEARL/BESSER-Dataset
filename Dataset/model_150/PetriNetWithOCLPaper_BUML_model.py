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
PetriNetModel_PetriNet = Class(name="PetriNetModel::PetriNet")
PetriNetModel_Transition = Class(name="PetriNetModel::Transition")
PetriNetModel_ArcPT = Class(name="PetriNetModel::ArcPT")
PetriNetModel_ArcTP = Class(name="PetriNetModel::ArcTP")
PetriNetModel_Place = Class(name="PetriNetModel::Place")

# PetriNetModel_PetriNet class attributes and methods
PetriNetModel_PetriNet_name: Property = Property(name="name", type=StringType)
PetriNetModel_PetriNet.attributes={PetriNetModel_PetriNet_name}

# PetriNetModel_Transition class attributes and methods
PetriNetModel_Transition_name: Property = Property(name="name", type=StringType)
PetriNetModel_Transition.attributes={PetriNetModel_Transition_name}

# PetriNetModel_ArcPT class attributes and methods
PetriNetModel_ArcPT_inscription: Property = Property(name="inscription", type=StringType)
PetriNetModel_ArcPT.attributes={PetriNetModel_ArcPT_inscription}

# PetriNetModel_ArcTP class attributes and methods
PetriNetModel_ArcTP_inscription: Property = Property(name="inscription", type=StringType)
PetriNetModel_ArcTP.attributes={PetriNetModel_ArcTP_inscription}

# PetriNetModel_Place class attributes and methods
PetriNetModel_Place_name: Property = Property(name="name", type=StringType)
PetriNetModel_Place_token: Property = Property(name="token", type=StringType)
PetriNetModel_Place.attributes={PetriNetModel_Place_name, PetriNetModel_Place_token}

# Relationships
transition0: BinaryAssociation = BinaryAssociation(
    name="transition0",
    ends={
        Property(name="PetriNetModel_Transition", type=PetriNetModel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_PetriNet", type=PetriNetModel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preArc7: BinaryAssociation = BinaryAssociation(
    name="preArc7",
    ends={
        Property(name="PetriNetModel_ArcPT9", type=PetriNetModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_Transition8", type=PetriNetModel_ArcPT, multiplicity=Multiplicity(0, 9999))
    }
)
postArc10: BinaryAssociation = BinaryAssociation(
    name="postArc10",
    ends={
        Property(name="PetriNetModel_ArcTP12", type=PetriNetModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_Transition11", type=PetriNetModel_ArcTP, multiplicity=Multiplicity(0, 9999))
    }
)
transition13: BinaryAssociation = BinaryAssociation(
    name="transition13",
    ends={
        Property(name="PetriNetModel_Transition15", type=PetriNetModel_ArcPT, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_ArcPT14", type=PetriNetModel_Transition, multiplicity=Multiplicity(0, 1))
    }
)
arcPT1: BinaryAssociation = BinaryAssociation(
    name="arcPT1",
    ends={
        Property(name="PetriNetModel_ArcPT", type=PetriNetModel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_PetriNet2", type=PetriNetModel_ArcPT, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcTP3: BinaryAssociation = BinaryAssociation(
    name="arcTP3",
    ends={
        Property(name="PetriNetModel_ArcTP", type=PetriNetModel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_PetriNet4", type=PetriNetModel_ArcTP, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place5: BinaryAssociation = BinaryAssociation(
    name="place5",
    ends={
        Property(name="PetriNetModel_Place", type=PetriNetModel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_PetriNet6", type=PetriNetModel_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place16: BinaryAssociation = BinaryAssociation(
    name="place16",
    ends={
        Property(name="PetriNetModel_Place18", type=PetriNetModel_ArcPT, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_ArcPT17", type=PetriNetModel_Place, multiplicity=Multiplicity(0, 1))
    }
)
place19: BinaryAssociation = BinaryAssociation(
    name="place19",
    ends={
        Property(name="PetriNetModel_Place21", type=PetriNetModel_ArcTP, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_ArcTP20", type=PetriNetModel_Place, multiplicity=Multiplicity(0, 1))
    }
)
transition22: BinaryAssociation = BinaryAssociation(
    name="transition22",
    ends={
        Property(name="PetriNetModel_Transition24", type=PetriNetModel_ArcTP, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_ArcTP23", type=PetriNetModel_Transition, multiplicity=Multiplicity(0, 1))
    }
)
preArc25: BinaryAssociation = BinaryAssociation(
    name="preArc25",
    ends={
        Property(name="PetriNetModel_ArcTP27", type=PetriNetModel_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_Place26", type=PetriNetModel_ArcTP, multiplicity=Multiplicity(0, 9999))
    }
)
postArc28: BinaryAssociation = BinaryAssociation(
    name="postArc28",
    ends={
        Property(name="PetriNetModel_ArcPT30", type=PetriNetModel_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_Place29", type=PetriNetModel_ArcPT, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PetriNetModel",
    types={PetriNetModel_PetriNet, PetriNetModel_Transition, PetriNetModel_ArcPT, PetriNetModel_ArcTP, PetriNetModel_Place},
    associations={transition0, preArc7, postArc10, transition13, arcPT1, arcTP3, place5, place16, place19, transition22, preArc25, postArc28},
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