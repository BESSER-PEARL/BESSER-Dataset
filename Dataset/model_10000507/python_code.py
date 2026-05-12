from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class checkers_Position(Enum):
    pass

############################################
# Definition of Classes
############################################







class Checkers_Select__Help__UseCase:

    pass


class Checkers_Start_the_Game_GUI_UseCase:

    pass


class Computer_Player_1_Actor:

    pass


class Human_Player_2_Actor:

    pass


class Human_Player_1_Actor:

    pass


class Checkers_Close_or_Exit_Game_UseCase:

    pass


class Checkers_Move_Game_Pieces_UseCase:

    pass


class Checkers_Start_New_Game_UseCase:

    pass


class Checkers_Select__Player_Mode__UseCase:

    pass


class Checkers_Select__Difficulty_Level__UseCase:

    pass


class Checkers_Toggle__Sound__UseCase:

    pass





class genmymodelreverse_java_lang_Exception:

    pass


class genmymodelreverse_javax_swing_JScrollPane:

    pass


class genmymodelreverse_java_awt_event_MouseEvent:

    pass


class genmymodelreverse_java_awt_event_ItemEvent:

    pass


class genmymodelreverse_java_awt_Point:

    pass


class genmymodelreverse_javax_swing_JComboBox:

    pass


class genmymodelreverse_javax_swing_JLabel:

    pass


class genmymodelreverse_javax_swing_JRadioButton:

    pass


class genmymodelreverse_javax_swing_ButtonGroup:

    pass


class genmymodelreverse_javax_swing_ImageIcon:

    pass


class genmymodelreverse_javax_swing_JTextArea:

    pass


class genmymodelreverse_java_awt_Graphics(ABC):

    pass


class genmymodelreverse_javax_swing_JButton:

    pass


class genmymodelreverse_java_lang_Thread:

    pass


class genmymodelreverse_javax_swing_JDialog:

    pass


class genmymodelreverse_java_awt_event_MouseListener_Interface(ABC):

    pass


class genmymodelreverse_java_awt_event_MouseMotionListener_Interface(ABC):

    pass


class genmymodelreverse_java_awt_event_ItemListener_Interface(ABC):

    pass


class genmymodelreverse_javax_swing_JPanel:

    pass


class genmymodelreverse_java_util_Vector:

    pass


class genmymodelreverse_javax_swing_JFrame:

    pass


class genmymodelreverse_java_awt_event_ActionEvent:

    pass


class checkers_CheckerFrame:

    def __init__(self, gamePanel: str, startButton: str):
        self.gamePanel = gamePanel
        self.startButton = startButton
        
        pass
    @property
    def gamePanel(self):
        return self.__gamePanel
    @gamePanel.setter
    def gamePanel(self, gamePanel: str):
        self.__gamePanel = gamePanel

    @property
    def startButton(self):
        return self.__startButton
    @startButton.setter
    def startButton(self, startButton: str):
        self.__startButton = startButton



class checkers_GameEngine:

    def __init__(self, inf: int, normal: int, king: int, pos: int, edge: int):
        self.inf = inf
        self.normal = normal
        self.king = king
        self.pos = pos
        self.edge = edge
        
        pass
    @property
    def pos(self):
        return self.__pos
    @pos.setter
    def pos(self, pos: int):
        self.__pos = pos

    @property
    def king(self):
        return self.__king
    @king.setter
    def king(self, king: int):
        self.__king = king

    @property
    def normal(self):
        return self.__normal
    @normal.setter
    def normal(self, normal: int):
        self.__normal = normal

    @property
    def inf(self):
        return self.__inf
    @inf.setter
    def inf(self, inf: int):
        self.__inf = inf

    @property
    def edge(self):
        return self.__edge
    @edge.setter
    def edge(self, edge: int):
        self.__edge = edge



class checkers_StartPanel:

    pass


class checkers_PlaySound:

    def __init__(self, filename: str, EXTERNAL_BUFFER_SIZE: int):
        self.filename = filename
        self.EXTERNAL_BUFFER_SIZE = EXTERNAL_BUFFER_SIZE
        
        pass
    @property
    def EXTERNAL_BUFFER_SIZE(self):
        return self.__EXTERNAL_BUFFER_SIZE
    @EXTERNAL_BUFFER_SIZE.setter
    def EXTERNAL_BUFFER_SIZE(self, EXTERNAL_BUFFER_SIZE: int):
        self.__EXTERNAL_BUFFER_SIZE = EXTERNAL_BUFFER_SIZE

    @property
    def filename(self):
        return self.__filename
    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename



