from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class int___1:

    pass


class Color:

    pass


class WildCard:

    def __init__(self, WildCard__: str, WildCard_String_: str):
        self.WildCard__ = WildCard__
        self.WildCard_String_ = WildCard_String_
        
        pass
    @property
    def WildCard__(self):
        return self.__WildCard__
    @WildCard__.setter
    def WildCard__(self, WildCard__: str):
        self.__WildCard__ = WildCard__

    @property
    def WildCard_String_(self):
        return self.__WildCard_String_
    @WildCard_String_.setter
    def WildCard_String_(self, WildCard_String_: str):
        self.__WildCard_String_ = WildCard_String_



class Wild4:

    pass


class Wild:

    pass


class Draw2:

    pass


class Skip:

    pass


class Reverse:

    pass


class ActionCard:

    def __init__(self, ActionCard__: str, ActionCard_Color_String_: str, _attr: str):
        self.ActionCard__ = ActionCard__
        self.ActionCard_Color_String_ = ActionCard_Color_String_
        self._attr = _attr
        
        pass
    @property
    def ActionCard__(self):
        return self.__ActionCard__
    @ActionCard__.setter
    def ActionCard__(self, ActionCard__: str):
        self.__ActionCard__ = ActionCard__

    @property
    def ActionCard_Color_String_(self):
        return self.__ActionCard_Color_String_
    @ActionCard_Color_String_.setter
    def ActionCard_Color_String_(self, ActionCard_Color_String_: str):
        self.__ActionCard_Color_String_ = ActionCard_Color_String_

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr



class NumberCard:

    def __init__(self, attribute: str, NumberCard__: str, NumberCard_Color__String_: str, attribute2: str):
        self.attribute = attribute
        self.NumberCard__ = NumberCard__
        self.NumberCard_Color__String_ = NumberCard_Color__String_
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def NumberCard__(self):
        return self.__NumberCard__
    @NumberCard__.setter
    def NumberCard__(self, NumberCard__: str):
        self.__NumberCard__ = NumberCard__

    @property
    def NumberCard_Color__String_(self):
        return self.__NumberCard_Color__String_
    @NumberCard_Color__String_.setter
    def NumberCard_Color__String_(self, NumberCard_Color__String_: str):
        self.__NumberCard_Color__String_ = NumberCard_Color__String_



class Card:

    def __init__(self, Card__: str, Card_Color__int__String_: str, setColor_Color_: str, getColor__: Color, setValue: str, Card__1: str):
        self.Card__ = Card__
        self.Card_Color__int__String_ = Card_Color__int__String_
        self.setColor_Color_ = setColor_Color_
        self.getColor__ = getColor__
        self.setValue = setValue
        self.Card__1 = Card__1
        
        pass
    @property
    def setValue(self):
        return self.__setValue
    @setValue.setter
    def setValue(self, setValue: str):
        self.__setValue = setValue

    @property
    def Card_Color__int__String_(self):
        return self.__Card_Color__int__String_
    @Card_Color__int__String_.setter
    def Card_Color__int__String_(self, Card_Color__int__String_: str):
        self.__Card_Color__int__String_ = Card_Color__int__String_

    @property
    def setColor_Color_(self):
        return self.__setColor_Color_
    @setColor_Color_.setter
    def setColor_Color_(self, setColor_Color_: str):
        self.__setColor_Color_ = setColor_Color_

    @property
    def getColor__(self):
        return self.__getColor__
    @getColor__.setter
    def getColor__(self, getColor__: Color):
        self.__getColor__ = getColor__

    @property
    def Card__1(self):
        return self.__Card__1
    @Card__1.setter
    def Card__1(self, Card__1: str):
        self.__Card__1 = Card__1

    @property
    def Card__(self):
        return self.__Card__
    @Card__.setter
    def Card__(self, Card__: str):
        self.__Card__ = Card__



class CardElements_Interface:

    pass


