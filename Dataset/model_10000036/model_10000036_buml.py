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
GameView = Class(name="GameView")
BasePlayer = Class(name="BasePlayer", is_abstract=True)
User_Actor = Class(name="User_Actor")
UseCase_UseCase = Class(name="UseCase_UseCase")
JLabel = Class(name="JLabel")
Player = Class(name="Player")
Dealer = Class(name="Dealer")
PlayerView = Class(name="PlayerView")
BlackjackGame = Class(name="BlackjackGame")
Deck = Class(name="Deck")
Hand = Class(name="Hand")
Profile = Class(name="Profile")
GameLauncher = Class(name="GameLauncher")
LoginView = Class(name="LoginView")
Card = Class(name="Card")
Strategy = Class(name="Strategy")
JButton = Class(name="JButton")

# GameView class attributes and methods
GameView_bet: Property = Property(name="bet", type=JLabel)
GameView_dealButton: Property = Property(name="dealButton", type=JButton)
GameView_hitButton: Property = Property(name="hitButton", type=JButton)
GameView_standButton: Property = Property(name="standButton", type=JButton)
GameView_splitButton: Property = Property(name="splitButton", type=JButton)
GameView_doubleButton: Property = Property(name="doubleButton", type=JButton)
GameView_showStrategy: Property = Property(name="showStrategy", type=BooleanType)
GameView.attributes={GameView_bet, GameView_dealButton, GameView_standButton, GameView_hitButton, GameView_showStrategy, GameView_splitButton, GameView_doubleButton}

# BasePlayer class attributes and methods
BasePlayer_isBusted: Property = Property(name="isBusted", type=BooleanType)
BasePlayer.attributes={BasePlayer_isBusted}

# User_Actor class attributes and methods

# UseCase_UseCase class attributes and methods

# JLabel class attributes and methods

# Player class attributes and methods
Player_hand: Property = Property(name="hand", type=Hand)
Player_profile: Property = Property(name="profile", type=Profile)
Player_money: Property = Property(name="money", type=IntegerType)
Player.attributes={Player_hand, Player_profile, Player_money}

# Dealer class attributes and methods
Dealer_hand: Property = Property(name="hand", type=Hand)
Dealer_cardTotalLimit: Property = Property(name="cardTotalLimit", type=IntegerType)
Dealer.attributes={Dealer_hand, Dealer_cardTotalLimit}

# PlayerView class attributes and methods
PlayerView_cardLabels: Property = Property(name="cardLabels", type=JLabel)
PlayerView_cardTotal: Property = Property(name="cardTotal", type=JLabel)
PlayerView_busted: Property = Property(name="busted", type=JLabel)
PlayerView_moneyBox: Property = Property(name="moneyBox", type=JLabel)
PlayerView_status: Property = Property(name="status", type=JLabel)
PlayerView_player: Property = Property(name="player", type=BasePlayer)
PlayerView.attributes={PlayerView_moneyBox, PlayerView_player, PlayerView_cardTotal, PlayerView_cardLabels, PlayerView_status, PlayerView_busted}

# BlackjackGame class attributes and methods
BlackjackGame_deck: Property = Property(name="deck", type=Deck)
BlackjackGame_dealer: Property = Property(name="dealer", type=Dealer)
BlackjackGame_player: Property = Property(name="player", type=Player)
BlackjackGame_bet: Property = Property(name="bet", type=IntegerType)
BlackjackGame.attributes={BlackjackGame_player, BlackjackGame_dealer, BlackjackGame_deck, BlackjackGame_bet}

# Deck class attributes and methods
Deck_cards: Property = Property(name="cards", type=Card)
Deck.attributes={Deck_cards}

# Hand class attributes and methods
Hand_cards: Property = Property(name="cards", type=Card)
Hand_total: Property = Property(name="total", type=IntegerType)
Hand.attributes={Hand_total, Hand_cards}

# Profile class attributes and methods
Profile_username: Property = Property(name="username", type=StringType)
Profile_money: Property = Property(name="money", type=IntegerType)
Profile.attributes={Profile_username, Profile_money}

# GameLauncher class attributes and methods
GameLauncher_blackjack: Property = Property(name="blackjack", type=BlackjackGame)
GameLauncher_login: Property = Property(name="login", type=LoginView)
GameLauncher.attributes={GameLauncher_login, GameLauncher_blackjack}

# LoginView class attributes and methods
LoginView_user: Property = Property(name="user", type=Profile)
LoginView.attributes={LoginView_user}

# Card class attributes and methods
Card_name: Property = Property(name="name", type=StringType)
Card_avatar: Property = Property(name="avatar", type=StringType)
Card_valueSoft: Property = Property(name="valueSoft", type=StringType)
Card_valueHard: Property = Property(name="valueHard", type=StringType)
Card_suit: Property = Property(name="suit", type=StringType)
Card_rank: Property = Property(name="rank", type=StringType)
Card_Count: Property = Property(name="Count", type=IntegerType)
Card.attributes={Card_rank, Card_name, Card_avatar, Card_suit, Card_valueHard, Card_valueSoft, Card_Count}

