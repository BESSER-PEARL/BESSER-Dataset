from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Orientation(Enum):
    undefined = "undefined"
    PtoT = "PtoT"
    TtoP = "TtoP"
    Inhibitor = "Inhibitor"
class Colour16(Enum):
    Aqua = "Aqua"
    Black = "Black"
    Blue = "Blue"
    Fuchsia = "Fuchsia"
    Gray = "Gray"
    Green = "Green"
    Lime = "Lime"
    Maroon = "Maroon"
    Navy = "Navy"
    Olive = "Olive"
    Purple = "Purple"
    Red = "Red"
    Silver = "Silver"
    Teal = "Teal"
    White = "White"
    Yellow = "Yellow"


############################################
# Definition of Classes
############################################

class CompoundColorSet:

    pass
class cpntools_List(CompoundColorSet):

    pass
class cpntools_Union(CompoundColorSet):

    pass
class cpntools_Alias(CompoundColorSet):

    pass
class cpntools_Record(CompoundColorSet):

    pass
class cpntools_Subset(CompoundColorSet):

    pass
class cpntools_Product(CompoundColorSet):

    pass
class SimpleColorSet:

    pass
class cpntools_Index(SimpleColorSet):

    def __init__(self, with: str):
        self.with = with
        
    @property
    def with(self) -> str:
        return self.__with

    @with.setter
    def with(self, with: str):
        self.__with = with

class cpntools_Enumerated(SimpleColorSet):

    def __init__(self, with: str):
        self.with = with
        
    @property
    def with(self) -> str:
        return self.__with

    @with.setter
    def with(self, with: str):
        self.__with = with

class cpntools_Unit(SimpleColorSet):

    def __init__(self, with: str):
        self.with = with
        
    @property
    def with(self) -> str:
        return self.__with

    @with.setter
    def with(self, with: str):
        self.__with = with

class ColorSet:

    pass
class cpntools_CompoundColorSet(ColorSet):

    pass
class cpntools_SimpleColorSet(ColorSet):

    pass
class cpntools_String(SimpleColorSet):

    def __init__(self, with: str, and: str):
        self.with = with
        self.and = and
        
    @property
    def with(self) -> str:
        return self.__with

    @with.setter
    def with(self, with: str):
        self.__with = with

    @property
    def and(self) -> str:
        return self.__and

    @and.setter
    def and(self, and: str):
        self.__and = and

class cpntools_Time(SimpleColorSet):

    pass
class cpntools_Real(SimpleColorSet):

    def __init__(self, with: str):
        self.with = with
        
    @property
    def with(self) -> str:
        return self.__with

    @with.setter
    def with(self, with: str):
        self.__with = with

class cpntools_LargeInteger(SimpleColorSet):

    def __init__(self, with: str):
        self.with = with
        
    @property
    def with(self) -> str:
        return self.__with

    @with.setter
    def with(self, with: str):
        self.__with = with

class cpntools_Integer(SimpleColorSet):

    def __init__(self, with: str):
        self.with = with
        
    @property
    def with(self) -> str:
        return self.__with

    @with.setter
    def with(self, with: str):
        self.__with = with

class cpntools_Boolean(SimpleColorSet):

    def __init__(self, with: str):
        self.with = with
        
    @property
    def with(self) -> str:
        return self.__with

    @with.setter
    def with(self, with: str):
        self.__with = with

class Auxiliary:

    pass
class cpntools_AuxEllipse(Auxiliary):

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

class cpntools_AuxBox(Auxiliary):

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

class cpntools_AuxText(Auxiliary):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class cpntools_Declaration(ABC):

    pass
class DiagramElement:

    pass