class GameElements:

    def __init__(self, OpeningHand: str, WildCardCol: str, CardColors: str, WildActions: str, Actions: str, CardNumber: str, Numbers: int___1, Action: str, Wild: str, CardsTotal: str):
        self.OpeningHand = OpeningHand
        self.WildCardCol = WildCardCol
        self.CardColors = CardColors
        self.WildActions = WildActions
        self.Actions = Actions
        self.CardNumber = CardNumber
        self.Numbers = Numbers
        self.Action = Action
        self.Wild = Wild
        self.CardsTotal = CardsTotal
        
        pass
    @property
    def Actions(self):
        return self.__Actions
    @Actions.setter
    def Actions(self, Actions: str):
        self.__Actions = Actions

    @property
    def CardNumber(self):
        return self.__CardNumber
    @CardNumber.setter
    def CardNumber(self, CardNumber: str):
        self.__CardNumber = CardNumber

    @property
    def OpeningHand(self):
        return self.__OpeningHand
    @OpeningHand.setter
    def OpeningHand(self, OpeningHand: str):
        self.__OpeningHand = OpeningHand

    @property
    def Numbers(self):
        return self.__Numbers
    @Numbers.setter
    def Numbers(self, Numbers: int___1):
        self.__Numbers = Numbers

    @property
    def WildActions(self):
        return self.__WildActions
    @WildActions.setter
    def WildActions(self, WildActions: str):
        self.__WildActions = WildActions

    @property
    def CardColors(self):
        return self.__CardColors
    @CardColors.setter
    def CardColors(self, CardColors: str):
        self.__CardColors = CardColors

    @property
    def Action(self):
        return self.__Action
    @Action.setter
    def Action(self, Action: str):
        self.__Action = Action

    @property
    def Wild(self):
        return self.__Wild
    @Wild.setter
    def Wild(self, Wild: str):
        self.__Wild = Wild

    @property
    def WildCardCol(self):
        return self.__WildCardCol
    @WildCardCol.setter
    def WildCardCol(self, WildCardCol: str):
        self.__WildCardCol = WildCardCol

    @property
    def CardsTotal(self):
        return self.__CardsTotal
    @CardsTotal.setter
    def CardsTotal(self, CardsTotal: str):
        self.__CardsTotal = CardsTotal



class GameElements_Interface:

    pass


class DiscardPile:

    def __init__(self, DiscardPile__: str, showTop__: str, DiscardPile__1: str):
        self.DiscardPile__ = DiscardPile__
        self.showTop__ = showTop__
        self.DiscardPile__1 = DiscardPile__1
        
        pass
    @property
    def DiscardPile__(self):
        return self.__DiscardPile__
    @DiscardPile__.setter
    def DiscardPile__(self, DiscardPile__: str):
        self.__DiscardPile__ = DiscardPile__

    @property
    def showTop__(self):
        return self.__showTop__
    @showTop__.setter
    def showTop__(self, showTop__: str):
        self.__showTop__ = showTop__

    @property
    def DiscardPile__1(self):
        return self.__DiscardPile__1
    @DiscardPile__1.setter
    def DiscardPile__1(self, DiscardPile__1: str):
        self.__DiscardPile__1 = DiscardPile__1



class DrawPile:

    def __init__(self, DrawPile__: str, removeCard_Card_: str, DrawPile__1: str):
        self.DrawPile__ = DrawPile__
        self.removeCard_Card_ = removeCard_Card_
        self.DrawPile__1 = DrawPile__1
        
        pass
    @property
    def DrawPile__1(self):
        return self.__DrawPile__1
    @DrawPile__1.setter
    def DrawPile__1(self, DrawPile__1: str):
        self.__DrawPile__1 = DrawPile__1

    @property
    def DrawPile__(self):
        return self.__DrawPile__
    @DrawPile__.setter
    def DrawPile__(self, DrawPile__: str):
        self.__DrawPile__ = DrawPile__

    @property
    def removeCard_Card_(self):
        return self.__removeCard_Card_
    @removeCard_Card_.setter
    def removeCard_Card_(self, removeCard_Card_: str):
        self.__removeCard_Card_ = removeCard_Card_



class Dealer:

    def __init__(self, Dealer__: str, shuffle__: str, distribute_Player___: str, Dealer__1: str):
        self.Dealer__ = Dealer__
        self.shuffle__ = shuffle__
        self.distribute_Player___ = distribute_Player___
        self.Dealer__1 = Dealer__1
        
        pass
    @property
    def Dealer__1(self):
        return self.__Dealer__1
    @Dealer__1.setter
    def Dealer__1(self, Dealer__1: str):
        self.__Dealer__1 = Dealer__1

    @property
    def distribute_Player___(self):
        return self.__distribute_Player___
    @distribute_Player___.setter
    def distribute_Player___(self, distribute_Player___: str):
        self.__distribute_Player___ = distribute_Player___

    @property
    def shuffle__(self):
        return self.__shuffle__
    @shuffle__.setter
    def shuffle__(self, shuffle__: str):
        self.__shuffle__ = shuffle__

    @property
    def Dealer__(self):
        return self.__Dealer__
    @Dealer__.setter
    def Dealer__(self, Dealer__: str):
        self.__Dealer__ = Dealer__



