from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################







class UseCase_UseCase:

    pass


class User_Actor:

    pass





class JButton:

    pass


class Strategy:

    def __init__(self, game: BlackjackGame, blackjack9: "BlackjackGame" = None):
        self.game = game
        self.blackjack9 = blackjack9
        
        pass
    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, game: BlackjackGame):
        self.__game = game

    @property
    def blackjack9(self):
        return self.__blackjack9
    @blackjack9.setter
    def blackjack9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Strategy__blackjack9", None)
        self.__blackjack9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "strategy8"):
                opp_val = getattr(old_value, "strategy8", None)
                if opp_val == self:
                    setattr(old_value, "strategy8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "strategy8"):
                opp_val = getattr(value, "strategy8", None)
                setattr(value, "strategy8", self)



class Card:

    def __init__(self, name: str, avatar: str, valueSoft: str, valueHard: str, suit: str, rank: str, Count: int, deck29: "Deck" = None, hand27: "Hand" = None):
        self.name = name
        self.avatar = avatar
        self.valueSoft = valueSoft
        self.valueHard = valueHard
        self.suit = suit
        self.rank = rank
        self.Count = Count
        self.deck29 = deck29
        self.hand27 = hand27
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def valueHard(self):
        return self.__valueHard
    @valueHard.setter
    def valueHard(self, valueHard: str):
        self.__valueHard = valueHard

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def valueSoft(self):
        return self.__valueSoft
    @valueSoft.setter
    def valueSoft(self, valueSoft: str):
        self.__valueSoft = valueSoft

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

    @property
    def avatar(self):
        return self.__avatar
    @avatar.setter
    def avatar(self, avatar: str):
        self.__avatar = avatar

    @property
    def Count(self):
        return self.__Count
    @Count.setter
    def Count(self, Count: int):
        self.__Count = Count

    @property
    def hand27(self):
        return self.__hand27
    @hand27.setter
    def hand27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__hand27", None)
        self.__hand27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card26"):
                opp_val = getattr(old_value, "card26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card26"):
                opp_val = getattr(value, "card26", None)
                if opp_val is None:
                    setattr(value, "card26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deck29(self):
        return self.__deck29
    @deck29.setter
    def deck29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck29", None)
        self.__deck29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card28"):
                opp_val = getattr(old_value, "card28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card28"):
                opp_val = getattr(value, "card28", None)
                if opp_val is None:
                    setattr(value, "card28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class LoginView:

    def __init__(self, user: Profile, profile0: "Profile" = None, gameLauncher3: "GameLauncher" = None):
        self.user = user
        self.profile0 = profile0
        self.gameLauncher3 = gameLauncher3
        
        pass
    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: Profile):
        self.__user = user

    @property
    def profile0(self):
        return self.__profile0
    @profile0.setter
    def profile0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LoginView__profile0", None)
        self.__profile0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loginView1"):
                opp_val = getattr(old_value, "loginView1", None)
                if opp_val == self:
                    setattr(old_value, "loginView1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loginView1"):
                opp_val = getattr(value, "loginView1", None)
                setattr(value, "loginView1", self)

    @property
    def gameLauncher3(self):
        return self.__gameLauncher3
    @gameLauncher3.setter
    def gameLauncher3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LoginView__gameLauncher3", None)
        self.__gameLauncher3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loginView2"):
                opp_val = getattr(old_value, "loginView2", None)
                if opp_val == self:
                    setattr(old_value, "loginView2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loginView2"):
                opp_val = getattr(value, "loginView2", None)
                setattr(value, "loginView2", self)



class GameLauncher:

    def __init__(self, blackjack: BlackjackGame, login: LoginView, loginView2: "LoginView" = None):
        self.blackjack = blackjack
        self.login = login
        self.loginView2 = loginView2
        
        pass
    @property
    def blackjack(self):
        return self.__blackjack
    @blackjack.setter
    def blackjack(self, blackjack: BlackjackGame):
        self.__blackjack = blackjack

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: LoginView):
        self.__login = login

    @property
    def loginView2(self):
        return self.__loginView2
    @loginView2.setter
    def loginView2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameLauncher__loginView2", None)
        self.__loginView2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameLauncher3"):
                opp_val = getattr(old_value, "gameLauncher3", None)
                if opp_val == self:
                    setattr(old_value, "gameLauncher3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameLauncher3"):
                opp_val = getattr(value, "gameLauncher3", None)
                setattr(value, "gameLauncher3", self)



class Profile:

    def __init__(self, username: str, money: int, player21: "Player" = None, loginView1: "LoginView" = None, blackjack4: "BlackjackGame" = None):
        self.username = username
        self.money = money
        self.player21 = player21
        self.loginView1 = loginView1
        self.blackjack4 = blackjack4
        
        pass
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: int):
        self.__money = money

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def loginView1(self):
        return self.__loginView1
    @loginView1.setter
    def loginView1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__loginView1", None)
        self.__loginView1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile0"):
                opp_val = getattr(old_value, "profile0", None)
                if opp_val == self:
                    setattr(old_value, "profile0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile0"):
                opp_val = getattr(value, "profile0", None)
                setattr(value, "profile0", self)

    @property
    def player21(self):
        return self.__player21
    @player21.setter
    def player21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__player21", None)
        self.__player21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile220"):
                opp_val = getattr(old_value, "profile220", None)
                if opp_val == self:
                    setattr(old_value, "profile220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile220"):
                opp_val = getattr(value, "profile220", None)
                setattr(value, "profile220", self)

    @property
    def blackjack4(self):
        return self.__blackjack4
    @blackjack4.setter
    def blackjack4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Profile__blackjack4", None)
        self.__blackjack4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "profile5"):
                opp_val = getattr(old_value, "profile5", None)
                if opp_val == self:
                    setattr(old_value, "profile5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "profile5"):
                opp_val = getattr(value, "profile5", None)
                setattr(value, "profile5", self)



class Hand:

    def __init__(self, cards: Card, total: int, dealer23: "Dealer" = None, player25: "Player" = None, card26: set["Card"] = None):
        self.cards = cards
        self.total = total
        self.dealer23 = dealer23
        self.player25 = player25
        self.card26 = card26 if card26 is not None else set()
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: int):
        self.__total = total

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: Card):
        self.__cards = cards

    @property
    def player25(self):
        return self.__player25
    @player25.setter
    def player25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__player25", None)
        self.__player25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand24"):
                opp_val = getattr(old_value, "hand24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand24"):
                opp_val = getattr(value, "hand24", None)
                if opp_val is None:
                    setattr(value, "hand24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def card26(self):
        return self.__card26
    @card26.setter
    def card26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__card26", None)
        self.__card26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand27"):
                    opp_val = getattr(item, "hand27", None)
                    
                    if opp_val == self:
                        setattr(item, "hand27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand27"):
                    opp_val = getattr(item, "hand27", None)
                    
                    setattr(item, "hand27", self)
                    

    @property
    def dealer23(self):
        return self.__dealer23
    @dealer23.setter
    def dealer23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__dealer23", None)
        self.__dealer23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand22"):
                opp_val = getattr(old_value, "hand22", None)
                if opp_val == self:
                    setattr(old_value, "hand22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand22"):
                opp_val = getattr(value, "hand22", None)
                setattr(value, "hand22", self)



class Deck:

    def __init__(self, cards: Card, blackjack17: "BlackjackGame" = None, card28: set["Card"] = None):
        self.cards = cards
        self.blackjack17 = blackjack17
        self.card28 = card28 if card28 is not None else set()
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: Card):
        self.__cards = cards

    @property
    def card28(self):
        return self.__card28
    @card28.setter
    def card28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card28", None)
        self.__card28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck29"):
                    opp_val = getattr(item, "deck29", None)
                    
                    if opp_val == self:
                        setattr(item, "deck29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck29"):
                    opp_val = getattr(item, "deck29", None)
                    
                    setattr(item, "deck29", self)
                    

    @property
    def blackjack17(self):
        return self.__blackjack17
    @blackjack17.setter
    def blackjack17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__blackjack17", None)
        self.__blackjack17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck216"):
                opp_val = getattr(old_value, "deck216", None)
                if opp_val == self:
                    setattr(old_value, "deck216", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck216"):
                opp_val = getattr(value, "deck216", None)
                setattr(value, "deck216", self)



class BlackjackGame:

    def __init__(self, deck: Deck, dealer: Dealer, player: Player, bet: int, player13: "Player" = None, dealer15: "Dealer" = None, deck216: "Deck" = None, profile5: "Profile" = None, gameView6: "GameView" = None, strategy8: "Strategy" = None):
        self.deck = deck
        self.dealer = dealer
        self.player = player
        self.bet = bet
        self.player13 = player13
        self.dealer15 = dealer15
        self.deck216 = deck216
        self.profile5 = profile5
        self.gameView6 = gameView6
        self.strategy8 = strategy8
        
        pass
    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: Player):
        self.__player = player

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck

    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: int):
        self.__bet = bet

    @property
    def dealer(self):
        return self.__dealer
    @dealer.setter
    def dealer(self, dealer: Dealer):
        self.__dealer = dealer

    @property
    def gameView6(self):
        return self.__gameView6
    @gameView6.setter
    def gameView6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__gameView6", None)
        self.__gameView6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack7"):
                opp_val = getattr(old_value, "blackjack7", None)
                if opp_val == self:
                    setattr(old_value, "blackjack7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack7"):
                opp_val = getattr(value, "blackjack7", None)
                setattr(value, "blackjack7", self)

    @property
    def dealer15(self):
        return self.__dealer15
    @dealer15.setter
    def dealer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__dealer15", None)
        self.__dealer15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack14"):
                opp_val = getattr(old_value, "blackjack14", None)
                if opp_val == self:
                    setattr(old_value, "blackjack14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack14"):
                opp_val = getattr(value, "blackjack14", None)
                setattr(value, "blackjack14", self)

    @property
    def profile5(self):
        return self.__profile5
    @profile5.setter
    def profile5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__profile5", None)
        self.__profile5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack4"):
                opp_val = getattr(old_value, "blackjack4", None)
                if opp_val == self:
                    setattr(old_value, "blackjack4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack4"):
                opp_val = getattr(value, "blackjack4", None)
                setattr(value, "blackjack4", self)

    @property
    def player13(self):
        return self.__player13
    @player13.setter
    def player13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__player13", None)
        self.__player13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack12"):
                opp_val = getattr(old_value, "blackjack12", None)
                if opp_val == self:
                    setattr(old_value, "blackjack12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack12"):
                opp_val = getattr(value, "blackjack12", None)
                setattr(value, "blackjack12", self)

    @property
    def deck216(self):
        return self.__deck216
    @deck216.setter
    def deck216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__deck216", None)
        self.__deck216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack17"):
                opp_val = getattr(old_value, "blackjack17", None)
                if opp_val == self:
                    setattr(old_value, "blackjack17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack17"):
                opp_val = getattr(value, "blackjack17", None)
                setattr(value, "blackjack17", self)

    @property
    def strategy8(self):
        return self.__strategy8
    @strategy8.setter
    def strategy8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackjackGame__strategy8", None)
        self.__strategy8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "blackjack9"):
                opp_val = getattr(old_value, "blackjack9", None)
                if opp_val == self:
                    setattr(old_value, "blackjack9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "blackjack9"):
                opp_val = getattr(value, "blackjack9", None)
                setattr(value, "blackjack9", self)



class PlayerView:

    def __init__(self, cardLabels: JLabel, cardTotal: JLabel, busted: JLabel, moneyBox: JLabel, status: JLabel, player: BasePlayer, gameView10: "GameView" = None, basePlayer19: "BasePlayer" = None):
        self.cardLabels = cardLabels
        self.cardTotal = cardTotal
        self.busted = busted
        self.moneyBox = moneyBox
        self.status = status
        self.player = player
        self.gameView10 = gameView10
        self.basePlayer19 = basePlayer19
        
        pass
    @property
    def cardLabels(self):
        return self.__cardLabels
    @cardLabels.setter
    def cardLabels(self, cardLabels: JLabel):
        self.__cardLabels = cardLabels

    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: BasePlayer):
        self.__player = player

    @property
    def busted(self):
        return self.__busted
    @busted.setter
    def busted(self, busted: JLabel):
        self.__busted = busted

    @property
    def moneyBox(self):
        return self.__moneyBox
    @moneyBox.setter
    def moneyBox(self, moneyBox: JLabel):
        self.__moneyBox = moneyBox

    @property
    def cardTotal(self):
        return self.__cardTotal
    @cardTotal.setter
    def cardTotal(self, cardTotal: JLabel):
        self.__cardTotal = cardTotal

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: JLabel):
        self.__status = status

    @property
    def basePlayer19(self):
        return self.__basePlayer19
    @basePlayer19.setter
    def basePlayer19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlayerView__basePlayer19", None)
        self.__basePlayer19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playerView18"):
                opp_val = getattr(old_value, "playerView18", None)
                if opp_val == self:
                    setattr(old_value, "playerView18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playerView18"):
                opp_val = getattr(value, "playerView18", None)
                setattr(value, "playerView18", self)

    @property
    def gameView10(self):
        return self.__gameView10
    @gameView10.setter
    def gameView10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlayerView__gameView10", None)
        self.__gameView10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playerView11"):
                opp_val = getattr(old_value, "playerView11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playerView11"):
                opp_val = getattr(value, "playerView11", None)
                if opp_val is None:
                    setattr(value, "playerView11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Dealer:

    def __init__(self, hand: Hand, cardTotalLimit: int, blackjack14: "BlackjackGame" = None, hand22: "Hand" = None):
        self.hand = hand
        self.cardTotalLimit = cardTotalLimit
        self.blackjack14 = blackjack14
        self.hand22 = hand22
        
        pass
    @property
    def cardTotalLimit(self):
        return self.__cardTotalLimit
    @cardTotalLimit.setter
    def cardTotalLimit(self, cardTotalLimit: int):
        self.__cardTotalLimit = cardTotalLimit

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Hand):
        self.__hand = hand

    @property
    def hand22(self):
        return self.__hand22
    @hand22.setter
    def hand22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__hand22", None)
        self.__hand22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer23"):
                opp_val = getattr(old_value, "dealer23", None)
                if opp_val == self:
                    setattr(old_value, "dealer23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer23"):
                opp_val = getattr(value, "dealer23", None)
                setattr(value, "dealer23", self)

    @property
    def blackjack14(self):
        return self.__blackjack14
    @blackjack14.setter
    def blackjack14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__blackjack14", None)
        self.__blackjack14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer15"):
                opp_val = getattr(old_value, "dealer15", None)
                if opp_val == self:
                    setattr(old_value, "dealer15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer15"):
                opp_val = getattr(value, "dealer15", None)
                setattr(value, "dealer15", self)



