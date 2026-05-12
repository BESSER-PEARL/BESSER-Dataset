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
Theme: Enumeration = Enumeration(
    name="Theme",
    literals={
            
    }
)

CarProperties: Enumeration = Enumeration(
    name="CarProperties",
    literals={
            
    }
)

TankProperties: Enumeration = Enumeration(
    name="TankProperties",
    literals={
            
    }
)

# Classes
Deck = Class(name="Deck")
Group = Class(name="Group")
Avatar = Class(name="Avatar")
Game = Class(name="Game", is_abstract=True)
Player = Class(name="Player", is_abstract=True)
Card = Class(name="Card")
Theme1 = Class(name="Theme1")
Score = Class(name="Score")

# Deck class attributes and methods

# Group class attributes and methods
Group_name: Property = Property(name="name", type=StringType)
Group_ID: Property = Property(name="ID", type=IntegerType)
Group.attributes={Group_ID, Group_name}

# Avatar class attributes and methods

# Game class attributes and methods
Game_name: Property = Property(name="name", type=StringType)
Game.attributes={Game_name}

# Player class attributes and methods
Player_name: Property = Property(name="name", type=StringType)
Player.attributes={Player_name}

# Card class attributes and methods
Card_theme: Property = Property(name="theme", type=Theme)
Card_ID: Property = Property(name="ID", type=StringType)
Card.attributes={Card_ID, Card_theme}

# Theme1 class attributes and methods
Theme1_name: Property = Property(name="name", type=StringType)
Theme1_year: Property = Property(name="year", type=IntegerType)
Theme1.attributes={Theme1_name, Theme1_year}

# Score class attributes and methods

# Relationships
Player_Avatar: BinaryAssociation = BinaryAssociation(
    name="Player_Avatar",
    ends={
        Property(name="avatar0", type=Avatar, multiplicity=Multiplicity(0, 1)),
        Property(name="players1", type=Player, multiplicity=Multiplicity(0, 9999))
    }
)
Game_Player: BinaryAssociation = BinaryAssociation(
    name="Game_Player",
    ends={
        Property(name="players2", type=Player, multiplicity=Multiplicity(1, 9999)),
        Property(name="games3", type=Game, multiplicity=Multiplicity(0, 9999))
    }
)
Deck__Group: BinaryAssociation = BinaryAssociation(
    name="Deck__Group",
    ends={
        Property(name="group4", type=Group, multiplicity=Multiplicity(8, 8)),
        Property(name="deck5", type=Deck, multiplicity=Multiplicity(1, 9999))
    }
)
Theme_Deck: BinaryAssociation = BinaryAssociation(
    name="Theme_Deck",
    ends={
        Property(name="deck6", type=Deck, multiplicity=Multiplicity(1, 9999)),
        Property(name="theme7", type=Theme1, multiplicity=Multiplicity(1, 9999))
    }
)
Group_Card: BinaryAssociation = BinaryAssociation(
    name="Group_Card",
    ends={
        Property(name="card8", type=Card, multiplicity=Multiplicity(4, 4)),
        Property(name="group9", type=Group, multiplicity=Multiplicity(8, 8))
    }
)
Player_Score: BinaryAssociation = BinaryAssociation(
    name="Player_Score",
    ends={
        Property(name="score10", type=Score, multiplicity=Multiplicity(0, 1)),
        Property(name="player11", type=Player, multiplicity=Multiplicity(1, 2))
    }
)
Theme_Game: BinaryAssociation = BinaryAssociation(
    name="Theme_Game",
    ends={
        Property(name="game12", type=Game, multiplicity=Multiplicity(0, 1)),
        Property(name="theme13", type=Theme1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5cb8fbb5_3a60_4e6a_a329_af05bf8b494e",
    types={Deck, Group, Avatar, Game, Player, Card, Theme1, Score, Theme, CarProperties, TankProperties},
    associations={Player_Avatar, Game_Player, Deck__Group, Theme_Deck, Group_Card, Player_Score, Theme_Game},
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