from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class User_Actor:

    pass





class Help_external:

    pass


class Game_external:

    pass


class Main_Game_Board_external:

    pass


class SoundThread:

    def __init__(self, sequencer: str):
        self.sequencer = sequencer
        
        pass
    @property
    def sequencer(self):
        return self.__sequencer
    @sequencer.setter
    def sequencer(self, sequencer: str):
        self.__sequencer = sequencer



class WinScreen:

    def __init__(self, sound: str):
        self.sound = sound
        
        pass
    @property
    def sound(self):
        return self.__sound
    @sound.setter
    def sound(self, sound: str):
        self.__sound = sound



class SolitairePanel:

    def __init__(self, backGroundNumber: str, background: str):
        self.backGroundNumber = backGroundNumber
        self.background = background
        
        pass
    @property
    def backGroundNumber(self):
        return self.__backGroundNumber
    @backGroundNumber.setter
    def backGroundNumber(self, backGroundNumber: str):
        self.__backGroundNumber = backGroundNumber

    @property
    def background(self):
        return self.__background
    @background.setter
    def background(self, background: str):
        self.__background = background



class SolitaireLayout:

    def __init__(self, COLUMN_ONE: str, COLUMN_TWO: str, COLUMN_THREE: str, COLUMN_FOUR: str, SPADES_ACE_PILE: str, deck: str, cellOne: str, cellTwo: str, cellThree: str, cellFour: str, CLUBS_ACE_PILE: str, DIAMONDS_ACE_PILE: str, HEARTS_ACE_PILE: str, DISCARD_PILE: str, DECK: str, CELL_ONE: str, CELL_TWO: str, CELL_THREE: str, CELL_FOUR: str, colOne: str, ColTwo: str, ColThree: str, ColFour: str, acespades: str, aceClubs: str, aceDiamonds: str, aceHearts: str, discardPile: str):
        self.COLUMN_ONE = COLUMN_ONE
        self.COLUMN_TWO = COLUMN_TWO
        self.COLUMN_THREE = COLUMN_THREE
        self.COLUMN_FOUR = COLUMN_FOUR
        self.SPADES_ACE_PILE = SPADES_ACE_PILE
        self.deck = deck
        self.cellOne = cellOne
        self.cellTwo = cellTwo
        self.cellThree = cellThree
        self.cellFour = cellFour
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
        self.ColTwo = ColTwo
        self.ColThree = ColThree
        self.ColFour = ColFour
        self.acespades = acespades
        self.aceClubs = aceClubs
        self.aceDiamonds = aceDiamonds
        self.aceHearts = aceHearts
        self.discardPile = discardPile
        
        pass
    @property
    def HEARTS_ACE_PILE(self):
        return self.__HEARTS_ACE_PILE
    @HEARTS_ACE_PILE.setter
    def HEARTS_ACE_PILE(self, HEARTS_ACE_PILE: str):
        self.__HEARTS_ACE_PILE = HEARTS_ACE_PILE

    @property
    def CELL_THREE(self):
        return self.__CELL_THREE
    @CELL_THREE.setter
    def CELL_THREE(self, CELL_THREE: str):
        self.__CELL_THREE = CELL_THREE

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def COLUMN_THREE(self):
        return self.__COLUMN_THREE
    @COLUMN_THREE.setter
    def COLUMN_THREE(self, COLUMN_THREE: str):
        self.__COLUMN_THREE = COLUMN_THREE

    @property
    def colOne(self):
        return self.__colOne
    @colOne.setter
    def colOne(self, colOne: str):
        self.__colOne = colOne

    @property
    def cellTwo(self):
        return self.__cellTwo
    @cellTwo.setter
    def cellTwo(self, cellTwo: str):
        self.__cellTwo = cellTwo

    @property
    def CELL_TWO(self):
        return self.__CELL_TWO
    @CELL_TWO.setter
    def CELL_TWO(self, CELL_TWO: str):
        self.__CELL_TWO = CELL_TWO

    @property
    def aceDiamonds(self):
        return self.__aceDiamonds
    @aceDiamonds.setter
    def aceDiamonds(self, aceDiamonds: str):
        self.__aceDiamonds = aceDiamonds

    @property
    def cellFour(self):
        return self.__cellFour
    @cellFour.setter
    def cellFour(self, cellFour: str):
        self.__cellFour = cellFour

    @property
    def SPADES_ACE_PILE(self):
        return self.__SPADES_ACE_PILE
    @SPADES_ACE_PILE.setter
    def SPADES_ACE_PILE(self, SPADES_ACE_PILE: str):
        self.__SPADES_ACE_PILE = SPADES_ACE_PILE

    @property
    def CELL_ONE(self):
        return self.__CELL_ONE
    @CELL_ONE.setter
    def CELL_ONE(self, CELL_ONE: str):
        self.__CELL_ONE = CELL_ONE

    @property
    def COLUMN_TWO(self):
        return self.__COLUMN_TWO
    @COLUMN_TWO.setter
    def COLUMN_TWO(self, COLUMN_TWO: str):
        self.__COLUMN_TWO = COLUMN_TWO

    @property
    def DECK(self):
        return self.__DECK
    @DECK.setter
    def DECK(self, DECK: str):
        self.__DECK = DECK

    @property
    def ColFour(self):
        return self.__ColFour
    @ColFour.setter
    def ColFour(self, ColFour: str):
        self.__ColFour = ColFour

    @property
    def discardPile(self):
        return self.__discardPile
    @discardPile.setter
    def discardPile(self, discardPile: str):
        self.__discardPile = discardPile

    @property
    def acespades(self):
        return self.__acespades
    @acespades.setter
    def acespades(self, acespades: str):
        self.__acespades = acespades

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
    def cellOne(self):
        return self.__cellOne
    @cellOne.setter
    def cellOne(self, cellOne: str):
        self.__cellOne = cellOne

    @property
    def cellThree(self):
        return self.__cellThree
    @cellThree.setter
    def cellThree(self, cellThree: str):
        self.__cellThree = cellThree

    @property
    def ColTwo(self):
        return self.__ColTwo
    @ColTwo.setter
    def ColTwo(self, ColTwo: str):
        self.__ColTwo = ColTwo

    @property
    def CLUBS_ACE_PILE(self):
        return self.__CLUBS_ACE_PILE
    @CLUBS_ACE_PILE.setter
    def CLUBS_ACE_PILE(self, CLUBS_ACE_PILE: str):
        self.__CLUBS_ACE_PILE = CLUBS_ACE_PILE

    @property
    def COLUMN_FOUR(self):
        return self.__COLUMN_FOUR
    @COLUMN_FOUR.setter
    def COLUMN_FOUR(self, COLUMN_FOUR: str):
        self.__COLUMN_FOUR = COLUMN_FOUR

    @property
    def aceHearts(self):
        return self.__aceHearts
    @aceHearts.setter
    def aceHearts(self, aceHearts: str):
        self.__aceHearts = aceHearts

    @property
    def ColThree(self):
        return self.__ColThree
    @ColThree.setter
    def ColThree(self, ColThree: str):
        self.__ColThree = ColThree

    @property
    def DIAMONDS_ACE_PILE(self):
        return self.__DIAMONDS_ACE_PILE
    @DIAMONDS_ACE_PILE.setter
    def DIAMONDS_ACE_PILE(self, DIAMONDS_ACE_PILE: str):
        self.__DIAMONDS_ACE_PILE = DIAMONDS_ACE_PILE

    @property
    def CELL_FOUR(self):
        return self.__CELL_FOUR
    @CELL_FOUR.setter
    def CELL_FOUR(self, CELL_FOUR: str):
        self.__CELL_FOUR = CELL_FOUR

    @property
    def COLUMN_ONE(self):
        return self.__COLUMN_ONE
    @COLUMN_ONE.setter
    def COLUMN_ONE(self, COLUMN_ONE: str):
        self.__COLUMN_ONE = COLUMN_ONE



