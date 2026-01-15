from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Severity(Enum):
    info = "info"
    warning = "warning"
    error = "error"
class TextFont(Enum):
    vector = "vector"
    proportional = "proportional"
    fixed = "fixed"
class AttributeDisplay(Enum):
    off = "off"
    value = "value"
    name = "name"
    both = "both"
class PinVisible(Enum):
    off = "off"
    pad = "pad"
    pin = "pin"
    both = "both"
class GridStyle(Enum):
    lines = "lines"
    dots = "dots"
class WireCap(Enum):
    flat = "flat"
    round = "round"
class VerticalText(Enum):
    up = "up"
    down = "down"
class Align(Enum):
    topright = "topright"
    bottomleft = "bottomleft"
    bottomcenter = "bottomcenter"
    bottomright = "bottomright"
    centerleft = "centerleft"
    center = "center"
    centerright = "centerright"
    topleft = "topleft"
    topcenter = "topcenter"
class PadShape(Enum):
    square = "square"
    round = "round"
    octagon = "octagon"
    long = "long"
    offset = "offset"
class PolygonPour(Enum):
    solid = "solid"
    hatch = "hatch"
    cutout = "cutout"
class DimensionType(Enum):
    parallel = "parallel"
    horizontal = "horizontal"
    vertical = "vertical"
    radius = "radius"
    diameter = "diameter"
    leader = "leader"
class ContactRoute(Enum):
    all = "all"
    any = "any"
class PinLength(Enum):
    point = "point"
    short = "short"
    middle = "middle"
    long = "long"
class GridUnit(Enum):
    mic = "mic"
    mm = "mm"
    mil = "mil"
    inch = "inch"
class GateAddLevel(Enum):
    must = "must"
    can = "can"
    next = "next"
    request = "request"
    always = "always"
class WireStyle(Enum):
    dashdot = "dashdot"
    continuous = "continuous"
    longdash = "longdash"
    shortdash = "shortdash"
class PinFunction(Enum):
    none = "none"
    dot = "dot"
    clk = "clk"
    dotclk = "dotclk"
class PinDirection(Enum):
    nc = "nc"
    in = "in"
    out = "out"
    io = "io"
    oc = "oc"
    pwr = "pwr"
    pas = "pas"
    hiz = "hiz"
    sup = "sup"


############################################
# Definition of Classes
############################################