class Player:

    def __init__(self, hand: Hand, profile: Profile, money: int, blackjack12: "BlackjackGame" = None, profile220: "Profile" = None, hand24: set["Hand"] = None):
        self.hand = hand
        self.profile = profile
        self.money = money
        self.blackjack12 = blackjack12
        self.profile220 = profile220
        self.hand24 = hand24 if hand24 is not None else set()
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: Hand):
        self.__hand = hand

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: int):
        self.__money = money

    @property
    def profile(self):
        return self.__profile
    @profile.setter
    def profile(self, profile: Profile):
        self.__profile = profile

    @property
    def profile220(self):
        return self.__profile220
    @profile220.setter
    def profile220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__profile220", None)
        self.__profile220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player21"):
                opp_val = getattr(old_value, "player21", None)
                if opp_val == self:
                    setattr(old_value, "player21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player21"):
                opp_val = getattr(value, "player21", None)
                setattr(value, "player21", self)

    @property
    def blackjack12(self):
        return self.__blackjack12
    @blackjack12.setter
    def blackjack12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__blackjack12", None)
        self.__blackjack12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player13"):
                opp_val = getattr(old_value, "player13", None)
                if opp_val == self:
                    setattr(old_value, "player13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player13"):
                opp_val = getattr(value, "player13", None)
                setattr(value, "player13", self)

    @property
    def hand24(self):
        return self.__hand24
    @hand24.setter
    def hand24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__hand24", None)
        self.__hand24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player25"):
                    opp_val = getattr(item, "player25", None)
                    
                    if opp_val == self:
                        setattr(item, "player25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player25"):
                    opp_val = getattr(item, "player25", None)
                    
                    setattr(item, "player25", self)
                    



