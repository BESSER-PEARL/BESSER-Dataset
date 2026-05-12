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
Main = Class(name="Main")
GameSession = Class(name="GameSession")
Game = Class(name="Game")
Players = Class(name="Players")
Dealer = Class(name="Dealer")
DrawPile = Class(name="DrawPile")
DiscardPile = Class(name="DiscardPile")
GameElements_Interface = Class(name="GameElements_Interface")
GameElements = Class(name="GameElements")
CardElements_Interface = Class(name="CardElements_Interface")
Card = Class(name="Card")
NumberCard = Class(name="NumberCard")
ActionCard = Class(name="ActionCard")
Reverse = Class(name="Reverse")
Skip = Class(name="Skip")
Draw2 = Class(name="Draw2")
Wild = Class(name="Wild")
Wild4 = Class(name="Wild4")
WildCard = Class(name="WildCard")
Color = Class(name="Color")
int___1 = Class(name="int___1")

# Main class attributes and methods
Main_Main__: Property = Property(name="Main__", type=StringType)
Main_main_String____: Property = Property(name="main_String____", type=StringType)
Main.attributes={Main_Main__, Main_main_String____}

# GameSession class attributes and methods
GameSession_GameSession_Game_: Property = Property(name="GameSession_Game_", type=StringType)
GameSession_setPlayers__: Property = Property(name="setPlayers__", type=StringType)
GameSession_GameSession_Game__Card_: Property = Property(name="GameSession_Game__Card_", type=StringType)
GameSession.attributes={GameSession_setPlayers__, GameSession_GameSession_Game_, GameSession_GameSession_Game__Card_}

# Game class attributes and methods
Game_Game__: Property = Property(name="Game__", type=StringType)
Game_getPlayers__: Property = Property(name="getPlayers__", type=StringType)
Game_PlayGame__: Property = Property(name="PlayGame__", type=StringType)
Game_Game__1: Property = Property(name="Game__1", type=StringType)
Game.attributes={Game_Game__1, Game_Game__, Game_PlayGame__, Game_getPlayers__}

# Players class attributes and methods
Players_Players__: Property = Property(name="Players__", type=StringType)
Players_Player_String_: Property = Property(name="Player_String_", type=StringType)
Players_getName: Property = Property(name="getName", type=StringType)
Players_drawCard_Card_: Property = Property(name="drawCard_Card_", type=StringType)
Players_hasCard_Card_: Property = Property(name="hasCard_Card_", type=StringType)
Players_playCard_Card_: Property = Property(name="playCard_Card_", type=StringType)
Players_Player__: Property = Property(name="Player__", type=StringType)
Players.attributes={Players_hasCard_Card_, Players_Players__, Players_Player__, Players_playCard_Card_, Players_getName, Players_drawCard_Card_, Players_Player_String_}

# Dealer class attributes and methods
Dealer_Dealer__: Property = Property(name="Dealer__", type=StringType)
Dealer_shuffle__: Property = Property(name="shuffle__", type=StringType)
Dealer_distribute_Player___: Property = Property(name="distribute_Player___", type=StringType)
Dealer_Dealer__1: Property = Property(name="Dealer__1", type=StringType)
Dealer.attributes={Dealer_distribute_Player___, Dealer_Dealer__, Dealer_Dealer__1, Dealer_shuffle__}

# DrawPile class attributes and methods
DrawPile_DrawPile__: Property = Property(name="DrawPile__", type=StringType)
DrawPile_removeCard_Card_: Property = Property(name="removeCard_Card_", type=StringType)
DrawPile_DrawPile__1: Property = Property(name="DrawPile__1", type=StringType)
DrawPile.attributes={DrawPile_DrawPile__, DrawPile_DrawPile__1, DrawPile_removeCard_Card_}

