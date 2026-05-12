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
model_Color: Enumeration = Enumeration(
    name="model_Color",
    literals={
            
    }
)

model_Value: Enumeration = Enumeration(
    name="model_Value",
    literals={
            
    }
)

# Classes
BlackJack_Program = Class(name="BlackJack_Program")
controller_PlayGame = Class(name="controller_PlayGame")
model_Card = Class(name="model_Card")
model_Dealer = Class(name="model_Dealer")
model_Deck = Class(name="model_Deck")
model_Game = Class(name="model_Game")
model_Player = Class(name="model_Player")
rules_AmericanNewGameStrategy = Class(name="rules_AmericanNewGameStrategy")
rules_BasicHitStrategy = Class(name="rules_BasicHitStrategy")
rules_IHitStrategy_Interface = Class(name="rules_IHitStrategy_Interface")
rules_INewGameStrategy_Interface = Class(name="rules_INewGameStrategy_Interface")
rules_InternationalNewGameStrategy = Class(name="rules_InternationalNewGameStrategy")
rules_RulesFactory = Class(name="rules_RulesFactory")
view_IView_Interface = Class(name="view_IView_Interface")
view_SimpleView = Class(name="view_SimpleView")
view_SwedishView = Class(name="view_SwedishView")
genmymodelreverse_java_lang_Iterable_Interface = Class(name="genmymodelreverse_java_lang_Iterable_Interface", is_abstract=True)
genmymodelreverse_C1 = Class(name="genmymodelreverse_C1")

# BlackJack_Program class attributes and methods

# controller_PlayGame class attributes and methods

# model_Card class attributes and methods
model_Card_m_color: Property = Property(name="m_color", type=model_Color)
model_Card_m_value: Property = Property(name="m_value", type=model_Value)
model_Card_m_isHidden: Property = Property(name="m_isHidden", type=BooleanType)
model_Card.attributes={model_Card_m_color, model_Card_m_value, model_Card_m_isHidden}

# model_Dealer class attributes and methods

# model_Deck class attributes and methods

# model_Game class attributes and methods

# model_Player class attributes and methods
model_Player_g_maxScore: Property = Property(name="g_maxScore", type=IntegerType)
model_Player.attributes={model_Player_g_maxScore}

# rules_AmericanNewGameStrategy class attributes and methods

# rules_BasicHitStrategy class attributes and methods
rules_BasicHitStrategy_g_hitLimit: Property = Property(name="g_hitLimit", type=IntegerType)
rules_BasicHitStrategy.attributes={rules_BasicHitStrategy_g_hitLimit}

# rules_IHitStrategy_Interface class attributes and methods

# rules_INewGameStrategy_Interface class attributes and methods

# rules_InternationalNewGameStrategy class attributes and methods

# rules_RulesFactory class attributes and methods

# view_IView_Interface class attributes and methods

# view_SimpleView class attributes and methods

# view_SwedishView class attributes and methods

# genmymodelreverse_java_lang_Iterable_Interface class attributes and methods

# genmymodelreverse_C1 class attributes and methods

# Relationships
m_cards_Deck_Card_5: BinaryAssociation = BinaryAssociation(
    name="m_cards_Deck_Card_5",
    ends={
        Property(name="deck0", type=model_Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="m_cards1", type=model_Card, multiplicity=Multiplicity(0, 9999))
    }
)
m_dealer_Game_Dealer_4: BinaryAssociation = BinaryAssociation(
    name="m_dealer_Game_Dealer_4",
    ends={
        Property(name="game2", type=model_Game, multiplicity=Multiplicity(0, 1)),
        Property(name="m_dealer3", type=model_Dealer, multiplicity=Multiplicity(0, 1))
    }
)
m_player_Game_Player_0: BinaryAssociation = BinaryAssociation(
    name="m_player_Game_Player_0",
    ends={
        Property(name="game4", type=model_Game, multiplicity=Multiplicity(0, 1)),
        Property(name="m_player5", type=model_Player, multiplicity=Multiplicity(0, 1))
    }
)
m_hitRule_Dealer_IHitStrategy_3: BinaryAssociation = BinaryAssociation(
    name="m_hitRule_Dealer_IHitStrategy_3",
    ends={
        Property(name="dealer6", type=model_Dealer, multiplicity=Multiplicity(0, 1)),
        Property(name="m_hitRule7", type=rules_IHitStrategy_Interface, multiplicity=Multiplicity(0, 1))
    }
)
m_deck_Dealer_Deck_6: BinaryAssociation = BinaryAssociation(
    name="m_deck_Dealer_Deck_6",
    ends={
        Property(name="dealer8", type=model_Dealer, multiplicity=Multiplicity(0, 1)),
        Property(name="m_deck9", type=model_Deck, multiplicity=Multiplicity(0, 1))
    }
)
m_hand_Player_Card_1: BinaryAssociation = BinaryAssociation(
    name="m_hand_Player_Card_1",
    ends={
        Property(name="player10", type=model_Player, multiplicity=Multiplicity(0, 1)),
        Property(name="m_hand11", type=model_Card, multiplicity=Multiplicity(0, 9999))
    }
)
m_newGameRule_Dealer_INewGameStrategy_2: BinaryAssociation = BinaryAssociation(
    name="m_newGameRule_Dealer_INewGameStrategy_2",
    ends={
        Property(name="dealer12", type=model_Dealer, multiplicity=Multiplicity(0, 1)),
        Property(name="m_newGameRule13", type=rules_INewGameStrategy_Interface, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_96abed87_8bf9_43e3_b35d_561c1b77e702",
    types={BlackJack_Program, controller_PlayGame, model_Card, model_Dealer, model_Deck, model_Game, model_Player, rules_AmericanNewGameStrategy, rules_BasicHitStrategy, rules_IHitStrategy_Interface, rules_INewGameStrategy_Interface, rules_InternationalNewGameStrategy, rules_RulesFactory, view_IView_Interface, view_SimpleView, view_SwedishView, genmymodelreverse_java_lang_Iterable_Interface, genmymodelreverse_C1, model_Color, model_Value},
    associations={m_cards_Deck_Card_5, m_dealer_Game_Dealer_4, m_player_Game_Player_0, m_hitRule_Dealer_IHitStrategy_3, m_deck_Dealer_Deck_6, m_hand_Player_Card_1, m_newGameRule_Dealer_INewGameStrategy_2},
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