class cpntools_Annot(DiagramElement):

    def __init__(self, text: str, cpntools_Annot: "cpntools_Arc" = None):
        self.text = text
        self.cpntools_Annot = cpntools_Annot
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def cpntools_Annot(self):
        return self.__cpntools_Annot

    @cpntools_Annot.setter
    def cpntools_Annot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Annot__cpntools_Annot", None)
        self.__cpntools_Annot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Arc"):
                opp_val = getattr(old_value, "cpntools_Arc", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Arc"):
                opp_val = getattr(value, "cpntools_Arc", None)
                setattr(value, "cpntools_Arc", self)

class cpntools_TransTime(DiagramElement):

    def __init__(self, text: str, cpntools_TransTime: "cpntools_Trans" = None):
        self.text = text
        self.cpntools_TransTime = cpntools_TransTime
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def cpntools_TransTime(self):
        return self.__cpntools_TransTime

    @cpntools_TransTime.setter
    def cpntools_TransTime(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_TransTime__cpntools_TransTime", None)
        self.__cpntools_TransTime = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Trans67"):
                opp_val = getattr(old_value, "cpntools_Trans67", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Trans67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Trans67"):
                opp_val = getattr(value, "cpntools_Trans67", None)
                setattr(value, "cpntools_Trans67", self)

class cpntools_TransCond(DiagramElement):

    def __init__(self, text: str, cpntools_TransCond: "cpntools_Trans" = None):
        self.text = text
        self.cpntools_TransCond = cpntools_TransCond
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def cpntools_TransCond(self):
        return self.__cpntools_TransCond

    @cpntools_TransCond.setter
    def cpntools_TransCond(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_TransCond__cpntools_TransCond", None)
        self.__cpntools_TransCond = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Trans"):
                opp_val = getattr(old_value, "cpntools_Trans", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Trans", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Trans"):
                opp_val = getattr(value, "cpntools_Trans", None)
                setattr(value, "cpntools_Trans", self)

class cpntools_TransPriority(DiagramElement):

    def __init__(self, text: str, cpntools_TransPriority: "cpntools_Trans" = None):
        self.text = text
        self.cpntools_TransPriority = cpntools_TransPriority
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def cpntools_TransPriority(self):
        return self.__cpntools_TransPriority

    @cpntools_TransPriority.setter
    def cpntools_TransPriority(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_TransPriority__cpntools_TransPriority", None)
        self.__cpntools_TransPriority = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Trans65"):
                opp_val = getattr(old_value, "cpntools_Trans65", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Trans65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Trans65"):
                opp_val = getattr(value, "cpntools_Trans65", None)
                setattr(value, "cpntools_Trans65", self)

class cpntools_DiagramElement(ABC):

    def __init__(self, lineColour: str, fillFilled: bool, lineThick: int, posx: int, lineType: str, posy: int, fillColour: str, fillPattern: str, DiagramElement: "cpntools_Group" = None, groupElms: "cpntools_Group" = None):
        self.lineColour = lineColour
        self.fillFilled = fillFilled
        self.lineThick = lineThick
        self.posx = posx
        self.lineType = lineType
        self.posy = posy
        self.fillColour = fillColour
        self.fillPattern = fillPattern
        self.DiagramElement = DiagramElement
        self.groupElms = groupElms
        
    @property
    def fillColour(self) -> str:
        return self.__fillColour

    @fillColour.setter
    def fillColour(self, fillColour: str):
        self.__fillColour = fillColour

    @property
    def posx(self) -> int:
        return self.__posx

    @posx.setter
    def posx(self, posx: int):
        self.__posx = posx

    @property
    def fillPattern(self) -> str:
        return self.__fillPattern

    @fillPattern.setter
    def fillPattern(self, fillPattern: str):
        self.__fillPattern = fillPattern

    @property
    def lineType(self) -> str:
        return self.__lineType

    @lineType.setter
    def lineType(self, lineType: str):
        self.__lineType = lineType

    @property
    def lineThick(self) -> int:
        return self.__lineThick

    @lineThick.setter
    def lineThick(self, lineThick: int):
        self.__lineThick = lineThick

    @property
    def lineColour(self) -> str:
        return self.__lineColour

    @lineColour.setter
    def lineColour(self, lineColour: str):
        self.__lineColour = lineColour

    @property
    def posy(self) -> int:
        return self.__posy

    @posy.setter
    def posy(self, posy: int):
        self.__posy = posy

    @property
    def fillFilled(self) -> bool:
        return self.__fillFilled

    @fillFilled.setter
    def fillFilled(self, fillFilled: bool):
        self.__fillFilled = fillFilled

    @property
    def groupElms(self):
        return self.__groupElms

    @groupElms.setter
    def groupElms(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_DiagramElement__groupElms", None)
        self.__groupElms = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Group20"):
                opp_val = getattr(old_value, "Group20", None)
                if opp_val == self:
                    setattr(old_value, "Group20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Group20"):
                opp_val = getattr(value, "Group20", None)
                setattr(value, "Group20", self)

    @property
    def DiagramElement(self):
        return self.__DiagramElement

    @DiagramElement.setter
    def DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_DiagramElement__DiagramElement", None)
        self.__DiagramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group"):
                opp_val = getattr(old_value, "group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group"):
                opp_val = getattr(value, "group", None)
                if opp_val is None:
                    setattr(value, "group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cpntools_Arc(DiagramElement):

    def __init__(self, headsize: float, orientation: str, currentcyckle: str, order: int, Arc32: "cpntools_Place" = None, Arc: "cpntools_Page" = None, arcs: "cpntools_Place" = None, arcs53: "cpntools_Trans" = None, cpntools_Arc: "cpntools_Annot" = None, arcs57: "cpntools_Page" = None, Arc63: "cpntools_Trans" = None):
        self.headsize = headsize
        self.orientation = orientation
        self.currentcyckle = currentcyckle
        self.order = order
        self.Arc32 = Arc32
        self.Arc = Arc
        self.arcs = arcs
        self.arcs53 = arcs53
        self.cpntools_Arc = cpntools_Arc
        self.arcs57 = arcs57
        self.Arc63 = Arc63
        
    @property
    def order(self) -> int:
        return self.__order

    @order.setter
    def order(self, order: int):
        self.__order = order

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def currentcyckle(self) -> str:
        return self.__currentcyckle

    @currentcyckle.setter
    def currentcyckle(self, currentcyckle: str):
        self.__currentcyckle = currentcyckle

    @property
    def headsize(self) -> float:
        return self.__headsize

    @headsize.setter
    def headsize(self, headsize: float):
        self.__headsize = headsize

    @property
    def arcs57(self):
        return self.__arcs57

    @arcs57.setter
    def arcs57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Arc__arcs57", None)
        self.__arcs57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page58"):
                opp_val = getattr(old_value, "Page58", None)
                if opp_val == self:
                    setattr(old_value, "Page58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page58"):
                opp_val = getattr(value, "Page58", None)
                setattr(value, "Page58", self)

    @property
    def arcs(self):
        return self.__arcs

    @arcs.setter
    def arcs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Arc__arcs", None)
        self.__arcs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Place51"):
                opp_val = getattr(old_value, "Place51", None)
                if opp_val == self:
                    setattr(old_value, "Place51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Place51"):
                opp_val = getattr(value, "Place51", None)
                setattr(value, "Place51", self)

    @property
    def Arc63(self):
        return self.__Arc63

    @Arc63.setter
    def Arc63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Arc__Arc63", None)
        self.__Arc63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trans"):
                opp_val = getattr(old_value, "trans", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trans"):
                opp_val = getattr(value, "trans", None)
                if opp_val is None:
                    setattr(value, "trans", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arc(self):
        return self.__Arc

    @Arc.setter
    def Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Arc__Arc", None)
        self.__Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page13"):
                opp_val = getattr(old_value, "page13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page13"):
                opp_val = getattr(value, "page13", None)
                if opp_val is None:
                    setattr(value, "page13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cpntools_Arc(self):
        return self.__cpntools_Arc

    @cpntools_Arc.setter
    def cpntools_Arc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Arc__cpntools_Arc", None)
        self.__cpntools_Arc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Annot"):
                opp_val = getattr(old_value, "cpntools_Annot", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Annot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Annot"):
                opp_val = getattr(value, "cpntools_Annot", None)
                setattr(value, "cpntools_Annot", self)

    @property
    def arcs53(self):
        return self.__arcs53

    @arcs53.setter
    def arcs53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Arc__arcs53", None)
        self.__arcs53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Trans54"):
                opp_val = getattr(old_value, "Trans54", None)
                if opp_val == self:
                    setattr(old_value, "Trans54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Trans54"):
                opp_val = getattr(value, "Trans54", None)
                setattr(value, "Trans54", self)

    @property
    def Arc32(self):
        return self.__Arc32

    @Arc32.setter
    def Arc32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Arc__Arc32", None)
        self.__Arc32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "place"):
                opp_val = getattr(old_value, "place", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "place"):
                opp_val = getattr(value, "place", None)
                if opp_val is None:
                    setattr(value, "place", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Declaration:

    pass
class cpntools_Ml(Declaration):

    def __init__(self, expression: str):
        self.expression = expression
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

class cpntools_Block(Declaration):

    def __init__(self, idname: str, Block: "cpntools_Declaration" = None, block: set["cpntools_Declaration"] = None):
        self.idname = idname
        self.Block = Block
        self.block = block if block is not None else set()
        
    @property
    def idname(self) -> str:
        return self.__idname

    @idname.setter
    def idname(self, idname: str):
        self.__idname = idname

    @property
    def Block(self):
        return self.__Block

    @Block.setter
    def Block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Block__Block", None)
        self.__Block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declarations36"):
                opp_val = getattr(old_value, "declarations36", None)
                if opp_val == self:
                    setattr(old_value, "declarations36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declarations36"):
                opp_val = getattr(value, "declarations36", None)
                setattr(value, "declarations36", self)

    @property
    def block(self):
        return self.__block

    @block.setter
    def block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Block__block", None)
        self.__block = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Declaration49"):
                    opp_val = getattr(item, "Declaration49", None)
                    
                    if opp_val == self:
                        setattr(item, "Declaration49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Declaration49"):
                    opp_val = getattr(item, "Declaration49", None)
                    
                    setattr(item, "Declaration49", self)
                    

class cpntools_Var(Declaration):

    def __init__(self, idname: str, cpntools_Var: "cpntools_ColorSet" = None):
        self.idname = idname
        self.cpntools_Var = cpntools_Var
        
    @property
    def idname(self) -> str:
        return self.__idname

    @idname.setter
    def idname(self, idname: str):
        self.__idname = idname

    @property
    def cpntools_Var(self):
        return self.__cpntools_Var

    @cpntools_Var.setter
    def cpntools_Var(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Var__cpntools_Var", None)
        self.__cpntools_Var = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_ColorSet47"):
                opp_val = getattr(old_value, "cpntools_ColorSet47", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_ColorSet47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_ColorSet47"):
                opp_val = getattr(value, "cpntools_ColorSet47", None)
                setattr(value, "cpntools_ColorSet47", self)

class cpntools_Globref(Declaration):

    def __init__(self, idname: str):
        self.idname = idname
        
    @property
    def idname(self) -> str:
        return self.__idname

    @idname.setter
    def idname(self, idname: str):
        self.__idname = idname

class cpntools_Trans(DiagramElement):

    def __init__(self, height: int, width: int, explicit: bool, text: str, Trans: "cpntools_Page" = None, Trans54: "cpntools_Arc" = None, trans: set["cpntools_Arc"] = None, cpntools_Trans65: "cpntools_TransPriority" = None, cpntools_Trans67: "cpntools_TransTime" = None, cpntools_Trans: "cpntools_TransCond" = None, transs: "cpntools_Page" = None):
        self.height = height
        self.width = width
        self.explicit = explicit
        self.text = text
        self.Trans = Trans
        self.Trans54 = Trans54
        self.trans = trans if trans is not None else set()
        self.cpntools_Trans65 = cpntools_Trans65
        self.cpntools_Trans67 = cpntools_Trans67
        self.cpntools_Trans = cpntools_Trans
        self.transs = transs
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def explicit(self) -> bool:
        return self.__explicit

    @explicit.setter
    def explicit(self, explicit: bool):
        self.__explicit = explicit

    @property
    def cpntools_Trans(self):
        return self.__cpntools_Trans

    @cpntools_Trans.setter
    def cpntools_Trans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Trans__cpntools_Trans", None)
        self.__cpntools_Trans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_TransCond"):
                opp_val = getattr(old_value, "cpntools_TransCond", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_TransCond", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_TransCond"):
                opp_val = getattr(value, "cpntools_TransCond", None)
                setattr(value, "cpntools_TransCond", self)

    @property
    def Trans(self):
        return self.__Trans

    @Trans.setter
    def Trans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Trans__Trans", None)
        self.__Trans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page11"):
                opp_val = getattr(old_value, "page11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page11"):
                opp_val = getattr(value, "page11", None)
                if opp_val is None:
                    setattr(value, "page11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cpntools_Trans67(self):
        return self.__cpntools_Trans67

    @cpntools_Trans67.setter
    def cpntools_Trans67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Trans__cpntools_Trans67", None)
        self.__cpntools_Trans67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_TransTime"):
                opp_val = getattr(old_value, "cpntools_TransTime", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_TransTime", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_TransTime"):
                opp_val = getattr(value, "cpntools_TransTime", None)
                setattr(value, "cpntools_TransTime", self)

    @property
    def transs(self):
        return self.__transs

    @transs.setter
    def transs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Trans__transs", None)
        self.__transs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page61"):
                opp_val = getattr(old_value, "Page61", None)
                if opp_val == self:
                    setattr(old_value, "Page61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page61"):
                opp_val = getattr(value, "Page61", None)
                setattr(value, "Page61", self)

    @property
    def trans(self):
        return self.__trans

    @trans.setter
    def trans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Trans__trans", None)
        self.__trans = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc63"):
                    opp_val = getattr(item, "Arc63", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc63"):
                    opp_val = getattr(item, "Arc63", None)
                    
                    setattr(item, "Arc63", self)
                    

    @property
    def Trans54(self):
        return self.__Trans54

    @Trans54.setter
    def Trans54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Trans__Trans54", None)
        self.__Trans54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arcs53"):
                opp_val = getattr(old_value, "arcs53", None)
                if opp_val == self:
                    setattr(old_value, "arcs53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arcs53"):
                opp_val = getattr(value, "arcs53", None)
                setattr(value, "arcs53", self)

    @property
    def cpntools_Trans65(self):
        return self.__cpntools_Trans65

    @cpntools_Trans65.setter
    def cpntools_Trans65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Trans__cpntools_Trans65", None)
        self.__cpntools_Trans65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_TransPriority"):
                opp_val = getattr(old_value, "cpntools_TransPriority", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_TransPriority", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_TransPriority"):
                opp_val = getattr(value, "cpntools_TransPriority", None)
                setattr(value, "cpntools_TransPriority", self)

class cpntools_Port(DiagramElement):

    def __init__(self, portType: str, cpntools_Port: "cpntools_Place" = None):
        self.portType = portType
        self.cpntools_Port = cpntools_Port
        
    @property
    def portType(self) -> str:
        return self.__portType

    @portType.setter
    def portType(self, portType: str):
        self.__portType = portType

    @property
    def cpntools_Port(self):
        return self.__cpntools_Port

    @cpntools_Port.setter
    def cpntools_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Port__cpntools_Port", None)
        self.__cpntools_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Place25"):
                opp_val = getattr(old_value, "cpntools_Place25", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Place25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Place25"):
                opp_val = getattr(value, "cpntools_Place25", None)
                setattr(value, "cpntools_Place25", self)

class cpntools_Initmark(DiagramElement):

    def __init__(self, expression: str, cpntools_Initmark: "cpntools_Place" = None):
        self.expression = expression
        self.cpntools_Initmark = cpntools_Initmark
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def cpntools_Initmark(self):
        return self.__cpntools_Initmark

    @cpntools_Initmark.setter
    def cpntools_Initmark(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Initmark__cpntools_Initmark", None)
        self.__cpntools_Initmark = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Place23"):
                opp_val = getattr(old_value, "cpntools_Place23", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Place23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Place23"):
                opp_val = getattr(value, "cpntools_Place23", None)
                setattr(value, "cpntools_Place23", self)

class cpntools_ColorSet(Declaration):

    def __init__(self, idname: str, colorSetType: str, timed: bool, declare: str, cpntools_ColorSet: "cpntools_Place" = None, cpntools_ColorSet47: "cpntools_Var" = None):
        self.idname = idname
        self.colorSetType = colorSetType
        self.timed = timed
        self.declare = declare
        self.cpntools_ColorSet = cpntools_ColorSet
        self.cpntools_ColorSet47 = cpntools_ColorSet47
        
    @property
    def colorSetType(self) -> str:
        return self.__colorSetType

    @colorSetType.setter
    def colorSetType(self, colorSetType: str):
        self.__colorSetType = colorSetType

    @property
    def declare(self) -> str:
        return self.__declare

    @declare.setter
    def declare(self, declare: str):
        self.__declare = declare

    @property
    def timed(self) -> bool:
        return self.__timed

    @timed.setter
    def timed(self, timed: bool):
        self.__timed = timed

    @property
    def idname(self) -> str:
        return self.__idname

    @idname.setter
    def idname(self, idname: str):
        self.__idname = idname

    @property
    def cpntools_ColorSet(self):
        return self.__cpntools_ColorSet

    @cpntools_ColorSet.setter
    def cpntools_ColorSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_ColorSet__cpntools_ColorSet", None)
        self.__cpntools_ColorSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Place"):
                opp_val = getattr(old_value, "cpntools_Place", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Place"):
                opp_val = getattr(value, "cpntools_Place", None)
                setattr(value, "cpntools_Place", self)

    @property
    def cpntools_ColorSet47(self):
        return self.__cpntools_ColorSet47

    @cpntools_ColorSet47.setter
    def cpntools_ColorSet47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_ColorSet__cpntools_ColorSet47", None)
        self.__cpntools_ColorSet47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Var"):
                opp_val = getattr(old_value, "cpntools_Var", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Var", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Var"):
                opp_val = getattr(value, "cpntools_Var", None)
                setattr(value, "cpntools_Var", self)

class cpntools_Binder:

    def __init__(self, posy: int, posx: int, width: int, height: int, Binder: "cpntools_Cpnet" = None, Binder15: "cpntools_Page" = None, binder: "cpntools_Cpnet" = None, binder72: set["cpntools_Page"] = None):
        self.posy = posy
        self.posx = posx
        self.width = width
        self.height = height
        self.Binder = Binder
        self.Binder15 = Binder15
        self.binder = binder
        self.binder72 = binder72 if binder72 is not None else set()
        
    @property
    def posy(self) -> int:
        return self.__posy

    @posy.setter
    def posy(self, posy: int):
        self.__posy = posy

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def posx(self) -> int:
        return self.__posx

    @posx.setter
    def posx(self, posx: int):
        self.__posx = posx

    @property
    def binder72(self):
        return self.__binder72

    @binder72.setter
    def binder72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Binder__binder72", None)
        self.__binder72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Page73"):
                    opp_val = getattr(item, "Page73", None)
                    
                    if opp_val == self:
                        setattr(item, "Page73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Page73"):
                    opp_val = getattr(item, "Page73", None)
                    
                    setattr(item, "Page73", self)
                    

    @property
    def Binder15(self):
        return self.__Binder15

    @Binder15.setter
    def Binder15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Binder__Binder15", None)
        self.__Binder15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pages"):
                opp_val = getattr(old_value, "pages", None)
                if opp_val == self:
                    setattr(old_value, "pages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pages"):
                opp_val = getattr(value, "pages", None)
                setattr(value, "pages", self)

    @property
    def Binder(self):
        return self.__Binder

    @Binder.setter
    def Binder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Binder__Binder", None)
        self.__Binder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpnet4"):
                opp_val = getattr(old_value, "cpnet4", None)
                if opp_val == self:
                    setattr(old_value, "cpnet4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpnet4"):
                opp_val = getattr(value, "cpnet4", None)
                setattr(value, "cpnet4", self)

    @property
    def binder(self):
        return self.__binder

    @binder.setter
    def binder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Binder__binder", None)
        self.__binder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cpnet70"):
                opp_val = getattr(old_value, "Cpnet70", None)
                if opp_val == self:
                    setattr(old_value, "Cpnet70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cpnet70"):
                opp_val = getattr(value, "Cpnet70", None)
                setattr(value, "Cpnet70", self)

class cpntools_Globbox:

    def __init__(self, name: str, Globbox: "cpntools_Cpnet" = None, globbox: "cpntools_Cpnet" = None, globbox45: set["cpntools_Declaration"] = None, Globbox34: "cpntools_Declaration" = None):
        self.name = name
        self.Globbox = Globbox
        self.globbox = globbox
        self.globbox45 = globbox45 if globbox45 is not None else set()
        self.Globbox34 = Globbox34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Globbox34(self):
        return self.__Globbox34

    @Globbox34.setter
    def Globbox34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Globbox__Globbox34", None)
        self.__Globbox34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declarations"):
                opp_val = getattr(old_value, "declarations", None)
                if opp_val == self:
                    setattr(old_value, "declarations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declarations"):
                opp_val = getattr(value, "declarations", None)
                setattr(value, "declarations", self)

    @property
    def Globbox(self):
        return self.__Globbox

    @Globbox.setter
    def Globbox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Globbox__Globbox", None)
        self.__Globbox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpnet2"):
                opp_val = getattr(old_value, "cpnet2", None)
                if opp_val == self:
                    setattr(old_value, "cpnet2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpnet2"):
                opp_val = getattr(value, "cpnet2", None)
                setattr(value, "cpnet2", self)

    @property
    def globbox45(self):
        return self.__globbox45

    @globbox45.setter
    def globbox45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Globbox__globbox45", None)
        self.__globbox45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Declaration"):
                    opp_val = getattr(item, "Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Declaration"):
                    opp_val = getattr(item, "Declaration", None)
                    
                    setattr(item, "Declaration", self)
                    

    @property
    def globbox(self):
        return self.__globbox

    @globbox.setter
    def globbox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Globbox__globbox", None)
        self.__globbox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cpnet43"):
                opp_val = getattr(old_value, "Cpnet43", None)
                if opp_val == self:
                    setattr(old_value, "Cpnet43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cpnet43"):
                opp_val = getattr(value, "Cpnet43", None)
                setattr(value, "Cpnet43", self)

class cpntools_Fusion:

    def __init__(self, name: str, Fusion: "cpntools_Cpnet" = None, Fusion27: "cpntools_Place" = None, fusion: set["cpntools_Place"] = None, fusions: "cpntools_Cpnet" = None):
        self.name = name
        self.Fusion = Fusion
        self.Fusion27 = Fusion27
        self.fusion = fusion if fusion is not None else set()
        self.fusions = fusions
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fusions(self):
        return self.__fusions

    @fusions.setter
    def fusions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Fusion__fusions", None)
        self.__fusions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Cpnet"):
                opp_val = getattr(old_value, "Cpnet", None)
                if opp_val == self:
                    setattr(old_value, "Cpnet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Cpnet"):
                opp_val = getattr(value, "Cpnet", None)
                setattr(value, "Cpnet", self)

    @property
    def Fusion27(self):
        return self.__Fusion27

    @Fusion27.setter
    def Fusion27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Fusion__Fusion27", None)
        self.__Fusion27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "places"):
                opp_val = getattr(old_value, "places", None)
                if opp_val == self:
                    setattr(old_value, "places", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "places"):
                opp_val = getattr(value, "places", None)
                setattr(value, "places", self)

    @property
    def fusion(self):
        return self.__fusion

    @fusion.setter
    def fusion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Fusion__fusion", None)
        self.__fusion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Place38"):
                    opp_val = getattr(item, "Place38", None)
                    
                    if opp_val == self:
                        setattr(item, "Place38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Place38"):
                    opp_val = getattr(item, "Place38", None)
                    
                    setattr(item, "Place38", self)
                    

    @property
    def Fusion(self):
        return self.__Fusion

    @Fusion.setter
    def Fusion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Fusion__Fusion", None)
        self.__Fusion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpnet"):
                opp_val = getattr(old_value, "cpnet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpnet"):
                opp_val = getattr(value, "cpnet", None)
                if opp_val is None:
                    setattr(value, "cpnet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cpntools_Cpnet:

    pass
class cpntools_Auxiliary(DiagramElement):

    pass
class cpntools_Place(DiagramElement):

    def __init__(self, width: int, text: str, height: int, Place: "cpntools_Page" = None, cpntools_Place: "cpntools_ColorSet" = None, cpntools_Place23: "cpntools_Initmark" = None, cpntools_Place25: "cpntools_Port" = None, places: "cpntools_Fusion" = None, places29: "cpntools_Page" = None, place: set["cpntools_Arc"] = None, Place38: "cpntools_Fusion" = None, Place51: "cpntools_Arc" = None):
        self.width = width
        self.text = text
        self.height = height
        self.Place = Place
        self.cpntools_Place = cpntools_Place
        self.cpntools_Place23 = cpntools_Place23
        self.cpntools_Place25 = cpntools_Place25
        self.places = places
        self.places29 = places29
        self.place = place if place is not None else set()
        self.Place38 = Place38
        self.Place51 = Place51
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def Place(self):
        return self.__Place

    @Place.setter
    def Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Place__Place", None)
        self.__Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page7"):
                opp_val = getattr(old_value, "page7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page7"):
                opp_val = getattr(value, "page7", None)
                if opp_val is None:
                    setattr(value, "page7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Place51(self):
        return self.__Place51

    @Place51.setter
    def Place51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Place__Place51", None)
        self.__Place51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arcs"):
                opp_val = getattr(old_value, "arcs", None)
                if opp_val == self:
                    setattr(old_value, "arcs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arcs"):
                opp_val = getattr(value, "arcs", None)
                setattr(value, "arcs", self)

    @property
    def Place38(self):
        return self.__Place38

    @Place38.setter
    def Place38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Place__Place38", None)
        self.__Place38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fusion"):
                opp_val = getattr(old_value, "fusion", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fusion"):
                opp_val = getattr(value, "fusion", None)
                if opp_val is None:
                    setattr(value, "fusion", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Place__place", None)
        self.__place = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc32"):
                    opp_val = getattr(item, "Arc32", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc32"):
                    opp_val = getattr(item, "Arc32", None)
                    
                    setattr(item, "Arc32", self)
                    

    @property
    def cpntools_Place23(self):
        return self.__cpntools_Place23

    @cpntools_Place23.setter
    def cpntools_Place23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Place__cpntools_Place23", None)
        self.__cpntools_Place23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Initmark"):
                opp_val = getattr(old_value, "cpntools_Initmark", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Initmark", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Initmark"):
                opp_val = getattr(value, "cpntools_Initmark", None)
                setattr(value, "cpntools_Initmark", self)

    @property
    def cpntools_Place(self):
        return self.__cpntools_Place

    @cpntools_Place.setter
    def cpntools_Place(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Place__cpntools_Place", None)
        self.__cpntools_Place = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_ColorSet"):
                opp_val = getattr(old_value, "cpntools_ColorSet", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_ColorSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_ColorSet"):
                opp_val = getattr(value, "cpntools_ColorSet", None)
                setattr(value, "cpntools_ColorSet", self)

    @property
    def cpntools_Place25(self):
        return self.__cpntools_Place25

    @cpntools_Place25.setter
    def cpntools_Place25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Place__cpntools_Place25", None)
        self.__cpntools_Place25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cpntools_Port"):
                opp_val = getattr(old_value, "cpntools_Port", None)
                if opp_val == self:
                    setattr(old_value, "cpntools_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cpntools_Port"):
                opp_val = getattr(value, "cpntools_Port", None)
                setattr(value, "cpntools_Port", self)

    @property
    def places29(self):
        return self.__places29

    @places29.setter
    def places29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Place__places29", None)
        self.__places29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page30"):
                opp_val = getattr(old_value, "Page30", None)
                if opp_val == self:
                    setattr(old_value, "Page30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page30"):
                opp_val = getattr(value, "Page30", None)
                setattr(value, "Page30", self)

    @property
    def places(self):
        return self.__places

    @places.setter
    def places(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Place__places", None)
        self.__places = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fusion27"):
                opp_val = getattr(old_value, "Fusion27", None)
                if opp_val == self:
                    setattr(old_value, "Fusion27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fusion27"):
                opp_val = getattr(value, "Fusion27", None)
                setattr(value, "Fusion27", self)

class cpntools_Group:

    def __init__(self, name: str, Group: "cpntools_Page" = None, group: set["cpntools_DiagramElement"] = None, group18: "cpntools_Page" = None, Group20: "cpntools_DiagramElement" = None):
        self.name = name
        self.Group = Group
        self.group = group if group is not None else set()
        self.group18 = group18
        self.Group20 = Group20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Group(self):
        return self.__Group

    @Group.setter
    def Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Group__Group", None)
        self.__Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page"):
                opp_val = getattr(old_value, "page", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page"):
                opp_val = getattr(value, "page", None)
                if opp_val is None:
                    setattr(value, "page", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Group__group", None)
        self.__group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElement"):
                    opp_val = getattr(item, "DiagramElement", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElement"):
                    opp_val = getattr(item, "DiagramElement", None)
                    
                    setattr(item, "DiagramElement", self)
                    

    @property
    def Group20(self):
        return self.__Group20

    @Group20.setter
    def Group20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Group__Group20", None)
        self.__Group20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groupElms"):
                opp_val = getattr(old_value, "groupElms", None)
                if opp_val == self:
                    setattr(old_value, "groupElms", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groupElms"):
                opp_val = getattr(value, "groupElms", None)
                setattr(value, "groupElms", self)

    @property
    def group18(self):
        return self.__group18

    @group18.setter
    def group18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Group__group18", None)
        self.__group18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page"):
                opp_val = getattr(old_value, "Page", None)
                if opp_val == self:
                    setattr(old_value, "Page", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page"):
                opp_val = getattr(value, "Page", None)
                setattr(value, "Page", self)

class cpntools_Page:

    def __init__(self, name: str, page: set["cpntools_Group"] = None, page7: set["cpntools_Place"] = None, page9: set["cpntools_Auxiliary"] = None, Page30: "cpntools_Place" = None, page11: set["cpntools_Trans"] = None, page13: set["cpntools_Arc"] = None, pages: "cpntools_Binder" = None, Page: "cpntools_Group" = None, Page41: "cpntools_Auxiliary" = None, Page58: "cpntools_Arc" = None, Page61: "cpntools_Trans" = None, Page73: "cpntools_Binder" = None):
        self.name = name
        self.page = page if page is not None else set()
        self.page7 = page7 if page7 is not None else set()
        self.page9 = page9 if page9 is not None else set()
        self.Page30 = Page30
        self.page11 = page11 if page11 is not None else set()
        self.page13 = page13 if page13 is not None else set()
        self.pages = pages
        self.Page = Page
        self.Page41 = Page41
        self.Page58 = Page58
        self.Page61 = Page61
        self.Page73 = Page73
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def page9(self):
        return self.__page9

    @page9.setter
    def page9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__page9", None)
        self.__page9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Auxiliary"):
                    opp_val = getattr(item, "Auxiliary", None)
                    
                    if opp_val == self:
                        setattr(item, "Auxiliary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Auxiliary"):
                    opp_val = getattr(item, "Auxiliary", None)
                    
                    setattr(item, "Auxiliary", self)
                    

    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__page", None)
        self.__page = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    if opp_val == self:
                        setattr(item, "Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    setattr(item, "Group", self)
                    

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__pages", None)
        self.__pages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Binder15"):
                opp_val = getattr(old_value, "Binder15", None)
                if opp_val == self:
                    setattr(old_value, "Binder15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Binder15"):
                opp_val = getattr(value, "Binder15", None)
                setattr(value, "Binder15", self)

    @property
    def Page61(self):
        return self.__Page61

    @Page61.setter
    def Page61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__Page61", None)
        self.__Page61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transs"):
                opp_val = getattr(old_value, "transs", None)
                if opp_val == self:
                    setattr(old_value, "transs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transs"):
                opp_val = getattr(value, "transs", None)
                setattr(value, "transs", self)

    @property
    def Page73(self):
        return self.__Page73

    @Page73.setter
    def Page73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__Page73", None)
        self.__Page73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "binder72"):
                opp_val = getattr(old_value, "binder72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "binder72"):
                opp_val = getattr(value, "binder72", None)
                if opp_val is None:
                    setattr(value, "binder72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def page13(self):
        return self.__page13

    @page13.setter
    def page13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__page13", None)
        self.__page13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    if opp_val == self:
                        setattr(item, "Arc", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arc"):
                    opp_val = getattr(item, "Arc", None)
                    
                    setattr(item, "Arc", self)
                    

    @property
    def Page30(self):
        return self.__Page30

    @Page30.setter
    def Page30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__Page30", None)
        self.__Page30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "places29"):
                opp_val = getattr(old_value, "places29", None)
                if opp_val == self:
                    setattr(old_value, "places29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "places29"):
                opp_val = getattr(value, "places29", None)
                setattr(value, "places29", self)

    @property
    def Page(self):
        return self.__Page

    @Page.setter
    def Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__Page", None)
        self.__Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group18"):
                opp_val = getattr(old_value, "group18", None)
                if opp_val == self:
                    setattr(old_value, "group18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group18"):
                opp_val = getattr(value, "group18", None)
                setattr(value, "group18", self)

    @property
    def Page58(self):
        return self.__Page58

    @Page58.setter
    def Page58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__Page58", None)
        self.__Page58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arcs57"):
                opp_val = getattr(old_value, "arcs57", None)
                if opp_val == self:
                    setattr(old_value, "arcs57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arcs57"):
                opp_val = getattr(value, "arcs57", None)
                setattr(value, "arcs57", self)

    @property
    def Page41(self):
        return self.__Page41

    @Page41.setter
    def Page41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__Page41", None)
        self.__Page41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auxiliarys"):
                opp_val = getattr(old_value, "auxiliarys", None)
                if opp_val == self:
                    setattr(old_value, "auxiliarys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auxiliarys"):
                opp_val = getattr(value, "auxiliarys", None)
                setattr(value, "auxiliarys", self)

    @property
    def page7(self):
        return self.__page7

    @page7.setter
    def page7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__page7", None)
        self.__page7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Place"):
                    opp_val = getattr(item, "Place", None)
                    
                    if opp_val == self:
                        setattr(item, "Place", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Place"):
                    opp_val = getattr(item, "Place", None)
                    
                    setattr(item, "Place", self)
                    

    @property
    def page11(self):
        return self.__page11

    @page11.setter
    def page11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cpntools_Page__page11", None)
        self.__page11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trans"):
                    opp_val = getattr(item, "Trans", None)
                    
                    if opp_val == self:
                        setattr(item, "Trans", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trans"):
                    opp_val = getattr(item, "Trans", None)
                    
                    setattr(item, "Trans", self)
                    

    def layout(self):
        # TODO: Implement layout method
        pass

    def layout(self, width: str, height: str, steps: str):
        # TODO: Implement layout method
        pass
