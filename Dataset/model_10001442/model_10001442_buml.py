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
blackjack_GameState: Enumeration = Enumeration(
    name="blackjack_GameState",
    literals={
            
    }
)

blackjack_Suit: Enumeration = Enumeration(
    name="blackjack_Suit",
    literals={
            
    }
)

blackjack_Value: Enumeration = Enumeration(
    name="blackjack_Value",
    literals={
            
    }
)

# Classes
blackjack_ExampleInstrumentedTest = Class(name="blackjack_ExampleInstrumentedTest")
blackjack_BlackjackGame = Class(name="blackjack_BlackjackGame")
blackjack_DeckShuffledListener_Interface = Class(name="blackjack_DeckShuffledListener_Interface")
blackjack_BlackjackHand = Class(name="blackjack_BlackjackHand")
blackjack_Card = Class(name="blackjack_Card")
blackjack_CardSet = Class(name="blackjack_CardSet", is_abstract=True)
blackjack_DealerBot = Class(name="blackjack_DealerBot")
blackjack_Deck = Class(name="blackjack_Deck")
blackjack_MainActivity = Class(name="blackjack_MainActivity")
blackjack_ExampleUnitTest = Class(name="blackjack_ExampleUnitTest")
genmymodelreverse_java_lang_Comparable_Interface = Class(name="genmymodelreverse_java_lang_Comparable_Interface", is_abstract=True)
genmymodelreverse_C1 = Class(name="genmymodelreverse_C1")
genmymodelreverse_java_util_Iterator_Interface = Class(name="genmymodelreverse_java_util_Iterator_Interface", is_abstract=True)
genmymodelreverse_C11 = Class(name="genmymodelreverse_C11")
genmymodelreverse_java_lang_Iterable_Interface = Class(name="genmymodelreverse_java_lang_Iterable_Interface", is_abstract=True)
genmymodelreverse_C12 = Class(name="genmymodelreverse_C12")
genmymodelreverse_android_support_v7_app_AppCompatActivity = Class(name="genmymodelreverse_android_support_v7_app_AppCompatActivity")
Comparable_BlackjackHand__Interface = Class(name="Comparable_BlackjackHand__Interface")
Iterable_Card__Interface = Class(name="Iterable_Card__Interface")

# blackjack_ExampleInstrumentedTest class attributes and methods

# blackjack_BlackjackGame class attributes and methods
blackjack_BlackjackGame_MAX_HITS: Property = Property(name="MAX_HITS", type=IntegerType)
blackjack_BlackjackGame_MAX_CARDS_PULLED: Property = Property(name="MAX_CARDS_PULLED", type=IntegerType)
blackjack_BlackjackGame_gstate: Property = Property(name="gstate", type=blackjack_GameState)
blackjack_BlackjackGame_hitButton: Property = Property(name="hitButton", type=StringType)
blackjack_BlackjackGame_stayButton: Property = Property(name="stayButton", type=StringType)
blackjack_BlackjackGame_gameResultTextView: Property = Property(name="gameResultTextView", type=StringType)
blackjack_BlackjackGame_playersHandTextView: Property = Property(name="playersHandTextView", type=StringType)
blackjack_BlackjackGame_dealersHandTextView: Property = Property(name="dealersHandTextView", type=StringType)
blackjack_BlackjackGame_playerHandValueTextView: Property = Property(name="playerHandValueTextView", type=StringType)
blackjack_BlackjackGame_dealersHandValueTextView: Property = Property(name="dealersHandValueTextView", type=StringType)
blackjack_BlackjackGame.attributes={blackjack_BlackjackGame_stayButton, blackjack_BlackjackGame_gstate, blackjack_BlackjackGame_playerHandValueTextView, blackjack_BlackjackGame_MAX_CARDS_PULLED, blackjack_BlackjackGame_dealersHandTextView, blackjack_BlackjackGame_hitButton, blackjack_BlackjackGame_dealersHandValueTextView, blackjack_BlackjackGame_gameResultTextView, blackjack_BlackjackGame_MAX_HITS, blackjack_BlackjackGame_playersHandTextView}

# blackjack_DeckShuffledListener_Interface class attributes and methods

# blackjack_BlackjackHand class attributes and methods

# blackjack_Card class attributes and methods
blackjack_Card_suit: Property = Property(name="suit", type=blackjack_Suit)
blackjack_Card_value: Property = Property(name="value", type=blackjack_Value)
blackjack_Card_MAX_VALUE_OF_ACE: Property = Property(name="MAX_VALUE_OF_ACE", type=IntegerType)
blackjack_Card_BLACKJACK_VALUE: Property = Property(name="BLACKJACK_VALUE", type=IntegerType)
blackjack_Card.attributes={blackjack_Card_BLACKJACK_VALUE, blackjack_Card_MAX_VALUE_OF_ACE, blackjack_Card_suit, blackjack_Card_value}