class windowclosing:

    pass


class TimerListener:

    pass


class MyMouseListener:

    def __init__(self, hasSelected: bool, singleCardSelected: bool, clickedCard: str, source: str, destination: str, temp: str, tempCard: str, rightClicked: bool):
        self.hasSelected = hasSelected
        self.singleCardSelected = singleCardSelected
        self.clickedCard = clickedCard
        self.source = source
        self.destination = destination
        self.temp = temp
        self.tempCard = tempCard
        self.rightClicked = rightClicked
        
        pass
    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self, temp: str):
        self.__temp = temp

    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination

    @property
    def clickedCard(self):
        return self.__clickedCard
    @clickedCard.setter
    def clickedCard(self, clickedCard: str):
        self.__clickedCard = clickedCard

    @property
    def rightClicked(self):
        return self.__rightClicked
    @rightClicked.setter
    def rightClicked(self, rightClicked: bool):
        self.__rightClicked = rightClicked

    @property
    def singleCardSelected(self):
        return self.__singleCardSelected
    @singleCardSelected.setter
    def singleCardSelected(self, singleCardSelected: bool):
        self.__singleCardSelected = singleCardSelected

    @property
    def hasSelected(self):
        return self.__hasSelected
    @hasSelected.setter
    def hasSelected(self, hasSelected: bool):
        self.__hasSelected = hasSelected

    @property
    def tempCard(self):
        return self.__tempCard
    @tempCard.setter
    def tempCard(self, tempCard: str):
        self.__tempCard = tempCard



