from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LineStyle(Enum):
    Solid = "Solid"
    Dash = "Dash"
    Dot = "Dot"


############################################
# Definition of Classes
############################################

class ChartElement:

    pass
class vml_Point(ChartElement):

    pass
class vml_Bar(ChartElement):

    pass
class Chart:

    pass
class vml_Scatter(Chart):

    pass
class vml_LineChart(Chart):

    pass
class vml_StackBarChart(Chart):

    pass
class vml_BarChart(Chart):

    pass
class vml_Category:

    def __init__(self, category: str, vml_Category: "vml_StackBarChart" = None, vml_Category65: "vml_StackBars" = None):
        self.category = category
        self.vml_Category = vml_Category
        self.vml_Category65 = vml_Category65
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def vml_Category(self):
        return self.__vml_Category

    @vml_Category.setter
    def vml_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Category__vml_Category", None)
        self.__vml_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_StackBarChart62"):
                opp_val = getattr(old_value, "vml_StackBarChart62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_StackBarChart62"):
                opp_val = getattr(value, "vml_StackBarChart62", None)
                if opp_val is None:
                    setattr(value, "vml_StackBarChart62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vml_Category65(self):
        return self.__vml_Category65

    @vml_Category65.setter
    def vml_Category65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Category__vml_Category65", None)
        self.__vml_Category65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_StackBars64"):
                opp_val = getattr(old_value, "vml_StackBars64", None)
                if opp_val == self:
                    setattr(old_value, "vml_StackBars64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_StackBars64"):
                opp_val = getattr(value, "vml_StackBars64", None)
                setattr(value, "vml_StackBars64", self)

class vml_StackBars(ChartElement):

    pass
class DiagramElement:

    pass
class vml_ChartElement(DiagramElement):

    def __init__(self, ID: str, xValue: str, yValue: str):
        self.ID = ID
        self.xValue = xValue
        self.yValue = yValue
        
    @property
    def xValue(self) -> str:
        return self.__xValue

    @xValue.setter
    def xValue(self, xValue: str):
        self.__xValue = xValue

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def yValue(self) -> str:
        return self.__yValue

    @yValue.setter
    def yValue(self, yValue: str):
        self.__yValue = yValue

class vml_Slice(DiagramElement):

    def __init__(self, title: str, value: int, vml_Slice: "vml_Pie" = None):
        self.title = title
        self.value = value
        self.vml_Slice = vml_Slice
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def vml_Slice(self):
        return self.__vml_Slice

    @vml_Slice.setter
    def vml_Slice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Slice__vml_Slice", None)
        self.__vml_Slice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Pie"):
                opp_val = getattr(old_value, "vml_Pie", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Pie"):
                opp_val = getattr(value, "vml_Pie", None)
                if opp_val is None:
                    setattr(value, "vml_Pie", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Diagram:

    pass
class vml_Graph(Diagram):

    def __init__(self, title: str, ID: str, vml_Graph: set["vml_Node"] = None, vml_Graph49: set["vml_Edge"] = None, vml_Graph51: "vml_GraphStyle" = None):
        self.title = title
        self.ID = ID
        self.vml_Graph = vml_Graph if vml_Graph is not None else set()
        self.vml_Graph49 = vml_Graph49 if vml_Graph49 is not None else set()
        self.vml_Graph51 = vml_Graph51
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def vml_Graph(self):
        return self.__vml_Graph

    @vml_Graph.setter
    def vml_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Graph__vml_Graph", None)
        self.__vml_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vml_Node47"):
                    opp_val = getattr(item, "vml_Node47", None)
                    
                    if opp_val == self:
                        setattr(item, "vml_Node47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vml_Node47"):
                    opp_val = getattr(item, "vml_Node47", None)
                    
                    setattr(item, "vml_Node47", self)
                    

    @property
    def vml_Graph51(self):
        return self.__vml_Graph51

    @vml_Graph51.setter
    def vml_Graph51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Graph__vml_Graph51", None)
        self.__vml_Graph51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_GraphStyle"):
                opp_val = getattr(old_value, "vml_GraphStyle", None)
                if opp_val == self:
                    setattr(old_value, "vml_GraphStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_GraphStyle"):
                opp_val = getattr(value, "vml_GraphStyle", None)
                setattr(value, "vml_GraphStyle", self)

    @property
    def vml_Graph49(self):
        return self.__vml_Graph49

    @vml_Graph49.setter
    def vml_Graph49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Graph__vml_Graph49", None)
        self.__vml_Graph49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vml_Edge"):
                    opp_val = getattr(item, "vml_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "vml_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vml_Edge"):
                    opp_val = getattr(item, "vml_Edge", None)
                    
                    setattr(item, "vml_Edge", self)
                    

class vml_Chart(Diagram):

    def __init__(self, ID: str, title: str, xTitle: str, yTitle: str, vml_Chart: "vml_ChartWithAxisStyle" = None):
        self.ID = ID
        self.title = title
        self.xTitle = xTitle
        self.yTitle = yTitle
        self.vml_Chart = vml_Chart
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def xTitle(self) -> str:
        return self.__xTitle

    @xTitle.setter
    def xTitle(self, xTitle: str):
        self.__xTitle = xTitle

    @property
    def yTitle(self) -> str:
        return self.__yTitle

    @yTitle.setter
    def yTitle(self, yTitle: str):
        self.__yTitle = yTitle

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def vml_Chart(self):
        return self.__vml_Chart

    @vml_Chart.setter
    def vml_Chart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Chart__vml_Chart", None)
        self.__vml_Chart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_ChartWithAxisStyle"):
                opp_val = getattr(old_value, "vml_ChartWithAxisStyle", None)
                if opp_val == self:
                    setattr(old_value, "vml_ChartWithAxisStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_ChartWithAxisStyle"):
                opp_val = getattr(value, "vml_ChartWithAxisStyle", None)
                setattr(value, "vml_ChartWithAxisStyle", self)

class vml_Pie(Diagram):

    def __init__(self, title: str, identifier: str, vml_Pie: set["vml_Slice"] = None, vml_Pie45: "vml_ChartWithoutAxisStyle" = None):
        self.title = title
        self.identifier = identifier
        self.vml_Pie = vml_Pie if vml_Pie is not None else set()
        self.vml_Pie45 = vml_Pie45
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def vml_Pie45(self):
        return self.__vml_Pie45

    @vml_Pie45.setter
    def vml_Pie45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Pie__vml_Pie45", None)
        self.__vml_Pie45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_ChartWithoutAxisStyle"):
                opp_val = getattr(old_value, "vml_ChartWithoutAxisStyle", None)
                if opp_val == self:
                    setattr(old_value, "vml_ChartWithoutAxisStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_ChartWithoutAxisStyle"):
                opp_val = getattr(value, "vml_ChartWithoutAxisStyle", None)
                setattr(value, "vml_ChartWithoutAxisStyle", self)

    @property
    def vml_Pie(self):
        return self.__vml_Pie

    @vml_Pie.setter
    def vml_Pie(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Pie__vml_Pie", None)
        self.__vml_Pie = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vml_Slice"):
                    opp_val = getattr(item, "vml_Slice", None)
                    
                    if opp_val == self:
                        setattr(item, "vml_Slice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vml_Slice"):
                    opp_val = getattr(item, "vml_Slice", None)
                    
                    setattr(item, "vml_Slice", self)
                    

class vml_DiagramElement(ABC):

    pass
class vml_Edge(DiagramElement):

    def __init__(self, relation: str, vml_Edge: "vml_Graph" = None, Edge: "vml_Node" = None, Edge54: "vml_Node" = None, outgoing: "vml_Node" = None, incoming: "vml_Node" = None):
        self.relation = relation
        self.vml_Edge = vml_Edge
        self.Edge = Edge
        self.Edge54 = Edge54
        self.outgoing = outgoing
        self.incoming = incoming
        
    @property
    def relation(self) -> str:
        return self.__relation

    @relation.setter
    def relation(self, relation: str):
        self.__relation = relation

    @property
    def outgoing(self):
        return self.__outgoing

    @outgoing.setter
    def outgoing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Edge__outgoing", None)
        self.__outgoing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def Edge54(self):
        return self.__Edge54

    @Edge54.setter
    def Edge54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Edge__Edge54", None)
        self.__Edge54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vml_Edge(self):
        return self.__vml_Edge

    @vml_Edge.setter
    def vml_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Edge__vml_Edge", None)
        self.__vml_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Graph49"):
                opp_val = getattr(old_value, "vml_Graph49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Graph49"):
                opp_val = getattr(value, "vml_Graph49", None)
                if opp_val is None:
                    setattr(value, "vml_Graph49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Edge(self):
        return self.__Edge

    @Edge.setter
    def Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Edge__Edge", None)
        self.__Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incoming(self):
        return self.__incoming

    @incoming.setter
    def incoming(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Edge__incoming", None)
        self.__incoming = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node57"):
                opp_val = getattr(old_value, "Node57", None)
                if opp_val == self:
                    setattr(old_value, "Node57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node57"):
                opp_val = getattr(value, "Node57", None)
                setattr(value, "Node57", self)

class vml_Color:

    def __init__(self, name: str, red: int, green: int, blue: int, vml_Color27: "vml_NodeStyle" = None, vml_Color34: "vml_EdgeStyle" = None, vml_Color: "vml_NodeStyle" = None, vml_Color18: "vml_NodeStyle" = None, vml_Color21: "vml_NodeStyle" = None, vml_Color24: "vml_NodeStyle" = None, vml_Color37: "vml_EdgeStyle" = None):
        self.name = name
        self.red = red
        self.green = green
        self.blue = blue
        self.vml_Color27 = vml_Color27
        self.vml_Color34 = vml_Color34
        self.vml_Color = vml_Color
        self.vml_Color18 = vml_Color18
        self.vml_Color21 = vml_Color21
        self.vml_Color24 = vml_Color24
        self.vml_Color37 = vml_Color37
        
    @property
    def red(self) -> int:
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red

    @property
    def blue(self) -> int:
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue

    @property
    def green(self) -> int:
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vml_Color27(self):
        return self.__vml_Color27

    @vml_Color27.setter
    def vml_Color27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Color__vml_Color27", None)
        self.__vml_Color27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_NodeStyle26"):
                opp_val = getattr(old_value, "vml_NodeStyle26", None)
                if opp_val == self:
                    setattr(old_value, "vml_NodeStyle26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_NodeStyle26"):
                opp_val = getattr(value, "vml_NodeStyle26", None)
                setattr(value, "vml_NodeStyle26", self)

    @property
    def vml_Color24(self):
        return self.__vml_Color24

    @vml_Color24.setter
    def vml_Color24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Color__vml_Color24", None)
        self.__vml_Color24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_NodeStyle23"):
                opp_val = getattr(old_value, "vml_NodeStyle23", None)
                if opp_val == self:
                    setattr(old_value, "vml_NodeStyle23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_NodeStyle23"):
                opp_val = getattr(value, "vml_NodeStyle23", None)
                setattr(value, "vml_NodeStyle23", self)

    @property
    def vml_Color21(self):
        return self.__vml_Color21

    @vml_Color21.setter
    def vml_Color21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Color__vml_Color21", None)
        self.__vml_Color21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_NodeStyle20"):
                opp_val = getattr(old_value, "vml_NodeStyle20", None)
                if opp_val == self:
                    setattr(old_value, "vml_NodeStyle20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_NodeStyle20"):
                opp_val = getattr(value, "vml_NodeStyle20", None)
                setattr(value, "vml_NodeStyle20", self)

    @property
    def vml_Color(self):
        return self.__vml_Color

    @vml_Color.setter
    def vml_Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Color__vml_Color", None)
        self.__vml_Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_NodeStyle"):
                opp_val = getattr(old_value, "vml_NodeStyle", None)
                if opp_val == self:
                    setattr(old_value, "vml_NodeStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_NodeStyle"):
                opp_val = getattr(value, "vml_NodeStyle", None)
                setattr(value, "vml_NodeStyle", self)

    @property
    def vml_Color34(self):
        return self.__vml_Color34

    @vml_Color34.setter
    def vml_Color34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Color__vml_Color34", None)
        self.__vml_Color34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_EdgeStyle33"):
                opp_val = getattr(old_value, "vml_EdgeStyle33", None)
                if opp_val == self:
                    setattr(old_value, "vml_EdgeStyle33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_EdgeStyle33"):
                opp_val = getattr(value, "vml_EdgeStyle33", None)
                setattr(value, "vml_EdgeStyle33", self)

    @property
    def vml_Color18(self):
        return self.__vml_Color18

    @vml_Color18.setter
    def vml_Color18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Color__vml_Color18", None)
        self.__vml_Color18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_NodeStyle17"):
                opp_val = getattr(old_value, "vml_NodeStyle17", None)
                if opp_val == self:
                    setattr(old_value, "vml_NodeStyle17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_NodeStyle17"):
                opp_val = getattr(value, "vml_NodeStyle17", None)
                setattr(value, "vml_NodeStyle17", self)

    @property
    def vml_Color37(self):
        return self.__vml_Color37

    @vml_Color37.setter
    def vml_Color37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Color__vml_Color37", None)
        self.__vml_Color37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_EdgeStyle36"):
                opp_val = getattr(old_value, "vml_EdgeStyle36", None)
                if opp_val == self:
                    setattr(old_value, "vml_EdgeStyle36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_EdgeStyle36"):
                opp_val = getattr(value, "vml_EdgeStyle36", None)
                setattr(value, "vml_EdgeStyle36", self)

class GraphStyle:

    pass
class vml_NodeStyle(GraphStyle):

    def __init__(self, borderWidth: int, padding: int, vml_NodeStyle26: "vml_Color" = None, vml_NodeStyle: "vml_Color" = None, vml_NodeStyle17: "vml_Color" = None, vml_NodeStyle20: "vml_Color" = None, vml_NodeStyle23: "vml_Color" = None):
        self.borderWidth = borderWidth
        self.padding = padding
        self.vml_NodeStyle26 = vml_NodeStyle26
        self.vml_NodeStyle = vml_NodeStyle
        self.vml_NodeStyle17 = vml_NodeStyle17
        self.vml_NodeStyle20 = vml_NodeStyle20
        self.vml_NodeStyle23 = vml_NodeStyle23
        
    @property
    def borderWidth(self) -> int:
        return self.__borderWidth

    @borderWidth.setter
    def borderWidth(self, borderWidth: int):
        self.__borderWidth = borderWidth

    @property
    def padding(self) -> int:
        return self.__padding

    @padding.setter
    def padding(self, padding: int):
        self.__padding = padding

    @property
    def vml_NodeStyle20(self):
        return self.__vml_NodeStyle20

    @vml_NodeStyle20.setter
    def vml_NodeStyle20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_NodeStyle__vml_NodeStyle20", None)
        self.__vml_NodeStyle20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Color21"):
                opp_val = getattr(old_value, "vml_Color21", None)
                if opp_val == self:
                    setattr(old_value, "vml_Color21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Color21"):
                opp_val = getattr(value, "vml_Color21", None)
                setattr(value, "vml_Color21", self)

    @property
    def vml_NodeStyle23(self):
        return self.__vml_NodeStyle23

    @vml_NodeStyle23.setter
    def vml_NodeStyle23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_NodeStyle__vml_NodeStyle23", None)
        self.__vml_NodeStyle23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Color24"):
                opp_val = getattr(old_value, "vml_Color24", None)
                if opp_val == self:
                    setattr(old_value, "vml_Color24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Color24"):
                opp_val = getattr(value, "vml_Color24", None)
                setattr(value, "vml_Color24", self)

    @property
    def vml_NodeStyle17(self):
        return self.__vml_NodeStyle17

    @vml_NodeStyle17.setter
    def vml_NodeStyle17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_NodeStyle__vml_NodeStyle17", None)
        self.__vml_NodeStyle17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Color18"):
                opp_val = getattr(old_value, "vml_Color18", None)
                if opp_val == self:
                    setattr(old_value, "vml_Color18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Color18"):
                opp_val = getattr(value, "vml_Color18", None)
                setattr(value, "vml_Color18", self)

    @property
    def vml_NodeStyle(self):
        return self.__vml_NodeStyle

    @vml_NodeStyle.setter
    def vml_NodeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_NodeStyle__vml_NodeStyle", None)
        self.__vml_NodeStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Color"):
                opp_val = getattr(old_value, "vml_Color", None)
                if opp_val == self:
                    setattr(old_value, "vml_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Color"):
                opp_val = getattr(value, "vml_Color", None)
                setattr(value, "vml_Color", self)

    @property
    def vml_NodeStyle26(self):
        return self.__vml_NodeStyle26

    @vml_NodeStyle26.setter
    def vml_NodeStyle26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_NodeStyle__vml_NodeStyle26", None)
        self.__vml_NodeStyle26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Color27"):
                opp_val = getattr(old_value, "vml_Color27", None)
                if opp_val == self:
                    setattr(old_value, "vml_Color27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Color27"):
                opp_val = getattr(value, "vml_Color27", None)
                setattr(value, "vml_Color27", self)

class Style:

    pass
class vml_ChartWithoutAxisStyle(Style):

    pass
class vml_ChartWithAxisStyle(Style):

    pass
class vml_GraphStyle(Style):

    pass
class vml_Style:

    pass
class vml_Cell:

    def __init__(self, textValue: str, vml_Cell: "vml_Row" = None, vml_Cell10: "vml_Column" = None):
        self.textValue = textValue
        self.vml_Cell = vml_Cell
        self.vml_Cell10 = vml_Cell10
        
    @property
    def textValue(self) -> str:
        return self.__textValue

    @textValue.setter
    def textValue(self, textValue: str):
        self.__textValue = textValue

    @property
    def vml_Cell(self):
        return self.__vml_Cell

    @vml_Cell.setter
    def vml_Cell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Cell__vml_Cell", None)
        self.__vml_Cell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Row8"):
                opp_val = getattr(old_value, "vml_Row8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Row8"):
                opp_val = getattr(value, "vml_Row8", None)
                if opp_val is None:
                    setattr(value, "vml_Row8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vml_Cell10(self):
        return self.__vml_Cell10

    @vml_Cell10.setter
    def vml_Cell10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Cell__vml_Cell10", None)
        self.__vml_Cell10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Column11"):
                opp_val = getattr(old_value, "vml_Column11", None)
                if opp_val == self:
                    setattr(old_value, "vml_Column11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Column11"):
                opp_val = getattr(value, "vml_Column11", None)
                setattr(value, "vml_Column11", self)

class vml_Row:

    pass
class vml_Node(DiagramElement):

    def __init__(self, title: str, icone: str, vml_Node: "vml_EdgeStyle" = None, vml_Node31: "vml_EdgeStyle" = None, vml_Node47: "vml_Graph" = None, source: set["vml_Edge"] = None, target: set["vml_Edge"] = None, Node: "vml_Edge" = None, Node57: "vml_Edge" = None):
        self.title = title
        self.icone = icone
        self.vml_Node = vml_Node
        self.vml_Node31 = vml_Node31
        self.vml_Node47 = vml_Node47
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.Node = Node
        self.Node57 = Node57
        
    @property
    def icone(self) -> str:
        return self.__icone

    @icone.setter
    def icone(self, icone: str):
        self.__icone = icone

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def vml_Node(self):
        return self.__vml_Node

    @vml_Node.setter
    def vml_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__vml_Node", None)
        self.__vml_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_EdgeStyle"):
                opp_val = getattr(old_value, "vml_EdgeStyle", None)
                if opp_val == self:
                    setattr(old_value, "vml_EdgeStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_EdgeStyle"):
                opp_val = getattr(value, "vml_EdgeStyle", None)
                setattr(value, "vml_EdgeStyle", self)

    @property
    def Node57(self):
        return self.__Node57

    @Node57.setter
    def Node57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__Node57", None)
        self.__Node57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incoming"):
                opp_val = getattr(old_value, "incoming", None)
                if opp_val == self:
                    setattr(old_value, "incoming", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incoming"):
                opp_val = getattr(value, "incoming", None)
                setattr(value, "incoming", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge54"):
                    opp_val = getattr(item, "Edge54", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge54"):
                    opp_val = getattr(item, "Edge54", None)
                    
                    setattr(item, "Edge54", self)
                    

    @property
    def vml_Node31(self):
        return self.__vml_Node31

    @vml_Node31.setter
    def vml_Node31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__vml_Node31", None)
        self.__vml_Node31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_EdgeStyle30"):
                opp_val = getattr(old_value, "vml_EdgeStyle30", None)
                if opp_val == self:
                    setattr(old_value, "vml_EdgeStyle30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_EdgeStyle30"):
                opp_val = getattr(value, "vml_EdgeStyle30", None)
                setattr(value, "vml_EdgeStyle30", self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoing"):
                opp_val = getattr(old_value, "outgoing", None)
                if opp_val == self:
                    setattr(old_value, "outgoing", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoing"):
                opp_val = getattr(value, "outgoing", None)
                setattr(value, "outgoing", self)

    @property
    def vml_Node47(self):
        return self.__vml_Node47

    @vml_Node47.setter
    def vml_Node47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__vml_Node47", None)
        self.__vml_Node47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Graph"):
                opp_val = getattr(old_value, "vml_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Graph"):
                opp_val = getattr(value, "vml_Graph", None)
                if opp_val is None:
                    setattr(value, "vml_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge"):
                    opp_val = getattr(item, "Edge", None)
                    
                    setattr(item, "Edge", self)
                    

class vml_EdgeStyle(GraphStyle):

    def __init__(self, lineWidth: int, weight: float, directed: bool, lineStyle: str, vml_EdgeStyle: "vml_Node" = None, vml_EdgeStyle30: "vml_Node" = None, vml_EdgeStyle33: "vml_Color" = None, vml_EdgeStyle36: "vml_Color" = None):
        self.lineWidth = lineWidth
        self.weight = weight
        self.directed = directed
        self.lineStyle = lineStyle
        self.vml_EdgeStyle = vml_EdgeStyle
        self.vml_EdgeStyle30 = vml_EdgeStyle30
        self.vml_EdgeStyle33 = vml_EdgeStyle33
        self.vml_EdgeStyle36 = vml_EdgeStyle36
        
    @property
    def lineStyle(self) -> str:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle

    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def directed(self) -> bool:
        return self.__directed

    @directed.setter
    def directed(self, directed: bool):
        self.__directed = directed

    @property
    def vml_EdgeStyle33(self):
        return self.__vml_EdgeStyle33

    @vml_EdgeStyle33.setter
    def vml_EdgeStyle33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_EdgeStyle__vml_EdgeStyle33", None)
        self.__vml_EdgeStyle33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Color34"):
                opp_val = getattr(old_value, "vml_Color34", None)
                if opp_val == self:
                    setattr(old_value, "vml_Color34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Color34"):
                opp_val = getattr(value, "vml_Color34", None)
                setattr(value, "vml_Color34", self)

    @property
    def vml_EdgeStyle30(self):
        return self.__vml_EdgeStyle30

    @vml_EdgeStyle30.setter
    def vml_EdgeStyle30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_EdgeStyle__vml_EdgeStyle30", None)
        self.__vml_EdgeStyle30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Node31"):
                opp_val = getattr(old_value, "vml_Node31", None)
                if opp_val == self:
                    setattr(old_value, "vml_Node31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Node31"):
                opp_val = getattr(value, "vml_Node31", None)
                setattr(value, "vml_Node31", self)

    @property
    def vml_EdgeStyle36(self):
        return self.__vml_EdgeStyle36

    @vml_EdgeStyle36.setter
    def vml_EdgeStyle36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_EdgeStyle__vml_EdgeStyle36", None)
        self.__vml_EdgeStyle36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Color37"):
                opp_val = getattr(old_value, "vml_Color37", None)
                if opp_val == self:
                    setattr(old_value, "vml_Color37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Color37"):
                opp_val = getattr(value, "vml_Color37", None)
                setattr(value, "vml_Color37", self)

    @property
    def vml_EdgeStyle(self):
        return self.__vml_EdgeStyle

    @vml_EdgeStyle.setter
    def vml_EdgeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_EdgeStyle__vml_EdgeStyle", None)
        self.__vml_EdgeStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Node"):
                opp_val = getattr(old_value, "vml_Node", None)
                if opp_val == self:
                    setattr(old_value, "vml_Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Node"):
                opp_val = getattr(value, "vml_Node", None)
                setattr(value, "vml_Node", self)

class vml_Column:

    def __init__(self, columnTitle: str, vml_Column: "vml_Table" = None, vml_Column11: "vml_Cell" = None):
        self.columnTitle = columnTitle
        self.vml_Column = vml_Column
        self.vml_Column11 = vml_Column11
        
    @property
    def columnTitle(self) -> str:
        return self.__columnTitle

    @columnTitle.setter
    def columnTitle(self, columnTitle: str):
        self.__columnTitle = columnTitle

    @property
    def vml_Column(self):
        return self.__vml_Column

    @vml_Column.setter
    def vml_Column(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Column__vml_Column", None)
        self.__vml_Column = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Table4"):
                opp_val = getattr(old_value, "vml_Table4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Table4"):
                opp_val = getattr(value, "vml_Table4", None)
                if opp_val is None:
                    setattr(value, "vml_Table4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vml_Column11(self):
        return self.__vml_Column11

    @vml_Column11.setter
    def vml_Column11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Column__vml_Column11", None)
        self.__vml_Column11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Cell10"):
                opp_val = getattr(old_value, "vml_Cell10", None)
                if opp_val == self:
                    setattr(old_value, "vml_Cell10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Cell10"):
                opp_val = getattr(value, "vml_Cell10", None)
                setattr(value, "vml_Cell10", self)

class vml_Table:

    def __init__(self, tableTitle: str, vml_Table: "vml_Model" = None, vml_Table4: set["vml_Column"] = None, vml_Table6: set["vml_Row"] = None, vml_Table42: "vml_DiagramElement" = None):
        self.tableTitle = tableTitle
        self.vml_Table = vml_Table
        self.vml_Table4 = vml_Table4 if vml_Table4 is not None else set()
        self.vml_Table6 = vml_Table6 if vml_Table6 is not None else set()
        self.vml_Table42 = vml_Table42
        
    @property
    def tableTitle(self) -> str:
        return self.__tableTitle

    @tableTitle.setter
    def tableTitle(self, tableTitle: str):
        self.__tableTitle = tableTitle

    @property
    def vml_Table42(self):
        return self.__vml_Table42

    @vml_Table42.setter
    def vml_Table42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Table__vml_Table42", None)
        self.__vml_Table42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_DiagramElement41"):
                opp_val = getattr(old_value, "vml_DiagramElement41", None)
                if opp_val == self:
                    setattr(old_value, "vml_DiagramElement41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_DiagramElement41"):
                opp_val = getattr(value, "vml_DiagramElement41", None)
                setattr(value, "vml_DiagramElement41", self)

    @property
    def vml_Table(self):
        return self.__vml_Table

    @vml_Table.setter
    def vml_Table(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Table__vml_Table", None)
        self.__vml_Table = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vml_Model2"):
                opp_val = getattr(old_value, "vml_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vml_Model2"):
                opp_val = getattr(value, "vml_Model2", None)
                if opp_val is None:
                    setattr(value, "vml_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vml_Table6(self):
        return self.__vml_Table6

    @vml_Table6.setter
    def vml_Table6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Table__vml_Table6", None)
        self.__vml_Table6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vml_Row"):
                    opp_val = getattr(item, "vml_Row", None)
                    
                    if opp_val == self:
                        setattr(item, "vml_Row", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vml_Row"):
                    opp_val = getattr(item, "vml_Row", None)
                    
                    setattr(item, "vml_Row", self)
                    

    @property
    def vml_Table4(self):
        return self.__vml_Table4

    @vml_Table4.setter
    def vml_Table4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vml_Table__vml_Table4", None)
        self.__vml_Table4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vml_Column"):
                    opp_val = getattr(item, "vml_Column", None)
                    
                    if opp_val == self:
                        setattr(item, "vml_Column", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vml_Column"):
                    opp_val = getattr(item, "vml_Column", None)
                    
                    setattr(item, "vml_Column", self)
                    

class vml_Diagram(ABC):

    pass
class vml_Model:

    pass