# blackjack_CardSet class attributes and methods

# blackjack_DealerBot class attributes and methods

# blackjack_Deck class attributes and methods

# blackjack_MainActivity class attributes and methods

# blackjack_ExampleUnitTest class attributes and methods

# genmymodelreverse_java_lang_Comparable_Interface class attributes and methods

# genmymodelreverse_C1 class attributes and methods

# genmymodelreverse_java_util_Iterator_Interface class attributes and methods

# genmymodelreverse_C11 class attributes and methods

# genmymodelreverse_java_lang_Iterable_Interface class attributes and methods

# genmymodelreverse_C12 class attributes and methods

# genmymodelreverse_android_support_v7_app_AppCompatActivity class attributes and methods

# Comparable_BlackjackHand__Interface class attributes and methods

# Iterable_Card__Interface class attributes and methods

# Relationships
hand_DealerBot_BlackjackHand_0: BinaryAssociation = BinaryAssociation(
    name="hand_DealerBot_BlackjackHand_0",
    ends={
        Property(name="dealerbot0", type=blackjack_DealerBot, multiplicity=Multiplicity(0, 1)),
        Property(name="hand1", type=blackjack_BlackjackHand, multiplicity=Multiplicity(0, 1))
    }
)
playerHand_BlackjackGame_BlackjackHand_1: BinaryAssociation = BinaryAssociation(
    name="playerHand_BlackjackGame_BlackjackHand_1",
    ends={
        Property(name="blackjackgame2", type=blackjack_BlackjackGame, multiplicity=Multiplicity(0, 1)),
        Property(name="playerHand3", type=blackjack_BlackjackHand, multiplicity=Multiplicity(0, 1))
    }
)
deck_DealerBot_Deck_6: BinaryAssociation = BinaryAssociation(
    name="deck_DealerBot_Deck_6",
    ends={
        Property(name="dealerbot4", type=blackjack_DealerBot, multiplicity=Multiplicity(0, 1)),
        Property(name="deck5", type=blackjack_Deck, multiplicity=Multiplicity(0, 1))
    }
)
cards_CardSet_Card_5: BinaryAssociation = BinaryAssociation(
    name="cards_CardSet_Card_5",
    ends={
        Property(name="cardset6", type=blackjack_CardSet, multiplicity=Multiplicity(0, 1)),
        Property(name="cards7", type=blackjack_Card, multiplicity=Multiplicity(0, 9999))
    }
)
deckShuffledListener_BlackjackGame_DeckShuffledListener_3: BinaryAssociation = BinaryAssociation(
    name="deckShuffledListener_BlackjackGame_DeckShuffledListener_3",
    ends={
        Property(name="blackjackgame8", type=blackjack_BlackjackGame, multiplicity=Multiplicity(0, 1)),
        Property(name="deckShuffledListener9", type=blackjack_DeckShuffledListener_Interface, multiplicity=Multiplicity(0, 1))
    }
)
theDeck_BlackjackGame_Deck_4: BinaryAssociation = BinaryAssociation(
    name="theDeck_BlackjackGame_Deck_4",
    ends={
        Property(name="blackjackgame10", type=blackjack_BlackjackGame, multiplicity=Multiplicity(0, 1)),
        Property(name="theDeck11", type=blackjack_Deck, multiplicity=Multiplicity(0, 1))
    }
)
dealerBot_BlackjackGame_DealerBot_2: BinaryAssociation = BinaryAssociation(
    name="dealerBot_BlackjackGame_DealerBot_2",
    ends={
        Property(name="blackjackgame12", type=blackjack_BlackjackGame, multiplicity=Multiplicity(0, 1)),
        Property(name="dealerBot13", type=blackjack_DealerBot, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6nBgAMclEeeWu_SLkciAbg",
    types={blackjack_ExampleInstrumentedTest, blackjack_BlackjackGame, blackjack_DeckShuffledListener_Interface, blackjack_BlackjackHand, blackjack_Card, blackjack_CardSet, blackjack_DealerBot, blackjack_Deck, blackjack_MainActivity, blackjack_ExampleUnitTest, genmymodelreverse_java_lang_Comparable_Interface, genmymodelreverse_C1, genmymodelreverse_java_util_Iterator_Interface, genmymodelreverse_C11, genmymodelreverse_java_lang_Iterable_Interface, genmymodelreverse_C12, genmymodelreverse_android_support_v7_app_AppCompatActivity, Comparable_BlackjackHand__Interface, Iterable_Card__Interface, blackjack_GameState, blackjack_Suit, blackjack_Value},
    associations={hand_DealerBot_BlackjackHand_0, playerHand_BlackjackGame_BlackjackHand_1, deck_DealerBot_Deck_6, cards_CardSet_Card_5, deckShuffledListener_BlackjackGame_DeckShuffledListener_3, theDeck_BlackjackGame_Deck_4, dealerBot_BlackjackGame_DealerBot_2},
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