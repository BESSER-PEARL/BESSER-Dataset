from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class ActionEvent:

    pass


class Graphics:

    pass


class WinScreen:

    pass


class SolitairePanel:

    def __init__(self, backgroundNumber: int, background: str, solitaireBoard1: "SolitaireBoard" = None):
        self.backgroundNumber = backgroundNumber
        self.background = background
        self.solitaireBoard1 = solitaireBoard1
        
        pass
    @property
    def background(self):
        return self.__background
    @background.setter
    def background(self, background: str):
        self.__background = background

    @property
    def backgroundNumber(self):
        return self.__backgroundNumber
    @backgroundNumber.setter
    def backgroundNumber(self, backgroundNumber: int):
        self.__backgroundNumber = backgroundNumber

    @property
    def solitaireBoard1(self):
        return self.__solitaireBoard1
    @solitaireBoard1.setter
    def solitaireBoard1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolitairePanel__solitaireBoard1", None)
        self.__solitaireBoard1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solitairePanel0"):
                opp_val = getattr(old_value, "solitairePanel0", None)
                if opp_val == self:
                    setattr(old_value, "solitairePanel0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solitairePanel0"):
                opp_val = getattr(value, "solitairePanel0", None)
                setattr(value, "solitairePanel0", self)



class SolitaireLayout:

    def __init__(self, SPADES_ACE_PILE: str, CLUBS_ACE_PILE: str, DIAMONDS_ACE_PILE: str, HEARTS_ACE_PILE: str, DISCARD_PILE: str, DECK: str, CELL_ONE: str, CELL_TWO: str, CELL_THREE: str, CELL_FOUR: str, colOne: str, colTwo: str, colThree: str, colFour: str, aceSpades: str, aceClubs: str, aceDiamonds: str, aceHearts: str, discardPile: str, deck: str, cellFour: str, cellOne: str, cellTwo: str, cellThree: str, COLUMEN_ONE: str, COLUMN_TWO: str, COLUMN_THREE: str, COLUMN_FOUR: str):
        self.SPADES_ACE_PILE = SPADES_ACE_PILE
        self.CLUBS_ACE_PILE = CLUBS_ACE_PILE
        self.DIAMONDS_ACE_PILE = DIAMONDS_ACE_PILE
        self.HEARTS_ACE_PILE = HEARTS_ACE_PILE
        self.DISCARD_PILE = DISCARD_PILE
        self.DECK = DECK
        self.CELL_ONE = CELL_ONE
        self.CELL_TWO = CELL_TWO
        self.CELL_THREE = CELL_THREE
        self.CELL_FOUR = CELL_FOUR
        self.colOne = colOne
        self.colTwo = colTwo
        self.colThree = colThree
        self.colFour = colFour
        self.aceSpades = aceSpades
        self.aceClubs = aceClubs
        self.aceDiamonds = aceDiamonds
        self.aceHearts = aceHearts
        self.discardPile = discardPile
        self.deck = deck
        self.cellFour = cellFour
        self.cellOne = cellOne
        self.cellTwo = cellTwo
        self.cellThree = cellThree
        self.COLUMEN_ONE = COLUMEN_ONE
        self.COLUMN_TWO = COLUMN_TWO
        self.COLUMN_THREE = COLUMN_THREE
        self.COLUMN_FOUR = COLUMN_FOUR
        
        pass
    @property
    def discardPile(self):
        return self.__discardPile
    @discardPile.setter
    def discardPile(self, discardPile: str):
        self.__discardPile = discardPile

    @property
    def CELL_FOUR(self):
        return self.__CELL_FOUR
    @CELL_FOUR.setter
    def CELL_FOUR(self, CELL_FOUR: str):
        self.__CELL_FOUR = CELL_FOUR

    @property
    def COLUMN_THREE(self):
        return self.__COLUMN_THREE
    @COLUMN_THREE.setter
    def COLUMN_THREE(self, COLUMN_THREE: str):
        self.__COLUMN_THREE = COLUMN_THREE

    @property
    def colTwo(self):
        return self.__colTwo
    @colTwo.setter
    def colTwo(self, colTwo: str):
        self.__colTwo = colTwo

    @property
    def aceSpades(self):
        return self.__aceSpades
    @aceSpades.setter
    def aceSpades(self, aceSpades: str):
        self.__aceSpades = aceSpades

    @property
    def HEARTS_ACE_PILE(self):
        return self.__HEARTS_ACE_PILE
    @HEARTS_ACE_PILE.setter
    def HEARTS_ACE_PILE(self, HEARTS_ACE_PILE: str):
        self.__HEARTS_ACE_PILE = HEARTS_ACE_PILE

    @property
    def CELL_ONE(self):
        return self.__CELL_ONE
    @CELL_ONE.setter
    def CELL_ONE(self, CELL_ONE: str):
        self.__CELL_ONE = CELL_ONE

    @property
    def cellThree(self):
        return self.__cellThree
    @cellThree.setter
    def cellThree(self, cellThree: str):
        self.__cellThree = cellThree

    @property
    def cellTwo(self):
        return self.__cellTwo
    @cellTwo.setter
    def cellTwo(self, cellTwo: str):
        self.__cellTwo = cellTwo

    @property
    def CLUBS_ACE_PILE(self):
        return self.__CLUBS_ACE_PILE
    @CLUBS_ACE_PILE.setter
    def CLUBS_ACE_PILE(self, CLUBS_ACE_PILE: str):
        self.__CLUBS_ACE_PILE = CLUBS_ACE_PILE

    @property
    def aceHearts(self):
        return self.__aceHearts
    @aceHearts.setter
    def aceHearts(self, aceHearts: str):
        self.__aceHearts = aceHearts

    @property
    def colThree(self):
        return self.__colThree
    @colThree.setter
    def colThree(self, colThree: str):
        self.__colThree = colThree

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def DIAMONDS_ACE_PILE(self):
        return self.__DIAMONDS_ACE_PILE
    @DIAMONDS_ACE_PILE.setter
    def DIAMONDS_ACE_PILE(self, DIAMONDS_ACE_PILE: str):
        self.__DIAMONDS_ACE_PILE = DIAMONDS_ACE_PILE

    @property
    def COLUMEN_ONE(self):
        return self.__COLUMEN_ONE
    @COLUMEN_ONE.setter
    def COLUMEN_ONE(self, COLUMEN_ONE: str):
        self.__COLUMEN_ONE = COLUMEN_ONE

    @property
    def colOne(self):
        return self.__colOne
    @colOne.setter
    def colOne(self, colOne: str):
        self.__colOne = colOne

    @property
    def DECK(self):
        return self.__DECK
    @DECK.setter
    def DECK(self, DECK: str):
        self.__DECK = DECK

    @property
    def CELL_THREE(self):
        return self.__CELL_THREE
    @CELL_THREE.setter
    def CELL_THREE(self, CELL_THREE: str):
        self.__CELL_THREE = CELL_THREE

    @property
    def colFour(self):
        return self.__colFour
    @colFour.setter
    def colFour(self, colFour: str):
        self.__colFour = colFour

    @property
    def aceDiamonds(self):
        return self.__aceDiamonds
    @aceDiamonds.setter
    def aceDiamonds(self, aceDiamonds: str):
        self.__aceDiamonds = aceDiamonds

    @property
    def SPADES_ACE_PILE(self):
        return self.__SPADES_ACE_PILE
    @SPADES_ACE_PILE.setter
    def SPADES_ACE_PILE(self, SPADES_ACE_PILE: str):
        self.__SPADES_ACE_PILE = SPADES_ACE_PILE

    @property
    def aceClubs(self):
        return self.__aceClubs
    @aceClubs.setter
    def aceClubs(self, aceClubs: str):
        self.__aceClubs = aceClubs

    @property
    def DISCARD_PILE(self):
        return self.__DISCARD_PILE
    @DISCARD_PILE.setter
    def DISCARD_PILE(self, DISCARD_PILE: str):
        self.__DISCARD_PILE = DISCARD_PILE

    @property
    def CELL_TWO(self):
        return self.__CELL_TWO
    @CELL_TWO.setter
    def CELL_TWO(self, CELL_TWO: str):
        self.__CELL_TWO = CELL_TWO

    @property
    def COLUMN_TWO(self):
        return self.__COLUMN_TWO
    @COLUMN_TWO.setter
    def COLUMN_TWO(self, COLUMN_TWO: str):
        self.__COLUMN_TWO = COLUMN_TWO

    @property
    def cellFour(self):
        return self.__cellFour
    @cellFour.setter
    def cellFour(self, cellFour: str):
        self.__cellFour = cellFour

    @property
    def COLUMN_FOUR(self):
        return self.__COLUMN_FOUR
    @COLUMN_FOUR.setter
    def COLUMN_FOUR(self, COLUMN_FOUR: str):
        self.__COLUMN_FOUR = COLUMN_FOUR

    @property
    def cellOne(self):
        return self.__cellOne
    @cellOne.setter
    def cellOne(self, cellOne: str):
        self.__cellOne = cellOne



