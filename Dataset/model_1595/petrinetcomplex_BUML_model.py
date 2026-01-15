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
petrinet_Token = Class(name="petrinet::Token")
petrinet_Net = Class(name="petrinet::Net")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")

# petrinet_Token class attributes and methods

# petrinet_Net class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_name: Property = Property(name="name", type=StringType)
petrinet_Place_initialTokens: Property = Property(name="initialTokens", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_initialTokens, petrinet_Place_name}

# petrinet_Transition class attributes and methods
petrinet_Transition_name: Property = Property(name="name", type=StringType)
petrinet_Transition.attributes={petrinet_Transition_name}

# Relationships
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="petrinet_Net2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="petrinet_Transition", type=petrinet_Net, multiplicity=Multiplicity(1, 1))
    }
)
tokens3: BinaryAssociation = BinaryAssociation(
    name="tokens3",
    ends={
        Property(name="petrinet_Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place4", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input5: BinaryAssociation = BinaryAssociation(
    name="input5",
    ends={
        Property(name="petrinet_Place7", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition6", type=petrinet_Place, multiplicity=Multiplicity(1, 9999))
    }
)
output8: BinaryAssociation = BinaryAssociation(
    name="output8",
    ends={
        Property(name="petrinet_Place10", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition9", type=petrinet_Place, multiplicity=Multiplicity(1, 9999))
    }
)
place0: BinaryAssociation = BinaryAssociation(
    name="place0",
    ends={
        Property(name="petrinet_Place", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Net", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Token, petrinet_Net, petrinet_Place, petrinet_Transition},
    associations={transition1, tokens3, input5, output8, place0},
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