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

# Enumerations
Color: Enumeration = Enumeration(
    name="Color",
    literals={
            
    }
)

CardType: Enumeration = Enumeration(
    name="CardType",
    literals={
            
    }
)

# Classes
Player = Class(name="Player")
Board = Class(name="Board")
Card = Class(name="Card")
Pawn = Class(name="Pawn")
Dice = Class(name="Dice")

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player.attributes={Player_name}

# Board class attributes and methods

# Card class attributes and methods
Card_card: Property = Property(name="card", type=CardType)
Card.attributes={Card_card}

# Pawn class attributes and methods
Pawn_position: Property = Property(name="position", type=IntegerType)
Pawn_color: Property = Property(name="color", type=Color)
Pawn.attributes={Pawn_color, Pawn_position}

# Dice class attributes and methods
Dice_value: Property = Property(name="value", type=IntegerType)
Dice.attributes={Dice_value}

# Relationships
Player_Pawn: BinaryAssociation = BinaryAssociation(
    name="Player_Pawn",
    ends={
        Property(name="pawn0", type=Pawn, multiplicity=Multiplicity(0, 1)),
        Property(name="player1", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Player_Dice: BinaryAssociation = BinaryAssociation(
    name="Player_Dice",
    ends={
        Property(name="dice2", type=Dice, multiplicity=Multiplicity(0, 1)),
        Property(name="player3", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Board_Card: BinaryAssociation = BinaryAssociation(
    name="Board_Card",
    ends={
        Property(name="card4", type=Card, multiplicity=Multiplicity(1, 9999)),
        Property(name="board5", type=Board, multiplicity=Multiplicity(0, 1))
    }
)
Board_Player: BinaryAssociation = BinaryAssociation(
    name="Board_Player",
    ends={
        Property(name="player6", type=Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="board7", type=Board, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_48c1353b_af82_4f09_837a_78f0c1bd1cce",
    types={Player, Board, Card, Pawn, Dice, Color, CardType},
    associations={Player_Pawn, Player_Dice, Board_Card, Board_Player},
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