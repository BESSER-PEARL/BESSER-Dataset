from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EventName(Enum):
    beforecreatemodel = "beforecreatemodel"
    beforecreaterelationinstance = "beforecreaterelationinstance"
    beforedeleteinstance = "beforedeleteinstance"
    beforedeletemodel = "beforedeletemodel"
    beforediscardmodel = "beforediscardmodel"
    beforesavemodel = "beforesavemodel"
    createinstance = "createinstance"
    createmodel = "createmodel"
    createrelationinstance = "createrelationinstance"
    deleteinstance = "deleteinstance"
    deletemodel = "deletemodel"
    deleterelationinstance = "deleterelationinstance"
    discardinstance = "discardinstance"
    discardmodel = "discardmodel"
    openmodel = "openmodel"
    renameinstance = "renameinstance"
    savemodel = "savemodel"
    setattributevalue = "setattributevalue"
    aftercreatemodelingconnector = "aftercreatemodelingconnector"
    aftercreatemodelingnode = "aftercreatemodelingnode"
    aftereditattributevalue = "aftereditattributevalue"
    toolinitialized = "toolinitialized"
class Color(Enum):
    aliceblue = "aliceblue"
    antiquewhite = "antiquewhite"
    aqua = "aqua"
    aquamarine = "aquamarine"
    azure = "azure"
    beige = "beige"
    bisque = "bisque"
    black = "black"
    blanchedalmond = "blanchedalmond"
    blue = "blue"
    blueviolet = "blueviolet"
    brown = "brown"
    burlywood = "burlywood"
    cadetblue = "cadetblue"
    chartreuse = "chartreuse"
    chocolate = "chocolate"
    coral = "coral"
    cornflowerblue = "cornflowerblue"
    cornsilk = "cornsilk"
    crimson = "crimson"
    cyan = "cyan"
    darkblue = "darkblue"
    darkcyan = "darkcyan"
    darkgoldenrod = "darkgoldenrod"
    darkgray = "darkgray"
    darkgreen = "darkgreen"
    darkkhaki = "darkkhaki"
    darkmagenta = "darkmagenta"
    darkolivegreen = "darkolivegreen"
    darkorange = "darkorange"
    darkorchid = "darkorchid"
    darkred = "darkred"
    darksalmon = "darksalmon"
    darkseagreen = "darkseagreen"
    darkslateblue = "darkslateblue"
    darkslategray = "darkslategray"
    darkturquoise = "darkturquoise"
    darkviolet = "darkviolet"
    deeppink = "deeppink"
    gray = "gray"
    green = "green"
    greenyellow = "greenyellow"
    honeydew = "honeydew"
    hotpink = "hotpink"
    indianred = "indianred"
    indigo = "indigo"
    ivory = "ivory"
    khaki = "khaki"
    lavender = "lavender"
    lavenderblush = "lavenderblush"
    lawngreen = "lawngreen"
    lemonchiffon = "lemonchiffon"
    lightblue = "lightblue"
    lightcoral = "lightcoral"
    lightcyan = "lightcyan"
    lightgoldenrodyellow = "lightgoldenrodyellow"
    lightgreen = "lightgreen"
    lightgray = "lightgray"
    lightmagenta = "lightmagenta"
    lightpink = "lightpink"
    lightsalmon = "lightsalmon"
    lightseagreen = "lightseagreen"
    lightskyblue = "lightskyblue"
    lightslategray = "lightslategray"
    deepskyblue = "deepskyblue"
    dimgray = "dimgray"
    dodgerblue = "dodgerblue"
    firebrick = "firebrick"
    floralwhite = "floralwhite"
    forestgreen = "forestgreen"
    fuchsia = "fuchsia"
    gainsboro = "gainsboro"
    ghostwhite = "ghostwhite"
    gold = "gold"
    goldenrod = "goldenrod"
    linen = "linen"
    magenta = "magenta"
    maroon = "maroon"
    mediumaquamarine = "mediumaquamarine"
    mediumblue = "mediumblue"
    mediumorchid = "mediumorchid"
    mediumpurple = "mediumpurple"
    mediumseagreen = "mediumseagreen"
    mediumslateblue = "mediumslateblue"
    mediumspringgreen = "mediumspringgreen"
    mediumturquoise = "mediumturquoise"
    mediumvioletred = "mediumvioletred"
    midnightblue = "midnightblue"
    mintcream = "mintcream"
    mistyrose = "mistyrose"
    moccasin = "moccasin"
    navajowhite = "navajowhite"
    lightsteelblue = "lightsteelblue"
    lightyellow = "lightyellow"
    lime = "lime"
    limegreen = "limegreen"
    orange = "orange"
    orangered = "orangered"
    orchid = "orchid"
    palegoldenrod = "palegoldenrod"
    palegreen = "palegreen"
    paleturquoise = "paleturquoise"
    palevioletred = "palevioletred"
    papayawhip = "papayawhip"
    peachpuff = "peachpuff"
    peru = "peru"
    pink = "pink"
    plum = "plum"
    powderblue = "powderblue"
    purple = "purple"
    red = "red"
    rosybrown = "rosybrown"
    royalblue = "royalblue"
    navy = "navy"
    oldlace = "oldlace"
    olive = "olive"
    olivedrab = "olivedrab"
    seashell = "seashell"
    sienna = "sienna"
    silver = "silver"
    skyblue = "skyblue"
    slateblue = "slateblue"
    slategray = "slategray"
    snow = "snow"
    springgreen = "springgreen"
    steelblue = "steelblue"
    tan = "tan"
    teal = "teal"
    thistle = "thistle"
    tomato = "tomato"
    turquoise = "turquoise"
    violet = "violet"
    saddlebrown = "saddlebrown"
    salmon = "salmon"
    sandybrown = "sandybrown"
    seagreen = "seagreen"
    yellowgreen = "yellowgreen"
    wheat = "wheat"
    white = "white"
    whitesmoke = "whitesmoke"
    yellow = "yellow"
class AccessType(Enum):
    write = "write"
    read = "read"
    internal = "internal"
class AttrGetParams(Enum):
    type = "type"
    value = "value"
    name = "name"
class ButtonType(Enum):
    ok = "ok"
    okcancel = "okcancel"
    yesno = "yesno"
    yesnocancel = "yesnocancel"
    retrycancel = "retrycancel"
    defok = "defok"
    defcancel = "defcancel"
    defyes = "defyes"
    defno = "defno"
    defretry = "defretry"
class AttrSetParams(Enum):
    value = "value"
class SimpleType(Enum):
    String = "String"
    Int = "Int"
    Double = "Double"
class Font(Enum):
    arial = "arial"
    arialblack = "arialblack"
    comicsansms = "comicsansms"
    couriernew = "couriernew"
    georgia = "georgia"
    mssansserif = "mssansserif"
    msserif = "msserif"
    impact = "impact"
    lucidaconsole = "lucidaconsole"
    lucidasansunicode = "lucidasansunicode"
    palatinolinotype = "palatinolinotype"
    tahoma = "tahoma"
    timesnewroman = "timesnewroman"
    trebuchetms = "trebuchetms"
    verdana = "verdana"
    symbol = "symbol"
    webdings = "webdings"
    windings = "windings"


############################################
# Definition of Classes
############################################

class Expression:

    pass
class mMDSL_MultiplicationExpression(Expression):

    pass
class mMDSL_AdditionExpression(Expression):

    pass
class mMDSL_AndExpression(Expression):

    pass
class mMDSL_EqualExpression(Expression):

    pass
class mMDSL_CompareExpression(Expression):

    pass
class mMDSL_OrExpression(Expression):

    pass