class checkers_IntelliChecker:

    pass


class checkers_Help:

    def __init__(self, hlp: genmymodelreverse_javax_swing_JScrollPane, txt: genmymodelreverse_javax_swing_JTextArea, checkers0: "checkers_Checkers" = None):
        self.hlp = hlp
        self.txt = txt
        self.checkers0 = checkers0
        
        pass
    @property
    def txt(self):
        return self.__txt
    @txt.setter
    def txt(self, txt: genmymodelreverse_javax_swing_JTextArea):
        self.__txt = txt

    @property
    def hlp(self):
        return self.__hlp
    @hlp.setter
    def hlp(self, hlp: genmymodelreverse_javax_swing_JScrollPane):
        self.__hlp = hlp

    @property
    def checkers0(self):
        return self.__checkers0
    @checkers0.setter
    def checkers0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_checkers_Help__checkers0", None)
        self.__checkers0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hp1"):
                opp_val = getattr(old_value, "hp1", None)
                if opp_val == self:
                    setattr(old_value, "hp1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hp1"):
                opp_val = getattr(value, "hp1", None)
                setattr(value, "hp1", self)



class checkers_GameWin:

    def __init__(self, p: genmymodelreverse_java_awt_Point, masseage: genmymodelreverse_javax_swing_JLabel):
        self.p = p
        self.masseage = masseage
        
        pass
    @property
    def p(self):
        return self.__p
    @p.setter
    def p(self, p: genmymodelreverse_java_awt_Point):
        self.__p = p

    @property
    def masseage(self):
        return self.__masseage
    @masseage.setter
    def masseage(self, masseage: genmymodelreverse_javax_swing_JLabel):
        self.__masseage = masseage