class SolitaireBoard:

    def __init__(self, acePiles: str, cells: str, mainPanel: str, ml: str, wl: str, timer: str, statusBar: str, timerLabel: str, timerCount: str, timerToRunNextGame: str, timerToRun: bool, winAnimationStatus: str, newDifficulty: str, sourceList: str, destinationList: str, numCards: str, numCardsInDiscardView: str, GAME_WON: str, GAME_LOST: str, RESET_STATS: str, DO_NOTHING: str, GAME_SAVED: str, drawCount: str, newDrawCount: str, backgroundNumber: str, deckNumber: str, deck: Deck, columns: str, discardPile: str, dealDeck: DealDeck):
        self.acePiles = acePiles
        self.cells = cells
        self.mainPanel = mainPanel
        self.ml = ml
        self.wl = wl
        self.timer = timer
        self.statusBar = statusBar
        self.timerLabel = timerLabel
        self.timerCount = timerCount
        self.timerToRunNextGame = timerToRunNextGame
        self.timerToRun = timerToRun
        self.winAnimationStatus = winAnimationStatus
        self.newDifficulty = newDifficulty
        self.sourceList = sourceList
        self.destinationList = destinationList
        self.numCards = numCards
        self.numCardsInDiscardView = numCardsInDiscardView
        self.GAME_WON = GAME_WON
        self.GAME_LOST = GAME_LOST
        self.RESET_STATS = RESET_STATS
        self.DO_NOTHING = DO_NOTHING
        self.GAME_SAVED = GAME_SAVED
        self.drawCount = drawCount
        self.newDrawCount = newDrawCount
        self.backgroundNumber = backgroundNumber
        self.deckNumber = deckNumber
        self.deck = deck
        self.columns = columns
        self.discardPile = discardPile
        self.dealDeck = dealDeck
        
        pass
    @property
    def newDifficulty(self):
        return self.__newDifficulty
    @newDifficulty.setter
    def newDifficulty(self, newDifficulty: str):
        self.__newDifficulty = newDifficulty

    @property
    def cells(self):
        return self.__cells
    @cells.setter
    def cells(self, cells: str):
        self.__cells = cells

    @property
    def discardPile(self):
        return self.__discardPile
    @discardPile.setter
    def discardPile(self, discardPile: str):
        self.__discardPile = discardPile

    @property
    def GAME_SAVED(self):
        return self.__GAME_SAVED
    @GAME_SAVED.setter
    def GAME_SAVED(self, GAME_SAVED: str):
        self.__GAME_SAVED = GAME_SAVED

    @property
    def ml(self):
        return self.__ml
    @ml.setter
    def ml(self, ml: str):
        self.__ml = ml

    @property
    def timerCount(self):
        return self.__timerCount
    @timerCount.setter
    def timerCount(self, timerCount: str):
        self.__timerCount = timerCount

    @property
    def sourceList(self):
        return self.__sourceList
    @sourceList.setter
    def sourceList(self, sourceList: str):
        self.__sourceList = sourceList

    @property
    def numCards(self):
        return self.__numCards
    @numCards.setter
    def numCards(self, numCards: str):
        self.__numCards = numCards

    @property
    def dealDeck(self):
        return self.__dealDeck
    @dealDeck.setter
    def dealDeck(self, dealDeck: DealDeck):
        self.__dealDeck = dealDeck

    @property
    def backgroundNumber(self):
        return self.__backgroundNumber
    @backgroundNumber.setter
    def backgroundNumber(self, backgroundNumber: str):
        self.__backgroundNumber = backgroundNumber

    @property
    def GAME_LOST(self):
        return self.__GAME_LOST
    @GAME_LOST.setter
    def GAME_LOST(self, GAME_LOST: str):
        self.__GAME_LOST = GAME_LOST

    @property
    def columns(self):
        return self.__columns
    @columns.setter
    def columns(self, columns: str):
        self.__columns = columns

    @property
    def statusBar(self):
        return self.__statusBar
    @statusBar.setter
    def statusBar(self, statusBar: str):
        self.__statusBar = statusBar

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: Deck):
        self.__deck = deck

    @property
    def wl(self):
        return self.__wl
    @wl.setter
    def wl(self, wl: str):
        self.__wl = wl

    @property
    def RESET_STATS(self):
        return self.__RESET_STATS
    @RESET_STATS.setter
    def RESET_STATS(self, RESET_STATS: str):
        self.__RESET_STATS = RESET_STATS

    @property
    def mainPanel(self):
        return self.__mainPanel
    @mainPanel.setter
    def mainPanel(self, mainPanel: str):
        self.__mainPanel = mainPanel

    @property
    def acePiles(self):
        return self.__acePiles
    @acePiles.setter
    def acePiles(self, acePiles: str):
        self.__acePiles = acePiles

    @property
    def GAME_WON(self):
        return self.__GAME_WON
    @GAME_WON.setter
    def GAME_WON(self, GAME_WON: str):
        self.__GAME_WON = GAME_WON

    @property
    def timerLabel(self):
        return self.__timerLabel
    @timerLabel.setter
    def timerLabel(self, timerLabel: str):
        self.__timerLabel = timerLabel

    @property
    def numCardsInDiscardView(self):
        return self.__numCardsInDiscardView
    @numCardsInDiscardView.setter
    def numCardsInDiscardView(self, numCardsInDiscardView: str):
        self.__numCardsInDiscardView = numCardsInDiscardView

    @property
    def winAnimationStatus(self):
        return self.__winAnimationStatus
    @winAnimationStatus.setter
    def winAnimationStatus(self, winAnimationStatus: str):
        self.__winAnimationStatus = winAnimationStatus

    @property
    def timerToRun(self):
        return self.__timerToRun
    @timerToRun.setter
    def timerToRun(self, timerToRun: bool):
        self.__timerToRun = timerToRun

    @property
    def DO_NOTHING(self):
        return self.__DO_NOTHING
    @DO_NOTHING.setter
    def DO_NOTHING(self, DO_NOTHING: str):
        self.__DO_NOTHING = DO_NOTHING

    @property
    def deckNumber(self):
        return self.__deckNumber
    @deckNumber.setter
    def deckNumber(self, deckNumber: str):
        self.__deckNumber = deckNumber

    @property
    def timer(self):
        return self.__timer
    @timer.setter
    def timer(self, timer: str):
        self.__timer = timer

    @property
    def drawCount(self):
        return self.__drawCount
    @drawCount.setter
    def drawCount(self, drawCount: str):
        self.__drawCount = drawCount

    @property
    def newDrawCount(self):
        return self.__newDrawCount
    @newDrawCount.setter
    def newDrawCount(self, newDrawCount: str):
        self.__newDrawCount = newDrawCount

    @property
    def destinationList(self):
        return self.__destinationList
    @destinationList.setter
    def destinationList(self, destinationList: str):
        self.__destinationList = destinationList

    @property
    def timerToRunNextGame(self):
        return self.__timerToRunNextGame
    @timerToRunNextGame.setter
    def timerToRunNextGame(self, timerToRunNextGame: str):
        self.__timerToRunNextGame = timerToRunNextGame