class mMDSL_AttributeSet:

    def __init__(self, attrsetparams: str, valueString: str, valueRealNumber: str, mMDSL_AttributeSet: "mMDSL_AttributeOperation" = None, mMDSL_AttributeSet481: "mMDSL_Variable" = None):
        self.attrsetparams = attrsetparams
        self.valueString = valueString
        self.valueRealNumber = valueRealNumber
        self.mMDSL_AttributeSet = mMDSL_AttributeSet
        self.mMDSL_AttributeSet481 = mMDSL_AttributeSet481
        
    @property
    def attrsetparams(self) -> str:
        return self.__attrsetparams

    @attrsetparams.setter
    def attrsetparams(self, attrsetparams: str):
        self.__attrsetparams = attrsetparams

    @property
    def valueString(self) -> str:
        return self.__valueString

    @valueString.setter
    def valueString(self, valueString: str):
        self.__valueString = valueString

    @property
    def valueRealNumber(self) -> str:
        return self.__valueRealNumber

    @valueRealNumber.setter
    def valueRealNumber(self, valueRealNumber: str):
        self.__valueRealNumber = valueRealNumber

    @property
    def mMDSL_AttributeSet(self):
        return self.__mMDSL_AttributeSet

    @mMDSL_AttributeSet.setter
    def mMDSL_AttributeSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_AttributeSet__mMDSL_AttributeSet", None)
        self.__mMDSL_AttributeSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_AttributeOperation479"):
                opp_val = getattr(old_value, "mMDSL_AttributeOperation479", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_AttributeOperation479", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_AttributeOperation479"):
                opp_val = getattr(value, "mMDSL_AttributeOperation479", None)
                setattr(value, "mMDSL_AttributeOperation479", self)

    @property
    def mMDSL_AttributeSet481(self):
        return self.__mMDSL_AttributeSet481

    @mMDSL_AttributeSet481.setter
    def mMDSL_AttributeSet481(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_AttributeSet__mMDSL_AttributeSet481", None)
        self.__mMDSL_AttributeSet481 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Variable482"):
                opp_val = getattr(old_value, "mMDSL_Variable482", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Variable482", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Variable482"):
                opp_val = getattr(value, "mMDSL_Variable482", None)
                setattr(value, "mMDSL_Variable482", self)

class mMDSL_AttributeGet:

    def __init__(self, attrgetparams: str, mMDSL_AttributeGet: "mMDSL_AttributeOperation" = None):
        self.attrgetparams = attrgetparams
        self.mMDSL_AttributeGet = mMDSL_AttributeGet
        
    @property
    def attrgetparams(self) -> str:
        return self.__attrgetparams

    @attrgetparams.setter
    def attrgetparams(self, attrgetparams: str):
        self.__attrgetparams = attrgetparams

    @property
    def mMDSL_AttributeGet(self):
        return self.__mMDSL_AttributeGet

    @mMDSL_AttributeGet.setter
    def mMDSL_AttributeGet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_AttributeGet__mMDSL_AttributeGet", None)
        self.__mMDSL_AttributeGet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_AttributeOperation477"):
                opp_val = getattr(old_value, "mMDSL_AttributeOperation477", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_AttributeOperation477", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_AttributeOperation477"):
                opp_val = getattr(value, "mMDSL_AttributeOperation477", None)
                setattr(value, "mMDSL_AttributeOperation477", self)

class mMDSL_RelationInstanceGetAll:

    pass
class mMDSL_RelationInstanceSet:

    pass
class mMDSL_RelationInstanceGet:

    pass
class mMDSL_RelationInstanceDelete:

    pass
class mMDSL_RelationInstanceCreate:

    def __init__(self, name: str, mMDSL_RelationInstanceCreate459: "mMDSL_ClassInstanceCreate" = None, mMDSL_RelationInstanceCreate463: "mMDSL_RelationInstanceDelete" = None, mMDSL_RelationInstanceCreate466: "mMDSL_RelationInstanceGet" = None, mMDSL_RelationInstanceCreate: "mMDSL_RelationInstance" = None, mMDSL_RelationInstanceCreate453: "mMDSL_Relation" = None, mMDSL_RelationInstanceCreate456: "mMDSL_ClassInstanceCreate" = None, mMDSL_RelationInstanceCreate472: "mMDSL_RelationInstanceSet" = None):
        self.name = name
        self.mMDSL_RelationInstanceCreate459 = mMDSL_RelationInstanceCreate459
        self.mMDSL_RelationInstanceCreate463 = mMDSL_RelationInstanceCreate463
        self.mMDSL_RelationInstanceCreate466 = mMDSL_RelationInstanceCreate466
        self.mMDSL_RelationInstanceCreate = mMDSL_RelationInstanceCreate
        self.mMDSL_RelationInstanceCreate453 = mMDSL_RelationInstanceCreate453
        self.mMDSL_RelationInstanceCreate456 = mMDSL_RelationInstanceCreate456
        self.mMDSL_RelationInstanceCreate472 = mMDSL_RelationInstanceCreate472
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_RelationInstanceCreate453(self):
        return self.__mMDSL_RelationInstanceCreate453

    @mMDSL_RelationInstanceCreate453.setter
    def mMDSL_RelationInstanceCreate453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_RelationInstanceCreate__mMDSL_RelationInstanceCreate453", None)
        self.__mMDSL_RelationInstanceCreate453 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Relation454"):
                opp_val = getattr(old_value, "mMDSL_Relation454", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Relation454", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Relation454"):
                opp_val = getattr(value, "mMDSL_Relation454", None)
                setattr(value, "mMDSL_Relation454", self)

    @property
    def mMDSL_RelationInstanceCreate463(self):
        return self.__mMDSL_RelationInstanceCreate463

    @mMDSL_RelationInstanceCreate463.setter
    def mMDSL_RelationInstanceCreate463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_RelationInstanceCreate__mMDSL_RelationInstanceCreate463", None)
        self.__mMDSL_RelationInstanceCreate463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RelationInstanceDelete462"):
                opp_val = getattr(old_value, "mMDSL_RelationInstanceDelete462", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RelationInstanceDelete462", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RelationInstanceDelete462"):
                opp_val = getattr(value, "mMDSL_RelationInstanceDelete462", None)
                setattr(value, "mMDSL_RelationInstanceDelete462", self)

    @property
    def mMDSL_RelationInstanceCreate459(self):
        return self.__mMDSL_RelationInstanceCreate459

    @mMDSL_RelationInstanceCreate459.setter
    def mMDSL_RelationInstanceCreate459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_RelationInstanceCreate__mMDSL_RelationInstanceCreate459", None)
        self.__mMDSL_RelationInstanceCreate459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ClassInstanceCreate460"):
                opp_val = getattr(old_value, "mMDSL_ClassInstanceCreate460", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ClassInstanceCreate460", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ClassInstanceCreate460"):
                opp_val = getattr(value, "mMDSL_ClassInstanceCreate460", None)
                setattr(value, "mMDSL_ClassInstanceCreate460", self)

    @property
    def mMDSL_RelationInstanceCreate456(self):
        return self.__mMDSL_RelationInstanceCreate456

    @mMDSL_RelationInstanceCreate456.setter
    def mMDSL_RelationInstanceCreate456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_RelationInstanceCreate__mMDSL_RelationInstanceCreate456", None)
        self.__mMDSL_RelationInstanceCreate456 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ClassInstanceCreate457"):
                opp_val = getattr(old_value, "mMDSL_ClassInstanceCreate457", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ClassInstanceCreate457", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ClassInstanceCreate457"):
                opp_val = getattr(value, "mMDSL_ClassInstanceCreate457", None)
                setattr(value, "mMDSL_ClassInstanceCreate457", self)

    @property
    def mMDSL_RelationInstanceCreate466(self):
        return self.__mMDSL_RelationInstanceCreate466

    @mMDSL_RelationInstanceCreate466.setter
    def mMDSL_RelationInstanceCreate466(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_RelationInstanceCreate__mMDSL_RelationInstanceCreate466", None)
        self.__mMDSL_RelationInstanceCreate466 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RelationInstanceGet465"):
                opp_val = getattr(old_value, "mMDSL_RelationInstanceGet465", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RelationInstanceGet465", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RelationInstanceGet465"):
                opp_val = getattr(value, "mMDSL_RelationInstanceGet465", None)
                setattr(value, "mMDSL_RelationInstanceGet465", self)

    @property
    def mMDSL_RelationInstanceCreate(self):
        return self.__mMDSL_RelationInstanceCreate

    @mMDSL_RelationInstanceCreate.setter
    def mMDSL_RelationInstanceCreate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_RelationInstanceCreate__mMDSL_RelationInstanceCreate", None)
        self.__mMDSL_RelationInstanceCreate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RelationInstance443"):
                opp_val = getattr(old_value, "mMDSL_RelationInstance443", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RelationInstance443", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RelationInstance443"):
                opp_val = getattr(value, "mMDSL_RelationInstance443", None)
                setattr(value, "mMDSL_RelationInstance443", self)

    @property
    def mMDSL_RelationInstanceCreate472(self):
        return self.__mMDSL_RelationInstanceCreate472

    @mMDSL_RelationInstanceCreate472.setter
    def mMDSL_RelationInstanceCreate472(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_RelationInstanceCreate__mMDSL_RelationInstanceCreate472", None)
        self.__mMDSL_RelationInstanceCreate472 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RelationInstanceSet471"):
                opp_val = getattr(old_value, "mMDSL_RelationInstanceSet471", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RelationInstanceSet471", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RelationInstanceSet471"):
                opp_val = getattr(value, "mMDSL_RelationInstanceSet471", None)
                setattr(value, "mMDSL_RelationInstanceSet471", self)

class mMDSL_ClassInstanceGetAll:

    pass
class mMDSL_ClassInstanceSet:

    pass
class mMDSL_ClassInstanceGet:

    pass
class mMDSL_ClassInstanceDelete:

    pass
class mMDSL_ClassInstanceCreate:

    def __init__(self, name: str, mMDSL_ClassInstanceCreate435: "mMDSL_ClassInstanceGet" = None, mMDSL_ClassInstanceCreate441: "mMDSL_ClassInstanceSet" = None, mMDSL_ClassInstanceCreate: "mMDSL_ClassInstance" = None, mMDSL_ClassInstanceCreate428: "mMDSL_Class" = None, mMDSL_ClassInstanceCreate432: "mMDSL_ClassInstanceDelete" = None, mMDSL_ClassInstanceCreate460: "mMDSL_RelationInstanceCreate" = None, mMDSL_ClassInstanceCreate457: "mMDSL_RelationInstanceCreate" = None):
        self.name = name
        self.mMDSL_ClassInstanceCreate435 = mMDSL_ClassInstanceCreate435
        self.mMDSL_ClassInstanceCreate441 = mMDSL_ClassInstanceCreate441
        self.mMDSL_ClassInstanceCreate = mMDSL_ClassInstanceCreate
        self.mMDSL_ClassInstanceCreate428 = mMDSL_ClassInstanceCreate428
        self.mMDSL_ClassInstanceCreate432 = mMDSL_ClassInstanceCreate432
        self.mMDSL_ClassInstanceCreate460 = mMDSL_ClassInstanceCreate460
        self.mMDSL_ClassInstanceCreate457 = mMDSL_ClassInstanceCreate457
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_ClassInstanceCreate428(self):
        return self.__mMDSL_ClassInstanceCreate428

    @mMDSL_ClassInstanceCreate428.setter
    def mMDSL_ClassInstanceCreate428(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ClassInstanceCreate__mMDSL_ClassInstanceCreate428", None)
        self.__mMDSL_ClassInstanceCreate428 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Class429"):
                opp_val = getattr(old_value, "mMDSL_Class429", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Class429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Class429"):
                opp_val = getattr(value, "mMDSL_Class429", None)
                setattr(value, "mMDSL_Class429", self)

    @property
    def mMDSL_ClassInstanceCreate(self):
        return self.__mMDSL_ClassInstanceCreate

    @mMDSL_ClassInstanceCreate.setter
    def mMDSL_ClassInstanceCreate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ClassInstanceCreate__mMDSL_ClassInstanceCreate", None)
        self.__mMDSL_ClassInstanceCreate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ClassInstance418"):
                opp_val = getattr(old_value, "mMDSL_ClassInstance418", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ClassInstance418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ClassInstance418"):
                opp_val = getattr(value, "mMDSL_ClassInstance418", None)
                setattr(value, "mMDSL_ClassInstance418", self)

    @property
    def mMDSL_ClassInstanceCreate441(self):
        return self.__mMDSL_ClassInstanceCreate441

    @mMDSL_ClassInstanceCreate441.setter
    def mMDSL_ClassInstanceCreate441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ClassInstanceCreate__mMDSL_ClassInstanceCreate441", None)
        self.__mMDSL_ClassInstanceCreate441 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ClassInstanceSet440"):
                opp_val = getattr(old_value, "mMDSL_ClassInstanceSet440", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ClassInstanceSet440", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ClassInstanceSet440"):
                opp_val = getattr(value, "mMDSL_ClassInstanceSet440", None)
                setattr(value, "mMDSL_ClassInstanceSet440", self)

    @property
    def mMDSL_ClassInstanceCreate457(self):
        return self.__mMDSL_ClassInstanceCreate457

    @mMDSL_ClassInstanceCreate457.setter
    def mMDSL_ClassInstanceCreate457(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ClassInstanceCreate__mMDSL_ClassInstanceCreate457", None)
        self.__mMDSL_ClassInstanceCreate457 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RelationInstanceCreate456"):
                opp_val = getattr(old_value, "mMDSL_RelationInstanceCreate456", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RelationInstanceCreate456", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RelationInstanceCreate456"):
                opp_val = getattr(value, "mMDSL_RelationInstanceCreate456", None)
                setattr(value, "mMDSL_RelationInstanceCreate456", self)

    @property
    def mMDSL_ClassInstanceCreate460(self):
        return self.__mMDSL_ClassInstanceCreate460

    @mMDSL_ClassInstanceCreate460.setter
    def mMDSL_ClassInstanceCreate460(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ClassInstanceCreate__mMDSL_ClassInstanceCreate460", None)
        self.__mMDSL_ClassInstanceCreate460 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RelationInstanceCreate459"):
                opp_val = getattr(old_value, "mMDSL_RelationInstanceCreate459", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RelationInstanceCreate459", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RelationInstanceCreate459"):
                opp_val = getattr(value, "mMDSL_RelationInstanceCreate459", None)
                setattr(value, "mMDSL_RelationInstanceCreate459", self)

    @property
    def mMDSL_ClassInstanceCreate432(self):
        return self.__mMDSL_ClassInstanceCreate432

    @mMDSL_ClassInstanceCreate432.setter
    def mMDSL_ClassInstanceCreate432(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ClassInstanceCreate__mMDSL_ClassInstanceCreate432", None)
        self.__mMDSL_ClassInstanceCreate432 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ClassInstanceDelete431"):
                opp_val = getattr(old_value, "mMDSL_ClassInstanceDelete431", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ClassInstanceDelete431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ClassInstanceDelete431"):
                opp_val = getattr(value, "mMDSL_ClassInstanceDelete431", None)
                setattr(value, "mMDSL_ClassInstanceDelete431", self)

    @property
    def mMDSL_ClassInstanceCreate435(self):
        return self.__mMDSL_ClassInstanceCreate435

    @mMDSL_ClassInstanceCreate435.setter
    def mMDSL_ClassInstanceCreate435(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ClassInstanceCreate__mMDSL_ClassInstanceCreate435", None)
        self.__mMDSL_ClassInstanceCreate435 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ClassInstanceGet434"):
                opp_val = getattr(old_value, "mMDSL_ClassInstanceGet434", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ClassInstanceGet434", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ClassInstanceGet434"):
                opp_val = getattr(value, "mMDSL_ClassInstanceGet434", None)
                setattr(value, "mMDSL_ClassInstanceGet434", self)

class mMDSL_RelationInstance:

    pass
class mMDSL_ClassInstance:

    pass
class mMDSL_ModelLoad:

    pass
class mMDSL_ModelSave:

    pass
class mMDSL_ModelDiscard:

    pass
class mMDSL_ModelDelete:

    pass
class mMDSL_ModelCreate:

    def __init__(self, name: str, mMDSL_ModelCreate396: "mMDSL_ModelType" = None, mMDSL_ModelCreate400: "mMDSL_ModelDelete" = None, mMDSL_ModelCreate403: "mMDSL_ModelDiscard" = None, mMDSL_ModelCreate406: "mMDSL_ModelSave" = None, mMDSL_ModelCreate: "mMDSL_ModelOperation" = None, mMDSL_ModelCreate409: "mMDSL_ModelLoad" = None, mMDSL_ModelCreate412: "mMDSL_ModelIsLoaded" = None):
        self.name = name
        self.mMDSL_ModelCreate396 = mMDSL_ModelCreate396
        self.mMDSL_ModelCreate400 = mMDSL_ModelCreate400
        self.mMDSL_ModelCreate403 = mMDSL_ModelCreate403
        self.mMDSL_ModelCreate406 = mMDSL_ModelCreate406
        self.mMDSL_ModelCreate = mMDSL_ModelCreate
        self.mMDSL_ModelCreate409 = mMDSL_ModelCreate409
        self.mMDSL_ModelCreate412 = mMDSL_ModelCreate412
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_ModelCreate400(self):
        return self.__mMDSL_ModelCreate400

    @mMDSL_ModelCreate400.setter
    def mMDSL_ModelCreate400(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelCreate__mMDSL_ModelCreate400", None)
        self.__mMDSL_ModelCreate400 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelDelete399"):
                opp_val = getattr(old_value, "mMDSL_ModelDelete399", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ModelDelete399", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelDelete399"):
                opp_val = getattr(value, "mMDSL_ModelDelete399", None)
                setattr(value, "mMDSL_ModelDelete399", self)

    @property
    def mMDSL_ModelCreate409(self):
        return self.__mMDSL_ModelCreate409

    @mMDSL_ModelCreate409.setter
    def mMDSL_ModelCreate409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelCreate__mMDSL_ModelCreate409", None)
        self.__mMDSL_ModelCreate409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelLoad408"):
                opp_val = getattr(old_value, "mMDSL_ModelLoad408", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ModelLoad408", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelLoad408"):
                opp_val = getattr(value, "mMDSL_ModelLoad408", None)
                setattr(value, "mMDSL_ModelLoad408", self)

    @property
    def mMDSL_ModelCreate406(self):
        return self.__mMDSL_ModelCreate406

    @mMDSL_ModelCreate406.setter
    def mMDSL_ModelCreate406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelCreate__mMDSL_ModelCreate406", None)
        self.__mMDSL_ModelCreate406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelSave405"):
                opp_val = getattr(old_value, "mMDSL_ModelSave405", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ModelSave405", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelSave405"):
                opp_val = getattr(value, "mMDSL_ModelSave405", None)
                setattr(value, "mMDSL_ModelSave405", self)

    @property
    def mMDSL_ModelCreate412(self):
        return self.__mMDSL_ModelCreate412

    @mMDSL_ModelCreate412.setter
    def mMDSL_ModelCreate412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelCreate__mMDSL_ModelCreate412", None)
        self.__mMDSL_ModelCreate412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelIsLoaded411"):
                opp_val = getattr(old_value, "mMDSL_ModelIsLoaded411", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ModelIsLoaded411", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelIsLoaded411"):
                opp_val = getattr(value, "mMDSL_ModelIsLoaded411", None)
                setattr(value, "mMDSL_ModelIsLoaded411", self)

    @property
    def mMDSL_ModelCreate(self):
        return self.__mMDSL_ModelCreate

    @mMDSL_ModelCreate.setter
    def mMDSL_ModelCreate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelCreate__mMDSL_ModelCreate", None)
        self.__mMDSL_ModelCreate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelOperation384"):
                opp_val = getattr(old_value, "mMDSL_ModelOperation384", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ModelOperation384", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelOperation384"):
                opp_val = getattr(value, "mMDSL_ModelOperation384", None)
                setattr(value, "mMDSL_ModelOperation384", self)

    @property
    def mMDSL_ModelCreate403(self):
        return self.__mMDSL_ModelCreate403

    @mMDSL_ModelCreate403.setter
    def mMDSL_ModelCreate403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelCreate__mMDSL_ModelCreate403", None)
        self.__mMDSL_ModelCreate403 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelDiscard402"):
                opp_val = getattr(old_value, "mMDSL_ModelDiscard402", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ModelDiscard402", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelDiscard402"):
                opp_val = getattr(value, "mMDSL_ModelDiscard402", None)
                setattr(value, "mMDSL_ModelDiscard402", self)

    @property
    def mMDSL_ModelCreate396(self):
        return self.__mMDSL_ModelCreate396

    @mMDSL_ModelCreate396.setter
    def mMDSL_ModelCreate396(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelCreate__mMDSL_ModelCreate396", None)
        self.__mMDSL_ModelCreate396 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelType397"):
                opp_val = getattr(old_value, "mMDSL_ModelType397", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ModelType397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelType397"):
                opp_val = getattr(value, "mMDSL_ModelType397", None)
                setattr(value, "mMDSL_ModelType397", self)

class mMDSL_RemoveContextItem:

    pass
class mMDSL_InsertContextItem:

    def __init__(self, name: str, context: str, mMDSL_InsertContextItem: "mMDSL_ContextItem" = None, mMDSL_InsertContextItem382: "mMDSL_RemoveContextItem" = None):
        self.name = name
        self.context = context
        self.mMDSL_InsertContextItem = mMDSL_InsertContextItem
        self.mMDSL_InsertContextItem382 = mMDSL_InsertContextItem382
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def mMDSL_InsertContextItem382(self):
        return self.__mMDSL_InsertContextItem382

    @mMDSL_InsertContextItem382.setter
    def mMDSL_InsertContextItem382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_InsertContextItem__mMDSL_InsertContextItem382", None)
        self.__mMDSL_InsertContextItem382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RemoveContextItem381"):
                opp_val = getattr(old_value, "mMDSL_RemoveContextItem381", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RemoveContextItem381", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RemoveContextItem381"):
                opp_val = getattr(value, "mMDSL_RemoveContextItem381", None)
                setattr(value, "mMDSL_RemoveContextItem381", self)

    @property
    def mMDSL_InsertContextItem(self):
        return self.__mMDSL_InsertContextItem

    @mMDSL_InsertContextItem.setter
    def mMDSL_InsertContextItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_InsertContextItem__mMDSL_InsertContextItem", None)
        self.__mMDSL_InsertContextItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ContextItem377"):
                opp_val = getattr(old_value, "mMDSL_ContextItem377", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ContextItem377", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ContextItem377"):
                opp_val = getattr(value, "mMDSL_ContextItem377", None)
                setattr(value, "mMDSL_ContextItem377", self)

class mMDSL_ModelIsLoaded:

    pass
class mMDSL_InsertMenuItem:

    def __init__(self, name: str, menu: str, mMDSL_InsertMenuItem: "mMDSL_MenuItem" = None, mMDSL_InsertMenuItem375: "mMDSL_RemoveMenuItem" = None):
        self.name = name
        self.menu = menu
        self.mMDSL_InsertMenuItem = mMDSL_InsertMenuItem
        self.mMDSL_InsertMenuItem375 = mMDSL_InsertMenuItem375
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def menu(self) -> str:
        return self.__menu

    @menu.setter
    def menu(self, menu: str):
        self.__menu = menu

    @property
    def mMDSL_InsertMenuItem(self):
        return self.__mMDSL_InsertMenuItem

    @mMDSL_InsertMenuItem.setter
    def mMDSL_InsertMenuItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_InsertMenuItem__mMDSL_InsertMenuItem", None)
        self.__mMDSL_InsertMenuItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_MenuItem370"):
                opp_val = getattr(old_value, "mMDSL_MenuItem370", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_MenuItem370", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_MenuItem370"):
                opp_val = getattr(value, "mMDSL_MenuItem370", None)
                setattr(value, "mMDSL_MenuItem370", self)

    @property
    def mMDSL_InsertMenuItem375(self):
        return self.__mMDSL_InsertMenuItem375

    @mMDSL_InsertMenuItem375.setter
    def mMDSL_InsertMenuItem375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_InsertMenuItem__mMDSL_InsertMenuItem375", None)
        self.__mMDSL_InsertMenuItem375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RemoveMenuItem374"):
                opp_val = getattr(old_value, "mMDSL_RemoveMenuItem374", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RemoveMenuItem374", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RemoveMenuItem374"):
                opp_val = getattr(value, "mMDSL_RemoveMenuItem374", None)
                setattr(value, "mMDSL_RemoveMenuItem374", self)

class mMDSL_ContextItem:

    pass
class mMDSL_MenuItem:

    pass
class mMDSL_RemoveMenuItem:

    pass
class mMDSL_ItemOperation:

    pass
class mMDSL_ViewBox:

    def __init__(self, title: str, text: str, mMDSL_ViewBox: "mMDSL_SimpleUI" = None):
        self.title = title
        self.text = text
        self.mMDSL_ViewBox = mMDSL_ViewBox
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def mMDSL_ViewBox(self):
        return self.__mMDSL_ViewBox

    @mMDSL_ViewBox.setter
    def mMDSL_ViewBox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ViewBox__mMDSL_ViewBox", None)
        self.__mMDSL_ViewBox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SimpleUI362"):
                opp_val = getattr(old_value, "mMDSL_SimpleUI362", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SimpleUI362", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SimpleUI362"):
                opp_val = getattr(value, "mMDSL_SimpleUI362", None)
                setattr(value, "mMDSL_SimpleUI362", self)

class mMDSL_WarningBox:

    def __init__(self, title: str, text: str, buttontype: str, mMDSL_WarningBox: "mMDSL_SimpleUI" = None):
        self.title = title
        self.text = text
        self.buttontype = buttontype
        self.mMDSL_WarningBox = mMDSL_WarningBox
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def buttontype(self) -> str:
        return self.__buttontype

    @buttontype.setter
    def buttontype(self, buttontype: str):
        self.__buttontype = buttontype

    @property
    def mMDSL_WarningBox(self):
        return self.__mMDSL_WarningBox

    @mMDSL_WarningBox.setter
    def mMDSL_WarningBox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_WarningBox__mMDSL_WarningBox", None)
        self.__mMDSL_WarningBox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SimpleUI360"):
                opp_val = getattr(old_value, "mMDSL_SimpleUI360", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SimpleUI360", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SimpleUI360"):
                opp_val = getattr(value, "mMDSL_SimpleUI360", None)
                setattr(value, "mMDSL_SimpleUI360", self)

class mMDSL_ErrorBox:

    def __init__(self, title: str, text: str, buttontype: str, mMDSL_ErrorBox: "mMDSL_SimpleUI" = None):
        self.title = title
        self.text = text
        self.buttontype = buttontype
        self.mMDSL_ErrorBox = mMDSL_ErrorBox
        
    @property
    def buttontype(self) -> str:
        return self.__buttontype

    @buttontype.setter
    def buttontype(self, buttontype: str):
        self.__buttontype = buttontype

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def mMDSL_ErrorBox(self):
        return self.__mMDSL_ErrorBox

    @mMDSL_ErrorBox.setter
    def mMDSL_ErrorBox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ErrorBox__mMDSL_ErrorBox", None)
        self.__mMDSL_ErrorBox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SimpleUI358"):
                opp_val = getattr(old_value, "mMDSL_SimpleUI358", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SimpleUI358", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SimpleUI358"):
                opp_val = getattr(value, "mMDSL_SimpleUI358", None)
                setattr(value, "mMDSL_SimpleUI358", self)

class mMDSL_InfoBox:

    def __init__(self, title: str, text: str, mMDSL_InfoBox: "mMDSL_SimpleUI" = None):
        self.title = title
        self.text = text
        self.mMDSL_InfoBox = mMDSL_InfoBox
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def mMDSL_InfoBox(self):
        return self.__mMDSL_InfoBox

    @mMDSL_InfoBox.setter
    def mMDSL_InfoBox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_InfoBox__mMDSL_InfoBox", None)
        self.__mMDSL_InfoBox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SimpleUI356"):
                opp_val = getattr(old_value, "mMDSL_SimpleUI356", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SimpleUI356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SimpleUI356"):
                opp_val = getattr(value, "mMDSL_SimpleUI356", None)
                setattr(value, "mMDSL_SimpleUI356", self)

class mMDSL_EditBox:

    def __init__(self, title: str, text: str, okbuttontext: str, mMDSL_EditBox: "mMDSL_SimpleUI" = None):
        self.title = title
        self.text = text
        self.okbuttontext = okbuttontext
        self.mMDSL_EditBox = mMDSL_EditBox
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def okbuttontext(self) -> str:
        return self.__okbuttontext

    @okbuttontext.setter
    def okbuttontext(self, okbuttontext: str):
        self.__okbuttontext = okbuttontext

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def mMDSL_EditBox(self):
        return self.__mMDSL_EditBox

    @mMDSL_EditBox.setter
    def mMDSL_EditBox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_EditBox__mMDSL_EditBox", None)
        self.__mMDSL_EditBox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SimpleUI354"):
                opp_val = getattr(old_value, "mMDSL_SimpleUI354", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SimpleUI354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SimpleUI354"):
                opp_val = getattr(value, "mMDSL_SimpleUI354", None)
                setattr(value, "mMDSL_SimpleUI354", self)

class mMDSL_DirSetWorking:

    def __init__(self, dirname: str, mMDSL_DirSetWorking: "mMDSL_DirOperation" = None):
        self.dirname = dirname
        self.mMDSL_DirSetWorking = mMDSL_DirSetWorking
        
    @property
    def dirname(self) -> str:
        return self.__dirname

    @dirname.setter
    def dirname(self, dirname: str):
        self.__dirname = dirname

    @property
    def mMDSL_DirSetWorking(self):
        return self.__mMDSL_DirSetWorking

    @mMDSL_DirSetWorking.setter
    def mMDSL_DirSetWorking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_DirSetWorking__mMDSL_DirSetWorking", None)
        self.__mMDSL_DirSetWorking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_DirOperation344"):
                opp_val = getattr(old_value, "mMDSL_DirOperation344", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_DirOperation344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_DirOperation344"):
                opp_val = getattr(value, "mMDSL_DirOperation344", None)
                setattr(value, "mMDSL_DirOperation344", self)

class mMDSL_FileWrite:

    def __init__(self, filename: str, text: str, append: str, mMDSL_FileWrite: "mMDSL_FileOperation" = None):
        self.filename = filename
        self.text = text
        self.append = append
        self.mMDSL_FileWrite = mMDSL_FileWrite
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def append(self) -> str:
        return self.__append

    @append.setter
    def append(self, append: str):
        self.__append = append

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def mMDSL_FileWrite(self):
        return self.__mMDSL_FileWrite

    @mMDSL_FileWrite.setter
    def mMDSL_FileWrite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_FileWrite__mMDSL_FileWrite", None)
        self.__mMDSL_FileWrite = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_FileOperation342"):
                opp_val = getattr(old_value, "mMDSL_FileOperation342", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_FileOperation342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_FileOperation342"):
                opp_val = getattr(value, "mMDSL_FileOperation342", None)
                setattr(value, "mMDSL_FileOperation342", self)

class mMDSL_FileRead:

    def __init__(self, filename: str, mMDSL_FileRead: "mMDSL_FileOperation" = None):
        self.filename = filename
        self.mMDSL_FileRead = mMDSL_FileRead
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def mMDSL_FileRead(self):
        return self.__mMDSL_FileRead

    @mMDSL_FileRead.setter
    def mMDSL_FileRead(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_FileRead__mMDSL_FileRead", None)
        self.__mMDSL_FileRead = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_FileOperation340"):
                opp_val = getattr(old_value, "mMDSL_FileOperation340", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_FileOperation340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_FileOperation340"):
                opp_val = getattr(value, "mMDSL_FileOperation340", None)
                setattr(value, "mMDSL_FileOperation340", self)

class mMDSL_FileCreate:

    def __init__(self, filename: str, mMDSL_FileCreate: "mMDSL_FileOperation" = None):
        self.filename = filename
        self.mMDSL_FileCreate = mMDSL_FileCreate
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def mMDSL_FileCreate(self):
        return self.__mMDSL_FileCreate

    @mMDSL_FileCreate.setter
    def mMDSL_FileCreate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_FileCreate__mMDSL_FileCreate", None)
        self.__mMDSL_FileCreate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_FileOperation338"):
                opp_val = getattr(old_value, "mMDSL_FileOperation338", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_FileOperation338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_FileOperation338"):
                opp_val = getattr(value, "mMDSL_FileOperation338", None)
                setattr(value, "mMDSL_FileOperation338", self)

class mMDSL_FileDelete:

    def __init__(self, filename: str, mMDSL_FileDelete: "mMDSL_FileOperation" = None):
        self.filename = filename
        self.mMDSL_FileDelete = mMDSL_FileDelete
        
    @property
    def filename(self) -> str:
        return self.__filename

    @filename.setter
    def filename(self, filename: str):
        self.__filename = filename

    @property
    def mMDSL_FileDelete(self):
        return self.__mMDSL_FileDelete

    @mMDSL_FileDelete.setter
    def mMDSL_FileDelete(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_FileDelete__mMDSL_FileDelete", None)
        self.__mMDSL_FileDelete = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_FileOperation336"):
                opp_val = getattr(old_value, "mMDSL_FileOperation336", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_FileOperation336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_FileOperation336"):
                opp_val = getattr(value, "mMDSL_FileOperation336", None)
                setattr(value, "mMDSL_FileOperation336", self)

class mMDSL_FileCopy:

    def __init__(self, src: str, dest: str, mMDSL_FileCopy: "mMDSL_FileOperation" = None):
        self.src = src
        self.dest = dest
        self.mMDSL_FileCopy = mMDSL_FileCopy
        
    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def dest(self) -> str:
        return self.__dest

    @dest.setter
    def dest(self, dest: str):
        self.__dest = dest

    @property
    def mMDSL_FileCopy(self):
        return self.__mMDSL_FileCopy

    @mMDSL_FileCopy.setter
    def mMDSL_FileCopy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_FileCopy__mMDSL_FileCopy", None)
        self.__mMDSL_FileCopy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_FileOperation334"):
                opp_val = getattr(old_value, "mMDSL_FileOperation334", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_FileOperation334", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_FileOperation334"):
                opp_val = getattr(value, "mMDSL_FileOperation334", None)
                setattr(value, "mMDSL_FileOperation334", self)

class mMDSL_DirList:

    def __init__(self, dirname: str, mMDSL_DirList: "mMDSL_DirOperation" = None):
        self.dirname = dirname
        self.mMDSL_DirList = mMDSL_DirList
        
    @property
    def dirname(self) -> str:
        return self.__dirname

    @dirname.setter
    def dirname(self, dirname: str):
        self.__dirname = dirname

    @property
    def mMDSL_DirList(self):
        return self.__mMDSL_DirList

    @mMDSL_DirList.setter
    def mMDSL_DirList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_DirList__mMDSL_DirList", None)
        self.__mMDSL_DirList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_DirOperation352"):
                opp_val = getattr(old_value, "mMDSL_DirOperation352", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_DirOperation352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_DirOperation352"):
                opp_val = getattr(value, "mMDSL_DirOperation352", None)
                setattr(value, "mMDSL_DirOperation352", self)

class mMDSL_DirDelete:

    def __init__(self, dirname: str, mMDSL_DirDelete: "mMDSL_DirOperation" = None):
        self.dirname = dirname
        self.mMDSL_DirDelete = mMDSL_DirDelete
        
    @property
    def dirname(self) -> str:
        return self.__dirname

    @dirname.setter
    def dirname(self, dirname: str):
        self.__dirname = dirname

    @property
    def mMDSL_DirDelete(self):
        return self.__mMDSL_DirDelete

    @mMDSL_DirDelete.setter
    def mMDSL_DirDelete(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_DirDelete__mMDSL_DirDelete", None)
        self.__mMDSL_DirDelete = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_DirOperation350"):
                opp_val = getattr(old_value, "mMDSL_DirOperation350", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_DirOperation350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_DirOperation350"):
                opp_val = getattr(value, "mMDSL_DirOperation350", None)
                setattr(value, "mMDSL_DirOperation350", self)

class mMDSL_DirCreate:

    def __init__(self, dirname: str, mMDSL_DirCreate: "mMDSL_DirOperation" = None):
        self.dirname = dirname
        self.mMDSL_DirCreate = mMDSL_DirCreate
        
    @property
    def dirname(self) -> str:
        return self.__dirname

    @dirname.setter
    def dirname(self, dirname: str):
        self.__dirname = dirname

    @property
    def mMDSL_DirCreate(self):
        return self.__mMDSL_DirCreate

    @mMDSL_DirCreate.setter
    def mMDSL_DirCreate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_DirCreate__mMDSL_DirCreate", None)
        self.__mMDSL_DirCreate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_DirOperation348"):
                opp_val = getattr(old_value, "mMDSL_DirOperation348", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_DirOperation348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_DirOperation348"):
                opp_val = getattr(value, "mMDSL_DirOperation348", None)
                setattr(value, "mMDSL_DirOperation348", self)

class mMDSL_DirGetWorking:

    pass
class mMDSL_EObject:

    pass
class mMDSL_Expression:

    def __init__(self, true: str, false: str, valueString: str, valueRealNumber: str, mMDSL_Expression: "mMDSL_Expr" = None, mMDSL_Expression302: "mMDSL_EObject" = None, mMDSL_Expression305: "mMDSL_Expression" = None, mMDSL_Expression303: "mMDSL_Expression" = None, mMDSL_Expression308: "mMDSL_Expression" = None, mMDSL_Expression306: "mMDSL_Expression" = None, mMDSL_Expression311: "mMDSL_Expression" = None, mMDSL_Expression309: "mMDSL_Expression" = None, mMDSL_Expression313: "mMDSL_Variable" = None, mMDSL_Expression317: "mMDSL_Expression" = None, mMDSL_Expression315: "mMDSL_Expression" = None, mMDSL_Expression320: "mMDSL_Expression" = None, mMDSL_Expression318: "mMDSL_Expression" = None):
        self.true = true
        self.false = false
        self.valueString = valueString
        self.valueRealNumber = valueRealNumber
        self.mMDSL_Expression = mMDSL_Expression
        self.mMDSL_Expression302 = mMDSL_Expression302
        self.mMDSL_Expression305 = mMDSL_Expression305
        self.mMDSL_Expression303 = mMDSL_Expression303
        self.mMDSL_Expression308 = mMDSL_Expression308
        self.mMDSL_Expression306 = mMDSL_Expression306
        self.mMDSL_Expression311 = mMDSL_Expression311
        self.mMDSL_Expression309 = mMDSL_Expression309
        self.mMDSL_Expression313 = mMDSL_Expression313
        self.mMDSL_Expression317 = mMDSL_Expression317
        self.mMDSL_Expression315 = mMDSL_Expression315
        self.mMDSL_Expression320 = mMDSL_Expression320
        self.mMDSL_Expression318 = mMDSL_Expression318
        
    @property
    def false(self) -> str:
        return self.__false

    @false.setter
    def false(self, false: str):
        self.__false = false

    @property
    def valueString(self) -> str:
        return self.__valueString

    @valueString.setter
    def valueString(self, valueString: str):
        self.__valueString = valueString

    @property
    def true(self) -> str:
        return self.__true

    @true.setter
    def true(self, true: str):
        self.__true = true

    @property
    def valueRealNumber(self) -> str:
        return self.__valueRealNumber

    @valueRealNumber.setter
    def valueRealNumber(self, valueRealNumber: str):
        self.__valueRealNumber = valueRealNumber

    @property
    def mMDSL_Expression306(self):
        return self.__mMDSL_Expression306

    @mMDSL_Expression306.setter
    def mMDSL_Expression306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression306", None)
        self.__mMDSL_Expression306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression308"):
                opp_val = getattr(old_value, "mMDSL_Expression308", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression308"):
                opp_val = getattr(value, "mMDSL_Expression308", None)
                setattr(value, "mMDSL_Expression308", self)

    @property
    def mMDSL_Expression313(self):
        return self.__mMDSL_Expression313

    @mMDSL_Expression313.setter
    def mMDSL_Expression313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression313", None)
        self.__mMDSL_Expression313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Variable314"):
                opp_val = getattr(old_value, "mMDSL_Variable314", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Variable314", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Variable314"):
                opp_val = getattr(value, "mMDSL_Variable314", None)
                setattr(value, "mMDSL_Variable314", self)

    @property
    def mMDSL_Expression315(self):
        return self.__mMDSL_Expression315

    @mMDSL_Expression315.setter
    def mMDSL_Expression315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression315", None)
        self.__mMDSL_Expression315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression317"):
                opp_val = getattr(old_value, "mMDSL_Expression317", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression317", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression317"):
                opp_val = getattr(value, "mMDSL_Expression317", None)
                setattr(value, "mMDSL_Expression317", self)

    @property
    def mMDSL_Expression308(self):
        return self.__mMDSL_Expression308

    @mMDSL_Expression308.setter
    def mMDSL_Expression308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression308", None)
        self.__mMDSL_Expression308 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression306"):
                opp_val = getattr(old_value, "mMDSL_Expression306", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression306"):
                opp_val = getattr(value, "mMDSL_Expression306", None)
                setattr(value, "mMDSL_Expression306", self)

    @property
    def mMDSL_Expression(self):
        return self.__mMDSL_Expression

    @mMDSL_Expression.setter
    def mMDSL_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression", None)
        self.__mMDSL_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expr300"):
                opp_val = getattr(old_value, "mMDSL_Expr300", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expr300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expr300"):
                opp_val = getattr(value, "mMDSL_Expr300", None)
                setattr(value, "mMDSL_Expr300", self)

    @property
    def mMDSL_Expression309(self):
        return self.__mMDSL_Expression309

    @mMDSL_Expression309.setter
    def mMDSL_Expression309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression309", None)
        self.__mMDSL_Expression309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression311"):
                opp_val = getattr(old_value, "mMDSL_Expression311", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression311"):
                opp_val = getattr(value, "mMDSL_Expression311", None)
                setattr(value, "mMDSL_Expression311", self)

    @property
    def mMDSL_Expression317(self):
        return self.__mMDSL_Expression317

    @mMDSL_Expression317.setter
    def mMDSL_Expression317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression317", None)
        self.__mMDSL_Expression317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression315"):
                opp_val = getattr(old_value, "mMDSL_Expression315", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression315", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression315"):
                opp_val = getattr(value, "mMDSL_Expression315", None)
                setattr(value, "mMDSL_Expression315", self)

    @property
    def mMDSL_Expression305(self):
        return self.__mMDSL_Expression305

    @mMDSL_Expression305.setter
    def mMDSL_Expression305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression305", None)
        self.__mMDSL_Expression305 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression303"):
                opp_val = getattr(old_value, "mMDSL_Expression303", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression303"):
                opp_val = getattr(value, "mMDSL_Expression303", None)
                setattr(value, "mMDSL_Expression303", self)

    @property
    def mMDSL_Expression320(self):
        return self.__mMDSL_Expression320

    @mMDSL_Expression320.setter
    def mMDSL_Expression320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression320", None)
        self.__mMDSL_Expression320 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression318"):
                opp_val = getattr(old_value, "mMDSL_Expression318", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression318", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression318"):
                opp_val = getattr(value, "mMDSL_Expression318", None)
                setattr(value, "mMDSL_Expression318", self)

    @property
    def mMDSL_Expression302(self):
        return self.__mMDSL_Expression302

    @mMDSL_Expression302.setter
    def mMDSL_Expression302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression302", None)
        self.__mMDSL_Expression302 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_EObject"):
                opp_val = getattr(old_value, "mMDSL_EObject", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_EObject"):
                opp_val = getattr(value, "mMDSL_EObject", None)
                setattr(value, "mMDSL_EObject", self)

    @property
    def mMDSL_Expression303(self):
        return self.__mMDSL_Expression303

    @mMDSL_Expression303.setter
    def mMDSL_Expression303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression303", None)
        self.__mMDSL_Expression303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression305"):
                opp_val = getattr(old_value, "mMDSL_Expression305", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression305"):
                opp_val = getattr(value, "mMDSL_Expression305", None)
                setattr(value, "mMDSL_Expression305", self)

    @property
    def mMDSL_Expression311(self):
        return self.__mMDSL_Expression311

    @mMDSL_Expression311.setter
    def mMDSL_Expression311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression311", None)
        self.__mMDSL_Expression311 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression309"):
                opp_val = getattr(old_value, "mMDSL_Expression309", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression309", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression309"):
                opp_val = getattr(value, "mMDSL_Expression309", None)
                setattr(value, "mMDSL_Expression309", self)

    @property
    def mMDSL_Expression318(self):
        return self.__mMDSL_Expression318

    @mMDSL_Expression318.setter
    def mMDSL_Expression318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Expression__mMDSL_Expression318", None)
        self.__mMDSL_Expression318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression320"):
                opp_val = getattr(old_value, "mMDSL_Expression320", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression320", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression320"):
                opp_val = getattr(value, "mMDSL_Expression320", None)
                setattr(value, "mMDSL_Expression320", self)

class mMDSL_OperatorOr:

    def __init__(self, or: str):
        self.or = or
        
    @property
    def or(self) -> str:
        return self.__or

    @or.setter
    def or(self, or: str):
        self.__or = or

class mMDSL_AttributeOperation:

    pass
class mMDSL_InstanceOperation:

    pass
class mMDSL_ModelOperation:

    pass
class mMDSL_SimpleUI:

    pass
class mMDSL_DirOperation:

    pass
class mMDSL_OperatorAdd:

    def __init__(self, subtract: str, add: str):
        self.subtract = subtract
        self.add = add
        
    @property
    def subtract(self) -> str:
        return self.__subtract

    @subtract.setter
    def subtract(self, subtract: str):
        self.__subtract = subtract

    @property
    def add(self) -> str:
        return self.__add

    @add.setter
    def add(self, add: str):
        self.__add = add

class mMDSL_FileOperation:

    pass
class mMDSL_OperatorMultiply:

    def __init__(self, multiply: str, divide: str, modulo: str):
        self.multiply = multiply
        self.divide = divide
        self.modulo = modulo
        
    @property
    def modulo(self) -> str:
        return self.__modulo

    @modulo.setter
    def modulo(self, modulo: str):
        self.__modulo = modulo

    @property
    def divide(self) -> str:
        return self.__divide

    @divide.setter
    def divide(self, divide: str):
        self.__divide = divide

    @property
    def multiply(self) -> str:
        return self.__multiply

    @multiply.setter
    def multiply(self, multiply: str):
        self.__multiply = multiply

class mMDSL_OperatorUnary:

    def __init__(self, not: str):
        self.not = not
        
    @property
    def not(self) -> str:
        return self.__not

    @not.setter
    def not(self, not: str):
        self.__not = not

class mMDSL_OperatorAnd:

    def __init__(self, and: str):
        self.and = and
        
    @property
    def and(self) -> str:
        return self.__and

    @and.setter
    def and(self, and: str):
        self.__and = and

class mMDSL_OperatorEqual:

    def __init__(self, equal: str, notequal: str):
        self.equal = equal
        self.notequal = notequal
        
    @property
    def notequal(self) -> str:
        return self.__notequal

    @notequal.setter
    def notequal(self, notequal: str):
        self.__notequal = notequal

    @property
    def equal(self) -> str:
        return self.__equal

    @equal.setter
    def equal(self, equal: str):
        self.__equal = equal

class mMDSL_OperatorCompare:

    def __init__(self, greaterequal: str, lesserequal: str, greater: str, lesser: str):
        self.greaterequal = greaterequal
        self.lesserequal = lesserequal
        self.greater = greater
        self.lesser = lesser
        
    @property
    def lesser(self) -> str:
        return self.__lesser

    @lesser.setter
    def lesser(self, lesser: str):
        self.__lesser = lesser

    @property
    def lesserequal(self) -> str:
        return self.__lesserequal

    @lesserequal.setter
    def lesserequal(self, lesserequal: str):
        self.__lesserequal = lesserequal

    @property
    def greaterequal(self) -> str:
        return self.__greaterequal

    @greaterequal.setter
    def greaterequal(self, greaterequal: str):
        self.__greaterequal = greaterequal

    @property
    def greater(self) -> str:
        return self.__greater

    @greater.setter
    def greater(self, greater: str):
        self.__greater = greater

class mMDSL_OperatorMultyAssign:

    def __init__(self, addassign: str, subassign: str, multiassign: str, divassign: str, mMDSL_OperatorMultyAssign: "mMDSL_OperatorAssign" = None):
        self.addassign = addassign
        self.subassign = subassign
        self.multiassign = multiassign
        self.divassign = divassign
        self.mMDSL_OperatorMultyAssign = mMDSL_OperatorMultyAssign
        
    @property
    def multiassign(self) -> str:
        return self.__multiassign

    @multiassign.setter
    def multiassign(self, multiassign: str):
        self.__multiassign = multiassign

    @property
    def subassign(self) -> str:
        return self.__subassign

    @subassign.setter
    def subassign(self, subassign: str):
        self.__subassign = subassign

    @property
    def divassign(self) -> str:
        return self.__divassign

    @divassign.setter
    def divassign(self, divassign: str):
        self.__divassign = divassign

    @property
    def addassign(self) -> str:
        return self.__addassign

    @addassign.setter
    def addassign(self, addassign: str):
        self.__addassign = addassign

    @property
    def mMDSL_OperatorMultyAssign(self):
        return self.__mMDSL_OperatorMultyAssign

    @mMDSL_OperatorMultyAssign.setter
    def mMDSL_OperatorMultyAssign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_OperatorMultyAssign__mMDSL_OperatorMultyAssign", None)
        self.__mMDSL_OperatorMultyAssign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_OperatorAssign298"):
                opp_val = getattr(old_value, "mMDSL_OperatorAssign298", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_OperatorAssign298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_OperatorAssign298"):
                opp_val = getattr(value, "mMDSL_OperatorAssign298", None)
                setattr(value, "mMDSL_OperatorAssign298", self)

class mMDSL_VarStatement:

    pass
class mMDSL_OperatorAssign:

    def __init__(self, assign: str, mMDSL_OperatorAssign: "mMDSL_Variable" = None, mMDSL_OperatorAssign298: "mMDSL_OperatorMultyAssign" = None):
        self.assign = assign
        self.mMDSL_OperatorAssign = mMDSL_OperatorAssign
        self.mMDSL_OperatorAssign298 = mMDSL_OperatorAssign298
        
    @property
    def assign(self) -> str:
        return self.__assign

    @assign.setter
    def assign(self, assign: str):
        self.__assign = assign

    @property
    def mMDSL_OperatorAssign(self):
        return self.__mMDSL_OperatorAssign

    @mMDSL_OperatorAssign.setter
    def mMDSL_OperatorAssign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_OperatorAssign__mMDSL_OperatorAssign", None)
        self.__mMDSL_OperatorAssign = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Variable261"):
                opp_val = getattr(old_value, "mMDSL_Variable261", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Variable261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Variable261"):
                opp_val = getattr(value, "mMDSL_Variable261", None)
                setattr(value, "mMDSL_Variable261", self)

    @property
    def mMDSL_OperatorAssign298(self):
        return self.__mMDSL_OperatorAssign298

    @mMDSL_OperatorAssign298.setter
    def mMDSL_OperatorAssign298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_OperatorAssign__mMDSL_OperatorAssign298", None)
        self.__mMDSL_OperatorAssign298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_OperatorMultyAssign"):
                opp_val = getattr(old_value, "mMDSL_OperatorMultyAssign", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_OperatorMultyAssign", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_OperatorMultyAssign"):
                opp_val = getattr(value, "mMDSL_OperatorMultyAssign", None)
                setattr(value, "mMDSL_OperatorMultyAssign", self)

class mMDSL_Expr:

    pass
class mMDSL_BreakContinue:

    def __init__(self, break: str, continue: str, mMDSL_BreakContinue259: "mMDSL_ForLoop" = None, mMDSL_BreakContinue: "mMDSL_WhileLoop" = None):
        self.break = break
        self.continue = continue
        self.mMDSL_BreakContinue259 = mMDSL_BreakContinue259
        self.mMDSL_BreakContinue = mMDSL_BreakContinue
        
    @property
    def continue(self) -> str:
        return self.__continue

    @continue.setter
    def continue(self, continue: str):
        self.__continue = continue

    @property
    def break(self) -> str:
        return self.__break

    @break.setter
    def break(self, break: str):
        self.__break = break

    @property
    def mMDSL_BreakContinue259(self):
        return self.__mMDSL_BreakContinue259

    @mMDSL_BreakContinue259.setter
    def mMDSL_BreakContinue259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_BreakContinue__mMDSL_BreakContinue259", None)
        self.__mMDSL_BreakContinue259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ForLoop258"):
                opp_val = getattr(old_value, "mMDSL_ForLoop258", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ForLoop258"):
                opp_val = getattr(value, "mMDSL_ForLoop258", None)
                if opp_val is None:
                    setattr(value, "mMDSL_ForLoop258", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_BreakContinue(self):
        return self.__mMDSL_BreakContinue

    @mMDSL_BreakContinue.setter
    def mMDSL_BreakContinue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_BreakContinue__mMDSL_BreakContinue", None)
        self.__mMDSL_BreakContinue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_WhileLoop253"):
                opp_val = getattr(old_value, "mMDSL_WhileLoop253", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_WhileLoop253"):
                opp_val = getattr(value, "mMDSL_WhileLoop253", None)
                if opp_val is None:
                    setattr(value, "mMDSL_WhileLoop253", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_ForLoop:

    def __init__(self, start: int, stop: int, interval: int, mMDSL_ForLoop255: set["mMDSL_Statement"] = None, mMDSL_ForLoop: "mMDSL_LoopStatement" = None, mMDSL_ForLoop258: set["mMDSL_BreakContinue"] = None):
        self.start = start
        self.stop = stop
        self.interval = interval
        self.mMDSL_ForLoop255 = mMDSL_ForLoop255 if mMDSL_ForLoop255 is not None else set()
        self.mMDSL_ForLoop = mMDSL_ForLoop
        self.mMDSL_ForLoop258 = mMDSL_ForLoop258 if mMDSL_ForLoop258 is not None else set()
        
    @property
    def stop(self) -> int:
        return self.__stop

    @stop.setter
    def stop(self, stop: int):
        self.__stop = stop

    @property
    def interval(self) -> int:
        return self.__interval

    @interval.setter
    def interval(self, interval: int):
        self.__interval = interval

    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start

    @property
    def mMDSL_ForLoop255(self):
        return self.__mMDSL_ForLoop255

    @mMDSL_ForLoop255.setter
    def mMDSL_ForLoop255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ForLoop__mMDSL_ForLoop255", None)
        self.__mMDSL_ForLoop255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_Statement256"):
                    opp_val = getattr(item, "mMDSL_Statement256", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_Statement256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_Statement256"):
                    opp_val = getattr(item, "mMDSL_Statement256", None)
                    
                    setattr(item, "mMDSL_Statement256", self)
                    

    @property
    def mMDSL_ForLoop(self):
        return self.__mMDSL_ForLoop

    @mMDSL_ForLoop.setter
    def mMDSL_ForLoop(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ForLoop__mMDSL_ForLoop", None)
        self.__mMDSL_ForLoop = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_LoopStatement245"):
                opp_val = getattr(old_value, "mMDSL_LoopStatement245", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_LoopStatement245", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_LoopStatement245"):
                opp_val = getattr(value, "mMDSL_LoopStatement245", None)
                setattr(value, "mMDSL_LoopStatement245", self)

    @property
    def mMDSL_ForLoop258(self):
        return self.__mMDSL_ForLoop258

    @mMDSL_ForLoop258.setter
    def mMDSL_ForLoop258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ForLoop__mMDSL_ForLoop258", None)
        self.__mMDSL_ForLoop258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_BreakContinue259"):
                    opp_val = getattr(item, "mMDSL_BreakContinue259", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_BreakContinue259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_BreakContinue259"):
                    opp_val = getattr(item, "mMDSL_BreakContinue259", None)
                    
                    setattr(item, "mMDSL_BreakContinue259", self)
                    

class mMDSL_WhileLoop:

    pass
class mMDSL_AlgorithmOperation:

    pass
class mMDSL_Variable:

    def __init__(self, name: str, mMDSL_Variable: "mMDSL_Statement" = None, mMDSL_Variable261: "mMDSL_OperatorAssign" = None, mMDSL_Variable263: "mMDSL_VarStatement" = None, mMDSL_Variable266: "mMDSL_Variable" = None, mMDSL_Variable264: "mMDSL_Variable" = None, mMDSL_Variable314: "mMDSL_Expression" = None, mMDSL_Variable482: "mMDSL_AttributeSet" = None):
        self.name = name
        self.mMDSL_Variable = mMDSL_Variable
        self.mMDSL_Variable261 = mMDSL_Variable261
        self.mMDSL_Variable263 = mMDSL_Variable263
        self.mMDSL_Variable266 = mMDSL_Variable266
        self.mMDSL_Variable264 = mMDSL_Variable264
        self.mMDSL_Variable314 = mMDSL_Variable314
        self.mMDSL_Variable482 = mMDSL_Variable482
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_Variable(self):
        return self.__mMDSL_Variable

    @mMDSL_Variable.setter
    def mMDSL_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Variable__mMDSL_Variable", None)
        self.__mMDSL_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Statement222"):
                opp_val = getattr(old_value, "mMDSL_Statement222", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Statement222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Statement222"):
                opp_val = getattr(value, "mMDSL_Statement222", None)
                setattr(value, "mMDSL_Statement222", self)

    @property
    def mMDSL_Variable263(self):
        return self.__mMDSL_Variable263

    @mMDSL_Variable263.setter
    def mMDSL_Variable263(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Variable__mMDSL_Variable263", None)
        self.__mMDSL_Variable263 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VarStatement"):
                opp_val = getattr(old_value, "mMDSL_VarStatement", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_VarStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VarStatement"):
                opp_val = getattr(value, "mMDSL_VarStatement", None)
                setattr(value, "mMDSL_VarStatement", self)

    @property
    def mMDSL_Variable482(self):
        return self.__mMDSL_Variable482

    @mMDSL_Variable482.setter
    def mMDSL_Variable482(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Variable__mMDSL_Variable482", None)
        self.__mMDSL_Variable482 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_AttributeSet481"):
                opp_val = getattr(old_value, "mMDSL_AttributeSet481", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_AttributeSet481", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_AttributeSet481"):
                opp_val = getattr(value, "mMDSL_AttributeSet481", None)
                setattr(value, "mMDSL_AttributeSet481", self)

    @property
    def mMDSL_Variable314(self):
        return self.__mMDSL_Variable314

    @mMDSL_Variable314.setter
    def mMDSL_Variable314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Variable__mMDSL_Variable314", None)
        self.__mMDSL_Variable314 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Expression313"):
                opp_val = getattr(old_value, "mMDSL_Expression313", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Expression313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Expression313"):
                opp_val = getattr(value, "mMDSL_Expression313", None)
                setattr(value, "mMDSL_Expression313", self)

    @property
    def mMDSL_Variable264(self):
        return self.__mMDSL_Variable264

    @mMDSL_Variable264.setter
    def mMDSL_Variable264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Variable__mMDSL_Variable264", None)
        self.__mMDSL_Variable264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Variable266"):
                opp_val = getattr(old_value, "mMDSL_Variable266", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Variable266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Variable266"):
                opp_val = getattr(value, "mMDSL_Variable266", None)
                setattr(value, "mMDSL_Variable266", self)

    @property
    def mMDSL_Variable266(self):
        return self.__mMDSL_Variable266

    @mMDSL_Variable266.setter
    def mMDSL_Variable266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Variable__mMDSL_Variable266", None)
        self.__mMDSL_Variable266 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Variable264"):
                opp_val = getattr(old_value, "mMDSL_Variable264", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Variable264", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Variable264"):
                opp_val = getattr(value, "mMDSL_Variable264", None)
                setattr(value, "mMDSL_Variable264", self)

    @property
    def mMDSL_Variable261(self):
        return self.__mMDSL_Variable261

    @mMDSL_Variable261.setter
    def mMDSL_Variable261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Variable__mMDSL_Variable261", None)
        self.__mMDSL_Variable261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_OperatorAssign"):
                opp_val = getattr(old_value, "mMDSL_OperatorAssign", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_OperatorAssign", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_OperatorAssign"):
                opp_val = getattr(value, "mMDSL_OperatorAssign", None)
                setattr(value, "mMDSL_OperatorAssign", self)

class mMDSL_LoopStatement:

    pass
class mMDSL_SelectionStatement:

    pass
class mMDSL_Statement:

    pass
class mMDSL_StrokeColor:

    def __init__(self, color: str, hexcolor: str, mMDSL_StrokeColor: "mMDSL_SymbolStyle" = None):
        self.color = color
        self.hexcolor = hexcolor
        self.mMDSL_StrokeColor = mMDSL_StrokeColor
        
    @property
    def hexcolor(self) -> str:
        return self.__hexcolor

    @hexcolor.setter
    def hexcolor(self, hexcolor: str):
        self.__hexcolor = hexcolor

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def mMDSL_StrokeColor(self):
        return self.__mMDSL_StrokeColor

    @mMDSL_StrokeColor.setter
    def mMDSL_StrokeColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_StrokeColor__mMDSL_StrokeColor", None)
        self.__mMDSL_StrokeColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SymbolStyle208"):
                opp_val = getattr(old_value, "mMDSL_SymbolStyle208", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SymbolStyle208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SymbolStyle208"):
                opp_val = getattr(value, "mMDSL_SymbolStyle208", None)
                setattr(value, "mMDSL_SymbolStyle208", self)

class mMDSL_PathParametersS:

    def __init__(self, x2: str, y: str, y2: str, x: str, mMDSL_PathParametersS: "mMDSL_SmoothCurveTo" = None):
        self.x2 = x2
        self.y = y
        self.y2 = y2
        self.x = x
        self.mMDSL_PathParametersS = mMDSL_PathParametersS
        
    @property
    def x2(self) -> str:
        return self.__x2

    @x2.setter
    def x2(self, x2: str):
        self.__x2 = x2

    @property
    def y2(self) -> str:
        return self.__y2

    @y2.setter
    def y2(self, y2: str):
        self.__y2 = y2

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def mMDSL_PathParametersS(self):
        return self.__mMDSL_PathParametersS

    @mMDSL_PathParametersS.setter
    def mMDSL_PathParametersS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathParametersS__mMDSL_PathParametersS", None)
        self.__mMDSL_PathParametersS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SmoothCurveTo196"):
                opp_val = getattr(old_value, "mMDSL_SmoothCurveTo196", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SmoothCurveTo196"):
                opp_val = getattr(value, "mMDSL_SmoothCurveTo196", None)
                if opp_val is None:
                    setattr(value, "mMDSL_SmoothCurveTo196", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_PathParametersA:

    def __init__(self, rx: str, ry: str, xaxisrot: str, largearcflag: str, sweepflag: str, x: str, y: str, mMDSL_PathParametersA: "mMDSL_EllipticalArc" = None):
        self.rx = rx
        self.ry = ry
        self.xaxisrot = xaxisrot
        self.largearcflag = largearcflag
        self.sweepflag = sweepflag
        self.x = x
        self.y = y
        self.mMDSL_PathParametersA = mMDSL_PathParametersA
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def largearcflag(self) -> str:
        return self.__largearcflag

    @largearcflag.setter
    def largearcflag(self, largearcflag: str):
        self.__largearcflag = largearcflag

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def xaxisrot(self) -> str:
        return self.__xaxisrot

    @xaxisrot.setter
    def xaxisrot(self, xaxisrot: str):
        self.__xaxisrot = xaxisrot

    @property
    def sweepflag(self) -> str:
        return self.__sweepflag

    @sweepflag.setter
    def sweepflag(self, sweepflag: str):
        self.__sweepflag = sweepflag

    @property
    def rx(self) -> str:
        return self.__rx

    @rx.setter
    def rx(self, rx: str):
        self.__rx = rx

    @property
    def ry(self) -> str:
        return self.__ry

    @ry.setter
    def ry(self, ry: str):
        self.__ry = ry

    @property
    def mMDSL_PathParametersA(self):
        return self.__mMDSL_PathParametersA

    @mMDSL_PathParametersA.setter
    def mMDSL_PathParametersA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathParametersA__mMDSL_PathParametersA", None)
        self.__mMDSL_PathParametersA = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_EllipticalArc203"):
                opp_val = getattr(old_value, "mMDSL_EllipticalArc203", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_EllipticalArc203"):
                opp_val = getattr(value, "mMDSL_EllipticalArc203", None)
                if opp_val is None:
                    setattr(value, "mMDSL_EllipticalArc203", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_PathParametersQ:

    def __init__(self, x1: str, y1: str, x: str, y: str, mMDSL_PathParametersQ: "mMDSL_QuadraticBezierCurve" = None):
        self.x1 = x1
        self.y1 = y1
        self.x = x
        self.y = y
        self.mMDSL_PathParametersQ = mMDSL_PathParametersQ
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def x1(self) -> str:
        return self.__x1

    @x1.setter
    def x1(self, x1: str):
        self.__x1 = x1

    @property
    def y1(self) -> str:
        return self.__y1

    @y1.setter
    def y1(self, y1: str):
        self.__y1 = y1

    @property
    def mMDSL_PathParametersQ(self):
        return self.__mMDSL_PathParametersQ

    @mMDSL_PathParametersQ.setter
    def mMDSL_PathParametersQ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathParametersQ__mMDSL_PathParametersQ", None)
        self.__mMDSL_PathParametersQ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_QuadraticBezierCurve198"):
                opp_val = getattr(old_value, "mMDSL_QuadraticBezierCurve198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_QuadraticBezierCurve198"):
                opp_val = getattr(value, "mMDSL_QuadraticBezierCurve198", None)
                if opp_val is None:
                    setattr(value, "mMDSL_QuadraticBezierCurve198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_HorizontalLineTo:

    pass
class mMDSL_LineTo:

    pass
class mMDSL_MoveTo:

    pass
class mMDSL_PathParametersC:

    def __init__(self, x1: str, y1: str, x2: str, y2: str, x: str, y: str, mMDSL_PathParametersC: "mMDSL_CurveTo" = None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x = x
        self.y = y
        self.mMDSL_PathParametersC = mMDSL_PathParametersC
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def y2(self) -> str:
        return self.__y2

    @y2.setter
    def y2(self, y2: str):
        self.__y2 = y2

    @property
    def x1(self) -> str:
        return self.__x1

    @x1.setter
    def x1(self, x1: str):
        self.__x1 = x1

    @property
    def x2(self) -> str:
        return self.__x2

    @x2.setter
    def x2(self, x2: str):
        self.__x2 = x2

    @property
    def y1(self) -> str:
        return self.__y1

    @y1.setter
    def y1(self, y1: str):
        self.__y1 = y1

    @property
    def mMDSL_PathParametersC(self):
        return self.__mMDSL_PathParametersC

    @mMDSL_PathParametersC.setter
    def mMDSL_PathParametersC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathParametersC__mMDSL_PathParametersC", None)
        self.__mMDSL_PathParametersC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_CurveTo194"):
                opp_val = getattr(old_value, "mMDSL_CurveTo194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_CurveTo194"):
                opp_val = getattr(value, "mMDSL_CurveTo194", None)
                if opp_val is None:
                    setattr(value, "mMDSL_CurveTo194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_PathParametersHV:

    def __init__(self, x: str, mMDSL_PathParametersHV: "mMDSL_HorizontalLineTo" = None, mMDSL_PathParametersHV192: "mMDSL_VerticalLineTo" = None):
        self.x = x
        self.mMDSL_PathParametersHV = mMDSL_PathParametersHV
        self.mMDSL_PathParametersHV192 = mMDSL_PathParametersHV192
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def mMDSL_PathParametersHV(self):
        return self.__mMDSL_PathParametersHV

    @mMDSL_PathParametersHV.setter
    def mMDSL_PathParametersHV(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathParametersHV__mMDSL_PathParametersHV", None)
        self.__mMDSL_PathParametersHV = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_HorizontalLineTo189"):
                opp_val = getattr(old_value, "mMDSL_HorizontalLineTo189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_HorizontalLineTo189"):
                opp_val = getattr(value, "mMDSL_HorizontalLineTo189", None)
                if opp_val is None:
                    setattr(value, "mMDSL_HorizontalLineTo189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_PathParametersHV192(self):
        return self.__mMDSL_PathParametersHV192

    @mMDSL_PathParametersHV192.setter
    def mMDSL_PathParametersHV192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathParametersHV__mMDSL_PathParametersHV192", None)
        self.__mMDSL_PathParametersHV192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VerticalLineTo191"):
                opp_val = getattr(old_value, "mMDSL_VerticalLineTo191", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VerticalLineTo191"):
                opp_val = getattr(value, "mMDSL_VerticalLineTo191", None)
                if opp_val is None:
                    setattr(value, "mMDSL_VerticalLineTo191", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_PathParametersMLT:

    def __init__(self, x: str, y: str, mMDSL_PathParametersMLT: "mMDSL_MoveTo" = None, mMDSL_PathParametersMLT187: "mMDSL_LineTo" = None, mMDSL_PathParametersMLT201: "mMDSL_SmoothQuadraticBezierCurveTo" = None):
        self.x = x
        self.y = y
        self.mMDSL_PathParametersMLT = mMDSL_PathParametersMLT
        self.mMDSL_PathParametersMLT187 = mMDSL_PathParametersMLT187
        self.mMDSL_PathParametersMLT201 = mMDSL_PathParametersMLT201
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def mMDSL_PathParametersMLT201(self):
        return self.__mMDSL_PathParametersMLT201

    @mMDSL_PathParametersMLT201.setter
    def mMDSL_PathParametersMLT201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathParametersMLT__mMDSL_PathParametersMLT201", None)
        self.__mMDSL_PathParametersMLT201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SmoothQuadraticBezierCurveTo200"):
                opp_val = getattr(old_value, "mMDSL_SmoothQuadraticBezierCurveTo200", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SmoothQuadraticBezierCurveTo200"):
                opp_val = getattr(value, "mMDSL_SmoothQuadraticBezierCurveTo200", None)
                if opp_val is None:
                    setattr(value, "mMDSL_SmoothQuadraticBezierCurveTo200", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_PathParametersMLT(self):
        return self.__mMDSL_PathParametersMLT

    @mMDSL_PathParametersMLT.setter
    def mMDSL_PathParametersMLT(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathParametersMLT__mMDSL_PathParametersMLT", None)
        self.__mMDSL_PathParametersMLT = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_MoveTo184"):
                opp_val = getattr(old_value, "mMDSL_MoveTo184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_MoveTo184"):
                opp_val = getattr(value, "mMDSL_MoveTo184", None)
                if opp_val is None:
                    setattr(value, "mMDSL_MoveTo184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_PathParametersMLT187(self):
        return self.__mMDSL_PathParametersMLT187

    @mMDSL_PathParametersMLT187.setter
    def mMDSL_PathParametersMLT187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathParametersMLT__mMDSL_PathParametersMLT187", None)
        self.__mMDSL_PathParametersMLT187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_LineTo186"):
                opp_val = getattr(old_value, "mMDSL_LineTo186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_LineTo186"):
                opp_val = getattr(value, "mMDSL_LineTo186", None)
                if opp_val is None:
                    setattr(value, "mMDSL_LineTo186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_EllipticalArc:

    pass
class mMDSL_SmoothQuadraticBezierCurveTo:

    pass
class mMDSL_QuadraticBezierCurve:

    pass
class mMDSL_SmoothCurveTo:

    pass
class mMDSL_CurveTo:

    pass
class mMDSL_VerticalLineTo:

    pass
class mMDSL_FillColor:

    def __init__(self, color: str, hexcolor: str, mMDSL_FillColor: "mMDSL_Text" = None, mMDSL_FillColor206: "mMDSL_SymbolStyle" = None):
        self.color = color
        self.hexcolor = hexcolor
        self.mMDSL_FillColor = mMDSL_FillColor
        self.mMDSL_FillColor206 = mMDSL_FillColor206
        
    @property
    def hexcolor(self) -> str:
        return self.__hexcolor

    @hexcolor.setter
    def hexcolor(self, hexcolor: str):
        self.__hexcolor = hexcolor

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def mMDSL_FillColor(self):
        return self.__mMDSL_FillColor

    @mMDSL_FillColor.setter
    def mMDSL_FillColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_FillColor__mMDSL_FillColor", None)
        self.__mMDSL_FillColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Text164"):
                opp_val = getattr(old_value, "mMDSL_Text164", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Text164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Text164"):
                opp_val = getattr(value, "mMDSL_Text164", None)
                setattr(value, "mMDSL_Text164", self)

    @property
    def mMDSL_FillColor206(self):
        return self.__mMDSL_FillColor206

    @mMDSL_FillColor206.setter
    def mMDSL_FillColor206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_FillColor__mMDSL_FillColor206", None)
        self.__mMDSL_FillColor206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SymbolStyle205"):
                opp_val = getattr(old_value, "mMDSL_SymbolStyle205", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SymbolStyle205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SymbolStyle205"):
                opp_val = getattr(value, "mMDSL_SymbolStyle205", None)
                setattr(value, "mMDSL_SymbolStyle205", self)

class mMDSL_FontFamily:

    def __init__(self, fontstr: str, font: str, mMDSL_FontFamily: "mMDSL_Text" = None, mMDSL_FontFamily211: "mMDSL_SymbolStyle" = None):
        self.fontstr = fontstr
        self.font = font
        self.mMDSL_FontFamily = mMDSL_FontFamily
        self.mMDSL_FontFamily211 = mMDSL_FontFamily211
        
    @property
    def fontstr(self) -> str:
        return self.__fontstr

    @fontstr.setter
    def fontstr(self, fontstr: str):
        self.__fontstr = fontstr

    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font

    @property
    def mMDSL_FontFamily211(self):
        return self.__mMDSL_FontFamily211

    @mMDSL_FontFamily211.setter
    def mMDSL_FontFamily211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_FontFamily__mMDSL_FontFamily211", None)
        self.__mMDSL_FontFamily211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SymbolStyle210"):
                opp_val = getattr(old_value, "mMDSL_SymbolStyle210", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SymbolStyle210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SymbolStyle210"):
                opp_val = getattr(value, "mMDSL_SymbolStyle210", None)
                setattr(value, "mMDSL_SymbolStyle210", self)

    @property
    def mMDSL_FontFamily(self):
        return self.__mMDSL_FontFamily

    @mMDSL_FontFamily.setter
    def mMDSL_FontFamily(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_FontFamily__mMDSL_FontFamily", None)
        self.__mMDSL_FontFamily = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Text162"):
                opp_val = getattr(old_value, "mMDSL_Text162", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Text162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Text162"):
                opp_val = getattr(value, "mMDSL_Text162", None)
                setattr(value, "mMDSL_Text162", self)

class mMDSL_PathData:

    def __init__(self, closepath: str, mMDSL_PathData: "mMDSL_Path" = None, mMDSL_PathData172: "mMDSL_VerticalLineTo" = None, mMDSL_PathData174: "mMDSL_CurveTo" = None, mMDSL_PathData176: "mMDSL_SmoothCurveTo" = None, mMDSL_PathData178: "mMDSL_QuadraticBezierCurve" = None, mMDSL_PathData180: "mMDSL_SmoothQuadraticBezierCurveTo" = None, mMDSL_PathData182: "mMDSL_EllipticalArc" = None, mMDSL_PathData166: "mMDSL_MoveTo" = None, mMDSL_PathData168: "mMDSL_LineTo" = None, mMDSL_PathData170: "mMDSL_HorizontalLineTo" = None):
        self.closepath = closepath
        self.mMDSL_PathData = mMDSL_PathData
        self.mMDSL_PathData172 = mMDSL_PathData172
        self.mMDSL_PathData174 = mMDSL_PathData174
        self.mMDSL_PathData176 = mMDSL_PathData176
        self.mMDSL_PathData178 = mMDSL_PathData178
        self.mMDSL_PathData180 = mMDSL_PathData180
        self.mMDSL_PathData182 = mMDSL_PathData182
        self.mMDSL_PathData166 = mMDSL_PathData166
        self.mMDSL_PathData168 = mMDSL_PathData168
        self.mMDSL_PathData170 = mMDSL_PathData170
        
    @property
    def closepath(self) -> str:
        return self.__closepath

    @closepath.setter
    def closepath(self, closepath: str):
        self.__closepath = closepath

    @property
    def mMDSL_PathData166(self):
        return self.__mMDSL_PathData166

    @mMDSL_PathData166.setter
    def mMDSL_PathData166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathData__mMDSL_PathData166", None)
        self.__mMDSL_PathData166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_MoveTo"):
                opp_val = getattr(old_value, "mMDSL_MoveTo", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_MoveTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_MoveTo"):
                opp_val = getattr(value, "mMDSL_MoveTo", None)
                setattr(value, "mMDSL_MoveTo", self)

    @property
    def mMDSL_PathData180(self):
        return self.__mMDSL_PathData180

    @mMDSL_PathData180.setter
    def mMDSL_PathData180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathData__mMDSL_PathData180", None)
        self.__mMDSL_PathData180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SmoothQuadraticBezierCurveTo"):
                opp_val = getattr(old_value, "mMDSL_SmoothQuadraticBezierCurveTo", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SmoothQuadraticBezierCurveTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SmoothQuadraticBezierCurveTo"):
                opp_val = getattr(value, "mMDSL_SmoothQuadraticBezierCurveTo", None)
                setattr(value, "mMDSL_SmoothQuadraticBezierCurveTo", self)

    @property
    def mMDSL_PathData168(self):
        return self.__mMDSL_PathData168

    @mMDSL_PathData168.setter
    def mMDSL_PathData168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathData__mMDSL_PathData168", None)
        self.__mMDSL_PathData168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_LineTo"):
                opp_val = getattr(old_value, "mMDSL_LineTo", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_LineTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_LineTo"):
                opp_val = getattr(value, "mMDSL_LineTo", None)
                setattr(value, "mMDSL_LineTo", self)

    @property
    def mMDSL_PathData182(self):
        return self.__mMDSL_PathData182

    @mMDSL_PathData182.setter
    def mMDSL_PathData182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathData__mMDSL_PathData182", None)
        self.__mMDSL_PathData182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_EllipticalArc"):
                opp_val = getattr(old_value, "mMDSL_EllipticalArc", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_EllipticalArc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_EllipticalArc"):
                opp_val = getattr(value, "mMDSL_EllipticalArc", None)
                setattr(value, "mMDSL_EllipticalArc", self)

    @property
    def mMDSL_PathData174(self):
        return self.__mMDSL_PathData174

    @mMDSL_PathData174.setter
    def mMDSL_PathData174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathData__mMDSL_PathData174", None)
        self.__mMDSL_PathData174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_CurveTo"):
                opp_val = getattr(old_value, "mMDSL_CurveTo", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_CurveTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_CurveTo"):
                opp_val = getattr(value, "mMDSL_CurveTo", None)
                setattr(value, "mMDSL_CurveTo", self)

    @property
    def mMDSL_PathData170(self):
        return self.__mMDSL_PathData170

    @mMDSL_PathData170.setter
    def mMDSL_PathData170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathData__mMDSL_PathData170", None)
        self.__mMDSL_PathData170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_HorizontalLineTo"):
                opp_val = getattr(old_value, "mMDSL_HorizontalLineTo", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_HorizontalLineTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_HorizontalLineTo"):
                opp_val = getattr(value, "mMDSL_HorizontalLineTo", None)
                setattr(value, "mMDSL_HorizontalLineTo", self)

    @property
    def mMDSL_PathData172(self):
        return self.__mMDSL_PathData172

    @mMDSL_PathData172.setter
    def mMDSL_PathData172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathData__mMDSL_PathData172", None)
        self.__mMDSL_PathData172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VerticalLineTo"):
                opp_val = getattr(old_value, "mMDSL_VerticalLineTo", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_VerticalLineTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VerticalLineTo"):
                opp_val = getattr(value, "mMDSL_VerticalLineTo", None)
                setattr(value, "mMDSL_VerticalLineTo", self)

    @property
    def mMDSL_PathData176(self):
        return self.__mMDSL_PathData176

    @mMDSL_PathData176.setter
    def mMDSL_PathData176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathData__mMDSL_PathData176", None)
        self.__mMDSL_PathData176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SmoothCurveTo"):
                opp_val = getattr(old_value, "mMDSL_SmoothCurveTo", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SmoothCurveTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SmoothCurveTo"):
                opp_val = getattr(value, "mMDSL_SmoothCurveTo", None)
                setattr(value, "mMDSL_SmoothCurveTo", self)

    @property
    def mMDSL_PathData(self):
        return self.__mMDSL_PathData

    @mMDSL_PathData.setter
    def mMDSL_PathData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathData__mMDSL_PathData", None)
        self.__mMDSL_PathData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Path160"):
                opp_val = getattr(old_value, "mMDSL_Path160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Path160"):
                opp_val = getattr(value, "mMDSL_Path160", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Path160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_PathData178(self):
        return self.__mMDSL_PathData178

    @mMDSL_PathData178.setter
    def mMDSL_PathData178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_PathData__mMDSL_PathData178", None)
        self.__mMDSL_PathData178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_QuadraticBezierCurve"):
                opp_val = getattr(old_value, "mMDSL_QuadraticBezierCurve", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_QuadraticBezierCurve", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_QuadraticBezierCurve"):
                opp_val = getattr(value, "mMDSL_QuadraticBezierCurve", None)
                setattr(value, "mMDSL_QuadraticBezierCurve", self)

class mMDSL_Points:

    def __init__(self, x: str, y: str, mMDSL_Points: "mMDSL_Polyline" = None, mMDSL_Points158: "mMDSL_Polygon" = None):
        self.x = x
        self.y = y
        self.mMDSL_Points = mMDSL_Points
        self.mMDSL_Points158 = mMDSL_Points158
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def mMDSL_Points(self):
        return self.__mMDSL_Points

    @mMDSL_Points.setter
    def mMDSL_Points(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Points__mMDSL_Points", None)
        self.__mMDSL_Points = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Polyline155"):
                opp_val = getattr(old_value, "mMDSL_Polyline155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Polyline155"):
                opp_val = getattr(value, "mMDSL_Polyline155", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Polyline155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Points158(self):
        return self.__mMDSL_Points158

    @mMDSL_Points158.setter
    def mMDSL_Points158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Points__mMDSL_Points158", None)
        self.__mMDSL_Points158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Polygon157"):
                opp_val = getattr(old_value, "mMDSL_Polygon157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Polygon157"):
                opp_val = getattr(value, "mMDSL_Polygon157", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Polygon157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_Text:

    def __init__(self, value: str, x: str, y: str, fontsize: str, mMDSL_Text: "mMDSL_SVGCommand" = None, mMDSL_Text162: "mMDSL_FontFamily" = None, mMDSL_Text164: "mMDSL_FillColor" = None):
        self.value = value
        self.x = x
        self.y = y
        self.fontsize = fontsize
        self.mMDSL_Text = mMDSL_Text
        self.mMDSL_Text162 = mMDSL_Text162
        self.mMDSL_Text164 = mMDSL_Text164
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def fontsize(self) -> str:
        return self.__fontsize

    @fontsize.setter
    def fontsize(self, fontsize: str):
        self.__fontsize = fontsize

    @property
    def mMDSL_Text(self):
        return self.__mMDSL_Text

    @mMDSL_Text.setter
    def mMDSL_Text(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Text__mMDSL_Text", None)
        self.__mMDSL_Text = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SVGCommand147"):
                opp_val = getattr(old_value, "mMDSL_SVGCommand147", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SVGCommand147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SVGCommand147"):
                opp_val = getattr(value, "mMDSL_SVGCommand147", None)
                setattr(value, "mMDSL_SVGCommand147", self)

    @property
    def mMDSL_Text164(self):
        return self.__mMDSL_Text164

    @mMDSL_Text164.setter
    def mMDSL_Text164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Text__mMDSL_Text164", None)
        self.__mMDSL_Text164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_FillColor"):
                opp_val = getattr(old_value, "mMDSL_FillColor", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_FillColor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_FillColor"):
                opp_val = getattr(value, "mMDSL_FillColor", None)
                setattr(value, "mMDSL_FillColor", self)

    @property
    def mMDSL_Text162(self):
        return self.__mMDSL_Text162

    @mMDSL_Text162.setter
    def mMDSL_Text162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Text__mMDSL_Text162", None)
        self.__mMDSL_Text162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_FontFamily"):
                opp_val = getattr(old_value, "mMDSL_FontFamily", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_FontFamily", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_FontFamily"):
                opp_val = getattr(value, "mMDSL_FontFamily", None)
                setattr(value, "mMDSL_FontFamily", self)

class mMDSL_Path:

    pass
class mMDSL_Polygon:

    pass
class mMDSL_Polyline:

    pass
class mMDSL_Line:

    def __init__(self, x1: str, y1: str, x2: str, y2: str, mMDSL_Line: "mMDSL_SVGCommand" = None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.mMDSL_Line = mMDSL_Line
        
    @property
    def x2(self) -> str:
        return self.__x2

    @x2.setter
    def x2(self, x2: str):
        self.__x2 = x2

    @property
    def y1(self) -> str:
        return self.__y1

    @y1.setter
    def y1(self, y1: str):
        self.__y1 = y1

    @property
    def x1(self) -> str:
        return self.__x1

    @x1.setter
    def x1(self, x1: str):
        self.__x1 = x1

    @property
    def y2(self) -> str:
        return self.__y2

    @y2.setter
    def y2(self, y2: str):
        self.__y2 = y2

    @property
    def mMDSL_Line(self):
        return self.__mMDSL_Line

    @mMDSL_Line.setter
    def mMDSL_Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Line__mMDSL_Line", None)
        self.__mMDSL_Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SVGCommand139"):
                opp_val = getattr(old_value, "mMDSL_SVGCommand139", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SVGCommand139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SVGCommand139"):
                opp_val = getattr(value, "mMDSL_SVGCommand139", None)
                setattr(value, "mMDSL_SVGCommand139", self)

class mMDSL_Ellipse:

    def __init__(self, cx: str, cy: str, rx: str, ry: str, mMDSL_Ellipse: "mMDSL_SVGCommand" = None):
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
        self.mMDSL_Ellipse = mMDSL_Ellipse
        
    @property
    def rx(self) -> str:
        return self.__rx

    @rx.setter
    def rx(self, rx: str):
        self.__rx = rx

    @property
    def ry(self) -> str:
        return self.__ry

    @ry.setter
    def ry(self, ry: str):
        self.__ry = ry

    @property
    def cx(self) -> str:
        return self.__cx

    @cx.setter
    def cx(self, cx: str):
        self.__cx = cx

    @property
    def cy(self) -> str:
        return self.__cy

    @cy.setter
    def cy(self, cy: str):
        self.__cy = cy

    @property
    def mMDSL_Ellipse(self):
        return self.__mMDSL_Ellipse

    @mMDSL_Ellipse.setter
    def mMDSL_Ellipse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Ellipse__mMDSL_Ellipse", None)
        self.__mMDSL_Ellipse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SVGCommand137"):
                opp_val = getattr(old_value, "mMDSL_SVGCommand137", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SVGCommand137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SVGCommand137"):
                opp_val = getattr(value, "mMDSL_SVGCommand137", None)
                setattr(value, "mMDSL_SVGCommand137", self)

class mMDSL_Circle:

    def __init__(self, cx: str, cy: str, r: str, mMDSL_Circle: "mMDSL_SVGCommand" = None):
        self.cx = cx
        self.cy = cy
        self.r = r
        self.mMDSL_Circle = mMDSL_Circle
        
    @property
    def cy(self) -> str:
        return self.__cy

    @cy.setter
    def cy(self, cy: str):
        self.__cy = cy

    @property
    def r(self) -> str:
        return self.__r

    @r.setter
    def r(self, r: str):
        self.__r = r

    @property
    def cx(self) -> str:
        return self.__cx

    @cx.setter
    def cx(self, cx: str):
        self.__cx = cx

    @property
    def mMDSL_Circle(self):
        return self.__mMDSL_Circle

    @mMDSL_Circle.setter
    def mMDSL_Circle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Circle__mMDSL_Circle", None)
        self.__mMDSL_Circle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SVGCommand135"):
                opp_val = getattr(old_value, "mMDSL_SVGCommand135", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SVGCommand135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SVGCommand135"):
                opp_val = getattr(value, "mMDSL_SVGCommand135", None)
                setattr(value, "mMDSL_SVGCommand135", self)

class mMDSL_Rectangle:

    def __init__(self, x: str, y: str, width: str, height: str, mMDSL_Rectangle: "mMDSL_SVGCommand" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.mMDSL_Rectangle = mMDSL_Rectangle
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def mMDSL_Rectangle(self):
        return self.__mMDSL_Rectangle

    @mMDSL_Rectangle.setter
    def mMDSL_Rectangle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Rectangle__mMDSL_Rectangle", None)
        self.__mMDSL_Rectangle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SVGCommand133"):
                opp_val = getattr(old_value, "mMDSL_SVGCommand133", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SVGCommand133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SVGCommand133"):
                opp_val = getattr(value, "mMDSL_SVGCommand133", None)
                setattr(value, "mMDSL_SVGCommand133", self)

class mMDSL_SVGCommand:

    pass
class mMDSL_Mode:

    def __init__(self, name: str, mMDSL_Mode: "mMDSL_ModelType" = None, mMDSL_Mode107: set["mMDSL_Class"] = None, mMDSL_Mode110: set["mMDSL_Relation"] = None):
        self.name = name
        self.mMDSL_Mode = mMDSL_Mode
        self.mMDSL_Mode107 = mMDSL_Mode107 if mMDSL_Mode107 is not None else set()
        self.mMDSL_Mode110 = mMDSL_Mode110 if mMDSL_Mode110 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_Mode107(self):
        return self.__mMDSL_Mode107

    @mMDSL_Mode107.setter
    def mMDSL_Mode107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Mode__mMDSL_Mode107", None)
        self.__mMDSL_Mode107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_Class108"):
                    opp_val = getattr(item, "mMDSL_Class108", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_Class108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_Class108"):
                    opp_val = getattr(item, "mMDSL_Class108", None)
                    
                    setattr(item, "mMDSL_Class108", self)
                    

    @property
    def mMDSL_Mode(self):
        return self.__mMDSL_Mode

    @mMDSL_Mode.setter
    def mMDSL_Mode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Mode__mMDSL_Mode", None)
        self.__mMDSL_Mode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelType105"):
                opp_val = getattr(old_value, "mMDSL_ModelType105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelType105"):
                opp_val = getattr(value, "mMDSL_ModelType105", None)
                if opp_val is None:
                    setattr(value, "mMDSL_ModelType105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Mode110(self):
        return self.__mMDSL_Mode110

    @mMDSL_Mode110.setter
    def mMDSL_Mode110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Mode__mMDSL_Mode110", None)
        self.__mMDSL_Mode110 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_Relation111"):
                    opp_val = getattr(item, "mMDSL_Relation111", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_Relation111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_Relation111"):
                    opp_val = getattr(item, "mMDSL_Relation111", None)
                    
                    setattr(item, "mMDSL_Relation111", self)
                    

class mMDSL_EnumType:

    pass
class mMDSL_ClassAttribute:

    def __init__(self, name: str, mMDSL_ClassAttribute83: "mMDSL_Type" = None, mMDSL_ClassAttribute: "mMDSL_Class" = None):
        self.name = name
        self.mMDSL_ClassAttribute83 = mMDSL_ClassAttribute83
        self.mMDSL_ClassAttribute = mMDSL_ClassAttribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_ClassAttribute(self):
        return self.__mMDSL_ClassAttribute

    @mMDSL_ClassAttribute.setter
    def mMDSL_ClassAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ClassAttribute__mMDSL_ClassAttribute", None)
        self.__mMDSL_ClassAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Class53"):
                opp_val = getattr(old_value, "mMDSL_Class53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Class53"):
                opp_val = getattr(value, "mMDSL_Class53", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Class53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_ClassAttribute83(self):
        return self.__mMDSL_ClassAttribute83

    @mMDSL_ClassAttribute83.setter
    def mMDSL_ClassAttribute83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ClassAttribute__mMDSL_ClassAttribute83", None)
        self.__mMDSL_ClassAttribute83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Type84"):
                opp_val = getattr(old_value, "mMDSL_Type84", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Type84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Type84"):
                opp_val = getattr(value, "mMDSL_Type84", None)
                setattr(value, "mMDSL_Type84", self)

class mMDSL_RefName:

    pass
class mMDSL_Type:

    def __init__(self, simpletype: str, mMDSL_Type: "mMDSL_Attribute" = None, mMDSL_Type84: "mMDSL_ClassAttribute" = None, mMDSL_Type94: "mMDSL_EnumType" = None):
        self.simpletype = simpletype
        self.mMDSL_Type = mMDSL_Type
        self.mMDSL_Type84 = mMDSL_Type84
        self.mMDSL_Type94 = mMDSL_Type94
        
    @property
    def simpletype(self) -> str:
        return self.__simpletype

    @simpletype.setter
    def simpletype(self, simpletype: str):
        self.__simpletype = simpletype

    @property
    def mMDSL_Type94(self):
        return self.__mMDSL_Type94

    @mMDSL_Type94.setter
    def mMDSL_Type94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Type__mMDSL_Type94", None)
        self.__mMDSL_Type94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_EnumType"):
                opp_val = getattr(old_value, "mMDSL_EnumType", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_EnumType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_EnumType"):
                opp_val = getattr(value, "mMDSL_EnumType", None)
                setattr(value, "mMDSL_EnumType", self)

    @property
    def mMDSL_Type(self):
        return self.__mMDSL_Type

    @mMDSL_Type.setter
    def mMDSL_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Type__mMDSL_Type", None)
        self.__mMDSL_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Attribute81"):
                opp_val = getattr(old_value, "mMDSL_Attribute81", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Attribute81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Attribute81"):
                opp_val = getattr(value, "mMDSL_Attribute81", None)
                setattr(value, "mMDSL_Attribute81", self)

    @property
    def mMDSL_Type84(self):
        return self.__mMDSL_Type84

    @mMDSL_Type84.setter
    def mMDSL_Type84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Type__mMDSL_Type84", None)
        self.__mMDSL_Type84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ClassAttribute83"):
                opp_val = getattr(old_value, "mMDSL_ClassAttribute83", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ClassAttribute83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ClassAttribute83"):
                opp_val = getattr(value, "mMDSL_ClassAttribute83", None)
                setattr(value, "mMDSL_ClassAttribute83", self)

class mMDSL_Reference:

    def __init__(self, name: str, mMDSL_Reference: "mMDSL_Class" = None, mMDSL_Reference86: "mMDSL_RefName" = None, mMDSL_Reference281: "mMDSL_VarStatement" = None):
        self.name = name
        self.mMDSL_Reference = mMDSL_Reference
        self.mMDSL_Reference86 = mMDSL_Reference86
        self.mMDSL_Reference281 = mMDSL_Reference281
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_Reference86(self):
        return self.__mMDSL_Reference86

    @mMDSL_Reference86.setter
    def mMDSL_Reference86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Reference__mMDSL_Reference86", None)
        self.__mMDSL_Reference86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RefName"):
                opp_val = getattr(old_value, "mMDSL_RefName", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RefName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RefName"):
                opp_val = getattr(value, "mMDSL_RefName", None)
                setattr(value, "mMDSL_RefName", self)

    @property
    def mMDSL_Reference281(self):
        return self.__mMDSL_Reference281

    @mMDSL_Reference281.setter
    def mMDSL_Reference281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Reference__mMDSL_Reference281", None)
        self.__mMDSL_Reference281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VarStatement280"):
                opp_val = getattr(old_value, "mMDSL_VarStatement280", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_VarStatement280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VarStatement280"):
                opp_val = getattr(value, "mMDSL_VarStatement280", None)
                setattr(value, "mMDSL_VarStatement280", self)

    @property
    def mMDSL_Reference(self):
        return self.__mMDSL_Reference

    @mMDSL_Reference.setter
    def mMDSL_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Reference__mMDSL_Reference", None)
        self.__mMDSL_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Class61"):
                opp_val = getattr(old_value, "mMDSL_Class61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Class61"):
                opp_val = getattr(value, "mMDSL_Class61", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Class61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_ModelType:

    def __init__(self, name: str, mMDSL_ModelType: "mMDSL_Metamodel" = None, mMDSL_ModelType99: set["mMDSL_Class"] = None, mMDSL_ModelType102: set["mMDSL_Relation"] = None, mMDSL_ModelType105: set["mMDSL_Mode"] = None, mMDSL_ModelType89: "mMDSL_RefName" = None, mMDSL_ModelType296: "mMDSL_VarStatement" = None, mMDSL_ModelType397: "mMDSL_ModelCreate" = None):
        self.name = name
        self.mMDSL_ModelType = mMDSL_ModelType
        self.mMDSL_ModelType99 = mMDSL_ModelType99 if mMDSL_ModelType99 is not None else set()
        self.mMDSL_ModelType102 = mMDSL_ModelType102 if mMDSL_ModelType102 is not None else set()
        self.mMDSL_ModelType105 = mMDSL_ModelType105 if mMDSL_ModelType105 is not None else set()
        self.mMDSL_ModelType89 = mMDSL_ModelType89
        self.mMDSL_ModelType296 = mMDSL_ModelType296
        self.mMDSL_ModelType397 = mMDSL_ModelType397
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_ModelType102(self):
        return self.__mMDSL_ModelType102

    @mMDSL_ModelType102.setter
    def mMDSL_ModelType102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelType__mMDSL_ModelType102", None)
        self.__mMDSL_ModelType102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_Relation103"):
                    opp_val = getattr(item, "mMDSL_Relation103", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_Relation103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_Relation103"):
                    opp_val = getattr(item, "mMDSL_Relation103", None)
                    
                    setattr(item, "mMDSL_Relation103", self)
                    

    @property
    def mMDSL_ModelType(self):
        return self.__mMDSL_ModelType

    @mMDSL_ModelType.setter
    def mMDSL_ModelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelType__mMDSL_ModelType", None)
        self.__mMDSL_ModelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Metamodel45"):
                opp_val = getattr(old_value, "mMDSL_Metamodel45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Metamodel45"):
                opp_val = getattr(value, "mMDSL_Metamodel45", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Metamodel45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_ModelType99(self):
        return self.__mMDSL_ModelType99

    @mMDSL_ModelType99.setter
    def mMDSL_ModelType99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelType__mMDSL_ModelType99", None)
        self.__mMDSL_ModelType99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_Class100"):
                    opp_val = getattr(item, "mMDSL_Class100", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_Class100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_Class100"):
                    opp_val = getattr(item, "mMDSL_Class100", None)
                    
                    setattr(item, "mMDSL_Class100", self)
                    

    @property
    def mMDSL_ModelType105(self):
        return self.__mMDSL_ModelType105

    @mMDSL_ModelType105.setter
    def mMDSL_ModelType105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelType__mMDSL_ModelType105", None)
        self.__mMDSL_ModelType105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_Mode"):
                    opp_val = getattr(item, "mMDSL_Mode", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_Mode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_Mode"):
                    opp_val = getattr(item, "mMDSL_Mode", None)
                    
                    setattr(item, "mMDSL_Mode", self)
                    

    @property
    def mMDSL_ModelType296(self):
        return self.__mMDSL_ModelType296

    @mMDSL_ModelType296.setter
    def mMDSL_ModelType296(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelType__mMDSL_ModelType296", None)
        self.__mMDSL_ModelType296 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VarStatement295"):
                opp_val = getattr(old_value, "mMDSL_VarStatement295", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_VarStatement295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VarStatement295"):
                opp_val = getattr(value, "mMDSL_VarStatement295", None)
                setattr(value, "mMDSL_VarStatement295", self)

    @property
    def mMDSL_ModelType89(self):
        return self.__mMDSL_ModelType89

    @mMDSL_ModelType89.setter
    def mMDSL_ModelType89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelType__mMDSL_ModelType89", None)
        self.__mMDSL_ModelType89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RefName88"):
                opp_val = getattr(old_value, "mMDSL_RefName88", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RefName88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RefName88"):
                opp_val = getattr(value, "mMDSL_RefName88", None)
                setattr(value, "mMDSL_RefName88", self)

    @property
    def mMDSL_ModelType397(self):
        return self.__mMDSL_ModelType397

    @mMDSL_ModelType397.setter
    def mMDSL_ModelType397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_ModelType__mMDSL_ModelType397", None)
        self.__mMDSL_ModelType397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelCreate396"):
                opp_val = getattr(old_value, "mMDSL_ModelCreate396", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ModelCreate396", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelCreate396"):
                opp_val = getattr(value, "mMDSL_ModelCreate396", None)
                setattr(value, "mMDSL_ModelCreate396", self)

class mMDSL_Attribute:

    def __init__(self, name: str, access: str, mMDSL_Attribute: "mMDSL_Metamodel" = None, mMDSL_Attribute76: "mMDSL_Relation" = None, mMDSL_Attribute81: "mMDSL_Type" = None, mMDSL_Attribute56: "mMDSL_Class" = None, mMDSL_Attribute278: "mMDSL_VarStatement" = None, mMDSL_Attribute475: "mMDSL_AttributeOperation" = None):
        self.name = name
        self.access = access
        self.mMDSL_Attribute = mMDSL_Attribute
        self.mMDSL_Attribute76 = mMDSL_Attribute76
        self.mMDSL_Attribute81 = mMDSL_Attribute81
        self.mMDSL_Attribute56 = mMDSL_Attribute56
        self.mMDSL_Attribute278 = mMDSL_Attribute278
        self.mMDSL_Attribute475 = mMDSL_Attribute475
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def access(self) -> str:
        return self.__access

    @access.setter
    def access(self, access: str):
        self.__access = access

    @property
    def mMDSL_Attribute278(self):
        return self.__mMDSL_Attribute278

    @mMDSL_Attribute278.setter
    def mMDSL_Attribute278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Attribute__mMDSL_Attribute278", None)
        self.__mMDSL_Attribute278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VarStatement277"):
                opp_val = getattr(old_value, "mMDSL_VarStatement277", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_VarStatement277", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VarStatement277"):
                opp_val = getattr(value, "mMDSL_VarStatement277", None)
                setattr(value, "mMDSL_VarStatement277", self)

    @property
    def mMDSL_Attribute56(self):
        return self.__mMDSL_Attribute56

    @mMDSL_Attribute56.setter
    def mMDSL_Attribute56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Attribute__mMDSL_Attribute56", None)
        self.__mMDSL_Attribute56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Class55"):
                opp_val = getattr(old_value, "mMDSL_Class55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Class55"):
                opp_val = getattr(value, "mMDSL_Class55", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Class55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Attribute(self):
        return self.__mMDSL_Attribute

    @mMDSL_Attribute.setter
    def mMDSL_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Attribute__mMDSL_Attribute", None)
        self.__mMDSL_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Metamodel43"):
                opp_val = getattr(old_value, "mMDSL_Metamodel43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Metamodel43"):
                opp_val = getattr(value, "mMDSL_Metamodel43", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Metamodel43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Attribute475(self):
        return self.__mMDSL_Attribute475

    @mMDSL_Attribute475.setter
    def mMDSL_Attribute475(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Attribute__mMDSL_Attribute475", None)
        self.__mMDSL_Attribute475 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_AttributeOperation474"):
                opp_val = getattr(old_value, "mMDSL_AttributeOperation474", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_AttributeOperation474", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_AttributeOperation474"):
                opp_val = getattr(value, "mMDSL_AttributeOperation474", None)
                setattr(value, "mMDSL_AttributeOperation474", self)

    @property
    def mMDSL_Attribute76(self):
        return self.__mMDSL_Attribute76

    @mMDSL_Attribute76.setter
    def mMDSL_Attribute76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Attribute__mMDSL_Attribute76", None)
        self.__mMDSL_Attribute76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Relation75"):
                opp_val = getattr(old_value, "mMDSL_Relation75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Relation75"):
                opp_val = getattr(value, "mMDSL_Relation75", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Relation75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Attribute81(self):
        return self.__mMDSL_Attribute81

    @mMDSL_Attribute81.setter
    def mMDSL_Attribute81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Attribute__mMDSL_Attribute81", None)
        self.__mMDSL_Attribute81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Type"):
                opp_val = getattr(old_value, "mMDSL_Type", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Type"):
                opp_val = getattr(value, "mMDSL_Type", None)
                setattr(value, "mMDSL_Type", self)

class mMDSL_Relation:

    def __init__(self, name: str, mMDSL_Relation: "mMDSL_Metamodel" = None, mMDSL_Relation64: "mMDSL_Relation" = None, mMDSL_Relation62: "mMDSL_Relation" = None, mMDSL_Relation66: "mMDSL_SymbolRelation" = None, mMDSL_Relation69: "mMDSL_Class" = None, mMDSL_Relation72: "mMDSL_Class" = None, mMDSL_Relation75: set["mMDSL_Attribute"] = None, mMDSL_Relation78: set["mMDSL_InsertEmbedCode"] = None, mMDSL_Relation103: "mMDSL_ModelType" = None, mMDSL_Relation111: "mMDSL_Mode" = None, mMDSL_Relation454: "mMDSL_RelationInstanceCreate" = None, mMDSL_Relation469: "mMDSL_RelationInstanceGetAll" = None):
        self.name = name
        self.mMDSL_Relation = mMDSL_Relation
        self.mMDSL_Relation64 = mMDSL_Relation64
        self.mMDSL_Relation62 = mMDSL_Relation62
        self.mMDSL_Relation66 = mMDSL_Relation66
        self.mMDSL_Relation69 = mMDSL_Relation69
        self.mMDSL_Relation72 = mMDSL_Relation72
        self.mMDSL_Relation75 = mMDSL_Relation75 if mMDSL_Relation75 is not None else set()
        self.mMDSL_Relation78 = mMDSL_Relation78 if mMDSL_Relation78 is not None else set()
        self.mMDSL_Relation103 = mMDSL_Relation103
        self.mMDSL_Relation111 = mMDSL_Relation111
        self.mMDSL_Relation454 = mMDSL_Relation454
        self.mMDSL_Relation469 = mMDSL_Relation469
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_Relation469(self):
        return self.__mMDSL_Relation469

    @mMDSL_Relation469.setter
    def mMDSL_Relation469(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation469", None)
        self.__mMDSL_Relation469 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RelationInstanceGetAll468"):
                opp_val = getattr(old_value, "mMDSL_RelationInstanceGetAll468", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RelationInstanceGetAll468", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RelationInstanceGetAll468"):
                opp_val = getattr(value, "mMDSL_RelationInstanceGetAll468", None)
                setattr(value, "mMDSL_RelationInstanceGetAll468", self)

    @property
    def mMDSL_Relation(self):
        return self.__mMDSL_Relation

    @mMDSL_Relation.setter
    def mMDSL_Relation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation", None)
        self.__mMDSL_Relation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Metamodel41"):
                opp_val = getattr(old_value, "mMDSL_Metamodel41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Metamodel41"):
                opp_val = getattr(value, "mMDSL_Metamodel41", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Metamodel41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Relation78(self):
        return self.__mMDSL_Relation78

    @mMDSL_Relation78.setter
    def mMDSL_Relation78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation78", None)
        self.__mMDSL_Relation78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_InsertEmbedCode79"):
                    opp_val = getattr(item, "mMDSL_InsertEmbedCode79", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_InsertEmbedCode79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_InsertEmbedCode79"):
                    opp_val = getattr(item, "mMDSL_InsertEmbedCode79", None)
                    
                    setattr(item, "mMDSL_InsertEmbedCode79", self)
                    

    @property
    def mMDSL_Relation62(self):
        return self.__mMDSL_Relation62

    @mMDSL_Relation62.setter
    def mMDSL_Relation62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation62", None)
        self.__mMDSL_Relation62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Relation64"):
                opp_val = getattr(old_value, "mMDSL_Relation64", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Relation64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Relation64"):
                opp_val = getattr(value, "mMDSL_Relation64", None)
                setattr(value, "mMDSL_Relation64", self)

    @property
    def mMDSL_Relation64(self):
        return self.__mMDSL_Relation64

    @mMDSL_Relation64.setter
    def mMDSL_Relation64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation64", None)
        self.__mMDSL_Relation64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Relation62"):
                opp_val = getattr(old_value, "mMDSL_Relation62", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Relation62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Relation62"):
                opp_val = getattr(value, "mMDSL_Relation62", None)
                setattr(value, "mMDSL_Relation62", self)

    @property
    def mMDSL_Relation454(self):
        return self.__mMDSL_Relation454

    @mMDSL_Relation454.setter
    def mMDSL_Relation454(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation454", None)
        self.__mMDSL_Relation454 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RelationInstanceCreate453"):
                opp_val = getattr(old_value, "mMDSL_RelationInstanceCreate453", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RelationInstanceCreate453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RelationInstanceCreate453"):
                opp_val = getattr(value, "mMDSL_RelationInstanceCreate453", None)
                setattr(value, "mMDSL_RelationInstanceCreate453", self)

    @property
    def mMDSL_Relation66(self):
        return self.__mMDSL_Relation66

    @mMDSL_Relation66.setter
    def mMDSL_Relation66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation66", None)
        self.__mMDSL_Relation66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SymbolRelation67"):
                opp_val = getattr(old_value, "mMDSL_SymbolRelation67", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SymbolRelation67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SymbolRelation67"):
                opp_val = getattr(value, "mMDSL_SymbolRelation67", None)
                setattr(value, "mMDSL_SymbolRelation67", self)

    @property
    def mMDSL_Relation69(self):
        return self.__mMDSL_Relation69

    @mMDSL_Relation69.setter
    def mMDSL_Relation69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation69", None)
        self.__mMDSL_Relation69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Class70"):
                opp_val = getattr(old_value, "mMDSL_Class70", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Class70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Class70"):
                opp_val = getattr(value, "mMDSL_Class70", None)
                setattr(value, "mMDSL_Class70", self)

    @property
    def mMDSL_Relation103(self):
        return self.__mMDSL_Relation103

    @mMDSL_Relation103.setter
    def mMDSL_Relation103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation103", None)
        self.__mMDSL_Relation103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelType102"):
                opp_val = getattr(old_value, "mMDSL_ModelType102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelType102"):
                opp_val = getattr(value, "mMDSL_ModelType102", None)
                if opp_val is None:
                    setattr(value, "mMDSL_ModelType102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Relation111(self):
        return self.__mMDSL_Relation111

    @mMDSL_Relation111.setter
    def mMDSL_Relation111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation111", None)
        self.__mMDSL_Relation111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Mode110"):
                opp_val = getattr(old_value, "mMDSL_Mode110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Mode110"):
                opp_val = getattr(value, "mMDSL_Mode110", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Mode110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Relation75(self):
        return self.__mMDSL_Relation75

    @mMDSL_Relation75.setter
    def mMDSL_Relation75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation75", None)
        self.__mMDSL_Relation75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_Attribute76"):
                    opp_val = getattr(item, "mMDSL_Attribute76", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_Attribute76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_Attribute76"):
                    opp_val = getattr(item, "mMDSL_Attribute76", None)
                    
                    setattr(item, "mMDSL_Attribute76", self)
                    

    @property
    def mMDSL_Relation72(self):
        return self.__mMDSL_Relation72

    @mMDSL_Relation72.setter
    def mMDSL_Relation72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Relation__mMDSL_Relation72", None)
        self.__mMDSL_Relation72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Class73"):
                opp_val = getattr(old_value, "mMDSL_Class73", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Class73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Class73"):
                opp_val = getattr(value, "mMDSL_Class73", None)
                setattr(value, "mMDSL_Class73", self)

class mMDSL_Class:

    def __init__(self, name: str, mMDSL_Class: "mMDSL_Metamodel" = None, mMDSL_Class58: set["mMDSL_InsertEmbedCode"] = None, mMDSL_Class61: set["mMDSL_Reference"] = None, mMDSL_Class70: "mMDSL_Relation" = None, mMDSL_Class73: "mMDSL_Relation" = None, mMDSL_Class48: "mMDSL_Class" = None, mMDSL_Class46: "mMDSL_Class" = None, mMDSL_Class50: "mMDSL_SymbolClass" = None, mMDSL_Class53: set["mMDSL_ClassAttribute"] = None, mMDSL_Class55: set["mMDSL_Attribute"] = None, mMDSL_Class100: "mMDSL_ModelType" = None, mMDSL_Class108: "mMDSL_Mode" = None, mMDSL_Class92: "mMDSL_RefName" = None, mMDSL_Class275: "mMDSL_VarStatement" = None, mMDSL_Class438: "mMDSL_ClassInstanceGetAll" = None, mMDSL_Class429: "mMDSL_ClassInstanceCreate" = None):
        self.name = name
        self.mMDSL_Class = mMDSL_Class
        self.mMDSL_Class58 = mMDSL_Class58 if mMDSL_Class58 is not None else set()
        self.mMDSL_Class61 = mMDSL_Class61 if mMDSL_Class61 is not None else set()
        self.mMDSL_Class70 = mMDSL_Class70
        self.mMDSL_Class73 = mMDSL_Class73
        self.mMDSL_Class48 = mMDSL_Class48
        self.mMDSL_Class46 = mMDSL_Class46
        self.mMDSL_Class50 = mMDSL_Class50
        self.mMDSL_Class53 = mMDSL_Class53 if mMDSL_Class53 is not None else set()
        self.mMDSL_Class55 = mMDSL_Class55 if mMDSL_Class55 is not None else set()
        self.mMDSL_Class100 = mMDSL_Class100
        self.mMDSL_Class108 = mMDSL_Class108
        self.mMDSL_Class92 = mMDSL_Class92
        self.mMDSL_Class275 = mMDSL_Class275
        self.mMDSL_Class438 = mMDSL_Class438
        self.mMDSL_Class429 = mMDSL_Class429
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_Class92(self):
        return self.__mMDSL_Class92

    @mMDSL_Class92.setter
    def mMDSL_Class92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class92", None)
        self.__mMDSL_Class92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_RefName91"):
                opp_val = getattr(old_value, "mMDSL_RefName91", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_RefName91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_RefName91"):
                opp_val = getattr(value, "mMDSL_RefName91", None)
                setattr(value, "mMDSL_RefName91", self)

    @property
    def mMDSL_Class61(self):
        return self.__mMDSL_Class61

    @mMDSL_Class61.setter
    def mMDSL_Class61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class61", None)
        self.__mMDSL_Class61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_Reference"):
                    opp_val = getattr(item, "mMDSL_Reference", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_Reference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_Reference"):
                    opp_val = getattr(item, "mMDSL_Reference", None)
                    
                    setattr(item, "mMDSL_Reference", self)
                    

    @property
    def mMDSL_Class108(self):
        return self.__mMDSL_Class108

    @mMDSL_Class108.setter
    def mMDSL_Class108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class108", None)
        self.__mMDSL_Class108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Mode107"):
                opp_val = getattr(old_value, "mMDSL_Mode107", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Mode107"):
                opp_val = getattr(value, "mMDSL_Mode107", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Mode107", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Class429(self):
        return self.__mMDSL_Class429

    @mMDSL_Class429.setter
    def mMDSL_Class429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class429", None)
        self.__mMDSL_Class429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ClassInstanceCreate428"):
                opp_val = getattr(old_value, "mMDSL_ClassInstanceCreate428", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ClassInstanceCreate428", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ClassInstanceCreate428"):
                opp_val = getattr(value, "mMDSL_ClassInstanceCreate428", None)
                setattr(value, "mMDSL_ClassInstanceCreate428", self)

    @property
    def mMDSL_Class(self):
        return self.__mMDSL_Class

    @mMDSL_Class.setter
    def mMDSL_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class", None)
        self.__mMDSL_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Metamodel39"):
                opp_val = getattr(old_value, "mMDSL_Metamodel39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Metamodel39"):
                opp_val = getattr(value, "mMDSL_Metamodel39", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Metamodel39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Class73(self):
        return self.__mMDSL_Class73

    @mMDSL_Class73.setter
    def mMDSL_Class73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class73", None)
        self.__mMDSL_Class73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Relation72"):
                opp_val = getattr(old_value, "mMDSL_Relation72", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Relation72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Relation72"):
                opp_val = getattr(value, "mMDSL_Relation72", None)
                setattr(value, "mMDSL_Relation72", self)

    @property
    def mMDSL_Class438(self):
        return self.__mMDSL_Class438

    @mMDSL_Class438.setter
    def mMDSL_Class438(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class438", None)
        self.__mMDSL_Class438 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ClassInstanceGetAll437"):
                opp_val = getattr(old_value, "mMDSL_ClassInstanceGetAll437", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_ClassInstanceGetAll437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ClassInstanceGetAll437"):
                opp_val = getattr(value, "mMDSL_ClassInstanceGetAll437", None)
                setattr(value, "mMDSL_ClassInstanceGetAll437", self)

    @property
    def mMDSL_Class100(self):
        return self.__mMDSL_Class100

    @mMDSL_Class100.setter
    def mMDSL_Class100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class100", None)
        self.__mMDSL_Class100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_ModelType99"):
                opp_val = getattr(old_value, "mMDSL_ModelType99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_ModelType99"):
                opp_val = getattr(value, "mMDSL_ModelType99", None)
                if opp_val is None:
                    setattr(value, "mMDSL_ModelType99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Class48(self):
        return self.__mMDSL_Class48

    @mMDSL_Class48.setter
    def mMDSL_Class48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class48", None)
        self.__mMDSL_Class48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Class46"):
                opp_val = getattr(old_value, "mMDSL_Class46", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Class46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Class46"):
                opp_val = getattr(value, "mMDSL_Class46", None)
                setattr(value, "mMDSL_Class46", self)

    @property
    def mMDSL_Class50(self):
        return self.__mMDSL_Class50

    @mMDSL_Class50.setter
    def mMDSL_Class50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class50", None)
        self.__mMDSL_Class50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SymbolClass51"):
                opp_val = getattr(old_value, "mMDSL_SymbolClass51", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SymbolClass51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SymbolClass51"):
                opp_val = getattr(value, "mMDSL_SymbolClass51", None)
                setattr(value, "mMDSL_SymbolClass51", self)

    @property
    def mMDSL_Class55(self):
        return self.__mMDSL_Class55

    @mMDSL_Class55.setter
    def mMDSL_Class55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class55", None)
        self.__mMDSL_Class55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_Attribute56"):
                    opp_val = getattr(item, "mMDSL_Attribute56", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_Attribute56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_Attribute56"):
                    opp_val = getattr(item, "mMDSL_Attribute56", None)
                    
                    setattr(item, "mMDSL_Attribute56", self)
                    

    @property
    def mMDSL_Class58(self):
        return self.__mMDSL_Class58

    @mMDSL_Class58.setter
    def mMDSL_Class58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class58", None)
        self.__mMDSL_Class58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_InsertEmbedCode59"):
                    opp_val = getattr(item, "mMDSL_InsertEmbedCode59", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_InsertEmbedCode59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_InsertEmbedCode59"):
                    opp_val = getattr(item, "mMDSL_InsertEmbedCode59", None)
                    
                    setattr(item, "mMDSL_InsertEmbedCode59", self)
                    

    @property
    def mMDSL_Class70(self):
        return self.__mMDSL_Class70

    @mMDSL_Class70.setter
    def mMDSL_Class70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class70", None)
        self.__mMDSL_Class70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Relation69"):
                opp_val = getattr(old_value, "mMDSL_Relation69", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Relation69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Relation69"):
                opp_val = getattr(value, "mMDSL_Relation69", None)
                setattr(value, "mMDSL_Relation69", self)

    @property
    def mMDSL_Class46(self):
        return self.__mMDSL_Class46

    @mMDSL_Class46.setter
    def mMDSL_Class46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class46", None)
        self.__mMDSL_Class46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Class48"):
                opp_val = getattr(old_value, "mMDSL_Class48", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Class48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Class48"):
                opp_val = getattr(value, "mMDSL_Class48", None)
                setattr(value, "mMDSL_Class48", self)

    @property
    def mMDSL_Class53(self):
        return self.__mMDSL_Class53

    @mMDSL_Class53.setter
    def mMDSL_Class53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class53", None)
        self.__mMDSL_Class53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_ClassAttribute"):
                    opp_val = getattr(item, "mMDSL_ClassAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_ClassAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_ClassAttribute"):
                    opp_val = getattr(item, "mMDSL_ClassAttribute", None)
                    
                    setattr(item, "mMDSL_ClassAttribute", self)
                    

    @property
    def mMDSL_Class275(self):
        return self.__mMDSL_Class275

    @mMDSL_Class275.setter
    def mMDSL_Class275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Class__mMDSL_Class275", None)
        self.__mMDSL_Class275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VarStatement274"):
                opp_val = getattr(old_value, "mMDSL_VarStatement274", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_VarStatement274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VarStatement274"):
                opp_val = getattr(value, "mMDSL_VarStatement274", None)
                setattr(value, "mMDSL_VarStatement274", self)

class mMDSL_Event:

    def __init__(self, name: str, mMDSL_Event: "mMDSL_Method" = None, mMDSL_Event484: "mMDSL_Algorithm" = None):
        self.name = name
        self.mMDSL_Event = mMDSL_Event
        self.mMDSL_Event484 = mMDSL_Event484
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_Event484(self):
        return self.__mMDSL_Event484

    @mMDSL_Event484.setter
    def mMDSL_Event484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Event__mMDSL_Event484", None)
        self.__mMDSL_Event484 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Algorithm485"):
                opp_val = getattr(old_value, "mMDSL_Algorithm485", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Algorithm485", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Algorithm485"):
                opp_val = getattr(value, "mMDSL_Algorithm485", None)
                setattr(value, "mMDSL_Algorithm485", self)

    @property
    def mMDSL_Event(self):
        return self.__mMDSL_Event

    @mMDSL_Event.setter
    def mMDSL_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Event__mMDSL_Event", None)
        self.__mMDSL_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Method37"):
                opp_val = getattr(old_value, "mMDSL_Method37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Method37"):
                opp_val = getattr(value, "mMDSL_Method37", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Method37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_Algorithm:

    def __init__(self, name: str, mMDSL_Algorithm: "mMDSL_Method" = None, mMDSL_Algorithm216: set["mMDSL_Statement"] = None, mMDSL_Algorithm485: "mMDSL_Event" = None):
        self.name = name
        self.mMDSL_Algorithm = mMDSL_Algorithm
        self.mMDSL_Algorithm216 = mMDSL_Algorithm216 if mMDSL_Algorithm216 is not None else set()
        self.mMDSL_Algorithm485 = mMDSL_Algorithm485
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_Algorithm(self):
        return self.__mMDSL_Algorithm

    @mMDSL_Algorithm.setter
    def mMDSL_Algorithm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Algorithm__mMDSL_Algorithm", None)
        self.__mMDSL_Algorithm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Method35"):
                opp_val = getattr(old_value, "mMDSL_Method35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Method35"):
                opp_val = getattr(value, "mMDSL_Method35", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Method35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_Algorithm485(self):
        return self.__mMDSL_Algorithm485

    @mMDSL_Algorithm485.setter
    def mMDSL_Algorithm485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Algorithm__mMDSL_Algorithm485", None)
        self.__mMDSL_Algorithm485 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Event484"):
                opp_val = getattr(old_value, "mMDSL_Event484", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Event484", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Event484"):
                opp_val = getattr(value, "mMDSL_Event484", None)
                setattr(value, "mMDSL_Event484", self)

    @property
    def mMDSL_Algorithm216(self):
        return self.__mMDSL_Algorithm216

    @mMDSL_Algorithm216.setter
    def mMDSL_Algorithm216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Algorithm__mMDSL_Algorithm216", None)
        self.__mMDSL_Algorithm216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_Statement"):
                    opp_val = getattr(item, "mMDSL_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_Statement"):
                    opp_val = getattr(item, "mMDSL_Statement", None)
                    
                    setattr(item, "mMDSL_Statement", self)
                    

class mMDSL_Metamodel:

    pass
class mMDSL_SymbolRelation:

    def __init__(self, name: str, mMDSL_SymbolRelation: "mMDSL_Method" = None, mMDSL_SymbolRelation67: "mMDSL_Relation" = None, mMDSL_SymbolRelation118: "mMDSL_SymbolStyle" = None, mMDSL_SymbolRelation121: set["mMDSL_SVGCommand"] = None, mMDSL_SymbolRelation124: set["mMDSL_SVGCommand"] = None, mMDSL_SymbolRelation127: set["mMDSL_SVGCommand"] = None, mMDSL_SymbolRelation287: "mMDSL_VarStatement" = None):
        self.name = name
        self.mMDSL_SymbolRelation = mMDSL_SymbolRelation
        self.mMDSL_SymbolRelation67 = mMDSL_SymbolRelation67
        self.mMDSL_SymbolRelation118 = mMDSL_SymbolRelation118
        self.mMDSL_SymbolRelation121 = mMDSL_SymbolRelation121 if mMDSL_SymbolRelation121 is not None else set()
        self.mMDSL_SymbolRelation124 = mMDSL_SymbolRelation124 if mMDSL_SymbolRelation124 is not None else set()
        self.mMDSL_SymbolRelation127 = mMDSL_SymbolRelation127 if mMDSL_SymbolRelation127 is not None else set()
        self.mMDSL_SymbolRelation287 = mMDSL_SymbolRelation287
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_SymbolRelation287(self):
        return self.__mMDSL_SymbolRelation287

    @mMDSL_SymbolRelation287.setter
    def mMDSL_SymbolRelation287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolRelation__mMDSL_SymbolRelation287", None)
        self.__mMDSL_SymbolRelation287 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VarStatement286"):
                opp_val = getattr(old_value, "mMDSL_VarStatement286", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_VarStatement286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VarStatement286"):
                opp_val = getattr(value, "mMDSL_VarStatement286", None)
                setattr(value, "mMDSL_VarStatement286", self)

    @property
    def mMDSL_SymbolRelation124(self):
        return self.__mMDSL_SymbolRelation124

    @mMDSL_SymbolRelation124.setter
    def mMDSL_SymbolRelation124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolRelation__mMDSL_SymbolRelation124", None)
        self.__mMDSL_SymbolRelation124 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_SVGCommand125"):
                    opp_val = getattr(item, "mMDSL_SVGCommand125", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_SVGCommand125", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_SVGCommand125"):
                    opp_val = getattr(item, "mMDSL_SVGCommand125", None)
                    
                    setattr(item, "mMDSL_SVGCommand125", self)
                    

    @property
    def mMDSL_SymbolRelation118(self):
        return self.__mMDSL_SymbolRelation118

    @mMDSL_SymbolRelation118.setter
    def mMDSL_SymbolRelation118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolRelation__mMDSL_SymbolRelation118", None)
        self.__mMDSL_SymbolRelation118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SymbolStyle119"):
                opp_val = getattr(old_value, "mMDSL_SymbolStyle119", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SymbolStyle119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SymbolStyle119"):
                opp_val = getattr(value, "mMDSL_SymbolStyle119", None)
                setattr(value, "mMDSL_SymbolStyle119", self)

    @property
    def mMDSL_SymbolRelation(self):
        return self.__mMDSL_SymbolRelation

    @mMDSL_SymbolRelation.setter
    def mMDSL_SymbolRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolRelation__mMDSL_SymbolRelation", None)
        self.__mMDSL_SymbolRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Method31"):
                opp_val = getattr(old_value, "mMDSL_Method31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Method31"):
                opp_val = getattr(value, "mMDSL_Method31", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Method31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_SymbolRelation127(self):
        return self.__mMDSL_SymbolRelation127

    @mMDSL_SymbolRelation127.setter
    def mMDSL_SymbolRelation127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolRelation__mMDSL_SymbolRelation127", None)
        self.__mMDSL_SymbolRelation127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_SVGCommand128"):
                    opp_val = getattr(item, "mMDSL_SVGCommand128", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_SVGCommand128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_SVGCommand128"):
                    opp_val = getattr(item, "mMDSL_SVGCommand128", None)
                    
                    setattr(item, "mMDSL_SVGCommand128", self)
                    

    @property
    def mMDSL_SymbolRelation67(self):
        return self.__mMDSL_SymbolRelation67

    @mMDSL_SymbolRelation67.setter
    def mMDSL_SymbolRelation67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolRelation__mMDSL_SymbolRelation67", None)
        self.__mMDSL_SymbolRelation67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Relation66"):
                opp_val = getattr(old_value, "mMDSL_Relation66", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Relation66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Relation66"):
                opp_val = getattr(value, "mMDSL_Relation66", None)
                setattr(value, "mMDSL_Relation66", self)

    @property
    def mMDSL_SymbolRelation121(self):
        return self.__mMDSL_SymbolRelation121

    @mMDSL_SymbolRelation121.setter
    def mMDSL_SymbolRelation121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolRelation__mMDSL_SymbolRelation121", None)
        self.__mMDSL_SymbolRelation121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_SVGCommand122"):
                    opp_val = getattr(item, "mMDSL_SVGCommand122", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_SVGCommand122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_SVGCommand122"):
                    opp_val = getattr(item, "mMDSL_SVGCommand122", None)
                    
                    setattr(item, "mMDSL_SVGCommand122", self)
                    

class mMDSL_SymbolClass:

    def __init__(self, name: str, mMDSL_SymbolClass: "mMDSL_Method" = None, mMDSL_SymbolClass51: "mMDSL_Class" = None, mMDSL_SymbolClass113: "mMDSL_SymbolStyle" = None, mMDSL_SymbolClass116: set["mMDSL_SVGCommand"] = None, mMDSL_SymbolClass284: "mMDSL_VarStatement" = None):
        self.name = name
        self.mMDSL_SymbolClass = mMDSL_SymbolClass
        self.mMDSL_SymbolClass51 = mMDSL_SymbolClass51
        self.mMDSL_SymbolClass113 = mMDSL_SymbolClass113
        self.mMDSL_SymbolClass116 = mMDSL_SymbolClass116 if mMDSL_SymbolClass116 is not None else set()
        self.mMDSL_SymbolClass284 = mMDSL_SymbolClass284
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_SymbolClass(self):
        return self.__mMDSL_SymbolClass

    @mMDSL_SymbolClass.setter
    def mMDSL_SymbolClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolClass__mMDSL_SymbolClass", None)
        self.__mMDSL_SymbolClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Method29"):
                opp_val = getattr(old_value, "mMDSL_Method29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Method29"):
                opp_val = getattr(value, "mMDSL_Method29", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Method29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_SymbolClass284(self):
        return self.__mMDSL_SymbolClass284

    @mMDSL_SymbolClass284.setter
    def mMDSL_SymbolClass284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolClass__mMDSL_SymbolClass284", None)
        self.__mMDSL_SymbolClass284 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VarStatement283"):
                opp_val = getattr(old_value, "mMDSL_VarStatement283", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_VarStatement283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VarStatement283"):
                opp_val = getattr(value, "mMDSL_VarStatement283", None)
                setattr(value, "mMDSL_VarStatement283", self)

    @property
    def mMDSL_SymbolClass51(self):
        return self.__mMDSL_SymbolClass51

    @mMDSL_SymbolClass51.setter
    def mMDSL_SymbolClass51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolClass__mMDSL_SymbolClass51", None)
        self.__mMDSL_SymbolClass51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Class50"):
                opp_val = getattr(old_value, "mMDSL_Class50", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Class50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Class50"):
                opp_val = getattr(value, "mMDSL_Class50", None)
                setattr(value, "mMDSL_Class50", self)

    @property
    def mMDSL_SymbolClass113(self):
        return self.__mMDSL_SymbolClass113

    @mMDSL_SymbolClass113.setter
    def mMDSL_SymbolClass113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolClass__mMDSL_SymbolClass113", None)
        self.__mMDSL_SymbolClass113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SymbolStyle114"):
                opp_val = getattr(old_value, "mMDSL_SymbolStyle114", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SymbolStyle114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SymbolStyle114"):
                opp_val = getattr(value, "mMDSL_SymbolStyle114", None)
                setattr(value, "mMDSL_SymbolStyle114", self)

    @property
    def mMDSL_SymbolClass116(self):
        return self.__mMDSL_SymbolClass116

    @mMDSL_SymbolClass116.setter
    def mMDSL_SymbolClass116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolClass__mMDSL_SymbolClass116", None)
        self.__mMDSL_SymbolClass116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_SVGCommand"):
                    opp_val = getattr(item, "mMDSL_SVGCommand", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_SVGCommand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_SVGCommand"):
                    opp_val = getattr(item, "mMDSL_SVGCommand", None)
                    
                    setattr(item, "mMDSL_SVGCommand", self)
                    

class mMDSL_SymbolStyle:

    def __init__(self, strokewidth: str, fontsize: str, name: str, mMDSL_SymbolStyle: "mMDSL_Method" = None, mMDSL_SymbolStyle114: "mMDSL_SymbolClass" = None, mMDSL_SymbolStyle119: "mMDSL_SymbolRelation" = None, mMDSL_SymbolStyle150: "mMDSL_SVGCommand" = None, mMDSL_SymbolStyle153: "mMDSL_SVGCommand" = None, mMDSL_SymbolStyle208: "mMDSL_StrokeColor" = None, mMDSL_SymbolStyle210: "mMDSL_FontFamily" = None, mMDSL_SymbolStyle213: set["mMDSL_InsertEmbedCode"] = None, mMDSL_SymbolStyle205: "mMDSL_FillColor" = None, mMDSL_SymbolStyle290: "mMDSL_VarStatement" = None):
        self.strokewidth = strokewidth
        self.fontsize = fontsize
        self.name = name
        self.mMDSL_SymbolStyle = mMDSL_SymbolStyle
        self.mMDSL_SymbolStyle114 = mMDSL_SymbolStyle114
        self.mMDSL_SymbolStyle119 = mMDSL_SymbolStyle119
        self.mMDSL_SymbolStyle150 = mMDSL_SymbolStyle150
        self.mMDSL_SymbolStyle153 = mMDSL_SymbolStyle153
        self.mMDSL_SymbolStyle208 = mMDSL_SymbolStyle208
        self.mMDSL_SymbolStyle210 = mMDSL_SymbolStyle210
        self.mMDSL_SymbolStyle213 = mMDSL_SymbolStyle213 if mMDSL_SymbolStyle213 is not None else set()
        self.mMDSL_SymbolStyle205 = mMDSL_SymbolStyle205
        self.mMDSL_SymbolStyle290 = mMDSL_SymbolStyle290
        
    @property
    def fontsize(self) -> str:
        return self.__fontsize

    @fontsize.setter
    def fontsize(self, fontsize: str):
        self.__fontsize = fontsize

    @property
    def strokewidth(self) -> str:
        return self.__strokewidth

    @strokewidth.setter
    def strokewidth(self, strokewidth: str):
        self.__strokewidth = strokewidth

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_SymbolStyle150(self):
        return self.__mMDSL_SymbolStyle150

    @mMDSL_SymbolStyle150.setter
    def mMDSL_SymbolStyle150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolStyle__mMDSL_SymbolStyle150", None)
        self.__mMDSL_SymbolStyle150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SVGCommand149"):
                opp_val = getattr(old_value, "mMDSL_SVGCommand149", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SVGCommand149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SVGCommand149"):
                opp_val = getattr(value, "mMDSL_SVGCommand149", None)
                setattr(value, "mMDSL_SVGCommand149", self)

    @property
    def mMDSL_SymbolStyle205(self):
        return self.__mMDSL_SymbolStyle205

    @mMDSL_SymbolStyle205.setter
    def mMDSL_SymbolStyle205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolStyle__mMDSL_SymbolStyle205", None)
        self.__mMDSL_SymbolStyle205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_FillColor206"):
                opp_val = getattr(old_value, "mMDSL_FillColor206", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_FillColor206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_FillColor206"):
                opp_val = getattr(value, "mMDSL_FillColor206", None)
                setattr(value, "mMDSL_FillColor206", self)

    @property
    def mMDSL_SymbolStyle210(self):
        return self.__mMDSL_SymbolStyle210

    @mMDSL_SymbolStyle210.setter
    def mMDSL_SymbolStyle210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolStyle__mMDSL_SymbolStyle210", None)
        self.__mMDSL_SymbolStyle210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_FontFamily211"):
                opp_val = getattr(old_value, "mMDSL_FontFamily211", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_FontFamily211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_FontFamily211"):
                opp_val = getattr(value, "mMDSL_FontFamily211", None)
                setattr(value, "mMDSL_FontFamily211", self)

    @property
    def mMDSL_SymbolStyle114(self):
        return self.__mMDSL_SymbolStyle114

    @mMDSL_SymbolStyle114.setter
    def mMDSL_SymbolStyle114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolStyle__mMDSL_SymbolStyle114", None)
        self.__mMDSL_SymbolStyle114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SymbolClass113"):
                opp_val = getattr(old_value, "mMDSL_SymbolClass113", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SymbolClass113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SymbolClass113"):
                opp_val = getattr(value, "mMDSL_SymbolClass113", None)
                setattr(value, "mMDSL_SymbolClass113", self)

    @property
    def mMDSL_SymbolStyle208(self):
        return self.__mMDSL_SymbolStyle208

    @mMDSL_SymbolStyle208.setter
    def mMDSL_SymbolStyle208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolStyle__mMDSL_SymbolStyle208", None)
        self.__mMDSL_SymbolStyle208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_StrokeColor"):
                opp_val = getattr(old_value, "mMDSL_StrokeColor", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_StrokeColor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_StrokeColor"):
                opp_val = getattr(value, "mMDSL_StrokeColor", None)
                setattr(value, "mMDSL_StrokeColor", self)

    @property
    def mMDSL_SymbolStyle153(self):
        return self.__mMDSL_SymbolStyle153

    @mMDSL_SymbolStyle153.setter
    def mMDSL_SymbolStyle153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolStyle__mMDSL_SymbolStyle153", None)
        self.__mMDSL_SymbolStyle153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SVGCommand152"):
                opp_val = getattr(old_value, "mMDSL_SVGCommand152", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SVGCommand152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SVGCommand152"):
                opp_val = getattr(value, "mMDSL_SVGCommand152", None)
                setattr(value, "mMDSL_SVGCommand152", self)

    @property
    def mMDSL_SymbolStyle213(self):
        return self.__mMDSL_SymbolStyle213

    @mMDSL_SymbolStyle213.setter
    def mMDSL_SymbolStyle213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolStyle__mMDSL_SymbolStyle213", None)
        self.__mMDSL_SymbolStyle213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mMDSL_InsertEmbedCode214"):
                    opp_val = getattr(item, "mMDSL_InsertEmbedCode214", None)
                    
                    if opp_val == self:
                        setattr(item, "mMDSL_InsertEmbedCode214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mMDSL_InsertEmbedCode214"):
                    opp_val = getattr(item, "mMDSL_InsertEmbedCode214", None)
                    
                    setattr(item, "mMDSL_InsertEmbedCode214", self)
                    

    @property
    def mMDSL_SymbolStyle119(self):
        return self.__mMDSL_SymbolStyle119

    @mMDSL_SymbolStyle119.setter
    def mMDSL_SymbolStyle119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolStyle__mMDSL_SymbolStyle119", None)
        self.__mMDSL_SymbolStyle119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_SymbolRelation118"):
                opp_val = getattr(old_value, "mMDSL_SymbolRelation118", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_SymbolRelation118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_SymbolRelation118"):
                opp_val = getattr(value, "mMDSL_SymbolRelation118", None)
                setattr(value, "mMDSL_SymbolRelation118", self)

    @property
    def mMDSL_SymbolStyle(self):
        return self.__mMDSL_SymbolStyle

    @mMDSL_SymbolStyle.setter
    def mMDSL_SymbolStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolStyle__mMDSL_SymbolStyle", None)
        self.__mMDSL_SymbolStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Method27"):
                opp_val = getattr(old_value, "mMDSL_Method27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Method27"):
                opp_val = getattr(value, "mMDSL_Method27", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Method27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_SymbolStyle290(self):
        return self.__mMDSL_SymbolStyle290

    @mMDSL_SymbolStyle290.setter
    def mMDSL_SymbolStyle290(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_SymbolStyle__mMDSL_SymbolStyle290", None)
        self.__mMDSL_SymbolStyle290 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VarStatement289"):
                opp_val = getattr(old_value, "mMDSL_VarStatement289", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_VarStatement289", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VarStatement289"):
                opp_val = getattr(value, "mMDSL_VarStatement289", None)
                setattr(value, "mMDSL_VarStatement289", self)

class mMDSL_Enumeration:

    def __init__(self, name: str, enumvalues: str, mMDSL_Enumeration: "mMDSL_Method" = None, mMDSL_Enumeration97: "mMDSL_EnumType" = None):
        self.name = name
        self.enumvalues = enumvalues
        self.mMDSL_Enumeration = mMDSL_Enumeration
        self.mMDSL_Enumeration97 = mMDSL_Enumeration97
        
    @property
    def enumvalues(self) -> str:
        return self.__enumvalues

    @enumvalues.setter
    def enumvalues(self, enumvalues: str):
        self.__enumvalues = enumvalues

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_Enumeration97(self):
        return self.__mMDSL_Enumeration97

    @mMDSL_Enumeration97.setter
    def mMDSL_Enumeration97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Enumeration__mMDSL_Enumeration97", None)
        self.__mMDSL_Enumeration97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_EnumType96"):
                opp_val = getattr(old_value, "mMDSL_EnumType96", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_EnumType96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_EnumType96"):
                opp_val = getattr(value, "mMDSL_EnumType96", None)
                setattr(value, "mMDSL_EnumType96", self)

    @property
    def mMDSL_Enumeration(self):
        return self.__mMDSL_Enumeration

    @mMDSL_Enumeration.setter
    def mMDSL_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_Enumeration__mMDSL_Enumeration", None)
        self.__mMDSL_Enumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Method25"):
                opp_val = getattr(old_value, "mMDSL_Method25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Method25"):
                opp_val = getattr(value, "mMDSL_Method25", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Method25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mMDSL_InsertEmbedCode:

    pass
class mMDSL_MethodName:

    def __init__(self, name: str, mMDSL_MethodName: "mMDSL_Root" = None):
        self.name = name
        self.mMDSL_MethodName = mMDSL_MethodName
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_MethodName(self):
        return self.__mMDSL_MethodName

    @mMDSL_MethodName.setter
    def mMDSL_MethodName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_MethodName__mMDSL_MethodName", None)
        self.__mMDSL_MethodName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Root"):
                opp_val = getattr(old_value, "mMDSL_Root", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_Root", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Root"):
                opp_val = getattr(value, "mMDSL_Root", None)
                setattr(value, "mMDSL_Root", self)

class mMDSL_Root:

    pass
class mMDSL_Method:

    pass
class mMDSL_EmbedCode:

    def __init__(self, embeddedcode: str, name: str, mMDSL_EmbedCode: "mMDSL_Root" = None, mMDSL_EmbedCode23: "mMDSL_InsertEmbedCode" = None, mMDSL_EmbedCode17: "mMDSL_EmbedPlatformType" = None, mMDSL_EmbedCode20: "mMDSL_EmbedCodeType" = None, mMDSL_EmbedCode293: "mMDSL_VarStatement" = None):
        self.embeddedcode = embeddedcode
        self.name = name
        self.mMDSL_EmbedCode = mMDSL_EmbedCode
        self.mMDSL_EmbedCode23 = mMDSL_EmbedCode23
        self.mMDSL_EmbedCode17 = mMDSL_EmbedCode17
        self.mMDSL_EmbedCode20 = mMDSL_EmbedCode20
        self.mMDSL_EmbedCode293 = mMDSL_EmbedCode293
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def embeddedcode(self) -> str:
        return self.__embeddedcode

    @embeddedcode.setter
    def embeddedcode(self, embeddedcode: str):
        self.__embeddedcode = embeddedcode

    @property
    def mMDSL_EmbedCode20(self):
        return self.__mMDSL_EmbedCode20

    @mMDSL_EmbedCode20.setter
    def mMDSL_EmbedCode20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_EmbedCode__mMDSL_EmbedCode20", None)
        self.__mMDSL_EmbedCode20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_EmbedCodeType21"):
                opp_val = getattr(old_value, "mMDSL_EmbedCodeType21", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_EmbedCodeType21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_EmbedCodeType21"):
                opp_val = getattr(value, "mMDSL_EmbedCodeType21", None)
                setattr(value, "mMDSL_EmbedCodeType21", self)

    @property
    def mMDSL_EmbedCode17(self):
        return self.__mMDSL_EmbedCode17

    @mMDSL_EmbedCode17.setter
    def mMDSL_EmbedCode17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_EmbedCode__mMDSL_EmbedCode17", None)
        self.__mMDSL_EmbedCode17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_EmbedPlatformType18"):
                opp_val = getattr(old_value, "mMDSL_EmbedPlatformType18", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_EmbedPlatformType18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_EmbedPlatformType18"):
                opp_val = getattr(value, "mMDSL_EmbedPlatformType18", None)
                setattr(value, "mMDSL_EmbedPlatformType18", self)

    @property
    def mMDSL_EmbedCode(self):
        return self.__mMDSL_EmbedCode

    @mMDSL_EmbedCode.setter
    def mMDSL_EmbedCode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_EmbedCode__mMDSL_EmbedCode", None)
        self.__mMDSL_EmbedCode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Root10"):
                opp_val = getattr(old_value, "mMDSL_Root10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Root10"):
                opp_val = getattr(value, "mMDSL_Root10", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Root10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_EmbedCode293(self):
        return self.__mMDSL_EmbedCode293

    @mMDSL_EmbedCode293.setter
    def mMDSL_EmbedCode293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_EmbedCode__mMDSL_EmbedCode293", None)
        self.__mMDSL_EmbedCode293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_VarStatement292"):
                opp_val = getattr(old_value, "mMDSL_VarStatement292", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_VarStatement292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_VarStatement292"):
                opp_val = getattr(value, "mMDSL_VarStatement292", None)
                setattr(value, "mMDSL_VarStatement292", self)

    @property
    def mMDSL_EmbedCode23(self):
        return self.__mMDSL_EmbedCode23

    @mMDSL_EmbedCode23.setter
    def mMDSL_EmbedCode23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_EmbedCode__mMDSL_EmbedCode23", None)
        self.__mMDSL_EmbedCode23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_InsertEmbedCode"):
                opp_val = getattr(old_value, "mMDSL_InsertEmbedCode", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_InsertEmbedCode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_InsertEmbedCode"):
                opp_val = getattr(value, "mMDSL_InsertEmbedCode", None)
                setattr(value, "mMDSL_InsertEmbedCode", self)

class mMDSL_IncludeLibrary:

    def __init__(self, name: str, mMDSL_IncludeLibrary: "mMDSL_Root" = None, mMDSL_IncludeLibrary14: "mMDSL_IncludeLibraryType" = None):
        self.name = name
        self.mMDSL_IncludeLibrary = mMDSL_IncludeLibrary
        self.mMDSL_IncludeLibrary14 = mMDSL_IncludeLibrary14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_IncludeLibrary(self):
        return self.__mMDSL_IncludeLibrary

    @mMDSL_IncludeLibrary.setter
    def mMDSL_IncludeLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_IncludeLibrary__mMDSL_IncludeLibrary", None)
        self.__mMDSL_IncludeLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Root8"):
                opp_val = getattr(old_value, "mMDSL_Root8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Root8"):
                opp_val = getattr(value, "mMDSL_Root8", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Root8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_IncludeLibrary14(self):
        return self.__mMDSL_IncludeLibrary14

    @mMDSL_IncludeLibrary14.setter
    def mMDSL_IncludeLibrary14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_IncludeLibrary__mMDSL_IncludeLibrary14", None)
        self.__mMDSL_IncludeLibrary14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_IncludeLibraryType15"):
                opp_val = getattr(old_value, "mMDSL_IncludeLibraryType15", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_IncludeLibraryType15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_IncludeLibraryType15"):
                opp_val = getattr(value, "mMDSL_IncludeLibraryType15", None)
                setattr(value, "mMDSL_IncludeLibraryType15", self)

class mMDSL_EmbedCodeType:

    def __init__(self, name: str, mMDSL_EmbedCodeType: "mMDSL_Root" = None, mMDSL_EmbedCodeType21: "mMDSL_EmbedCode" = None):
        self.name = name
        self.mMDSL_EmbedCodeType = mMDSL_EmbedCodeType
        self.mMDSL_EmbedCodeType21 = mMDSL_EmbedCodeType21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_EmbedCodeType(self):
        return self.__mMDSL_EmbedCodeType

    @mMDSL_EmbedCodeType.setter
    def mMDSL_EmbedCodeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_EmbedCodeType__mMDSL_EmbedCodeType", None)
        self.__mMDSL_EmbedCodeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Root6"):
                opp_val = getattr(old_value, "mMDSL_Root6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Root6"):
                opp_val = getattr(value, "mMDSL_Root6", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Root6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_EmbedCodeType21(self):
        return self.__mMDSL_EmbedCodeType21

    @mMDSL_EmbedCodeType21.setter
    def mMDSL_EmbedCodeType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_EmbedCodeType__mMDSL_EmbedCodeType21", None)
        self.__mMDSL_EmbedCodeType21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_EmbedCode20"):
                opp_val = getattr(old_value, "mMDSL_EmbedCode20", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_EmbedCode20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_EmbedCode20"):
                opp_val = getattr(value, "mMDSL_EmbedCode20", None)
                setattr(value, "mMDSL_EmbedCode20", self)

class mMDSL_EmbedPlatformType:

    def __init__(self, name: str, mMDSL_EmbedPlatformType: "mMDSL_Root" = None, mMDSL_EmbedPlatformType18: "mMDSL_EmbedCode" = None):
        self.name = name
        self.mMDSL_EmbedPlatformType = mMDSL_EmbedPlatformType
        self.mMDSL_EmbedPlatformType18 = mMDSL_EmbedPlatformType18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_EmbedPlatformType(self):
        return self.__mMDSL_EmbedPlatformType

    @mMDSL_EmbedPlatformType.setter
    def mMDSL_EmbedPlatformType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_EmbedPlatformType__mMDSL_EmbedPlatformType", None)
        self.__mMDSL_EmbedPlatformType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Root4"):
                opp_val = getattr(old_value, "mMDSL_Root4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Root4"):
                opp_val = getattr(value, "mMDSL_Root4", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Root4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_EmbedPlatformType18(self):
        return self.__mMDSL_EmbedPlatformType18

    @mMDSL_EmbedPlatformType18.setter
    def mMDSL_EmbedPlatformType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_EmbedPlatformType__mMDSL_EmbedPlatformType18", None)
        self.__mMDSL_EmbedPlatformType18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_EmbedCode17"):
                opp_val = getattr(old_value, "mMDSL_EmbedCode17", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_EmbedCode17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_EmbedCode17"):
                opp_val = getattr(value, "mMDSL_EmbedCode17", None)
                setattr(value, "mMDSL_EmbedCode17", self)

class mMDSL_IncludeLibraryType:

    def __init__(self, name: str, mMDSL_IncludeLibraryType: "mMDSL_Root" = None, mMDSL_IncludeLibraryType15: "mMDSL_IncludeLibrary" = None):
        self.name = name
        self.mMDSL_IncludeLibraryType = mMDSL_IncludeLibraryType
        self.mMDSL_IncludeLibraryType15 = mMDSL_IncludeLibraryType15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mMDSL_IncludeLibraryType(self):
        return self.__mMDSL_IncludeLibraryType

    @mMDSL_IncludeLibraryType.setter
    def mMDSL_IncludeLibraryType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_IncludeLibraryType__mMDSL_IncludeLibraryType", None)
        self.__mMDSL_IncludeLibraryType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_Root2"):
                opp_val = getattr(old_value, "mMDSL_Root2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_Root2"):
                opp_val = getattr(value, "mMDSL_Root2", None)
                if opp_val is None:
                    setattr(value, "mMDSL_Root2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mMDSL_IncludeLibraryType15(self):
        return self.__mMDSL_IncludeLibraryType15

    @mMDSL_IncludeLibraryType15.setter
    def mMDSL_IncludeLibraryType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mMDSL_IncludeLibraryType__mMDSL_IncludeLibraryType15", None)
        self.__mMDSL_IncludeLibraryType15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mMDSL_IncludeLibrary14"):
                opp_val = getattr(old_value, "mMDSL_IncludeLibrary14", None)
                if opp_val == self:
                    setattr(old_value, "mMDSL_IncludeLibrary14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mMDSL_IncludeLibrary14"):
                opp_val = getattr(value, "mMDSL_IncludeLibrary14", None)
                setattr(value, "mMDSL_IncludeLibrary14", self)
