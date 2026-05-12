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
genmymodelreverse_java_lang_Throwable = Class(name="genmymodelreverse_java_lang_Throwable")
genmymodelreverse_java_lang_Exception = Class(name="genmymodelreverse_java_lang_Exception")
Comparable_Score__Interface = Class(name="Comparable_Score__Interface")
Main = Class(name="Main")
card_Card = Class(name="card_Card")
card_Pack = Class(name="card_Pack")
deck_Deck = Class(name="deck_Deck")
deck_Foundations = Class(name="deck_Foundations")
deck_Stock = Class(name="deck_Stock")
deck_Tableau = Class(name="deck_Tableau")
entities_Comment = Class(name="entities_Comment")
entities_Rating = Class(name="entities_Rating")
entities_Score = Class(name="entities_Score")
features_History = Class(name="features_History")
services_CommentException = Class(name="services_CommentException")
services_CommentService_Interface = Class(name="services_CommentService_Interface")
services_CommentServiceJDBC = Class(name="services_CommentServiceJDBC")
services_RatingException = Class(name="services_RatingException")
services_RatingService_Interface = Class(name="services_RatingService_Interface")
services_RatingServiceJDBC = Class(name="services_RatingServiceJDBC")
services_ScoreException = Class(name="services_ScoreException")
services_ScoreService_Interface = Class(name="services_ScoreService_Interface")
services_ScoreServiceJDBC = Class(name="services_ScoreServiceJDBC")
CommentServiceJDBCTest = Class(name="CommentServiceJDBCTest")
CommentServiceTest = Class(name="CommentServiceTest")
RatingServiceTest = Class(name="RatingServiceTest")
ScoreServiceJDBCTest = Class(name="ScoreServiceJDBCTest")
ScoreServiceTest = Class(name="ScoreServiceTest")
SpiderSolitaireTestSuite = Class(name="SpiderSolitaireTestSuite")
genmymodelreverse_java_util_List_Interface = Class(name="genmymodelreverse_java_util_List_Interface", is_abstract=True)
genmymodelreverse_C1 = Class(name="genmymodelreverse_C1")
genmymodelreverse_java_util_Date = Class(name="genmymodelreverse_java_util_Date")
genmymodelreverse_java_io_Serializable_Interface = Class(name="genmymodelreverse_java_io_Serializable_Interface", is_abstract=True)
genmymodelreverse_java_lang_Comparable_Interface = Class(name="genmymodelreverse_java_lang_Comparable_Interface", is_abstract=True)
genmymodelreverse_C11 = Class(name="genmymodelreverse_C11")
genmymodelreverse_java_lang_RuntimeException = Class(name="genmymodelreverse_java_lang_RuntimeException")

# genmymodelreverse_java_lang_Throwable class attributes and methods

# genmymodelreverse_java_lang_Exception class attributes and methods

# Comparable_Score__Interface class attributes and methods

# Main class attributes and methods

# card_Card class attributes and methods
card_Card_rank: Property = Property(name="rank", type=IntegerType)
card_Card_flipped: Property = Property(name="flipped", type=BooleanType)
card_Card.attributes={card_Card_flipped, card_Card_rank}

# card_Pack class attributes and methods
card_Pack_cardPack: Property = Property(name="cardPack", type=StringType)
card_Pack.attributes={card_Pack_cardPack}

# deck_Deck class attributes and methods
deck_Deck_removeItemFromArrayIndex: Property = Property(name="removeItemFromArrayIndex", type=IntegerType)
deck_Deck_score: Property = Property(name="score", type=IntegerType)
deck_Deck_stepCounter: Property = Property(name="stepCounter", type=IntegerType)
deck_Deck_inputDestinationRow: Property = Property(name="inputDestinationRow", type=IntegerType)
deck_Deck_foundationIndex: Property = Property(name="foundationIndex", type=IntegerType)
deck_Deck.attributes={deck_Deck_foundationIndex, deck_Deck_stepCounter, deck_Deck_removeItemFromArrayIndex, deck_Deck_inputDestinationRow, deck_Deck_score}