class SolitaireBoard:

    def __init__(self, GAME_WON: int, GAME_LOST: int, RESET_STATS: int, DO_NOTHING: int, GAME_SAVED: int, drawCount: int, newDrawCount: int, backgroundNumber: int, deckNumber: int, timer: str, statusBar: str, timerLabel: str, timerCount: int, timerToRunNextGame: int, timerToRun: bool, winAnimationStatus: int, winSoundsStatus: int, difficulty: int, newDifficulty: int, numCards: str, numCardsInDiscardView: str, solitairePanel0: "SolitairePanel" = None, deck2: "Deck" = None, acePile6: set["AcePile"] = None, cardStack8: set["CardStack"] = None, discardPile14: "DiscardPile" = None, singleCell16: set["SingleCell"] = None, column18: set["Column"] = None):
        self.GAME_WON = GAME_WON
        self.GAME_LOST = GAME_LOST
        self.RESET_STATS = RESET_STATS
        self.DO_NOTHING = DO_NOTHING
        self.GAME_SAVED = GAME_SAVED
        self.drawCount = drawCount
        self.newDrawCount = newDrawCount
        self.backgroundNumber = backgroundNumber
        self.deckNumber = deckNumber
        self.timer = timer
        self.statusBar = statusBar
        self.timerLabel = timerLabel
        self.timerCount = timerCount
        self.timerToRunNextGame = timerToRunNextGame
        self.timerToRun = timerToRun
        self.winAnimationStatus = winAnimationStatus
        self.winSoundsStatus = winSoundsStatus
        self.difficulty = difficulty
        self.newDifficulty = newDifficulty
        self.numCards = numCards
        self.numCardsInDiscardView = numCardsInDiscardView
        self.solitairePanel0 = solitairePanel0
        self.deck2 = deck2
        self.acePile6 = acePile6 if acePile6 is not None else set()
        self.cardStack8 = cardStack8 if cardStack8 is not None else set()
        self.discardPile14 = discardPile14
        self.singleCell16 = singleCell16 if singleCell16 is not None else set()
        self.column18 = column18 if column18 is not None else set()
        
        pass
    @property
    def difficulty(self):
        return self.__difficulty
    @difficulty.setter
    def difficulty(self, difficulty: int):
        self.__difficulty = difficulty

    @property
    def backgroundNumber(self):
        return self.__backgroundNumber
    @backgroundNumber.setter
    def backgroundNumber(self, backgroundNumber: int):
        self.__backgroundNumber = backgroundNumber

    @property
    def timer(self):
        return self.__timer
    @timer.setter
    def timer(self, timer: str):
        self.__timer = timer

    @property
    def GAME_WON(self):
        return self.__GAME_WON
    @GAME_WON.setter
    def GAME_WON(self, GAME_WON: int):
        self.__GAME_WON = GAME_WON

    @property
    def timerToRunNextGame(self):
        return self.__timerToRunNextGame
    @timerToRunNextGame.setter
    def timerToRunNextGame(self, timerToRunNextGame: int):
        self.__timerToRunNextGame = timerToRunNextGame

    @property
    def timerLabel(self):
        return self.__timerLabel
    @timerLabel.setter
    def timerLabel(self, timerLabel: str):
        self.__timerLabel = timerLabel

    @property
    def winSoundsStatus(self):
        return self.__winSoundsStatus
    @winSoundsStatus.setter
    def winSoundsStatus(self, winSoundsStatus: int):
        self.__winSoundsStatus = winSoundsStatus

    @property
    def drawCount(self):
        return self.__drawCount
    @drawCount.setter
    def drawCount(self, drawCount: int):
        self.__drawCount = drawCount

    @property
    def timerToRun(self):
        return self.__timerToRun
    @timerToRun.setter
    def timerToRun(self, timerToRun: bool):
        self.__timerToRun = timerToRun

    @property
    def GAME_SAVED(self):
        return self.__GAME_SAVED
    @GAME_SAVED.setter
    def GAME_SAVED(self, GAME_SAVED: int):
        self.__GAME_SAVED = GAME_SAVED

    @property
    def winAnimationStatus(self):
        return self.__winAnimationStatus
    @winAnimationStatus.setter
    def winAnimationStatus(self, winAnimationStatus: int):
        self.__winAnimationStatus = winAnimationStatus

    @property
    def deckNumber(self):
        return self.__deckNumber
    @deckNumber.setter
    def deckNumber(self, deckNumber: int):
        self.__deckNumber = deckNumber

    @property
    def timerCount(self):
        return self.__timerCount
    @timerCount.setter
    def timerCount(self, timerCount: int):
        self.__timerCount = timerCount

    @property
    def newDrawCount(self):
        return self.__newDrawCount
    @newDrawCount.setter
    def newDrawCount(self, newDrawCount: int):
        self.__newDrawCount = newDrawCount

    @property
    def newDifficulty(self):
        return self.__newDifficulty
    @newDifficulty.setter
    def newDifficulty(self, newDifficulty: int):
        self.__newDifficulty = newDifficulty

    @property
    def numCardsInDiscardView(self):
        return self.__numCardsInDiscardView
    @numCardsInDiscardView.setter
    def numCardsInDiscardView(self, numCardsInDiscardView: str):
        self.__numCardsInDiscardView = numCardsInDiscardView

    @property
    def statusBar(self):
        return self.__statusBar
    @statusBar.setter
    def statusBar(self, statusBar: str):
        self.__statusBar = statusBar

    @property
    def DO_NOTHING(self):
        return self.__DO_NOTHING
    @DO_NOTHING.setter
    def DO_NOTHING(self, DO_NOTHING: int):
        self.__DO_NOTHING = DO_NOTHING

    @property
    def RESET_STATS(self):
        return self.__RESET_STATS
    @RESET_STATS.setter
    def RESET_STATS(self, RESET_STATS: int):
        self.__RESET_STATS = RESET_STATS

    @property
    def numCards(self):
        return self.__numCards
    @numCards.setter
    def numCards(self, numCards: str):
        self.__numCards = numCards

    @property
    def GAME_LOST(self):
        return self.__GAME_LOST
    @GAME_LOST.setter
    def GAME_LOST(self, GAME_LOST: int):
        self.__GAME_LOST = GAME_LOST

    @property
    def cardStack8(self):
        return self.__cardStack8
    @cardStack8.setter
    def cardStack8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolitaireBoard__cardStack8", None)
        self.__cardStack8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solitaireBoard9"):
                    opp_val = getattr(item, "solitaireBoard9", None)
                    
                    if opp_val == self:
                        setattr(item, "solitaireBoard9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solitaireBoard9"):
                    opp_val = getattr(item, "solitaireBoard9", None)
                    
                    setattr(item, "solitaireBoard9", self)
                    

    @property
    def column18(self):
        return self.__column18
    @column18.setter
    def column18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolitaireBoard__column18", None)
        self.__column18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solitaireBoard19"):
                    opp_val = getattr(item, "solitaireBoard19", None)
                    
                    if opp_val == self:
                        setattr(item, "solitaireBoard19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solitaireBoard19"):
                    opp_val = getattr(item, "solitaireBoard19", None)
                    
                    setattr(item, "solitaireBoard19", self)
                    

    @property
    def acePile6(self):
        return self.__acePile6
    @acePile6.setter
    def acePile6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolitaireBoard__acePile6", None)
        self.__acePile6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solitaireBoard7"):
                    opp_val = getattr(item, "solitaireBoard7", None)
                    
                    if opp_val == self:
                        setattr(item, "solitaireBoard7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solitaireBoard7"):
                    opp_val = getattr(item, "solitaireBoard7", None)
                    
                    setattr(item, "solitaireBoard7", self)
                    

    @property
    def discardPile14(self):
        return self.__discardPile14
    @discardPile14.setter
    def discardPile14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolitaireBoard__discardPile14", None)
        self.__discardPile14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solitaireBoard15"):
                opp_val = getattr(old_value, "solitaireBoard15", None)
                if opp_val == self:
                    setattr(old_value, "solitaireBoard15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solitaireBoard15"):
                opp_val = getattr(value, "solitaireBoard15", None)
                setattr(value, "solitaireBoard15", self)

    @property
    def deck2(self):
        return self.__deck2
    @deck2.setter
    def deck2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolitaireBoard__deck2", None)
        self.__deck2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solitaireBoard3"):
                opp_val = getattr(old_value, "solitaireBoard3", None)
                if opp_val == self:
                    setattr(old_value, "solitaireBoard3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solitaireBoard3"):
                opp_val = getattr(value, "solitaireBoard3", None)
                setattr(value, "solitaireBoard3", self)

    @property
    def singleCell16(self):
        return self.__singleCell16
    @singleCell16.setter
    def singleCell16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolitaireBoard__singleCell16", None)
        self.__singleCell16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "solitaireBoard17"):
                    opp_val = getattr(item, "solitaireBoard17", None)
                    
                    if opp_val == self:
                        setattr(item, "solitaireBoard17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "solitaireBoard17"):
                    opp_val = getattr(item, "solitaireBoard17", None)
                    
                    setattr(item, "solitaireBoard17", self)
                    

    @property
    def solitairePanel0(self):
        return self.__solitairePanel0
    @solitairePanel0.setter
    def solitairePanel0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SolitaireBoard__solitairePanel0", None)
        self.__solitairePanel0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "solitaireBoard1"):
                opp_val = getattr(old_value, "solitaireBoard1", None)
                if opp_val == self:
                    setattr(old_value, "solitaireBoard1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "solitaireBoard1"):
                opp_val = getattr(value, "solitaireBoard1", None)
                setattr(value, "solitaireBoard1", self)



class SingleCell:

    pass


class FourRowSolitaire:

    def __init__(self, version: AcePile, menuBar: str, game: str, helpMenu: str, newGame: str, undo: str, hint: str, statistics: str, options: str, appearance: str, exit: str, help: str, about: str, checkUpdate: str):
        self.version = version
        self.menuBar = menuBar
        self.game = game
        self.helpMenu = helpMenu
        self.newGame = newGame
        self.undo = undo
        self.hint = hint
        self.statistics = statistics
        self.options = options
        self.appearance = appearance
        self.exit = exit
        self.help = help
        self.about = about
        self.checkUpdate = checkUpdate
        
        pass
    @property
    def help(self):
        return self.__help
    @help.setter
    def help(self, help: str):
        self.__help = help

    @property
    def checkUpdate(self):
        return self.__checkUpdate
    @checkUpdate.setter
    def checkUpdate(self, checkUpdate: str):
        self.__checkUpdate = checkUpdate

    @property
    def newGame(self):
        return self.__newGame
    @newGame.setter
    def newGame(self, newGame: str):
        self.__newGame = newGame

    @property
    def appearance(self):
        return self.__appearance
    @appearance.setter
    def appearance(self, appearance: str):
        self.__appearance = appearance

    @property
    def statistics(self):
        return self.__statistics
    @statistics.setter
    def statistics(self, statistics: str):
        self.__statistics = statistics

    @property
    def hint(self):
        return self.__hint
    @hint.setter
    def hint(self, hint: str):
        self.__hint = hint

    @property
    def helpMenu(self):
        return self.__helpMenu
    @helpMenu.setter
    def helpMenu(self, helpMenu: str):
        self.__helpMenu = helpMenu

    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, game: str):
        self.__game = game

    @property
    def version(self):
        return self.__version
    @version.setter
    def version(self, version: AcePile):
        self.__version = version

    @property
    def about(self):
        return self.__about
    @about.setter
    def about(self, about: str):
        self.__about = about

    @property
    def options(self):
        return self.__options
    @options.setter
    def options(self, options: str):
        self.__options = options

    @property
    def undo(self):
        return self.__undo
    @undo.setter
    def undo(self, undo: str):
        self.__undo = undo

    @property
    def exit(self):
        return self.__exit
    @exit.setter
    def exit(self, exit: str):
        self.__exit = exit

    @property
    def menuBar(self):
        return self.__menuBar
    @menuBar.setter
    def menuBar(self, menuBar: str):
        self.__menuBar = menuBar



