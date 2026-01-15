from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ArrangeConstraint(Enum):
    KEEP_LOCATION = "KEEP_LOCATION"
    KEEP_SIZE = "KEEP_SIZE"
    KEEP_RATIO = "KEEP_RATIO"
class BundledImageShape(Enum):
    square = "square"
    stroke = "stroke"
    triangle = "triangle"
    dot = "dot"
    ring = "ring"
    providedShape = "providedShape"
class LabelPosition(Enum):
    border = "border"
    node = "node"
class ResizeKind(Enum):
    NONE = "NONE"
    NSEW = "NSEW"
    NORTH_SOUTH = "NORTH_SOUTH"
    EAST_WEST = "EAST_WEST"
class ContainerLayout(Enum):
    FreeForm = "FreeForm"
    List = "List"
    HorizontalStack = "HorizontalStack"
    VerticalStack = "VerticalStack"
class EdgeArrows(Enum):
    NoDecoration = "NoDecoration"
    OutputClosedArrow = "OutputClosedArrow"
    InputClosedArrow = "InputClosedArrow"
    OutputFillClosedArrow = "OutputFillClosedArrow"
    InputFillClosedArrow = "InputFillClosedArrow"
    Diamond = "Diamond"
    OutputArrow = "OutputArrow"
    FillDiamond = "FillDiamond"
    InputArrow = "InputArrow"
    InputArrowWithDiamond = "InputArrowWithDiamond"
    InputArrowWithFillDiamond = "InputArrowWithFillDiamond"
class FilterKind(Enum):
    HIDE = "HIDE"
    COLLAPSE = "COLLAPSE"
class ReconnectionKind(Enum):
    RECONNECT_TARGET = "RECONNECT_TARGET"
    RECONNECT_SOURCE = "RECONNECT_SOURCE"
    RECONNECT_BOTH = "RECONNECT_BOTH"
class Side(Enum):
    WEST = "WEST"
    SOUTH = "SOUTH"
    EAST = "EAST"
    NORTH = "NORTH"
class LayoutDirection(Enum):
    LeftToRight = "LeftToRight"
    BottomToTop = "BottomToTop"
    TopToBottom = "TopToBottom"
class CenteringStyle(Enum):
    None = "None"
    Both = "Both"
    Source = "Source"
    Target = "Target"
class FoldingStyle(Enum):
    NONE = "NONE"
    SOURCE = "SOURCE"
    TARGET = "TARGET"
class EdgeRouting(Enum):
    straight = "straight"
    manhattan = "manhattan"
    tree = "tree"
