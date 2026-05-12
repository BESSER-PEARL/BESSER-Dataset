from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class genmymodelreverse_java_lang_Throwable:

    pass


class genmymodelreverse_java_lang_RuntimeException:

    pass


class Comparable_Score__Interface:

    pass


class genmymodelreverse_C11:

    pass


class genmymodelreverse_java_lang_Exception:

    pass


class genmymodelreverse_java_lang_Comparable_Interface(ABC):

    pass


class genmymodelreverse_java_io_Serializable_Interface(ABC):

    pass


class genmymodelreverse_java_util_Date:

    pass


class genmymodelreverse_C1:

    pass


class genmymodelreverse_java_util_List_Interface(ABC):

    pass


class SpiderSolitaireTestSuite:

    pass


class ScoreServiceTest:

    def __init__(self, GAME_NAME: str, scoreService1: "services_ScoreService_Interface" = None):
        self.GAME_NAME = GAME_NAME
        self.scoreService1 = scoreService1
        
        pass
    @property
    def GAME_NAME(self):
        return self.__GAME_NAME
    @GAME_NAME.setter
    def GAME_NAME(self, GAME_NAME: str):
        self.__GAME_NAME = GAME_NAME

    @property
    def scoreService1(self):
        return self.__scoreService1
    @scoreService1.setter
    def scoreService1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScoreServiceTest__scoreService1", None)
        self.__scoreService1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scoreservicetest0"):
                opp_val = getattr(old_value, "scoreservicetest0", None)
                if opp_val == self:
                    setattr(old_value, "scoreservicetest0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scoreservicetest0"):
                opp_val = getattr(value, "scoreservicetest0", None)
                setattr(value, "scoreservicetest0", self)



class ScoreServiceJDBCTest:

    def __init__(self, DELETE: str, URL: str, USER: str, PASS: str):
        self.DELETE = DELETE
        self.URL = URL
        self.USER = USER
        self.PASS = PASS
        
        pass
    @property
    def DELETE(self):
        return self.__DELETE
    @DELETE.setter
    def DELETE(self, DELETE: str):
        self.__DELETE = DELETE

    @property
    def PASS(self):
        return self.__PASS
    @PASS.setter
    def PASS(self, PASS: str):
        self.__PASS = PASS

    @property
    def URL(self):
        return self.__URL
    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL

    @property
    def USER(self):
        return self.__USER
    @USER.setter
    def USER(self, USER: str):
        self.__USER = USER



class RatingServiceTest:

    def __init__(self, GAME_NAME: str, TEST_PLAYER: str, TEST_PLAYER_2: str, TEST_PLAYER_3: str, ratingService15: "services_RatingService_Interface" = None):
        self.GAME_NAME = GAME_NAME
        self.TEST_PLAYER = TEST_PLAYER
        self.TEST_PLAYER_2 = TEST_PLAYER_2
        self.TEST_PLAYER_3 = TEST_PLAYER_3
        self.ratingService15 = ratingService15
        
        pass
    @property
    def TEST_PLAYER(self):
        return self.__TEST_PLAYER
    @TEST_PLAYER.setter
    def TEST_PLAYER(self, TEST_PLAYER: str):
        self.__TEST_PLAYER = TEST_PLAYER

    @property
    def GAME_NAME(self):
        return self.__GAME_NAME
    @GAME_NAME.setter
    def GAME_NAME(self, GAME_NAME: str):
        self.__GAME_NAME = GAME_NAME

    @property
    def TEST_PLAYER_2(self):
        return self.__TEST_PLAYER_2
    @TEST_PLAYER_2.setter
    def TEST_PLAYER_2(self, TEST_PLAYER_2: str):
        self.__TEST_PLAYER_2 = TEST_PLAYER_2

    @property
    def TEST_PLAYER_3(self):
        return self.__TEST_PLAYER_3
    @TEST_PLAYER_3.setter
    def TEST_PLAYER_3(self, TEST_PLAYER_3: str):
        self.__TEST_PLAYER_3 = TEST_PLAYER_3

    @property
    def ratingService15(self):
        return self.__ratingService15
    @ratingService15.setter
    def ratingService15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RatingServiceTest__ratingService15", None)
        self.__ratingService15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ratingservicetest14"):
                opp_val = getattr(old_value, "ratingservicetest14", None)
                if opp_val == self:
                    setattr(old_value, "ratingservicetest14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ratingservicetest14"):
                opp_val = getattr(value, "ratingservicetest14", None)
                setattr(value, "ratingservicetest14", self)



