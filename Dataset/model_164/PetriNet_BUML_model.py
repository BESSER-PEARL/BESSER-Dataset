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
PetriNet_Place = Class(name="PetriNet::Place")
Identifiable = Class(name="Identifiable")
PetriNet_Token = Class(name="PetriNet::Token")
PetriNet_InputArc = Class(name="PetriNet::InputArc")
PetriNet_OutputArc = Class(name="PetriNet::OutputArc")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Net = Class(name="PetriNet::Net")

# PetriNet_Place class attributes and methods
PetriNet_Place_name: Property = Property(name="name", type=StringType)
PetriNet_Place.attributes={PetriNet_Place_name}

# Identifiable class attributes and methods

# PetriNet_Token class attributes and methods

# PetriNet_InputArc class attributes and methods

# PetriNet_OutputArc class attributes and methods

# PetriNet_Transition class attributes and methods
PetriNet_Transition_name: Property = Property(name="name", type=StringType)
PetriNet_Transition.attributes={PetriNet_Transition_name}

# PetriNet_Net class attributes and methods

# Relationships
token0: BinaryAssociation = BinaryAssociation(
    name="token0",
    ends={
        Property(name="PetriNet_Token", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Place", type=PetriNet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputArc1: BinaryAssociation = BinaryAssociation(
    name="inputArc1",
    ends={
        Property(name="PetriNet_InputArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Place2", type=PetriNet_InputArc, multiplicity=Multiplicity(0, 9999))
    }
)
outputArc3: BinaryAssociation = BinaryAssociation(
    name="outputArc3",
    ends={
        Property(name="PetriNet_OutputArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Place4", type=PetriNet_OutputArc, multiplicity=Multiplicity(0, 9999))
    }
)
inputArc5: BinaryAssociation = BinaryAssociation(
    name="inputArc5",
    ends={
        Property(name="PetriNet_InputArc6", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Transition", type=PetriNet_InputArc, multiplicity=Multiplicity(0, 9999))
    }
)
outputArc7: BinaryAssociation = BinaryAssociation(
    name="outputArc7",
    ends={
        Property(name="PetriNet_OutputArc9", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Transition8", type=PetriNet_OutputArc, multiplicity=Multiplicity(0, 9999))
    }
)
place22: BinaryAssociation = BinaryAssociation(
    name="place22",
    ends={
        Property(name="PetriNet_Place23", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Net", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
token24: BinaryAssociation = BinaryAssociation(
    name="token24",
    ends={
        Property(name="PetriNet_Token26", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Net25", type=PetriNet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputArc27: BinaryAssociation = BinaryAssociation(
    name="inputArc27",
    ends={
        Property(name="PetriNet_InputArc29", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Net28", type=PetriNet_InputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputArc30: BinaryAssociation = BinaryAssociation(
    name="outputArc30",
    ends={
        Property(name="PetriNet_OutputArc32", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Net31", type=PetriNet_OutputArc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place10: BinaryAssociation = BinaryAssociation(
    name="place10",
    ends={
        Property(name="PetriNet_Place12", type=PetriNet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_InputArc11", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
transition13: BinaryAssociation = BinaryAssociation(
    name="transition13",
    ends={
        Property(name="PetriNet_Transition15", type=PetriNet_InputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_InputArc14", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
place16: BinaryAssociation = BinaryAssociation(
    name="place16",
    ends={
        Property(name="PetriNet_Place18", type=PetriNet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_OutputArc17", type=PetriNet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
transition19: BinaryAssociation = BinaryAssociation(
    name="transition19",
    ends={
        Property(name="PetriNet_Transition21", type=PetriNet_OutputArc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_OutputArc20", type=PetriNet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_PetriNet_Place_Identifiable = Generalization(general=Identifiable, specific=PetriNet_Place)
gen_PetriNet_Transition_Identifiable = Generalization(general=Identifiable, specific=PetriNet_Transition)
gen_PetriNet_Token_Identifiable = Generalization(general=Identifiable, specific=PetriNet_Token)
gen_PetriNet_Net_Identifiable = Generalization(general=Identifiable, specific=PetriNet_Net)
gen_PetriNet_InputArc_Identifiable = Generalization(general=Identifiable, specific=PetriNet_InputArc)
gen_PetriNet_OutputArc_Identifiable = Generalization(general=Identifiable, specific=PetriNet_OutputArc)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Place, Identifiable, PetriNet_Token, PetriNet_InputArc, PetriNet_OutputArc, PetriNet_Transition, PetriNet_Net},
    associations={token0, inputArc1, outputArc3, inputArc5, outputArc7, place22, token24, inputArc27, outputArc30, place10, transition13, place16, transition19},
    generalizations={gen_PetriNet_Place_Identifiable, gen_PetriNet_Transition_Identifiable, gen_PetriNet_Token_Identifiable, gen_PetriNet_Net_Identifiable, gen_PetriNet_InputArc_Identifiable, gen_PetriNet_OutputArc_Identifiable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)