class AlignmentKind(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
    SQUARE = "SQUARE"
class ContainerShape(Enum):
    parallelogram = "parallelogram"
class BackgroundStyle(Enum):
    Liquid = "Liquid"
    GradientTopToBottom = "GradientTopToBottom"
    GradientLeftToRight = "GradientLeftToRight"
class LineStyle(Enum):
    solid = "solid"
    dash = "dash"
    dot = "dot"
    dash_dot = "dash_dot"


############################################
# Definition of Classes
############################################

class InteractiveVariableDescription:

    pass
class filter_Filter:

    pass
class FilterDescription:

    pass
class diagram_filter_CompositeFilterDescription(FilterDescription):

    pass
class diagram_filter_Filter(ABC):

    def __init__(self, filterKind: str):
        self.filterKind = filterKind
        
    @property
    def filterKind(self) -> str:
        return self.__filterKind

    @filterKind.setter
    def filterKind(self, filterKind: str):
        self.__filterKind = filterKind

    def isVisible(self, element: DDiagramElement) -> bool:
        # TODO: Implement isVisible method
        pass

class Filter:

    pass
class diagram_filter_VariableFilter(Filter):

    def __init__(self, semanticConditionExpression: str, diagram_filter_VariableFilter: set["InteractiveVariableDescription"] = None):
        self.semanticConditionExpression = semanticConditionExpression
        self.diagram_filter_VariableFilter = diagram_filter_VariableFilter if diagram_filter_VariableFilter is not None else set()
        
    @property
    def semanticConditionExpression(self) -> str:
        return self.__semanticConditionExpression

    @semanticConditionExpression.setter
    def semanticConditionExpression(self, semanticConditionExpression: str):
        self.__semanticConditionExpression = semanticConditionExpression

    @property
    def diagram_filter_VariableFilter(self):
        return self.__diagram_filter_VariableFilter

    @diagram_filter_VariableFilter.setter
    def diagram_filter_VariableFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_filter_VariableFilter__diagram_filter_VariableFilter", None)
        self.__diagram_filter_VariableFilter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InteractiveVariableDescription"):
                    opp_val = getattr(item, "InteractiveVariableDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "InteractiveVariableDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InteractiveVariableDescription"):
                    opp_val = getattr(item, "InteractiveVariableDescription", None)
                    
                    setattr(item, "InteractiveVariableDescription", self)
                    

    def resetVariables(self):
        # TODO: Implement resetVariables method
        pass

class diagram_filter_MappingFilter(Filter):

    def __init__(self, semanticConditionExpression: str, viewConditionExpression: str, diagram_filter_MappingFilter: set["DiagramElementMapping"] = None):
        self.semanticConditionExpression = semanticConditionExpression
        self.viewConditionExpression = viewConditionExpression
        self.diagram_filter_MappingFilter = diagram_filter_MappingFilter if diagram_filter_MappingFilter is not None else set()
        
    @property
    def viewConditionExpression(self) -> str:
        return self.__viewConditionExpression

    @viewConditionExpression.setter
    def viewConditionExpression(self, viewConditionExpression: str):
        self.__viewConditionExpression = viewConditionExpression

    @property
    def semanticConditionExpression(self) -> str:
        return self.__semanticConditionExpression

    @semanticConditionExpression.setter
    def semanticConditionExpression(self, semanticConditionExpression: str):
        self.__semanticConditionExpression = semanticConditionExpression

    @property
    def diagram_filter_MappingFilter(self):
        return self.__diagram_filter_MappingFilter

    @diagram_filter_MappingFilter.setter
    def diagram_filter_MappingFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_filter_MappingFilter__diagram_filter_MappingFilter", None)
        self.__diagram_filter_MappingFilter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping457"):
                    opp_val = getattr(item, "DiagramElementMapping457", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping457", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping457"):
                    opp_val = getattr(item, "DiagramElementMapping457", None)
                    
                    setattr(item, "DiagramElementMapping457", self)
                    

class tool_InitialContainerDropOperation:

    pass
class tool_ElementDropVariable:

    pass
class tool_DropContainerVariable:

    pass
class RepresentationNavigationDescription:

    pass
class diagram_tool_DiagramNavigationDescription(RepresentationNavigationDescription):

    pass
class RepresentationCreationDescription:

    pass
class diagram_tool_DiagramCreationDescription(RepresentationCreationDescription):

    pass
class CreateView:

    pass
class diagram_tool_CreateEdgeView(CreateView):

    def __init__(self, sourceExpression: str, targetExpression: str):
        self.sourceExpression = sourceExpression
        self.targetExpression = targetExpression
        
    @property
    def targetExpression(self) -> str:
        return self.__targetExpression

    @targetExpression.setter
    def targetExpression(self, targetExpression: str):
        self.__targetExpression = targetExpression

    @property
    def sourceExpression(self) -> str:
        return self.__sourceExpression

    @sourceExpression.setter
    def sourceExpression(self, sourceExpression: str):
        self.__sourceExpression = sourceExpression

class ContainerModelOperation:

    pass
class diagram_tool_Navigation(ContainerModelOperation):

    def __init__(self, createIfNotExistent: bool, diagram_tool_Navigation: "DiagramDescription" = None):
        self.createIfNotExistent = createIfNotExistent
        self.diagram_tool_Navigation = diagram_tool_Navigation
        
    @property
    def createIfNotExistent(self) -> bool:
        return self.__createIfNotExistent

    @createIfNotExistent.setter
    def createIfNotExistent(self, createIfNotExistent: bool):
        self.__createIfNotExistent = createIfNotExistent

    @property
    def diagram_tool_Navigation(self):
        return self.__diagram_tool_Navigation

    @diagram_tool_Navigation.setter
    def diagram_tool_Navigation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_Navigation__diagram_tool_Navigation", None)
        self.__diagram_tool_Navigation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramDescription437"):
                opp_val = getattr(old_value, "DiagramDescription437", None)
                if opp_val == self:
                    setattr(old_value, "DiagramDescription437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramDescription437"):
                opp_val = getattr(value, "DiagramDescription437", None)
                setattr(value, "DiagramDescription437", self)

class diagram_tool_CreateView(ContainerModelOperation):

    def __init__(self, containerViewExpression: str, variableName: str, diagram_tool_CreateView: "DiagramElementMapping" = None):
        self.containerViewExpression = containerViewExpression
        self.variableName = variableName
        self.diagram_tool_CreateView = diagram_tool_CreateView
        
    @property
    def containerViewExpression(self) -> str:
        return self.__containerViewExpression

    @containerViewExpression.setter
    def containerViewExpression(self, containerViewExpression: str):
        self.__containerViewExpression = containerViewExpression

    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def diagram_tool_CreateView(self):
        return self.__diagram_tool_CreateView

    @diagram_tool_CreateView.setter
    def diagram_tool_CreateView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_CreateView__diagram_tool_CreateView", None)
        self.__diagram_tool_CreateView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramElementMapping435"):
                opp_val = getattr(old_value, "DiagramElementMapping435", None)
                if opp_val == self:
                    setattr(old_value, "DiagramElementMapping435", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramElementMapping435"):
                opp_val = getattr(value, "DiagramElementMapping435", None)
                setattr(value, "DiagramElementMapping435", self)

class tool_VariableContainer:

    pass
class description_AbstractVariable:

    pass
class diagram_tool_TargetEdgeCreationVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class diagram_tool_SourceEdgeViewCreationVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class diagram_tool_ElementDoubleClickVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class diagram_tool_NodeCreationVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class diagram_tool_TargetEdgeViewCreationVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class diagram_tool_SourceEdgeCreationVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class tool_ElementSelectVariable:

    pass
class tool_EditMaskVariables:

    pass
class AbstractToolDescription:

    pass
class diagram_tool_BehaviorTool(AbstractToolDescription):

    def __init__(self, domainClass: str, diagram_tool_BehaviorTool: "tool_InitialOperation" = None):
        self.domainClass = domainClass
        self.diagram_tool_BehaviorTool = diagram_tool_BehaviorTool
        
    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def diagram_tool_BehaviorTool(self):
        return self.__diagram_tool_BehaviorTool

    @diagram_tool_BehaviorTool.setter
    def diagram_tool_BehaviorTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_BehaviorTool__diagram_tool_BehaviorTool", None)
        self.__diagram_tool_BehaviorTool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation433"):
                opp_val = getattr(old_value, "tool_InitialOperation433", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation433", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation433"):
                opp_val = getattr(value, "tool_InitialOperation433", None)
                setattr(value, "tool_InitialOperation433", self)

class diagram_tool_RequestDescription(AbstractToolDescription):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class tool_ElementDeleteVariable:

    pass
class diagram_tool_DeleteHookParameter:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class tool_DeleteHookParameter:

    pass
class diagram_tool_DeleteHook:

    def __init__(self, id: str, diagram_tool_DeleteHook: set["tool_DeleteHookParameter"] = None):
        self.id = id
        self.diagram_tool_DeleteHook = diagram_tool_DeleteHook if diagram_tool_DeleteHook is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def diagram_tool_DeleteHook(self):
        return self.__diagram_tool_DeleteHook

    @diagram_tool_DeleteHook.setter
    def diagram_tool_DeleteHook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteHook__diagram_tool_DeleteHook", None)
        self.__diagram_tool_DeleteHook = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_DeleteHookParameter"):
                    opp_val = getattr(item, "tool_DeleteHookParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_DeleteHookParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_DeleteHookParameter"):
                    opp_val = getattr(item, "tool_DeleteHookParameter", None)
                    
                    setattr(item, "tool_DeleteHookParameter", self)
                    

class tool_ElementDoubleClickVariable:

    pass
class tool_DeleteHook:

    pass
class tool_SourceEdgeViewCreationVariable:

    pass
class tool_TargetEdgeCreationVariable:

    pass
class tool_SourceEdgeCreationVariable:

    pass
class tool_InitEdgeCreationOperation:

    pass
class tool_TargetEdgeViewCreationVariable:

    pass
class tool_InitialNodeCreationOperation:

    pass
class MappingBasedToolDescription:

    pass
class diagram_tool_EdgeCreationDescription(MappingBasedToolDescription):

    def __init__(self, connectionStartPrecondition: str, iconPath: str, diagram_tool_EdgeCreationDescription361: "tool_SourceEdgeViewCreationVariable" = None, diagram_tool_EdgeCreationDescription363: "tool_TargetEdgeViewCreationVariable" = None, diagram_tool_EdgeCreationDescription: set["EdgeMapping"] = None, diagram_tool_EdgeCreationDescription357: "tool_SourceEdgeCreationVariable" = None, diagram_tool_EdgeCreationDescription359: "tool_TargetEdgeCreationVariable" = None, diagram_tool_EdgeCreationDescription365: "tool_InitEdgeCreationOperation" = None, diagram_tool_EdgeCreationDescription367: set["DiagramElementMapping"] = None, diagram_tool_EdgeCreationDescription370: set["DiagramElementMapping"] = None):
        self.connectionStartPrecondition = connectionStartPrecondition
        self.iconPath = iconPath
        self.diagram_tool_EdgeCreationDescription361 = diagram_tool_EdgeCreationDescription361
        self.diagram_tool_EdgeCreationDescription363 = diagram_tool_EdgeCreationDescription363
        self.diagram_tool_EdgeCreationDescription = diagram_tool_EdgeCreationDescription if diagram_tool_EdgeCreationDescription is not None else set()
        self.diagram_tool_EdgeCreationDescription357 = diagram_tool_EdgeCreationDescription357
        self.diagram_tool_EdgeCreationDescription359 = diagram_tool_EdgeCreationDescription359
        self.diagram_tool_EdgeCreationDescription365 = diagram_tool_EdgeCreationDescription365
        self.diagram_tool_EdgeCreationDescription367 = diagram_tool_EdgeCreationDescription367 if diagram_tool_EdgeCreationDescription367 is not None else set()
        self.diagram_tool_EdgeCreationDescription370 = diagram_tool_EdgeCreationDescription370 if diagram_tool_EdgeCreationDescription370 is not None else set()
        
    @property
    def connectionStartPrecondition(self) -> str:
        return self.__connectionStartPrecondition

    @connectionStartPrecondition.setter
    def connectionStartPrecondition(self, connectionStartPrecondition: str):
        self.__connectionStartPrecondition = connectionStartPrecondition

    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def diagram_tool_EdgeCreationDescription359(self):
        return self.__diagram_tool_EdgeCreationDescription359

    @diagram_tool_EdgeCreationDescription359.setter
    def diagram_tool_EdgeCreationDescription359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription359", None)
        self.__diagram_tool_EdgeCreationDescription359 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_TargetEdgeCreationVariable"):
                opp_val = getattr(old_value, "tool_TargetEdgeCreationVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_TargetEdgeCreationVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_TargetEdgeCreationVariable"):
                opp_val = getattr(value, "tool_TargetEdgeCreationVariable", None)
                setattr(value, "tool_TargetEdgeCreationVariable", self)

    @property
    def diagram_tool_EdgeCreationDescription370(self):
        return self.__diagram_tool_EdgeCreationDescription370

    @diagram_tool_EdgeCreationDescription370.setter
    def diagram_tool_EdgeCreationDescription370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription370", None)
        self.__diagram_tool_EdgeCreationDescription370 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping371"):
                    opp_val = getattr(item, "DiagramElementMapping371", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping371", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping371"):
                    opp_val = getattr(item, "DiagramElementMapping371", None)
                    
                    setattr(item, "DiagramElementMapping371", self)
                    

    @property
    def diagram_tool_EdgeCreationDescription361(self):
        return self.__diagram_tool_EdgeCreationDescription361

    @diagram_tool_EdgeCreationDescription361.setter
    def diagram_tool_EdgeCreationDescription361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription361", None)
        self.__diagram_tool_EdgeCreationDescription361 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SourceEdgeViewCreationVariable"):
                opp_val = getattr(old_value, "tool_SourceEdgeViewCreationVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_SourceEdgeViewCreationVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SourceEdgeViewCreationVariable"):
                opp_val = getattr(value, "tool_SourceEdgeViewCreationVariable", None)
                setattr(value, "tool_SourceEdgeViewCreationVariable", self)

    @property
    def diagram_tool_EdgeCreationDescription357(self):
        return self.__diagram_tool_EdgeCreationDescription357

    @diagram_tool_EdgeCreationDescription357.setter
    def diagram_tool_EdgeCreationDescription357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription357", None)
        self.__diagram_tool_EdgeCreationDescription357 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SourceEdgeCreationVariable"):
                opp_val = getattr(old_value, "tool_SourceEdgeCreationVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_SourceEdgeCreationVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SourceEdgeCreationVariable"):
                opp_val = getattr(value, "tool_SourceEdgeCreationVariable", None)
                setattr(value, "tool_SourceEdgeCreationVariable", self)

    @property
    def diagram_tool_EdgeCreationDescription(self):
        return self.__diagram_tool_EdgeCreationDescription

    @diagram_tool_EdgeCreationDescription.setter
    def diagram_tool_EdgeCreationDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription", None)
        self.__diagram_tool_EdgeCreationDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMapping355"):
                    opp_val = getattr(item, "EdgeMapping355", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping355", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping355"):
                    opp_val = getattr(item, "EdgeMapping355", None)
                    
                    setattr(item, "EdgeMapping355", self)
                    

    @property
    def diagram_tool_EdgeCreationDescription363(self):
        return self.__diagram_tool_EdgeCreationDescription363

    @diagram_tool_EdgeCreationDescription363.setter
    def diagram_tool_EdgeCreationDescription363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription363", None)
        self.__diagram_tool_EdgeCreationDescription363 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_TargetEdgeViewCreationVariable"):
                opp_val = getattr(old_value, "tool_TargetEdgeViewCreationVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_TargetEdgeViewCreationVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_TargetEdgeViewCreationVariable"):
                opp_val = getattr(value, "tool_TargetEdgeViewCreationVariable", None)
                setattr(value, "tool_TargetEdgeViewCreationVariable", self)

    @property
    def diagram_tool_EdgeCreationDescription365(self):
        return self.__diagram_tool_EdgeCreationDescription365

    @diagram_tool_EdgeCreationDescription365.setter
    def diagram_tool_EdgeCreationDescription365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription365", None)
        self.__diagram_tool_EdgeCreationDescription365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitEdgeCreationOperation"):
                opp_val = getattr(old_value, "tool_InitEdgeCreationOperation", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitEdgeCreationOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitEdgeCreationOperation"):
                opp_val = getattr(value, "tool_InitEdgeCreationOperation", None)
                setattr(value, "tool_InitEdgeCreationOperation", self)

    @property
    def diagram_tool_EdgeCreationDescription367(self):
        return self.__diagram_tool_EdgeCreationDescription367

    @diagram_tool_EdgeCreationDescription367.setter
    def diagram_tool_EdgeCreationDescription367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription367", None)
        self.__diagram_tool_EdgeCreationDescription367 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping368"):
                    opp_val = getattr(item, "DiagramElementMapping368", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping368", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping368"):
                    opp_val = getattr(item, "DiagramElementMapping368", None)
                    
                    setattr(item, "DiagramElementMapping368", self)
                    

    def getBestMapping(self, createdElements: str, source: EdgeTarget, target: EdgeTarget) -> str:
        # TODO: Implement getBestMapping method
        pass

class diagram_tool_ContainerDropDescription(MappingBasedToolDescription):

    def __init__(self, dragSource: str, moveEdges: bool, diagram_tool_ContainerDropDescription: set["DiagramElementMapping"] = None, diagram_tool_ContainerDropDescription445: "tool_DropContainerVariable" = None, diagram_tool_ContainerDropDescription447: "tool_DropContainerVariable" = None, diagram_tool_ContainerDropDescription450: "tool_ElementDropVariable" = None, diagram_tool_ContainerDropDescription452: "tool_ContainerViewVariable" = None, diagram_tool_ContainerDropDescription455: "tool_InitialContainerDropOperation" = None):
        self.dragSource = dragSource
        self.moveEdges = moveEdges
        self.diagram_tool_ContainerDropDescription = diagram_tool_ContainerDropDescription if diagram_tool_ContainerDropDescription is not None else set()
        self.diagram_tool_ContainerDropDescription445 = diagram_tool_ContainerDropDescription445
        self.diagram_tool_ContainerDropDescription447 = diagram_tool_ContainerDropDescription447
        self.diagram_tool_ContainerDropDescription450 = diagram_tool_ContainerDropDescription450
        self.diagram_tool_ContainerDropDescription452 = diagram_tool_ContainerDropDescription452
        self.diagram_tool_ContainerDropDescription455 = diagram_tool_ContainerDropDescription455
        
    @property
    def moveEdges(self) -> bool:
        return self.__moveEdges

    @moveEdges.setter
    def moveEdges(self, moveEdges: bool):
        self.__moveEdges = moveEdges

    @property
    def dragSource(self) -> str:
        return self.__dragSource

    @dragSource.setter
    def dragSource(self, dragSource: str):
        self.__dragSource = dragSource

    @property
    def diagram_tool_ContainerDropDescription450(self):
        return self.__diagram_tool_ContainerDropDescription450

    @diagram_tool_ContainerDropDescription450.setter
    def diagram_tool_ContainerDropDescription450(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription450", None)
        self.__diagram_tool_ContainerDropDescription450 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementDropVariable"):
                opp_val = getattr(old_value, "tool_ElementDropVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementDropVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementDropVariable"):
                opp_val = getattr(value, "tool_ElementDropVariable", None)
                setattr(value, "tool_ElementDropVariable", self)

    @property
    def diagram_tool_ContainerDropDescription(self):
        return self.__diagram_tool_ContainerDropDescription

    @diagram_tool_ContainerDropDescription.setter
    def diagram_tool_ContainerDropDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription", None)
        self.__diagram_tool_ContainerDropDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping443"):
                    opp_val = getattr(item, "DiagramElementMapping443", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping443", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping443"):
                    opp_val = getattr(item, "DiagramElementMapping443", None)
                    
                    setattr(item, "DiagramElementMapping443", self)
                    

    @property
    def diagram_tool_ContainerDropDescription447(self):
        return self.__diagram_tool_ContainerDropDescription447

    @diagram_tool_ContainerDropDescription447.setter
    def diagram_tool_ContainerDropDescription447(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription447", None)
        self.__diagram_tool_ContainerDropDescription447 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DropContainerVariable448"):
                opp_val = getattr(old_value, "tool_DropContainerVariable448", None)
                if opp_val == self:
                    setattr(old_value, "tool_DropContainerVariable448", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DropContainerVariable448"):
                opp_val = getattr(value, "tool_DropContainerVariable448", None)
                setattr(value, "tool_DropContainerVariable448", self)

    @property
    def diagram_tool_ContainerDropDescription452(self):
        return self.__diagram_tool_ContainerDropDescription452

    @diagram_tool_ContainerDropDescription452.setter
    def diagram_tool_ContainerDropDescription452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription452", None)
        self.__diagram_tool_ContainerDropDescription452 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable453"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable453", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable453"):
                opp_val = getattr(value, "tool_ContainerViewVariable453", None)
                setattr(value, "tool_ContainerViewVariable453", self)

    @property
    def diagram_tool_ContainerDropDescription445(self):
        return self.__diagram_tool_ContainerDropDescription445

    @diagram_tool_ContainerDropDescription445.setter
    def diagram_tool_ContainerDropDescription445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription445", None)
        self.__diagram_tool_ContainerDropDescription445 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DropContainerVariable"):
                opp_val = getattr(old_value, "tool_DropContainerVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_DropContainerVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DropContainerVariable"):
                opp_val = getattr(value, "tool_DropContainerVariable", None)
                setattr(value, "tool_DropContainerVariable", self)

    @property
    def diagram_tool_ContainerDropDescription455(self):
        return self.__diagram_tool_ContainerDropDescription455

    @diagram_tool_ContainerDropDescription455.setter
    def diagram_tool_ContainerDropDescription455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription455", None)
        self.__diagram_tool_ContainerDropDescription455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialContainerDropOperation"):
                opp_val = getattr(old_value, "tool_InitialContainerDropOperation", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialContainerDropOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialContainerDropOperation"):
                opp_val = getattr(value, "tool_InitialContainerDropOperation", None)
                setattr(value, "tool_InitialContainerDropOperation", self)

    def getContainers(self) -> str:
        # TODO: Implement getContainers method
        pass

    def getBestMapping(self, targetContainer: DragAndDropTarget, droppedElement: str) -> str:
        # TODO: Implement getBestMapping method
        pass

class diagram_tool_DirectEditLabel(MappingBasedToolDescription):

    def __init__(self, inputLabelExpression: str, diagram_tool_DirectEditLabel: "tool_EditMaskVariables" = None, diagram_tool_DirectEditLabel430: "tool_InitialOperation" = None):
        self.inputLabelExpression = inputLabelExpression
        self.diagram_tool_DirectEditLabel = diagram_tool_DirectEditLabel
        self.diagram_tool_DirectEditLabel430 = diagram_tool_DirectEditLabel430
        
    @property
    def inputLabelExpression(self) -> str:
        return self.__inputLabelExpression

    @inputLabelExpression.setter
    def inputLabelExpression(self, inputLabelExpression: str):
        self.__inputLabelExpression = inputLabelExpression

    @property
    def diagram_tool_DirectEditLabel430(self):
        return self.__diagram_tool_DirectEditLabel430

    @diagram_tool_DirectEditLabel430.setter
    def diagram_tool_DirectEditLabel430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DirectEditLabel__diagram_tool_DirectEditLabel430", None)
        self.__diagram_tool_DirectEditLabel430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation431"):
                opp_val = getattr(old_value, "tool_InitialOperation431", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation431"):
                opp_val = getattr(value, "tool_InitialOperation431", None)
                setattr(value, "tool_InitialOperation431", self)

    @property
    def diagram_tool_DirectEditLabel(self):
        return self.__diagram_tool_DirectEditLabel

    @diagram_tool_DirectEditLabel.setter
    def diagram_tool_DirectEditLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DirectEditLabel__diagram_tool_DirectEditLabel", None)
        self.__diagram_tool_DirectEditLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_EditMaskVariables"):
                opp_val = getattr(old_value, "tool_EditMaskVariables", None)
                if opp_val == self:
                    setattr(old_value, "tool_EditMaskVariables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_EditMaskVariables"):
                opp_val = getattr(value, "tool_EditMaskVariables", None)
                setattr(value, "tool_EditMaskVariables", self)

    def getMapping(self) -> str:
        # TODO: Implement getMapping method
        pass

class diagram_tool_DoubleClickDescription(MappingBasedToolDescription):

    pass
class diagram_tool_ContainerCreationDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, diagram_tool_ContainerCreationDescription: set["ContainerMapping"] = None, diagram_tool_ContainerCreationDescription375: "tool_NodeCreationVariable" = None, diagram_tool_ContainerCreationDescription378: "tool_ContainerViewVariable" = None, diagram_tool_ContainerCreationDescription381: "tool_InitialNodeCreationOperation" = None, diagram_tool_ContainerCreationDescription384: set["AbstractNodeMapping"] = None):
        self.iconPath = iconPath
        self.diagram_tool_ContainerCreationDescription = diagram_tool_ContainerCreationDescription if diagram_tool_ContainerCreationDescription is not None else set()
        self.diagram_tool_ContainerCreationDescription375 = diagram_tool_ContainerCreationDescription375
        self.diagram_tool_ContainerCreationDescription378 = diagram_tool_ContainerCreationDescription378
        self.diagram_tool_ContainerCreationDescription381 = diagram_tool_ContainerCreationDescription381
        self.diagram_tool_ContainerCreationDescription384 = diagram_tool_ContainerCreationDescription384 if diagram_tool_ContainerCreationDescription384 is not None else set()
        
    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def diagram_tool_ContainerCreationDescription378(self):
        return self.__diagram_tool_ContainerCreationDescription378

    @diagram_tool_ContainerCreationDescription378.setter
    def diagram_tool_ContainerCreationDescription378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription378", None)
        self.__diagram_tool_ContainerCreationDescription378 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable379"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable379", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable379", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable379"):
                opp_val = getattr(value, "tool_ContainerViewVariable379", None)
                setattr(value, "tool_ContainerViewVariable379", self)

    @property
    def diagram_tool_ContainerCreationDescription381(self):
        return self.__diagram_tool_ContainerCreationDescription381

    @diagram_tool_ContainerCreationDescription381.setter
    def diagram_tool_ContainerCreationDescription381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription381", None)
        self.__diagram_tool_ContainerCreationDescription381 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialNodeCreationOperation382"):
                opp_val = getattr(old_value, "tool_InitialNodeCreationOperation382", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialNodeCreationOperation382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialNodeCreationOperation382"):
                opp_val = getattr(value, "tool_InitialNodeCreationOperation382", None)
                setattr(value, "tool_InitialNodeCreationOperation382", self)

    @property
    def diagram_tool_ContainerCreationDescription(self):
        return self.__diagram_tool_ContainerCreationDescription

    @diagram_tool_ContainerCreationDescription.setter
    def diagram_tool_ContainerCreationDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription", None)
        self.__diagram_tool_ContainerCreationDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping373"):
                    opp_val = getattr(item, "ContainerMapping373", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping373", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping373"):
                    opp_val = getattr(item, "ContainerMapping373", None)
                    
                    setattr(item, "ContainerMapping373", self)
                    

    @property
    def diagram_tool_ContainerCreationDescription384(self):
        return self.__diagram_tool_ContainerCreationDescription384

    @diagram_tool_ContainerCreationDescription384.setter
    def diagram_tool_ContainerCreationDescription384(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription384", None)
        self.__diagram_tool_ContainerCreationDescription384 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractNodeMapping385"):
                    opp_val = getattr(item, "AbstractNodeMapping385", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractNodeMapping385", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractNodeMapping385"):
                    opp_val = getattr(item, "AbstractNodeMapping385", None)
                    
                    setattr(item, "AbstractNodeMapping385", self)
                    

    @property
    def diagram_tool_ContainerCreationDescription375(self):
        return self.__diagram_tool_ContainerCreationDescription375

    @diagram_tool_ContainerCreationDescription375.setter
    def diagram_tool_ContainerCreationDescription375(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription375", None)
        self.__diagram_tool_ContainerCreationDescription375 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_NodeCreationVariable376"):
                opp_val = getattr(old_value, "tool_NodeCreationVariable376", None)
                if opp_val == self:
                    setattr(old_value, "tool_NodeCreationVariable376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_NodeCreationVariable376"):
                opp_val = getattr(value, "tool_NodeCreationVariable376", None)
                setattr(value, "tool_NodeCreationVariable376", self)

class diagram_tool_ReconnectEdgeDescription(MappingBasedToolDescription):

    def __init__(self, reconnectionKind: str, diagram_tool_ReconnectEdgeDescription412: "tool_TargetEdgeCreationVariable" = None, diagram_tool_ReconnectEdgeDescription415: "tool_SourceEdgeViewCreationVariable" = None, diagram_tool_ReconnectEdgeDescription418: "tool_TargetEdgeViewCreationVariable" = None, diagram_tool_ReconnectEdgeDescription: "tool_SourceEdgeCreationVariable" = None, diagram_tool_ReconnectEdgeDescription421: "tool_ElementSelectVariable" = None, diagram_tool_ReconnectEdgeDescription423: "tool_InitialOperation" = None, diagram_tool_ReconnectEdgeDescription426: "tool_ElementSelectVariable" = None):
        self.reconnectionKind = reconnectionKind
        self.diagram_tool_ReconnectEdgeDescription412 = diagram_tool_ReconnectEdgeDescription412
        self.diagram_tool_ReconnectEdgeDescription415 = diagram_tool_ReconnectEdgeDescription415
        self.diagram_tool_ReconnectEdgeDescription418 = diagram_tool_ReconnectEdgeDescription418
        self.diagram_tool_ReconnectEdgeDescription = diagram_tool_ReconnectEdgeDescription
        self.diagram_tool_ReconnectEdgeDescription421 = diagram_tool_ReconnectEdgeDescription421
        self.diagram_tool_ReconnectEdgeDescription423 = diagram_tool_ReconnectEdgeDescription423
        self.diagram_tool_ReconnectEdgeDescription426 = diagram_tool_ReconnectEdgeDescription426
        
    @property
    def reconnectionKind(self) -> str:
        return self.__reconnectionKind

    @reconnectionKind.setter
    def reconnectionKind(self, reconnectionKind: str):
        self.__reconnectionKind = reconnectionKind

    @property
    def diagram_tool_ReconnectEdgeDescription421(self):
        return self.__diagram_tool_ReconnectEdgeDescription421

    @diagram_tool_ReconnectEdgeDescription421.setter
    def diagram_tool_ReconnectEdgeDescription421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription421", None)
        self.__diagram_tool_ReconnectEdgeDescription421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementSelectVariable"):
                opp_val = getattr(old_value, "tool_ElementSelectVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementSelectVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementSelectVariable"):
                opp_val = getattr(value, "tool_ElementSelectVariable", None)
                setattr(value, "tool_ElementSelectVariable", self)

    @property
    def diagram_tool_ReconnectEdgeDescription(self):
        return self.__diagram_tool_ReconnectEdgeDescription

    @diagram_tool_ReconnectEdgeDescription.setter
    def diagram_tool_ReconnectEdgeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription", None)
        self.__diagram_tool_ReconnectEdgeDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SourceEdgeCreationVariable410"):
                opp_val = getattr(old_value, "tool_SourceEdgeCreationVariable410", None)
                if opp_val == self:
                    setattr(old_value, "tool_SourceEdgeCreationVariable410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SourceEdgeCreationVariable410"):
                opp_val = getattr(value, "tool_SourceEdgeCreationVariable410", None)
                setattr(value, "tool_SourceEdgeCreationVariable410", self)

    @property
    def diagram_tool_ReconnectEdgeDescription412(self):
        return self.__diagram_tool_ReconnectEdgeDescription412

    @diagram_tool_ReconnectEdgeDescription412.setter
    def diagram_tool_ReconnectEdgeDescription412(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription412", None)
        self.__diagram_tool_ReconnectEdgeDescription412 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_TargetEdgeCreationVariable413"):
                opp_val = getattr(old_value, "tool_TargetEdgeCreationVariable413", None)
                if opp_val == self:
                    setattr(old_value, "tool_TargetEdgeCreationVariable413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_TargetEdgeCreationVariable413"):
                opp_val = getattr(value, "tool_TargetEdgeCreationVariable413", None)
                setattr(value, "tool_TargetEdgeCreationVariable413", self)

    @property
    def diagram_tool_ReconnectEdgeDescription426(self):
        return self.__diagram_tool_ReconnectEdgeDescription426

    @diagram_tool_ReconnectEdgeDescription426.setter
    def diagram_tool_ReconnectEdgeDescription426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription426", None)
        self.__diagram_tool_ReconnectEdgeDescription426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementSelectVariable427"):
                opp_val = getattr(old_value, "tool_ElementSelectVariable427", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementSelectVariable427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementSelectVariable427"):
                opp_val = getattr(value, "tool_ElementSelectVariable427", None)
                setattr(value, "tool_ElementSelectVariable427", self)

    @property
    def diagram_tool_ReconnectEdgeDescription415(self):
        return self.__diagram_tool_ReconnectEdgeDescription415

    @diagram_tool_ReconnectEdgeDescription415.setter
    def diagram_tool_ReconnectEdgeDescription415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription415", None)
        self.__diagram_tool_ReconnectEdgeDescription415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SourceEdgeViewCreationVariable416"):
                opp_val = getattr(old_value, "tool_SourceEdgeViewCreationVariable416", None)
                if opp_val == self:
                    setattr(old_value, "tool_SourceEdgeViewCreationVariable416", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SourceEdgeViewCreationVariable416"):
                opp_val = getattr(value, "tool_SourceEdgeViewCreationVariable416", None)
                setattr(value, "tool_SourceEdgeViewCreationVariable416", self)

    @property
    def diagram_tool_ReconnectEdgeDescription423(self):
        return self.__diagram_tool_ReconnectEdgeDescription423

    @diagram_tool_ReconnectEdgeDescription423.setter
    def diagram_tool_ReconnectEdgeDescription423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription423", None)
        self.__diagram_tool_ReconnectEdgeDescription423 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation424"):
                opp_val = getattr(old_value, "tool_InitialOperation424", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation424"):
                opp_val = getattr(value, "tool_InitialOperation424", None)
                setattr(value, "tool_InitialOperation424", self)

    @property
    def diagram_tool_ReconnectEdgeDescription418(self):
        return self.__diagram_tool_ReconnectEdgeDescription418

    @diagram_tool_ReconnectEdgeDescription418.setter
    def diagram_tool_ReconnectEdgeDescription418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription418", None)
        self.__diagram_tool_ReconnectEdgeDescription418 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_TargetEdgeViewCreationVariable419"):
                opp_val = getattr(old_value, "tool_TargetEdgeViewCreationVariable419", None)
                if opp_val == self:
                    setattr(old_value, "tool_TargetEdgeViewCreationVariable419", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_TargetEdgeViewCreationVariable419"):
                opp_val = getattr(value, "tool_TargetEdgeViewCreationVariable419", None)
                setattr(value, "tool_TargetEdgeViewCreationVariable419", self)

    def getMappings(self) -> str:
        # TODO: Implement getMappings method
        pass

class diagram_tool_DeleteElementDescription(MappingBasedToolDescription):

    def __init__(self, diagram_tool_DeleteElementDescription397: "tool_DeleteHook" = None, diagram_tool_DeleteElementDescription: "tool_ElementDeleteVariable" = None, diagram_tool_DeleteElementDescription388: "tool_ElementDeleteVariable" = None, diagram_tool_DeleteElementDescription391: "tool_ContainerViewVariable" = None, diagram_tool_DeleteElementDescription394: "tool_InitialOperation" = None):
        self.diagram_tool_DeleteElementDescription397 = diagram_tool_DeleteElementDescription397
        self.diagram_tool_DeleteElementDescription = diagram_tool_DeleteElementDescription
        self.diagram_tool_DeleteElementDescription388 = diagram_tool_DeleteElementDescription388
        self.diagram_tool_DeleteElementDescription391 = diagram_tool_DeleteElementDescription391
        self.diagram_tool_DeleteElementDescription394 = diagram_tool_DeleteElementDescription394
        
    @property
    def diagram_tool_DeleteElementDescription397(self):
        return self.__diagram_tool_DeleteElementDescription397

    @diagram_tool_DeleteElementDescription397.setter
    def diagram_tool_DeleteElementDescription397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription397", None)
        self.__diagram_tool_DeleteElementDescription397 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DeleteHook"):
                opp_val = getattr(old_value, "tool_DeleteHook", None)
                if opp_val == self:
                    setattr(old_value, "tool_DeleteHook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DeleteHook"):
                opp_val = getattr(value, "tool_DeleteHook", None)
                setattr(value, "tool_DeleteHook", self)

    @property
    def diagram_tool_DeleteElementDescription394(self):
        return self.__diagram_tool_DeleteElementDescription394

    @diagram_tool_DeleteElementDescription394.setter
    def diagram_tool_DeleteElementDescription394(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription394", None)
        self.__diagram_tool_DeleteElementDescription394 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation395"):
                opp_val = getattr(old_value, "tool_InitialOperation395", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation395", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation395"):
                opp_val = getattr(value, "tool_InitialOperation395", None)
                setattr(value, "tool_InitialOperation395", self)

    @property
    def diagram_tool_DeleteElementDescription388(self):
        return self.__diagram_tool_DeleteElementDescription388

    @diagram_tool_DeleteElementDescription388.setter
    def diagram_tool_DeleteElementDescription388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription388", None)
        self.__diagram_tool_DeleteElementDescription388 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementDeleteVariable389"):
                opp_val = getattr(old_value, "tool_ElementDeleteVariable389", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementDeleteVariable389", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementDeleteVariable389"):
                opp_val = getattr(value, "tool_ElementDeleteVariable389", None)
                setattr(value, "tool_ElementDeleteVariable389", self)

    @property
    def diagram_tool_DeleteElementDescription391(self):
        return self.__diagram_tool_DeleteElementDescription391

    @diagram_tool_DeleteElementDescription391.setter
    def diagram_tool_DeleteElementDescription391(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription391", None)
        self.__diagram_tool_DeleteElementDescription391 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable392"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable392", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable392", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable392"):
                opp_val = getattr(value, "tool_ContainerViewVariable392", None)
                setattr(value, "tool_ContainerViewVariable392", self)

    @property
    def diagram_tool_DeleteElementDescription(self):
        return self.__diagram_tool_DeleteElementDescription

    @diagram_tool_DeleteElementDescription.setter
    def diagram_tool_DeleteElementDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription", None)
        self.__diagram_tool_DeleteElementDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementDeleteVariable"):
                opp_val = getattr(old_value, "tool_ElementDeleteVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementDeleteVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementDeleteVariable"):
                opp_val = getattr(value, "tool_ElementDeleteVariable", None)
                setattr(value, "tool_ElementDeleteVariable", self)

    def getMappings(self) -> str:
        # TODO: Implement getMappings method
        pass

class diagram_tool_NodeCreationDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, diagram_tool_NodeCreationDescription346: "tool_NodeCreationVariable" = None, diagram_tool_NodeCreationDescription348: "tool_ContainerViewVariable" = None, diagram_tool_NodeCreationDescription: set["NodeMapping"] = None, diagram_tool_NodeCreationDescription350: "tool_InitialNodeCreationOperation" = None, diagram_tool_NodeCreationDescription352: set["AbstractNodeMapping"] = None):
        self.iconPath = iconPath
        self.diagram_tool_NodeCreationDescription346 = diagram_tool_NodeCreationDescription346
        self.diagram_tool_NodeCreationDescription348 = diagram_tool_NodeCreationDescription348
        self.diagram_tool_NodeCreationDescription = diagram_tool_NodeCreationDescription if diagram_tool_NodeCreationDescription is not None else set()
        self.diagram_tool_NodeCreationDescription350 = diagram_tool_NodeCreationDescription350
        self.diagram_tool_NodeCreationDescription352 = diagram_tool_NodeCreationDescription352 if diagram_tool_NodeCreationDescription352 is not None else set()
        
    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def diagram_tool_NodeCreationDescription350(self):
        return self.__diagram_tool_NodeCreationDescription350

    @diagram_tool_NodeCreationDescription350.setter
    def diagram_tool_NodeCreationDescription350(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription350", None)
        self.__diagram_tool_NodeCreationDescription350 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialNodeCreationOperation"):
                opp_val = getattr(old_value, "tool_InitialNodeCreationOperation", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialNodeCreationOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialNodeCreationOperation"):
                opp_val = getattr(value, "tool_InitialNodeCreationOperation", None)
                setattr(value, "tool_InitialNodeCreationOperation", self)

    @property
    def diagram_tool_NodeCreationDescription(self):
        return self.__diagram_tool_NodeCreationDescription

    @diagram_tool_NodeCreationDescription.setter
    def diagram_tool_NodeCreationDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription", None)
        self.__diagram_tool_NodeCreationDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping344"):
                    opp_val = getattr(item, "NodeMapping344", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping344", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping344"):
                    opp_val = getattr(item, "NodeMapping344", None)
                    
                    setattr(item, "NodeMapping344", self)
                    

    @property
    def diagram_tool_NodeCreationDescription352(self):
        return self.__diagram_tool_NodeCreationDescription352

    @diagram_tool_NodeCreationDescription352.setter
    def diagram_tool_NodeCreationDescription352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription352", None)
        self.__diagram_tool_NodeCreationDescription352 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractNodeMapping353"):
                    opp_val = getattr(item, "AbstractNodeMapping353", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractNodeMapping353", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractNodeMapping353"):
                    opp_val = getattr(item, "AbstractNodeMapping353", None)
                    
                    setattr(item, "AbstractNodeMapping353", self)
                    

    @property
    def diagram_tool_NodeCreationDescription348(self):
        return self.__diagram_tool_NodeCreationDescription348

    @diagram_tool_NodeCreationDescription348.setter
    def diagram_tool_NodeCreationDescription348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription348", None)
        self.__diagram_tool_NodeCreationDescription348 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable"):
                opp_val = getattr(value, "tool_ContainerViewVariable", None)
                setattr(value, "tool_ContainerViewVariable", self)

    @property
    def diagram_tool_NodeCreationDescription346(self):
        return self.__diagram_tool_NodeCreationDescription346

    @diagram_tool_NodeCreationDescription346.setter
    def diagram_tool_NodeCreationDescription346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription346", None)
        self.__diagram_tool_NodeCreationDescription346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_NodeCreationVariable"):
                opp_val = getattr(old_value, "tool_NodeCreationVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_NodeCreationVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_NodeCreationVariable"):
                opp_val = getattr(value, "tool_NodeCreationVariable", None)
                setattr(value, "tool_NodeCreationVariable", self)

class tool_ToolGroup:

    pass
class diagram_tool_ToolGroupExtension:

    pass
class tool_ContainerViewVariable:

    pass
class tool_NodeCreationVariable:

    pass
class tool_ToolEntry:

    pass
class ToolEntry:

    pass
class diagram_tool_ToolGroup(ToolEntry):

    pass
class tool_ToolGroupExtension:

    pass
class tool_PopupMenu:

    pass
class BasicLabelStyleDescription:

    pass
class diagram_style_CenterLabelStyleDescription(BasicLabelStyleDescription):

    pass
class diagram_style_BeginLabelStyleDescription(BasicLabelStyleDescription):

    pass
class diagram_style_HideLabelCapabilityStyleDescription(ABC):

    def __init__(self, hideLabelByDefault: bool):
        self.hideLabelByDefault = hideLabelByDefault
        
    @property
    def hideLabelByDefault(self) -> bool:
        return self.__hideLabelByDefault

    @hideLabelByDefault.setter
    def hideLabelByDefault(self, hideLabelByDefault: bool):
        self.__hideLabelByDefault = hideLabelByDefault

class EdgeStyleDescription:

    pass
class diagram_style_BracketEdgeStyleDescription(EdgeStyleDescription):

    pass
class diagram_style_EndLabelStyleDescription(BasicLabelStyleDescription):

    pass
class style_EndLabelStyleDescription:

    pass
class style_CenterLabelStyleDescription:

    pass
class style_BeginLabelStyleDescription:

    pass
class style_LabelBorderStyleDescription:

    pass
class style_RoundedCornerStyleDescription:

    pass
class style_SizeComputationContainerStyleDescription:

    pass
class diagram_style_SizeComputationContainerStyleDescription(ABC):

    def __init__(self, widthComputationExpression: str, heightComputationExpression: str):
        self.widthComputationExpression = widthComputationExpression
        self.heightComputationExpression = heightComputationExpression
        
    @property
    def heightComputationExpression(self) -> str:
        return self.__heightComputationExpression

    @heightComputationExpression.setter
    def heightComputationExpression(self, heightComputationExpression: str):
        self.__heightComputationExpression = heightComputationExpression

    @property
    def widthComputationExpression(self) -> str:
        return self.__widthComputationExpression

    @widthComputationExpression.setter
    def widthComputationExpression(self, widthComputationExpression: str):
        self.__widthComputationExpression = widthComputationExpression

class diagram_style_GaugeSectionDescription:

    def __init__(self, minValueExpression: str, label: str, maxValueExpression: str, valueExpression: str, diagram_style_GaugeSectionDescription301: "ColorDescription" = None, diagram_style_GaugeSectionDescription: "ColorDescription" = None):
        self.minValueExpression = minValueExpression
        self.label = label
        self.maxValueExpression = maxValueExpression
        self.valueExpression = valueExpression
        self.diagram_style_GaugeSectionDescription301 = diagram_style_GaugeSectionDescription301
        self.diagram_style_GaugeSectionDescription = diagram_style_GaugeSectionDescription
        
    @property
    def minValueExpression(self) -> str:
        return self.__minValueExpression

    @minValueExpression.setter
    def minValueExpression(self, minValueExpression: str):
        self.__minValueExpression = minValueExpression

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def valueExpression(self) -> str:
        return self.__valueExpression

    @valueExpression.setter
    def valueExpression(self, valueExpression: str):
        self.__valueExpression = valueExpression

    @property
    def maxValueExpression(self) -> str:
        return self.__maxValueExpression

    @maxValueExpression.setter
    def maxValueExpression(self, maxValueExpression: str):
        self.__maxValueExpression = maxValueExpression

    @property
    def diagram_style_GaugeSectionDescription301(self):
        return self.__diagram_style_GaugeSectionDescription301

    @diagram_style_GaugeSectionDescription301.setter
    def diagram_style_GaugeSectionDescription301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_GaugeSectionDescription__diagram_style_GaugeSectionDescription301", None)
        self.__diagram_style_GaugeSectionDescription301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription302"):
                opp_val = getattr(old_value, "ColorDescription302", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription302", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription302"):
                opp_val = getattr(value, "ColorDescription302", None)
                setattr(value, "ColorDescription302", self)

    @property
    def diagram_style_GaugeSectionDescription(self):
        return self.__diagram_style_GaugeSectionDescription

    @diagram_style_GaugeSectionDescription.setter
    def diagram_style_GaugeSectionDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_GaugeSectionDescription__diagram_style_GaugeSectionDescription", None)
        self.__diagram_style_GaugeSectionDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription299"):
                opp_val = getattr(old_value, "ColorDescription299", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription299", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription299"):
                opp_val = getattr(value, "ColorDescription299", None)
                setattr(value, "ColorDescription299", self)

class style_GaugeSectionDescription:

    pass
class NodeStyleDescription:

    pass
class diagram_style_BundledImageDescription(NodeStyleDescription):

    def __init__(self, shape: str, providedShapeID: str, diagram_style_BundledImageDescription: "ColorDescription" = None):
        self.shape = shape
        self.providedShapeID = providedShapeID
        self.diagram_style_BundledImageDescription = diagram_style_BundledImageDescription
        
    @property
    def providedShapeID(self) -> str:
        return self.__providedShapeID

    @providedShapeID.setter
    def providedShapeID(self, providedShapeID: str):
        self.__providedShapeID = providedShapeID

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def diagram_style_BundledImageDescription(self):
        return self.__diagram_style_BundledImageDescription

    @diagram_style_BundledImageDescription.setter
    def diagram_style_BundledImageDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_BundledImageDescription__diagram_style_BundledImageDescription", None)
        self.__diagram_style_BundledImageDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription292"):
                opp_val = getattr(old_value, "ColorDescription292", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription292"):
                opp_val = getattr(value, "ColorDescription292", None)
                setattr(value, "ColorDescription292", self)

class diagram_style_EllipseNodeDescription(NodeStyleDescription):

    def __init__(self, verticalDiameterComputationExpression: str, horizontalDiameterComputationExpression: str, diagram_style_EllipseNodeDescription: "ColorDescription" = None):
        self.verticalDiameterComputationExpression = verticalDiameterComputationExpression
        self.horizontalDiameterComputationExpression = horizontalDiameterComputationExpression
        self.diagram_style_EllipseNodeDescription = diagram_style_EllipseNodeDescription
        
    @property
    def verticalDiameterComputationExpression(self) -> str:
        return self.__verticalDiameterComputationExpression

    @verticalDiameterComputationExpression.setter
    def verticalDiameterComputationExpression(self, verticalDiameterComputationExpression: str):
        self.__verticalDiameterComputationExpression = verticalDiameterComputationExpression

    @property
    def horizontalDiameterComputationExpression(self) -> str:
        return self.__horizontalDiameterComputationExpression

    @horizontalDiameterComputationExpression.setter
    def horizontalDiameterComputationExpression(self, horizontalDiameterComputationExpression: str):
        self.__horizontalDiameterComputationExpression = horizontalDiameterComputationExpression

    @property
    def diagram_style_EllipseNodeDescription(self):
        return self.__diagram_style_EllipseNodeDescription

    @diagram_style_EllipseNodeDescription.setter
    def diagram_style_EllipseNodeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EllipseNodeDescription__diagram_style_EllipseNodeDescription", None)
        self.__diagram_style_EllipseNodeDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription290"):
                opp_val = getattr(old_value, "ColorDescription290", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription290"):
                opp_val = getattr(value, "ColorDescription290", None)
                setattr(value, "ColorDescription290", self)

class diagram_style_DotDescription(NodeStyleDescription):

    def __init__(self, strokeSizeComputationExpression: str, diagram_style_DotDescription: "ColorDescription" = None):
        self.strokeSizeComputationExpression = strokeSizeComputationExpression
        self.diagram_style_DotDescription = diagram_style_DotDescription
        
    @property
    def strokeSizeComputationExpression(self) -> str:
        return self.__strokeSizeComputationExpression

    @strokeSizeComputationExpression.setter
    def strokeSizeComputationExpression(self, strokeSizeComputationExpression: str):
        self.__strokeSizeComputationExpression = strokeSizeComputationExpression

    @property
    def diagram_style_DotDescription(self):
        return self.__diagram_style_DotDescription

    @diagram_style_DotDescription.setter
    def diagram_style_DotDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_DotDescription__diagram_style_DotDescription", None)
        self.__diagram_style_DotDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription296"):
                opp_val = getattr(old_value, "ColorDescription296", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription296", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription296"):
                opp_val = getattr(value, "ColorDescription296", None)
                setattr(value, "ColorDescription296", self)

class diagram_style_GaugeCompositeStyleDescription(NodeStyleDescription):

    def __init__(self, alignment: str, diagram_style_GaugeCompositeStyleDescription: set["style_GaugeSectionDescription"] = None):
        self.alignment = alignment
        self.diagram_style_GaugeCompositeStyleDescription = diagram_style_GaugeCompositeStyleDescription if diagram_style_GaugeCompositeStyleDescription is not None else set()
        
    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def diagram_style_GaugeCompositeStyleDescription(self):
        return self.__diagram_style_GaugeCompositeStyleDescription

    @diagram_style_GaugeCompositeStyleDescription.setter
    def diagram_style_GaugeCompositeStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_GaugeCompositeStyleDescription__diagram_style_GaugeCompositeStyleDescription", None)
        self.__diagram_style_GaugeCompositeStyleDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "style_GaugeSectionDescription"):
                    opp_val = getattr(item, "style_GaugeSectionDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "style_GaugeSectionDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "style_GaugeSectionDescription"):
                    opp_val = getattr(item, "style_GaugeSectionDescription", None)
                    
                    setattr(item, "style_GaugeSectionDescription", self)
                    

class diagram_style_NoteDescription(NodeStyleDescription):

    pass
class diagram_style_SquareDescription(NodeStyleDescription):

    def __init__(self, width: str, height: str, diagram_style_SquareDescription: "ColorDescription" = None):
        self.width = width
        self.height = height
        self.diagram_style_SquareDescription = diagram_style_SquareDescription
        
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
    def diagram_style_SquareDescription(self):
        return self.__diagram_style_SquareDescription

    @diagram_style_SquareDescription.setter
    def diagram_style_SquareDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_SquareDescription__diagram_style_SquareDescription", None)
        self.__diagram_style_SquareDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription286"):
                opp_val = getattr(old_value, "ColorDescription286", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription286"):
                opp_val = getattr(value, "ColorDescription286", None)
                setattr(value, "ColorDescription286", self)

class diagram_style_CustomStyleDescription(NodeStyleDescription):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class diagram_style_LozengeNodeDescription(NodeStyleDescription):

    def __init__(self, widthComputationExpression: str, heightComputationExpression: str, diagram_style_LozengeNodeDescription: "ColorDescription" = None):
        self.widthComputationExpression = widthComputationExpression
        self.heightComputationExpression = heightComputationExpression
        self.diagram_style_LozengeNodeDescription = diagram_style_LozengeNodeDescription
        
    @property
    def heightComputationExpression(self) -> str:
        return self.__heightComputationExpression

    @heightComputationExpression.setter
    def heightComputationExpression(self, heightComputationExpression: str):
        self.__heightComputationExpression = heightComputationExpression

    @property
    def widthComputationExpression(self) -> str:
        return self.__widthComputationExpression

    @widthComputationExpression.setter
    def widthComputationExpression(self, widthComputationExpression: str):
        self.__widthComputationExpression = widthComputationExpression

    @property
    def diagram_style_LozengeNodeDescription(self):
        return self.__diagram_style_LozengeNodeDescription

    @diagram_style_LozengeNodeDescription.setter
    def diagram_style_LozengeNodeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_LozengeNodeDescription__diagram_style_LozengeNodeDescription", None)
        self.__diagram_style_LozengeNodeDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription288"):
                opp_val = getattr(old_value, "ColorDescription288", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription288"):
                opp_val = getattr(value, "ColorDescription288", None)
                setattr(value, "ColorDescription288", self)

class style_BorderedStyleDescription:

    pass
class ColorDescription:

    pass
class style_HideLabelCapabilityStyleDescription:

    pass
class style_TooltipStyleDescription:

    pass
class style_LabelStyleDescription:

    pass
class diagram_style_ContainerStyleDescription(style_BorderedStyleDescription, style_LabelStyleDescription, style_HideLabelCapabilityStyleDescription, style_RoundedCornerStyleDescription, style_TooltipStyleDescription):

    def __init__(self, roundedCorner: bool):
        self.roundedCorner = roundedCorner
        
    @property
    def roundedCorner(self) -> bool:
        return self.__roundedCorner

    @roundedCorner.setter
    def roundedCorner(self, roundedCorner: bool):
        self.__roundedCorner = roundedCorner

class Customization:

    pass
class DecorationDescriptionsSet:

    pass
class StyleDescription:

    pass
class diagram_style_EdgeStyleDescription(StyleDescription):

    def __init__(self, lineStyle: str, sourceArrow: str, foldingStyle: str, endsCentering: str, targetArrow: str, sizeComputationExpression: str, routingStyle: str, diagram_style_EdgeStyleDescription: "ColorDescription" = None, diagram_style_EdgeStyleDescription315: "style_BeginLabelStyleDescription" = None, diagram_style_EdgeStyleDescription317: "style_CenterLabelStyleDescription" = None, diagram_style_EdgeStyleDescription319: "style_EndLabelStyleDescription" = None, diagram_style_EdgeStyleDescription321: set["DiagramElementMapping"] = None, diagram_style_EdgeStyleDescription324: set["DiagramElementMapping"] = None):
        self.lineStyle = lineStyle
        self.sourceArrow = sourceArrow
        self.foldingStyle = foldingStyle
        self.endsCentering = endsCentering
        self.targetArrow = targetArrow
        self.sizeComputationExpression = sizeComputationExpression
        self.routingStyle = routingStyle
        self.diagram_style_EdgeStyleDescription = diagram_style_EdgeStyleDescription
        self.diagram_style_EdgeStyleDescription315 = diagram_style_EdgeStyleDescription315
        self.diagram_style_EdgeStyleDescription317 = diagram_style_EdgeStyleDescription317
        self.diagram_style_EdgeStyleDescription319 = diagram_style_EdgeStyleDescription319
        self.diagram_style_EdgeStyleDescription321 = diagram_style_EdgeStyleDescription321 if diagram_style_EdgeStyleDescription321 is not None else set()
        self.diagram_style_EdgeStyleDescription324 = diagram_style_EdgeStyleDescription324 if diagram_style_EdgeStyleDescription324 is not None else set()
        
    @property
    def foldingStyle(self) -> str:
        return self.__foldingStyle

    @foldingStyle.setter
    def foldingStyle(self, foldingStyle: str):
        self.__foldingStyle = foldingStyle

    @property
    def endsCentering(self) -> str:
        return self.__endsCentering

    @endsCentering.setter
    def endsCentering(self, endsCentering: str):
        self.__endsCentering = endsCentering

    @property
    def routingStyle(self) -> str:
        return self.__routingStyle

    @routingStyle.setter
    def routingStyle(self, routingStyle: str):
        self.__routingStyle = routingStyle

    @property
    def sourceArrow(self) -> str:
        return self.__sourceArrow

    @sourceArrow.setter
    def sourceArrow(self, sourceArrow: str):
        self.__sourceArrow = sourceArrow

    @property
    def targetArrow(self) -> str:
        return self.__targetArrow

    @targetArrow.setter
    def targetArrow(self, targetArrow: str):
        self.__targetArrow = targetArrow

    @property
    def lineStyle(self) -> str:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle

    @property
    def sizeComputationExpression(self) -> str:
        return self.__sizeComputationExpression

    @sizeComputationExpression.setter
    def sizeComputationExpression(self, sizeComputationExpression: str):
        self.__sizeComputationExpression = sizeComputationExpression

    @property
    def diagram_style_EdgeStyleDescription(self):
        return self.__diagram_style_EdgeStyleDescription

    @diagram_style_EdgeStyleDescription.setter
    def diagram_style_EdgeStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription", None)
        self.__diagram_style_EdgeStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription313"):
                opp_val = getattr(old_value, "ColorDescription313", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription313"):
                opp_val = getattr(value, "ColorDescription313", None)
                setattr(value, "ColorDescription313", self)

    @property
    def diagram_style_EdgeStyleDescription315(self):
        return self.__diagram_style_EdgeStyleDescription315

    @diagram_style_EdgeStyleDescription315.setter
    def diagram_style_EdgeStyleDescription315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription315", None)
        self.__diagram_style_EdgeStyleDescription315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_BeginLabelStyleDescription"):
                opp_val = getattr(old_value, "style_BeginLabelStyleDescription", None)
                if opp_val == self:
                    setattr(old_value, "style_BeginLabelStyleDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_BeginLabelStyleDescription"):
                opp_val = getattr(value, "style_BeginLabelStyleDescription", None)
                setattr(value, "style_BeginLabelStyleDescription", self)

    @property
    def diagram_style_EdgeStyleDescription321(self):
        return self.__diagram_style_EdgeStyleDescription321

    @diagram_style_EdgeStyleDescription321.setter
    def diagram_style_EdgeStyleDescription321(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription321", None)
        self.__diagram_style_EdgeStyleDescription321 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping322"):
                    opp_val = getattr(item, "DiagramElementMapping322", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping322"):
                    opp_val = getattr(item, "DiagramElementMapping322", None)
                    
                    setattr(item, "DiagramElementMapping322", self)
                    

    @property
    def diagram_style_EdgeStyleDescription319(self):
        return self.__diagram_style_EdgeStyleDescription319

    @diagram_style_EdgeStyleDescription319.setter
    def diagram_style_EdgeStyleDescription319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription319", None)
        self.__diagram_style_EdgeStyleDescription319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_EndLabelStyleDescription"):
                opp_val = getattr(old_value, "style_EndLabelStyleDescription", None)
                if opp_val == self:
                    setattr(old_value, "style_EndLabelStyleDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_EndLabelStyleDescription"):
                opp_val = getattr(value, "style_EndLabelStyleDescription", None)
                setattr(value, "style_EndLabelStyleDescription", self)

    @property
    def diagram_style_EdgeStyleDescription317(self):
        return self.__diagram_style_EdgeStyleDescription317

    @diagram_style_EdgeStyleDescription317.setter
    def diagram_style_EdgeStyleDescription317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription317", None)
        self.__diagram_style_EdgeStyleDescription317 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_CenterLabelStyleDescription"):
                opp_val = getattr(old_value, "style_CenterLabelStyleDescription", None)
                if opp_val == self:
                    setattr(old_value, "style_CenterLabelStyleDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_CenterLabelStyleDescription"):
                opp_val = getattr(value, "style_CenterLabelStyleDescription", None)
                setattr(value, "style_CenterLabelStyleDescription", self)

    @property
    def diagram_style_EdgeStyleDescription324(self):
        return self.__diagram_style_EdgeStyleDescription324

    @diagram_style_EdgeStyleDescription324.setter
    def diagram_style_EdgeStyleDescription324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription324", None)
        self.__diagram_style_EdgeStyleDescription324 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping325"):
                    opp_val = getattr(item, "DiagramElementMapping325", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping325", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping325"):
                    opp_val = getattr(item, "DiagramElementMapping325", None)
                    
                    setattr(item, "DiagramElementMapping325", self)
                    

class diagram_style_RoundedCornerStyleDescription(StyleDescription):

    def __init__(self, arcWidth: str, arcHeight: str):
        self.arcWidth = arcWidth
        self.arcHeight = arcHeight
        
    @property
    def arcWidth(self) -> str:
        return self.__arcWidth

    @arcWidth.setter
    def arcWidth(self, arcWidth: str):
        self.__arcWidth = arcWidth

    @property
    def arcHeight(self) -> str:
        return self.__arcHeight

    @arcHeight.setter
    def arcHeight(self, arcHeight: str):
        self.__arcHeight = arcHeight

class diagram_style_BorderedStyleDescription(StyleDescription):

    def __init__(self, borderSizeComputationExpression: str, borderLineStyle: str, diagram_style_BorderedStyleDescription: "ColorDescription" = None):
        self.borderSizeComputationExpression = borderSizeComputationExpression
        self.borderLineStyle = borderLineStyle
        self.diagram_style_BorderedStyleDescription = diagram_style_BorderedStyleDescription
        
    @property
    def borderLineStyle(self) -> str:
        return self.__borderLineStyle

    @borderLineStyle.setter
    def borderLineStyle(self, borderLineStyle: str):
        self.__borderLineStyle = borderLineStyle

    @property
    def borderSizeComputationExpression(self) -> str:
        return self.__borderSizeComputationExpression

    @borderSizeComputationExpression.setter
    def borderSizeComputationExpression(self, borderSizeComputationExpression: str):
        self.__borderSizeComputationExpression = borderSizeComputationExpression

    @property
    def diagram_style_BorderedStyleDescription(self):
        return self.__diagram_style_BorderedStyleDescription

    @diagram_style_BorderedStyleDescription.setter
    def diagram_style_BorderedStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_BorderedStyleDescription__diagram_style_BorderedStyleDescription", None)
        self.__diagram_style_BorderedStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription"):
                opp_val = getattr(old_value, "ColorDescription", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription"):
                opp_val = getattr(value, "ColorDescription", None)
                setattr(value, "ColorDescription", self)

class tool_ContainerDropDescription:

    pass
class diagram_description_DragAndDropTargetDescription(ABC):

    pass
class description_EndUserDocumentedElement:

    pass
class DecorationDescription:

    pass
class diagram_description_MappingBasedDecoration(DecorationDescription):

    pass
class ConditionalStyleDescription:

    pass
class diagram_description_ConditionalEdgeStyleDescription(ConditionalStyleDescription):

    pass
class diagram_description_ConditionalContainerStyleDescription(ConditionalStyleDescription):

    pass
class diagram_description_ConditionalNodeStyleDescription(ConditionalStyleDescription):

    pass
class DocumentedElement:

    pass
class diagram_concern_ConcernSet(DocumentedElement):

    pass
class diagram_description_Layout(DocumentedElement):

    pass
class diagram_description_IEdgeMapping(ABC):

    def __init__(self):
        
    def getBestStyle(self, viewVariable: str, containerVariable: str, modelElement: str) -> EdgeStyle:
        # TODO: Implement getBestStyle method
        pass

class AbstractNodeMapping:

    pass
class description_IdentifiedElement:

    pass
class style_EdgeStyleDescription:

    pass
class tool_ReconnectEdgeDescription:

    pass
class ConditionalEdgeStyleDescription:

    pass
class description_ContainerMapping:

    pass
class description_AbstractMappingImport:

    pass
class diagram_description_ContainerMappingImport(description_ContainerMapping, description_AbstractMappingImport):

    pass
class description_NodeMapping:

    pass
class diagram_description_NodeMappingImport(description_AbstractMappingImport, description_NodeMapping):

    pass
class description_IEdgeMapping:

    pass
class ConditionalContainerStyleDescription:

    pass
class style_ContainerStyleDescription:

    pass
class diagram_style_FlatContainerStyleDescription(style_ContainerStyleDescription, style_SizeComputationContainerStyleDescription):

    def __init__(self, backgroundStyle: str, diagram_style_FlatContainerStyleDescription: "ColorDescription" = None, diagram_style_FlatContainerStyleDescription306: "ColorDescription" = None, diagram_style_FlatContainerStyleDescription309: "style_LabelBorderStyleDescription" = None, style_ContainerStyleDescription248: "diagram_description_ConditionalContainerStyleDescription", style_ContainerStyleDescription: "diagram_description_ContainerMapping"):
        self.backgroundStyle = backgroundStyle
        self.diagram_style_FlatContainerStyleDescription = diagram_style_FlatContainerStyleDescription
        self.diagram_style_FlatContainerStyleDescription306 = diagram_style_FlatContainerStyleDescription306
        self.diagram_style_FlatContainerStyleDescription309 = diagram_style_FlatContainerStyleDescription309
        
    @property
    def backgroundStyle(self) -> str:
        return self.__backgroundStyle

    @backgroundStyle.setter
    def backgroundStyle(self, backgroundStyle: str):
        self.__backgroundStyle = backgroundStyle

    @property
    def diagram_style_FlatContainerStyleDescription(self):
        return self.__diagram_style_FlatContainerStyleDescription

    @diagram_style_FlatContainerStyleDescription.setter
    def diagram_style_FlatContainerStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_FlatContainerStyleDescription__diagram_style_FlatContainerStyleDescription", None)
        self.__diagram_style_FlatContainerStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription304"):
                opp_val = getattr(old_value, "ColorDescription304", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription304", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription304"):
                opp_val = getattr(value, "ColorDescription304", None)
                setattr(value, "ColorDescription304", self)

    @property
    def diagram_style_FlatContainerStyleDescription309(self):
        return self.__diagram_style_FlatContainerStyleDescription309

    @diagram_style_FlatContainerStyleDescription309.setter
    def diagram_style_FlatContainerStyleDescription309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_FlatContainerStyleDescription__diagram_style_FlatContainerStyleDescription309", None)
        self.__diagram_style_FlatContainerStyleDescription309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_LabelBorderStyleDescription"):
                opp_val = getattr(old_value, "style_LabelBorderStyleDescription", None)
                if opp_val == self:
                    setattr(old_value, "style_LabelBorderStyleDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_LabelBorderStyleDescription"):
                opp_val = getattr(value, "style_LabelBorderStyleDescription", None)
                setattr(value, "style_LabelBorderStyleDescription", self)

    @property
    def diagram_style_FlatContainerStyleDescription306(self):
        return self.__diagram_style_FlatContainerStyleDescription306

    @diagram_style_FlatContainerStyleDescription306.setter
    def diagram_style_FlatContainerStyleDescription306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_FlatContainerStyleDescription__diagram_style_FlatContainerStyleDescription306", None)
        self.__diagram_style_FlatContainerStyleDescription306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription307"):
                opp_val = getattr(old_value, "ColorDescription307", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription307"):
                opp_val = getattr(value, "ColorDescription307", None)
                setattr(value, "ColorDescription307", self)

class diagram_style_ShapeContainerStyleDescription(style_ContainerStyleDescription, style_SizeComputationContainerStyleDescription):

    def __init__(self, shape: str, diagram_style_ShapeContainerStyleDescription: "ColorDescription" = None, style_ContainerStyleDescription248: "diagram_description_ConditionalContainerStyleDescription", style_ContainerStyleDescription: "diagram_description_ContainerMapping"):
        self.shape = shape
        self.diagram_style_ShapeContainerStyleDescription = diagram_style_ShapeContainerStyleDescription
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def diagram_style_ShapeContainerStyleDescription(self):
        return self.__diagram_style_ShapeContainerStyleDescription

    @diagram_style_ShapeContainerStyleDescription.setter
    def diagram_style_ShapeContainerStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_ShapeContainerStyleDescription__diagram_style_ShapeContainerStyleDescription", None)
        self.__diagram_style_ShapeContainerStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription311"):
                opp_val = getattr(old_value, "ColorDescription311", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription311", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription311"):
                opp_val = getattr(value, "ColorDescription311", None)
                setattr(value, "ColorDescription311", self)

class ConditionalNodeStyleDescription:

    pass
class style_NodeStyleDescription:

    pass
class diagram_style_WorkspaceImageDescription(style_NodeStyleDescription, style_ContainerStyleDescription):

    def __init__(self, workspacePath: str, style_NodeStyleDescription: "diagram_description_NodeMapping", style_NodeStyleDescription244: "diagram_description_ConditionalNodeStyleDescription", style_ContainerStyleDescription248: "diagram_description_ConditionalContainerStyleDescription", style_ContainerStyleDescription: "diagram_description_ContainerMapping"):
        self.workspacePath = workspacePath
        
    @property
    def workspacePath(self) -> str:
        return self.__workspacePath

    @workspacePath.setter
    def workspacePath(self, workspacePath: str):
        self.__workspacePath = workspacePath

class description_AbstractNodeMapping:

    pass
class description_DiagramElementMapping:

    pass
class tool_DoubleClickDescription:

    pass
class tool_DirectEditLabel:

    pass
class tool_DeleteElementDescription:

    pass
class description_RepresentationElementMapping:

    pass
class tool_ToolSection:

    pass
class RepresentationExtensionDescription:

    pass
class diagram_description_DiagramExtensionDescription(RepresentationExtensionDescription):

    pass
class description_DiagramDescription:

    pass
class description_RepresentationImportDescription:

    pass
class diagram_description_DiagramImportDescription(description_RepresentationImportDescription, description_DiagramDescription):

    pass
class EdgeMappingImport:

    pass
class tool_InitialOperation:

    pass
class Layout:

    pass
class diagram_description_OrderedTreeLayout(Layout):

    def __init__(self, childrenExpression: str, diagram_description_OrderedTreeLayout: set["AbstractNodeMapping"] = None, Layout: "diagram_description_DiagramDescription"):
        self.childrenExpression = childrenExpression
        self.diagram_description_OrderedTreeLayout = diagram_description_OrderedTreeLayout if diagram_description_OrderedTreeLayout is not None else set()
        
    @property
    def childrenExpression(self) -> str:
        return self.__childrenExpression

    @childrenExpression.setter
    def childrenExpression(self, childrenExpression: str):
        self.__childrenExpression = childrenExpression

    @property
    def diagram_description_OrderedTreeLayout(self):
        return self.__diagram_description_OrderedTreeLayout

    @diagram_description_OrderedTreeLayout.setter
    def diagram_description_OrderedTreeLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_OrderedTreeLayout__diagram_description_OrderedTreeLayout", None)
        self.__diagram_description_OrderedTreeLayout = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractNodeMapping250"):
                    opp_val = getattr(item, "AbstractNodeMapping250", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractNodeMapping250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractNodeMapping250"):
                    opp_val = getattr(item, "AbstractNodeMapping250", None)
                    
                    setattr(item, "AbstractNodeMapping250", self)
                    

class diagram_description_CompositeLayout(Layout):

    def __init__(self, padding: int, direction: str, Layout: "diagram_description_DiagramDescription"):
        self.padding = padding
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def padding(self) -> int:
        return self.__padding

    @padding.setter
    def padding(self, padding: int):
        self.__padding = padding

class tool_RepresentationCreationDescription:

    pass
class EdgeMapping:

    pass
class tool_AbstractToolDescription:

    pass
class concern_ConcernSet:

    pass
class validation_ValidationSet:

    pass
class TypedVariable:

    pass
class VariableValue:

    pass
class diagram_EObjectVariableValue(VariableValue):

    pass
class diagram_TypedVariableValue(VariableValue):

    def __init__(self, value: str, diagram_TypedVariableValue: "TypedVariable" = None):
        self.value = value
        self.diagram_TypedVariableValue = diagram_TypedVariableValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def diagram_TypedVariableValue(self):
        return self.__diagram_TypedVariableValue

    @diagram_TypedVariableValue.setter
    def diagram_TypedVariableValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_TypedVariableValue__diagram_TypedVariableValue", None)
        self.__diagram_TypedVariableValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TypedVariable"):
                opp_val = getattr(old_value, "TypedVariable", None)
                if opp_val == self:
                    setattr(old_value, "TypedVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TypedVariable"):
                opp_val = getattr(value, "TypedVariable", None)
                setattr(value, "TypedVariable", self)

class diagram_HideLabelCapabilityStyle(ABC):

    def __init__(self, hideLabelByDefault: bool):
        self.hideLabelByDefault = hideLabelByDefault
        
    @property
    def hideLabelByDefault(self) -> bool:
        return self.__hideLabelByDefault

    @hideLabelByDefault.setter
    def hideLabelByDefault(self, hideLabelByDefault: bool):
        self.__hideLabelByDefault = hideLabelByDefault

class description_PasteTargetDescription:

    pass
class diagram_description_DiagramElementMapping(description_PasteTargetDescription, description_RepresentationElementMapping):

    def __init__(self, semanticCandidatesExpression: str, createElements: bool, preconditionExpression: str, semanticElements: str, synchronizationLock: bool, diagram_description_DiagramElementMapping: "tool_DeleteElementDescription" = None, diagram_description_DiagramElementMapping190: "tool_DirectEditLabel" = None, tool: "tool_DoubleClickDescription" = None):
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.createElements = createElements
        self.preconditionExpression = preconditionExpression
        self.semanticElements = semanticElements
        self.synchronizationLock = synchronizationLock
        self.diagram_description_DiagramElementMapping = diagram_description_DiagramElementMapping
        self.diagram_description_DiagramElementMapping190 = diagram_description_DiagramElementMapping190
        self.tool = tool
        
    @property
    def synchronizationLock(self) -> bool:
        return self.__synchronizationLock

    @synchronizationLock.setter
    def synchronizationLock(self, synchronizationLock: bool):
        self.__synchronizationLock = synchronizationLock

    @property
    def createElements(self) -> bool:
        return self.__createElements

    @createElements.setter
    def createElements(self, createElements: bool):
        self.__createElements = createElements

    @property
    def preconditionExpression(self) -> str:
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression

    @property
    def semanticCandidatesExpression(self) -> str:
        return self.__semanticCandidatesExpression

    @semanticCandidatesExpression.setter
    def semanticCandidatesExpression(self, semanticCandidatesExpression: str):
        self.__semanticCandidatesExpression = semanticCandidatesExpression

    @property
    def semanticElements(self) -> str:
        return self.__semanticElements

    @semanticElements.setter
    def semanticElements(self, semanticElements: str):
        self.__semanticElements = semanticElements

    @property
    def diagram_description_DiagramElementMapping190(self):
        return self.__diagram_description_DiagramElementMapping190

    @diagram_description_DiagramElementMapping190.setter
    def diagram_description_DiagramElementMapping190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramElementMapping__diagram_description_DiagramElementMapping190", None)
        self.__diagram_description_DiagramElementMapping190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DirectEditLabel"):
                opp_val = getattr(old_value, "tool_DirectEditLabel", None)
                if opp_val == self:
                    setattr(old_value, "tool_DirectEditLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DirectEditLabel"):
                opp_val = getattr(value, "tool_DirectEditLabel", None)
                setattr(value, "tool_DirectEditLabel", self)

    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramElementMapping__tool", None)
        self.__tool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description"):
                opp_val = getattr(old_value, "description", None)
                if opp_val == self:
                    setattr(old_value, "description", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description"):
                opp_val = getattr(value, "description", None)
                setattr(value, "description", self)

    @property
    def diagram_description_DiagramElementMapping(self):
        return self.__diagram_description_DiagramElementMapping

    @diagram_description_DiagramElementMapping.setter
    def diagram_description_DiagramElementMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramElementMapping__diagram_description_DiagramElementMapping", None)
        self.__diagram_description_DiagramElementMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DeleteElementDescription"):
                opp_val = getattr(old_value, "tool_DeleteElementDescription", None)
                if opp_val == self:
                    setattr(old_value, "tool_DeleteElementDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DeleteElementDescription"):
                opp_val = getattr(value, "tool_DeleteElementDescription", None)
                setattr(value, "tool_DeleteElementDescription", self)

    def checkPrecondition(self, modelElement: str, container: str, containerView: str) -> bool:
        # TODO: Implement checkPrecondition method
        pass

    def isFrom(self, element: str) -> bool:
        # TODO: Implement isFrom method
        pass

    def getAllMappings(self) -> str:
        # TODO: Implement getAllMappings method
        pass

class description_RepresentationDescription:

    pass
class description_DragAndDropTargetDescription:

    pass
class diagram_description_ContainerMapping(description_AbstractNodeMapping, description_DragAndDropTargetDescription):

    def __init__(self, childrenPresentation: str, diagram_description_ContainerMapping212: set["ContainerMapping"] = None, diagram_description_ContainerMapping215: set["ContainerMapping"] = None, diagram_description_ContainerMapping218: "style_ContainerStyleDescription" = None, diagram_description_ContainerMapping220: set["ConditionalContainerStyleDescription"] = None, diagram_description_ContainerMapping: set["NodeMapping"] = None, diagram_description_ContainerMapping203: set["NodeMapping"] = None, diagram_description_ContainerMapping206: set["NodeMapping"] = None, diagram_description_ContainerMapping209: set["ContainerMapping"] = None):
        self.childrenPresentation = childrenPresentation
        self.diagram_description_ContainerMapping212 = diagram_description_ContainerMapping212 if diagram_description_ContainerMapping212 is not None else set()
        self.diagram_description_ContainerMapping215 = diagram_description_ContainerMapping215 if diagram_description_ContainerMapping215 is not None else set()
        self.diagram_description_ContainerMapping218 = diagram_description_ContainerMapping218
        self.diagram_description_ContainerMapping220 = diagram_description_ContainerMapping220 if diagram_description_ContainerMapping220 is not None else set()
        self.diagram_description_ContainerMapping = diagram_description_ContainerMapping if diagram_description_ContainerMapping is not None else set()
        self.diagram_description_ContainerMapping203 = diagram_description_ContainerMapping203 if diagram_description_ContainerMapping203 is not None else set()
        self.diagram_description_ContainerMapping206 = diagram_description_ContainerMapping206 if diagram_description_ContainerMapping206 is not None else set()
        self.diagram_description_ContainerMapping209 = diagram_description_ContainerMapping209 if diagram_description_ContainerMapping209 is not None else set()
        
    @property
    def childrenPresentation(self) -> str:
        return self.__childrenPresentation

    @childrenPresentation.setter
    def childrenPresentation(self, childrenPresentation: str):
        self.__childrenPresentation = childrenPresentation

    @property
    def diagram_description_ContainerMapping215(self):
        return self.__diagram_description_ContainerMapping215

    @diagram_description_ContainerMapping215.setter
    def diagram_description_ContainerMapping215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping215", None)
        self.__diagram_description_ContainerMapping215 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping216"):
                    opp_val = getattr(item, "ContainerMapping216", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping216", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping216"):
                    opp_val = getattr(item, "ContainerMapping216", None)
                    
                    setattr(item, "ContainerMapping216", self)
                    

    @property
    def diagram_description_ContainerMapping218(self):
        return self.__diagram_description_ContainerMapping218

    @diagram_description_ContainerMapping218.setter
    def diagram_description_ContainerMapping218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping218", None)
        self.__diagram_description_ContainerMapping218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_ContainerStyleDescription"):
                opp_val = getattr(old_value, "style_ContainerStyleDescription", None)
                if opp_val == self:
                    setattr(old_value, "style_ContainerStyleDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_ContainerStyleDescription"):
                opp_val = getattr(value, "style_ContainerStyleDescription", None)
                setattr(value, "style_ContainerStyleDescription", self)

    @property
    def diagram_description_ContainerMapping209(self):
        return self.__diagram_description_ContainerMapping209

    @diagram_description_ContainerMapping209.setter
    def diagram_description_ContainerMapping209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping209", None)
        self.__diagram_description_ContainerMapping209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping210"):
                    opp_val = getattr(item, "ContainerMapping210", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping210"):
                    opp_val = getattr(item, "ContainerMapping210", None)
                    
                    setattr(item, "ContainerMapping210", self)
                    

    @property
    def diagram_description_ContainerMapping(self):
        return self.__diagram_description_ContainerMapping

    @diagram_description_ContainerMapping.setter
    def diagram_description_ContainerMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping", None)
        self.__diagram_description_ContainerMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping201"):
                    opp_val = getattr(item, "NodeMapping201", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping201"):
                    opp_val = getattr(item, "NodeMapping201", None)
                    
                    setattr(item, "NodeMapping201", self)
                    

    @property
    def diagram_description_ContainerMapping206(self):
        return self.__diagram_description_ContainerMapping206

    @diagram_description_ContainerMapping206.setter
    def diagram_description_ContainerMapping206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping206", None)
        self.__diagram_description_ContainerMapping206 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping207"):
                    opp_val = getattr(item, "NodeMapping207", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping207", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping207"):
                    opp_val = getattr(item, "NodeMapping207", None)
                    
                    setattr(item, "NodeMapping207", self)
                    

    @property
    def diagram_description_ContainerMapping203(self):
        return self.__diagram_description_ContainerMapping203

    @diagram_description_ContainerMapping203.setter
    def diagram_description_ContainerMapping203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping203", None)
        self.__diagram_description_ContainerMapping203 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping204"):
                    opp_val = getattr(item, "NodeMapping204", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping204", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping204"):
                    opp_val = getattr(item, "NodeMapping204", None)
                    
                    setattr(item, "NodeMapping204", self)
                    

    @property
    def diagram_description_ContainerMapping212(self):
        return self.__diagram_description_ContainerMapping212

    @diagram_description_ContainerMapping212.setter
    def diagram_description_ContainerMapping212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping212", None)
        self.__diagram_description_ContainerMapping212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping213"):
                    opp_val = getattr(item, "ContainerMapping213", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping213", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping213"):
                    opp_val = getattr(item, "ContainerMapping213", None)
                    
                    setattr(item, "ContainerMapping213", self)
                    

    @property
    def diagram_description_ContainerMapping220(self):
        return self.__diagram_description_ContainerMapping220

    @diagram_description_ContainerMapping220.setter
    def diagram_description_ContainerMapping220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping220", None)
        self.__diagram_description_ContainerMapping220 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConditionalContainerStyleDescription"):
                    opp_val = getattr(item, "ConditionalContainerStyleDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "ConditionalContainerStyleDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConditionalContainerStyleDescription"):
                    opp_val = getattr(item, "ConditionalContainerStyleDescription", None)
                    
                    setattr(item, "ConditionalContainerStyleDescription", self)
                    

    def getBestStyle(self, modelElement: str, containerVariable: str, viewVariable: str) -> ContainerStyle:
        # TODO: Implement getBestStyle method
        pass

class diagram_description_NodeMapping(description_AbstractNodeMapping, description_DragAndDropTargetDescription):

    def __init__(self, diagram_description_NodeMapping: "style_NodeStyleDescription" = None, diagram_description_NodeMapping199: set["ConditionalNodeStyleDescription"] = None):
        self.diagram_description_NodeMapping = diagram_description_NodeMapping
        self.diagram_description_NodeMapping199 = diagram_description_NodeMapping199 if diagram_description_NodeMapping199 is not None else set()
        
    @property
    def diagram_description_NodeMapping(self):
        return self.__diagram_description_NodeMapping

    @diagram_description_NodeMapping.setter
    def diagram_description_NodeMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_NodeMapping__diagram_description_NodeMapping", None)
        self.__diagram_description_NodeMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_NodeStyleDescription"):
                opp_val = getattr(old_value, "style_NodeStyleDescription", None)
                if opp_val == self:
                    setattr(old_value, "style_NodeStyleDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_NodeStyleDescription"):
                opp_val = getattr(value, "style_NodeStyleDescription", None)
                setattr(value, "style_NodeStyleDescription", self)

    @property
    def diagram_description_NodeMapping199(self):
        return self.__diagram_description_NodeMapping199

    @diagram_description_NodeMapping199.setter
    def diagram_description_NodeMapping199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_NodeMapping__diagram_description_NodeMapping199", None)
        self.__diagram_description_NodeMapping199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConditionalNodeStyleDescription"):
                    opp_val = getattr(item, "ConditionalNodeStyleDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "ConditionalNodeStyleDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConditionalNodeStyleDescription"):
                    opp_val = getattr(item, "ConditionalNodeStyleDescription", None)
                    
                    setattr(item, "ConditionalNodeStyleDescription", self)
                    

    def getNodesCandidates(self, semanticOrigin: str, container: str) -> str:
        # TODO: Implement getNodesCandidates method
        pass

    def createNode(self, modelElement: str, viewPoint: DDiagram, container: str) -> str:
        # TODO: Implement createNode method
        pass

    def getNodesCandidates(self, containerView: str, container: str, semanticOrigin: str) -> str:
        # TODO: Implement getNodesCandidates method
        pass

    def updateListElement(self, listElement: str):
        # TODO: Implement updateListElement method
        pass

    def updateNode(self, node: str):
        # TODO: Implement updateNode method
        pass

class diagram_description_DiagramDescription(description_DragAndDropTargetDescription, description_PasteTargetDescription, description_RepresentationDescription):

    def __init__(self, domainClass: str, preconditionExpression: str, rootExpression: str, enablePopupBars: bool, diagram_description_DiagramDescription130: set["ContainerMapping"] = None, diagram_description_DiagramDescription133: "validation_ValidationSet" = None, diagram_description_DiagramDescription135: "concern_ConcernSet" = None, diagram_description_DiagramDescription: set["filter_FilterDescription"] = None, diagram_description_DiagramDescription125: set["EdgeMapping"] = None, diagram_description_DiagramDescription127: set["NodeMapping"] = None, diagram_description_DiagramDescription142: "tool_RepresentationCreationDescription" = None, diagram_description_DiagramDescription144: "Layout" = None, diagram_description_DiagramDescription146: "tool_InitialOperation" = None, diagram_description_DiagramDescription137: set["tool_AbstractToolDescription"] = None, diagram_description_DiagramDescription139: "concern_ConcernDescription" = None, diagram_description_DiagramDescription163: set["EdgeMapping"] = None, diagram_description_DiagramDescription166: set["EdgeMappingImport"] = None, diagram_description_DiagramDescription168: set["ContainerMapping"] = None, diagram_description_DiagramDescription148: "Layer" = None, diagram_description_DiagramDescription151: set["AdditionalLayer"] = None, diagram_description_DiagramDescription154: set["Layer"] = None, diagram_description_DiagramDescription157: set["tool_AbstractToolDescription"] = None, diagram_description_DiagramDescription160: set["NodeMapping"] = None, diagram_description_DiagramDescription171: set["DiagramElementMapping"] = None, diagram_description_DiagramDescription174: "tool_ToolSection" = None, diagram_description_DiagramDescription176: set["tool_AbstractToolDescription"] = None):
        self.domainClass = domainClass
        self.preconditionExpression = preconditionExpression
        self.rootExpression = rootExpression
        self.enablePopupBars = enablePopupBars
        self.diagram_description_DiagramDescription130 = diagram_description_DiagramDescription130 if diagram_description_DiagramDescription130 is not None else set()
        self.diagram_description_DiagramDescription133 = diagram_description_DiagramDescription133
        self.diagram_description_DiagramDescription135 = diagram_description_DiagramDescription135
        self.diagram_description_DiagramDescription = diagram_description_DiagramDescription if diagram_description_DiagramDescription is not None else set()
        self.diagram_description_DiagramDescription125 = diagram_description_DiagramDescription125 if diagram_description_DiagramDescription125 is not None else set()
        self.diagram_description_DiagramDescription127 = diagram_description_DiagramDescription127 if diagram_description_DiagramDescription127 is not None else set()
        self.diagram_description_DiagramDescription142 = diagram_description_DiagramDescription142
        self.diagram_description_DiagramDescription144 = diagram_description_DiagramDescription144
        self.diagram_description_DiagramDescription146 = diagram_description_DiagramDescription146
        self.diagram_description_DiagramDescription137 = diagram_description_DiagramDescription137 if diagram_description_DiagramDescription137 is not None else set()
        self.diagram_description_DiagramDescription139 = diagram_description_DiagramDescription139
        self.diagram_description_DiagramDescription163 = diagram_description_DiagramDescription163 if diagram_description_DiagramDescription163 is not None else set()
        self.diagram_description_DiagramDescription166 = diagram_description_DiagramDescription166 if diagram_description_DiagramDescription166 is not None else set()
        self.diagram_description_DiagramDescription168 = diagram_description_DiagramDescription168 if diagram_description_DiagramDescription168 is not None else set()
        self.diagram_description_DiagramDescription148 = diagram_description_DiagramDescription148
        self.diagram_description_DiagramDescription151 = diagram_description_DiagramDescription151 if diagram_description_DiagramDescription151 is not None else set()
        self.diagram_description_DiagramDescription154 = diagram_description_DiagramDescription154 if diagram_description_DiagramDescription154 is not None else set()
        self.diagram_description_DiagramDescription157 = diagram_description_DiagramDescription157 if diagram_description_DiagramDescription157 is not None else set()
        self.diagram_description_DiagramDescription160 = diagram_description_DiagramDescription160 if diagram_description_DiagramDescription160 is not None else set()
        self.diagram_description_DiagramDescription171 = diagram_description_DiagramDescription171 if diagram_description_DiagramDescription171 is not None else set()
        self.diagram_description_DiagramDescription174 = diagram_description_DiagramDescription174
        self.diagram_description_DiagramDescription176 = diagram_description_DiagramDescription176 if diagram_description_DiagramDescription176 is not None else set()
        
    @property
    def preconditionExpression(self) -> str:
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression

    @property
    def enablePopupBars(self) -> bool:
        return self.__enablePopupBars

    @enablePopupBars.setter
    def enablePopupBars(self, enablePopupBars: bool):
        self.__enablePopupBars = enablePopupBars

    @property
    def rootExpression(self) -> str:
        return self.__rootExpression

    @rootExpression.setter
    def rootExpression(self, rootExpression: str):
        self.__rootExpression = rootExpression

    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def diagram_description_DiagramDescription171(self):
        return self.__diagram_description_DiagramDescription171

    @diagram_description_DiagramDescription171.setter
    def diagram_description_DiagramDescription171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription171", None)
        self.__diagram_description_DiagramDescription171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping172"):
                    opp_val = getattr(item, "DiagramElementMapping172", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping172"):
                    opp_val = getattr(item, "DiagramElementMapping172", None)
                    
                    setattr(item, "DiagramElementMapping172", self)
                    

    @property
    def diagram_description_DiagramDescription(self):
        return self.__diagram_description_DiagramDescription

    @diagram_description_DiagramDescription.setter
    def diagram_description_DiagramDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription", None)
        self.__diagram_description_DiagramDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "filter_FilterDescription123"):
                    opp_val = getattr(item, "filter_FilterDescription123", None)
                    
                    if opp_val == self:
                        setattr(item, "filter_FilterDescription123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filter_FilterDescription123"):
                    opp_val = getattr(item, "filter_FilterDescription123", None)
                    
                    setattr(item, "filter_FilterDescription123", self)
                    

    @property
    def diagram_description_DiagramDescription127(self):
        return self.__diagram_description_DiagramDescription127

    @diagram_description_DiagramDescription127.setter
    def diagram_description_DiagramDescription127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription127", None)
        self.__diagram_description_DiagramDescription127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping128"):
                    opp_val = getattr(item, "NodeMapping128", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping128", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping128"):
                    opp_val = getattr(item, "NodeMapping128", None)
                    
                    setattr(item, "NodeMapping128", self)
                    

    @property
    def diagram_description_DiagramDescription176(self):
        return self.__diagram_description_DiagramDescription176

    @diagram_description_DiagramDescription176.setter
    def diagram_description_DiagramDescription176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription176", None)
        self.__diagram_description_DiagramDescription176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription177"):
                    opp_val = getattr(item, "tool_AbstractToolDescription177", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription177"):
                    opp_val = getattr(item, "tool_AbstractToolDescription177", None)
                    
                    setattr(item, "tool_AbstractToolDescription177", self)
                    

    @property
    def diagram_description_DiagramDescription168(self):
        return self.__diagram_description_DiagramDescription168

    @diagram_description_DiagramDescription168.setter
    def diagram_description_DiagramDescription168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription168", None)
        self.__diagram_description_DiagramDescription168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping169"):
                    opp_val = getattr(item, "ContainerMapping169", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping169"):
                    opp_val = getattr(item, "ContainerMapping169", None)
                    
                    setattr(item, "ContainerMapping169", self)
                    

    @property
    def diagram_description_DiagramDescription133(self):
        return self.__diagram_description_DiagramDescription133

    @diagram_description_DiagramDescription133.setter
    def diagram_description_DiagramDescription133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription133", None)
        self.__diagram_description_DiagramDescription133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "validation_ValidationSet"):
                opp_val = getattr(old_value, "validation_ValidationSet", None)
                if opp_val == self:
                    setattr(old_value, "validation_ValidationSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "validation_ValidationSet"):
                opp_val = getattr(value, "validation_ValidationSet", None)
                setattr(value, "validation_ValidationSet", self)

    @property
    def diagram_description_DiagramDescription139(self):
        return self.__diagram_description_DiagramDescription139

    @diagram_description_DiagramDescription139.setter
    def diagram_description_DiagramDescription139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription139", None)
        self.__diagram_description_DiagramDescription139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "concern_ConcernDescription140"):
                opp_val = getattr(old_value, "concern_ConcernDescription140", None)
                if opp_val == self:
                    setattr(old_value, "concern_ConcernDescription140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "concern_ConcernDescription140"):
                opp_val = getattr(value, "concern_ConcernDescription140", None)
                setattr(value, "concern_ConcernDescription140", self)

    @property
    def diagram_description_DiagramDescription163(self):
        return self.__diagram_description_DiagramDescription163

    @diagram_description_DiagramDescription163.setter
    def diagram_description_DiagramDescription163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription163", None)
        self.__diagram_description_DiagramDescription163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMapping164"):
                    opp_val = getattr(item, "EdgeMapping164", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping164"):
                    opp_val = getattr(item, "EdgeMapping164", None)
                    
                    setattr(item, "EdgeMapping164", self)
                    

    @property
    def diagram_description_DiagramDescription125(self):
        return self.__diagram_description_DiagramDescription125

    @diagram_description_DiagramDescription125.setter
    def diagram_description_DiagramDescription125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription125", None)
        self.__diagram_description_DiagramDescription125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMapping"):
                    opp_val = getattr(item, "EdgeMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping"):
                    opp_val = getattr(item, "EdgeMapping", None)
                    
                    setattr(item, "EdgeMapping", self)
                    

    @property
    def diagram_description_DiagramDescription137(self):
        return self.__diagram_description_DiagramDescription137

    @diagram_description_DiagramDescription137.setter
    def diagram_description_DiagramDescription137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription137", None)
        self.__diagram_description_DiagramDescription137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription"):
                    opp_val = getattr(item, "tool_AbstractToolDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription"):
                    opp_val = getattr(item, "tool_AbstractToolDescription", None)
                    
                    setattr(item, "tool_AbstractToolDescription", self)
                    

    @property
    def diagram_description_DiagramDescription135(self):
        return self.__diagram_description_DiagramDescription135

    @diagram_description_DiagramDescription135.setter
    def diagram_description_DiagramDescription135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription135", None)
        self.__diagram_description_DiagramDescription135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "concern_ConcernSet"):
                opp_val = getattr(old_value, "concern_ConcernSet", None)
                if opp_val == self:
                    setattr(old_value, "concern_ConcernSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "concern_ConcernSet"):
                opp_val = getattr(value, "concern_ConcernSet", None)
                setattr(value, "concern_ConcernSet", self)

    @property
    def diagram_description_DiagramDescription157(self):
        return self.__diagram_description_DiagramDescription157

    @diagram_description_DiagramDescription157.setter
    def diagram_description_DiagramDescription157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription157", None)
        self.__diagram_description_DiagramDescription157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription158"):
                    opp_val = getattr(item, "tool_AbstractToolDescription158", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription158"):
                    opp_val = getattr(item, "tool_AbstractToolDescription158", None)
                    
                    setattr(item, "tool_AbstractToolDescription158", self)
                    

    @property
    def diagram_description_DiagramDescription166(self):
        return self.__diagram_description_DiagramDescription166

    @diagram_description_DiagramDescription166.setter
    def diagram_description_DiagramDescription166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription166", None)
        self.__diagram_description_DiagramDescription166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMappingImport"):
                    opp_val = getattr(item, "EdgeMappingImport", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMappingImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMappingImport"):
                    opp_val = getattr(item, "EdgeMappingImport", None)
                    
                    setattr(item, "EdgeMappingImport", self)
                    

    @property
    def diagram_description_DiagramDescription151(self):
        return self.__diagram_description_DiagramDescription151

    @diagram_description_DiagramDescription151.setter
    def diagram_description_DiagramDescription151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription151", None)
        self.__diagram_description_DiagramDescription151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AdditionalLayer152"):
                    opp_val = getattr(item, "AdditionalLayer152", None)
                    
                    if opp_val == self:
                        setattr(item, "AdditionalLayer152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AdditionalLayer152"):
                    opp_val = getattr(item, "AdditionalLayer152", None)
                    
                    setattr(item, "AdditionalLayer152", self)
                    

    @property
    def diagram_description_DiagramDescription160(self):
        return self.__diagram_description_DiagramDescription160

    @diagram_description_DiagramDescription160.setter
    def diagram_description_DiagramDescription160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription160", None)
        self.__diagram_description_DiagramDescription160 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping161"):
                    opp_val = getattr(item, "NodeMapping161", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping161"):
                    opp_val = getattr(item, "NodeMapping161", None)
                    
                    setattr(item, "NodeMapping161", self)
                    

    @property
    def diagram_description_DiagramDescription148(self):
        return self.__diagram_description_DiagramDescription148

    @diagram_description_DiagramDescription148.setter
    def diagram_description_DiagramDescription148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription148", None)
        self.__diagram_description_DiagramDescription148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Layer149"):
                opp_val = getattr(old_value, "Layer149", None)
                if opp_val == self:
                    setattr(old_value, "Layer149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Layer149"):
                opp_val = getattr(value, "Layer149", None)
                setattr(value, "Layer149", self)

    @property
    def diagram_description_DiagramDescription174(self):
        return self.__diagram_description_DiagramDescription174

    @diagram_description_DiagramDescription174.setter
    def diagram_description_DiagramDescription174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription174", None)
        self.__diagram_description_DiagramDescription174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ToolSection"):
                opp_val = getattr(old_value, "tool_ToolSection", None)
                if opp_val == self:
                    setattr(old_value, "tool_ToolSection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ToolSection"):
                opp_val = getattr(value, "tool_ToolSection", None)
                setattr(value, "tool_ToolSection", self)

    @property
    def diagram_description_DiagramDescription142(self):
        return self.__diagram_description_DiagramDescription142

    @diagram_description_DiagramDescription142.setter
    def diagram_description_DiagramDescription142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription142", None)
        self.__diagram_description_DiagramDescription142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_RepresentationCreationDescription"):
                opp_val = getattr(old_value, "tool_RepresentationCreationDescription", None)
                if opp_val == self:
                    setattr(old_value, "tool_RepresentationCreationDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_RepresentationCreationDescription"):
                opp_val = getattr(value, "tool_RepresentationCreationDescription", None)
                setattr(value, "tool_RepresentationCreationDescription", self)

    @property
    def diagram_description_DiagramDescription146(self):
        return self.__diagram_description_DiagramDescription146

    @diagram_description_DiagramDescription146.setter
    def diagram_description_DiagramDescription146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription146", None)
        self.__diagram_description_DiagramDescription146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation"):
                opp_val = getattr(old_value, "tool_InitialOperation", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation"):
                opp_val = getattr(value, "tool_InitialOperation", None)
                setattr(value, "tool_InitialOperation", self)

    @property
    def diagram_description_DiagramDescription130(self):
        return self.__diagram_description_DiagramDescription130

    @diagram_description_DiagramDescription130.setter
    def diagram_description_DiagramDescription130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription130", None)
        self.__diagram_description_DiagramDescription130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping131"):
                    opp_val = getattr(item, "ContainerMapping131", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping131"):
                    opp_val = getattr(item, "ContainerMapping131", None)
                    
                    setattr(item, "ContainerMapping131", self)
                    

    @property
    def diagram_description_DiagramDescription144(self):
        return self.__diagram_description_DiagramDescription144

    @diagram_description_DiagramDescription144.setter
    def diagram_description_DiagramDescription144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription144", None)
        self.__diagram_description_DiagramDescription144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Layout"):
                opp_val = getattr(old_value, "Layout", None)
                if opp_val == self:
                    setattr(old_value, "Layout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Layout"):
                opp_val = getattr(value, "Layout", None)
                setattr(value, "Layout", self)

    @property
    def diagram_description_DiagramDescription154(self):
        return self.__diagram_description_DiagramDescription154

    @diagram_description_DiagramDescription154.setter
    def diagram_description_DiagramDescription154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription154", None)
        self.__diagram_description_DiagramDescription154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Layer155"):
                    opp_val = getattr(item, "Layer155", None)
                    
                    if opp_val == self:
                        setattr(item, "Layer155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Layer155"):
                    opp_val = getattr(item, "Layer155", None)
                    
                    setattr(item, "Layer155", self)
                    

    def createDiagram(self) -> str:
        # TODO: Implement createDiagram method
        pass

class diagram_EObject:

    pass
class tool_SelectModelElementVariable:

    pass
class BasicLabelStyle:

    pass
class CollapseFilter:

    pass
class diagram_IndirectlyCollapseFilter(CollapseFilter):

    pass
class diagram_DragAndDropTarget:

    def __init__(self):
        
    def getDragAndDropDescription(self) -> str:
        # TODO: Implement getDragAndDropDescription method
        pass

class style_StyleDescription:

    pass
class diagram_style_NodeStyleDescription(style_StyleDescription, style_BorderedStyleDescription, style_LabelStyleDescription, style_HideLabelCapabilityStyleDescription, style_TooltipStyleDescription):

    def __init__(self, sizeComputationExpression: str, labelPosition: str, resizeKind: str, forbiddenSides: str, style_StyleDescription: "diagram_ComputedStyleDescriptionRegistry"):
        self.sizeComputationExpression = sizeComputationExpression
        self.labelPosition = labelPosition
        self.resizeKind = resizeKind
        self.forbiddenSides = forbiddenSides
        
    @property
    def labelPosition(self) -> str:
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition

    @property
    def forbiddenSides(self) -> str:
        return self.__forbiddenSides

    @forbiddenSides.setter
    def forbiddenSides(self, forbiddenSides: str):
        self.__forbiddenSides = forbiddenSides

    @property
    def resizeKind(self) -> str:
        return self.__resizeKind

    @resizeKind.setter
    def resizeKind(self, resizeKind: str):
        self.__resizeKind = resizeKind

    @property
    def sizeComputationExpression(self) -> str:
        return self.__sizeComputationExpression

    @sizeComputationExpression.setter
    def sizeComputationExpression(self, sizeComputationExpression: str):
        self.__sizeComputationExpression = sizeComputationExpression

class diagram_ComputedStyleDescriptionRegistry:

    pass
class EdgeStyle:

    pass
class diagram_BracketEdgeStyle(EdgeStyle):

    pass
class diagram_VariableValue(ABC):

    pass
class diagram_EndLabelStyle(BasicLabelStyle):

    def __init__(self, diagram_EndLabelStyle: "diagram_EdgeStyle" = None):
        self.diagram_EndLabelStyle = diagram_EndLabelStyle
        
    @property
    def diagram_EndLabelStyle(self):
        return self.__diagram_EndLabelStyle

    @diagram_EndLabelStyle.setter
    def diagram_EndLabelStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EndLabelStyle__diagram_EndLabelStyle", None)
        self.__diagram_EndLabelStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_EdgeStyle113"):
                opp_val = getattr(old_value, "diagram_EdgeStyle113", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EdgeStyle113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EdgeStyle113"):
                opp_val = getattr(value, "diagram_EdgeStyle113", None)
                setattr(value, "diagram_EdgeStyle113", self)

    def setDescription(self, description: str):
        # TODO: Implement setDescription method
        pass

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

class diagram_CenterLabelStyle(BasicLabelStyle):

    def __init__(self, diagram_CenterLabelStyle: "diagram_EdgeStyle" = None):
        self.diagram_CenterLabelStyle = diagram_CenterLabelStyle
        
    @property
    def diagram_CenterLabelStyle(self):
        return self.__diagram_CenterLabelStyle

    @diagram_CenterLabelStyle.setter
    def diagram_CenterLabelStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_CenterLabelStyle__diagram_CenterLabelStyle", None)
        self.__diagram_CenterLabelStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_EdgeStyle111"):
                opp_val = getattr(old_value, "diagram_EdgeStyle111", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EdgeStyle111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EdgeStyle111"):
                opp_val = getattr(value, "diagram_EdgeStyle111", None)
                setattr(value, "diagram_EdgeStyle111", self)

    def setDescription(self, description: str):
        # TODO: Implement setDescription method
        pass

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

class diagram_BeginLabelStyle(BasicLabelStyle):

    def __init__(self, diagram_BeginLabelStyle: "diagram_EdgeStyle" = None):
        self.diagram_BeginLabelStyle = diagram_BeginLabelStyle
        
    @property
    def diagram_BeginLabelStyle(self):
        return self.__diagram_BeginLabelStyle

    @diagram_BeginLabelStyle.setter
    def diagram_BeginLabelStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_BeginLabelStyle__diagram_BeginLabelStyle", None)
        self.__diagram_BeginLabelStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_EdgeStyle109"):
                opp_val = getattr(old_value, "diagram_EdgeStyle109", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EdgeStyle109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EdgeStyle109"):
                opp_val = getattr(value, "diagram_EdgeStyle109", None)
                setattr(value, "diagram_EdgeStyle109", self)

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

    def setDescription(self, description: str):
        # TODO: Implement setDescription method
        pass

class Customizable:

    pass
class diagram_GaugeSection(Customizable):

    def __init__(self, foregroundColor: str, min: str, max: str, value: str, label: str, backgroundColor: str, diagram_GaugeSection: "diagram_GaugeCompositeStyle" = None):
        self.foregroundColor = foregroundColor
        self.min = min
        self.max = max
        self.value = value
        self.label = label
        self.backgroundColor = backgroundColor
        self.diagram_GaugeSection = diagram_GaugeSection
        
    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def foregroundColor(self) -> str:
        return self.__foregroundColor

    @foregroundColor.setter
    def foregroundColor(self, foregroundColor: str):
        self.__foregroundColor = foregroundColor

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def diagram_GaugeSection(self):
        return self.__diagram_GaugeSection

    @diagram_GaugeSection.setter
    def diagram_GaugeSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_GaugeSection__diagram_GaugeSection", None)
        self.__diagram_GaugeSection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_GaugeCompositeStyle"):
                opp_val = getattr(old_value, "diagram_GaugeCompositeStyle", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_GaugeCompositeStyle"):
                opp_val = getattr(value, "diagram_GaugeCompositeStyle", None)
                if opp_val is None:
                    setattr(value, "diagram_GaugeCompositeStyle", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ContainerStyle:

    pass
class diagram_ShapeContainerStyle(ContainerStyle):

    def __init__(self, shape: str, backgroundColor: str):
        self.shape = shape
        self.backgroundColor = backgroundColor
        
    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

class diagram_FlatContainerStyle(ContainerStyle):

    def __init__(self, backgroundStyle: str, backgroundColor: str, foregroundColor: str):
        self.backgroundStyle = backgroundStyle
        self.backgroundColor = backgroundColor
        self.foregroundColor = foregroundColor
        
    @property
    def backgroundStyle(self) -> str:
        return self.__backgroundStyle

    @backgroundStyle.setter
    def backgroundStyle(self, backgroundStyle: str):
        self.__backgroundStyle = backgroundStyle

    @property
    def foregroundColor(self) -> str:
        return self.__foregroundColor

    @foregroundColor.setter
    def foregroundColor(self, foregroundColor: str):
        self.__foregroundColor = foregroundColor

    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

class NodeStyle:

    pass
class diagram_Lozenge(NodeStyle):

    def __init__(self, height: str, color: str, width: str):
        self.height = height
        self.color = color
        self.width = width
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

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

class diagram_Square(NodeStyle):

    def __init__(self, width: str, height: str, color: str):
        self.width = width
        self.height = height
        self.color = color
        
    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

class diagram_Ellipse(NodeStyle):

    def __init__(self, horizontalDiameter: str, verticalDiameter: str, color: str):
        self.horizontalDiameter = horizontalDiameter
        self.verticalDiameter = verticalDiameter
        self.color = color
        
    @property
    def horizontalDiameter(self) -> str:
        return self.__horizontalDiameter

    @horizontalDiameter.setter
    def horizontalDiameter(self, horizontalDiameter: str):
        self.__horizontalDiameter = horizontalDiameter

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def verticalDiameter(self) -> str:
        return self.__verticalDiameter

    @verticalDiameter.setter
    def verticalDiameter(self, verticalDiameter: str):
        self.__verticalDiameter = verticalDiameter

class diagram_BundledImage(NodeStyle):

    def __init__(self, shape: str, color: str, providedShapeID: str):
        self.shape = shape
        self.color = color
        self.providedShapeID = providedShapeID
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def providedShapeID(self) -> str:
        return self.__providedShapeID

    @providedShapeID.setter
    def providedShapeID(self, providedShapeID: str):
        self.__providedShapeID = providedShapeID

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class diagram_WorkspaceImage(ContainerStyle, NodeStyle):

    def __init__(self, workspacePath: str):
        self.workspacePath = workspacePath
        
    @property
    def workspacePath(self) -> str:
        return self.__workspacePath

    @workspacePath.setter
    def workspacePath(self, workspacePath: str):
        self.__workspacePath = workspacePath

class diagram_GaugeCompositeStyle(NodeStyle):

    def __init__(self, alignment: str, diagram_GaugeCompositeStyle: set["diagram_GaugeSection"] = None):
        self.alignment = alignment
        self.diagram_GaugeCompositeStyle = diagram_GaugeCompositeStyle if diagram_GaugeCompositeStyle is not None else set()
        
    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def diagram_GaugeCompositeStyle(self):
        return self.__diagram_GaugeCompositeStyle

    @diagram_GaugeCompositeStyle.setter
    def diagram_GaugeCompositeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_GaugeCompositeStyle__diagram_GaugeCompositeStyle", None)
        self.__diagram_GaugeCompositeStyle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_GaugeSection"):
                    opp_val = getattr(item, "diagram_GaugeSection", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_GaugeSection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_GaugeSection"):
                    opp_val = getattr(item, "diagram_GaugeSection", None)
                    
                    setattr(item, "diagram_GaugeSection", self)
                    

class diagram_Note(NodeStyle):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class diagram_CustomStyle(NodeStyle):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class HideLabelCapabilityStyle:

    pass
class BorderedStyle:

    pass
class Style:

    pass
class diagram_BorderedStyle(Style):

    def __init__(self, borderSize: str, borderSizeComputationExpression: str, borderColor: str, borderLineStyle: str):
        self.borderSize = borderSize
        self.borderSizeComputationExpression = borderSizeComputationExpression
        self.borderColor = borderColor
        self.borderLineStyle = borderLineStyle
        
    @property
    def borderSizeComputationExpression(self) -> str:
        return self.__borderSizeComputationExpression

    @borderSizeComputationExpression.setter
    def borderSizeComputationExpression(self, borderSizeComputationExpression: str):
        self.__borderSizeComputationExpression = borderSizeComputationExpression

    @property
    def borderSize(self) -> str:
        return self.__borderSize

    @borderSize.setter
    def borderSize(self, borderSize: str):
        self.__borderSize = borderSize

    @property
    def borderLineStyle(self) -> str:
        return self.__borderLineStyle

    @borderLineStyle.setter
    def borderLineStyle(self, borderLineStyle: str):
        self.__borderLineStyle = borderLineStyle

    @property
    def borderColor(self) -> str:
        return self.__borderColor

    @borderColor.setter
    def borderColor(self, borderColor: str):
        self.__borderColor = borderColor

class LabelStyle:

    pass
class diagram_Dot(NodeStyle):

    def __init__(self, strokeSizeComputationExpression: str, backgroundColor: str):
        self.strokeSizeComputationExpression = strokeSizeComputationExpression
        self.backgroundColor = backgroundColor
        
    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

    @property
    def strokeSizeComputationExpression(self) -> str:
        return self.__strokeSizeComputationExpression

    @strokeSizeComputationExpression.setter
    def strokeSizeComputationExpression(self, strokeSizeComputationExpression: str):
        self.__strokeSizeComputationExpression = strokeSizeComputationExpression

class IEdgeMapping:

    pass
class diagram_EdgeTarget(ABC):

    pass
class diagram_EdgeStyle(Style):

    def __init__(self, lineStyle: str, sourceArrow: str, targetArrow: str, foldingStyle: str, size: str, centered: str, strokeColor: str, routingStyle: str, diagram_EdgeStyle: "diagram_DEdge" = None, diagram_EdgeStyle109: "diagram_BeginLabelStyle" = None, diagram_EdgeStyle111: "diagram_CenterLabelStyle" = None, diagram_EdgeStyle113: "diagram_EndLabelStyle" = None):
        self.lineStyle = lineStyle
        self.sourceArrow = sourceArrow
        self.targetArrow = targetArrow
        self.foldingStyle = foldingStyle
        self.size = size
        self.centered = centered
        self.strokeColor = strokeColor
        self.routingStyle = routingStyle
        self.diagram_EdgeStyle = diagram_EdgeStyle
        self.diagram_EdgeStyle109 = diagram_EdgeStyle109
        self.diagram_EdgeStyle111 = diagram_EdgeStyle111
        self.diagram_EdgeStyle113 = diagram_EdgeStyle113
        
    @property
    def targetArrow(self) -> str:
        return self.__targetArrow

    @targetArrow.setter
    def targetArrow(self, targetArrow: str):
        self.__targetArrow = targetArrow

    @property
    def sourceArrow(self) -> str:
        return self.__sourceArrow

    @sourceArrow.setter
    def sourceArrow(self, sourceArrow: str):
        self.__sourceArrow = sourceArrow

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def foldingStyle(self) -> str:
        return self.__foldingStyle

    @foldingStyle.setter
    def foldingStyle(self, foldingStyle: str):
        self.__foldingStyle = foldingStyle

    @property
    def lineStyle(self) -> str:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle

    @property
    def routingStyle(self) -> str:
        return self.__routingStyle

    @routingStyle.setter
    def routingStyle(self, routingStyle: str):
        self.__routingStyle = routingStyle

    @property
    def centered(self) -> str:
        return self.__centered

    @centered.setter
    def centered(self, centered: str):
        self.__centered = centered

    @property
    def strokeColor(self) -> str:
        return self.__strokeColor

    @strokeColor.setter
    def strokeColor(self, strokeColor: str):
        self.__strokeColor = strokeColor

    @property
    def diagram_EdgeStyle109(self):
        return self.__diagram_EdgeStyle109

    @diagram_EdgeStyle109.setter
    def diagram_EdgeStyle109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle109", None)
        self.__diagram_EdgeStyle109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_BeginLabelStyle"):
                opp_val = getattr(old_value, "diagram_BeginLabelStyle", None)
                if opp_val == self:
                    setattr(old_value, "diagram_BeginLabelStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_BeginLabelStyle"):
                opp_val = getattr(value, "diagram_BeginLabelStyle", None)
                setattr(value, "diagram_BeginLabelStyle", self)

    @property
    def diagram_EdgeStyle113(self):
        return self.__diagram_EdgeStyle113

    @diagram_EdgeStyle113.setter
    def diagram_EdgeStyle113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle113", None)
        self.__diagram_EdgeStyle113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_EndLabelStyle"):
                opp_val = getattr(old_value, "diagram_EndLabelStyle", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EndLabelStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EndLabelStyle"):
                opp_val = getattr(value, "diagram_EndLabelStyle", None)
                setattr(value, "diagram_EndLabelStyle", self)

    @property
    def diagram_EdgeStyle111(self):
        return self.__diagram_EdgeStyle111

    @diagram_EdgeStyle111.setter
    def diagram_EdgeStyle111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle111", None)
        self.__diagram_EdgeStyle111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_CenterLabelStyle"):
                opp_val = getattr(old_value, "diagram_CenterLabelStyle", None)
                if opp_val == self:
                    setattr(old_value, "diagram_CenterLabelStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_CenterLabelStyle"):
                opp_val = getattr(value, "diagram_CenterLabelStyle", None)
                setattr(value, "diagram_CenterLabelStyle", self)

    @property
    def diagram_EdgeStyle(self):
        return self.__diagram_EdgeStyle

    @diagram_EdgeStyle.setter
    def diagram_EdgeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle", None)
        self.__diagram_EdgeStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DEdge94"):
                opp_val = getattr(old_value, "diagram_DEdge94", None)
                if opp_val == self:
                    setattr(old_value, "diagram_DEdge94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DEdge94"):
                opp_val = getattr(value, "diagram_DEdge94", None)
                setattr(value, "diagram_DEdge94", self)

class DDiagramElementContainer:

    pass
class diagram_DNodeContainer(DDiagramElementContainer):

    def __init__(self, childrenPresentation: str, diagram_DNodeContainer: set["diagram_DDiagramElement"] = None):
        self.childrenPresentation = childrenPresentation
        self.diagram_DNodeContainer = diagram_DNodeContainer if diagram_DNodeContainer is not None else set()
        
    @property
    def childrenPresentation(self) -> str:
        return self.__childrenPresentation

    @childrenPresentation.setter
    def childrenPresentation(self, childrenPresentation: str):
        self.__childrenPresentation = childrenPresentation

    @property
    def diagram_DNodeContainer(self):
        return self.__diagram_DNodeContainer

    @diagram_DNodeContainer.setter
    def diagram_DNodeContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNodeContainer__diagram_DNodeContainer", None)
        self.__diagram_DNodeContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DDiagramElement78"):
                    opp_val = getattr(item, "diagram_DDiagramElement78", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElement78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElement78"):
                    opp_val = getattr(item, "diagram_DDiagramElement78", None)
                    
                    setattr(item, "diagram_DDiagramElement78", self)
                    

class ContainerMapping:

    pass
class diagram_DNodeList(DDiagramElementContainer):

    pass
class diagram_ContainerStyle(LabelStyle, BorderedStyle, HideLabelCapabilityStyle, Style):

    pass
class NodeMapping:

    pass
class diagram_Style:

    pass
class diagram_NodeStyle(LabelStyle, BorderedStyle, HideLabelCapabilityStyle, Style):

    def __init__(self, labelPosition: str, diagram_NodeStyle: "diagram_DNode" = None, diagram_NodeStyle83: "diagram_DNodeListElement" = None):
        self.labelPosition = labelPosition
        self.diagram_NodeStyle = diagram_NodeStyle
        self.diagram_NodeStyle83 = diagram_NodeStyle83
        
    @property
    def labelPosition(self) -> str:
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition

    @property
    def diagram_NodeStyle(self):
        return self.__diagram_NodeStyle

    @diagram_NodeStyle.setter
    def diagram_NodeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_NodeStyle__diagram_NodeStyle", None)
        self.__diagram_NodeStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DNode50"):
                opp_val = getattr(old_value, "diagram_DNode50", None)
                if opp_val == self:
                    setattr(old_value, "diagram_DNode50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DNode50"):
                opp_val = getattr(value, "diagram_DNode50", None)
                setattr(value, "diagram_DNode50", self)

    @property
    def diagram_NodeStyle83(self):
        return self.__diagram_NodeStyle83

    @diagram_NodeStyle83.setter
    def diagram_NodeStyle83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_NodeStyle__diagram_NodeStyle83", None)
        self.__diagram_NodeStyle83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DNodeListElement82"):
                opp_val = getattr(old_value, "diagram_DNodeListElement82", None)
                if opp_val == self:
                    setattr(old_value, "diagram_DNodeListElement82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DNodeListElement82"):
                opp_val = getattr(value, "diagram_DNodeListElement82", None)
                setattr(value, "diagram_DNodeListElement82", self)

class AbstractDNode:

    pass
class DDiagramElement:

    pass
class diagram_AbstractDNode(DDiagramElement):

    def __init__(self, arrangeConstraints: str, diagram_AbstractDNode: set["diagram_DNode"] = None):
        self.arrangeConstraints = arrangeConstraints
        self.diagram_AbstractDNode = diagram_AbstractDNode if diagram_AbstractDNode is not None else set()
        
    @property
    def arrangeConstraints(self) -> str:
        return self.__arrangeConstraints

    @arrangeConstraints.setter
    def arrangeConstraints(self, arrangeConstraints: str):
        self.__arrangeConstraints = arrangeConstraints

    @property
    def diagram_AbstractDNode(self):
        return self.__diagram_AbstractDNode

    @diagram_AbstractDNode.setter
    def diagram_AbstractDNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_AbstractDNode__diagram_AbstractDNode", None)
        self.__diagram_AbstractDNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DNode48"):
                    opp_val = getattr(item, "diagram_DNode48", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DNode48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DNode48"):
                    opp_val = getattr(item, "diagram_DNode48", None)
                    
                    setattr(item, "diagram_DNode48", self)
                    

class filter_CompositeFilterDescription:

    pass
class EdgeTarget:

    pass
class GraphicalFilter:

    pass
class diagram_HideLabelFilter(GraphicalFilter):

    pass
class diagram_CollapseFilter(GraphicalFilter):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        
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

class diagram_AbsoluteBoundsFilter(GraphicalFilter):

    def __init__(self, x: str, y: str, height: str, width: str):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

class diagram_AppliedCompositeFilters(GraphicalFilter):

    pass
class diagram_HideFilter(GraphicalFilter):

    pass
class diagram_GraphicalFilter(ABC):

    pass
class DiagramElementMapping:

    pass
class diagram_Decoration:

    pass
class diagram_FoldingFilter(GraphicalFilter):

    pass
class diagram_FoldingPointFilter(GraphicalFilter):

    pass
class DRepresentationElement:

    pass
class DSemanticDecorator:

    pass
class DDiagram:

    pass
class diagram_DSemanticDiagram(DSemanticDecorator, DDiagram):

    pass
class Layer:

    pass
class diagram_description_AdditionalLayer(Layer):

    def __init__(self, activeByDefault: bool, optional: bool, Layer155: "diagram_description_DiagramDescription", Layer: "diagram_DDiagram", Layer149: "diagram_description_DiagramDescription", Layer36: "diagram_DDiagramElement"):
        self.activeByDefault = activeByDefault
        self.optional = optional
        
    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def activeByDefault(self) -> bool:
        return self.__activeByDefault

    @activeByDefault.setter
    def activeByDefault(self, activeByDefault: bool):
        self.__activeByDefault = activeByDefault

class diagram_FilterVariableHistory:

    pass
class validation_ValidationRule:

    pass
class AdditionalLayer:

    pass
class filter_FilterDescription:

    pass
class concern_ConcernDescription:

    pass
class tool_BehaviorTool:

    pass
class diagram_DNodeListElement(AbstractDNode):

    pass
class diagram_DEdge(EdgeTarget, DDiagramElement):

    def __init__(self, isMockEdge: bool, size: str, routingStyle: str, isFold: bool, arrangeConstraints: str, beginLabel: str, endLabel: str, diagram_DEdge: "diagram_DDiagram" = None, diagram_DEdge101: "diagram_Style" = None, diagram_DEdge94: "diagram_EdgeStyle" = None, outgoingEdges: "diagram_EdgeTarget" = None, incomingEdges: "diagram_EdgeTarget" = None, diagram_DEdge99: "IEdgeMapping" = None, diagram_DEdge104: set["diagram_EdgeTarget"] = None, DEdge: "diagram_EdgeTarget" = None, DEdge107: "diagram_EdgeTarget" = None):
        self.isMockEdge = isMockEdge
        self.size = size
        self.routingStyle = routingStyle
        self.isFold = isFold
        self.arrangeConstraints = arrangeConstraints
        self.beginLabel = beginLabel
        self.endLabel = endLabel
        self.diagram_DEdge = diagram_DEdge
        self.diagram_DEdge101 = diagram_DEdge101
        self.diagram_DEdge94 = diagram_DEdge94
        self.outgoingEdges = outgoingEdges
        self.incomingEdges = incomingEdges
        self.diagram_DEdge99 = diagram_DEdge99
        self.diagram_DEdge104 = diagram_DEdge104 if diagram_DEdge104 is not None else set()
        self.DEdge = DEdge
        self.DEdge107 = DEdge107
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def beginLabel(self) -> str:
        return self.__beginLabel

    @beginLabel.setter
    def beginLabel(self, beginLabel: str):
        self.__beginLabel = beginLabel

    @property
    def routingStyle(self) -> str:
        return self.__routingStyle

    @routingStyle.setter
    def routingStyle(self, routingStyle: str):
        self.__routingStyle = routingStyle

    @property
    def isMockEdge(self) -> bool:
        return self.__isMockEdge

    @isMockEdge.setter
    def isMockEdge(self, isMockEdge: bool):
        self.__isMockEdge = isMockEdge

    @property
    def isFold(self) -> bool:
        return self.__isFold

    @isFold.setter
    def isFold(self, isFold: bool):
        self.__isFold = isFold

    @property
    def endLabel(self) -> str:
        return self.__endLabel

    @endLabel.setter
    def endLabel(self, endLabel: str):
        self.__endLabel = endLabel

    @property
    def arrangeConstraints(self) -> str:
        return self.__arrangeConstraints

    @arrangeConstraints.setter
    def arrangeConstraints(self, arrangeConstraints: str):
        self.__arrangeConstraints = arrangeConstraints

    @property
    def diagram_DEdge99(self):
        return self.__diagram_DEdge99

    @diagram_DEdge99.setter
    def diagram_DEdge99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__diagram_DEdge99", None)
        self.__diagram_DEdge99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IEdgeMapping"):
                opp_val = getattr(old_value, "IEdgeMapping", None)
                if opp_val == self:
                    setattr(old_value, "IEdgeMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IEdgeMapping"):
                opp_val = getattr(value, "IEdgeMapping", None)
                setattr(value, "IEdgeMapping", self)

    @property
    def DEdge107(self):
        return self.__DEdge107

    @DEdge107.setter
    def DEdge107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__DEdge107", None)
        self.__DEdge107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetNode"):
                opp_val = getattr(old_value, "targetNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetNode"):
                opp_val = getattr(value, "targetNode", None)
                if opp_val is None:
                    setattr(value, "targetNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DEdge94(self):
        return self.__diagram_DEdge94

    @diagram_DEdge94.setter
    def diagram_DEdge94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__diagram_DEdge94", None)
        self.__diagram_DEdge94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_EdgeStyle"):
                opp_val = getattr(old_value, "diagram_EdgeStyle", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EdgeStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EdgeStyle"):
                opp_val = getattr(value, "diagram_EdgeStyle", None)
                setattr(value, "diagram_EdgeStyle", self)

    @property
    def diagram_DEdge(self):
        return self.__diagram_DEdge

    @diagram_DEdge.setter
    def diagram_DEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__diagram_DEdge", None)
        self.__diagram_DEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagram7"):
                opp_val = getattr(old_value, "diagram_DDiagram7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagram7"):
                opp_val = getattr(value, "diagram_DDiagram7", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagram7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingEdges(self):
        return self.__incomingEdges

    @incomingEdges.setter
    def incomingEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__incomingEdges", None)
        self.__incomingEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeTarget97"):
                opp_val = getattr(old_value, "EdgeTarget97", None)
                if opp_val == self:
                    setattr(old_value, "EdgeTarget97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeTarget97"):
                opp_val = getattr(value, "EdgeTarget97", None)
                setattr(value, "EdgeTarget97", self)

    @property
    def diagram_DEdge101(self):
        return self.__diagram_DEdge101

    @diagram_DEdge101.setter
    def diagram_DEdge101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__diagram_DEdge101", None)
        self.__diagram_DEdge101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_Style102"):
                opp_val = getattr(old_value, "diagram_Style102", None)
                if opp_val == self:
                    setattr(old_value, "diagram_Style102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_Style102"):
                opp_val = getattr(value, "diagram_Style102", None)
                setattr(value, "diagram_Style102", self)

    @property
    def DEdge(self):
        return self.__DEdge

    @DEdge.setter
    def DEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__DEdge", None)
        self.__DEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceNode"):
                opp_val = getattr(old_value, "sourceNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceNode"):
                opp_val = getattr(value, "sourceNode", None)
                if opp_val is None:
                    setattr(value, "sourceNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DEdge104(self):
        return self.__diagram_DEdge104

    @diagram_DEdge104.setter
    def diagram_DEdge104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__diagram_DEdge104", None)
        self.__diagram_DEdge104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_EdgeTarget"):
                    opp_val = getattr(item, "diagram_EdgeTarget", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_EdgeTarget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_EdgeTarget"):
                    opp_val = getattr(item, "diagram_EdgeTarget", None)
                    
                    setattr(item, "diagram_EdgeTarget", self)
                    

    @property
    def outgoingEdges(self):
        return self.__outgoingEdges

    @outgoingEdges.setter
    def outgoingEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__outgoingEdges", None)
        self.__outgoingEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeTarget"):
                opp_val = getattr(old_value, "EdgeTarget", None)
                if opp_val == self:
                    setattr(old_value, "EdgeTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeTarget"):
                opp_val = getattr(value, "EdgeTarget", None)
                setattr(value, "EdgeTarget", self)

    def isRootFolding(self) -> bool:
        # TODO: Implement isRootFolding method
        pass

class DiagramDescription:

    pass
class diagram_DDiagramElement(DRepresentationElement):

    def __init__(self, visible: bool, tooltipText: str, diagram_DDiagramElement: "diagram_DDiagram" = None, diagram_DDiagramElement3: "diagram_DDiagram" = None, diagram_DDiagramElement33: "diagram_DDiagram" = None, diagram_DDiagramElement35: set["Layer"] = None, diagram_DDiagramElement38: set["diagram_Decoration"] = None, diagram_DDiagramElement40: set["diagram_Decoration"] = None, diagram_DDiagramElement43: "DiagramElementMapping" = None, diagram_DDiagramElement45: set["diagram_GraphicalFilter"] = None, diagram_DDiagramElement66: "diagram_DDiagramElementContainer" = None, diagram_DDiagramElement78: "diagram_DNodeContainer" = None):
        self.visible = visible
        self.tooltipText = tooltipText
        self.diagram_DDiagramElement = diagram_DDiagramElement
        self.diagram_DDiagramElement3 = diagram_DDiagramElement3
        self.diagram_DDiagramElement33 = diagram_DDiagramElement33
        self.diagram_DDiagramElement35 = diagram_DDiagramElement35 if diagram_DDiagramElement35 is not None else set()
        self.diagram_DDiagramElement38 = diagram_DDiagramElement38 if diagram_DDiagramElement38 is not None else set()
        self.diagram_DDiagramElement40 = diagram_DDiagramElement40 if diagram_DDiagramElement40 is not None else set()
        self.diagram_DDiagramElement43 = diagram_DDiagramElement43
        self.diagram_DDiagramElement45 = diagram_DDiagramElement45 if diagram_DDiagramElement45 is not None else set()
        self.diagram_DDiagramElement66 = diagram_DDiagramElement66
        self.diagram_DDiagramElement78 = diagram_DDiagramElement78
        
    @property
    def tooltipText(self) -> str:
        return self.__tooltipText

    @tooltipText.setter
    def tooltipText(self, tooltipText: str):
        self.__tooltipText = tooltipText

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def diagram_DDiagramElement33(self):
        return self.__diagram_DDiagramElement33

    @diagram_DDiagramElement33.setter
    def diagram_DDiagramElement33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement33", None)
        self.__diagram_DDiagramElement33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagram32"):
                opp_val = getattr(old_value, "diagram_DDiagram32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagram32"):
                opp_val = getattr(value, "diagram_DDiagram32", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagram32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DDiagramElement66(self):
        return self.__diagram_DDiagramElement66

    @diagram_DDiagramElement66.setter
    def diagram_DDiagramElement66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement66", None)
        self.__diagram_DDiagramElement66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagramElementContainer65"):
                opp_val = getattr(old_value, "diagram_DDiagramElementContainer65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagramElementContainer65"):
                opp_val = getattr(value, "diagram_DDiagramElementContainer65", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagramElementContainer65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DDiagramElement3(self):
        return self.__diagram_DDiagramElement3

    @diagram_DDiagramElement3.setter
    def diagram_DDiagramElement3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement3", None)
        self.__diagram_DDiagramElement3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagram2"):
                opp_val = getattr(old_value, "diagram_DDiagram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagram2"):
                opp_val = getattr(value, "diagram_DDiagram2", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DDiagramElement45(self):
        return self.__diagram_DDiagramElement45

    @diagram_DDiagramElement45.setter
    def diagram_DDiagramElement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement45", None)
        self.__diagram_DDiagramElement45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_GraphicalFilter"):
                    opp_val = getattr(item, "diagram_GraphicalFilter", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_GraphicalFilter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_GraphicalFilter"):
                    opp_val = getattr(item, "diagram_GraphicalFilter", None)
                    
                    setattr(item, "diagram_GraphicalFilter", self)
                    

    @property
    def diagram_DDiagramElement78(self):
        return self.__diagram_DDiagramElement78

    @diagram_DDiagramElement78.setter
    def diagram_DDiagramElement78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement78", None)
        self.__diagram_DDiagramElement78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DNodeContainer"):
                opp_val = getattr(old_value, "diagram_DNodeContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DNodeContainer"):
                opp_val = getattr(value, "diagram_DNodeContainer", None)
                if opp_val is None:
                    setattr(value, "diagram_DNodeContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DDiagramElement35(self):
        return self.__diagram_DDiagramElement35

    @diagram_DDiagramElement35.setter
    def diagram_DDiagramElement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement35", None)
        self.__diagram_DDiagramElement35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Layer36"):
                    opp_val = getattr(item, "Layer36", None)
                    
                    if opp_val == self:
                        setattr(item, "Layer36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Layer36"):
                    opp_val = getattr(item, "Layer36", None)
                    
                    setattr(item, "Layer36", self)
                    

    @property
    def diagram_DDiagramElement43(self):
        return self.__diagram_DDiagramElement43

    @diagram_DDiagramElement43.setter
    def diagram_DDiagramElement43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement43", None)
        self.__diagram_DDiagramElement43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramElementMapping"):
                opp_val = getattr(old_value, "DiagramElementMapping", None)
                if opp_val == self:
                    setattr(old_value, "DiagramElementMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramElementMapping"):
                opp_val = getattr(value, "DiagramElementMapping", None)
                setattr(value, "DiagramElementMapping", self)

    @property
    def diagram_DDiagramElement(self):
        return self.__diagram_DDiagramElement

    @diagram_DDiagramElement.setter
    def diagram_DDiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement", None)
        self.__diagram_DDiagramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagram"):
                opp_val = getattr(old_value, "diagram_DDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagram"):
                opp_val = getattr(value, "diagram_DDiagram", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DDiagramElement40(self):
        return self.__diagram_DDiagramElement40

    @diagram_DDiagramElement40.setter
    def diagram_DDiagramElement40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement40", None)
        self.__diagram_DDiagramElement40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_Decoration41"):
                    opp_val = getattr(item, "diagram_Decoration41", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_Decoration41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_Decoration41"):
                    opp_val = getattr(item, "diagram_Decoration41", None)
                    
                    setattr(item, "diagram_Decoration41", self)
                    

    @property
    def diagram_DDiagramElement38(self):
        return self.__diagram_DDiagramElement38

    @diagram_DDiagramElement38.setter
    def diagram_DDiagramElement38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement38", None)
        self.__diagram_DDiagramElement38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_Decoration"):
                    opp_val = getattr(item, "diagram_Decoration", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_Decoration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_Decoration"):
                    opp_val = getattr(item, "diagram_Decoration", None)
                    
                    setattr(item, "diagram_Decoration", self)
                    

    def getParentDiagram(self) -> DDiagram:
        # TODO: Implement getParentDiagram method
        pass

class DragAndDropTarget:

    pass
class diagram_DDiagramElementContainer(AbstractDNode, EdgeTarget, DragAndDropTarget):

    def __init__(self, width: str, height: str, diagram_DDiagramElementContainer: "diagram_DDiagram" = None, diagram_DDiagramElementContainer68: "diagram_ContainerStyle" = None, diagram_DDiagramElementContainer70: "diagram_Style" = None, diagram_DDiagramElementContainer59: set["diagram_DNode"] = None, diagram_DDiagramElementContainer63: "diagram_DDiagramElementContainer" = None, diagram_DDiagramElementContainer61: set["diagram_DDiagramElementContainer"] = None, diagram_DDiagramElementContainer65: set["diagram_DDiagramElement"] = None, diagram_DDiagramElementContainer73: "ContainerMapping" = None, diagram_DDiagramElementContainer75: set["ContainerMapping"] = None):
        self.width = width
        self.height = height
        self.diagram_DDiagramElementContainer = diagram_DDiagramElementContainer
        self.diagram_DDiagramElementContainer68 = diagram_DDiagramElementContainer68
        self.diagram_DDiagramElementContainer70 = diagram_DDiagramElementContainer70
        self.diagram_DDiagramElementContainer59 = diagram_DDiagramElementContainer59 if diagram_DDiagramElementContainer59 is not None else set()
        self.diagram_DDiagramElementContainer63 = diagram_DDiagramElementContainer63
        self.diagram_DDiagramElementContainer61 = diagram_DDiagramElementContainer61 if diagram_DDiagramElementContainer61 is not None else set()
        self.diagram_DDiagramElementContainer65 = diagram_DDiagramElementContainer65 if diagram_DDiagramElementContainer65 is not None else set()
        self.diagram_DDiagramElementContainer73 = diagram_DDiagramElementContainer73
        self.diagram_DDiagramElementContainer75 = diagram_DDiagramElementContainer75 if diagram_DDiagramElementContainer75 is not None else set()
        
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
    def diagram_DDiagramElementContainer65(self):
        return self.__diagram_DDiagramElementContainer65

    @diagram_DDiagramElementContainer65.setter
    def diagram_DDiagramElementContainer65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer65", None)
        self.__diagram_DDiagramElementContainer65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DDiagramElement66"):
                    opp_val = getattr(item, "diagram_DDiagramElement66", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElement66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElement66"):
                    opp_val = getattr(item, "diagram_DDiagramElement66", None)
                    
                    setattr(item, "diagram_DDiagramElement66", self)
                    

    @property
    def diagram_DDiagramElementContainer75(self):
        return self.__diagram_DDiagramElementContainer75

    @diagram_DDiagramElementContainer75.setter
    def diagram_DDiagramElementContainer75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer75", None)
        self.__diagram_DDiagramElementContainer75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping76"):
                    opp_val = getattr(item, "ContainerMapping76", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping76"):
                    opp_val = getattr(item, "ContainerMapping76", None)
                    
                    setattr(item, "ContainerMapping76", self)
                    

    @property
    def diagram_DDiagramElementContainer(self):
        return self.__diagram_DDiagramElementContainer

    @diagram_DDiagramElementContainer.setter
    def diagram_DDiagramElementContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer", None)
        self.__diagram_DDiagramElementContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagram13"):
                opp_val = getattr(old_value, "diagram_DDiagram13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagram13"):
                opp_val = getattr(value, "diagram_DDiagram13", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagram13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DDiagramElementContainer59(self):
        return self.__diagram_DDiagramElementContainer59

    @diagram_DDiagramElementContainer59.setter
    def diagram_DDiagramElementContainer59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer59", None)
        self.__diagram_DDiagramElementContainer59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DNode60"):
                    opp_val = getattr(item, "diagram_DNode60", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DNode60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DNode60"):
                    opp_val = getattr(item, "diagram_DNode60", None)
                    
                    setattr(item, "diagram_DNode60", self)
                    

    @property
    def diagram_DDiagramElementContainer73(self):
        return self.__diagram_DDiagramElementContainer73

    @diagram_DDiagramElementContainer73.setter
    def diagram_DDiagramElementContainer73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer73", None)
        self.__diagram_DDiagramElementContainer73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContainerMapping"):
                opp_val = getattr(old_value, "ContainerMapping", None)
                if opp_val == self:
                    setattr(old_value, "ContainerMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContainerMapping"):
                opp_val = getattr(value, "ContainerMapping", None)
                setattr(value, "ContainerMapping", self)

    @property
    def diagram_DDiagramElementContainer70(self):
        return self.__diagram_DDiagramElementContainer70

    @diagram_DDiagramElementContainer70.setter
    def diagram_DDiagramElementContainer70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer70", None)
        self.__diagram_DDiagramElementContainer70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_Style71"):
                opp_val = getattr(old_value, "diagram_Style71", None)
                if opp_val == self:
                    setattr(old_value, "diagram_Style71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_Style71"):
                opp_val = getattr(value, "diagram_Style71", None)
                setattr(value, "diagram_Style71", self)

    @property
    def diagram_DDiagramElementContainer63(self):
        return self.__diagram_DDiagramElementContainer63

    @diagram_DDiagramElementContainer63.setter
    def diagram_DDiagramElementContainer63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer63", None)
        self.__diagram_DDiagramElementContainer63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagramElementContainer61"):
                opp_val = getattr(old_value, "diagram_DDiagramElementContainer61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagramElementContainer61"):
                opp_val = getattr(value, "diagram_DDiagramElementContainer61", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagramElementContainer61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DDiagramElementContainer61(self):
        return self.__diagram_DDiagramElementContainer61

    @diagram_DDiagramElementContainer61.setter
    def diagram_DDiagramElementContainer61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer61", None)
        self.__diagram_DDiagramElementContainer61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DDiagramElementContainer63"):
                    opp_val = getattr(item, "diagram_DDiagramElementContainer63", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElementContainer63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElementContainer63"):
                    opp_val = getattr(item, "diagram_DDiagramElementContainer63", None)
                    
                    setattr(item, "diagram_DDiagramElementContainer63", self)
                    

    @property
    def diagram_DDiagramElementContainer68(self):
        return self.__diagram_DDiagramElementContainer68

    @diagram_DDiagramElementContainer68.setter
    def diagram_DDiagramElementContainer68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer68", None)
        self.__diagram_DDiagramElementContainer68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_ContainerStyle"):
                opp_val = getattr(old_value, "diagram_ContainerStyle", None)
                if opp_val == self:
                    setattr(old_value, "diagram_ContainerStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_ContainerStyle"):
                opp_val = getattr(value, "diagram_ContainerStyle", None)
                setattr(value, "diagram_ContainerStyle", self)

    def getContainersFromMapping(self, mapping: str) -> str:
        # TODO: Implement getContainersFromMapping method
        pass

    def getNodesFromMapping(self, mapping: str) -> str:
        # TODO: Implement getNodesFromMapping method
        pass

class diagram_DNode(EdgeTarget, AbstractDNode, DragAndDropTarget):

    def __init__(self, width: str, height: str, labelPosition: str, resizeKind: str, diagram_DNode: "diagram_DDiagram" = None, diagram_DNode48: "diagram_AbstractDNode" = None, diagram_DNode50: "diagram_NodeStyle" = None, diagram_DNode52: "diagram_Style" = None, diagram_DNode54: "NodeMapping" = None, diagram_DNode56: set["NodeMapping"] = None, diagram_DNode60: "diagram_DDiagramElementContainer" = None):
        self.width = width
        self.height = height
        self.labelPosition = labelPosition
        self.resizeKind = resizeKind
        self.diagram_DNode = diagram_DNode
        self.diagram_DNode48 = diagram_DNode48
        self.diagram_DNode50 = diagram_DNode50
        self.diagram_DNode52 = diagram_DNode52
        self.diagram_DNode54 = diagram_DNode54
        self.diagram_DNode56 = diagram_DNode56 if diagram_DNode56 is not None else set()
        self.diagram_DNode60 = diagram_DNode60
        
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
    def resizeKind(self) -> str:
        return self.__resizeKind

    @resizeKind.setter
    def resizeKind(self, resizeKind: str):
        self.__resizeKind = resizeKind

    @property
    def labelPosition(self) -> str:
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition

    @property
    def diagram_DNode60(self):
        return self.__diagram_DNode60

    @diagram_DNode60.setter
    def diagram_DNode60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode60", None)
        self.__diagram_DNode60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagramElementContainer59"):
                opp_val = getattr(old_value, "diagram_DDiagramElementContainer59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagramElementContainer59"):
                opp_val = getattr(value, "diagram_DDiagramElementContainer59", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagramElementContainer59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DNode56(self):
        return self.__diagram_DNode56

    @diagram_DNode56.setter
    def diagram_DNode56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode56", None)
        self.__diagram_DNode56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping57"):
                    opp_val = getattr(item, "NodeMapping57", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping57"):
                    opp_val = getattr(item, "NodeMapping57", None)
                    
                    setattr(item, "NodeMapping57", self)
                    

    @property
    def diagram_DNode54(self):
        return self.__diagram_DNode54

    @diagram_DNode54.setter
    def diagram_DNode54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode54", None)
        self.__diagram_DNode54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeMapping"):
                opp_val = getattr(old_value, "NodeMapping", None)
                if opp_val == self:
                    setattr(old_value, "NodeMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeMapping"):
                opp_val = getattr(value, "NodeMapping", None)
                setattr(value, "NodeMapping", self)

    @property
    def diagram_DNode52(self):
        return self.__diagram_DNode52

    @diagram_DNode52.setter
    def diagram_DNode52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode52", None)
        self.__diagram_DNode52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_Style"):
                opp_val = getattr(old_value, "diagram_Style", None)
                if opp_val == self:
                    setattr(old_value, "diagram_Style", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_Style"):
                opp_val = getattr(value, "diagram_Style", None)
                setattr(value, "diagram_Style", self)

    @property
    def diagram_DNode48(self):
        return self.__diagram_DNode48

    @diagram_DNode48.setter
    def diagram_DNode48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode48", None)
        self.__diagram_DNode48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_AbstractDNode"):
                opp_val = getattr(old_value, "diagram_AbstractDNode", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_AbstractDNode"):
                opp_val = getattr(value, "diagram_AbstractDNode", None)
                if opp_val is None:
                    setattr(value, "diagram_AbstractDNode", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DNode(self):
        return self.__diagram_DNode

    @diagram_DNode.setter
    def diagram_DNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode", None)
        self.__diagram_DNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagram9"):
                opp_val = getattr(old_value, "diagram_DDiagram9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagram9"):
                opp_val = getattr(value, "diagram_DDiagram9", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagram9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DNode50(self):
        return self.__diagram_DNode50

    @diagram_DNode50.setter
    def diagram_DNode50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode50", None)
        self.__diagram_DNode50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_NodeStyle"):
                opp_val = getattr(old_value, "diagram_NodeStyle", None)
                if opp_val == self:
                    setattr(old_value, "diagram_NodeStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_NodeStyle"):
                opp_val = getattr(value, "diagram_NodeStyle", None)
                setattr(value, "diagram_NodeStyle", self)

class description_DocumentedElement:

    pass
class diagram_tool_ToolSection(description_DocumentedElement, description_IdentifiedElement):

    def __init__(self, icon: str, diagram_tool_ToolSection331: set["tool_PopupMenu"] = None, diagram_tool_ToolSection333: set["tool_ToolEntry"] = None, diagram_tool_ToolSection336: set["tool_ToolGroupExtension"] = None, diagram_tool_ToolSection: set["tool_ToolEntry"] = None, diagram_tool_ToolSection328: set["tool_ToolSection"] = None):
        self.icon = icon
        self.diagram_tool_ToolSection331 = diagram_tool_ToolSection331 if diagram_tool_ToolSection331 is not None else set()
        self.diagram_tool_ToolSection333 = diagram_tool_ToolSection333 if diagram_tool_ToolSection333 is not None else set()
        self.diagram_tool_ToolSection336 = diagram_tool_ToolSection336 if diagram_tool_ToolSection336 is not None else set()
        self.diagram_tool_ToolSection = diagram_tool_ToolSection if diagram_tool_ToolSection is not None else set()
        self.diagram_tool_ToolSection328 = diagram_tool_ToolSection328 if diagram_tool_ToolSection328 is not None else set()
        
    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def diagram_tool_ToolSection336(self):
        return self.__diagram_tool_ToolSection336

    @diagram_tool_ToolSection336.setter
    def diagram_tool_ToolSection336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection336", None)
        self.__diagram_tool_ToolSection336 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolGroupExtension"):
                    opp_val = getattr(item, "tool_ToolGroupExtension", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolGroupExtension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolGroupExtension"):
                    opp_val = getattr(item, "tool_ToolGroupExtension", None)
                    
                    setattr(item, "tool_ToolGroupExtension", self)
                    

    @property
    def diagram_tool_ToolSection(self):
        return self.__diagram_tool_ToolSection

    @diagram_tool_ToolSection.setter
    def diagram_tool_ToolSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection", None)
        self.__diagram_tool_ToolSection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolEntry"):
                    opp_val = getattr(item, "tool_ToolEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolEntry"):
                    opp_val = getattr(item, "tool_ToolEntry", None)
                    
                    setattr(item, "tool_ToolEntry", self)
                    

    @property
    def diagram_tool_ToolSection331(self):
        return self.__diagram_tool_ToolSection331

    @diagram_tool_ToolSection331.setter
    def diagram_tool_ToolSection331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection331", None)
        self.__diagram_tool_ToolSection331 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_PopupMenu"):
                    opp_val = getattr(item, "tool_PopupMenu", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_PopupMenu", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_PopupMenu"):
                    opp_val = getattr(item, "tool_PopupMenu", None)
                    
                    setattr(item, "tool_PopupMenu", self)
                    

    @property
    def diagram_tool_ToolSection328(self):
        return self.__diagram_tool_ToolSection328

    @diagram_tool_ToolSection328.setter
    def diagram_tool_ToolSection328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection328", None)
        self.__diagram_tool_ToolSection328 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolSection329"):
                    opp_val = getattr(item, "tool_ToolSection329", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolSection329", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolSection329"):
                    opp_val = getattr(item, "tool_ToolSection329", None)
                    
                    setattr(item, "tool_ToolSection329", self)
                    

    @property
    def diagram_tool_ToolSection333(self):
        return self.__diagram_tool_ToolSection333

    @diagram_tool_ToolSection333.setter
    def diagram_tool_ToolSection333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection333", None)
        self.__diagram_tool_ToolSection333 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolEntry334"):
                    opp_val = getattr(item, "tool_ToolEntry334", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolEntry334", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolEntry334"):
                    opp_val = getattr(item, "tool_ToolEntry334", None)
                    
                    setattr(item, "tool_ToolEntry334", self)
                    

class diagram_description_EdgeMapping(description_DocumentedElement, description_DiagramElementMapping, description_IEdgeMapping):

    def __init__(self, targetFinderExpression: str, targetExpression: str, domainClass: str, useDomainElement: bool, sourceFinderExpression: str, pathExpression: str, diagram_description_EdgeMapping: set["DiagramElementMapping"] = None, diagram_description_EdgeMapping228: set["DiagramElementMapping"] = None, diagram_description_EdgeMapping233: set["ConditionalEdgeStyleDescription"] = None, diagram_description_EdgeMapping231: "style_EdgeStyleDescription" = None, diagram_description_EdgeMapping235: set["tool_ReconnectEdgeDescription"] = None, diagram_description_EdgeMapping237: set["AbstractNodeMapping"] = None):
        self.targetFinderExpression = targetFinderExpression
        self.targetExpression = targetExpression
        self.domainClass = domainClass
        self.useDomainElement = useDomainElement
        self.sourceFinderExpression = sourceFinderExpression
        self.pathExpression = pathExpression
        self.diagram_description_EdgeMapping = diagram_description_EdgeMapping if diagram_description_EdgeMapping is not None else set()
        self.diagram_description_EdgeMapping228 = diagram_description_EdgeMapping228 if diagram_description_EdgeMapping228 is not None else set()
        self.diagram_description_EdgeMapping233 = diagram_description_EdgeMapping233 if diagram_description_EdgeMapping233 is not None else set()
        self.diagram_description_EdgeMapping231 = diagram_description_EdgeMapping231
        self.diagram_description_EdgeMapping235 = diagram_description_EdgeMapping235 if diagram_description_EdgeMapping235 is not None else set()
        self.diagram_description_EdgeMapping237 = diagram_description_EdgeMapping237 if diagram_description_EdgeMapping237 is not None else set()
        
    @property
    def pathExpression(self) -> str:
        return self.__pathExpression

    @pathExpression.setter
    def pathExpression(self, pathExpression: str):
        self.__pathExpression = pathExpression

    @property
    def sourceFinderExpression(self) -> str:
        return self.__sourceFinderExpression

    @sourceFinderExpression.setter
    def sourceFinderExpression(self, sourceFinderExpression: str):
        self.__sourceFinderExpression = sourceFinderExpression

    @property
    def useDomainElement(self) -> bool:
        return self.__useDomainElement

    @useDomainElement.setter
    def useDomainElement(self, useDomainElement: bool):
        self.__useDomainElement = useDomainElement

    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def targetFinderExpression(self) -> str:
        return self.__targetFinderExpression

    @targetFinderExpression.setter
    def targetFinderExpression(self, targetFinderExpression: str):
        self.__targetFinderExpression = targetFinderExpression

    @property
    def targetExpression(self) -> str:
        return self.__targetExpression

    @targetExpression.setter
    def targetExpression(self, targetExpression: str):
        self.__targetExpression = targetExpression

    @property
    def diagram_description_EdgeMapping237(self):
        return self.__diagram_description_EdgeMapping237

    @diagram_description_EdgeMapping237.setter
    def diagram_description_EdgeMapping237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping237", None)
        self.__diagram_description_EdgeMapping237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractNodeMapping"):
                    opp_val = getattr(item, "AbstractNodeMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractNodeMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractNodeMapping"):
                    opp_val = getattr(item, "AbstractNodeMapping", None)
                    
                    setattr(item, "AbstractNodeMapping", self)
                    

    @property
    def diagram_description_EdgeMapping235(self):
        return self.__diagram_description_EdgeMapping235

    @diagram_description_EdgeMapping235.setter
    def diagram_description_EdgeMapping235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping235", None)
        self.__diagram_description_EdgeMapping235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ReconnectEdgeDescription"):
                    opp_val = getattr(item, "tool_ReconnectEdgeDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ReconnectEdgeDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ReconnectEdgeDescription"):
                    opp_val = getattr(item, "tool_ReconnectEdgeDescription", None)
                    
                    setattr(item, "tool_ReconnectEdgeDescription", self)
                    

    @property
    def diagram_description_EdgeMapping(self):
        return self.__diagram_description_EdgeMapping

    @diagram_description_EdgeMapping.setter
    def diagram_description_EdgeMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping", None)
        self.__diagram_description_EdgeMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping226"):
                    opp_val = getattr(item, "DiagramElementMapping226", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping226"):
                    opp_val = getattr(item, "DiagramElementMapping226", None)
                    
                    setattr(item, "DiagramElementMapping226", self)
                    

    @property
    def diagram_description_EdgeMapping228(self):
        return self.__diagram_description_EdgeMapping228

    @diagram_description_EdgeMapping228.setter
    def diagram_description_EdgeMapping228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping228", None)
        self.__diagram_description_EdgeMapping228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping229"):
                    opp_val = getattr(item, "DiagramElementMapping229", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping229"):
                    opp_val = getattr(item, "DiagramElementMapping229", None)
                    
                    setattr(item, "DiagramElementMapping229", self)
                    

    @property
    def diagram_description_EdgeMapping231(self):
        return self.__diagram_description_EdgeMapping231

    @diagram_description_EdgeMapping231.setter
    def diagram_description_EdgeMapping231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping231", None)
        self.__diagram_description_EdgeMapping231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_EdgeStyleDescription"):
                opp_val = getattr(old_value, "style_EdgeStyleDescription", None)
                if opp_val == self:
                    setattr(old_value, "style_EdgeStyleDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_EdgeStyleDescription"):
                opp_val = getattr(value, "style_EdgeStyleDescription", None)
                setattr(value, "style_EdgeStyleDescription", self)

    @property
    def diagram_description_EdgeMapping233(self):
        return self.__diagram_description_EdgeMapping233

    @diagram_description_EdgeMapping233.setter
    def diagram_description_EdgeMapping233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping233", None)
        self.__diagram_description_EdgeMapping233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConditionalEdgeStyleDescription"):
                    opp_val = getattr(item, "ConditionalEdgeStyleDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "ConditionalEdgeStyleDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConditionalEdgeStyleDescription"):
                    opp_val = getattr(item, "ConditionalEdgeStyleDescription", None)
                    
                    setattr(item, "ConditionalEdgeStyleDescription", self)
                    

    def getEdgeTargetCandidates(self, semanticOrigin: str, viewPoint: DDiagram) -> str:
        # TODO: Implement getEdgeTargetCandidates method
        pass

    def updateEdge(self, viewEdge: str):
        # TODO: Implement updateEdge method
        pass

    def getEdgeSourceCandidates(self, viewPoint: DDiagram, semanticOrigin: str) -> str:
        # TODO: Implement getEdgeSourceCandidates method
        pass

    def createEdge(self, container: str, source: EdgeTarget, semanticTarget: str, target: EdgeTarget) -> str:
        # TODO: Implement createEdge method
        pass

    def getEdgeTargetCandidates(self, semanticOrigin: str, containerView: str, container: str) -> str:
        # TODO: Implement getEdgeTargetCandidates method
        pass

    def createEdge(self, semanticTarget: str, target: EdgeTarget, source: EdgeTarget) -> str:
        # TODO: Implement createEdge method
        pass

    def getBestStyle(self, viewVariable: str, modelElement: str, containerVariable: str) -> EdgeStyle:
        # TODO: Implement getBestStyle method
        pass

class diagram_description_AbstractNodeMapping(description_DocumentedElement, description_DiagramElementMapping):

    def __init__(self, domainClass: str, diagram_description_AbstractNodeMapping: set["NodeMapping"] = None, diagram_description_AbstractNodeMapping195: set["NodeMapping"] = None):
        self.domainClass = domainClass
        self.diagram_description_AbstractNodeMapping = diagram_description_AbstractNodeMapping if diagram_description_AbstractNodeMapping is not None else set()
        self.diagram_description_AbstractNodeMapping195 = diagram_description_AbstractNodeMapping195 if diagram_description_AbstractNodeMapping195 is not None else set()
        
    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def diagram_description_AbstractNodeMapping195(self):
        return self.__diagram_description_AbstractNodeMapping195

    @diagram_description_AbstractNodeMapping195.setter
    def diagram_description_AbstractNodeMapping195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_AbstractNodeMapping__diagram_description_AbstractNodeMapping195", None)
        self.__diagram_description_AbstractNodeMapping195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping196"):
                    opp_val = getattr(item, "NodeMapping196", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping196"):
                    opp_val = getattr(item, "NodeMapping196", None)
                    
                    setattr(item, "NodeMapping196", self)
                    

    @property
    def diagram_description_AbstractNodeMapping(self):
        return self.__diagram_description_AbstractNodeMapping

    @diagram_description_AbstractNodeMapping.setter
    def diagram_description_AbstractNodeMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_AbstractNodeMapping__diagram_description_AbstractNodeMapping", None)
        self.__diagram_description_AbstractNodeMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping193"):
                    opp_val = getattr(item, "NodeMapping193", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping193"):
                    opp_val = getattr(item, "NodeMapping193", None)
                    
                    setattr(item, "NodeMapping193", self)
                    

    def clearDNodesDone(self):
        # TODO: Implement clearDNodesDone method
        pass

    def findDNodeFromEObject(self, eObject: str) -> DDiagramElement:
        # TODO: Implement findDNodeFromEObject method
        pass

    def addDoneNode(self, node: DSemanticDecorator):
        # TODO: Implement addDoneNode method
        pass

    def getAllBorderedNodeMappings(self) -> str:
        # TODO: Implement getAllBorderedNodeMappings method
        pass

class diagram_description_Layer(description_DocumentedElement, description_EndUserDocumentedElement, description_IdentifiedElement):

    def __init__(self, icon: str, diagram_description_Layer: set["NodeMapping"] = None, diagram_description_Layer265: set["DiagramElementMapping"] = None, diagram_description_Layer268: set["tool_AbstractToolDescription"] = None, diagram_description_Layer271: set["tool_ToolSection"] = None, diagram_description_Layer274: set["tool_AbstractToolDescription"] = None, diagram_description_Layer256: set["EdgeMapping"] = None, diagram_description_Layer259: set["EdgeMappingImport"] = None, diagram_description_Layer262: set["ContainerMapping"] = None, diagram_description_Layer277: "DecorationDescriptionsSet" = None, diagram_description_Layer279: set["EdgeMapping"] = None, diagram_description_Layer282: "Customization" = None):
        self.icon = icon
        self.diagram_description_Layer = diagram_description_Layer if diagram_description_Layer is not None else set()
        self.diagram_description_Layer265 = diagram_description_Layer265 if diagram_description_Layer265 is not None else set()
        self.diagram_description_Layer268 = diagram_description_Layer268 if diagram_description_Layer268 is not None else set()
        self.diagram_description_Layer271 = diagram_description_Layer271 if diagram_description_Layer271 is not None else set()
        self.diagram_description_Layer274 = diagram_description_Layer274 if diagram_description_Layer274 is not None else set()
        self.diagram_description_Layer256 = diagram_description_Layer256 if diagram_description_Layer256 is not None else set()
        self.diagram_description_Layer259 = diagram_description_Layer259 if diagram_description_Layer259 is not None else set()
        self.diagram_description_Layer262 = diagram_description_Layer262 if diagram_description_Layer262 is not None else set()
        self.diagram_description_Layer277 = diagram_description_Layer277
        self.diagram_description_Layer279 = diagram_description_Layer279 if diagram_description_Layer279 is not None else set()
        self.diagram_description_Layer282 = diagram_description_Layer282
        
    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def diagram_description_Layer259(self):
        return self.__diagram_description_Layer259

    @diagram_description_Layer259.setter
    def diagram_description_Layer259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer259", None)
        self.__diagram_description_Layer259 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMappingImport260"):
                    opp_val = getattr(item, "EdgeMappingImport260", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMappingImport260", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMappingImport260"):
                    opp_val = getattr(item, "EdgeMappingImport260", None)
                    
                    setattr(item, "EdgeMappingImport260", self)
                    

    @property
    def diagram_description_Layer256(self):
        return self.__diagram_description_Layer256

    @diagram_description_Layer256.setter
    def diagram_description_Layer256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer256", None)
        self.__diagram_description_Layer256 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMapping257"):
                    opp_val = getattr(item, "EdgeMapping257", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping257", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping257"):
                    opp_val = getattr(item, "EdgeMapping257", None)
                    
                    setattr(item, "EdgeMapping257", self)
                    

    @property
    def diagram_description_Layer282(self):
        return self.__diagram_description_Layer282

    @diagram_description_Layer282.setter
    def diagram_description_Layer282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer282", None)
        self.__diagram_description_Layer282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customization"):
                opp_val = getattr(old_value, "Customization", None)
                if opp_val == self:
                    setattr(old_value, "Customization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customization"):
                opp_val = getattr(value, "Customization", None)
                setattr(value, "Customization", self)

    @property
    def diagram_description_Layer279(self):
        return self.__diagram_description_Layer279

    @diagram_description_Layer279.setter
    def diagram_description_Layer279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer279", None)
        self.__diagram_description_Layer279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMapping280"):
                    opp_val = getattr(item, "EdgeMapping280", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping280"):
                    opp_val = getattr(item, "EdgeMapping280", None)
                    
                    setattr(item, "EdgeMapping280", self)
                    

    @property
    def diagram_description_Layer271(self):
        return self.__diagram_description_Layer271

    @diagram_description_Layer271.setter
    def diagram_description_Layer271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer271", None)
        self.__diagram_description_Layer271 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolSection272"):
                    opp_val = getattr(item, "tool_ToolSection272", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolSection272", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolSection272"):
                    opp_val = getattr(item, "tool_ToolSection272", None)
                    
                    setattr(item, "tool_ToolSection272", self)
                    

    @property
    def diagram_description_Layer(self):
        return self.__diagram_description_Layer

    @diagram_description_Layer.setter
    def diagram_description_Layer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer", None)
        self.__diagram_description_Layer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping254"):
                    opp_val = getattr(item, "NodeMapping254", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping254"):
                    opp_val = getattr(item, "NodeMapping254", None)
                    
                    setattr(item, "NodeMapping254", self)
                    

    @property
    def diagram_description_Layer262(self):
        return self.__diagram_description_Layer262

    @diagram_description_Layer262.setter
    def diagram_description_Layer262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer262", None)
        self.__diagram_description_Layer262 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping263"):
                    opp_val = getattr(item, "ContainerMapping263", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping263", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping263"):
                    opp_val = getattr(item, "ContainerMapping263", None)
                    
                    setattr(item, "ContainerMapping263", self)
                    

    @property
    def diagram_description_Layer265(self):
        return self.__diagram_description_Layer265

    @diagram_description_Layer265.setter
    def diagram_description_Layer265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer265", None)
        self.__diagram_description_Layer265 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping266"):
                    opp_val = getattr(item, "DiagramElementMapping266", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping266", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping266"):
                    opp_val = getattr(item, "DiagramElementMapping266", None)
                    
                    setattr(item, "DiagramElementMapping266", self)
                    

    @property
    def diagram_description_Layer277(self):
        return self.__diagram_description_Layer277

    @diagram_description_Layer277.setter
    def diagram_description_Layer277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer277", None)
        self.__diagram_description_Layer277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DecorationDescriptionsSet"):
                opp_val = getattr(old_value, "DecorationDescriptionsSet", None)
                if opp_val == self:
                    setattr(old_value, "DecorationDescriptionsSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DecorationDescriptionsSet"):
                opp_val = getattr(value, "DecorationDescriptionsSet", None)
                setattr(value, "DecorationDescriptionsSet", self)

    @property
    def diagram_description_Layer268(self):
        return self.__diagram_description_Layer268

    @diagram_description_Layer268.setter
    def diagram_description_Layer268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer268", None)
        self.__diagram_description_Layer268 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription269"):
                    opp_val = getattr(item, "tool_AbstractToolDescription269", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription269", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription269"):
                    opp_val = getattr(item, "tool_AbstractToolDescription269", None)
                    
                    setattr(item, "tool_AbstractToolDescription269", self)
                    

    @property
    def diagram_description_Layer274(self):
        return self.__diagram_description_Layer274

    @diagram_description_Layer274.setter
    def diagram_description_Layer274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer274", None)
        self.__diagram_description_Layer274 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription275"):
                    opp_val = getattr(item, "tool_AbstractToolDescription275", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription275", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription275"):
                    opp_val = getattr(item, "tool_AbstractToolDescription275", None)
                    
                    setattr(item, "tool_AbstractToolDescription275", self)
                    

class diagram_concern_ConcernDescription(description_DocumentedElement, description_IdentifiedElement):

    pass
class diagram_filter_FilterDescription(description_DocumentedElement, description_IdentifiedElement):

    def __init__(self):
        
    def isVisible(self, element: DDiagramElement) -> bool:
        # TODO: Implement isVisible method
        pass

class diagram_description_EdgeMappingImport(description_DocumentedElement, description_IdentifiedElement, description_IEdgeMapping):

    def __init__(self, inheritsAncestorFilters: bool, diagram_description_EdgeMappingImport: "IEdgeMapping" = None, diagram_description_EdgeMappingImport241: set["ConditionalEdgeStyleDescription"] = None):
        self.inheritsAncestorFilters = inheritsAncestorFilters
        self.diagram_description_EdgeMappingImport = diagram_description_EdgeMappingImport
        self.diagram_description_EdgeMappingImport241 = diagram_description_EdgeMappingImport241 if diagram_description_EdgeMappingImport241 is not None else set()
        
    @property
    def inheritsAncestorFilters(self) -> bool:
        return self.__inheritsAncestorFilters

    @inheritsAncestorFilters.setter
    def inheritsAncestorFilters(self, inheritsAncestorFilters: bool):
        self.__inheritsAncestorFilters = inheritsAncestorFilters

    @property
    def diagram_description_EdgeMappingImport(self):
        return self.__diagram_description_EdgeMappingImport

    @diagram_description_EdgeMappingImport.setter
    def diagram_description_EdgeMappingImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMappingImport__diagram_description_EdgeMappingImport", None)
        self.__diagram_description_EdgeMappingImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IEdgeMapping239"):
                opp_val = getattr(old_value, "IEdgeMapping239", None)
                if opp_val == self:
                    setattr(old_value, "IEdgeMapping239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IEdgeMapping239"):
                opp_val = getattr(value, "IEdgeMapping239", None)
                setattr(value, "IEdgeMapping239", self)

    @property
    def diagram_description_EdgeMappingImport241(self):
        return self.__diagram_description_EdgeMappingImport241

    @diagram_description_EdgeMappingImport241.setter
    def diagram_description_EdgeMappingImport241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMappingImport__diagram_description_EdgeMappingImport241", None)
        self.__diagram_description_EdgeMappingImport241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConditionalEdgeStyleDescription242"):
                    opp_val = getattr(item, "ConditionalEdgeStyleDescription242", None)
                    
                    if opp_val == self:
                        setattr(item, "ConditionalEdgeStyleDescription242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConditionalEdgeStyleDescription242"):
                    opp_val = getattr(item, "ConditionalEdgeStyleDescription242", None)
                    
                    setattr(item, "ConditionalEdgeStyleDescription242", self)
                    

class DRepresentation:

    pass
class diagram_DDiagram(DragAndDropTarget, description_DocumentedElement, DRepresentation):

    def __init__(self, synchronized: bool, isInLayoutingMode: bool, headerHeight: int, diagram_DDiagram11: set["diagram_DNodeListElement"] = None, diagram_DDiagram: set["diagram_DDiagramElement"] = None, diagram_DDiagram2: set["diagram_DDiagramElement"] = None, diagram_DDiagram5: "DiagramDescription" = None, diagram_DDiagram7: set["diagram_DEdge"] = None, diagram_DDiagram9: set["diagram_DNode"] = None, diagram_DDiagram26: set["tool_BehaviorTool"] = None, diagram_DDiagram13: set["diagram_DDiagramElementContainer"] = None, diagram_DDiagram15: "concern_ConcernDescription" = None, diagram_DDiagram17: set["filter_FilterDescription"] = None, diagram_DDiagram19: set["AdditionalLayer"] = None, diagram_DDiagram21: set["filter_FilterDescription"] = None, diagram_DDiagram24: set["validation_ValidationRule"] = None, diagram_DDiagram28: "diagram_FilterVariableHistory" = None, diagram_DDiagram30: set["Layer"] = None, diagram_DDiagram32: set["diagram_DDiagramElement"] = None):
        self.synchronized = synchronized
        self.isInLayoutingMode = isInLayoutingMode
        self.headerHeight = headerHeight
        self.diagram_DDiagram11 = diagram_DDiagram11 if diagram_DDiagram11 is not None else set()
        self.diagram_DDiagram = diagram_DDiagram if diagram_DDiagram is not None else set()
        self.diagram_DDiagram2 = diagram_DDiagram2 if diagram_DDiagram2 is not None else set()
        self.diagram_DDiagram5 = diagram_DDiagram5
        self.diagram_DDiagram7 = diagram_DDiagram7 if diagram_DDiagram7 is not None else set()
        self.diagram_DDiagram9 = diagram_DDiagram9 if diagram_DDiagram9 is not None else set()
        self.diagram_DDiagram26 = diagram_DDiagram26 if diagram_DDiagram26 is not None else set()
        self.diagram_DDiagram13 = diagram_DDiagram13 if diagram_DDiagram13 is not None else set()
        self.diagram_DDiagram15 = diagram_DDiagram15
        self.diagram_DDiagram17 = diagram_DDiagram17 if diagram_DDiagram17 is not None else set()
        self.diagram_DDiagram19 = diagram_DDiagram19 if diagram_DDiagram19 is not None else set()
        self.diagram_DDiagram21 = diagram_DDiagram21 if diagram_DDiagram21 is not None else set()
        self.diagram_DDiagram24 = diagram_DDiagram24 if diagram_DDiagram24 is not None else set()
        self.diagram_DDiagram28 = diagram_DDiagram28
        self.diagram_DDiagram30 = diagram_DDiagram30 if diagram_DDiagram30 is not None else set()
        self.diagram_DDiagram32 = diagram_DDiagram32 if diagram_DDiagram32 is not None else set()
        
    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def isInLayoutingMode(self) -> bool:
        return self.__isInLayoutingMode

    @isInLayoutingMode.setter
    def isInLayoutingMode(self, isInLayoutingMode: bool):
        self.__isInLayoutingMode = isInLayoutingMode

    @property
    def headerHeight(self) -> int:
        return self.__headerHeight

    @headerHeight.setter
    def headerHeight(self, headerHeight: int):
        self.__headerHeight = headerHeight

    @property
    def diagram_DDiagram21(self):
        return self.__diagram_DDiagram21

    @diagram_DDiagram21.setter
    def diagram_DDiagram21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram21", None)
        self.__diagram_DDiagram21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "filter_FilterDescription22"):
                    opp_val = getattr(item, "filter_FilterDescription22", None)
                    
                    if opp_val == self:
                        setattr(item, "filter_FilterDescription22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filter_FilterDescription22"):
                    opp_val = getattr(item, "filter_FilterDescription22", None)
                    
                    setattr(item, "filter_FilterDescription22", self)
                    

    @property
    def diagram_DDiagram5(self):
        return self.__diagram_DDiagram5

    @diagram_DDiagram5.setter
    def diagram_DDiagram5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram5", None)
        self.__diagram_DDiagram5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramDescription"):
                opp_val = getattr(old_value, "DiagramDescription", None)
                if opp_val == self:
                    setattr(old_value, "DiagramDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramDescription"):
                opp_val = getattr(value, "DiagramDescription", None)
                setattr(value, "DiagramDescription", self)

    @property
    def diagram_DDiagram30(self):
        return self.__diagram_DDiagram30

    @diagram_DDiagram30.setter
    def diagram_DDiagram30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram30", None)
        self.__diagram_DDiagram30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Layer"):
                    opp_val = getattr(item, "Layer", None)
                    
                    if opp_val == self:
                        setattr(item, "Layer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Layer"):
                    opp_val = getattr(item, "Layer", None)
                    
                    setattr(item, "Layer", self)
                    

    @property
    def diagram_DDiagram7(self):
        return self.__diagram_DDiagram7

    @diagram_DDiagram7.setter
    def diagram_DDiagram7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram7", None)
        self.__diagram_DDiagram7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DEdge"):
                    opp_val = getattr(item, "diagram_DEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DEdge"):
                    opp_val = getattr(item, "diagram_DEdge", None)
                    
                    setattr(item, "diagram_DEdge", self)
                    

    @property
    def diagram_DDiagram32(self):
        return self.__diagram_DDiagram32

    @diagram_DDiagram32.setter
    def diagram_DDiagram32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram32", None)
        self.__diagram_DDiagram32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DDiagramElement33"):
                    opp_val = getattr(item, "diagram_DDiagramElement33", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElement33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElement33"):
                    opp_val = getattr(item, "diagram_DDiagramElement33", None)
                    
                    setattr(item, "diagram_DDiagramElement33", self)
                    

    @property
    def diagram_DDiagram28(self):
        return self.__diagram_DDiagram28

    @diagram_DDiagram28.setter
    def diagram_DDiagram28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram28", None)
        self.__diagram_DDiagram28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_FilterVariableHistory"):
                opp_val = getattr(old_value, "diagram_FilterVariableHistory", None)
                if opp_val == self:
                    setattr(old_value, "diagram_FilterVariableHistory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_FilterVariableHistory"):
                opp_val = getattr(value, "diagram_FilterVariableHistory", None)
                setattr(value, "diagram_FilterVariableHistory", self)

    @property
    def diagram_DDiagram26(self):
        return self.__diagram_DDiagram26

    @diagram_DDiagram26.setter
    def diagram_DDiagram26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram26", None)
        self.__diagram_DDiagram26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_BehaviorTool"):
                    opp_val = getattr(item, "tool_BehaviorTool", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_BehaviorTool", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_BehaviorTool"):
                    opp_val = getattr(item, "tool_BehaviorTool", None)
                    
                    setattr(item, "tool_BehaviorTool", self)
                    

    @property
    def diagram_DDiagram2(self):
        return self.__diagram_DDiagram2

    @diagram_DDiagram2.setter
    def diagram_DDiagram2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram2", None)
        self.__diagram_DDiagram2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DDiagramElement3"):
                    opp_val = getattr(item, "diagram_DDiagramElement3", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElement3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElement3"):
                    opp_val = getattr(item, "diagram_DDiagramElement3", None)
                    
                    setattr(item, "diagram_DDiagramElement3", self)
                    

    @property
    def diagram_DDiagram11(self):
        return self.__diagram_DDiagram11

    @diagram_DDiagram11.setter
    def diagram_DDiagram11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram11", None)
        self.__diagram_DDiagram11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DNodeListElement"):
                    opp_val = getattr(item, "diagram_DNodeListElement", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DNodeListElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DNodeListElement"):
                    opp_val = getattr(item, "diagram_DNodeListElement", None)
                    
                    setattr(item, "diagram_DNodeListElement", self)
                    

    @property
    def diagram_DDiagram19(self):
        return self.__diagram_DDiagram19

    @diagram_DDiagram19.setter
    def diagram_DDiagram19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram19", None)
        self.__diagram_DDiagram19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AdditionalLayer"):
                    opp_val = getattr(item, "AdditionalLayer", None)
                    
                    if opp_val == self:
                        setattr(item, "AdditionalLayer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AdditionalLayer"):
                    opp_val = getattr(item, "AdditionalLayer", None)
                    
                    setattr(item, "AdditionalLayer", self)
                    

    @property
    def diagram_DDiagram9(self):
        return self.__diagram_DDiagram9

    @diagram_DDiagram9.setter
    def diagram_DDiagram9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram9", None)
        self.__diagram_DDiagram9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DNode"):
                    opp_val = getattr(item, "diagram_DNode", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DNode"):
                    opp_val = getattr(item, "diagram_DNode", None)
                    
                    setattr(item, "diagram_DNode", self)
                    

    @property
    def diagram_DDiagram(self):
        return self.__diagram_DDiagram

    @diagram_DDiagram.setter
    def diagram_DDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram", None)
        self.__diagram_DDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DDiagramElement"):
                    opp_val = getattr(item, "diagram_DDiagramElement", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElement"):
                    opp_val = getattr(item, "diagram_DDiagramElement", None)
                    
                    setattr(item, "diagram_DDiagramElement", self)
                    

    @property
    def diagram_DDiagram13(self):
        return self.__diagram_DDiagram13

    @diagram_DDiagram13.setter
    def diagram_DDiagram13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram13", None)
        self.__diagram_DDiagram13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DDiagramElementContainer"):
                    opp_val = getattr(item, "diagram_DDiagramElementContainer", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElementContainer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElementContainer"):
                    opp_val = getattr(item, "diagram_DDiagramElementContainer", None)
                    
                    setattr(item, "diagram_DDiagramElementContainer", self)
                    

    @property
    def diagram_DDiagram15(self):
        return self.__diagram_DDiagram15

    @diagram_DDiagram15.setter
    def diagram_DDiagram15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram15", None)
        self.__diagram_DDiagram15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "concern_ConcernDescription"):
                opp_val = getattr(old_value, "concern_ConcernDescription", None)
                if opp_val == self:
                    setattr(old_value, "concern_ConcernDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "concern_ConcernDescription"):
                opp_val = getattr(value, "concern_ConcernDescription", None)
                setattr(value, "concern_ConcernDescription", self)

    @property
    def diagram_DDiagram17(self):
        return self.__diagram_DDiagram17

    @diagram_DDiagram17.setter
    def diagram_DDiagram17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram17", None)
        self.__diagram_DDiagram17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "filter_FilterDescription"):
                    opp_val = getattr(item, "filter_FilterDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "filter_FilterDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filter_FilterDescription"):
                    opp_val = getattr(item, "filter_FilterDescription", None)
                    
                    setattr(item, "filter_FilterDescription", self)
                    

    @property
    def diagram_DDiagram24(self):
        return self.__diagram_DDiagram24

    @diagram_DDiagram24.setter
    def diagram_DDiagram24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram24", None)
        self.__diagram_DDiagram24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "validation_ValidationRule"):
                    opp_val = getattr(item, "validation_ValidationRule", None)
                    
                    if opp_val == self:
                        setattr(item, "validation_ValidationRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "validation_ValidationRule"):
                    opp_val = getattr(item, "validation_ValidationRule", None)
                    
                    setattr(item, "validation_ValidationRule", self)
                    

    def getNodesFromMapping(self, mapping: str) -> str:
        # TODO: Implement getNodesFromMapping method
        pass

    def getContainersFromMapping(self, mapping: str) -> str:
        # TODO: Implement getContainersFromMapping method
        pass

    def getEdgesFromMapping(self, mapping: str) -> str:
        # TODO: Implement getEdgesFromMapping method
        pass