class JLabel:

    pass


class BasePlayer(ABC):

    def __init__(self, isBusted: bool, playerView18: "PlayerView" = None):
        self.isBusted = isBusted
        self.playerView18 = playerView18
        
        pass
    @property
    def isBusted(self):
        return self.__isBusted
    @isBusted.setter
    def isBusted(self, isBusted: bool):
        self.__isBusted = isBusted

    @property
    def playerView18(self):
        return self.__playerView18
    @playerView18.setter
    def playerView18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BasePlayer__playerView18", None)
        self.__playerView18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basePlayer19"):
                opp_val = getattr(old_value, "basePlayer19", None)
                if opp_val == self:
                    setattr(old_value, "basePlayer19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basePlayer19"):
                opp_val = getattr(value, "basePlayer19", None)
                setattr(value, "basePlayer19", self)



class GameView:

    def __init__(self, bet: JLabel, dealButton: JButton, hitButton: JButton, standButton: JButton, splitButton: JButton, doubleButton: JButton, showStrategy: bool, playerView11: set["PlayerView"] = None, blackjack7: "BlackjackGame" = None):
        self.bet = bet
        self.dealButton = dealButton
        self.hitButton = hitButton
        self.standButton = standButton
        self.splitButton = splitButton
        self.doubleButton = doubleButton
        self.showStrategy = showStrategy
        self.playerView11 = playerView11 if playerView11 is not None else set()
        self.blackjack7 = blackjack7
        
        pass
    @property
    def doubleButton(self):
        return self.__doubleButton
    @doubleButton.setter
    def doubleButton(self, doubleButton: JButton):
        self.__doubleButton = doubleButton

    @property
    def dealButton(self):
        return self.__dealButton
    @dealButton.setter
    def dealButton(self, dealButton: JButton):
        self.__dealButton = dealButton

    @property
    def standButton(self):
        return self.__standButton
    @standButton.setter
    def standButton(self, standButton: JButton):
        self.__standButton = standButton

    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: JLabel):
        self.__bet = bet

    @property
    def splitButton(self):
        return self.__splitButton
    @splitButton.setter
    def splitButton(self, splitButton: JButton):
        self.__splitButton = splitButton

    @property
    def hitButton(self):
        return self.__hitButton
    @hitButton.setter
    def hitButton(self, hitButton: JButton):
        self.__hitButton = hitButton

    @property
    def showStrategy(self):
        return self.__showStrategy
    @showStrategy.setter
    def showStrategy(self, showStrategy: bool):
        self.__showStrategy = showStrategy

    @property
    def playerView11(self):
        return self.__playerView11
    @playerView11.setter
    def playerView11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameView__playerView11", None)
        self.__playerView11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gameView10"):
                    opp_val = getattr(item, "gameView10", None)
                    
                    if opp_val == self:
                        setattr(item, "gameView10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gameView10"):
                    opp_val = getattr(item, "gameView10", None)
                    
                    setattr(item, "gameView10", self)
                    

    @property
    def blackjack7(self):
        return self.__blackjack7
    @blackjack7.setter
    def blackjack7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GameView__blackjack7", None)
        self.__blackjack7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gameView6"):
                opp_val = getattr(old_value, "gameView6", None)
                if opp_val == self:
                    setattr(old_value, "gameView6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gameView6"):
                opp_val = getattr(value, "gameView6", None)
                setattr(value, "gameView6", self)