class eaglemodel_Label:

    def __init__(self, x: float, y: float, size: float, layer: int, font: str, ratio: int, rot: int, xref: bool, eaglemodel_Label: "eaglemodel_Segment" = None):
        self.x = x
        self.y = y
        self.size = size
        self.layer = layer
        self.font = font
        self.ratio = ratio
        self.rot = rot
        self.xref = xref
        self.eaglemodel_Label = eaglemodel_Label
        
    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size

    @property
    def rot(self) -> int:
        return self.__rot

    @rot.setter
    def rot(self, rot: int):
        self.__rot = rot

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def layer(self) -> int:
        return self.__layer

    @layer.setter
    def layer(self, layer: int):
        self.__layer = layer

    @property
    def xref(self) -> bool:
        return self.__xref

    @xref.setter
    def xref(self, xref: bool):
        self.__xref = xref

    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def eaglemodel_Label(self):
        return self.__eaglemodel_Label

    @eaglemodel_Label.setter
    def eaglemodel_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Label__eaglemodel_Label", None)
        self.__eaglemodel_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Segment199"):
                opp_val = getattr(old_value, "eaglemodel_Segment199", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Segment199"):
                opp_val = getattr(value, "eaglemodel_Segment199", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Segment199", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Junction:

    def __init__(self, x: float, y: float, eaglemodel_Junction: "eaglemodel_Segment" = None):
        self.x = x
        self.y = y
        self.eaglemodel_Junction = eaglemodel_Junction
        
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def eaglemodel_Junction(self):
        return self.__eaglemodel_Junction

    @eaglemodel_Junction.setter
    def eaglemodel_Junction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Junction__eaglemodel_Junction", None)
        self.__eaglemodel_Junction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Segment197"):
                opp_val = getattr(old_value, "eaglemodel_Segment197", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Segment197"):
                opp_val = getattr(value, "eaglemodel_Segment197", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Segment197", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Pinref:

    def __init__(self, part: str, gate: str, pin: str, eaglemodel_Pinref: "eaglemodel_Segment" = None):
        self.part = part
        self.gate = gate
        self.pin = pin
        self.eaglemodel_Pinref = eaglemodel_Pinref
        
    @property
    def pin(self) -> str:
        return self.__pin

    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def gate(self) -> str:
        return self.__gate

    @gate.setter
    def gate(self, gate: str):
        self.__gate = gate

    @property
    def part(self) -> str:
        return self.__part

    @part.setter
    def part(self, part: str):
        self.__part = part

    @property
    def eaglemodel_Pinref(self):
        return self.__eaglemodel_Pinref

    @eaglemodel_Pinref.setter
    def eaglemodel_Pinref(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Pinref__eaglemodel_Pinref", None)
        self.__eaglemodel_Pinref = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Segment192"):
                opp_val = getattr(old_value, "eaglemodel_Segment192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Segment192"):
                opp_val = getattr(value, "eaglemodel_Segment192", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Segment192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Bus:

    def __init__(self, name: str, eaglemodel_Bus185: set["eaglemodel_Segment"] = None, eaglemodel_Bus: "eaglemodel_Busses" = None):
        self.name = name
        self.eaglemodel_Bus185 = eaglemodel_Bus185 if eaglemodel_Bus185 is not None else set()
        self.eaglemodel_Bus = eaglemodel_Bus
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eaglemodel_Bus(self):
        return self.__eaglemodel_Bus

    @eaglemodel_Bus.setter
    def eaglemodel_Bus(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Bus__eaglemodel_Bus", None)
        self.__eaglemodel_Bus = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Busses183"):
                opp_val = getattr(old_value, "eaglemodel_Busses183", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Busses183"):
                opp_val = getattr(value, "eaglemodel_Busses183", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Busses183", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Bus185(self):
        return self.__eaglemodel_Bus185

    @eaglemodel_Bus185.setter
    def eaglemodel_Bus185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Bus__eaglemodel_Bus185", None)
        self.__eaglemodel_Bus185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Segment"):
                    opp_val = getattr(item, "eaglemodel_Segment", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Segment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Segment"):
                    opp_val = getattr(item, "eaglemodel_Segment", None)
                    
                    setattr(item, "eaglemodel_Segment", self)
                    

class eaglemodel_Net:

    def __init__(self, name: str, class: int, eaglemodel_Net: "eaglemodel_Nets" = None, eaglemodel_Net189: set["eaglemodel_Segment"] = None):
        self.name = name
        self.class = class
        self.eaglemodel_Net = eaglemodel_Net
        self.eaglemodel_Net189 = eaglemodel_Net189 if eaglemodel_Net189 is not None else set()
        
    @property
    def class(self) -> int:
        return self.__class

    @class.setter
    def class(self, class: int):
        self.__class = class

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eaglemodel_Net189(self):
        return self.__eaglemodel_Net189

    @eaglemodel_Net189.setter
    def eaglemodel_Net189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Net__eaglemodel_Net189", None)
        self.__eaglemodel_Net189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Segment190"):
                    opp_val = getattr(item, "eaglemodel_Segment190", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Segment190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Segment190"):
                    opp_val = getattr(item, "eaglemodel_Segment190", None)
                    
                    setattr(item, "eaglemodel_Segment190", self)
                    

    @property
    def eaglemodel_Net(self):
        return self.__eaglemodel_Net

    @eaglemodel_Net.setter
    def eaglemodel_Net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Net__eaglemodel_Net", None)
        self.__eaglemodel_Net = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Nets187"):
                opp_val = getattr(old_value, "eaglemodel_Nets187", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Nets187"):
                opp_val = getattr(value, "eaglemodel_Nets187", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Nets187", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Segment:

    pass
class eaglemodel_Instance:

    def __init__(self, part: str, gate: str, x: float, y: float, smashed: bool, rot: int, eaglemodel_Instance: "eaglemodel_Instances" = None, eaglemodel_Instance180: set["eaglemodel_Attribute"] = None):
        self.part = part
        self.gate = gate
        self.x = x
        self.y = y
        self.smashed = smashed
        self.rot = rot
        self.eaglemodel_Instance = eaglemodel_Instance
        self.eaglemodel_Instance180 = eaglemodel_Instance180 if eaglemodel_Instance180 is not None else set()
        
    @property
    def rot(self) -> int:
        return self.__rot

    @rot.setter
    def rot(self, rot: int):
        self.__rot = rot

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def gate(self) -> str:
        return self.__gate

    @gate.setter
    def gate(self, gate: str):
        self.__gate = gate

    @property
    def part(self) -> str:
        return self.__part

    @part.setter
    def part(self, part: str):
        self.__part = part

    @property
    def smashed(self) -> bool:
        return self.__smashed

    @smashed.setter
    def smashed(self, smashed: bool):
        self.__smashed = smashed

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def eaglemodel_Instance(self):
        return self.__eaglemodel_Instance

    @eaglemodel_Instance.setter
    def eaglemodel_Instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Instance__eaglemodel_Instance", None)
        self.__eaglemodel_Instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Instances178"):
                opp_val = getattr(old_value, "eaglemodel_Instances178", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Instances178"):
                opp_val = getattr(value, "eaglemodel_Instances178", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Instances178", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Instance180(self):
        return self.__eaglemodel_Instance180

    @eaglemodel_Instance180.setter
    def eaglemodel_Instance180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Instance__eaglemodel_Instance180", None)
        self.__eaglemodel_Instance180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Attribute181"):
                    opp_val = getattr(item, "eaglemodel_Attribute181", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Attribute181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Attribute181"):
                    opp_val = getattr(item, "eaglemodel_Attribute181", None)
                    
                    setattr(item, "eaglemodel_Attribute181", self)
                    

class eaglemodel_Connect:

    def __init__(self, gate: str, pin: str, pad: str, route: str, eaglemodel_Connect: "eaglemodel_Connects" = None):
        self.gate = gate
        self.pin = pin
        self.pad = pad
        self.route = route
        self.eaglemodel_Connect = eaglemodel_Connect
        
    @property
    def pad(self) -> str:
        return self.__pad

    @pad.setter
    def pad(self, pad: str):
        self.__pad = pad

    @property
    def pin(self) -> str:
        return self.__pin

    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def route(self) -> str:
        return self.__route

    @route.setter
    def route(self, route: str):
        self.__route = route

    @property
    def gate(self) -> str:
        return self.__gate

    @gate.setter
    def gate(self, gate: str):
        self.__gate = gate

    @property
    def eaglemodel_Connect(self):
        return self.__eaglemodel_Connect

    @eaglemodel_Connect.setter
    def eaglemodel_Connect(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Connect__eaglemodel_Connect", None)
        self.__eaglemodel_Connect = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Connects147"):
                opp_val = getattr(old_value, "eaglemodel_Connects147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Connects147"):
                opp_val = getattr(value, "eaglemodel_Connects147", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Connects147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Technologies:

    pass
class eaglemodel_Connects:

    pass
class eaglemodel_Device:

    def __init__(self, name: str, package: str, eaglemodel_Device: "eaglemodel_Devices" = None, eaglemodel_Device143: "eaglemodel_Connects" = None, eaglemodel_Device145: "eaglemodel_Technologies" = None):
        self.name = name
        self.package = package
        self.eaglemodel_Device = eaglemodel_Device
        self.eaglemodel_Device143 = eaglemodel_Device143
        self.eaglemodel_Device145 = eaglemodel_Device145
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eaglemodel_Device(self):
        return self.__eaglemodel_Device

    @eaglemodel_Device.setter
    def eaglemodel_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Device__eaglemodel_Device", None)
        self.__eaglemodel_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Devices141"):
                opp_val = getattr(old_value, "eaglemodel_Devices141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Devices141"):
                opp_val = getattr(value, "eaglemodel_Devices141", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Devices141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Device143(self):
        return self.__eaglemodel_Device143

    @eaglemodel_Device143.setter
    def eaglemodel_Device143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Device__eaglemodel_Device143", None)
        self.__eaglemodel_Device143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Connects"):
                opp_val = getattr(old_value, "eaglemodel_Connects", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Connects", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Connects"):
                opp_val = getattr(value, "eaglemodel_Connects", None)
                setattr(value, "eaglemodel_Connects", self)

    @property
    def eaglemodel_Device145(self):
        return self.__eaglemodel_Device145

    @eaglemodel_Device145.setter
    def eaglemodel_Device145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Device__eaglemodel_Device145", None)
        self.__eaglemodel_Device145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Technologies"):
                opp_val = getattr(old_value, "eaglemodel_Technologies", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Technologies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Technologies"):
                opp_val = getattr(value, "eaglemodel_Technologies", None)
                setattr(value, "eaglemodel_Technologies", self)

class eaglemodel_Technology:

    def __init__(self, name: str, eaglemodel_Technology: "eaglemodel_Technologies" = None, eaglemodel_Technology151: set["eaglemodel_Attribute"] = None):
        self.name = name
        self.eaglemodel_Technology = eaglemodel_Technology
        self.eaglemodel_Technology151 = eaglemodel_Technology151 if eaglemodel_Technology151 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eaglemodel_Technology(self):
        return self.__eaglemodel_Technology

    @eaglemodel_Technology.setter
    def eaglemodel_Technology(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Technology__eaglemodel_Technology", None)
        self.__eaglemodel_Technology = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Technologies149"):
                opp_val = getattr(old_value, "eaglemodel_Technologies149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Technologies149"):
                opp_val = getattr(value, "eaglemodel_Technologies149", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Technologies149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Technology151(self):
        return self.__eaglemodel_Technology151

    @eaglemodel_Technology151.setter
    def eaglemodel_Technology151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Technology__eaglemodel_Technology151", None)
        self.__eaglemodel_Technology151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Attribute152"):
                    opp_val = getattr(item, "eaglemodel_Attribute152", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Attribute152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Attribute152"):
                    opp_val = getattr(item, "eaglemodel_Attribute152", None)
                    
                    setattr(item, "eaglemodel_Attribute152", self)
                    

class eaglemodel_Gate:

    def __init__(self, name: str, symbol: str, x: float, y: float, addlevel: str, swaplevel: int, eaglemodel_Gate: "eaglemodel_Gates" = None):
        self.name = name
        self.symbol = symbol
        self.x = x
        self.y = y
        self.addlevel = addlevel
        self.swaplevel = swaplevel
        self.eaglemodel_Gate = eaglemodel_Gate
        
    @property
    def swaplevel(self) -> int:
        return self.__swaplevel

    @swaplevel.setter
    def swaplevel(self, swaplevel: int):
        self.__swaplevel = swaplevel

    @property
    def addlevel(self) -> str:
        return self.__addlevel

    @addlevel.setter
    def addlevel(self, addlevel: str):
        self.__addlevel = addlevel

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def eaglemodel_Gate(self):
        return self.__eaglemodel_Gate

    @eaglemodel_Gate.setter
    def eaglemodel_Gate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Gate__eaglemodel_Gate", None)
        self.__eaglemodel_Gate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Gates139"):
                opp_val = getattr(old_value, "eaglemodel_Gates139", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Gates139"):
                opp_val = getattr(value, "eaglemodel_Gates139", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Gates139", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Vertex:

    def __init__(self, x: float, y: float, curve: float, eaglemodel_Vertex: "eaglemodel_Polygon" = None):
        self.x = x
        self.y = y
        self.curve = curve
        self.eaglemodel_Vertex = eaglemodel_Vertex
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def curve(self) -> float:
        return self.__curve

    @curve.setter
    def curve(self, curve: float):
        self.__curve = curve

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def eaglemodel_Vertex(self):
        return self.__eaglemodel_Vertex

    @eaglemodel_Vertex.setter
    def eaglemodel_Vertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Vertex__eaglemodel_Vertex", None)
        self.__eaglemodel_Vertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Polygon137"):
                opp_val = getattr(old_value, "eaglemodel_Polygon137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Polygon137"):
                opp_val = getattr(value, "eaglemodel_Polygon137", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Polygon137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Deviceset:

    def __init__(self, name: str, prefix: str, uservalue: bool, eaglemodel_Deviceset130: "eaglemodel_Description" = None, eaglemodel_Deviceset133: "eaglemodel_Gates" = None, eaglemodel_Deviceset135: "eaglemodel_Devices" = None, eaglemodel_Deviceset: "eaglemodel_Devicesets" = None):
        self.name = name
        self.prefix = prefix
        self.uservalue = uservalue
        self.eaglemodel_Deviceset130 = eaglemodel_Deviceset130
        self.eaglemodel_Deviceset133 = eaglemodel_Deviceset133
        self.eaglemodel_Deviceset135 = eaglemodel_Deviceset135
        self.eaglemodel_Deviceset = eaglemodel_Deviceset
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def uservalue(self) -> bool:
        return self.__uservalue

    @uservalue.setter
    def uservalue(self, uservalue: bool):
        self.__uservalue = uservalue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eaglemodel_Deviceset(self):
        return self.__eaglemodel_Deviceset

    @eaglemodel_Deviceset.setter
    def eaglemodel_Deviceset(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Deviceset__eaglemodel_Deviceset", None)
        self.__eaglemodel_Deviceset = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Devicesets128"):
                opp_val = getattr(old_value, "eaglemodel_Devicesets128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Devicesets128"):
                opp_val = getattr(value, "eaglemodel_Devicesets128", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Devicesets128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Deviceset133(self):
        return self.__eaglemodel_Deviceset133

    @eaglemodel_Deviceset133.setter
    def eaglemodel_Deviceset133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Deviceset__eaglemodel_Deviceset133", None)
        self.__eaglemodel_Deviceset133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Gates"):
                opp_val = getattr(old_value, "eaglemodel_Gates", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Gates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Gates"):
                opp_val = getattr(value, "eaglemodel_Gates", None)
                setattr(value, "eaglemodel_Gates", self)

    @property
    def eaglemodel_Deviceset130(self):
        return self.__eaglemodel_Deviceset130

    @eaglemodel_Deviceset130.setter
    def eaglemodel_Deviceset130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Deviceset__eaglemodel_Deviceset130", None)
        self.__eaglemodel_Deviceset130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Description131"):
                opp_val = getattr(old_value, "eaglemodel_Description131", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Description131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Description131"):
                opp_val = getattr(value, "eaglemodel_Description131", None)
                setattr(value, "eaglemodel_Description131", self)

    @property
    def eaglemodel_Deviceset135(self):
        return self.__eaglemodel_Deviceset135

    @eaglemodel_Deviceset135.setter
    def eaglemodel_Deviceset135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Deviceset__eaglemodel_Deviceset135", None)
        self.__eaglemodel_Deviceset135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Devices"):
                opp_val = getattr(old_value, "eaglemodel_Devices", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Devices", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Devices"):
                opp_val = getattr(value, "eaglemodel_Devices", None)
                setattr(value, "eaglemodel_Devices", self)

class eaglemodel_Pin:

    def __init__(self, name: str, x: float, y: float, visible: str, length: str, direction: str, function: str, swaplevel: int, rot: int, eaglemodel_Pin: "eaglemodel_Symbol" = None):
        self.name = name
        self.x = x
        self.y = y
        self.visible = visible
        self.length = length
        self.direction = direction
        self.function = function
        self.swaplevel = swaplevel
        self.rot = rot
        self.eaglemodel_Pin = eaglemodel_Pin
        
    @property
    def swaplevel(self) -> int:
        return self.__swaplevel

    @swaplevel.setter
    def swaplevel(self, swaplevel: int):
        self.__swaplevel = swaplevel

    @property
    def visible(self) -> str:
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def function(self) -> str:
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def rot(self) -> int:
        return self.__rot

    @rot.setter
    def rot(self, rot: int):
        self.__rot = rot

    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def eaglemodel_Pin(self):
        return self.__eaglemodel_Pin

    @eaglemodel_Pin.setter
    def eaglemodel_Pin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Pin__eaglemodel_Pin", None)
        self.__eaglemodel_Pin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbol117"):
                opp_val = getattr(old_value, "eaglemodel_Symbol117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbol117"):
                opp_val = getattr(value, "eaglemodel_Symbol117", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Symbol117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Devices:

    pass
class eaglemodel_Gates:

    pass
class eaglemodel_Symbol:

    def __init__(self, name: str, eaglemodel_Symbol102: "eaglemodel_Description" = None, eaglemodel_Symbol105: set["eaglemodel_Polygon"] = None, eaglemodel_Symbol108: set["eaglemodel_Wire"] = None, eaglemodel_Symbol111: set["eaglemodel_Text"] = None, eaglemodel_Symbol: "eaglemodel_Symbols" = None, eaglemodel_Symbol114: set["eaglemodel_Dimension"] = None, eaglemodel_Symbol117: set["eaglemodel_Pin"] = None, eaglemodel_Symbol119: set["eaglemodel_Circle"] = None, eaglemodel_Symbol122: set["eaglemodel_Rectangle"] = None, eaglemodel_Symbol125: set["eaglemodel_Frame"] = None):
        self.name = name
        self.eaglemodel_Symbol102 = eaglemodel_Symbol102
        self.eaglemodel_Symbol105 = eaglemodel_Symbol105 if eaglemodel_Symbol105 is not None else set()
        self.eaglemodel_Symbol108 = eaglemodel_Symbol108 if eaglemodel_Symbol108 is not None else set()
        self.eaglemodel_Symbol111 = eaglemodel_Symbol111 if eaglemodel_Symbol111 is not None else set()
        self.eaglemodel_Symbol = eaglemodel_Symbol
        self.eaglemodel_Symbol114 = eaglemodel_Symbol114 if eaglemodel_Symbol114 is not None else set()
        self.eaglemodel_Symbol117 = eaglemodel_Symbol117 if eaglemodel_Symbol117 is not None else set()
        self.eaglemodel_Symbol119 = eaglemodel_Symbol119 if eaglemodel_Symbol119 is not None else set()
        self.eaglemodel_Symbol122 = eaglemodel_Symbol122 if eaglemodel_Symbol122 is not None else set()
        self.eaglemodel_Symbol125 = eaglemodel_Symbol125 if eaglemodel_Symbol125 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eaglemodel_Symbol119(self):
        return self.__eaglemodel_Symbol119

    @eaglemodel_Symbol119.setter
    def eaglemodel_Symbol119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Symbol__eaglemodel_Symbol119", None)
        self.__eaglemodel_Symbol119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Circle120"):
                    opp_val = getattr(item, "eaglemodel_Circle120", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Circle120", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Circle120"):
                    opp_val = getattr(item, "eaglemodel_Circle120", None)
                    
                    setattr(item, "eaglemodel_Circle120", self)
                    

    @property
    def eaglemodel_Symbol114(self):
        return self.__eaglemodel_Symbol114

    @eaglemodel_Symbol114.setter
    def eaglemodel_Symbol114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Symbol__eaglemodel_Symbol114", None)
        self.__eaglemodel_Symbol114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Dimension115"):
                    opp_val = getattr(item, "eaglemodel_Dimension115", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Dimension115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Dimension115"):
                    opp_val = getattr(item, "eaglemodel_Dimension115", None)
                    
                    setattr(item, "eaglemodel_Dimension115", self)
                    

    @property
    def eaglemodel_Symbol(self):
        return self.__eaglemodel_Symbol

    @eaglemodel_Symbol.setter
    def eaglemodel_Symbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Symbol__eaglemodel_Symbol", None)
        self.__eaglemodel_Symbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbols100"):
                opp_val = getattr(old_value, "eaglemodel_Symbols100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbols100"):
                opp_val = getattr(value, "eaglemodel_Symbols100", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Symbols100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Symbol111(self):
        return self.__eaglemodel_Symbol111

    @eaglemodel_Symbol111.setter
    def eaglemodel_Symbol111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Symbol__eaglemodel_Symbol111", None)
        self.__eaglemodel_Symbol111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Text112"):
                    opp_val = getattr(item, "eaglemodel_Text112", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Text112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Text112"):
                    opp_val = getattr(item, "eaglemodel_Text112", None)
                    
                    setattr(item, "eaglemodel_Text112", self)
                    

    @property
    def eaglemodel_Symbol102(self):
        return self.__eaglemodel_Symbol102

    @eaglemodel_Symbol102.setter
    def eaglemodel_Symbol102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Symbol__eaglemodel_Symbol102", None)
        self.__eaglemodel_Symbol102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Description103"):
                opp_val = getattr(old_value, "eaglemodel_Description103", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Description103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Description103"):
                opp_val = getattr(value, "eaglemodel_Description103", None)
                setattr(value, "eaglemodel_Description103", self)

    @property
    def eaglemodel_Symbol125(self):
        return self.__eaglemodel_Symbol125

    @eaglemodel_Symbol125.setter
    def eaglemodel_Symbol125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Symbol__eaglemodel_Symbol125", None)
        self.__eaglemodel_Symbol125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Frame126"):
                    opp_val = getattr(item, "eaglemodel_Frame126", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Frame126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Frame126"):
                    opp_val = getattr(item, "eaglemodel_Frame126", None)
                    
                    setattr(item, "eaglemodel_Frame126", self)
                    

    @property
    def eaglemodel_Symbol105(self):
        return self.__eaglemodel_Symbol105

    @eaglemodel_Symbol105.setter
    def eaglemodel_Symbol105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Symbol__eaglemodel_Symbol105", None)
        self.__eaglemodel_Symbol105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Polygon106"):
                    opp_val = getattr(item, "eaglemodel_Polygon106", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Polygon106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Polygon106"):
                    opp_val = getattr(item, "eaglemodel_Polygon106", None)
                    
                    setattr(item, "eaglemodel_Polygon106", self)
                    

    @property
    def eaglemodel_Symbol122(self):
        return self.__eaglemodel_Symbol122

    @eaglemodel_Symbol122.setter
    def eaglemodel_Symbol122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Symbol__eaglemodel_Symbol122", None)
        self.__eaglemodel_Symbol122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Rectangle123"):
                    opp_val = getattr(item, "eaglemodel_Rectangle123", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Rectangle123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Rectangle123"):
                    opp_val = getattr(item, "eaglemodel_Rectangle123", None)
                    
                    setattr(item, "eaglemodel_Rectangle123", self)
                    

    @property
    def eaglemodel_Symbol108(self):
        return self.__eaglemodel_Symbol108

    @eaglemodel_Symbol108.setter
    def eaglemodel_Symbol108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Symbol__eaglemodel_Symbol108", None)
        self.__eaglemodel_Symbol108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Wire109"):
                    opp_val = getattr(item, "eaglemodel_Wire109", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Wire109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Wire109"):
                    opp_val = getattr(item, "eaglemodel_Wire109", None)
                    
                    setattr(item, "eaglemodel_Wire109", self)
                    

    @property
    def eaglemodel_Symbol117(self):
        return self.__eaglemodel_Symbol117

    @eaglemodel_Symbol117.setter
    def eaglemodel_Symbol117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Symbol__eaglemodel_Symbol117", None)
        self.__eaglemodel_Symbol117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Pin"):
                    opp_val = getattr(item, "eaglemodel_Pin", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Pin", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Pin"):
                    opp_val = getattr(item, "eaglemodel_Pin", None)
                    
                    setattr(item, "eaglemodel_Pin", self)
                    

class eaglemodel_SMD:

    def __init__(self, thermals: bool, cream: bool, name: str, x: float, y: float, dx: float, dy: float, layer: int, roundness: int, rot: int, stop: bool, eaglemodel_SMD: "eaglemodel_Package" = None):
        self.thermals = thermals
        self.cream = cream
        self.name = name
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.layer = layer
        self.roundness = roundness
        self.rot = rot
        self.stop = stop
        self.eaglemodel_SMD = eaglemodel_SMD
        
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def cream(self) -> bool:
        return self.__cream

    @cream.setter
    def cream(self, cream: bool):
        self.__cream = cream

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dx(self) -> float:
        return self.__dx

    @dx.setter
    def dx(self, dx: float):
        self.__dx = dx

    @property
    def dy(self) -> float:
        return self.__dy

    @dy.setter
    def dy(self, dy: float):
        self.__dy = dy

    @property
    def stop(self) -> bool:
        return self.__stop

    @stop.setter
    def stop(self, stop: bool):
        self.__stop = stop

    @property
    def roundness(self) -> int:
        return self.__roundness

    @roundness.setter
    def roundness(self, roundness: int):
        self.__roundness = roundness

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def thermals(self) -> bool:
        return self.__thermals

    @thermals.setter
    def thermals(self, thermals: bool):
        self.__thermals = thermals

    @property
    def layer(self) -> int:
        return self.__layer

    @layer.setter
    def layer(self, layer: int):
        self.__layer = layer

    @property
    def rot(self) -> int:
        return self.__rot

    @rot.setter
    def rot(self, rot: int):
        self.__rot = rot

    @property
    def eaglemodel_SMD(self):
        return self.__eaglemodel_SMD

    @eaglemodel_SMD.setter
    def eaglemodel_SMD(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_SMD__eaglemodel_SMD", None)
        self.__eaglemodel_SMD = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package98"):
                opp_val = getattr(old_value, "eaglemodel_Package98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package98"):
                opp_val = getattr(value, "eaglemodel_Package98", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Package98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Pad:

    def __init__(self, name: str, x: float, y: float, drill: float, diameter: float, shape: str, rot: int, stop: bool, thermals: bool, first: bool, eaglemodel_Pad: "eaglemodel_Package" = None):
        self.name = name
        self.x = x
        self.y = y
        self.drill = drill
        self.diameter = diameter
        self.shape = shape
        self.rot = rot
        self.stop = stop
        self.thermals = thermals
        self.first = first
        self.eaglemodel_Pad = eaglemodel_Pad
        
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def thermals(self) -> bool:
        return self.__thermals

    @thermals.setter
    def thermals(self, thermals: bool):
        self.__thermals = thermals

    @property
    def diameter(self) -> float:
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter: float):
        self.__diameter = diameter

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def drill(self) -> float:
        return self.__drill

    @drill.setter
    def drill(self, drill: float):
        self.__drill = drill

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def rot(self) -> int:
        return self.__rot

    @rot.setter
    def rot(self, rot: int):
        self.__rot = rot

    @property
    def first(self) -> bool:
        return self.__first

    @first.setter
    def first(self, first: bool):
        self.__first = first

    @property
    def stop(self) -> bool:
        return self.__stop

    @stop.setter
    def stop(self, stop: bool):
        self.__stop = stop

    @property
    def eaglemodel_Pad(self):
        return self.__eaglemodel_Pad

    @eaglemodel_Pad.setter
    def eaglemodel_Pad(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Pad__eaglemodel_Pad", None)
        self.__eaglemodel_Pad = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package96"):
                opp_val = getattr(old_value, "eaglemodel_Package96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package96"):
                opp_val = getattr(value, "eaglemodel_Package96", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Package96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Hole:

    def __init__(self, x: float, y: float, drill: float, eaglemodel_Hole: "eaglemodel_Package" = None, eaglemodel_Hole176: "eaglemodel_Plain" = None):
        self.x = x
        self.y = y
        self.drill = drill
        self.eaglemodel_Hole = eaglemodel_Hole
        self.eaglemodel_Hole176 = eaglemodel_Hole176
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def drill(self) -> float:
        return self.__drill

    @drill.setter
    def drill(self, drill: float):
        self.__drill = drill

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def eaglemodel_Hole(self):
        return self.__eaglemodel_Hole

    @eaglemodel_Hole.setter
    def eaglemodel_Hole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Hole__eaglemodel_Hole", None)
        self.__eaglemodel_Hole = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package94"):
                opp_val = getattr(old_value, "eaglemodel_Package94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package94"):
                opp_val = getattr(value, "eaglemodel_Package94", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Package94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Hole176(self):
        return self.__eaglemodel_Hole176

    @eaglemodel_Hole176.setter
    def eaglemodel_Hole176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Hole__eaglemodel_Hole176", None)
        self.__eaglemodel_Hole176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Plain175"):
                opp_val = getattr(old_value, "eaglemodel_Plain175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Plain175"):
                opp_val = getattr(value, "eaglemodel_Plain175", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Plain175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Frame:

    def __init__(self, x1: float, y1: float, x2: float, y2: float, columns: int, rows: int, layer: int, borderleft: bool, bordertop: bool, borderright: bool, borderbottom: bool, eaglemodel_Frame: "eaglemodel_Package" = None, eaglemodel_Frame126: "eaglemodel_Symbol" = None, eaglemodel_Frame173: "eaglemodel_Plain" = None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.columns = columns
        self.rows = rows
        self.layer = layer
        self.borderleft = borderleft
        self.bordertop = bordertop
        self.borderright = borderright
        self.borderbottom = borderbottom
        self.eaglemodel_Frame = eaglemodel_Frame
        self.eaglemodel_Frame126 = eaglemodel_Frame126
        self.eaglemodel_Frame173 = eaglemodel_Frame173
        
    @property
    def layer(self) -> int:
        return self.__layer

    @layer.setter
    def layer(self, layer: int):
        self.__layer = layer

    @property
    def borderleft(self) -> bool:
        return self.__borderleft

    @borderleft.setter
    def borderleft(self, borderleft: bool):
        self.__borderleft = borderleft

    @property
    def borderright(self) -> bool:
        return self.__borderright

    @borderright.setter
    def borderright(self, borderright: bool):
        self.__borderright = borderright

    @property
    def y1(self) -> float:
        return self.__y1

    @y1.setter
    def y1(self, y1: float):
        self.__y1 = y1

    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

    @property
    def x2(self) -> float:
        return self.__x2

    @x2.setter
    def x2(self, x2: float):
        self.__x2 = x2

    @property
    def borderbottom(self) -> bool:
        return self.__borderbottom

    @borderbottom.setter
    def borderbottom(self, borderbottom: bool):
        self.__borderbottom = borderbottom

    @property
    def x1(self) -> float:
        return self.__x1

    @x1.setter
    def x1(self, x1: float):
        self.__x1 = x1

    @property
    def bordertop(self) -> bool:
        return self.__bordertop

    @bordertop.setter
    def bordertop(self, bordertop: bool):
        self.__bordertop = bordertop

    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, rows: int):
        self.__rows = rows

    @property
    def y2(self) -> float:
        return self.__y2

    @y2.setter
    def y2(self, y2: float):
        self.__y2 = y2

    @property
    def eaglemodel_Frame(self):
        return self.__eaglemodel_Frame

    @eaglemodel_Frame.setter
    def eaglemodel_Frame(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Frame__eaglemodel_Frame", None)
        self.__eaglemodel_Frame = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package92"):
                opp_val = getattr(old_value, "eaglemodel_Package92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package92"):
                opp_val = getattr(value, "eaglemodel_Package92", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Package92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Frame126(self):
        return self.__eaglemodel_Frame126

    @eaglemodel_Frame126.setter
    def eaglemodel_Frame126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Frame__eaglemodel_Frame126", None)
        self.__eaglemodel_Frame126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbol125"):
                opp_val = getattr(old_value, "eaglemodel_Symbol125", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbol125"):
                opp_val = getattr(value, "eaglemodel_Symbol125", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Symbol125", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Frame173(self):
        return self.__eaglemodel_Frame173

    @eaglemodel_Frame173.setter
    def eaglemodel_Frame173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Frame__eaglemodel_Frame173", None)
        self.__eaglemodel_Frame173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Plain172"):
                opp_val = getattr(old_value, "eaglemodel_Plain172", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Plain172"):
                opp_val = getattr(value, "eaglemodel_Plain172", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Plain172", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Wire:

    def __init__(self, x1: float, y1: float, x2: float, y2: float, width: float, layer: int, extent: str, style: str, curve: float, cap: str, eaglemodel_Wire: "eaglemodel_Package" = None, eaglemodel_Wire109: "eaglemodel_Symbol" = None, eaglemodel_Wire158: "eaglemodel_Plain" = None, eaglemodel_Wire195: "eaglemodel_Segment" = None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
        self.layer = layer
        self.extent = extent
        self.style = style
        self.curve = curve
        self.cap = cap
        self.eaglemodel_Wire = eaglemodel_Wire
        self.eaglemodel_Wire109 = eaglemodel_Wire109
        self.eaglemodel_Wire158 = eaglemodel_Wire158
        self.eaglemodel_Wire195 = eaglemodel_Wire195
        
    @property
    def y1(self) -> float:
        return self.__y1

    @y1.setter
    def y1(self, y1: float):
        self.__y1 = y1

    @property
    def y2(self) -> float:
        return self.__y2

    @y2.setter
    def y2(self, y2: float):
        self.__y2 = y2

    @property
    def x2(self) -> float:
        return self.__x2

    @x2.setter
    def x2(self, x2: float):
        self.__x2 = x2

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def cap(self) -> str:
        return self.__cap

    @cap.setter
    def cap(self, cap: str):
        self.__cap = cap

    @property
    def x1(self) -> float:
        return self.__x1

    @x1.setter
    def x1(self, x1: float):
        self.__x1 = x1

    @property
    def extent(self) -> str:
        return self.__extent

    @extent.setter
    def extent(self, extent: str):
        self.__extent = extent

    @property
    def curve(self) -> float:
        return self.__curve

    @curve.setter
    def curve(self, curve: float):
        self.__curve = curve

    @property
    def layer(self) -> int:
        return self.__layer

    @layer.setter
    def layer(self, layer: int):
        self.__layer = layer

    @property
    def eaglemodel_Wire(self):
        return self.__eaglemodel_Wire

    @eaglemodel_Wire.setter
    def eaglemodel_Wire(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Wire__eaglemodel_Wire", None)
        self.__eaglemodel_Wire = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package82"):
                opp_val = getattr(old_value, "eaglemodel_Package82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package82"):
                opp_val = getattr(value, "eaglemodel_Package82", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Package82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Wire109(self):
        return self.__eaglemodel_Wire109

    @eaglemodel_Wire109.setter
    def eaglemodel_Wire109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Wire__eaglemodel_Wire109", None)
        self.__eaglemodel_Wire109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbol108"):
                opp_val = getattr(old_value, "eaglemodel_Symbol108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbol108"):
                opp_val = getattr(value, "eaglemodel_Symbol108", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Symbol108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Wire158(self):
        return self.__eaglemodel_Wire158

    @eaglemodel_Wire158.setter
    def eaglemodel_Wire158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Wire__eaglemodel_Wire158", None)
        self.__eaglemodel_Wire158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Plain157"):
                opp_val = getattr(old_value, "eaglemodel_Plain157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Plain157"):
                opp_val = getattr(value, "eaglemodel_Plain157", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Plain157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Wire195(self):
        return self.__eaglemodel_Wire195

    @eaglemodel_Wire195.setter
    def eaglemodel_Wire195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Wire__eaglemodel_Wire195", None)
        self.__eaglemodel_Wire195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Segment194"):
                opp_val = getattr(old_value, "eaglemodel_Segment194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Segment194"):
                opp_val = getattr(value, "eaglemodel_Segment194", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Segment194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Polygon:

    def __init__(self, width: float, layer: int, spacing: float, pour: str, isolate: float, orphans: bool, thermals: bool, rank: int, eaglemodel_Polygon: "eaglemodel_Package" = None, eaglemodel_Polygon106: "eaglemodel_Symbol" = None, eaglemodel_Polygon137: set["eaglemodel_Vertex"] = None, eaglemodel_Polygon155: "eaglemodel_Plain" = None):
        self.width = width
        self.layer = layer
        self.spacing = spacing
        self.pour = pour
        self.isolate = isolate
        self.orphans = orphans
        self.thermals = thermals
        self.rank = rank
        self.eaglemodel_Polygon = eaglemodel_Polygon
        self.eaglemodel_Polygon106 = eaglemodel_Polygon106
        self.eaglemodel_Polygon137 = eaglemodel_Polygon137 if eaglemodel_Polygon137 is not None else set()
        self.eaglemodel_Polygon155 = eaglemodel_Polygon155
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def layer(self) -> int:
        return self.__layer

    @layer.setter
    def layer(self, layer: int):
        self.__layer = layer

    @property
    def pour(self) -> str:
        return self.__pour

    @pour.setter
    def pour(self, pour: str):
        self.__pour = pour

    @property
    def thermals(self) -> bool:
        return self.__thermals

    @thermals.setter
    def thermals(self, thermals: bool):
        self.__thermals = thermals

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def spacing(self) -> float:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: float):
        self.__spacing = spacing

    @property
    def isolate(self) -> float:
        return self.__isolate

    @isolate.setter
    def isolate(self, isolate: float):
        self.__isolate = isolate

    @property
    def orphans(self) -> bool:
        return self.__orphans

    @orphans.setter
    def orphans(self, orphans: bool):
        self.__orphans = orphans

    @property
    def eaglemodel_Polygon(self):
        return self.__eaglemodel_Polygon

    @eaglemodel_Polygon.setter
    def eaglemodel_Polygon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Polygon__eaglemodel_Polygon", None)
        self.__eaglemodel_Polygon = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package80"):
                opp_val = getattr(old_value, "eaglemodel_Package80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package80"):
                opp_val = getattr(value, "eaglemodel_Package80", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Package80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Polygon137(self):
        return self.__eaglemodel_Polygon137

    @eaglemodel_Polygon137.setter
    def eaglemodel_Polygon137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Polygon__eaglemodel_Polygon137", None)
        self.__eaglemodel_Polygon137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Vertex"):
                    opp_val = getattr(item, "eaglemodel_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Vertex"):
                    opp_val = getattr(item, "eaglemodel_Vertex", None)
                    
                    setattr(item, "eaglemodel_Vertex", self)
                    

    @property
    def eaglemodel_Polygon155(self):
        return self.__eaglemodel_Polygon155

    @eaglemodel_Polygon155.setter
    def eaglemodel_Polygon155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Polygon__eaglemodel_Polygon155", None)
        self.__eaglemodel_Polygon155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Plain154"):
                opp_val = getattr(old_value, "eaglemodel_Plain154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Plain154"):
                opp_val = getattr(value, "eaglemodel_Plain154", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Plain154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Polygon106(self):
        return self.__eaglemodel_Polygon106

    @eaglemodel_Polygon106.setter
    def eaglemodel_Polygon106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Polygon__eaglemodel_Polygon106", None)
        self.__eaglemodel_Polygon106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbol105"):
                opp_val = getattr(old_value, "eaglemodel_Symbol105", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbol105"):
                opp_val = getattr(value, "eaglemodel_Symbol105", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Symbol105", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Package:

    def __init__(self, name: str, eaglemodel_Package84: set["eaglemodel_Text"] = None, eaglemodel_Package86: set["eaglemodel_Dimension"] = None, eaglemodel_Package88: set["eaglemodel_Circle"] = None, eaglemodel_Package: "eaglemodel_Packages" = None, eaglemodel_Package77: "eaglemodel_Description" = None, eaglemodel_Package80: set["eaglemodel_Polygon"] = None, eaglemodel_Package82: set["eaglemodel_Wire"] = None, eaglemodel_Package90: set["eaglemodel_Rectangle"] = None, eaglemodel_Package92: set["eaglemodel_Frame"] = None, eaglemodel_Package94: set["eaglemodel_Hole"] = None, eaglemodel_Package96: set["eaglemodel_Pad"] = None, eaglemodel_Package98: set["eaglemodel_SMD"] = None):
        self.name = name
        self.eaglemodel_Package84 = eaglemodel_Package84 if eaglemodel_Package84 is not None else set()
        self.eaglemodel_Package86 = eaglemodel_Package86 if eaglemodel_Package86 is not None else set()
        self.eaglemodel_Package88 = eaglemodel_Package88 if eaglemodel_Package88 is not None else set()
        self.eaglemodel_Package = eaglemodel_Package
        self.eaglemodel_Package77 = eaglemodel_Package77
        self.eaglemodel_Package80 = eaglemodel_Package80 if eaglemodel_Package80 is not None else set()
        self.eaglemodel_Package82 = eaglemodel_Package82 if eaglemodel_Package82 is not None else set()
        self.eaglemodel_Package90 = eaglemodel_Package90 if eaglemodel_Package90 is not None else set()
        self.eaglemodel_Package92 = eaglemodel_Package92 if eaglemodel_Package92 is not None else set()
        self.eaglemodel_Package94 = eaglemodel_Package94 if eaglemodel_Package94 is not None else set()
        self.eaglemodel_Package96 = eaglemodel_Package96 if eaglemodel_Package96 is not None else set()
        self.eaglemodel_Package98 = eaglemodel_Package98 if eaglemodel_Package98 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eaglemodel_Package94(self):
        return self.__eaglemodel_Package94

    @eaglemodel_Package94.setter
    def eaglemodel_Package94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package94", None)
        self.__eaglemodel_Package94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Hole"):
                    opp_val = getattr(item, "eaglemodel_Hole", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Hole", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Hole"):
                    opp_val = getattr(item, "eaglemodel_Hole", None)
                    
                    setattr(item, "eaglemodel_Hole", self)
                    

    @property
    def eaglemodel_Package(self):
        return self.__eaglemodel_Package

    @eaglemodel_Package.setter
    def eaglemodel_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package", None)
        self.__eaglemodel_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Packages75"):
                opp_val = getattr(old_value, "eaglemodel_Packages75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Packages75"):
                opp_val = getattr(value, "eaglemodel_Packages75", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Packages75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Package82(self):
        return self.__eaglemodel_Package82

    @eaglemodel_Package82.setter
    def eaglemodel_Package82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package82", None)
        self.__eaglemodel_Package82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Wire"):
                    opp_val = getattr(item, "eaglemodel_Wire", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Wire", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Wire"):
                    opp_val = getattr(item, "eaglemodel_Wire", None)
                    
                    setattr(item, "eaglemodel_Wire", self)
                    

    @property
    def eaglemodel_Package77(self):
        return self.__eaglemodel_Package77

    @eaglemodel_Package77.setter
    def eaglemodel_Package77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package77", None)
        self.__eaglemodel_Package77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Description78"):
                opp_val = getattr(old_value, "eaglemodel_Description78", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Description78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Description78"):
                opp_val = getattr(value, "eaglemodel_Description78", None)
                setattr(value, "eaglemodel_Description78", self)

    @property
    def eaglemodel_Package92(self):
        return self.__eaglemodel_Package92

    @eaglemodel_Package92.setter
    def eaglemodel_Package92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package92", None)
        self.__eaglemodel_Package92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Frame"):
                    opp_val = getattr(item, "eaglemodel_Frame", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Frame", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Frame"):
                    opp_val = getattr(item, "eaglemodel_Frame", None)
                    
                    setattr(item, "eaglemodel_Frame", self)
                    

    @property
    def eaglemodel_Package98(self):
        return self.__eaglemodel_Package98

    @eaglemodel_Package98.setter
    def eaglemodel_Package98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package98", None)
        self.__eaglemodel_Package98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_SMD"):
                    opp_val = getattr(item, "eaglemodel_SMD", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_SMD", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_SMD"):
                    opp_val = getattr(item, "eaglemodel_SMD", None)
                    
                    setattr(item, "eaglemodel_SMD", self)
                    

    @property
    def eaglemodel_Package86(self):
        return self.__eaglemodel_Package86

    @eaglemodel_Package86.setter
    def eaglemodel_Package86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package86", None)
        self.__eaglemodel_Package86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Dimension"):
                    opp_val = getattr(item, "eaglemodel_Dimension", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Dimension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Dimension"):
                    opp_val = getattr(item, "eaglemodel_Dimension", None)
                    
                    setattr(item, "eaglemodel_Dimension", self)
                    

    @property
    def eaglemodel_Package88(self):
        return self.__eaglemodel_Package88

    @eaglemodel_Package88.setter
    def eaglemodel_Package88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package88", None)
        self.__eaglemodel_Package88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Circle"):
                    opp_val = getattr(item, "eaglemodel_Circle", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Circle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Circle"):
                    opp_val = getattr(item, "eaglemodel_Circle", None)
                    
                    setattr(item, "eaglemodel_Circle", self)
                    

    @property
    def eaglemodel_Package90(self):
        return self.__eaglemodel_Package90

    @eaglemodel_Package90.setter
    def eaglemodel_Package90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package90", None)
        self.__eaglemodel_Package90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Rectangle"):
                    opp_val = getattr(item, "eaglemodel_Rectangle", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Rectangle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Rectangle"):
                    opp_val = getattr(item, "eaglemodel_Rectangle", None)
                    
                    setattr(item, "eaglemodel_Rectangle", self)
                    

    @property
    def eaglemodel_Package84(self):
        return self.__eaglemodel_Package84

    @eaglemodel_Package84.setter
    def eaglemodel_Package84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package84", None)
        self.__eaglemodel_Package84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Text"):
                    opp_val = getattr(item, "eaglemodel_Text", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Text", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Text"):
                    opp_val = getattr(item, "eaglemodel_Text", None)
                    
                    setattr(item, "eaglemodel_Text", self)
                    

    @property
    def eaglemodel_Package80(self):
        return self.__eaglemodel_Package80

    @eaglemodel_Package80.setter
    def eaglemodel_Package80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package80", None)
        self.__eaglemodel_Package80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Polygon"):
                    opp_val = getattr(item, "eaglemodel_Polygon", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Polygon", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Polygon"):
                    opp_val = getattr(item, "eaglemodel_Polygon", None)
                    
                    setattr(item, "eaglemodel_Polygon", self)
                    

    @property
    def eaglemodel_Package96(self):
        return self.__eaglemodel_Package96

    @eaglemodel_Package96.setter
    def eaglemodel_Package96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Package__eaglemodel_Package96", None)
        self.__eaglemodel_Package96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Pad"):
                    opp_val = getattr(item, "eaglemodel_Pad", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Pad", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Pad"):
                    opp_val = getattr(item, "eaglemodel_Pad", None)
                    
                    setattr(item, "eaglemodel_Pad", self)
                    

class eaglemodel_Approved:

    def __init__(self, hash: str, eaglemodel_Approved: "eaglemodel_Errors" = None):
        self.hash = hash
        self.eaglemodel_Approved = eaglemodel_Approved
        
    @property
    def hash(self) -> str:
        return self.__hash

    @hash.setter
    def hash(self, hash: str):
        self.__hash = hash

    @property
    def eaglemodel_Approved(self):
        return self.__eaglemodel_Approved

    @eaglemodel_Approved.setter
    def eaglemodel_Approved(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Approved__eaglemodel_Approved", None)
        self.__eaglemodel_Approved = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Errors73"):
                opp_val = getattr(old_value, "eaglemodel_Errors73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Errors73"):
                opp_val = getattr(value, "eaglemodel_Errors73", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Errors73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Nets:

    pass
class eaglemodel_Rectangle:

    def __init__(self, x1: float, y1: float, x2: float, y2: float, layer: int, rot: int, eaglemodel_Rectangle: "eaglemodel_Package" = None, eaglemodel_Rectangle123: "eaglemodel_Symbol" = None, eaglemodel_Rectangle170: "eaglemodel_Plain" = None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.layer = layer
        self.rot = rot
        self.eaglemodel_Rectangle = eaglemodel_Rectangle
        self.eaglemodel_Rectangle123 = eaglemodel_Rectangle123
        self.eaglemodel_Rectangle170 = eaglemodel_Rectangle170
        
    @property
    def y2(self) -> float:
        return self.__y2

    @y2.setter
    def y2(self, y2: float):
        self.__y2 = y2

    @property
    def rot(self) -> int:
        return self.__rot

    @rot.setter
    def rot(self, rot: int):
        self.__rot = rot

    @property
    def x2(self) -> float:
        return self.__x2

    @x2.setter
    def x2(self, x2: float):
        self.__x2 = x2

    @property
    def layer(self) -> int:
        return self.__layer

    @layer.setter
    def layer(self, layer: int):
        self.__layer = layer

    @property
    def y1(self) -> float:
        return self.__y1

    @y1.setter
    def y1(self, y1: float):
        self.__y1 = y1

    @property
    def x1(self) -> float:
        return self.__x1

    @x1.setter
    def x1(self, x1: float):
        self.__x1 = x1

    @property
    def eaglemodel_Rectangle123(self):
        return self.__eaglemodel_Rectangle123

    @eaglemodel_Rectangle123.setter
    def eaglemodel_Rectangle123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Rectangle__eaglemodel_Rectangle123", None)
        self.__eaglemodel_Rectangle123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbol122"):
                opp_val = getattr(old_value, "eaglemodel_Symbol122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbol122"):
                opp_val = getattr(value, "eaglemodel_Symbol122", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Symbol122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Rectangle(self):
        return self.__eaglemodel_Rectangle

    @eaglemodel_Rectangle.setter
    def eaglemodel_Rectangle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Rectangle__eaglemodel_Rectangle", None)
        self.__eaglemodel_Rectangle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package90"):
                opp_val = getattr(old_value, "eaglemodel_Package90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package90"):
                opp_val = getattr(value, "eaglemodel_Package90", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Package90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Rectangle170(self):
        return self.__eaglemodel_Rectangle170

    @eaglemodel_Rectangle170.setter
    def eaglemodel_Rectangle170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Rectangle__eaglemodel_Rectangle170", None)
        self.__eaglemodel_Rectangle170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Plain169"):
                opp_val = getattr(old_value, "eaglemodel_Plain169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Plain169"):
                opp_val = getattr(value, "eaglemodel_Plain169", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Plain169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Circle:

    def __init__(self, x: float, y: float, radius: float, width: float, layer: int, eaglemodel_Circle: "eaglemodel_Package" = None, eaglemodel_Circle120: "eaglemodel_Symbol" = None, eaglemodel_Circle167: "eaglemodel_Plain" = None):
        self.x = x
        self.y = y
        self.radius = radius
        self.width = width
        self.layer = layer
        self.eaglemodel_Circle = eaglemodel_Circle
        self.eaglemodel_Circle120 = eaglemodel_Circle120
        self.eaglemodel_Circle167 = eaglemodel_Circle167
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def layer(self) -> int:
        return self.__layer

    @layer.setter
    def layer(self, layer: int):
        self.__layer = layer

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        self.__radius = radius

    @property
    def eaglemodel_Circle167(self):
        return self.__eaglemodel_Circle167

    @eaglemodel_Circle167.setter
    def eaglemodel_Circle167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Circle__eaglemodel_Circle167", None)
        self.__eaglemodel_Circle167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Plain166"):
                opp_val = getattr(old_value, "eaglemodel_Plain166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Plain166"):
                opp_val = getattr(value, "eaglemodel_Plain166", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Plain166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Circle120(self):
        return self.__eaglemodel_Circle120

    @eaglemodel_Circle120.setter
    def eaglemodel_Circle120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Circle__eaglemodel_Circle120", None)
        self.__eaglemodel_Circle120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbol119"):
                opp_val = getattr(old_value, "eaglemodel_Symbol119", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbol119"):
                opp_val = getattr(value, "eaglemodel_Symbol119", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Symbol119", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Circle(self):
        return self.__eaglemodel_Circle

    @eaglemodel_Circle.setter
    def eaglemodel_Circle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Circle__eaglemodel_Circle", None)
        self.__eaglemodel_Circle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package88"):
                opp_val = getattr(old_value, "eaglemodel_Package88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package88"):
                opp_val = getattr(value, "eaglemodel_Package88", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Package88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Dimension:

    def __init__(self, x2: float, y2: float, x3: float, y3: float, layer: int, dtype: str, width: float, extwidth: float, extlength: float, extoffset: float, x1: float, y1: float, textsize: float, textratio: int, unit: str, precision: int, visible: bool, eaglemodel_Dimension: "eaglemodel_Package" = None, eaglemodel_Dimension115: "eaglemodel_Symbol" = None, eaglemodel_Dimension164: "eaglemodel_Plain" = None):
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.layer = layer
        self.dtype = dtype
        self.width = width
        self.extwidth = extwidth
        self.extlength = extlength
        self.extoffset = extoffset
        self.x1 = x1
        self.y1 = y1
        self.textsize = textsize
        self.textratio = textratio
        self.unit = unit
        self.precision = precision
        self.visible = visible
        self.eaglemodel_Dimension = eaglemodel_Dimension
        self.eaglemodel_Dimension115 = eaglemodel_Dimension115
        self.eaglemodel_Dimension164 = eaglemodel_Dimension164
        
    @property
    def x3(self) -> float:
        return self.__x3

    @x3.setter
    def x3(self, x3: float):
        self.__x3 = x3

    @property
    def layer(self) -> int:
        return self.__layer

    @layer.setter
    def layer(self, layer: int):
        self.__layer = layer

    @property
    def y1(self) -> float:
        return self.__y1

    @y1.setter
    def y1(self, y1: float):
        self.__y1 = y1

    @property
    def dtype(self) -> str:
        return self.__dtype

    @dtype.setter
    def dtype(self, dtype: str):
        self.__dtype = dtype

    @property
    def textsize(self) -> float:
        return self.__textsize

    @textsize.setter
    def textsize(self, textsize: float):
        self.__textsize = textsize

    @property
    def y2(self) -> float:
        return self.__y2

    @y2.setter
    def y2(self, y2: float):
        self.__y2 = y2

    @property
    def y3(self) -> float:
        return self.__y3

    @y3.setter
    def y3(self, y3: float):
        self.__y3 = y3

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def x2(self) -> float:
        return self.__x2

    @x2.setter
    def x2(self, x2: float):
        self.__x2 = x2

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def extoffset(self) -> float:
        return self.__extoffset

    @extoffset.setter
    def extoffset(self, extoffset: float):
        self.__extoffset = extoffset

    @property
    def textratio(self) -> int:
        return self.__textratio

    @textratio.setter
    def textratio(self, textratio: int):
        self.__textratio = textratio

    @property
    def extlength(self) -> float:
        return self.__extlength

    @extlength.setter
    def extlength(self, extlength: float):
        self.__extlength = extlength

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def extwidth(self) -> float:
        return self.__extwidth

    @extwidth.setter
    def extwidth(self, extwidth: float):
        self.__extwidth = extwidth

    @property
    def x1(self) -> float:
        return self.__x1

    @x1.setter
    def x1(self, x1: float):
        self.__x1 = x1

    @property
    def precision(self) -> int:
        return self.__precision

    @precision.setter
    def precision(self, precision: int):
        self.__precision = precision

    @property
    def eaglemodel_Dimension115(self):
        return self.__eaglemodel_Dimension115

    @eaglemodel_Dimension115.setter
    def eaglemodel_Dimension115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Dimension__eaglemodel_Dimension115", None)
        self.__eaglemodel_Dimension115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbol114"):
                opp_val = getattr(old_value, "eaglemodel_Symbol114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbol114"):
                opp_val = getattr(value, "eaglemodel_Symbol114", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Symbol114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Dimension(self):
        return self.__eaglemodel_Dimension

    @eaglemodel_Dimension.setter
    def eaglemodel_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Dimension__eaglemodel_Dimension", None)
        self.__eaglemodel_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package86"):
                opp_val = getattr(old_value, "eaglemodel_Package86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package86"):
                opp_val = getattr(value, "eaglemodel_Package86", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Package86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Dimension164(self):
        return self.__eaglemodel_Dimension164

    @eaglemodel_Dimension164.setter
    def eaglemodel_Dimension164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Dimension__eaglemodel_Dimension164", None)
        self.__eaglemodel_Dimension164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Plain163"):
                opp_val = getattr(old_value, "eaglemodel_Plain163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Plain163"):
                opp_val = getattr(value, "eaglemodel_Plain163", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Plain163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Text:

    def __init__(self, x: float, y: float, size: float, layer: int, font: str, ratio: int, rot: int, align: str, distance: int, value: str, eaglemodel_Text: "eaglemodel_Package" = None, eaglemodel_Text112: "eaglemodel_Symbol" = None, eaglemodel_Text161: "eaglemodel_Plain" = None):
        self.x = x
        self.y = y
        self.size = size
        self.layer = layer
        self.font = font
        self.ratio = ratio
        self.rot = rot
        self.align = align
        self.distance = distance
        self.value = value
        self.eaglemodel_Text = eaglemodel_Text
        self.eaglemodel_Text112 = eaglemodel_Text112
        self.eaglemodel_Text161 = eaglemodel_Text161
        
    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font

    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

    @property
    def rot(self) -> int:
        return self.__rot

    @rot.setter
    def rot(self, rot: int):
        self.__rot = rot

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def layer(self) -> int:
        return self.__layer

    @layer.setter
    def layer(self, layer: int):
        self.__layer = layer

    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def eaglemodel_Text(self):
        return self.__eaglemodel_Text

    @eaglemodel_Text.setter
    def eaglemodel_Text(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Text__eaglemodel_Text", None)
        self.__eaglemodel_Text = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package84"):
                opp_val = getattr(old_value, "eaglemodel_Package84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package84"):
                opp_val = getattr(value, "eaglemodel_Package84", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Package84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Text161(self):
        return self.__eaglemodel_Text161

    @eaglemodel_Text161.setter
    def eaglemodel_Text161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Text__eaglemodel_Text161", None)
        self.__eaglemodel_Text161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Plain160"):
                opp_val = getattr(old_value, "eaglemodel_Plain160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Plain160"):
                opp_val = getattr(value, "eaglemodel_Plain160", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Plain160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Text112(self):
        return self.__eaglemodel_Text112

    @eaglemodel_Text112.setter
    def eaglemodel_Text112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Text__eaglemodel_Text112", None)
        self.__eaglemodel_Text112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbol111"):
                opp_val = getattr(old_value, "eaglemodel_Symbol111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbol111"):
                opp_val = getattr(value, "eaglemodel_Symbol111", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Symbol111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Sheet:

    pass
class eaglemodel_Busses:

    pass
class eaglemodel_Instances:

    pass
class eaglemodel_Plain:

    pass
class eaglemodel_Clearance:

    def __init__(self, class: int, value: float, eaglemodel_Clearance: "eaglemodel_Class" = None):
        self.class = class
        self.value = value
        self.eaglemodel_Clearance = eaglemodel_Clearance
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def class(self) -> int:
        return self.__class

    @class.setter
    def class(self, class: int):
        self.__class = class

    @property
    def eaglemodel_Clearance(self):
        return self.__eaglemodel_Clearance

    @eaglemodel_Clearance.setter
    def eaglemodel_Clearance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Clearance__eaglemodel_Clearance", None)
        self.__eaglemodel_Clearance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Class51"):
                opp_val = getattr(old_value, "eaglemodel_Class51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Class51"):
                opp_val = getattr(value, "eaglemodel_Class51", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Class51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Class:

    def __init__(self, number: int, name: str, width: float, drill: float, eaglemodel_Class: "eaglemodel_Classes" = None, eaglemodel_Class51: set["eaglemodel_Clearance"] = None):
        self.number = number
        self.name = name
        self.width = width
        self.drill = drill
        self.eaglemodel_Class = eaglemodel_Class
        self.eaglemodel_Class51 = eaglemodel_Class51 if eaglemodel_Class51 is not None else set()
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def drill(self) -> float:
        return self.__drill

    @drill.setter
    def drill(self, drill: float):
        self.__drill = drill

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eaglemodel_Class(self):
        return self.__eaglemodel_Class

    @eaglemodel_Class.setter
    def eaglemodel_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Class__eaglemodel_Class", None)
        self.__eaglemodel_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Classes49"):
                opp_val = getattr(old_value, "eaglemodel_Classes49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Classes49"):
                opp_val = getattr(value, "eaglemodel_Classes49", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Classes49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Class51(self):
        return self.__eaglemodel_Class51

    @eaglemodel_Class51.setter
    def eaglemodel_Class51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Class__eaglemodel_Class51", None)
        self.__eaglemodel_Class51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Clearance"):
                    opp_val = getattr(item, "eaglemodel_Clearance", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Clearance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Clearance"):
                    opp_val = getattr(item, "eaglemodel_Clearance", None)
                    
                    setattr(item, "eaglemodel_Clearance", self)
                    

class eaglemodel_Variant:

    def __init__(self, name: str, populate: bool, value: str, technology: str, eaglemodel_Variant: "eaglemodel_Part" = None):
        self.name = name
        self.populate = populate
        self.value = value
        self.technology = technology
        self.eaglemodel_Variant = eaglemodel_Variant
        
    @property
    def technology(self) -> str:
        return self.__technology

    @technology.setter
    def technology(self, technology: str):
        self.__technology = technology

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def populate(self) -> bool:
        return self.__populate

    @populate.setter
    def populate(self, populate: bool):
        self.__populate = populate

    @property
    def eaglemodel_Variant(self):
        return self.__eaglemodel_Variant

    @eaglemodel_Variant.setter
    def eaglemodel_Variant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Variant__eaglemodel_Variant", None)
        self.__eaglemodel_Variant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Part58"):
                opp_val = getattr(old_value, "eaglemodel_Part58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Part58"):
                opp_val = getattr(value, "eaglemodel_Part58", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Part58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Part:

    def __init__(self, name: str, library: str, deviceset: str, device: str, technology: str, value: str, gate: str, x: float, y: float, smashed: bool, rot: int, uid: int, eaglemodel_Part: "eaglemodel_Parts" = None, eaglemodel_Part55: set["eaglemodel_Attribute"] = None, eaglemodel_Part58: set["eaglemodel_Variant"] = None):
        self.name = name
        self.library = library
        self.deviceset = deviceset
        self.device = device
        self.technology = technology
        self.value = value
        self.gate = gate
        self.x = x
        self.y = y
        self.smashed = smashed
        self.rot = rot
        self.uid = uid
        self.eaglemodel_Part = eaglemodel_Part
        self.eaglemodel_Part55 = eaglemodel_Part55 if eaglemodel_Part55 is not None else set()
        self.eaglemodel_Part58 = eaglemodel_Part58 if eaglemodel_Part58 is not None else set()
        
    @property
    def device(self) -> str:
        return self.__device

    @device.setter
    def device(self, device: str):
        self.__device = device

    @property
    def gate(self) -> str:
        return self.__gate

    @gate.setter
    def gate(self, gate: str):
        self.__gate = gate

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def rot(self) -> int:
        return self.__rot

    @rot.setter
    def rot(self, rot: int):
        self.__rot = rot

    @property
    def uid(self) -> int:
        return self.__uid

    @uid.setter
    def uid(self, uid: int):
        self.__uid = uid

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def deviceset(self) -> str:
        return self.__deviceset

    @deviceset.setter
    def deviceset(self, deviceset: str):
        self.__deviceset = deviceset

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smashed(self) -> bool:
        return self.__smashed

    @smashed.setter
    def smashed(self, smashed: bool):
        self.__smashed = smashed

    @property
    def library(self) -> str:
        return self.__library

    @library.setter
    def library(self, library: str):
        self.__library = library

    @property
    def technology(self) -> str:
        return self.__technology

    @technology.setter
    def technology(self, technology: str):
        self.__technology = technology

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def eaglemodel_Part55(self):
        return self.__eaglemodel_Part55

    @eaglemodel_Part55.setter
    def eaglemodel_Part55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Part__eaglemodel_Part55", None)
        self.__eaglemodel_Part55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Attribute56"):
                    opp_val = getattr(item, "eaglemodel_Attribute56", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Attribute56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Attribute56"):
                    opp_val = getattr(item, "eaglemodel_Attribute56", None)
                    
                    setattr(item, "eaglemodel_Attribute56", self)
                    

    @property
    def eaglemodel_Part(self):
        return self.__eaglemodel_Part

    @eaglemodel_Part.setter
    def eaglemodel_Part(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Part__eaglemodel_Part", None)
        self.__eaglemodel_Part = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Parts53"):
                opp_val = getattr(old_value, "eaglemodel_Parts53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Parts53"):
                opp_val = getattr(value, "eaglemodel_Parts53", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Parts53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Part58(self):
        return self.__eaglemodel_Part58

    @eaglemodel_Part58.setter
    def eaglemodel_Part58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Part__eaglemodel_Part58", None)
        self.__eaglemodel_Part58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eaglemodel_Variant"):
                    opp_val = getattr(item, "eaglemodel_Variant", None)
                    
                    if opp_val == self:
                        setattr(item, "eaglemodel_Variant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eaglemodel_Variant"):
                    opp_val = getattr(item, "eaglemodel_Variant", None)
                    
                    setattr(item, "eaglemodel_Variant", self)
                    

class eaglemodel_Attribute:

    def __init__(self, name: str, value: str, x: float, y: float, size: float, layer: int, font: str, ratio: int, rot: int, display: str, constant: bool, eaglemodel_Attribute: "eaglemodel_Attributes" = None, eaglemodel_Attribute56: "eaglemodel_Part" = None, eaglemodel_Attribute152: "eaglemodel_Technology" = None, eaglemodel_Attribute181: "eaglemodel_Instance" = None):
        self.name = name
        self.value = value
        self.x = x
        self.y = y
        self.size = size
        self.layer = layer
        self.font = font
        self.ratio = ratio
        self.rot = rot
        self.display = display
        self.constant = constant
        self.eaglemodel_Attribute = eaglemodel_Attribute
        self.eaglemodel_Attribute56 = eaglemodel_Attribute56
        self.eaglemodel_Attribute152 = eaglemodel_Attribute152
        self.eaglemodel_Attribute181 = eaglemodel_Attribute181
        
    @property
    def display(self) -> str:
        return self.__display

    @display.setter
    def display(self, display: str):
        self.__display = display

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def font(self) -> str:
        return self.__font

    @font.setter
    def font(self, font: str):
        self.__font = font

    @property
    def rot(self) -> int:
        return self.__rot

    @rot.setter
    def rot(self, rot: int):
        self.__rot = rot

    @property
    def ratio(self) -> int:
        return self.__ratio

    @ratio.setter
    def ratio(self, ratio: int):
        self.__ratio = ratio

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def layer(self) -> int:
        return self.__layer

    @layer.setter
    def layer(self, layer: int):
        self.__layer = layer

    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, size: float):
        self.__size = size

    @property
    def eaglemodel_Attribute181(self):
        return self.__eaglemodel_Attribute181

    @eaglemodel_Attribute181.setter
    def eaglemodel_Attribute181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Attribute__eaglemodel_Attribute181", None)
        self.__eaglemodel_Attribute181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Instance180"):
                opp_val = getattr(old_value, "eaglemodel_Instance180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Instance180"):
                opp_val = getattr(value, "eaglemodel_Instance180", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Instance180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Attribute(self):
        return self.__eaglemodel_Attribute

    @eaglemodel_Attribute.setter
    def eaglemodel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Attribute__eaglemodel_Attribute", None)
        self.__eaglemodel_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Attributes45"):
                opp_val = getattr(old_value, "eaglemodel_Attributes45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Attributes45"):
                opp_val = getattr(value, "eaglemodel_Attributes45", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Attributes45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Attribute152(self):
        return self.__eaglemodel_Attribute152

    @eaglemodel_Attribute152.setter
    def eaglemodel_Attribute152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Attribute__eaglemodel_Attribute152", None)
        self.__eaglemodel_Attribute152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Technology151"):
                opp_val = getattr(old_value, "eaglemodel_Technology151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Technology151"):
                opp_val = getattr(value, "eaglemodel_Technology151", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Technology151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eaglemodel_Attribute56(self):
        return self.__eaglemodel_Attribute56

    @eaglemodel_Attribute56.setter
    def eaglemodel_Attribute56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Attribute__eaglemodel_Attribute56", None)
        self.__eaglemodel_Attribute56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Part55"):
                opp_val = getattr(old_value, "eaglemodel_Part55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Part55"):
                opp_val = getattr(value, "eaglemodel_Part55", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Part55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Variantdef:

    def __init__(self, name: str, current: bool, eaglemodel_Variantdef: "eaglemodel_Variantdefs" = None):
        self.name = name
        self.current = current
        self.eaglemodel_Variantdef = eaglemodel_Variantdef
        
    @property
    def current(self) -> bool:
        return self.__current

    @current.setter
    def current(self, current: bool):
        self.__current = current

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eaglemodel_Variantdef(self):
        return self.__eaglemodel_Variantdef

    @eaglemodel_Variantdef.setter
    def eaglemodel_Variantdef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Variantdef__eaglemodel_Variantdef", None)
        self.__eaglemodel_Variantdef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Variantdefs47"):
                opp_val = getattr(old_value, "eaglemodel_Variantdefs47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Variantdefs47"):
                opp_val = getattr(value, "eaglemodel_Variantdefs47", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Variantdefs47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Library:

    def __init__(self, name: str, eaglemodel_Library36: "eaglemodel_Description" = None, eaglemodel_Library39: "eaglemodel_Packages" = None, eaglemodel_Library41: "eaglemodel_Symbols" = None, eaglemodel_Library43: "eaglemodel_Devicesets" = None, eaglemodel_Library: "eaglemodel_Libraries" = None):
        self.name = name
        self.eaglemodel_Library36 = eaglemodel_Library36
        self.eaglemodel_Library39 = eaglemodel_Library39
        self.eaglemodel_Library41 = eaglemodel_Library41
        self.eaglemodel_Library43 = eaglemodel_Library43
        self.eaglemodel_Library = eaglemodel_Library
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eaglemodel_Library43(self):
        return self.__eaglemodel_Library43

    @eaglemodel_Library43.setter
    def eaglemodel_Library43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Library__eaglemodel_Library43", None)
        self.__eaglemodel_Library43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Devicesets"):
                opp_val = getattr(old_value, "eaglemodel_Devicesets", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Devicesets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Devicesets"):
                opp_val = getattr(value, "eaglemodel_Devicesets", None)
                setattr(value, "eaglemodel_Devicesets", self)

    @property
    def eaglemodel_Library36(self):
        return self.__eaglemodel_Library36

    @eaglemodel_Library36.setter
    def eaglemodel_Library36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Library__eaglemodel_Library36", None)
        self.__eaglemodel_Library36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Description37"):
                opp_val = getattr(old_value, "eaglemodel_Description37", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Description37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Description37"):
                opp_val = getattr(value, "eaglemodel_Description37", None)
                setattr(value, "eaglemodel_Description37", self)

    @property
    def eaglemodel_Library39(self):
        return self.__eaglemodel_Library39

    @eaglemodel_Library39.setter
    def eaglemodel_Library39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Library__eaglemodel_Library39", None)
        self.__eaglemodel_Library39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Packages"):
                opp_val = getattr(old_value, "eaglemodel_Packages", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Packages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Packages"):
                opp_val = getattr(value, "eaglemodel_Packages", None)
                setattr(value, "eaglemodel_Packages", self)

    @property
    def eaglemodel_Library41(self):
        return self.__eaglemodel_Library41

    @eaglemodel_Library41.setter
    def eaglemodel_Library41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Library__eaglemodel_Library41", None)
        self.__eaglemodel_Library41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbols"):
                opp_val = getattr(old_value, "eaglemodel_Symbols", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Symbols", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbols"):
                opp_val = getattr(value, "eaglemodel_Symbols", None)
                setattr(value, "eaglemodel_Symbols", self)

    @property
    def eaglemodel_Library(self):
        return self.__eaglemodel_Library

    @eaglemodel_Library.setter
    def eaglemodel_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Library__eaglemodel_Library", None)
        self.__eaglemodel_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Libraries34"):
                opp_val = getattr(old_value, "eaglemodel_Libraries34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Libraries34"):
                opp_val = getattr(value, "eaglemodel_Libraries34", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Libraries34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Errors:

    pass
class eaglemodel_Sheets:

    pass
class eaglemodel_Parts:

    pass
class eaglemodel_Devicesets:

    pass
class eaglemodel_Classes:

    pass
class eaglemodel_Symbols:

    pass
class eaglemodel_Packages:

    pass
class eaglemodel_Description:

    def __init__(self, language: str, value: str, eaglemodel_Description: "eaglemodel_Schematic" = None, eaglemodel_Description37: "eaglemodel_Library" = None, eaglemodel_Description63: "eaglemodel_Sheet" = None, eaglemodel_Description78: "eaglemodel_Package" = None, eaglemodel_Description103: "eaglemodel_Symbol" = None, eaglemodel_Description131: "eaglemodel_Deviceset" = None):
        self.language = language
        self.value = value
        self.eaglemodel_Description = eaglemodel_Description
        self.eaglemodel_Description37 = eaglemodel_Description37
        self.eaglemodel_Description63 = eaglemodel_Description63
        self.eaglemodel_Description78 = eaglemodel_Description78
        self.eaglemodel_Description103 = eaglemodel_Description103
        self.eaglemodel_Description131 = eaglemodel_Description131
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def eaglemodel_Description37(self):
        return self.__eaglemodel_Description37

    @eaglemodel_Description37.setter
    def eaglemodel_Description37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Description__eaglemodel_Description37", None)
        self.__eaglemodel_Description37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Library36"):
                opp_val = getattr(old_value, "eaglemodel_Library36", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Library36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Library36"):
                opp_val = getattr(value, "eaglemodel_Library36", None)
                setattr(value, "eaglemodel_Library36", self)

    @property
    def eaglemodel_Description78(self):
        return self.__eaglemodel_Description78

    @eaglemodel_Description78.setter
    def eaglemodel_Description78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Description__eaglemodel_Description78", None)
        self.__eaglemodel_Description78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Package77"):
                opp_val = getattr(old_value, "eaglemodel_Package77", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Package77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Package77"):
                opp_val = getattr(value, "eaglemodel_Package77", None)
                setattr(value, "eaglemodel_Package77", self)

    @property
    def eaglemodel_Description103(self):
        return self.__eaglemodel_Description103

    @eaglemodel_Description103.setter
    def eaglemodel_Description103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Description__eaglemodel_Description103", None)
        self.__eaglemodel_Description103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Symbol102"):
                opp_val = getattr(old_value, "eaglemodel_Symbol102", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Symbol102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Symbol102"):
                opp_val = getattr(value, "eaglemodel_Symbol102", None)
                setattr(value, "eaglemodel_Symbol102", self)

    @property
    def eaglemodel_Description63(self):
        return self.__eaglemodel_Description63

    @eaglemodel_Description63.setter
    def eaglemodel_Description63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Description__eaglemodel_Description63", None)
        self.__eaglemodel_Description63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Sheet62"):
                opp_val = getattr(old_value, "eaglemodel_Sheet62", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Sheet62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Sheet62"):
                opp_val = getattr(value, "eaglemodel_Sheet62", None)
                setattr(value, "eaglemodel_Sheet62", self)

    @property
    def eaglemodel_Description131(self):
        return self.__eaglemodel_Description131

    @eaglemodel_Description131.setter
    def eaglemodel_Description131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Description__eaglemodel_Description131", None)
        self.__eaglemodel_Description131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Deviceset130"):
                opp_val = getattr(old_value, "eaglemodel_Deviceset130", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Deviceset130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Deviceset130"):
                opp_val = getattr(value, "eaglemodel_Deviceset130", None)
                setattr(value, "eaglemodel_Deviceset130", self)

    @property
    def eaglemodel_Description(self):
        return self.__eaglemodel_Description

    @eaglemodel_Description.setter
    def eaglemodel_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Description__eaglemodel_Description", None)
        self.__eaglemodel_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Schematic18"):
                opp_val = getattr(old_value, "eaglemodel_Schematic18", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Schematic18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Schematic18"):
                opp_val = getattr(value, "eaglemodel_Schematic18", None)
                setattr(value, "eaglemodel_Schematic18", self)

class eaglemodel_Layer:

    def __init__(self, number: int, name: str, color: int, fill: int, visible: bool, active: bool, eaglemodel_Layer: "eaglemodel_Layers" = None):
        self.number = number
        self.name = name
        self.color = color
        self.fill = fill
        self.visible = visible
        self.active = active
        self.eaglemodel_Layer = eaglemodel_Layer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def color(self) -> int:
        return self.__color

    @color.setter
    def color(self, color: int):
        self.__color = color

    @property
    def fill(self) -> int:
        return self.__fill

    @fill.setter
    def fill(self, fill: int):
        self.__fill = fill

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def active(self) -> bool:
        return self.__active

    @active.setter
    def active(self, active: bool):
        self.__active = active

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def eaglemodel_Layer(self):
        return self.__eaglemodel_Layer

    @eaglemodel_Layer.setter
    def eaglemodel_Layer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Layer__eaglemodel_Layer", None)
        self.__eaglemodel_Layer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Layers16"):
                opp_val = getattr(old_value, "eaglemodel_Layers16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Layers16"):
                opp_val = getattr(value, "eaglemodel_Layers16", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Layers16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Variantdefs:

    pass
class eaglemodel_Attributes:

    pass
class eaglemodel_Libraries:

    pass
class eaglemodel_Setting:

    def __init__(self, alwaysvectorfont: bool, verticaltext: str, eaglemodel_Setting: "eaglemodel_Settings" = None):
        self.alwaysvectorfont = alwaysvectorfont
        self.verticaltext = verticaltext
        self.eaglemodel_Setting = eaglemodel_Setting
        
    @property
    def alwaysvectorfont(self) -> bool:
        return self.__alwaysvectorfont

    @alwaysvectorfont.setter
    def alwaysvectorfont(self, alwaysvectorfont: bool):
        self.__alwaysvectorfont = alwaysvectorfont

    @property
    def verticaltext(self) -> str:
        return self.__verticaltext

    @verticaltext.setter
    def verticaltext(self, verticaltext: str):
        self.__verticaltext = verticaltext

    @property
    def eaglemodel_Setting(self):
        return self.__eaglemodel_Setting

    @eaglemodel_Setting.setter
    def eaglemodel_Setting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Setting__eaglemodel_Setting", None)
        self.__eaglemodel_Setting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Settings14"):
                opp_val = getattr(old_value, "eaglemodel_Settings14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Settings14"):
                opp_val = getattr(value, "eaglemodel_Settings14", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Settings14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Schematic:

    def __init__(self, xreflabel: str, xrefpart: str, eaglemodel_Schematic: "eaglemodel_Drawing" = None, eaglemodel_Schematic20: "eaglemodel_Libraries" = None, eaglemodel_Schematic22: "eaglemodel_Attributes" = None, eaglemodel_Schematic24: "eaglemodel_Variantdefs" = None, eaglemodel_Schematic18: "eaglemodel_Description" = None, eaglemodel_Schematic26: "eaglemodel_Classes" = None, eaglemodel_Schematic28: "eaglemodel_Parts" = None, eaglemodel_Schematic30: "eaglemodel_Sheets" = None, eaglemodel_Schematic32: "eaglemodel_Errors" = None):
        self.xreflabel = xreflabel
        self.xrefpart = xrefpart
        self.eaglemodel_Schematic = eaglemodel_Schematic
        self.eaglemodel_Schematic20 = eaglemodel_Schematic20
        self.eaglemodel_Schematic22 = eaglemodel_Schematic22
        self.eaglemodel_Schematic24 = eaglemodel_Schematic24
        self.eaglemodel_Schematic18 = eaglemodel_Schematic18
        self.eaglemodel_Schematic26 = eaglemodel_Schematic26
        self.eaglemodel_Schematic28 = eaglemodel_Schematic28
        self.eaglemodel_Schematic30 = eaglemodel_Schematic30
        self.eaglemodel_Schematic32 = eaglemodel_Schematic32
        
    @property
    def xreflabel(self) -> str:
        return self.__xreflabel

    @xreflabel.setter
    def xreflabel(self, xreflabel: str):
        self.__xreflabel = xreflabel

    @property
    def xrefpart(self) -> str:
        return self.__xrefpart

    @xrefpart.setter
    def xrefpart(self, xrefpart: str):
        self.__xrefpart = xrefpart

    @property
    def eaglemodel_Schematic18(self):
        return self.__eaglemodel_Schematic18

    @eaglemodel_Schematic18.setter
    def eaglemodel_Schematic18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Schematic__eaglemodel_Schematic18", None)
        self.__eaglemodel_Schematic18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Description"):
                opp_val = getattr(old_value, "eaglemodel_Description", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Description"):
                opp_val = getattr(value, "eaglemodel_Description", None)
                setattr(value, "eaglemodel_Description", self)

    @property
    def eaglemodel_Schematic20(self):
        return self.__eaglemodel_Schematic20

    @eaglemodel_Schematic20.setter
    def eaglemodel_Schematic20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Schematic__eaglemodel_Schematic20", None)
        self.__eaglemodel_Schematic20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Libraries"):
                opp_val = getattr(old_value, "eaglemodel_Libraries", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Libraries", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Libraries"):
                opp_val = getattr(value, "eaglemodel_Libraries", None)
                setattr(value, "eaglemodel_Libraries", self)

    @property
    def eaglemodel_Schematic24(self):
        return self.__eaglemodel_Schematic24

    @eaglemodel_Schematic24.setter
    def eaglemodel_Schematic24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Schematic__eaglemodel_Schematic24", None)
        self.__eaglemodel_Schematic24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Variantdefs"):
                opp_val = getattr(old_value, "eaglemodel_Variantdefs", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Variantdefs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Variantdefs"):
                opp_val = getattr(value, "eaglemodel_Variantdefs", None)
                setattr(value, "eaglemodel_Variantdefs", self)

    @property
    def eaglemodel_Schematic26(self):
        return self.__eaglemodel_Schematic26

    @eaglemodel_Schematic26.setter
    def eaglemodel_Schematic26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Schematic__eaglemodel_Schematic26", None)
        self.__eaglemodel_Schematic26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Classes"):
                opp_val = getattr(old_value, "eaglemodel_Classes", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Classes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Classes"):
                opp_val = getattr(value, "eaglemodel_Classes", None)
                setattr(value, "eaglemodel_Classes", self)

    @property
    def eaglemodel_Schematic22(self):
        return self.__eaglemodel_Schematic22

    @eaglemodel_Schematic22.setter
    def eaglemodel_Schematic22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Schematic__eaglemodel_Schematic22", None)
        self.__eaglemodel_Schematic22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Attributes"):
                opp_val = getattr(old_value, "eaglemodel_Attributes", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Attributes"):
                opp_val = getattr(value, "eaglemodel_Attributes", None)
                setattr(value, "eaglemodel_Attributes", self)

    @property
    def eaglemodel_Schematic30(self):
        return self.__eaglemodel_Schematic30

    @eaglemodel_Schematic30.setter
    def eaglemodel_Schematic30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Schematic__eaglemodel_Schematic30", None)
        self.__eaglemodel_Schematic30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Sheets"):
                opp_val = getattr(old_value, "eaglemodel_Sheets", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Sheets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Sheets"):
                opp_val = getattr(value, "eaglemodel_Sheets", None)
                setattr(value, "eaglemodel_Sheets", self)

    @property
    def eaglemodel_Schematic28(self):
        return self.__eaglemodel_Schematic28

    @eaglemodel_Schematic28.setter
    def eaglemodel_Schematic28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Schematic__eaglemodel_Schematic28", None)
        self.__eaglemodel_Schematic28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Parts"):
                opp_val = getattr(old_value, "eaglemodel_Parts", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Parts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Parts"):
                opp_val = getattr(value, "eaglemodel_Parts", None)
                setattr(value, "eaglemodel_Parts", self)

    @property
    def eaglemodel_Schematic32(self):
        return self.__eaglemodel_Schematic32

    @eaglemodel_Schematic32.setter
    def eaglemodel_Schematic32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Schematic__eaglemodel_Schematic32", None)
        self.__eaglemodel_Schematic32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Errors"):
                opp_val = getattr(old_value, "eaglemodel_Errors", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Errors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Errors"):
                opp_val = getattr(value, "eaglemodel_Errors", None)
                setattr(value, "eaglemodel_Errors", self)

    @property
    def eaglemodel_Schematic(self):
        return self.__eaglemodel_Schematic

    @eaglemodel_Schematic.setter
    def eaglemodel_Schematic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Schematic__eaglemodel_Schematic", None)
        self.__eaglemodel_Schematic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Drawing12"):
                opp_val = getattr(old_value, "eaglemodel_Drawing12", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Drawing12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Drawing12"):
                opp_val = getattr(value, "eaglemodel_Drawing12", None)
                setattr(value, "eaglemodel_Drawing12", self)

class eaglemodel_Layers:

    pass
class eaglemodel_Grid:

    def __init__(self, style: str, multiple: int, display: bool, distance: float, unitdist: str, unit: str, altdistance: float, altunitdist: str, altunit: str, eaglemodel_Grid: "eaglemodel_Drawing" = None):
        self.style = style
        self.multiple = multiple
        self.display = display
        self.distance = distance
        self.unitdist = unitdist
        self.unit = unit
        self.altdistance = altdistance
        self.altunitdist = altunitdist
        self.altunit = altunit
        self.eaglemodel_Grid = eaglemodel_Grid
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def altdistance(self) -> float:
        return self.__altdistance

    @altdistance.setter
    def altdistance(self, altdistance: float):
        self.__altdistance = altdistance

    @property
    def multiple(self) -> int:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: int):
        self.__multiple = multiple

    @property
    def altunitdist(self) -> str:
        return self.__altunitdist

    @altunitdist.setter
    def altunitdist(self, altunitdist: str):
        self.__altunitdist = altunitdist

    @property
    def altunit(self) -> str:
        return self.__altunit

    @altunit.setter
    def altunit(self, altunit: str):
        self.__altunit = altunit

    @property
    def distance(self) -> float:
        return self.__distance

    @distance.setter
    def distance(self, distance: float):
        self.__distance = distance

    @property
    def unitdist(self) -> str:
        return self.__unitdist

    @unitdist.setter
    def unitdist(self, unitdist: str):
        self.__unitdist = unitdist

    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def display(self) -> bool:
        return self.__display

    @display.setter
    def display(self, display: bool):
        self.__display = display

    @property
    def eaglemodel_Grid(self):
        return self.__eaglemodel_Grid

    @eaglemodel_Grid.setter
    def eaglemodel_Grid(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Grid__eaglemodel_Grid", None)
        self.__eaglemodel_Grid = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Drawing8"):
                opp_val = getattr(old_value, "eaglemodel_Drawing8", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Drawing8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Drawing8"):
                opp_val = getattr(value, "eaglemodel_Drawing8", None)
                setattr(value, "eaglemodel_Drawing8", self)

class eaglemodel_Settings:

    pass
class eaglemodel_Note:

    def __init__(self, version: str, severity: str, value: str, eaglemodel_Note: "eaglemodel_Compatibility" = None):
        self.version = version
        self.severity = severity
        self.value = value
        self.eaglemodel_Note = eaglemodel_Note
        
    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def eaglemodel_Note(self):
        return self.__eaglemodel_Note

    @eaglemodel_Note.setter
    def eaglemodel_Note(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Note__eaglemodel_Note", None)
        self.__eaglemodel_Note = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Compatibility4"):
                opp_val = getattr(old_value, "eaglemodel_Compatibility4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Compatibility4"):
                opp_val = getattr(value, "eaglemodel_Compatibility4", None)
                if opp_val is None:
                    setattr(value, "eaglemodel_Compatibility4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eaglemodel_Drawing:

    pass
class eaglemodel_Compatibility:

    pass
class eaglemodel_Eagle:

    def __init__(self, version: str, eaglemodel_Eagle: "eaglemodel_Compatibility" = None, eaglemodel_Eagle2: "eaglemodel_Drawing" = None):
        self.version = version
        self.eaglemodel_Eagle = eaglemodel_Eagle
        self.eaglemodel_Eagle2 = eaglemodel_Eagle2
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def eaglemodel_Eagle(self):
        return self.__eaglemodel_Eagle

    @eaglemodel_Eagle.setter
    def eaglemodel_Eagle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Eagle__eaglemodel_Eagle", None)
        self.__eaglemodel_Eagle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Compatibility"):
                opp_val = getattr(old_value, "eaglemodel_Compatibility", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Compatibility", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Compatibility"):
                opp_val = getattr(value, "eaglemodel_Compatibility", None)
                setattr(value, "eaglemodel_Compatibility", self)

    @property
    def eaglemodel_Eagle2(self):
        return self.__eaglemodel_Eagle2

    @eaglemodel_Eagle2.setter
    def eaglemodel_Eagle2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eaglemodel_Eagle__eaglemodel_Eagle2", None)
        self.__eaglemodel_Eagle2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eaglemodel_Drawing"):
                opp_val = getattr(old_value, "eaglemodel_Drawing", None)
                if opp_val == self:
                    setattr(old_value, "eaglemodel_Drawing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eaglemodel_Drawing"):
                opp_val = getattr(value, "eaglemodel_Drawing", None)
                setattr(value, "eaglemodel_Drawing", self)