class CommentServiceTest:

    def __init__(self, GAME_NAME: str, PLAYER_NAME: str, commentService11: "services_CommentService_Interface" = None):
        self.GAME_NAME = GAME_NAME
        self.PLAYER_NAME = PLAYER_NAME
        self.commentService11 = commentService11
        
        pass
    @property
    def PLAYER_NAME(self):
        return self.__PLAYER_NAME
    @PLAYER_NAME.setter
    def PLAYER_NAME(self, PLAYER_NAME: str):
        self.__PLAYER_NAME = PLAYER_NAME

    @property
    def GAME_NAME(self):
        return self.__GAME_NAME
    @GAME_NAME.setter
    def GAME_NAME(self, GAME_NAME: str):
        self.__GAME_NAME = GAME_NAME

    @property
    def commentService11(self):
        return self.__commentService11
    @commentService11.setter
    def commentService11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CommentServiceTest__commentService11", None)
        self.__commentService11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commentservicetest10"):
                opp_val = getattr(old_value, "commentservicetest10", None)
                if opp_val == self:
                    setattr(old_value, "commentservicetest10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commentservicetest10"):
                opp_val = getattr(value, "commentservicetest10", None)
                setattr(value, "commentservicetest10", self)



class CommentServiceJDBCTest:

    def __init__(self, DELETE: str, URL: str, USER: str, PASS: str):
        self.DELETE = DELETE
        self.URL = URL
        self.USER = USER
        self.PASS = PASS
        
        pass
    @property
    def PASS(self):
        return self.__PASS
    @PASS.setter
    def PASS(self, PASS: str):
        self.__PASS = PASS

    @property
    def USER(self):
        return self.__USER
    @USER.setter
    def USER(self, USER: str):
        self.__USER = USER

    @property
    def DELETE(self):
        return self.__DELETE
    @DELETE.setter
    def DELETE(self, DELETE: str):
        self.__DELETE = DELETE

    @property
    def URL(self):
        return self.__URL
    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL



class services_ScoreServiceJDBC:

    def __init__(self, URL: str, USER: str, PASSWORD: str, INSERT_SCORE: str, SELECT_SCORE: str):
        self.URL = URL
        self.USER = USER
        self.PASSWORD = PASSWORD
        self.INSERT_SCORE = INSERT_SCORE
        self.SELECT_SCORE = SELECT_SCORE
        
        pass
    @property
    def PASSWORD(self):
        return self.__PASSWORD
    @PASSWORD.setter
    def PASSWORD(self, PASSWORD: str):
        self.__PASSWORD = PASSWORD

    @property
    def SELECT_SCORE(self):
        return self.__SELECT_SCORE
    @SELECT_SCORE.setter
    def SELECT_SCORE(self, SELECT_SCORE: str):
        self.__SELECT_SCORE = SELECT_SCORE

    @property
    def URL(self):
        return self.__URL
    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL

    @property
    def USER(self):
        return self.__USER
    @USER.setter
    def USER(self, USER: str):
        self.__USER = USER

    @property
    def INSERT_SCORE(self):
        return self.__INSERT_SCORE
    @INSERT_SCORE.setter
    def INSERT_SCORE(self, INSERT_SCORE: str):
        self.__INSERT_SCORE = INSERT_SCORE



class services_ScoreService_Interface:

    pass


class services_ScoreException:

    pass