class Players:

    def __init__(self, Players__: str, Player_String_: str, getName: str, drawCard_Card_: str, hasCard_Card_: str, playCard_Card_: str, Player__: str):
        self.Players__ = Players__
        self.Player_String_ = Player_String_
        self.getName = getName
        self.drawCard_Card_ = drawCard_Card_
        self.hasCard_Card_ = hasCard_Card_
        self.playCard_Card_ = playCard_Card_
        self.Player__ = Player__
        
        pass
    @property
    def playCard_Card_(self):
        return self.__playCard_Card_
    @playCard_Card_.setter
    def playCard_Card_(self, playCard_Card_: str):
        self.__playCard_Card_ = playCard_Card_

    @property
    def Players__(self):
        return self.__Players__
    @Players__.setter
    def Players__(self, Players__: str):
        self.__Players__ = Players__

    @property
    def getName(self):
        return self.__getName
    @getName.setter
    def getName(self, getName: str):
        self.__getName = getName

    @property
    def drawCard_Card_(self):
        return self.__drawCard_Card_
    @drawCard_Card_.setter
    def drawCard_Card_(self, drawCard_Card_: str):
        self.__drawCard_Card_ = drawCard_Card_

    @property
    def Player__(self):
        return self.__Player__
    @Player__.setter
    def Player__(self, Player__: str):
        self.__Player__ = Player__

    @property
    def Player_String_(self):
        return self.__Player_String_
    @Player_String_.setter
    def Player_String_(self, Player_String_: str):
        self.__Player_String_ = Player_String_

    @property
    def hasCard_Card_(self):
        return self.__hasCard_Card_
    @hasCard_Card_.setter
    def hasCard_Card_(self, hasCard_Card_: str):
        self.__hasCard_Card_ = hasCard_Card_



class Game:

    def __init__(self, Game__: str, getPlayers__: str, PlayGame__: str, Game__1: str):
        self.Game__ = Game__
        self.getPlayers__ = getPlayers__
        self.PlayGame__ = PlayGame__
        self.Game__1 = Game__1
        
        pass
    @property
    def getPlayers__(self):
        return self.__getPlayers__
    @getPlayers__.setter
    def getPlayers__(self, getPlayers__: str):
        self.__getPlayers__ = getPlayers__

    @property
    def PlayGame__(self):
        return self.__PlayGame__
    @PlayGame__.setter
    def PlayGame__(self, PlayGame__: str):
        self.__PlayGame__ = PlayGame__

    @property
    def Game__(self):
        return self.__Game__
    @Game__.setter
    def Game__(self, Game__: str):
        self.__Game__ = Game__

    @property
    def Game__1(self):
        return self.__Game__1
    @Game__1.setter
    def Game__1(self, Game__1: str):
        self.__Game__1 = Game__1



class GameSession:

    def __init__(self, GameSession_Game_: str, setPlayers__: str, GameSession_Game__Card_: str):
        self.GameSession_Game_ = GameSession_Game_
        self.setPlayers__ = setPlayers__
        self.GameSession_Game__Card_ = GameSession_Game__Card_
        
        pass
    @property
    def setPlayers__(self):
        return self.__setPlayers__
    @setPlayers__.setter
    def setPlayers__(self, setPlayers__: str):
        self.__setPlayers__ = setPlayers__

    @property
    def GameSession_Game_(self):
        return self.__GameSession_Game_
    @GameSession_Game_.setter
    def GameSession_Game_(self, GameSession_Game_: str):
        self.__GameSession_Game_ = GameSession_Game_

    @property
    def GameSession_Game__Card_(self):
        return self.__GameSession_Game__Card_
    @GameSession_Game__Card_.setter
    def GameSession_Game__Card_(self, GameSession_Game__Card_: str):
        self.__GameSession_Game__Card_ = GameSession_Game__Card_



class Main:

    def __init__(self, Main__: str, main_String____: str):
        self.Main__ = Main__
        self.main_String____ = main_String____
        
        pass
    @property
    def main_String____(self):
        return self.__main_String____
    @main_String____.setter
    def main_String____(self, main_String____: str):
        self.__main_String____ = main_String____

    @property
    def Main__(self):
        return self.__Main__
    @Main__.setter
    def Main__(self, Main__: str):
        self.__Main__ = Main__