# DiscardPile class attributes and methods
DiscardPile_DiscardPile__: Property = Property(name="DiscardPile__", type=StringType)
DiscardPile_showTop__: Property = Property(name="showTop__", type=StringType)
DiscardPile_DiscardPile__1: Property = Property(name="DiscardPile__1", type=StringType)
DiscardPile.attributes={DiscardPile_DiscardPile__1, DiscardPile_DiscardPile__, DiscardPile_showTop__}

# GameElements_Interface class attributes and methods

# GameElements class attributes and methods
GameElements_CardsTotal: Property = Property(name="CardsTotal", type=StringType)
GameElements_OpeningHand: Property = Property(name="OpeningHand", type=StringType)
GameElements_WildCardCol: Property = Property(name="WildCardCol", type=StringType)
GameElements_CardColors: Property = Property(name="CardColors", type=StringType)
GameElements_WildActions: Property = Property(name="WildActions", type=StringType)
GameElements_Actions: Property = Property(name="Actions", type=StringType)
GameElements_CardNumber: Property = Property(name="CardNumber", type=StringType)
GameElements_Numbers: Property = Property(name="Numbers", type=int___1)
GameElements_Action: Property = Property(name="Action", type=StringType)
GameElements_Wild: Property = Property(name="Wild", type=StringType)
GameElements.attributes={GameElements_WildActions, GameElements_CardNumber, GameElements_WildCardCol, GameElements_Actions, GameElements_OpeningHand, GameElements_Numbers, GameElements_Wild, GameElements_CardsTotal, GameElements_CardColors, GameElements_Action}

# CardElements_Interface class attributes and methods

# Card class attributes and methods
Card_Card__: Property = Property(name="Card__", type=StringType)
Card_Card_Color__int__String_: Property = Property(name="Card_Color__int__String_", type=StringType)
Card_setColor_Color_: Property = Property(name="setColor_Color_", type=StringType)
Card_getColor__: Property = Property(name="getColor__", type=Color)
Card_setValue: Property = Property(name="setValue", type=StringType)
Card_Card__1: Property = Property(name="Card__1", type=StringType)
Card.attributes={Card_setColor_Color_, Card_getColor__, Card_Card_Color__int__String_, Card_setValue, Card_Card__, Card_Card__1}

# NumberCard class attributes and methods
NumberCard_attribute: Property = Property(name="attribute", type=StringType)
NumberCard_NumberCard__: Property = Property(name="NumberCard__", type=StringType)
NumberCard_NumberCard_Color__String_: Property = Property(name="NumberCard_Color__String_", type=StringType)
NumberCard_attribute2: Property = Property(name="attribute2", type=StringType)
NumberCard.attributes={NumberCard_attribute, NumberCard_NumberCard__, NumberCard_NumberCard_Color__String_, NumberCard_attribute2}

# ActionCard class attributes and methods
ActionCard_ActionCard__: Property = Property(name="ActionCard__", type=StringType)
ActionCard_ActionCard_Color_String_: Property = Property(name="ActionCard_Color_String_", type=StringType)
ActionCard__attr: Property = Property(name="_attr", type=StringType)
ActionCard.attributes={ActionCard_ActionCard_Color_String_, ActionCard_ActionCard__, ActionCard__attr}

# Reverse class attributes and methods

# Skip class attributes and methods

# Draw2 class attributes and methods

# Wild class attributes and methods

# Wild4 class attributes and methods

# WildCard class attributes and methods
WildCard_WildCard__: Property = Property(name="WildCard__", type=StringType)
WildCard_WildCard_String_: Property = Property(name="WildCard_String_", type=StringType)
WildCard.attributes={WildCard_WildCard__, WildCard_WildCard_String_}

# Color class attributes and methods

# int___1 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_iegdsB2TEeqPCsas7676rw",
    types={Main, GameSession, Game, Players, Dealer, DrawPile, DiscardPile, GameElements_Interface, GameElements, CardElements_Interface, Card, NumberCard, ActionCard, Reverse, Skip, Draw2, Wild, Wild4, WildCard, Color, int___1},
    associations={},
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