class FireworksDisplay:

    def __init__(self, NUM_FIREWORKS: int, FIREWORKS_SIZE: int, SET_DELAY: int, FIREWORKS_TIME: int, x: str, y: str, colors: str, xx: str, num: int, yy: str, numSets: int, startValue: int, timer: str, random: str):
        self.NUM_FIREWORKS = NUM_FIREWORKS
        self.FIREWORKS_SIZE = FIREWORKS_SIZE
        self.SET_DELAY = SET_DELAY
        self.FIREWORKS_TIME = FIREWORKS_TIME
        self.x = x
        self.y = y
        self.colors = colors
        self.xx = xx
        self.num = num
        self.yy = yy
        self.numSets = numSets
        self.startValue = startValue
        self.timer = timer
        self.random = random
        
        pass
    @property
    def NUM_FIREWORKS(self):
        return self.__NUM_FIREWORKS
    @NUM_FIREWORKS.setter
    def NUM_FIREWORKS(self, NUM_FIREWORKS: int):
        self.__NUM_FIREWORKS = NUM_FIREWORKS

    @property
    def startValue(self):
        return self.__startValue
    @startValue.setter
    def startValue(self, startValue: int):
        self.__startValue = startValue

    @property
    def numSets(self):
        return self.__numSets
    @numSets.setter
    def numSets(self, numSets: int):
        self.__numSets = numSets

    @property
    def random(self):
        return self.__random
    @random.setter
    def random(self, random: str):
        self.__random = random

    @property
    def xx(self):
        return self.__xx
    @xx.setter
    def xx(self, xx: str):
        self.__xx = xx

    @property
    def timer(self):
        return self.__timer
    @timer.setter
    def timer(self, timer: str):
        self.__timer = timer

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def FIREWORKS_SIZE(self):
        return self.__FIREWORKS_SIZE
    @FIREWORKS_SIZE.setter
    def FIREWORKS_SIZE(self, FIREWORKS_SIZE: int):
        self.__FIREWORKS_SIZE = FIREWORKS_SIZE

    @property
    def colors(self):
        return self.__colors
    @colors.setter
    def colors(self, colors: str):
        self.__colors = colors

    @property
    def yy(self):
        return self.__yy
    @yy.setter
    def yy(self, yy: str):
        self.__yy = yy

    @property
    def FIREWORKS_TIME(self):
        return self.__FIREWORKS_TIME
    @FIREWORKS_TIME.setter
    def FIREWORKS_TIME(self, FIREWORKS_TIME: int):
        self.__FIREWORKS_TIME = FIREWORKS_TIME

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def SET_DELAY(self):
        return self.__SET_DELAY
    @SET_DELAY.setter
    def SET_DELAY(self, SET_DELAY: int):
        self.__SET_DELAY = SET_DELAY

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: str):
        self.__y = y