# Strategy class attributes and methods
Strategy_game: Property = Property(name="game", type=BlackjackGame)
Strategy.attributes={Strategy_game}

# JButton class attributes and methods

# Relationships
LoginView_Profile2: BinaryAssociation = BinaryAssociation(
    name="LoginView_Profile2",
    ends={
        Property(name="profile0", type=Profile, multiplicity=Multiplicity(0, 1)),
        Property(name="loginView1", type=LoginView, multiplicity=Multiplicity(0, 1))
    }
)
GameLauncher_LoginView: BinaryAssociation = BinaryAssociation(
    name="GameLauncher_LoginView",
    ends={
        Property(name="loginView2", type=LoginView, multiplicity=Multiplicity(0, 1)),
        Property(name="gameLauncher3", type=GameLauncher, multiplicity=Multiplicity(0, 1))
    }
)
Profile_Blackjack: BinaryAssociation = BinaryAssociation(
    name="Profile_Blackjack",
    ends={
        Property(name="blackjack4", type=BlackjackGame, multiplicity=Multiplicity(0, 1)),
        Property(name="profile5", type=Profile, multiplicity=Multiplicity(0, 1))
    }
)
Blackjack_GameView: BinaryAssociation = BinaryAssociation(
    name="Blackjack_GameView",
    ends={
        Property(name="gameView6", type=GameView, multiplicity=Multiplicity(0, 1)),
        Property(name="blackjack7", type=BlackjackGame, multiplicity=Multiplicity(0, 1))
    }
)
Blackjack_Strategy: BinaryAssociation = BinaryAssociation(
    name="Blackjack_Strategy",
    ends={
        Property(name="strategy8", type=Strategy, multiplicity=Multiplicity(0, 1)),
        Property(name="blackjack9", type=BlackjackGame, multiplicity=Multiplicity(0, 1))
    }
)
Deck_Card: BinaryAssociation = BinaryAssociation(
    name="Deck_Card",
    ends={
        Property(name="card28", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="deck29", type=Deck, multiplicity=Multiplicity(0, 1))
    }
)
PlayerView_GameView: BinaryAssociation = BinaryAssociation(
    name="PlayerView_GameView",
    ends={
        Property(name="gameView10", type=GameView, multiplicity=Multiplicity(0, 1)),
        Property(name="playerView11", type=PlayerView, multiplicity=Multiplicity(1, 9999))
    }
)
Player_Blackjack: BinaryAssociation = BinaryAssociation(
    name="Player_Blackjack",
    ends={
        Property(name="blackjack12", type=BlackjackGame, multiplicity=Multiplicity(0, 1)),
        Property(name="player13", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Blackjack: BinaryAssociation = BinaryAssociation(
    name="Dealer_Blackjack",
    ends={
        Property(name="blackjack14", type=BlackjackGame, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer15", type=Dealer, multiplicity=Multiplicity(0, 1))
    }
)
Blackjack_Deck: BinaryAssociation = BinaryAssociation(
    name="Blackjack_Deck",
    ends={
        Property(name="deck216", type=Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="blackjack17", type=BlackjackGame, multiplicity=Multiplicity(0, 1))
    }
)
BasePlayer_PlayerView: BinaryAssociation = BinaryAssociation(
    name="BasePlayer_PlayerView",
    ends={
        Property(name="playerView18", type=PlayerView, multiplicity=Multiplicity(0, 1)),
        Property(name="basePlayer19", type=BasePlayer, multiplicity=Multiplicity(0, 1))
    }
)
Player_Profile: BinaryAssociation = BinaryAssociation(
    name="Player_Profile",
    ends={
        Property(name="profile220", type=Profile, multiplicity=Multiplicity(0, 1)),
        Property(name="player21", type=Player, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Hand: BinaryAssociation = BinaryAssociation(
    name="Dealer_Hand",
    ends={
        Property(name="hand22", type=Hand, multiplicity=Multiplicity(1, 1)),
        Property(name="dealer23", type=Dealer, multiplicity=Multiplicity(1, 1))
    }
)
Player_Hand: BinaryAssociation = BinaryAssociation(
    name="Player_Hand",
    ends={
        Property(name="hand24", type=Hand, multiplicity=Multiplicity(1, 9999)),
        Property(name="player25", type=Player, multiplicity=Multiplicity(1, 1))
    }
)
Hand_Card: BinaryAssociation = BinaryAssociation(
    name="Hand_Card",
    ends={
        Property(name="card26", type=Card, multiplicity=Multiplicity(0, 9999)),
        Property(name="hand27", type=Hand, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_056e42da_7ca5_4c9f_bda7_f6e45fd28058",
    types={GameView, BasePlayer, User_Actor, UseCase_UseCase, JLabel, Player, Dealer, PlayerView, BlackjackGame, Deck, Hand, Profile, GameLauncher, LoginView, Card, Strategy, JButton},
    associations={LoginView_Profile2, GameLauncher_LoginView, Profile_Blackjack, Blackjack_GameView, Blackjack_Strategy, Deck_Card, PlayerView_GameView, Player_Blackjack, Dealer_Blackjack, Blackjack_Deck, BasePlayer_PlayerView, Player_Profile, Dealer_Hand, Player_Hand, Hand_Card},
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