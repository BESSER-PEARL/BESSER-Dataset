from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LayoutDirection(Enum):
    TopToBottom = "TopToBottom"
    LeftToRight = "LeftToRight"
    BottomToTop = "BottomToTop"
class EdgeRouting(Enum):
    straight = "straight"
    manhattan = "manhattan"
    tree = "tree"
class ContainerLabelDirection(Enum):
    Horizontal = "Horizontal"
    Vertical = "Vertical"
class BackgroundStyle(Enum):
    GradientLeftToRight = "GradientLeftToRight"
    Liquid = "Liquid"
    GradientTopToBottom = "GradientTopToBottom"
class CenteringStyle(Enum):
    None = "None"
    Both = "Both"
    Source = "Source"
    Target = "Target"
class LineStyle(Enum):
    solid = "solid"
    dash = "dash"
    dot = "dot"
    dash_dot = "dash_dot"
class FilterKind(Enum):
    HIDE = "HIDE"
    COLLAPSE = "COLLAPSE"
class EdgeArrows(Enum):
    OutputClosedArrow = "OutputClosedArrow"
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
class FoldingStyle(Enum):
    NONE = "NONE"
    SOURCE = "SOURCE"
    TARGET = "TARGET"
class BundledImageShape(Enum):
    square = "square"
    stroke = "stroke"
    triangle = "triangle"
    dot = "dot"
    ring = "ring"
    providedShape = "providedShape"
class ResizeKind(Enum):
    NONE = "NONE"
    NSEW = "NSEW"
    NORTH_SOUTH = "NORTH_SOUTH"
    EAST_WEST = "EAST_WEST"
class ArrangeConstraint(Enum):
    KEEP_LOCATION = "KEEP_LOCATION"
    KEEP_SIZE = "KEEP_SIZE"
    KEEP_RATIO = "KEEP_RATIO"
class ContainerLayout(Enum):
    FreeForm = "FreeForm"
    List = "List"
    HorizontalStack = "HorizontalStack"
    VerticalStack = "VerticalStack"
class LabelDirection(Enum):
    Horizontal = "Horizontal"
    Vertical = "Vertical"
class LabelPosition(Enum):
    border = "border"
    node = "node"
class Side(Enum):
    SOUTH = "SOUTH"
    EAST = "EAST"
    NORTH = "NORTH"
    WEST = "WEST"
class ContainerShape(Enum):
    parallelogram = "parallelogram"