class DiscardPile:

    def __init__(self, drawCount: int, cardsLeftFromDraw: int, dealDeck13: "DealDeck" = None, solitaireBoard15: "SolitaireBoard" = None):
        self.drawCount = drawCount
        self.cardsLeftFromDraw = cardsLeftFromDraw
        self.dealDeck13 = dealDeck13
        self.solitaireBoard15 = solitaireBoard15
        
        pass
    @property
    def cardsLeftFromDraw(self):
        return self.__cardsLeftFromDraw
    @cardsLeftFromDraw.setter
    def cardsLeftFromDraw(self, cardsLeftFromDraw: int):
        self.__cardsLeftFromDraw = cardsLeftFromDraw

    @property
    def drawCount(self):
        return self.__drawCount
    @drawCount.setter
    def drawCount(self, drawCount: int):
        self.__drawCount = drawCount

    @property
    def solitaireBoard15(self):
        return self.__solitaireBoard15
    @solitaireBoard15.setter
    def solitaireBoard15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiscardPile__solitaireBoard15", None)
        self.__solitaireBoard15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "discardPile14"):
                opp_val = getattr(old_value, "discardPile14", None)
                if opp_val == self:
                    setattr(old_value, "discardPile14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "discardPile14"):
                opp_val = getattr(value, "discardPile14", None)
                setattr(value, "discardPile14", self)

    @property
    def dealDeck13(self):
        return self.__dealDeck13
    @dealDeck13.setter
    def dealDeck13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DiscardPile__dealDeck13", None)
        self.__dealDeck13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "discardPile12"):
                opp_val = getattr(old_value, "discardPile12", None)
                if opp_val == self:
                    setattr(old_value, "discardPile12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "discardPile12"):
                opp_val = getattr(value, "discardPile12", None)
                setattr(value, "discardPile12", self)



class Deck:

    def __init__(self, deckNumber: int, solitaireBoard3: "SolitaireBoard" = None, card4: set["Card"] = None):
        self.deckNumber = deckNumber
        self.solitaireBoard3 = solitaireBoard3
        self.card4 = card4 if card4 is not None else set()
        
        pass
    @property
    def deckNumber(self):
        return self.__deckNumber
    @deckNumber.setter
    def deckNumber(self, deckNumber: int):
        self.__deckNumber = deckNumber

    @property
    def solitaireBoard3(self):
        return self.__solitaireBoard3
    @solitaireBoard3.setter
    def solitaireBoard3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__solitaireBoard3", None)
        self.__solitaireBoard3 = value
        
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
    def card4(self):
        return self.__card4
    @card4.setter
    def card4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__card4", None)
        self.__card4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "deck5"):
                    opp_val = getattr(item, "deck5", None)
                    
                    if opp_val == self:
                        setattr(item, "deck5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "deck5"):
                    opp_val = getattr(item, "deck5", None)
                    
                    setattr(item, "deck5", self)
                    



class DealDeck:

    def __init__(self, numTimesThroughDeck: int, drawCount: int, difficulty: int, DRAW_ONE_THROUGH_LIMIT: int, DRAW_THREE_THROUGH_LIMIT: int, EASY_THROUGH_LIMIT: int, MEDIUM_THROUGH_LIMIT: int, HARD_THROUGH_LIMIT: int, deckThroughLimit: int, redealable: bool, discardPile12: "DiscardPile" = None):
        self.numTimesThroughDeck = numTimesThroughDeck
        self.drawCount = drawCount
        self.difficulty = difficulty
        self.DRAW_ONE_THROUGH_LIMIT = DRAW_ONE_THROUGH_LIMIT
        self.DRAW_THREE_THROUGH_LIMIT = DRAW_THREE_THROUGH_LIMIT
        self.EASY_THROUGH_LIMIT = EASY_THROUGH_LIMIT
        self.MEDIUM_THROUGH_LIMIT = MEDIUM_THROUGH_LIMIT
        self.HARD_THROUGH_LIMIT = HARD_THROUGH_LIMIT
        self.deckThroughLimit = deckThroughLimit
        self.redealable = redealable
        self.discardPile12 = discardPile12
        
        pass
    @property
    def HARD_THROUGH_LIMIT(self):
        return self.__HARD_THROUGH_LIMIT
    @HARD_THROUGH_LIMIT.setter
    def HARD_THROUGH_LIMIT(self, HARD_THROUGH_LIMIT: int):
        self.__HARD_THROUGH_LIMIT = HARD_THROUGH_LIMIT

    @property
    def EASY_THROUGH_LIMIT(self):
        return self.__EASY_THROUGH_LIMIT
    @EASY_THROUGH_LIMIT.setter
    def EASY_THROUGH_LIMIT(self, EASY_THROUGH_LIMIT: int):
        self.__EASY_THROUGH_LIMIT = EASY_THROUGH_LIMIT

    @property
    def numTimesThroughDeck(self):
        return self.__numTimesThroughDeck
    @numTimesThroughDeck.setter
    def numTimesThroughDeck(self, numTimesThroughDeck: int):
        self.__numTimesThroughDeck = numTimesThroughDeck

    @property
    def drawCount(self):
        return self.__drawCount
    @drawCount.setter
    def drawCount(self, drawCount: int):
        self.__drawCount = drawCount

    @property
    def MEDIUM_THROUGH_LIMIT(self):
        return self.__MEDIUM_THROUGH_LIMIT
    @MEDIUM_THROUGH_LIMIT.setter
    def MEDIUM_THROUGH_LIMIT(self, MEDIUM_THROUGH_LIMIT: int):
        self.__MEDIUM_THROUGH_LIMIT = MEDIUM_THROUGH_LIMIT

    @property
    def deckThroughLimit(self):
        return self.__deckThroughLimit
    @deckThroughLimit.setter
    def deckThroughLimit(self, deckThroughLimit: int):
        self.__deckThroughLimit = deckThroughLimit

    @property
    def DRAW_THREE_THROUGH_LIMIT(self):
        return self.__DRAW_THREE_THROUGH_LIMIT
    @DRAW_THREE_THROUGH_LIMIT.setter
    def DRAW_THREE_THROUGH_LIMIT(self, DRAW_THREE_THROUGH_LIMIT: int):
        self.__DRAW_THREE_THROUGH_LIMIT = DRAW_THREE_THROUGH_LIMIT

    @property
    def DRAW_ONE_THROUGH_LIMIT(self):
        return self.__DRAW_ONE_THROUGH_LIMIT
    @DRAW_ONE_THROUGH_LIMIT.setter
    def DRAW_ONE_THROUGH_LIMIT(self, DRAW_ONE_THROUGH_LIMIT: int):
        self.__DRAW_ONE_THROUGH_LIMIT = DRAW_ONE_THROUGH_LIMIT

    @property
    def redealable(self):
        return self.__redealable
    @redealable.setter
    def redealable(self, redealable: bool):
        self.__redealable = redealable

    @property
    def difficulty(self):
        return self.__difficulty
    @difficulty.setter
    def difficulty(self, difficulty: int):
        self.__difficulty = difficulty

    @property
    def discardPile12(self):
        return self.__discardPile12
    @discardPile12.setter
    def discardPile12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DealDeck__discardPile12", None)
        self.__discardPile12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealDeck13"):
                opp_val = getattr(old_value, "dealDeck13", None)
                if opp_val == self:
                    setattr(old_value, "dealDeck13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealDeck13"):
                opp_val = getattr(value, "dealDeck13", None)
                setattr(value, "dealDeck13", self)



class Column:

    pass


class ChangeOptions:

    def __init__(self, drawCount: int, drawOne: str, drawThree: str, timerCheck: str, timer: int, winAnimationCheck: str, animation: int, winSoundsCheck: str, sounds: int, difficulty: int, easy: str, medium: str, hard: str, ok: str, exited: bool):
        self.drawCount = drawCount
        self.drawOne = drawOne
        self.drawThree = drawThree
        self.timerCheck = timerCheck
        self.timer = timer
        self.winAnimationCheck = winAnimationCheck
        self.animation = animation
        self.winSoundsCheck = winSoundsCheck
        self.sounds = sounds
        self.difficulty = difficulty
        self.easy = easy
        self.medium = medium
        self.hard = hard
        self.ok = ok
        self.exited = exited
        
        pass
    @property
    def drawCount(self):
        return self.__drawCount
    @drawCount.setter
    def drawCount(self, drawCount: int):
        self.__drawCount = drawCount

    @property
    def easy(self):
        return self.__easy
    @easy.setter
    def easy(self, easy: str):
        self.__easy = easy

    @property
    def hard(self):
        return self.__hard
    @hard.setter
    def hard(self, hard: str):
        self.__hard = hard

    @property
    def medium(self):
        return self.__medium
    @medium.setter
    def medium(self, medium: str):
        self.__medium = medium

    @property
    def winAnimationCheck(self):
        return self.__winAnimationCheck
    @winAnimationCheck.setter
    def winAnimationCheck(self, winAnimationCheck: str):
        self.__winAnimationCheck = winAnimationCheck

    @property
    def drawThree(self):
        return self.__drawThree
    @drawThree.setter
    def drawThree(self, drawThree: str):
        self.__drawThree = drawThree

    @property
    def winSoundsCheck(self):
        return self.__winSoundsCheck
    @winSoundsCheck.setter
    def winSoundsCheck(self, winSoundsCheck: str):
        self.__winSoundsCheck = winSoundsCheck

    @property
    def difficulty(self):
        return self.__difficulty
    @difficulty.setter
    def difficulty(self, difficulty: int):
        self.__difficulty = difficulty

    @property
    def timerCheck(self):
        return self.__timerCheck
    @timerCheck.setter
    def timerCheck(self, timerCheck: str):
        self.__timerCheck = timerCheck

    @property
    def drawOne(self):
        return self.__drawOne
    @drawOne.setter
    def drawOne(self, drawOne: str):
        self.__drawOne = drawOne

    @property
    def timer(self):
        return self.__timer
    @timer.setter
    def timer(self, timer: int):
        self.__timer = timer

    @property
    def ok(self):
        return self.__ok
    @ok.setter
    def ok(self, ok: str):
        self.__ok = ok

    @property
    def animation(self):
        return self.__animation
    @animation.setter
    def animation(self, animation: int):
        self.__animation = animation

    @property
    def sounds(self):
        return self.__sounds
    @sounds.setter
    def sounds(self, sounds: int):
        self.__sounds = sounds

    @property
    def exited(self):
        return self.__exited
    @exited.setter
    def exited(self, exited: bool):
        self.__exited = exited



class ChangeAppearance:

    def __init__(self, NUM_DECKS: int, NUM_BACKGROUNDS: int, FRS_DECK: int, FRS_BACKGROUND: int, decks: str, backgrounds: str, ok: str, deckNumber: int, backgroundNumber: int, exited: bool, cardBackLabel: str, backgroundLabel: str):
        self.NUM_DECKS = NUM_DECKS
        self.NUM_BACKGROUNDS = NUM_BACKGROUNDS
        self.FRS_DECK = FRS_DECK
        self.FRS_BACKGROUND = FRS_BACKGROUND
        self.decks = decks
        self.backgrounds = backgrounds
        self.ok = ok
        self.deckNumber = deckNumber
        self.backgroundNumber = backgroundNumber
        self.exited = exited
        self.cardBackLabel = cardBackLabel
        self.backgroundLabel = backgroundLabel
        
        pass
    @property
    def backgroundLabel(self):
        return self.__backgroundLabel
    @backgroundLabel.setter
    def backgroundLabel(self, backgroundLabel: str):
        self.__backgroundLabel = backgroundLabel

    @property
    def NUM_BACKGROUNDS(self):
        return self.__NUM_BACKGROUNDS
    @NUM_BACKGROUNDS.setter
    def NUM_BACKGROUNDS(self, NUM_BACKGROUNDS: int):
        self.__NUM_BACKGROUNDS = NUM_BACKGROUNDS

    @property
    def backgroundNumber(self):
        return self.__backgroundNumber
    @backgroundNumber.setter
    def backgroundNumber(self, backgroundNumber: int):
        self.__backgroundNumber = backgroundNumber

    @property
    def exited(self):
        return self.__exited
    @exited.setter
    def exited(self, exited: bool):
        self.__exited = exited

    @property
    def decks(self):
        return self.__decks
    @decks.setter
    def decks(self, decks: str):
        self.__decks = decks

    @property
    def NUM_DECKS(self):
        return self.__NUM_DECKS
    @NUM_DECKS.setter
    def NUM_DECKS(self, NUM_DECKS: int):
        self.__NUM_DECKS = NUM_DECKS

    @property
    def FRS_BACKGROUND(self):
        return self.__FRS_BACKGROUND
    @FRS_BACKGROUND.setter
    def FRS_BACKGROUND(self, FRS_BACKGROUND: int):
        self.__FRS_BACKGROUND = FRS_BACKGROUND

    @property
    def FRS_DECK(self):
        return self.__FRS_DECK
    @FRS_DECK.setter
    def FRS_DECK(self, FRS_DECK: int):
        self.__FRS_DECK = FRS_DECK

    @property
    def ok(self):
        return self.__ok
    @ok.setter
    def ok(self, ok: str):
        self.__ok = ok

    @property
    def backgrounds(self):
        return self.__backgrounds
    @backgrounds.setter
    def backgrounds(self, backgrounds: str):
        self.__backgrounds = backgrounds

    @property
    def cardBackLabel(self):
        return self.__cardBackLabel
    @cardBackLabel.setter
    def cardBackLabel(self, cardBackLabel: str):
        self.__cardBackLabel = cardBackLabel

    @property
    def deckNumber(self):
        return self.__deckNumber
    @deckNumber.setter
    def deckNumber(self, deckNumber: int):
        self.__deckNumber = deckNumber



class CardStack:

    pass


class Card:

    def __init__(self, SPADES_SUIT: str, CLUBS_SUIT: str, HEARTS_SUIT: str, DIAMONDS_SUIT: str, INVALID_SUIT: str, ACE: int, TWO: int, THREE: int, FOUR: int, FIVE: int, SIX: int, SEVEN: int, EIGHT: int, NINE: int, TEN: int, JACK: int, QUEEN: int, KING: int, INVALID_NUMBER: int, cardSuit: str, cardNumber: int, fullCardNumber: int, cardColor: int, deckNumber: int, image: str, cardBack: str, cardImageString: str, cardHighlighted: str, faceUp: bool, highlighted: bool, location: str, deck5: "Deck" = None, cardStack11: "CardStack" = None):
        self.SPADES_SUIT = SPADES_SUIT
        self.CLUBS_SUIT = CLUBS_SUIT
        self.HEARTS_SUIT = HEARTS_SUIT
        self.DIAMONDS_SUIT = DIAMONDS_SUIT
        self.INVALID_SUIT = INVALID_SUIT
        self.ACE = ACE
        self.TWO = TWO
        self.THREE = THREE
        self.FOUR = FOUR
        self.FIVE = FIVE
        self.SIX = SIX
        self.SEVEN = SEVEN
        self.EIGHT = EIGHT
        self.NINE = NINE
        self.TEN = TEN
        self.JACK = JACK
        self.QUEEN = QUEEN
        self.KING = KING
        self.INVALID_NUMBER = INVALID_NUMBER
        self.cardSuit = cardSuit
        self.cardNumber = cardNumber
        self.fullCardNumber = fullCardNumber
        self.cardColor = cardColor
        self.deckNumber = deckNumber
        self.image = image
        self.cardBack = cardBack
        self.cardImageString = cardImageString
        self.cardHighlighted = cardHighlighted
        self.faceUp = faceUp
        self.highlighted = highlighted
        self.location = location
        self.deck5 = deck5
        self.cardStack11 = cardStack11
        
        pass
    @property
    def cardImageString(self):
        return self.__cardImageString
    @cardImageString.setter
    def cardImageString(self, cardImageString: str):
        self.__cardImageString = cardImageString

    @property
    def highlighted(self):
        return self.__highlighted
    @highlighted.setter
    def highlighted(self, highlighted: bool):
        self.__highlighted = highlighted

    @property
    def fullCardNumber(self):
        return self.__fullCardNumber
    @fullCardNumber.setter
    def fullCardNumber(self, fullCardNumber: int):
        self.__fullCardNumber = fullCardNumber

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def cardNumber(self):
        return self.__cardNumber
    @cardNumber.setter
    def cardNumber(self, cardNumber: int):
        self.__cardNumber = cardNumber

    @property
    def cardHighlighted(self):
        return self.__cardHighlighted
    @cardHighlighted.setter
    def cardHighlighted(self, cardHighlighted: str):
        self.__cardHighlighted = cardHighlighted

    @property
    def QUEEN(self):
        return self.__QUEEN
    @QUEEN.setter
    def QUEEN(self, QUEEN: int):
        self.__QUEEN = QUEEN

    @property
    def HEARTS_SUIT(self):
        return self.__HEARTS_SUIT
    @HEARTS_SUIT.setter
    def HEARTS_SUIT(self, HEARTS_SUIT: str):
        self.__HEARTS_SUIT = HEARTS_SUIT

    @property
    def JACK(self):
        return self.__JACK
    @JACK.setter
    def JACK(self, JACK: int):
        self.__JACK = JACK

    @property
    def INVALID_NUMBER(self):
        return self.__INVALID_NUMBER
    @INVALID_NUMBER.setter
    def INVALID_NUMBER(self, INVALID_NUMBER: int):
        self.__INVALID_NUMBER = INVALID_NUMBER

    @property
    def FOUR(self):
        return self.__FOUR
    @FOUR.setter
    def FOUR(self, FOUR: int):
        self.__FOUR = FOUR

    @property
    def DIAMONDS_SUIT(self):
        return self.__DIAMONDS_SUIT
    @DIAMONDS_SUIT.setter
    def DIAMONDS_SUIT(self, DIAMONDS_SUIT: str):
        self.__DIAMONDS_SUIT = DIAMONDS_SUIT

    @property
    def faceUp(self):
        return self.__faceUp
    @faceUp.setter
    def faceUp(self, faceUp: bool):
        self.__faceUp = faceUp

    @property
    def TWO(self):
        return self.__TWO
    @TWO.setter
    def TWO(self, TWO: int):
        self.__TWO = TWO

    @property
    def INVALID_SUIT(self):
        return self.__INVALID_SUIT
    @INVALID_SUIT.setter
    def INVALID_SUIT(self, INVALID_SUIT: str):
        self.__INVALID_SUIT = INVALID_SUIT

    @property
    def cardBack(self):
        return self.__cardBack
    @cardBack.setter
    def cardBack(self, cardBack: str):
        self.__cardBack = cardBack

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def EIGHT(self):
        return self.__EIGHT
    @EIGHT.setter
    def EIGHT(self, EIGHT: int):
        self.__EIGHT = EIGHT

    @property
    def FIVE(self):
        return self.__FIVE
    @FIVE.setter
    def FIVE(self, FIVE: int):
        self.__FIVE = FIVE

    @property
    def SPADES_SUIT(self):
        return self.__SPADES_SUIT
    @SPADES_SUIT.setter
    def SPADES_SUIT(self, SPADES_SUIT: str):
        self.__SPADES_SUIT = SPADES_SUIT

    @property
    def THREE(self):
        return self.__THREE
    @THREE.setter
    def THREE(self, THREE: int):
        self.__THREE = THREE

    @property
    def TEN(self):
        return self.__TEN
    @TEN.setter
    def TEN(self, TEN: int):
        self.__TEN = TEN

    @property
    def ACE(self):
        return self.__ACE
    @ACE.setter
    def ACE(self, ACE: int):
        self.__ACE = ACE

    @property
    def SEVEN(self):
        return self.__SEVEN
    @SEVEN.setter
    def SEVEN(self, SEVEN: int):
        self.__SEVEN = SEVEN

    @property
    def KING(self):
        return self.__KING
    @KING.setter
    def KING(self, KING: int):
        self.__KING = KING

    @property
    def cardSuit(self):
        return self.__cardSuit
    @cardSuit.setter
    def cardSuit(self, cardSuit: str):
        self.__cardSuit = cardSuit

    @property
    def deckNumber(self):
        return self.__deckNumber
    @deckNumber.setter
    def deckNumber(self, deckNumber: int):
        self.__deckNumber = deckNumber

    @property
    def NINE(self):
        return self.__NINE
    @NINE.setter
    def NINE(self, NINE: int):
        self.__NINE = NINE

    @property
    def CLUBS_SUIT(self):
        return self.__CLUBS_SUIT
    @CLUBS_SUIT.setter
    def CLUBS_SUIT(self, CLUBS_SUIT: str):
        self.__CLUBS_SUIT = CLUBS_SUIT

    @property
    def SIX(self):
        return self.__SIX
    @SIX.setter
    def SIX(self, SIX: int):
        self.__SIX = SIX

    @property
    def cardColor(self):
        return self.__cardColor
    @cardColor.setter
    def cardColor(self, cardColor: int):
        self.__cardColor = cardColor

    @property
    def deck5(self):
        return self.__deck5
    @deck5.setter
    def deck5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__deck5", None)
        self.__deck5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card4"):
                opp_val = getattr(old_value, "card4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card4"):
                opp_val = getattr(value, "card4", None)
                if opp_val is None:
                    setattr(value, "card4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cardStack11(self):
        return self.__cardStack11
    @cardStack11.setter
    def cardStack11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__cardStack11", None)
        self.__cardStack11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card10"):
                opp_val = getattr(old_value, "card10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card10"):
                opp_val = getattr(value, "card10", None)
                if opp_val is None:
                    setattr(value, "card10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class AcePile:

    def __init__(self, suit: str, solitaireBoard7: "SolitaireBoard" = None):
        self.suit = suit
        self.solitaireBoard7 = solitaireBoard7
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit

    @property
    def solitaireBoard7(self):
        return self.__solitaireBoard7
    @solitaireBoard7.setter
    def solitaireBoard7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AcePile__solitaireBoard7", None)
        self.__solitaireBoard7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "acePile6"):
                opp_val = getattr(old_value, "acePile6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "acePile6"):
                opp_val = getattr(value, "acePile6", None)
                if opp_val is None:
                    setattr(value, "acePile6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