# deck_Foundations class attributes and methods
deck_Foundations_foundationList: Property = Property(name="foundationList", type=StringType)
deck_Foundations.attributes={deck_Foundations_foundationList}

# deck_Stock class attributes and methods
deck_Stock_stock: Property = Property(name="stock", type=StringType)
deck_Stock_STARTING_INDEX: Property = Property(name="STARTING_INDEX", type=IntegerType)
deck_Stock.attributes={deck_Stock_STARTING_INDEX, deck_Stock_stock}

# deck_Tableau class attributes and methods
deck_Tableau_columns: Property = Property(name="columns", type=StringType)
deck_Tableau.attributes={deck_Tableau_columns}

# entities_Comment class attributes and methods
entities_Comment_player: Property = Property(name="player", type=StringType)
entities_Comment_game: Property = Property(name="game", type=StringType)
entities_Comment_comment: Property = Property(name="comment", type=StringType)
entities_Comment_commentedOn: Property = Property(name="commentedOn", type=genmymodelreverse_java_util_Date)
entities_Comment.attributes={entities_Comment_comment, entities_Comment_commentedOn, entities_Comment_game, entities_Comment_player}

# entities_Rating class attributes and methods
entities_Rating_player: Property = Property(name="player", type=StringType)
entities_Rating_game: Property = Property(name="game", type=StringType)
entities_Rating_rating: Property = Property(name="rating", type=IntegerType)
entities_Rating_ratedon: Property = Property(name="ratedon", type=genmymodelreverse_java_util_Date)
entities_Rating.attributes={entities_Rating_game, entities_Rating_ratedon, entities_Rating_player, entities_Rating_rating}

# entities_Score class attributes and methods
entities_Score_game: Property = Property(name="game", type=StringType)
entities_Score_player: Property = Property(name="player", type=StringType)
entities_Score_points: Property = Property(name="points", type=IntegerType)
entities_Score_playedOn: Property = Property(name="playedOn", type=genmymodelreverse_java_util_Date)
entities_Score.attributes={entities_Score_game, entities_Score_playedOn, entities_Score_points, entities_Score_player}

# features_History class attributes and methods
features_History_revertList: Property = Property(name="revertList", type=IntegerType)
features_History.attributes={features_History_revertList}

# services_CommentException class attributes and methods

# services_CommentService_Interface class attributes and methods

# services_CommentServiceJDBC class attributes and methods
services_CommentServiceJDBC_URL: Property = Property(name="URL", type=StringType)
services_CommentServiceJDBC_USER: Property = Property(name="USER", type=StringType)
services_CommentServiceJDBC_PASSWORD: Property = Property(name="PASSWORD", type=StringType)
services_CommentServiceJDBC_INSERT_COMMENT: Property = Property(name="INSERT_COMMENT", type=StringType)
services_CommentServiceJDBC_SELECT_COMMENTS: Property = Property(name="SELECT_COMMENTS", type=StringType)
services_CommentServiceJDBC.attributes={services_CommentServiceJDBC_SELECT_COMMENTS, services_CommentServiceJDBC_URL, services_CommentServiceJDBC_PASSWORD, services_CommentServiceJDBC_USER, services_CommentServiceJDBC_INSERT_COMMENT}

# services_RatingException class attributes and methods

# services_RatingService_Interface class attributes and methods

# services_RatingServiceJDBC class attributes and methods
services_RatingServiceJDBC_URL: Property = Property(name="URL", type=StringType)
services_RatingServiceJDBC_USER: Property = Property(name="USER", type=StringType)
services_RatingServiceJDBC_PASSWORD: Property = Property(name="PASSWORD", type=StringType)
services_RatingServiceJDBC_INSERT_RATING: Property = Property(name="INSERT_RATING", type=StringType)
services_RatingServiceJDBC_SELECT_RATING: Property = Property(name="SELECT_RATING", type=StringType)
services_RatingServiceJDBC_SELECT_AVERAGE_RATING: Property = Property(name="SELECT_AVERAGE_RATING", type=StringType)
services_RatingServiceJDBC.attributes={services_RatingServiceJDBC_URL, services_RatingServiceJDBC_SELECT_RATING, services_RatingServiceJDBC_INSERT_RATING, services_RatingServiceJDBC_SELECT_AVERAGE_RATING, services_RatingServiceJDBC_PASSWORD, services_RatingServiceJDBC_USER}

