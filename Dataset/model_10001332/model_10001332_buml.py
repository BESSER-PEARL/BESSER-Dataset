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
CardGame = Class(name="CardGame")
Cards = Class(name="Cards")

# CardGame class attributes and methods
CardGame_CardNumber: Property = Property(name="CardNumber", type=IntegerType)
CardGame_suit: Property = Property(name="suit", type=StringType)
CardGame.attributes={CardGame_suit, CardGame_CardNumber}

# Cards class attributes and methods
Cards_card: Property = Property(name="card", type=CardGame)
Cards_attribute2: Property = Property(name="attribute2", type=IntegerType)
Cards_attribute3: Property = Property(name="attribute3", type=StringType)
Cards.attributes={Cards_attribute2, Cards_card, Cards_attribute3}

# Relationships
Cards_CardGame: BinaryAssociation = BinaryAssociation(
    name="Cards_CardGame",
    ends={
        Property(name="cardGame0", type=CardGame, multiplicity=Multiplicity(0, 1)),
        Property(name="cards1", type=Cards, multiplicity=Multiplicity(1, 52))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0dBTQPPEEee2hpeWh535Sw",
    types={CardGame, Cards},
    associations={Cards_CardGame},
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