class AlignmentKind(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
    SQUARE = "SQUARE"
class ReconnectionKind(Enum):
    RECONNECT_TARGET = "RECONNECT_TARGET"
    RECONNECT_SOURCE = "RECONNECT_SOURCE"
    RECONNECT_BOTH = "RECONNECT_BOTH"


############################################
# Definition of Classes
############################################

class Filter:

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
                if hasattr(item, "DiagramElementMapping451"):
                    opp_val = getattr(item, "DiagramElementMapping451", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping451", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping451"):
                    opp_val = getattr(item, "DiagramElementMapping451", None)
                    
                    setattr(item, "DiagramElementMapping451", self)
                    

class InteractiveVariableDescription:

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

class tool_ElementDropVariable:

    pass
class tool_InitialContainerDropOperation:

    pass
class RepresentationNavigationDescription:

    pass
class diagram_tool_DiagramNavigationDescription(RepresentationNavigationDescription):

    pass
class tool_DropContainerVariable:

    pass
class RepresentationCreationDescription:

    pass
class diagram_tool_DiagramCreationDescription(RepresentationCreationDescription):

    pass
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
            if hasattr(old_value, "DiagramDescription431"):
                opp_val = getattr(old_value, "DiagramDescription431", None)
                if opp_val == self:
                    setattr(old_value, "DiagramDescription431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramDescription431"):
                opp_val = getattr(value, "DiagramDescription431", None)
                setattr(value, "DiagramDescription431", self)

class diagram_tool_CreateView(ContainerModelOperation):

    def __init__(self, variableName: str, containerViewExpression: str, diagram_tool_CreateView: "DiagramElementMapping" = None):
        self.variableName = variableName
        self.containerViewExpression = containerViewExpression
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
            if hasattr(old_value, "DiagramElementMapping429"):
                opp_val = getattr(old_value, "DiagramElementMapping429", None)
                if opp_val == self:
                    setattr(old_value, "DiagramElementMapping429", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramElementMapping429"):
                opp_val = getattr(value, "DiagramElementMapping429", None)
                setattr(value, "DiagramElementMapping429", self)

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

class tool_VariableContainer:

    pass
class description_AbstractVariable:

    pass
class diagram_tool_NodeCreationVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class diagram_tool_SourceEdgeCreationVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class diagram_tool_ElementDoubleClickVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class diagram_tool_TargetEdgeViewCreationVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class diagram_tool_TargetEdgeCreationVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class diagram_tool_SourceEdgeViewCreationVariable(tool_VariableContainer, description_AbstractVariable):

    pass
class tool_EditMaskVariables:

    pass
class tool_ElementSelectVariable:

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
            if hasattr(old_value, "tool_InitialOperation427"):
                opp_val = getattr(old_value, "tool_InitialOperation427", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation427"):
                opp_val = getattr(value, "tool_InitialOperation427", None)
                setattr(value, "tool_InitialOperation427", self)

class diagram_tool_RequestDescription(AbstractToolDescription):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
                    

class diagram_tool_DeleteHookParameter:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
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

class tool_DeleteHook:

    pass
class tool_ElementDoubleClickVariable:

    pass
class tool_ElementDeleteVariable:

    pass
class tool_TargetEdgeViewCreationVariable:

    pass
class tool_SourceEdgeViewCreationVariable:

    pass
class tool_TargetEdgeCreationVariable:

    pass
class tool_InitEdgeCreationOperation:

    pass
class tool_SourceEdgeCreationVariable:

    pass
class tool_InitialNodeCreationOperation:

    pass
class tool_ContainerViewVariable:

    pass
class tool_ToolGroup:

    pass
class diagram_tool_ToolGroupExtension:

    pass
class tool_NodeCreationVariable:

    pass
class MappingBasedToolDescription:

    pass
class diagram_tool_DirectEditLabel(MappingBasedToolDescription):

    def __init__(self, inputLabelExpression: str, diagram_tool_DirectEditLabel: "tool_EditMaskVariables" = None, diagram_tool_DirectEditLabel424: "tool_InitialOperation" = None):
        self.inputLabelExpression = inputLabelExpression
        self.diagram_tool_DirectEditLabel = diagram_tool_DirectEditLabel
        self.diagram_tool_DirectEditLabel424 = diagram_tool_DirectEditLabel424
        
    @property
    def inputLabelExpression(self) -> str:
        return self.__inputLabelExpression

    @inputLabelExpression.setter
    def inputLabelExpression(self, inputLabelExpression: str):
        self.__inputLabelExpression = inputLabelExpression

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

    @property
    def diagram_tool_DirectEditLabel424(self):
        return self.__diagram_tool_DirectEditLabel424

    @diagram_tool_DirectEditLabel424.setter
    def diagram_tool_DirectEditLabel424(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DirectEditLabel__diagram_tool_DirectEditLabel424", None)
        self.__diagram_tool_DirectEditLabel424 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation425"):
                opp_val = getattr(old_value, "tool_InitialOperation425", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation425", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation425"):
                opp_val = getattr(value, "tool_InitialOperation425", None)
                setattr(value, "tool_InitialOperation425", self)

    def getMapping(self) -> str:
        # TODO: Implement getMapping method
        pass

class diagram_tool_ContainerCreationDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, diagram_tool_ContainerCreationDescription372: "tool_ContainerViewVariable" = None, diagram_tool_ContainerCreationDescription: set["ContainerMapping"] = None, diagram_tool_ContainerCreationDescription369: "tool_NodeCreationVariable" = None, diagram_tool_ContainerCreationDescription375: "tool_InitialNodeCreationOperation" = None, diagram_tool_ContainerCreationDescription378: set["AbstractNodeMapping"] = None):
        self.iconPath = iconPath
        self.diagram_tool_ContainerCreationDescription372 = diagram_tool_ContainerCreationDescription372
        self.diagram_tool_ContainerCreationDescription = diagram_tool_ContainerCreationDescription if diagram_tool_ContainerCreationDescription is not None else set()
        self.diagram_tool_ContainerCreationDescription369 = diagram_tool_ContainerCreationDescription369
        self.diagram_tool_ContainerCreationDescription375 = diagram_tool_ContainerCreationDescription375
        self.diagram_tool_ContainerCreationDescription378 = diagram_tool_ContainerCreationDescription378 if diagram_tool_ContainerCreationDescription378 is not None else set()
        
    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def diagram_tool_ContainerCreationDescription369(self):
        return self.__diagram_tool_ContainerCreationDescription369

    @diagram_tool_ContainerCreationDescription369.setter
    def diagram_tool_ContainerCreationDescription369(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription369", None)
        self.__diagram_tool_ContainerCreationDescription369 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_NodeCreationVariable370"):
                opp_val = getattr(old_value, "tool_NodeCreationVariable370", None)
                if opp_val == self:
                    setattr(old_value, "tool_NodeCreationVariable370", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_NodeCreationVariable370"):
                opp_val = getattr(value, "tool_NodeCreationVariable370", None)
                setattr(value, "tool_NodeCreationVariable370", self)

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
                if hasattr(item, "ContainerMapping367"):
                    opp_val = getattr(item, "ContainerMapping367", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping367", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping367"):
                    opp_val = getattr(item, "ContainerMapping367", None)
                    
                    setattr(item, "ContainerMapping367", self)
                    

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
            if hasattr(old_value, "tool_InitialNodeCreationOperation376"):
                opp_val = getattr(old_value, "tool_InitialNodeCreationOperation376", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialNodeCreationOperation376", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialNodeCreationOperation376"):
                opp_val = getattr(value, "tool_InitialNodeCreationOperation376", None)
                setattr(value, "tool_InitialNodeCreationOperation376", self)

    @property
    def diagram_tool_ContainerCreationDescription378(self):
        return self.__diagram_tool_ContainerCreationDescription378

    @diagram_tool_ContainerCreationDescription378.setter
    def diagram_tool_ContainerCreationDescription378(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription378", None)
        self.__diagram_tool_ContainerCreationDescription378 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractNodeMapping379"):
                    opp_val = getattr(item, "AbstractNodeMapping379", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractNodeMapping379", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractNodeMapping379"):
                    opp_val = getattr(item, "AbstractNodeMapping379", None)
                    
                    setattr(item, "AbstractNodeMapping379", self)
                    

    @property
    def diagram_tool_ContainerCreationDescription372(self):
        return self.__diagram_tool_ContainerCreationDescription372

    @diagram_tool_ContainerCreationDescription372.setter
    def diagram_tool_ContainerCreationDescription372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerCreationDescription__diagram_tool_ContainerCreationDescription372", None)
        self.__diagram_tool_ContainerCreationDescription372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable373"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable373", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable373", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable373"):
                opp_val = getattr(value, "tool_ContainerViewVariable373", None)
                setattr(value, "tool_ContainerViewVariable373", self)

class diagram_tool_EdgeCreationDescription(MappingBasedToolDescription):

    def __init__(self, connectionStartPrecondition: str, iconPath: str, diagram_tool_EdgeCreationDescription: set["EdgeMapping"] = None, diagram_tool_EdgeCreationDescription351: "tool_SourceEdgeCreationVariable" = None, diagram_tool_EdgeCreationDescription359: "tool_InitEdgeCreationOperation" = None, diagram_tool_EdgeCreationDescription353: "tool_TargetEdgeCreationVariable" = None, diagram_tool_EdgeCreationDescription355: "tool_SourceEdgeViewCreationVariable" = None, diagram_tool_EdgeCreationDescription357: "tool_TargetEdgeViewCreationVariable" = None, diagram_tool_EdgeCreationDescription361: set["DiagramElementMapping"] = None, diagram_tool_EdgeCreationDescription364: set["DiagramElementMapping"] = None):
        self.connectionStartPrecondition = connectionStartPrecondition
        self.iconPath = iconPath
        self.diagram_tool_EdgeCreationDescription = diagram_tool_EdgeCreationDescription if diagram_tool_EdgeCreationDescription is not None else set()
        self.diagram_tool_EdgeCreationDescription351 = diagram_tool_EdgeCreationDescription351
        self.diagram_tool_EdgeCreationDescription359 = diagram_tool_EdgeCreationDescription359
        self.diagram_tool_EdgeCreationDescription353 = diagram_tool_EdgeCreationDescription353
        self.diagram_tool_EdgeCreationDescription355 = diagram_tool_EdgeCreationDescription355
        self.diagram_tool_EdgeCreationDescription357 = diagram_tool_EdgeCreationDescription357
        self.diagram_tool_EdgeCreationDescription361 = diagram_tool_EdgeCreationDescription361 if diagram_tool_EdgeCreationDescription361 is not None else set()
        self.diagram_tool_EdgeCreationDescription364 = diagram_tool_EdgeCreationDescription364 if diagram_tool_EdgeCreationDescription364 is not None else set()
        
    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def connectionStartPrecondition(self) -> str:
        return self.__connectionStartPrecondition

    @connectionStartPrecondition.setter
    def connectionStartPrecondition(self, connectionStartPrecondition: str):
        self.__connectionStartPrecondition = connectionStartPrecondition

    @property
    def diagram_tool_EdgeCreationDescription361(self):
        return self.__diagram_tool_EdgeCreationDescription361

    @diagram_tool_EdgeCreationDescription361.setter
    def diagram_tool_EdgeCreationDescription361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription361", None)
        self.__diagram_tool_EdgeCreationDescription361 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping362"):
                    opp_val = getattr(item, "DiagramElementMapping362", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping362", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping362"):
                    opp_val = getattr(item, "DiagramElementMapping362", None)
                    
                    setattr(item, "DiagramElementMapping362", self)
                    

    @property
    def diagram_tool_EdgeCreationDescription364(self):
        return self.__diagram_tool_EdgeCreationDescription364

    @diagram_tool_EdgeCreationDescription364.setter
    def diagram_tool_EdgeCreationDescription364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription364", None)
        self.__diagram_tool_EdgeCreationDescription364 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping365"):
                    opp_val = getattr(item, "DiagramElementMapping365", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping365", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping365"):
                    opp_val = getattr(item, "DiagramElementMapping365", None)
                    
                    setattr(item, "DiagramElementMapping365", self)
                    

    @property
    def diagram_tool_EdgeCreationDescription353(self):
        return self.__diagram_tool_EdgeCreationDescription353

    @diagram_tool_EdgeCreationDescription353.setter
    def diagram_tool_EdgeCreationDescription353(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription353", None)
        self.__diagram_tool_EdgeCreationDescription353 = value
        
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
                if hasattr(item, "EdgeMapping349"):
                    opp_val = getattr(item, "EdgeMapping349", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping349", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping349"):
                    opp_val = getattr(item, "EdgeMapping349", None)
                    
                    setattr(item, "EdgeMapping349", self)
                    

    @property
    def diagram_tool_EdgeCreationDescription351(self):
        return self.__diagram_tool_EdgeCreationDescription351

    @diagram_tool_EdgeCreationDescription351.setter
    def diagram_tool_EdgeCreationDescription351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription351", None)
        self.__diagram_tool_EdgeCreationDescription351 = value
        
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
    def diagram_tool_EdgeCreationDescription357(self):
        return self.__diagram_tool_EdgeCreationDescription357

    @diagram_tool_EdgeCreationDescription357.setter
    def diagram_tool_EdgeCreationDescription357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription357", None)
        self.__diagram_tool_EdgeCreationDescription357 = value
        
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
    def diagram_tool_EdgeCreationDescription359(self):
        return self.__diagram_tool_EdgeCreationDescription359

    @diagram_tool_EdgeCreationDescription359.setter
    def diagram_tool_EdgeCreationDescription359(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription359", None)
        self.__diagram_tool_EdgeCreationDescription359 = value
        
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
    def diagram_tool_EdgeCreationDescription355(self):
        return self.__diagram_tool_EdgeCreationDescription355

    @diagram_tool_EdgeCreationDescription355.setter
    def diagram_tool_EdgeCreationDescription355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_EdgeCreationDescription__diagram_tool_EdgeCreationDescription355", None)
        self.__diagram_tool_EdgeCreationDescription355 = value
        
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

    def getBestMapping(self, target: EdgeTarget, source: EdgeTarget, createdElements: str) -> str:
        # TODO: Implement getBestMapping method
        pass

class diagram_tool_DoubleClickDescription(MappingBasedToolDescription):

    pass
class diagram_tool_NodeCreationDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, diagram_tool_NodeCreationDescription: set["NodeMapping"] = None, diagram_tool_NodeCreationDescription346: set["AbstractNodeMapping"] = None, diagram_tool_NodeCreationDescription340: "tool_NodeCreationVariable" = None, diagram_tool_NodeCreationDescription342: "tool_ContainerViewVariable" = None, diagram_tool_NodeCreationDescription344: "tool_InitialNodeCreationOperation" = None):
        self.iconPath = iconPath
        self.diagram_tool_NodeCreationDescription = diagram_tool_NodeCreationDescription if diagram_tool_NodeCreationDescription is not None else set()
        self.diagram_tool_NodeCreationDescription346 = diagram_tool_NodeCreationDescription346 if diagram_tool_NodeCreationDescription346 is not None else set()
        self.diagram_tool_NodeCreationDescription340 = diagram_tool_NodeCreationDescription340
        self.diagram_tool_NodeCreationDescription342 = diagram_tool_NodeCreationDescription342
        self.diagram_tool_NodeCreationDescription344 = diagram_tool_NodeCreationDescription344
        
    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def diagram_tool_NodeCreationDescription340(self):
        return self.__diagram_tool_NodeCreationDescription340

    @diagram_tool_NodeCreationDescription340.setter
    def diagram_tool_NodeCreationDescription340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription340", None)
        self.__diagram_tool_NodeCreationDescription340 = value
        
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
    def diagram_tool_NodeCreationDescription344(self):
        return self.__diagram_tool_NodeCreationDescription344

    @diagram_tool_NodeCreationDescription344.setter
    def diagram_tool_NodeCreationDescription344(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription344", None)
        self.__diagram_tool_NodeCreationDescription344 = value
        
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
    def diagram_tool_NodeCreationDescription346(self):
        return self.__diagram_tool_NodeCreationDescription346

    @diagram_tool_NodeCreationDescription346.setter
    def diagram_tool_NodeCreationDescription346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription346", None)
        self.__diagram_tool_NodeCreationDescription346 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractNodeMapping347"):
                    opp_val = getattr(item, "AbstractNodeMapping347", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractNodeMapping347", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractNodeMapping347"):
                    opp_val = getattr(item, "AbstractNodeMapping347", None)
                    
                    setattr(item, "AbstractNodeMapping347", self)
                    

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
                if hasattr(item, "NodeMapping338"):
                    opp_val = getattr(item, "NodeMapping338", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping338", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping338"):
                    opp_val = getattr(item, "NodeMapping338", None)
                    
                    setattr(item, "NodeMapping338", self)
                    

    @property
    def diagram_tool_NodeCreationDescription342(self):
        return self.__diagram_tool_NodeCreationDescription342

    @diagram_tool_NodeCreationDescription342.setter
    def diagram_tool_NodeCreationDescription342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_NodeCreationDescription__diagram_tool_NodeCreationDescription342", None)
        self.__diagram_tool_NodeCreationDescription342 = value
        
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

class diagram_tool_DeleteElementDescription(MappingBasedToolDescription):

    def __init__(self, diagram_tool_DeleteElementDescription: "tool_ElementDeleteVariable" = None, diagram_tool_DeleteElementDescription382: "tool_ElementDeleteVariable" = None, diagram_tool_DeleteElementDescription385: "tool_ContainerViewVariable" = None, diagram_tool_DeleteElementDescription388: "tool_InitialOperation" = None, diagram_tool_DeleteElementDescription391: "tool_DeleteHook" = None):
        self.diagram_tool_DeleteElementDescription = diagram_tool_DeleteElementDescription
        self.diagram_tool_DeleteElementDescription382 = diagram_tool_DeleteElementDescription382
        self.diagram_tool_DeleteElementDescription385 = diagram_tool_DeleteElementDescription385
        self.diagram_tool_DeleteElementDescription388 = diagram_tool_DeleteElementDescription388
        self.diagram_tool_DeleteElementDescription391 = diagram_tool_DeleteElementDescription391
        
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
    def diagram_tool_DeleteElementDescription382(self):
        return self.__diagram_tool_DeleteElementDescription382

    @diagram_tool_DeleteElementDescription382.setter
    def diagram_tool_DeleteElementDescription382(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription382", None)
        self.__diagram_tool_DeleteElementDescription382 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementDeleteVariable383"):
                opp_val = getattr(old_value, "tool_ElementDeleteVariable383", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementDeleteVariable383", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementDeleteVariable383"):
                opp_val = getattr(value, "tool_ElementDeleteVariable383", None)
                setattr(value, "tool_ElementDeleteVariable383", self)

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
    def diagram_tool_DeleteElementDescription385(self):
        return self.__diagram_tool_DeleteElementDescription385

    @diagram_tool_DeleteElementDescription385.setter
    def diagram_tool_DeleteElementDescription385(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_DeleteElementDescription__diagram_tool_DeleteElementDescription385", None)
        self.__diagram_tool_DeleteElementDescription385 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable386"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable386", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable386", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable386"):
                opp_val = getattr(value, "tool_ContainerViewVariable386", None)
                setattr(value, "tool_ContainerViewVariable386", self)

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
            if hasattr(old_value, "tool_InitialOperation389"):
                opp_val = getattr(old_value, "tool_InitialOperation389", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation389", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation389"):
                opp_val = getattr(value, "tool_InitialOperation389", None)
                setattr(value, "tool_InitialOperation389", self)

    def getMappings(self) -> str:
        # TODO: Implement getMappings method
        pass

class diagram_tool_ReconnectEdgeDescription(MappingBasedToolDescription):

    def __init__(self, reconnectionKind: str, diagram_tool_ReconnectEdgeDescription406: "tool_TargetEdgeCreationVariable" = None, diagram_tool_ReconnectEdgeDescription409: "tool_SourceEdgeViewCreationVariable" = None, diagram_tool_ReconnectEdgeDescription: "tool_SourceEdgeCreationVariable" = None, diagram_tool_ReconnectEdgeDescription420: "tool_ElementSelectVariable" = None, diagram_tool_ReconnectEdgeDescription412: "tool_TargetEdgeViewCreationVariable" = None, diagram_tool_ReconnectEdgeDescription415: "tool_ElementSelectVariable" = None, diagram_tool_ReconnectEdgeDescription417: "tool_InitialOperation" = None):
        self.reconnectionKind = reconnectionKind
        self.diagram_tool_ReconnectEdgeDescription406 = diagram_tool_ReconnectEdgeDescription406
        self.diagram_tool_ReconnectEdgeDescription409 = diagram_tool_ReconnectEdgeDescription409
        self.diagram_tool_ReconnectEdgeDescription = diagram_tool_ReconnectEdgeDescription
        self.diagram_tool_ReconnectEdgeDescription420 = diagram_tool_ReconnectEdgeDescription420
        self.diagram_tool_ReconnectEdgeDescription412 = diagram_tool_ReconnectEdgeDescription412
        self.diagram_tool_ReconnectEdgeDescription415 = diagram_tool_ReconnectEdgeDescription415
        self.diagram_tool_ReconnectEdgeDescription417 = diagram_tool_ReconnectEdgeDescription417
        
    @property
    def reconnectionKind(self) -> str:
        return self.__reconnectionKind

    @reconnectionKind.setter
    def reconnectionKind(self, reconnectionKind: str):
        self.__reconnectionKind = reconnectionKind

    @property
    def diagram_tool_ReconnectEdgeDescription409(self):
        return self.__diagram_tool_ReconnectEdgeDescription409

    @diagram_tool_ReconnectEdgeDescription409.setter
    def diagram_tool_ReconnectEdgeDescription409(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription409", None)
        self.__diagram_tool_ReconnectEdgeDescription409 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SourceEdgeViewCreationVariable410"):
                opp_val = getattr(old_value, "tool_SourceEdgeViewCreationVariable410", None)
                if opp_val == self:
                    setattr(old_value, "tool_SourceEdgeViewCreationVariable410", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SourceEdgeViewCreationVariable410"):
                opp_val = getattr(value, "tool_SourceEdgeViewCreationVariable410", None)
                setattr(value, "tool_SourceEdgeViewCreationVariable410", self)

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
    def diagram_tool_ReconnectEdgeDescription417(self):
        return self.__diagram_tool_ReconnectEdgeDescription417

    @diagram_tool_ReconnectEdgeDescription417.setter
    def diagram_tool_ReconnectEdgeDescription417(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription417", None)
        self.__diagram_tool_ReconnectEdgeDescription417 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation418"):
                opp_val = getattr(old_value, "tool_InitialOperation418", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation418", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation418"):
                opp_val = getattr(value, "tool_InitialOperation418", None)
                setattr(value, "tool_InitialOperation418", self)

    @property
    def diagram_tool_ReconnectEdgeDescription406(self):
        return self.__diagram_tool_ReconnectEdgeDescription406

    @diagram_tool_ReconnectEdgeDescription406.setter
    def diagram_tool_ReconnectEdgeDescription406(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription406", None)
        self.__diagram_tool_ReconnectEdgeDescription406 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_TargetEdgeCreationVariable407"):
                opp_val = getattr(old_value, "tool_TargetEdgeCreationVariable407", None)
                if opp_val == self:
                    setattr(old_value, "tool_TargetEdgeCreationVariable407", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_TargetEdgeCreationVariable407"):
                opp_val = getattr(value, "tool_TargetEdgeCreationVariable407", None)
                setattr(value, "tool_TargetEdgeCreationVariable407", self)

    @property
    def diagram_tool_ReconnectEdgeDescription420(self):
        return self.__diagram_tool_ReconnectEdgeDescription420

    @diagram_tool_ReconnectEdgeDescription420.setter
    def diagram_tool_ReconnectEdgeDescription420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ReconnectEdgeDescription__diagram_tool_ReconnectEdgeDescription420", None)
        self.__diagram_tool_ReconnectEdgeDescription420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementSelectVariable421"):
                opp_val = getattr(old_value, "tool_ElementSelectVariable421", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementSelectVariable421", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementSelectVariable421"):
                opp_val = getattr(value, "tool_ElementSelectVariable421", None)
                setattr(value, "tool_ElementSelectVariable421", self)

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
            if hasattr(old_value, "tool_TargetEdgeViewCreationVariable413"):
                opp_val = getattr(old_value, "tool_TargetEdgeViewCreationVariable413", None)
                if opp_val == self:
                    setattr(old_value, "tool_TargetEdgeViewCreationVariable413", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_TargetEdgeViewCreationVariable413"):
                opp_val = getattr(value, "tool_TargetEdgeViewCreationVariable413", None)
                setattr(value, "tool_TargetEdgeViewCreationVariable413", self)

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
            if hasattr(old_value, "tool_SourceEdgeCreationVariable404"):
                opp_val = getattr(old_value, "tool_SourceEdgeCreationVariable404", None)
                if opp_val == self:
                    setattr(old_value, "tool_SourceEdgeCreationVariable404", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SourceEdgeCreationVariable404"):
                opp_val = getattr(value, "tool_SourceEdgeCreationVariable404", None)
                setattr(value, "tool_SourceEdgeCreationVariable404", self)

    def getMappings(self) -> str:
        # TODO: Implement getMappings method
        pass

class diagram_tool_ContainerDropDescription(MappingBasedToolDescription):

    def __init__(self, dragSource: str, moveEdges: bool, diagram_tool_ContainerDropDescription: set["DiagramElementMapping"] = None, diagram_tool_ContainerDropDescription439: "tool_DropContainerVariable" = None, diagram_tool_ContainerDropDescription449: "tool_InitialContainerDropOperation" = None, diagram_tool_ContainerDropDescription441: "tool_DropContainerVariable" = None, diagram_tool_ContainerDropDescription444: "tool_ElementDropVariable" = None, diagram_tool_ContainerDropDescription446: "tool_ContainerViewVariable" = None):
        self.dragSource = dragSource
        self.moveEdges = moveEdges
        self.diagram_tool_ContainerDropDescription = diagram_tool_ContainerDropDescription if diagram_tool_ContainerDropDescription is not None else set()
        self.diagram_tool_ContainerDropDescription439 = diagram_tool_ContainerDropDescription439
        self.diagram_tool_ContainerDropDescription449 = diagram_tool_ContainerDropDescription449
        self.diagram_tool_ContainerDropDescription441 = diagram_tool_ContainerDropDescription441
        self.diagram_tool_ContainerDropDescription444 = diagram_tool_ContainerDropDescription444
        self.diagram_tool_ContainerDropDescription446 = diagram_tool_ContainerDropDescription446
        
    @property
    def dragSource(self) -> str:
        return self.__dragSource

    @dragSource.setter
    def dragSource(self, dragSource: str):
        self.__dragSource = dragSource

    @property
    def moveEdges(self) -> bool:
        return self.__moveEdges

    @moveEdges.setter
    def moveEdges(self, moveEdges: bool):
        self.__moveEdges = moveEdges

    @property
    def diagram_tool_ContainerDropDescription446(self):
        return self.__diagram_tool_ContainerDropDescription446

    @diagram_tool_ContainerDropDescription446.setter
    def diagram_tool_ContainerDropDescription446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription446", None)
        self.__diagram_tool_ContainerDropDescription446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable447"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable447", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable447", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable447"):
                opp_val = getattr(value, "tool_ContainerViewVariable447", None)
                setattr(value, "tool_ContainerViewVariable447", self)

    @property
    def diagram_tool_ContainerDropDescription439(self):
        return self.__diagram_tool_ContainerDropDescription439

    @diagram_tool_ContainerDropDescription439.setter
    def diagram_tool_ContainerDropDescription439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription439", None)
        self.__diagram_tool_ContainerDropDescription439 = value
        
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
    def diagram_tool_ContainerDropDescription449(self):
        return self.__diagram_tool_ContainerDropDescription449

    @diagram_tool_ContainerDropDescription449.setter
    def diagram_tool_ContainerDropDescription449(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription449", None)
        self.__diagram_tool_ContainerDropDescription449 = value
        
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
                if hasattr(item, "DiagramElementMapping437"):
                    opp_val = getattr(item, "DiagramElementMapping437", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping437", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping437"):
                    opp_val = getattr(item, "DiagramElementMapping437", None)
                    
                    setattr(item, "DiagramElementMapping437", self)
                    

    @property
    def diagram_tool_ContainerDropDescription444(self):
        return self.__diagram_tool_ContainerDropDescription444

    @diagram_tool_ContainerDropDescription444.setter
    def diagram_tool_ContainerDropDescription444(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription444", None)
        self.__diagram_tool_ContainerDropDescription444 = value
        
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
    def diagram_tool_ContainerDropDescription441(self):
        return self.__diagram_tool_ContainerDropDescription441

    @diagram_tool_ContainerDropDescription441.setter
    def diagram_tool_ContainerDropDescription441(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ContainerDropDescription__diagram_tool_ContainerDropDescription441", None)
        self.__diagram_tool_ContainerDropDescription441 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DropContainerVariable442"):
                opp_val = getattr(old_value, "tool_DropContainerVariable442", None)
                if opp_val == self:
                    setattr(old_value, "tool_DropContainerVariable442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DropContainerVariable442"):
                opp_val = getattr(value, "tool_DropContainerVariable442", None)
                setattr(value, "tool_DropContainerVariable442", self)

    def getContainers(self) -> str:
        # TODO: Implement getContainers method
        pass

    def getBestMapping(self, droppedElement: str, targetContainer: DragAndDropTarget) -> str:
        # TODO: Implement getBestMapping method
        pass

class tool_PopupMenu:

    pass
class ToolEntry:

    pass
class diagram_tool_ToolGroup(ToolEntry):

    pass
class tool_ToolGroupExtension:

    pass
class tool_ToolEntry:

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
class BasicLabelStyleDescription:

    pass
class diagram_style_BeginLabelStyleDescription(BasicLabelStyleDescription):

    pass
class diagram_style_EndLabelStyleDescription(BasicLabelStyleDescription):

    pass
class diagram_style_CenterLabelStyleDescription(BasicLabelStyleDescription):

    pass
class style_EndLabelStyleDescription:

    pass
class style_CenterLabelStyleDescription:

    pass
class style_BeginLabelStyleDescription:

    pass
class style_SizeComputationContainerStyleDescription:

    pass
class style_RoundedCornerStyleDescription:

    pass
class style_LabelBorderStyleDescription:

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

    def __init__(self, maxValueExpression: str, valueExpression: str, minValueExpression: str, label: str, diagram_style_GaugeSectionDescription: "ColorDescription" = None, diagram_style_GaugeSectionDescription295: "ColorDescription" = None):
        self.maxValueExpression = maxValueExpression
        self.valueExpression = valueExpression
        self.minValueExpression = minValueExpression
        self.label = label
        self.diagram_style_GaugeSectionDescription = diagram_style_GaugeSectionDescription
        self.diagram_style_GaugeSectionDescription295 = diagram_style_GaugeSectionDescription295
        
    @property
    def minValueExpression(self) -> str:
        return self.__minValueExpression

    @minValueExpression.setter
    def minValueExpression(self, minValueExpression: str):
        self.__minValueExpression = minValueExpression

    @property
    def valueExpression(self) -> str:
        return self.__valueExpression

    @valueExpression.setter
    def valueExpression(self, valueExpression: str):
        self.__valueExpression = valueExpression

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
    def diagram_style_GaugeSectionDescription295(self):
        return self.__diagram_style_GaugeSectionDescription295

    @diagram_style_GaugeSectionDescription295.setter
    def diagram_style_GaugeSectionDescription295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_GaugeSectionDescription__diagram_style_GaugeSectionDescription295", None)
        self.__diagram_style_GaugeSectionDescription295 = value
        
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
            if hasattr(old_value, "ColorDescription293"):
                opp_val = getattr(old_value, "ColorDescription293", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription293", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription293"):
                opp_val = getattr(value, "ColorDescription293", None)
                setattr(value, "ColorDescription293", self)

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
            if hasattr(old_value, "ColorDescription286"):
                opp_val = getattr(old_value, "ColorDescription286", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription286", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription286"):
                opp_val = getattr(value, "ColorDescription286", None)
                setattr(value, "ColorDescription286", self)

class diagram_style_NoteDescription(NodeStyleDescription):

    pass
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
            if hasattr(old_value, "ColorDescription290"):
                opp_val = getattr(old_value, "ColorDescription290", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription290", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription290"):
                opp_val = getattr(value, "ColorDescription290", None)
                setattr(value, "ColorDescription290", self)

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
            if hasattr(old_value, "ColorDescription280"):
                opp_val = getattr(old_value, "ColorDescription280", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription280", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription280"):
                opp_val = getattr(value, "ColorDescription280", None)
                setattr(value, "ColorDescription280", self)

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
            if hasattr(old_value, "ColorDescription282"):
                opp_val = getattr(old_value, "ColorDescription282", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription282", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription282"):
                opp_val = getattr(value, "ColorDescription282", None)
                setattr(value, "ColorDescription282", self)

class diagram_style_CustomStyleDescription(NodeStyleDescription):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class diagram_style_EllipseNodeDescription(NodeStyleDescription):

    def __init__(self, horizontalDiameterComputationExpression: str, verticalDiameterComputationExpression: str, diagram_style_EllipseNodeDescription: "ColorDescription" = None):
        self.horizontalDiameterComputationExpression = horizontalDiameterComputationExpression
        self.verticalDiameterComputationExpression = verticalDiameterComputationExpression
        self.diagram_style_EllipseNodeDescription = diagram_style_EllipseNodeDescription
        
    @property
    def horizontalDiameterComputationExpression(self) -> str:
        return self.__horizontalDiameterComputationExpression

    @horizontalDiameterComputationExpression.setter
    def horizontalDiameterComputationExpression(self, horizontalDiameterComputationExpression: str):
        self.__horizontalDiameterComputationExpression = horizontalDiameterComputationExpression

    @property
    def verticalDiameterComputationExpression(self) -> str:
        return self.__verticalDiameterComputationExpression

    @verticalDiameterComputationExpression.setter
    def verticalDiameterComputationExpression(self, verticalDiameterComputationExpression: str):
        self.__verticalDiameterComputationExpression = verticalDiameterComputationExpression

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
            if hasattr(old_value, "ColorDescription284"):
                opp_val = getattr(old_value, "ColorDescription284", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription284"):
                opp_val = getattr(value, "ColorDescription284", None)
                setattr(value, "ColorDescription284", self)

class StyleDescription:

    pass
class diagram_style_EdgeStyleDescription(StyleDescription):

    def __init__(self, lineStyle: str, sourceArrow: str, targetArrow: str, sizeComputationExpression: str, routingStyle: str, foldingStyle: str, endsCentering: str, diagram_style_EdgeStyleDescription: "ColorDescription" = None, diagram_style_EdgeStyleDescription315: set["DiagramElementMapping"] = None, diagram_style_EdgeStyleDescription309: "style_BeginLabelStyleDescription" = None, diagram_style_EdgeStyleDescription311: "style_CenterLabelStyleDescription" = None, diagram_style_EdgeStyleDescription313: "style_EndLabelStyleDescription" = None, diagram_style_EdgeStyleDescription318: set["DiagramElementMapping"] = None):
        self.lineStyle = lineStyle
        self.sourceArrow = sourceArrow
        self.targetArrow = targetArrow
        self.sizeComputationExpression = sizeComputationExpression
        self.routingStyle = routingStyle
        self.foldingStyle = foldingStyle
        self.endsCentering = endsCentering
        self.diagram_style_EdgeStyleDescription = diagram_style_EdgeStyleDescription
        self.diagram_style_EdgeStyleDescription315 = diagram_style_EdgeStyleDescription315 if diagram_style_EdgeStyleDescription315 is not None else set()
        self.diagram_style_EdgeStyleDescription309 = diagram_style_EdgeStyleDescription309
        self.diagram_style_EdgeStyleDescription311 = diagram_style_EdgeStyleDescription311
        self.diagram_style_EdgeStyleDescription313 = diagram_style_EdgeStyleDescription313
        self.diagram_style_EdgeStyleDescription318 = diagram_style_EdgeStyleDescription318 if diagram_style_EdgeStyleDescription318 is not None else set()
        
    @property
    def endsCentering(self) -> str:
        return self.__endsCentering

    @endsCentering.setter
    def endsCentering(self, endsCentering: str):
        self.__endsCentering = endsCentering

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
    def diagram_style_EdgeStyleDescription313(self):
        return self.__diagram_style_EdgeStyleDescription313

    @diagram_style_EdgeStyleDescription313.setter
    def diagram_style_EdgeStyleDescription313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription313", None)
        self.__diagram_style_EdgeStyleDescription313 = value
        
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
            if hasattr(old_value, "ColorDescription307"):
                opp_val = getattr(old_value, "ColorDescription307", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription307"):
                opp_val = getattr(value, "ColorDescription307", None)
                setattr(value, "ColorDescription307", self)

    @property
    def diagram_style_EdgeStyleDescription309(self):
        return self.__diagram_style_EdgeStyleDescription309

    @diagram_style_EdgeStyleDescription309.setter
    def diagram_style_EdgeStyleDescription309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription309", None)
        self.__diagram_style_EdgeStyleDescription309 = value
        
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
    def diagram_style_EdgeStyleDescription311(self):
        return self.__diagram_style_EdgeStyleDescription311

    @diagram_style_EdgeStyleDescription311.setter
    def diagram_style_EdgeStyleDescription311(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription311", None)
        self.__diagram_style_EdgeStyleDescription311 = value
        
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
    def diagram_style_EdgeStyleDescription318(self):
        return self.__diagram_style_EdgeStyleDescription318

    @diagram_style_EdgeStyleDescription318.setter
    def diagram_style_EdgeStyleDescription318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription318", None)
        self.__diagram_style_EdgeStyleDescription318 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping319"):
                    opp_val = getattr(item, "DiagramElementMapping319", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping319", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping319"):
                    opp_val = getattr(item, "DiagramElementMapping319", None)
                    
                    setattr(item, "DiagramElementMapping319", self)
                    

    @property
    def diagram_style_EdgeStyleDescription315(self):
        return self.__diagram_style_EdgeStyleDescription315

    @diagram_style_EdgeStyleDescription315.setter
    def diagram_style_EdgeStyleDescription315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_EdgeStyleDescription__diagram_style_EdgeStyleDescription315", None)
        self.__diagram_style_EdgeStyleDescription315 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping316"):
                    opp_val = getattr(item, "DiagramElementMapping316", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping316", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping316"):
                    opp_val = getattr(item, "DiagramElementMapping316", None)
                    
                    setattr(item, "DiagramElementMapping316", self)
                    

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

    def __init__(self, borderLineStyle: str, borderSizeComputationExpression: str, diagram_style_BorderedStyleDescription: "ColorDescription" = None):
        self.borderLineStyle = borderLineStyle
        self.borderSizeComputationExpression = borderSizeComputationExpression
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
class Customization:

    pass
class style_HideLabelCapabilityStyleDescription:

    pass
class style_TooltipStyleDescription:

    pass
class style_LabelStyleDescription:

    pass
class style_BorderedStyleDescription:

    pass
class diagram_style_ContainerStyleDescription(style_TooltipStyleDescription, style_BorderedStyleDescription, style_HideLabelCapabilityStyleDescription, style_RoundedCornerStyleDescription, style_LabelStyleDescription):

    def __init__(self, roundedCorner: bool, containerLabelDirection: str):
        self.roundedCorner = roundedCorner
        self.containerLabelDirection = containerLabelDirection
        
    @property
    def roundedCorner(self) -> bool:
        return self.__roundedCorner

    @roundedCorner.setter
    def roundedCorner(self, roundedCorner: bool):
        self.__roundedCorner = roundedCorner

    @property
    def containerLabelDirection(self) -> str:
        return self.__containerLabelDirection

    @containerLabelDirection.setter
    def containerLabelDirection(self, containerLabelDirection: str):
        self.__containerLabelDirection = containerLabelDirection

class ColorDescription:

    pass
class description_EndUserDocumentedElement:

    pass
class DecorationDescriptionsSet:

    pass
class DocumentedElement:

    pass
class diagram_concern_ConcernSet(DocumentedElement):

    pass
class diagram_description_Layout(DocumentedElement):

    pass
class DecorationDescription:

    pass
class diagram_description_MappingBasedDecoration(DecorationDescription):

    pass
class diagram_description_IEdgeMapping(ABC):

    def __init__(self):
        
    def getBestStyle(self, containerVariable: str, viewVariable: str, modelElement: str) -> EdgeStyle:
        # TODO: Implement getBestStyle method
        pass

class AbstractNodeMapping:

    pass
class tool_ReconnectEdgeDescription:

    pass
class ConditionalStyleDescription:

    pass
class diagram_description_ConditionalContainerStyleDescription(ConditionalStyleDescription):

    pass
class diagram_description_ConditionalEdgeStyleDescription(ConditionalStyleDescription):

    pass
class diagram_description_ConditionalNodeStyleDescription(ConditionalStyleDescription):

    pass
class description_IdentifiedElement:

    pass
class ConditionalEdgeStyleDescription:

    pass
class style_EdgeStyleDescription:

    pass
class ConditionalContainerStyleDescription:

    pass
class style_ContainerStyleDescription:

    pass
class diagram_style_FlatContainerStyleDescription(style_SizeComputationContainerStyleDescription, style_ContainerStyleDescription):

    def __init__(self, backgroundStyle: str, diagram_style_FlatContainerStyleDescription300: "ColorDescription" = None, diagram_style_FlatContainerStyleDescription303: "style_LabelBorderStyleDescription" = None, diagram_style_FlatContainerStyleDescription: "ColorDescription" = None, style_ContainerStyleDescription: "diagram_description_ContainerMapping", style_ContainerStyleDescription242: "diagram_description_ConditionalContainerStyleDescription"):
        self.backgroundStyle = backgroundStyle
        self.diagram_style_FlatContainerStyleDescription300 = diagram_style_FlatContainerStyleDescription300
        self.diagram_style_FlatContainerStyleDescription303 = diagram_style_FlatContainerStyleDescription303
        self.diagram_style_FlatContainerStyleDescription = diagram_style_FlatContainerStyleDescription
        
    @property
    def backgroundStyle(self) -> str:
        return self.__backgroundStyle

    @backgroundStyle.setter
    def backgroundStyle(self, backgroundStyle: str):
        self.__backgroundStyle = backgroundStyle

    @property
    def diagram_style_FlatContainerStyleDescription300(self):
        return self.__diagram_style_FlatContainerStyleDescription300

    @diagram_style_FlatContainerStyleDescription300.setter
    def diagram_style_FlatContainerStyleDescription300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_FlatContainerStyleDescription__diagram_style_FlatContainerStyleDescription300", None)
        self.__diagram_style_FlatContainerStyleDescription300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription301"):
                opp_val = getattr(old_value, "ColorDescription301", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription301"):
                opp_val = getattr(value, "ColorDescription301", None)
                setattr(value, "ColorDescription301", self)

    @property
    def diagram_style_FlatContainerStyleDescription303(self):
        return self.__diagram_style_FlatContainerStyleDescription303

    @diagram_style_FlatContainerStyleDescription303.setter
    def diagram_style_FlatContainerStyleDescription303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_FlatContainerStyleDescription__diagram_style_FlatContainerStyleDescription303", None)
        self.__diagram_style_FlatContainerStyleDescription303 = value
        
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
    def diagram_style_FlatContainerStyleDescription(self):
        return self.__diagram_style_FlatContainerStyleDescription

    @diagram_style_FlatContainerStyleDescription.setter
    def diagram_style_FlatContainerStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_style_FlatContainerStyleDescription__diagram_style_FlatContainerStyleDescription", None)
        self.__diagram_style_FlatContainerStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription298"):
                opp_val = getattr(old_value, "ColorDescription298", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription298", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription298"):
                opp_val = getattr(value, "ColorDescription298", None)
                setattr(value, "ColorDescription298", self)

class diagram_style_ShapeContainerStyleDescription(style_SizeComputationContainerStyleDescription, style_ContainerStyleDescription):

    def __init__(self, shape: str, diagram_style_ShapeContainerStyleDescription: "ColorDescription" = None, style_ContainerStyleDescription: "diagram_description_ContainerMapping", style_ContainerStyleDescription242: "diagram_description_ConditionalContainerStyleDescription"):
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
            if hasattr(old_value, "ColorDescription305"):
                opp_val = getattr(old_value, "ColorDescription305", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription305", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription305"):
                opp_val = getattr(value, "ColorDescription305", None)
                setattr(value, "ColorDescription305", self)

class description_IEdgeMapping:

    pass
class description_ContainerMapping:

    pass
class description_AbstractMappingImport:

    pass
class diagram_description_ContainerMappingImport(description_AbstractMappingImport, description_ContainerMapping):

    pass
class description_NodeMapping:

    pass
class diagram_description_NodeMappingImport(description_AbstractMappingImport, description_NodeMapping):

    pass
class ConditionalNodeStyleDescription:

    pass
class style_NodeStyleDescription:

    pass
class diagram_style_WorkspaceImageDescription(style_NodeStyleDescription, style_ContainerStyleDescription):

    def __init__(self, workspacePath: str, style_NodeStyleDescription238: "diagram_description_ConditionalNodeStyleDescription", style_NodeStyleDescription: "diagram_description_NodeMapping", style_ContainerStyleDescription: "diagram_description_ContainerMapping", style_ContainerStyleDescription242: "diagram_description_ConditionalContainerStyleDescription"):
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
class description_DiagramDescription:

    pass
class description_RepresentationImportDescription:

    pass
class diagram_description_DiagramImportDescription(description_DiagramDescription, description_RepresentationImportDescription):

    pass
class description_RepresentationElementMapping:

    pass
class EdgeMappingImport:

    pass
class tool_ToolSection:

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
                if hasattr(item, "AbstractNodeMapping244"):
                    opp_val = getattr(item, "AbstractNodeMapping244", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractNodeMapping244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractNodeMapping244"):
                    opp_val = getattr(item, "AbstractNodeMapping244", None)
                    
                    setattr(item, "AbstractNodeMapping244", self)
                    

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
class AdditionalLayer:

    pass
class tool_AbstractToolDescription:

    pass
class concern_ConcernSet:

    pass
class validation_ValidationSet:

    pass
class description_PasteTargetDescription:

    pass
class diagram_description_DiagramElementMapping(description_RepresentationElementMapping, description_PasteTargetDescription):

    def __init__(self, semanticCandidatesExpression: str, createElements: bool, semanticElements: str, preconditionExpression: str, synchronizationLock: bool, diagram_description_DiagramElementMapping184: "tool_DirectEditLabel" = None, diagram_description_DiagramElementMapping: "tool_DeleteElementDescription" = None, tool: "tool_DoubleClickDescription" = None):
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.createElements = createElements
        self.semanticElements = semanticElements
        self.preconditionExpression = preconditionExpression
        self.synchronizationLock = synchronizationLock
        self.diagram_description_DiagramElementMapping184 = diagram_description_DiagramElementMapping184
        self.diagram_description_DiagramElementMapping = diagram_description_DiagramElementMapping
        self.tool = tool
        
    @property
    def semanticCandidatesExpression(self) -> str:
        return self.__semanticCandidatesExpression

    @semanticCandidatesExpression.setter
    def semanticCandidatesExpression(self, semanticCandidatesExpression: str):
        self.__semanticCandidatesExpression = semanticCandidatesExpression

    @property
    def preconditionExpression(self) -> str:
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression

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
    def createElements(self) -> bool:
        return self.__createElements

    @createElements.setter
    def createElements(self, createElements: bool):
        self.__createElements = createElements

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
    def diagram_description_DiagramElementMapping184(self):
        return self.__diagram_description_DiagramElementMapping184

    @diagram_description_DiagramElementMapping184.setter
    def diagram_description_DiagramElementMapping184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramElementMapping__diagram_description_DiagramElementMapping184", None)
        self.__diagram_description_DiagramElementMapping184 = value
        
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

    def getAllMappings(self) -> str:
        # TODO: Implement getAllMappings method
        pass

    def checkPrecondition(self, modelElement: str, container: str, containerView: str) -> bool:
        # TODO: Implement checkPrecondition method
        pass

    def isFrom(self, element: str) -> bool:
        # TODO: Implement isFrom method
        pass

class description_RepresentationDescription:

    pass
class description_DragAndDropTargetDescription:

    pass
class diagram_description_ContainerMapping(description_AbstractNodeMapping, description_DragAndDropTargetDescription):

    def __init__(self, childrenPresentation: str, diagram_description_ContainerMapping: set["NodeMapping"] = None, diagram_description_ContainerMapping197: set["NodeMapping"] = None, diagram_description_ContainerMapping200: set["NodeMapping"] = None, diagram_description_ContainerMapping203: set["ContainerMapping"] = None, diagram_description_ContainerMapping206: set["ContainerMapping"] = None, diagram_description_ContainerMapping209: set["ContainerMapping"] = None, diagram_description_ContainerMapping212: "style_ContainerStyleDescription" = None, diagram_description_ContainerMapping214: set["ConditionalContainerStyleDescription"] = None):
        self.childrenPresentation = childrenPresentation
        self.diagram_description_ContainerMapping = diagram_description_ContainerMapping if diagram_description_ContainerMapping is not None else set()
        self.diagram_description_ContainerMapping197 = diagram_description_ContainerMapping197 if diagram_description_ContainerMapping197 is not None else set()
        self.diagram_description_ContainerMapping200 = diagram_description_ContainerMapping200 if diagram_description_ContainerMapping200 is not None else set()
        self.diagram_description_ContainerMapping203 = diagram_description_ContainerMapping203 if diagram_description_ContainerMapping203 is not None else set()
        self.diagram_description_ContainerMapping206 = diagram_description_ContainerMapping206 if diagram_description_ContainerMapping206 is not None else set()
        self.diagram_description_ContainerMapping209 = diagram_description_ContainerMapping209 if diagram_description_ContainerMapping209 is not None else set()
        self.diagram_description_ContainerMapping212 = diagram_description_ContainerMapping212
        self.diagram_description_ContainerMapping214 = diagram_description_ContainerMapping214 if diagram_description_ContainerMapping214 is not None else set()
        
    @property
    def childrenPresentation(self) -> str:
        return self.__childrenPresentation

    @childrenPresentation.setter
    def childrenPresentation(self, childrenPresentation: str):
        self.__childrenPresentation = childrenPresentation

    @property
    def diagram_description_ContainerMapping212(self):
        return self.__diagram_description_ContainerMapping212

    @diagram_description_ContainerMapping212.setter
    def diagram_description_ContainerMapping212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping212", None)
        self.__diagram_description_ContainerMapping212 = value
        
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
    def diagram_description_ContainerMapping200(self):
        return self.__diagram_description_ContainerMapping200

    @diagram_description_ContainerMapping200.setter
    def diagram_description_ContainerMapping200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping200", None)
        self.__diagram_description_ContainerMapping200 = value if value is not None else set()
        
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
                if hasattr(item, "NodeMapping195"):
                    opp_val = getattr(item, "NodeMapping195", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping195"):
                    opp_val = getattr(item, "NodeMapping195", None)
                    
                    setattr(item, "NodeMapping195", self)
                    

    @property
    def diagram_description_ContainerMapping197(self):
        return self.__diagram_description_ContainerMapping197

    @diagram_description_ContainerMapping197.setter
    def diagram_description_ContainerMapping197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping197", None)
        self.__diagram_description_ContainerMapping197 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping198"):
                    opp_val = getattr(item, "NodeMapping198", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping198", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping198"):
                    opp_val = getattr(item, "NodeMapping198", None)
                    
                    setattr(item, "NodeMapping198", self)
                    

    @property
    def diagram_description_ContainerMapping214(self):
        return self.__diagram_description_ContainerMapping214

    @diagram_description_ContainerMapping214.setter
    def diagram_description_ContainerMapping214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_ContainerMapping__diagram_description_ContainerMapping214", None)
        self.__diagram_description_ContainerMapping214 = value if value is not None else set()
        
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
                if hasattr(item, "ContainerMapping204"):
                    opp_val = getattr(item, "ContainerMapping204", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping204", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping204"):
                    opp_val = getattr(item, "ContainerMapping204", None)
                    
                    setattr(item, "ContainerMapping204", self)
                    

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
                if hasattr(item, "ContainerMapping207"):
                    opp_val = getattr(item, "ContainerMapping207", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping207", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping207"):
                    opp_val = getattr(item, "ContainerMapping207", None)
                    
                    setattr(item, "ContainerMapping207", self)
                    

    def getBestStyle(self, viewVariable: str, containerVariable: str, modelElement: str) -> ContainerStyle:
        # TODO: Implement getBestStyle method
        pass

class diagram_description_NodeMapping(description_AbstractNodeMapping, description_DragAndDropTargetDescription):

    def __init__(self, diagram_description_NodeMapping: "style_NodeStyleDescription" = None, diagram_description_NodeMapping193: set["ConditionalNodeStyleDescription"] = None):
        self.diagram_description_NodeMapping = diagram_description_NodeMapping
        self.diagram_description_NodeMapping193 = diagram_description_NodeMapping193 if diagram_description_NodeMapping193 is not None else set()
        
    @property
    def diagram_description_NodeMapping193(self):
        return self.__diagram_description_NodeMapping193

    @diagram_description_NodeMapping193.setter
    def diagram_description_NodeMapping193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_NodeMapping__diagram_description_NodeMapping193", None)
        self.__diagram_description_NodeMapping193 = value if value is not None else set()
        
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

    def getNodesCandidates(self, container: str, semanticOrigin: str) -> str:
        # TODO: Implement getNodesCandidates method
        pass

    def getNodesCandidates(self, containerView: str, semanticOrigin: str, container: str) -> str:
        # TODO: Implement getNodesCandidates method
        pass

    def updateListElement(self, listElement: str):
        # TODO: Implement updateListElement method
        pass

    def createNode(self, viewPoint: DDiagram, modelElement: str, container: str) -> str:
        # TODO: Implement createNode method
        pass

    def updateNode(self, node: str):
        # TODO: Implement updateNode method
        pass

class diagram_description_DiagramDescription(description_DragAndDropTargetDescription, description_RepresentationDescription, description_PasteTargetDescription):

    def __init__(self, domainClass: str, preconditionExpression: str, rootExpression: str, enablePopupBars: bool, diagram_description_DiagramDescription: set["filter_FilterDescription"] = None, diagram_description_DiagramDescription120: set["EdgeMapping"] = None, diagram_description_DiagramDescription132: set["tool_AbstractToolDescription"] = None, diagram_description_DiagramDescription122: set["NodeMapping"] = None, diagram_description_DiagramDescription125: set["ContainerMapping"] = None, diagram_description_DiagramDescription128: "validation_ValidationSet" = None, diagram_description_DiagramDescription130: "concern_ConcernSet" = None, diagram_description_DiagramDescription143: "Layer" = None, diagram_description_DiagramDescription146: set["AdditionalLayer"] = None, diagram_description_DiagramDescription148: set["Layer"] = None, diagram_description_DiagramDescription151: set["tool_AbstractToolDescription"] = None, diagram_description_DiagramDescription134: "concern_ConcernDescription" = None, diagram_description_DiagramDescription137: "tool_RepresentationCreationDescription" = None, diagram_description_DiagramDescription139: "Layout" = None, diagram_description_DiagramDescription141: "tool_InitialOperation" = None, diagram_description_DiagramDescription165: set["DiagramElementMapping"] = None, diagram_description_DiagramDescription168: "tool_ToolSection" = None, diagram_description_DiagramDescription154: set["NodeMapping"] = None, diagram_description_DiagramDescription157: set["EdgeMapping"] = None, diagram_description_DiagramDescription160: set["EdgeMappingImport"] = None, diagram_description_DiagramDescription162: set["ContainerMapping"] = None, diagram_description_DiagramDescription170: set["tool_AbstractToolDescription"] = None):
        self.domainClass = domainClass
        self.preconditionExpression = preconditionExpression
        self.rootExpression = rootExpression
        self.enablePopupBars = enablePopupBars
        self.diagram_description_DiagramDescription = diagram_description_DiagramDescription if diagram_description_DiagramDescription is not None else set()
        self.diagram_description_DiagramDescription120 = diagram_description_DiagramDescription120 if diagram_description_DiagramDescription120 is not None else set()
        self.diagram_description_DiagramDescription132 = diagram_description_DiagramDescription132 if diagram_description_DiagramDescription132 is not None else set()
        self.diagram_description_DiagramDescription122 = diagram_description_DiagramDescription122 if diagram_description_DiagramDescription122 is not None else set()
        self.diagram_description_DiagramDescription125 = diagram_description_DiagramDescription125 if diagram_description_DiagramDescription125 is not None else set()
        self.diagram_description_DiagramDescription128 = diagram_description_DiagramDescription128
        self.diagram_description_DiagramDescription130 = diagram_description_DiagramDescription130
        self.diagram_description_DiagramDescription143 = diagram_description_DiagramDescription143
        self.diagram_description_DiagramDescription146 = diagram_description_DiagramDescription146 if diagram_description_DiagramDescription146 is not None else set()
        self.diagram_description_DiagramDescription148 = diagram_description_DiagramDescription148 if diagram_description_DiagramDescription148 is not None else set()
        self.diagram_description_DiagramDescription151 = diagram_description_DiagramDescription151 if diagram_description_DiagramDescription151 is not None else set()
        self.diagram_description_DiagramDescription134 = diagram_description_DiagramDescription134
        self.diagram_description_DiagramDescription137 = diagram_description_DiagramDescription137
        self.diagram_description_DiagramDescription139 = diagram_description_DiagramDescription139
        self.diagram_description_DiagramDescription141 = diagram_description_DiagramDescription141
        self.diagram_description_DiagramDescription165 = diagram_description_DiagramDescription165 if diagram_description_DiagramDescription165 is not None else set()
        self.diagram_description_DiagramDescription168 = diagram_description_DiagramDescription168
        self.diagram_description_DiagramDescription154 = diagram_description_DiagramDescription154 if diagram_description_DiagramDescription154 is not None else set()
        self.diagram_description_DiagramDescription157 = diagram_description_DiagramDescription157 if diagram_description_DiagramDescription157 is not None else set()
        self.diagram_description_DiagramDescription160 = diagram_description_DiagramDescription160 if diagram_description_DiagramDescription160 is not None else set()
        self.diagram_description_DiagramDescription162 = diagram_description_DiagramDescription162 if diagram_description_DiagramDescription162 is not None else set()
        self.diagram_description_DiagramDescription170 = diagram_description_DiagramDescription170 if diagram_description_DiagramDescription170 is not None else set()
        
    @property
    def preconditionExpression(self) -> str:
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression

    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def rootExpression(self) -> str:
        return self.__rootExpression

    @rootExpression.setter
    def rootExpression(self, rootExpression: str):
        self.__rootExpression = rootExpression

    @property
    def enablePopupBars(self) -> bool:
        return self.__enablePopupBars

    @enablePopupBars.setter
    def enablePopupBars(self, enablePopupBars: bool):
        self.__enablePopupBars = enablePopupBars

    @property
    def diagram_description_DiagramDescription130(self):
        return self.__diagram_description_DiagramDescription130

    @diagram_description_DiagramDescription130.setter
    def diagram_description_DiagramDescription130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription130", None)
        self.__diagram_description_DiagramDescription130 = value
        
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
    def diagram_description_DiagramDescription134(self):
        return self.__diagram_description_DiagramDescription134

    @diagram_description_DiagramDescription134.setter
    def diagram_description_DiagramDescription134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription134", None)
        self.__diagram_description_DiagramDescription134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "concern_ConcernDescription135"):
                opp_val = getattr(old_value, "concern_ConcernDescription135", None)
                if opp_val == self:
                    setattr(old_value, "concern_ConcernDescription135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "concern_ConcernDescription135"):
                opp_val = getattr(value, "concern_ConcernDescription135", None)
                setattr(value, "concern_ConcernDescription135", self)

    @property
    def diagram_description_DiagramDescription146(self):
        return self.__diagram_description_DiagramDescription146

    @diagram_description_DiagramDescription146.setter
    def diagram_description_DiagramDescription146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription146", None)
        self.__diagram_description_DiagramDescription146 = value if value is not None else set()
        
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
    def diagram_description_DiagramDescription120(self):
        return self.__diagram_description_DiagramDescription120

    @diagram_description_DiagramDescription120.setter
    def diagram_description_DiagramDescription120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription120", None)
        self.__diagram_description_DiagramDescription120 = value if value is not None else set()
        
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
    def diagram_description_DiagramDescription139(self):
        return self.__diagram_description_DiagramDescription139

    @diagram_description_DiagramDescription139.setter
    def diagram_description_DiagramDescription139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription139", None)
        self.__diagram_description_DiagramDescription139 = value
        
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
    def diagram_description_DiagramDescription168(self):
        return self.__diagram_description_DiagramDescription168

    @diagram_description_DiagramDescription168.setter
    def diagram_description_DiagramDescription168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription168", None)
        self.__diagram_description_DiagramDescription168 = value
        
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
    def diagram_description_DiagramDescription128(self):
        return self.__diagram_description_DiagramDescription128

    @diagram_description_DiagramDescription128.setter
    def diagram_description_DiagramDescription128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription128", None)
        self.__diagram_description_DiagramDescription128 = value
        
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
    def diagram_description_DiagramDescription170(self):
        return self.__diagram_description_DiagramDescription170

    @diagram_description_DiagramDescription170.setter
    def diagram_description_DiagramDescription170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription170", None)
        self.__diagram_description_DiagramDescription170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription171"):
                    opp_val = getattr(item, "tool_AbstractToolDescription171", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription171"):
                    opp_val = getattr(item, "tool_AbstractToolDescription171", None)
                    
                    setattr(item, "tool_AbstractToolDescription171", self)
                    

    @property
    def diagram_description_DiagramDescription148(self):
        return self.__diagram_description_DiagramDescription148

    @diagram_description_DiagramDescription148.setter
    def diagram_description_DiagramDescription148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription148", None)
        self.__diagram_description_DiagramDescription148 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Layer149"):
                    opp_val = getattr(item, "Layer149", None)
                    
                    if opp_val == self:
                        setattr(item, "Layer149", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Layer149"):
                    opp_val = getattr(item, "Layer149", None)
                    
                    setattr(item, "Layer149", self)
                    

    @property
    def diagram_description_DiagramDescription122(self):
        return self.__diagram_description_DiagramDescription122

    @diagram_description_DiagramDescription122.setter
    def diagram_description_DiagramDescription122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription122", None)
        self.__diagram_description_DiagramDescription122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping123"):
                    opp_val = getattr(item, "NodeMapping123", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping123"):
                    opp_val = getattr(item, "NodeMapping123", None)
                    
                    setattr(item, "NodeMapping123", self)
                    

    @property
    def diagram_description_DiagramDescription141(self):
        return self.__diagram_description_DiagramDescription141

    @diagram_description_DiagramDescription141.setter
    def diagram_description_DiagramDescription141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription141", None)
        self.__diagram_description_DiagramDescription141 = value
        
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
                if hasattr(item, "filter_FilterDescription118"):
                    opp_val = getattr(item, "filter_FilterDescription118", None)
                    
                    if opp_val == self:
                        setattr(item, "filter_FilterDescription118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filter_FilterDescription118"):
                    opp_val = getattr(item, "filter_FilterDescription118", None)
                    
                    setattr(item, "filter_FilterDescription118", self)
                    

    @property
    def diagram_description_DiagramDescription162(self):
        return self.__diagram_description_DiagramDescription162

    @diagram_description_DiagramDescription162.setter
    def diagram_description_DiagramDescription162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription162", None)
        self.__diagram_description_DiagramDescription162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ContainerMapping163"):
                    opp_val = getattr(item, "ContainerMapping163", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping163"):
                    opp_val = getattr(item, "ContainerMapping163", None)
                    
                    setattr(item, "ContainerMapping163", self)
                    

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
                if hasattr(item, "tool_AbstractToolDescription152"):
                    opp_val = getattr(item, "tool_AbstractToolDescription152", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription152"):
                    opp_val = getattr(item, "tool_AbstractToolDescription152", None)
                    
                    setattr(item, "tool_AbstractToolDescription152", self)
                    

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
                if hasattr(item, "EdgeMapping158"):
                    opp_val = getattr(item, "EdgeMapping158", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping158", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping158"):
                    opp_val = getattr(item, "EdgeMapping158", None)
                    
                    setattr(item, "EdgeMapping158", self)
                    

    @property
    def diagram_description_DiagramDescription137(self):
        return self.__diagram_description_DiagramDescription137

    @diagram_description_DiagramDescription137.setter
    def diagram_description_DiagramDescription137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription137", None)
        self.__diagram_description_DiagramDescription137 = value
        
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
    def diagram_description_DiagramDescription165(self):
        return self.__diagram_description_DiagramDescription165

    @diagram_description_DiagramDescription165.setter
    def diagram_description_DiagramDescription165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription165", None)
        self.__diagram_description_DiagramDescription165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping166"):
                    opp_val = getattr(item, "DiagramElementMapping166", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping166", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping166"):
                    opp_val = getattr(item, "DiagramElementMapping166", None)
                    
                    setattr(item, "DiagramElementMapping166", self)
                    

    @property
    def diagram_description_DiagramDescription132(self):
        return self.__diagram_description_DiagramDescription132

    @diagram_description_DiagramDescription132.setter
    def diagram_description_DiagramDescription132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription132", None)
        self.__diagram_description_DiagramDescription132 = value if value is not None else set()
        
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
                if hasattr(item, "NodeMapping155"):
                    opp_val = getattr(item, "NodeMapping155", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping155"):
                    opp_val = getattr(item, "NodeMapping155", None)
                    
                    setattr(item, "NodeMapping155", self)
                    

    @property
    def diagram_description_DiagramDescription143(self):
        return self.__diagram_description_DiagramDescription143

    @diagram_description_DiagramDescription143.setter
    def diagram_description_DiagramDescription143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_DiagramDescription__diagram_description_DiagramDescription143", None)
        self.__diagram_description_DiagramDescription143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Layer144"):
                opp_val = getattr(old_value, "Layer144", None)
                if opp_val == self:
                    setattr(old_value, "Layer144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Layer144"):
                opp_val = getattr(value, "Layer144", None)
                setattr(value, "Layer144", self)

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
                if hasattr(item, "ContainerMapping126"):
                    opp_val = getattr(item, "ContainerMapping126", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping126"):
                    opp_val = getattr(item, "ContainerMapping126", None)
                    
                    setattr(item, "ContainerMapping126", self)
                    

    def createDiagram(self) -> str:
        # TODO: Implement createDiagram method
        pass

class diagram_EObject:

    pass
class tool_SelectModelElementVariable:

    pass
class EdgeMapping:

    pass
class diagram_DragAndDropTarget:

    def __init__(self):
        
    def getDragAndDropDescription(self) -> str:
        # TODO: Implement getDragAndDropDescription method
        pass

class style_StyleDescription:

    pass
class diagram_style_NodeStyleDescription(style_TooltipStyleDescription, style_BorderedStyleDescription, style_HideLabelCapabilityStyleDescription, style_StyleDescription, style_LabelStyleDescription):

    def __init__(self, sizeComputationExpression: str, labelPosition: str, resizeKind: str, forbiddenSides: str, labelDirection: str, style_StyleDescription: "diagram_ComputedStyleDescriptionRegistry"):
        self.sizeComputationExpression = sizeComputationExpression
        self.labelPosition = labelPosition
        self.resizeKind = resizeKind
        self.forbiddenSides = forbiddenSides
        self.labelDirection = labelDirection
        
    @property
    def forbiddenSides(self) -> str:
        return self.__forbiddenSides

    @forbiddenSides.setter
    def forbiddenSides(self, forbiddenSides: str):
        self.__forbiddenSides = forbiddenSides

    @property
    def labelPosition(self) -> str:
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition

    @property
    def resizeKind(self) -> str:
        return self.__resizeKind

    @resizeKind.setter
    def resizeKind(self, resizeKind: str):
        self.__resizeKind = resizeKind

    @property
    def labelDirection(self) -> str:
        return self.__labelDirection

    @labelDirection.setter
    def labelDirection(self, labelDirection: str):
        self.__labelDirection = labelDirection

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

class diagram_VariableValue(ABC):

    pass
class BasicLabelStyle:

    pass
class CollapseFilter:

    pass
class diagram_IndirectlyCollapseFilter(CollapseFilter):

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
            if hasattr(old_value, "diagram_EdgeStyle108"):
                opp_val = getattr(old_value, "diagram_EdgeStyle108", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EdgeStyle108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EdgeStyle108"):
                opp_val = getattr(value, "diagram_EdgeStyle108", None)
                setattr(value, "diagram_EdgeStyle108", self)

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
            if hasattr(old_value, "diagram_EdgeStyle106"):
                opp_val = getattr(old_value, "diagram_EdgeStyle106", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EdgeStyle106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EdgeStyle106"):
                opp_val = getattr(value, "diagram_EdgeStyle106", None)
                setattr(value, "diagram_EdgeStyle106", self)

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
            if hasattr(old_value, "diagram_EdgeStyle104"):
                opp_val = getattr(old_value, "diagram_EdgeStyle104", None)
                if opp_val == self:
                    setattr(old_value, "diagram_EdgeStyle104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_EdgeStyle104"):
                opp_val = getattr(value, "diagram_EdgeStyle104", None)
                setattr(value, "diagram_EdgeStyle104", self)

    def getDescription(self) -> str:
        # TODO: Implement getDescription method
        pass

    def setDescription(self, description: str):
        # TODO: Implement setDescription method
        pass

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
    def foregroundColor(self) -> str:
        return self.__foregroundColor

    @foregroundColor.setter
    def foregroundColor(self, foregroundColor: str):
        self.__foregroundColor = foregroundColor

    @property
    def backgroundStyle(self) -> str:
        return self.__backgroundStyle

    @backgroundStyle.setter
    def backgroundStyle(self, backgroundStyle: str):
        self.__backgroundStyle = backgroundStyle

    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

class NodeStyle:

    pass
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
                    

class diagram_WorkspaceImage(NodeStyle, ContainerStyle):

    def __init__(self, workspacePath: str):
        self.workspacePath = workspacePath
        
    @property
    def workspacePath(self) -> str:
        return self.__workspacePath

    @workspacePath.setter
    def workspacePath(self, workspacePath: str):
        self.__workspacePath = workspacePath

class diagram_Square(NodeStyle):

    def __init__(self, width: str, height: str, color: str):
        self.width = width
        self.height = height
        self.color = color
        
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
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class diagram_Note(NodeStyle):

    def __init__(self, color: str):
        self.color = color
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class diagram_Lozenge(NodeStyle):

    def __init__(self, width: str, height: str, color: str):
        self.width = width
        self.height = height
        self.color = color
        
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

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

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

class diagram_CustomStyle(NodeStyle):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

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

class diagram_Dot(NodeStyle):

    def __init__(self, strokeSizeComputationExpression: str, backgroundColor: str):
        self.strokeSizeComputationExpression = strokeSizeComputationExpression
        self.backgroundColor = backgroundColor
        
    @property
    def strokeSizeComputationExpression(self) -> str:
        return self.__strokeSizeComputationExpression

    @strokeSizeComputationExpression.setter
    def strokeSizeComputationExpression(self, strokeSizeComputationExpression: str):
        self.__strokeSizeComputationExpression = strokeSizeComputationExpression

    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

class HideLabelCapabilityStyle:

    pass
class BorderedStyle:

    pass
class Style:

    pass
class diagram_BorderedStyle(Style):

    def __init__(self, borderColor: str, borderSize: str, borderSizeComputationExpression: str, borderLineStyle: str):
        self.borderColor = borderColor
        self.borderSize = borderSize
        self.borderSizeComputationExpression = borderSizeComputationExpression
        self.borderLineStyle = borderLineStyle
        
    @property
    def borderColor(self) -> str:
        return self.__borderColor

    @borderColor.setter
    def borderColor(self, borderColor: str):
        self.__borderColor = borderColor

    @property
    def borderSizeComputationExpression(self) -> str:
        return self.__borderSizeComputationExpression

    @borderSizeComputationExpression.setter
    def borderSizeComputationExpression(self, borderSizeComputationExpression: str):
        self.__borderSizeComputationExpression = borderSizeComputationExpression

    @property
    def borderLineStyle(self) -> str:
        return self.__borderLineStyle

    @borderLineStyle.setter
    def borderLineStyle(self, borderLineStyle: str):
        self.__borderLineStyle = borderLineStyle

    @property
    def borderSize(self) -> str:
        return self.__borderSize

    @borderSize.setter
    def borderSize(self, borderSize: str):
        self.__borderSize = borderSize

class LabelStyle:

    pass
class Customizable:

    pass
class diagram_GaugeSection(Customizable):

    def __init__(self, min: str, max: str, value: str, label: str, backgroundColor: str, foregroundColor: str, diagram_GaugeSection: "diagram_GaugeCompositeStyle" = None):
        self.min = min
        self.max = max
        self.value = value
        self.label = label
        self.backgroundColor = backgroundColor
        self.foregroundColor = foregroundColor
        self.diagram_GaugeSection = diagram_GaugeSection
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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

    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

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

class diagram_EdgeTarget(ABC):

    pass
class diagram_EdgeStyle(Style):

    def __init__(self, lineStyle: str, sourceArrow: str, targetArrow: str, foldingStyle: str, size: str, routingStyle: str, centered: str, strokeColor: str, diagram_EdgeStyle: "diagram_DEdge" = None, diagram_EdgeStyle104: "diagram_BeginLabelStyle" = None, diagram_EdgeStyle106: "diagram_CenterLabelStyle" = None, diagram_EdgeStyle108: "diagram_EndLabelStyle" = None):
        self.lineStyle = lineStyle
        self.sourceArrow = sourceArrow
        self.targetArrow = targetArrow
        self.foldingStyle = foldingStyle
        self.size = size
        self.routingStyle = routingStyle
        self.centered = centered
        self.strokeColor = strokeColor
        self.diagram_EdgeStyle = diagram_EdgeStyle
        self.diagram_EdgeStyle104 = diagram_EdgeStyle104
        self.diagram_EdgeStyle106 = diagram_EdgeStyle106
        self.diagram_EdgeStyle108 = diagram_EdgeStyle108
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

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
    def centered(self) -> str:
        return self.__centered

    @centered.setter
    def centered(self, centered: str):
        self.__centered = centered

    @property
    def lineStyle(self) -> str:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle

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
    def strokeColor(self) -> str:
        return self.__strokeColor

    @strokeColor.setter
    def strokeColor(self, strokeColor: str):
        self.__strokeColor = strokeColor

    @property
    def diagram_EdgeStyle108(self):
        return self.__diagram_EdgeStyle108

    @diagram_EdgeStyle108.setter
    def diagram_EdgeStyle108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle108", None)
        self.__diagram_EdgeStyle108 = value
        
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
    def diagram_EdgeStyle106(self):
        return self.__diagram_EdgeStyle106

    @diagram_EdgeStyle106.setter
    def diagram_EdgeStyle106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle106", None)
        self.__diagram_EdgeStyle106 = value
        
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
    def diagram_EdgeStyle104(self):
        return self.__diagram_EdgeStyle104

    @diagram_EdgeStyle104.setter
    def diagram_EdgeStyle104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_EdgeStyle__diagram_EdgeStyle104", None)
        self.__diagram_EdgeStyle104 = value
        
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

class IEdgeMapping:

    pass
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
class diagram_ContainerStyle(Style, HideLabelCapabilityStyle, LabelStyle, BorderedStyle):

    def __init__(self, containerLabelDirection: str, diagram_ContainerStyle: "diagram_DDiagramElementContainer" = None):
        self.containerLabelDirection = containerLabelDirection
        self.diagram_ContainerStyle = diagram_ContainerStyle
        
    @property
    def containerLabelDirection(self) -> str:
        return self.__containerLabelDirection

    @containerLabelDirection.setter
    def containerLabelDirection(self, containerLabelDirection: str):
        self.__containerLabelDirection = containerLabelDirection

    @property
    def diagram_ContainerStyle(self):
        return self.__diagram_ContainerStyle

    @diagram_ContainerStyle.setter
    def diagram_ContainerStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_ContainerStyle__diagram_ContainerStyle", None)
        self.__diagram_ContainerStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_DDiagramElementContainer63"):
                opp_val = getattr(old_value, "diagram_DDiagramElementContainer63", None)
                if opp_val == self:
                    setattr(old_value, "diagram_DDiagramElementContainer63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DDiagramElementContainer63"):
                opp_val = getattr(value, "diagram_DDiagramElementContainer63", None)
                setattr(value, "diagram_DDiagramElementContainer63", self)

class diagram_DNodeList(DDiagramElementContainer):

    pass
class NodeMapping:

    pass
class diagram_Style:

    pass
class diagram_NodeStyle(Style, HideLabelCapabilityStyle, LabelStyle, BorderedStyle):

    def __init__(self, labelPosition: str, labelDirection: str, diagram_NodeStyle: "diagram_DNode" = None, diagram_NodeStyle78: "diagram_DNodeListElement" = None):
        self.labelPosition = labelPosition
        self.labelDirection = labelDirection
        self.diagram_NodeStyle = diagram_NodeStyle
        self.diagram_NodeStyle78 = diagram_NodeStyle78
        
    @property
    def labelDirection(self) -> str:
        return self.__labelDirection

    @labelDirection.setter
    def labelDirection(self, labelDirection: str):
        self.__labelDirection = labelDirection

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
            if hasattr(old_value, "diagram_DNode45"):
                opp_val = getattr(old_value, "diagram_DNode45", None)
                if opp_val == self:
                    setattr(old_value, "diagram_DNode45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_DNode45"):
                opp_val = getattr(value, "diagram_DNode45", None)
                setattr(value, "diagram_DNode45", self)

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

class EdgeTarget:

    pass
class AbstractDNode:

    pass
class GraphicalFilter:

    pass
class diagram_HideLabelFilter(GraphicalFilter):

    pass
class diagram_FoldingPointFilter(GraphicalFilter):

    pass
class diagram_CollapseFilter(GraphicalFilter):

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

class diagram_HideFilter(GraphicalFilter):

    pass
class diagram_GraphicalFilter(ABC):

    pass
class DiagramElementMapping:

    pass
class diagram_Decoration:

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
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

class filter_CompositeFilterDescription:

    pass
class diagram_AppliedCompositeFilters(GraphicalFilter):

    pass
class diagram_FoldingFilter(GraphicalFilter):

    pass
class Layer:

    pass
class diagram_description_AdditionalLayer(Layer):

    def __init__(self, activeByDefault: bool, optional: bool, Layer: "diagram_DDiagram", Layer34: "diagram_DDiagramElement", Layer149: "diagram_description_DiagramDescription", Layer144: "diagram_description_DiagramDescription"):
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
class DRepresentationElement:

    pass
class DSemanticDecorator:

    pass
class DDiagram:

    pass
class diagram_DSemanticDiagram(DDiagram, DSemanticDecorator):

    pass
class diagram_DNodeListElement(AbstractDNode):

    pass
class diagram_DEdge(DDiagramElement, EdgeTarget):

    def __init__(self, routingStyle: str, isFold: bool, isMockEdge: bool, arrangeConstraints: str, beginLabel: str, size: str, endLabel: str, diagram_DEdge: "diagram_DDiagram" = None, incomingEdges: "diagram_EdgeTarget" = None, diagram_DEdge94: "IEdgeMapping" = None, diagram_DEdge96: "diagram_Style" = None, diagram_DEdge99: set["diagram_EdgeTarget"] = None, diagram_DEdge89: "diagram_EdgeStyle" = None, outgoingEdges: "diagram_EdgeTarget" = None, DEdge: "diagram_EdgeTarget" = None, DEdge102: "diagram_EdgeTarget" = None):
        self.routingStyle = routingStyle
        self.isFold = isFold
        self.isMockEdge = isMockEdge
        self.arrangeConstraints = arrangeConstraints
        self.beginLabel = beginLabel
        self.size = size
        self.endLabel = endLabel
        self.diagram_DEdge = diagram_DEdge
        self.incomingEdges = incomingEdges
        self.diagram_DEdge94 = diagram_DEdge94
        self.diagram_DEdge96 = diagram_DEdge96
        self.diagram_DEdge99 = diagram_DEdge99 if diagram_DEdge99 is not None else set()
        self.diagram_DEdge89 = diagram_DEdge89
        self.outgoingEdges = outgoingEdges
        self.DEdge = DEdge
        self.DEdge102 = DEdge102
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def arrangeConstraints(self) -> str:
        return self.__arrangeConstraints

    @arrangeConstraints.setter
    def arrangeConstraints(self, arrangeConstraints: str):
        self.__arrangeConstraints = arrangeConstraints

    @property
    def isFold(self) -> bool:
        return self.__isFold

    @isFold.setter
    def isFold(self, isFold: bool):
        self.__isFold = isFold

    @property
    def routingStyle(self) -> str:
        return self.__routingStyle

    @routingStyle.setter
    def routingStyle(self, routingStyle: str):
        self.__routingStyle = routingStyle

    @property
    def beginLabel(self) -> str:
        return self.__beginLabel

    @beginLabel.setter
    def beginLabel(self, beginLabel: str):
        self.__beginLabel = beginLabel

    @property
    def isMockEdge(self) -> bool:
        return self.__isMockEdge

    @isMockEdge.setter
    def isMockEdge(self, isMockEdge: bool):
        self.__isMockEdge = isMockEdge

    @property
    def endLabel(self) -> str:
        return self.__endLabel

    @endLabel.setter
    def endLabel(self, endLabel: str):
        self.__endLabel = endLabel

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
    def DEdge102(self):
        return self.__DEdge102

    @DEdge102.setter
    def DEdge102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_DEdge__DEdge102", None)
        self.__DEdge102 = value
        
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

    def isRootFolding(self) -> bool:
        # TODO: Implement isRootFolding method
        pass

class DiagramDescription:

    pass
class diagram_DDiagramElement(DRepresentationElement):

    def __init__(self, visible: bool, tooltipText: str, diagram_DDiagramElement: "diagram_DDiagram" = None, diagram_DDiagramElement3: "diagram_DDiagram" = None, diagram_DDiagramElement31: "diagram_DDiagram" = None, diagram_DDiagramElement33: set["Layer"] = None, diagram_DDiagramElement36: set["diagram_Decoration"] = None, diagram_DDiagramElement38: "DiagramElementMapping" = None, diagram_DDiagramElement40: set["diagram_GraphicalFilter"] = None, diagram_DDiagramElement73: "diagram_DNodeContainer" = None, diagram_DDiagramElement61: "diagram_DDiagramElementContainer" = None):
        self.visible = visible
        self.tooltipText = tooltipText
        self.diagram_DDiagramElement = diagram_DDiagramElement
        self.diagram_DDiagramElement3 = diagram_DDiagramElement3
        self.diagram_DDiagramElement31 = diagram_DDiagramElement31
        self.diagram_DDiagramElement33 = diagram_DDiagramElement33 if diagram_DDiagramElement33 is not None else set()
        self.diagram_DDiagramElement36 = diagram_DDiagramElement36 if diagram_DDiagramElement36 is not None else set()
        self.diagram_DDiagramElement38 = diagram_DDiagramElement38
        self.diagram_DDiagramElement40 = diagram_DDiagramElement40 if diagram_DDiagramElement40 is not None else set()
        self.diagram_DDiagramElement73 = diagram_DDiagramElement73
        self.diagram_DDiagramElement61 = diagram_DDiagramElement61
        
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
                    

    def getParentDiagram(self) -> DDiagram:
        # TODO: Implement getParentDiagram method
        pass

class tool_BehaviorTool:

    pass
class validation_ValidationRule:

    pass
class filter_FilterDescription:

    pass
class concern_ConcernDescription:

    pass
class DragAndDropTarget:

    pass
class diagram_DDiagramElementContainer(AbstractDNode, DragAndDropTarget, EdgeTarget):

    def __init__(self, width: str, height: str, diagram_DDiagramElementContainer: "diagram_DDiagram" = None, diagram_DDiagramElementContainer54: set["diagram_DNode"] = None, diagram_DDiagramElementContainer58: "diagram_DDiagramElementContainer" = None, diagram_DDiagramElementContainer56: set["diagram_DDiagramElementContainer"] = None, diagram_DDiagramElementContainer60: set["diagram_DDiagramElement"] = None, diagram_DDiagramElementContainer63: "diagram_ContainerStyle" = None, diagram_DDiagramElementContainer65: "diagram_Style" = None, diagram_DDiagramElementContainer68: "ContainerMapping" = None, diagram_DDiagramElementContainer70: set["ContainerMapping"] = None):
        self.width = width
        self.height = height
        self.diagram_DDiagramElementContainer = diagram_DDiagramElementContainer
        self.diagram_DDiagramElementContainer54 = diagram_DDiagramElementContainer54 if diagram_DDiagramElementContainer54 is not None else set()
        self.diagram_DDiagramElementContainer58 = diagram_DDiagramElementContainer58
        self.diagram_DDiagramElementContainer56 = diagram_DDiagramElementContainer56 if diagram_DDiagramElementContainer56 is not None else set()
        self.diagram_DDiagramElementContainer60 = diagram_DDiagramElementContainer60 if diagram_DDiagramElementContainer60 is not None else set()
        self.diagram_DDiagramElementContainer63 = diagram_DDiagramElementContainer63
        self.diagram_DDiagramElementContainer65 = diagram_DDiagramElementContainer65
        self.diagram_DDiagramElementContainer68 = diagram_DDiagramElementContainer68
        self.diagram_DDiagramElementContainer70 = diagram_DDiagramElementContainer70 if diagram_DDiagramElementContainer70 is not None else set()
        
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
                    

    def getContainersFromMapping(self, mapping: str) -> str:
        # TODO: Implement getContainersFromMapping method
        pass

    def getNodesFromMapping(self, mapping: str) -> str:
        # TODO: Implement getNodesFromMapping method
        pass

class diagram_DNode(AbstractDNode, DragAndDropTarget, EdgeTarget):

    def __init__(self, width: str, height: str, labelPosition: str, resizeKind: str, diagram_DNode: "diagram_DDiagram" = None, diagram_DNode55: "diagram_DDiagramElementContainer" = None, diagram_DNode43: "diagram_AbstractDNode" = None, diagram_DNode45: "diagram_NodeStyle" = None, diagram_DNode47: "diagram_Style" = None, diagram_DNode49: "NodeMapping" = None, diagram_DNode51: set["NodeMapping"] = None):
        self.width = width
        self.height = height
        self.labelPosition = labelPosition
        self.resizeKind = resizeKind
        self.diagram_DNode = diagram_DNode
        self.diagram_DNode55 = diagram_DNode55
        self.diagram_DNode43 = diagram_DNode43
        self.diagram_DNode45 = diagram_DNode45
        self.diagram_DNode47 = diagram_DNode47
        self.diagram_DNode49 = diagram_DNode49
        self.diagram_DNode51 = diagram_DNode51 if diagram_DNode51 is not None else set()
        
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
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

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

class description_DocumentedElement:

    pass
class diagram_description_AbstractNodeMapping(description_DocumentedElement, description_DiagramElementMapping):

    def __init__(self, domainClass: str, diagram_description_AbstractNodeMapping: set["NodeMapping"] = None, diagram_description_AbstractNodeMapping189: set["NodeMapping"] = None):
        self.domainClass = domainClass
        self.diagram_description_AbstractNodeMapping = diagram_description_AbstractNodeMapping if diagram_description_AbstractNodeMapping is not None else set()
        self.diagram_description_AbstractNodeMapping189 = diagram_description_AbstractNodeMapping189 if diagram_description_AbstractNodeMapping189 is not None else set()
        
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
                if hasattr(item, "NodeMapping187"):
                    opp_val = getattr(item, "NodeMapping187", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping187"):
                    opp_val = getattr(item, "NodeMapping187", None)
                    
                    setattr(item, "NodeMapping187", self)
                    

    @property
    def diagram_description_AbstractNodeMapping189(self):
        return self.__diagram_description_AbstractNodeMapping189

    @diagram_description_AbstractNodeMapping189.setter
    def diagram_description_AbstractNodeMapping189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_AbstractNodeMapping__diagram_description_AbstractNodeMapping189", None)
        self.__diagram_description_AbstractNodeMapping189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "NodeMapping190"):
                    opp_val = getattr(item, "NodeMapping190", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping190"):
                    opp_val = getattr(item, "NodeMapping190", None)
                    
                    setattr(item, "NodeMapping190", self)
                    

    def addDoneNode(self, node: DSemanticDecorator):
        # TODO: Implement addDoneNode method
        pass

    def findDNodeFromEObject(self, eObject: str) -> DDiagramElement:
        # TODO: Implement findDNodeFromEObject method
        pass

    def getAllBorderedNodeMappings(self) -> str:
        # TODO: Implement getAllBorderedNodeMappings method
        pass

    def clearDNodesDone(self):
        # TODO: Implement clearDNodesDone method
        pass

class diagram_tool_ToolSection(description_IdentifiedElement, description_DocumentedElement):

    def __init__(self, icon: str, diagram_tool_ToolSection322: set["tool_ToolSection"] = None, diagram_tool_ToolSection: set["tool_ToolEntry"] = None, diagram_tool_ToolSection330: set["tool_ToolGroupExtension"] = None, diagram_tool_ToolSection325: set["tool_PopupMenu"] = None, diagram_tool_ToolSection327: set["tool_ToolEntry"] = None):
        self.icon = icon
        self.diagram_tool_ToolSection322 = diagram_tool_ToolSection322 if diagram_tool_ToolSection322 is not None else set()
        self.diagram_tool_ToolSection = diagram_tool_ToolSection if diagram_tool_ToolSection is not None else set()
        self.diagram_tool_ToolSection330 = diagram_tool_ToolSection330 if diagram_tool_ToolSection330 is not None else set()
        self.diagram_tool_ToolSection325 = diagram_tool_ToolSection325 if diagram_tool_ToolSection325 is not None else set()
        self.diagram_tool_ToolSection327 = diagram_tool_ToolSection327 if diagram_tool_ToolSection327 is not None else set()
        
    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def diagram_tool_ToolSection322(self):
        return self.__diagram_tool_ToolSection322

    @diagram_tool_ToolSection322.setter
    def diagram_tool_ToolSection322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection322", None)
        self.__diagram_tool_ToolSection322 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolSection323"):
                    opp_val = getattr(item, "tool_ToolSection323", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolSection323", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolSection323"):
                    opp_val = getattr(item, "tool_ToolSection323", None)
                    
                    setattr(item, "tool_ToolSection323", self)
                    

    @property
    def diagram_tool_ToolSection325(self):
        return self.__diagram_tool_ToolSection325

    @diagram_tool_ToolSection325.setter
    def diagram_tool_ToolSection325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection325", None)
        self.__diagram_tool_ToolSection325 = value if value is not None else set()
        
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
    def diagram_tool_ToolSection330(self):
        return self.__diagram_tool_ToolSection330

    @diagram_tool_ToolSection330.setter
    def diagram_tool_ToolSection330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection330", None)
        self.__diagram_tool_ToolSection330 = value if value is not None else set()
        
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
    def diagram_tool_ToolSection327(self):
        return self.__diagram_tool_ToolSection327

    @diagram_tool_ToolSection327.setter
    def diagram_tool_ToolSection327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_tool_ToolSection__diagram_tool_ToolSection327", None)
        self.__diagram_tool_ToolSection327 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolEntry328"):
                    opp_val = getattr(item, "tool_ToolEntry328", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolEntry328", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolEntry328"):
                    opp_val = getattr(item, "tool_ToolEntry328", None)
                    
                    setattr(item, "tool_ToolEntry328", self)
                    

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
                    

class diagram_description_EdgeMapping(description_IEdgeMapping, description_DocumentedElement, description_DiagramElementMapping):

    def __init__(self, targetFinderExpression: str, sourceFinderExpression: str, targetExpression: str, domainClass: str, useDomainElement: bool, pathExpression: str, diagram_description_EdgeMapping222: set["DiagramElementMapping"] = None, diagram_description_EdgeMapping225: "style_EdgeStyleDescription" = None, diagram_description_EdgeMapping227: set["ConditionalEdgeStyleDescription"] = None, diagram_description_EdgeMapping: set["DiagramElementMapping"] = None, diagram_description_EdgeMapping229: set["tool_ReconnectEdgeDescription"] = None, diagram_description_EdgeMapping231: set["AbstractNodeMapping"] = None):
        self.targetFinderExpression = targetFinderExpression
        self.sourceFinderExpression = sourceFinderExpression
        self.targetExpression = targetExpression
        self.domainClass = domainClass
        self.useDomainElement = useDomainElement
        self.pathExpression = pathExpression
        self.diagram_description_EdgeMapping222 = diagram_description_EdgeMapping222 if diagram_description_EdgeMapping222 is not None else set()
        self.diagram_description_EdgeMapping225 = diagram_description_EdgeMapping225
        self.diagram_description_EdgeMapping227 = diagram_description_EdgeMapping227 if diagram_description_EdgeMapping227 is not None else set()
        self.diagram_description_EdgeMapping = diagram_description_EdgeMapping if diagram_description_EdgeMapping is not None else set()
        self.diagram_description_EdgeMapping229 = diagram_description_EdgeMapping229 if diagram_description_EdgeMapping229 is not None else set()
        self.diagram_description_EdgeMapping231 = diagram_description_EdgeMapping231 if diagram_description_EdgeMapping231 is not None else set()
        
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
    def pathExpression(self) -> str:
        return self.__pathExpression

    @pathExpression.setter
    def pathExpression(self, pathExpression: str):
        self.__pathExpression = pathExpression

    @property
    def targetFinderExpression(self) -> str:
        return self.__targetFinderExpression

    @targetFinderExpression.setter
    def targetFinderExpression(self, targetFinderExpression: str):
        self.__targetFinderExpression = targetFinderExpression

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
    def diagram_description_EdgeMapping225(self):
        return self.__diagram_description_EdgeMapping225

    @diagram_description_EdgeMapping225.setter
    def diagram_description_EdgeMapping225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping225", None)
        self.__diagram_description_EdgeMapping225 = value
        
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
    def diagram_description_EdgeMapping222(self):
        return self.__diagram_description_EdgeMapping222

    @diagram_description_EdgeMapping222.setter
    def diagram_description_EdgeMapping222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping222", None)
        self.__diagram_description_EdgeMapping222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DiagramElementMapping223"):
                    opp_val = getattr(item, "DiagramElementMapping223", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping223"):
                    opp_val = getattr(item, "DiagramElementMapping223", None)
                    
                    setattr(item, "DiagramElementMapping223", self)
                    

    @property
    def diagram_description_EdgeMapping229(self):
        return self.__diagram_description_EdgeMapping229

    @diagram_description_EdgeMapping229.setter
    def diagram_description_EdgeMapping229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping229", None)
        self.__diagram_description_EdgeMapping229 = value if value is not None else set()
        
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
    def diagram_description_EdgeMapping227(self):
        return self.__diagram_description_EdgeMapping227

    @diagram_description_EdgeMapping227.setter
    def diagram_description_EdgeMapping227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping227", None)
        self.__diagram_description_EdgeMapping227 = value if value is not None else set()
        
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
                if hasattr(item, "DiagramElementMapping220"):
                    opp_val = getattr(item, "DiagramElementMapping220", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping220"):
                    opp_val = getattr(item, "DiagramElementMapping220", None)
                    
                    setattr(item, "DiagramElementMapping220", self)
                    

    @property
    def diagram_description_EdgeMapping231(self):
        return self.__diagram_description_EdgeMapping231

    @diagram_description_EdgeMapping231.setter
    def diagram_description_EdgeMapping231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMapping__diagram_description_EdgeMapping231", None)
        self.__diagram_description_EdgeMapping231 = value if value is not None else set()
        
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
                    

    def getEdgeTargetCandidates(self, semanticOrigin: str, viewPoint: DDiagram) -> str:
        # TODO: Implement getEdgeTargetCandidates method
        pass

    def getBestStyle(self, viewVariable: str, containerVariable: str, modelElement: str) -> EdgeStyle:
        # TODO: Implement getBestStyle method
        pass

    def updateEdge(self, viewEdge: str):
        # TODO: Implement updateEdge method
        pass

    def getEdgeSourceCandidates(self, viewPoint: DDiagram, semanticOrigin: str) -> str:
        # TODO: Implement getEdgeSourceCandidates method
        pass

    def getEdgeTargetCandidates(self, container: str, containerView: str, semanticOrigin: str) -> str:
        # TODO: Implement getEdgeTargetCandidates method
        pass

    def createEdge(self, target: EdgeTarget, source: EdgeTarget, container: str, semanticTarget: str) -> str:
        # TODO: Implement createEdge method
        pass

    def createEdge(self, source: EdgeTarget, target: EdgeTarget, semanticTarget: str) -> str:
        # TODO: Implement createEdge method
        pass

class diagram_description_EdgeMappingImport(description_IEdgeMapping, description_IdentifiedElement, description_DocumentedElement):

    def __init__(self, inheritsAncestorFilters: bool, diagram_description_EdgeMappingImport: "IEdgeMapping" = None, diagram_description_EdgeMappingImport235: set["ConditionalEdgeStyleDescription"] = None):
        self.inheritsAncestorFilters = inheritsAncestorFilters
        self.diagram_description_EdgeMappingImport = diagram_description_EdgeMappingImport
        self.diagram_description_EdgeMappingImport235 = diagram_description_EdgeMappingImport235 if diagram_description_EdgeMappingImport235 is not None else set()
        
    @property
    def inheritsAncestorFilters(self) -> bool:
        return self.__inheritsAncestorFilters

    @inheritsAncestorFilters.setter
    def inheritsAncestorFilters(self, inheritsAncestorFilters: bool):
        self.__inheritsAncestorFilters = inheritsAncestorFilters

    @property
    def diagram_description_EdgeMappingImport235(self):
        return self.__diagram_description_EdgeMappingImport235

    @diagram_description_EdgeMappingImport235.setter
    def diagram_description_EdgeMappingImport235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_EdgeMappingImport__diagram_description_EdgeMappingImport235", None)
        self.__diagram_description_EdgeMappingImport235 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ConditionalEdgeStyleDescription236"):
                    opp_val = getattr(item, "ConditionalEdgeStyleDescription236", None)
                    
                    if opp_val == self:
                        setattr(item, "ConditionalEdgeStyleDescription236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ConditionalEdgeStyleDescription236"):
                    opp_val = getattr(item, "ConditionalEdgeStyleDescription236", None)
                    
                    setattr(item, "ConditionalEdgeStyleDescription236", self)
                    

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
            if hasattr(old_value, "IEdgeMapping233"):
                opp_val = getattr(old_value, "IEdgeMapping233", None)
                if opp_val == self:
                    setattr(old_value, "IEdgeMapping233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IEdgeMapping233"):
                opp_val = getattr(value, "IEdgeMapping233", None)
                setattr(value, "IEdgeMapping233", self)

class diagram_concern_ConcernDescription(description_IdentifiedElement, description_DocumentedElement):

    pass
class diagram_description_Layer(description_DocumentedElement, description_IdentifiedElement, description_EndUserDocumentedElement):

    def __init__(self, icon: str, diagram_description_Layer256: set["ContainerMapping"] = None, diagram_description_Layer259: set["DiagramElementMapping"] = None, diagram_description_Layer262: set["tool_AbstractToolDescription"] = None, diagram_description_Layer265: set["tool_ToolSection"] = None, diagram_description_Layer268: set["tool_AbstractToolDescription"] = None, diagram_description_Layer271: "DecorationDescriptionsSet" = None, diagram_description_Layer: set["NodeMapping"] = None, diagram_description_Layer250: set["EdgeMapping"] = None, diagram_description_Layer253: set["EdgeMappingImport"] = None, diagram_description_Layer273: set["EdgeMapping"] = None, diagram_description_Layer276: "Customization" = None):
        self.icon = icon
        self.diagram_description_Layer256 = diagram_description_Layer256 if diagram_description_Layer256 is not None else set()
        self.diagram_description_Layer259 = diagram_description_Layer259 if diagram_description_Layer259 is not None else set()
        self.diagram_description_Layer262 = diagram_description_Layer262 if diagram_description_Layer262 is not None else set()
        self.diagram_description_Layer265 = diagram_description_Layer265 if diagram_description_Layer265 is not None else set()
        self.diagram_description_Layer268 = diagram_description_Layer268 if diagram_description_Layer268 is not None else set()
        self.diagram_description_Layer271 = diagram_description_Layer271
        self.diagram_description_Layer = diagram_description_Layer if diagram_description_Layer is not None else set()
        self.diagram_description_Layer250 = diagram_description_Layer250 if diagram_description_Layer250 is not None else set()
        self.diagram_description_Layer253 = diagram_description_Layer253 if diagram_description_Layer253 is not None else set()
        self.diagram_description_Layer273 = diagram_description_Layer273 if diagram_description_Layer273 is not None else set()
        self.diagram_description_Layer276 = diagram_description_Layer276
        
    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def diagram_description_Layer253(self):
        return self.__diagram_description_Layer253

    @diagram_description_Layer253.setter
    def diagram_description_Layer253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer253", None)
        self.__diagram_description_Layer253 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMappingImport254"):
                    opp_val = getattr(item, "EdgeMappingImport254", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMappingImport254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMappingImport254"):
                    opp_val = getattr(item, "EdgeMappingImport254", None)
                    
                    setattr(item, "EdgeMappingImport254", self)
                    

    @property
    def diagram_description_Layer250(self):
        return self.__diagram_description_Layer250

    @diagram_description_Layer250.setter
    def diagram_description_Layer250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer250", None)
        self.__diagram_description_Layer250 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMapping251"):
                    opp_val = getattr(item, "EdgeMapping251", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping251", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping251"):
                    opp_val = getattr(item, "EdgeMapping251", None)
                    
                    setattr(item, "EdgeMapping251", self)
                    

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
                if hasattr(item, "NodeMapping248"):
                    opp_val = getattr(item, "NodeMapping248", None)
                    
                    if opp_val == self:
                        setattr(item, "NodeMapping248", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "NodeMapping248"):
                    opp_val = getattr(item, "NodeMapping248", None)
                    
                    setattr(item, "NodeMapping248", self)
                    

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
                if hasattr(item, "tool_ToolSection266"):
                    opp_val = getattr(item, "tool_ToolSection266", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolSection266", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolSection266"):
                    opp_val = getattr(item, "tool_ToolSection266", None)
                    
                    setattr(item, "tool_ToolSection266", self)
                    

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
                if hasattr(item, "tool_AbstractToolDescription263"):
                    opp_val = getattr(item, "tool_AbstractToolDescription263", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription263", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription263"):
                    opp_val = getattr(item, "tool_AbstractToolDescription263", None)
                    
                    setattr(item, "tool_AbstractToolDescription263", self)
                    

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
    def diagram_description_Layer273(self):
        return self.__diagram_description_Layer273

    @diagram_description_Layer273.setter
    def diagram_description_Layer273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer273", None)
        self.__diagram_description_Layer273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeMapping274"):
                    opp_val = getattr(item, "EdgeMapping274", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeMapping274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeMapping274"):
                    opp_val = getattr(item, "EdgeMapping274", None)
                    
                    setattr(item, "EdgeMapping274", self)
                    

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
                if hasattr(item, "DiagramElementMapping260"):
                    opp_val = getattr(item, "DiagramElementMapping260", None)
                    
                    if opp_val == self:
                        setattr(item, "DiagramElementMapping260", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DiagramElementMapping260"):
                    opp_val = getattr(item, "DiagramElementMapping260", None)
                    
                    setattr(item, "DiagramElementMapping260", self)
                    

    @property
    def diagram_description_Layer271(self):
        return self.__diagram_description_Layer271

    @diagram_description_Layer271.setter
    def diagram_description_Layer271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer271", None)
        self.__diagram_description_Layer271 = value
        
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
    def diagram_description_Layer276(self):
        return self.__diagram_description_Layer276

    @diagram_description_Layer276.setter
    def diagram_description_Layer276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagram_description_Layer__diagram_description_Layer276", None)
        self.__diagram_description_Layer276 = value
        
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
                if hasattr(item, "ContainerMapping257"):
                    opp_val = getattr(item, "ContainerMapping257", None)
                    
                    if opp_val == self:
                        setattr(item, "ContainerMapping257", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ContainerMapping257"):
                    opp_val = getattr(item, "ContainerMapping257", None)
                    
                    setattr(item, "ContainerMapping257", self)
                    

class diagram_filter_FilterDescription(description_IdentifiedElement, description_DocumentedElement):

    def __init__(self):
        
    def isVisible(self, element: DDiagramElement) -> bool:
        # TODO: Implement isVisible method
        pass

class DRepresentation:

    pass
class diagram_DDiagram(DragAndDropTarget, description_DocumentedElement, DRepresentation):

    def __init__(self, isInLayoutingMode: bool, headerHeight: int, synchronized: bool, diagram_DDiagram13: set["diagram_DDiagramElementContainer"] = None, diagram_DDiagram15: "concern_ConcernDescription" = None, diagram_DDiagram17: set["filter_FilterDescription"] = None, diagram_DDiagram19: set["filter_FilterDescription"] = None, diagram_DDiagram22: set["validation_ValidationRule"] = None, diagram_DDiagram24: set["tool_BehaviorTool"] = None, diagram_DDiagram: set["diagram_DDiagramElement"] = None, diagram_DDiagram2: set["diagram_DDiagramElement"] = None, diagram_DDiagram5: "DiagramDescription" = None, diagram_DDiagram7: set["diagram_DEdge"] = None, diagram_DDiagram9: set["diagram_DNode"] = None, diagram_DDiagram11: set["diagram_DNodeListElement"] = None, diagram_DDiagram26: "diagram_FilterVariableHistory" = None, diagram_DDiagram28: set["Layer"] = None, diagram_DDiagram30: set["diagram_DDiagramElement"] = None):
        self.isInLayoutingMode = isInLayoutingMode
        self.headerHeight = headerHeight
        self.synchronized = synchronized
        self.diagram_DDiagram13 = diagram_DDiagram13 if diagram_DDiagram13 is not None else set()
        self.diagram_DDiagram15 = diagram_DDiagram15
        self.diagram_DDiagram17 = diagram_DDiagram17 if diagram_DDiagram17 is not None else set()
        self.diagram_DDiagram19 = diagram_DDiagram19 if diagram_DDiagram19 is not None else set()
        self.diagram_DDiagram22 = diagram_DDiagram22 if diagram_DDiagram22 is not None else set()
        self.diagram_DDiagram24 = diagram_DDiagram24 if diagram_DDiagram24 is not None else set()
        self.diagram_DDiagram = diagram_DDiagram if diagram_DDiagram is not None else set()
        self.diagram_DDiagram2 = diagram_DDiagram2 if diagram_DDiagram2 is not None else set()
        self.diagram_DDiagram5 = diagram_DDiagram5
        self.diagram_DDiagram7 = diagram_DDiagram7 if diagram_DDiagram7 is not None else set()
        self.diagram_DDiagram9 = diagram_DDiagram9 if diagram_DDiagram9 is not None else set()
        self.diagram_DDiagram11 = diagram_DDiagram11 if diagram_DDiagram11 is not None else set()
        self.diagram_DDiagram26 = diagram_DDiagram26
        self.diagram_DDiagram28 = diagram_DDiagram28 if diagram_DDiagram28 is not None else set()
        self.diagram_DDiagram30 = diagram_DDiagram30 if diagram_DDiagram30 is not None else set()
        
    @property
    def isInLayoutingMode(self) -> bool:
        return self.__isInLayoutingMode

    @isInLayoutingMode.setter
    def isInLayoutingMode(self, isInLayoutingMode: bool):
        self.__isInLayoutingMode = isInLayoutingMode

    @property
    def synchronized(self) -> bool:
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized

    @property
    def headerHeight(self) -> int:
        return self.__headerHeight

    @headerHeight.setter
    def headerHeight(self, headerHeight: int):
        self.__headerHeight = headerHeight

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

    def getNodesFromMapping(self, mapping: str) -> str:
        # TODO: Implement getNodesFromMapping method
        pass

    def getEdgesFromMapping(self, mapping: str) -> str:
        # TODO: Implement getEdgesFromMapping method
        pass

    def getContainersFromMapping(self, mapping: str) -> str:
        # TODO: Implement getContainersFromMapping method
        pass