class checkers_Checkers:

    def __init__(self, g: genmymodelreverse_java_awt_Graphics, msg: genmymodelreverse_javax_swing_JTextArea, redN: genmymodelreverse_javax_swing_ImageIcon, yellowN: genmymodelreverse_javax_swing_ImageIcon, redK: genmymodelreverse_javax_swing_ImageIcon, yellowK: genmymodelreverse_javax_swing_ImageIcon, hlp: genmymodelreverse_javax_swing_ImageIcon, snp: genmymodelreverse_javax_swing_ImageIcon, mup: genmymodelreverse_javax_swing_ImageIcon, nwB: genmymodelreverse_javax_swing_JButton, unB: genmymodelreverse_javax_swing_JButton, hlpB: genmymodelreverse_javax_swing_JButton, snB: genmymodelreverse_javax_swing_JButton, players: genmymodelreverse_javax_swing_ButtonGroup, selectedColor: str, selectedMode: int, difficulty: int, redNormal: int, yellowNormal: int, redKing: int, yellowKing: int, empty: int, currType: int, movable: bool, board: str, preBoard1: str, preToMove1: int, preBoard2: str, preToMove2: int, preBoard3: str, preToMove3: int, endY: int, incomplete: bool, highlight: bool, toMove: int, loser: int, silent: bool, undoCount: int, won: int, winPoint: genmymodelreverse_java_awt_Point, p1: genmymodelreverse_javax_swing_JRadioButton, p2: genmymodelreverse_javax_swing_JRadioButton, colors: genmymodelreverse_javax_swing_ButtonGroup, c1: genmymodelreverse_javax_swing_JRadioButton, c2: genmymodelreverse_javax_swing_JRadioButton, mode: genmymodelreverse_javax_swing_JLabel, col: genmymodelreverse_javax_swing_JLabel, diff: genmymodelreverse_javax_swing_JLabel, rp: genmymodelreverse_javax_swing_JLabel, rpt: genmymodelreverse_javax_swing_JLabel, bpt: genmymodelreverse_javax_swing_JLabel, bp: genmymodelreverse_javax_swing_JLabel, rk: genmymodelreverse_javax_swing_JLabel, rkt: genmymodelreverse_javax_swing_JLabel, bkt: genmymodelreverse_javax_swing_JLabel, bk: genmymodelreverse_javax_swing_JLabel, level: genmymodelreverse_javax_swing_JComboBox, hp1: "checkers_Help" = None):
        self.g = g
        self.msg = msg
        self.redN = redN
        self.yellowN = yellowN
        self.redK = redK
        self.yellowK = yellowK
        self.hlp = hlp
        self.snp = snp
        self.mup = mup
        self.nwB = nwB
        self.unB = unB
        self.hlpB = hlpB
        self.snB = snB
        self.players = players
        self.selectedColor = selectedColor
        self.selectedMode = selectedMode
        self.difficulty = difficulty
        self.redNormal = redNormal
        self.yellowNormal = yellowNormal
        self.redKing = redKing
        self.yellowKing = yellowKing
        self.empty = empty
        self.currType = currType
        self.movable = movable
        self.board = board
        self.preBoard1 = preBoard1
        self.preToMove1 = preToMove1
        self.preBoard2 = preBoard2
        self.preToMove2 = preToMove2
        self.preBoard3 = preBoard3
        self.preToMove3 = preToMove3
        self.endY = endY
        self.incomplete = incomplete
        self.highlight = highlight
        self.toMove = toMove
        self.loser = loser
        self.silent = silent
        self.undoCount = undoCount
        self.won = won
        self.winPoint = winPoint
        self.p1 = p1
        self.p2 = p2
        self.colors = colors
        self.c1 = c1
        self.c2 = c2
        self.mode = mode
        self.col = col
        self.diff = diff
        self.rp = rp
        self.rpt = rpt
        self.bpt = bpt
        self.bp = bp
        self.rk = rk
        self.rkt = rkt
        self.bkt = bkt
        self.bk = bk
        self.level = level
        self.hp1 = hp1
        
        pass
    @property
    def hlp(self):
        return self.__hlp
    @hlp.setter
    def hlp(self, hlp: genmymodelreverse_javax_swing_ImageIcon):
        self.__hlp = hlp

    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: genmymodelreverse_javax_swing_ButtonGroup):
        self.__players = players

    @property
    def silent(self):
        return self.__silent
    @silent.setter
    def silent(self, silent: bool):
        self.__silent = silent

    @property
    def bkt(self):
        return self.__bkt
    @bkt.setter
    def bkt(self, bkt: genmymodelreverse_javax_swing_JLabel):
        self.__bkt = bkt

    @property
    def colors(self):
        return self.__colors
    @colors.setter
    def colors(self, colors: genmymodelreverse_javax_swing_ButtonGroup):
        self.__colors = colors

    @property
    def preToMove1(self):
        return self.__preToMove1
    @preToMove1.setter
    def preToMove1(self, preToMove1: int):
        self.__preToMove1 = preToMove1

    @property
    def rk(self):
        return self.__rk
    @rk.setter
    def rk(self, rk: genmymodelreverse_javax_swing_JLabel):
        self.__rk = rk

    @property
    def rkt(self):
        return self.__rkt
    @rkt.setter
    def rkt(self, rkt: genmymodelreverse_javax_swing_JLabel):
        self.__rkt = rkt

    @property
    def redNormal(self):
        return self.__redNormal
    @redNormal.setter
    def redNormal(self, redNormal: int):
        self.__redNormal = redNormal

    @property
    def col(self):
        return self.__col
    @col.setter
    def col(self, col: genmymodelreverse_javax_swing_JLabel):
        self.__col = col

    @property
    def mup(self):
        return self.__mup
    @mup.setter
    def mup(self, mup: genmymodelreverse_javax_swing_ImageIcon):
        self.__mup = mup

    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: str):
        self.__board = board

    @property
    def endY(self):
        return self.__endY
    @endY.setter
    def endY(self, endY: int):
        self.__endY = endY

    @property
    def rpt(self):
        return self.__rpt
    @rpt.setter
    def rpt(self, rpt: genmymodelreverse_javax_swing_JLabel):
        self.__rpt = rpt

    @property
    def g(self):
        return self.__g
    @g.setter
    def g(self, g: genmymodelreverse_java_awt_Graphics):
        self.__g = g

    @property
    def p1(self):
        return self.__p1
    @p1.setter
    def p1(self, p1: genmymodelreverse_javax_swing_JRadioButton):
        self.__p1 = p1

    @property
    def yellowK(self):
        return self.__yellowK
    @yellowK.setter
    def yellowK(self, yellowK: genmymodelreverse_javax_swing_ImageIcon):
        self.__yellowK = yellowK

    @property
    def nwB(self):
        return self.__nwB
    @nwB.setter
    def nwB(self, nwB: genmymodelreverse_javax_swing_JButton):
        self.__nwB = nwB

    @property
    def difficulty(self):
        return self.__difficulty
    @difficulty.setter
    def difficulty(self, difficulty: int):
        self.__difficulty = difficulty

    @property
    def selectedColor(self):
        return self.__selectedColor
    @selectedColor.setter
    def selectedColor(self, selectedColor: str):
        self.__selectedColor = selectedColor

    @property
    def preBoard3(self):
        return self.__preBoard3
    @preBoard3.setter
    def preBoard3(self, preBoard3: str):
        self.__preBoard3 = preBoard3

    @property
    def unB(self):
        return self.__unB
    @unB.setter
    def unB(self, unB: genmymodelreverse_javax_swing_JButton):
        self.__unB = unB

    @property
    def bp(self):
        return self.__bp
    @bp.setter
    def bp(self, bp: genmymodelreverse_javax_swing_JLabel):
        self.__bp = bp

    @property
    def preToMove3(self):
        return self.__preToMove3
    @preToMove3.setter
    def preToMove3(self, preToMove3: int):
        self.__preToMove3 = preToMove3

    @property
    def loser(self):
        return self.__loser
    @loser.setter
    def loser(self, loser: int):
        self.__loser = loser

    @property
    def currType(self):
        return self.__currType
    @currType.setter
    def currType(self, currType: int):
        self.__currType = currType

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, level: genmymodelreverse_javax_swing_JComboBox):
        self.__level = level

    @property
    def incomplete(self):
        return self.__incomplete
    @incomplete.setter
    def incomplete(self, incomplete: bool):
        self.__incomplete = incomplete

    @property
    def preBoard2(self):
        return self.__preBoard2
    @preBoard2.setter
    def preBoard2(self, preBoard2: str):
        self.__preBoard2 = preBoard2

    @property
    def c2(self):
        return self.__c2
    @c2.setter
    def c2(self, c2: genmymodelreverse_javax_swing_JRadioButton):
        self.__c2 = c2

    @property
    def diff(self):
        return self.__diff
    @diff.setter
    def diff(self, diff: genmymodelreverse_javax_swing_JLabel):
        self.__diff = diff

    @property
    def p2(self):
        return self.__p2
    @p2.setter
    def p2(self, p2: genmymodelreverse_javax_swing_JRadioButton):
        self.__p2 = p2

    @property
    def snB(self):
        return self.__snB
    @snB.setter
    def snB(self, snB: genmymodelreverse_javax_swing_JButton):
        self.__snB = snB

    @property
    def snp(self):
        return self.__snp
    @snp.setter
    def snp(self, snp: genmymodelreverse_javax_swing_ImageIcon):
        self.__snp = snp

    @property
    def preBoard1(self):
        return self.__preBoard1
    @preBoard1.setter
    def preBoard1(self, preBoard1: str):
        self.__preBoard1 = preBoard1

    @property
    def msg(self):
        return self.__msg
    @msg.setter
    def msg(self, msg: genmymodelreverse_javax_swing_JTextArea):
        self.__msg = msg

    @property
    def bk(self):
        return self.__bk
    @bk.setter
    def bk(self, bk: genmymodelreverse_javax_swing_JLabel):
        self.__bk = bk

    @property
    def won(self):
        return self.__won
    @won.setter
    def won(self, won: int):
        self.__won = won

    @property
    def mode(self):
        return self.__mode
    @mode.setter
    def mode(self, mode: genmymodelreverse_javax_swing_JLabel):
        self.__mode = mode

    @property
    def redKing(self):
        return self.__redKing
    @redKing.setter
    def redKing(self, redKing: int):
        self.__redKing = redKing

    @property
    def empty(self):
        return self.__empty
    @empty.setter
    def empty(self, empty: int):
        self.__empty = empty

    @property
    def yellowNormal(self):
        return self.__yellowNormal
    @yellowNormal.setter
    def yellowNormal(self, yellowNormal: int):
        self.__yellowNormal = yellowNormal

    @property
    def hlpB(self):
        return self.__hlpB
    @hlpB.setter
    def hlpB(self, hlpB: genmymodelreverse_javax_swing_JButton):
        self.__hlpB = hlpB

    @property
    def c1(self):
        return self.__c1
    @c1.setter
    def c1(self, c1: genmymodelreverse_javax_swing_JRadioButton):
        self.__c1 = c1

    @property
    def redK(self):
        return self.__redK
    @redK.setter
    def redK(self, redK: genmymodelreverse_javax_swing_ImageIcon):
        self.__redK = redK

    @property
    def toMove(self):
        return self.__toMove
    @toMove.setter
    def toMove(self, toMove: int):
        self.__toMove = toMove

    @property
    def selectedMode(self):
        return self.__selectedMode
    @selectedMode.setter
    def selectedMode(self, selectedMode: int):
        self.__selectedMode = selectedMode

    @property
    def highlight(self):
        return self.__highlight
    @highlight.setter
    def highlight(self, highlight: bool):
        self.__highlight = highlight

    @property
    def winPoint(self):
        return self.__winPoint
    @winPoint.setter
    def winPoint(self, winPoint: genmymodelreverse_java_awt_Point):
        self.__winPoint = winPoint

    @property
    def movable(self):
        return self.__movable
    @movable.setter
    def movable(self, movable: bool):
        self.__movable = movable

    @property
    def preToMove2(self):
        return self.__preToMove2
    @preToMove2.setter
    def preToMove2(self, preToMove2: int):
        self.__preToMove2 = preToMove2

    @property
    def redN(self):
        return self.__redN
    @redN.setter
    def redN(self, redN: genmymodelreverse_javax_swing_ImageIcon):
        self.__redN = redN

    @property
    def undoCount(self):
        return self.__undoCount
    @undoCount.setter
    def undoCount(self, undoCount: int):
        self.__undoCount = undoCount

    @property
    def rp(self):
        return self.__rp
    @rp.setter
    def rp(self, rp: genmymodelreverse_javax_swing_JLabel):
        self.__rp = rp

    @property
    def yellowKing(self):
        return self.__yellowKing
    @yellowKing.setter
    def yellowKing(self, yellowKing: int):
        self.__yellowKing = yellowKing

    @property
    def yellowN(self):
        return self.__yellowN
    @yellowN.setter
    def yellowN(self, yellowN: genmymodelreverse_javax_swing_ImageIcon):
        self.__yellowN = yellowN

    @property
    def bpt(self):
        return self.__bpt
    @bpt.setter
    def bpt(self, bpt: genmymodelreverse_javax_swing_JLabel):
        self.__bpt = bpt

    @property
    def hp1(self):
        return self.__hp1
    @hp1.setter
    def hp1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_checkers_Checkers__hp1", None)
        self.__hp1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checkers0"):
                opp_val = getattr(old_value, "checkers0", None)
                if opp_val == self:
                    setattr(old_value, "checkers0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checkers0"):
                opp_val = getattr(value, "checkers0", None)
                setattr(value, "checkers0", self)



class checkers_CheckerMove:

    def __init__(self, legalMove: int, illegalMove: int, incompleteMove: int):
        self.legalMove = legalMove
        self.illegalMove = illegalMove
        self.incompleteMove = incompleteMove
        
        pass
    @property
    def incompleteMove(self):
        return self.__incompleteMove
    @incompleteMove.setter
    def incompleteMove(self, incompleteMove: int):
        self.__incompleteMove = incompleteMove

    @property
    def illegalMove(self):
        return self.__illegalMove
    @illegalMove.setter
    def illegalMove(self, illegalMove: int):
        self.__illegalMove = illegalMove

    @property
    def legalMove(self):
        return self.__legalMove
    @legalMove.setter
    def legalMove(self, legalMove: int):
        self.__legalMove = legalMove

