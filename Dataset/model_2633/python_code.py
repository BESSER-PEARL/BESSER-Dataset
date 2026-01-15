from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LabelAlignment(Enum):
    CENTER = "CENTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class FontFormat(Enum):
    normal = "normal"
    italic = "italic"
    bold = "bold"
    bold_italic = "bold_italic"
class BackgroundStyle(Enum):
    GradientTopToBottom = "GradientTopToBottom"
    GradientLeftToRight = "GradientLeftToRight"
    Liquid = "Liquid"
class ContainerShape(Enum):
    parallelogram = "parallelogram"
class AlignmentKind(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
    SQUARE = "SQUARE"
class RoutingStyle(Enum):
    Straight = "Straight"
    Manhattan = "Manhattan"
    Tree = "Tree"
class LabelPosition(Enum):
    border = "border"
    node = "node"
class BundledImageShape(Enum):
    square = "square"
    stroke = "stroke"
    triangle = "triangle"
    dot = "dot"
    ring = "ring"


############################################
# Definition of Classes
############################################

class BasicLabelStyle:

    pass
class migrationmodeler_LabelStyle(BasicLabelStyle):

    def __init__(self, labelAlignment: str):
        self.labelAlignment = labelAlignment
        
    @property
    def labelAlignment(self) -> str:
        return self.__labelAlignment

    @labelAlignment.setter
    def labelAlignment(self, labelAlignment: str):
        self.__labelAlignment = labelAlignment

class ContainerStyle:

    pass
class migrationmodeler_ShapeContainerStyle(ContainerStyle):

    def __init__(self, shape: str, migrationmodeler_ShapeContainerStyle: "migrationmodeler_Color" = None):
        self.shape = shape
        self.migrationmodeler_ShapeContainerStyle = migrationmodeler_ShapeContainerStyle
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def migrationmodeler_ShapeContainerStyle(self):
        return self.__migrationmodeler_ShapeContainerStyle

    @migrationmodeler_ShapeContainerStyle.setter
    def migrationmodeler_ShapeContainerStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_ShapeContainerStyle__migrationmodeler_ShapeContainerStyle", None)
        self.__migrationmodeler_ShapeContainerStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color70"):
                opp_val = getattr(old_value, "migrationmodeler_Color70", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color70"):
                opp_val = getattr(value, "migrationmodeler_Color70", None)
                setattr(value, "migrationmodeler_Color70", self)

class migrationmodeler_FlatContainerStyle(ContainerStyle):

    def __init__(self, backgroundStyle: str, migrationmodeler_FlatContainerStyle: "migrationmodeler_Color" = None, migrationmodeler_FlatContainerStyle67: "migrationmodeler_Color" = None):
        self.backgroundStyle = backgroundStyle
        self.migrationmodeler_FlatContainerStyle = migrationmodeler_FlatContainerStyle
        self.migrationmodeler_FlatContainerStyle67 = migrationmodeler_FlatContainerStyle67
        
    @property
    def backgroundStyle(self) -> str:
        return self.__backgroundStyle

    @backgroundStyle.setter
    def backgroundStyle(self, backgroundStyle: str):
        self.__backgroundStyle = backgroundStyle

    @property
    def migrationmodeler_FlatContainerStyle67(self):
        return self.__migrationmodeler_FlatContainerStyle67

    @migrationmodeler_FlatContainerStyle67.setter
    def migrationmodeler_FlatContainerStyle67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_FlatContainerStyle__migrationmodeler_FlatContainerStyle67", None)
        self.__migrationmodeler_FlatContainerStyle67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color68"):
                opp_val = getattr(old_value, "migrationmodeler_Color68", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color68"):
                opp_val = getattr(value, "migrationmodeler_Color68", None)
                setattr(value, "migrationmodeler_Color68", self)

    @property
    def migrationmodeler_FlatContainerStyle(self):
        return self.__migrationmodeler_FlatContainerStyle

    @migrationmodeler_FlatContainerStyle.setter
    def migrationmodeler_FlatContainerStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_FlatContainerStyle__migrationmodeler_FlatContainerStyle", None)
        self.__migrationmodeler_FlatContainerStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color65"):
                opp_val = getattr(old_value, "migrationmodeler_Color65", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color65"):
                opp_val = getattr(value, "migrationmodeler_Color65", None)
                setattr(value, "migrationmodeler_Color65", self)

class migrationmodeler_GaugeSection:

    def __init__(self, min: str, max: str, value: str, label: str, migrationmodeler_GaugeSection: "migrationmodeler_Color" = None, migrationmodeler_GaugeSection62: "migrationmodeler_Color" = None, migrationmodeler_GaugeSection80: "migrationmodeler_GaugeCompositeStyle" = None):
        self.min = min
        self.max = max
        self.value = value
        self.label = label
        self.migrationmodeler_GaugeSection = migrationmodeler_GaugeSection
        self.migrationmodeler_GaugeSection62 = migrationmodeler_GaugeSection62
        self.migrationmodeler_GaugeSection80 = migrationmodeler_GaugeSection80
        
    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def migrationmodeler_GaugeSection62(self):
        return self.__migrationmodeler_GaugeSection62

    @migrationmodeler_GaugeSection62.setter
    def migrationmodeler_GaugeSection62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_GaugeSection__migrationmodeler_GaugeSection62", None)
        self.__migrationmodeler_GaugeSection62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color63"):
                opp_val = getattr(old_value, "migrationmodeler_Color63", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color63"):
                opp_val = getattr(value, "migrationmodeler_Color63", None)
                setattr(value, "migrationmodeler_Color63", self)

    @property
    def migrationmodeler_GaugeSection80(self):
        return self.__migrationmodeler_GaugeSection80

    @migrationmodeler_GaugeSection80.setter
    def migrationmodeler_GaugeSection80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_GaugeSection__migrationmodeler_GaugeSection80", None)
        self.__migrationmodeler_GaugeSection80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_GaugeCompositeStyle"):
                opp_val = getattr(old_value, "migrationmodeler_GaugeCompositeStyle", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_GaugeCompositeStyle"):
                opp_val = getattr(value, "migrationmodeler_GaugeCompositeStyle", None)
                if opp_val is None:
                    setattr(value, "migrationmodeler_GaugeCompositeStyle", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def migrationmodeler_GaugeSection(self):
        return self.__migrationmodeler_GaugeSection

    @migrationmodeler_GaugeSection.setter
    def migrationmodeler_GaugeSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_GaugeSection__migrationmodeler_GaugeSection", None)
        self.__migrationmodeler_GaugeSection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color60"):
                opp_val = getattr(old_value, "migrationmodeler_Color60", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color60"):
                opp_val = getattr(value, "migrationmodeler_Color60", None)
                setattr(value, "migrationmodeler_Color60", self)

class NodeStyle:

    pass
class migrationmodeler_Note(NodeStyle):

    pass
class migrationmodeler_Ellipse(NodeStyle):

    def __init__(self, horizontalDiameter: str, verticalDiameter: str, migrationmodeler_Ellipse: "migrationmodeler_Color" = None):
        self.horizontalDiameter = horizontalDiameter
        self.verticalDiameter = verticalDiameter
        self.migrationmodeler_Ellipse = migrationmodeler_Ellipse
        
    @property
    def horizontalDiameter(self) -> str:
        return self.__horizontalDiameter

    @horizontalDiameter.setter
    def horizontalDiameter(self, horizontalDiameter: str):
        self.__horizontalDiameter = horizontalDiameter

    @property
    def verticalDiameter(self) -> str:
        return self.__verticalDiameter

    @verticalDiameter.setter
    def verticalDiameter(self, verticalDiameter: str):
        self.__verticalDiameter = verticalDiameter

    @property
    def migrationmodeler_Ellipse(self):
        return self.__migrationmodeler_Ellipse

    @migrationmodeler_Ellipse.setter
    def migrationmodeler_Ellipse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Ellipse__migrationmodeler_Ellipse", None)
        self.__migrationmodeler_Ellipse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color74"):
                opp_val = getattr(old_value, "migrationmodeler_Color74", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color74"):
                opp_val = getattr(value, "migrationmodeler_Color74", None)
                setattr(value, "migrationmodeler_Color74", self)

class migrationmodeler_BundledImage(NodeStyle):

    def __init__(self, shape: str, migrationmodeler_BundledImage: "migrationmodeler_Color" = None):
        self.shape = shape
        self.migrationmodeler_BundledImage = migrationmodeler_BundledImage
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def migrationmodeler_BundledImage(self):
        return self.__migrationmodeler_BundledImage

    @migrationmodeler_BundledImage.setter
    def migrationmodeler_BundledImage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_BundledImage__migrationmodeler_BundledImage", None)
        self.__migrationmodeler_BundledImage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color78"):
                opp_val = getattr(old_value, "migrationmodeler_Color78", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color78"):
                opp_val = getattr(value, "migrationmodeler_Color78", None)
                setattr(value, "migrationmodeler_Color78", self)

class migrationmodeler_GaugeCompositeStyle(NodeStyle):

    def __init__(self, alignment: str, migrationmodeler_GaugeCompositeStyle: set["migrationmodeler_GaugeSection"] = None):
        self.alignment = alignment
        self.migrationmodeler_GaugeCompositeStyle = migrationmodeler_GaugeCompositeStyle if migrationmodeler_GaugeCompositeStyle is not None else set()
        
    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def migrationmodeler_GaugeCompositeStyle(self):
        return self.__migrationmodeler_GaugeCompositeStyle

    @migrationmodeler_GaugeCompositeStyle.setter
    def migrationmodeler_GaugeCompositeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_GaugeCompositeStyle__migrationmodeler_GaugeCompositeStyle", None)
        self.__migrationmodeler_GaugeCompositeStyle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "migrationmodeler_GaugeSection80"):
                    opp_val = getattr(item, "migrationmodeler_GaugeSection80", None)
                    
                    if opp_val == self:
                        setattr(item, "migrationmodeler_GaugeSection80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "migrationmodeler_GaugeSection80"):
                    opp_val = getattr(item, "migrationmodeler_GaugeSection80", None)
                    
                    setattr(item, "migrationmodeler_GaugeSection80", self)
                    

class migrationmodeler_Lozenge(NodeStyle):

    def __init__(self, width: str, height: str, migrationmodeler_Lozenge: "migrationmodeler_Color" = None):
        self.width = width
        self.height = height
        self.migrationmodeler_Lozenge = migrationmodeler_Lozenge
        
    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def migrationmodeler_Lozenge(self):
        return self.__migrationmodeler_Lozenge

    @migrationmodeler_Lozenge.setter
    def migrationmodeler_Lozenge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Lozenge__migrationmodeler_Lozenge", None)
        self.__migrationmodeler_Lozenge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color76"):
                opp_val = getattr(old_value, "migrationmodeler_Color76", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color76"):
                opp_val = getattr(value, "migrationmodeler_Color76", None)
                setattr(value, "migrationmodeler_Color76", self)

class migrationmodeler_WorkspaceImage(ContainerStyle, NodeStyle):

    def __init__(self, workspacePath: str):
        self.workspacePath = workspacePath
        
    @property
    def workspacePath(self) -> str:
        return self.__workspacePath

    @workspacePath.setter
    def workspacePath(self, workspacePath: str):
        self.__workspacePath = workspacePath

class migrationmodeler_Square(NodeStyle):

    def __init__(self, width: str, height: str, migrationmodeler_Square: "migrationmodeler_Color" = None):
        self.width = width
        self.height = height
        self.migrationmodeler_Square = migrationmodeler_Square
        
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
    def migrationmodeler_Square(self):
        return self.__migrationmodeler_Square

    @migrationmodeler_Square.setter
    def migrationmodeler_Square(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Square__migrationmodeler_Square", None)
        self.__migrationmodeler_Square = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color72"):
                opp_val = getattr(old_value, "migrationmodeler_Color72", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color72"):
                opp_val = getattr(value, "migrationmodeler_Color72", None)
                setattr(value, "migrationmodeler_Color72", self)

class migrationmodeler_Dot(NodeStyle):

    pass
class BorderedStyle:

    pass
class LabelStyle:

    pass
class migrationmodeler_BorderedStyle:

    def __init__(self, borderSize: int, migrationmodeler_BorderedStyle: "migrationmodeler_Color" = None):
        self.borderSize = borderSize
        self.migrationmodeler_BorderedStyle = migrationmodeler_BorderedStyle
        
    @property
    def borderSize(self) -> int:
        return self.__borderSize

    @borderSize.setter
    def borderSize(self, borderSize: int):
        self.__borderSize = borderSize

    @property
    def migrationmodeler_BorderedStyle(self):
        return self.__migrationmodeler_BorderedStyle

    @migrationmodeler_BorderedStyle.setter
    def migrationmodeler_BorderedStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_BorderedStyle__migrationmodeler_BorderedStyle", None)
        self.__migrationmodeler_BorderedStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color53"):
                opp_val = getattr(old_value, "migrationmodeler_Color53", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color53"):
                opp_val = getattr(value, "migrationmodeler_Color53", None)
                setattr(value, "migrationmodeler_Color53", self)

class migrationmodeler_Representation(ABC):

    def __init__(self, name: str, migrationmodeler_Representation: "migrationmodeler_TestCase" = None):
        self.name = name
        self.migrationmodeler_Representation = migrationmodeler_Representation
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def migrationmodeler_Representation(self):
        return self.__migrationmodeler_Representation

    @migrationmodeler_Representation.setter
    def migrationmodeler_Representation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Representation__migrationmodeler_Representation", None)
        self.__migrationmodeler_Representation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_TestCase"):
                opp_val = getattr(old_value, "migrationmodeler_TestCase", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_TestCase"):
                opp_val = getattr(value, "migrationmodeler_TestCase", None)
                if opp_val is None:
                    setattr(value, "migrationmodeler_TestCase", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class migrationmodeler_TestCase:

    pass
class AbstractRepresentation:

    pass
class migrationmodeler_BasicLabelStyle:

    def __init__(self, labelSize: int, labelFormat: str, showIcon: bool, iconPath: str, migrationmodeler_BasicLabelStyle: "migrationmodeler_EdgeStyle" = None, migrationmodeler_BasicLabelStyle47: "migrationmodeler_EdgeStyle" = None, migrationmodeler_BasicLabelStyle50: "migrationmodeler_EdgeStyle" = None, migrationmodeler_BasicLabelStyle55: "migrationmodeler_Color" = None):
        self.labelSize = labelSize
        self.labelFormat = labelFormat
        self.showIcon = showIcon
        self.iconPath = iconPath
        self.migrationmodeler_BasicLabelStyle = migrationmodeler_BasicLabelStyle
        self.migrationmodeler_BasicLabelStyle47 = migrationmodeler_BasicLabelStyle47
        self.migrationmodeler_BasicLabelStyle50 = migrationmodeler_BasicLabelStyle50
        self.migrationmodeler_BasicLabelStyle55 = migrationmodeler_BasicLabelStyle55
        
    @property
    def showIcon(self) -> bool:
        return self.__showIcon

    @showIcon.setter
    def showIcon(self, showIcon: bool):
        self.__showIcon = showIcon

    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def labelSize(self) -> int:
        return self.__labelSize

    @labelSize.setter
    def labelSize(self, labelSize: int):
        self.__labelSize = labelSize

    @property
    def labelFormat(self) -> str:
        return self.__labelFormat

    @labelFormat.setter
    def labelFormat(self, labelFormat: str):
        self.__labelFormat = labelFormat

    @property
    def migrationmodeler_BasicLabelStyle(self):
        return self.__migrationmodeler_BasicLabelStyle

    @migrationmodeler_BasicLabelStyle.setter
    def migrationmodeler_BasicLabelStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_BasicLabelStyle__migrationmodeler_BasicLabelStyle", None)
        self.__migrationmodeler_BasicLabelStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_EdgeStyle44"):
                opp_val = getattr(old_value, "migrationmodeler_EdgeStyle44", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_EdgeStyle44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_EdgeStyle44"):
                opp_val = getattr(value, "migrationmodeler_EdgeStyle44", None)
                setattr(value, "migrationmodeler_EdgeStyle44", self)

    @property
    def migrationmodeler_BasicLabelStyle47(self):
        return self.__migrationmodeler_BasicLabelStyle47

    @migrationmodeler_BasicLabelStyle47.setter
    def migrationmodeler_BasicLabelStyle47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_BasicLabelStyle__migrationmodeler_BasicLabelStyle47", None)
        self.__migrationmodeler_BasicLabelStyle47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_EdgeStyle46"):
                opp_val = getattr(old_value, "migrationmodeler_EdgeStyle46", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_EdgeStyle46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_EdgeStyle46"):
                opp_val = getattr(value, "migrationmodeler_EdgeStyle46", None)
                setattr(value, "migrationmodeler_EdgeStyle46", self)

    @property
    def migrationmodeler_BasicLabelStyle55(self):
        return self.__migrationmodeler_BasicLabelStyle55

    @migrationmodeler_BasicLabelStyle55.setter
    def migrationmodeler_BasicLabelStyle55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_BasicLabelStyle__migrationmodeler_BasicLabelStyle55", None)
        self.__migrationmodeler_BasicLabelStyle55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color56"):
                opp_val = getattr(old_value, "migrationmodeler_Color56", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color56"):
                opp_val = getattr(value, "migrationmodeler_Color56", None)
                setattr(value, "migrationmodeler_Color56", self)

    @property
    def migrationmodeler_BasicLabelStyle50(self):
        return self.__migrationmodeler_BasicLabelStyle50

    @migrationmodeler_BasicLabelStyle50.setter
    def migrationmodeler_BasicLabelStyle50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_BasicLabelStyle__migrationmodeler_BasicLabelStyle50", None)
        self.__migrationmodeler_BasicLabelStyle50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_EdgeStyle49"):
                opp_val = getattr(old_value, "migrationmodeler_EdgeStyle49", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_EdgeStyle49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_EdgeStyle49"):
                opp_val = getattr(value, "migrationmodeler_EdgeStyle49", None)
                setattr(value, "migrationmodeler_EdgeStyle49", self)

class migrationmodeler_Color:

    def __init__(self, red: int, green: int, blue: int, migrationmodeler_Color: "migrationmodeler_EdgeStyle" = None, migrationmodeler_Color53: "migrationmodeler_BorderedStyle" = None, migrationmodeler_Color56: "migrationmodeler_BasicLabelStyle" = None, migrationmodeler_Color58: "migrationmodeler_Dot" = None, migrationmodeler_Color60: "migrationmodeler_GaugeSection" = None, migrationmodeler_Color63: "migrationmodeler_GaugeSection" = None, migrationmodeler_Color65: "migrationmodeler_FlatContainerStyle" = None, migrationmodeler_Color68: "migrationmodeler_FlatContainerStyle" = None, migrationmodeler_Color70: "migrationmodeler_ShapeContainerStyle" = None, migrationmodeler_Color72: "migrationmodeler_Square" = None, migrationmodeler_Color74: "migrationmodeler_Ellipse" = None, migrationmodeler_Color76: "migrationmodeler_Lozenge" = None, migrationmodeler_Color82: "migrationmodeler_Note" = None, migrationmodeler_Color78: "migrationmodeler_BundledImage" = None):
        self.red = red
        self.green = green
        self.blue = blue
        self.migrationmodeler_Color = migrationmodeler_Color
        self.migrationmodeler_Color53 = migrationmodeler_Color53
        self.migrationmodeler_Color56 = migrationmodeler_Color56
        self.migrationmodeler_Color58 = migrationmodeler_Color58
        self.migrationmodeler_Color60 = migrationmodeler_Color60
        self.migrationmodeler_Color63 = migrationmodeler_Color63
        self.migrationmodeler_Color65 = migrationmodeler_Color65
        self.migrationmodeler_Color68 = migrationmodeler_Color68
        self.migrationmodeler_Color70 = migrationmodeler_Color70
        self.migrationmodeler_Color72 = migrationmodeler_Color72
        self.migrationmodeler_Color74 = migrationmodeler_Color74
        self.migrationmodeler_Color76 = migrationmodeler_Color76
        self.migrationmodeler_Color82 = migrationmodeler_Color82
        self.migrationmodeler_Color78 = migrationmodeler_Color78
        
    @property
    def red(self) -> int:
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red

    @property
    def green(self) -> int:
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green

    @property
    def blue(self) -> int:
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue

    @property
    def migrationmodeler_Color74(self):
        return self.__migrationmodeler_Color74

    @migrationmodeler_Color74.setter
    def migrationmodeler_Color74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color74", None)
        self.__migrationmodeler_Color74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Ellipse"):
                opp_val = getattr(old_value, "migrationmodeler_Ellipse", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Ellipse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Ellipse"):
                opp_val = getattr(value, "migrationmodeler_Ellipse", None)
                setattr(value, "migrationmodeler_Ellipse", self)

    @property
    def migrationmodeler_Color63(self):
        return self.__migrationmodeler_Color63

    @migrationmodeler_Color63.setter
    def migrationmodeler_Color63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color63", None)
        self.__migrationmodeler_Color63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_GaugeSection62"):
                opp_val = getattr(old_value, "migrationmodeler_GaugeSection62", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_GaugeSection62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_GaugeSection62"):
                opp_val = getattr(value, "migrationmodeler_GaugeSection62", None)
                setattr(value, "migrationmodeler_GaugeSection62", self)

    @property
    def migrationmodeler_Color68(self):
        return self.__migrationmodeler_Color68

    @migrationmodeler_Color68.setter
    def migrationmodeler_Color68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color68", None)
        self.__migrationmodeler_Color68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_FlatContainerStyle67"):
                opp_val = getattr(old_value, "migrationmodeler_FlatContainerStyle67", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_FlatContainerStyle67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_FlatContainerStyle67"):
                opp_val = getattr(value, "migrationmodeler_FlatContainerStyle67", None)
                setattr(value, "migrationmodeler_FlatContainerStyle67", self)

    @property
    def migrationmodeler_Color53(self):
        return self.__migrationmodeler_Color53

    @migrationmodeler_Color53.setter
    def migrationmodeler_Color53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color53", None)
        self.__migrationmodeler_Color53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_BorderedStyle"):
                opp_val = getattr(old_value, "migrationmodeler_BorderedStyle", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_BorderedStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_BorderedStyle"):
                opp_val = getattr(value, "migrationmodeler_BorderedStyle", None)
                setattr(value, "migrationmodeler_BorderedStyle", self)

    @property
    def migrationmodeler_Color65(self):
        return self.__migrationmodeler_Color65

    @migrationmodeler_Color65.setter
    def migrationmodeler_Color65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color65", None)
        self.__migrationmodeler_Color65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_FlatContainerStyle"):
                opp_val = getattr(old_value, "migrationmodeler_FlatContainerStyle", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_FlatContainerStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_FlatContainerStyle"):
                opp_val = getattr(value, "migrationmodeler_FlatContainerStyle", None)
                setattr(value, "migrationmodeler_FlatContainerStyle", self)

    @property
    def migrationmodeler_Color76(self):
        return self.__migrationmodeler_Color76

    @migrationmodeler_Color76.setter
    def migrationmodeler_Color76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color76", None)
        self.__migrationmodeler_Color76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Lozenge"):
                opp_val = getattr(old_value, "migrationmodeler_Lozenge", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Lozenge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Lozenge"):
                opp_val = getattr(value, "migrationmodeler_Lozenge", None)
                setattr(value, "migrationmodeler_Lozenge", self)

    @property
    def migrationmodeler_Color60(self):
        return self.__migrationmodeler_Color60

    @migrationmodeler_Color60.setter
    def migrationmodeler_Color60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color60", None)
        self.__migrationmodeler_Color60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_GaugeSection"):
                opp_val = getattr(old_value, "migrationmodeler_GaugeSection", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_GaugeSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_GaugeSection"):
                opp_val = getattr(value, "migrationmodeler_GaugeSection", None)
                setattr(value, "migrationmodeler_GaugeSection", self)

    @property
    def migrationmodeler_Color72(self):
        return self.__migrationmodeler_Color72

    @migrationmodeler_Color72.setter
    def migrationmodeler_Color72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color72", None)
        self.__migrationmodeler_Color72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Square"):
                opp_val = getattr(old_value, "migrationmodeler_Square", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Square", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Square"):
                opp_val = getattr(value, "migrationmodeler_Square", None)
                setattr(value, "migrationmodeler_Square", self)

    @property
    def migrationmodeler_Color58(self):
        return self.__migrationmodeler_Color58

    @migrationmodeler_Color58.setter
    def migrationmodeler_Color58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color58", None)
        self.__migrationmodeler_Color58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Dot"):
                opp_val = getattr(old_value, "migrationmodeler_Dot", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Dot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Dot"):
                opp_val = getattr(value, "migrationmodeler_Dot", None)
                setattr(value, "migrationmodeler_Dot", self)

    @property
    def migrationmodeler_Color70(self):
        return self.__migrationmodeler_Color70

    @migrationmodeler_Color70.setter
    def migrationmodeler_Color70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color70", None)
        self.__migrationmodeler_Color70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_ShapeContainerStyle"):
                opp_val = getattr(old_value, "migrationmodeler_ShapeContainerStyle", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_ShapeContainerStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_ShapeContainerStyle"):
                opp_val = getattr(value, "migrationmodeler_ShapeContainerStyle", None)
                setattr(value, "migrationmodeler_ShapeContainerStyle", self)

    @property
    def migrationmodeler_Color82(self):
        return self.__migrationmodeler_Color82

    @migrationmodeler_Color82.setter
    def migrationmodeler_Color82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color82", None)
        self.__migrationmodeler_Color82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Note"):
                opp_val = getattr(old_value, "migrationmodeler_Note", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Note", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Note"):
                opp_val = getattr(value, "migrationmodeler_Note", None)
                setattr(value, "migrationmodeler_Note", self)

    @property
    def migrationmodeler_Color56(self):
        return self.__migrationmodeler_Color56

    @migrationmodeler_Color56.setter
    def migrationmodeler_Color56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color56", None)
        self.__migrationmodeler_Color56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_BasicLabelStyle55"):
                opp_val = getattr(old_value, "migrationmodeler_BasicLabelStyle55", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_BasicLabelStyle55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_BasicLabelStyle55"):
                opp_val = getattr(value, "migrationmodeler_BasicLabelStyle55", None)
                setattr(value, "migrationmodeler_BasicLabelStyle55", self)

    @property
    def migrationmodeler_Color78(self):
        return self.__migrationmodeler_Color78

    @migrationmodeler_Color78.setter
    def migrationmodeler_Color78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color78", None)
        self.__migrationmodeler_Color78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_BundledImage"):
                opp_val = getattr(old_value, "migrationmodeler_BundledImage", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_BundledImage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_BundledImage"):
                opp_val = getattr(value, "migrationmodeler_BundledImage", None)
                setattr(value, "migrationmodeler_BundledImage", self)

    @property
    def migrationmodeler_Color(self):
        return self.__migrationmodeler_Color

    @migrationmodeler_Color.setter
    def migrationmodeler_Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Color__migrationmodeler_Color", None)
        self.__migrationmodeler_Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_EdgeStyle42"):
                opp_val = getattr(old_value, "migrationmodeler_EdgeStyle42", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_EdgeStyle42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_EdgeStyle42"):
                opp_val = getattr(value, "migrationmodeler_EdgeStyle42", None)
                setattr(value, "migrationmodeler_EdgeStyle42", self)

class migrationmodeler_ContainerStyle(BorderedStyle, LabelStyle):

    pass
class AbstractNodeRepresentation:

    pass
class migrationmodeler_NodeStyle(BorderedStyle, LabelStyle):

    def __init__(self, labelPosition: str, hideLabelByDefault: bool, migrationmodeler_NodeStyle: "migrationmodeler_AbstractNodeRepresentation" = None):
        self.labelPosition = labelPosition
        self.hideLabelByDefault = hideLabelByDefault
        self.migrationmodeler_NodeStyle = migrationmodeler_NodeStyle
        
    @property
    def labelPosition(self) -> str:
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition

    @property
    def hideLabelByDefault(self) -> bool:
        return self.__hideLabelByDefault

    @hideLabelByDefault.setter
    def hideLabelByDefault(self, hideLabelByDefault: bool):
        self.__hideLabelByDefault = hideLabelByDefault

    @property
    def migrationmodeler_NodeStyle(self):
        return self.__migrationmodeler_NodeStyle

    @migrationmodeler_NodeStyle.setter
    def migrationmodeler_NodeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_NodeStyle__migrationmodeler_NodeStyle", None)
        self.__migrationmodeler_NodeStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_AbstractNodeRepresentation38"):
                opp_val = getattr(old_value, "migrationmodeler_AbstractNodeRepresentation38", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_AbstractNodeRepresentation38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_AbstractNodeRepresentation38"):
                opp_val = getattr(value, "migrationmodeler_AbstractNodeRepresentation38", None)
                setattr(value, "migrationmodeler_AbstractNodeRepresentation38", self)

class migrationmodeler_AbstractNodeRepresentation(AbstractRepresentation):

    pass
class migrationmodeler_EdgeStyle:

    def __init__(self, routingStyle: str, migrationmodeler_EdgeStyle: "migrationmodeler_EdgeRepresentation" = None, migrationmodeler_EdgeStyle42: "migrationmodeler_Color" = None, migrationmodeler_EdgeStyle44: "migrationmodeler_BasicLabelStyle" = None, migrationmodeler_EdgeStyle46: "migrationmodeler_BasicLabelStyle" = None, migrationmodeler_EdgeStyle49: "migrationmodeler_BasicLabelStyle" = None):
        self.routingStyle = routingStyle
        self.migrationmodeler_EdgeStyle = migrationmodeler_EdgeStyle
        self.migrationmodeler_EdgeStyle42 = migrationmodeler_EdgeStyle42
        self.migrationmodeler_EdgeStyle44 = migrationmodeler_EdgeStyle44
        self.migrationmodeler_EdgeStyle46 = migrationmodeler_EdgeStyle46
        self.migrationmodeler_EdgeStyle49 = migrationmodeler_EdgeStyle49
        
    @property
    def routingStyle(self) -> str:
        return self.__routingStyle

    @routingStyle.setter
    def routingStyle(self, routingStyle: str):
        self.__routingStyle = routingStyle

    @property
    def migrationmodeler_EdgeStyle(self):
        return self.__migrationmodeler_EdgeStyle

    @migrationmodeler_EdgeStyle.setter
    def migrationmodeler_EdgeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_EdgeStyle__migrationmodeler_EdgeStyle", None)
        self.__migrationmodeler_EdgeStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_EdgeRepresentation34"):
                opp_val = getattr(old_value, "migrationmodeler_EdgeRepresentation34", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_EdgeRepresentation34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_EdgeRepresentation34"):
                opp_val = getattr(value, "migrationmodeler_EdgeRepresentation34", None)
                setattr(value, "migrationmodeler_EdgeRepresentation34", self)

    @property
    def migrationmodeler_EdgeStyle46(self):
        return self.__migrationmodeler_EdgeStyle46

    @migrationmodeler_EdgeStyle46.setter
    def migrationmodeler_EdgeStyle46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_EdgeStyle__migrationmodeler_EdgeStyle46", None)
        self.__migrationmodeler_EdgeStyle46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_BasicLabelStyle47"):
                opp_val = getattr(old_value, "migrationmodeler_BasicLabelStyle47", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_BasicLabelStyle47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_BasicLabelStyle47"):
                opp_val = getattr(value, "migrationmodeler_BasicLabelStyle47", None)
                setattr(value, "migrationmodeler_BasicLabelStyle47", self)

    @property
    def migrationmodeler_EdgeStyle49(self):
        return self.__migrationmodeler_EdgeStyle49

    @migrationmodeler_EdgeStyle49.setter
    def migrationmodeler_EdgeStyle49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_EdgeStyle__migrationmodeler_EdgeStyle49", None)
        self.__migrationmodeler_EdgeStyle49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_BasicLabelStyle50"):
                opp_val = getattr(old_value, "migrationmodeler_BasicLabelStyle50", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_BasicLabelStyle50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_BasicLabelStyle50"):
                opp_val = getattr(value, "migrationmodeler_BasicLabelStyle50", None)
                setattr(value, "migrationmodeler_BasicLabelStyle50", self)

    @property
    def migrationmodeler_EdgeStyle44(self):
        return self.__migrationmodeler_EdgeStyle44

    @migrationmodeler_EdgeStyle44.setter
    def migrationmodeler_EdgeStyle44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_EdgeStyle__migrationmodeler_EdgeStyle44", None)
        self.__migrationmodeler_EdgeStyle44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_BasicLabelStyle"):
                opp_val = getattr(old_value, "migrationmodeler_BasicLabelStyle", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_BasicLabelStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_BasicLabelStyle"):
                opp_val = getattr(value, "migrationmodeler_BasicLabelStyle", None)
                setattr(value, "migrationmodeler_BasicLabelStyle", self)

    @property
    def migrationmodeler_EdgeStyle42(self):
        return self.__migrationmodeler_EdgeStyle42

    @migrationmodeler_EdgeStyle42.setter
    def migrationmodeler_EdgeStyle42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_EdgeStyle__migrationmodeler_EdgeStyle42", None)
        self.__migrationmodeler_EdgeStyle42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Color"):
                opp_val = getattr(old_value, "migrationmodeler_Color", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Color"):
                opp_val = getattr(value, "migrationmodeler_Color", None)
                setattr(value, "migrationmodeler_Color", self)

class migrationmodeler_Point:

    def __init__(self, x: int, y: int, migrationmodeler_Point: "migrationmodeler_EdgeRepresentation" = None):
        self.x = x
        self.y = y
        self.migrationmodeler_Point = migrationmodeler_Point
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def migrationmodeler_Point(self):
        return self.__migrationmodeler_Point

    @migrationmodeler_Point.setter
    def migrationmodeler_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Point__migrationmodeler_Point", None)
        self.__migrationmodeler_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_EdgeRepresentation32"):
                opp_val = getattr(old_value, "migrationmodeler_EdgeRepresentation32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_EdgeRepresentation32"):
                opp_val = getattr(value, "migrationmodeler_EdgeRepresentation32", None)
                if opp_val is None:
                    setattr(value, "migrationmodeler_EdgeRepresentation32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Representation:

    pass
class migrationmodeler_Layout:

    def __init__(self, x: int, y: int, width: int, height: int, migrationmodeler_Layout: "migrationmodeler_AbstractRepresentation" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.migrationmodeler_Layout = migrationmodeler_Layout
        
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
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def migrationmodeler_Layout(self):
        return self.__migrationmodeler_Layout

    @migrationmodeler_Layout.setter
    def migrationmodeler_Layout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Layout__migrationmodeler_Layout", None)
        self.__migrationmodeler_Layout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_AbstractRepresentation"):
                opp_val = getattr(old_value, "migrationmodeler_AbstractRepresentation", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_AbstractRepresentation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_AbstractRepresentation"):
                opp_val = getattr(value, "migrationmodeler_AbstractRepresentation", None)
                setattr(value, "migrationmodeler_AbstractRepresentation", self)

class migrationmodeler_AbstractRepresentation(ABC):

    def __init__(self, mappingId: str, displayed: bool, hidden: bool, pinned: bool, migrationmodeler_AbstractRepresentation: "migrationmodeler_Layout" = None):
        self.mappingId = mappingId
        self.displayed = displayed
        self.hidden = hidden
        self.pinned = pinned
        self.migrationmodeler_AbstractRepresentation = migrationmodeler_AbstractRepresentation
        
    @property
    def displayed(self) -> bool:
        return self.__displayed

    @displayed.setter
    def displayed(self, displayed: bool):
        self.__displayed = displayed

    @property
    def mappingId(self) -> str:
        return self.__mappingId

    @mappingId.setter
    def mappingId(self, mappingId: str):
        self.__mappingId = mappingId

    @property
    def hidden(self) -> bool:
        return self.__hidden

    @hidden.setter
    def hidden(self, hidden: bool):
        self.__hidden = hidden

    @property
    def pinned(self) -> bool:
        return self.__pinned

    @pinned.setter
    def pinned(self, pinned: bool):
        self.__pinned = pinned

    @property
    def migrationmodeler_AbstractRepresentation(self):
        return self.__migrationmodeler_AbstractRepresentation

    @migrationmodeler_AbstractRepresentation.setter
    def migrationmodeler_AbstractRepresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_AbstractRepresentation__migrationmodeler_AbstractRepresentation", None)
        self.__migrationmodeler_AbstractRepresentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Layout"):
                opp_val = getattr(old_value, "migrationmodeler_Layout", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Layout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Layout"):
                opp_val = getattr(value, "migrationmodeler_Layout", None)
                setattr(value, "migrationmodeler_Layout", self)

class migrationmodeler_EdgeRepresentation(AbstractRepresentation):

    pass
class migrationmodeler_ContainerRepresentation(AbstractRepresentation):

    def __init__(self, autoSized: bool, migrationmodeler_ContainerRepresentation: "migrationmodeler_Container" = None, migrationmodeler_ContainerRepresentation40: "migrationmodeler_ContainerStyle" = None):
        self.autoSized = autoSized
        self.migrationmodeler_ContainerRepresentation = migrationmodeler_ContainerRepresentation
        self.migrationmodeler_ContainerRepresentation40 = migrationmodeler_ContainerRepresentation40
        
    @property
    def autoSized(self) -> bool:
        return self.__autoSized

    @autoSized.setter
    def autoSized(self, autoSized: bool):
        self.__autoSized = autoSized

    @property
    def migrationmodeler_ContainerRepresentation40(self):
        return self.__migrationmodeler_ContainerRepresentation40

    @migrationmodeler_ContainerRepresentation40.setter
    def migrationmodeler_ContainerRepresentation40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_ContainerRepresentation__migrationmodeler_ContainerRepresentation40", None)
        self.__migrationmodeler_ContainerRepresentation40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_ContainerStyle"):
                opp_val = getattr(old_value, "migrationmodeler_ContainerStyle", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_ContainerStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_ContainerStyle"):
                opp_val = getattr(value, "migrationmodeler_ContainerStyle", None)
                setattr(value, "migrationmodeler_ContainerStyle", self)

    @property
    def migrationmodeler_ContainerRepresentation(self):
        return self.__migrationmodeler_ContainerRepresentation

    @migrationmodeler_ContainerRepresentation.setter
    def migrationmodeler_ContainerRepresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_ContainerRepresentation__migrationmodeler_ContainerRepresentation", None)
        self.__migrationmodeler_ContainerRepresentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Container13"):
                opp_val = getattr(old_value, "migrationmodeler_Container13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Container13"):
                opp_val = getattr(value, "migrationmodeler_Container13", None)
                if opp_val is None:
                    setattr(value, "migrationmodeler_Container13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class migrationmodeler_BorderedRepresentation(AbstractNodeRepresentation):

    pass
class migrationmodeler_NodeRepresentation(AbstractNodeRepresentation):

    pass
class AbstractNode:

    pass
class migrationmodeler_Bordered(AbstractNode):

    pass
class migrationmodeler_Node(AbstractNode):

    pass
class GraphicalElement:

    pass
class migrationmodeler_Container(GraphicalElement):

    pass
class migrationmodeler_AbstractNode(GraphicalElement):

    pass
class migrationmodeler_GraphicalElement(ABC):

    def __init__(self, id: str, migrationmodeler_GraphicalElement: "migrationmodeler_Container" = None, migrationmodeler_GraphicalElement20: "migrationmodeler_Edge" = None, migrationmodeler_GraphicalElement23: "migrationmodeler_Edge" = None, migrationmodeler_GraphicalElement27: "migrationmodeler_EdgeRepresentation" = None, migrationmodeler_GraphicalElement30: "migrationmodeler_EdgeRepresentation" = None):
        self.id = id
        self.migrationmodeler_GraphicalElement = migrationmodeler_GraphicalElement
        self.migrationmodeler_GraphicalElement20 = migrationmodeler_GraphicalElement20
        self.migrationmodeler_GraphicalElement23 = migrationmodeler_GraphicalElement23
        self.migrationmodeler_GraphicalElement27 = migrationmodeler_GraphicalElement27
        self.migrationmodeler_GraphicalElement30 = migrationmodeler_GraphicalElement30
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def migrationmodeler_GraphicalElement23(self):
        return self.__migrationmodeler_GraphicalElement23

    @migrationmodeler_GraphicalElement23.setter
    def migrationmodeler_GraphicalElement23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_GraphicalElement__migrationmodeler_GraphicalElement23", None)
        self.__migrationmodeler_GraphicalElement23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Edge22"):
                opp_val = getattr(old_value, "migrationmodeler_Edge22", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Edge22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Edge22"):
                opp_val = getattr(value, "migrationmodeler_Edge22", None)
                setattr(value, "migrationmodeler_Edge22", self)

    @property
    def migrationmodeler_GraphicalElement(self):
        return self.__migrationmodeler_GraphicalElement

    @migrationmodeler_GraphicalElement.setter
    def migrationmodeler_GraphicalElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_GraphicalElement__migrationmodeler_GraphicalElement", None)
        self.__migrationmodeler_GraphicalElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Container15"):
                opp_val = getattr(old_value, "migrationmodeler_Container15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Container15"):
                opp_val = getattr(value, "migrationmodeler_Container15", None)
                if opp_val is None:
                    setattr(value, "migrationmodeler_Container15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def migrationmodeler_GraphicalElement20(self):
        return self.__migrationmodeler_GraphicalElement20

    @migrationmodeler_GraphicalElement20.setter
    def migrationmodeler_GraphicalElement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_GraphicalElement__migrationmodeler_GraphicalElement20", None)
        self.__migrationmodeler_GraphicalElement20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Edge19"):
                opp_val = getattr(old_value, "migrationmodeler_Edge19", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_Edge19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Edge19"):
                opp_val = getattr(value, "migrationmodeler_Edge19", None)
                setattr(value, "migrationmodeler_Edge19", self)

    @property
    def migrationmodeler_GraphicalElement27(self):
        return self.__migrationmodeler_GraphicalElement27

    @migrationmodeler_GraphicalElement27.setter
    def migrationmodeler_GraphicalElement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_GraphicalElement__migrationmodeler_GraphicalElement27", None)
        self.__migrationmodeler_GraphicalElement27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_EdgeRepresentation26"):
                opp_val = getattr(old_value, "migrationmodeler_EdgeRepresentation26", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_EdgeRepresentation26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_EdgeRepresentation26"):
                opp_val = getattr(value, "migrationmodeler_EdgeRepresentation26", None)
                setattr(value, "migrationmodeler_EdgeRepresentation26", self)

    @property
    def migrationmodeler_GraphicalElement30(self):
        return self.__migrationmodeler_GraphicalElement30

    @migrationmodeler_GraphicalElement30.setter
    def migrationmodeler_GraphicalElement30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_GraphicalElement__migrationmodeler_GraphicalElement30", None)
        self.__migrationmodeler_GraphicalElement30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_EdgeRepresentation29"):
                opp_val = getattr(old_value, "migrationmodeler_EdgeRepresentation29", None)
                if opp_val == self:
                    setattr(old_value, "migrationmodeler_EdgeRepresentation29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_EdgeRepresentation29"):
                opp_val = getattr(value, "migrationmodeler_EdgeRepresentation29", None)
                setattr(value, "migrationmodeler_EdgeRepresentation29", self)

class migrationmodeler_Layer:

    def __init__(self, id: str, activated: bool, migrationmodeler_Layer: "migrationmodeler_Diagram" = None):
        self.id = id
        self.activated = activated
        self.migrationmodeler_Layer = migrationmodeler_Layer
        
    @property
    def activated(self) -> bool:
        return self.__activated

    @activated.setter
    def activated(self, activated: bool):
        self.__activated = activated

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def migrationmodeler_Layer(self):
        return self.__migrationmodeler_Layer

    @migrationmodeler_Layer.setter
    def migrationmodeler_Layer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Layer__migrationmodeler_Layer", None)
        self.__migrationmodeler_Layer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Diagram8"):
                opp_val = getattr(old_value, "migrationmodeler_Diagram8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Diagram8"):
                opp_val = getattr(value, "migrationmodeler_Diagram8", None)
                if opp_val is None:
                    setattr(value, "migrationmodeler_Diagram8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class migrationmodeler_Filter:

    def __init__(self, id: str, activated: bool, migrationmodeler_Filter: "migrationmodeler_Diagram" = None):
        self.id = id
        self.activated = activated
        self.migrationmodeler_Filter = migrationmodeler_Filter
        
    @property
    def activated(self) -> bool:
        return self.__activated

    @activated.setter
    def activated(self, activated: bool):
        self.__activated = activated

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def migrationmodeler_Filter(self):
        return self.__migrationmodeler_Filter

    @migrationmodeler_Filter.setter
    def migrationmodeler_Filter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_migrationmodeler_Filter__migrationmodeler_Filter", None)
        self.__migrationmodeler_Filter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "migrationmodeler_Diagram6"):
                opp_val = getattr(old_value, "migrationmodeler_Diagram6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "migrationmodeler_Diagram6"):
                opp_val = getattr(value, "migrationmodeler_Diagram6", None)
                if opp_val is None:
                    setattr(value, "migrationmodeler_Diagram6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class migrationmodeler_Edge(GraphicalElement):

    pass
class migrationmodeler_Diagram(Representation):

    pass