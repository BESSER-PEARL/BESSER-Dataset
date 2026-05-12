from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class GameController:

    def __init__(self, cardGame: CardGame, gameView: GameBoard, game9: "CardGame" = None, gameBoard10: "GameBoard" = None):
        self.cardGame = cardGame
        self.gameView = gameView
        self.game9 = game9
        self.gameBoard10 = gameBoard10
        
        pass
    @property
    def cardGame(self):
        return self.__cardGame
    @cardGame.setter
    def cardGame(self, cardGame: CardGame):
        self.__cardGame = cardGame

    @property
    def gameView(self):
        return self.__gameView
    @gameView.setter
    def gameView(self, gameView: GameBoard):
        self.__gameView = gameView

    @property
    def gameBoard10(self):
        return self.__gameBoard10
    @gameBoard10.setter
    def gameBoard10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameController__gameBoard10", None)
        self.__gameBoard10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controller11"):
                opp_val = getattr(old_value, "controller11", None)
                if opp_val == self:
                    setattr(old_value, "controller11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controller11"):
                opp_val = getattr(value, "controller11", None)
                setattr(value, "controller11", self)

    @property
    def game9(self):
        return self.__game9
    @game9.setter
    def game9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameController__game9", None)
        self.__game9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "controller8"):
                opp_val = getattr(old_value, "controller8", None)
                if opp_val == self:
                    setattr(old_value, "controller8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "controller8"):
                opp_val = getattr(value, "controller8", None)
                setattr(value, "controller8", self)



class int_Interface:

    pass


class MatchingGame:

    def __init__(self, matches: int):
        self.matches = matches
        
        pass
    @property
    def matches(self):
        return self.__matches
    @matches.setter
    def matches(self, matches: int):
        self.__matches = matches



class TrickGame:

    def __init__(self, trickRules: str):
        self.trickRules = trickRules
        
        pass
    @property
    def trickRules(self):
        return self.__trickRules
    @trickRules.setter
    def trickRules(self, trickRules: str):
        self.__trickRules = trickRules



class SheddingGame:

    pass


class GameBoard:

    def __init__(self, startGame: str, board: str, selectCard: str, drawCard: str, score: str, controller11: "GameController" = None):
        self.startGame = startGame
        self.board = board
        self.selectCard = selectCard
        self.drawCard = drawCard
        self.score = score
        self.controller11 = controller11
        
        pass
    @property
    def startGame(self):
        return self.__startGame
    @startGame.setter
    def startGame(self, startGame: str):
        self.__startGame = startGame

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: str):
        self.__score = score

    @property
    def drawCard(self):
        return self.__drawCard
    @drawCard.setter
    def drawCard(self, drawCard: str):
        self.__drawCard = drawCard

    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: str):
        self.__board = board

    @property
    def selectCard(self):
        return self.__selectCard
    @selectCard.setter
    def selectCard(self, selectCard: str):
        self.__selectCard = selectCard

    @property
    def controller11(self):
        return self.__controller11
    @controller11.setter
    def controller11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameBoard__controller11", None)
        self.__controller11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameBoard10"):
                opp_val = getattr(old_value, "gameBoard10", None)
                if opp_val == self:
                    setattr(old_value, "gameBoard10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameBoard10"):
                opp_val = getattr(value, "gameBoard10", None)
                setattr(value, "gameBoard10", self)



class Player:

    def __init__(self, hand: str, score: int, card3: set["Card"] = None, game5: "CardGame" = None):
        self.hand = hand
        self.score = score
        self.card3 = card3 if card3 is not None else set()
        self.game5 = game5
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: str):
        self.__hand = hand

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def card3(self):
        return self.__card3
    @card3.setter
    def card3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__card3", None)
        self.__card3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player2"):
                    opp_val = getattr(item, "player2", None)
                    
                    if opp_val == self:
                        setattr(item, "player2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player2"):
                    opp_val = getattr(item, "player2", None)
                    
                    setattr(item, "player2", self)
                    

    @property
    def game5(self):
        return self.__game5
    @game5.setter
    def game5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__game5", None)
        self.__game5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player4"):
                opp_val = getattr(old_value, "player4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player4"):
                opp_val = getattr(value, "player4", None)
                if opp_val is None:
                    setattr(value, "player4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class CardGame:

    def __init__(self, players: str, round: int, winner: Player, player4: set["Player"] = None, deck6: "Deck" = None, controller8: "GameController" = None):
        self.players = players
        self.round = round
        self.winner = winner
        self.player4 = player4 if player4 is not None else set()
        self.deck6 = deck6
        self.controller8 = controller8
        
        pass
    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: str):
        self.__players = players

    @property
    def winner(self):
        return self.__winner
    @winner.setter
    def winner(self, winner: Player):
        self.__winner = winner

    @property
    def round(self):
        return self.__round
    @round.setter
    def round(self, round: int):
        self.__round = round

    @property
    def deck6(self):
        return self.__deck6
    @deck6.setter
    def deck6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CardGame__deck6", None)
        self.__deck6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game7"):
                opp_val = getattr(old_value, "game7", None)
                if opp_val == self:
                    setattr(old_value, "game7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game7"):
                opp_val = getattr(value, "game7", None)
                setattr(value, "game7", self)

    @property
    def player4(self):
        return self.__player4
    @player4.setter
    def player4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CardGame__player4", None)
        self.__player4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game5"):
                    opp_val = getattr(item, "game5", None)
                    
                    if opp_val == self:
                        setattr(item, "game5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game5"):
                    opp_val = getattr(item, "game5", None)
                    
                    setattr(item, "game5", self)
                    

    @property
    def controller8(self):
        return self.__controller8
    @controller8.setter
    def controller8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CardGame__controller8", None)
        self.__controller8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game9"):
                opp_val = getattr(old_value, "game9", None)
                if opp_val == self:
                    setattr(old_value, "game9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game9"):
                opp_val = getattr(value, "game9", None)
                setattr(value, "game9", self)



class Deck:

    def __init__(self, deck: str, size: int, card0: set["Card"] = None, game7: "CardGame" = None):
        self.deck = deck
        self.size = size
        self.card0 = card0 if card0 is not None else set()
        self.game7 = game7
        
        pass
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def card0(self):
        return self.__card0
    @card0.setter
    def card0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card0", None)
        self.__card0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck1"):
                    opp_val = getattr(item, "deck1", None)
                    
                    if opp_val == self:
                        setattr(item, "deck1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck1"):
                    opp_val = getattr(item, "deck1", None)
                    
                    setattr(item, "deck1", self)
                    

    @property
    def game7(self):
        return self.__game7
    @game7.setter
    def game7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__game7", None)
        self.__game7 = value
        
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



class Card:

    def __init__(self, face: int, suit: str, deck1: "Deck" = None, player2: "Player" = None):
        self.face = face
        self.suit = suit
        self.deck1 = deck1
        self.player2 = player2
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def face(self):
        return self.__face
    @face.setter
    def face(self, face: int):
        self.__face = face

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__player2", None)
        self.__player2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card3"):
                opp_val = getattr(old_value, "card3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card3"):
                opp_val = getattr(value, "card3", None)
                if opp_val is None:
                    setattr(value, "card3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deck1(self):
        return self.__deck1
    @deck1.setter
    def deck1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck1", None)
        self.__deck1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card0"):
                opp_val = getattr(old_value, "card0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card0"):
                opp_val = getattr(value, "card0", None)
                if opp_val is None:
                    setattr(value, "card0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