class SingleCell:

    pass


class FourRowSolitaire:

    def __init__(self, version: str, menubar: str, game: str, helpMenu: str, newGame: str, undo: str, hint: str, statistics: str, options: str, appearance: str, exit: str, help: str, about: str, checkUpdate: str):
        self.version = version
        self.menubar = menubar
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
    def about(self):
        return self.__about
    @about.setter
    def about(self, about: str):
        self.__about = about

    @property
    def menubar(self):
        return self.__menubar
    @menubar.setter
    def menubar(self, menubar: str):
        self.__menubar = menubar

    @property
    def version(self):
        return self.__version
    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def statistics(self):
        return self.__statistics
    @statistics.setter
    def statistics(self, statistics: str):
        self.__statistics = statistics

    @property
    def exit(self):
        return self.__exit
    @exit.setter
    def exit(self, exit: str):
        self.__exit = exit

    @property
    def checkUpdate(self):
        return self.__checkUpdate
    @checkUpdate.setter
    def checkUpdate(self, checkUpdate: str):
        self.__checkUpdate = checkUpdate

    @property
    def helpMenu(self):
        return self.__helpMenu
    @helpMenu.setter
    def helpMenu(self, helpMenu: str):
        self.__helpMenu = helpMenu

    @property
    def help(self):
        return self.__help
    @help.setter
    def help(self, help: str):
        self.__help = help

    @property
    def options(self):
        return self.__options
    @options.setter
    def options(self, options: str):
        self.__options = options

    @property
    def newGame(self):
        return self.__newGame
    @newGame.setter
    def newGame(self, newGame: str):
        self.__newGame = newGame

    @property
    def hint(self):
        return self.__hint
    @hint.setter
    def hint(self, hint: str):
        self.__hint = hint

    @property
    def game(self):
        return self.__game
    @game.setter
    def game(self, game: str):
        self.__game = game

    @property
    def appearance(self):
        return self.__appearance
    @appearance.setter
    def appearance(self, appearance: str):
        self.__appearance = appearance

    @property
    def undo(self):
        return self.__undo
    @undo.setter
    def undo(self, undo: str):
        self.__undo = undo