class services_RatingServiceJDBC:

    def __init__(self, URL: str, USER: str, PASSWORD: str, INSERT_RATING: str, SELECT_RATING: str, SELECT_AVERAGE_RATING: str):
        self.URL = URL
        self.USER = USER
        self.PASSWORD = PASSWORD
        self.INSERT_RATING = INSERT_RATING
        self.SELECT_RATING = SELECT_RATING
        self.SELECT_AVERAGE_RATING = SELECT_AVERAGE_RATING
        
        pass
    @property
    def USER(self):
        return self.__USER
    @USER.setter
    def USER(self, USER: str):
        self.__USER = USER

    @property
    def URL(self):
        return self.__URL
    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL

    @property
    def SELECT_RATING(self):
        return self.__SELECT_RATING
    @SELECT_RATING.setter
    def SELECT_RATING(self, SELECT_RATING: str):
        self.__SELECT_RATING = SELECT_RATING

    @property
    def INSERT_RATING(self):
        return self.__INSERT_RATING
    @INSERT_RATING.setter
    def INSERT_RATING(self, INSERT_RATING: str):
        self.__INSERT_RATING = INSERT_RATING

    @property
    def PASSWORD(self):
        return self.__PASSWORD
    @PASSWORD.setter
    def PASSWORD(self, PASSWORD: str):
        self.__PASSWORD = PASSWORD

    @property
    def SELECT_AVERAGE_RATING(self):
        return self.__SELECT_AVERAGE_RATING
    @SELECT_AVERAGE_RATING.setter
    def SELECT_AVERAGE_RATING(self, SELECT_AVERAGE_RATING: str):
        self.__SELECT_AVERAGE_RATING = SELECT_AVERAGE_RATING



class services_RatingService_Interface:

    pass


class services_RatingException:

    pass


class services_CommentServiceJDBC:

    def __init__(self, URL: str, USER: str, PASSWORD: str, INSERT_COMMENT: str, SELECT_COMMENTS: str):
        self.URL = URL
        self.USER = USER
        self.PASSWORD = PASSWORD
        self.INSERT_COMMENT = INSERT_COMMENT
        self.SELECT_COMMENTS = SELECT_COMMENTS
        
        pass
    @property
    def SELECT_COMMENTS(self):
        return self.__SELECT_COMMENTS
    @SELECT_COMMENTS.setter
    def SELECT_COMMENTS(self, SELECT_COMMENTS: str):
        self.__SELECT_COMMENTS = SELECT_COMMENTS

    @property
    def URL(self):
        return self.__URL
    @URL.setter
    def URL(self, URL: str):
        self.__URL = URL

    @property
    def PASSWORD(self):
        return self.__PASSWORD
    @PASSWORD.setter
    def PASSWORD(self, PASSWORD: str):
        self.__PASSWORD = PASSWORD

    @property
    def INSERT_COMMENT(self):
        return self.__INSERT_COMMENT
    @INSERT_COMMENT.setter
    def INSERT_COMMENT(self, INSERT_COMMENT: str):
        self.__INSERT_COMMENT = INSERT_COMMENT

    @property
    def USER(self):
        return self.__USER
    @USER.setter
    def USER(self, USER: str):
        self.__USER = USER



class services_CommentService_Interface:

    pass


class services_CommentException:

    pass


class features_History:

    def __init__(self, revertList: int, deck2: "deck_Deck" = None):
        self.revertList = revertList
        self.deck2 = deck2
        
        pass
    @property
    def revertList(self):
        return self.__revertList
    @revertList.setter
    def revertList(self, revertList: int):
        self.__revertList = revertList

    @property
    def deck2(self):
        return self.__deck2
    @deck2.setter
    def deck2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_features_History__deck2", None)
        self.__deck2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "history3"):
                opp_val = getattr(old_value, "history3", None)
                if opp_val == self:
                    setattr(old_value, "history3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "history3"):
                opp_val = getattr(value, "history3", None)
                setattr(value, "history3", self)



class entities_Score:

    def __init__(self, game: str, player: str, points: int, playedOn: genmymodelreverse_java_util_Date):
        self.game = game
        self.player = player
        self.points = points
        self.playedOn = playedOn
        
        pass
    @property
    def playedOn(self):
        return self.__playedOn
    @playedOn.setter
    def playedOn(self, playedOn: genmymodelreverse_java_util_Date):
        self.__playedOn = playedOn

    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: str):
        self.__player = player

    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, game: str):
        self.__game = game



class entities_Rating:

    def __init__(self, player: str, game: str, rating: int, ratedon: genmymodelreverse_java_util_Date):
        self.player = player
        self.game = game
        self.rating = rating
        self.ratedon = ratedon
        
        pass
    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, game: str):
        self.__game = game

    @property
    def rating(self):
        return self.__rating
    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating

    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: str):
        self.__player = player

    @property
    def ratedon(self):
        return self.__ratedon
    @ratedon.setter
    def ratedon(self, ratedon: genmymodelreverse_java_util_Date):
        self.__ratedon = ratedon



