from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class NavigationTargetType(Enum):
    model = "model"
    file = "file"
class ResizeKind(Enum):
    NONE = "NONE"
    NSEW = "NSEW"
    NORTH_SOUTH = "NORTH_SOUTH"
    EAST_WEST = "EAST_WEST"
class DragSource(Enum):
    DIAGRAM = "DIAGRAM"
    PROJECT_EXPLORER = "PROJECT_EXPLORER"
    BOTH = "BOTH"
class ArrangeConstraint(Enum):
    KEEP_LOCATION = "KEEP_LOCATION"
    KEEP_SIZE = "KEEP_SIZE"
    KEEP_RATIO = "KEEP_RATIO"
class FilterKind(Enum):
    HIDE = "HIDE"
    COLLAPSE = "COLLAPSE"
class EdgeArrows(Enum):
    NoDecoration = "NoDecoration"
    OutputArrow = "OutputArrow"
    InputArrow = "InputArrow"
    OutputClosedArrow = "OutputClosedArrow"
    InputClosedArrow = "InputClosedArrow"
    OutputFillClosedArrow = "OutputFillClosedArrow"
    InputFillClosedArrow = "InputFillClosedArrow"
    Diamond = "Diamond"
    FillDiamond = "FillDiamond"
    InputArrowWithDiamond = "InputArrowWithDiamond"
    InputArrowWithFillDiamond = "InputArrowWithFillDiamond"
class SystemColors(Enum):
    red = "red"
    green = "green"
    yellow = "yellow"
    purple = "purple"
    orange = "orange"
    chocolate = "chocolate"
    gray = "gray"
    white = "white"
    dark_blue = "dark_blue"
    dark_red = "dark_red"
    dark_green = "dark_green"
    dark_yellow = "dark_yellow"
    dark_purple = "dark_purple"
    dark_orange = "dark_orange"
    black = "black"
    blue = "blue"
    dark_chocolate = "dark_chocolate"
    dark_gray = "dark_gray"
    light_blue = "light_blue"
    light_red = "light_red"
    light_green = "light_green"
    light_yellow = "light_yellow"
    light_purple = "light_purple"
    light_orange = "light_orange"
    light_chocolate = "light_chocolate"
    light_gray = "light_gray"
class BundledImageShape(Enum):
    square = "square"
    stroke = "stroke"
    triangle = "triangle"
    dot = "dot"
    ring = "ring"
class LineStyle(Enum):
    solid = "solid"
    dash = "dash"
    dot = "dot"
    dash_dot = "dash_dot"
class ContainerShape(Enum):
    parallelogram = "parallelogram"
class FoldingStyle(Enum):
    NONE = "NONE"
    SOURCE = "SOURCE"
    TARGET = "TARGET"
class LabelAlignment(Enum):
    CENTER = "CENTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class ContainerLayout(Enum):
    FreeForm = "FreeForm"
    List = "List"
    HorizontalStack = "HorizontalStack"
    VerticalStack = "VerticalStack"
class LabelPosition(Enum):
    border = "border"
    node = "node"