class FireworksDisplay:

    def __init__(self, x: str, y: str, colors: str, xx: str, yy: str, num: str, numSets: str, startValue: str, time: str, random: str, NUM_FIREWORKS: str, FIREWORKS_SIZE: str, SET_DELAY: str, FIREWORKS_TIME: str):
        self.x = x
        self.y = y
        self.colors = colors
        self.xx = xx
        self.yy = yy
        self.num = num
        self.numSets = numSets
        self.startValue = startValue
        self.time = time
        self.random = random
        self.NUM_FIREWORKS = NUM_FIREWORKS
        self.FIREWORKS_SIZE = FIREWORKS_SIZE
        self.SET_DELAY = SET_DELAY
        self.FIREWORKS_TIME = FIREWORKS_TIME
        
        pass
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def yy(self):
        return self.__yy
    @yy.setter
    def yy(self, yy: str):
        self.__yy = yy

    @property
    def colors(self):
        return self.__colors
    @colors.setter
    def colors(self, colors: str):
        self.__colors = colors

    @property
    def NUM_FIREWORKS(self):
        return self.__NUM_FIREWORKS
    @NUM_FIREWORKS.setter
    def NUM_FIREWORKS(self, NUM_FIREWORKS: str):
        self.__NUM_FIREWORKS = NUM_FIREWORKS

    @property
    def xx(self):
        return self.__xx
    @xx.setter
    def xx(self, xx: str):
        self.__xx = xx

    @property
    def startValue(self):
        return self.__startValue
    @startValue.setter
    def startValue(self, startValue: str):
        self.__startValue = startValue

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: str):
        self.__num = num

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def numSets(self):
        return self.__numSets
    @numSets.setter
    def numSets(self, numSets: str):
        self.__numSets = numSets

    @property
    def SET_DELAY(self):
        return self.__SET_DELAY
    @SET_DELAY.setter
    def SET_DELAY(self, SET_DELAY: str):
        self.__SET_DELAY = SET_DELAY

    @property
    def FIREWORKS_SIZE(self):
        return self.__FIREWORKS_SIZE
    @FIREWORKS_SIZE.setter
    def FIREWORKS_SIZE(self, FIREWORKS_SIZE: str):
        self.__FIREWORKS_SIZE = FIREWORKS_SIZE

    @property
    def random(self):
        return self.__random
    @random.setter
    def random(self, random: str):
        self.__random = random

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def FIREWORKS_TIME(self):
        return self.__FIREWORKS_TIME
    @FIREWORKS_TIME.setter
    def FIREWORKS_TIME(self, FIREWORKS_TIME: str):
        self.__FIREWORKS_TIME = FIREWORKS_TIME



class DiscardPile:

    def __init__(self, drawCount: str, CardsLeftFromDraw: str):
        self.drawCount = drawCount
        self.CardsLeftFromDraw = CardsLeftFromDraw
        
        pass
    @property
    def CardsLeftFromDraw(self):
        return self.__CardsLeftFromDraw
    @CardsLeftFromDraw.setter
    def CardsLeftFromDraw(self, CardsLeftFromDraw: str):
        self.__CardsLeftFromDraw = CardsLeftFromDraw

    @property
    def drawCount(self):
        return self.__drawCount
    @drawCount.setter
    def drawCount(self, drawCount: str):
        self.__drawCount = drawCount



class Deck:

    def __init__(self, deckNumber: str, deck: str):
        self.deckNumber = deckNumber
        self.deck = deck
        
        pass
    @property
    def deckNumber(self):
        return self.__deckNumber
    @deckNumber.setter
    def deckNumber(self, deckNumber: str):
        self.__deckNumber = deckNumber

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck



class DealDeck:

    def __init__(self, discardPile: str, numTimesThroughDeck: str, drawCount: str, difficulty: str, DRAW_ONE_THROUGH_LIMIT: str, DRAW_THREE_THROUGH_LIMIT: str, EASY_THROUGH_LIMIT: str, MEDIUM_THROUGH_LIMIT: str, HARD_THROUGH_LIMIT: str, deckThroughLimit: str, redealable: bool):
        self.discardPile = discardPile
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
        
        pass
    @property
    def HARD_THROUGH_LIMIT(self):
        return self.__HARD_THROUGH_LIMIT
    @HARD_THROUGH_LIMIT.setter
    def HARD_THROUGH_LIMIT(self, HARD_THROUGH_LIMIT: str):
        self.__HARD_THROUGH_LIMIT = HARD_THROUGH_LIMIT

    @property
    def deckThroughLimit(self):
        return self.__deckThroughLimit
    @deckThroughLimit.setter
    def deckThroughLimit(self, deckThroughLimit: str):
        self.__deckThroughLimit = deckThroughLimit

    @property
    def drawCount(self):
        return self.__drawCount
    @drawCount.setter
    def drawCount(self, drawCount: str):
        self.__drawCount = drawCount

    @property
    def numTimesThroughDeck(self):
        return self.__numTimesThroughDeck
    @numTimesThroughDeck.setter
    def numTimesThroughDeck(self, numTimesThroughDeck: str):
        self.__numTimesThroughDeck = numTimesThroughDeck

    @property
    def EASY_THROUGH_LIMIT(self):
        return self.__EASY_THROUGH_LIMIT
    @EASY_THROUGH_LIMIT.setter
    def EASY_THROUGH_LIMIT(self, EASY_THROUGH_LIMIT: str):
        self.__EASY_THROUGH_LIMIT = EASY_THROUGH_LIMIT

    @property
    def discardPile(self):
        return self.__discardPile
    @discardPile.setter
    def discardPile(self, discardPile: str):
        self.__discardPile = discardPile

    @property
    def DRAW_ONE_THROUGH_LIMIT(self):
        return self.__DRAW_ONE_THROUGH_LIMIT
    @DRAW_ONE_THROUGH_LIMIT.setter
    def DRAW_ONE_THROUGH_LIMIT(self, DRAW_ONE_THROUGH_LIMIT: str):
        self.__DRAW_ONE_THROUGH_LIMIT = DRAW_ONE_THROUGH_LIMIT

    @property
    def MEDIUM_THROUGH_LIMIT(self):
        return self.__MEDIUM_THROUGH_LIMIT
    @MEDIUM_THROUGH_LIMIT.setter
    def MEDIUM_THROUGH_LIMIT(self, MEDIUM_THROUGH_LIMIT: str):
        self.__MEDIUM_THROUGH_LIMIT = MEDIUM_THROUGH_LIMIT

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
    def difficulty(self, difficulty: str):
        self.__difficulty = difficulty

    @property
    def DRAW_THREE_THROUGH_LIMIT(self):
        return self.__DRAW_THREE_THROUGH_LIMIT
    @DRAW_THREE_THROUGH_LIMIT.setter
    def DRAW_THREE_THROUGH_LIMIT(self, DRAW_THREE_THROUGH_LIMIT: str):
        self.__DRAW_THREE_THROUGH_LIMIT = DRAW_THREE_THROUGH_LIMIT



class Column:

    pass


class ChangeOptions:

    def __init__(self, drawCount: str, drawOne: str, drawThree: str, timerCheck: str, timer: str, winAnimationCheck: str, animation: str, winSoundCheck: str, sounds: str, difficulty: str, easy: str, medium: str, hard: str, ok: str, exited: bool):
        self.drawCount = drawCount
        self.drawOne = drawOne
        self.drawThree = drawThree
        self.timerCheck = timerCheck
        self.timer = timer
        self.winAnimationCheck = winAnimationCheck
        self.animation = animation
        self.winSoundCheck = winSoundCheck
        self.sounds = sounds
        self.difficulty = difficulty
        self.easy = easy
        self.medium = medium
        self.hard = hard
        self.ok = ok
        self.exited = exited
        
        pass
    @property
    def winSoundCheck(self):
        return self.__winSoundCheck
    @winSoundCheck.setter
    def winSoundCheck(self, winSoundCheck: str):
        self.__winSoundCheck = winSoundCheck

    @property
    def exited(self):
        return self.__exited
    @exited.setter
    def exited(self, exited: bool):
        self.__exited = exited

    @property
    def drawCount(self):
        return self.__drawCount
    @drawCount.setter
    def drawCount(self, drawCount: str):
        self.__drawCount = drawCount

    @property
    def drawThree(self):
        return self.__drawThree
    @drawThree.setter
    def drawThree(self, drawThree: str):
        self.__drawThree = drawThree

    @property
    def hard(self):
        return self.__hard
    @hard.setter
    def hard(self, hard: str):
        self.__hard = hard

    @property
    def winAnimationCheck(self):
        return self.__winAnimationCheck
    @winAnimationCheck.setter
    def winAnimationCheck(self, winAnimationCheck: str):
        self.__winAnimationCheck = winAnimationCheck

    @property
    def drawOne(self):
        return self.__drawOne
    @drawOne.setter
    def drawOne(self, drawOne: str):
        self.__drawOne = drawOne

    @property
    def easy(self):
        return self.__easy
    @easy.setter
    def easy(self, easy: str):
        self.__easy = easy

    @property
    def animation(self):
        return self.__animation
    @animation.setter
    def animation(self, animation: str):
        self.__animation = animation

    @property
    def sounds(self):
        return self.__sounds
    @sounds.setter
    def sounds(self, sounds: str):
        self.__sounds = sounds

    @property
    def timer(self):
        return self.__timer
    @timer.setter
    def timer(self, timer: str):
        self.__timer = timer

    @property
    def ok(self):
        return self.__ok
    @ok.setter
    def ok(self, ok: str):
        self.__ok = ok

    @property
    def medium(self):
        return self.__medium
    @medium.setter
    def medium(self, medium: str):
        self.__medium = medium

    @property
    def difficulty(self):
        return self.__difficulty
    @difficulty.setter
    def difficulty(self, difficulty: str):
        self.__difficulty = difficulty

    @property
    def timerCheck(self):
        return self.__timerCheck
    @timerCheck.setter
    def timerCheck(self, timerCheck: str):
        self.__timerCheck = timerCheck