class entities_Comment:

    def __init__(self, player: str, game: str, comment: str, commentedOn: genmymodelreverse_java_util_Date):
        self.player = player
        self.game = game
        self.comment = comment
        self.commentedOn = commentedOn
        
        pass
    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, game: str):
        self.__game = game

    @property
    def commentedOn(self):
        return self.__commentedOn
    @commentedOn.setter
    def commentedOn(self, commentedOn: genmymodelreverse_java_util_Date):
        self.__commentedOn = commentedOn

    @property
    def comment(self):
        return self.__comment
    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: str):
        self.__player = player



class deck_Tableau:

    def __init__(self, columns: str, tableau25: set["card_Card"] = None, deck8: "deck_Deck" = None, tableau817: set["card_Card"] = None, tableau719: set["card_Card"] = None, tableau321: set["card_Card"] = None, tableau623: set["card_Card"] = None, tableau125: set["card_Card"] = None, tableau429: set["card_Card"] = None, tableau531: set["card_Card"] = None, tableau933: set["card_Card"] = None, tableau1035: set["card_Card"] = None):
        self.columns = columns
        self.tableau25 = tableau25 if tableau25 is not None else set()
        self.deck8 = deck8
        self.tableau817 = tableau817 if tableau817 is not None else set()
        self.tableau719 = tableau719 if tableau719 is not None else set()
        self.tableau321 = tableau321 if tableau321 is not None else set()
        self.tableau623 = tableau623 if tableau623 is not None else set()
        self.tableau125 = tableau125 if tableau125 is not None else set()
        self.tableau429 = tableau429 if tableau429 is not None else set()
        self.tableau531 = tableau531 if tableau531 is not None else set()
        self.tableau933 = tableau933 if tableau933 is not None else set()
        self.tableau1035 = tableau1035 if tableau1035 is not None else set()
        
        pass
    @property
    def columns(self):
        return self.__columns
    @columns.setter
    def columns(self, columns: str):
        self.__columns = columns

    @property
    def tableau719(self):
        return self.__tableau719
    @tableau719.setter
    def tableau719(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__tableau719", None)
        self.__tableau719 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tableau18"):
                    opp_val = getattr(item, "tableau18", None)
                    
                    if opp_val == self:
                        setattr(item, "tableau18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tableau18"):
                    opp_val = getattr(item, "tableau18", None)
                    
                    setattr(item, "tableau18", self)
                    

    @property
    def tableau429(self):
        return self.__tableau429
    @tableau429.setter
    def tableau429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__tableau429", None)
        self.__tableau429 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tableau28"):
                    opp_val = getattr(item, "tableau28", None)
                    
                    if opp_val == self:
                        setattr(item, "tableau28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tableau28"):
                    opp_val = getattr(item, "tableau28", None)
                    
                    setattr(item, "tableau28", self)
                    

    @property
    def tableau1035(self):
        return self.__tableau1035
    @tableau1035.setter
    def tableau1035(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__tableau1035", None)
        self.__tableau1035 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tableau34"):
                    opp_val = getattr(item, "tableau34", None)
                    
                    if opp_val == self:
                        setattr(item, "tableau34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tableau34"):
                    opp_val = getattr(item, "tableau34", None)
                    
                    setattr(item, "tableau34", self)
                    

    @property
    def deck8(self):
        return self.__deck8
    @deck8.setter
    def deck8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__deck8", None)
        self.__deck8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau9"):
                opp_val = getattr(old_value, "tableau9", None)
                if opp_val == self:
                    setattr(old_value, "tableau9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau9"):
                opp_val = getattr(value, "tableau9", None)
                setattr(value, "tableau9", self)

    @property
    def tableau321(self):
        return self.__tableau321
    @tableau321.setter
    def tableau321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__tableau321", None)
        self.__tableau321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tableau20"):
                    opp_val = getattr(item, "tableau20", None)
                    
                    if opp_val == self:
                        setattr(item, "tableau20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tableau20"):
                    opp_val = getattr(item, "tableau20", None)
                    
                    setattr(item, "tableau20", self)
                    

    @property
    def tableau623(self):
        return self.__tableau623
    @tableau623.setter
    def tableau623(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__tableau623", None)
        self.__tableau623 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tableau22"):
                    opp_val = getattr(item, "tableau22", None)
                    
                    if opp_val == self:
                        setattr(item, "tableau22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tableau22"):
                    opp_val = getattr(item, "tableau22", None)
                    
                    setattr(item, "tableau22", self)
                    

    @property
    def tableau125(self):
        return self.__tableau125
    @tableau125.setter
    def tableau125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__tableau125", None)
        self.__tableau125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tableau24"):
                    opp_val = getattr(item, "tableau24", None)
                    
                    if opp_val == self:
                        setattr(item, "tableau24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tableau24"):
                    opp_val = getattr(item, "tableau24", None)
                    
                    setattr(item, "tableau24", self)
                    

    @property
    def tableau933(self):
        return self.__tableau933
    @tableau933.setter
    def tableau933(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__tableau933", None)
        self.__tableau933 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tableau32"):
                    opp_val = getattr(item, "tableau32", None)
                    
                    if opp_val == self:
                        setattr(item, "tableau32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tableau32"):
                    opp_val = getattr(item, "tableau32", None)
                    
                    setattr(item, "tableau32", self)
                    

    @property
    def tableau817(self):
        return self.__tableau817
    @tableau817.setter
    def tableau817(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__tableau817", None)
        self.__tableau817 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tableau16"):
                    opp_val = getattr(item, "tableau16", None)
                    
                    if opp_val == self:
                        setattr(item, "tableau16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tableau16"):
                    opp_val = getattr(item, "tableau16", None)
                    
                    setattr(item, "tableau16", self)
                    

    @property
    def tableau25(self):
        return self.__tableau25
    @tableau25.setter
    def tableau25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__tableau25", None)
        self.__tableau25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tableau4"):
                    opp_val = getattr(item, "tableau4", None)
                    
                    if opp_val == self:
                        setattr(item, "tableau4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tableau4"):
                    opp_val = getattr(item, "tableau4", None)
                    
                    setattr(item, "tableau4", self)
                    

    @property
    def tableau531(self):
        return self.__tableau531
    @tableau531.setter
    def tableau531(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Tableau__tableau531", None)
        self.__tableau531 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tableau30"):
                    opp_val = getattr(item, "tableau30", None)
                    
                    if opp_val == self:
                        setattr(item, "tableau30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tableau30"):
                    opp_val = getattr(item, "tableau30", None)
                    
                    setattr(item, "tableau30", self)
                    



class deck_Stock:

    def __init__(self, stock: str, STARTING_INDEX: int, deck26: "deck_Deck" = None):
        self.stock = stock
        self.STARTING_INDEX = STARTING_INDEX
        self.deck26 = deck26
        
        pass
    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock: str):
        self.__stock = stock

    @property
    def STARTING_INDEX(self):
        return self.__STARTING_INDEX
    @STARTING_INDEX.setter
    def STARTING_INDEX(self, STARTING_INDEX: int):
        self.__STARTING_INDEX = STARTING_INDEX

    @property
    def deck26(self):
        return self.__deck26
    @deck26.setter
    def deck26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Stock__deck26", None)
        self.__deck26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "stock27"):
                opp_val = getattr(old_value, "stock27", None)
                if opp_val == self:
                    setattr(old_value, "stock27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "stock27"):
                opp_val = getattr(value, "stock27", None)
                setattr(value, "stock27", self)



class deck_Foundations:

    def __init__(self, foundationList: str, deck12: "deck_Deck" = None):
        self.foundationList = foundationList
        self.deck12 = deck12
        
        pass
    @property
    def foundationList(self):
        return self.__foundationList
    @foundationList.setter
    def foundationList(self, foundationList: str):
        self.__foundationList = foundationList

    @property
    def deck12(self):
        return self.__deck12
    @deck12.setter
    def deck12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Foundations__deck12", None)
        self.__deck12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "foundations13"):
                opp_val = getattr(old_value, "foundations13", None)
                if opp_val == self:
                    setattr(old_value, "foundations13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "foundations13"):
                opp_val = getattr(value, "foundations13", None)
                setattr(value, "foundations13", self)



class deck_Deck:

    def __init__(self, removeItemFromArrayIndex: int, score: int, stepCounter: int, inputDestinationRow: int, foundationIndex: int, history3: "features_History" = None, pack7: "card_Deck" = None, tableau9: "deck_Tableau" = None, foundations13: "deck_Foundations" = None, stock27: "deck_Stock" = None):
        self.removeItemFromArrayIndex = removeItemFromArrayIndex
        self.score = score
        self.stepCounter = stepCounter
        self.inputDestinationRow = inputDestinationRow
        self.foundationIndex = foundationIndex
        self.history3 = history3
        self.pack7 = pack7
        self.tableau9 = tableau9
        self.foundations13 = foundations13
        self.stock27 = stock27
        
        pass
    @property
    def stepCounter(self):
        return self.__stepCounter
    @stepCounter.setter
    def stepCounter(self, stepCounter: int):
        self.__stepCounter = stepCounter

    @property
    def removeItemFromArrayIndex(self):
        return self.__removeItemFromArrayIndex
    @removeItemFromArrayIndex.setter
    def removeItemFromArrayIndex(self, removeItemFromArrayIndex: int):
        self.__removeItemFromArrayIndex = removeItemFromArrayIndex

    @property
    def inputDestinationRow(self):
        return self.__inputDestinationRow
    @inputDestinationRow.setter
    def inputDestinationRow(self, inputDestinationRow: int):
        self.__inputDestinationRow = inputDestinationRow

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def foundationIndex(self):
        return self.__foundationIndex
    @foundationIndex.setter
    def foundationIndex(self, foundationIndex: int):
        self.__foundationIndex = foundationIndex

    @property
    def stock27(self):
        return self.__stock27
    @stock27.setter
    def stock27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Deck__stock27", None)
        self.__stock27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck26"):
                opp_val = getattr(old_value, "deck26", None)
                if opp_val == self:
                    setattr(old_value, "deck26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck26"):
                opp_val = getattr(value, "deck26", None)
                setattr(value, "deck26", self)

    @property
    def pack7(self):
        return self.__pack7
    @pack7.setter
    def pack7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Deck__pack7", None)
        self.__pack7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck6"):
                opp_val = getattr(old_value, "deck6", None)
                if opp_val == self:
                    setattr(old_value, "deck6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck6"):
                opp_val = getattr(value, "deck6", None)
                setattr(value, "deck6", self)

    @property
    def history3(self):
        return self.__history3
    @history3.setter
    def history3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Deck__history3", None)
        self.__history3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck2"):
                opp_val = getattr(old_value, "deck2", None)
                if opp_val == self:
                    setattr(old_value, "deck2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck2"):
                opp_val = getattr(value, "deck2", None)
                setattr(value, "deck2", self)

    @property
    def foundations13(self):
        return self.__foundations13
    @foundations13.setter
    def foundations13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Deck__foundations13", None)
        self.__foundations13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck12"):
                opp_val = getattr(old_value, "deck12", None)
                if opp_val == self:
                    setattr(old_value, "deck12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck12"):
                opp_val = getattr(value, "deck12", None)
                setattr(value, "deck12", self)

    @property
    def tableau9(self):
        return self.__tableau9
    @tableau9.setter
    def tableau9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_deck_Deck__tableau9", None)
        self.__tableau9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck8"):
                opp_val = getattr(old_value, "deck8", None)
                if opp_val == self:
                    setattr(old_value, "deck8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck8"):
                opp_val = getattr(value, "deck8", None)
                setattr(value, "deck8", self)



class card_Deck:

    def __init__(self, cardPack: str, deck6: "deck_Deck" = None):
        self.cardPack = cardPack
        self.deck6 = deck6
        
        pass
    @property
    def cardPack(self):
        return self.__cardPack
    @cardPack.setter
    def cardPack(self, cardPack: str):
        self.__cardPack = cardPack

    @property
    def deck6(self):
        return self.__deck6
    @deck6.setter
    def deck6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Deck__deck6", None)
        self.__deck6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pack7"):
                opp_val = getattr(old_value, "pack7", None)
                if opp_val == self:
                    setattr(old_value, "pack7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pack7"):
                opp_val = getattr(value, "pack7", None)
                setattr(value, "pack7", self)



class card_Card:

    def __init__(self, rank: int, flipped: bool, tableau4: "deck_Tableau" = None, tableau16: "deck_Tableau" = None, tableau18: "deck_Tableau" = None, tableau20: "deck_Tableau" = None, tableau22: "deck_Tableau" = None, tableau24: "deck_Tableau" = None, tableau28: "deck_Tableau" = None, tableau30: "deck_Tableau" = None, tableau32: "deck_Tableau" = None, tableau34: "deck_Tableau" = None):
        self.rank = rank
        self.flipped = flipped
        self.tableau4 = tableau4
        self.tableau16 = tableau16
        self.tableau18 = tableau18
        self.tableau20 = tableau20
        self.tableau22 = tableau22
        self.tableau24 = tableau24
        self.tableau28 = tableau28
        self.tableau30 = tableau30
        self.tableau32 = tableau32
        self.tableau34 = tableau34
        
        pass
    @property
    def flipped(self):
        return self.__flipped
    @flipped.setter
    def flipped(self, flipped: bool):
        self.__flipped = flipped

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def tableau4(self):
        return self.__tableau4
    @tableau4.setter
    def tableau4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Card__tableau4", None)
        self.__tableau4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau25"):
                opp_val = getattr(old_value, "tableau25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau25"):
                opp_val = getattr(value, "tableau25", None)
                if opp_val is None:
                    setattr(value, "tableau25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tableau24(self):
        return self.__tableau24
    @tableau24.setter
    def tableau24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Card__tableau24", None)
        self.__tableau24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau125"):
                opp_val = getattr(old_value, "tableau125", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau125"):
                opp_val = getattr(value, "tableau125", None)
                if opp_val is None:
                    setattr(value, "tableau125", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tableau20(self):
        return self.__tableau20
    @tableau20.setter
    def tableau20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Card__tableau20", None)
        self.__tableau20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau321"):
                opp_val = getattr(old_value, "tableau321", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau321"):
                opp_val = getattr(value, "tableau321", None)
                if opp_val is None:
                    setattr(value, "tableau321", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tableau32(self):
        return self.__tableau32
    @tableau32.setter
    def tableau32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Card__tableau32", None)
        self.__tableau32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau933"):
                opp_val = getattr(old_value, "tableau933", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau933"):
                opp_val = getattr(value, "tableau933", None)
                if opp_val is None:
                    setattr(value, "tableau933", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tableau30(self):
        return self.__tableau30
    @tableau30.setter
    def tableau30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Card__tableau30", None)
        self.__tableau30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau531"):
                opp_val = getattr(old_value, "tableau531", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau531"):
                opp_val = getattr(value, "tableau531", None)
                if opp_val is None:
                    setattr(value, "tableau531", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tableau34(self):
        return self.__tableau34
    @tableau34.setter
    def tableau34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Card__tableau34", None)
        self.__tableau34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau1035"):
                opp_val = getattr(old_value, "tableau1035", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau1035"):
                opp_val = getattr(value, "tableau1035", None)
                if opp_val is None:
                    setattr(value, "tableau1035", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tableau18(self):
        return self.__tableau18
    @tableau18.setter
    def tableau18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Card__tableau18", None)
        self.__tableau18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau719"):
                opp_val = getattr(old_value, "tableau719", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau719"):
                opp_val = getattr(value, "tableau719", None)
                if opp_val is None:
                    setattr(value, "tableau719", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tableau28(self):
        return self.__tableau28
    @tableau28.setter
    def tableau28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Card__tableau28", None)
        self.__tableau28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau429"):
                opp_val = getattr(old_value, "tableau429", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau429"):
                opp_val = getattr(value, "tableau429", None)
                if opp_val is None:
                    setattr(value, "tableau429", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tableau16(self):
        return self.__tableau16
    @tableau16.setter
    def tableau16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Card__tableau16", None)
        self.__tableau16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau817"):
                opp_val = getattr(old_value, "tableau817", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau817"):
                opp_val = getattr(value, "tableau817", None)
                if opp_val is None:
                    setattr(value, "tableau817", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tableau22(self):
        return self.__tableau22
    @tableau22.setter
    def tableau22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_card_Card__tableau22", None)
        self.__tableau22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tableau623"):
                opp_val = getattr(old_value, "tableau623", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tableau623"):
                opp_val = getattr(value, "tableau623", None)
                if opp_val is None:
                    setattr(value, "tableau623", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Main:

    pass