# services_ScoreException class attributes and methods

# services_ScoreService_Interface class attributes and methods

# services_ScoreServiceJDBC class attributes and methods
services_ScoreServiceJDBC_URL: Property = Property(name="URL", type=StringType)
services_ScoreServiceJDBC_USER: Property = Property(name="USER", type=StringType)
services_ScoreServiceJDBC_PASSWORD: Property = Property(name="PASSWORD", type=StringType)
services_ScoreServiceJDBC_INSERT_SCORE: Property = Property(name="INSERT_SCORE", type=StringType)
services_ScoreServiceJDBC_SELECT_SCORE: Property = Property(name="SELECT_SCORE", type=StringType)
services_ScoreServiceJDBC.attributes={services_ScoreServiceJDBC_PASSWORD, services_ScoreServiceJDBC_URL, services_ScoreServiceJDBC_SELECT_SCORE, services_ScoreServiceJDBC_INSERT_SCORE, services_ScoreServiceJDBC_USER}

# CommentServiceJDBCTest class attributes and methods
CommentServiceJDBCTest_DELETE: Property = Property(name="DELETE", type=StringType)
CommentServiceJDBCTest_URL: Property = Property(name="URL", type=StringType)
CommentServiceJDBCTest_USER: Property = Property(name="USER", type=StringType)
CommentServiceJDBCTest_PASS: Property = Property(name="PASS", type=StringType)
CommentServiceJDBCTest.attributes={CommentServiceJDBCTest_USER, CommentServiceJDBCTest_PASS, CommentServiceJDBCTest_DELETE, CommentServiceJDBCTest_URL}

# CommentServiceTest class attributes and methods
CommentServiceTest_GAME_NAME: Property = Property(name="GAME_NAME", type=StringType)
CommentServiceTest_PLAYER_NAME: Property = Property(name="PLAYER_NAME", type=StringType)
CommentServiceTest.attributes={CommentServiceTest_GAME_NAME, CommentServiceTest_PLAYER_NAME}

# RatingServiceTest class attributes and methods
RatingServiceTest_GAME_NAME: Property = Property(name="GAME_NAME", type=StringType)
RatingServiceTest_TEST_PLAYER: Property = Property(name="TEST_PLAYER", type=StringType)
RatingServiceTest_TEST_PLAYER_2: Property = Property(name="TEST_PLAYER_2", type=StringType)
RatingServiceTest_TEST_PLAYER_3: Property = Property(name="TEST_PLAYER_3", type=StringType)
RatingServiceTest.attributes={RatingServiceTest_TEST_PLAYER_3, RatingServiceTest_GAME_NAME, RatingServiceTest_TEST_PLAYER_2, RatingServiceTest_TEST_PLAYER}

# ScoreServiceJDBCTest class attributes and methods
ScoreServiceJDBCTest_DELETE: Property = Property(name="DELETE", type=StringType)
ScoreServiceJDBCTest_URL: Property = Property(name="URL", type=StringType)
ScoreServiceJDBCTest_USER: Property = Property(name="USER", type=StringType)
ScoreServiceJDBCTest_PASS: Property = Property(name="PASS", type=StringType)
ScoreServiceJDBCTest.attributes={ScoreServiceJDBCTest_DELETE, ScoreServiceJDBCTest_URL, ScoreServiceJDBCTest_USER, ScoreServiceJDBCTest_PASS}

# ScoreServiceTest class attributes and methods
ScoreServiceTest_GAME_NAME: Property = Property(name="GAME_NAME", type=StringType)
ScoreServiceTest.attributes={ScoreServiceTest_GAME_NAME}