class AlignmentKind(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
    SQUARE = "SQUARE"
class EdgeRouting(Enum):
    straight = "straight"
    manhattan = "manhattan"
    tree = "tree"
class ERROR_LEVEL(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
class Position(Enum):
    NORTH_WEST = "NORTH_WEST"
    NORTH_EAST = "NORTH_EAST"
    SOUTH_WEST = "SOUTH_WEST"
    SOUTH_EAST = "SOUTH_EAST"
    CENTER = "CENTER"
    NORTH = "NORTH"
    WEST = "WEST"
    SOUTH = "SOUTH"
    EAST = "EAST"
class LayoutDirection(Enum):
    TopToBottom = "TopToBottom"
    LeftToRight = "LeftToRight"
    BottomToTop = "BottomToTop"
class ReconnectionKind(Enum):
    RECONNECT_TARGET = "RECONNECT_TARGET"
    RECONNECT_SOURCE = "RECONNECT_SOURCE"
    RECONNECT_BOTH = "RECONNECT_BOTH"
class SyncStatus(Enum):
    dirty = "dirty"
    sync = "sync"
class FontFormat(Enum):
    normal = "normal"
    italic = "italic"
    bold = "bold"
    bold_italic = "bold_italic"
class BackgroundStyle(Enum):
    GradientLeftToRight = "GradientLeftToRight"
    Liquid = "Liquid"
    GradientTopToBottom = "GradientTopToBottom"


############################################
# Definition of Classes
############################################

class viewpoint_tool_EditMaskVariables:

    def __init__(self, mask: str):
        self.mask = mask
        
        pass
    @property
    def mask(self):
        return self.__mask

    @mask.setter
    def mask(self, mask: str):
        self.__mask = mask


class tool_AbstractVariable:

    pass
class AbstractVariable:

    pass
class viewpoint_tool_DialogVariable(AbstractVariable):

    def __init__(self, dialogPrompt: str):
        self.dialogPrompt = dialogPrompt
        
        pass
    @property
    def dialogPrompt(self):
        return self.__dialogPrompt

    @dialogPrompt.setter
    def dialogPrompt(self, dialogPrompt: str):
        self.__dialogPrompt = dialogPrompt


class viewpoint_tool_ElementSelectVariable(AbstractVariable):

    pass
class viewpoint_tool_SubVariable(AbstractVariable):

    pass
class tool_VariableContainer:

    pass
class viewpoint_tool_SelectContainerVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ContainerViewVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ElementVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ElementDropVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class tool_SubVariable:

    pass
class viewpoint_tool_AcceleoVariable(tool_SubVariable, tool_VariableContainer):

    def __init__(self, computationExpression: str, tool_SubVariable: "viewpoint_tool_VariableContainer" = None):
        self.computationExpression = computationExpression
        
        pass
    @property
    def computationExpression(self):
        return self.__computationExpression

    @computationExpression.setter
    def computationExpression(self, computationExpression: str):
        self.__computationExpression = computationExpression


class viewpoint_tool_VariableContainer(ABC):

    pass
class viewpoint_tool_AbstractVariable(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class tool_ExternalJavaAction:

    pass
class viewpoint_validation_ValidationFix:

    def __init__(self, name: str, viewpoint_validation_ValidationFix: "tool_InitialOperation" = None):
        self.name = name
        self.viewpoint_validation_ValidationFix = viewpoint_validation_ValidationFix
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def viewpoint_validation_ValidationFix(self):
        return self.__viewpoint_validation_ValidationFix

    @viewpoint_validation_ValidationFix.setter
    def viewpoint_validation_ValidationFix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_validation_ValidationFix__viewpoint_validation_ValidationFix", None)
        self.__viewpoint_validation_ValidationFix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation742"):
                opp_val = getattr(old_value, "tool_InitialOperation742", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation742", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation742"):
                opp_val = getattr(value, "tool_InitialOperation742", None)
                setattr(value, "tool_InitialOperation742", self)

class ValidationRule:

    pass
class viewpoint_validation_ViewValidationRule(ValidationRule):

    pass
class viewpoint_validation_SemanticValidationRule(ValidationRule):

    def __init__(self, targetClass: str):
        self.targetClass = targetClass
        
        pass
    @property
    def targetClass(self):
        return self.__targetClass

    @targetClass.setter
    def targetClass(self, targetClass: str):
        self.__targetClass = targetClass


class validation_ValidationFix:

    pass
class validation_RuleAudit:

    pass
class viewpoint_validation_ValidationRule(ABC):

    def __init__(self, level: str, message: str, viewpoint_validation_ValidationRule: set["validation_RuleAudit"] = None, viewpoint_validation_ValidationRule738: set["validation_ValidationFix"] = None):
        self.level = level
        self.message = message
        self.viewpoint_validation_ValidationRule = viewpoint_validation_ValidationRule if viewpoint_validation_ValidationRule is not None else set()
        self.viewpoint_validation_ValidationRule738 = viewpoint_validation_ValidationRule738 if viewpoint_validation_ValidationRule738 is not None else set()
        
        pass
    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def viewpoint_validation_ValidationRule(self):
        return self.__viewpoint_validation_ValidationRule

    @viewpoint_validation_ValidationRule.setter
    def viewpoint_validation_ValidationRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_validation_ValidationRule__viewpoint_validation_ValidationRule", None)
        self.__viewpoint_validation_ValidationRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "validation_RuleAudit"):
                    opp_val = getattr(item, "validation_RuleAudit", None)
                    
                    if opp_val == self:
                        setattr(item, "validation_RuleAudit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "validation_RuleAudit"):
                    opp_val = getattr(item, "validation_RuleAudit", None)
                    
                    setattr(item, "validation_RuleAudit", self)
                    

    @property
    def viewpoint_validation_ValidationRule738(self):
        return self.__viewpoint_validation_ValidationRule738

    @viewpoint_validation_ValidationRule738.setter
    def viewpoint_validation_ValidationRule738(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_validation_ValidationRule__viewpoint_validation_ValidationRule738", None)
        self.__viewpoint_validation_ValidationRule738 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "validation_ValidationFix"):
                    opp_val = getattr(item, "validation_ValidationFix", None)
                    
                    if opp_val == self:
                        setattr(item, "validation_ValidationFix", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "validation_ValidationFix"):
                    opp_val = getattr(item, "validation_ValidationFix", None)
                    
                    setattr(item, "validation_ValidationFix", self)
                    

    def getMessage(self, viewpoint_eObj) :
        # TODO: Implement getMessage method
        pass

    def checkRule(self, viewpoint_eObj) :
        # TODO: Implement checkRule method
        pass

class viewpoint_validation_RuleAudit:

    def __init__(self, auditExpression: str):
        self.auditExpression = auditExpression
        
        pass
    @property
    def auditExpression(self):
        return self.__auditExpression

    @auditExpression.setter
    def auditExpression(self, auditExpression: str):
        self.__auditExpression = auditExpression


class SelectionDescription:

    pass
class viewpoint_filter_FilterVariable(SelectionDescription):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class filter_Filter:

    pass
class FilterDescription:

    pass
class viewpoint_filter_CompositeFilterDescription(FilterDescription):

    pass
class Filter:

    pass
class viewpoint_filter_VariableFilter(Filter):

    def __init__(self, semanticConditionExpression: str, viewpoint_filter_VariableFilter: set["filter_FilterVariable"] = None):
        self.semanticConditionExpression = semanticConditionExpression
        self.viewpoint_filter_VariableFilter = viewpoint_filter_VariableFilter if viewpoint_filter_VariableFilter is not None else set()
        
        pass
    @property
    def semanticConditionExpression(self):
        return self.__semanticConditionExpression

    @semanticConditionExpression.setter
    def semanticConditionExpression(self, semanticConditionExpression: str):
        self.__semanticConditionExpression = semanticConditionExpression


    @property
    def viewpoint_filter_VariableFilter(self):
        return self.__viewpoint_filter_VariableFilter

    @viewpoint_filter_VariableFilter.setter
    def viewpoint_filter_VariableFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_filter_VariableFilter__viewpoint_filter_VariableFilter", None)
        self.__viewpoint_filter_VariableFilter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "filter_FilterVariable727"):
                    opp_val = getattr(item, "filter_FilterVariable727", None)
                    
                    if opp_val == self:
                        setattr(item, "filter_FilterVariable727", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filter_FilterVariable727"):
                    opp_val = getattr(item, "filter_FilterVariable727", None)
                    
                    setattr(item, "filter_FilterVariable727", self)
                    

    def setFilterContext(self, viewpoint_variables):
        # TODO: Implement setFilterContext method
        pass

class viewpoint_filter_MappingFilter(Filter):

    def __init__(self, semanticConditionExpression: str, viewConditionExpression: str, viewpoint_filter_MappingFilter: set["description_DiagramElementMapping"] = None):
        self.semanticConditionExpression = semanticConditionExpression
        self.viewConditionExpression = viewConditionExpression
        self.viewpoint_filter_MappingFilter = viewpoint_filter_MappingFilter if viewpoint_filter_MappingFilter is not None else set()
        
        pass
    @property
    def viewConditionExpression(self):
        return self.__viewConditionExpression

    @viewConditionExpression.setter
    def viewConditionExpression(self, viewConditionExpression: str):
        self.__viewConditionExpression = viewConditionExpression


    @property
    def semanticConditionExpression(self):
        return self.__semanticConditionExpression

    @semanticConditionExpression.setter
    def semanticConditionExpression(self, semanticConditionExpression: str):
        self.__semanticConditionExpression = semanticConditionExpression


    @property
    def viewpoint_filter_MappingFilter(self):
        return self.__viewpoint_filter_MappingFilter

    @viewpoint_filter_MappingFilter.setter
    def viewpoint_filter_MappingFilter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_filter_MappingFilter__viewpoint_filter_MappingFilter", None)
        self.__viewpoint_filter_MappingFilter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_DiagramElementMapping724"):
                    opp_val = getattr(item, "description_DiagramElementMapping724", None)
                    
                    if opp_val == self:
                        setattr(item, "description_DiagramElementMapping724", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_DiagramElementMapping724"):
                    opp_val = getattr(item, "description_DiagramElementMapping724", None)
                    
                    setattr(item, "description_DiagramElementMapping724", self)
                    

class viewpoint_filter_Filter(ABC):

    def __init__(self, filterKind: str):
        self.filterKind = filterKind
        
        pass
    @property
    def filterKind(self):
        return self.__filterKind

    @filterKind.setter
    def filterKind(self, filterKind: str):
        self.__filterKind = filterKind


    def isVisible(self, viewpoint_element) :
        # TODO: Implement isVisible method
        pass

class RepresentationNavigationDescription:

    pass
class CreateView:

    pass
class viewpoint_tool_DiagramNavigationDescription(RepresentationNavigationDescription):

    pass
class viewpoint_tool_CreateEdgeView(CreateView):

    def __init__(self, sourceExpression: str, targetExpression: str):
        self.sourceExpression = sourceExpression
        self.targetExpression = targetExpression
        
        pass
    @property
    def sourceExpression(self):
        return self.__sourceExpression

    @sourceExpression.setter
    def sourceExpression(self, sourceExpression: str):
        self.__sourceExpression = sourceExpression


    @property
    def targetExpression(self):
        return self.__targetExpression

    @targetExpression.setter
    def targetExpression(self, targetExpression: str):
        self.__targetExpression = targetExpression


class RepresentationCreationDescription:

    pass
class viewpoint_tool_DiagramCreationDescription(RepresentationCreationDescription):

    pass
class viewpoint_tool_NodeCreationVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ElementDoubleClickVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_TargetEdgeViewCreationVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_TargetEdgeCreationVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_SourceEdgeViewCreationVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_SourceEdgeCreationVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class tool_EditMaskVariables:

    pass
class tool_ElementDoubleClickVariable:

    pass
class tool_DeleteHook:

    pass
class viewpoint_tool_DeleteHookParameter:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class tool_DeleteHookParameter:

    pass
class viewpoint_tool_DeleteHook:

    def __init__(self, id: str, viewpoint_tool_DeleteHook: set["tool_DeleteHookParameter"] = None):
        self.id = id
        self.viewpoint_tool_DeleteHook = viewpoint_tool_DeleteHook if viewpoint_tool_DeleteHook is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def viewpoint_tool_DeleteHook(self):
        return self.__viewpoint_tool_DeleteHook

    @viewpoint_tool_DeleteHook.setter
    def viewpoint_tool_DeleteHook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_DeleteHook__viewpoint_tool_DeleteHook", None)
        self.__viewpoint_tool_DeleteHook = value if value is not None else set()
        
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
                    

class tool_ElementDeleteVariable:

    pass
class tool_TargetEdgeViewCreationVariable:

    pass
class tool_SourceEdgeViewCreationVariable:

    pass
class tool_TargetEdgeCreationVariable:

    pass
class tool_SourceEdgeCreationVariable:

    pass
class tool_InitEdgeCreationOperation:

    pass
class tool_InitialNodeCreationOperation:

    pass
class tool_NodeCreationVariable:

    pass
class tool_PopupMenu:

    pass
class tool_ToolGroup:

    pass
class viewpoint_tool_ToolGroupExtension:

    pass
class tool_ToolGroupExtension:

    pass
class style_BeginLabelStyleDescription:

    pass
class EdgeStyleDescription:

    pass
class viewpoint_style_BracketEdgeStyleDescription(EdgeStyleDescription):

    pass
class style_EndLabelStyleDescription:

    pass
class style_CenterLabelStyleDescription:

    pass
class viewpoint_style_SizeComputationContainerStyleDescription(ABC):

    def __init__(self, widthComputationExpression: str, heightComputationExpression: str):
        self.widthComputationExpression = widthComputationExpression
        self.heightComputationExpression = heightComputationExpression
        
        pass
    @property
    def widthComputationExpression(self):
        return self.__widthComputationExpression

    @widthComputationExpression.setter
    def widthComputationExpression(self, widthComputationExpression: str):
        self.__widthComputationExpression = widthComputationExpression


    @property
    def heightComputationExpression(self):
        return self.__heightComputationExpression

    @heightComputationExpression.setter
    def heightComputationExpression(self, heightComputationExpression: str):
        self.__heightComputationExpression = heightComputationExpression


class style_SizeComputationContainerStyleDescription:

    pass
class style_RoundedCornerStyleDescription:

    pass
class viewpoint_style_GaugeSectionDescription:

    def __init__(self, valueExpression: str, minValueExpression: str, maxValueExpression: str, label: str, viewpoint_style_GaugeSectionDescription: "ColorDescription" = None, viewpoint_style_GaugeSectionDescription586: "ColorDescription" = None):
        self.valueExpression = valueExpression
        self.minValueExpression = minValueExpression
        self.maxValueExpression = maxValueExpression
        self.label = label
        self.viewpoint_style_GaugeSectionDescription = viewpoint_style_GaugeSectionDescription
        self.viewpoint_style_GaugeSectionDescription586 = viewpoint_style_GaugeSectionDescription586
        
        pass
    @property
    def maxValueExpression(self):
        return self.__maxValueExpression

    @maxValueExpression.setter
    def maxValueExpression(self, maxValueExpression: str):
        self.__maxValueExpression = maxValueExpression


    @property
    def valueExpression(self):
        return self.__valueExpression

    @valueExpression.setter
    def valueExpression(self, valueExpression: str):
        self.__valueExpression = valueExpression


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def minValueExpression(self):
        return self.__minValueExpression

    @minValueExpression.setter
    def minValueExpression(self, minValueExpression: str):
        self.__minValueExpression = minValueExpression


    @property
    def viewpoint_style_GaugeSectionDescription(self):
        return self.__viewpoint_style_GaugeSectionDescription

    @viewpoint_style_GaugeSectionDescription.setter
    def viewpoint_style_GaugeSectionDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_GaugeSectionDescription__viewpoint_style_GaugeSectionDescription", None)
        self.__viewpoint_style_GaugeSectionDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription584"):
                opp_val = getattr(old_value, "ColorDescription584", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription584", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription584"):
                opp_val = getattr(value, "ColorDescription584", None)
                setattr(value, "ColorDescription584", self)

    @property
    def viewpoint_style_GaugeSectionDescription586(self):
        return self.__viewpoint_style_GaugeSectionDescription586

    @viewpoint_style_GaugeSectionDescription586.setter
    def viewpoint_style_GaugeSectionDescription586(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_GaugeSectionDescription__viewpoint_style_GaugeSectionDescription586", None)
        self.__viewpoint_style_GaugeSectionDescription586 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription587"):
                opp_val = getattr(old_value, "ColorDescription587", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription587", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription587"):
                opp_val = getattr(value, "ColorDescription587", None)
                setattr(value, "ColorDescription587", self)

class style_GaugeSectionDescription:

    pass
class NodeStyleDescription:

    pass
class viewpoint_style_LozengeNodeDescription(NodeStyleDescription):

    def __init__(self, widthComputationExpression: str, heightComputationExpression: str, viewpoint_style_LozengeNodeDescription: "ColorDescription" = None):
        self.widthComputationExpression = widthComputationExpression
        self.heightComputationExpression = heightComputationExpression
        self.viewpoint_style_LozengeNodeDescription = viewpoint_style_LozengeNodeDescription
        
        pass
    @property
    def widthComputationExpression(self):
        return self.__widthComputationExpression

    @widthComputationExpression.setter
    def widthComputationExpression(self, widthComputationExpression: str):
        self.__widthComputationExpression = widthComputationExpression


    @property
    def heightComputationExpression(self):
        return self.__heightComputationExpression

    @heightComputationExpression.setter
    def heightComputationExpression(self, heightComputationExpression: str):
        self.__heightComputationExpression = heightComputationExpression


    @property
    def viewpoint_style_LozengeNodeDescription(self):
        return self.__viewpoint_style_LozengeNodeDescription

    @viewpoint_style_LozengeNodeDescription.setter
    def viewpoint_style_LozengeNodeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_LozengeNodeDescription__viewpoint_style_LozengeNodeDescription", None)
        self.__viewpoint_style_LozengeNodeDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription573"):
                opp_val = getattr(old_value, "ColorDescription573", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription573", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription573"):
                opp_val = getattr(value, "ColorDescription573", None)
                setattr(value, "ColorDescription573", self)

class viewpoint_style_GaugeCompositeStyleDescription(NodeStyleDescription):

    def __init__(self, alignment: str, viewpoint_style_GaugeCompositeStyleDescription: set["style_GaugeSectionDescription"] = None):
        self.alignment = alignment
        self.viewpoint_style_GaugeCompositeStyleDescription = viewpoint_style_GaugeCompositeStyleDescription if viewpoint_style_GaugeCompositeStyleDescription is not None else set()
        
        pass
    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment


    @property
    def viewpoint_style_GaugeCompositeStyleDescription(self):
        return self.__viewpoint_style_GaugeCompositeStyleDescription

    @viewpoint_style_GaugeCompositeStyleDescription.setter
    def viewpoint_style_GaugeCompositeStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_GaugeCompositeStyleDescription__viewpoint_style_GaugeCompositeStyleDescription", None)
        self.__viewpoint_style_GaugeCompositeStyleDescription = value if value is not None else set()
        
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
                    

class viewpoint_style_BundledImageDescription(NodeStyleDescription):

    def __init__(self, shape: str, viewpoint_style_BundledImageDescription: "ColorDescription" = None):
        self.shape = shape
        self.viewpoint_style_BundledImageDescription = viewpoint_style_BundledImageDescription
        
        pass
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def viewpoint_style_BundledImageDescription(self):
        return self.__viewpoint_style_BundledImageDescription

    @viewpoint_style_BundledImageDescription.setter
    def viewpoint_style_BundledImageDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_BundledImageDescription__viewpoint_style_BundledImageDescription", None)
        self.__viewpoint_style_BundledImageDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription577"):
                opp_val = getattr(old_value, "ColorDescription577", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription577", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription577"):
                opp_val = getattr(value, "ColorDescription577", None)
                setattr(value, "ColorDescription577", self)

class viewpoint_style_NoteDescription(NodeStyleDescription):

    pass
class viewpoint_style_SquareDescription(NodeStyleDescription):

    def __init__(self, width: str, height: str, viewpoint_style_SquareDescription: "ColorDescription" = None):
        self.width = width
        self.height = height
        self.viewpoint_style_SquareDescription = viewpoint_style_SquareDescription
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def viewpoint_style_SquareDescription(self):
        return self.__viewpoint_style_SquareDescription

    @viewpoint_style_SquareDescription.setter
    def viewpoint_style_SquareDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_SquareDescription__viewpoint_style_SquareDescription", None)
        self.__viewpoint_style_SquareDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription571"):
                opp_val = getattr(old_value, "ColorDescription571", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription571", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription571"):
                opp_val = getattr(value, "ColorDescription571", None)
                setattr(value, "ColorDescription571", self)

class viewpoint_style_DotDescription(NodeStyleDescription):

    def __init__(self, strokeSizeComputationExpression: str, viewpoint_style_DotDescription: "ColorDescription" = None):
        self.strokeSizeComputationExpression = strokeSizeComputationExpression
        self.viewpoint_style_DotDescription = viewpoint_style_DotDescription
        
        pass
    @property
    def strokeSizeComputationExpression(self):
        return self.__strokeSizeComputationExpression

    @strokeSizeComputationExpression.setter
    def strokeSizeComputationExpression(self, strokeSizeComputationExpression: str):
        self.__strokeSizeComputationExpression = strokeSizeComputationExpression


    @property
    def viewpoint_style_DotDescription(self):
        return self.__viewpoint_style_DotDescription

    @viewpoint_style_DotDescription.setter
    def viewpoint_style_DotDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_DotDescription__viewpoint_style_DotDescription", None)
        self.__viewpoint_style_DotDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription581"):
                opp_val = getattr(old_value, "ColorDescription581", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription581", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription581"):
                opp_val = getattr(value, "ColorDescription581", None)
                setattr(value, "ColorDescription581", self)

class viewpoint_style_CustomStyleDescription(NodeStyleDescription):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class viewpoint_style_EllipseNodeDescription(NodeStyleDescription):

    def __init__(self, horizontalDiameterComputationExpression: str, verticalDiameterComputationExpression: str, viewpoint_style_EllipseNodeDescription: "ColorDescription" = None):
        self.horizontalDiameterComputationExpression = horizontalDiameterComputationExpression
        self.verticalDiameterComputationExpression = verticalDiameterComputationExpression
        self.viewpoint_style_EllipseNodeDescription = viewpoint_style_EllipseNodeDescription
        
        pass
    @property
    def horizontalDiameterComputationExpression(self):
        return self.__horizontalDiameterComputationExpression

    @horizontalDiameterComputationExpression.setter
    def horizontalDiameterComputationExpression(self, horizontalDiameterComputationExpression: str):
        self.__horizontalDiameterComputationExpression = horizontalDiameterComputationExpression


    @property
    def verticalDiameterComputationExpression(self):
        return self.__verticalDiameterComputationExpression

    @verticalDiameterComputationExpression.setter
    def verticalDiameterComputationExpression(self, verticalDiameterComputationExpression: str):
        self.__verticalDiameterComputationExpression = verticalDiameterComputationExpression


    @property
    def viewpoint_style_EllipseNodeDescription(self):
        return self.__viewpoint_style_EllipseNodeDescription

    @viewpoint_style_EllipseNodeDescription.setter
    def viewpoint_style_EllipseNodeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_EllipseNodeDescription__viewpoint_style_EllipseNodeDescription", None)
        self.__viewpoint_style_EllipseNodeDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription575"):
                opp_val = getattr(old_value, "ColorDescription575", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription575", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription575"):
                opp_val = getattr(value, "ColorDescription575", None)
                setattr(value, "ColorDescription575", self)

class style_TooltipStyleDescription:

    pass
class style_LabelStyleDescription:

    pass
class style_BorderedStyleDescription:

    pass
class viewpoint_style_ContainerStyleDescription(style_LabelStyleDescription, style_BorderedStyleDescription, style_RoundedCornerStyleDescription, style_TooltipStyleDescription):

    def __init__(self, roundedCorner: bool):
        self.roundedCorner = roundedCorner
        
        pass
    @property
    def roundedCorner(self):
        return self.__roundedCorner

    @roundedCorner.setter
    def roundedCorner(self, roundedCorner: bool):
        self.__roundedCorner = roundedCorner


class StyleDescription:

    pass
class viewpoint_style_EdgeStyleDescription(StyleDescription):

    def __init__(self, lineStyle: str, sourceArrow: str, targetArrow: str, sizeComputationExpression: str, routingStyle: str, foldingStyle: str, viewpoint_style_EdgeStyleDescription: "ColorDescription" = None, viewpoint_style_EdgeStyleDescription603: "style_CenterLabelStyleDescription" = None, viewpoint_style_EdgeStyleDescription605: "style_EndLabelStyleDescription" = None, viewpoint_style_EdgeStyleDescription601: "style_BeginLabelStyleDescription" = None):
        self.lineStyle = lineStyle
        self.sourceArrow = sourceArrow
        self.targetArrow = targetArrow
        self.sizeComputationExpression = sizeComputationExpression
        self.routingStyle = routingStyle
        self.foldingStyle = foldingStyle
        self.viewpoint_style_EdgeStyleDescription = viewpoint_style_EdgeStyleDescription
        self.viewpoint_style_EdgeStyleDescription603 = viewpoint_style_EdgeStyleDescription603
        self.viewpoint_style_EdgeStyleDescription605 = viewpoint_style_EdgeStyleDescription605
        self.viewpoint_style_EdgeStyleDescription601 = viewpoint_style_EdgeStyleDescription601
        
        pass
    @property
    def sizeComputationExpression(self):
        return self.__sizeComputationExpression

    @sizeComputationExpression.setter
    def sizeComputationExpression(self, sizeComputationExpression: str):
        self.__sizeComputationExpression = sizeComputationExpression


    @property
    def routingStyle(self):
        return self.__routingStyle

    @routingStyle.setter
    def routingStyle(self, routingStyle: str):
        self.__routingStyle = routingStyle


    @property
    def foldingStyle(self):
        return self.__foldingStyle

    @foldingStyle.setter
    def foldingStyle(self, foldingStyle: str):
        self.__foldingStyle = foldingStyle


    @property
    def targetArrow(self):
        return self.__targetArrow

    @targetArrow.setter
    def targetArrow(self, targetArrow: str):
        self.__targetArrow = targetArrow


    @property
    def sourceArrow(self):
        return self.__sourceArrow

    @sourceArrow.setter
    def sourceArrow(self, sourceArrow: str):
        self.__sourceArrow = sourceArrow


    @property
    def lineStyle(self):
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle


    @property
    def viewpoint_style_EdgeStyleDescription603(self):
        return self.__viewpoint_style_EdgeStyleDescription603

    @viewpoint_style_EdgeStyleDescription603.setter
    def viewpoint_style_EdgeStyleDescription603(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_EdgeStyleDescription__viewpoint_style_EdgeStyleDescription603", None)
        self.__viewpoint_style_EdgeStyleDescription603 = value
        
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
    def viewpoint_style_EdgeStyleDescription605(self):
        return self.__viewpoint_style_EdgeStyleDescription605

    @viewpoint_style_EdgeStyleDescription605.setter
    def viewpoint_style_EdgeStyleDescription605(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_EdgeStyleDescription__viewpoint_style_EdgeStyleDescription605", None)
        self.__viewpoint_style_EdgeStyleDescription605 = value
        
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
    def viewpoint_style_EdgeStyleDescription601(self):
        return self.__viewpoint_style_EdgeStyleDescription601

    @viewpoint_style_EdgeStyleDescription601.setter
    def viewpoint_style_EdgeStyleDescription601(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_EdgeStyleDescription__viewpoint_style_EdgeStyleDescription601", None)
        self.__viewpoint_style_EdgeStyleDescription601 = value
        
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
    def viewpoint_style_EdgeStyleDescription(self):
        return self.__viewpoint_style_EdgeStyleDescription

    @viewpoint_style_EdgeStyleDescription.setter
    def viewpoint_style_EdgeStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_EdgeStyleDescription__viewpoint_style_EdgeStyleDescription", None)
        self.__viewpoint_style_EdgeStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription599"):
                opp_val = getattr(old_value, "ColorDescription599", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription599", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription599"):
                opp_val = getattr(value, "ColorDescription599", None)
                setattr(value, "ColorDescription599", self)

class viewpoint_style_RoundedCornerStyleDescription(StyleDescription):

    def __init__(self, arcHeight: str, arcWidth: str):
        self.arcHeight = arcHeight
        self.arcWidth = arcWidth
        
        pass
    @property
    def arcHeight(self):
        return self.__arcHeight

    @arcHeight.setter
    def arcHeight(self, arcHeight: str):
        self.__arcHeight = arcHeight


    @property
    def arcWidth(self):
        return self.__arcWidth

    @arcWidth.setter
    def arcWidth(self, arcWidth: str):
        self.__arcWidth = arcWidth


class viewpoint_style_BorderedStyleDescription(StyleDescription):

    def __init__(self, borderSizeComputationExpression: str, viewpoint_style_BorderedStyleDescription: "ColorDescription" = None):
        self.borderSizeComputationExpression = borderSizeComputationExpression
        self.viewpoint_style_BorderedStyleDescription = viewpoint_style_BorderedStyleDescription
        
        pass
    @property
    def borderSizeComputationExpression(self):
        return self.__borderSizeComputationExpression

    @borderSizeComputationExpression.setter
    def borderSizeComputationExpression(self, borderSizeComputationExpression: str):
        self.__borderSizeComputationExpression = borderSizeComputationExpression


    @property
    def viewpoint_style_BorderedStyleDescription(self):
        return self.__viewpoint_style_BorderedStyleDescription

    @viewpoint_style_BorderedStyleDescription.setter
    def viewpoint_style_BorderedStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_BorderedStyleDescription__viewpoint_style_BorderedStyleDescription", None)
        self.__viewpoint_style_BorderedStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription569"):
                opp_val = getattr(old_value, "ColorDescription569", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription569", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription569"):
                opp_val = getattr(value, "ColorDescription569", None)
                setattr(value, "ColorDescription569", self)

class Layer:

    pass
class viewpoint_description_AdditionalLayer(Layer):

    def __init__(self, activeByDefault: bool, optional: bool):
        self.activeByDefault = activeByDefault
        self.optional = optional
        
        pass
    @property
    def activeByDefault(self):
        return self.__activeByDefault

    @activeByDefault.setter
    def activeByDefault(self, activeByDefault: bool):
        self.__activeByDefault = activeByDefault


    @property
    def optional(self):
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional


class Customization:

    pass
class DecorationDescriptionsSet:

    pass
class Layout:

    pass
class viewpoint_description_CompositeLayout(Layout):

    def __init__(self, padding: int, direction: str):
        self.padding = padding
        self.direction = direction
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def padding(self):
        return self.__padding

    @padding.setter
    def padding(self, padding: int):
        self.__padding = padding


class viewpoint_description_OrderedTreeLayout(Layout):

    def __init__(self, childrenExpression: str, viewpoint_description_OrderedTreeLayout: set["description_AbstractNodeMapping"] = None):
        self.childrenExpression = childrenExpression
        self.viewpoint_description_OrderedTreeLayout = viewpoint_description_OrderedTreeLayout if viewpoint_description_OrderedTreeLayout is not None else set()
        
        pass
    @property
    def childrenExpression(self):
        return self.__childrenExpression

    @childrenExpression.setter
    def childrenExpression(self, childrenExpression: str):
        self.__childrenExpression = childrenExpression


    @property
    def viewpoint_description_OrderedTreeLayout(self):
        return self.__viewpoint_description_OrderedTreeLayout

    @viewpoint_description_OrderedTreeLayout.setter
    def viewpoint_description_OrderedTreeLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_OrderedTreeLayout__viewpoint_description_OrderedTreeLayout", None)
        self.__viewpoint_description_OrderedTreeLayout = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_AbstractNodeMapping535"):
                    opp_val = getattr(item, "description_AbstractNodeMapping535", None)
                    
                    if opp_val == self:
                        setattr(item, "description_AbstractNodeMapping535", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_AbstractNodeMapping535"):
                    opp_val = getattr(item, "description_AbstractNodeMapping535", None)
                    
                    setattr(item, "description_AbstractNodeMapping535", self)
                    

class DocumentedElement:

    pass
class viewpoint_concern_ConcernSet(DocumentedElement):

    pass
class viewpoint_validation_ValidationSet(DocumentedElement):

    def __init__(self, name: str, viewpoint_validation_ValidationSet731: set["validation_ValidationRule"] = None, viewpoint_validation_ValidationSet734: set["validation_ValidationRule"] = None, viewpoint_validation_ValidationSet: set["validation_ValidationRule"] = None):
        self.name = name
        self.viewpoint_validation_ValidationSet731 = viewpoint_validation_ValidationSet731 if viewpoint_validation_ValidationSet731 is not None else set()
        self.viewpoint_validation_ValidationSet734 = viewpoint_validation_ValidationSet734 if viewpoint_validation_ValidationSet734 is not None else set()
        self.viewpoint_validation_ValidationSet = viewpoint_validation_ValidationSet if viewpoint_validation_ValidationSet is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def viewpoint_validation_ValidationSet734(self):
        return self.__viewpoint_validation_ValidationSet734

    @viewpoint_validation_ValidationSet734.setter
    def viewpoint_validation_ValidationSet734(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_validation_ValidationSet__viewpoint_validation_ValidationSet734", None)
        self.__viewpoint_validation_ValidationSet734 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "validation_ValidationRule735"):
                    opp_val = getattr(item, "validation_ValidationRule735", None)
                    
                    if opp_val == self:
                        setattr(item, "validation_ValidationRule735", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "validation_ValidationRule735"):
                    opp_val = getattr(item, "validation_ValidationRule735", None)
                    
                    setattr(item, "validation_ValidationRule735", self)
                    

    @property
    def viewpoint_validation_ValidationSet731(self):
        return self.__viewpoint_validation_ValidationSet731

    @viewpoint_validation_ValidationSet731.setter
    def viewpoint_validation_ValidationSet731(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_validation_ValidationSet__viewpoint_validation_ValidationSet731", None)
        self.__viewpoint_validation_ValidationSet731 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "validation_ValidationRule732"):
                    opp_val = getattr(item, "validation_ValidationRule732", None)
                    
                    if opp_val == self:
                        setattr(item, "validation_ValidationRule732", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "validation_ValidationRule732"):
                    opp_val = getattr(item, "validation_ValidationRule732", None)
                    
                    setattr(item, "validation_ValidationRule732", self)
                    

    @property
    def viewpoint_validation_ValidationSet(self):
        return self.__viewpoint_validation_ValidationSet

    @viewpoint_validation_ValidationSet.setter
    def viewpoint_validation_ValidationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_validation_ValidationSet__viewpoint_validation_ValidationSet", None)
        self.__viewpoint_validation_ValidationSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "validation_ValidationRule729"):
                    opp_val = getattr(item, "validation_ValidationRule729", None)
                    
                    if opp_val == self:
                        setattr(item, "validation_ValidationRule729", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "validation_ValidationRule729"):
                    opp_val = getattr(item, "validation_ValidationRule729", None)
                    
                    setattr(item, "validation_ValidationRule729", self)
                    

class viewpoint_description_Layout(DocumentedElement):

    pass
class ConditionalStyleDescription:

    pass
class viewpoint_description_ConditionalContainerStyleDescription(ConditionalStyleDescription):

    pass
class viewpoint_description_ConditionalEdgeStyleDescription(ConditionalStyleDescription):

    pass
class viewpoint_description_ConditionalNodeStyleDescription(ConditionalStyleDescription):

    pass
class description_ConditionalEdgeStyleDescription:

    pass
class style_EdgeStyleDescription:

    pass
class viewpoint_description_IEdgeMapping(ABC):

    def __init__(self):
        
        pass
    def getBestStyle(self, viewpoint_viewVariable, viewpoint_containerVariable, viewpoint_modelElement) :
        # TODO: Implement getBestStyle method
        pass

class tool_ReconnectEdgeDescription:

    pass
class description_ConditionalContainerStyleDescription:

    pass
class style_ContainerStyleDescription:

    pass
class viewpoint_style_ShapeContainerStyleDescription(style_SizeComputationContainerStyleDescription, style_ContainerStyleDescription):

    def __init__(self, shape: str, viewpoint_style_ShapeContainerStyleDescription: "ColorDescription" = None, style_ContainerStyleDescription533: "viewpoint_description_ConditionalContainerStyleDescription" = None, style_ContainerStyleDescription: "viewpoint_description_ContainerMapping" = None):
        self.shape = shape
        self.viewpoint_style_ShapeContainerStyleDescription = viewpoint_style_ShapeContainerStyleDescription
        
        pass
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def viewpoint_style_ShapeContainerStyleDescription(self):
        return self.__viewpoint_style_ShapeContainerStyleDescription

    @viewpoint_style_ShapeContainerStyleDescription.setter
    def viewpoint_style_ShapeContainerStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_ShapeContainerStyleDescription__viewpoint_style_ShapeContainerStyleDescription", None)
        self.__viewpoint_style_ShapeContainerStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription597"):
                opp_val = getattr(old_value, "ColorDescription597", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription597", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription597"):
                opp_val = getattr(value, "ColorDescription597", None)
                setattr(value, "ColorDescription597", self)

class viewpoint_style_FlatContainerStyleDescription(style_SizeComputationContainerStyleDescription, style_ContainerStyleDescription):

    def __init__(self, backgroundStyle: str, viewpoint_style_FlatContainerStyleDescription: "ColorDescription" = None, viewpoint_style_FlatContainerStyleDescription591: "ColorDescription" = None, viewpoint_style_FlatContainerStyleDescription594: "style_LabelBorderStyleDescription" = None, style_ContainerStyleDescription533: "viewpoint_description_ConditionalContainerStyleDescription" = None, style_ContainerStyleDescription: "viewpoint_description_ContainerMapping" = None):
        self.backgroundStyle = backgroundStyle
        self.viewpoint_style_FlatContainerStyleDescription = viewpoint_style_FlatContainerStyleDescription
        self.viewpoint_style_FlatContainerStyleDescription591 = viewpoint_style_FlatContainerStyleDescription591
        self.viewpoint_style_FlatContainerStyleDescription594 = viewpoint_style_FlatContainerStyleDescription594
        
        pass
    @property
    def backgroundStyle(self):
        return self.__backgroundStyle

    @backgroundStyle.setter
    def backgroundStyle(self, backgroundStyle: str):
        self.__backgroundStyle = backgroundStyle


    @property
    def viewpoint_style_FlatContainerStyleDescription(self):
        return self.__viewpoint_style_FlatContainerStyleDescription

    @viewpoint_style_FlatContainerStyleDescription.setter
    def viewpoint_style_FlatContainerStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_FlatContainerStyleDescription__viewpoint_style_FlatContainerStyleDescription", None)
        self.__viewpoint_style_FlatContainerStyleDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription589"):
                opp_val = getattr(old_value, "ColorDescription589", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription589", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription589"):
                opp_val = getattr(value, "ColorDescription589", None)
                setattr(value, "ColorDescription589", self)

    @property
    def viewpoint_style_FlatContainerStyleDescription594(self):
        return self.__viewpoint_style_FlatContainerStyleDescription594

    @viewpoint_style_FlatContainerStyleDescription594.setter
    def viewpoint_style_FlatContainerStyleDescription594(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_FlatContainerStyleDescription__viewpoint_style_FlatContainerStyleDescription594", None)
        self.__viewpoint_style_FlatContainerStyleDescription594 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "style_LabelBorderStyleDescription595"):
                opp_val = getattr(old_value, "style_LabelBorderStyleDescription595", None)
                if opp_val == self:
                    setattr(old_value, "style_LabelBorderStyleDescription595", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "style_LabelBorderStyleDescription595"):
                opp_val = getattr(value, "style_LabelBorderStyleDescription595", None)
                setattr(value, "style_LabelBorderStyleDescription595", self)

    @property
    def viewpoint_style_FlatContainerStyleDescription591(self):
        return self.__viewpoint_style_FlatContainerStyleDescription591

    @viewpoint_style_FlatContainerStyleDescription591.setter
    def viewpoint_style_FlatContainerStyleDescription591(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_FlatContainerStyleDescription__viewpoint_style_FlatContainerStyleDescription591", None)
        self.__viewpoint_style_FlatContainerStyleDescription591 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ColorDescription592"):
                opp_val = getattr(old_value, "ColorDescription592", None)
                if opp_val == self:
                    setattr(old_value, "ColorDescription592", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ColorDescription592"):
                opp_val = getattr(value, "ColorDescription592", None)
                setattr(value, "ColorDescription592", self)

class description_AbstractMappingImport:

    pass
class description_ConditionalNodeStyleDescription:

    pass
class style_NodeStyleDescription:

    pass
class viewpoint_style_WorkspaceImageDescription(style_NodeStyleDescription, style_ContainerStyleDescription):

    def __init__(self, workspacePath: str, style_NodeStyleDescription529: "viewpoint_description_ConditionalNodeStyleDescription" = None, style_NodeStyleDescription: "viewpoint_description_NodeMapping" = None, style_ContainerStyleDescription533: "viewpoint_description_ConditionalContainerStyleDescription" = None, style_ContainerStyleDescription: "viewpoint_description_ContainerMapping" = None):
        self.workspacePath = workspacePath
        
        pass
    @property
    def workspacePath(self):
        return self.__workspacePath

    @workspacePath.setter
    def workspacePath(self, workspacePath: str):
        self.__workspacePath = workspacePath


class tool_DoubleClickDescription:

    pass
class description_AbstractNodeMapping:

    pass
class tool_DirectEditLabel:

    pass
class tool_DeleteElementDescription:

    pass
class tool_ToolSection:

    pass
class description_RepresentationElementMapping:

    pass
class description_RepresentationImportDescription:

    pass
class description_AdditionalLayer:

    pass
class description_Layout:

    pass
class description_EdgeMappingImport:

    pass
class description_EdgeMapping:

    pass
class concern_ConcernSet:

    pass
class ModelElement2ViewVariable:

    pass
class viewpoint_diagram_DiagramElementMapping2ModelElement:

    pass
class DiagramElementMapping2ModelElement:

    pass
class viewpoint_diagram_ComputedStyleDescriptionRegistry:

    pass
class description_PasteTargetDescription:

    pass
class viewpoint_description_DiagramElementMapping(description_PasteTargetDescription, description_RepresentationElementMapping):

    def __init__(self, preconditionExpression: str, semanticCandidatesExpression: str, createElements: bool, semanticElements: str, synchronizationLock: bool, viewpoint_description_DiagramElementMapping: "tool_DeleteElementDescription" = None, viewpoint_description_DiagramElementMapping475: "tool_DirectEditLabel" = None, mappings: "tool_DoubleClickDescription" = None):
        self.preconditionExpression = preconditionExpression
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.createElements = createElements
        self.semanticElements = semanticElements
        self.synchronizationLock = synchronizationLock
        self.viewpoint_description_DiagramElementMapping = viewpoint_description_DiagramElementMapping
        self.viewpoint_description_DiagramElementMapping475 = viewpoint_description_DiagramElementMapping475
        self.mappings = mappings
        
        pass
    @property
    def preconditionExpression(self):
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression


    @property
    def semanticCandidatesExpression(self):
        return self.__semanticCandidatesExpression

    @semanticCandidatesExpression.setter
    def semanticCandidatesExpression(self, semanticCandidatesExpression: str):
        self.__semanticCandidatesExpression = semanticCandidatesExpression


    @property
    def semanticElements(self):
        return self.__semanticElements

    @semanticElements.setter
    def semanticElements(self, semanticElements: str):
        self.__semanticElements = semanticElements


    @property
    def synchronizationLock(self):
        return self.__synchronizationLock

    @synchronizationLock.setter
    def synchronizationLock(self, synchronizationLock: bool):
        self.__synchronizationLock = synchronizationLock


    @property
    def createElements(self):
        return self.__createElements

    @createElements.setter
    def createElements(self, createElements: bool):
        self.__createElements = createElements


    @property
    def viewpoint_description_DiagramElementMapping(self):
        return self.__viewpoint_description_DiagramElementMapping

    @viewpoint_description_DiagramElementMapping.setter
    def viewpoint_description_DiagramElementMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramElementMapping__viewpoint_description_DiagramElementMapping", None)
        self.__viewpoint_description_DiagramElementMapping = value
        
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

    @property
    def mappings(self):
        return self.__mappings

    @mappings.setter
    def mappings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramElementMapping__mappings", None)
        self.__mappings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DoubleClickDescription"):
                opp_val = getattr(old_value, "DoubleClickDescription", None)
                if opp_val == self:
                    setattr(old_value, "DoubleClickDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DoubleClickDescription"):
                opp_val = getattr(value, "DoubleClickDescription", None)
                setattr(value, "DoubleClickDescription", self)

    @property
    def viewpoint_description_DiagramElementMapping475(self):
        return self.__viewpoint_description_DiagramElementMapping475

    @viewpoint_description_DiagramElementMapping475.setter
    def viewpoint_description_DiagramElementMapping475(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramElementMapping__viewpoint_description_DiagramElementMapping475", None)
        self.__viewpoint_description_DiagramElementMapping475 = value
        
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

    def isFrom(self, viewpoint_element) :
        # TODO: Implement isFrom method
        pass

    def checkPrecondition(self, viewpoint_modelElement, viewpoint_containerView, viewpoint_container) :
        # TODO: Implement checkPrecondition method
        pass

    def getAllMappings(self) :
        # TODO: Implement getAllMappings method
        pass

class description_RepresentationDescription:

    pass
class description_DragAndDropTargetDescription:

    pass
class viewpoint_description_ContainerMapping(description_DragAndDropTargetDescription, description_AbstractNodeMapping):

    def __init__(self, childrenPresentation: str, viewpoint_description_ContainerMapping: set["description_NodeMapping"] = None, viewpoint_description_ContainerMapping488: set["description_NodeMapping"] = None, viewpoint_description_ContainerMapping491: set["description_NodeMapping"] = None, viewpoint_description_ContainerMapping494: set["description_ContainerMapping"] = None, viewpoint_description_ContainerMapping497: set["description_ContainerMapping"] = None, viewpoint_description_ContainerMapping500: set["description_ContainerMapping"] = None, viewpoint_description_ContainerMapping503: "style_ContainerStyleDescription" = None, viewpoint_description_ContainerMapping505: set["description_ConditionalContainerStyleDescription"] = None, description_AbstractNodeMapping535: "viewpoint_description_OrderedTreeLayout" = None, description_AbstractNodeMapping635: "viewpoint_tool_NodeCreationDescription" = None, description_AbstractNodeMapping: "viewpoint_description_EdgeMapping" = None, description_AbstractNodeMapping667: "viewpoint_tool_ContainerCreationDescription" = None):
        self.childrenPresentation = childrenPresentation
        self.viewpoint_description_ContainerMapping = viewpoint_description_ContainerMapping if viewpoint_description_ContainerMapping is not None else set()
        self.viewpoint_description_ContainerMapping488 = viewpoint_description_ContainerMapping488 if viewpoint_description_ContainerMapping488 is not None else set()
        self.viewpoint_description_ContainerMapping491 = viewpoint_description_ContainerMapping491 if viewpoint_description_ContainerMapping491 is not None else set()
        self.viewpoint_description_ContainerMapping494 = viewpoint_description_ContainerMapping494 if viewpoint_description_ContainerMapping494 is not None else set()
        self.viewpoint_description_ContainerMapping497 = viewpoint_description_ContainerMapping497 if viewpoint_description_ContainerMapping497 is not None else set()
        self.viewpoint_description_ContainerMapping500 = viewpoint_description_ContainerMapping500 if viewpoint_description_ContainerMapping500 is not None else set()
        self.viewpoint_description_ContainerMapping503 = viewpoint_description_ContainerMapping503
        self.viewpoint_description_ContainerMapping505 = viewpoint_description_ContainerMapping505 if viewpoint_description_ContainerMapping505 is not None else set()
        
        pass
    @property
    def childrenPresentation(self):
        return self.__childrenPresentation

    @childrenPresentation.setter
    def childrenPresentation(self, childrenPresentation: str):
        self.__childrenPresentation = childrenPresentation


    @property
    def viewpoint_description_ContainerMapping497(self):
        return self.__viewpoint_description_ContainerMapping497

    @viewpoint_description_ContainerMapping497.setter
    def viewpoint_description_ContainerMapping497(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_ContainerMapping__viewpoint_description_ContainerMapping497", None)
        self.__viewpoint_description_ContainerMapping497 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ContainerMapping498"):
                    opp_val = getattr(item, "description_ContainerMapping498", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ContainerMapping498", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ContainerMapping498"):
                    opp_val = getattr(item, "description_ContainerMapping498", None)
                    
                    setattr(item, "description_ContainerMapping498", self)
                    

    @property
    def viewpoint_description_ContainerMapping505(self):
        return self.__viewpoint_description_ContainerMapping505

    @viewpoint_description_ContainerMapping505.setter
    def viewpoint_description_ContainerMapping505(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_ContainerMapping__viewpoint_description_ContainerMapping505", None)
        self.__viewpoint_description_ContainerMapping505 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ConditionalContainerStyleDescription"):
                    opp_val = getattr(item, "description_ConditionalContainerStyleDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ConditionalContainerStyleDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ConditionalContainerStyleDescription"):
                    opp_val = getattr(item, "description_ConditionalContainerStyleDescription", None)
                    
                    setattr(item, "description_ConditionalContainerStyleDescription", self)
                    

    @property
    def viewpoint_description_ContainerMapping503(self):
        return self.__viewpoint_description_ContainerMapping503

    @viewpoint_description_ContainerMapping503.setter
    def viewpoint_description_ContainerMapping503(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_ContainerMapping__viewpoint_description_ContainerMapping503", None)
        self.__viewpoint_description_ContainerMapping503 = value
        
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
    def viewpoint_description_ContainerMapping(self):
        return self.__viewpoint_description_ContainerMapping

    @viewpoint_description_ContainerMapping.setter
    def viewpoint_description_ContainerMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_ContainerMapping__viewpoint_description_ContainerMapping", None)
        self.__viewpoint_description_ContainerMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_NodeMapping486"):
                    opp_val = getattr(item, "description_NodeMapping486", None)
                    
                    if opp_val == self:
                        setattr(item, "description_NodeMapping486", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_NodeMapping486"):
                    opp_val = getattr(item, "description_NodeMapping486", None)
                    
                    setattr(item, "description_NodeMapping486", self)
                    

    @property
    def viewpoint_description_ContainerMapping488(self):
        return self.__viewpoint_description_ContainerMapping488

    @viewpoint_description_ContainerMapping488.setter
    def viewpoint_description_ContainerMapping488(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_ContainerMapping__viewpoint_description_ContainerMapping488", None)
        self.__viewpoint_description_ContainerMapping488 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_NodeMapping489"):
                    opp_val = getattr(item, "description_NodeMapping489", None)
                    
                    if opp_val == self:
                        setattr(item, "description_NodeMapping489", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_NodeMapping489"):
                    opp_val = getattr(item, "description_NodeMapping489", None)
                    
                    setattr(item, "description_NodeMapping489", self)
                    

    @property
    def viewpoint_description_ContainerMapping491(self):
        return self.__viewpoint_description_ContainerMapping491

    @viewpoint_description_ContainerMapping491.setter
    def viewpoint_description_ContainerMapping491(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_ContainerMapping__viewpoint_description_ContainerMapping491", None)
        self.__viewpoint_description_ContainerMapping491 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_NodeMapping492"):
                    opp_val = getattr(item, "description_NodeMapping492", None)
                    
                    if opp_val == self:
                        setattr(item, "description_NodeMapping492", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_NodeMapping492"):
                    opp_val = getattr(item, "description_NodeMapping492", None)
                    
                    setattr(item, "description_NodeMapping492", self)
                    

    @property
    def viewpoint_description_ContainerMapping494(self):
        return self.__viewpoint_description_ContainerMapping494

    @viewpoint_description_ContainerMapping494.setter
    def viewpoint_description_ContainerMapping494(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_ContainerMapping__viewpoint_description_ContainerMapping494", None)
        self.__viewpoint_description_ContainerMapping494 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ContainerMapping495"):
                    opp_val = getattr(item, "description_ContainerMapping495", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ContainerMapping495", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ContainerMapping495"):
                    opp_val = getattr(item, "description_ContainerMapping495", None)
                    
                    setattr(item, "description_ContainerMapping495", self)
                    

    @property
    def viewpoint_description_ContainerMapping500(self):
        return self.__viewpoint_description_ContainerMapping500

    @viewpoint_description_ContainerMapping500.setter
    def viewpoint_description_ContainerMapping500(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_ContainerMapping__viewpoint_description_ContainerMapping500", None)
        self.__viewpoint_description_ContainerMapping500 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ContainerMapping501"):
                    opp_val = getattr(item, "description_ContainerMapping501", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ContainerMapping501", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ContainerMapping501"):
                    opp_val = getattr(item, "description_ContainerMapping501", None)
                    
                    setattr(item, "description_ContainerMapping501", self)
                    

    def createContainer(self, viewpoint_modelElement, viewpoint_container, viewpoint_viewPoint) :
        # TODO: Implement createContainer method
        pass

    def getNodesCandidates(self, viewpoint_container, viewpoint_semanticOrigin, viewpoint_containerView) :
        # TODO: Implement getNodesCandidates method
        pass

    def updateContainer(self, viewpoint_node):
        # TODO: Implement updateContainer method
        pass

    def getBestStyle(self, viewpoint_modelElement, viewpoint_viewVariable, viewpoint_containerVariable) :
        # TODO: Implement getBestStyle method
        pass

class viewpoint_description_NodeMapping(description_DragAndDropTargetDescription, description_AbstractNodeMapping):

    def __init__(self, viewpoint_description_NodeMapping: "style_NodeStyleDescription" = None, viewpoint_description_NodeMapping484: set["description_ConditionalNodeStyleDescription"] = None, description_AbstractNodeMapping535: "viewpoint_description_OrderedTreeLayout" = None, description_AbstractNodeMapping635: "viewpoint_tool_NodeCreationDescription" = None, description_AbstractNodeMapping: "viewpoint_description_EdgeMapping" = None, description_AbstractNodeMapping667: "viewpoint_tool_ContainerCreationDescription" = None):
        self.viewpoint_description_NodeMapping = viewpoint_description_NodeMapping
        self.viewpoint_description_NodeMapping484 = viewpoint_description_NodeMapping484 if viewpoint_description_NodeMapping484 is not None else set()
        
        pass
    @property
    def viewpoint_description_NodeMapping(self):
        return self.__viewpoint_description_NodeMapping

    @viewpoint_description_NodeMapping.setter
    def viewpoint_description_NodeMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_NodeMapping__viewpoint_description_NodeMapping", None)
        self.__viewpoint_description_NodeMapping = value
        
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
    def viewpoint_description_NodeMapping484(self):
        return self.__viewpoint_description_NodeMapping484

    @viewpoint_description_NodeMapping484.setter
    def viewpoint_description_NodeMapping484(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_NodeMapping__viewpoint_description_NodeMapping484", None)
        self.__viewpoint_description_NodeMapping484 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ConditionalNodeStyleDescription"):
                    opp_val = getattr(item, "description_ConditionalNodeStyleDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ConditionalNodeStyleDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ConditionalNodeStyleDescription"):
                    opp_val = getattr(item, "description_ConditionalNodeStyleDescription", None)
                    
                    setattr(item, "description_ConditionalNodeStyleDescription", self)
                    

    def updateNode(self, viewpoint_node):
        # TODO: Implement updateNode method
        pass

    def updateListElement(self, viewpoint_listElement):
        # TODO: Implement updateListElement method
        pass

    def createNode(self, viewpoint_modelElement, viewpoint_viewPoint, viewpoint_container) :
        # TODO: Implement createNode method
        pass

    def getNodesCandidates(self, viewpoint_semanticOrigin, viewpoint_containerView, viewpoint_container) :
        # TODO: Implement getNodesCandidates method
        pass

    def createListElement(self, viewpoint_diagram, viewpoint_modelElement) :
        # TODO: Implement createListElement method
        pass

    def getBestStyle(self, viewpoint_viewVariable, viewpoint_containerVariable, viewpoint_modelElement) :
        # TODO: Implement getBestStyle method
        pass

class viewpoint_description_DiagramDescription(description_PasteTargetDescription, description_DragAndDropTargetDescription, description_RepresentationDescription):

    def __init__(self, domainClass: str, preconditionExpression: str, rootExpression: str, enablePopupBars: bool, viewpoint_description_DiagramDescription416: "validation_ValidationSet" = None, viewpoint_description_DiagramDescription419: "concern_ConcernSet" = None, viewpoint_description_DiagramDescription421: set["tool_AbstractToolDescription"] = None, viewpoint_description_DiagramDescription423: "concern_ConcernDescription" = None, viewpoint_description_DiagramDescription: set["filter_FilterDescription"] = None, viewpoint_description_DiagramDescription408: set["description_EdgeMapping"] = None, viewpoint_description_DiagramDescription410: set["description_NodeMapping"] = None, viewpoint_description_DiagramDescription413: set["description_ContainerMapping"] = None, viewpoint_description_DiagramDescription439: set["description_Layer"] = None, viewpoint_description_DiagramDescription442: set["tool_AbstractToolDescription"] = None, viewpoint_description_DiagramDescription445: set["description_NodeMapping"] = None, viewpoint_description_DiagramDescription448: set["description_EdgeMapping"] = None, viewpoint_description_DiagramDescription451: set["description_EdgeMappingImport"] = None, viewpoint_description_DiagramDescription453: set["description_ContainerMapping"] = None, viewpoint_description_DiagramDescription426: "tool_RepresentationCreationDescription" = None, viewpoint_description_DiagramDescription429: "description_Layout" = None, viewpoint_description_DiagramDescription431: "tool_InitialOperation" = None, viewpoint_description_DiagramDescription434: "description_Layer" = None, viewpoint_description_DiagramDescription437: set["description_AdditionalLayer"] = None, viewpoint_description_DiagramDescription456: set["description_DiagramElementMapping"] = None, viewpoint_description_DiagramDescription459: "tool_ToolSection" = None, viewpoint_description_DiagramDescription461: set["tool_AbstractToolDescription"] = None):
        self.domainClass = domainClass
        self.preconditionExpression = preconditionExpression
        self.rootExpression = rootExpression
        self.enablePopupBars = enablePopupBars
        self.viewpoint_description_DiagramDescription416 = viewpoint_description_DiagramDescription416
        self.viewpoint_description_DiagramDescription419 = viewpoint_description_DiagramDescription419
        self.viewpoint_description_DiagramDescription421 = viewpoint_description_DiagramDescription421 if viewpoint_description_DiagramDescription421 is not None else set()
        self.viewpoint_description_DiagramDescription423 = viewpoint_description_DiagramDescription423
        self.viewpoint_description_DiagramDescription = viewpoint_description_DiagramDescription if viewpoint_description_DiagramDescription is not None else set()
        self.viewpoint_description_DiagramDescription408 = viewpoint_description_DiagramDescription408 if viewpoint_description_DiagramDescription408 is not None else set()
        self.viewpoint_description_DiagramDescription410 = viewpoint_description_DiagramDescription410 if viewpoint_description_DiagramDescription410 is not None else set()
        self.viewpoint_description_DiagramDescription413 = viewpoint_description_DiagramDescription413 if viewpoint_description_DiagramDescription413 is not None else set()
        self.viewpoint_description_DiagramDescription439 = viewpoint_description_DiagramDescription439 if viewpoint_description_DiagramDescription439 is not None else set()
        self.viewpoint_description_DiagramDescription442 = viewpoint_description_DiagramDescription442 if viewpoint_description_DiagramDescription442 is not None else set()
        self.viewpoint_description_DiagramDescription445 = viewpoint_description_DiagramDescription445 if viewpoint_description_DiagramDescription445 is not None else set()
        self.viewpoint_description_DiagramDescription448 = viewpoint_description_DiagramDescription448 if viewpoint_description_DiagramDescription448 is not None else set()
        self.viewpoint_description_DiagramDescription451 = viewpoint_description_DiagramDescription451 if viewpoint_description_DiagramDescription451 is not None else set()
        self.viewpoint_description_DiagramDescription453 = viewpoint_description_DiagramDescription453 if viewpoint_description_DiagramDescription453 is not None else set()
        self.viewpoint_description_DiagramDescription426 = viewpoint_description_DiagramDescription426
        self.viewpoint_description_DiagramDescription429 = viewpoint_description_DiagramDescription429
        self.viewpoint_description_DiagramDescription431 = viewpoint_description_DiagramDescription431
        self.viewpoint_description_DiagramDescription434 = viewpoint_description_DiagramDescription434
        self.viewpoint_description_DiagramDescription437 = viewpoint_description_DiagramDescription437 if viewpoint_description_DiagramDescription437 is not None else set()
        self.viewpoint_description_DiagramDescription456 = viewpoint_description_DiagramDescription456 if viewpoint_description_DiagramDescription456 is not None else set()
        self.viewpoint_description_DiagramDescription459 = viewpoint_description_DiagramDescription459
        self.viewpoint_description_DiagramDescription461 = viewpoint_description_DiagramDescription461 if viewpoint_description_DiagramDescription461 is not None else set()
        
        pass
    @property
    def rootExpression(self):
        return self.__rootExpression

    @rootExpression.setter
    def rootExpression(self, rootExpression: str):
        self.__rootExpression = rootExpression


    @property
    def enablePopupBars(self):
        return self.__enablePopupBars

    @enablePopupBars.setter
    def enablePopupBars(self, enablePopupBars: bool):
        self.__enablePopupBars = enablePopupBars


    @property
    def domainClass(self):
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass


    @property
    def preconditionExpression(self):
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression


    @property
    def viewpoint_description_DiagramDescription431(self):
        return self.__viewpoint_description_DiagramDescription431

    @viewpoint_description_DiagramDescription431.setter
    def viewpoint_description_DiagramDescription431(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription431", None)
        self.__viewpoint_description_DiagramDescription431 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation432"):
                opp_val = getattr(old_value, "tool_InitialOperation432", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation432", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation432"):
                opp_val = getattr(value, "tool_InitialOperation432", None)
                setattr(value, "tool_InitialOperation432", self)

    @property
    def viewpoint_description_DiagramDescription410(self):
        return self.__viewpoint_description_DiagramDescription410

    @viewpoint_description_DiagramDescription410.setter
    def viewpoint_description_DiagramDescription410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription410", None)
        self.__viewpoint_description_DiagramDescription410 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_NodeMapping411"):
                    opp_val = getattr(item, "description_NodeMapping411", None)
                    
                    if opp_val == self:
                        setattr(item, "description_NodeMapping411", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_NodeMapping411"):
                    opp_val = getattr(item, "description_NodeMapping411", None)
                    
                    setattr(item, "description_NodeMapping411", self)
                    

    @property
    def viewpoint_description_DiagramDescription453(self):
        return self.__viewpoint_description_DiagramDescription453

    @viewpoint_description_DiagramDescription453.setter
    def viewpoint_description_DiagramDescription453(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription453", None)
        self.__viewpoint_description_DiagramDescription453 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ContainerMapping454"):
                    opp_val = getattr(item, "description_ContainerMapping454", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ContainerMapping454", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ContainerMapping454"):
                    opp_val = getattr(item, "description_ContainerMapping454", None)
                    
                    setattr(item, "description_ContainerMapping454", self)
                    

    @property
    def viewpoint_description_DiagramDescription451(self):
        return self.__viewpoint_description_DiagramDescription451

    @viewpoint_description_DiagramDescription451.setter
    def viewpoint_description_DiagramDescription451(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription451", None)
        self.__viewpoint_description_DiagramDescription451 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_EdgeMappingImport"):
                    opp_val = getattr(item, "description_EdgeMappingImport", None)
                    
                    if opp_val == self:
                        setattr(item, "description_EdgeMappingImport", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_EdgeMappingImport"):
                    opp_val = getattr(item, "description_EdgeMappingImport", None)
                    
                    setattr(item, "description_EdgeMappingImport", self)
                    

    @property
    def viewpoint_description_DiagramDescription448(self):
        return self.__viewpoint_description_DiagramDescription448

    @viewpoint_description_DiagramDescription448.setter
    def viewpoint_description_DiagramDescription448(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription448", None)
        self.__viewpoint_description_DiagramDescription448 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_EdgeMapping449"):
                    opp_val = getattr(item, "description_EdgeMapping449", None)
                    
                    if opp_val == self:
                        setattr(item, "description_EdgeMapping449", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_EdgeMapping449"):
                    opp_val = getattr(item, "description_EdgeMapping449", None)
                    
                    setattr(item, "description_EdgeMapping449", self)
                    

    @property
    def viewpoint_description_DiagramDescription461(self):
        return self.__viewpoint_description_DiagramDescription461

    @viewpoint_description_DiagramDescription461.setter
    def viewpoint_description_DiagramDescription461(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription461", None)
        self.__viewpoint_description_DiagramDescription461 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription462"):
                    opp_val = getattr(item, "tool_AbstractToolDescription462", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription462", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription462"):
                    opp_val = getattr(item, "tool_AbstractToolDescription462", None)
                    
                    setattr(item, "tool_AbstractToolDescription462", self)
                    

    @property
    def viewpoint_description_DiagramDescription426(self):
        return self.__viewpoint_description_DiagramDescription426

    @viewpoint_description_DiagramDescription426.setter
    def viewpoint_description_DiagramDescription426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription426", None)
        self.__viewpoint_description_DiagramDescription426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_RepresentationCreationDescription427"):
                opp_val = getattr(old_value, "tool_RepresentationCreationDescription427", None)
                if opp_val == self:
                    setattr(old_value, "tool_RepresentationCreationDescription427", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_RepresentationCreationDescription427"):
                opp_val = getattr(value, "tool_RepresentationCreationDescription427", None)
                setattr(value, "tool_RepresentationCreationDescription427", self)

    @property
    def viewpoint_description_DiagramDescription429(self):
        return self.__viewpoint_description_DiagramDescription429

    @viewpoint_description_DiagramDescription429.setter
    def viewpoint_description_DiagramDescription429(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription429", None)
        self.__viewpoint_description_DiagramDescription429 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_Layout"):
                opp_val = getattr(old_value, "description_Layout", None)
                if opp_val == self:
                    setattr(old_value, "description_Layout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_Layout"):
                opp_val = getattr(value, "description_Layout", None)
                setattr(value, "description_Layout", self)

    @property
    def viewpoint_description_DiagramDescription439(self):
        return self.__viewpoint_description_DiagramDescription439

    @viewpoint_description_DiagramDescription439.setter
    def viewpoint_description_DiagramDescription439(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription439", None)
        self.__viewpoint_description_DiagramDescription439 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_Layer440"):
                    opp_val = getattr(item, "description_Layer440", None)
                    
                    if opp_val == self:
                        setattr(item, "description_Layer440", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_Layer440"):
                    opp_val = getattr(item, "description_Layer440", None)
                    
                    setattr(item, "description_Layer440", self)
                    

    @property
    def viewpoint_description_DiagramDescription413(self):
        return self.__viewpoint_description_DiagramDescription413

    @viewpoint_description_DiagramDescription413.setter
    def viewpoint_description_DiagramDescription413(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription413", None)
        self.__viewpoint_description_DiagramDescription413 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ContainerMapping414"):
                    opp_val = getattr(item, "description_ContainerMapping414", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ContainerMapping414", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ContainerMapping414"):
                    opp_val = getattr(item, "description_ContainerMapping414", None)
                    
                    setattr(item, "description_ContainerMapping414", self)
                    

    @property
    def viewpoint_description_DiagramDescription437(self):
        return self.__viewpoint_description_DiagramDescription437

    @viewpoint_description_DiagramDescription437.setter
    def viewpoint_description_DiagramDescription437(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription437", None)
        self.__viewpoint_description_DiagramDescription437 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_AdditionalLayer"):
                    opp_val = getattr(item, "description_AdditionalLayer", None)
                    
                    if opp_val == self:
                        setattr(item, "description_AdditionalLayer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_AdditionalLayer"):
                    opp_val = getattr(item, "description_AdditionalLayer", None)
                    
                    setattr(item, "description_AdditionalLayer", self)
                    

    @property
    def viewpoint_description_DiagramDescription416(self):
        return self.__viewpoint_description_DiagramDescription416

    @viewpoint_description_DiagramDescription416.setter
    def viewpoint_description_DiagramDescription416(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription416", None)
        self.__viewpoint_description_DiagramDescription416 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "validation_ValidationSet417"):
                opp_val = getattr(old_value, "validation_ValidationSet417", None)
                if opp_val == self:
                    setattr(old_value, "validation_ValidationSet417", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "validation_ValidationSet417"):
                opp_val = getattr(value, "validation_ValidationSet417", None)
                setattr(value, "validation_ValidationSet417", self)

    @property
    def viewpoint_description_DiagramDescription408(self):
        return self.__viewpoint_description_DiagramDescription408

    @viewpoint_description_DiagramDescription408.setter
    def viewpoint_description_DiagramDescription408(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription408", None)
        self.__viewpoint_description_DiagramDescription408 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_EdgeMapping"):
                    opp_val = getattr(item, "description_EdgeMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "description_EdgeMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_EdgeMapping"):
                    opp_val = getattr(item, "description_EdgeMapping", None)
                    
                    setattr(item, "description_EdgeMapping", self)
                    

    @property
    def viewpoint_description_DiagramDescription459(self):
        return self.__viewpoint_description_DiagramDescription459

    @viewpoint_description_DiagramDescription459.setter
    def viewpoint_description_DiagramDescription459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription459", None)
        self.__viewpoint_description_DiagramDescription459 = value
        
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
    def viewpoint_description_DiagramDescription(self):
        return self.__viewpoint_description_DiagramDescription

    @viewpoint_description_DiagramDescription.setter
    def viewpoint_description_DiagramDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription", None)
        self.__viewpoint_description_DiagramDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "filter_FilterDescription406"):
                    opp_val = getattr(item, "filter_FilterDescription406", None)
                    
                    if opp_val == self:
                        setattr(item, "filter_FilterDescription406", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filter_FilterDescription406"):
                    opp_val = getattr(item, "filter_FilterDescription406", None)
                    
                    setattr(item, "filter_FilterDescription406", self)
                    

    @property
    def viewpoint_description_DiagramDescription419(self):
        return self.__viewpoint_description_DiagramDescription419

    @viewpoint_description_DiagramDescription419.setter
    def viewpoint_description_DiagramDescription419(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription419", None)
        self.__viewpoint_description_DiagramDescription419 = value
        
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
    def viewpoint_description_DiagramDescription456(self):
        return self.__viewpoint_description_DiagramDescription456

    @viewpoint_description_DiagramDescription456.setter
    def viewpoint_description_DiagramDescription456(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription456", None)
        self.__viewpoint_description_DiagramDescription456 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_DiagramElementMapping457"):
                    opp_val = getattr(item, "description_DiagramElementMapping457", None)
                    
                    if opp_val == self:
                        setattr(item, "description_DiagramElementMapping457", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_DiagramElementMapping457"):
                    opp_val = getattr(item, "description_DiagramElementMapping457", None)
                    
                    setattr(item, "description_DiagramElementMapping457", self)
                    

    @property
    def viewpoint_description_DiagramDescription442(self):
        return self.__viewpoint_description_DiagramDescription442

    @viewpoint_description_DiagramDescription442.setter
    def viewpoint_description_DiagramDescription442(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription442", None)
        self.__viewpoint_description_DiagramDescription442 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription443"):
                    opp_val = getattr(item, "tool_AbstractToolDescription443", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription443", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription443"):
                    opp_val = getattr(item, "tool_AbstractToolDescription443", None)
                    
                    setattr(item, "tool_AbstractToolDescription443", self)
                    

    @property
    def viewpoint_description_DiagramDescription434(self):
        return self.__viewpoint_description_DiagramDescription434

    @viewpoint_description_DiagramDescription434.setter
    def viewpoint_description_DiagramDescription434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription434", None)
        self.__viewpoint_description_DiagramDescription434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_Layer435"):
                opp_val = getattr(old_value, "description_Layer435", None)
                if opp_val == self:
                    setattr(old_value, "description_Layer435", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_Layer435"):
                opp_val = getattr(value, "description_Layer435", None)
                setattr(value, "description_Layer435", self)

    @property
    def viewpoint_description_DiagramDescription421(self):
        return self.__viewpoint_description_DiagramDescription421

    @viewpoint_description_DiagramDescription421.setter
    def viewpoint_description_DiagramDescription421(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription421", None)
        self.__viewpoint_description_DiagramDescription421 = value if value is not None else set()
        
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
    def viewpoint_description_DiagramDescription423(self):
        return self.__viewpoint_description_DiagramDescription423

    @viewpoint_description_DiagramDescription423.setter
    def viewpoint_description_DiagramDescription423(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription423", None)
        self.__viewpoint_description_DiagramDescription423 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "concern_ConcernDescription424"):
                opp_val = getattr(old_value, "concern_ConcernDescription424", None)
                if opp_val == self:
                    setattr(old_value, "concern_ConcernDescription424", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "concern_ConcernDescription424"):
                opp_val = getattr(value, "concern_ConcernDescription424", None)
                setattr(value, "concern_ConcernDescription424", self)

    @property
    def viewpoint_description_DiagramDescription445(self):
        return self.__viewpoint_description_DiagramDescription445

    @viewpoint_description_DiagramDescription445.setter
    def viewpoint_description_DiagramDescription445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DiagramDescription__viewpoint_description_DiagramDescription445", None)
        self.__viewpoint_description_DiagramDescription445 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_NodeMapping446"):
                    opp_val = getattr(item, "description_NodeMapping446", None)
                    
                    if opp_val == self:
                        setattr(item, "description_NodeMapping446", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_NodeMapping446"):
                    opp_val = getattr(item, "description_NodeMapping446", None)
                    
                    setattr(item, "description_NodeMapping446", self)
                    

    def createDiagram(self) :
        # TODO: Implement createDiagram method
        pass

class viewpoint_diagram_ContainerVariable2StyleDescription:

    pass
class ContainerVariable2StyleDescription:

    pass
class viewpoint_diagram_ViewVariable2ContainerVariable:

    pass
class ViewVariable2ContainerVariable:

    pass
class viewpoint_diagram_ModelElement2ViewVariable:

    pass
class diagram_viewpoint_EObject:

    pass
class filter_FilterVariable:

    pass
class viewpoint_diagram_FilterVariableValue:

    pass
class FilterVariableValue:

    pass
class CollapseFilter:

    pass
class viewpoint_diagram_IndirectlyCollapseFilter(CollapseFilter):

    pass
class viewpoint_diagram_FilterVariableHistory:

    pass
class GaugeSection:

    pass
class EndLabelStyle:

    pass
class CenterLabelStyle:

    pass
class BeginLabelStyle:

    pass
class diagram_ContainerStyle:

    pass
class diagram_NodeStyle:

    pass
class viewpoint_diagram_WorkspaceImage(diagram_ContainerStyle, diagram_NodeStyle):

    def __init__(self, workspacePath: str):
        self.workspacePath = workspacePath
        
        pass
    @property
    def workspacePath(self):
        return self.__workspacePath

    @workspacePath.setter
    def workspacePath(self, workspacePath: str):
        self.__workspacePath = workspacePath


class viewpoint_diagram_EdgeTarget(ABC):

    pass
class diagram_BorderedStyle:

    pass
class Style:

    pass
class viewpoint_diagram_BorderedStyle(Style):

    def __init__(self, borderSize: str, borderSizeComputationExpression: str, viewpoint_diagram_BorderedStyle: "diagram_viewpoint_RGBValues" = None):
        self.borderSize = borderSize
        self.borderSizeComputationExpression = borderSizeComputationExpression
        self.viewpoint_diagram_BorderedStyle = viewpoint_diagram_BorderedStyle
        
        pass
    @property
    def borderSize(self):
        return self.__borderSize

    @borderSize.setter
    def borderSize(self, borderSize: str):
        self.__borderSize = borderSize


    @property
    def borderSizeComputationExpression(self):
        return self.__borderSizeComputationExpression

    @borderSizeComputationExpression.setter
    def borderSizeComputationExpression(self, borderSizeComputationExpression: str):
        self.__borderSizeComputationExpression = borderSizeComputationExpression


    @property
    def viewpoint_diagram_BorderedStyle(self):
        return self.__viewpoint_diagram_BorderedStyle

    @viewpoint_diagram_BorderedStyle.setter
    def viewpoint_diagram_BorderedStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_BorderedStyle__viewpoint_diagram_BorderedStyle", None)
        self.__viewpoint_diagram_BorderedStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues377"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues377", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues377", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues377"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues377", None)
                setattr(value, "diagram_viewpoint_RGBValues377", self)

class viewpoint_diagram_EdgeStyle(Style):

    def __init__(self, lineStyle: str, sourceArrow: str, targetArrow: str, foldingStyle: str, size: str, routingStyle: str, viewpoint_diagram_EdgeStyle: "diagram_viewpoint_RGBValues" = None, viewpoint_diagram_EdgeStyle370: "BeginLabelStyle" = None, viewpoint_diagram_EdgeStyle372: "CenterLabelStyle" = None, viewpoint_diagram_EdgeStyle374: "EndLabelStyle" = None):
        self.lineStyle = lineStyle
        self.sourceArrow = sourceArrow
        self.targetArrow = targetArrow
        self.foldingStyle = foldingStyle
        self.size = size
        self.routingStyle = routingStyle
        self.viewpoint_diagram_EdgeStyle = viewpoint_diagram_EdgeStyle
        self.viewpoint_diagram_EdgeStyle370 = viewpoint_diagram_EdgeStyle370
        self.viewpoint_diagram_EdgeStyle372 = viewpoint_diagram_EdgeStyle372
        self.viewpoint_diagram_EdgeStyle374 = viewpoint_diagram_EdgeStyle374
        
        pass
    @property
    def sourceArrow(self):
        return self.__sourceArrow

    @sourceArrow.setter
    def sourceArrow(self, sourceArrow: str):
        self.__sourceArrow = sourceArrow


    @property
    def routingStyle(self):
        return self.__routingStyle

    @routingStyle.setter
    def routingStyle(self, routingStyle: str):
        self.__routingStyle = routingStyle


    @property
    def foldingStyle(self):
        return self.__foldingStyle

    @foldingStyle.setter
    def foldingStyle(self, foldingStyle: str):
        self.__foldingStyle = foldingStyle


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def lineStyle(self):
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle


    @property
    def targetArrow(self):
        return self.__targetArrow

    @targetArrow.setter
    def targetArrow(self, targetArrow: str):
        self.__targetArrow = targetArrow


    @property
    def viewpoint_diagram_EdgeStyle370(self):
        return self.__viewpoint_diagram_EdgeStyle370

    @viewpoint_diagram_EdgeStyle370.setter
    def viewpoint_diagram_EdgeStyle370(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_EdgeStyle__viewpoint_diagram_EdgeStyle370", None)
        self.__viewpoint_diagram_EdgeStyle370 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BeginLabelStyle"):
                opp_val = getattr(old_value, "BeginLabelStyle", None)
                if opp_val == self:
                    setattr(old_value, "BeginLabelStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BeginLabelStyle"):
                opp_val = getattr(value, "BeginLabelStyle", None)
                setattr(value, "BeginLabelStyle", self)

    @property
    def viewpoint_diagram_EdgeStyle374(self):
        return self.__viewpoint_diagram_EdgeStyle374

    @viewpoint_diagram_EdgeStyle374.setter
    def viewpoint_diagram_EdgeStyle374(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_EdgeStyle__viewpoint_diagram_EdgeStyle374", None)
        self.__viewpoint_diagram_EdgeStyle374 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EndLabelStyle"):
                opp_val = getattr(old_value, "EndLabelStyle", None)
                if opp_val == self:
                    setattr(old_value, "EndLabelStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EndLabelStyle"):
                opp_val = getattr(value, "EndLabelStyle", None)
                setattr(value, "EndLabelStyle", self)

    @property
    def viewpoint_diagram_EdgeStyle372(self):
        return self.__viewpoint_diagram_EdgeStyle372

    @viewpoint_diagram_EdgeStyle372.setter
    def viewpoint_diagram_EdgeStyle372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_EdgeStyle__viewpoint_diagram_EdgeStyle372", None)
        self.__viewpoint_diagram_EdgeStyle372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CenterLabelStyle"):
                opp_val = getattr(old_value, "CenterLabelStyle", None)
                if opp_val == self:
                    setattr(old_value, "CenterLabelStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CenterLabelStyle"):
                opp_val = getattr(value, "CenterLabelStyle", None)
                setattr(value, "CenterLabelStyle", self)

    @property
    def viewpoint_diagram_EdgeStyle(self):
        return self.__viewpoint_diagram_EdgeStyle

    @viewpoint_diagram_EdgeStyle.setter
    def viewpoint_diagram_EdgeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_EdgeStyle__viewpoint_diagram_EdgeStyle", None)
        self.__viewpoint_diagram_EdgeStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues368"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues368", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues368", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues368"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues368", None)
                setattr(value, "diagram_viewpoint_RGBValues368", self)

class LabelStyle:

    pass
class viewpoint_diagram_ContainerStyle(Style, diagram_BorderedStyle, LabelStyle):

    pass
class viewpoint_diagram_NodeStyle(Style, diagram_BorderedStyle, LabelStyle):

    def __init__(self, labelPosition: str, hideLabelByDefault: bool):
        self.labelPosition = labelPosition
        self.hideLabelByDefault = hideLabelByDefault
        
        pass
    @property
    def labelPosition(self):
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition


    @property
    def hideLabelByDefault(self):
        return self.__hideLabelByDefault

    @hideLabelByDefault.setter
    def hideLabelByDefault(self, hideLabelByDefault: bool):
        self.__hideLabelByDefault = hideLabelByDefault


class diagram_viewpoint_DRepresentationContainer:

    pass
class diagram_viewpoint_RGBValues:

    pass
class description_IEdgeMapping:

    pass
class viewpoint_diagram_DDiagramSet:

    pass
class AbstractDNode:

    pass
class viewpoint_diagram_DNodeListElement(AbstractDNode):

    pass
class EdgeStyle:

    pass
class viewpoint_diagram_BracketEdgeStyle(EdgeStyle):

    pass
class diagram_DDiagramElement:

    pass
class description_ContainerMapping:

    pass
class viewpoint_description_ContainerMappingImport(description_ContainerMapping, description_AbstractMappingImport):

    pass
class ContainerStyle:

    pass
class viewpoint_diagram_ShapeContainerStyle(ContainerStyle):

    def __init__(self, shape: str, viewpoint_diagram_ShapeContainerStyle: "diagram_viewpoint_RGBValues" = None, ContainerStyle: "viewpoint_diagram_DDiagramElementContainer" = None):
        self.shape = shape
        self.viewpoint_diagram_ShapeContainerStyle = viewpoint_diagram_ShapeContainerStyle
        
        pass
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def viewpoint_diagram_ShapeContainerStyle(self):
        return self.__viewpoint_diagram_ShapeContainerStyle

    @viewpoint_diagram_ShapeContainerStyle.setter
    def viewpoint_diagram_ShapeContainerStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_ShapeContainerStyle__viewpoint_diagram_ShapeContainerStyle", None)
        self.__viewpoint_diagram_ShapeContainerStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues354"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues354", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues354"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues354", None)
                setattr(value, "diagram_viewpoint_RGBValues354", self)

class viewpoint_diagram_FlatContainerStyle(ContainerStyle):

    def __init__(self, backgroundStyle: str, viewpoint_diagram_FlatContainerStyle351: "diagram_viewpoint_RGBValues" = None, viewpoint_diagram_FlatContainerStyle: "diagram_viewpoint_RGBValues" = None, ContainerStyle: "viewpoint_diagram_DDiagramElementContainer" = None):
        self.backgroundStyle = backgroundStyle
        self.viewpoint_diagram_FlatContainerStyle351 = viewpoint_diagram_FlatContainerStyle351
        self.viewpoint_diagram_FlatContainerStyle = viewpoint_diagram_FlatContainerStyle
        
        pass
    @property
    def backgroundStyle(self):
        return self.__backgroundStyle

    @backgroundStyle.setter
    def backgroundStyle(self, backgroundStyle: str):
        self.__backgroundStyle = backgroundStyle


    @property
    def viewpoint_diagram_FlatContainerStyle(self):
        return self.__viewpoint_diagram_FlatContainerStyle

    @viewpoint_diagram_FlatContainerStyle.setter
    def viewpoint_diagram_FlatContainerStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_FlatContainerStyle__viewpoint_diagram_FlatContainerStyle", None)
        self.__viewpoint_diagram_FlatContainerStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues349"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues349", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues349", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues349"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues349", None)
                setattr(value, "diagram_viewpoint_RGBValues349", self)

    @property
    def viewpoint_diagram_FlatContainerStyle351(self):
        return self.__viewpoint_diagram_FlatContainerStyle351

    @viewpoint_diagram_FlatContainerStyle351.setter
    def viewpoint_diagram_FlatContainerStyle351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_FlatContainerStyle__viewpoint_diagram_FlatContainerStyle351", None)
        self.__viewpoint_diagram_FlatContainerStyle351 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues352"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues352", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues352", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues352"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues352", None)
                setattr(value, "diagram_viewpoint_RGBValues352", self)

class diagram_EdgeTarget:

    pass
class viewpoint_diagram_DEdge(diagram_EdgeTarget, diagram_DDiagramElement):

    def __init__(self, size: str, arrangeConstraints: str, beginLabel: str, endLabel: str, routingStyle: str, isFold: bool, isMockEdge: bool, viewpoint_diagram_DEdge: "EdgeStyle" = None, outgoingEdges: "EdgeTarget" = None, incomingEdges: "EdgeTarget" = None, viewpoint_diagram_DEdge330: "diagram_viewpoint_Style" = None, viewpoint_diagram_DEdge333: set["EdgeTarget"] = None, viewpoint_diagram_DEdge328: "description_IEdgeMapping" = None):
        self.size = size
        self.arrangeConstraints = arrangeConstraints
        self.beginLabel = beginLabel
        self.endLabel = endLabel
        self.routingStyle = routingStyle
        self.isFold = isFold
        self.isMockEdge = isMockEdge
        self.viewpoint_diagram_DEdge = viewpoint_diagram_DEdge
        self.outgoingEdges = outgoingEdges
        self.incomingEdges = incomingEdges
        self.viewpoint_diagram_DEdge330 = viewpoint_diagram_DEdge330
        self.viewpoint_diagram_DEdge333 = viewpoint_diagram_DEdge333 if viewpoint_diagram_DEdge333 is not None else set()
        self.viewpoint_diagram_DEdge328 = viewpoint_diagram_DEdge328
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def isFold(self):
        return self.__isFold

    @isFold.setter
    def isFold(self, isFold: bool):
        self.__isFold = isFold


    @property
    def beginLabel(self):
        return self.__beginLabel

    @beginLabel.setter
    def beginLabel(self, beginLabel: str):
        self.__beginLabel = beginLabel


    @property
    def arrangeConstraints(self):
        return self.__arrangeConstraints

    @arrangeConstraints.setter
    def arrangeConstraints(self, arrangeConstraints: str):
        self.__arrangeConstraints = arrangeConstraints


    @property
    def routingStyle(self):
        return self.__routingStyle

    @routingStyle.setter
    def routingStyle(self, routingStyle: str):
        self.__routingStyle = routingStyle


    @property
    def isMockEdge(self):
        return self.__isMockEdge

    @isMockEdge.setter
    def isMockEdge(self, isMockEdge: bool):
        self.__isMockEdge = isMockEdge


    @property
    def endLabel(self):
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
        old_value = getattr(self, f"_viewpoint_diagram_DEdge__outgoingEdges", None)
        self.__outgoingEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeTarget324"):
                opp_val = getattr(old_value, "EdgeTarget324", None)
                if opp_val == self:
                    setattr(old_value, "EdgeTarget324", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeTarget324"):
                opp_val = getattr(value, "EdgeTarget324", None)
                setattr(value, "EdgeTarget324", self)

    @property
    def viewpoint_diagram_DEdge(self):
        return self.__viewpoint_diagram_DEdge

    @viewpoint_diagram_DEdge.setter
    def viewpoint_diagram_DEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DEdge__viewpoint_diagram_DEdge", None)
        self.__viewpoint_diagram_DEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeStyle"):
                opp_val = getattr(old_value, "EdgeStyle", None)
                if opp_val == self:
                    setattr(old_value, "EdgeStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeStyle"):
                opp_val = getattr(value, "EdgeStyle", None)
                setattr(value, "EdgeStyle", self)

    @property
    def viewpoint_diagram_DEdge330(self):
        return self.__viewpoint_diagram_DEdge330

    @viewpoint_diagram_DEdge330.setter
    def viewpoint_diagram_DEdge330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DEdge__viewpoint_diagram_DEdge330", None)
        self.__viewpoint_diagram_DEdge330 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_Style331"):
                opp_val = getattr(old_value, "diagram_viewpoint_Style331", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_Style331", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_Style331"):
                opp_val = getattr(value, "diagram_viewpoint_Style331", None)
                setattr(value, "diagram_viewpoint_Style331", self)

    @property
    def incomingEdges(self):
        return self.__incomingEdges

    @incomingEdges.setter
    def incomingEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DEdge__incomingEdges", None)
        self.__incomingEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeTarget326"):
                opp_val = getattr(old_value, "EdgeTarget326", None)
                if opp_val == self:
                    setattr(old_value, "EdgeTarget326", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeTarget326"):
                opp_val = getattr(value, "EdgeTarget326", None)
                setattr(value, "EdgeTarget326", self)

    @property
    def viewpoint_diagram_DEdge333(self):
        return self.__viewpoint_diagram_DEdge333

    @viewpoint_diagram_DEdge333.setter
    def viewpoint_diagram_DEdge333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DEdge__viewpoint_diagram_DEdge333", None)
        self.__viewpoint_diagram_DEdge333 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EdgeTarget334"):
                    opp_val = getattr(item, "EdgeTarget334", None)
                    
                    if opp_val == self:
                        setattr(item, "EdgeTarget334", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EdgeTarget334"):
                    opp_val = getattr(item, "EdgeTarget334", None)
                    
                    setattr(item, "EdgeTarget334", self)
                    

    @property
    def viewpoint_diagram_DEdge328(self):
        return self.__viewpoint_diagram_DEdge328

    @viewpoint_diagram_DEdge328.setter
    def viewpoint_diagram_DEdge328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DEdge__viewpoint_diagram_DEdge328", None)
        self.__viewpoint_diagram_DEdge328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_IEdgeMapping"):
                opp_val = getattr(old_value, "description_IEdgeMapping", None)
                if opp_val == self:
                    setattr(old_value, "description_IEdgeMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_IEdgeMapping"):
                opp_val = getattr(value, "description_IEdgeMapping", None)
                setattr(value, "description_IEdgeMapping", self)

    def isRootFolding(self) :
        # TODO: Implement isRootFolding method
        pass

class diagram_AbstractDNode:

    pass
class EdgeTarget:

    pass
class description_NodeMapping:

    pass
class viewpoint_description_NodeMappingImport(description_NodeMapping, description_AbstractMappingImport):

    pass
class diagram_viewpoint_Style:

    pass
class NodeStyle:

    pass
class viewpoint_diagram_BundledImage(NodeStyle):

    def __init__(self, shape: str, viewpoint_diagram_BundledImage: "diagram_viewpoint_RGBValues" = None, NodeStyle: "viewpoint_diagram_DNode" = None, NodeStyle312: "viewpoint_diagram_DNodeListElement" = None):
        self.shape = shape
        self.viewpoint_diagram_BundledImage = viewpoint_diagram_BundledImage
        
        pass
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def viewpoint_diagram_BundledImage(self):
        return self.__viewpoint_diagram_BundledImage

    @viewpoint_diagram_BundledImage.setter
    def viewpoint_diagram_BundledImage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_BundledImage__viewpoint_diagram_BundledImage", None)
        self.__viewpoint_diagram_BundledImage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues362"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues362", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues362", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues362"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues362", None)
                setattr(value, "diagram_viewpoint_RGBValues362", self)

class viewpoint_diagram_Note(NodeStyle):

    pass
class viewpoint_diagram_CustomStyle(NodeStyle):

    def __init__(self, id: str, NodeStyle: "viewpoint_diagram_DNode" = None, NodeStyle312: "viewpoint_diagram_DNodeListElement" = None):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class viewpoint_diagram_Ellipse(NodeStyle):

    def __init__(self, horizontalDiameter: str, verticalDiameter: str, viewpoint_diagram_Ellipse: "diagram_viewpoint_RGBValues" = None, NodeStyle: "viewpoint_diagram_DNode" = None, NodeStyle312: "viewpoint_diagram_DNodeListElement" = None):
        self.horizontalDiameter = horizontalDiameter
        self.verticalDiameter = verticalDiameter
        self.viewpoint_diagram_Ellipse = viewpoint_diagram_Ellipse
        
        pass
    @property
    def horizontalDiameter(self):
        return self.__horizontalDiameter

    @horizontalDiameter.setter
    def horizontalDiameter(self, horizontalDiameter: str):
        self.__horizontalDiameter = horizontalDiameter


    @property
    def verticalDiameter(self):
        return self.__verticalDiameter

    @verticalDiameter.setter
    def verticalDiameter(self, verticalDiameter: str):
        self.__verticalDiameter = verticalDiameter


    @property
    def viewpoint_diagram_Ellipse(self):
        return self.__viewpoint_diagram_Ellipse

    @viewpoint_diagram_Ellipse.setter
    def viewpoint_diagram_Ellipse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_Ellipse__viewpoint_diagram_Ellipse", None)
        self.__viewpoint_diagram_Ellipse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues358"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues358", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues358", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues358"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues358", None)
                setattr(value, "diagram_viewpoint_RGBValues358", self)

class viewpoint_diagram_GaugeCompositeStyle(NodeStyle):

    def __init__(self, alignment: str, viewpoint_diagram_GaugeCompositeStyle: set["GaugeSection"] = None, NodeStyle: "viewpoint_diagram_DNode" = None, NodeStyle312: "viewpoint_diagram_DNodeListElement" = None):
        self.alignment = alignment
        self.viewpoint_diagram_GaugeCompositeStyle = viewpoint_diagram_GaugeCompositeStyle if viewpoint_diagram_GaugeCompositeStyle is not None else set()
        
        pass
    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment


    @property
    def viewpoint_diagram_GaugeCompositeStyle(self):
        return self.__viewpoint_diagram_GaugeCompositeStyle

    @viewpoint_diagram_GaugeCompositeStyle.setter
    def viewpoint_diagram_GaugeCompositeStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_GaugeCompositeStyle__viewpoint_diagram_GaugeCompositeStyle", None)
        self.__viewpoint_diagram_GaugeCompositeStyle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GaugeSection"):
                    opp_val = getattr(item, "GaugeSection", None)
                    
                    if opp_val == self:
                        setattr(item, "GaugeSection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GaugeSection"):
                    opp_val = getattr(item, "GaugeSection", None)
                    
                    setattr(item, "GaugeSection", self)
                    

class viewpoint_diagram_Square(NodeStyle):

    def __init__(self, width: str, height: str, viewpoint_diagram_Square: "diagram_viewpoint_RGBValues" = None, NodeStyle: "viewpoint_diagram_DNode" = None, NodeStyle312: "viewpoint_diagram_DNodeListElement" = None):
        self.width = width
        self.height = height
        self.viewpoint_diagram_Square = viewpoint_diagram_Square
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def viewpoint_diagram_Square(self):
        return self.__viewpoint_diagram_Square

    @viewpoint_diagram_Square.setter
    def viewpoint_diagram_Square(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_Square__viewpoint_diagram_Square", None)
        self.__viewpoint_diagram_Square = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues356"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues356", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues356", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues356"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues356", None)
                setattr(value, "diagram_viewpoint_RGBValues356", self)

class viewpoint_diagram_Lozenge(NodeStyle):

    def __init__(self, width: str, height: str, viewpoint_diagram_Lozenge: "diagram_viewpoint_RGBValues" = None, NodeStyle: "viewpoint_diagram_DNode" = None, NodeStyle312: "viewpoint_diagram_DNodeListElement" = None):
        self.width = width
        self.height = height
        self.viewpoint_diagram_Lozenge = viewpoint_diagram_Lozenge
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def viewpoint_diagram_Lozenge(self):
        return self.__viewpoint_diagram_Lozenge

    @viewpoint_diagram_Lozenge.setter
    def viewpoint_diagram_Lozenge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_Lozenge__viewpoint_diagram_Lozenge", None)
        self.__viewpoint_diagram_Lozenge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues360"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues360", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues360", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues360"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues360", None)
                setattr(value, "diagram_viewpoint_RGBValues360", self)

class viewpoint_diagram_Dot(NodeStyle):

    def __init__(self, strokeSizeComputationExpression: str, viewpoint_diagram_Dot: "diagram_viewpoint_RGBValues" = None, NodeStyle: "viewpoint_diagram_DNode" = None, NodeStyle312: "viewpoint_diagram_DNodeListElement" = None):
        self.strokeSizeComputationExpression = strokeSizeComputationExpression
        self.viewpoint_diagram_Dot = viewpoint_diagram_Dot
        
        pass
    @property
    def strokeSizeComputationExpression(self):
        return self.__strokeSizeComputationExpression

    @strokeSizeComputationExpression.setter
    def strokeSizeComputationExpression(self, strokeSizeComputationExpression: str):
        self.__strokeSizeComputationExpression = strokeSizeComputationExpression


    @property
    def viewpoint_diagram_Dot(self):
        return self.__viewpoint_diagram_Dot

    @viewpoint_diagram_Dot.setter
    def viewpoint_diagram_Dot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_Dot__viewpoint_diagram_Dot", None)
        self.__viewpoint_diagram_Dot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues", None)
                setattr(value, "diagram_viewpoint_RGBValues", self)

class viewpoint_diagram_GraphicalFilter(ABC):

    pass
class GraphicalFilter:

    pass
class viewpoint_diagram_CollapseFilter(GraphicalFilter):

    def __init__(self, width: int, height: int, GraphicalFilter: "viewpoint_diagram_DDiagramElement" = None):
        self.width = width
        self.height = height
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


class diagram_viewpoint_Decoration:

    pass
class viewpoint_diagram_AbsoluteBoundsFilter(GraphicalFilter):

    def __init__(self, x: str, y: str, height: str, width: str, GraphicalFilter: "viewpoint_diagram_DDiagramElement" = None):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


class filter_CompositeFilterDescription:

    pass
class viewpoint_diagram_AppliedCompositeFilters(GraphicalFilter):

    pass
class viewpoint_diagram_FoldingFilter(GraphicalFilter):

    pass
class viewpoint_diagram_FoldingPointFilter(GraphicalFilter):

    pass
class viewpoint_diagram_HideLabelFilter(GraphicalFilter):

    pass
class viewpoint_diagram_HideFilter(GraphicalFilter):

    pass
class description_Layer:

    pass
class FilterVariableHistory:

    pass
class tool_BehaviorTool:

    pass
class validation_ValidationRule:

    pass
class DNavigable:

    pass
class DRepresentationElement:

    pass
class diagram_DDiagram:

    pass
class DEdge:

    pass
class DDiagram:

    pass
class filter_FilterDescription:

    pass
class concern_ConcernDescription:

    pass
class DDiagramElementContainer:

    pass
class viewpoint_diagram_DNodeContainer(DDiagramElementContainer):

    def __init__(self, childrenPresentation: str, viewpoint_diagram_DNodeContainer: set["DDiagramElement"] = None, DDiagramElementContainer: "viewpoint_diagram_DDiagram" = None, DDiagramElementContainer290: "viewpoint_diagram_DDiagramElementContainer" = None):
        self.childrenPresentation = childrenPresentation
        self.viewpoint_diagram_DNodeContainer = viewpoint_diagram_DNodeContainer if viewpoint_diagram_DNodeContainer is not None else set()
        
        pass
    @property
    def childrenPresentation(self):
        return self.__childrenPresentation

    @childrenPresentation.setter
    def childrenPresentation(self, childrenPresentation: str):
        self.__childrenPresentation = childrenPresentation


    @property
    def viewpoint_diagram_DNodeContainer(self):
        return self.__viewpoint_diagram_DNodeContainer

    @viewpoint_diagram_DNodeContainer.setter
    def viewpoint_diagram_DNodeContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DNodeContainer__viewpoint_diagram_DNodeContainer", None)
        self.__viewpoint_diagram_DNodeContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagramElement308"):
                    opp_val = getattr(item, "DDiagramElement308", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagramElement308", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagramElement308"):
                    opp_val = getattr(item, "DDiagramElement308", None)
                    
                    setattr(item, "DDiagramElement308", self)
                    

class viewpoint_diagram_DNodeList(DDiagramElementContainer):

    def __init__(self, lineWidth: int, viewpoint_diagram_DNodeList: set["DNodeListElement"] = None, DDiagramElementContainer: "viewpoint_diagram_DDiagram" = None, DDiagramElementContainer290: "viewpoint_diagram_DDiagramElementContainer" = None):
        self.lineWidth = lineWidth
        self.viewpoint_diagram_DNodeList = viewpoint_diagram_DNodeList if viewpoint_diagram_DNodeList is not None else set()
        
        pass
    @property
    def lineWidth(self):
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth


    @property
    def viewpoint_diagram_DNodeList(self):
        return self.__viewpoint_diagram_DNodeList

    @viewpoint_diagram_DNodeList.setter
    def viewpoint_diagram_DNodeList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DNodeList__viewpoint_diagram_DNodeList", None)
        self.__viewpoint_diagram_DNodeList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DNodeListElement310"):
                    opp_val = getattr(item, "DNodeListElement310", None)
                    
                    if opp_val == self:
                        setattr(item, "DNodeListElement310", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DNodeListElement310"):
                    opp_val = getattr(item, "DNodeListElement310", None)
                    
                    setattr(item, "DNodeListElement310", self)
                    

class DNodeListElement:

    pass
class DNode:

    pass
class DContainer:

    pass
class DValidable:

    pass
class viewpoint_diagram_DDiagramElement(DNavigable, DRepresentationElement, DValidable):

    def __init__(self, visible: bool, tooltipText: str, viewpoint_diagram_DDiagramElement: set["description_Layer"] = None, viewpoint_diagram_DDiagramElement262: set["diagram_viewpoint_Decoration"] = None, viewpoint_diagram_DDiagramElement264: "description_DiagramElementMapping" = None, viewpoint_diagram_DDiagramElement267: set["GraphicalFilter"] = None):
        self.visible = visible
        self.tooltipText = tooltipText
        self.viewpoint_diagram_DDiagramElement = viewpoint_diagram_DDiagramElement if viewpoint_diagram_DDiagramElement is not None else set()
        self.viewpoint_diagram_DDiagramElement262 = viewpoint_diagram_DDiagramElement262 if viewpoint_diagram_DDiagramElement262 is not None else set()
        self.viewpoint_diagram_DDiagramElement264 = viewpoint_diagram_DDiagramElement264
        self.viewpoint_diagram_DDiagramElement267 = viewpoint_diagram_DDiagramElement267 if viewpoint_diagram_DDiagramElement267 is not None else set()
        
        pass
    @property
    def tooltipText(self):
        return self.__tooltipText

    @tooltipText.setter
    def tooltipText(self, tooltipText: str):
        self.__tooltipText = tooltipText


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible


    @property
    def viewpoint_diagram_DDiagramElement262(self):
        return self.__viewpoint_diagram_DDiagramElement262

    @viewpoint_diagram_DDiagramElement262.setter
    def viewpoint_diagram_DDiagramElement262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElement__viewpoint_diagram_DDiagramElement262", None)
        self.__viewpoint_diagram_DDiagramElement262 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagram_viewpoint_Decoration"):
                    opp_val = getattr(item, "diagram_viewpoint_Decoration", None)
                    
                    if opp_val == self:
                        setattr(item, "diagram_viewpoint_Decoration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagram_viewpoint_Decoration"):
                    opp_val = getattr(item, "diagram_viewpoint_Decoration", None)
                    
                    setattr(item, "diagram_viewpoint_Decoration", self)
                    

    @property
    def viewpoint_diagram_DDiagramElement(self):
        return self.__viewpoint_diagram_DDiagramElement

    @viewpoint_diagram_DDiagramElement.setter
    def viewpoint_diagram_DDiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElement__viewpoint_diagram_DDiagramElement", None)
        self.__viewpoint_diagram_DDiagramElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_Layer260"):
                    opp_val = getattr(item, "description_Layer260", None)
                    
                    if opp_val == self:
                        setattr(item, "description_Layer260", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_Layer260"):
                    opp_val = getattr(item, "description_Layer260", None)
                    
                    setattr(item, "description_Layer260", self)
                    

    @property
    def viewpoint_diagram_DDiagramElement264(self):
        return self.__viewpoint_diagram_DDiagramElement264

    @viewpoint_diagram_DDiagramElement264.setter
    def viewpoint_diagram_DDiagramElement264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElement__viewpoint_diagram_DDiagramElement264", None)
        self.__viewpoint_diagram_DDiagramElement264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_DiagramElementMapping265"):
                opp_val = getattr(old_value, "description_DiagramElementMapping265", None)
                if opp_val == self:
                    setattr(old_value, "description_DiagramElementMapping265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_DiagramElementMapping265"):
                opp_val = getattr(value, "description_DiagramElementMapping265", None)
                setattr(value, "description_DiagramElementMapping265", self)

    @property
    def viewpoint_diagram_DDiagramElement267(self):
        return self.__viewpoint_diagram_DDiagramElement267

    @viewpoint_diagram_DDiagramElement267.setter
    def viewpoint_diagram_DDiagramElement267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElement__viewpoint_diagram_DDiagramElement267", None)
        self.__viewpoint_diagram_DDiagramElement267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GraphicalFilter"):
                    opp_val = getattr(item, "GraphicalFilter", None)
                    
                    if opp_val == self:
                        setattr(item, "GraphicalFilter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GraphicalFilter"):
                    opp_val = getattr(item, "GraphicalFilter", None)
                    
                    setattr(item, "GraphicalFilter", self)
                    

    def isFold(self, viewpoint_alreadyManagedElements) :
        # TODO: Implement isFold method
        pass

    def getParentDiagram(self) :
        # TODO: Implement getParentDiagram method
        pass

class DragAndDropTarget:

    pass
class viewpoint_diagram_DDiagramElementContainer(diagram_EdgeTarget, DContainer, DragAndDropTarget, diagram_AbstractDNode):

    def __init__(self, width: str, height: str, viewpoint_diagram_DDiagramElementContainer289: set["DDiagramElementContainer"] = None, viewpoint_diagram_DDiagramElementContainer292: set["DDiagramElement"] = None, viewpoint_diagram_DDiagramElementContainer295: "ContainerStyle" = None, viewpoint_diagram_DDiagramElementContainer297: set["DDiagram"] = None, viewpoint_diagram_DDiagramElementContainer: set["DNode"] = None, viewpoint_diagram_DDiagramElementContainer300: "diagram_viewpoint_Style" = None, viewpoint_diagram_DDiagramElementContainer303: "description_ContainerMapping" = None, viewpoint_diagram_DDiagramElementContainer305: set["description_ContainerMapping"] = None):
        self.width = width
        self.height = height
        self.viewpoint_diagram_DDiagramElementContainer289 = viewpoint_diagram_DDiagramElementContainer289 if viewpoint_diagram_DDiagramElementContainer289 is not None else set()
        self.viewpoint_diagram_DDiagramElementContainer292 = viewpoint_diagram_DDiagramElementContainer292 if viewpoint_diagram_DDiagramElementContainer292 is not None else set()
        self.viewpoint_diagram_DDiagramElementContainer295 = viewpoint_diagram_DDiagramElementContainer295
        self.viewpoint_diagram_DDiagramElementContainer297 = viewpoint_diagram_DDiagramElementContainer297 if viewpoint_diagram_DDiagramElementContainer297 is not None else set()
        self.viewpoint_diagram_DDiagramElementContainer = viewpoint_diagram_DDiagramElementContainer if viewpoint_diagram_DDiagramElementContainer is not None else set()
        self.viewpoint_diagram_DDiagramElementContainer300 = viewpoint_diagram_DDiagramElementContainer300
        self.viewpoint_diagram_DDiagramElementContainer303 = viewpoint_diagram_DDiagramElementContainer303
        self.viewpoint_diagram_DDiagramElementContainer305 = viewpoint_diagram_DDiagramElementContainer305 if viewpoint_diagram_DDiagramElementContainer305 is not None else set()
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def viewpoint_diagram_DDiagramElementContainer297(self):
        return self.__viewpoint_diagram_DDiagramElementContainer297

    @viewpoint_diagram_DDiagramElementContainer297.setter
    def viewpoint_diagram_DDiagramElementContainer297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElementContainer__viewpoint_diagram_DDiagramElementContainer297", None)
        self.__viewpoint_diagram_DDiagramElementContainer297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagram298"):
                    opp_val = getattr(item, "DDiagram298", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagram298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagram298"):
                    opp_val = getattr(item, "DDiagram298", None)
                    
                    setattr(item, "DDiagram298", self)
                    

    @property
    def viewpoint_diagram_DDiagramElementContainer303(self):
        return self.__viewpoint_diagram_DDiagramElementContainer303

    @viewpoint_diagram_DDiagramElementContainer303.setter
    def viewpoint_diagram_DDiagramElementContainer303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElementContainer__viewpoint_diagram_DDiagramElementContainer303", None)
        self.__viewpoint_diagram_DDiagramElementContainer303 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_ContainerMapping"):
                opp_val = getattr(old_value, "description_ContainerMapping", None)
                if opp_val == self:
                    setattr(old_value, "description_ContainerMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_ContainerMapping"):
                opp_val = getattr(value, "description_ContainerMapping", None)
                setattr(value, "description_ContainerMapping", self)

    @property
    def viewpoint_diagram_DDiagramElementContainer305(self):
        return self.__viewpoint_diagram_DDiagramElementContainer305

    @viewpoint_diagram_DDiagramElementContainer305.setter
    def viewpoint_diagram_DDiagramElementContainer305(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElementContainer__viewpoint_diagram_DDiagramElementContainer305", None)
        self.__viewpoint_diagram_DDiagramElementContainer305 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ContainerMapping306"):
                    opp_val = getattr(item, "description_ContainerMapping306", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ContainerMapping306", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ContainerMapping306"):
                    opp_val = getattr(item, "description_ContainerMapping306", None)
                    
                    setattr(item, "description_ContainerMapping306", self)
                    

    @property
    def viewpoint_diagram_DDiagramElementContainer295(self):
        return self.__viewpoint_diagram_DDiagramElementContainer295

    @viewpoint_diagram_DDiagramElementContainer295.setter
    def viewpoint_diagram_DDiagramElementContainer295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElementContainer__viewpoint_diagram_DDiagramElementContainer295", None)
        self.__viewpoint_diagram_DDiagramElementContainer295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContainerStyle"):
                opp_val = getattr(old_value, "ContainerStyle", None)
                if opp_val == self:
                    setattr(old_value, "ContainerStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContainerStyle"):
                opp_val = getattr(value, "ContainerStyle", None)
                setattr(value, "ContainerStyle", self)

    @property
    def viewpoint_diagram_DDiagramElementContainer292(self):
        return self.__viewpoint_diagram_DDiagramElementContainer292

    @viewpoint_diagram_DDiagramElementContainer292.setter
    def viewpoint_diagram_DDiagramElementContainer292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElementContainer__viewpoint_diagram_DDiagramElementContainer292", None)
        self.__viewpoint_diagram_DDiagramElementContainer292 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagramElement293"):
                    opp_val = getattr(item, "DDiagramElement293", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagramElement293", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagramElement293"):
                    opp_val = getattr(item, "DDiagramElement293", None)
                    
                    setattr(item, "DDiagramElement293", self)
                    

    @property
    def viewpoint_diagram_DDiagramElementContainer300(self):
        return self.__viewpoint_diagram_DDiagramElementContainer300

    @viewpoint_diagram_DDiagramElementContainer300.setter
    def viewpoint_diagram_DDiagramElementContainer300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElementContainer__viewpoint_diagram_DDiagramElementContainer300", None)
        self.__viewpoint_diagram_DDiagramElementContainer300 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_Style301"):
                opp_val = getattr(old_value, "diagram_viewpoint_Style301", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_Style301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_Style301"):
                opp_val = getattr(value, "diagram_viewpoint_Style301", None)
                setattr(value, "diagram_viewpoint_Style301", self)

    @property
    def viewpoint_diagram_DDiagramElementContainer(self):
        return self.__viewpoint_diagram_DDiagramElementContainer

    @viewpoint_diagram_DDiagramElementContainer.setter
    def viewpoint_diagram_DDiagramElementContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElementContainer__viewpoint_diagram_DDiagramElementContainer", None)
        self.__viewpoint_diagram_DDiagramElementContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DNode287"):
                    opp_val = getattr(item, "DNode287", None)
                    
                    if opp_val == self:
                        setattr(item, "DNode287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DNode287"):
                    opp_val = getattr(item, "DNode287", None)
                    
                    setattr(item, "DNode287", self)
                    

    @property
    def viewpoint_diagram_DDiagramElementContainer289(self):
        return self.__viewpoint_diagram_DDiagramElementContainer289

    @viewpoint_diagram_DDiagramElementContainer289.setter
    def viewpoint_diagram_DDiagramElementContainer289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagramElementContainer__viewpoint_diagram_DDiagramElementContainer289", None)
        self.__viewpoint_diagram_DDiagramElementContainer289 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagramElementContainer290"):
                    opp_val = getattr(item, "DDiagramElementContainer290", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagramElementContainer290", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagramElementContainer290"):
                    opp_val = getattr(item, "DDiagramElementContainer290", None)
                    
                    setattr(item, "DDiagramElementContainer290", self)
                    

    def getContainersFromMapping(self, viewpoint_mapping) :
        # TODO: Implement getContainersFromMapping method
        pass

    def getNodesFromMapping(self, viewpoint_mapping) :
        # TODO: Implement getNodesFromMapping method
        pass

class viewpoint_diagram_DNode(diagram_EdgeTarget, DragAndDropTarget, diagram_AbstractDNode):

    def __init__(self, height: str, labelPosition: str, resizeKind: str, width: str, viewpoint_diagram_DNode282: "description_NodeMapping" = None, viewpoint_diagram_DNode284: set["description_NodeMapping"] = None, viewpoint_diagram_DNode: "NodeStyle" = None, viewpoint_diagram_DNode277: set["DDiagram"] = None, viewpoint_diagram_DNode280: "diagram_viewpoint_Style" = None):
        self.height = height
        self.labelPosition = labelPosition
        self.resizeKind = resizeKind
        self.width = width
        self.viewpoint_diagram_DNode282 = viewpoint_diagram_DNode282
        self.viewpoint_diagram_DNode284 = viewpoint_diagram_DNode284 if viewpoint_diagram_DNode284 is not None else set()
        self.viewpoint_diagram_DNode = viewpoint_diagram_DNode
        self.viewpoint_diagram_DNode277 = viewpoint_diagram_DNode277 if viewpoint_diagram_DNode277 is not None else set()
        self.viewpoint_diagram_DNode280 = viewpoint_diagram_DNode280
        
        pass
    @property
    def labelPosition(self):
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def resizeKind(self):
        return self.__resizeKind

    @resizeKind.setter
    def resizeKind(self, resizeKind: str):
        self.__resizeKind = resizeKind


    @property
    def viewpoint_diagram_DNode277(self):
        return self.__viewpoint_diagram_DNode277

    @viewpoint_diagram_DNode277.setter
    def viewpoint_diagram_DNode277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DNode__viewpoint_diagram_DNode277", None)
        self.__viewpoint_diagram_DNode277 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagram278"):
                    opp_val = getattr(item, "DDiagram278", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagram278", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagram278"):
                    opp_val = getattr(item, "DDiagram278", None)
                    
                    setattr(item, "DDiagram278", self)
                    

    @property
    def viewpoint_diagram_DNode284(self):
        return self.__viewpoint_diagram_DNode284

    @viewpoint_diagram_DNode284.setter
    def viewpoint_diagram_DNode284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DNode__viewpoint_diagram_DNode284", None)
        self.__viewpoint_diagram_DNode284 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_NodeMapping285"):
                    opp_val = getattr(item, "description_NodeMapping285", None)
                    
                    if opp_val == self:
                        setattr(item, "description_NodeMapping285", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_NodeMapping285"):
                    opp_val = getattr(item, "description_NodeMapping285", None)
                    
                    setattr(item, "description_NodeMapping285", self)
                    

    @property
    def viewpoint_diagram_DNode(self):
        return self.__viewpoint_diagram_DNode

    @viewpoint_diagram_DNode.setter
    def viewpoint_diagram_DNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DNode__viewpoint_diagram_DNode", None)
        self.__viewpoint_diagram_DNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeStyle"):
                opp_val = getattr(old_value, "NodeStyle", None)
                if opp_val == self:
                    setattr(old_value, "NodeStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeStyle"):
                opp_val = getattr(value, "NodeStyle", None)
                setattr(value, "NodeStyle", self)

    @property
    def viewpoint_diagram_DNode280(self):
        return self.__viewpoint_diagram_DNode280

    @viewpoint_diagram_DNode280.setter
    def viewpoint_diagram_DNode280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DNode__viewpoint_diagram_DNode280", None)
        self.__viewpoint_diagram_DNode280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_Style"):
                opp_val = getattr(old_value, "diagram_viewpoint_Style", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_Style", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_Style"):
                opp_val = getattr(value, "diagram_viewpoint_Style", None)
                setattr(value, "diagram_viewpoint_Style", self)

    @property
    def viewpoint_diagram_DNode282(self):
        return self.__viewpoint_diagram_DNode282

    @viewpoint_diagram_DNode282.setter
    def viewpoint_diagram_DNode282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DNode__viewpoint_diagram_DNode282", None)
        self.__viewpoint_diagram_DNode282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_NodeMapping"):
                opp_val = getattr(old_value, "description_NodeMapping", None)
                if opp_val == self:
                    setattr(old_value, "description_NodeMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_NodeMapping"):
                opp_val = getattr(value, "description_NodeMapping", None)
                setattr(value, "description_NodeMapping", self)

class DRepresentation:

    pass
class InformationSection:

    pass
class viewpoint_audit_TemplateInformationSection(InformationSection):

    def __init__(self, templatePath: str):
        self.templatePath = templatePath
        
        pass
    @property
    def templatePath(self):
        return self.__templatePath

    @templatePath.setter
    def templatePath(self, templatePath: str):
        self.__templatePath = templatePath


class description_DiagramDescription:

    pass
class viewpoint_description_DiagramImportDescription(description_RepresentationImportDescription, description_DiagramDescription):

    pass
class DDiagramElement:

    pass
class viewpoint_diagram_AbstractDNode(DDiagramElement):

    def __init__(self, arrangeConstraints: str, viewpoint_diagram_AbstractDNode: set["DNode"] = None, DDiagramElement228: "viewpoint_diagram_DDiagram" = None, DDiagramElement: "viewpoint_diagram_DDiagram" = None, DDiagramElement308: "viewpoint_diagram_DNodeContainer" = None, DDiagramElement293: "viewpoint_diagram_DDiagramElementContainer" = None, DDiagramElement258: "viewpoint_diagram_DDiagram" = None):
        self.arrangeConstraints = arrangeConstraints
        self.viewpoint_diagram_AbstractDNode = viewpoint_diagram_AbstractDNode if viewpoint_diagram_AbstractDNode is not None else set()
        
        pass
    @property
    def arrangeConstraints(self):
        return self.__arrangeConstraints

    @arrangeConstraints.setter
    def arrangeConstraints(self, arrangeConstraints: str):
        self.__arrangeConstraints = arrangeConstraints


    @property
    def viewpoint_diagram_AbstractDNode(self):
        return self.__viewpoint_diagram_AbstractDNode

    @viewpoint_diagram_AbstractDNode.setter
    def viewpoint_diagram_AbstractDNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_AbstractDNode__viewpoint_diagram_AbstractDNode", None)
        self.__viewpoint_diagram_AbstractDNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DNode274"):
                    opp_val = getattr(item, "DNode274", None)
                    
                    if opp_val == self:
                        setattr(item, "DNode274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DNode274"):
                    opp_val = getattr(item, "DNode274", None)
                    
                    setattr(item, "DNode274", self)
                    

class SwitchChild:

    pass
class viewpoint_tool_Case(SwitchChild):

    def __init__(self, conditionExpression: str):
        self.conditionExpression = conditionExpression
        
        pass
    @property
    def conditionExpression(self):
        return self.__conditionExpression

    @conditionExpression.setter
    def conditionExpression(self, conditionExpression: str):
        self.__conditionExpression = conditionExpression


class viewpoint_tool_FeatureChangeListener:

    def __init__(self, domainClass: str, featureName: str):
        self.domainClass = domainClass
        self.featureName = featureName
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def domainClass(self):
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass


class tool_FeatureChangeListener:

    pass
class viewpoint_audit_InformationSection(ABC):

    def __init__(self):
        
        pass
    def getContent(self, viewpoint_eObj) :
        # TODO: Implement getContent method
        pass

class tool_Default:

    pass
class tool_Case:

    pass
class viewpoint_tool_Default(SwitchChild):

    pass
class viewpoint_tool_SwitchChild(ABC):

    pass
class viewpoint_tool_ToolFilterDescription:

    def __init__(self, precondition: str, elementsToListen: str, viewpoint_tool_ToolFilterDescription: set["tool_FeatureChangeListener"] = None):
        self.precondition = precondition
        self.elementsToListen = elementsToListen
        self.viewpoint_tool_ToolFilterDescription = viewpoint_tool_ToolFilterDescription if viewpoint_tool_ToolFilterDescription is not None else set()
        
        pass
    @property
    def precondition(self):
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition


    @property
    def elementsToListen(self):
        return self.__elementsToListen

    @elementsToListen.setter
    def elementsToListen(self, elementsToListen: str):
        self.__elementsToListen = elementsToListen


    @property
    def viewpoint_tool_ToolFilterDescription(self):
        return self.__viewpoint_tool_ToolFilterDescription

    @viewpoint_tool_ToolFilterDescription.setter
    def viewpoint_tool_ToolFilterDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolFilterDescription__viewpoint_tool_ToolFilterDescription", None)
        self.__viewpoint_tool_ToolFilterDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_FeatureChangeListener"):
                    opp_val = getattr(item, "tool_FeatureChangeListener", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_FeatureChangeListener", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_FeatureChangeListener"):
                    opp_val = getattr(item, "tool_FeatureChangeListener", None)
                    
                    setattr(item, "tool_FeatureChangeListener", self)
                    

class viewpoint_tool_ExternalJavaActionParameter:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class viewpoint_tool_NameVariable(AbstractVariable):

    pass
class tool_viewpoint_EObject:

    pass
class ContainerModelOperation:

    pass
class viewpoint_tool_MoveElement(ContainerModelOperation):

    def __init__(self, newContainerExpression: str, featureName: str):
        self.newContainerExpression = newContainerExpression
        self.featureName = featureName
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def newContainerExpression(self):
        return self.__newContainerExpression

    @newContainerExpression.setter
    def newContainerExpression(self, newContainerExpression: str):
        self.__newContainerExpression = newContainerExpression


class viewpoint_tool_SetValue(ContainerModelOperation):

    def __init__(self, featureName: str, valueExpression: str):
        self.featureName = featureName
        self.valueExpression = valueExpression
        
        pass
    @property
    def valueExpression(self):
        return self.__valueExpression

    @valueExpression.setter
    def valueExpression(self, valueExpression: str):
        self.__valueExpression = valueExpression


    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


class viewpoint_tool_CreateView(ContainerModelOperation):

    def __init__(self, containerViewExpression: str, variableName: str, viewpoint_tool_CreateView: "description_DiagramElementMapping" = None):
        self.containerViewExpression = containerViewExpression
        self.variableName = variableName
        self.viewpoint_tool_CreateView = viewpoint_tool_CreateView
        
        pass
    @property
    def variableName(self):
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName


    @property
    def containerViewExpression(self):
        return self.__containerViewExpression

    @containerViewExpression.setter
    def containerViewExpression(self, containerViewExpression: str):
        self.__containerViewExpression = containerViewExpression


    @property
    def viewpoint_tool_CreateView(self):
        return self.__viewpoint_tool_CreateView

    @viewpoint_tool_CreateView.setter
    def viewpoint_tool_CreateView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_CreateView__viewpoint_tool_CreateView", None)
        self.__viewpoint_tool_CreateView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_DiagramElementMapping716"):
                opp_val = getattr(old_value, "description_DiagramElementMapping716", None)
                if opp_val == self:
                    setattr(old_value, "description_DiagramElementMapping716", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_DiagramElementMapping716"):
                opp_val = getattr(value, "description_DiagramElementMapping716", None)
                setattr(value, "description_DiagramElementMapping716", self)

class viewpoint_tool_If(ContainerModelOperation):

    def __init__(self, conditionExpression: str):
        self.conditionExpression = conditionExpression
        
        pass
    @property
    def conditionExpression(self):
        return self.__conditionExpression

    @conditionExpression.setter
    def conditionExpression(self, conditionExpression: str):
        self.__conditionExpression = conditionExpression


class viewpoint_tool_SetObject(ContainerModelOperation):

    def __init__(self, featureName: str, viewpoint_tool_SetObject: "tool_viewpoint_EObject" = None):
        self.featureName = featureName
        self.viewpoint_tool_SetObject = viewpoint_tool_SetObject
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def viewpoint_tool_SetObject(self):
        return self.__viewpoint_tool_SetObject

    @viewpoint_tool_SetObject.setter
    def viewpoint_tool_SetObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_SetObject__viewpoint_tool_SetObject", None)
        self.__viewpoint_tool_SetObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_viewpoint_EObject"):
                opp_val = getattr(old_value, "tool_viewpoint_EObject", None)
                if opp_val == self:
                    setattr(old_value, "tool_viewpoint_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_viewpoint_EObject"):
                opp_val = getattr(value, "tool_viewpoint_EObject", None)
                setattr(value, "tool_viewpoint_EObject", self)

class viewpoint_tool_For(ContainerModelOperation):

    def __init__(self, expression: str, iteratorName: str):
        self.expression = expression
        self.iteratorName = iteratorName
        
        pass
    @property
    def iteratorName(self):
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName


    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


class viewpoint_tool_ChangeContext(ContainerModelOperation):

    def __init__(self, browseExpression: str):
        self.browseExpression = browseExpression
        
        pass
    @property
    def browseExpression(self):
        return self.__browseExpression

    @browseExpression.setter
    def browseExpression(self, browseExpression: str):
        self.__browseExpression = browseExpression


class viewpoint_tool_Navigation(ContainerModelOperation):

    def __init__(self, createIfNotExistent: bool, viewpoint_tool_Navigation: "description_DiagramDescription" = None):
        self.createIfNotExistent = createIfNotExistent
        self.viewpoint_tool_Navigation = viewpoint_tool_Navigation
        
        pass
    @property
    def createIfNotExistent(self):
        return self.__createIfNotExistent

    @createIfNotExistent.setter
    def createIfNotExistent(self, createIfNotExistent: bool):
        self.__createIfNotExistent = createIfNotExistent


    @property
    def viewpoint_tool_Navigation(self):
        return self.__viewpoint_tool_Navigation

    @viewpoint_tool_Navigation.setter
    def viewpoint_tool_Navigation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_Navigation__viewpoint_tool_Navigation", None)
        self.__viewpoint_tool_Navigation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_DiagramDescription718"):
                opp_val = getattr(old_value, "description_DiagramDescription718", None)
                if opp_val == self:
                    setattr(old_value, "description_DiagramDescription718", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_DiagramDescription718"):
                opp_val = getattr(value, "description_DiagramDescription718", None)
                setattr(value, "description_DiagramDescription718", self)

class viewpoint_tool_RemoveElement(ContainerModelOperation):

    pass
class viewpoint_tool_Unset(ContainerModelOperation):

    def __init__(self, elementExpression: str, featureName: str):
        self.elementExpression = elementExpression
        self.featureName = featureName
        
        pass
    @property
    def featureName(self):
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName


    @property
    def elementExpression(self):
        return self.__elementExpression

    @elementExpression.setter
    def elementExpression(self, elementExpression: str):
        self.__elementExpression = elementExpression


class viewpoint_tool_DeleteView(ContainerModelOperation):

    pass
class viewpoint_tool_CreateInstance(ContainerModelOperation):

    def __init__(self, typeName: str, referenceName: str, variableName: str):
        self.typeName = typeName
        self.referenceName = referenceName
        self.variableName = variableName
        
        pass
    @property
    def typeName(self):
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName


    @property
    def variableName(self):
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName


    @property
    def referenceName(self):
        return self.__referenceName

    @referenceName.setter
    def referenceName(self, referenceName: str):
        self.__referenceName = referenceName


class viewpoint_tool_InitialContainerDropOperation:

    pass
class viewpoint_tool_InitEdgeCreationOperation:

    pass
class viewpoint_tool_InitialOperation:

    pass
class viewpoint_tool_InitialNodeCreationOperation:

    pass
class viewpoint_tool_ModelOperation(ABC):

    pass
class tool_ModelOperation:

    pass
class ModelOperation:

    pass
class viewpoint_tool_Switch(ModelOperation):

    pass
class viewpoint_tool_ContainerModelOperation(ModelOperation):

    pass
class tool_ExternalJavaActionParameter:

    pass
class tool_ContainerModelOperation:

    pass
class viewpoint_tool_DropContainerVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ElementDeleteVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ElementViewVariable(tool_AbstractVariable, tool_VariableContainer):

    pass
class MenuItemDescription:

    pass
class viewpoint_tool_OperationAction(MenuItemDescription):

    pass
class tool_MenuItemDescription:

    pass
class viewpoint_tool_ExternalJavaAction(tool_ContainerModelOperation, tool_MenuItemDescription):

    def __init__(self, id: str, viewpoint_tool_ExternalJavaAction: set["tool_ExternalJavaActionParameter"] = None, tool_MenuItemDescription207: "viewpoint_tool_PopupMenu" = None, tool_MenuItemDescription: "viewpoint_tool_MenuItemDescriptionReference" = None):
        self.id = id
        self.viewpoint_tool_ExternalJavaAction = viewpoint_tool_ExternalJavaAction if viewpoint_tool_ExternalJavaAction is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def viewpoint_tool_ExternalJavaAction(self):
        return self.__viewpoint_tool_ExternalJavaAction

    @viewpoint_tool_ExternalJavaAction.setter
    def viewpoint_tool_ExternalJavaAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ExternalJavaAction__viewpoint_tool_ExternalJavaAction", None)
        self.__viewpoint_tool_ExternalJavaAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ExternalJavaActionParameter"):
                    opp_val = getattr(item, "tool_ExternalJavaActionParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ExternalJavaActionParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ExternalJavaActionParameter"):
                    opp_val = getattr(item, "tool_ExternalJavaActionParameter", None)
                    
                    setattr(item, "tool_ExternalJavaActionParameter", self)
                    

class viewpoint_tool_ExternalJavaActionCall(tool_ContainerModelOperation, tool_MenuItemDescription):

    pass
class MenuItemOrRef:

    pass
class viewpoint_tool_MenuItemDescriptionReference(MenuItemOrRef):

    pass
class tool_MenuItemOrRef:

    pass
class viewpoint_tool_MenuItemOrRef(ABC):

    pass
class tool_NameVariable:

    pass
class tool_SelectContainerVariable:

    pass
class tool_InitialContainerDropOperation:

    pass
class tool_ContainerViewVariable:

    pass
class tool_ElementSelectVariable:

    pass
class description_SelectionDescription:

    pass
class viewpoint_tool_SelectModelElementVariable(tool_SubVariable, description_SelectionDescription):

    pass
class tool_AbstractToolDescription:

    pass
class viewpoint_tool_MenuItemDescription(tool_AbstractToolDescription, tool_MenuItemOrRef):

    def __init__(self, icon: str, tool_AbstractToolDescription560: "viewpoint_description_Layer" = None, tool_AbstractToolDescription623: "viewpoint_tool_ToolGroupExtension" = None, tool_AbstractToolDescription443: "viewpoint_description_DiagramDescription" = None, tool_AbstractToolDescription619: "viewpoint_tool_ToolGroup" = None, tool_AbstractToolDescription462: "viewpoint_description_DiagramDescription" = None, tool_AbstractToolDescription554: "viewpoint_description_Layer" = None, tool_AbstractToolDescription: "viewpoint_description_DiagramDescription" = None):
        self.icon = icon
        
        pass
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon


class viewpoint_tool_SelectionWizardDescription(tool_AbstractToolDescription, description_SelectionDescription):

    def __init__(self, iconPath: str, windowTitle: str, windowImagePath: str, viewpoint_tool_SelectionWizardDescription159: "tool_ContainerViewVariable" = None, viewpoint_tool_SelectionWizardDescription162: "tool_SelectContainerVariable" = None, viewpoint_tool_SelectionWizardDescription164: "tool_InitialOperation" = None, viewpoint_tool_SelectionWizardDescription: "tool_ElementSelectVariable" = None, tool_AbstractToolDescription560: "viewpoint_description_Layer" = None, tool_AbstractToolDescription623: "viewpoint_tool_ToolGroupExtension" = None, tool_AbstractToolDescription443: "viewpoint_description_DiagramDescription" = None, tool_AbstractToolDescription619: "viewpoint_tool_ToolGroup" = None, tool_AbstractToolDescription462: "viewpoint_description_DiagramDescription" = None, tool_AbstractToolDescription554: "viewpoint_description_Layer" = None, tool_AbstractToolDescription: "viewpoint_description_DiagramDescription" = None):
        self.iconPath = iconPath
        self.windowTitle = windowTitle
        self.windowImagePath = windowImagePath
        self.viewpoint_tool_SelectionWizardDescription159 = viewpoint_tool_SelectionWizardDescription159
        self.viewpoint_tool_SelectionWizardDescription162 = viewpoint_tool_SelectionWizardDescription162
        self.viewpoint_tool_SelectionWizardDescription164 = viewpoint_tool_SelectionWizardDescription164
        self.viewpoint_tool_SelectionWizardDescription = viewpoint_tool_SelectionWizardDescription
        
        pass
    @property
    def iconPath(self):
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath


    @property
    def windowImagePath(self):
        return self.__windowImagePath

    @windowImagePath.setter
    def windowImagePath(self, windowImagePath: str):
        self.__windowImagePath = windowImagePath


    @property
    def windowTitle(self):
        return self.__windowTitle

    @windowTitle.setter
    def windowTitle(self, windowTitle: str):
        self.__windowTitle = windowTitle


    @property
    def viewpoint_tool_SelectionWizardDescription(self):
        return self.__viewpoint_tool_SelectionWizardDescription

    @viewpoint_tool_SelectionWizardDescription.setter
    def viewpoint_tool_SelectionWizardDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_SelectionWizardDescription__viewpoint_tool_SelectionWizardDescription", None)
        self.__viewpoint_tool_SelectionWizardDescription = value
        
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
    def viewpoint_tool_SelectionWizardDescription162(self):
        return self.__viewpoint_tool_SelectionWizardDescription162

    @viewpoint_tool_SelectionWizardDescription162.setter
    def viewpoint_tool_SelectionWizardDescription162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_SelectionWizardDescription__viewpoint_tool_SelectionWizardDescription162", None)
        self.__viewpoint_tool_SelectionWizardDescription162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SelectContainerVariable"):
                opp_val = getattr(old_value, "tool_SelectContainerVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_SelectContainerVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SelectContainerVariable"):
                opp_val = getattr(value, "tool_SelectContainerVariable", None)
                setattr(value, "tool_SelectContainerVariable", self)

    @property
    def viewpoint_tool_SelectionWizardDescription164(self):
        return self.__viewpoint_tool_SelectionWizardDescription164

    @viewpoint_tool_SelectionWizardDescription164.setter
    def viewpoint_tool_SelectionWizardDescription164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_SelectionWizardDescription__viewpoint_tool_SelectionWizardDescription164", None)
        self.__viewpoint_tool_SelectionWizardDescription164 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation165"):
                opp_val = getattr(old_value, "tool_InitialOperation165", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation165"):
                opp_val = getattr(value, "tool_InitialOperation165", None)
                setattr(value, "tool_InitialOperation165", self)

    @property
    def viewpoint_tool_SelectionWizardDescription159(self):
        return self.__viewpoint_tool_SelectionWizardDescription159

    @viewpoint_tool_SelectionWizardDescription159.setter
    def viewpoint_tool_SelectionWizardDescription159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_SelectionWizardDescription__viewpoint_tool_SelectionWizardDescription159", None)
        self.__viewpoint_tool_SelectionWizardDescription159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable160"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable160", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable160"):
                opp_val = getattr(value, "tool_ContainerViewVariable160", None)
                setattr(value, "tool_ContainerViewVariable160", self)

class tool_DropContainerVariable:

    pass
class description_DiagramElementMapping:

    pass
class tool_InitialOperation:

    pass
class tool_ElementViewVariable:

    pass
class tool_ElementVariable:

    pass
class MappingBasedToolDescription:

    pass
class viewpoint_tool_PasteDescription(MappingBasedToolDescription):

    def __init__(self, viewpoint_tool_PasteDescription: "tool_DropContainerVariable" = None, viewpoint_tool_PasteDescription146: "tool_ContainerViewVariable" = None, viewpoint_tool_PasteDescription149: "tool_ElementViewVariable" = None, viewpoint_tool_PasteDescription152: "tool_ElementVariable" = None, viewpoint_tool_PasteDescription155: "tool_InitialOperation" = None):
        self.viewpoint_tool_PasteDescription = viewpoint_tool_PasteDescription
        self.viewpoint_tool_PasteDescription146 = viewpoint_tool_PasteDescription146
        self.viewpoint_tool_PasteDescription149 = viewpoint_tool_PasteDescription149
        self.viewpoint_tool_PasteDescription152 = viewpoint_tool_PasteDescription152
        self.viewpoint_tool_PasteDescription155 = viewpoint_tool_PasteDescription155
        
        pass
    @property
    def viewpoint_tool_PasteDescription155(self):
        return self.__viewpoint_tool_PasteDescription155

    @viewpoint_tool_PasteDescription155.setter
    def viewpoint_tool_PasteDescription155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PasteDescription__viewpoint_tool_PasteDescription155", None)
        self.__viewpoint_tool_PasteDescription155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation156"):
                opp_val = getattr(old_value, "tool_InitialOperation156", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation156"):
                opp_val = getattr(value, "tool_InitialOperation156", None)
                setattr(value, "tool_InitialOperation156", self)

    @property
    def viewpoint_tool_PasteDescription152(self):
        return self.__viewpoint_tool_PasteDescription152

    @viewpoint_tool_PasteDescription152.setter
    def viewpoint_tool_PasteDescription152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PasteDescription__viewpoint_tool_PasteDescription152", None)
        self.__viewpoint_tool_PasteDescription152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementVariable153"):
                opp_val = getattr(old_value, "tool_ElementVariable153", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementVariable153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementVariable153"):
                opp_val = getattr(value, "tool_ElementVariable153", None)
                setattr(value, "tool_ElementVariable153", self)

    @property
    def viewpoint_tool_PasteDescription149(self):
        return self.__viewpoint_tool_PasteDescription149

    @viewpoint_tool_PasteDescription149.setter
    def viewpoint_tool_PasteDescription149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PasteDescription__viewpoint_tool_PasteDescription149", None)
        self.__viewpoint_tool_PasteDescription149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementViewVariable150"):
                opp_val = getattr(old_value, "tool_ElementViewVariable150", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementViewVariable150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementViewVariable150"):
                opp_val = getattr(value, "tool_ElementViewVariable150", None)
                setattr(value, "tool_ElementViewVariable150", self)

    @property
    def viewpoint_tool_PasteDescription146(self):
        return self.__viewpoint_tool_PasteDescription146

    @viewpoint_tool_PasteDescription146.setter
    def viewpoint_tool_PasteDescription146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PasteDescription__viewpoint_tool_PasteDescription146", None)
        self.__viewpoint_tool_PasteDescription146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable147"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable147", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable147"):
                opp_val = getattr(value, "tool_ContainerViewVariable147", None)
                setattr(value, "tool_ContainerViewVariable147", self)

    @property
    def viewpoint_tool_PasteDescription(self):
        return self.__viewpoint_tool_PasteDescription

    @viewpoint_tool_PasteDescription.setter
    def viewpoint_tool_PasteDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PasteDescription__viewpoint_tool_PasteDescription", None)
        self.__viewpoint_tool_PasteDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DropContainerVariable144"):
                opp_val = getattr(old_value, "tool_DropContainerVariable144", None)
                if opp_val == self:
                    setattr(old_value, "tool_DropContainerVariable144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DropContainerVariable144"):
                opp_val = getattr(value, "tool_DropContainerVariable144", None)
                setattr(value, "tool_DropContainerVariable144", self)

    def getContainers(self) :
        # TODO: Implement getContainers method
        pass

class viewpoint_tool_ContainerDropDescription(MappingBasedToolDescription):

    def __init__(self, dragSource: str, moveEdges: bool, viewpoint_tool_ContainerDropDescription138: "tool_ElementDropVariable" = None, viewpoint_tool_ContainerDropDescription: set["description_DiagramElementMapping"] = None, viewpoint_tool_ContainerDropDescription133: "tool_DropContainerVariable" = None, viewpoint_tool_ContainerDropDescription135: "tool_DropContainerVariable" = None, viewpoint_tool_ContainerDropDescription140: "tool_ContainerViewVariable" = None, viewpoint_tool_ContainerDropDescription142: "tool_InitialContainerDropOperation" = None):
        self.dragSource = dragSource
        self.moveEdges = moveEdges
        self.viewpoint_tool_ContainerDropDescription138 = viewpoint_tool_ContainerDropDescription138
        self.viewpoint_tool_ContainerDropDescription = viewpoint_tool_ContainerDropDescription if viewpoint_tool_ContainerDropDescription is not None else set()
        self.viewpoint_tool_ContainerDropDescription133 = viewpoint_tool_ContainerDropDescription133
        self.viewpoint_tool_ContainerDropDescription135 = viewpoint_tool_ContainerDropDescription135
        self.viewpoint_tool_ContainerDropDescription140 = viewpoint_tool_ContainerDropDescription140
        self.viewpoint_tool_ContainerDropDescription142 = viewpoint_tool_ContainerDropDescription142
        
        pass
    @property
    def dragSource(self):
        return self.__dragSource

    @dragSource.setter
    def dragSource(self, dragSource: str):
        self.__dragSource = dragSource


    @property
    def moveEdges(self):
        return self.__moveEdges

    @moveEdges.setter
    def moveEdges(self, moveEdges: bool):
        self.__moveEdges = moveEdges


    @property
    def viewpoint_tool_ContainerDropDescription142(self):
        return self.__viewpoint_tool_ContainerDropDescription142

    @viewpoint_tool_ContainerDropDescription142.setter
    def viewpoint_tool_ContainerDropDescription142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerDropDescription__viewpoint_tool_ContainerDropDescription142", None)
        self.__viewpoint_tool_ContainerDropDescription142 = value
        
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
    def viewpoint_tool_ContainerDropDescription(self):
        return self.__viewpoint_tool_ContainerDropDescription

    @viewpoint_tool_ContainerDropDescription.setter
    def viewpoint_tool_ContainerDropDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerDropDescription__viewpoint_tool_ContainerDropDescription", None)
        self.__viewpoint_tool_ContainerDropDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_DiagramElementMapping"):
                    opp_val = getattr(item, "description_DiagramElementMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "description_DiagramElementMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_DiagramElementMapping"):
                    opp_val = getattr(item, "description_DiagramElementMapping", None)
                    
                    setattr(item, "description_DiagramElementMapping", self)
                    

    @property
    def viewpoint_tool_ContainerDropDescription133(self):
        return self.__viewpoint_tool_ContainerDropDescription133

    @viewpoint_tool_ContainerDropDescription133.setter
    def viewpoint_tool_ContainerDropDescription133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerDropDescription__viewpoint_tool_ContainerDropDescription133", None)
        self.__viewpoint_tool_ContainerDropDescription133 = value
        
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
    def viewpoint_tool_ContainerDropDescription140(self):
        return self.__viewpoint_tool_ContainerDropDescription140

    @viewpoint_tool_ContainerDropDescription140.setter
    def viewpoint_tool_ContainerDropDescription140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerDropDescription__viewpoint_tool_ContainerDropDescription140", None)
        self.__viewpoint_tool_ContainerDropDescription140 = value
        
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
    def viewpoint_tool_ContainerDropDescription138(self):
        return self.__viewpoint_tool_ContainerDropDescription138

    @viewpoint_tool_ContainerDropDescription138.setter
    def viewpoint_tool_ContainerDropDescription138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerDropDescription__viewpoint_tool_ContainerDropDescription138", None)
        self.__viewpoint_tool_ContainerDropDescription138 = value
        
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
    def viewpoint_tool_ContainerDropDescription135(self):
        return self.__viewpoint_tool_ContainerDropDescription135

    @viewpoint_tool_ContainerDropDescription135.setter
    def viewpoint_tool_ContainerDropDescription135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerDropDescription__viewpoint_tool_ContainerDropDescription135", None)
        self.__viewpoint_tool_ContainerDropDescription135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DropContainerVariable136"):
                opp_val = getattr(old_value, "tool_DropContainerVariable136", None)
                if opp_val == self:
                    setattr(old_value, "tool_DropContainerVariable136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DropContainerVariable136"):
                opp_val = getattr(value, "tool_DropContainerVariable136", None)
                setattr(value, "tool_DropContainerVariable136", self)

    def getBestMapping(self, viewpoint_droppedElement, viewpoint_targetContainer) :
        # TODO: Implement getBestMapping method
        pass

    def getContainers(self) :
        # TODO: Implement getContainers method
        pass

class viewpoint_tool_ContainerCreationDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, viewpoint_tool_ContainerCreationDescription666: set["description_AbstractNodeMapping"] = None, viewpoint_tool_ContainerCreationDescription: set["description_ContainerMapping"] = None, viewpoint_tool_ContainerCreationDescription657: "tool_NodeCreationVariable" = None, viewpoint_tool_ContainerCreationDescription660: "tool_ContainerViewVariable" = None, viewpoint_tool_ContainerCreationDescription663: "tool_InitialNodeCreationOperation" = None):
        self.iconPath = iconPath
        self.viewpoint_tool_ContainerCreationDescription666 = viewpoint_tool_ContainerCreationDescription666 if viewpoint_tool_ContainerCreationDescription666 is not None else set()
        self.viewpoint_tool_ContainerCreationDescription = viewpoint_tool_ContainerCreationDescription if viewpoint_tool_ContainerCreationDescription is not None else set()
        self.viewpoint_tool_ContainerCreationDescription657 = viewpoint_tool_ContainerCreationDescription657
        self.viewpoint_tool_ContainerCreationDescription660 = viewpoint_tool_ContainerCreationDescription660
        self.viewpoint_tool_ContainerCreationDescription663 = viewpoint_tool_ContainerCreationDescription663
        
        pass
    @property
    def iconPath(self):
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath


    @property
    def viewpoint_tool_ContainerCreationDescription660(self):
        return self.__viewpoint_tool_ContainerCreationDescription660

    @viewpoint_tool_ContainerCreationDescription660.setter
    def viewpoint_tool_ContainerCreationDescription660(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerCreationDescription__viewpoint_tool_ContainerCreationDescription660", None)
        self.__viewpoint_tool_ContainerCreationDescription660 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable661"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable661", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable661", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable661"):
                opp_val = getattr(value, "tool_ContainerViewVariable661", None)
                setattr(value, "tool_ContainerViewVariable661", self)

    @property
    def viewpoint_tool_ContainerCreationDescription(self):
        return self.__viewpoint_tool_ContainerCreationDescription

    @viewpoint_tool_ContainerCreationDescription.setter
    def viewpoint_tool_ContainerCreationDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerCreationDescription__viewpoint_tool_ContainerCreationDescription", None)
        self.__viewpoint_tool_ContainerCreationDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ContainerMapping655"):
                    opp_val = getattr(item, "description_ContainerMapping655", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ContainerMapping655", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ContainerMapping655"):
                    opp_val = getattr(item, "description_ContainerMapping655", None)
                    
                    setattr(item, "description_ContainerMapping655", self)
                    

    @property
    def viewpoint_tool_ContainerCreationDescription666(self):
        return self.__viewpoint_tool_ContainerCreationDescription666

    @viewpoint_tool_ContainerCreationDescription666.setter
    def viewpoint_tool_ContainerCreationDescription666(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerCreationDescription__viewpoint_tool_ContainerCreationDescription666", None)
        self.__viewpoint_tool_ContainerCreationDescription666 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_AbstractNodeMapping667"):
                    opp_val = getattr(item, "description_AbstractNodeMapping667", None)
                    
                    if opp_val == self:
                        setattr(item, "description_AbstractNodeMapping667", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_AbstractNodeMapping667"):
                    opp_val = getattr(item, "description_AbstractNodeMapping667", None)
                    
                    setattr(item, "description_AbstractNodeMapping667", self)
                    

    @property
    def viewpoint_tool_ContainerCreationDescription663(self):
        return self.__viewpoint_tool_ContainerCreationDescription663

    @viewpoint_tool_ContainerCreationDescription663.setter
    def viewpoint_tool_ContainerCreationDescription663(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerCreationDescription__viewpoint_tool_ContainerCreationDescription663", None)
        self.__viewpoint_tool_ContainerCreationDescription663 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialNodeCreationOperation664"):
                opp_val = getattr(old_value, "tool_InitialNodeCreationOperation664", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialNodeCreationOperation664", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialNodeCreationOperation664"):
                opp_val = getattr(value, "tool_InitialNodeCreationOperation664", None)
                setattr(value, "tool_InitialNodeCreationOperation664", self)

    @property
    def viewpoint_tool_ContainerCreationDescription657(self):
        return self.__viewpoint_tool_ContainerCreationDescription657

    @viewpoint_tool_ContainerCreationDescription657.setter
    def viewpoint_tool_ContainerCreationDescription657(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ContainerCreationDescription__viewpoint_tool_ContainerCreationDescription657", None)
        self.__viewpoint_tool_ContainerCreationDescription657 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_NodeCreationVariable658"):
                opp_val = getattr(old_value, "tool_NodeCreationVariable658", None)
                if opp_val == self:
                    setattr(old_value, "tool_NodeCreationVariable658", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_NodeCreationVariable658"):
                opp_val = getattr(value, "tool_NodeCreationVariable658", None)
                setattr(value, "tool_NodeCreationVariable658", self)

class viewpoint_tool_NodeCreationDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, viewpoint_tool_NodeCreationDescription634: set["description_AbstractNodeMapping"] = None, viewpoint_tool_NodeCreationDescription: set["description_NodeMapping"] = None, viewpoint_tool_NodeCreationDescription627: "tool_NodeCreationVariable" = None, viewpoint_tool_NodeCreationDescription629: "tool_ContainerViewVariable" = None, viewpoint_tool_NodeCreationDescription632: "tool_InitialNodeCreationOperation" = None):
        self.iconPath = iconPath
        self.viewpoint_tool_NodeCreationDescription634 = viewpoint_tool_NodeCreationDescription634 if viewpoint_tool_NodeCreationDescription634 is not None else set()
        self.viewpoint_tool_NodeCreationDescription = viewpoint_tool_NodeCreationDescription if viewpoint_tool_NodeCreationDescription is not None else set()
        self.viewpoint_tool_NodeCreationDescription627 = viewpoint_tool_NodeCreationDescription627
        self.viewpoint_tool_NodeCreationDescription629 = viewpoint_tool_NodeCreationDescription629
        self.viewpoint_tool_NodeCreationDescription632 = viewpoint_tool_NodeCreationDescription632
        
        pass
    @property
    def iconPath(self):
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath


    @property
    def viewpoint_tool_NodeCreationDescription632(self):
        return self.__viewpoint_tool_NodeCreationDescription632

    @viewpoint_tool_NodeCreationDescription632.setter
    def viewpoint_tool_NodeCreationDescription632(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_NodeCreationDescription__viewpoint_tool_NodeCreationDescription632", None)
        self.__viewpoint_tool_NodeCreationDescription632 = value
        
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
    def viewpoint_tool_NodeCreationDescription634(self):
        return self.__viewpoint_tool_NodeCreationDescription634

    @viewpoint_tool_NodeCreationDescription634.setter
    def viewpoint_tool_NodeCreationDescription634(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_NodeCreationDescription__viewpoint_tool_NodeCreationDescription634", None)
        self.__viewpoint_tool_NodeCreationDescription634 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_AbstractNodeMapping635"):
                    opp_val = getattr(item, "description_AbstractNodeMapping635", None)
                    
                    if opp_val == self:
                        setattr(item, "description_AbstractNodeMapping635", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_AbstractNodeMapping635"):
                    opp_val = getattr(item, "description_AbstractNodeMapping635", None)
                    
                    setattr(item, "description_AbstractNodeMapping635", self)
                    

    @property
    def viewpoint_tool_NodeCreationDescription629(self):
        return self.__viewpoint_tool_NodeCreationDescription629

    @viewpoint_tool_NodeCreationDescription629.setter
    def viewpoint_tool_NodeCreationDescription629(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_NodeCreationDescription__viewpoint_tool_NodeCreationDescription629", None)
        self.__viewpoint_tool_NodeCreationDescription629 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable630"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable630", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable630", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable630"):
                opp_val = getattr(value, "tool_ContainerViewVariable630", None)
                setattr(value, "tool_ContainerViewVariable630", self)

    @property
    def viewpoint_tool_NodeCreationDescription627(self):
        return self.__viewpoint_tool_NodeCreationDescription627

    @viewpoint_tool_NodeCreationDescription627.setter
    def viewpoint_tool_NodeCreationDescription627(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_NodeCreationDescription__viewpoint_tool_NodeCreationDescription627", None)
        self.__viewpoint_tool_NodeCreationDescription627 = value
        
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
    def viewpoint_tool_NodeCreationDescription(self):
        return self.__viewpoint_tool_NodeCreationDescription

    @viewpoint_tool_NodeCreationDescription.setter
    def viewpoint_tool_NodeCreationDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_NodeCreationDescription__viewpoint_tool_NodeCreationDescription", None)
        self.__viewpoint_tool_NodeCreationDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_NodeMapping625"):
                    opp_val = getattr(item, "description_NodeMapping625", None)
                    
                    if opp_val == self:
                        setattr(item, "description_NodeMapping625", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_NodeMapping625"):
                    opp_val = getattr(item, "description_NodeMapping625", None)
                    
                    setattr(item, "description_NodeMapping625", self)
                    

class viewpoint_tool_ReconnectEdgeDescription(MappingBasedToolDescription):

    def __init__(self, reconnectionKind: str, viewpoint_tool_ReconnectEdgeDescription695: "tool_SourceEdgeViewCreationVariable" = None, viewpoint_tool_ReconnectEdgeDescription698: "tool_TargetEdgeViewCreationVariable" = None, viewpoint_tool_ReconnectEdgeDescription701: "tool_ElementSelectVariable" = None, viewpoint_tool_ReconnectEdgeDescription: "tool_SourceEdgeCreationVariable" = None, viewpoint_tool_ReconnectEdgeDescription692: "tool_TargetEdgeCreationVariable" = None, viewpoint_tool_ReconnectEdgeDescription704: "tool_InitialOperation" = None, viewpoint_tool_ReconnectEdgeDescription707: "tool_ElementSelectVariable" = None):
        self.reconnectionKind = reconnectionKind
        self.viewpoint_tool_ReconnectEdgeDescription695 = viewpoint_tool_ReconnectEdgeDescription695
        self.viewpoint_tool_ReconnectEdgeDescription698 = viewpoint_tool_ReconnectEdgeDescription698
        self.viewpoint_tool_ReconnectEdgeDescription701 = viewpoint_tool_ReconnectEdgeDescription701
        self.viewpoint_tool_ReconnectEdgeDescription = viewpoint_tool_ReconnectEdgeDescription
        self.viewpoint_tool_ReconnectEdgeDescription692 = viewpoint_tool_ReconnectEdgeDescription692
        self.viewpoint_tool_ReconnectEdgeDescription704 = viewpoint_tool_ReconnectEdgeDescription704
        self.viewpoint_tool_ReconnectEdgeDescription707 = viewpoint_tool_ReconnectEdgeDescription707
        
        pass
    @property
    def reconnectionKind(self):
        return self.__reconnectionKind

    @reconnectionKind.setter
    def reconnectionKind(self, reconnectionKind: str):
        self.__reconnectionKind = reconnectionKind


    @property
    def viewpoint_tool_ReconnectEdgeDescription707(self):
        return self.__viewpoint_tool_ReconnectEdgeDescription707

    @viewpoint_tool_ReconnectEdgeDescription707.setter
    def viewpoint_tool_ReconnectEdgeDescription707(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ReconnectEdgeDescription__viewpoint_tool_ReconnectEdgeDescription707", None)
        self.__viewpoint_tool_ReconnectEdgeDescription707 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementSelectVariable708"):
                opp_val = getattr(old_value, "tool_ElementSelectVariable708", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementSelectVariable708", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementSelectVariable708"):
                opp_val = getattr(value, "tool_ElementSelectVariable708", None)
                setattr(value, "tool_ElementSelectVariable708", self)

    @property
    def viewpoint_tool_ReconnectEdgeDescription698(self):
        return self.__viewpoint_tool_ReconnectEdgeDescription698

    @viewpoint_tool_ReconnectEdgeDescription698.setter
    def viewpoint_tool_ReconnectEdgeDescription698(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ReconnectEdgeDescription__viewpoint_tool_ReconnectEdgeDescription698", None)
        self.__viewpoint_tool_ReconnectEdgeDescription698 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_TargetEdgeViewCreationVariable699"):
                opp_val = getattr(old_value, "tool_TargetEdgeViewCreationVariable699", None)
                if opp_val == self:
                    setattr(old_value, "tool_TargetEdgeViewCreationVariable699", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_TargetEdgeViewCreationVariable699"):
                opp_val = getattr(value, "tool_TargetEdgeViewCreationVariable699", None)
                setattr(value, "tool_TargetEdgeViewCreationVariable699", self)

    @property
    def viewpoint_tool_ReconnectEdgeDescription701(self):
        return self.__viewpoint_tool_ReconnectEdgeDescription701

    @viewpoint_tool_ReconnectEdgeDescription701.setter
    def viewpoint_tool_ReconnectEdgeDescription701(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ReconnectEdgeDescription__viewpoint_tool_ReconnectEdgeDescription701", None)
        self.__viewpoint_tool_ReconnectEdgeDescription701 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementSelectVariable702"):
                opp_val = getattr(old_value, "tool_ElementSelectVariable702", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementSelectVariable702", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementSelectVariable702"):
                opp_val = getattr(value, "tool_ElementSelectVariable702", None)
                setattr(value, "tool_ElementSelectVariable702", self)

    @property
    def viewpoint_tool_ReconnectEdgeDescription(self):
        return self.__viewpoint_tool_ReconnectEdgeDescription

    @viewpoint_tool_ReconnectEdgeDescription.setter
    def viewpoint_tool_ReconnectEdgeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ReconnectEdgeDescription__viewpoint_tool_ReconnectEdgeDescription", None)
        self.__viewpoint_tool_ReconnectEdgeDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SourceEdgeCreationVariable690"):
                opp_val = getattr(old_value, "tool_SourceEdgeCreationVariable690", None)
                if opp_val == self:
                    setattr(old_value, "tool_SourceEdgeCreationVariable690", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SourceEdgeCreationVariable690"):
                opp_val = getattr(value, "tool_SourceEdgeCreationVariable690", None)
                setattr(value, "tool_SourceEdgeCreationVariable690", self)

    @property
    def viewpoint_tool_ReconnectEdgeDescription692(self):
        return self.__viewpoint_tool_ReconnectEdgeDescription692

    @viewpoint_tool_ReconnectEdgeDescription692.setter
    def viewpoint_tool_ReconnectEdgeDescription692(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ReconnectEdgeDescription__viewpoint_tool_ReconnectEdgeDescription692", None)
        self.__viewpoint_tool_ReconnectEdgeDescription692 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_TargetEdgeCreationVariable693"):
                opp_val = getattr(old_value, "tool_TargetEdgeCreationVariable693", None)
                if opp_val == self:
                    setattr(old_value, "tool_TargetEdgeCreationVariable693", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_TargetEdgeCreationVariable693"):
                opp_val = getattr(value, "tool_TargetEdgeCreationVariable693", None)
                setattr(value, "tool_TargetEdgeCreationVariable693", self)

    @property
    def viewpoint_tool_ReconnectEdgeDescription695(self):
        return self.__viewpoint_tool_ReconnectEdgeDescription695

    @viewpoint_tool_ReconnectEdgeDescription695.setter
    def viewpoint_tool_ReconnectEdgeDescription695(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ReconnectEdgeDescription__viewpoint_tool_ReconnectEdgeDescription695", None)
        self.__viewpoint_tool_ReconnectEdgeDescription695 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SourceEdgeViewCreationVariable696"):
                opp_val = getattr(old_value, "tool_SourceEdgeViewCreationVariable696", None)
                if opp_val == self:
                    setattr(old_value, "tool_SourceEdgeViewCreationVariable696", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SourceEdgeViewCreationVariable696"):
                opp_val = getattr(value, "tool_SourceEdgeViewCreationVariable696", None)
                setattr(value, "tool_SourceEdgeViewCreationVariable696", self)

    @property
    def viewpoint_tool_ReconnectEdgeDescription704(self):
        return self.__viewpoint_tool_ReconnectEdgeDescription704

    @viewpoint_tool_ReconnectEdgeDescription704.setter
    def viewpoint_tool_ReconnectEdgeDescription704(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ReconnectEdgeDescription__viewpoint_tool_ReconnectEdgeDescription704", None)
        self.__viewpoint_tool_ReconnectEdgeDescription704 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation705"):
                opp_val = getattr(old_value, "tool_InitialOperation705", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation705", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation705"):
                opp_val = getattr(value, "tool_InitialOperation705", None)
                setattr(value, "tool_InitialOperation705", self)

    def getMappings(self) :
        # TODO: Implement getMappings method
        pass

class viewpoint_tool_EdgeCreationDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, connectionStartPrecondition: str, viewpoint_tool_EdgeCreationDescription647: "tool_InitEdgeCreationOperation" = None, viewpoint_tool_EdgeCreationDescription639: "tool_SourceEdgeCreationVariable" = None, viewpoint_tool_EdgeCreationDescription641: "tool_TargetEdgeCreationVariable" = None, viewpoint_tool_EdgeCreationDescription643: "tool_SourceEdgeViewCreationVariable" = None, viewpoint_tool_EdgeCreationDescription645: "tool_TargetEdgeViewCreationVariable" = None, viewpoint_tool_EdgeCreationDescription649: set["description_DiagramElementMapping"] = None, viewpoint_tool_EdgeCreationDescription652: set["description_DiagramElementMapping"] = None, viewpoint_tool_EdgeCreationDescription: set["description_EdgeMapping"] = None):
        self.iconPath = iconPath
        self.connectionStartPrecondition = connectionStartPrecondition
        self.viewpoint_tool_EdgeCreationDescription647 = viewpoint_tool_EdgeCreationDescription647
        self.viewpoint_tool_EdgeCreationDescription639 = viewpoint_tool_EdgeCreationDescription639
        self.viewpoint_tool_EdgeCreationDescription641 = viewpoint_tool_EdgeCreationDescription641
        self.viewpoint_tool_EdgeCreationDescription643 = viewpoint_tool_EdgeCreationDescription643
        self.viewpoint_tool_EdgeCreationDescription645 = viewpoint_tool_EdgeCreationDescription645
        self.viewpoint_tool_EdgeCreationDescription649 = viewpoint_tool_EdgeCreationDescription649 if viewpoint_tool_EdgeCreationDescription649 is not None else set()
        self.viewpoint_tool_EdgeCreationDescription652 = viewpoint_tool_EdgeCreationDescription652 if viewpoint_tool_EdgeCreationDescription652 is not None else set()
        self.viewpoint_tool_EdgeCreationDescription = viewpoint_tool_EdgeCreationDescription if viewpoint_tool_EdgeCreationDescription is not None else set()
        
        pass
    @property
    def iconPath(self):
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath


    @property
    def connectionStartPrecondition(self):
        return self.__connectionStartPrecondition

    @connectionStartPrecondition.setter
    def connectionStartPrecondition(self, connectionStartPrecondition: str):
        self.__connectionStartPrecondition = connectionStartPrecondition


    @property
    def viewpoint_tool_EdgeCreationDescription(self):
        return self.__viewpoint_tool_EdgeCreationDescription

    @viewpoint_tool_EdgeCreationDescription.setter
    def viewpoint_tool_EdgeCreationDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_EdgeCreationDescription__viewpoint_tool_EdgeCreationDescription", None)
        self.__viewpoint_tool_EdgeCreationDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_EdgeMapping637"):
                    opp_val = getattr(item, "description_EdgeMapping637", None)
                    
                    if opp_val == self:
                        setattr(item, "description_EdgeMapping637", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_EdgeMapping637"):
                    opp_val = getattr(item, "description_EdgeMapping637", None)
                    
                    setattr(item, "description_EdgeMapping637", self)
                    

    @property
    def viewpoint_tool_EdgeCreationDescription652(self):
        return self.__viewpoint_tool_EdgeCreationDescription652

    @viewpoint_tool_EdgeCreationDescription652.setter
    def viewpoint_tool_EdgeCreationDescription652(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_EdgeCreationDescription__viewpoint_tool_EdgeCreationDescription652", None)
        self.__viewpoint_tool_EdgeCreationDescription652 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_DiagramElementMapping653"):
                    opp_val = getattr(item, "description_DiagramElementMapping653", None)
                    
                    if opp_val == self:
                        setattr(item, "description_DiagramElementMapping653", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_DiagramElementMapping653"):
                    opp_val = getattr(item, "description_DiagramElementMapping653", None)
                    
                    setattr(item, "description_DiagramElementMapping653", self)
                    

    @property
    def viewpoint_tool_EdgeCreationDescription639(self):
        return self.__viewpoint_tool_EdgeCreationDescription639

    @viewpoint_tool_EdgeCreationDescription639.setter
    def viewpoint_tool_EdgeCreationDescription639(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_EdgeCreationDescription__viewpoint_tool_EdgeCreationDescription639", None)
        self.__viewpoint_tool_EdgeCreationDescription639 = value
        
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
    def viewpoint_tool_EdgeCreationDescription641(self):
        return self.__viewpoint_tool_EdgeCreationDescription641

    @viewpoint_tool_EdgeCreationDescription641.setter
    def viewpoint_tool_EdgeCreationDescription641(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_EdgeCreationDescription__viewpoint_tool_EdgeCreationDescription641", None)
        self.__viewpoint_tool_EdgeCreationDescription641 = value
        
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
    def viewpoint_tool_EdgeCreationDescription647(self):
        return self.__viewpoint_tool_EdgeCreationDescription647

    @viewpoint_tool_EdgeCreationDescription647.setter
    def viewpoint_tool_EdgeCreationDescription647(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_EdgeCreationDescription__viewpoint_tool_EdgeCreationDescription647", None)
        self.__viewpoint_tool_EdgeCreationDescription647 = value
        
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
    def viewpoint_tool_EdgeCreationDescription649(self):
        return self.__viewpoint_tool_EdgeCreationDescription649

    @viewpoint_tool_EdgeCreationDescription649.setter
    def viewpoint_tool_EdgeCreationDescription649(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_EdgeCreationDescription__viewpoint_tool_EdgeCreationDescription649", None)
        self.__viewpoint_tool_EdgeCreationDescription649 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_DiagramElementMapping650"):
                    opp_val = getattr(item, "description_DiagramElementMapping650", None)
                    
                    if opp_val == self:
                        setattr(item, "description_DiagramElementMapping650", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_DiagramElementMapping650"):
                    opp_val = getattr(item, "description_DiagramElementMapping650", None)
                    
                    setattr(item, "description_DiagramElementMapping650", self)
                    

    @property
    def viewpoint_tool_EdgeCreationDescription643(self):
        return self.__viewpoint_tool_EdgeCreationDescription643

    @viewpoint_tool_EdgeCreationDescription643.setter
    def viewpoint_tool_EdgeCreationDescription643(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_EdgeCreationDescription__viewpoint_tool_EdgeCreationDescription643", None)
        self.__viewpoint_tool_EdgeCreationDescription643 = value
        
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
    def viewpoint_tool_EdgeCreationDescription645(self):
        return self.__viewpoint_tool_EdgeCreationDescription645

    @viewpoint_tool_EdgeCreationDescription645.setter
    def viewpoint_tool_EdgeCreationDescription645(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_EdgeCreationDescription__viewpoint_tool_EdgeCreationDescription645", None)
        self.__viewpoint_tool_EdgeCreationDescription645 = value
        
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

    def getBestMapping(self, viewpoint_target, viewpoint_createdElements, viewpoint_source) :
        # TODO: Implement getBestMapping method
        pass

class viewpoint_tool_DirectEditLabel(MappingBasedToolDescription):

    def __init__(self, inputLabelExpression: str, viewpoint_tool_DirectEditLabel: "tool_EditMaskVariables" = None, viewpoint_tool_DirectEditLabel711: "tool_InitialOperation" = None):
        self.inputLabelExpression = inputLabelExpression
        self.viewpoint_tool_DirectEditLabel = viewpoint_tool_DirectEditLabel
        self.viewpoint_tool_DirectEditLabel711 = viewpoint_tool_DirectEditLabel711
        
        pass
    @property
    def inputLabelExpression(self):
        return self.__inputLabelExpression

    @inputLabelExpression.setter
    def inputLabelExpression(self, inputLabelExpression: str):
        self.__inputLabelExpression = inputLabelExpression


    @property
    def viewpoint_tool_DirectEditLabel(self):
        return self.__viewpoint_tool_DirectEditLabel

    @viewpoint_tool_DirectEditLabel.setter
    def viewpoint_tool_DirectEditLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_DirectEditLabel__viewpoint_tool_DirectEditLabel", None)
        self.__viewpoint_tool_DirectEditLabel = value
        
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
    def viewpoint_tool_DirectEditLabel711(self):
        return self.__viewpoint_tool_DirectEditLabel711

    @viewpoint_tool_DirectEditLabel711.setter
    def viewpoint_tool_DirectEditLabel711(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_DirectEditLabel__viewpoint_tool_DirectEditLabel711", None)
        self.__viewpoint_tool_DirectEditLabel711 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation712"):
                opp_val = getattr(old_value, "tool_InitialOperation712", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation712", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation712"):
                opp_val = getattr(value, "tool_InitialOperation712", None)
                setattr(value, "tool_InitialOperation712", self)

    def getMapping(self) :
        # TODO: Implement getMapping method
        pass

class viewpoint_tool_DoubleClickDescription(MappingBasedToolDescription):

    pass
class viewpoint_tool_DeleteElementDescription(MappingBasedToolDescription):

    def __init__(self, viewpoint_tool_DeleteElementDescription: "tool_ElementDeleteVariable" = None, viewpoint_tool_DeleteElementDescription670: "tool_ElementDeleteVariable" = None, viewpoint_tool_DeleteElementDescription673: "tool_ContainerViewVariable" = None, viewpoint_tool_DeleteElementDescription676: "tool_InitialOperation" = None, viewpoint_tool_DeleteElementDescription679: "tool_DeleteHook" = None):
        self.viewpoint_tool_DeleteElementDescription = viewpoint_tool_DeleteElementDescription
        self.viewpoint_tool_DeleteElementDescription670 = viewpoint_tool_DeleteElementDescription670
        self.viewpoint_tool_DeleteElementDescription673 = viewpoint_tool_DeleteElementDescription673
        self.viewpoint_tool_DeleteElementDescription676 = viewpoint_tool_DeleteElementDescription676
        self.viewpoint_tool_DeleteElementDescription679 = viewpoint_tool_DeleteElementDescription679
        
        pass
    @property
    def viewpoint_tool_DeleteElementDescription676(self):
        return self.__viewpoint_tool_DeleteElementDescription676

    @viewpoint_tool_DeleteElementDescription676.setter
    def viewpoint_tool_DeleteElementDescription676(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_DeleteElementDescription__viewpoint_tool_DeleteElementDescription676", None)
        self.__viewpoint_tool_DeleteElementDescription676 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation677"):
                opp_val = getattr(old_value, "tool_InitialOperation677", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation677", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation677"):
                opp_val = getattr(value, "tool_InitialOperation677", None)
                setattr(value, "tool_InitialOperation677", self)

    @property
    def viewpoint_tool_DeleteElementDescription670(self):
        return self.__viewpoint_tool_DeleteElementDescription670

    @viewpoint_tool_DeleteElementDescription670.setter
    def viewpoint_tool_DeleteElementDescription670(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_DeleteElementDescription__viewpoint_tool_DeleteElementDescription670", None)
        self.__viewpoint_tool_DeleteElementDescription670 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementDeleteVariable671"):
                opp_val = getattr(old_value, "tool_ElementDeleteVariable671", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementDeleteVariable671", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementDeleteVariable671"):
                opp_val = getattr(value, "tool_ElementDeleteVariable671", None)
                setattr(value, "tool_ElementDeleteVariable671", self)

    @property
    def viewpoint_tool_DeleteElementDescription679(self):
        return self.__viewpoint_tool_DeleteElementDescription679

    @viewpoint_tool_DeleteElementDescription679.setter
    def viewpoint_tool_DeleteElementDescription679(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_DeleteElementDescription__viewpoint_tool_DeleteElementDescription679", None)
        self.__viewpoint_tool_DeleteElementDescription679 = value
        
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
    def viewpoint_tool_DeleteElementDescription673(self):
        return self.__viewpoint_tool_DeleteElementDescription673

    @viewpoint_tool_DeleteElementDescription673.setter
    def viewpoint_tool_DeleteElementDescription673(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_DeleteElementDescription__viewpoint_tool_DeleteElementDescription673", None)
        self.__viewpoint_tool_DeleteElementDescription673 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable674"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable674", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable674", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable674"):
                opp_val = getattr(value, "tool_ContainerViewVariable674", None)
                setattr(value, "tool_ContainerViewVariable674", self)

    @property
    def viewpoint_tool_DeleteElementDescription(self):
        return self.__viewpoint_tool_DeleteElementDescription

    @viewpoint_tool_DeleteElementDescription.setter
    def viewpoint_tool_DeleteElementDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_DeleteElementDescription__viewpoint_tool_DeleteElementDescription", None)
        self.__viewpoint_tool_DeleteElementDescription = value
        
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

    def getMappings(self) :
        # TODO: Implement getMappings method
        pass

class viewpoint_tool_ToolDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, viewpoint_tool_ToolDescription: "tool_ElementVariable" = None, viewpoint_tool_ToolDescription128: "tool_ElementViewVariable" = None, viewpoint_tool_ToolDescription130: "tool_InitialOperation" = None):
        self.iconPath = iconPath
        self.viewpoint_tool_ToolDescription = viewpoint_tool_ToolDescription
        self.viewpoint_tool_ToolDescription128 = viewpoint_tool_ToolDescription128
        self.viewpoint_tool_ToolDescription130 = viewpoint_tool_ToolDescription130
        
        pass
    @property
    def iconPath(self):
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath


    @property
    def viewpoint_tool_ToolDescription(self):
        return self.__viewpoint_tool_ToolDescription

    @viewpoint_tool_ToolDescription.setter
    def viewpoint_tool_ToolDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolDescription__viewpoint_tool_ToolDescription", None)
        self.__viewpoint_tool_ToolDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementVariable"):
                opp_val = getattr(old_value, "tool_ElementVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementVariable"):
                opp_val = getattr(value, "tool_ElementVariable", None)
                setattr(value, "tool_ElementVariable", self)

    @property
    def viewpoint_tool_ToolDescription130(self):
        return self.__viewpoint_tool_ToolDescription130

    @viewpoint_tool_ToolDescription130.setter
    def viewpoint_tool_ToolDescription130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolDescription__viewpoint_tool_ToolDescription130", None)
        self.__viewpoint_tool_ToolDescription130 = value
        
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
    def viewpoint_tool_ToolDescription128(self):
        return self.__viewpoint_tool_ToolDescription128

    @viewpoint_tool_ToolDescription128.setter
    def viewpoint_tool_ToolDescription128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolDescription__viewpoint_tool_ToolDescription128", None)
        self.__viewpoint_tool_ToolDescription128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementViewVariable"):
                opp_val = getattr(old_value, "tool_ElementViewVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementViewVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementViewVariable"):
                opp_val = getattr(value, "tool_ElementViewVariable", None)
                setattr(value, "tool_ElementViewVariable", self)

class AbstractToolDescription:

    pass
class viewpoint_tool_PopupMenu(AbstractToolDescription):

    pass
class viewpoint_tool_BehaviorTool(AbstractToolDescription):

    def __init__(self, domainClass: str, viewpoint_tool_BehaviorTool: "tool_InitialOperation" = None):
        self.domainClass = domainClass
        self.viewpoint_tool_BehaviorTool = viewpoint_tool_BehaviorTool
        
        pass
    @property
    def domainClass(self):
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass


    @property
    def viewpoint_tool_BehaviorTool(self):
        return self.__viewpoint_tool_BehaviorTool

    @viewpoint_tool_BehaviorTool.setter
    def viewpoint_tool_BehaviorTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_BehaviorTool__viewpoint_tool_BehaviorTool", None)
        self.__viewpoint_tool_BehaviorTool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation714"):
                opp_val = getattr(old_value, "tool_InitialOperation714", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation714", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation714"):
                opp_val = getattr(value, "tool_InitialOperation714", None)
                setattr(value, "tool_InitialOperation714", self)

class viewpoint_tool_RepresentationCreationDescription(AbstractToolDescription):

    def __init__(self, titleExpression: str, browseExpression: str, viewpoint_tool_RepresentationCreationDescription: "RepresentationDescription" = None, viewpoint_tool_RepresentationCreationDescription180: "tool_InitialOperation" = None, viewpoint_tool_RepresentationCreationDescription183: "tool_ContainerViewVariable" = None, viewpoint_tool_RepresentationCreationDescription186: "tool_NameVariable" = None):
        self.titleExpression = titleExpression
        self.browseExpression = browseExpression
        self.viewpoint_tool_RepresentationCreationDescription = viewpoint_tool_RepresentationCreationDescription
        self.viewpoint_tool_RepresentationCreationDescription180 = viewpoint_tool_RepresentationCreationDescription180
        self.viewpoint_tool_RepresentationCreationDescription183 = viewpoint_tool_RepresentationCreationDescription183
        self.viewpoint_tool_RepresentationCreationDescription186 = viewpoint_tool_RepresentationCreationDescription186
        
        pass
    @property
    def titleExpression(self):
        return self.__titleExpression

    @titleExpression.setter
    def titleExpression(self, titleExpression: str):
        self.__titleExpression = titleExpression


    @property
    def browseExpression(self):
        return self.__browseExpression

    @browseExpression.setter
    def browseExpression(self, browseExpression: str):
        self.__browseExpression = browseExpression


    @property
    def viewpoint_tool_RepresentationCreationDescription186(self):
        return self.__viewpoint_tool_RepresentationCreationDescription186

    @viewpoint_tool_RepresentationCreationDescription186.setter
    def viewpoint_tool_RepresentationCreationDescription186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationCreationDescription__viewpoint_tool_RepresentationCreationDescription186", None)
        self.__viewpoint_tool_RepresentationCreationDescription186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_NameVariable"):
                opp_val = getattr(old_value, "tool_NameVariable", None)
                if opp_val == self:
                    setattr(old_value, "tool_NameVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_NameVariable"):
                opp_val = getattr(value, "tool_NameVariable", None)
                setattr(value, "tool_NameVariable", self)

    @property
    def viewpoint_tool_RepresentationCreationDescription(self):
        return self.__viewpoint_tool_RepresentationCreationDescription

    @viewpoint_tool_RepresentationCreationDescription.setter
    def viewpoint_tool_RepresentationCreationDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationCreationDescription__viewpoint_tool_RepresentationCreationDescription", None)
        self.__viewpoint_tool_RepresentationCreationDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepresentationDescription178"):
                opp_val = getattr(old_value, "RepresentationDescription178", None)
                if opp_val == self:
                    setattr(old_value, "RepresentationDescription178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentationDescription178"):
                opp_val = getattr(value, "RepresentationDescription178", None)
                setattr(value, "RepresentationDescription178", self)

    @property
    def viewpoint_tool_RepresentationCreationDescription183(self):
        return self.__viewpoint_tool_RepresentationCreationDescription183

    @viewpoint_tool_RepresentationCreationDescription183.setter
    def viewpoint_tool_RepresentationCreationDescription183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationCreationDescription__viewpoint_tool_RepresentationCreationDescription183", None)
        self.__viewpoint_tool_RepresentationCreationDescription183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable184"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable184", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable184"):
                opp_val = getattr(value, "tool_ContainerViewVariable184", None)
                setattr(value, "tool_ContainerViewVariable184", self)

    @property
    def viewpoint_tool_RepresentationCreationDescription180(self):
        return self.__viewpoint_tool_RepresentationCreationDescription180

    @viewpoint_tool_RepresentationCreationDescription180.setter
    def viewpoint_tool_RepresentationCreationDescription180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationCreationDescription__viewpoint_tool_RepresentationCreationDescription180", None)
        self.__viewpoint_tool_RepresentationCreationDescription180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation181"):
                opp_val = getattr(old_value, "tool_InitialOperation181", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation181"):
                opp_val = getattr(value, "tool_InitialOperation181", None)
                setattr(value, "tool_InitialOperation181", self)

    def getMappings(self) :
        # TODO: Implement getMappings method
        pass

class viewpoint_tool_RepresentationNavigationDescription(AbstractToolDescription):

    def __init__(self, browseExpression: str, navigationNameExpression: str, viewpoint_tool_RepresentationNavigationDescription: "RepresentationDescription" = None, viewpoint_tool_RepresentationNavigationDescription190: "tool_ContainerViewVariable" = None, viewpoint_tool_RepresentationNavigationDescription193: "tool_ElementSelectVariable" = None, viewpoint_tool_RepresentationNavigationDescription196: "tool_NameVariable" = None):
        self.browseExpression = browseExpression
        self.navigationNameExpression = navigationNameExpression
        self.viewpoint_tool_RepresentationNavigationDescription = viewpoint_tool_RepresentationNavigationDescription
        self.viewpoint_tool_RepresentationNavigationDescription190 = viewpoint_tool_RepresentationNavigationDescription190
        self.viewpoint_tool_RepresentationNavigationDescription193 = viewpoint_tool_RepresentationNavigationDescription193
        self.viewpoint_tool_RepresentationNavigationDescription196 = viewpoint_tool_RepresentationNavigationDescription196
        
        pass
    @property
    def navigationNameExpression(self):
        return self.__navigationNameExpression

    @navigationNameExpression.setter
    def navigationNameExpression(self, navigationNameExpression: str):
        self.__navigationNameExpression = navigationNameExpression


    @property
    def browseExpression(self):
        return self.__browseExpression

    @browseExpression.setter
    def browseExpression(self, browseExpression: str):
        self.__browseExpression = browseExpression


    @property
    def viewpoint_tool_RepresentationNavigationDescription193(self):
        return self.__viewpoint_tool_RepresentationNavigationDescription193

    @viewpoint_tool_RepresentationNavigationDescription193.setter
    def viewpoint_tool_RepresentationNavigationDescription193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationNavigationDescription__viewpoint_tool_RepresentationNavigationDescription193", None)
        self.__viewpoint_tool_RepresentationNavigationDescription193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementSelectVariable194"):
                opp_val = getattr(old_value, "tool_ElementSelectVariable194", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementSelectVariable194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementSelectVariable194"):
                opp_val = getattr(value, "tool_ElementSelectVariable194", None)
                setattr(value, "tool_ElementSelectVariable194", self)

    @property
    def viewpoint_tool_RepresentationNavigationDescription190(self):
        return self.__viewpoint_tool_RepresentationNavigationDescription190

    @viewpoint_tool_RepresentationNavigationDescription190.setter
    def viewpoint_tool_RepresentationNavigationDescription190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationNavigationDescription__viewpoint_tool_RepresentationNavigationDescription190", None)
        self.__viewpoint_tool_RepresentationNavigationDescription190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable191"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable191", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable191"):
                opp_val = getattr(value, "tool_ContainerViewVariable191", None)
                setattr(value, "tool_ContainerViewVariable191", self)

    @property
    def viewpoint_tool_RepresentationNavigationDescription196(self):
        return self.__viewpoint_tool_RepresentationNavigationDescription196

    @viewpoint_tool_RepresentationNavigationDescription196.setter
    def viewpoint_tool_RepresentationNavigationDescription196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationNavigationDescription__viewpoint_tool_RepresentationNavigationDescription196", None)
        self.__viewpoint_tool_RepresentationNavigationDescription196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_NameVariable197"):
                opp_val = getattr(old_value, "tool_NameVariable197", None)
                if opp_val == self:
                    setattr(old_value, "tool_NameVariable197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_NameVariable197"):
                opp_val = getattr(value, "tool_NameVariable197", None)
                setattr(value, "tool_NameVariable197", self)

    @property
    def viewpoint_tool_RepresentationNavigationDescription(self):
        return self.__viewpoint_tool_RepresentationNavigationDescription

    @viewpoint_tool_RepresentationNavigationDescription.setter
    def viewpoint_tool_RepresentationNavigationDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationNavigationDescription__viewpoint_tool_RepresentationNavigationDescription", None)
        self.__viewpoint_tool_RepresentationNavigationDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepresentationDescription188"):
                opp_val = getattr(old_value, "RepresentationDescription188", None)
                if opp_val == self:
                    setattr(old_value, "RepresentationDescription188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentationDescription188"):
                opp_val = getattr(value, "RepresentationDescription188", None)
                setattr(value, "RepresentationDescription188", self)

    def getMappings(self) :
        # TODO: Implement getMappings method
        pass

class viewpoint_tool_RequestDescription(AbstractToolDescription):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class viewpoint_tool_PaneBasedSelectionWizardDescription(AbstractToolDescription):

    def __init__(self, tree: bool, iconPath: str, windowTitle: str, windowImagePath: str, message: str, choiceOfValuesMessage: str, candidatesExpression: str, rootExpression: str, childrenExpression: str, selectedValuesMessage: str, preSelectedCandidatesExpression: str, viewpoint_tool_PaneBasedSelectionWizardDescription: "tool_ElementSelectVariable" = None, viewpoint_tool_PaneBasedSelectionWizardDescription169: "tool_ContainerViewVariable" = None, viewpoint_tool_PaneBasedSelectionWizardDescription172: "tool_SelectContainerVariable" = None, viewpoint_tool_PaneBasedSelectionWizardDescription175: "tool_InitialOperation" = None):
        self.tree = tree
        self.iconPath = iconPath
        self.windowTitle = windowTitle
        self.windowImagePath = windowImagePath
        self.message = message
        self.choiceOfValuesMessage = choiceOfValuesMessage
        self.candidatesExpression = candidatesExpression
        self.rootExpression = rootExpression
        self.childrenExpression = childrenExpression
        self.selectedValuesMessage = selectedValuesMessage
        self.preSelectedCandidatesExpression = preSelectedCandidatesExpression
        self.viewpoint_tool_PaneBasedSelectionWizardDescription = viewpoint_tool_PaneBasedSelectionWizardDescription
        self.viewpoint_tool_PaneBasedSelectionWizardDescription169 = viewpoint_tool_PaneBasedSelectionWizardDescription169
        self.viewpoint_tool_PaneBasedSelectionWizardDescription172 = viewpoint_tool_PaneBasedSelectionWizardDescription172
        self.viewpoint_tool_PaneBasedSelectionWizardDescription175 = viewpoint_tool_PaneBasedSelectionWizardDescription175
        
        pass
    @property
    def preSelectedCandidatesExpression(self):
        return self.__preSelectedCandidatesExpression

    @preSelectedCandidatesExpression.setter
    def preSelectedCandidatesExpression(self, preSelectedCandidatesExpression: str):
        self.__preSelectedCandidatesExpression = preSelectedCandidatesExpression


    @property
    def candidatesExpression(self):
        return self.__candidatesExpression

    @candidatesExpression.setter
    def candidatesExpression(self, candidatesExpression: str):
        self.__candidatesExpression = candidatesExpression


    @property
    def windowTitle(self):
        return self.__windowTitle

    @windowTitle.setter
    def windowTitle(self, windowTitle: str):
        self.__windowTitle = windowTitle


    @property
    def choiceOfValuesMessage(self):
        return self.__choiceOfValuesMessage

    @choiceOfValuesMessage.setter
    def choiceOfValuesMessage(self, choiceOfValuesMessage: str):
        self.__choiceOfValuesMessage = choiceOfValuesMessage


    @property
    def selectedValuesMessage(self):
        return self.__selectedValuesMessage

    @selectedValuesMessage.setter
    def selectedValuesMessage(self, selectedValuesMessage: str):
        self.__selectedValuesMessage = selectedValuesMessage


    @property
    def windowImagePath(self):
        return self.__windowImagePath

    @windowImagePath.setter
    def windowImagePath(self, windowImagePath: str):
        self.__windowImagePath = windowImagePath


    @property
    def iconPath(self):
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath


    @property
    def tree(self):
        return self.__tree

    @tree.setter
    def tree(self, tree: bool):
        self.__tree = tree


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def childrenExpression(self):
        return self.__childrenExpression

    @childrenExpression.setter
    def childrenExpression(self, childrenExpression: str):
        self.__childrenExpression = childrenExpression


    @property
    def rootExpression(self):
        return self.__rootExpression

    @rootExpression.setter
    def rootExpression(self, rootExpression: str):
        self.__rootExpression = rootExpression


    @property
    def viewpoint_tool_PaneBasedSelectionWizardDescription169(self):
        return self.__viewpoint_tool_PaneBasedSelectionWizardDescription169

    @viewpoint_tool_PaneBasedSelectionWizardDescription169.setter
    def viewpoint_tool_PaneBasedSelectionWizardDescription169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PaneBasedSelectionWizardDescription__viewpoint_tool_PaneBasedSelectionWizardDescription169", None)
        self.__viewpoint_tool_PaneBasedSelectionWizardDescription169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable170"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable170", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable170"):
                opp_val = getattr(value, "tool_ContainerViewVariable170", None)
                setattr(value, "tool_ContainerViewVariable170", self)

    @property
    def viewpoint_tool_PaneBasedSelectionWizardDescription172(self):
        return self.__viewpoint_tool_PaneBasedSelectionWizardDescription172

    @viewpoint_tool_PaneBasedSelectionWizardDescription172.setter
    def viewpoint_tool_PaneBasedSelectionWizardDescription172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PaneBasedSelectionWizardDescription__viewpoint_tool_PaneBasedSelectionWizardDescription172", None)
        self.__viewpoint_tool_PaneBasedSelectionWizardDescription172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SelectContainerVariable173"):
                opp_val = getattr(old_value, "tool_SelectContainerVariable173", None)
                if opp_val == self:
                    setattr(old_value, "tool_SelectContainerVariable173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SelectContainerVariable173"):
                opp_val = getattr(value, "tool_SelectContainerVariable173", None)
                setattr(value, "tool_SelectContainerVariable173", self)

    @property
    def viewpoint_tool_PaneBasedSelectionWizardDescription(self):
        return self.__viewpoint_tool_PaneBasedSelectionWizardDescription

    @viewpoint_tool_PaneBasedSelectionWizardDescription.setter
    def viewpoint_tool_PaneBasedSelectionWizardDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PaneBasedSelectionWizardDescription__viewpoint_tool_PaneBasedSelectionWizardDescription", None)
        self.__viewpoint_tool_PaneBasedSelectionWizardDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementSelectVariable167"):
                opp_val = getattr(old_value, "tool_ElementSelectVariable167", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementSelectVariable167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementSelectVariable167"):
                opp_val = getattr(value, "tool_ElementSelectVariable167", None)
                setattr(value, "tool_ElementSelectVariable167", self)

    @property
    def viewpoint_tool_PaneBasedSelectionWizardDescription175(self):
        return self.__viewpoint_tool_PaneBasedSelectionWizardDescription175

    @viewpoint_tool_PaneBasedSelectionWizardDescription175.setter
    def viewpoint_tool_PaneBasedSelectionWizardDescription175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PaneBasedSelectionWizardDescription__viewpoint_tool_PaneBasedSelectionWizardDescription175", None)
        self.__viewpoint_tool_PaneBasedSelectionWizardDescription175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation176"):
                opp_val = getattr(old_value, "tool_InitialOperation176", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation176"):
                opp_val = getattr(value, "tool_InitialOperation176", None)
                setattr(value, "tool_InitialOperation176", self)

class viewpoint_tool_MappingBasedToolDescription(AbstractToolDescription):

    pass
class tool_ElementDropVariable:

    pass
class tool_ToolFilterDescription:

    pass
class ToolEntry:

    pass
class viewpoint_tool_ToolGroup(ToolEntry):

    pass
class viewpoint_tool_AbstractToolDescription(ToolEntry):

    def __init__(self, precondition: str, forceRefresh: bool, viewpoint_tool_AbstractToolDescription: set["tool_ToolFilterDescription"] = None):
        self.precondition = precondition
        self.forceRefresh = forceRefresh
        self.viewpoint_tool_AbstractToolDescription = viewpoint_tool_AbstractToolDescription if viewpoint_tool_AbstractToolDescription is not None else set()
        
        pass
    @property
    def forceRefresh(self):
        return self.__forceRefresh

    @forceRefresh.setter
    def forceRefresh(self, forceRefresh: bool):
        self.__forceRefresh = forceRefresh


    @property
    def precondition(self):
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition


    @property
    def viewpoint_tool_AbstractToolDescription(self):
        return self.__viewpoint_tool_AbstractToolDescription

    @viewpoint_tool_AbstractToolDescription.setter
    def viewpoint_tool_AbstractToolDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_AbstractToolDescription__viewpoint_tool_AbstractToolDescription", None)
        self.__viewpoint_tool_AbstractToolDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolFilterDescription"):
                    opp_val = getattr(item, "tool_ToolFilterDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolFilterDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolFilterDescription"):
                    opp_val = getattr(item, "tool_ToolFilterDescription", None)
                    
                    setattr(item, "tool_ToolFilterDescription", self)
                    

class viewpoint_style_TooltipStyleDescription:

    def __init__(self, tooltipExpression: str):
        self.tooltipExpression = tooltipExpression
        
        pass
    @property
    def tooltipExpression(self):
        return self.__tooltipExpression

    @tooltipExpression.setter
    def tooltipExpression(self, tooltipExpression: str):
        self.__tooltipExpression = tooltipExpression


class viewpoint_style_LabelBorderStyleDescription:

    def __init__(self, id: str, name: str, cornerHeight: int, cornerWidth: int):
        self.id = id
        self.name = name
        self.cornerHeight = cornerHeight
        self.cornerWidth = cornerWidth
        
        pass
    @property
    def cornerHeight(self):
        return self.__cornerHeight

    @cornerHeight.setter
    def cornerHeight(self, cornerHeight: int):
        self.__cornerHeight = cornerHeight


    @property
    def cornerWidth(self):
        return self.__cornerWidth

    @cornerWidth.setter
    def cornerWidth(self, cornerWidth: int):
        self.__cornerWidth = cornerWidth


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class style_LabelBorderStyleDescription:

    pass
class viewpoint_style_LabelBorderStyles:

    pass
class BasicLabelStyleDescription:

    pass
class viewpoint_style_CenterLabelStyleDescription(BasicLabelStyleDescription):

    pass
class viewpoint_style_EndLabelStyleDescription(BasicLabelStyleDescription):

    pass
class viewpoint_style_BeginLabelStyleDescription(BasicLabelStyleDescription):

    pass
class viewpoint_style_LabelStyleDescription(BasicLabelStyleDescription):

    def __init__(self, labelAlignment: str):
        self.labelAlignment = labelAlignment
        
        pass
    @property
    def labelAlignment(self):
        return self.__labelAlignment

    @labelAlignment.setter
    def labelAlignment(self, labelAlignment: str):
        self.__labelAlignment = labelAlignment


class viewpoint_style_BasicLabelStyleDescription:

    def __init__(self, iconPath: str, labelSize: int, labelFormat: str, showIcon: bool, labelExpression: str, viewpoint_style_BasicLabelStyleDescription: "ColorDescription" = None):
        self.iconPath = iconPath
        self.labelSize = labelSize
        self.labelFormat = labelFormat
        self.showIcon = showIcon
        self.labelExpression = labelExpression
        self.viewpoint_style_BasicLabelStyleDescription = viewpoint_style_BasicLabelStyleDescription
        
        pass
    @property
    def labelSize(self):
        return self.__labelSize

    @labelSize.setter
    def labelSize(self, labelSize: int):
        self.__labelSize = labelSize


    @property
    def showIcon(self):
        return self.__showIcon

    @showIcon.setter
    def showIcon(self, showIcon: bool):
        self.__showIcon = showIcon


    @property
    def iconPath(self):
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath


    @property
    def labelFormat(self):
        return self.__labelFormat

    @labelFormat.setter
    def labelFormat(self, labelFormat: str):
        self.__labelFormat = labelFormat


    @property
    def labelExpression(self):
        return self.__labelExpression

    @labelExpression.setter
    def labelExpression(self, labelExpression: str):
        self.__labelExpression = labelExpression


    @property
    def viewpoint_style_BasicLabelStyleDescription(self):
        return self.__viewpoint_style_BasicLabelStyleDescription

    @viewpoint_style_BasicLabelStyleDescription.setter
    def viewpoint_style_BasicLabelStyleDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_style_BasicLabelStyleDescription__viewpoint_style_BasicLabelStyleDescription", None)
        self.__viewpoint_style_BasicLabelStyleDescription = value
        
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

class viewpoint_style_StyleDescription(ABC):

    pass
class viewpoint_description_DAnnotationEntry:

    def __init__(self, source: str, details: str):
        self.source = source
        self.details = details
        
        pass
    @property
    def details(self):
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


class viewpoint_description_IdentifiedElement:

    def __init__(self, name: str, label: str):
        self.name = name
        self.label = label
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


class viewpoint_description_EndUserDocumentedElement(ABC):

    def __init__(self, endUserDocumentation: str):
        self.endUserDocumentation = endUserDocumentation
        
        pass
    @property
    def endUserDocumentation(self):
        return self.__endUserDocumentation

    @endUserDocumentation.setter
    def endUserDocumentation(self, endUserDocumentation: str):
        self.__endUserDocumentation = endUserDocumentation


class viewpoint_description_AnnotationEntry:

    def __init__(self, source: str, viewpoint_description_AnnotationEntry: "description_viewpoint_EObject" = None):
        self.source = source
        self.viewpoint_description_AnnotationEntry = viewpoint_description_AnnotationEntry
        
        pass
    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def viewpoint_description_AnnotationEntry(self):
        return self.__viewpoint_description_AnnotationEntry

    @viewpoint_description_AnnotationEntry.setter
    def viewpoint_description_AnnotationEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_AnnotationEntry__viewpoint_description_AnnotationEntry", None)
        self.__viewpoint_description_AnnotationEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_viewpoint_EObject122"):
                opp_val = getattr(old_value, "description_viewpoint_EObject122", None)
                if opp_val == self:
                    setattr(old_value, "description_viewpoint_EObject122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_viewpoint_EObject122"):
                opp_val = getattr(value, "description_viewpoint_EObject122", None)
                setattr(value, "description_viewpoint_EObject122", self)

class UserColor:

    pass
class viewpoint_description_UserColorsPalette:

    def __init__(self, name: str, viewpoint_description_UserColorsPalette: set["UserColor"] = None):
        self.name = name
        self.viewpoint_description_UserColorsPalette = viewpoint_description_UserColorsPalette if viewpoint_description_UserColorsPalette is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def viewpoint_description_UserColorsPalette(self):
        return self.__viewpoint_description_UserColorsPalette

    @viewpoint_description_UserColorsPalette.setter
    def viewpoint_description_UserColorsPalette(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_UserColorsPalette__viewpoint_description_UserColorsPalette", None)
        self.__viewpoint_description_UserColorsPalette = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UserColor"):
                    opp_val = getattr(item, "UserColor", None)
                    
                    if opp_val == self:
                        setattr(item, "UserColor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UserColor"):
                    opp_val = getattr(item, "UserColor", None)
                    
                    setattr(item, "UserColor", self)
                    

class SystemColor:

    pass
class viewpoint_description_SytemColorsPalette:

    pass
class style_LabelBorderStyles:

    pass
class tool_ToolEntry:

    pass
class viewpoint_description_Environment:

    pass
class viewpoint_description_UserColor(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class description_FixedColor:

    pass
class ColorDescription:

    pass
class viewpoint_description_FixedColor(ColorDescription):

    def __init__(self, red: int, green: int, blue: int, ColorDescription: "viewpoint_style_BasicLabelStyleDescription" = None, ColorDescription584: "viewpoint_style_GaugeSectionDescription" = None, ColorDescription597: "viewpoint_style_ShapeContainerStyleDescription" = None, ColorDescription581: "viewpoint_style_DotDescription" = None, ColorDescription599: "viewpoint_style_EdgeStyleDescription" = None, ColorDescription577: "viewpoint_style_BundledImageDescription" = None, ColorDescription575: "viewpoint_style_EllipseNodeDescription" = None, ColorDescription579: "viewpoint_style_NoteDescription" = None, ColorDescription592: "viewpoint_style_FlatContainerStyleDescription" = None, ColorDescription573: "viewpoint_style_LozengeNodeDescription" = None, ColorDescription589: "viewpoint_style_FlatContainerStyleDescription" = None, ColorDescription571: "viewpoint_style_SquareDescription" = None, ColorDescription587: "viewpoint_style_GaugeSectionDescription" = None, ColorDescription569: "viewpoint_style_BorderedStyleDescription" = None):
        self.red = red
        self.green = green
        self.blue = blue
        
        pass
    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green


    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red


    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue


class viewpoint_description_ColorStep:

    def __init__(self, associatedValue: str, viewpoint_description_ColorStep: "FixedColor" = None):
        self.associatedValue = associatedValue
        self.viewpoint_description_ColorStep = viewpoint_description_ColorStep
        
        pass
    @property
    def associatedValue(self):
        return self.__associatedValue

    @associatedValue.setter
    def associatedValue(self, associatedValue: str):
        self.__associatedValue = associatedValue


    @property
    def viewpoint_description_ColorStep(self):
        return self.__viewpoint_description_ColorStep

    @viewpoint_description_ColorStep.setter
    def viewpoint_description_ColorStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_ColorStep__viewpoint_description_ColorStep", None)
        self.__viewpoint_description_ColorStep = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FixedColor"):
                opp_val = getattr(old_value, "FixedColor", None)
                if opp_val == self:
                    setattr(old_value, "FixedColor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FixedColor"):
                opp_val = getattr(value, "FixedColor", None)
                setattr(value, "FixedColor", self)

class ColorStep:

    pass
class description_ColorDescription:

    pass
class FixedColor:

    pass
class viewpoint_description_SystemColor(FixedColor):

    def __init__(self, name: str, FixedColor: "viewpoint_description_ColorStep" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class viewpoint_description_ColorDescription(ABC):

    pass
class viewpoint_description_SelectionDescription(ABC):

    def __init__(self, candidatesExpression: str, multiple: bool, tree: bool, rootExpression: str, childrenExpression: str, message: str):
        self.candidatesExpression = candidatesExpression
        self.multiple = multiple
        self.tree = tree
        self.rootExpression = rootExpression
        self.childrenExpression = childrenExpression
        self.message = message
        
        pass
    @property
    def multiple(self):
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def candidatesExpression(self):
        return self.__candidatesExpression

    @candidatesExpression.setter
    def candidatesExpression(self, candidatesExpression: str):
        self.__candidatesExpression = candidatesExpression


    @property
    def childrenExpression(self):
        return self.__childrenExpression

    @childrenExpression.setter
    def childrenExpression(self, childrenExpression: str):
        self.__childrenExpression = childrenExpression


    @property
    def tree(self):
        return self.__tree

    @tree.setter
    def tree(self, tree: bool):
        self.__tree = tree


    @property
    def rootExpression(self):
        return self.__rootExpression

    @rootExpression.setter
    def rootExpression(self, rootExpression: str):
        self.__rootExpression = rootExpression


class description_UserColor:

    pass
class viewpoint_description_UserFixedColor(description_FixedColor, description_UserColor):

    pass
class viewpoint_description_ComputedColor(description_ColorDescription, description_UserColor):

    def __init__(self, red: str, green: str, blue: str):
        self.red = red
        self.green = green
        self.blue = blue
        
        pass
    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, blue: str):
        self.__blue = blue


    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, red: str):
        self.__red = red


    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, green: str):
        self.__green = green


class viewpoint_description_InterpolatedColor(description_ColorDescription, description_UserColor):

    def __init__(self, colorValueComputationExpression: str, minValueComputationExpression: str, maxValueComputationExpression: str, viewpoint_description_InterpolatedColor: set["ColorStep"] = None):
        self.colorValueComputationExpression = colorValueComputationExpression
        self.minValueComputationExpression = minValueComputationExpression
        self.maxValueComputationExpression = maxValueComputationExpression
        self.viewpoint_description_InterpolatedColor = viewpoint_description_InterpolatedColor if viewpoint_description_InterpolatedColor is not None else set()
        
        pass
    @property
    def colorValueComputationExpression(self):
        return self.__colorValueComputationExpression

    @colorValueComputationExpression.setter
    def colorValueComputationExpression(self, colorValueComputationExpression: str):
        self.__colorValueComputationExpression = colorValueComputationExpression


    @property
    def minValueComputationExpression(self):
        return self.__minValueComputationExpression

    @minValueComputationExpression.setter
    def minValueComputationExpression(self, minValueComputationExpression: str):
        self.__minValueComputationExpression = minValueComputationExpression


    @property
    def maxValueComputationExpression(self):
        return self.__maxValueComputationExpression

    @maxValueComputationExpression.setter
    def maxValueComputationExpression(self, maxValueComputationExpression: str):
        self.__maxValueComputationExpression = maxValueComputationExpression


    @property
    def viewpoint_description_InterpolatedColor(self):
        return self.__viewpoint_description_InterpolatedColor

    @viewpoint_description_InterpolatedColor.setter
    def viewpoint_description_InterpolatedColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_InterpolatedColor__viewpoint_description_InterpolatedColor", None)
        self.__viewpoint_description_InterpolatedColor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ColorStep"):
                    opp_val = getattr(item, "ColorStep", None)
                    
                    if opp_val == self:
                        setattr(item, "ColorStep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ColorStep"):
                    opp_val = getattr(item, "ColorStep", None)
                    
                    setattr(item, "ColorStep", self)
                    

class EStructuralFeatureCustomization:

    pass
class viewpoint_description_EReferenceCustomization(EStructuralFeatureCustomization):

    def __init__(self, referenceName: str, viewpoint_description_EReferenceCustomization: "description_viewpoint_EObject" = None, EStructuralFeatureCustomization103: "viewpoint_description_VSMElementCustomizationReuse" = None, EStructuralFeatureCustomization: "viewpoint_description_VSMElementCustomization" = None):
        self.referenceName = referenceName
        self.viewpoint_description_EReferenceCustomization = viewpoint_description_EReferenceCustomization
        
        pass
    @property
    def referenceName(self):
        return self.__referenceName

    @referenceName.setter
    def referenceName(self, referenceName: str):
        self.__referenceName = referenceName


    @property
    def viewpoint_description_EReferenceCustomization(self):
        return self.__viewpoint_description_EReferenceCustomization

    @viewpoint_description_EReferenceCustomization.setter
    def viewpoint_description_EReferenceCustomization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_EReferenceCustomization__viewpoint_description_EReferenceCustomization", None)
        self.__viewpoint_description_EReferenceCustomization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_viewpoint_EObject110"):
                opp_val = getattr(old_value, "description_viewpoint_EObject110", None)
                if opp_val == self:
                    setattr(old_value, "description_viewpoint_EObject110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_viewpoint_EObject110"):
                opp_val = getattr(value, "description_viewpoint_EObject110", None)
                setattr(value, "description_viewpoint_EObject110", self)

class viewpoint_description_IVSMElementCustomization(ABC):

    pass
class IVSMElementCustomization:

    pass
class viewpoint_description_VSMElementCustomization(IVSMElementCustomization):

    def __init__(self, predicateExpression: str, viewpoint_description_VSMElementCustomization: set["EStructuralFeatureCustomization"] = None, IVSMElementCustomization: "viewpoint_description_Customization" = None):
        self.predicateExpression = predicateExpression
        self.viewpoint_description_VSMElementCustomization = viewpoint_description_VSMElementCustomization if viewpoint_description_VSMElementCustomization is not None else set()
        
        pass
    @property
    def predicateExpression(self):
        return self.__predicateExpression

    @predicateExpression.setter
    def predicateExpression(self, predicateExpression: str):
        self.__predicateExpression = predicateExpression


    @property
    def viewpoint_description_VSMElementCustomization(self):
        return self.__viewpoint_description_VSMElementCustomization

    @viewpoint_description_VSMElementCustomization.setter
    def viewpoint_description_VSMElementCustomization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_VSMElementCustomization__viewpoint_description_VSMElementCustomization", None)
        self.__viewpoint_description_VSMElementCustomization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EStructuralFeatureCustomization"):
                    opp_val = getattr(item, "EStructuralFeatureCustomization", None)
                    
                    if opp_val == self:
                        setattr(item, "EStructuralFeatureCustomization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EStructuralFeatureCustomization"):
                    opp_val = getattr(item, "EStructuralFeatureCustomization", None)
                    
                    setattr(item, "EStructuralFeatureCustomization", self)
                    

class viewpoint_description_VSMElementCustomizationReuse(IVSMElementCustomization):

    pass
class viewpoint_description_Customization:

    pass
class viewpoint_description_EAttributeCustomization(EStructuralFeatureCustomization):

    def __init__(self, attributeName: str, value: str, EStructuralFeatureCustomization103: "viewpoint_description_VSMElementCustomizationReuse" = None, EStructuralFeatureCustomization: "viewpoint_description_VSMElementCustomization" = None):
        self.attributeName = attributeName
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def attributeName(self):
        return self.__attributeName

    @attributeName.setter
    def attributeName(self, attributeName: str):
        self.__attributeName = attributeName


class viewpoint_description_EStructuralFeatureCustomization(ABC):

    def __init__(self, applyOnAll: bool, viewpoint_description_EStructuralFeatureCustomization: set["description_viewpoint_EObject"] = None):
        self.applyOnAll = applyOnAll
        self.viewpoint_description_EStructuralFeatureCustomization = viewpoint_description_EStructuralFeatureCustomization if viewpoint_description_EStructuralFeatureCustomization is not None else set()
        
        pass
    @property
    def applyOnAll(self):
        return self.__applyOnAll

    @applyOnAll.setter
    def applyOnAll(self, applyOnAll: bool):
        self.__applyOnAll = applyOnAll


    @property
    def viewpoint_description_EStructuralFeatureCustomization(self):
        return self.__viewpoint_description_EStructuralFeatureCustomization

    @viewpoint_description_EStructuralFeatureCustomization.setter
    def viewpoint_description_EStructuralFeatureCustomization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_EStructuralFeatureCustomization__viewpoint_description_EStructuralFeatureCustomization", None)
        self.__viewpoint_description_EStructuralFeatureCustomization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_viewpoint_EObject108"):
                    opp_val = getattr(item, "description_viewpoint_EObject108", None)
                    
                    if opp_val == self:
                        setattr(item, "description_viewpoint_EObject108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_viewpoint_EObject108"):
                    opp_val = getattr(item, "description_viewpoint_EObject108", None)
                    
                    setattr(item, "description_viewpoint_EObject108", self)
                    

class viewpoint_description_DecorationDescription(ABC):

    def __init__(self, position: str, decoratorPath: str, preconditionExpression: str, name: str):
        self.position = position
        self.decoratorPath = decoratorPath
        self.preconditionExpression = preconditionExpression
        self.name = name
        
        pass
    @property
    def decoratorPath(self):
        return self.__decoratorPath

    @decoratorPath.setter
    def decoratorPath(self, decoratorPath: str):
        self.__decoratorPath = decoratorPath


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def preconditionExpression(self):
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression


class viewpoint_description_DecorationDescriptionsSet:

    pass
class tool_PasteDescription:

    pass
class viewpoint_description_PasteTargetDescription(ABC):

    pass
class tool_ContainerDropDescription:

    pass
class viewpoint_description_DragAndDropTargetDescription(ABC):

    pass
class viewpoint_description_ConditionalStyleDescription(ABC):

    def __init__(self, predicateExpression: str):
        self.predicateExpression = predicateExpression
        
        pass
    @property
    def predicateExpression(self):
        return self.__predicateExpression

    @predicateExpression.setter
    def predicateExpression(self, predicateExpression: str):
        self.__predicateExpression = predicateExpression


    def checkPredicate(self, viewpoint_viewVariable, viewpoint_modelElement, viewpoint_containerVariable) :
        # TODO: Implement checkPredicate method
        pass

class description_viewpoint_EStringToStringMapEntry:

    pass
class viewpoint_description_DAnnotation:

    def __init__(self, source: str, viewpoint_description_DAnnotation: set["description_viewpoint_EStringToStringMapEntry"] = None):
        self.source = source
        self.viewpoint_description_DAnnotation = viewpoint_description_DAnnotation if viewpoint_description_DAnnotation is not None else set()
        
        pass
    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source


    @property
    def viewpoint_description_DAnnotation(self):
        return self.__viewpoint_description_DAnnotation

    @viewpoint_description_DAnnotation.setter
    def viewpoint_description_DAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DAnnotation__viewpoint_description_DAnnotation", None)
        self.__viewpoint_description_DAnnotation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_viewpoint_EStringToStringMapEntry"):
                    opp_val = getattr(item, "description_viewpoint_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "description_viewpoint_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_viewpoint_EStringToStringMapEntry"):
                    opp_val = getattr(item, "description_viewpoint_EStringToStringMapEntry", None)
                    
                    setattr(item, "description_viewpoint_EStringToStringMapEntry", self)
                    

class DAnnotation:

    pass
class viewpoint_description_AbstractMappingImport(ABC):

    def __init__(self, hideSubMappings: bool, inheritsAncestorFilters: bool):
        self.hideSubMappings = hideSubMappings
        self.inheritsAncestorFilters = inheritsAncestorFilters
        
        pass
    @property
    def hideSubMappings(self):
        return self.__hideSubMappings

    @hideSubMappings.setter
    def hideSubMappings(self, hideSubMappings: bool):
        self.__hideSubMappings = hideSubMappings


    @property
    def inheritsAncestorFilters(self):
        return self.__inheritsAncestorFilters

    @inheritsAncestorFilters.setter
    def inheritsAncestorFilters(self, inheritsAncestorFilters: bool):
        self.__inheritsAncestorFilters = inheritsAncestorFilters


class tool_RepresentationNavigationDescription:

    pass
class tool_RepresentationCreationDescription:

    pass
class IdentifiedElement:

    pass
class viewpoint_description_RepresentationElementMapping(IdentifiedElement):

    pass
class viewpoint_description_JavaExtension:

    def __init__(self, qualifiedClassName: str):
        self.qualifiedClassName = qualifiedClassName
        
        pass
    @property
    def qualifiedClassName(self):
        return self.__qualifiedClassName

    @qualifiedClassName.setter
    def qualifiedClassName(self, qualifiedClassName: str):
        self.__qualifiedClassName = qualifiedClassName


class description_viewpoint_EObject:

    pass
class viewpoint_description_MetamodelExtensionSetting:

    pass
class viewpoint_description_RepresentationExtensionDescription(ABC):

    def __init__(self, name: str, viewpointURI: str, representationName: str, viewpoint_description_RepresentationExtensionDescription: set["description_viewpoint_EPackage"] = None):
        self.name = name
        self.viewpointURI = viewpointURI
        self.representationName = representationName
        self.viewpoint_description_RepresentationExtensionDescription = viewpoint_description_RepresentationExtensionDescription if viewpoint_description_RepresentationExtensionDescription is not None else set()
        
        pass
    @property
    def viewpointURI(self):
        return self.__viewpointURI

    @viewpointURI.setter
    def viewpointURI(self, viewpointURI: str):
        self.__viewpointURI = viewpointURI


    @property
    def representationName(self):
        return self.__representationName

    @representationName.setter
    def representationName(self, representationName: str):
        self.__representationName = representationName


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def viewpoint_description_RepresentationExtensionDescription(self):
        return self.__viewpoint_description_RepresentationExtensionDescription

    @viewpoint_description_RepresentationExtensionDescription.setter
    def viewpoint_description_RepresentationExtensionDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_RepresentationExtensionDescription__viewpoint_description_RepresentationExtensionDescription", None)
        self.__viewpoint_description_RepresentationExtensionDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_viewpoint_EPackage89"):
                    opp_val = getattr(item, "description_viewpoint_EPackage89", None)
                    
                    if opp_val == self:
                        setattr(item, "description_viewpoint_EPackage89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_viewpoint_EPackage89"):
                    opp_val = getattr(item, "description_viewpoint_EPackage89", None)
                    
                    setattr(item, "description_viewpoint_EPackage89", self)
                    

class viewpoint_description_DModelElement(ABC):

    def __init__(self, viewpoint_description_DModelElement: set["DAnnotation"] = None):
        self.viewpoint_description_DModelElement = viewpoint_description_DModelElement if viewpoint_description_DModelElement is not None else set()
        
        pass
    @property
    def viewpoint_description_DModelElement(self):
        return self.__viewpoint_description_DModelElement

    @viewpoint_description_DModelElement.setter
    def viewpoint_description_DModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_DModelElement__viewpoint_description_DModelElement", None)
        self.__viewpoint_description_DModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DAnnotation"):
                    opp_val = getattr(item, "DAnnotation", None)
                    
                    if opp_val == self:
                        setattr(item, "DAnnotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DAnnotation"):
                    opp_val = getattr(item, "DAnnotation", None)
                    
                    setattr(item, "DAnnotation", self)
                    

    def getDAnnotation(self, viewpoint_source) :
        # TODO: Implement getDAnnotation method
        pass

class viewpoint_description_DocumentedElement(ABC):

    def __init__(self, documentation: str):
        self.documentation = documentation
        
        pass
    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


class description_viewpoint_EPackage:

    pass
class viewpoint_description_FeatureExtensionDescription(ABC):

    pass
class RepresentationTemplate:

    pass
class MetamodelExtensionSetting:

    pass
class JavaExtension:

    pass
class RepresentationExtensionDescription:

    pass
class viewpoint_description_DiagramExtensionDescription(RepresentationExtensionDescription):

    pass
class RepresentationDescription:

    pass
class viewpoint_description_RepresentationImportDescription(RepresentationDescription):

    pass
class viewpoint_description_RepresentationTemplate(ABC):

    def __init__(self, name: str, viewpoint_description_RepresentationTemplate: set["RepresentationDescription"] = None):
        self.name = name
        self.viewpoint_description_RepresentationTemplate = viewpoint_description_RepresentationTemplate if viewpoint_description_RepresentationTemplate is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def viewpoint_description_RepresentationTemplate(self):
        return self.__viewpoint_description_RepresentationTemplate

    @viewpoint_description_RepresentationTemplate.setter
    def viewpoint_description_RepresentationTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_RepresentationTemplate__viewpoint_description_RepresentationTemplate", None)
        self.__viewpoint_description_RepresentationTemplate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RepresentationDescription87"):
                    opp_val = getattr(item, "RepresentationDescription87", None)
                    
                    if opp_val == self:
                        setattr(item, "RepresentationDescription87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepresentationDescription87"):
                    opp_val = getattr(item, "RepresentationDescription87", None)
                    
                    setattr(item, "RepresentationDescription87", self)
                    

class validation_ValidationSet:

    pass
class description_IdentifiedElement:

    pass
class description_EndUserDocumentedElement:

    pass
class description_Component:

    pass
class viewpoint_description_Component(ABC):

    pass
class UserColorsPalette:

    pass
class SytemColorsPalette:

    pass
class viewpoint_Customizable(ABC):

    def __init__(self, customFeatures: str):
        self.customFeatures = customFeatures
        
        pass
    @property
    def customFeatures(self):
        return self.__customFeatures

    @customFeatures.setter
    def customFeatures(self, customFeatures: str):
        self.__customFeatures = customFeatures


class DFile:

    pass
class viewpoint_DModel(DFile):

    pass
class DResourceContainer:

    pass
class viewpoint_DFolder(DResourceContainer):

    pass
class viewpoint_DProject(DResourceContainer):

    pass
class DResource:

    pass
class viewpoint_DResourceContainer(DResource):

    pass
class viewpoint_DFile(DResource):

    pass
class viewpoint_DResource(ABC):

    def __init__(self, name: str, path: str, viewpoint_DResource: "viewpoint_DResourceContainer" = None):
        self.name = name
        self.path = path
        self.viewpoint_DResource = viewpoint_DResource
        
        pass
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def viewpoint_DResource(self):
        return self.__viewpoint_DResource

    @viewpoint_DResource.setter
    def viewpoint_DResource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DResource__viewpoint_DResource", None)
        self.__viewpoint_DResource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DResourceContainer"):
                opp_val = getattr(old_value, "viewpoint_DResourceContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DResourceContainer"):
                opp_val = getattr(value, "viewpoint_DResourceContainer", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DResourceContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class viewpoint_SessionManagerEObject:

    pass
class viewpoint_DAnalysisSessionEObject:

    def __init__(self, open: bool, blocked: bool, resources: str, controlledResources: str, synchronizationStatus: str, viewpoint_DAnalysisSessionEObject: set["Viewpoint"] = None, viewpoint_DAnalysisSessionEObject59: set["viewpoint_DAnalysis"] = None, viewpoint_DAnalysisSessionEObject62: "viewpoint_SessionManagerEObject" = None):
        self.open = open
        self.blocked = blocked
        self.resources = resources
        self.controlledResources = controlledResources
        self.synchronizationStatus = synchronizationStatus
        self.viewpoint_DAnalysisSessionEObject = viewpoint_DAnalysisSessionEObject if viewpoint_DAnalysisSessionEObject is not None else set()
        self.viewpoint_DAnalysisSessionEObject59 = viewpoint_DAnalysisSessionEObject59 if viewpoint_DAnalysisSessionEObject59 is not None else set()
        self.viewpoint_DAnalysisSessionEObject62 = viewpoint_DAnalysisSessionEObject62
        
        pass
    @property
    def resources(self):
        return self.__resources

    @resources.setter
    def resources(self, resources: str):
        self.__resources = resources


    @property
    def blocked(self):
        return self.__blocked

    @blocked.setter
    def blocked(self, blocked: bool):
        self.__blocked = blocked


    @property
    def open(self):
        return self.__open

    @open.setter
    def open(self, open: bool):
        self.__open = open


    @property
    def controlledResources(self):
        return self.__controlledResources

    @controlledResources.setter
    def controlledResources(self, controlledResources: str):
        self.__controlledResources = controlledResources


    @property
    def synchronizationStatus(self):
        return self.__synchronizationStatus

    @synchronizationStatus.setter
    def synchronizationStatus(self, synchronizationStatus: str):
        self.__synchronizationStatus = synchronizationStatus


    @property
    def viewpoint_DAnalysisSessionEObject(self):
        return self.__viewpoint_DAnalysisSessionEObject

    @viewpoint_DAnalysisSessionEObject.setter
    def viewpoint_DAnalysisSessionEObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysisSessionEObject__viewpoint_DAnalysisSessionEObject", None)
        self.__viewpoint_DAnalysisSessionEObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Viewpoint57"):
                    opp_val = getattr(item, "Viewpoint57", None)
                    
                    if opp_val == self:
                        setattr(item, "Viewpoint57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Viewpoint57"):
                    opp_val = getattr(item, "Viewpoint57", None)
                    
                    setattr(item, "Viewpoint57", self)
                    

    @property
    def viewpoint_DAnalysisSessionEObject62(self):
        return self.__viewpoint_DAnalysisSessionEObject62

    @viewpoint_DAnalysisSessionEObject62.setter
    def viewpoint_DAnalysisSessionEObject62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysisSessionEObject__viewpoint_DAnalysisSessionEObject62", None)
        self.__viewpoint_DAnalysisSessionEObject62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_SessionManagerEObject"):
                opp_val = getattr(old_value, "viewpoint_SessionManagerEObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_SessionManagerEObject"):
                opp_val = getattr(value, "viewpoint_SessionManagerEObject", None)
                if opp_val is None:
                    setattr(value, "viewpoint_SessionManagerEObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DAnalysisSessionEObject59(self):
        return self.__viewpoint_DAnalysisSessionEObject59

    @viewpoint_DAnalysisSessionEObject59.setter
    def viewpoint_DAnalysisSessionEObject59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysisSessionEObject__viewpoint_DAnalysisSessionEObject59", None)
        self.__viewpoint_DAnalysisSessionEObject59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DAnalysis60"):
                    opp_val = getattr(item, "viewpoint_DAnalysis60", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DAnalysis60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DAnalysis60"):
                    opp_val = getattr(item, "viewpoint_DAnalysis60", None)
                    
                    setattr(item, "viewpoint_DAnalysis60", self)
                    

class viewpoint_RGBValues:

    def __init__(self, red: int, green: int, blue: int, viewpoint_RGBValues: "viewpoint_BasicLabelStyle" = None):
        self.red = red
        self.green = green
        self.blue = blue
        self.viewpoint_RGBValues = viewpoint_RGBValues
        
        pass
    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green


    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue


    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red


    @property
    def viewpoint_RGBValues(self):
        return self.__viewpoint_RGBValues

    @viewpoint_RGBValues.setter
    def viewpoint_RGBValues(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_RGBValues__viewpoint_RGBValues", None)
        self.__viewpoint_RGBValues = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_BasicLabelStyle"):
                opp_val = getattr(old_value, "viewpoint_BasicLabelStyle", None)
                if opp_val == self:
                    setattr(old_value, "viewpoint_BasicLabelStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_BasicLabelStyle"):
                opp_val = getattr(value, "viewpoint_BasicLabelStyle", None)
                setattr(value, "viewpoint_BasicLabelStyle", self)

class DNavigationLink:

    pass
class viewpoint_diagram_DDiagramLink(DNavigationLink):

    pass
class viewpoint_DEObjectLink(DNavigationLink):

    pass
class viewpoint_DragAndDropTarget:

    def __init__(self):
        
        pass
    def getDragAndDropDescription(self) :
        # TODO: Implement getDragAndDropDescription method
        pass

class style_StyleDescription:

    pass
class viewpoint_style_NodeStyleDescription(style_LabelStyleDescription, style_BorderedStyleDescription, style_StyleDescription, style_TooltipStyleDescription):

    def __init__(self, sizeComputationExpression: str, hideLabelByDefault: bool, resizeKind: str, labelPosition: str, style_StyleDescription: "viewpoint_Style" = None, style_StyleDescription404: "viewpoint_diagram_ContainerVariable2StyleDescription" = None, style_StyleDescription385: "viewpoint_diagram_ComputedStyleDescriptionRegistry" = None):
        self.sizeComputationExpression = sizeComputationExpression
        self.hideLabelByDefault = hideLabelByDefault
        self.resizeKind = resizeKind
        self.labelPosition = labelPosition
        
        pass
    @property
    def labelPosition(self):
        return self.__labelPosition

    @labelPosition.setter
    def labelPosition(self, labelPosition: str):
        self.__labelPosition = labelPosition


    @property
    def sizeComputationExpression(self):
        return self.__sizeComputationExpression

    @sizeComputationExpression.setter
    def sizeComputationExpression(self, sizeComputationExpression: str):
        self.__sizeComputationExpression = sizeComputationExpression


    @property
    def resizeKind(self):
        return self.__resizeKind

    @resizeKind.setter
    def resizeKind(self, resizeKind: str):
        self.__resizeKind = resizeKind


    @property
    def hideLabelByDefault(self):
        return self.__hideLabelByDefault

    @hideLabelByDefault.setter
    def hideLabelByDefault(self, hideLabelByDefault: bool):
        self.__hideLabelByDefault = hideLabelByDefault


class Customizable:

    pass
class viewpoint_diagram_GaugeSection(Customizable):

    def __init__(self, min: str, max: str, value: str, label: str, viewpoint_diagram_GaugeSection: "diagram_viewpoint_RGBValues" = None, viewpoint_diagram_GaugeSection346: "diagram_viewpoint_RGBValues" = None):
        self.min = min
        self.max = max
        self.value = value
        self.label = label
        self.viewpoint_diagram_GaugeSection = viewpoint_diagram_GaugeSection
        self.viewpoint_diagram_GaugeSection346 = viewpoint_diagram_GaugeSection346
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min


    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, max: str):
        self.__max = max


    @property
    def viewpoint_diagram_GaugeSection(self):
        return self.__viewpoint_diagram_GaugeSection

    @viewpoint_diagram_GaugeSection.setter
    def viewpoint_diagram_GaugeSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_GaugeSection__viewpoint_diagram_GaugeSection", None)
        self.__viewpoint_diagram_GaugeSection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues344"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues344", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues344"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues344", None)
                setattr(value, "diagram_viewpoint_RGBValues344", self)

    @property
    def viewpoint_diagram_GaugeSection346(self):
        return self.__viewpoint_diagram_GaugeSection346

    @viewpoint_diagram_GaugeSection346.setter
    def viewpoint_diagram_GaugeSection346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_GaugeSection__viewpoint_diagram_GaugeSection346", None)
        self.__viewpoint_diagram_GaugeSection346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagram_viewpoint_RGBValues347"):
                opp_val = getattr(old_value, "diagram_viewpoint_RGBValues347", None)
                if opp_val == self:
                    setattr(old_value, "diagram_viewpoint_RGBValues347", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagram_viewpoint_RGBValues347"):
                opp_val = getattr(value, "diagram_viewpoint_RGBValues347", None)
                setattr(value, "diagram_viewpoint_RGBValues347", self)

class viewpoint_BasicLabelStyle(Customizable):

    def __init__(self, labelSize: int, labelFormat: str, showIcon: bool, iconPath: str, viewpoint_BasicLabelStyle: "viewpoint_RGBValues" = None):
        self.labelSize = labelSize
        self.labelFormat = labelFormat
        self.showIcon = showIcon
        self.iconPath = iconPath
        self.viewpoint_BasicLabelStyle = viewpoint_BasicLabelStyle
        
        pass
    @property
    def labelFormat(self):
        return self.__labelFormat

    @labelFormat.setter
    def labelFormat(self, labelFormat: str):
        self.__labelFormat = labelFormat


    @property
    def iconPath(self):
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath


    @property
    def labelSize(self):
        return self.__labelSize

    @labelSize.setter
    def labelSize(self, labelSize: int):
        self.__labelSize = labelSize


    @property
    def showIcon(self):
        return self.__showIcon

    @showIcon.setter
    def showIcon(self, showIcon: bool):
        self.__showIcon = showIcon


    @property
    def viewpoint_BasicLabelStyle(self):
        return self.__viewpoint_BasicLabelStyle

    @viewpoint_BasicLabelStyle.setter
    def viewpoint_BasicLabelStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_BasicLabelStyle__viewpoint_BasicLabelStyle", None)
        self.__viewpoint_BasicLabelStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_RGBValues"):
                opp_val = getattr(old_value, "viewpoint_RGBValues", None)
                if opp_val == self:
                    setattr(old_value, "viewpoint_RGBValues", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_RGBValues"):
                opp_val = getattr(value, "viewpoint_RGBValues", None)
                setattr(value, "viewpoint_RGBValues", self)

class BasicLabelStyle:

    pass
class viewpoint_diagram_BeginLabelStyle(BasicLabelStyle):

    def __init__(self):
        
        pass
    def getDescription(self) :
        # TODO: Implement getDescription method
        pass

    def setDescription(self, viewpoint_description):
        # TODO: Implement setDescription method
        pass

class viewpoint_diagram_CenterLabelStyle(BasicLabelStyle):

    def __init__(self):
        
        pass
    def setDescription(self, viewpoint_description):
        # TODO: Implement setDescription method
        pass

    def getDescription(self) :
        # TODO: Implement getDescription method
        pass

class viewpoint_diagram_EndLabelStyle(BasicLabelStyle):

    def __init__(self):
        
        pass
    def setDescription(self, viewpoint_description):
        # TODO: Implement setDescription method
        pass

    def getDescription(self) :
        # TODO: Implement getDescription method
        pass

class viewpoint_LabelStyle(BasicLabelStyle):

    def __init__(self, labelAlignment: str):
        self.labelAlignment = labelAlignment
        
        pass
    @property
    def labelAlignment(self):
        return self.__labelAlignment

    @labelAlignment.setter
    def labelAlignment(self, labelAlignment: str):
        self.__labelAlignment = labelAlignment


class viewpoint_DAnalysisCustomData:

    def __init__(self, key: str, viewpoint_DAnalysisCustomData: "viewpoint_EObject" = None):
        self.key = key
        self.viewpoint_DAnalysisCustomData = viewpoint_DAnalysisCustomData
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def viewpoint_DAnalysisCustomData(self):
        return self.__viewpoint_DAnalysisCustomData

    @viewpoint_DAnalysisCustomData.setter
    def viewpoint_DAnalysisCustomData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysisCustomData__viewpoint_DAnalysisCustomData", None)
        self.__viewpoint_DAnalysisCustomData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_EObject54"):
                opp_val = getattr(old_value, "viewpoint_EObject54", None)
                if opp_val == self:
                    setattr(old_value, "viewpoint_EObject54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_EObject54"):
                opp_val = getattr(value, "viewpoint_EObject54", None)
                setattr(value, "viewpoint_EObject54", self)

class viewpoint_DSourceFileLink(DNavigationLink):

    def __init__(self, filePath: str, startPosition: int, endPosition: int):
        self.filePath = filePath
        self.startPosition = startPosition
        self.endPosition = endPosition
        
        pass
    @property
    def endPosition(self):
        return self.__endPosition

    @endPosition.setter
    def endPosition(self, endPosition: int):
        self.__endPosition = endPosition


    @property
    def startPosition(self):
        return self.__startPosition

    @startPosition.setter
    def startPosition(self, startPosition: int):
        self.__startPosition = startPosition


    @property
    def filePath(self):
        return self.__filePath

    @filePath.setter
    def filePath(self, filePath: str):
        self.__filePath = filePath


class DecorationDescription:

    pass
class viewpoint_description_SemanticBasedDecoration(DecorationDescription):

    def __init__(self, domainClass: str, DecorationDescription: "viewpoint_Decoration" = None, DecorationDescription99: "viewpoint_description_DecorationDescriptionsSet" = None):
        self.domainClass = domainClass
        
        pass
    @property
    def domainClass(self):
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass


class viewpoint_description_MappingBasedDecoration(DecorationDescription):

    pass
class viewpoint_Decoration:

    pass
class Viewpoint:

    pass
class viewpoint_MetaModelExtension:

    pass
class DSemanticDecorator:

    pass
class viewpoint_diagram_DSemanticDiagram(DSemanticDecorator, diagram_DDiagram):

    def __init__(self):
        
        pass
    def getRootContent(self) :
        # TODO: Implement getRootContent method
        pass

class DStylizable:

    pass
class DMappingBased:

    pass
class DLabelled:

    pass
class AnnotationEntry:

    pass
class description_DModelElement:

    pass
class DRefreshable:

    pass
class viewpoint_DRepresentationElement(DRefreshable, DMappingBased, DSemanticDecorator, DLabelled, DStylizable):

    def __init__(self, name: str, viewpoint_DRepresentationElement: "viewpoint_DRepresentation" = None, viewpoint_DRepresentationElement25: "viewpoint_DRepresentation" = None, viewpoint_DRepresentationElement29: set["viewpoint_EObject"] = None):
        self.name = name
        self.viewpoint_DRepresentationElement = viewpoint_DRepresentationElement
        self.viewpoint_DRepresentationElement25 = viewpoint_DRepresentationElement25
        self.viewpoint_DRepresentationElement29 = viewpoint_DRepresentationElement29 if viewpoint_DRepresentationElement29 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def viewpoint_DRepresentationElement29(self):
        return self.__viewpoint_DRepresentationElement29

    @viewpoint_DRepresentationElement29.setter
    def viewpoint_DRepresentationElement29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationElement__viewpoint_DRepresentationElement29", None)
        self.__viewpoint_DRepresentationElement29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_EObject30"):
                    opp_val = getattr(item, "viewpoint_EObject30", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_EObject30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_EObject30"):
                    opp_val = getattr(item, "viewpoint_EObject30", None)
                    
                    setattr(item, "viewpoint_EObject30", self)
                    

    @property
    def viewpoint_DRepresentationElement(self):
        return self.__viewpoint_DRepresentationElement

    @viewpoint_DRepresentationElement.setter
    def viewpoint_DRepresentationElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationElement__viewpoint_DRepresentationElement", None)
        self.__viewpoint_DRepresentationElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DRepresentation"):
                opp_val = getattr(old_value, "viewpoint_DRepresentation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DRepresentation"):
                opp_val = getattr(value, "viewpoint_DRepresentation", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DRepresentation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DRepresentationElement25(self):
        return self.__viewpoint_DRepresentationElement25

    @viewpoint_DRepresentationElement25.setter
    def viewpoint_DRepresentationElement25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationElement__viewpoint_DRepresentationElement25", None)
        self.__viewpoint_DRepresentationElement25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DRepresentation24"):
                opp_val = getattr(old_value, "viewpoint_DRepresentation24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DRepresentation24"):
                opp_val = getattr(value, "viewpoint_DRepresentation24", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DRepresentation24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class viewpoint_Style(Customizable, DRefreshable):

    pass
class description_DocumentedElement:

    pass
class viewpoint_description_Group(description_DModelElement, description_DocumentedElement):

    def __init__(self, name: str, version: str, viewpoint_description_Group: set["Viewpoint"] = None, viewpoint_description_Group68: "SytemColorsPalette" = None, viewpoint_description_Group70: set["UserColorsPalette"] = None):
        self.name = name
        self.version = version
        self.viewpoint_description_Group = viewpoint_description_Group if viewpoint_description_Group is not None else set()
        self.viewpoint_description_Group68 = viewpoint_description_Group68
        self.viewpoint_description_Group70 = viewpoint_description_Group70 if viewpoint_description_Group70 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def viewpoint_description_Group(self):
        return self.__viewpoint_description_Group

    @viewpoint_description_Group.setter
    def viewpoint_description_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Group__viewpoint_description_Group", None)
        self.__viewpoint_description_Group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Viewpoint66"):
                    opp_val = getattr(item, "Viewpoint66", None)
                    
                    if opp_val == self:
                        setattr(item, "Viewpoint66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Viewpoint66"):
                    opp_val = getattr(item, "Viewpoint66", None)
                    
                    setattr(item, "Viewpoint66", self)
                    

    @property
    def viewpoint_description_Group68(self):
        return self.__viewpoint_description_Group68

    @viewpoint_description_Group68.setter
    def viewpoint_description_Group68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Group__viewpoint_description_Group68", None)
        self.__viewpoint_description_Group68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SytemColorsPalette"):
                opp_val = getattr(old_value, "SytemColorsPalette", None)
                if opp_val == self:
                    setattr(old_value, "SytemColorsPalette", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SytemColorsPalette"):
                opp_val = getattr(value, "SytemColorsPalette", None)
                setattr(value, "SytemColorsPalette", self)

    @property
    def viewpoint_description_Group70(self):
        return self.__viewpoint_description_Group70

    @viewpoint_description_Group70.setter
    def viewpoint_description_Group70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Group__viewpoint_description_Group70", None)
        self.__viewpoint_description_Group70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UserColorsPalette"):
                    opp_val = getattr(item, "UserColorsPalette", None)
                    
                    if opp_val == self:
                        setattr(item, "UserColorsPalette", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UserColorsPalette"):
                    opp_val = getattr(item, "UserColorsPalette", None)
                    
                    setattr(item, "UserColorsPalette", self)
                    

class viewpoint_description_AbstractNodeMapping(description_DocumentedElement, description_DiagramElementMapping):

    def __init__(self, domainClass: str, viewpoint_description_AbstractNodeMapping: set["description_NodeMapping"] = None, viewpoint_description_AbstractNodeMapping480: set["description_NodeMapping"] = None, description_DiagramElementMapping: "viewpoint_tool_ContainerDropDescription" = None, description_DiagramElementMapping511: "viewpoint_description_EdgeMapping" = None, description_DiagramElementMapping653: "viewpoint_tool_EdgeCreationDescription" = None, description_DiagramElementMapping716: "viewpoint_tool_CreateView" = None, DiagramElementMapping: "viewpoint_tool_DoubleClickDescription" = None, description_DiagramElementMapping537: "viewpoint_description_MappingBasedDecoration" = None, description_DiagramElementMapping265: "viewpoint_diagram_DDiagramElement" = None, description_DiagramElementMapping514: "viewpoint_description_EdgeMapping" = None, description_DiagramElementMapping740: "viewpoint_validation_ViewValidationRule" = None, description_DiagramElementMapping724: "viewpoint_filter_MappingFilter" = None, description_DiagramElementMapping389: "viewpoint_diagram_DiagramElementMapping2ModelElement" = None, description_DiagramElementMapping457: "viewpoint_description_DiagramDescription" = None, description_DiagramElementMapping650: "viewpoint_tool_EdgeCreationDescription" = None, description_DiagramElementMapping551: "viewpoint_description_Layer" = None):
        self.domainClass = domainClass
        self.viewpoint_description_AbstractNodeMapping = viewpoint_description_AbstractNodeMapping if viewpoint_description_AbstractNodeMapping is not None else set()
        self.viewpoint_description_AbstractNodeMapping480 = viewpoint_description_AbstractNodeMapping480 if viewpoint_description_AbstractNodeMapping480 is not None else set()
        
        pass
    @property
    def domainClass(self):
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass


    @property
    def viewpoint_description_AbstractNodeMapping480(self):
        return self.__viewpoint_description_AbstractNodeMapping480

    @viewpoint_description_AbstractNodeMapping480.setter
    def viewpoint_description_AbstractNodeMapping480(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_AbstractNodeMapping__viewpoint_description_AbstractNodeMapping480", None)
        self.__viewpoint_description_AbstractNodeMapping480 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_NodeMapping481"):
                    opp_val = getattr(item, "description_NodeMapping481", None)
                    
                    if opp_val == self:
                        setattr(item, "description_NodeMapping481", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_NodeMapping481"):
                    opp_val = getattr(item, "description_NodeMapping481", None)
                    
                    setattr(item, "description_NodeMapping481", self)
                    

    @property
    def viewpoint_description_AbstractNodeMapping(self):
        return self.__viewpoint_description_AbstractNodeMapping

    @viewpoint_description_AbstractNodeMapping.setter
    def viewpoint_description_AbstractNodeMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_AbstractNodeMapping__viewpoint_description_AbstractNodeMapping", None)
        self.__viewpoint_description_AbstractNodeMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_NodeMapping478"):
                    opp_val = getattr(item, "description_NodeMapping478", None)
                    
                    if opp_val == self:
                        setattr(item, "description_NodeMapping478", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_NodeMapping478"):
                    opp_val = getattr(item, "description_NodeMapping478", None)
                    
                    setattr(item, "description_NodeMapping478", self)
                    

    def getDNodesDone(self) :
        # TODO: Implement getDNodesDone method
        pass

    def clearDNodesDone(self):
        # TODO: Implement clearDNodesDone method
        pass

    def getAllBorderedNodeMappings(self) :
        # TODO: Implement getAllBorderedNodeMappings method
        pass

    def findDNodeFromEObject(self, viewpoint_eObject) :
        # TODO: Implement findDNodeFromEObject method
        pass

    def addDoneNode(self, viewpoint_node):
        # TODO: Implement addDoneNode method
        pass

class viewpoint_concern_ConcernDescription(description_DocumentedElement, description_IdentifiedElement):

    pass
class viewpoint_description_RepresentationDescription(description_EndUserDocumentedElement, description_DocumentedElement, description_IdentifiedElement):

    def __init__(self, showOnStartup: bool, titleExpression: str, initialisation: bool, viewpoint_description_RepresentationDescription: set["description_viewpoint_EPackage"] = None):
        self.showOnStartup = showOnStartup
        self.titleExpression = titleExpression
        self.initialisation = initialisation
        self.viewpoint_description_RepresentationDescription = viewpoint_description_RepresentationDescription if viewpoint_description_RepresentationDescription is not None else set()
        
        pass
    @property
    def titleExpression(self):
        return self.__titleExpression

    @titleExpression.setter
    def titleExpression(self, titleExpression: str):
        self.__titleExpression = titleExpression


    @property
    def initialisation(self):
        return self.__initialisation

    @initialisation.setter
    def initialisation(self, initialisation: bool):
        self.__initialisation = initialisation


    @property
    def showOnStartup(self):
        return self.__showOnStartup

    @showOnStartup.setter
    def showOnStartup(self, showOnStartup: bool):
        self.__showOnStartup = showOnStartup


    @property
    def viewpoint_description_RepresentationDescription(self):
        return self.__viewpoint_description_RepresentationDescription

    @viewpoint_description_RepresentationDescription.setter
    def viewpoint_description_RepresentationDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_RepresentationDescription__viewpoint_description_RepresentationDescription", None)
        self.__viewpoint_description_RepresentationDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_viewpoint_EPackage"):
                    opp_val = getattr(item, "description_viewpoint_EPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "description_viewpoint_EPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_viewpoint_EPackage"):
                    opp_val = getattr(item, "description_viewpoint_EPackage", None)
                    
                    setattr(item, "description_viewpoint_EPackage", self)
                    

class viewpoint_filter_FilterDescription(description_DocumentedElement, description_IdentifiedElement):

    def __init__(self):
        
        pass
    def isVisible(self, viewpoint_element) :
        # TODO: Implement isVisible method
        pass

class viewpoint_description_EdgeMappingImport(description_DocumentedElement, description_IEdgeMapping, description_IdentifiedElement):

    def __init__(self, inheritsAncestorFilters: bool, viewpoint_description_EdgeMappingImport: "description_IEdgeMapping" = None, viewpoint_description_EdgeMappingImport526: set["description_ConditionalEdgeStyleDescription"] = None, description_IEdgeMapping524: "viewpoint_description_EdgeMappingImport" = None, description_IEdgeMapping: "viewpoint_diagram_DEdge" = None):
        self.inheritsAncestorFilters = inheritsAncestorFilters
        self.viewpoint_description_EdgeMappingImport = viewpoint_description_EdgeMappingImport
        self.viewpoint_description_EdgeMappingImport526 = viewpoint_description_EdgeMappingImport526 if viewpoint_description_EdgeMappingImport526 is not None else set()
        
        pass
    @property
    def inheritsAncestorFilters(self):
        return self.__inheritsAncestorFilters

    @inheritsAncestorFilters.setter
    def inheritsAncestorFilters(self, inheritsAncestorFilters: bool):
        self.__inheritsAncestorFilters = inheritsAncestorFilters


    @property
    def viewpoint_description_EdgeMappingImport(self):
        return self.__viewpoint_description_EdgeMappingImport

    @viewpoint_description_EdgeMappingImport.setter
    def viewpoint_description_EdgeMappingImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_EdgeMappingImport__viewpoint_description_EdgeMappingImport", None)
        self.__viewpoint_description_EdgeMappingImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_IEdgeMapping524"):
                opp_val = getattr(old_value, "description_IEdgeMapping524", None)
                if opp_val == self:
                    setattr(old_value, "description_IEdgeMapping524", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_IEdgeMapping524"):
                opp_val = getattr(value, "description_IEdgeMapping524", None)
                setattr(value, "description_IEdgeMapping524", self)

    @property
    def viewpoint_description_EdgeMappingImport526(self):
        return self.__viewpoint_description_EdgeMappingImport526

    @viewpoint_description_EdgeMappingImport526.setter
    def viewpoint_description_EdgeMappingImport526(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_EdgeMappingImport__viewpoint_description_EdgeMappingImport526", None)
        self.__viewpoint_description_EdgeMappingImport526 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ConditionalEdgeStyleDescription527"):
                    opp_val = getattr(item, "description_ConditionalEdgeStyleDescription527", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ConditionalEdgeStyleDescription527", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ConditionalEdgeStyleDescription527"):
                    opp_val = getattr(item, "description_ConditionalEdgeStyleDescription527", None)
                    
                    setattr(item, "description_ConditionalEdgeStyleDescription527", self)
                    

class viewpoint_diagram_DDiagram(DragAndDropTarget, description_DocumentedElement, DValidable, DContainer, DRepresentation):

    def __init__(self, info: str, isInLayoutingMode: bool, headerHeight: int, synchronized: bool, viewpoint_diagram_DDiagram: set["DDiagramElement"] = None, viewpoint_diagram_DDiagram227: set["DDiagramElement"] = None, viewpoint_diagram_DDiagram230: "description_DiagramDescription" = None, viewpoint_diagram_DDiagram236: set["DNode"] = None, viewpoint_diagram_DDiagram238: set["DNodeListElement"] = None, viewpoint_diagram_DDiagram240: set["DDiagramElementContainer"] = None, viewpoint_diagram_DDiagram242: "concern_ConcernDescription" = None, viewpoint_diagram_DDiagram244: set["filter_FilterDescription"] = None, viewpoint_diagram_DDiagram246: set["filter_FilterDescription"] = None, viewpoint_diagram_DDiagram232: set["DDiagram"] = None, viewpoint_diagram_DDiagram234: set["DEdge"] = None, viewpoint_diagram_DDiagram257: set["DDiagramElement"] = None, viewpoint_diagram_DDiagram249: set["validation_ValidationRule"] = None, viewpoint_diagram_DDiagram251: set["tool_BehaviorTool"] = None, viewpoint_diagram_DDiagram253: "FilterVariableHistory" = None, viewpoint_diagram_DDiagram255: set["description_Layer"] = None):
        self.info = info
        self.isInLayoutingMode = isInLayoutingMode
        self.headerHeight = headerHeight
        self.synchronized = synchronized
        self.viewpoint_diagram_DDiagram = viewpoint_diagram_DDiagram if viewpoint_diagram_DDiagram is not None else set()
        self.viewpoint_diagram_DDiagram227 = viewpoint_diagram_DDiagram227 if viewpoint_diagram_DDiagram227 is not None else set()
        self.viewpoint_diagram_DDiagram230 = viewpoint_diagram_DDiagram230
        self.viewpoint_diagram_DDiagram236 = viewpoint_diagram_DDiagram236 if viewpoint_diagram_DDiagram236 is not None else set()
        self.viewpoint_diagram_DDiagram238 = viewpoint_diagram_DDiagram238 if viewpoint_diagram_DDiagram238 is not None else set()
        self.viewpoint_diagram_DDiagram240 = viewpoint_diagram_DDiagram240 if viewpoint_diagram_DDiagram240 is not None else set()
        self.viewpoint_diagram_DDiagram242 = viewpoint_diagram_DDiagram242
        self.viewpoint_diagram_DDiagram244 = viewpoint_diagram_DDiagram244 if viewpoint_diagram_DDiagram244 is not None else set()
        self.viewpoint_diagram_DDiagram246 = viewpoint_diagram_DDiagram246 if viewpoint_diagram_DDiagram246 is not None else set()
        self.viewpoint_diagram_DDiagram232 = viewpoint_diagram_DDiagram232 if viewpoint_diagram_DDiagram232 is not None else set()
        self.viewpoint_diagram_DDiagram234 = viewpoint_diagram_DDiagram234 if viewpoint_diagram_DDiagram234 is not None else set()
        self.viewpoint_diagram_DDiagram257 = viewpoint_diagram_DDiagram257 if viewpoint_diagram_DDiagram257 is not None else set()
        self.viewpoint_diagram_DDiagram249 = viewpoint_diagram_DDiagram249 if viewpoint_diagram_DDiagram249 is not None else set()
        self.viewpoint_diagram_DDiagram251 = viewpoint_diagram_DDiagram251 if viewpoint_diagram_DDiagram251 is not None else set()
        self.viewpoint_diagram_DDiagram253 = viewpoint_diagram_DDiagram253
        self.viewpoint_diagram_DDiagram255 = viewpoint_diagram_DDiagram255 if viewpoint_diagram_DDiagram255 is not None else set()
        
        pass
    @property
    def isInLayoutingMode(self):
        return self.__isInLayoutingMode

    @isInLayoutingMode.setter
    def isInLayoutingMode(self, isInLayoutingMode: bool):
        self.__isInLayoutingMode = isInLayoutingMode


    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info


    @property
    def synchronized(self):
        return self.__synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self.__synchronized = synchronized


    @property
    def headerHeight(self):
        return self.__headerHeight

    @headerHeight.setter
    def headerHeight(self, headerHeight: int):
        self.__headerHeight = headerHeight


    @property
    def viewpoint_diagram_DDiagram227(self):
        return self.__viewpoint_diagram_DDiagram227

    @viewpoint_diagram_DDiagram227.setter
    def viewpoint_diagram_DDiagram227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram227", None)
        self.__viewpoint_diagram_DDiagram227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagramElement228"):
                    opp_val = getattr(item, "DDiagramElement228", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagramElement228", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagramElement228"):
                    opp_val = getattr(item, "DDiagramElement228", None)
                    
                    setattr(item, "DDiagramElement228", self)
                    

    @property
    def viewpoint_diagram_DDiagram242(self):
        return self.__viewpoint_diagram_DDiagram242

    @viewpoint_diagram_DDiagram242.setter
    def viewpoint_diagram_DDiagram242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram242", None)
        self.__viewpoint_diagram_DDiagram242 = value
        
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
    def viewpoint_diagram_DDiagram257(self):
        return self.__viewpoint_diagram_DDiagram257

    @viewpoint_diagram_DDiagram257.setter
    def viewpoint_diagram_DDiagram257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram257", None)
        self.__viewpoint_diagram_DDiagram257 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagramElement258"):
                    opp_val = getattr(item, "DDiagramElement258", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagramElement258", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagramElement258"):
                    opp_val = getattr(item, "DDiagramElement258", None)
                    
                    setattr(item, "DDiagramElement258", self)
                    

    @property
    def viewpoint_diagram_DDiagram238(self):
        return self.__viewpoint_diagram_DDiagram238

    @viewpoint_diagram_DDiagram238.setter
    def viewpoint_diagram_DDiagram238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram238", None)
        self.__viewpoint_diagram_DDiagram238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DNodeListElement"):
                    opp_val = getattr(item, "DNodeListElement", None)
                    
                    if opp_val == self:
                        setattr(item, "DNodeListElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DNodeListElement"):
                    opp_val = getattr(item, "DNodeListElement", None)
                    
                    setattr(item, "DNodeListElement", self)
                    

    @property
    def viewpoint_diagram_DDiagram255(self):
        return self.__viewpoint_diagram_DDiagram255

    @viewpoint_diagram_DDiagram255.setter
    def viewpoint_diagram_DDiagram255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram255", None)
        self.__viewpoint_diagram_DDiagram255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_Layer"):
                    opp_val = getattr(item, "description_Layer", None)
                    
                    if opp_val == self:
                        setattr(item, "description_Layer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_Layer"):
                    opp_val = getattr(item, "description_Layer", None)
                    
                    setattr(item, "description_Layer", self)
                    

    @property
    def viewpoint_diagram_DDiagram246(self):
        return self.__viewpoint_diagram_DDiagram246

    @viewpoint_diagram_DDiagram246.setter
    def viewpoint_diagram_DDiagram246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram246", None)
        self.__viewpoint_diagram_DDiagram246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "filter_FilterDescription247"):
                    opp_val = getattr(item, "filter_FilterDescription247", None)
                    
                    if opp_val == self:
                        setattr(item, "filter_FilterDescription247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "filter_FilterDescription247"):
                    opp_val = getattr(item, "filter_FilterDescription247", None)
                    
                    setattr(item, "filter_FilterDescription247", self)
                    

    @property
    def viewpoint_diagram_DDiagram230(self):
        return self.__viewpoint_diagram_DDiagram230

    @viewpoint_diagram_DDiagram230.setter
    def viewpoint_diagram_DDiagram230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram230", None)
        self.__viewpoint_diagram_DDiagram230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_DiagramDescription"):
                opp_val = getattr(old_value, "description_DiagramDescription", None)
                if opp_val == self:
                    setattr(old_value, "description_DiagramDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_DiagramDescription"):
                opp_val = getattr(value, "description_DiagramDescription", None)
                setattr(value, "description_DiagramDescription", self)

    @property
    def viewpoint_diagram_DDiagram232(self):
        return self.__viewpoint_diagram_DDiagram232

    @viewpoint_diagram_DDiagram232.setter
    def viewpoint_diagram_DDiagram232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram232", None)
        self.__viewpoint_diagram_DDiagram232 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagram"):
                    opp_val = getattr(item, "DDiagram", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagram"):
                    opp_val = getattr(item, "DDiagram", None)
                    
                    setattr(item, "DDiagram", self)
                    

    @property
    def viewpoint_diagram_DDiagram240(self):
        return self.__viewpoint_diagram_DDiagram240

    @viewpoint_diagram_DDiagram240.setter
    def viewpoint_diagram_DDiagram240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram240", None)
        self.__viewpoint_diagram_DDiagram240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagramElementContainer"):
                    opp_val = getattr(item, "DDiagramElementContainer", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagramElementContainer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagramElementContainer"):
                    opp_val = getattr(item, "DDiagramElementContainer", None)
                    
                    setattr(item, "DDiagramElementContainer", self)
                    

    @property
    def viewpoint_diagram_DDiagram251(self):
        return self.__viewpoint_diagram_DDiagram251

    @viewpoint_diagram_DDiagram251.setter
    def viewpoint_diagram_DDiagram251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram251", None)
        self.__viewpoint_diagram_DDiagram251 = value if value is not None else set()
        
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
    def viewpoint_diagram_DDiagram236(self):
        return self.__viewpoint_diagram_DDiagram236

    @viewpoint_diagram_DDiagram236.setter
    def viewpoint_diagram_DDiagram236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram236", None)
        self.__viewpoint_diagram_DDiagram236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DNode"):
                    opp_val = getattr(item, "DNode", None)
                    
                    if opp_val == self:
                        setattr(item, "DNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DNode"):
                    opp_val = getattr(item, "DNode", None)
                    
                    setattr(item, "DNode", self)
                    

    @property
    def viewpoint_diagram_DDiagram244(self):
        return self.__viewpoint_diagram_DDiagram244

    @viewpoint_diagram_DDiagram244.setter
    def viewpoint_diagram_DDiagram244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram244", None)
        self.__viewpoint_diagram_DDiagram244 = value if value is not None else set()
        
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
    def viewpoint_diagram_DDiagram253(self):
        return self.__viewpoint_diagram_DDiagram253

    @viewpoint_diagram_DDiagram253.setter
    def viewpoint_diagram_DDiagram253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram253", None)
        self.__viewpoint_diagram_DDiagram253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FilterVariableHistory"):
                opp_val = getattr(old_value, "FilterVariableHistory", None)
                if opp_val == self:
                    setattr(old_value, "FilterVariableHistory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FilterVariableHistory"):
                opp_val = getattr(value, "FilterVariableHistory", None)
                setattr(value, "FilterVariableHistory", self)

    @property
    def viewpoint_diagram_DDiagram249(self):
        return self.__viewpoint_diagram_DDiagram249

    @viewpoint_diagram_DDiagram249.setter
    def viewpoint_diagram_DDiagram249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram249", None)
        self.__viewpoint_diagram_DDiagram249 = value if value is not None else set()
        
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
    def viewpoint_diagram_DDiagram(self):
        return self.__viewpoint_diagram_DDiagram

    @viewpoint_diagram_DDiagram.setter
    def viewpoint_diagram_DDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram", None)
        self.__viewpoint_diagram_DDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagramElement"):
                    opp_val = getattr(item, "DDiagramElement", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagramElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagramElement"):
                    opp_val = getattr(item, "DDiagramElement", None)
                    
                    setattr(item, "DDiagramElement", self)
                    

    @property
    def viewpoint_diagram_DDiagram234(self):
        return self.__viewpoint_diagram_DDiagram234

    @viewpoint_diagram_DDiagram234.setter
    def viewpoint_diagram_DDiagram234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_diagram_DDiagram__viewpoint_diagram_DDiagram234", None)
        self.__viewpoint_diagram_DDiagram234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DEdge"):
                    opp_val = getattr(item, "DEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "DEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DEdge"):
                    opp_val = getattr(item, "DEdge", None)
                    
                    setattr(item, "DEdge", self)
                    

    def getContainersFromMapping(self, viewpoint_mapping) :
        # TODO: Implement getContainersFromMapping method
        pass

    def clean(self):
        # TODO: Implement clean method
        pass

    def findDiagramElements(self, viewpoint_semanticElement, viewpoint_type) :
        # TODO: Implement findDiagramElements method
        pass

    def getEdgesFromMapping(self, viewpoint_mapping) :
        # TODO: Implement getEdgesFromMapping method
        pass

    def getNodesFromMapping(self, viewpoint_mapping) :
        # TODO: Implement getNodesFromMapping method
        pass

class viewpoint_tool_ToolEntry(description_DocumentedElement, description_IdentifiedElement):

    pass
class viewpoint_tool_ToolSection(description_DocumentedElement, description_IdentifiedElement):

    def __init__(self, icon: str, viewpoint_tool_ToolSection617: set["tool_ToolGroupExtension"] = None, viewpoint_tool_ToolSection: set["tool_ToolEntry"] = None, viewpoint_tool_ToolSection609: set["tool_ToolSection"] = None, viewpoint_tool_ToolSection612: set["tool_PopupMenu"] = None, viewpoint_tool_ToolSection614: set["tool_ToolEntry"] = None):
        self.icon = icon
        self.viewpoint_tool_ToolSection617 = viewpoint_tool_ToolSection617 if viewpoint_tool_ToolSection617 is not None else set()
        self.viewpoint_tool_ToolSection = viewpoint_tool_ToolSection if viewpoint_tool_ToolSection is not None else set()
        self.viewpoint_tool_ToolSection609 = viewpoint_tool_ToolSection609 if viewpoint_tool_ToolSection609 is not None else set()
        self.viewpoint_tool_ToolSection612 = viewpoint_tool_ToolSection612 if viewpoint_tool_ToolSection612 is not None else set()
        self.viewpoint_tool_ToolSection614 = viewpoint_tool_ToolSection614 if viewpoint_tool_ToolSection614 is not None else set()
        
        pass
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon


    @property
    def viewpoint_tool_ToolSection609(self):
        return self.__viewpoint_tool_ToolSection609

    @viewpoint_tool_ToolSection609.setter
    def viewpoint_tool_ToolSection609(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolSection__viewpoint_tool_ToolSection609", None)
        self.__viewpoint_tool_ToolSection609 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolSection610"):
                    opp_val = getattr(item, "tool_ToolSection610", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolSection610", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolSection610"):
                    opp_val = getattr(item, "tool_ToolSection610", None)
                    
                    setattr(item, "tool_ToolSection610", self)
                    

    @property
    def viewpoint_tool_ToolSection614(self):
        return self.__viewpoint_tool_ToolSection614

    @viewpoint_tool_ToolSection614.setter
    def viewpoint_tool_ToolSection614(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolSection__viewpoint_tool_ToolSection614", None)
        self.__viewpoint_tool_ToolSection614 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolEntry615"):
                    opp_val = getattr(item, "tool_ToolEntry615", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolEntry615", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolEntry615"):
                    opp_val = getattr(item, "tool_ToolEntry615", None)
                    
                    setattr(item, "tool_ToolEntry615", self)
                    

    @property
    def viewpoint_tool_ToolSection(self):
        return self.__viewpoint_tool_ToolSection

    @viewpoint_tool_ToolSection.setter
    def viewpoint_tool_ToolSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolSection__viewpoint_tool_ToolSection", None)
        self.__viewpoint_tool_ToolSection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolEntry607"):
                    opp_val = getattr(item, "tool_ToolEntry607", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolEntry607", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolEntry607"):
                    opp_val = getattr(item, "tool_ToolEntry607", None)
                    
                    setattr(item, "tool_ToolEntry607", self)
                    

    @property
    def viewpoint_tool_ToolSection612(self):
        return self.__viewpoint_tool_ToolSection612

    @viewpoint_tool_ToolSection612.setter
    def viewpoint_tool_ToolSection612(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolSection__viewpoint_tool_ToolSection612", None)
        self.__viewpoint_tool_ToolSection612 = value if value is not None else set()
        
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
    def viewpoint_tool_ToolSection617(self):
        return self.__viewpoint_tool_ToolSection617

    @viewpoint_tool_ToolSection617.setter
    def viewpoint_tool_ToolSection617(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolSection__viewpoint_tool_ToolSection617", None)
        self.__viewpoint_tool_ToolSection617 = value if value is not None else set()
        
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
                    

class viewpoint_description_EdgeMapping(description_IEdgeMapping, description_DocumentedElement, description_DiagramElementMapping):

    def __init__(self, targetFinderExpression: str, sourceFinderExpression: str, domainClass: str, useDomainElement: bool, pathExpression: str, targetExpression: str, viewpoint_description_EdgeMapping: set["description_DiagramElementMapping"] = None, viewpoint_description_EdgeMapping513: set["description_DiagramElementMapping"] = None, viewpoint_description_EdgeMapping520: set["tool_ReconnectEdgeDescription"] = None, viewpoint_description_EdgeMapping522: set["description_AbstractNodeMapping"] = None, viewpoint_description_EdgeMapping516: "style_EdgeStyleDescription" = None, viewpoint_description_EdgeMapping518: set["description_ConditionalEdgeStyleDescription"] = None, description_DiagramElementMapping: "viewpoint_tool_ContainerDropDescription" = None, description_DiagramElementMapping511: "viewpoint_description_EdgeMapping" = None, description_DiagramElementMapping653: "viewpoint_tool_EdgeCreationDescription" = None, description_DiagramElementMapping716: "viewpoint_tool_CreateView" = None, DiagramElementMapping: "viewpoint_tool_DoubleClickDescription" = None, description_DiagramElementMapping537: "viewpoint_description_MappingBasedDecoration" = None, description_DiagramElementMapping265: "viewpoint_diagram_DDiagramElement" = None, description_DiagramElementMapping514: "viewpoint_description_EdgeMapping" = None, description_DiagramElementMapping740: "viewpoint_validation_ViewValidationRule" = None, description_DiagramElementMapping724: "viewpoint_filter_MappingFilter" = None, description_DiagramElementMapping389: "viewpoint_diagram_DiagramElementMapping2ModelElement" = None, description_DiagramElementMapping457: "viewpoint_description_DiagramDescription" = None, description_DiagramElementMapping650: "viewpoint_tool_EdgeCreationDescription" = None, description_DiagramElementMapping551: "viewpoint_description_Layer" = None, description_IEdgeMapping524: "viewpoint_description_EdgeMappingImport" = None, description_IEdgeMapping: "viewpoint_diagram_DEdge" = None):
        self.targetFinderExpression = targetFinderExpression
        self.sourceFinderExpression = sourceFinderExpression
        self.domainClass = domainClass
        self.useDomainElement = useDomainElement
        self.pathExpression = pathExpression
        self.targetExpression = targetExpression
        self.viewpoint_description_EdgeMapping = viewpoint_description_EdgeMapping if viewpoint_description_EdgeMapping is not None else set()
        self.viewpoint_description_EdgeMapping513 = viewpoint_description_EdgeMapping513 if viewpoint_description_EdgeMapping513 is not None else set()
        self.viewpoint_description_EdgeMapping520 = viewpoint_description_EdgeMapping520 if viewpoint_description_EdgeMapping520 is not None else set()
        self.viewpoint_description_EdgeMapping522 = viewpoint_description_EdgeMapping522 if viewpoint_description_EdgeMapping522 is not None else set()
        self.viewpoint_description_EdgeMapping516 = viewpoint_description_EdgeMapping516
        self.viewpoint_description_EdgeMapping518 = viewpoint_description_EdgeMapping518 if viewpoint_description_EdgeMapping518 is not None else set()
        
        pass
    @property
    def targetFinderExpression(self):
        return self.__targetFinderExpression

    @targetFinderExpression.setter
    def targetFinderExpression(self, targetFinderExpression: str):
        self.__targetFinderExpression = targetFinderExpression


    @property
    def pathExpression(self):
        return self.__pathExpression

    @pathExpression.setter
    def pathExpression(self, pathExpression: str):
        self.__pathExpression = pathExpression


    @property
    def targetExpression(self):
        return self.__targetExpression

    @targetExpression.setter
    def targetExpression(self, targetExpression: str):
        self.__targetExpression = targetExpression


    @property
    def useDomainElement(self):
        return self.__useDomainElement

    @useDomainElement.setter
    def useDomainElement(self, useDomainElement: bool):
        self.__useDomainElement = useDomainElement


    @property
    def domainClass(self):
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass


    @property
    def sourceFinderExpression(self):
        return self.__sourceFinderExpression

    @sourceFinderExpression.setter
    def sourceFinderExpression(self, sourceFinderExpression: str):
        self.__sourceFinderExpression = sourceFinderExpression


    @property
    def viewpoint_description_EdgeMapping520(self):
        return self.__viewpoint_description_EdgeMapping520

    @viewpoint_description_EdgeMapping520.setter
    def viewpoint_description_EdgeMapping520(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_EdgeMapping__viewpoint_description_EdgeMapping520", None)
        self.__viewpoint_description_EdgeMapping520 = value if value is not None else set()
        
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
    def viewpoint_description_EdgeMapping513(self):
        return self.__viewpoint_description_EdgeMapping513

    @viewpoint_description_EdgeMapping513.setter
    def viewpoint_description_EdgeMapping513(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_EdgeMapping__viewpoint_description_EdgeMapping513", None)
        self.__viewpoint_description_EdgeMapping513 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_DiagramElementMapping514"):
                    opp_val = getattr(item, "description_DiagramElementMapping514", None)
                    
                    if opp_val == self:
                        setattr(item, "description_DiagramElementMapping514", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_DiagramElementMapping514"):
                    opp_val = getattr(item, "description_DiagramElementMapping514", None)
                    
                    setattr(item, "description_DiagramElementMapping514", self)
                    

    @property
    def viewpoint_description_EdgeMapping518(self):
        return self.__viewpoint_description_EdgeMapping518

    @viewpoint_description_EdgeMapping518.setter
    def viewpoint_description_EdgeMapping518(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_EdgeMapping__viewpoint_description_EdgeMapping518", None)
        self.__viewpoint_description_EdgeMapping518 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ConditionalEdgeStyleDescription"):
                    opp_val = getattr(item, "description_ConditionalEdgeStyleDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ConditionalEdgeStyleDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ConditionalEdgeStyleDescription"):
                    opp_val = getattr(item, "description_ConditionalEdgeStyleDescription", None)
                    
                    setattr(item, "description_ConditionalEdgeStyleDescription", self)
                    

    @property
    def viewpoint_description_EdgeMapping516(self):
        return self.__viewpoint_description_EdgeMapping516

    @viewpoint_description_EdgeMapping516.setter
    def viewpoint_description_EdgeMapping516(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_EdgeMapping__viewpoint_description_EdgeMapping516", None)
        self.__viewpoint_description_EdgeMapping516 = value
        
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
    def viewpoint_description_EdgeMapping(self):
        return self.__viewpoint_description_EdgeMapping

    @viewpoint_description_EdgeMapping.setter
    def viewpoint_description_EdgeMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_EdgeMapping__viewpoint_description_EdgeMapping", None)
        self.__viewpoint_description_EdgeMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_DiagramElementMapping511"):
                    opp_val = getattr(item, "description_DiagramElementMapping511", None)
                    
                    if opp_val == self:
                        setattr(item, "description_DiagramElementMapping511", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_DiagramElementMapping511"):
                    opp_val = getattr(item, "description_DiagramElementMapping511", None)
                    
                    setattr(item, "description_DiagramElementMapping511", self)
                    

    @property
    def viewpoint_description_EdgeMapping522(self):
        return self.__viewpoint_description_EdgeMapping522

    @viewpoint_description_EdgeMapping522.setter
    def viewpoint_description_EdgeMapping522(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_EdgeMapping__viewpoint_description_EdgeMapping522", None)
        self.__viewpoint_description_EdgeMapping522 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_AbstractNodeMapping"):
                    opp_val = getattr(item, "description_AbstractNodeMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "description_AbstractNodeMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_AbstractNodeMapping"):
                    opp_val = getattr(item, "description_AbstractNodeMapping", None)
                    
                    setattr(item, "description_AbstractNodeMapping", self)
                    

    def getEdgeTargetCandidates(self, viewpoint_semanticOrigin, viewpoint_viewPoint) :
        # TODO: Implement getEdgeTargetCandidates method
        pass

    def createEdge(self, viewpoint_semanticTarget, viewpoint_target, viewpoint_container, viewpoint_source) :
        # TODO: Implement createEdge method
        pass

    def getBestStyle(self, viewpoint_viewVariable, viewpoint_modelElement, viewpoint_containerVariable) :
        # TODO: Implement getBestStyle method
        pass

    def updateEdge(self, viewpoint_viewEdge):
        # TODO: Implement updateEdge method
        pass

    def getEdgeSourceCandidates(self, viewpoint_viewPoint, viewpoint_semanticOrigin) :
        # TODO: Implement getEdgeSourceCandidates method
        pass

class viewpoint_description_Layer(description_EndUserDocumentedElement, description_DocumentedElement, description_IdentifiedElement):

    def __init__(self, icon: str, viewpoint_description_Layer: set["description_NodeMapping"] = None, viewpoint_description_Layer541: set["description_EdgeMapping"] = None, viewpoint_description_Layer547: set["description_ContainerMapping"] = None, viewpoint_description_Layer550: set["description_DiagramElementMapping"] = None, viewpoint_description_Layer553: set["tool_AbstractToolDescription"] = None, viewpoint_description_Layer556: set["tool_ToolSection"] = None, viewpoint_description_Layer559: set["tool_AbstractToolDescription"] = None, viewpoint_description_Layer562: "DecorationDescriptionsSet" = None, viewpoint_description_Layer564: set["description_EdgeMapping"] = None, viewpoint_description_Layer544: set["description_EdgeMappingImport"] = None, viewpoint_description_Layer567: "Customization" = None):
        self.icon = icon
        self.viewpoint_description_Layer = viewpoint_description_Layer if viewpoint_description_Layer is not None else set()
        self.viewpoint_description_Layer541 = viewpoint_description_Layer541 if viewpoint_description_Layer541 is not None else set()
        self.viewpoint_description_Layer547 = viewpoint_description_Layer547 if viewpoint_description_Layer547 is not None else set()
        self.viewpoint_description_Layer550 = viewpoint_description_Layer550 if viewpoint_description_Layer550 is not None else set()
        self.viewpoint_description_Layer553 = viewpoint_description_Layer553 if viewpoint_description_Layer553 is not None else set()
        self.viewpoint_description_Layer556 = viewpoint_description_Layer556 if viewpoint_description_Layer556 is not None else set()
        self.viewpoint_description_Layer559 = viewpoint_description_Layer559 if viewpoint_description_Layer559 is not None else set()
        self.viewpoint_description_Layer562 = viewpoint_description_Layer562
        self.viewpoint_description_Layer564 = viewpoint_description_Layer564 if viewpoint_description_Layer564 is not None else set()
        self.viewpoint_description_Layer544 = viewpoint_description_Layer544 if viewpoint_description_Layer544 is not None else set()
        self.viewpoint_description_Layer567 = viewpoint_description_Layer567
        
        pass
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon


    @property
    def viewpoint_description_Layer550(self):
        return self.__viewpoint_description_Layer550

    @viewpoint_description_Layer550.setter
    def viewpoint_description_Layer550(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer550", None)
        self.__viewpoint_description_Layer550 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_DiagramElementMapping551"):
                    opp_val = getattr(item, "description_DiagramElementMapping551", None)
                    
                    if opp_val == self:
                        setattr(item, "description_DiagramElementMapping551", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_DiagramElementMapping551"):
                    opp_val = getattr(item, "description_DiagramElementMapping551", None)
                    
                    setattr(item, "description_DiagramElementMapping551", self)
                    

    @property
    def viewpoint_description_Layer567(self):
        return self.__viewpoint_description_Layer567

    @viewpoint_description_Layer567.setter
    def viewpoint_description_Layer567(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer567", None)
        self.__viewpoint_description_Layer567 = value
        
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
    def viewpoint_description_Layer553(self):
        return self.__viewpoint_description_Layer553

    @viewpoint_description_Layer553.setter
    def viewpoint_description_Layer553(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer553", None)
        self.__viewpoint_description_Layer553 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription554"):
                    opp_val = getattr(item, "tool_AbstractToolDescription554", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription554", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription554"):
                    opp_val = getattr(item, "tool_AbstractToolDescription554", None)
                    
                    setattr(item, "tool_AbstractToolDescription554", self)
                    

    @property
    def viewpoint_description_Layer562(self):
        return self.__viewpoint_description_Layer562

    @viewpoint_description_Layer562.setter
    def viewpoint_description_Layer562(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer562", None)
        self.__viewpoint_description_Layer562 = value
        
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
    def viewpoint_description_Layer559(self):
        return self.__viewpoint_description_Layer559

    @viewpoint_description_Layer559.setter
    def viewpoint_description_Layer559(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer559", None)
        self.__viewpoint_description_Layer559 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_AbstractToolDescription560"):
                    opp_val = getattr(item, "tool_AbstractToolDescription560", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_AbstractToolDescription560", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_AbstractToolDescription560"):
                    opp_val = getattr(item, "tool_AbstractToolDescription560", None)
                    
                    setattr(item, "tool_AbstractToolDescription560", self)
                    

    @property
    def viewpoint_description_Layer541(self):
        return self.__viewpoint_description_Layer541

    @viewpoint_description_Layer541.setter
    def viewpoint_description_Layer541(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer541", None)
        self.__viewpoint_description_Layer541 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_EdgeMapping542"):
                    opp_val = getattr(item, "description_EdgeMapping542", None)
                    
                    if opp_val == self:
                        setattr(item, "description_EdgeMapping542", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_EdgeMapping542"):
                    opp_val = getattr(item, "description_EdgeMapping542", None)
                    
                    setattr(item, "description_EdgeMapping542", self)
                    

    @property
    def viewpoint_description_Layer564(self):
        return self.__viewpoint_description_Layer564

    @viewpoint_description_Layer564.setter
    def viewpoint_description_Layer564(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer564", None)
        self.__viewpoint_description_Layer564 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_EdgeMapping565"):
                    opp_val = getattr(item, "description_EdgeMapping565", None)
                    
                    if opp_val == self:
                        setattr(item, "description_EdgeMapping565", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_EdgeMapping565"):
                    opp_val = getattr(item, "description_EdgeMapping565", None)
                    
                    setattr(item, "description_EdgeMapping565", self)
                    

    @property
    def viewpoint_description_Layer556(self):
        return self.__viewpoint_description_Layer556

    @viewpoint_description_Layer556.setter
    def viewpoint_description_Layer556(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer556", None)
        self.__viewpoint_description_Layer556 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_ToolSection557"):
                    opp_val = getattr(item, "tool_ToolSection557", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_ToolSection557", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_ToolSection557"):
                    opp_val = getattr(item, "tool_ToolSection557", None)
                    
                    setattr(item, "tool_ToolSection557", self)
                    

    @property
    def viewpoint_description_Layer544(self):
        return self.__viewpoint_description_Layer544

    @viewpoint_description_Layer544.setter
    def viewpoint_description_Layer544(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer544", None)
        self.__viewpoint_description_Layer544 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_EdgeMappingImport545"):
                    opp_val = getattr(item, "description_EdgeMappingImport545", None)
                    
                    if opp_val == self:
                        setattr(item, "description_EdgeMappingImport545", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_EdgeMappingImport545"):
                    opp_val = getattr(item, "description_EdgeMappingImport545", None)
                    
                    setattr(item, "description_EdgeMappingImport545", self)
                    

    @property
    def viewpoint_description_Layer(self):
        return self.__viewpoint_description_Layer

    @viewpoint_description_Layer.setter
    def viewpoint_description_Layer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer", None)
        self.__viewpoint_description_Layer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_NodeMapping539"):
                    opp_val = getattr(item, "description_NodeMapping539", None)
                    
                    if opp_val == self:
                        setattr(item, "description_NodeMapping539", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_NodeMapping539"):
                    opp_val = getattr(item, "description_NodeMapping539", None)
                    
                    setattr(item, "description_NodeMapping539", self)
                    

    @property
    def viewpoint_description_Layer547(self):
        return self.__viewpoint_description_Layer547

    @viewpoint_description_Layer547.setter
    def viewpoint_description_Layer547(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Layer__viewpoint_description_Layer547", None)
        self.__viewpoint_description_Layer547 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "description_ContainerMapping548"):
                    opp_val = getattr(item, "description_ContainerMapping548", None)
                    
                    if opp_val == self:
                        setattr(item, "description_ContainerMapping548", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_ContainerMapping548"):
                    opp_val = getattr(item, "description_ContainerMapping548", None)
                    
                    setattr(item, "description_ContainerMapping548", self)
                    

class viewpoint_description_Viewpoint(description_EndUserDocumentedElement, description_Component, description_DocumentedElement, description_IdentifiedElement):

    def __init__(self, modelFileExtension: str, icon: str, conflicts: str, reuses: str, customizes: str, viewpoint_description_Viewpoint73: set["RepresentationDescription"] = None, viewpoint_description_Viewpoint75: set["RepresentationExtensionDescription"] = None, viewpoint_description_Viewpoint77: set["JavaExtension"] = None, viewpoint_description_Viewpoint79: set["MetamodelExtensionSetting"] = None, viewpoint_description_Viewpoint81: set["FeatureExtensionDescription"] = None, viewpoint_description_Viewpoint84: set["RepresentationTemplate"] = None, viewpoint_description_Viewpoint: "validation_ValidationSet" = None):
        self.modelFileExtension = modelFileExtension
        self.icon = icon
        self.conflicts = conflicts
        self.reuses = reuses
        self.customizes = customizes
        self.viewpoint_description_Viewpoint73 = viewpoint_description_Viewpoint73 if viewpoint_description_Viewpoint73 is not None else set()
        self.viewpoint_description_Viewpoint75 = viewpoint_description_Viewpoint75 if viewpoint_description_Viewpoint75 is not None else set()
        self.viewpoint_description_Viewpoint77 = viewpoint_description_Viewpoint77 if viewpoint_description_Viewpoint77 is not None else set()
        self.viewpoint_description_Viewpoint79 = viewpoint_description_Viewpoint79 if viewpoint_description_Viewpoint79 is not None else set()
        self.viewpoint_description_Viewpoint81 = viewpoint_description_Viewpoint81 if viewpoint_description_Viewpoint81 is not None else set()
        self.viewpoint_description_Viewpoint84 = viewpoint_description_Viewpoint84 if viewpoint_description_Viewpoint84 is not None else set()
        self.viewpoint_description_Viewpoint = viewpoint_description_Viewpoint
        
        pass
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon


    @property
    def modelFileExtension(self):
        return self.__modelFileExtension

    @modelFileExtension.setter
    def modelFileExtension(self, modelFileExtension: str):
        self.__modelFileExtension = modelFileExtension


    @property
    def reuses(self):
        return self.__reuses

    @reuses.setter
    def reuses(self, reuses: str):
        self.__reuses = reuses


    @property
    def conflicts(self):
        return self.__conflicts

    @conflicts.setter
    def conflicts(self, conflicts: str):
        self.__conflicts = conflicts


    @property
    def customizes(self):
        return self.__customizes

    @customizes.setter
    def customizes(self, customizes: str):
        self.__customizes = customizes


    @property
    def viewpoint_description_Viewpoint73(self):
        return self.__viewpoint_description_Viewpoint73

    @viewpoint_description_Viewpoint73.setter
    def viewpoint_description_Viewpoint73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint73", None)
        self.__viewpoint_description_Viewpoint73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RepresentationDescription"):
                    opp_val = getattr(item, "RepresentationDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "RepresentationDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepresentationDescription"):
                    opp_val = getattr(item, "RepresentationDescription", None)
                    
                    setattr(item, "RepresentationDescription", self)
                    

    @property
    def viewpoint_description_Viewpoint(self):
        return self.__viewpoint_description_Viewpoint

    @viewpoint_description_Viewpoint.setter
    def viewpoint_description_Viewpoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint", None)
        self.__viewpoint_description_Viewpoint = value
        
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
    def viewpoint_description_Viewpoint81(self):
        return self.__viewpoint_description_Viewpoint81

    @viewpoint_description_Viewpoint81.setter
    def viewpoint_description_Viewpoint81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint81", None)
        self.__viewpoint_description_Viewpoint81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureExtensionDescription82"):
                    opp_val = getattr(item, "FeatureExtensionDescription82", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureExtensionDescription82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureExtensionDescription82"):
                    opp_val = getattr(item, "FeatureExtensionDescription82", None)
                    
                    setattr(item, "FeatureExtensionDescription82", self)
                    

    @property
    def viewpoint_description_Viewpoint75(self):
        return self.__viewpoint_description_Viewpoint75

    @viewpoint_description_Viewpoint75.setter
    def viewpoint_description_Viewpoint75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint75", None)
        self.__viewpoint_description_Viewpoint75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RepresentationExtensionDescription"):
                    opp_val = getattr(item, "RepresentationExtensionDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "RepresentationExtensionDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepresentationExtensionDescription"):
                    opp_val = getattr(item, "RepresentationExtensionDescription", None)
                    
                    setattr(item, "RepresentationExtensionDescription", self)
                    

    @property
    def viewpoint_description_Viewpoint84(self):
        return self.__viewpoint_description_Viewpoint84

    @viewpoint_description_Viewpoint84.setter
    def viewpoint_description_Viewpoint84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint84", None)
        self.__viewpoint_description_Viewpoint84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RepresentationTemplate"):
                    opp_val = getattr(item, "RepresentationTemplate", None)
                    
                    if opp_val == self:
                        setattr(item, "RepresentationTemplate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepresentationTemplate"):
                    opp_val = getattr(item, "RepresentationTemplate", None)
                    
                    setattr(item, "RepresentationTemplate", self)
                    

    @property
    def viewpoint_description_Viewpoint79(self):
        return self.__viewpoint_description_Viewpoint79

    @viewpoint_description_Viewpoint79.setter
    def viewpoint_description_Viewpoint79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint79", None)
        self.__viewpoint_description_Viewpoint79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MetamodelExtensionSetting"):
                    opp_val = getattr(item, "MetamodelExtensionSetting", None)
                    
                    if opp_val == self:
                        setattr(item, "MetamodelExtensionSetting", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MetamodelExtensionSetting"):
                    opp_val = getattr(item, "MetamodelExtensionSetting", None)
                    
                    setattr(item, "MetamodelExtensionSetting", self)
                    

    @property
    def viewpoint_description_Viewpoint77(self):
        return self.__viewpoint_description_Viewpoint77

    @viewpoint_description_Viewpoint77.setter
    def viewpoint_description_Viewpoint77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint77", None)
        self.__viewpoint_description_Viewpoint77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "JavaExtension"):
                    opp_val = getattr(item, "JavaExtension", None)
                    
                    if opp_val == self:
                        setattr(item, "JavaExtension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "JavaExtension"):
                    opp_val = getattr(item, "JavaExtension", None)
                    
                    setattr(item, "JavaExtension", self)
                    

    def initView(self, viewpoint_model):
        # TODO: Implement initView method
        pass

class viewpoint_DRepresentation(description_DModelElement, description_DocumentedElement, DRefreshable):

    def __init__(self, name: str, viewpoint_DRepresentation: set["viewpoint_DRepresentationElement"] = None, viewpoint_DRepresentation24: set["viewpoint_DRepresentationElement"] = None, viewpoint_DRepresentation27: set["AnnotationEntry"] = None, viewpoint_DRepresentation38: "viewpoint_DView" = None, viewpoint_DRepresentation41: "viewpoint_DView" = None, viewpoint_DRepresentation44: "viewpoint_DView" = None, viewpoint_DRepresentation33: "viewpoint_DView" = None):
        self.name = name
        self.viewpoint_DRepresentation = viewpoint_DRepresentation if viewpoint_DRepresentation is not None else set()
        self.viewpoint_DRepresentation24 = viewpoint_DRepresentation24 if viewpoint_DRepresentation24 is not None else set()
        self.viewpoint_DRepresentation27 = viewpoint_DRepresentation27 if viewpoint_DRepresentation27 is not None else set()
        self.viewpoint_DRepresentation38 = viewpoint_DRepresentation38
        self.viewpoint_DRepresentation41 = viewpoint_DRepresentation41
        self.viewpoint_DRepresentation44 = viewpoint_DRepresentation44
        self.viewpoint_DRepresentation33 = viewpoint_DRepresentation33
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def viewpoint_DRepresentation38(self):
        return self.__viewpoint_DRepresentation38

    @viewpoint_DRepresentation38.setter
    def viewpoint_DRepresentation38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation38", None)
        self.__viewpoint_DRepresentation38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DView37"):
                opp_val = getattr(old_value, "viewpoint_DView37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DView37"):
                opp_val = getattr(value, "viewpoint_DView37", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DView37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DRepresentation33(self):
        return self.__viewpoint_DRepresentation33

    @viewpoint_DRepresentation33.setter
    def viewpoint_DRepresentation33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation33", None)
        self.__viewpoint_DRepresentation33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DView32"):
                opp_val = getattr(old_value, "viewpoint_DView32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DView32"):
                opp_val = getattr(value, "viewpoint_DView32", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DView32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DRepresentation41(self):
        return self.__viewpoint_DRepresentation41

    @viewpoint_DRepresentation41.setter
    def viewpoint_DRepresentation41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation41", None)
        self.__viewpoint_DRepresentation41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DView40"):
                opp_val = getattr(old_value, "viewpoint_DView40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DView40"):
                opp_val = getattr(value, "viewpoint_DView40", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DView40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DRepresentation24(self):
        return self.__viewpoint_DRepresentation24

    @viewpoint_DRepresentation24.setter
    def viewpoint_DRepresentation24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation24", None)
        self.__viewpoint_DRepresentation24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DRepresentationElement25"):
                    opp_val = getattr(item, "viewpoint_DRepresentationElement25", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DRepresentationElement25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DRepresentationElement25"):
                    opp_val = getattr(item, "viewpoint_DRepresentationElement25", None)
                    
                    setattr(item, "viewpoint_DRepresentationElement25", self)
                    

    @property
    def viewpoint_DRepresentation44(self):
        return self.__viewpoint_DRepresentation44

    @viewpoint_DRepresentation44.setter
    def viewpoint_DRepresentation44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation44", None)
        self.__viewpoint_DRepresentation44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DView43"):
                opp_val = getattr(old_value, "viewpoint_DView43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DView43"):
                opp_val = getattr(value, "viewpoint_DView43", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DView43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DRepresentation(self):
        return self.__viewpoint_DRepresentation

    @viewpoint_DRepresentation.setter
    def viewpoint_DRepresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation", None)
        self.__viewpoint_DRepresentation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DRepresentationElement"):
                    opp_val = getattr(item, "viewpoint_DRepresentationElement", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DRepresentationElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DRepresentationElement"):
                    opp_val = getattr(item, "viewpoint_DRepresentationElement", None)
                    
                    setattr(item, "viewpoint_DRepresentationElement", self)
                    

    @property
    def viewpoint_DRepresentation27(self):
        return self.__viewpoint_DRepresentation27

    @viewpoint_DRepresentation27.setter
    def viewpoint_DRepresentation27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation27", None)
        self.__viewpoint_DRepresentation27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AnnotationEntry"):
                    opp_val = getattr(item, "AnnotationEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "AnnotationEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AnnotationEntry"):
                    opp_val = getattr(item, "AnnotationEntry", None)
                    
                    setattr(item, "AnnotationEntry", self)
                    

    def createContents(self, viewpoint_rootElement):
        # TODO: Implement createContents method
        pass

    def updateContent(self):
        # TODO: Implement updateContent method
        pass

class viewpoint_DSemanticDecorator(ABC):

    pass
class DDiagramSet:

    pass
class DView:

    pass
class viewpoint_DRepresentationContainer(DView):

    def __init__(self, viewpoint_DRepresentationContainer: set["DDiagramSet"] = None, viewpoint_DRepresentationContainer18: set["viewpoint_EObject"] = None):
        self.viewpoint_DRepresentationContainer = viewpoint_DRepresentationContainer if viewpoint_DRepresentationContainer is not None else set()
        self.viewpoint_DRepresentationContainer18 = viewpoint_DRepresentationContainer18 if viewpoint_DRepresentationContainer18 is not None else set()
        
        pass
    @property
    def viewpoint_DRepresentationContainer(self):
        return self.__viewpoint_DRepresentationContainer

    @viewpoint_DRepresentationContainer.setter
    def viewpoint_DRepresentationContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationContainer__viewpoint_DRepresentationContainer", None)
        self.__viewpoint_DRepresentationContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DDiagramSet"):
                    opp_val = getattr(item, "DDiagramSet", None)
                    
                    if opp_val == self:
                        setattr(item, "DDiagramSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DDiagramSet"):
                    opp_val = getattr(item, "DDiagramSet", None)
                    
                    setattr(item, "DDiagramSet", self)
                    

    @property
    def viewpoint_DRepresentationContainer18(self):
        return self.__viewpoint_DRepresentationContainer18

    @viewpoint_DRepresentationContainer18.setter
    def viewpoint_DRepresentationContainer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationContainer__viewpoint_DRepresentationContainer18", None)
        self.__viewpoint_DRepresentationContainer18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_EObject19"):
                    opp_val = getattr(item, "viewpoint_EObject19", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_EObject19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_EObject19"):
                    opp_val = getattr(item, "viewpoint_EObject19", None)
                    
                    setattr(item, "viewpoint_EObject19", self)
                    

    def addSemanticDiagram(self, viewpoint_diagram):
        # TODO: Implement addSemanticDiagram method
        pass

class viewpoint_DContainer(ABC):

    pass
class viewpoint_DMappingBased(ABC):

    def __init__(self):
        
        pass
    def getMapping(self) :
        # TODO: Implement getMapping method
        pass

class viewpoint_DLabelled(ABC):

    pass
class viewpoint_DRefreshable(ABC):

    def __init__(self):
        
        pass
    def refresh(self):
        # TODO: Implement refresh method
        pass

class viewpoint_DStylizable(ABC):

    def __init__(self):
        
        pass
    def getStyle(self) :
        # TODO: Implement getStyle method
        pass

class viewpoint_DNavigationLink(ABC):

    def __init__(self, targetType: str, label: str, viewpoint_DNavigationLink: "viewpoint_DNavigable" = None):
        self.targetType = targetType
        self.label = label
        self.viewpoint_DNavigationLink = viewpoint_DNavigationLink
        
        pass
    @property
    def targetType(self):
        return self.__targetType

    @targetType.setter
    def targetType(self, targetType: str):
        self.__targetType = targetType


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def viewpoint_DNavigationLink(self):
        return self.__viewpoint_DNavigationLink

    @viewpoint_DNavigationLink.setter
    def viewpoint_DNavigationLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DNavigationLink__viewpoint_DNavigationLink", None)
        self.__viewpoint_DNavigationLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DNavigable"):
                opp_val = getattr(old_value, "viewpoint_DNavigable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DNavigable"):
                opp_val = getattr(value, "viewpoint_DNavigable", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DNavigable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def isAvailable(self) :
        # TODO: Implement isAvailable method
        pass

class viewpoint_DNavigable(ABC):

    pass
class viewpoint_DValidable(ABC):

    def __init__(self):
        
        pass
    def validate(self) :
        # TODO: Implement validate method
        pass

class FeatureExtensionDescription:

    pass
class viewpoint_DFeatureExtension(ABC):

    pass
class viewpoint_DView(DRefreshable):

    def __init__(self, initialized: bool, viewpoint_DView: "viewpoint_DAnalysis" = None, viewpoint_DView10: "viewpoint_DAnalysis" = None, viewpoint_DView35: "viewpoint_MetaModelExtension" = None, viewpoint_DView37: set["viewpoint_DRepresentation"] = None, viewpoint_DView40: set["viewpoint_DRepresentation"] = None, viewpoint_DView43: set["viewpoint_DRepresentation"] = None, viewpoint_DView46: "Viewpoint" = None, viewpoint_DView32: set["viewpoint_DRepresentation"] = None):
        self.initialized = initialized
        self.viewpoint_DView = viewpoint_DView
        self.viewpoint_DView10 = viewpoint_DView10
        self.viewpoint_DView35 = viewpoint_DView35
        self.viewpoint_DView37 = viewpoint_DView37 if viewpoint_DView37 is not None else set()
        self.viewpoint_DView40 = viewpoint_DView40 if viewpoint_DView40 is not None else set()
        self.viewpoint_DView43 = viewpoint_DView43 if viewpoint_DView43 is not None else set()
        self.viewpoint_DView46 = viewpoint_DView46
        self.viewpoint_DView32 = viewpoint_DView32 if viewpoint_DView32 is not None else set()
        
        pass
    @property
    def initialized(self):
        return self.__initialized

    @initialized.setter
    def initialized(self, initialized: bool):
        self.__initialized = initialized


    @property
    def viewpoint_DView46(self):
        return self.__viewpoint_DView46

    @viewpoint_DView46.setter
    def viewpoint_DView46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DView__viewpoint_DView46", None)
        self.__viewpoint_DView46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Viewpoint"):
                opp_val = getattr(old_value, "Viewpoint", None)
                if opp_val == self:
                    setattr(old_value, "Viewpoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Viewpoint"):
                opp_val = getattr(value, "Viewpoint", None)
                setattr(value, "Viewpoint", self)

    @property
    def viewpoint_DView37(self):
        return self.__viewpoint_DView37

    @viewpoint_DView37.setter
    def viewpoint_DView37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DView__viewpoint_DView37", None)
        self.__viewpoint_DView37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DRepresentation38"):
                    opp_val = getattr(item, "viewpoint_DRepresentation38", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DRepresentation38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DRepresentation38"):
                    opp_val = getattr(item, "viewpoint_DRepresentation38", None)
                    
                    setattr(item, "viewpoint_DRepresentation38", self)
                    

    @property
    def viewpoint_DView(self):
        return self.__viewpoint_DView

    @viewpoint_DView.setter
    def viewpoint_DView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DView__viewpoint_DView", None)
        self.__viewpoint_DView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DAnalysis7"):
                opp_val = getattr(old_value, "viewpoint_DAnalysis7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DAnalysis7"):
                opp_val = getattr(value, "viewpoint_DAnalysis7", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DAnalysis7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DView35(self):
        return self.__viewpoint_DView35

    @viewpoint_DView35.setter
    def viewpoint_DView35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DView__viewpoint_DView35", None)
        self.__viewpoint_DView35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_MetaModelExtension"):
                opp_val = getattr(old_value, "viewpoint_MetaModelExtension", None)
                if opp_val == self:
                    setattr(old_value, "viewpoint_MetaModelExtension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_MetaModelExtension"):
                opp_val = getattr(value, "viewpoint_MetaModelExtension", None)
                setattr(value, "viewpoint_MetaModelExtension", self)

    @property
    def viewpoint_DView43(self):
        return self.__viewpoint_DView43

    @viewpoint_DView43.setter
    def viewpoint_DView43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DView__viewpoint_DView43", None)
        self.__viewpoint_DView43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DRepresentation44"):
                    opp_val = getattr(item, "viewpoint_DRepresentation44", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DRepresentation44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DRepresentation44"):
                    opp_val = getattr(item, "viewpoint_DRepresentation44", None)
                    
                    setattr(item, "viewpoint_DRepresentation44", self)
                    

    @property
    def viewpoint_DView10(self):
        return self.__viewpoint_DView10

    @viewpoint_DView10.setter
    def viewpoint_DView10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DView__viewpoint_DView10", None)
        self.__viewpoint_DView10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DAnalysis9"):
                opp_val = getattr(old_value, "viewpoint_DAnalysis9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DAnalysis9"):
                opp_val = getattr(value, "viewpoint_DAnalysis9", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DAnalysis9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DView32(self):
        return self.__viewpoint_DView32

    @viewpoint_DView32.setter
    def viewpoint_DView32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DView__viewpoint_DView32", None)
        self.__viewpoint_DView32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DRepresentation33"):
                    opp_val = getattr(item, "viewpoint_DRepresentation33", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DRepresentation33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DRepresentation33"):
                    opp_val = getattr(item, "viewpoint_DRepresentation33", None)
                    
                    setattr(item, "viewpoint_DRepresentation33", self)
                    

    @property
    def viewpoint_DView40(self):
        return self.__viewpoint_DView40

    @viewpoint_DView40.setter
    def viewpoint_DView40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DView__viewpoint_DView40", None)
        self.__viewpoint_DView40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DRepresentation41"):
                    opp_val = getattr(item, "viewpoint_DRepresentation41", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DRepresentation41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DRepresentation41"):
                    opp_val = getattr(item, "viewpoint_DRepresentation41", None)
                    
                    setattr(item, "viewpoint_DRepresentation41", self)
                    

class DAnnotationEntry:

    pass
class viewpoint_EObject:

    pass
class viewpoint_DAnalysis:

    def __init__(self, version: str, viewpoint_DAnalysis: "viewpoint_DAnalysis" = None, viewpoint_DAnalysis0: set["viewpoint_DAnalysis"] = None, viewpoint_DAnalysis3: set["viewpoint_EObject"] = None, viewpoint_DAnalysis5: set["DAnnotationEntry"] = None, viewpoint_DAnalysis7: set["viewpoint_DView"] = None, viewpoint_DAnalysis9: set["viewpoint_DView"] = None, viewpoint_DAnalysis12: set["viewpoint_DFeatureExtension"] = None, viewpoint_DAnalysis60: "viewpoint_DAnalysisSessionEObject" = None):
        self.version = version
        self.viewpoint_DAnalysis = viewpoint_DAnalysis
        self.viewpoint_DAnalysis0 = viewpoint_DAnalysis0 if viewpoint_DAnalysis0 is not None else set()
        self.viewpoint_DAnalysis3 = viewpoint_DAnalysis3 if viewpoint_DAnalysis3 is not None else set()
        self.viewpoint_DAnalysis5 = viewpoint_DAnalysis5 if viewpoint_DAnalysis5 is not None else set()
        self.viewpoint_DAnalysis7 = viewpoint_DAnalysis7 if viewpoint_DAnalysis7 is not None else set()
        self.viewpoint_DAnalysis9 = viewpoint_DAnalysis9 if viewpoint_DAnalysis9 is not None else set()
        self.viewpoint_DAnalysis12 = viewpoint_DAnalysis12 if viewpoint_DAnalysis12 is not None else set()
        self.viewpoint_DAnalysis60 = viewpoint_DAnalysis60
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def viewpoint_DAnalysis9(self):
        return self.__viewpoint_DAnalysis9

    @viewpoint_DAnalysis9.setter
    def viewpoint_DAnalysis9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysis__viewpoint_DAnalysis9", None)
        self.__viewpoint_DAnalysis9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DView10"):
                    opp_val = getattr(item, "viewpoint_DView10", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DView10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DView10"):
                    opp_val = getattr(item, "viewpoint_DView10", None)
                    
                    setattr(item, "viewpoint_DView10", self)
                    

    @property
    def viewpoint_DAnalysis60(self):
        return self.__viewpoint_DAnalysis60

    @viewpoint_DAnalysis60.setter
    def viewpoint_DAnalysis60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysis__viewpoint_DAnalysis60", None)
        self.__viewpoint_DAnalysis60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DAnalysisSessionEObject59"):
                opp_val = getattr(old_value, "viewpoint_DAnalysisSessionEObject59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DAnalysisSessionEObject59"):
                opp_val = getattr(value, "viewpoint_DAnalysisSessionEObject59", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DAnalysisSessionEObject59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DAnalysis12(self):
        return self.__viewpoint_DAnalysis12

    @viewpoint_DAnalysis12.setter
    def viewpoint_DAnalysis12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysis__viewpoint_DAnalysis12", None)
        self.__viewpoint_DAnalysis12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DFeatureExtension"):
                    opp_val = getattr(item, "viewpoint_DFeatureExtension", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DFeatureExtension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DFeatureExtension"):
                    opp_val = getattr(item, "viewpoint_DFeatureExtension", None)
                    
                    setattr(item, "viewpoint_DFeatureExtension", self)
                    

    @property
    def viewpoint_DAnalysis7(self):
        return self.__viewpoint_DAnalysis7

    @viewpoint_DAnalysis7.setter
    def viewpoint_DAnalysis7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysis__viewpoint_DAnalysis7", None)
        self.__viewpoint_DAnalysis7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DView"):
                    opp_val = getattr(item, "viewpoint_DView", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DView"):
                    opp_val = getattr(item, "viewpoint_DView", None)
                    
                    setattr(item, "viewpoint_DView", self)
                    

    @property
    def viewpoint_DAnalysis5(self):
        return self.__viewpoint_DAnalysis5

    @viewpoint_DAnalysis5.setter
    def viewpoint_DAnalysis5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysis__viewpoint_DAnalysis5", None)
        self.__viewpoint_DAnalysis5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DAnnotationEntry"):
                    opp_val = getattr(item, "DAnnotationEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "DAnnotationEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DAnnotationEntry"):
                    opp_val = getattr(item, "DAnnotationEntry", None)
                    
                    setattr(item, "DAnnotationEntry", self)
                    

    @property
    def viewpoint_DAnalysis0(self):
        return self.__viewpoint_DAnalysis0

    @viewpoint_DAnalysis0.setter
    def viewpoint_DAnalysis0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysis__viewpoint_DAnalysis0", None)
        self.__viewpoint_DAnalysis0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DAnalysis"):
                    opp_val = getattr(item, "viewpoint_DAnalysis", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DAnalysis", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DAnalysis"):
                    opp_val = getattr(item, "viewpoint_DAnalysis", None)
                    
                    setattr(item, "viewpoint_DAnalysis", self)
                    

    @property
    def viewpoint_DAnalysis(self):
        return self.__viewpoint_DAnalysis

    @viewpoint_DAnalysis.setter
    def viewpoint_DAnalysis(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysis__viewpoint_DAnalysis", None)
        self.__viewpoint_DAnalysis = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DAnalysis0"):
                opp_val = getattr(old_value, "viewpoint_DAnalysis0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DAnalysis0"):
                opp_val = getattr(value, "viewpoint_DAnalysis0", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DAnalysis0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DAnalysis3(self):
        return self.__viewpoint_DAnalysis3

    @viewpoint_DAnalysis3.setter
    def viewpoint_DAnalysis3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysis__viewpoint_DAnalysis3", None)
        self.__viewpoint_DAnalysis3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_EObject"):
                    opp_val = getattr(item, "viewpoint_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_EObject"):
                    opp_val = getattr(item, "viewpoint_EObject", None)
                    
                    setattr(item, "viewpoint_EObject", self)
                    
