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
Player_Actor = Class(name="Player_Actor")
Dealer__automated__Actor = Class(name="Dealer__automated__Actor")
Place_Bet_UseCase = Class(name="Place_Bet_UseCase")
Split_Hand_UseCase = Class(name="Split_Hand_UseCase")
Double_Down_UseCase = Class(name="Double_Down_UseCase")
Stand_UseCase = Class(name="Stand_UseCase")
Hit_UseCase = Class(name="Hit_UseCase")
Sit_at_Table_UseCase = Class(name="Sit_at_Table_UseCase")
Leave_Table_UseCase = Class(name="Leave_Table_UseCase")
Hit_UseCase1 = Class(name="Hit_UseCase1")
Take_Chips_UseCase = Class(name="Take_Chips_UseCase")
Pay_Chips_UseCase = Class(name="Pay_Chips_UseCase")
Shuffle_Shoe_UseCase = Class(name="Shuffle_Shoe_UseCase")
Cut_Deck_UseCase = Class(name="Cut_Deck_UseCase")
Deal_UseCase = Class(name="Deal_UseCase")
Call_for_Last_Bets_UseCase = Class(name="Call_for_Last_Bets_UseCase")
Reveal_Last_Card_UseCase = Class(name="Reveal_Last_Card_UseCase")
Ask_Player_to_Cut_Deck_UseCase = Class(name="Ask_Player_to_Cut_Deck_UseCase")
Stand_UseCase1 = Class(name="Stand_UseCase1")
Blackjack = Class(name="Blackjack")
Joueur = Class(name="Joueur")
Croupier = Class(name="Croupier")
Main = Class(name="Main")
Card = Class(name="Card")

# Player_Actor class attributes and methods

# Dealer__automated__Actor class attributes and methods

# Place_Bet_UseCase class attributes and methods

# Split_Hand_UseCase class attributes and methods

# Double_Down_UseCase class attributes and methods

# Stand_UseCase class attributes and methods

# Hit_UseCase class attributes and methods

# Sit_at_Table_UseCase class attributes and methods

# Leave_Table_UseCase class attributes and methods

# Hit_UseCase1 class attributes and methods

# Take_Chips_UseCase class attributes and methods

# Pay_Chips_UseCase class attributes and methods

# Shuffle_Shoe_UseCase class attributes and methods

# Cut_Deck_UseCase class attributes and methods

# Deal_UseCase class attributes and methods

# Call_for_Last_Bets_UseCase class attributes and methods

# Reveal_Last_Card_UseCase class attributes and methods

# Ask_Player_to_Cut_Deck_UseCase class attributes and methods

# Stand_UseCase1 class attributes and methods

# Blackjack class attributes and methods
Blackjack_joueurs: Property = Property(name="joueurs", type=StringType)
Blackjack_croupier: Property = Property(name="croupier", type=Croupier)
Blackjack.attributes={Blackjack_joueurs, Blackjack_croupier}

# Joueur class attributes and methods
Joueur_main: Property = Property(name="main", type=StringType)
Joueur_nom: Property = Property(name="nom", type=StringType)
Joueur_playerbank: Property = Property(name="playerbank", type=IntegerType)
Joueur.attributes={Joueur_main, Joueur_nom, Joueur_playerbank}

# Croupier class attributes and methods
Croupier_main: Property = Property(name="main", type=StringType)
Croupier.attributes={Croupier_main}

# Main class attributes and methods
Main_cartes: Property = Property(name="cartes", type=StringType)
Main_value: Property = Property(name="value", type=IntegerType)
Main_bet: Property = Property(name="bet", type=StringType)
Main.attributes={Main_cartes, Main_bet, Main_value}

# Card class attributes and methods
Card_rank: Property = Property(name="rank", type=StringType)
Card_suit: Property = Property(name="suit", type=IntegerType)
Card.attributes={Card_suit, Card_rank}

