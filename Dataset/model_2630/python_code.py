from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BackgroundStyle(Enum):
    GradientLeftToRight = "GradientLeftToRight"
    Liquid = "Liquid"
    GradientTopToBottom = "GradientTopToBottom"
class BundledImageShape(Enum):
    square = "square"
    stroke = "stroke"
    triangle = "triangle"
    dot = "dot"
    ring = "ring"
class ContainerLayout(Enum):
    FreeForm = "FreeForm"
    List = "List"
    HorizontalStack = "HorizontalStack"
    VerticalStack = "VerticalStack"
class FoldingStyle(Enum):
    NONE = "NONE"
    SOURCE = "SOURCE"
    TARGET = "TARGET"
class ContainerShape(Enum):
    parallelogram = "parallelogram"
class LayoutDirection(Enum):
    TopToBottom = "TopToBottom"
    LeftToRight = "LeftToRight"
    BottomToTop = "BottomToTop"
class ArrangeConstraint(Enum):
    KEEP_LOCATION = "KEEP_LOCATION"
    KEEP_SIZE = "KEEP_SIZE"
    KEEP_RATIO = "KEEP_RATIO"
class LineStyle(Enum):
    solid = "solid"
    dash = "dash"
    dot = "dot"
    dash_dot = "dash_dot"
class FilterKind(Enum):
    HIDE = "HIDE"
    COLLAPSE = "COLLAPSE"
class EdgeArrows(Enum):
    InputClosedArrow = "InputClosedArrow"
    OutputFillClosedArrow = "OutputFillClosedArrow"
    InputFillClosedArrow = "InputFillClosedArrow"
    Diamond = "Diamond"
    FillDiamond = "FillDiamond"
    InputArrowWithDiamond = "InputArrowWithDiamond"
    InputArrowWithFillDiamond = "InputArrowWithFillDiamond"
    NoDecoration = "NoDecoration"
    OutputArrow = "OutputArrow"
    InputArrow = "InputArrow"
    OutputClosedArrow = "OutputClosedArrow"
class LabelPosition(Enum):
    border = "border"
    node = "node"