# SpiderSolitaireTestSuite class attributes and methods

# genmymodelreverse_java_util_List_Interface class attributes and methods

# genmymodelreverse_C1 class attributes and methods

# genmymodelreverse_java_util_Date class attributes and methods

# genmymodelreverse_java_io_Serializable_Interface class attributes and methods

# genmymodelreverse_java_lang_Comparable_Interface class attributes and methods

# genmymodelreverse_C11 class attributes and methods

# genmymodelreverse_java_lang_RuntimeException class attributes and methods

# Relationships
commentService_CommentServiceTest_CommentService_13: BinaryAssociation = BinaryAssociation(
    name="commentService_CommentServiceTest_CommentService_13",
    ends={
        Property(name="commentservicetest10", type=CommentServiceTest, multiplicity=Multiplicity(0, 1)),
        Property(name="commentService11", type=services_CommentService_Interface, multiplicity=Multiplicity(0, 1))
    }
)
foundations_Deck_Foundations_17: BinaryAssociation = BinaryAssociation(
    name="foundations_Deck_Foundations_17",
    ends={
        Property(name="deck12", type=deck_Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="foundations13", type=deck_Foundations, multiplicity=Multiplicity(0, 1))
    }
)
ratingService_RatingServiceTest_RatingService_2: BinaryAssociation = BinaryAssociation(
    name="ratingService_RatingServiceTest_RatingService_2",
    ends={
        Property(name="ratingservicetest14", type=RatingServiceTest, multiplicity=Multiplicity(0, 1)),
        Property(name="ratingService15", type=services_RatingService_Interface, multiplicity=Multiplicity(0, 1))
    }
)
tableau8_Tableau_Card_9: BinaryAssociation = BinaryAssociation(
    name="tableau8_Tableau_Card_9",
    ends={
        Property(name="tableau16", type=deck_Tableau, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau817", type=card_Card, multiplicity=Multiplicity(0, 9999))
    }
)
tableau7_Tableau_Card_0: BinaryAssociation = BinaryAssociation(
    name="tableau7_Tableau_Card_0",
    ends={
        Property(name="tableau18", type=deck_Tableau, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau719", type=card_Card, multiplicity=Multiplicity(0, 9999))
    }
)
tableau3_Tableau_Card_5: BinaryAssociation = BinaryAssociation(
    name="tableau3_Tableau_Card_5",
    ends={
        Property(name="tableau20", type=deck_Tableau, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau321", type=card_Card, multiplicity=Multiplicity(0, 9999))
    }
)
tableau6_Tableau_Card_10: BinaryAssociation = BinaryAssociation(
    name="tableau6_Tableau_Card_10",
    ends={
        Property(name="tableau22", type=deck_Tableau, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau623", type=card_Card, multiplicity=Multiplicity(0, 9999))
    }
)
tableau1_Tableau_Card_15: BinaryAssociation = BinaryAssociation(
    name="tableau1_Tableau_Card_15",
    ends={
        Property(name="tableau24", type=deck_Tableau, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau125", type=card_Card, multiplicity=Multiplicity(0, 9999))
    }
)
scoreService_ScoreServiceTest_ScoreService_6: BinaryAssociation = BinaryAssociation(
    name="scoreService_ScoreServiceTest_ScoreService_6",
    ends={
        Property(name="scoreservicetest0", type=ScoreServiceTest, multiplicity=Multiplicity(0, 1)),
        Property(name="scoreService1", type=services_ScoreService_Interface, multiplicity=Multiplicity(0, 1))
    }
)
history_Deck_History_11: BinaryAssociation = BinaryAssociation(
    name="history_Deck_History_11",
    ends={
        Property(name="deck2", type=deck_Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="history3", type=features_History, multiplicity=Multiplicity(0, 1))
    }
)
tableau2_Tableau_Card_14: BinaryAssociation = BinaryAssociation(
    name="tableau2_Tableau_Card_14",
    ends={
        Property(name="tableau4", type=deck_Tableau, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau25", type=card_Card, multiplicity=Multiplicity(0, 9999))
    }
)
pack_Deck_Pack_16: BinaryAssociation = BinaryAssociation(
    name="pack_Deck_Pack_16",
    ends={
        Property(name="deck6", type=deck_Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="pack7", type=card_Pack, multiplicity=Multiplicity(0, 1))
    }
)
tableau_Deck_Tableau_7: BinaryAssociation = BinaryAssociation(
    name="tableau_Deck_Tableau_7",
    ends={
        Property(name="deck8", type=deck_Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau9", type=deck_Tableau, multiplicity=Multiplicity(0, 1))
    }
)
stock_Deck_Stock_8: BinaryAssociation = BinaryAssociation(
    name="stock_Deck_Stock_8",
    ends={
        Property(name="deck26", type=deck_Deck, multiplicity=Multiplicity(0, 1)),
        Property(name="stock27", type=deck_Stock, multiplicity=Multiplicity(0, 1))
    }
)
tableau4_Tableau_Card_12: BinaryAssociation = BinaryAssociation(
    name="tableau4_Tableau_Card_12",
    ends={
        Property(name="tableau28", type=deck_Tableau, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau429", type=card_Card, multiplicity=Multiplicity(0, 9999))
    }
)
tableau5_Tableau_Card_1: BinaryAssociation = BinaryAssociation(
    name="tableau5_Tableau_Card_1",
    ends={
        Property(name="tableau30", type=deck_Tableau, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau531", type=card_Card, multiplicity=Multiplicity(0, 9999))
    }
)
tableau9_Tableau_Card_3: BinaryAssociation = BinaryAssociation(
    name="tableau9_Tableau_Card_3",
    ends={
        Property(name="tableau32", type=deck_Tableau, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau933", type=card_Card, multiplicity=Multiplicity(0, 9999))
    }
)
tableau10_Tableau_Card_4: BinaryAssociation = BinaryAssociation(
    name="tableau10_Tableau_Card_4",
    ends={
        Property(name="tableau34", type=deck_Tableau, multiplicity=Multiplicity(0, 1)),
        Property(name="tableau1035", type=card_Card, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_wJS0wCqtEeiGfabwoJ7AXg",
    types={genmymodelreverse_java_lang_Throwable, genmymodelreverse_java_lang_Exception, Comparable_Score__Interface, Main, card_Card, card_Pack, deck_Deck, deck_Foundations, deck_Stock, deck_Tableau, entities_Comment, entities_Rating, entities_Score, features_History, services_CommentException, services_CommentService_Interface, services_CommentServiceJDBC, services_RatingException, services_RatingService_Interface, services_RatingServiceJDBC, services_ScoreException, services_ScoreService_Interface, services_ScoreServiceJDBC, CommentServiceJDBCTest, CommentServiceTest, RatingServiceTest, ScoreServiceJDBCTest, ScoreServiceTest, SpiderSolitaireTestSuite, genmymodelreverse_java_util_List_Interface, genmymodelreverse_C1, genmymodelreverse_java_util_Date, genmymodelreverse_java_io_Serializable_Interface, genmymodelreverse_java_lang_Comparable_Interface, genmymodelreverse_C11, genmymodelreverse_java_lang_RuntimeException},
    associations={commentService_CommentServiceTest_CommentService_13, foundations_Deck_Foundations_17, ratingService_RatingServiceTest_RatingService_2, tableau8_Tableau_Card_9, tableau7_Tableau_Card_0, tableau3_Tableau_Card_5, tableau6_Tableau_Card_10, tableau1_Tableau_Card_15, scoreService_ScoreServiceTest_ScoreService_6, history_Deck_History_11, tableau2_Tableau_Card_14, pack_Deck_Pack_16, tableau_Deck_Tableau_7, stock_Deck_Stock_8, tableau4_Tableau_Card_12, tableau5_Tableau_Card_1, tableau9_Tableau_Card_3, tableau10_Tableau_Card_4},
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