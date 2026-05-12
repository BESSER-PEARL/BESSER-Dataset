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
Dealer_Actor = Class(name="Dealer_Actor")
Blackjack_Hit_UseCase = Class(name="Blackjack_Hit_UseCase")
Blackjack_Deal_UseCase = Class(name="Blackjack_Deal_UseCase")
Blackjack_Check_Win_Condition_UseCase = Class(name="Blackjack_Check_Win_Condition_UseCase")
Blackjack_Stay_UseCase = Class(name="Blackjack_Stay_UseCase")
Blackjack_Split_UseCase = Class(name="Blackjack_Split_UseCase")
Blackjack_Double_Down_UseCase = Class(name="Blackjack_Double_Down_UseCase")
Blackjack_Bet_UseCase = Class(name="Blackjack_Bet_UseCase")
Blackjack_Start_Game_UseCase = Class(name="Blackjack_Start_Game_UseCase")
Blackjack_Play_Again_UseCase = Class(name="Blackjack_Play_Again_UseCase")
Blackjack_Exit_UseCase = Class(name="Blackjack_Exit_UseCase")
BlackJack = Class(name="BlackJack")
Card = Class(name="Card")
BlackJackDriver = Class(name="BlackJackDriver")
Deck = Class(name="Deck")
BlackJackPlayer = Class(name="BlackJackPlayer")

# Player_Actor class attributes and methods

# Dealer_Actor class attributes and methods

# Blackjack_Hit_UseCase class attributes and methods

# Blackjack_Deal_UseCase class attributes and methods

# Blackjack_Check_Win_Condition_UseCase class attributes and methods

# Blackjack_Stay_UseCase class attributes and methods

# Blackjack_Split_UseCase class attributes and methods

# Blackjack_Double_Down_UseCase class attributes and methods

# Blackjack_Bet_UseCase class attributes and methods

# Blackjack_Start_Game_UseCase class attributes and methods

# Blackjack_Play_Again_UseCase class attributes and methods

# Blackjack_Exit_UseCase class attributes and methods

# BlackJack class attributes and methods
BlackJack_handCount: Property = Property(name="handCount", type=IntegerType)
BlackJack_bet: Property = Property(name="bet", type=IntegerType)
BlackJack_money: Property = Property(name="money", type=IntegerType)
BlackJack_deck: Property = Property(name="deck", type=Deck)
BlackJack_dealersHand: Property = Property(name="dealersHand", type=BlackJackPlayer)
BlackJack_playersHand: Property = Property(name="playersHand", type=BlackJackPlayer)
BlackJack.attributes={BlackJack_dealersHand, BlackJack_deck, BlackJack_playersHand, BlackJack_handCount, BlackJack_money, BlackJack_bet}

# Card class attributes and methods
Card_value: Property = Property(name="value", type=IntegerType)
Card_suit: Property = Property(name="suit", type=StringType)
Card_faceValue: Property = Property(name="faceValue", type=StringType)
Card.attributes={Card_faceValue, Card_value, Card_suit}

# BlackJackDriver class attributes and methods

# Deck class attributes and methods
Deck_cardsUsed: Property = Property(name="cardsUsed", type=IntegerType)
Deck_deck: Property = Property(name="deck", type=Card)
Deck.attributes={Deck_cardsUsed, Deck_deck}

# BlackJackPlayer class attributes and methods
BlackJackPlayer_cardCount: Property = Property(name="cardCount", type=IntegerType)
BlackJackPlayer_cards__: Property = Property(name="cards__", type=Card)
BlackJackPlayer_MaxNumCards: Property = Property(name="MaxNumCards", type=IntegerType)
BlackJackPlayer.attributes={BlackJackPlayer_MaxNumCards, BlackJackPlayer_cardCount, BlackJackPlayer_cards__}