class AlignmentKind(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
    SQUARE = "SQUARE"
class ResizeKind(Enum):
    NONE = "NONE"
    NSEW = "NSEW"
    NORTH_SOUTH = "NORTH_SOUTH"
    EAST_WEST = "EAST_WEST"
class EdgeRouting(Enum):
    straight = "straight"
    manhattan = "manhattan"
    tree = "tree"
class ReconnectionKind(Enum):
    RECONNECT_TARGET = "RECONNECT_TARGET"
    RECONNECT_SOURCE = "RECONNECT_SOURCE"
    RECONNECT_BOTH = "RECONNECT_BOTH"


############################################
# Definition of Classes
############################################

class filter_Filter:

    pass
class SelectionDescription:

    pass
class diagram_filter_FilterVariable(SelectionDescription):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class tool_InitialContainerDropOperation:

    pass
class tool_ElementDropVariable:

    pass
class FilterDescription:

    pass
class diagram_filter_CompositeFilterDescription(FilterDescription):

    pass
class Filter:

    pass
class diagram_filter_VariableFilter(Filter):

    def __init__(self, semanticConditionExpression: str, diagram_filter_VariableFilter: set["filter_FilterVariable"] = None):
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
                if hasattr(item, "filter_FilterVariable500"):
                    opp_val = getattr(item, "filter_FilterVariable500", None)
                    
                    if opp_val == self:
                        setattr(item, "filter_FilterVariable500", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filter_FilterVariable500"):
                    opp_val = getattr(item, "filter_FilterVariable500", None)
                    
                    setattr(item, "filter_FilterVariable500", self)
                    

    def setFilterContext(self, variables: str):
        # TODO: Implement setFilterContext method
        pass

class diagram_filter_MappingFilter(Filter):

    def __init__(self, semanticConditionExpression: str, viewConditionExpression: str, diagram_filter_MappingFilter: set["DiagramElementMapping"] = None):
        self.semanticConditionExpression = semanticConditionExpression
        self.viewConditionExpression = viewConditionExpression
        self.diagram_filter_MappingFilter = diagram_filter_MappingFilter if diagram_filter_MappingFilter is not None else set()
        
    @property
    def semanticConditionExpression(self) -> str:
        return self.__semanticConditionExpression

    @semanticConditionExpression.setter
    def semanticConditionExpression(self, semanticConditionExpression: str):
        self.__semanticConditionExpression = semanticConditionExpression

    @property
    def viewConditionExpression(self) -> str:
        return self.__viewConditionExpression

    @viewConditionExpression.setter
    def viewConditionExpression(self, viewConditionExpression: str):
        self.__viewConditionExpression = viewConditionExpression

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
                if hasattr(item, "DiagramElementMapping497"):
                    opp_val = getattr(item, "DiagramElementMapping497", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping497", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping497"):
                    opp_val = getattr(item, "DiagramElementMapping497", None)
                    
                    setattr(item, "DiagramElementMapping497", self)
                    

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
    def sourceExpression(self) -> str:
        return self.__sourceExpression

    @sourceExpression.setter
    def sourceExpression(self, sourceExpression: str):
        self.__sourceExpression = sourceExpression

    @property
    def targetExpression(self) -> str:
        return self.__targetExpression

    @targetExpression.setter
    def targetExpression(self, targetExpression: str):
        self.__targetExpression = targetExpression

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
            if hasattr(old_value, "DiagramDescription477"):
                opp_val = getattr(old_value, "DiagramDescription477", None)
                if opp_val == self:
                    setattr(old_value, "DiagramDescription477", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramDescription477"):
                opp_val = getattr(value, "DiagramDescription477", None)
                setattr(value, "DiagramDescription477", self)

class diagram_tool_CreateView(ContainerModelOperation):

    def __init__(self, containerViewExpression: str, variableName: str, diagram_tool_CreateView: "DiagramElementMapping" = None):
        self.containerViewExpression = containerViewExpression
        self.variableName = variableName
        self.diagram_tool_CreateView = diagram_tool_CreateView
        
    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def containerViewExpression(self) -> str:
        return self.__containerViewExpression

    @containerViewExpression.setter
    def containerViewExpression(self, containerViewExpression: str):
        self.__containerViewExpression = containerViewExpression

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
            if hasattr(old_value, "DiagramElementMapping475"):
                opp_val = getattr(old_value, "DiagramElementMapping475", None)
                if opp_val == self:
                    setattr(old_value, "DiagramElementMapping475", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramElementMapping475"):
                opp_val = getattr(value, "DiagramElementMapping475", None)
                setattr(value, "DiagramElementMapping475", self)

class tool_VariableContainer:

    pass
class tool_AbstractVariable:

    pass
class diagram_tool_TargetEdgeViewCreationVariable(tool_VariableContainer, tool_AbstractVariable):

    pass
class diagram_tool_SourceEdgeViewCreationVariable(tool_VariableContainer, tool_AbstractVariable):

    pass
class diagram_tool_NodeCreationVariable(tool_VariableContainer, tool_AbstractVariable):

    pass
class diagram_tool_TargetEdgeCreationVariable(tool_VariableContainer, tool_AbstractVariable):

    pass
class diagram_tool_ElementDoubleClickVariable(tool_VariableContainer, tool_AbstractVariable):

    pass
class diagram_tool_SourceEdgeCreationVariable(tool_VariableContainer, tool_AbstractVariable):

    pass
class AbstractToolDescription:

    pass
class diagram_tool_RequestDescription(AbstractToolDescription):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
            if hasattr(old_value, "tool_InitialOperation473"):
                opp_val = getattr(old_value, "tool_InitialOperation473", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation473", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation473"):
                opp_val = getattr(value, "tool_InitialOperation473", None)
                setattr(value, "tool_InitialOperation473", self)

class tool_EditMaskVariables:

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
class tool_ElementSelectVariable:

    pass
class tool_DeleteHook:

    pass
class tool_ElementDeleteVariable:

    pass
class tool_TargetEdgeCreationVariable:

    pass
class tool_SourceEdgeCreationVariable:

    pass
class tool_InitEdgeCreationOperation:

    pass
class tool_TargetEdgeViewCreationVariable:

    pass
class tool_SourceEdgeViewCreationVariable:

    pass
class MappingBasedToolDescription:

    pass
class diagram_tool_ContainerDropDescription(MappingBasedToolDescription):

    def __init__(self, dragSource: str, moveEdges: bool, diagram_tool_ContainerDropDescription: set["DiagramElementMapping"] = None, diagram_tool_ContainerDropDescription485: "tool_DropContainerVariable" = None, diagram_tool_ContainerDropDescription487: "tool_DropContainerVariable" = None, diagram_tool_ContainerDropDescription490: "tool_ElementDropVariable" = None, diagram_tool_ContainerDropDescription492: "tool_ContainerViewVariable" = None, diagram_tool_ContainerDropDescription495: "tool_InitialContainerDropOperation" = None):
        self.dragSource = dragSource
        self.moveEdges = moveEdges
        self.diagram_tool_ContainerDropDescription = diagram_tool_ContainerDropDescription if diagram_tool_ContainerDropDescription is not None else set()
        self.diagram_tool_ContainerDropDescription485 = diagram_tool_ContainerDropDescription485
        self.diagram_tool_ContainerDropDescription487 = diagram_tool_ContainerDropDescription487
        self.diagram_tool_ContainerDropDescription490 = diagram_tool_ContainerDropDescription490
        self.diagram_tool_ContainerDropDescription492 = diagram_tool_ContainerDropDescription492
        self.diagram_tool_ContainerDropDescription495 = diagram_tool_ContainerDropDescription495
        
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
                if hasattr(item, "DiagramElementMapping483"):
                    opp_val = getattr(item, "DiagramElementMapping483", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping483", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping483"):
                    opp_val = getattr(item, "DiagramElementMapping483", None)
                    
                    setattr(item, "DiagramElementMapping483", self)
                    

    @property
    def diagram_tool_ContainerDropDescription492(self):
        return self.__diagram_tool_ContainerDropDescription492

    @diagram_tool_ContainerDropDescription492.setter
    def diagram_tool_ContainerDropDescription492(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription492", None)
        self.__diagram_tool_ContainerDropDescription492 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable493"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable493", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable493", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable493"):
                opp_val = getattr(value, "tool_ContainerViewVariable493", None)
                setattr(value, "tool_ContainerViewVariable493", self)

    @property
    def diagram_tool_ContainerDropDescription490(self):
        return self.__diagram_tool_ContainerDropDescription490

    @diagram_tool_ContainerDropDescription490.setter
    def diagram_tool_ContainerDropDescription490(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription490", None)
        self.__diagram_tool_ContainerDropDescription490 = value
        
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
    def diagram_tool_ContainerDropDescription485(self):
        return self.__diagram_tool_ContainerDropDescription485

    @diagram_tool_ContainerDropDescription485.setter
    def diagram_tool_ContainerDropDescription485(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription485", None)
        self.__diagram_tool_ContainerDropDescription485 = value
        
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
    def diagram_tool_ContainerDropDescription495(self):
        return self.__diagram_tool_ContainerDropDescription495

    @diagram_tool_ContainerDropDescription495.setter
    def diagram_tool_ContainerDropDescription495(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription495", None)
        self.__diagram_tool_ContainerDropDescription495 = value
        
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

    @property
    def diagram_tool_ContainerDropDescription487(self):
        return self.__diagram_tool_ContainerDropDescription487

    @diagram_tool_ContainerDropDescription487.setter
    def diagram_tool_ContainerDropDescription487(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription487", None)
        self.__diagram_tool_ContainerDropDescription487 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DropContainerVariable488"):
                opp_val = getattr(old_value, "tool_DropContainerVariable488", None)
                if opp_val == self:
                    setattr(old_value, "tool_DropContainerVariable488", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DropContainerVariable488"):
                opp_val = getattr(value, "tool_DropContainerVariable488", None)
                setattr(value, "tool_DropContainerVariable488", self)

    def getContainers(self) -> str:
        # TODO: Implement getContainers method
        pass

    def getBestMapping(self, droppedElement: str, targetContainer: DragAndDropTarget) -> str:
        # TODO: Implement getBestMapping method
        pass

class diagram_tool_DoubleClickDescription(MappingBasedToolDescription):

    pass
class diagram_tool_DeleteElementDescription(MappingBasedToolDescription):

    def __init__(self, diagram_tool_DeleteElementDescription: "tool_ElementDeleteVariable" = None, diagram_tool_DeleteElementDescription428: "tool_ElementDeleteVariable" = None, diagram_tool_DeleteElementDescription431: "tool_ContainerViewVariable" = None, diagram_tool_DeleteElementDescription434: "tool_InitialOperation" = None, diagram_tool_DeleteElementDescription437: "tool_DeleteHook" = None):
        self.diagram_tool_DeleteElementDescription = diagram_tool_DeleteElementDescription
        self.diagram_tool_DeleteElementDescription428 = diagram_tool_DeleteElementDescription428
        self.diagram_tool_DeleteElementDescription431 = diagram_tool_DeleteElementDescription431
        self.diagram_tool_DeleteElementDescription434 = diagram_tool_DeleteElementDescription434
        self.diagram_tool_DeleteElementDescription437 = diagram_tool_DeleteElementDescription437
        
    @property
    def diagram_tool_DeleteElementDescription437(self):
        return self.__diagram_tool_DeleteElementDescription437

    @diagram_tool_DeleteElementDescription437.setter
    def diagram_tool_DeleteElementDescription437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription437", None)
        self.__diagram_tool_DeleteElementDescription437 = value
        
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
    def diagram_tool_DeleteElementDescription431(self):
        return self.__diagram_tool_DeleteElementDescription431

    @diagram_tool_DeleteElementDescription431.setter
    def diagram_tool_DeleteElementDescription431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription431", None)
        self.__diagram_tool_DeleteElementDescription431 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable432"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable432", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable432"):
                opp_val = getattr(value, "tool_ContainerViewVariable432", None)
                setattr(value, "tool_ContainerViewVariable432", self)

    @property
    def diagram_tool_DeleteElementDescription428(self):
        return self.__diagram_tool_DeleteElementDescription428

    @diagram_tool_DeleteElementDescription428.setter
    def diagram_tool_DeleteElementDescription428(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription428", None)
        self.__diagram_tool_DeleteElementDescription428 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementDeleteVariable429"):
                opp_val = getattr(old_value, "tool_ElementDeleteVariable429", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementDeleteVariable429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementDeleteVariable429"):
                opp_val = getattr(value, "tool_ElementDeleteVariable429", None)
                setattr(value, "tool_ElementDeleteVariable429", self)

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

    @property
    def diagram_tool_DeleteElementDescription434(self):
        return self.__diagram_tool_DeleteElementDescription434

    @diagram_tool_DeleteElementDescription434.setter
    def diagram_tool_DeleteElementDescription434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription434", None)
        self.__diagram_tool_DeleteElementDescription434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation435"):
                opp_val = getattr(old_value, "tool_InitialOperation435", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation435", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation435"):
                opp_val = getattr(value, "tool_InitialOperation435", None)
                setattr(value, "tool_InitialOperation435", self)

    def getMappings(self) -> str:
        # TODO: Implement getMappings method
        pass

class diagram_tool_DirectEditLabel(MappingBasedToolDescription):

    def __init__(self, inputLabelExpression: str, diagram_tool_DirectEditLabel: "tool_EditMaskVariables" = None, diagram_tool_DirectEditLabel470: "tool_InitialOperation" = None):
        self.inputLabelExpression = inputLabelExpression
        self.diagram_tool_DirectEditLabel = diagram_tool_DirectEditLabel
        self.diagram_tool_DirectEditLabel470 = diagram_tool_DirectEditLabel470
        
    @property
    def inputLabelExpression(self) -> str:
        return self.__inputLabelExpression

    @inputLabelExpression.setter
    def inputLabelExpression(self, inputLabelExpression: str):
        self.__inputLabelExpression = inputLabelExpression

    @property
    def diagram_tool_DirectEditLabel470(self):
        return self.__diagram_tool_DirectEditLabel470

    @diagram_tool_DirectEditLabel470.setter
    def diagram_tool_DirectEditLabel470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DirectEditLabel__diagram_tool_DirectEditLabel470", None)
        self.__diagram_tool_DirectEditLabel470 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation471"):
                opp_val = getattr(old_value, "tool_InitialOperation471", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation471", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation471"):
                opp_val = getattr(value, "tool_InitialOperation471", None)
                setattr(value, "tool_InitialOperation471", self)

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

class diagram_tool_ContainerCreationDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, diagram_tool_ContainerCreationDescription424: set["AbstractNodeMapping"] = None, diagram_tool_ContainerCreationDescription: set["ContainerMapping"] = None, diagram_tool_ContainerCreationDescription415: "tool_NodeCreationVariable" = None, diagram_tool_ContainerCreationDescription418: "tool_ContainerViewVariable" = None, diagram_tool_ContainerCreationDescription421: "tool_InitialNodeCreationOperation" = None):
        self.iconPath = iconPath
        self.diagram_tool_ContainerCreationDescription424 = diagram_tool_ContainerCreationDescription424 if diagram_tool_ContainerCreationDescription424 is not None else set()
        self.diagram_tool_ContainerCreationDescription = diagram_tool_ContainerCreationDescription if diagram_tool_ContainerCreationDescription is not None else set()
        self.diagram_tool_ContainerCreationDescription415 = diagram_tool_ContainerCreationDescription415
        self.diagram_tool_ContainerCreationDescription418 = diagram_tool_ContainerCreationDescription418
        self.diagram_tool_ContainerCreationDescription421 = diagram_tool_ContainerCreationDescription421
        
    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def diagram_tool_ContainerCreationDescription421(self):
        return self.__diagram_tool_ContainerCreationDescription421

    @diagram_tool_ContainerCreationDescription421.setter
    def diagram_tool_ContainerCreationDescription421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription421", None)
        self.__diagram_tool_ContainerCreationDescription421 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialNodeCreationOperation422"):
                opp_val = getattr(old_value, "tool_InitialNodeCreationOperation422", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialNodeCreationOperation422", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialNodeCreationOperation422"):
                opp_val = getattr(value, "tool_InitialNodeCreationOperation422", None)
                setattr(value, "tool_InitialNodeCreationOperation422", self)

    @property
    def diagram_tool_ContainerCreationDescription415(self):
        return self.__diagram_tool_ContainerCreationDescription415

    @diagram_tool_ContainerCreationDescription415.setter
    def diagram_tool_ContainerCreationDescription415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription415", None)
        self.__diagram_tool_ContainerCreationDescription415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_NodeCreationVariable416"):
                opp_val = getattr(old_value, "tool_NodeCreationVariable416", None)
                if opp_val == self:
                    setattr(old_value, "tool_NodeCreationVariable416", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_NodeCreationVariable416"):
                opp_val = getattr(value, "tool_NodeCreationVariable416", None)
                setattr(value, "tool_NodeCreationVariable416", self)

    @property
    def diagram_tool_ContainerCreationDescription424(self):
        return self.__diagram_tool_ContainerCreationDescription424

    @diagram_tool_ContainerCreationDescription424.setter
    def diagram_tool_ContainerCreationDescription424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription424", None)
        self.__diagram_tool_ContainerCreationDescription424 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractNodeMapping425"):
                    opp_val = getattr(item, "AbstractNodeMapping425", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractNodeMapping425", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractNodeMapping425"):
                    opp_val = getattr(item, "AbstractNodeMapping425", None)
                    
                    setattr(item, "AbstractNodeMapping425", self)
                    

    @property
    def diagram_tool_ContainerCreationDescription418(self):
        return self.__diagram_tool_ContainerCreationDescription418

    @diagram_tool_ContainerCreationDescription418.setter
    def diagram_tool_ContainerCreationDescription418(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription418", None)
        self.__diagram_tool_ContainerCreationDescription418 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable419"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable419", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable419", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable419"):
                opp_val = getattr(value, "tool_ContainerViewVariable419", None)
                setattr(value, "tool_ContainerViewVariable419", self)

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
                if hasattr(item, "ContainerMapping413"):
                    opp_val = getattr(item, "ContainerMapping413", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping413", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping413"):
                    opp_val = getattr(item, "ContainerMapping413", None)
                    
                    setattr(item, "ContainerMapping413", self)
                    

class diagram_tool_ReconnectEdgeDescription(MappingBasedToolDescription):

    def __init__(self, reconnectionKind: str, diagram_tool_ReconnectEdgeDescription: "tool_SourceEdgeCreationVariable" = None, diagram_tool_ReconnectEdgeDescription452: "tool_TargetEdgeCreationVariable" = None, diagram_tool_ReconnectEdgeDescription455: "tool_SourceEdgeViewCreationVariable" = None, diagram_tool_ReconnectEdgeDescription458: "tool_TargetEdgeViewCreationVariable" = None, diagram_tool_ReconnectEdgeDescription461: "tool_ElementSelectVariable" = None, diagram_tool_ReconnectEdgeDescription463: "tool_InitialOperation" = None, diagram_tool_ReconnectEdgeDescription466: "tool_ElementSelectVariable" = None):
        self.reconnectionKind = reconnectionKind
        self.diagram_tool_ReconnectEdgeDescription = diagram_tool_ReconnectEdgeDescription
        self.diagram_tool_ReconnectEdgeDescription452 = diagram_tool_ReconnectEdgeDescription452
        self.diagram_tool_ReconnectEdgeDescription455 = diagram_tool_ReconnectEdgeDescription455
        self.diagram_tool_ReconnectEdgeDescription458 = diagram_tool_ReconnectEdgeDescription458
        self.diagram_tool_ReconnectEdgeDescription461 = diagram_tool_ReconnectEdgeDescription461
        self.diagram_tool_ReconnectEdgeDescription463 = diagram_tool_ReconnectEdgeDescription463
        self.diagram_tool_ReconnectEdgeDescription466 = diagram_tool_ReconnectEdgeDescription466
        
    @property
    def reconnectionKind(self) -> str:
        return self.__reconnectionKind

    @reconnectionKind.setter
    def reconnectionKind(self, reconnectionKind: str):
        self.__reconnectionKind = reconnectionKind

    @property
    def diagram_tool_ReconnectEdgeDescription455(self):
        return self.__diagram_tool_ReconnectEdgeDescription455

    @diagram_tool_ReconnectEdgeDescription455.setter
    def diagram_tool_ReconnectEdgeDescription455(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription455", None)
        self.__diagram_tool_ReconnectEdgeDescription455 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SourceEdgeViewCreationVariable456"):
                opp_val = getattr(old_value, "tool_SourceEdgeViewCreationVariable456", None)
                if opp_val == self:
                    setattr(old_value, "tool_SourceEdgeViewCreationVariable456", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SourceEdgeViewCreationVariable456"):
                opp_val = getattr(value, "tool_SourceEdgeViewCreationVariable456", None)
                setattr(value, "tool_SourceEdgeViewCreationVariable456", self)

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
            if hasattr(old_value, "tool_SourceEdgeCreationVariable450"):
                opp_val = getattr(old_value, "tool_SourceEdgeCreationVariable450", None)
                if opp_val == self:
                    setattr(old_value, "tool_SourceEdgeCreationVariable450", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SourceEdgeCreationVariable450"):
                opp_val = getattr(value, "tool_SourceEdgeCreationVariable450", None)
                setattr(value, "tool_SourceEdgeCreationVariable450", self)

    @property
    def diagram_tool_ReconnectEdgeDescription452(self):
        return self.__diagram_tool_ReconnectEdgeDescription452

    @diagram_tool_ReconnectEdgeDescription452.setter
    def diagram_tool_ReconnectEdgeDescription452(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription452", None)
        self.__diagram_tool_ReconnectEdgeDescription452 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_TargetEdgeCreationVariable453"):
                opp_val = getattr(old_value, "tool_TargetEdgeCreationVariable453", None)
                if opp_val == self:
                    setattr(old_value, "tool_TargetEdgeCreationVariable453", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_TargetEdgeCreationVariable453"):
                opp_val = getattr(value, "tool_TargetEdgeCreationVariable453", None)
                setattr(value, "tool_TargetEdgeCreationVariable453", self)

    @property
    def diagram_tool_ReconnectEdgeDescription466(self):
        return self.__diagram_tool_ReconnectEdgeDescription466

    @diagram_tool_ReconnectEdgeDescription466.setter
    def diagram_tool_ReconnectEdgeDescription466(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription466", None)
        self.__diagram_tool_ReconnectEdgeDescription466 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementSelectVariable467"):
                opp_val = getattr(old_value, "tool_ElementSelectVariable467", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementSelectVariable467", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementSelectVariable467"):
                opp_val = getattr(value, "tool_ElementSelectVariable467", None)
                setattr(value, "tool_ElementSelectVariable467", self)

    @property
    def diagram_tool_ReconnectEdgeDescription463(self):
        return self.__diagram_tool_ReconnectEdgeDescription463

    @diagram_tool_ReconnectEdgeDescription463.setter
    def diagram_tool_ReconnectEdgeDescription463(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription463", None)
        self.__diagram_tool_ReconnectEdgeDescription463 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation464"):
                opp_val = getattr(old_value, "tool_InitialOperation464", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation464", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation464"):
                opp_val = getattr(value, "tool_InitialOperation464", None)
                setattr(value, "tool_InitialOperation464", self)

    @property
    def diagram_tool_ReconnectEdgeDescription461(self):
        return self.__diagram_tool_ReconnectEdgeDescription461

    @diagram_tool_ReconnectEdgeDescription461.setter
    def diagram_tool_ReconnectEdgeDescription461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription461", None)
        self.__diagram_tool_ReconnectEdgeDescription461 = value
        
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
    def diagram_tool_ReconnectEdgeDescription458(self):
        return self.__diagram_tool_ReconnectEdgeDescription458

    @diagram_tool_ReconnectEdgeDescription458.setter
    def diagram_tool_ReconnectEdgeDescription458(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription458", None)
        self.__diagram_tool_ReconnectEdgeDescription458 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_TargetEdgeViewCreationVariable459"):
                opp_val = getattr(old_value, "tool_TargetEdgeViewCreationVariable459", None)
                if opp_val == self:
                    setattr(old_value, "tool_TargetEdgeViewCreationVariable459", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_TargetEdgeViewCreationVariable459"):
                opp_val = getattr(value, "tool_TargetEdgeViewCreationVariable459", None)
                setattr(value, "tool_TargetEdgeViewCreationVariable459", self)

    def getMappings(self) -> str:
        # TODO: Implement getMappings method
        pass

class diagram_tool_NodeCreationDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, diagram_tool_NodeCreationDescription386: "tool_NodeCreationVariable" = None, diagram_tool_NodeCreationDescription388: "tool_ContainerViewVariable" = None, diagram_tool_NodeCreationDescription390: "tool_InitialNodeCreationOperation" = None, diagram_tool_NodeCreationDescription392: set["AbstractNodeMapping"] = None, diagram_tool_NodeCreationDescription: set["NodeMapping"] = None):
        self.iconPath = iconPath
        self.diagram_tool_NodeCreationDescription386 = diagram_tool_NodeCreationDescription386
        self.diagram_tool_NodeCreationDescription388 = diagram_tool_NodeCreationDescription388
        self.diagram_tool_NodeCreationDescription390 = diagram_tool_NodeCreationDescription390
        self.diagram_tool_NodeCreationDescription392 = diagram_tool_NodeCreationDescription392 if diagram_tool_NodeCreationDescription392 is not None else set()
        self.diagram_tool_NodeCreationDescription = diagram_tool_NodeCreationDescription if diagram_tool_NodeCreationDescription is not None else set()
        
    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

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
                if hasattr(item, "NodeMapping384"):
                    opp_val = getattr(item, "NodeMapping384", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping384", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping384"):
                    opp_val = getattr(item, "NodeMapping384", None)
                    
                    setattr(item, "NodeMapping384", self)
                    

    @property
    def diagram_tool_NodeCreationDescription390(self):
        return self.__diagram_tool_NodeCreationDescription390

    @diagram_tool_NodeCreationDescription390.setter
    def diagram_tool_NodeCreationDescription390(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription390", None)
        self.__diagram_tool_NodeCreationDescription390 = value
        
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
    def diagram_tool_NodeCreationDescription386(self):
        return self.__diagram_tool_NodeCreationDescription386

    @diagram_tool_NodeCreationDescription386.setter
    def diagram_tool_NodeCreationDescription386(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription386", None)
        self.__diagram_tool_NodeCreationDescription386 = value
        
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

    @property
    def diagram_tool_NodeCreationDescription392(self):
        return self.__diagram_tool_NodeCreationDescription392

    @diagram_tool_NodeCreationDescription392.setter
    def diagram_tool_NodeCreationDescription392(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription392", None)
        self.__diagram_tool_NodeCreationDescription392 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractNodeMapping393"):
                    opp_val = getattr(item, "AbstractNodeMapping393", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractNodeMapping393", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractNodeMapping393"):
                    opp_val = getattr(item, "AbstractNodeMapping393", None)
                    
                    setattr(item, "AbstractNodeMapping393", self)
                    

    @property
    def diagram_tool_NodeCreationDescription388(self):
        return self.__diagram_tool_NodeCreationDescription388

    @diagram_tool_NodeCreationDescription388.setter
    def diagram_tool_NodeCreationDescription388(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription388", None)
        self.__diagram_tool_NodeCreationDescription388 = value
        
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

class tool_ToolGroup:

    pass
class diagram_tool_ToolGroupExtension:

    pass
class ToolEntry:

    pass
class diagram_tool_ToolGroup(ToolEntry):

    pass
class diagram_tool_EdgeCreationDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, connectionStartPrecondition: str, diagram_tool_EdgeCreationDescription401: "tool_SourceEdgeViewCreationVariable" = None, diagram_tool_EdgeCreationDescription403: "tool_TargetEdgeViewCreationVariable" = None, diagram_tool_EdgeCreationDescription405: "tool_InitEdgeCreationOperation" = None, diagram_tool_EdgeCreationDescription407: set["DiagramElementMapping"] = None, diagram_tool_EdgeCreationDescription410: set["DiagramElementMapping"] = None, diagram_tool_EdgeCreationDescription: set["EdgeMapping"] = None, diagram_tool_EdgeCreationDescription397: "tool_SourceEdgeCreationVariable" = None, diagram_tool_EdgeCreationDescription399: "tool_TargetEdgeCreationVariable" = None):
        self.iconPath = iconPath
        self.connectionStartPrecondition = connectionStartPrecondition
        self.diagram_tool_EdgeCreationDescription401 = diagram_tool_EdgeCreationDescription401
        self.diagram_tool_EdgeCreationDescription403 = diagram_tool_EdgeCreationDescription403
        self.diagram_tool_EdgeCreationDescription405 = diagram_tool_EdgeCreationDescription405
        self.diagram_tool_EdgeCreationDescription407 = diagram_tool_EdgeCreationDescription407 if diagram_tool_EdgeCreationDescription407 is not None else set()
        self.diagram_tool_EdgeCreationDescription410 = diagram_tool_EdgeCreationDescription410 if diagram_tool_EdgeCreationDescription410 is not None else set()
        self.diagram_tool_EdgeCreationDescription = diagram_tool_EdgeCreationDescription if diagram_tool_EdgeCreationDescription is not None else set()
        self.diagram_tool_EdgeCreationDescription397 = diagram_tool_EdgeCreationDescription397
        self.diagram_tool_EdgeCreationDescription399 = diagram_tool_EdgeCreationDescription399
        
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
    def diagram_tool_EdgeCreationDescription401(self):
        return self.__diagram_tool_EdgeCreationDescription401

    @diagram_tool_EdgeCreationDescription401.setter
    def diagram_tool_EdgeCreationDescription401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription401", None)
        self.__diagram_tool_EdgeCreationDescription401 = value
        
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
    def diagram_tool_EdgeCreationDescription403(self):
        return self.__diagram_tool_EdgeCreationDescription403

    @diagram_tool_EdgeCreationDescription403.setter
    def diagram_tool_EdgeCreationDescription403(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription403", None)
        self.__diagram_tool_EdgeCreationDescription403 = value
        
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
    def diagram_tool_EdgeCreationDescription407(self):
        return self.__diagram_tool_EdgeCreationDescription407

    @diagram_tool_EdgeCreationDescription407.setter
    def diagram_tool_EdgeCreationDescription407(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription407", None)
        self.__diagram_tool_EdgeCreationDescription407 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping408"):
                    opp_val = getattr(item, "DiagramElementMapping408", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping408", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping408"):
                    opp_val = getattr(item, "DiagramElementMapping408", None)
                    
                    setattr(item, "DiagramElementMapping408", self)
                    

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
                if hasattr(item, "EdgeMapping395"):
                    opp_val = getattr(item, "EdgeMapping395", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping395", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping395"):
                    opp_val = getattr(item, "EdgeMapping395", None)
                    
                    setattr(item, "EdgeMapping395", self)
                    

    @property
    def diagram_tool_EdgeCreationDescription399(self):
        return self.__diagram_tool_EdgeCreationDescription399

    @diagram_tool_EdgeCreationDescription399.setter
    def diagram_tool_EdgeCreationDescription399(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription399", None)
        self.__diagram_tool_EdgeCreationDescription399 = value
        
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
    def diagram_tool_EdgeCreationDescription410(self):
        return self.__diagram_tool_EdgeCreationDescription410

    @diagram_tool_EdgeCreationDescription410.setter
    def diagram_tool_EdgeCreationDescription410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription410", None)
        self.__diagram_tool_EdgeCreationDescription410 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping411"):
                    opp_val = getattr(item, "DiagramElementMapping411", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping411", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping411"):
                    opp_val = getattr(item, "DiagramElementMapping411", None)
                    
                    setattr(item, "DiagramElementMapping411", self)
                    

    @property
    def diagram_tool_EdgeCreationDescription405(self):
        return self.__diagram_tool_EdgeCreationDescription405

    @diagram_tool_EdgeCreationDescription405.setter
    def diagram_tool_EdgeCreationDescription405(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription405", None)
        self.__diagram_tool_EdgeCreationDescription405 = value
        
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
    def diagram_tool_EdgeCreationDescription397(self):
        return self.__diagram_tool_EdgeCreationDescription397

    @diagram_tool_EdgeCreationDescription397.setter
    def diagram_tool_EdgeCreationDescription397(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription397", None)
        self.__diagram_tool_EdgeCreationDescription397 = value
        
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

    def getBestMapping(self, createdElements: str, source: EdgeTarget, target: EdgeTarget) -> str:
        # TODO: Implement getBestMapping method
        pass

class tool_InitialNodeCreationOperation:

    pass
class tool_ContainerViewVariable:

    pass
class tool_NodeCreationVariable:

    pass
class BasicLabelStyleDescription:

    pass
class diagram_style_BeginLabelStyleDescription(BasicLabelStyleDescription):

    pass
class style_EndLabelStyleDescription:

    pass
class style_CenterLabelStyleDescription:

    pass
class style_BeginLabelStyleDescription:

    pass
class tool_ToolGroupExtension:

    pass
class tool_PopupMenu:

    pass
class tool_ToolEntry:

    pass
class EdgeStyleDescription:

    pass
class diagram_style_BracketEdgeStyleDescription(EdgeStyleDescription):

    pass
class diagram_style_EndLabelStyleDescription(BasicLabelStyleDescription):

    pass
class diagram_style_CenterLabelStyleDescription(BasicLabelStyleDescription):

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

    def __init__(self, minValueExpression: str, maxValueExpression: str, valueExpression: str, label: str, diagram_style_GaugeSectionDescription: "ColorDescription" = None, diagram_style_GaugeSectionDescription347: "ColorDescription" = None):
        self.minValueExpression = minValueExpression
        self.maxValueExpression = maxValueExpression
        self.valueExpression = valueExpression
        self.label = label
        self.diagram_style_GaugeSectionDescription = diagram_style_GaugeSectionDescription
        self.diagram_style_GaugeSectionDescription347 = diagram_style_GaugeSectionDescription347
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def maxValueExpression(self) -> str:
        return self.__maxValueExpression

    @maxValueExpression.setter
    def maxValueExpression(self, maxValueExpression: str):
        self.__maxValueExpression = maxValueExpression

    @property
    def valueExpression(self) -> str:
        return self.__valueExpression

    @valueExpression.setter
    def valueExpression(self, valueExpression: str):
        self.__valueExpression = valueExpression

    @property
    def minValueExpression(self) -> str:
        return self.__minValueExpression

    @minValueExpression.setter
    def minValueExpression(self, minValueExpression: str):
        self.__minValueExpression = minValueExpression

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
            if hasattr(old_value, "ColorDescription345"):
                opp_val = getattr(old_value, "ColorDescription345", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription345", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription345"):
                opp_val = getattr(value, "ColorDescription345", None)
                setattr(value, "ColorDescription345", self)

    @property
    def diagram_style_GaugeSectionDescription347(self):
        return self.__diagram_style_GaugeSectionDescription347

    @diagram_style_GaugeSectionDescription347.setter
    def diagram_style_GaugeSectionDescription347(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_GaugeSectionDescription__diagram_style_GaugeSectionDescription347", None)
        self.__diagram_style_GaugeSectionDescription347 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription348"):
                opp_val = getattr(old_value, "ColorDescription348", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription348", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription348"):
                opp_val = getattr(value, "ColorDescription348", None)
                setattr(value, "ColorDescription348", self)

class style_GaugeSectionDescription:

    pass
class tool_ContainerDropDescription:

    pass
class diagram_description_DragAndDropTargetDescription(ABC):

    pass
class Customization:

    pass
class NodeStyleDescription:

    pass
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
            if hasattr(old_value, "ColorDescription342"):
                opp_val = getattr(old_value, "ColorDescription342", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription342", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription342"):
                opp_val = getattr(value, "ColorDescription342", None)
                setattr(value, "ColorDescription342", self)

class diagram_style_NoteDescription(NodeStyleDescription):

    pass
class diagram_style_SquareDescription(NodeStyleDescription):

    def __init__(self, width: str, height: str, diagram_style_SquareDescription: "ColorDescription" = None):
        self.width = width
        self.height = height
        self.diagram_style_SquareDescription = diagram_style_SquareDescription
        
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
    def diagram_style_SquareDescription(self):
        return self.__diagram_style_SquareDescription

    @diagram_style_SquareDescription.setter
    def diagram_style_SquareDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_SquareDescription__diagram_style_SquareDescription", None)
        self.__diagram_style_SquareDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription332"):
                opp_val = getattr(old_value, "ColorDescription332", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription332", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription332"):
                opp_val = getattr(value, "ColorDescription332", None)
                setattr(value, "ColorDescription332", self)

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
            if hasattr(old_value, "ColorDescription334"):
                opp_val = getattr(old_value, "ColorDescription334", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription334", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription334"):
                opp_val = getattr(value, "ColorDescription334", None)
                setattr(value, "ColorDescription334", self)

class diagram_style_EllipseNodeDescription(NodeStyleDescription):

    def __init__(self, horizontalDiameterComputationExpression: str, verticalDiameterComputationExpression: str, diagram_style_EllipseNodeDescription: "ColorDescription" = None):
        self.horizontalDiameterComputationExpression = horizontalDiameterComputationExpression
        self.verticalDiameterComputationExpression = verticalDiameterComputationExpression
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
            if hasattr(old_value, "ColorDescription336"):
                opp_val = getattr(old_value, "ColorDescription336", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription336", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription336"):
                opp_val = getattr(value, "ColorDescription336", None)
                setattr(value, "ColorDescription336", self)

class diagram_style_BundledImageDescription(NodeStyleDescription):

    def __init__(self, shape: str, diagram_style_BundledImageDescription: "ColorDescription" = None):
        self.shape = shape
        self.diagram_style_BundledImageDescription = diagram_style_BundledImageDescription
        
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
            if hasattr(old_value, "ColorDescription338"):
                opp_val = getattr(old_value, "ColorDescription338", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription338", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription338"):
                opp_val = getattr(value, "ColorDescription338", None)
                setattr(value, "ColorDescription338", self)

class diagram_style_CustomStyleDescription(NodeStyleDescription):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class style_TooltipStyleDescription:

    pass
class style_LabelStyleDescription:

    pass
class style_BorderedStyleDescription:

    pass
class diagram_style_ContainerStyleDescription(style_RoundedCornerStyleDescription, style_LabelStyleDescription, style_BorderedStyleDescription, style_TooltipStyleDescription):

    def __init__(self, roundedCorner: bool):
        self.roundedCorner = roundedCorner
        
    @property
    def roundedCorner(self) -> bool:
        return self.__roundedCorner

    @roundedCorner.setter
    def roundedCorner(self, roundedCorner: bool):
        self.__roundedCorner = roundedCorner

class ColorDescription:

    pass
class StyleDescription:

    pass
class diagram_style_EdgeStyleDescription(StyleDescription):

    def __init__(self, lineStyle: str, sourceArrow: str, targetArrow: str, sizeComputationExpression: str, routingStyle: str, foldingStyle: str, diagram_style_EdgeStyleDescription: "ColorDescription" = None, diagram_style_EdgeStyleDescription361: "style_BeginLabelStyleDescription" = None, diagram_style_EdgeStyleDescription363: "style_CenterLabelStyleDescription" = None, diagram_style_EdgeStyleDescription365: "style_EndLabelStyleDescription" = None):
        self.lineStyle = lineStyle
        self.sourceArrow = sourceArrow
        self.targetArrow = targetArrow
        self.sizeComputationExpression = sizeComputationExpression
        self.routingStyle = routingStyle
        self.foldingStyle = foldingStyle
        self.diagram_style_EdgeStyleDescription = diagram_style_EdgeStyleDescription
        self.diagram_style_EdgeStyleDescription361 = diagram_style_EdgeStyleDescription361
        self.diagram_style_EdgeStyleDescription363 = diagram_style_EdgeStyleDescription363
        self.diagram_style_EdgeStyleDescription365 = diagram_style_EdgeStyleDescription365
        
    @property
    def sourceArrow(self) -> str:
        return self.__sourceArrow

    @sourceArrow.setter
    def sourceArrow(self, sourceArrow: str):
        self.__sourceArrow = sourceArrow

    @property
    def routingStyle(self) -> str:
        return self.__routingStyle

    @routingStyle.setter
    def routingStyle(self, routingStyle: str):
        self.__routingStyle = routingStyle

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
    def sizeComputationExpression(self) -> str:
        return self.__sizeComputationExpression

    @sizeComputationExpression.setter
    def sizeComputationExpression(self, sizeComputationExpression: str):
        self.__sizeComputationExpression = sizeComputationExpression

    @property
    def targetArrow(self) -> str:
        return self.__targetArrow

    @targetArrow.setter
    def targetArrow(self, targetArrow: str):
        self.__targetArrow = targetArrow

    @property
    def diagram_style_EdgeStyleDescription361(self):
        return self.__diagram_style_EdgeStyleDescription361

    @diagram_style_EdgeStyleDescription361.setter
    def diagram_style_EdgeStyleDescription361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription361", None)
        self.__diagram_style_EdgeStyleDescription361 = value
        
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
    def diagram_style_EdgeStyleDescription363(self):
        return self.__diagram_style_EdgeStyleDescription363

    @diagram_style_EdgeStyleDescription363.setter
    def diagram_style_EdgeStyleDescription363(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription363", None)
        self.__diagram_style_EdgeStyleDescription363 = value
        
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
    def diagram_style_EdgeStyleDescription365(self):
        return self.__diagram_style_EdgeStyleDescription365

    @diagram_style_EdgeStyleDescription365.setter
    def diagram_style_EdgeStyleDescription365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription365", None)
        self.__diagram_style_EdgeStyleDescription365 = value
        
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
    def diagram_style_EdgeStyleDescription(self):
        return self.__diagram_style_EdgeStyleDescription

    @diagram_style_EdgeStyleDescription.setter
    def diagram_style_EdgeStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription", None)
        self.__diagram_style_EdgeStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription359"):
                opp_val = getattr(old_value, "ColorDescription359", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription359", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription359"):
                opp_val = getattr(value, "ColorDescription359", None)
                setattr(value, "ColorDescription359", self)

class diagram_style_RoundedCornerStyleDescription(StyleDescription):

    def __init__(self, arcWidth: str, arcHeight: str):
        self.arcWidth = arcWidth
        self.arcHeight = arcHeight
        
    @property
    def arcHeight(self) -> str:
        return self.__arcHeight

    @arcHeight.setter
    def arcHeight(self, arcHeight: str):
        self.__arcHeight = arcHeight

    @property
    def arcWidth(self) -> str:
        return self.__arcWidth

    @arcWidth.setter
    def arcWidth(self, arcWidth: str):
        self.__arcWidth = arcWidth

class diagram_style_BorderedStyleDescription(StyleDescription):

    def __init__(self, borderSizeComputationExpression: str, diagram_style_BorderedStyleDescription: "ColorDescription" = None):
        self.borderSizeComputationExpression = borderSizeComputationExpression
        self.diagram_style_BorderedStyleDescription = diagram_style_BorderedStyleDescription
        
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

class description_EndUserDocumentedElement:

    pass
class DecorationDescription:

    pass
class diagram_description_MappingBasedDecoration(DecorationDescription):

    pass
class DecorationDescriptionsSet:

    pass
class description_IdentifiedElement:

    pass
class diagram_description_IEdgeMapping(ABC):

    def __init__(self):
        
    def getBestStyle(self, modelElement: str, viewVariable: str, containerVariable: str) -> EdgeStyle:
        # TODO: Implement getBestStyle method
        pass

class DocumentedElement:

    pass
class diagram_concern_ConcernSet(DocumentedElement):

    pass
class diagram_description_Layout(DocumentedElement):

    pass
class ConditionalStyleDescription:

    pass
class diagram_description_ConditionalContainerStyleDescription(ConditionalStyleDescription):

    pass
class diagram_description_ConditionalEdgeStyleDescription(ConditionalStyleDescription):

    pass
class diagram_description_ConditionalNodeStyleDescription(ConditionalStyleDescription):

    pass
class AbstractNodeMapping:

    pass
class tool_ReconnectEdgeDescription:

    pass
class ConditionalEdgeStyleDescription:

    pass
class style_EdgeStyleDescription:

    pass
class description_AbstractMappingImport:

    pass
class description_NodeMapping:

    pass
class diagram_description_NodeMappingImport(description_NodeMapping, description_AbstractMappingImport):

    pass
class ConditionalContainerStyleDescription:

    pass
class style_ContainerStyleDescription:

    pass
class diagram_style_ShapeContainerStyleDescription(style_ContainerStyleDescription, style_SizeComputationContainerStyleDescription):

    def __init__(self, shape: str, diagram_style_ShapeContainerStyleDescription: "ColorDescription" = None, style_ContainerStyleDescription294: "diagram_description_ConditionalContainerStyleDescription", style_ContainerStyleDescription: "diagram_description_ContainerMapping"):
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
            if hasattr(old_value, "ColorDescription357"):
                opp_val = getattr(old_value, "ColorDescription357", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription357", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription357"):
                opp_val = getattr(value, "ColorDescription357", None)
                setattr(value, "ColorDescription357", self)

class diagram_style_FlatContainerStyleDescription(style_ContainerStyleDescription, style_SizeComputationContainerStyleDescription):

    def __init__(self, backgroundStyle: str, diagram_style_FlatContainerStyleDescription: "ColorDescription" = None, diagram_style_FlatContainerStyleDescription352: "ColorDescription" = None, diagram_style_FlatContainerStyleDescription355: "style_LabelBorderStyleDescription" = None, style_ContainerStyleDescription294: "diagram_description_ConditionalContainerStyleDescription", style_ContainerStyleDescription: "diagram_description_ContainerMapping"):
        self.backgroundStyle = backgroundStyle
        self.diagram_style_FlatContainerStyleDescription = diagram_style_FlatContainerStyleDescription
        self.diagram_style_FlatContainerStyleDescription352 = diagram_style_FlatContainerStyleDescription352
        self.diagram_style_FlatContainerStyleDescription355 = diagram_style_FlatContainerStyleDescription355
        
    @property
    def backgroundStyle(self) -> str:
        return self.__backgroundStyle

    @backgroundStyle.setter
    def backgroundStyle(self, backgroundStyle: str):
        self.__backgroundStyle = backgroundStyle

    @property
    def diagram_style_FlatContainerStyleDescription355(self):
        return self.__diagram_style_FlatContainerStyleDescription355

    @diagram_style_FlatContainerStyleDescription355.setter
    def diagram_style_FlatContainerStyleDescription355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_FlatContainerStyleDescription__diagram_style_FlatContainerStyleDescription355", None)
        self.__diagram_style_FlatContainerStyleDescription355 = value
        
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
    def diagram_style_FlatContainerStyleDescription352(self):
        return self.__diagram_style_FlatContainerStyleDescription352

    @diagram_style_FlatContainerStyleDescription352.setter
    def diagram_style_FlatContainerStyleDescription352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_FlatContainerStyleDescription__diagram_style_FlatContainerStyleDescription352", None)
        self.__diagram_style_FlatContainerStyleDescription352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription353"):
                opp_val = getattr(old_value, "ColorDescription353", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription353", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription353"):
                opp_val = getattr(value, "ColorDescription353", None)
                setattr(value, "ColorDescription353", self)

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
            if hasattr(old_value, "ColorDescription350"):
                opp_val = getattr(old_value, "ColorDescription350", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription350", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription350"):
                opp_val = getattr(value, "ColorDescription350", None)
                setattr(value, "ColorDescription350", self)

class description_IEdgeMapping:

    pass
class description_ContainerMapping:

    pass
class diagram_description_ContainerMappingImport(description_ContainerMapping, description_AbstractMappingImport):

    pass
class ConditionalNodeStyleDescription:

    pass
class style_NodeStyleDescription:

    pass
class diagram_style_WorkspaceImageDescription(style_ContainerStyleDescription, style_NodeStyleDescription):

    def __init__(self, workspacePath: str, style_NodeStyleDescription290: "diagram_description_ConditionalNodeStyleDescription", style_NodeStyleDescription: "diagram_description_NodeMapping", style_ContainerStyleDescription294: "diagram_description_ConditionalContainerStyleDescription", style_ContainerStyleDescription: "diagram_description_ContainerMapping"):
        self.workspacePath = workspacePath
        
    @property
    def workspacePath(self) -> str:
        return self.__workspacePath

    @workspacePath.setter
    def workspacePath(self, workspacePath: str):
        self.__workspacePath = workspacePath

class description_DiagramElementMapping:

    pass
class tool_DoubleClickDescription:

    pass
class description_AbstractNodeMapping:

    pass
class tool_DeleteElementDescription:

    pass
class tool_DirectEditLabel:

    pass
class RepresentationExtensionDescription:

    pass
class diagram_description_DiagramExtensionDescription(RepresentationExtensionDescription):

    pass
class description_RepresentationElementMapping:

    pass
class description_DiagramDescription:

    pass
class description_RepresentationImportDescription:

    pass
class diagram_description_DiagramImportDescription(description_DiagramDescription, description_RepresentationImportDescription):

    pass
class tool_ToolSection:

    pass
class EdgeMappingImport:

    pass
class tool_AbstractToolDescription:

    pass
class AdditionalLayer:

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
                if hasattr(item, "AbstractNodeMapping296"):
                    opp_val = getattr(item, "AbstractNodeMapping296", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractNodeMapping296", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractNodeMapping296"):
                    opp_val = getattr(item, "AbstractNodeMapping296", None)
                    
                    setattr(item, "AbstractNodeMapping296", self)
                    

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
class description_PasteTargetDescription:

    pass
class diagram_description_DiagramElementMapping(description_RepresentationElementMapping, description_PasteTargetDescription):

    def __init__(self, preconditionExpression: str, semanticCandidatesExpression: str, createElements: bool, semanticElements: str, synchronizationLock: bool, diagram_description_DiagramElementMapping236: "tool_DirectEditLabel" = None, diagram_description_DiagramElementMapping: "tool_DeleteElementDescription" = None, tool: "tool_DoubleClickDescription" = None):
        self.preconditionExpression = preconditionExpression
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.createElements = createElements
        self.semanticElements = semanticElements
        self.synchronizationLock = synchronizationLock
        self.diagram_description_DiagramElementMapping236 = diagram_description_DiagramElementMapping236
        self.diagram_description_DiagramElementMapping = diagram_description_DiagramElementMapping
        self.tool = tool
        
    @property
    def createElements(self) -> bool:
        return self.__createElements

    @createElements.setter
    def createElements(self, createElements: bool):
        self.__createElements = createElements

    @property
    def synchronizationLock(self) -> bool:
        return self.__synchronizationLock

    @synchronizationLock.setter
    def synchronizationLock(self, synchronizationLock: bool):
        self.__synchronizationLock = synchronizationLock

    @property
    def semanticElements(self) -> str:
        return self.__semanticElements

    @semanticElements.setter
    def semanticElements(self, semanticElements: str):
        self.__semanticElements = semanticElements

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
    def diagram_description_DiagramElementMapping236(self):
        return self.__diagram_description_DiagramElementMapping236

    @diagram_description_DiagramElementMapping236.setter
    def diagram_description_DiagramElementMapping236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramElementMapping__diagram_description_DiagramElementMapping236", None)
        self.__diagram_description_DiagramElementMapping236 = value
        
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

    def isFrom(self, element: str) -> bool:
        # TODO: Implement isFrom method
        pass

    def getAllMappings(self) -> str:
        # TODO: Implement getAllMappings method
        pass

    def checkPrecondition(self, container: str, modelElement: str, containerView: str) -> bool:
        # TODO: Implement checkPrecondition method
        pass

class description_RepresentationDescription:

    pass
class description_DragAndDropTargetDescription:

    pass
class diagram_description_NodeMapping(description_AbstractNodeMapping, description_DragAndDropTargetDescription):

    def __init__(self, diagram_description_NodeMapping: "style_NodeStyleDescription" = None, diagram_description_NodeMapping245: set["ConditionalNodeStyleDescription"] = None):
        self.diagram_description_NodeMapping = diagram_description_NodeMapping
        self.diagram_description_NodeMapping245 = diagram_description_NodeMapping245 if diagram_description_NodeMapping245 is not None else set()
        
    @property
    def diagram_description_NodeMapping245(self):
        return self.__diagram_description_NodeMapping245

    @diagram_description_NodeMapping245.setter
    def diagram_description_NodeMapping245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_NodeMapping__diagram_description_NodeMapping245", None)
        self.__diagram_description_NodeMapping245 = value if value is not None else set()
        
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

    def getNodesCandidates(self, containerView: str, container: str, semanticOrigin: str) -> str:
        # TODO: Implement getNodesCandidates method
        pass

    def getNodesCandidates(self, semanticOrigin: str, container: str) -> str:
        # TODO: Implement getNodesCandidates method
        pass

    def updateNode(self, node: str):
        # TODO: Implement updateNode method
        pass

    def createNode(self, viewPoint: DDiagram, container: str, modelElement: str) -> str:
        # TODO: Implement createNode method
        pass

    def updateListElement(self, listElement: str):
        # TODO: Implement updateListElement method
        pass

class diagram_description_ContainerMapping(description_AbstractNodeMapping, description_DragAndDropTargetDescription):

    def __init__(self, childrenPresentation: str, diagram_description_ContainerMapping: set["NodeMapping"] = None, diagram_description_ContainerMapping249: set["NodeMapping"] = None, diagram_description_ContainerMapping252: set["NodeMapping"] = None, diagram_description_ContainerMapping255: set["ContainerMapping"] = None, diagram_description_ContainerMapping258: set["ContainerMapping"] = None, diagram_description_ContainerMapping261: set["ContainerMapping"] = None, diagram_description_ContainerMapping264: "style_ContainerStyleDescription" = None, diagram_description_ContainerMapping266: set["ConditionalContainerStyleDescription"] = None):
        self.childrenPresentation = childrenPresentation
        self.diagram_description_ContainerMapping = diagram_description_ContainerMapping if diagram_description_ContainerMapping is not None else set()
        self.diagram_description_ContainerMapping249 = diagram_description_ContainerMapping249 if diagram_description_ContainerMapping249 is not None else set()
        self.diagram_description_ContainerMapping252 = diagram_description_ContainerMapping252 if diagram_description_ContainerMapping252 is not None else set()
        self.diagram_description_ContainerMapping255 = diagram_description_ContainerMapping255 if diagram_description_ContainerMapping255 is not None else set()
        self.diagram_description_ContainerMapping258 = diagram_description_ContainerMapping258 if diagram_description_ContainerMapping258 is not None else set()
        self.diagram_description_ContainerMapping261 = diagram_description_ContainerMapping261 if diagram_description_ContainerMapping261 is not None else set()
        self.diagram_description_ContainerMapping264 = diagram_description_ContainerMapping264
        self.diagram_description_ContainerMapping266 = diagram_description_ContainerMapping266 if diagram_description_ContainerMapping266 is not None else set()
        
    @property
    def childrenPresentation(self) -> str:
        return self.__childrenPresentation

    @childrenPresentation.setter
    def childrenPresentation(self, childrenPresentation: str):
        self.__childrenPresentation = childrenPresentation

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
                if hasattr(item, "NodeMapping247"):
                    opp_val = getattr(item, "NodeMapping247", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping247"):
                    opp_val = getattr(item, "NodeMapping247", None)
                    
                    setattr(item, "NodeMapping247", self)
                    

    @property
    def diagram_description_ContainerMapping249(self):
        return self.__diagram_description_ContainerMapping249

    @diagram_description_ContainerMapping249.setter
    def diagram_description_ContainerMapping249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping249", None)
        self.__diagram_description_ContainerMapping249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping250"):
                    opp_val = getattr(item, "NodeMapping250", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping250"):
                    opp_val = getattr(item, "NodeMapping250", None)
                    
                    setattr(item, "NodeMapping250", self)
                    

    @property
    def diagram_description_ContainerMapping252(self):
        return self.__diagram_description_ContainerMapping252

    @diagram_description_ContainerMapping252.setter
    def diagram_description_ContainerMapping252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping252", None)
        self.__diagram_description_ContainerMapping252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping253"):
                    opp_val = getattr(item, "NodeMapping253", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping253", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping253"):
                    opp_val = getattr(item, "NodeMapping253", None)
                    
                    setattr(item, "NodeMapping253", self)
                    

    @property
    def diagram_description_ContainerMapping266(self):
        return self.__diagram_description_ContainerMapping266

    @diagram_description_ContainerMapping266.setter
    def diagram_description_ContainerMapping266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping266", None)
        self.__diagram_description_ContainerMapping266 = value if value is not None else set()
        
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
                    

    @property
    def diagram_description_ContainerMapping255(self):
        return self.__diagram_description_ContainerMapping255

    @diagram_description_ContainerMapping255.setter
    def diagram_description_ContainerMapping255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping255", None)
        self.__diagram_description_ContainerMapping255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping256"):
                    opp_val = getattr(item, "ContainerMapping256", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping256"):
                    opp_val = getattr(item, "ContainerMapping256", None)
                    
                    setattr(item, "ContainerMapping256", self)
                    

    @property
    def diagram_description_ContainerMapping261(self):
        return self.__diagram_description_ContainerMapping261

    @diagram_description_ContainerMapping261.setter
    def diagram_description_ContainerMapping261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping261", None)
        self.__diagram_description_ContainerMapping261 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping262"):
                    opp_val = getattr(item, "ContainerMapping262", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping262", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping262"):
                    opp_val = getattr(item, "ContainerMapping262", None)
                    
                    setattr(item, "ContainerMapping262", self)
                    

    @property
    def diagram_description_ContainerMapping264(self):
        return self.__diagram_description_ContainerMapping264

    @diagram_description_ContainerMapping264.setter
    def diagram_description_ContainerMapping264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping264", None)
        self.__diagram_description_ContainerMapping264 = value
        
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
    def diagram_description_ContainerMapping258(self):
        return self.__diagram_description_ContainerMapping258

    @diagram_description_ContainerMapping258.setter
    def diagram_description_ContainerMapping258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping258", None)
        self.__diagram_description_ContainerMapping258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping259"):
                    opp_val = getattr(item, "ContainerMapping259", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping259"):
                    opp_val = getattr(item, "ContainerMapping259", None)
                    
                    setattr(item, "ContainerMapping259", self)
                    

    def getBestStyle(self, containerVariable: str, modelElement: str, viewVariable: str) -> ContainerStyle:
        # TODO: Implement getBestStyle method
        pass

class diagram_description_DiagramDescription(description_PasteTargetDescription, description_DragAndDropTargetDescription, description_RepresentationDescription):

    def __init__(self, rootExpression: str, domainClass: str, preconditionExpression: str, enablePopupBars: bool, diagram_description_DiagramDescription: set["filter_FilterDescription"] = None, diagram_description_DiagramDescription172: set["EdgeMapping"] = None, diagram_description_DiagramDescription174: set["NodeMapping"] = None, diagram_description_DiagramDescription177: set["ContainerMapping"] = None, diagram_description_DiagramDescription180: "validation_ValidationSet" = None, diagram_description_DiagramDescription182: "concern_ConcernSet" = None, diagram_description_DiagramDescription186: "concern_ConcernDescription" = None, diagram_description_DiagramDescription189: "tool_RepresentationCreationDescription" = None, diagram_description_DiagramDescription191: "Layout" = None, diagram_description_DiagramDescription193: "tool_InitialOperation" = None, diagram_description_DiagramDescription195: "Layer" = None, diagram_description_DiagramDescription198: set["AdditionalLayer"] = None, diagram_description_DiagramDescription200: set["Layer"] = None, diagram_description_DiagramDescription184: set["tool_AbstractToolDescription"] = None, diagram_description_DiagramDescription212: set["EdgeMappingImport"] = None, diagram_description_DiagramDescription214: set["ContainerMapping"] = None, diagram_description_DiagramDescription217: set["DiagramElementMapping"] = None, diagram_description_DiagramDescription220: "tool_ToolSection" = None, diagram_description_DiagramDescription222: set["tool_AbstractToolDescription"] = None, diagram_description_DiagramDescription203: set["tool_AbstractToolDescription"] = None, diagram_description_DiagramDescription206: set["NodeMapping"] = None, diagram_description_DiagramDescription209: set["EdgeMapping"] = None):
        self.rootExpression = rootExpression
        self.domainClass = domainClass
        self.preconditionExpression = preconditionExpression
        self.enablePopupBars = enablePopupBars
        self.diagram_description_DiagramDescription = diagram_description_DiagramDescription if diagram_description_DiagramDescription is not None else set()
        self.diagram_description_DiagramDescription172 = diagram_description_DiagramDescription172 if diagram_description_DiagramDescription172 is not None else set()
        self.diagram_description_DiagramDescription174 = diagram_description_DiagramDescription174 if diagram_description_DiagramDescription174 is not None else set()
        self.diagram_description_DiagramDescription177 = diagram_description_DiagramDescription177 if diagram_description_DiagramDescription177 is not None else set()
        self.diagram_description_DiagramDescription180 = diagram_description_DiagramDescription180
        self.diagram_description_DiagramDescription182 = diagram_description_DiagramDescription182
        self.diagram_description_DiagramDescription186 = diagram_description_DiagramDescription186
        self.diagram_description_DiagramDescription189 = diagram_description_DiagramDescription189
        self.diagram_description_DiagramDescription191 = diagram_description_DiagramDescription191
        self.diagram_description_DiagramDescription193 = diagram_description_DiagramDescription193
        self.diagram_description_DiagramDescription195 = diagram_description_DiagramDescription195
        self.diagram_description_DiagramDescription198 = diagram_description_DiagramDescription198 if diagram_description_DiagramDescription198 is not None else set()
        self.diagram_description_DiagramDescription200 = diagram_description_DiagramDescription200 if diagram_description_DiagramDescription200 is not None else set()
        self.diagram_description_DiagramDescription184 = diagram_description_DiagramDescription184 if diagram_description_DiagramDescription184 is not None else set()
        self.diagram_description_DiagramDescription212 = diagram_description_DiagramDescription212 if diagram_description_DiagramDescription212 is not None else set()
        self.diagram_description_DiagramDescription214 = diagram_description_DiagramDescription214 if diagram_description_DiagramDescription214 is not None else set()
        self.diagram_description_DiagramDescription217 = diagram_description_DiagramDescription217 if diagram_description_DiagramDescription217 is not None else set()
        self.diagram_description_DiagramDescription220 = diagram_description_DiagramDescription220
        self.diagram_description_DiagramDescription222 = diagram_description_DiagramDescription222 if diagram_description_DiagramDescription222 is not None else set()
        self.diagram_description_DiagramDescription203 = diagram_description_DiagramDescription203 if diagram_description_DiagramDescription203 is not None else set()
        self.diagram_description_DiagramDescription206 = diagram_description_DiagramDescription206 if diagram_description_DiagramDescription206 is not None else set()
        self.diagram_description_DiagramDescription209 = diagram_description_DiagramDescription209 if diagram_description_DiagramDescription209 is not None else set()
        
    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

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
    def diagram_description_DiagramDescription217(self):
        return self.__diagram_description_DiagramDescription217

    @diagram_description_DiagramDescription217.setter
    def diagram_description_DiagramDescription217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription217", None)
        self.__diagram_description_DiagramDescription217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping218"):
                    opp_val = getattr(item, "DiagramElementMapping218", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping218"):
                    opp_val = getattr(item, "DiagramElementMapping218", None)
                    
                    setattr(item, "DiagramElementMapping218", self)
                    

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
                if hasattr(item, "filter_FilterDescription170"):
                    opp_val = getattr(item, "filter_FilterDescription170", None)
                    
                    if opp_val == self:
                        setattr(item, "filter_FilterDescription170", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filter_FilterDescription170"):
                    opp_val = getattr(item, "filter_FilterDescription170", None)
                    
                    setattr(item, "filter_FilterDescription170", self)
                    

    @property
    def diagram_description_DiagramDescription193(self):
        return self.__diagram_description_DiagramDescription193

    @diagram_description_DiagramDescription193.setter
    def diagram_description_DiagramDescription193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription193", None)
        self.__diagram_description_DiagramDescription193 = value
        
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
    def diagram_description_DiagramDescription220(self):
        return self.__diagram_description_DiagramDescription220

    @diagram_description_DiagramDescription220.setter
    def diagram_description_DiagramDescription220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription220", None)
        self.__diagram_description_DiagramDescription220 = value
        
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
    def diagram_description_DiagramDescription184(self):
        return self.__diagram_description_DiagramDescription184

    @diagram_description_DiagramDescription184.setter
    def diagram_description_DiagramDescription184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription184", None)
        self.__diagram_description_DiagramDescription184 = value if value is not None else set()
        
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
    def diagram_description_DiagramDescription212(self):
        return self.__diagram_description_DiagramDescription212

    @diagram_description_DiagramDescription212.setter
    def diagram_description_DiagramDescription212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription212", None)
        self.__diagram_description_DiagramDescription212 = value if value is not None else set()
        
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
    def diagram_description_DiagramDescription186(self):
        return self.__diagram_description_DiagramDescription186

    @diagram_description_DiagramDescription186.setter
    def diagram_description_DiagramDescription186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription186", None)
        self.__diagram_description_DiagramDescription186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "concern_ConcernDescription187"):
                opp_val = getattr(old_value, "concern_ConcernDescription187", None)
                if opp_val == self:
                    setattr(old_value, "concern_ConcernDescription187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "concern_ConcernDescription187"):
                opp_val = getattr(value, "concern_ConcernDescription187", None)
                setattr(value, "concern_ConcernDescription187", self)

    @property
    def diagram_description_DiagramDescription180(self):
        return self.__diagram_description_DiagramDescription180

    @diagram_description_DiagramDescription180.setter
    def diagram_description_DiagramDescription180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription180", None)
        self.__diagram_description_DiagramDescription180 = value
        
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
    def diagram_description_DiagramDescription189(self):
        return self.__diagram_description_DiagramDescription189

    @diagram_description_DiagramDescription189.setter
    def diagram_description_DiagramDescription189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription189", None)
        self.__diagram_description_DiagramDescription189 = value
        
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
    def diagram_description_DiagramDescription174(self):
        return self.__diagram_description_DiagramDescription174

    @diagram_description_DiagramDescription174.setter
    def diagram_description_DiagramDescription174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription174", None)
        self.__diagram_description_DiagramDescription174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping175"):
                    opp_val = getattr(item, "NodeMapping175", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping175"):
                    opp_val = getattr(item, "NodeMapping175", None)
                    
                    setattr(item, "NodeMapping175", self)
                    

    @property
    def diagram_description_DiagramDescription200(self):
        return self.__diagram_description_DiagramDescription200

    @diagram_description_DiagramDescription200.setter
    def diagram_description_DiagramDescription200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription200", None)
        self.__diagram_description_DiagramDescription200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Layer201"):
                    opp_val = getattr(item, "Layer201", None)
                    
                    if opp_val == self:
                        setattr(item, "Layer201", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Layer201"):
                    opp_val = getattr(item, "Layer201", None)
                    
                    setattr(item, "Layer201", self)
                    

    @property
    def diagram_description_DiagramDescription214(self):
        return self.__diagram_description_DiagramDescription214

    @diagram_description_DiagramDescription214.setter
    def diagram_description_DiagramDescription214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription214", None)
        self.__diagram_description_DiagramDescription214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping215"):
                    opp_val = getattr(item, "ContainerMapping215", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping215"):
                    opp_val = getattr(item, "ContainerMapping215", None)
                    
                    setattr(item, "ContainerMapping215", self)
                    

    @property
    def diagram_description_DiagramDescription209(self):
        return self.__diagram_description_DiagramDescription209

    @diagram_description_DiagramDescription209.setter
    def diagram_description_DiagramDescription209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription209", None)
        self.__diagram_description_DiagramDescription209 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMapping210"):
                    opp_val = getattr(item, "EdgeMapping210", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping210", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping210"):
                    opp_val = getattr(item, "EdgeMapping210", None)
                    
                    setattr(item, "EdgeMapping210", self)
                    

    @property
    def diagram_description_DiagramDescription206(self):
        return self.__diagram_description_DiagramDescription206

    @diagram_description_DiagramDescription206.setter
    def diagram_description_DiagramDescription206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription206", None)
        self.__diagram_description_DiagramDescription206 = value if value is not None else set()
        
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
    def diagram_description_DiagramDescription172(self):
        return self.__diagram_description_DiagramDescription172

    @diagram_description_DiagramDescription172.setter
    def diagram_description_DiagramDescription172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription172", None)
        self.__diagram_description_DiagramDescription172 = value if value is not None else set()
        
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
    def diagram_description_DiagramDescription177(self):
        return self.__diagram_description_DiagramDescription177

    @diagram_description_DiagramDescription177.setter
    def diagram_description_DiagramDescription177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription177", None)
        self.__diagram_description_DiagramDescription177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping178"):
                    opp_val = getattr(item, "ContainerMapping178", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping178", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping178"):
                    opp_val = getattr(item, "ContainerMapping178", None)
                    
                    setattr(item, "ContainerMapping178", self)
                    

    @property
    def diagram_description_DiagramDescription222(self):
        return self.__diagram_description_DiagramDescription222

    @diagram_description_DiagramDescription222.setter
    def diagram_description_DiagramDescription222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription222", None)
        self.__diagram_description_DiagramDescription222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription223"):
                    opp_val = getattr(item, "tool_AbstractToolDescription223", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription223"):
                    opp_val = getattr(item, "tool_AbstractToolDescription223", None)
                    
                    setattr(item, "tool_AbstractToolDescription223", self)
                    

    @property
    def diagram_description_DiagramDescription195(self):
        return self.__diagram_description_DiagramDescription195

    @diagram_description_DiagramDescription195.setter
    def diagram_description_DiagramDescription195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription195", None)
        self.__diagram_description_DiagramDescription195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Layer196"):
                opp_val = getattr(old_value, "Layer196", None)
                if opp_val == self:
                    setattr(old_value, "Layer196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Layer196"):
                opp_val = getattr(value, "Layer196", None)
                setattr(value, "Layer196", self)

    @property
    def diagram_description_DiagramDescription198(self):
        return self.__diagram_description_DiagramDescription198

    @diagram_description_DiagramDescription198.setter
    def diagram_description_DiagramDescription198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription198", None)
        self.__diagram_description_DiagramDescription198 = value if value is not None else set()
        
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
    def diagram_description_DiagramDescription191(self):
        return self.__diagram_description_DiagramDescription191

    @diagram_description_DiagramDescription191.setter
    def diagram_description_DiagramDescription191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription191", None)
        self.__diagram_description_DiagramDescription191 = value
        
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
    def diagram_description_DiagramDescription203(self):
        return self.__diagram_description_DiagramDescription203

    @diagram_description_DiagramDescription203.setter
    def diagram_description_DiagramDescription203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription203", None)
        self.__diagram_description_DiagramDescription203 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription204"):
                    opp_val = getattr(item, "tool_AbstractToolDescription204", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription204", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription204"):
                    opp_val = getattr(item, "tool_AbstractToolDescription204", None)
                    
                    setattr(item, "tool_AbstractToolDescription204", self)
                    

    @property
    def diagram_description_DiagramDescription182(self):
        return self.__diagram_description_DiagramDescription182

    @diagram_description_DiagramDescription182.setter
    def diagram_description_DiagramDescription182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription182", None)
        self.__diagram_description_DiagramDescription182 = value
        
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

    def createDiagram(self) -> str:
        # TODO: Implement createDiagram method
        pass

class diagram_DragAndDropTarget:

    def __init__(self):
        
    def getDragAndDropDescription(self) -> str:
        # TODO: Implement getDragAndDropDescription method
        pass

class concern_ConcernSet:

    pass
class validation_ValidationSet:

    pass
class EdgeMapping:

    pass
class EdgeStyle:

    pass
class diagram_BracketEdgeStyle(EdgeStyle):

    pass
class diagram_ContainerVariable2StyleDescription:

    pass
class diagram_ViewVariable2ContainerVariable:

    pass
class diagram_ModelElement2ViewVariable:

    pass
class diagram_DiagramElementMapping2ModelElement:

    pass
class style_StyleDescription:

    pass
class diagram_style_NodeStyleDescription(style_StyleDescription, style_LabelStyleDescription, style_BorderedStyleDescription, style_TooltipStyleDescription):

    def __init__(self, sizeComputationExpression: str, labelPosition: str, hideLabelByDefault: bool, resizeKind: str, style_StyleDescription168: "diagram_ContainerVariable2StyleDescription", style_StyleDescription: "diagram_ComputedStyleDescriptionRegistry"):
        self.sizeComputationExpression = sizeComputationExpression
        self.labelPosition = labelPosition
        self.hideLabelByDefault = hideLabelByDefault
        self.resizeKind = resizeKind
        
    @property
    def labelPosition(self) -> str:
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition

    @property
    def sizeComputationExpression(self) -> str:
        return self.__sizeComputationExpression

    @sizeComputationExpression.setter
    def sizeComputationExpression(self, sizeComputationExpression: str):
        self.__sizeComputationExpression = sizeComputationExpression

    @property
    def resizeKind(self) -> str:
        return self.__resizeKind

    @resizeKind.setter
    def resizeKind(self, resizeKind: str):
        self.__resizeKind = resizeKind

    @property
    def hideLabelByDefault(self) -> bool:
        return self.__hideLabelByDefault

    @hideLabelByDefault.setter
    def hideLabelByDefault(self, hideLabelByDefault: bool):
        self.__hideLabelByDefault = hideLabelByDefault

class diagram_ComputedStyleDescriptionRegistry:

    pass
class diagram_FilterVariableValue:

    pass
class BasicLabelStyle:

    pass
class CollapseFilter:

    pass
class diagram_IndirectlyCollapseFilter(CollapseFilter):

    pass
class diagram_EObject:

    pass
class filter_FilterVariable:

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
            if hasattr(old_value, "diagram_EdgeStyle132"):
                opp_val = getattr(old_value, "diagram_EdgeStyle132", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EdgeStyle132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EdgeStyle132"):
                opp_val = getattr(value, "diagram_EdgeStyle132", None)
                setattr(value, "diagram_EdgeStyle132", self)

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

    def setDescription(self, description: str):
        # TODO: Implement setDescription method
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
            if hasattr(old_value, "diagram_EdgeStyle130"):
                opp_val = getattr(old_value, "diagram_EdgeStyle130", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EdgeStyle130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EdgeStyle130"):
                opp_val = getattr(value, "diagram_EdgeStyle130", None)
                setattr(value, "diagram_EdgeStyle130", self)

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

    def setDescription(self, description: str):
        # TODO: Implement setDescription method
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
            if hasattr(old_value, "diagram_EdgeStyle128"):
                opp_val = getattr(old_value, "diagram_EdgeStyle128", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EdgeStyle128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EdgeStyle128"):
                opp_val = getattr(value, "diagram_EdgeStyle128", None)
                setattr(value, "diagram_EdgeStyle128", self)

    def setDescription(self, description: str):
        # TODO: Implement setDescription method
        pass

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

class Customizable:

    pass
class diagram_GaugeSection(Customizable):

    def __init__(self, min: str, max: str, value: str, label: str, diagram_GaugeSection104: "diagram_RGBValues" = None, diagram_GaugeSection: "diagram_RGBValues" = None, diagram_GaugeSection134: "diagram_GaugeCompositeStyle" = None):
        self.min = min
        self.max = max
        self.value = value
        self.label = label
        self.diagram_GaugeSection104 = diagram_GaugeSection104
        self.diagram_GaugeSection = diagram_GaugeSection
        self.diagram_GaugeSection134 = diagram_GaugeSection134
        
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
    def max(self) -> str:
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

    @property
    def diagram_GaugeSection134(self):
        return self.__diagram_GaugeSection134

    @diagram_GaugeSection134.setter
    def diagram_GaugeSection134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_GaugeSection__diagram_GaugeSection134", None)
        self.__diagram_GaugeSection134 = value
        
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
            if hasattr(old_value, "diagram_RGBValues102"):
                opp_val = getattr(old_value, "diagram_RGBValues102", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues102"):
                opp_val = getattr(value, "diagram_RGBValues102", None)
                setattr(value, "diagram_RGBValues102", self)

    @property
    def diagram_GaugeSection104(self):
        return self.__diagram_GaugeSection104

    @diagram_GaugeSection104.setter
    def diagram_GaugeSection104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_GaugeSection__diagram_GaugeSection104", None)
        self.__diagram_GaugeSection104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues105"):
                opp_val = getattr(old_value, "diagram_RGBValues105", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues105"):
                opp_val = getattr(value, "diagram_RGBValues105", None)
                setattr(value, "diagram_RGBValues105", self)

class ContainerStyle:

    pass
class diagram_ShapeContainerStyle(ContainerStyle):

    def __init__(self, shape: str, diagram_ShapeContainerStyle: "diagram_RGBValues" = None):
        self.shape = shape
        self.diagram_ShapeContainerStyle = diagram_ShapeContainerStyle
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def diagram_ShapeContainerStyle(self):
        return self.__diagram_ShapeContainerStyle

    @diagram_ShapeContainerStyle.setter
    def diagram_ShapeContainerStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_ShapeContainerStyle__diagram_ShapeContainerStyle", None)
        self.__diagram_ShapeContainerStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues112"):
                opp_val = getattr(old_value, "diagram_RGBValues112", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues112"):
                opp_val = getattr(value, "diagram_RGBValues112", None)
                setattr(value, "diagram_RGBValues112", self)

class diagram_FlatContainerStyle(ContainerStyle):

    def __init__(self, backgroundStyle: str, diagram_FlatContainerStyle: "diagram_RGBValues" = None, diagram_FlatContainerStyle109: "diagram_RGBValues" = None):
        self.backgroundStyle = backgroundStyle
        self.diagram_FlatContainerStyle = diagram_FlatContainerStyle
        self.diagram_FlatContainerStyle109 = diagram_FlatContainerStyle109
        
    @property
    def backgroundStyle(self) -> str:
        return self.__backgroundStyle

    @backgroundStyle.setter
    def backgroundStyle(self, backgroundStyle: str):
        self.__backgroundStyle = backgroundStyle

    @property
    def diagram_FlatContainerStyle(self):
        return self.__diagram_FlatContainerStyle

    @diagram_FlatContainerStyle.setter
    def diagram_FlatContainerStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_FlatContainerStyle__diagram_FlatContainerStyle", None)
        self.__diagram_FlatContainerStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues107"):
                opp_val = getattr(old_value, "diagram_RGBValues107", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues107"):
                opp_val = getattr(value, "diagram_RGBValues107", None)
                setattr(value, "diagram_RGBValues107", self)

    @property
    def diagram_FlatContainerStyle109(self):
        return self.__diagram_FlatContainerStyle109

    @diagram_FlatContainerStyle109.setter
    def diagram_FlatContainerStyle109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_FlatContainerStyle__diagram_FlatContainerStyle109", None)
        self.__diagram_FlatContainerStyle109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues110"):
                opp_val = getattr(old_value, "diagram_RGBValues110", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues110"):
                opp_val = getattr(value, "diagram_RGBValues110", None)
                setattr(value, "diagram_RGBValues110", self)

class diagram_RGBValues:

    pass
class NodeStyle:

    pass
class diagram_Lozenge(NodeStyle):

    def __init__(self, width: str, height: str, diagram_Lozenge: "diagram_RGBValues" = None):
        self.width = width
        self.height = height
        self.diagram_Lozenge = diagram_Lozenge
        
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
    def diagram_Lozenge(self):
        return self.__diagram_Lozenge

    @diagram_Lozenge.setter
    def diagram_Lozenge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_Lozenge__diagram_Lozenge", None)
        self.__diagram_Lozenge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues118"):
                opp_val = getattr(old_value, "diagram_RGBValues118", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues118"):
                opp_val = getattr(value, "diagram_RGBValues118", None)
                setattr(value, "diagram_RGBValues118", self)

class diagram_BundledImage(NodeStyle):

    def __init__(self, shape: str, diagram_BundledImage: "diagram_RGBValues" = None):
        self.shape = shape
        self.diagram_BundledImage = diagram_BundledImage
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def diagram_BundledImage(self):
        return self.__diagram_BundledImage

    @diagram_BundledImage.setter
    def diagram_BundledImage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_BundledImage__diagram_BundledImage", None)
        self.__diagram_BundledImage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues120"):
                opp_val = getattr(old_value, "diagram_RGBValues120", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues120"):
                opp_val = getattr(value, "diagram_RGBValues120", None)
                setattr(value, "diagram_RGBValues120", self)

class diagram_Square(NodeStyle):

    def __init__(self, width: str, height: str, diagram_Square: "diagram_RGBValues" = None):
        self.width = width
        self.height = height
        self.diagram_Square = diagram_Square
        
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
    def diagram_Square(self):
        return self.__diagram_Square

    @diagram_Square.setter
    def diagram_Square(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_Square__diagram_Square", None)
        self.__diagram_Square = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues114"):
                opp_val = getattr(old_value, "diagram_RGBValues114", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues114"):
                opp_val = getattr(value, "diagram_RGBValues114", None)
                setattr(value, "diagram_RGBValues114", self)

class diagram_Note(NodeStyle):

    pass
class diagram_Ellipse(NodeStyle):

    def __init__(self, verticalDiameter: str, horizontalDiameter: str, diagram_Ellipse: "diagram_RGBValues" = None):
        self.verticalDiameter = verticalDiameter
        self.horizontalDiameter = horizontalDiameter
        self.diagram_Ellipse = diagram_Ellipse
        
    @property
    def verticalDiameter(self) -> str:
        return self.__verticalDiameter

    @verticalDiameter.setter
    def verticalDiameter(self, verticalDiameter: str):
        self.__verticalDiameter = verticalDiameter

    @property
    def horizontalDiameter(self) -> str:
        return self.__horizontalDiameter

    @horizontalDiameter.setter
    def horizontalDiameter(self, horizontalDiameter: str):
        self.__horizontalDiameter = horizontalDiameter

    @property
    def diagram_Ellipse(self):
        return self.__diagram_Ellipse

    @diagram_Ellipse.setter
    def diagram_Ellipse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_Ellipse__diagram_Ellipse", None)
        self.__diagram_Ellipse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues116"):
                opp_val = getattr(old_value, "diagram_RGBValues116", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues116"):
                opp_val = getattr(value, "diagram_RGBValues116", None)
                setattr(value, "diagram_RGBValues116", self)

class diagram_WorkspaceImage(ContainerStyle, NodeStyle):

    def __init__(self, workspacePath: str):
        self.workspacePath = workspacePath
        
    @property
    def workspacePath(self) -> str:
        return self.__workspacePath

    @workspacePath.setter
    def workspacePath(self, workspacePath: str):
        self.__workspacePath = workspacePath

class diagram_CustomStyle(NodeStyle):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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
                if hasattr(item, "diagram_GaugeSection134"):
                    opp_val = getattr(item, "diagram_GaugeSection134", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_GaugeSection134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_GaugeSection134"):
                    opp_val = getattr(item, "diagram_GaugeSection134", None)
                    
                    setattr(item, "diagram_GaugeSection134", self)
                    

class diagram_Dot(NodeStyle):

    def __init__(self, strokeSizeComputationExpression: str, diagram_Dot: "diagram_RGBValues" = None):
        self.strokeSizeComputationExpression = strokeSizeComputationExpression
        self.diagram_Dot = diagram_Dot
        
    @property
    def strokeSizeComputationExpression(self) -> str:
        return self.__strokeSizeComputationExpression

    @strokeSizeComputationExpression.setter
    def strokeSizeComputationExpression(self, strokeSizeComputationExpression: str):
        self.__strokeSizeComputationExpression = strokeSizeComputationExpression

    @property
    def diagram_Dot(self):
        return self.__diagram_Dot

    @diagram_Dot.setter
    def diagram_Dot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_Dot__diagram_Dot", None)
        self.__diagram_Dot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues"):
                opp_val = getattr(old_value, "diagram_RGBValues", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues"):
                opp_val = getattr(value, "diagram_RGBValues", None)
                setattr(value, "diagram_RGBValues", self)

class BorderedStyle:

    pass
class Style:

    pass
class diagram_BorderedStyle(Style):

    def __init__(self, borderSize: str, borderSizeComputationExpression: str, diagram_BorderedStyle: "diagram_RGBValues" = None):
        self.borderSize = borderSize
        self.borderSizeComputationExpression = borderSizeComputationExpression
        self.diagram_BorderedStyle = diagram_BorderedStyle
        
    @property
    def borderSize(self) -> str:
        return self.__borderSize

    @borderSize.setter
    def borderSize(self, borderSize: str):
        self.__borderSize = borderSize

    @property
    def borderSizeComputationExpression(self) -> str:
        return self.__borderSizeComputationExpression

    @borderSizeComputationExpression.setter
    def borderSizeComputationExpression(self, borderSizeComputationExpression: str):
        self.__borderSizeComputationExpression = borderSizeComputationExpression

    @property
    def diagram_BorderedStyle(self):
        return self.__diagram_BorderedStyle

    @diagram_BorderedStyle.setter
    def diagram_BorderedStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_BorderedStyle__diagram_BorderedStyle", None)
        self.__diagram_BorderedStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues136"):
                opp_val = getattr(old_value, "diagram_RGBValues136", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues136"):
                opp_val = getattr(value, "diagram_RGBValues136", None)
                setattr(value, "diagram_RGBValues136", self)

class LabelStyle:

    pass
class IEdgeMapping:

    pass
class diagram_EdgeTarget(ABC):

    pass
class diagram_EdgeStyle(Style):

    def __init__(self, lineStyle: str, sourceArrow: str, targetArrow: str, foldingStyle: str, size: str, routingStyle: str, diagram_EdgeStyle: "diagram_DEdge" = None, diagram_EdgeStyle125: "diagram_RGBValues" = None, diagram_EdgeStyle128: "diagram_BeginLabelStyle" = None, diagram_EdgeStyle130: "diagram_CenterLabelStyle" = None, diagram_EdgeStyle132: "diagram_EndLabelStyle" = None):
        self.lineStyle = lineStyle
        self.sourceArrow = sourceArrow
        self.targetArrow = targetArrow
        self.foldingStyle = foldingStyle
        self.size = size
        self.routingStyle = routingStyle
        self.diagram_EdgeStyle = diagram_EdgeStyle
        self.diagram_EdgeStyle125 = diagram_EdgeStyle125
        self.diagram_EdgeStyle128 = diagram_EdgeStyle128
        self.diagram_EdgeStyle130 = diagram_EdgeStyle130
        self.diagram_EdgeStyle132 = diagram_EdgeStyle132
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def lineStyle(self) -> str:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle

    @property
    def sourceArrow(self) -> str:
        return self.__sourceArrow

    @sourceArrow.setter
    def sourceArrow(self, sourceArrow: str):
        self.__sourceArrow = sourceArrow

    @property
    def foldingStyle(self) -> str:
        return self.__foldingStyle

    @foldingStyle.setter
    def foldingStyle(self, foldingStyle: str):
        self.__foldingStyle = foldingStyle

    @property
    def routingStyle(self) -> str:
        return self.__routingStyle

    @routingStyle.setter
    def routingStyle(self, routingStyle: str):
        self.__routingStyle = routingStyle

    @property
    def targetArrow(self) -> str:
        return self.__targetArrow

    @targetArrow.setter
    def targetArrow(self, targetArrow: str):
        self.__targetArrow = targetArrow

    @property
    def diagram_EdgeStyle130(self):
        return self.__diagram_EdgeStyle130

    @diagram_EdgeStyle130.setter
    def diagram_EdgeStyle130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle130", None)
        self.__diagram_EdgeStyle130 = value
        
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
    def diagram_EdgeStyle128(self):
        return self.__diagram_EdgeStyle128

    @diagram_EdgeStyle128.setter
    def diagram_EdgeStyle128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle128", None)
        self.__diagram_EdgeStyle128 = value
        
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
    def diagram_EdgeStyle132(self):
        return self.__diagram_EdgeStyle132

    @diagram_EdgeStyle132.setter
    def diagram_EdgeStyle132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle132", None)
        self.__diagram_EdgeStyle132 = value
        
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
    def diagram_EdgeStyle125(self):
        return self.__diagram_EdgeStyle125

    @diagram_EdgeStyle125.setter
    def diagram_EdgeStyle125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle125", None)
        self.__diagram_EdgeStyle125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_RGBValues126"):
                opp_val = getattr(old_value, "diagram_RGBValues126", None)
                if opp_val == self:
                    setattr(old_value, "diagram_RGBValues126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_RGBValues126"):
                opp_val = getattr(value, "diagram_RGBValues126", None)
                setattr(value, "diagram_RGBValues126", self)

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
            if hasattr(old_value, "diagram_DEdge89"):
                opp_val = getattr(old_value, "diagram_DEdge89", None)
                if opp_val == self:
                    setattr(old_value, "diagram_DEdge89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DEdge89"):
                opp_val = getattr(value, "diagram_DEdge89", None)
                setattr(value, "diagram_DEdge89", self)

class DDiagramElementContainer:

    pass
class diagram_DNodeList(DDiagramElementContainer):

    def __init__(self, lineWidth: int, diagram_DNodeList: set["diagram_DNodeListElement"] = None):
        self.lineWidth = lineWidth
        self.diagram_DNodeList = diagram_DNodeList if diagram_DNodeList is not None else set()
        
    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

    @property
    def diagram_DNodeList(self):
        return self.__diagram_DNodeList

    @diagram_DNodeList.setter
    def diagram_DNodeList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNodeList__diagram_DNodeList", None)
        self.__diagram_DNodeList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DNodeListElement75"):
                    opp_val = getattr(item, "diagram_DNodeListElement75", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DNodeListElement75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DNodeListElement75"):
                    opp_val = getattr(item, "diagram_DNodeListElement75", None)
                    
                    setattr(item, "diagram_DNodeListElement75", self)
                    

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
                if hasattr(item, "diagram_DDiagramElement73"):
                    opp_val = getattr(item, "diagram_DDiagramElement73", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElement73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElement73"):
                    opp_val = getattr(item, "diagram_DDiagramElement73", None)
                    
                    setattr(item, "diagram_DDiagramElement73", self)
                    

class ContainerMapping:

    pass
class diagram_ContainerStyle(BorderedStyle, Style, LabelStyle):

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
                if hasattr(item, "diagram_DNode43"):
                    opp_val = getattr(item, "diagram_DNode43", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DNode43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DNode43"):
                    opp_val = getattr(item, "diagram_DNode43", None)
                    
                    setattr(item, "diagram_DNode43", self)
                    

class filter_CompositeFilterDescription:

    pass
class NodeMapping:

    pass
class diagram_Style:

    pass
class diagram_NodeStyle(BorderedStyle, Style, LabelStyle):

    def __init__(self, labelPosition: str, hideLabelByDefault: bool, diagram_NodeStyle: "diagram_DNode" = None, diagram_NodeStyle78: "diagram_DNodeListElement" = None):
        self.labelPosition = labelPosition
        self.hideLabelByDefault = hideLabelByDefault
        self.diagram_NodeStyle = diagram_NodeStyle
        self.diagram_NodeStyle78 = diagram_NodeStyle78
        
    @property
    def hideLabelByDefault(self) -> bool:
        return self.__hideLabelByDefault

    @hideLabelByDefault.setter
    def hideLabelByDefault(self, hideLabelByDefault: bool):
        self.__hideLabelByDefault = hideLabelByDefault

    @property
    def labelPosition(self) -> str:
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition

    @property
    def diagram_NodeStyle78(self):
        return self.__diagram_NodeStyle78

    @diagram_NodeStyle78.setter
    def diagram_NodeStyle78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_NodeStyle__diagram_NodeStyle78", None)
        self.__diagram_NodeStyle78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DNodeListElement77"):
                opp_val = getattr(old_value, "diagram_DNodeListElement77", None)
                if opp_val == self:
                    setattr(old_value, "diagram_DNodeListElement77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DNodeListElement77"):
                opp_val = getattr(value, "diagram_DNodeListElement77", None)
                setattr(value, "diagram_DNodeListElement77", self)

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
            if hasattr(old_value, "diagram_DNode45"):
                opp_val = getattr(old_value, "diagram_DNode45", None)
                if opp_val == self:
                    setattr(old_value, "diagram_DNode45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DNode45"):
                opp_val = getattr(value, "diagram_DNode45", None)
                setattr(value, "diagram_DNode45", self)

class EdgeTarget:

    pass
class AbstractDNode:

    pass
class DNavigable:

    pass
class DRepresentationElement:

    pass
class DSemanticDecorator:

    pass
class DDiagram:

    pass
class diagram_DSemanticDiagram(DSemanticDecorator, DDiagram):

    pass
class GraphicalFilter:

    pass
class diagram_FoldingPointFilter(GraphicalFilter):

    pass
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
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

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

class diagram_FoldingFilter(GraphicalFilter):

    pass
class diagram_AppliedCompositeFilters(GraphicalFilter):

    pass
class diagram_HideLabelFilter(GraphicalFilter):

    pass
class diagram_CollapseFilter(GraphicalFilter):

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        
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

class diagram_HideFilter(GraphicalFilter):

    pass
class diagram_GraphicalFilter(ABC):

    pass
class DiagramElementMapping:

    pass
class diagram_Decoration:

    pass
class Layer:

    pass
class diagram_description_AdditionalLayer(Layer):

    def __init__(self, activeByDefault: bool, optional: bool, Layer196: "diagram_description_DiagramDescription", Layer: "diagram_DDiagram", Layer201: "diagram_description_DiagramDescription", Layer34: "diagram_DDiagramElement"):
        self.activeByDefault = activeByDefault
        self.optional = optional
        
    @property
    def activeByDefault(self) -> bool:
        return self.__activeByDefault

    @activeByDefault.setter
    def activeByDefault(self, activeByDefault: bool):
        self.__activeByDefault = activeByDefault

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

class diagram_FilterVariableHistory:

    pass
class tool_BehaviorTool:

    pass
class validation_ValidationRule:

    pass
class diagram_DEdge(DDiagramElement, EdgeTarget):

    def __init__(self, size: str, arrangeConstraints: str, beginLabel: str, endLabel: str, routingStyle: str, isFold: bool, isMockEdge: bool, diagram_DEdge: "diagram_DDiagram" = None, diagram_DEdge89: "diagram_EdgeStyle" = None, outgoingEdges: "diagram_EdgeTarget" = None, incomingEdges: "diagram_EdgeTarget" = None, diagram_DEdge94: "IEdgeMapping" = None, diagram_DEdge96: "diagram_Style" = None, diagram_DEdge99: set["diagram_EdgeTarget"] = None, DEdge: "diagram_EdgeTarget" = None, DEdge123: "diagram_EdgeTarget" = None):
        self.size = size
        self.arrangeConstraints = arrangeConstraints
        self.beginLabel = beginLabel
        self.endLabel = endLabel
        self.routingStyle = routingStyle
        self.isFold = isFold
        self.isMockEdge = isMockEdge
        self.diagram_DEdge = diagram_DEdge
        self.diagram_DEdge89 = diagram_DEdge89
        self.outgoingEdges = outgoingEdges
        self.incomingEdges = incomingEdges
        self.diagram_DEdge94 = diagram_DEdge94
        self.diagram_DEdge96 = diagram_DEdge96
        self.diagram_DEdge99 = diagram_DEdge99 if diagram_DEdge99 is not None else set()
        self.DEdge = DEdge
        self.DEdge123 = DEdge123
        
    @property
    def beginLabel(self) -> str:
        return self.__beginLabel

    @beginLabel.setter
    def beginLabel(self, beginLabel: str):
        self.__beginLabel = beginLabel

    @property
    def isFold(self) -> bool:
        return self.__isFold

    @isFold.setter
    def isFold(self, isFold: bool):
        self.__isFold = isFold

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def endLabel(self) -> str:
        return self.__endLabel

    @endLabel.setter
    def endLabel(self, endLabel: str):
        self.__endLabel = endLabel

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
    def arrangeConstraints(self) -> str:
        return self.__arrangeConstraints

    @arrangeConstraints.setter
    def arrangeConstraints(self, arrangeConstraints: str):
        self.__arrangeConstraints = arrangeConstraints

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
    def diagram_DEdge96(self):
        return self.__diagram_DEdge96

    @diagram_DEdge96.setter
    def diagram_DEdge96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__diagram_DEdge96", None)
        self.__diagram_DEdge96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_Style97"):
                opp_val = getattr(old_value, "diagram_Style97", None)
                if opp_val == self:
                    setattr(old_value, "diagram_Style97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_Style97"):
                opp_val = getattr(value, "diagram_Style97", None)
                setattr(value, "diagram_Style97", self)

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
    def diagram_DEdge99(self):
        return self.__diagram_DEdge99

    @diagram_DEdge99.setter
    def diagram_DEdge99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__diagram_DEdge99", None)
        self.__diagram_DEdge99 = value if value is not None else set()
        
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
    def DEdge123(self):
        return self.__DEdge123

    @DEdge123.setter
    def DEdge123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__DEdge123", None)
        self.__DEdge123 = value
        
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
    def incomingEdges(self):
        return self.__incomingEdges

    @incomingEdges.setter
    def incomingEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__incomingEdges", None)
        self.__incomingEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeTarget92"):
                opp_val = getattr(old_value, "EdgeTarget92", None)
                if opp_val == self:
                    setattr(old_value, "EdgeTarget92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeTarget92"):
                opp_val = getattr(value, "EdgeTarget92", None)
                setattr(value, "EdgeTarget92", self)

    @property
    def diagram_DEdge89(self):
        return self.__diagram_DEdge89

    @diagram_DEdge89.setter
    def diagram_DEdge89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__diagram_DEdge89", None)
        self.__diagram_DEdge89 = value
        
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

    def isRootFolding(self) -> bool:
        # TODO: Implement isRootFolding method
        pass

class DiagramDescription:

    pass
class filter_FilterDescription:

    pass
class concern_ConcernDescription:

    pass
class diagram_DNodeListElement(AbstractDNode):

    pass
class DContainer:

    pass
class DValidable:

    pass
class DragAndDropTarget:

    pass
class diagram_DDiagramElementContainer(AbstractDNode, EdgeTarget, DragAndDropTarget, DContainer):

    def __init__(self, width: str, height: str, diagram_DDiagramElementContainer: "diagram_DDiagram" = None, diagram_DDiagramElementContainer60: set["diagram_DDiagramElement"] = None, diagram_DDiagramElementContainer63: "diagram_ContainerStyle" = None, diagram_DDiagramElementContainer65: "diagram_Style" = None, diagram_DDiagramElementContainer68: "ContainerMapping" = None, diagram_DDiagramElementContainer70: set["ContainerMapping"] = None, diagram_DDiagramElementContainer54: set["diagram_DNode"] = None, diagram_DDiagramElementContainer58: "diagram_DDiagramElementContainer" = None, diagram_DDiagramElementContainer56: set["diagram_DDiagramElementContainer"] = None):
        self.width = width
        self.height = height
        self.diagram_DDiagramElementContainer = diagram_DDiagramElementContainer
        self.diagram_DDiagramElementContainer60 = diagram_DDiagramElementContainer60 if diagram_DDiagramElementContainer60 is not None else set()
        self.diagram_DDiagramElementContainer63 = diagram_DDiagramElementContainer63
        self.diagram_DDiagramElementContainer65 = diagram_DDiagramElementContainer65
        self.diagram_DDiagramElementContainer68 = diagram_DDiagramElementContainer68
        self.diagram_DDiagramElementContainer70 = diagram_DDiagramElementContainer70 if diagram_DDiagramElementContainer70 is not None else set()
        self.diagram_DDiagramElementContainer54 = diagram_DDiagramElementContainer54 if diagram_DDiagramElementContainer54 is not None else set()
        self.diagram_DDiagramElementContainer58 = diagram_DDiagramElementContainer58
        self.diagram_DDiagramElementContainer56 = diagram_DDiagramElementContainer56 if diagram_DDiagramElementContainer56 is not None else set()
        
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
    def diagram_DDiagramElementContainer60(self):
        return self.__diagram_DDiagramElementContainer60

    @diagram_DDiagramElementContainer60.setter
    def diagram_DDiagramElementContainer60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer60", None)
        self.__diagram_DDiagramElementContainer60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DDiagramElement61"):
                    opp_val = getattr(item, "diagram_DDiagramElement61", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElement61", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElement61"):
                    opp_val = getattr(item, "diagram_DDiagramElement61", None)
                    
                    setattr(item, "diagram_DDiagramElement61", self)
                    

    @property
    def diagram_DDiagramElementContainer70(self):
        return self.__diagram_DDiagramElementContainer70

    @diagram_DDiagramElementContainer70.setter
    def diagram_DDiagramElementContainer70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer70", None)
        self.__diagram_DDiagramElementContainer70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping71"):
                    opp_val = getattr(item, "ContainerMapping71", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping71"):
                    opp_val = getattr(item, "ContainerMapping71", None)
                    
                    setattr(item, "ContainerMapping71", self)
                    

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
    def diagram_DDiagramElementContainer58(self):
        return self.__diagram_DDiagramElementContainer58

    @diagram_DDiagramElementContainer58.setter
    def diagram_DDiagramElementContainer58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer58", None)
        self.__diagram_DDiagramElementContainer58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagramElementContainer56"):
                opp_val = getattr(old_value, "diagram_DDiagramElementContainer56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagramElementContainer56"):
                opp_val = getattr(value, "diagram_DDiagramElementContainer56", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagramElementContainer56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def diagram_DDiagramElementContainer65(self):
        return self.__diagram_DDiagramElementContainer65

    @diagram_DDiagramElementContainer65.setter
    def diagram_DDiagramElementContainer65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer65", None)
        self.__diagram_DDiagramElementContainer65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_Style66"):
                opp_val = getattr(old_value, "diagram_Style66", None)
                if opp_val == self:
                    setattr(old_value, "diagram_Style66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_Style66"):
                opp_val = getattr(value, "diagram_Style66", None)
                setattr(value, "diagram_Style66", self)

    @property
    def diagram_DDiagramElementContainer54(self):
        return self.__diagram_DDiagramElementContainer54

    @diagram_DDiagramElementContainer54.setter
    def diagram_DDiagramElementContainer54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer54", None)
        self.__diagram_DDiagramElementContainer54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DNode55"):
                    opp_val = getattr(item, "diagram_DNode55", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DNode55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DNode55"):
                    opp_val = getattr(item, "diagram_DNode55", None)
                    
                    setattr(item, "diagram_DNode55", self)
                    

    @property
    def diagram_DDiagramElementContainer56(self):
        return self.__diagram_DDiagramElementContainer56

    @diagram_DDiagramElementContainer56.setter
    def diagram_DDiagramElementContainer56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElementContainer__diagram_DDiagramElementContainer56", None)
        self.__diagram_DDiagramElementContainer56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_DDiagramElementContainer58"):
                    opp_val = getattr(item, "diagram_DDiagramElementContainer58", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElementContainer58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElementContainer58"):
                    opp_val = getattr(item, "diagram_DDiagramElementContainer58", None)
                    
                    setattr(item, "diagram_DDiagramElementContainer58", self)
                    

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

class diagram_DNode(AbstractDNode, EdgeTarget, DragAndDropTarget):

    def __init__(self, width: str, height: str, labelPosition: str, resizeKind: str, diagram_DNode: "diagram_DDiagram" = None, diagram_DNode45: "diagram_NodeStyle" = None, diagram_DNode47: "diagram_Style" = None, diagram_DNode49: "NodeMapping" = None, diagram_DNode51: set["NodeMapping"] = None, diagram_DNode43: "diagram_AbstractDNode" = None, diagram_DNode55: "diagram_DDiagramElementContainer" = None):
        self.width = width
        self.height = height
        self.labelPosition = labelPosition
        self.resizeKind = resizeKind
        self.diagram_DNode = diagram_DNode
        self.diagram_DNode45 = diagram_DNode45
        self.diagram_DNode47 = diagram_DNode47
        self.diagram_DNode49 = diagram_DNode49
        self.diagram_DNode51 = diagram_DNode51 if diagram_DNode51 is not None else set()
        self.diagram_DNode43 = diagram_DNode43
        self.diagram_DNode55 = diagram_DNode55
        
    @property
    def resizeKind(self) -> str:
        return self.__resizeKind

    @resizeKind.setter
    def resizeKind(self, resizeKind: str):
        self.__resizeKind = resizeKind

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def labelPosition(self) -> str:
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def diagram_DNode51(self):
        return self.__diagram_DNode51

    @diagram_DNode51.setter
    def diagram_DNode51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode51", None)
        self.__diagram_DNode51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping52"):
                    opp_val = getattr(item, "NodeMapping52", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping52"):
                    opp_val = getattr(item, "NodeMapping52", None)
                    
                    setattr(item, "NodeMapping52", self)
                    

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
    def diagram_DNode43(self):
        return self.__diagram_DNode43

    @diagram_DNode43.setter
    def diagram_DNode43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode43", None)
        self.__diagram_DNode43 = value
        
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
    def diagram_DNode47(self):
        return self.__diagram_DNode47

    @diagram_DNode47.setter
    def diagram_DNode47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode47", None)
        self.__diagram_DNode47 = value
        
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
    def diagram_DNode55(self):
        return self.__diagram_DNode55

    @diagram_DNode55.setter
    def diagram_DNode55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode55", None)
        self.__diagram_DNode55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagramElementContainer54"):
                opp_val = getattr(old_value, "diagram_DDiagramElementContainer54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagramElementContainer54"):
                opp_val = getattr(value, "diagram_DDiagramElementContainer54", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagramElementContainer54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DNode49(self):
        return self.__diagram_DNode49

    @diagram_DNode49.setter
    def diagram_DNode49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode49", None)
        self.__diagram_DNode49 = value
        
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
    def diagram_DNode45(self):
        return self.__diagram_DNode45

    @diagram_DNode45.setter
    def diagram_DNode45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DNode__diagram_DNode45", None)
        self.__diagram_DNode45 = value
        
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
class diagram_concern_ConcernDescription(description_IdentifiedElement, description_DocumentedElement):

    pass
class diagram_description_AbstractNodeMapping(description_DiagramElementMapping, description_DocumentedElement):

    def __init__(self, domainClass: str, diagram_description_AbstractNodeMapping: set["NodeMapping"] = None, diagram_description_AbstractNodeMapping241: set["NodeMapping"] = None):
        self.domainClass = domainClass
        self.diagram_description_AbstractNodeMapping = diagram_description_AbstractNodeMapping if diagram_description_AbstractNodeMapping is not None else set()
        self.diagram_description_AbstractNodeMapping241 = diagram_description_AbstractNodeMapping241 if diagram_description_AbstractNodeMapping241 is not None else set()
        
    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

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
                if hasattr(item, "NodeMapping239"):
                    opp_val = getattr(item, "NodeMapping239", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping239"):
                    opp_val = getattr(item, "NodeMapping239", None)
                    
                    setattr(item, "NodeMapping239", self)
                    

    @property
    def diagram_description_AbstractNodeMapping241(self):
        return self.__diagram_description_AbstractNodeMapping241

    @diagram_description_AbstractNodeMapping241.setter
    def diagram_description_AbstractNodeMapping241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_AbstractNodeMapping__diagram_description_AbstractNodeMapping241", None)
        self.__diagram_description_AbstractNodeMapping241 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping242"):
                    opp_val = getattr(item, "NodeMapping242", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping242", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping242"):
                    opp_val = getattr(item, "NodeMapping242", None)
                    
                    setattr(item, "NodeMapping242", self)
                    

    def findDNodeFromEObject(self, eObject: str) -> DDiagramElement:
        # TODO: Implement findDNodeFromEObject method
        pass

    def getAllBorderedNodeMappings(self) -> str:
        # TODO: Implement getAllBorderedNodeMappings method
        pass

    def clearDNodesDone(self):
        # TODO: Implement clearDNodesDone method
        pass

    def addDoneNode(self, node: DSemanticDecorator):
        # TODO: Implement addDoneNode method
        pass

class diagram_description_EdgeMappingImport(description_IdentifiedElement, description_IEdgeMapping, description_DocumentedElement):

    def __init__(self, inheritsAncestorFilters: bool, diagram_description_EdgeMappingImport: "IEdgeMapping" = None, diagram_description_EdgeMappingImport287: set["ConditionalEdgeStyleDescription"] = None):
        self.inheritsAncestorFilters = inheritsAncestorFilters
        self.diagram_description_EdgeMappingImport = diagram_description_EdgeMappingImport
        self.diagram_description_EdgeMappingImport287 = diagram_description_EdgeMappingImport287 if diagram_description_EdgeMappingImport287 is not None else set()
        
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
            if hasattr(old_value, "IEdgeMapping285"):
                opp_val = getattr(old_value, "IEdgeMapping285", None)
                if opp_val == self:
                    setattr(old_value, "IEdgeMapping285", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IEdgeMapping285"):
                opp_val = getattr(value, "IEdgeMapping285", None)
                setattr(value, "IEdgeMapping285", self)

    @property
    def diagram_description_EdgeMappingImport287(self):
        return self.__diagram_description_EdgeMappingImport287

    @diagram_description_EdgeMappingImport287.setter
    def diagram_description_EdgeMappingImport287(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMappingImport__diagram_description_EdgeMappingImport287", None)
        self.__diagram_description_EdgeMappingImport287 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConditionalEdgeStyleDescription288"):
                    opp_val = getattr(item, "ConditionalEdgeStyleDescription288", None)
                    
                    if opp_val == self:
                        setattr(item, "ConditionalEdgeStyleDescription288", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConditionalEdgeStyleDescription288"):
                    opp_val = getattr(item, "ConditionalEdgeStyleDescription288", None)
                    
                    setattr(item, "ConditionalEdgeStyleDescription288", self)
                    

class diagram_filter_FilterDescription(description_IdentifiedElement, description_DocumentedElement):

    def __init__(self):
        
    def isVisible(self, element: DDiagramElement) -> bool:
        # TODO: Implement isVisible method
        pass

class diagram_description_Layer(description_IdentifiedElement, description_EndUserDocumentedElement, description_DocumentedElement):

    def __init__(self, icon: str, diagram_description_Layer302: set["EdgeMapping"] = None, diagram_description_Layer305: set["EdgeMappingImport"] = None, diagram_description_Layer308: set["ContainerMapping"] = None, diagram_description_Layer311: set["DiagramElementMapping"] = None, diagram_description_Layer314: set["tool_AbstractToolDescription"] = None, diagram_description_Layer317: set["tool_ToolSection"] = None, diagram_description_Layer320: set["tool_AbstractToolDescription"] = None, diagram_description_Layer323: "DecorationDescriptionsSet" = None, diagram_description_Layer: set["NodeMapping"] = None, diagram_description_Layer325: set["EdgeMapping"] = None, diagram_description_Layer328: "Customization" = None):
        self.icon = icon
        self.diagram_description_Layer302 = diagram_description_Layer302 if diagram_description_Layer302 is not None else set()
        self.diagram_description_Layer305 = diagram_description_Layer305 if diagram_description_Layer305 is not None else set()
        self.diagram_description_Layer308 = diagram_description_Layer308 if diagram_description_Layer308 is not None else set()
        self.diagram_description_Layer311 = diagram_description_Layer311 if diagram_description_Layer311 is not None else set()
        self.diagram_description_Layer314 = diagram_description_Layer314 if diagram_description_Layer314 is not None else set()
        self.diagram_description_Layer317 = diagram_description_Layer317 if diagram_description_Layer317 is not None else set()
        self.diagram_description_Layer320 = diagram_description_Layer320 if diagram_description_Layer320 is not None else set()
        self.diagram_description_Layer323 = diagram_description_Layer323
        self.diagram_description_Layer = diagram_description_Layer if diagram_description_Layer is not None else set()
        self.diagram_description_Layer325 = diagram_description_Layer325 if diagram_description_Layer325 is not None else set()
        self.diagram_description_Layer328 = diagram_description_Layer328
        
    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def diagram_description_Layer325(self):
        return self.__diagram_description_Layer325

    @diagram_description_Layer325.setter
    def diagram_description_Layer325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer325", None)
        self.__diagram_description_Layer325 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMapping326"):
                    opp_val = getattr(item, "EdgeMapping326", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping326", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping326"):
                    opp_val = getattr(item, "EdgeMapping326", None)
                    
                    setattr(item, "EdgeMapping326", self)
                    

    @property
    def diagram_description_Layer323(self):
        return self.__diagram_description_Layer323

    @diagram_description_Layer323.setter
    def diagram_description_Layer323(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer323", None)
        self.__diagram_description_Layer323 = value
        
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
    def diagram_description_Layer302(self):
        return self.__diagram_description_Layer302

    @diagram_description_Layer302.setter
    def diagram_description_Layer302(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer302", None)
        self.__diagram_description_Layer302 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMapping303"):
                    opp_val = getattr(item, "EdgeMapping303", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping303", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping303"):
                    opp_val = getattr(item, "EdgeMapping303", None)
                    
                    setattr(item, "EdgeMapping303", self)
                    

    @property
    def diagram_description_Layer308(self):
        return self.__diagram_description_Layer308

    @diagram_description_Layer308.setter
    def diagram_description_Layer308(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer308", None)
        self.__diagram_description_Layer308 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping309"):
                    opp_val = getattr(item, "ContainerMapping309", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping309", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping309"):
                    opp_val = getattr(item, "ContainerMapping309", None)
                    
                    setattr(item, "ContainerMapping309", self)
                    

    @property
    def diagram_description_Layer311(self):
        return self.__diagram_description_Layer311

    @diagram_description_Layer311.setter
    def diagram_description_Layer311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer311", None)
        self.__diagram_description_Layer311 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping312"):
                    opp_val = getattr(item, "DiagramElementMapping312", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping312", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping312"):
                    opp_val = getattr(item, "DiagramElementMapping312", None)
                    
                    setattr(item, "DiagramElementMapping312", self)
                    

    @property
    def diagram_description_Layer317(self):
        return self.__diagram_description_Layer317

    @diagram_description_Layer317.setter
    def diagram_description_Layer317(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer317", None)
        self.__diagram_description_Layer317 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolSection318"):
                    opp_val = getattr(item, "tool_ToolSection318", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolSection318", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolSection318"):
                    opp_val = getattr(item, "tool_ToolSection318", None)
                    
                    setattr(item, "tool_ToolSection318", self)
                    

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
                if hasattr(item, "NodeMapping300"):
                    opp_val = getattr(item, "NodeMapping300", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping300", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping300"):
                    opp_val = getattr(item, "NodeMapping300", None)
                    
                    setattr(item, "NodeMapping300", self)
                    

    @property
    def diagram_description_Layer328(self):
        return self.__diagram_description_Layer328

    @diagram_description_Layer328.setter
    def diagram_description_Layer328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer328", None)
        self.__diagram_description_Layer328 = value
        
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
    def diagram_description_Layer320(self):
        return self.__diagram_description_Layer320

    @diagram_description_Layer320.setter
    def diagram_description_Layer320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer320", None)
        self.__diagram_description_Layer320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription321"):
                    opp_val = getattr(item, "tool_AbstractToolDescription321", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription321", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription321"):
                    opp_val = getattr(item, "tool_AbstractToolDescription321", None)
                    
                    setattr(item, "tool_AbstractToolDescription321", self)
                    

    @property
    def diagram_description_Layer305(self):
        return self.__diagram_description_Layer305

    @diagram_description_Layer305.setter
    def diagram_description_Layer305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer305", None)
        self.__diagram_description_Layer305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMappingImport306"):
                    opp_val = getattr(item, "EdgeMappingImport306", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMappingImport306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMappingImport306"):
                    opp_val = getattr(item, "EdgeMappingImport306", None)
                    
                    setattr(item, "EdgeMappingImport306", self)
                    

    @property
    def diagram_description_Layer314(self):
        return self.__diagram_description_Layer314

    @diagram_description_Layer314.setter
    def diagram_description_Layer314(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer314", None)
        self.__diagram_description_Layer314 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription315"):
                    opp_val = getattr(item, "tool_AbstractToolDescription315", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription315", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription315"):
                    opp_val = getattr(item, "tool_AbstractToolDescription315", None)
                    
                    setattr(item, "tool_AbstractToolDescription315", self)
                    

class diagram_tool_ToolSection(description_IdentifiedElement, description_DocumentedElement):

    def __init__(self, icon: str, diagram_tool_ToolSection: set["tool_ToolEntry"] = None, diagram_tool_ToolSection368: set["tool_ToolSection"] = None, diagram_tool_ToolSection371: set["tool_PopupMenu"] = None, diagram_tool_ToolSection373: set["tool_ToolEntry"] = None, diagram_tool_ToolSection376: set["tool_ToolGroupExtension"] = None):
        self.icon = icon
        self.diagram_tool_ToolSection = diagram_tool_ToolSection if diagram_tool_ToolSection is not None else set()
        self.diagram_tool_ToolSection368 = diagram_tool_ToolSection368 if diagram_tool_ToolSection368 is not None else set()
        self.diagram_tool_ToolSection371 = diagram_tool_ToolSection371 if diagram_tool_ToolSection371 is not None else set()
        self.diagram_tool_ToolSection373 = diagram_tool_ToolSection373 if diagram_tool_ToolSection373 is not None else set()
        self.diagram_tool_ToolSection376 = diagram_tool_ToolSection376 if diagram_tool_ToolSection376 is not None else set()
        
    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def diagram_tool_ToolSection376(self):
        return self.__diagram_tool_ToolSection376

    @diagram_tool_ToolSection376.setter
    def diagram_tool_ToolSection376(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection376", None)
        self.__diagram_tool_ToolSection376 = value if value is not None else set()
        
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
    def diagram_tool_ToolSection368(self):
        return self.__diagram_tool_ToolSection368

    @diagram_tool_ToolSection368.setter
    def diagram_tool_ToolSection368(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection368", None)
        self.__diagram_tool_ToolSection368 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolSection369"):
                    opp_val = getattr(item, "tool_ToolSection369", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolSection369", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolSection369"):
                    opp_val = getattr(item, "tool_ToolSection369", None)
                    
                    setattr(item, "tool_ToolSection369", self)
                    

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
    def diagram_tool_ToolSection373(self):
        return self.__diagram_tool_ToolSection373

    @diagram_tool_ToolSection373.setter
    def diagram_tool_ToolSection373(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection373", None)
        self.__diagram_tool_ToolSection373 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolEntry374"):
                    opp_val = getattr(item, "tool_ToolEntry374", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolEntry374", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolEntry374"):
                    opp_val = getattr(item, "tool_ToolEntry374", None)
                    
                    setattr(item, "tool_ToolEntry374", self)
                    

    @property
    def diagram_tool_ToolSection371(self):
        return self.__diagram_tool_ToolSection371

    @diagram_tool_ToolSection371.setter
    def diagram_tool_ToolSection371(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection371", None)
        self.__diagram_tool_ToolSection371 = value if value is not None else set()
        
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
                    

class diagram_description_EdgeMapping(description_DiagramElementMapping, description_IEdgeMapping, description_DocumentedElement):

    def __init__(self, sourceFinderExpression: str, targetExpression: str, domainClass: str, useDomainElement: bool, pathExpression: str, targetFinderExpression: str, diagram_description_EdgeMapping277: "style_EdgeStyleDescription" = None, diagram_description_EdgeMapping279: set["ConditionalEdgeStyleDescription"] = None, diagram_description_EdgeMapping281: set["tool_ReconnectEdgeDescription"] = None, diagram_description_EdgeMapping283: set["AbstractNodeMapping"] = None, diagram_description_EdgeMapping: set["DiagramElementMapping"] = None, diagram_description_EdgeMapping274: set["DiagramElementMapping"] = None):
        self.sourceFinderExpression = sourceFinderExpression
        self.targetExpression = targetExpression
        self.domainClass = domainClass
        self.useDomainElement = useDomainElement
        self.pathExpression = pathExpression
        self.targetFinderExpression = targetFinderExpression
        self.diagram_description_EdgeMapping277 = diagram_description_EdgeMapping277
        self.diagram_description_EdgeMapping279 = diagram_description_EdgeMapping279 if diagram_description_EdgeMapping279 is not None else set()
        self.diagram_description_EdgeMapping281 = diagram_description_EdgeMapping281 if diagram_description_EdgeMapping281 is not None else set()
        self.diagram_description_EdgeMapping283 = diagram_description_EdgeMapping283 if diagram_description_EdgeMapping283 is not None else set()
        self.diagram_description_EdgeMapping = diagram_description_EdgeMapping if diagram_description_EdgeMapping is not None else set()
        self.diagram_description_EdgeMapping274 = diagram_description_EdgeMapping274 if diagram_description_EdgeMapping274 is not None else set()
        
    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def targetExpression(self) -> str:
        return self.__targetExpression

    @targetExpression.setter
    def targetExpression(self, targetExpression: str):
        self.__targetExpression = targetExpression

    @property
    def sourceFinderExpression(self) -> str:
        return self.__sourceFinderExpression

    @sourceFinderExpression.setter
    def sourceFinderExpression(self, sourceFinderExpression: str):
        self.__sourceFinderExpression = sourceFinderExpression

    @property
    def targetFinderExpression(self) -> str:
        return self.__targetFinderExpression

    @targetFinderExpression.setter
    def targetFinderExpression(self, targetFinderExpression: str):
        self.__targetFinderExpression = targetFinderExpression

    @property
    def pathExpression(self) -> str:
        return self.__pathExpression

    @pathExpression.setter
    def pathExpression(self, pathExpression: str):
        self.__pathExpression = pathExpression

    @property
    def useDomainElement(self) -> bool:
        return self.__useDomainElement

    @useDomainElement.setter
    def useDomainElement(self, useDomainElement: bool):
        self.__useDomainElement = useDomainElement

    @property
    def diagram_description_EdgeMapping281(self):
        return self.__diagram_description_EdgeMapping281

    @diagram_description_EdgeMapping281.setter
    def diagram_description_EdgeMapping281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping281", None)
        self.__diagram_description_EdgeMapping281 = value if value is not None else set()
        
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
    def diagram_description_EdgeMapping283(self):
        return self.__diagram_description_EdgeMapping283

    @diagram_description_EdgeMapping283.setter
    def diagram_description_EdgeMapping283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping283", None)
        self.__diagram_description_EdgeMapping283 = value if value is not None else set()
        
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
    def diagram_description_EdgeMapping279(self):
        return self.__diagram_description_EdgeMapping279

    @diagram_description_EdgeMapping279.setter
    def diagram_description_EdgeMapping279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping279", None)
        self.__diagram_description_EdgeMapping279 = value if value is not None else set()
        
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
                    

    @property
    def diagram_description_EdgeMapping277(self):
        return self.__diagram_description_EdgeMapping277

    @diagram_description_EdgeMapping277.setter
    def diagram_description_EdgeMapping277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping277", None)
        self.__diagram_description_EdgeMapping277 = value
        
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
                if hasattr(item, "DiagramElementMapping272"):
                    opp_val = getattr(item, "DiagramElementMapping272", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping272", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping272"):
                    opp_val = getattr(item, "DiagramElementMapping272", None)
                    
                    setattr(item, "DiagramElementMapping272", self)
                    

    @property
    def diagram_description_EdgeMapping274(self):
        return self.__diagram_description_EdgeMapping274

    @diagram_description_EdgeMapping274.setter
    def diagram_description_EdgeMapping274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping274", None)
        self.__diagram_description_EdgeMapping274 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping275"):
                    opp_val = getattr(item, "DiagramElementMapping275", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping275", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping275"):
                    opp_val = getattr(item, "DiagramElementMapping275", None)
                    
                    setattr(item, "DiagramElementMapping275", self)
                    

    def updateEdge(self, viewEdge: str):
        # TODO: Implement updateEdge method
        pass

    def getBestStyle(self, viewVariable: str, modelElement: str, containerVariable: str) -> EdgeStyle:
        # TODO: Implement getBestStyle method
        pass

    def getEdgeTargetCandidates(self, semanticOrigin: str, viewPoint: DDiagram) -> str:
        # TODO: Implement getEdgeTargetCandidates method
        pass

    def getEdgeTargetCandidates(self, containerView: str, semanticOrigin: str, container: str) -> str:
        # TODO: Implement getEdgeTargetCandidates method
        pass

    def getEdgeSourceCandidates(self, semanticOrigin: str, viewPoint: DDiagram) -> str:
        # TODO: Implement getEdgeSourceCandidates method
        pass

    def createEdge(self, semanticTarget: str, container: str, source: EdgeTarget, target: EdgeTarget) -> str:
        # TODO: Implement createEdge method
        pass

    def createEdge(self, source: EdgeTarget, target: EdgeTarget, semanticTarget: str) -> str:
        # TODO: Implement createEdge method
        pass

class DRepresentation:

    pass
class diagram_DDiagram(DRepresentation, description_DocumentedElement, DContainer, DValidable, DragAndDropTarget):

    def __init__(self, synchronized: bool, isInLayoutingMode: bool, headerHeight: int, diagram_DDiagram: set["diagram_DDiagramElement"] = None, diagram_DDiagram2: set["diagram_DDiagramElement"] = None, diagram_DDiagram9: set["diagram_DNode"] = None, diagram_DDiagram11: set["diagram_DNodeListElement"] = None, diagram_DDiagram13: set["diagram_DDiagramElementContainer"] = None, diagram_DDiagram15: "concern_ConcernDescription" = None, diagram_DDiagram5: "DiagramDescription" = None, diagram_DDiagram7: set["diagram_DEdge"] = None, diagram_DDiagram22: set["validation_ValidationRule"] = None, diagram_DDiagram24: set["tool_BehaviorTool"] = None, diagram_DDiagram26: "diagram_FilterVariableHistory" = None, diagram_DDiagram28: set["Layer"] = None, diagram_DDiagram30: set["diagram_DDiagramElement"] = None, diagram_DDiagram17: set["filter_FilterDescription"] = None, diagram_DDiagram19: set["filter_FilterDescription"] = None):
        self.synchronized = synchronized
        self.isInLayoutingMode = isInLayoutingMode
        self.headerHeight = headerHeight
        self.diagram_DDiagram = diagram_DDiagram if diagram_DDiagram is not None else set()
        self.diagram_DDiagram2 = diagram_DDiagram2 if diagram_DDiagram2 is not None else set()
        self.diagram_DDiagram9 = diagram_DDiagram9 if diagram_DDiagram9 is not None else set()
        self.diagram_DDiagram11 = diagram_DDiagram11 if diagram_DDiagram11 is not None else set()
        self.diagram_DDiagram13 = diagram_DDiagram13 if diagram_DDiagram13 is not None else set()
        self.diagram_DDiagram15 = diagram_DDiagram15
        self.diagram_DDiagram5 = diagram_DDiagram5
        self.diagram_DDiagram7 = diagram_DDiagram7 if diagram_DDiagram7 is not None else set()
        self.diagram_DDiagram22 = diagram_DDiagram22 if diagram_DDiagram22 is not None else set()
        self.diagram_DDiagram24 = diagram_DDiagram24 if diagram_DDiagram24 is not None else set()
        self.diagram_DDiagram26 = diagram_DDiagram26
        self.diagram_DDiagram28 = diagram_DDiagram28 if diagram_DDiagram28 is not None else set()
        self.diagram_DDiagram30 = diagram_DDiagram30 if diagram_DDiagram30 is not None else set()
        self.diagram_DDiagram17 = diagram_DDiagram17 if diagram_DDiagram17 is not None else set()
        self.diagram_DDiagram19 = diagram_DDiagram19 if diagram_DDiagram19 is not None else set()
        
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
    def diagram_DDiagram26(self):
        return self.__diagram_DDiagram26

    @diagram_DDiagram26.setter
    def diagram_DDiagram26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram26", None)
        self.__diagram_DDiagram26 = value
        
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
                if hasattr(item, "filter_FilterDescription20"):
                    opp_val = getattr(item, "filter_FilterDescription20", None)
                    
                    if opp_val == self:
                        setattr(item, "filter_FilterDescription20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filter_FilterDescription20"):
                    opp_val = getattr(item, "filter_FilterDescription20", None)
                    
                    setattr(item, "filter_FilterDescription20", self)
                    

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
                if hasattr(item, "diagram_DDiagramElement31"):
                    opp_val = getattr(item, "diagram_DDiagramElement31", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_DDiagramElement31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_DDiagramElement31"):
                    opp_val = getattr(item, "diagram_DDiagramElement31", None)
                    
                    setattr(item, "diagram_DDiagramElement31", self)
                    

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
    def diagram_DDiagram22(self):
        return self.__diagram_DDiagram22

    @diagram_DDiagram22.setter
    def diagram_DDiagram22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram22", None)
        self.__diagram_DDiagram22 = value if value is not None else set()
        
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
    def diagram_DDiagram28(self):
        return self.__diagram_DDiagram28

    @diagram_DDiagram28.setter
    def diagram_DDiagram28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagram__diagram_DDiagram28", None)
        self.__diagram_DDiagram28 = value if value is not None else set()
        
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
                    

    def getNodesFromMapping(self, mapping: str) -> str:
        # TODO: Implement getNodesFromMapping method
        pass

    def getEdgesFromMapping(self, mapping: str) -> str:
        # TODO: Implement getEdgesFromMapping method
        pass

    def getContainersFromMapping(self, mapping: str) -> str:
        # TODO: Implement getContainersFromMapping method
        pass

class diagram_DDiagramElement(DNavigable, DValidable, DRepresentationElement):

    def __init__(self, tooltipText: str, visible: bool, diagram_DDiagramElement: "diagram_DDiagram" = None, diagram_DDiagramElement3: "diagram_DDiagram" = None, diagram_DDiagramElement31: "diagram_DDiagram" = None, diagram_DDiagramElement33: set["Layer"] = None, diagram_DDiagramElement36: set["diagram_Decoration"] = None, diagram_DDiagramElement38: "DiagramElementMapping" = None, diagram_DDiagramElement40: set["diagram_GraphicalFilter"] = None, diagram_DDiagramElement61: "diagram_DDiagramElementContainer" = None, diagram_DDiagramElement73: "diagram_DNodeContainer" = None):
        self.tooltipText = tooltipText
        self.visible = visible
        self.diagram_DDiagramElement = diagram_DDiagramElement
        self.diagram_DDiagramElement3 = diagram_DDiagramElement3
        self.diagram_DDiagramElement31 = diagram_DDiagramElement31
        self.diagram_DDiagramElement33 = diagram_DDiagramElement33 if diagram_DDiagramElement33 is not None else set()
        self.diagram_DDiagramElement36 = diagram_DDiagramElement36 if diagram_DDiagramElement36 is not None else set()
        self.diagram_DDiagramElement38 = diagram_DDiagramElement38
        self.diagram_DDiagramElement40 = diagram_DDiagramElement40 if diagram_DDiagramElement40 is not None else set()
        self.diagram_DDiagramElement61 = diagram_DDiagramElement61
        self.diagram_DDiagramElement73 = diagram_DDiagramElement73
        
    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def tooltipText(self) -> str:
        return self.__tooltipText

    @tooltipText.setter
    def tooltipText(self, tooltipText: str):
        self.__tooltipText = tooltipText

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
    def diagram_DDiagramElement61(self):
        return self.__diagram_DDiagramElement61

    @diagram_DDiagramElement61.setter
    def diagram_DDiagramElement61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement61", None)
        self.__diagram_DDiagramElement61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagramElementContainer60"):
                opp_val = getattr(old_value, "diagram_DDiagramElementContainer60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagramElementContainer60"):
                opp_val = getattr(value, "diagram_DDiagramElementContainer60", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagramElementContainer60", set([self]))
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
    def diagram_DDiagramElement73(self):
        return self.__diagram_DDiagramElement73

    @diagram_DDiagramElement73.setter
    def diagram_DDiagramElement73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement73", None)
        self.__diagram_DDiagramElement73 = value
        
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
    def diagram_DDiagramElement36(self):
        return self.__diagram_DDiagramElement36

    @diagram_DDiagramElement36.setter
    def diagram_DDiagramElement36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement36", None)
        self.__diagram_DDiagramElement36 = value if value is not None else set()
        
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
                    

    @property
    def diagram_DDiagramElement33(self):
        return self.__diagram_DDiagramElement33

    @diagram_DDiagramElement33.setter
    def diagram_DDiagramElement33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement33", None)
        self.__diagram_DDiagramElement33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Layer34"):
                    opp_val = getattr(item, "Layer34", None)
                    
                    if opp_val == self:
                        setattr(item, "Layer34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Layer34"):
                    opp_val = getattr(item, "Layer34", None)
                    
                    setattr(item, "Layer34", self)
                    

    @property
    def diagram_DDiagramElement31(self):
        return self.__diagram_DDiagramElement31

    @diagram_DDiagramElement31.setter
    def diagram_DDiagramElement31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement31", None)
        self.__diagram_DDiagramElement31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagram30"):
                opp_val = getattr(old_value, "diagram_DDiagram30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagram30"):
                opp_val = getattr(value, "diagram_DDiagram30", None)
                if opp_val is None:
                    setattr(value, "diagram_DDiagram30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diagram_DDiagramElement38(self):
        return self.__diagram_DDiagramElement38

    @diagram_DDiagramElement38.setter
    def diagram_DDiagramElement38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DDiagramElement__diagram_DDiagramElement38", None)
        self.__diagram_DDiagramElement38 = value
        
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

    def getParentDiagram(self) -> DDiagram:
        # TODO: Implement getParentDiagram method
        pass
