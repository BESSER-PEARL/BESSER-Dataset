from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Var:

    pass
class flowgraph_Param(Var):

    pass
class Block:

    pass
class flowgraph_Item(ABC):

    def __init__(self, txt: str, line: int):
        self.txt = txt
        self.line = line
        
    @property
    def txt(self) -> str:
        return self.__txt

    @txt.setter
    def txt(self, txt: str):
        self.__txt = txt

    @property
    def line(self) -> int:
        return self.__line

    @line.setter
    def line(self, line: int):
        self.__line = line

class Conditional:

    pass
class flowgraph_Loop(Conditional):

    pass
class flowgraph_If(Conditional):

    pass
class FlowInstr:

    pass
class flowgraph_Method(Block, FlowInstr):

    pass
class flowgraph_Exit(FlowInstr):

    pass
class flowgraph_Expr(FlowInstr):

    pass
class Stmt:

    pass
class flowgraph_Return(FlowInstr, Stmt):

    pass
class flowgraph_Block(Stmt):

    pass
class flowgraph_SimpleStmt(FlowInstr, Stmt):

    def __init__(self, type: str, valiableAccess: str, functionAccess: str):
        self.type = type
        self.valiableAccess = valiableAccess
        self.functionAccess = functionAccess
        
    @property
    def valiableAccess(self) -> str:
        return self.__valiableAccess

    @valiableAccess.setter
    def valiableAccess(self, valiableAccess: str):
        self.__valiableAccess = valiableAccess

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def functionAccess(self) -> str:
        return self.__functionAccess

    @functionAccess.setter
    def functionAccess(self, functionAccess: str):
        self.__functionAccess = functionAccess

class Item:

    pass
class flowgraph_Var(Item):

    pass
class flowgraph_FlowInstr(Item):

    pass
class flowgraph_Stmt(Item):

    pass
class JumpStmt:

    pass
class flowgraph_Continue(JumpStmt):

    pass
class flowgraph_Break(JumpStmt):

    pass
class flowgraph_Label(Stmt):

    pass
class flowgraph_JumpStmt(FlowInstr, Stmt):

    pass
class flowgraph_Conditional(Stmt):

    pass