# Relationships
Player_Stay: BinaryAssociation = BinaryAssociation(
    name="Player_Stay",
    ends={
        Property(name="stay0", type=Blackjack_Stay_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player1", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Stay_Dealer: BinaryAssociation = BinaryAssociation(
    name="Stay_Dealer",
    ends={
        Property(name="dealer2", type=Dealer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="stay3", type=Blackjack_Stay_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Player_Start_Game: BinaryAssociation = BinaryAssociation(
    name="Player_Start_Game",
    ends={
        Property(name="start_Game4", type=Blackjack_Start_Game_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player5", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Bet: BinaryAssociation = BinaryAssociation(
    name="Player_Bet",
    ends={
        Property(name="bet6", type=Blackjack_Bet_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player7", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Deal: BinaryAssociation = BinaryAssociation(
    name="Dealer_Deal",
    ends={
        Property(name="deal8", type=Blackjack_Deal_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer9", type=Dealer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Play_Again: BinaryAssociation = BinaryAssociation(
    name="Player_Play_Again",
    ends={
        Property(name="play_Again10", type=Blackjack_Play_Again_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player11", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Check_Win_Condition: BinaryAssociation = BinaryAssociation(
    name="Dealer_Check_Win_Condition",
    ends={
        Property(name="check_Win_Condition12", type=Blackjack_Check_Win_Condition_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer13", type=Dealer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Double_Down: BinaryAssociation = BinaryAssociation(
    name="Player_Double_Down",
    ends={
        Property(name="double_Down14", type=Blackjack_Double_Down_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player15", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Split: BinaryAssociation = BinaryAssociation(
    name="Player_Split",
    ends={
        Property(name="split16", type=Blackjack_Split_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player17", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Player_Exit: BinaryAssociation = BinaryAssociation(
    name="Player_Exit",
    ends={
        Property(name="exit18", type=Blackjack_Exit_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player19", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Hit_Dealer: BinaryAssociation = BinaryAssociation(
    name="Hit_Dealer",
    ends={
        Property(name="dealer20", type=Dealer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="hit21", type=Blackjack_Hit_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Player_Hit: BinaryAssociation = BinaryAssociation(
    name="Player_Hit",
    ends={
        Property(name="hit22", type=Blackjack_Hit_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="player23", type=Player_Actor, multiplicity=Multiplicity(0, 1))
    }
)
BlackJack_Deck: BinaryAssociation = BinaryAssociation(
    name="BlackJack_Deck",
    ends={
        Property(name="deck224", type=Deck, multiplicity=Multiplicity(1, 1)),
        Property(name="blackJack25", type=BlackJack, multiplicity=Multiplicity(1, 1))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card26", type=Card, multiplicity=Multiplicity(1, 52)),
        Property(name="deck27", type=Deck, multiplicity=Multiplicity(1, 1))
    }
)
BlackJack_BlackJackPlayer: BinaryAssociation = BinaryAssociation(
    name="BlackJack_BlackJackPlayer",
    ends={
        Property(name="blackJackPlayer28", type=BlackJackPlayer, multiplicity=Multiplicity(2, 2)),
        Property(name="blackJack29", type=BlackJack, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_wLtqgEwdEeeu8_4LH_yuyg",
    types={Player_Actor, Dealer_Actor, Blackjack_Hit_UseCase, Blackjack_Deal_UseCase, Blackjack_Check_Win_Condition_UseCase, Blackjack_Stay_UseCase, Blackjack_Split_UseCase, Blackjack_Double_Down_UseCase, Blackjack_Bet_UseCase, Blackjack_Start_Game_UseCase, Blackjack_Play_Again_UseCase, Blackjack_Exit_UseCase, BlackJack, Card, BlackJackDriver, Deck, BlackJackPlayer},
    associations={Player_Stay, Stay_Dealer, Player_Start_Game, Player_Bet, Dealer_Deal, Player_Play_Again, Dealer_Check_Win_Condition, Player_Double_Down, Player_Split, Player_Exit, Hit_Dealer, Player_Hit, BlackJack_Deck, Deck_Card, BlackJack_BlackJackPlayer},
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