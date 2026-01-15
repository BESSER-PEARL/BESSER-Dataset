from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class JumpStmt:

    pass
class flowgraph_Continue(JumpStmt):

    pass
class flowgraph_Break(JumpStmt):

    pass
class Var:

    pass
class flowgraph_Param(Var):

    pass
class Block:

    pass
class flowgraph_Item(ABC):

    def __init__(self, txt: str):
        self.txt = txt
        
    @property
    def txt(self) -> str:
        return self.__txt

    @txt.setter
    def txt(self, txt: str):
        self.__txt = txt

class Conditional:

    pass
class flowgraph_Loop(Conditional):

    pass
class flowgraph_If(Conditional):

    pass
class FlowInstr:

    pass
class flowgraph_Method(FlowInstr, Block):

    pass
class flowgraph_Expr(FlowInstr):

    pass
class flowgraph_Exit(FlowInstr):

    pass
class Stmt:

    pass
class flowgraph_Block(Stmt):

    pass
class flowgraph_Return(FlowInstr, Stmt):

    pass
class flowgraph_JumpStmt(FlowInstr, Stmt):

    pass
class flowgraph_Conditional(Stmt):

    pass
class flowgraph_Label(Stmt):

    pass
class flowgraph_SimpleStmt(FlowInstr, Stmt):

    pass
class Item:

    pass
class flowgraph_FlowInstr(Item):

    pass
class flowgraph_Var(Item):

    pass
class flowgraph_Stmt(Item):

    pass