class ChangeAppearance:

    def __init__(self, cardBackLabel: str, backGroundLabel: str, NUM_DECKS: str, NUM_BACKGROUNDS: str, FRS_DECK: str, FRS_BACKGROUND: str, decks: str, backgrounds: str, ok: str, deckNumber: str, backgroundNumber: str, exited: bool):
        self.cardBackLabel = cardBackLabel
        self.backGroundLabel = backGroundLabel
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
        
        pass
    @property
    def backGroundLabel(self):
        return self.__backGroundLabel
    @backGroundLabel.setter
    def backGroundLabel(self, backGroundLabel: str):
        self.__backGroundLabel = backGroundLabel

    @property
    def exited(self):
        return self.__exited
    @exited.setter
    def exited(self, exited: bool):
        self.__exited = exited

    @property
    def FRS_DECK(self):
        return self.__FRS_DECK
    @FRS_DECK.setter
    def FRS_DECK(self, FRS_DECK: str):
        self.__FRS_DECK = FRS_DECK

    @property
    def NUM_BACKGROUNDS(self):
        return self.__NUM_BACKGROUNDS
    @NUM_BACKGROUNDS.setter
    def NUM_BACKGROUNDS(self, NUM_BACKGROUNDS: str):
        self.__NUM_BACKGROUNDS = NUM_BACKGROUNDS

    @property
    def ok(self):
        return self.__ok
    @ok.setter
    def ok(self, ok: str):
        self.__ok = ok

    @property
    def backgroundNumber(self):
        return self.__backgroundNumber
    @backgroundNumber.setter
    def backgroundNumber(self, backgroundNumber: str):
        self.__backgroundNumber = backgroundNumber

    @property
    def NUM_DECKS(self):
        return self.__NUM_DECKS
    @NUM_DECKS.setter
    def NUM_DECKS(self, NUM_DECKS: str):
        self.__NUM_DECKS = NUM_DECKS

    @property
    def deckNumber(self):
        return self.__deckNumber
    @deckNumber.setter
    def deckNumber(self, deckNumber: str):
        self.__deckNumber = deckNumber

    @property
    def cardBackLabel(self):
        return self.__cardBackLabel
    @cardBackLabel.setter
    def cardBackLabel(self, cardBackLabel: str):
        self.__cardBackLabel = cardBackLabel

    @property
    def decks(self):
        return self.__decks
    @decks.setter
    def decks(self, decks: str):
        self.__decks = decks

    @property
    def backgrounds(self):
        return self.__backgrounds
    @backgrounds.setter
    def backgrounds(self, backgrounds: str):
        self.__backgrounds = backgrounds

    @property
    def FRS_BACKGROUND(self):
        return self.__FRS_BACKGROUND
    @FRS_BACKGROUND.setter
    def FRS_BACKGROUND(self, FRS_BACKGROUND: str):
        self.__FRS_BACKGROUND = FRS_BACKGROUND



class CardStack:

    def __init__(self, cards: str):
        self.cards = cards
        
        pass
    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards



class Card:

    def __init__(self, SPADES_SUIT: str, CLUBS_SUIT: str, HEARTS_SUIT: str, DIAMONDS_SUIT: str, INVALID_SUIT: str, ACE: str, TWO: str, THREE: str, FOUR: str, FIVE: str, SIX: str, SEVEN: str, EIGHT: str, NINE: str, TEN: str, JACK: str, QUEEN: str, KING: str, INVALID_NUMBER: str, cardSuit: str, cardNumber: str, fullCardNumber: str, cardColor: str, int_deckNumber: str, image: str, cardBack: str, cardImageString: str, cardHighLighted: str, faceUp: bool, highlighted: bool, location: str):
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
        self.int_deckNumber = int_deckNumber
        self.image = image
        self.cardBack = cardBack
        self.cardImageString = cardImageString
        self.cardHighLighted = cardHighLighted
        self.faceUp = faceUp
        self.highlighted = highlighted
        self.location = location
        
        pass
    @property
    def QUEEN(self):
        return self.__QUEEN
    @QUEEN.setter
    def QUEEN(self, QUEEN: str):
        self.__QUEEN = QUEEN

    @property
    def SPADES_SUIT(self):
        return self.__SPADES_SUIT
    @SPADES_SUIT.setter
    def SPADES_SUIT(self, SPADES_SUIT: str):
        self.__SPADES_SUIT = SPADES_SUIT

    @property
    def cardImageString(self):
        return self.__cardImageString
    @cardImageString.setter
    def cardImageString(self, cardImageString: str):
        self.__cardImageString = cardImageString

    @property
    def cardNumber(self):
        return self.__cardNumber
    @cardNumber.setter
    def cardNumber(self, cardNumber: str):
        self.__cardNumber = cardNumber

    @property
    def KING(self):
        return self.__KING
    @KING.setter
    def KING(self, KING: str):
        self.__KING = KING

    @property
    def ACE(self):
        return self.__ACE
    @ACE.setter
    def ACE(self, ACE: str):
        self.__ACE = ACE

    @property
    def DIAMONDS_SUIT(self):
        return self.__DIAMONDS_SUIT
    @DIAMONDS_SUIT.setter
    def DIAMONDS_SUIT(self, DIAMONDS_SUIT: str):
        self.__DIAMONDS_SUIT = DIAMONDS_SUIT

    @property
    def INVALID_SUIT(self):
        return self.__INVALID_SUIT
    @INVALID_SUIT.setter
    def INVALID_SUIT(self, INVALID_SUIT: str):
        self.__INVALID_SUIT = INVALID_SUIT

    @property
    def int_deckNumber(self):
        return self.__int_deckNumber
    @int_deckNumber.setter
    def int_deckNumber(self, int_deckNumber: str):
        self.__int_deckNumber = int_deckNumber

    @property
    def cardBack(self):
        return self.__cardBack
    @cardBack.setter
    def cardBack(self, cardBack: str):
        self.__cardBack = cardBack

    @property
    def SIX(self):
        return self.__SIX
    @SIX.setter
    def SIX(self, SIX: str):
        self.__SIX = SIX

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def JACK(self):
        return self.__JACK
    @JACK.setter
    def JACK(self, JACK: str):
        self.__JACK = JACK

    @property
    def faceUp(self):
        return self.__faceUp
    @faceUp.setter
    def faceUp(self, faceUp: bool):
        self.__faceUp = faceUp

    @property
    def HEARTS_SUIT(self):
        return self.__HEARTS_SUIT
    @HEARTS_SUIT.setter
    def HEARTS_SUIT(self, HEARTS_SUIT: str):
        self.__HEARTS_SUIT = HEARTS_SUIT

    @property
    def cardSuit(self):
        return self.__cardSuit
    @cardSuit.setter
    def cardSuit(self, cardSuit: str):
        self.__cardSuit = cardSuit

    @property
    def TEN(self):
        return self.__TEN
    @TEN.setter
    def TEN(self, TEN: str):
        self.__TEN = TEN

    @property
    def FOUR(self):
        return self.__FOUR
    @FOUR.setter
    def FOUR(self, FOUR: str):
        self.__FOUR = FOUR

    @property
    def TWO(self):
        return self.__TWO
    @TWO.setter
    def TWO(self, TWO: str):
        self.__TWO = TWO

    @property
    def THREE(self):
        return self.__THREE
    @THREE.setter
    def THREE(self, THREE: str):
        self.__THREE = THREE

    @property
    def highlighted(self):
        return self.__highlighted
    @highlighted.setter
    def highlighted(self, highlighted: bool):
        self.__highlighted = highlighted

    @property
    def cardHighLighted(self):
        return self.__cardHighLighted
    @cardHighLighted.setter
    def cardHighLighted(self, cardHighLighted: str):
        self.__cardHighLighted = cardHighLighted

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def NINE(self):
        return self.__NINE
    @NINE.setter
    def NINE(self, NINE: str):
        self.__NINE = NINE

    @property
    def SEVEN(self):
        return self.__SEVEN
    @SEVEN.setter
    def SEVEN(self, SEVEN: str):
        self.__SEVEN = SEVEN

    @property
    def FIVE(self):
        return self.__FIVE
    @FIVE.setter
    def FIVE(self, FIVE: str):
        self.__FIVE = FIVE

    @property
    def fullCardNumber(self):
        return self.__fullCardNumber
    @fullCardNumber.setter
    def fullCardNumber(self, fullCardNumber: str):
        self.__fullCardNumber = fullCardNumber

    @property
    def CLUBS_SUIT(self):
        return self.__CLUBS_SUIT
    @CLUBS_SUIT.setter
    def CLUBS_SUIT(self, CLUBS_SUIT: str):
        self.__CLUBS_SUIT = CLUBS_SUIT

    @property
    def INVALID_NUMBER(self):
        return self.__INVALID_NUMBER
    @INVALID_NUMBER.setter
    def INVALID_NUMBER(self, INVALID_NUMBER: str):
        self.__INVALID_NUMBER = INVALID_NUMBER

    @property
    def cardColor(self):
        return self.__cardColor
    @cardColor.setter
    def cardColor(self, cardColor: str):
        self.__cardColor = cardColor

    @property
    def EIGHT(self):
        return self.__EIGHT
    @EIGHT.setter
    def EIGHT(self, EIGHT: str):
        self.__EIGHT = EIGHT



class AcePile:

    def __init__(self, suit: str):
        self.suit = suit
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: str):
        self.__suit = suit



class Four_Row_Solitaire___Component:

    pass