# Relationships
Player_Place_Bet: BinaryAssociation = BinaryAssociation(
    name="Player_Place_Bet",
    ends={
        Property(name="place_Bet0", type=Place_Bet_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player1", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Split_Hand: BinaryAssociation = BinaryAssociation(
    name="Player_Split_Hand",
    ends={
        Property(name="split_Hand2", type=Split_Hand_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player3", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Double_Down: BinaryAssociation = BinaryAssociation(
    name="Player_Double_Down",
    ends={
        Property(name="double_Down4", type=Double_Down_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player5", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Stand: BinaryAssociation = BinaryAssociation(
    name="Player_Stand",
    ends={
        Property(name="stand6", type=Stand_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player7", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Hit: BinaryAssociation = BinaryAssociation(
    name="Player_Hit",
    ends={
        Property(name="hit8", type=Hit_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player9", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Sit_at_Table: BinaryAssociation = BinaryAssociation(
    name="Player_Sit_at_Table",
    ends={
        Property(name="sit_at_Table10", type=Sit_at_Table_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player11", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Cut_Deck: BinaryAssociation = BinaryAssociation(
    name="Player_Cut_Deck",
    ends={
        Property(name="cut_Deck12", type=Cut_Deck_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player13", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer__automated__Pay_Chips: BinaryAssociation = BinaryAssociation(
    name="Dealer__automated__Pay_Chips",
    ends={
        Property(name="pay_Chips14", type=Pay_Chips_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer__automated_15", type=Dealer__automated__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer__automated__Take_Chips: BinaryAssociation = BinaryAssociation(
    name="Dealer__automated__Take_Chips",
    ends={
        Property(name="take_Chips16", type=Take_Chips_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer__automated_17", type=Dealer__automated__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer__automated__Hit: BinaryAssociation = BinaryAssociation(
    name="Dealer__automated__Hit",
    ends={
        Property(name="hit18", type=Hit_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer__automated_19", type=Dealer__automated__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer__automated__Shuffle_Shoe: BinaryAssociation = BinaryAssociation(
    name="Dealer__automated__Shuffle_Shoe",
    ends={
        Property(name="shuffle_Shoe20", type=Shuffle_Shoe_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer__automated_21", type=Dealer__automated__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer__automated__Deal: BinaryAssociation = BinaryAssociation(
    name="Dealer__automated__Deal",
    ends={
        Property(name="deal22", type=Deal_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer__automated_23", type=Dealer__automated__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer__automated__Call_for_Last_Bets: BinaryAssociation = BinaryAssociation(
    name="Dealer__automated__Call_for_Last_Bets",
    ends={
        Property(name="call_for_Last_Bets24", type=Call_for_Last_Bets_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer__automated_25", type=Dealer__automated__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer__automated__Reveal_Last_Card: BinaryAssociation = BinaryAssociation(
    name="Dealer__automated__Reveal_Last_Card",
    ends={
        Property(name="reveal_Last_Card26", type=Reveal_Last_Card_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer__automated_27", type=Dealer__automated__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer__automated__Ask_Player_to_Cut_Deck: BinaryAssociation = BinaryAssociation(
    name="Dealer__automated__Ask_Player_to_Cut_Deck",
    ends={
        Property(name="ask_Player_to_Cut_Deck28", type=Ask_Player_to_Cut_Deck_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer__automated_29", type=Dealer__automated__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer__automated__Stand: BinaryAssociation = BinaryAssociation(
    name="Dealer__automated__Stand",
    ends={
        Property(name="stand30", type=Stand_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer__automated_31", type=Dealer__automated__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Hand: BinaryAssociation = BinaryAssociation(
    name="Player_Hand",
    ends={
        Property(name="hand32", type=Main, multiplicity=Multiplicity(1, 9999)),
        Property(name="player33", type=Joueur, multiplicity=Multiplicity(1, 1))
    }
)
Blackjack_Player: BinaryAssociation = BinaryAssociation(
    name="Blackjack_Player",
    ends={
        Property(name="player34", type=Joueur, multiplicity=Multiplicity(1, 9999)),
        Property(name="blackjack35", type=Blackjack, multiplicity=Multiplicity(1, 1))
    }
)
Blackjack_Dealer: BinaryAssociation = BinaryAssociation(
    name="Blackjack_Dealer",
    ends={
        Property(name="dealer36", type=Croupier, multiplicity=Multiplicity(1, 1)),
        Property(name="blackjack37", type=Blackjack, multiplicity=Multiplicity(1, 1))
    }
)
Dealer_Hand: BinaryAssociation = BinaryAssociation(
    name="Dealer_Hand",
    ends={
        Property(name="hand38", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="dealer39", type=Croupier, multiplicity=Multiplicity(1, 1))
    }
)
Card_Hand: BinaryAssociation = BinaryAssociation(
    name="Card_Hand",
    ends={
        Property(name="hand40", type=Main, multiplicity=Multiplicity(1, 1)),
        Property(name="card41", type=Card, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_459834e7_d501_4c16_af21_48a41df80190",
    types={Player_Actor, Dealer__automated__Actor, Place_Bet_UseCase, Split_Hand_UseCase, Double_Down_UseCase, Stand_UseCase, Hit_UseCase, Sit_at_Table_UseCase, Leave_Table_UseCase, Hit_UseCase1, Take_Chips_UseCase, Pay_Chips_UseCase, Shuffle_Shoe_UseCase, Cut_Deck_UseCase, Deal_UseCase, Call_for_Last_Bets_UseCase, Reveal_Last_Card_UseCase, Ask_Player_to_Cut_Deck_UseCase, Stand_UseCase1, Blackjack, Joueur, Croupier, Main, Card},
    associations={Player_Place_Bet, Player_Split_Hand, Player_Double_Down, Player_Stand, Player_Hit, Player_Sit_at_Table, Player_Cut_Deck, Dealer__automated__Pay_Chips, Dealer__automated__Take_Chips, Dealer__automated__Hit, Dealer__automated__Shuffle_Shoe, Dealer__automated__Deal, Dealer__automated__Call_for_Last_Bets, Dealer__automated__Reveal_Last_Card, Dealer__automated__Ask_Player_to_Cut_Deck, Dealer__automated__Stand, Player_Hand, Blackjack_Player, Blackjack_Dealer, Dealer_Hand, Card_Hand},
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