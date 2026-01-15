from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SystemColors(Enum):
    black = "black"
    blue = "blue"
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
class Position(Enum):
    SOUTH_WEST = "SOUTH_WEST"
    SOUTH_EAST = "SOUTH_EAST"
    CENTER = "CENTER"
    NORTH = "NORTH"
    WEST = "WEST"
    SOUTH = "SOUTH"
    EAST = "EAST"
    NORTH_WEST = "NORTH_WEST"
    NORTH_EAST = "NORTH_EAST"
class LabelAlignment(Enum):
    CENTER = "CENTER"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
class ERROR_LEVEL(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
class FontFormat(Enum):
    underline = "underline"
    strike_through = "strike_through"
    italic = "italic"
    bold = "bold"
class DecorationDistributionDirection(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
class DragSource(Enum):
    DIAGRAM = "DIAGRAM"
    PROJECT_EXPLORER = "PROJECT_EXPLORER"
    BOTH = "BOTH"
class SyncStatus(Enum):
    dirty = "dirty"
    sync = "sync"


############################################
# Definition of Classes
############################################

class RepresentationElementMapping:

    pass
class InformationSection:

    pass
class viewpoint_audit_TemplateInformationSection(InformationSection):

    def __init__(self, templatePath: str):
        self.templatePath = templatePath
        
    @property
    def templatePath(self) -> str:
        return self.__templatePath

    @templatePath.setter
    def templatePath(self, templatePath: str):
        self.__templatePath = templatePath

class viewpoint_audit_InformationSection(ABC):

    def __init__(self):
        
    def getContent(self, eObj: str) -> str:
        # TODO: Implement getContent method
        pass

class viewpoint_validation_ValidationFix:

    def __init__(self, name: str, viewpoint_validation_ValidationFix: "tool_InitialOperation" = None):
        self.name = name
        self.viewpoint_validation_ValidationFix = viewpoint_validation_ValidationFix
        
    @property
    def name(self) -> str:
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
            if hasattr(old_value, "tool_InitialOperation224"):
                opp_val = getattr(old_value, "tool_InitialOperation224", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation224"):
                opp_val = getattr(value, "tool_InitialOperation224", None)
                setattr(value, "tool_InitialOperation224", self)

class viewpoint_validation_RuleAudit:

    def __init__(self, auditExpression: str):
        self.auditExpression = auditExpression
        
    @property
    def auditExpression(self) -> str:
        return self.__auditExpression

    @auditExpression.setter
    def auditExpression(self, auditExpression: str):
        self.__auditExpression = auditExpression

class tool_Default:

    pass
class ValidationRule:

    pass
class viewpoint_validation_ViewValidationRule(ValidationRule):

    pass
class viewpoint_validation_SemanticValidationRule(ValidationRule):

    def __init__(self, targetClass: str):
        self.targetClass = targetClass
        
    @property
    def targetClass(self) -> str:
        return self.__targetClass

    @targetClass.setter
    def targetClass(self, targetClass: str):
        self.__targetClass = targetClass

class validation_ValidationFix:

    pass
class validation_RuleAudit:

    pass
class validation_ValidationRule:

    pass
class DocumentedElement:

    pass
class viewpoint_validation_ValidationSet(DocumentedElement):

    def __init__(self, name: str, viewpoint_validation_ValidationSet: set["validation_ValidationRule"] = None, viewpoint_validation_ValidationSet214: set["validation_ValidationRule"] = None, viewpoint_validation_ValidationSet217: set["validation_ValidationRule"] = None):
        self.name = name
        self.viewpoint_validation_ValidationSet = viewpoint_validation_ValidationSet if viewpoint_validation_ValidationSet is not None else set()
        self.viewpoint_validation_ValidationSet214 = viewpoint_validation_ValidationSet214 if viewpoint_validation_ValidationSet214 is not None else set()
        self.viewpoint_validation_ValidationSet217 = viewpoint_validation_ValidationSet217 if viewpoint_validation_ValidationSet217 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def viewpoint_validation_ValidationSet214(self):
        return self.__viewpoint_validation_ValidationSet214

    @viewpoint_validation_ValidationSet214.setter
    def viewpoint_validation_ValidationSet214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_validation_ValidationSet__viewpoint_validation_ValidationSet214", None)
        self.__viewpoint_validation_ValidationSet214 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "validation_ValidationRule215"):
                    opp_val = getattr(item, "validation_ValidationRule215", None)
                    
                    if opp_val == self:
                        setattr(item, "validation_ValidationRule215", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "validation_ValidationRule215"):
                    opp_val = getattr(item, "validation_ValidationRule215", None)
                    
                    setattr(item, "validation_ValidationRule215", self)
                    

    @property
    def viewpoint_validation_ValidationSet217(self):
        return self.__viewpoint_validation_ValidationSet217

    @viewpoint_validation_ValidationSet217.setter
    def viewpoint_validation_ValidationSet217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_validation_ValidationSet__viewpoint_validation_ValidationSet217", None)
        self.__viewpoint_validation_ValidationSet217 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "validation_ValidationRule218"):
                    opp_val = getattr(item, "validation_ValidationRule218", None)
                    
                    if opp_val == self:
                        setattr(item, "validation_ValidationRule218", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "validation_ValidationRule218"):
                    opp_val = getattr(item, "validation_ValidationRule218", None)
                    
                    setattr(item, "validation_ValidationRule218", self)
                    

class tool_Case:

    pass
class viewpoint_tool_SwitchChild(ABC):

    pass
class SwitchChild:

    pass
class viewpoint_tool_Default(SwitchChild):

    pass
class viewpoint_tool_Case(SwitchChild):

    def __init__(self, conditionExpression: str):
        self.conditionExpression = conditionExpression
        
    @property
    def conditionExpression(self) -> str:
        return self.__conditionExpression

    @conditionExpression.setter
    def conditionExpression(self, conditionExpression: str):
        self.__conditionExpression = conditionExpression

class viewpoint_tool_FeatureChangeListener:

    def __init__(self, domainClass: str, featureName: str):
        self.domainClass = domainClass
        self.featureName = featureName
        
    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

class tool_FeatureChangeListener:

    pass
class viewpoint_tool_ToolFilterDescription:

    def __init__(self, precondition: str, elementsToListen: str, viewpoint_tool_ToolFilterDescription: set["tool_FeatureChangeListener"] = None):
        self.precondition = precondition
        self.elementsToListen = elementsToListen
        self.viewpoint_tool_ToolFilterDescription = viewpoint_tool_ToolFilterDescription if viewpoint_tool_ToolFilterDescription is not None else set()
        
    @property
    def precondition(self) -> str:
        return self.__precondition

    @precondition.setter
    def precondition(self, precondition: str):
        self.__precondition = precondition

    @property
    def elementsToListen(self) -> str:
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

class tool_viewpoint_EObject:

    pass
class ModelOperation:

    pass
class viewpoint_tool_Switch(ModelOperation):

    pass
class viewpoint_tool_ContainerModelOperation(ModelOperation):

    pass
class viewpoint_tool_EditMaskVariables:

    def __init__(self, mask: str):
        self.mask = mask
        
    @property
    def mask(self) -> str:
        return self.__mask

    @mask.setter
    def mask(self, mask: str):
        self.__mask = mask

class ContainerModelOperation:

    pass
class viewpoint_tool_For(ContainerModelOperation):

    def __init__(self, expression: str, iteratorName: str):
        self.expression = expression
        self.iteratorName = iteratorName
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def iteratorName(self) -> str:
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName

class viewpoint_tool_DeleteView(ContainerModelOperation):

    pass
class viewpoint_tool_MoveElement(ContainerModelOperation):

    def __init__(self, newContainerExpression: str, featureName: str):
        self.newContainerExpression = newContainerExpression
        self.featureName = featureName
        
    @property
    def newContainerExpression(self) -> str:
        return self.__newContainerExpression

    @newContainerExpression.setter
    def newContainerExpression(self, newContainerExpression: str):
        self.__newContainerExpression = newContainerExpression

    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

class viewpoint_tool_Unset(ContainerModelOperation):

    def __init__(self, featureName: str, elementExpression: str):
        self.featureName = featureName
        self.elementExpression = elementExpression
        
    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def elementExpression(self) -> str:
        return self.__elementExpression

    @elementExpression.setter
    def elementExpression(self, elementExpression: str):
        self.__elementExpression = elementExpression

class viewpoint_tool_ChangeContext(ContainerModelOperation):

    def __init__(self, browseExpression: str):
        self.browseExpression = browseExpression
        
    @property
    def browseExpression(self) -> str:
        return self.__browseExpression

    @browseExpression.setter
    def browseExpression(self, browseExpression: str):
        self.__browseExpression = browseExpression

class viewpoint_tool_SetObject(ContainerModelOperation):

    def __init__(self, featureName: str, viewpoint_tool_SetObject: "tool_viewpoint_EObject" = None):
        self.featureName = featureName
        self.viewpoint_tool_SetObject = viewpoint_tool_SetObject
        
    @property
    def featureName(self) -> str:
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

class viewpoint_tool_Let(ContainerModelOperation):

    def __init__(self, variableName: str, valueExpression: str):
        self.variableName = variableName
        self.valueExpression = valueExpression
        
    @property
    def valueExpression(self) -> str:
        return self.__valueExpression

    @valueExpression.setter
    def valueExpression(self, valueExpression: str):
        self.__valueExpression = valueExpression

    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

class viewpoint_tool_RemoveElement(ContainerModelOperation):

    pass
class viewpoint_tool_If(ContainerModelOperation):

    def __init__(self, conditionExpression: str):
        self.conditionExpression = conditionExpression
        
    @property
    def conditionExpression(self) -> str:
        return self.__conditionExpression

    @conditionExpression.setter
    def conditionExpression(self, conditionExpression: str):
        self.__conditionExpression = conditionExpression

class viewpoint_tool_SetValue(ContainerModelOperation):

    def __init__(self, featureName: str, valueExpression: str):
        self.featureName = featureName
        self.valueExpression = valueExpression
        
    @property
    def valueExpression(self) -> str:
        return self.__valueExpression

    @valueExpression.setter
    def valueExpression(self, valueExpression: str):
        self.__valueExpression = valueExpression

    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

class viewpoint_tool_CreateInstance(ContainerModelOperation):

    def __init__(self, typeName: str, referenceName: str, variableName: str):
        self.typeName = typeName
        self.referenceName = referenceName
        self.variableName = variableName
        
    @property
    def variableName(self) -> str:
        return self.__variableName

    @variableName.setter
    def variableName(self, variableName: str):
        self.__variableName = variableName

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def referenceName(self) -> str:
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
class description_AbstractVariable:

    pass
class tool_VariableContainer:

    pass
class viewpoint_tool_SelectContainerVariable(description_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ElementViewVariable(description_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ElementDropVariable(description_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ElementDeleteVariable(description_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ElementVariable(description_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_DropContainerVariable(description_AbstractVariable, tool_VariableContainer):

    pass
class viewpoint_tool_ContainerViewVariable(description_AbstractVariable, tool_VariableContainer):

    pass
class SubVariable:

    pass
class viewpoint_tool_VariableContainer(ABC):

    pass
class tool_ExternalJavaAction:

    pass
class tool_ExternalJavaActionParameter:

    pass
class tool_ContainerModelOperation:

    pass
class MenuItemDescription:

    pass
class viewpoint_tool_OperationAction(MenuItemDescription):

    pass
class tool_MenuItemDescription:

    pass
class viewpoint_tool_ExternalJavaActionCall(tool_MenuItemDescription, tool_ContainerModelOperation):

    pass
class viewpoint_tool_ExternalJavaAction(tool_MenuItemDescription, tool_ContainerModelOperation):

    def __init__(self, id: str, viewpoint_tool_ExternalJavaAction: set["tool_ExternalJavaActionParameter"] = None, tool_MenuItemDescription: "viewpoint_tool_MenuItemDescriptionReference", tool_MenuItemDescription194: "viewpoint_tool_PopupMenu"):
        self.id = id
        self.viewpoint_tool_ExternalJavaAction = viewpoint_tool_ExternalJavaAction if viewpoint_tool_ExternalJavaAction is not None else set()
        
    @property
    def id(self) -> str:
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
class tool_ElementSelectVariable:

    pass
class description_SelectionDescription:

    pass
class tool_AbstractToolDescription:

    pass
class viewpoint_tool_MenuItemDescription(tool_AbstractToolDescription, tool_MenuItemOrRef):

    def __init__(self, icon: str):
        self.icon = icon
        
    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

class viewpoint_tool_SelectionWizardDescription(tool_AbstractToolDescription, description_SelectionDescription):

    def __init__(self, iconPath: str, windowTitle: str, windowImagePath: str, viewpoint_tool_SelectionWizardDescription151: "tool_InitialOperation" = None, viewpoint_tool_SelectionWizardDescription: "tool_ElementSelectVariable" = None, viewpoint_tool_SelectionWizardDescription146: "tool_ContainerViewVariable" = None, viewpoint_tool_SelectionWizardDescription149: "tool_SelectContainerVariable" = None):
        self.iconPath = iconPath
        self.windowTitle = windowTitle
        self.windowImagePath = windowImagePath
        self.viewpoint_tool_SelectionWizardDescription151 = viewpoint_tool_SelectionWizardDescription151
        self.viewpoint_tool_SelectionWizardDescription = viewpoint_tool_SelectionWizardDescription
        self.viewpoint_tool_SelectionWizardDescription146 = viewpoint_tool_SelectionWizardDescription146
        self.viewpoint_tool_SelectionWizardDescription149 = viewpoint_tool_SelectionWizardDescription149
        
    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def windowTitle(self) -> str:
        return self.__windowTitle

    @windowTitle.setter
    def windowTitle(self, windowTitle: str):
        self.__windowTitle = windowTitle

    @property
    def windowImagePath(self) -> str:
        return self.__windowImagePath

    @windowImagePath.setter
    def windowImagePath(self, windowImagePath: str):
        self.__windowImagePath = windowImagePath

    @property
    def viewpoint_tool_SelectionWizardDescription149(self):
        return self.__viewpoint_tool_SelectionWizardDescription149

    @viewpoint_tool_SelectionWizardDescription149.setter
    def viewpoint_tool_SelectionWizardDescription149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_SelectionWizardDescription__viewpoint_tool_SelectionWizardDescription149", None)
        self.__viewpoint_tool_SelectionWizardDescription149 = value
        
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
    def viewpoint_tool_SelectionWizardDescription151(self):
        return self.__viewpoint_tool_SelectionWizardDescription151

    @viewpoint_tool_SelectionWizardDescription151.setter
    def viewpoint_tool_SelectionWizardDescription151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_SelectionWizardDescription__viewpoint_tool_SelectionWizardDescription151", None)
        self.__viewpoint_tool_SelectionWizardDescription151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation152"):
                opp_val = getattr(old_value, "tool_InitialOperation152", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation152"):
                opp_val = getattr(value, "tool_InitialOperation152", None)
                setattr(value, "tool_InitialOperation152", self)

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
    def viewpoint_tool_SelectionWizardDescription146(self):
        return self.__viewpoint_tool_SelectionWizardDescription146

    @viewpoint_tool_SelectionWizardDescription146.setter
    def viewpoint_tool_SelectionWizardDescription146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_SelectionWizardDescription__viewpoint_tool_SelectionWizardDescription146", None)
        self.__viewpoint_tool_SelectionWizardDescription146 = value
        
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

class MappingBasedToolDescription:

    pass
class viewpoint_tool_ToolDescription(MappingBasedToolDescription):

    def __init__(self, iconPath: str, viewpoint_tool_ToolDescription: "tool_ElementVariable" = None, viewpoint_tool_ToolDescription129: "tool_ElementViewVariable" = None, viewpoint_tool_ToolDescription131: "tool_InitialOperation" = None):
        self.iconPath = iconPath
        self.viewpoint_tool_ToolDescription = viewpoint_tool_ToolDescription
        self.viewpoint_tool_ToolDescription129 = viewpoint_tool_ToolDescription129
        self.viewpoint_tool_ToolDescription131 = viewpoint_tool_ToolDescription131
        
    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def viewpoint_tool_ToolDescription131(self):
        return self.__viewpoint_tool_ToolDescription131

    @viewpoint_tool_ToolDescription131.setter
    def viewpoint_tool_ToolDescription131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolDescription__viewpoint_tool_ToolDescription131", None)
        self.__viewpoint_tool_ToolDescription131 = value
        
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
    def viewpoint_tool_ToolDescription129(self):
        return self.__viewpoint_tool_ToolDescription129

    @viewpoint_tool_ToolDescription129.setter
    def viewpoint_tool_ToolDescription129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_ToolDescription__viewpoint_tool_ToolDescription129", None)
        self.__viewpoint_tool_ToolDescription129 = value
        
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
class viewpoint_tool_RepresentationCreationDescription(AbstractToolDescription):

    def __init__(self, titleExpression: str, browseExpression: str, viewpoint_tool_RepresentationCreationDescription: "RepresentationDescription" = None, viewpoint_tool_RepresentationCreationDescription167: "tool_InitialOperation" = None, viewpoint_tool_RepresentationCreationDescription170: "tool_ContainerViewVariable" = None, viewpoint_tool_RepresentationCreationDescription173: "tool_NameVariable" = None):
        self.titleExpression = titleExpression
        self.browseExpression = browseExpression
        self.viewpoint_tool_RepresentationCreationDescription = viewpoint_tool_RepresentationCreationDescription
        self.viewpoint_tool_RepresentationCreationDescription167 = viewpoint_tool_RepresentationCreationDescription167
        self.viewpoint_tool_RepresentationCreationDescription170 = viewpoint_tool_RepresentationCreationDescription170
        self.viewpoint_tool_RepresentationCreationDescription173 = viewpoint_tool_RepresentationCreationDescription173
        
    @property
    def titleExpression(self) -> str:
        return self.__titleExpression

    @titleExpression.setter
    def titleExpression(self, titleExpression: str):
        self.__titleExpression = titleExpression

    @property
    def browseExpression(self) -> str:
        return self.__browseExpression

    @browseExpression.setter
    def browseExpression(self, browseExpression: str):
        self.__browseExpression = browseExpression

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
            if hasattr(old_value, "RepresentationDescription165"):
                opp_val = getattr(old_value, "RepresentationDescription165", None)
                if opp_val == self:
                    setattr(old_value, "RepresentationDescription165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentationDescription165"):
                opp_val = getattr(value, "RepresentationDescription165", None)
                setattr(value, "RepresentationDescription165", self)

    @property
    def viewpoint_tool_RepresentationCreationDescription167(self):
        return self.__viewpoint_tool_RepresentationCreationDescription167

    @viewpoint_tool_RepresentationCreationDescription167.setter
    def viewpoint_tool_RepresentationCreationDescription167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationCreationDescription__viewpoint_tool_RepresentationCreationDescription167", None)
        self.__viewpoint_tool_RepresentationCreationDescription167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation168"):
                opp_val = getattr(old_value, "tool_InitialOperation168", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation168"):
                opp_val = getattr(value, "tool_InitialOperation168", None)
                setattr(value, "tool_InitialOperation168", self)

    @property
    def viewpoint_tool_RepresentationCreationDescription170(self):
        return self.__viewpoint_tool_RepresentationCreationDescription170

    @viewpoint_tool_RepresentationCreationDescription170.setter
    def viewpoint_tool_RepresentationCreationDescription170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationCreationDescription__viewpoint_tool_RepresentationCreationDescription170", None)
        self.__viewpoint_tool_RepresentationCreationDescription170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable171"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable171", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable171"):
                opp_val = getattr(value, "tool_ContainerViewVariable171", None)
                setattr(value, "tool_ContainerViewVariable171", self)

    @property
    def viewpoint_tool_RepresentationCreationDescription173(self):
        return self.__viewpoint_tool_RepresentationCreationDescription173

    @viewpoint_tool_RepresentationCreationDescription173.setter
    def viewpoint_tool_RepresentationCreationDescription173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationCreationDescription__viewpoint_tool_RepresentationCreationDescription173", None)
        self.__viewpoint_tool_RepresentationCreationDescription173 = value
        
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

    def getMappings(self) -> str:
        # TODO: Implement getMappings method
        pass

class viewpoint_tool_PopupMenu(AbstractToolDescription):

    pass
class viewpoint_tool_RepresentationNavigationDescription(AbstractToolDescription):

    def __init__(self, browseExpression: str, navigationNameExpression: str, viewpoint_tool_RepresentationNavigationDescription180: "tool_ElementSelectVariable" = None, viewpoint_tool_RepresentationNavigationDescription183: "tool_NameVariable" = None, viewpoint_tool_RepresentationNavigationDescription: "RepresentationDescription" = None, viewpoint_tool_RepresentationNavigationDescription177: "tool_ContainerViewVariable" = None):
        self.browseExpression = browseExpression
        self.navigationNameExpression = navigationNameExpression
        self.viewpoint_tool_RepresentationNavigationDescription180 = viewpoint_tool_RepresentationNavigationDescription180
        self.viewpoint_tool_RepresentationNavigationDescription183 = viewpoint_tool_RepresentationNavigationDescription183
        self.viewpoint_tool_RepresentationNavigationDescription = viewpoint_tool_RepresentationNavigationDescription
        self.viewpoint_tool_RepresentationNavigationDescription177 = viewpoint_tool_RepresentationNavigationDescription177
        
    @property
    def browseExpression(self) -> str:
        return self.__browseExpression

    @browseExpression.setter
    def browseExpression(self, browseExpression: str):
        self.__browseExpression = browseExpression

    @property
    def navigationNameExpression(self) -> str:
        return self.__navigationNameExpression

    @navigationNameExpression.setter
    def navigationNameExpression(self, navigationNameExpression: str):
        self.__navigationNameExpression = navigationNameExpression

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
            if hasattr(old_value, "RepresentationDescription175"):
                opp_val = getattr(old_value, "RepresentationDescription175", None)
                if opp_val == self:
                    setattr(old_value, "RepresentationDescription175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentationDescription175"):
                opp_val = getattr(value, "RepresentationDescription175", None)
                setattr(value, "RepresentationDescription175", self)

    @property
    def viewpoint_tool_RepresentationNavigationDescription177(self):
        return self.__viewpoint_tool_RepresentationNavigationDescription177

    @viewpoint_tool_RepresentationNavigationDescription177.setter
    def viewpoint_tool_RepresentationNavigationDescription177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationNavigationDescription__viewpoint_tool_RepresentationNavigationDescription177", None)
        self.__viewpoint_tool_RepresentationNavigationDescription177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable178"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable178", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable178"):
                opp_val = getattr(value, "tool_ContainerViewVariable178", None)
                setattr(value, "tool_ContainerViewVariable178", self)

    @property
    def viewpoint_tool_RepresentationNavigationDescription183(self):
        return self.__viewpoint_tool_RepresentationNavigationDescription183

    @viewpoint_tool_RepresentationNavigationDescription183.setter
    def viewpoint_tool_RepresentationNavigationDescription183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationNavigationDescription__viewpoint_tool_RepresentationNavigationDescription183", None)
        self.__viewpoint_tool_RepresentationNavigationDescription183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_NameVariable184"):
                opp_val = getattr(old_value, "tool_NameVariable184", None)
                if opp_val == self:
                    setattr(old_value, "tool_NameVariable184", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_NameVariable184"):
                opp_val = getattr(value, "tool_NameVariable184", None)
                setattr(value, "tool_NameVariable184", self)

    @property
    def viewpoint_tool_RepresentationNavigationDescription180(self):
        return self.__viewpoint_tool_RepresentationNavigationDescription180

    @viewpoint_tool_RepresentationNavigationDescription180.setter
    def viewpoint_tool_RepresentationNavigationDescription180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_RepresentationNavigationDescription__viewpoint_tool_RepresentationNavigationDescription180", None)
        self.__viewpoint_tool_RepresentationNavigationDescription180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementSelectVariable181"):
                opp_val = getattr(old_value, "tool_ElementSelectVariable181", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementSelectVariable181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementSelectVariable181"):
                opp_val = getattr(value, "tool_ElementSelectVariable181", None)
                setattr(value, "tool_ElementSelectVariable181", self)

    def getMappings(self) -> str:
        # TODO: Implement getMappings method
        pass

class viewpoint_tool_PaneBasedSelectionWizardDescription(AbstractToolDescription):

    def __init__(self, iconPath: str, windowTitle: str, windowImagePath: str, message: str, choiceOfValuesMessage: str, candidatesExpression: str, tree: bool, rootExpression: str, childrenExpression: str, selectedValuesMessage: str, preSelectedCandidatesExpression: str, viewpoint_tool_PaneBasedSelectionWizardDescription: "tool_ElementSelectVariable" = None, viewpoint_tool_PaneBasedSelectionWizardDescription156: "tool_ContainerViewVariable" = None, viewpoint_tool_PaneBasedSelectionWizardDescription159: "tool_SelectContainerVariable" = None, viewpoint_tool_PaneBasedSelectionWizardDescription162: "tool_InitialOperation" = None):
        self.iconPath = iconPath
        self.windowTitle = windowTitle
        self.windowImagePath = windowImagePath
        self.message = message
        self.choiceOfValuesMessage = choiceOfValuesMessage
        self.candidatesExpression = candidatesExpression
        self.tree = tree
        self.rootExpression = rootExpression
        self.childrenExpression = childrenExpression
        self.selectedValuesMessage = selectedValuesMessage
        self.preSelectedCandidatesExpression = preSelectedCandidatesExpression
        self.viewpoint_tool_PaneBasedSelectionWizardDescription = viewpoint_tool_PaneBasedSelectionWizardDescription
        self.viewpoint_tool_PaneBasedSelectionWizardDescription156 = viewpoint_tool_PaneBasedSelectionWizardDescription156
        self.viewpoint_tool_PaneBasedSelectionWizardDescription159 = viewpoint_tool_PaneBasedSelectionWizardDescription159
        self.viewpoint_tool_PaneBasedSelectionWizardDescription162 = viewpoint_tool_PaneBasedSelectionWizardDescription162
        
    @property
    def choiceOfValuesMessage(self) -> str:
        return self.__choiceOfValuesMessage

    @choiceOfValuesMessage.setter
    def choiceOfValuesMessage(self, choiceOfValuesMessage: str):
        self.__choiceOfValuesMessage = choiceOfValuesMessage

    @property
    def selectedValuesMessage(self) -> str:
        return self.__selectedValuesMessage

    @selectedValuesMessage.setter
    def selectedValuesMessage(self, selectedValuesMessage: str):
        self.__selectedValuesMessage = selectedValuesMessage

    @property
    def rootExpression(self) -> str:
        return self.__rootExpression

    @rootExpression.setter
    def rootExpression(self, rootExpression: str):
        self.__rootExpression = rootExpression

    @property
    def preSelectedCandidatesExpression(self) -> str:
        return self.__preSelectedCandidatesExpression

    @preSelectedCandidatesExpression.setter
    def preSelectedCandidatesExpression(self, preSelectedCandidatesExpression: str):
        self.__preSelectedCandidatesExpression = preSelectedCandidatesExpression

    @property
    def windowTitle(self) -> str:
        return self.__windowTitle

    @windowTitle.setter
    def windowTitle(self, windowTitle: str):
        self.__windowTitle = windowTitle

    @property
    def candidatesExpression(self) -> str:
        return self.__candidatesExpression

    @candidatesExpression.setter
    def candidatesExpression(self, candidatesExpression: str):
        self.__candidatesExpression = candidatesExpression

    @property
    def tree(self) -> bool:
        return self.__tree

    @tree.setter
    def tree(self, tree: bool):
        self.__tree = tree

    @property
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def windowImagePath(self) -> str:
        return self.__windowImagePath

    @windowImagePath.setter
    def windowImagePath(self, windowImagePath: str):
        self.__windowImagePath = windowImagePath

    @property
    def childrenExpression(self) -> str:
        return self.__childrenExpression

    @childrenExpression.setter
    def childrenExpression(self, childrenExpression: str):
        self.__childrenExpression = childrenExpression

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def viewpoint_tool_PaneBasedSelectionWizardDescription156(self):
        return self.__viewpoint_tool_PaneBasedSelectionWizardDescription156

    @viewpoint_tool_PaneBasedSelectionWizardDescription156.setter
    def viewpoint_tool_PaneBasedSelectionWizardDescription156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PaneBasedSelectionWizardDescription__viewpoint_tool_PaneBasedSelectionWizardDescription156", None)
        self.__viewpoint_tool_PaneBasedSelectionWizardDescription156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable157"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable157", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable157"):
                opp_val = getattr(value, "tool_ContainerViewVariable157", None)
                setattr(value, "tool_ContainerViewVariable157", self)

    @property
    def viewpoint_tool_PaneBasedSelectionWizardDescription162(self):
        return self.__viewpoint_tool_PaneBasedSelectionWizardDescription162

    @viewpoint_tool_PaneBasedSelectionWizardDescription162.setter
    def viewpoint_tool_PaneBasedSelectionWizardDescription162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PaneBasedSelectionWizardDescription__viewpoint_tool_PaneBasedSelectionWizardDescription162", None)
        self.__viewpoint_tool_PaneBasedSelectionWizardDescription162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation163"):
                opp_val = getattr(old_value, "tool_InitialOperation163", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation163"):
                opp_val = getattr(value, "tool_InitialOperation163", None)
                setattr(value, "tool_InitialOperation163", self)

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
            if hasattr(old_value, "tool_ElementSelectVariable154"):
                opp_val = getattr(old_value, "tool_ElementSelectVariable154", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementSelectVariable154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementSelectVariable154"):
                opp_val = getattr(value, "tool_ElementSelectVariable154", None)
                setattr(value, "tool_ElementSelectVariable154", self)

    @property
    def viewpoint_tool_PaneBasedSelectionWizardDescription159(self):
        return self.__viewpoint_tool_PaneBasedSelectionWizardDescription159

    @viewpoint_tool_PaneBasedSelectionWizardDescription159.setter
    def viewpoint_tool_PaneBasedSelectionWizardDescription159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PaneBasedSelectionWizardDescription__viewpoint_tool_PaneBasedSelectionWizardDescription159", None)
        self.__viewpoint_tool_PaneBasedSelectionWizardDescription159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_SelectContainerVariable160"):
                opp_val = getattr(old_value, "tool_SelectContainerVariable160", None)
                if opp_val == self:
                    setattr(old_value, "tool_SelectContainerVariable160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_SelectContainerVariable160"):
                opp_val = getattr(value, "tool_SelectContainerVariable160", None)
                setattr(value, "tool_SelectContainerVariable160", self)

class viewpoint_tool_MappingBasedToolDescription(AbstractToolDescription):

    pass
class tool_ContainerViewVariable:

    pass
class tool_DropContainerVariable:

    pass
class viewpoint_tool_PasteDescription(MappingBasedToolDescription):

    def __init__(self, viewpoint_tool_PasteDescription: "tool_DropContainerVariable" = None, viewpoint_tool_PasteDescription134: "tool_ContainerViewVariable" = None, viewpoint_tool_PasteDescription136: "tool_ElementViewVariable" = None, viewpoint_tool_PasteDescription139: "tool_ElementVariable" = None, viewpoint_tool_PasteDescription142: "tool_InitialOperation" = None):
        self.viewpoint_tool_PasteDescription = viewpoint_tool_PasteDescription
        self.viewpoint_tool_PasteDescription134 = viewpoint_tool_PasteDescription134
        self.viewpoint_tool_PasteDescription136 = viewpoint_tool_PasteDescription136
        self.viewpoint_tool_PasteDescription139 = viewpoint_tool_PasteDescription139
        self.viewpoint_tool_PasteDescription142 = viewpoint_tool_PasteDescription142
        
    @property
    def viewpoint_tool_PasteDescription139(self):
        return self.__viewpoint_tool_PasteDescription139

    @viewpoint_tool_PasteDescription139.setter
    def viewpoint_tool_PasteDescription139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PasteDescription__viewpoint_tool_PasteDescription139", None)
        self.__viewpoint_tool_PasteDescription139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementVariable140"):
                opp_val = getattr(old_value, "tool_ElementVariable140", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementVariable140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementVariable140"):
                opp_val = getattr(value, "tool_ElementVariable140", None)
                setattr(value, "tool_ElementVariable140", self)

    @property
    def viewpoint_tool_PasteDescription136(self):
        return self.__viewpoint_tool_PasteDescription136

    @viewpoint_tool_PasteDescription136.setter
    def viewpoint_tool_PasteDescription136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PasteDescription__viewpoint_tool_PasteDescription136", None)
        self.__viewpoint_tool_PasteDescription136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementViewVariable137"):
                opp_val = getattr(old_value, "tool_ElementViewVariable137", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementViewVariable137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementViewVariable137"):
                opp_val = getattr(value, "tool_ElementViewVariable137", None)
                setattr(value, "tool_ElementViewVariable137", self)

    @property
    def viewpoint_tool_PasteDescription142(self):
        return self.__viewpoint_tool_PasteDescription142

    @viewpoint_tool_PasteDescription142.setter
    def viewpoint_tool_PasteDescription142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PasteDescription__viewpoint_tool_PasteDescription142", None)
        self.__viewpoint_tool_PasteDescription142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_InitialOperation143"):
                opp_val = getattr(old_value, "tool_InitialOperation143", None)
                if opp_val == self:
                    setattr(old_value, "tool_InitialOperation143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_InitialOperation143"):
                opp_val = getattr(value, "tool_InitialOperation143", None)
                setattr(value, "tool_InitialOperation143", self)

    @property
    def viewpoint_tool_PasteDescription134(self):
        return self.__viewpoint_tool_PasteDescription134

    @viewpoint_tool_PasteDescription134.setter
    def viewpoint_tool_PasteDescription134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PasteDescription__viewpoint_tool_PasteDescription134", None)
        self.__viewpoint_tool_PasteDescription134 = value
        
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
    def viewpoint_tool_PasteDescription(self):
        return self.__viewpoint_tool_PasteDescription

    @viewpoint_tool_PasteDescription.setter
    def viewpoint_tool_PasteDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_tool_PasteDescription__viewpoint_tool_PasteDescription", None)
        self.__viewpoint_tool_PasteDescription = value
        
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

    def getContainers(self) -> str:
        # TODO: Implement getContainers method
        pass

class tool_InitialOperation:

    pass
class tool_ElementViewVariable:

    pass
class tool_ElementVariable:

    pass
class style_LabelBorderStyleDescription:

    pass
class viewpoint_style_LabelBorderStyles:

    pass
class BasicLabelStyleDescription:

    pass
class viewpoint_style_LabelStyleDescription(BasicLabelStyleDescription):

    def __init__(self, labelAlignment: str):
        self.labelAlignment = labelAlignment
        
    @property
    def labelAlignment(self) -> str:
        return self.__labelAlignment

    @labelAlignment.setter
    def labelAlignment(self, labelAlignment: str):
        self.__labelAlignment = labelAlignment

class tool_ToolFilterDescription:

    pass
class ToolEntry:

    pass
class viewpoint_tool_AbstractToolDescription(ToolEntry):

    def __init__(self, precondition: str, forceRefresh: bool, elementsToSelect: str, inverseSelectionOrder: bool, viewpoint_tool_AbstractToolDescription: set["tool_ToolFilterDescription"] = None):
        self.precondition = precondition
        self.forceRefresh = forceRefresh
        self.elementsToSelect = elementsToSelect
        self.inverseSelectionOrder = inverseSelectionOrder
        self.viewpoint_tool_AbstractToolDescription = viewpoint_tool_AbstractToolDescription if viewpoint_tool_AbstractToolDescription is not None else set()
        
    @property
    def inverseSelectionOrder(self) -> bool:
        return self.__inverseSelectionOrder

    @inverseSelectionOrder.setter
    def inverseSelectionOrder(self, inverseSelectionOrder: bool):
        self.__inverseSelectionOrder = inverseSelectionOrder

    @property
    def elementsToSelect(self) -> str:
        return self.__elementsToSelect

    @elementsToSelect.setter
    def elementsToSelect(self, elementsToSelect: str):
        self.__elementsToSelect = elementsToSelect

    @property
    def forceRefresh(self) -> bool:
        return self.__forceRefresh

    @forceRefresh.setter
    def forceRefresh(self, forceRefresh: bool):
        self.__forceRefresh = forceRefresh

    @property
    def precondition(self) -> str:
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
        
    @property
    def tooltipExpression(self) -> str:
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
        
    @property
    def cornerHeight(self) -> int:
        return self.__cornerHeight

    @cornerHeight.setter
    def cornerHeight(self, cornerHeight: int):
        self.__cornerHeight = cornerHeight

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cornerWidth(self) -> int:
        return self.__cornerWidth

    @cornerWidth.setter
    def cornerWidth(self, cornerWidth: int):
        self.__cornerWidth = cornerWidth

class viewpoint_description_AbstractVariable(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class viewpoint_description_DAnnotationEntry:

    def __init__(self, source: str, details: str):
        self.source = source
        self.details = details
        
    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def details(self) -> str:
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details

class viewpoint_style_BasicLabelStyleDescription:

    def __init__(self, labelSize: int, labelFormat: str, showIcon: bool, labelExpression: str, iconPath: str, viewpoint_style_BasicLabelStyleDescription: "ColorDescription" = None):
        self.labelSize = labelSize
        self.labelFormat = labelFormat
        self.showIcon = showIcon
        self.labelExpression = labelExpression
        self.iconPath = iconPath
        self.viewpoint_style_BasicLabelStyleDescription = viewpoint_style_BasicLabelStyleDescription
        
    @property
    def labelFormat(self) -> str:
        return self.__labelFormat

    @labelFormat.setter
    def labelFormat(self, labelFormat: str):
        self.__labelFormat = labelFormat

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
    def labelExpression(self) -> str:
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
class description_viewpoint_EDataType:

    pass
class description_SubVariable:

    pass
class viewpoint_tool_AcceleoVariable(description_SubVariable, tool_VariableContainer):

    def __init__(self, computationExpression: str):
        self.computationExpression = computationExpression
        
    @property
    def computationExpression(self) -> str:
        return self.__computationExpression

    @computationExpression.setter
    def computationExpression(self, computationExpression: str):
        self.__computationExpression = computationExpression

class description_InteractiveVariableDescription:

    pass
class viewpoint_tool_SelectModelElementVariable(description_InteractiveVariableDescription, description_SubVariable, description_SelectionDescription):

    pass
class viewpoint_description_TypedVariable(description_InteractiveVariableDescription, description_SubVariable):

    def __init__(self, defaultValueExpression: str, viewpoint_description_TypedVariable: "description_viewpoint_EDataType" = None):
        self.defaultValueExpression = defaultValueExpression
        self.viewpoint_description_TypedVariable = viewpoint_description_TypedVariable
        
    @property
    def defaultValueExpression(self) -> str:
        return self.__defaultValueExpression

    @defaultValueExpression.setter
    def defaultValueExpression(self, defaultValueExpression: str):
        self.__defaultValueExpression = defaultValueExpression

    @property
    def viewpoint_description_TypedVariable(self):
        return self.__viewpoint_description_TypedVariable

    @viewpoint_description_TypedVariable.setter
    def viewpoint_description_TypedVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_TypedVariable__viewpoint_description_TypedVariable", None)
        self.__viewpoint_description_TypedVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "description_viewpoint_EDataType"):
                opp_val = getattr(old_value, "description_viewpoint_EDataType", None)
                if opp_val == self:
                    setattr(old_value, "description_viewpoint_EDataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "description_viewpoint_EDataType"):
                opp_val = getattr(value, "description_viewpoint_EDataType", None)
                setattr(value, "description_viewpoint_EDataType", self)

class viewpoint_description_InteractiveVariableDescription(ABC):

    def __init__(self, userDocumentation: str):
        self.userDocumentation = userDocumentation
        
    @property
    def userDocumentation(self) -> str:
        return self.__userDocumentation

    @userDocumentation.setter
    def userDocumentation(self, userDocumentation: str):
        self.__userDocumentation = userDocumentation

class AbstractVariable:

    pass
class viewpoint_tool_NameVariable(AbstractVariable):

    pass
class viewpoint_tool_DialogVariable(AbstractVariable):

    def __init__(self, dialogPrompt: str):
        self.dialogPrompt = dialogPrompt
        
    @property
    def dialogPrompt(self) -> str:
        return self.__dialogPrompt

    @dialogPrompt.setter
    def dialogPrompt(self, dialogPrompt: str):
        self.__dialogPrompt = dialogPrompt

class viewpoint_tool_ElementSelectVariable(AbstractVariable):

    pass
class viewpoint_description_SubVariable(AbstractVariable):

    pass
class viewpoint_description_Environment:

    pass
class viewpoint_description_IdentifiedElement:

    def __init__(self, name: str, label: str):
        self.name = name
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class viewpoint_description_EndUserDocumentedElement(ABC):

    def __init__(self, endUserDocumentation: str):
        self.endUserDocumentation = endUserDocumentation
        
    @property
    def endUserDocumentation(self) -> str:
        return self.__endUserDocumentation

    @endUserDocumentation.setter
    def endUserDocumentation(self, endUserDocumentation: str):
        self.__endUserDocumentation = endUserDocumentation

class viewpoint_description_AnnotationEntry:

    def __init__(self, source: str, viewpoint_description_AnnotationEntry: "description_viewpoint_EObject" = None):
        self.source = source
        self.viewpoint_description_AnnotationEntry = viewpoint_description_AnnotationEntry
        
    @property
    def source(self) -> str:
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
        
    @property
    def name(self) -> str:
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
class ColorStep:

    pass
class viewpoint_description_UserColor(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class description_FixedColor:

    pass
class ColorDescription:

    pass
class viewpoint_description_FixedColor(ColorDescription):

    def __init__(self, red: int, green: int, blue: int, ColorDescription: "viewpoint_style_BasicLabelStyleDescription"):
        self.red = red
        self.green = green
        self.blue = blue
        
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
    def red(self) -> int:
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red

class viewpoint_description_ColorStep:

    def __init__(self, associatedValue: str, viewpoint_description_ColorStep: "FixedColor" = None):
        self.associatedValue = associatedValue
        self.viewpoint_description_ColorStep = viewpoint_description_ColorStep
        
    @property
    def associatedValue(self) -> str:
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

class description_UserColor:

    pass
class viewpoint_description_UserFixedColor(description_UserColor, description_FixedColor):

    pass
class description_ColorDescription:

    pass
class viewpoint_description_ComputedColor(description_UserColor, description_ColorDescription):

    def __init__(self, red: str, green: str, blue: str):
        self.red = red
        self.green = green
        self.blue = blue
        
    @property
    def red(self) -> str:
        return self.__red

    @red.setter
    def red(self, red: str):
        self.__red = red

    @property
    def blue(self) -> str:
        return self.__blue

    @blue.setter
    def blue(self, blue: str):
        self.__blue = blue

    @property
    def green(self) -> str:
        return self.__green

    @green.setter
    def green(self, green: str):
        self.__green = green

class viewpoint_description_InterpolatedColor(description_UserColor, description_ColorDescription):

    def __init__(self, colorValueComputationExpression: str, minValueComputationExpression: str, maxValueComputationExpression: str, viewpoint_description_InterpolatedColor: set["ColorStep"] = None):
        self.colorValueComputationExpression = colorValueComputationExpression
        self.minValueComputationExpression = minValueComputationExpression
        self.maxValueComputationExpression = maxValueComputationExpression
        self.viewpoint_description_InterpolatedColor = viewpoint_description_InterpolatedColor if viewpoint_description_InterpolatedColor is not None else set()
        
    @property
    def maxValueComputationExpression(self) -> str:
        return self.__maxValueComputationExpression

    @maxValueComputationExpression.setter
    def maxValueComputationExpression(self, maxValueComputationExpression: str):
        self.__maxValueComputationExpression = maxValueComputationExpression

    @property
    def colorValueComputationExpression(self) -> str:
        return self.__colorValueComputationExpression

    @colorValueComputationExpression.setter
    def colorValueComputationExpression(self, colorValueComputationExpression: str):
        self.__colorValueComputationExpression = colorValueComputationExpression

    @property
    def minValueComputationExpression(self) -> str:
        return self.__minValueComputationExpression

    @minValueComputationExpression.setter
    def minValueComputationExpression(self, minValueComputationExpression: str):
        self.__minValueComputationExpression = minValueComputationExpression

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
                    

class FixedColor:

    pass
class viewpoint_description_SystemColor(FixedColor):

    def __init__(self, name: str, FixedColor: "viewpoint_description_ColorStep"):
        self.name = name
        
    @property
    def name(self) -> str:
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
        
    @property
    def tree(self) -> bool:
        return self.__tree

    @tree.setter
    def tree(self, tree: bool):
        self.__tree = tree

    @property
    def candidatesExpression(self) -> str:
        return self.__candidatesExpression

    @candidatesExpression.setter
    def candidatesExpression(self, candidatesExpression: str):
        self.__candidatesExpression = candidatesExpression

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

    @property
    def rootExpression(self) -> str:
        return self.__rootExpression

    @rootExpression.setter
    def rootExpression(self, rootExpression: str):
        self.__rootExpression = rootExpression

    @property
    def childrenExpression(self) -> str:
        return self.__childrenExpression

    @childrenExpression.setter
    def childrenExpression(self, childrenExpression: str):
        self.__childrenExpression = childrenExpression

class viewpoint_description_EStructuralFeatureCustomization(ABC):

    def __init__(self, applyOnAll: bool, viewpoint_description_EStructuralFeatureCustomization: set["description_viewpoint_EObject"] = None):
        self.applyOnAll = applyOnAll
        self.viewpoint_description_EStructuralFeatureCustomization = viewpoint_description_EStructuralFeatureCustomization if viewpoint_description_EStructuralFeatureCustomization is not None else set()
        
    @property
    def applyOnAll(self) -> bool:
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
                    

class EStructuralFeatureCustomization:

    pass
class viewpoint_description_EAttributeCustomization(EStructuralFeatureCustomization):

    def __init__(self, attributeName: str, value: str, EStructuralFeatureCustomization103: "viewpoint_description_VSMElementCustomizationReuse", EStructuralFeatureCustomization: "viewpoint_description_VSMElementCustomization"):
        self.attributeName = attributeName
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def attributeName(self) -> str:
        return self.__attributeName

    @attributeName.setter
    def attributeName(self, attributeName: str):
        self.__attributeName = attributeName

class viewpoint_description_EReferenceCustomization(EStructuralFeatureCustomization):

    def __init__(self, referenceName: str, viewpoint_description_EReferenceCustomization: "description_viewpoint_EObject" = None, EStructuralFeatureCustomization103: "viewpoint_description_VSMElementCustomizationReuse", EStructuralFeatureCustomization: "viewpoint_description_VSMElementCustomization"):
        self.referenceName = referenceName
        self.viewpoint_description_EReferenceCustomization = viewpoint_description_EReferenceCustomization
        
    @property
    def referenceName(self) -> str:
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
class viewpoint_description_VSMElementCustomizationReuse(IVSMElementCustomization):

    pass
class viewpoint_description_VSMElementCustomization(IVSMElementCustomization):

    def __init__(self, predicateExpression: str, viewpoint_description_VSMElementCustomization: set["EStructuralFeatureCustomization"] = None, IVSMElementCustomization: "viewpoint_description_Customization"):
        self.predicateExpression = predicateExpression
        self.viewpoint_description_VSMElementCustomization = viewpoint_description_VSMElementCustomization if viewpoint_description_VSMElementCustomization is not None else set()
        
    @property
    def predicateExpression(self) -> str:
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
                    

class viewpoint_description_Customization:

    pass
class viewpoint_description_ConditionalStyleDescription(ABC):

    def __init__(self, predicateExpression: str):
        self.predicateExpression = predicateExpression
        
    @property
    def predicateExpression(self) -> str:
        return self.__predicateExpression

    @predicateExpression.setter
    def predicateExpression(self, predicateExpression: str):
        self.__predicateExpression = predicateExpression

    def checkPredicate(self, modelElement: str, containerVariable: str, viewVariable: str) -> bool:
        # TODO: Implement checkPredicate method
        pass

class description_viewpoint_EStringToStringMapEntry:

    pass
class viewpoint_description_DecorationDescription(ABC):

    def __init__(self, name: str, position: str, distributionDirection: str, preconditionExpression: str, imageExpression: str, tooltipExpression: str):
        self.name = name
        self.position = position
        self.distributionDirection = distributionDirection
        self.preconditionExpression = preconditionExpression
        self.imageExpression = imageExpression
        self.tooltipExpression = tooltipExpression
        
    @property
    def tooltipExpression(self) -> str:
        return self.__tooltipExpression

    @tooltipExpression.setter
    def tooltipExpression(self, tooltipExpression: str):
        self.__tooltipExpression = tooltipExpression

    @property
    def distributionDirection(self) -> str:
        return self.__distributionDirection

    @distributionDirection.setter
    def distributionDirection(self, distributionDirection: str):
        self.__distributionDirection = distributionDirection

    @property
    def imageExpression(self) -> str:
        return self.__imageExpression

    @imageExpression.setter
    def imageExpression(self, imageExpression: str):
        self.__imageExpression = imageExpression

    @property
    def preconditionExpression(self) -> str:
        return self.__preconditionExpression

    @preconditionExpression.setter
    def preconditionExpression(self, preconditionExpression: str):
        self.__preconditionExpression = preconditionExpression

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

class viewpoint_description_DecorationDescriptionsSet:

    pass
class tool_PasteDescription:

    pass
class viewpoint_description_PasteTargetDescription(ABC):

    pass
class viewpoint_description_RepresentationExtensionDescription(ABC):

    def __init__(self, name: str, viewpointURI: str, representationName: str, viewpoint_description_RepresentationExtensionDescription: set["description_viewpoint_EPackage"] = None):
        self.name = name
        self.viewpointURI = viewpointURI
        self.representationName = representationName
        self.viewpoint_description_RepresentationExtensionDescription = viewpoint_description_RepresentationExtensionDescription if viewpoint_description_RepresentationExtensionDescription is not None else set()
        
    @property
    def viewpointURI(self) -> str:
        return self.__viewpointURI

    @viewpointURI.setter
    def viewpointURI(self, viewpointURI: str):
        self.__viewpointURI = viewpointURI

    @property
    def representationName(self) -> str:
        return self.__representationName

    @representationName.setter
    def representationName(self, representationName: str):
        self.__representationName = representationName

    @property
    def name(self) -> str:
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
                if hasattr(item, "description_viewpoint_EPackage90"):
                    opp_val = getattr(item, "description_viewpoint_EPackage90", None)
                    
                    if opp_val == self:
                        setattr(item, "description_viewpoint_EPackage90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "description_viewpoint_EPackage90"):
                    opp_val = getattr(item, "description_viewpoint_EPackage90", None)
                    
                    setattr(item, "description_viewpoint_EPackage90", self)
                    

class viewpoint_description_DAnnotation:

    def __init__(self, source: str, viewpoint_description_DAnnotation: set["description_viewpoint_EStringToStringMapEntry"] = None):
        self.source = source
        self.viewpoint_description_DAnnotation = viewpoint_description_DAnnotation if viewpoint_description_DAnnotation is not None else set()
        
    @property
    def source(self) -> str:
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
class viewpoint_description_DModelElement(ABC):

    def __init__(self, viewpoint_description_DModelElement: set["DAnnotation"] = None):
        self.viewpoint_description_DModelElement = viewpoint_description_DModelElement if viewpoint_description_DModelElement is not None else set()
        
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
                    

    def getDAnnotation(self, source: str) -> str:
        # TODO: Implement getDAnnotation method
        pass

class viewpoint_description_DocumentedElement(ABC):

    def __init__(self, documentation: str):
        self.documentation = documentation
        
    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

class viewpoint_description_AbstractMappingImport(ABC):

    def __init__(self, hideSubMappings: bool, inheritsAncestorFilters: bool):
        self.hideSubMappings = hideSubMappings
        self.inheritsAncestorFilters = inheritsAncestorFilters
        
    @property
    def hideSubMappings(self) -> bool:
        return self.__hideSubMappings

    @hideSubMappings.setter
    def hideSubMappings(self, hideSubMappings: bool):
        self.__hideSubMappings = hideSubMappings

    @property
    def inheritsAncestorFilters(self) -> bool:
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
class viewpoint_validation_ValidationRule(IdentifiedElement):

    def __init__(self, level: str, message: str, viewpoint_validation_ValidationRule: set["validation_RuleAudit"] = None, viewpoint_validation_ValidationRule221: set["validation_ValidationFix"] = None):
        self.level = level
        self.message = message
        self.viewpoint_validation_ValidationRule = viewpoint_validation_ValidationRule if viewpoint_validation_ValidationRule is not None else set()
        self.viewpoint_validation_ValidationRule221 = viewpoint_validation_ValidationRule221 if viewpoint_validation_ValidationRule221 is not None else set()
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def message(self) -> str:
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
    def viewpoint_validation_ValidationRule221(self):
        return self.__viewpoint_validation_ValidationRule221

    @viewpoint_validation_ValidationRule221.setter
    def viewpoint_validation_ValidationRule221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_validation_ValidationRule__viewpoint_validation_ValidationRule221", None)
        self.__viewpoint_validation_ValidationRule221 = value if value is not None else set()
        
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
                    

    def checkRule(self, eObj: str) -> bool:
        # TODO: Implement checkRule method
        pass

    def getMessage(self, eObj: str) -> str:
        # TODO: Implement getMessage method
        pass

class viewpoint_description_RepresentationElementMapping(IdentifiedElement):

    pass
class viewpoint_description_JavaExtension:

    def __init__(self, qualifiedClassName: str):
        self.qualifiedClassName = qualifiedClassName
        
    @property
    def qualifiedClassName(self) -> str:
        return self.__qualifiedClassName

    @qualifiedClassName.setter
    def qualifiedClassName(self, qualifiedClassName: str):
        self.__qualifiedClassName = qualifiedClassName

class description_viewpoint_EObject:

    pass
class viewpoint_description_MetamodelExtensionSetting:

    pass
class RepresentationExtensionDescription:

    pass
class validation_ValidationSet:

    pass
class viewpoint_description_RepresentationTemplate(ABC):

    def __init__(self, name: str, viewpoint_description_RepresentationTemplate: set["RepresentationDescription"] = None):
        self.name = name
        self.viewpoint_description_RepresentationTemplate = viewpoint_description_RepresentationTemplate if viewpoint_description_RepresentationTemplate is not None else set()
        
    @property
    def name(self) -> str:
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
                if hasattr(item, "RepresentationDescription88"):
                    opp_val = getattr(item, "RepresentationDescription88", None)
                    
                    if opp_val == self:
                        setattr(item, "RepresentationDescription88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepresentationDescription88"):
                    opp_val = getattr(item, "RepresentationDescription88", None)
                    
                    setattr(item, "RepresentationDescription88", self)
                    

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
class viewpoint_Customizable(ABC):

    def __init__(self, customFeatures: str):
        self.customFeatures = customFeatures
        
    @property
    def customFeatures(self) -> str:
        return self.__customFeatures

    @customFeatures.setter
    def customFeatures(self, customFeatures: str):
        self.__customFeatures = customFeatures

class description_IdentifiedElement:

    pass
class description_EndUserDocumentedElement:

    pass
class description_Component:

    pass
class viewpoint_description_Component(ABC):

    pass
class viewpoint_description_Extension(ABC):

    pass
class Extension:

    pass
class UserColorsPalette:

    pass
class SytemColorsPalette:

    pass
class DResource:

    pass
class viewpoint_DFile(DResource):

    pass
class viewpoint_DResource(ABC):

    def __init__(self, name: str, path: str, viewpoint_DResource: "viewpoint_DResourceContainer" = None):
        self.name = name
        self.path = path
        self.viewpoint_DResource = viewpoint_DResource
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

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
class viewpoint_DResourceContainer(DResource):

    pass
class viewpoint_SessionManagerEObject:

    pass
class viewpoint_DAnalysisSessionEObject:

    def __init__(self, open: bool, resources: str, controlledResources: str, synchronizationStatus: str, viewpoint_DAnalysisSessionEObject: set["Viewpoint"] = None, viewpoint_DAnalysisSessionEObject55: set["viewpoint_DAnalysis"] = None, viewpoint_DAnalysisSessionEObject58: "viewpoint_SessionManagerEObject" = None):
        self.open = open
        self.resources = resources
        self.controlledResources = controlledResources
        self.synchronizationStatus = synchronizationStatus
        self.viewpoint_DAnalysisSessionEObject = viewpoint_DAnalysisSessionEObject if viewpoint_DAnalysisSessionEObject is not None else set()
        self.viewpoint_DAnalysisSessionEObject55 = viewpoint_DAnalysisSessionEObject55 if viewpoint_DAnalysisSessionEObject55 is not None else set()
        self.viewpoint_DAnalysisSessionEObject58 = viewpoint_DAnalysisSessionEObject58
        
    @property
    def synchronizationStatus(self) -> str:
        return self.__synchronizationStatus

    @synchronizationStatus.setter
    def synchronizationStatus(self, synchronizationStatus: str):
        self.__synchronizationStatus = synchronizationStatus

    @property
    def open(self) -> bool:
        return self.__open

    @open.setter
    def open(self, open: bool):
        self.__open = open

    @property
    def resources(self) -> str:
        return self.__resources

    @resources.setter
    def resources(self, resources: str):
        self.__resources = resources

    @property
    def controlledResources(self) -> str:
        return self.__controlledResources

    @controlledResources.setter
    def controlledResources(self, controlledResources: str):
        self.__controlledResources = controlledResources

    @property
    def viewpoint_DAnalysisSessionEObject55(self):
        return self.__viewpoint_DAnalysisSessionEObject55

    @viewpoint_DAnalysisSessionEObject55.setter
    def viewpoint_DAnalysisSessionEObject55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysisSessionEObject__viewpoint_DAnalysisSessionEObject55", None)
        self.__viewpoint_DAnalysisSessionEObject55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DAnalysis56"):
                    opp_val = getattr(item, "viewpoint_DAnalysis56", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DAnalysis56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DAnalysis56"):
                    opp_val = getattr(item, "viewpoint_DAnalysis56", None)
                    
                    setattr(item, "viewpoint_DAnalysis56", self)
                    

    @property
    def viewpoint_DAnalysisSessionEObject58(self):
        return self.__viewpoint_DAnalysisSessionEObject58

    @viewpoint_DAnalysisSessionEObject58.setter
    def viewpoint_DAnalysisSessionEObject58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysisSessionEObject__viewpoint_DAnalysisSessionEObject58", None)
        self.__viewpoint_DAnalysisSessionEObject58 = value
        
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
                if hasattr(item, "Viewpoint53"):
                    opp_val = getattr(item, "Viewpoint53", None)
                    
                    if opp_val == self:
                        setattr(item, "Viewpoint53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Viewpoint53"):
                    opp_val = getattr(item, "Viewpoint53", None)
                    
                    setattr(item, "Viewpoint53", self)
                    

class style_StyleDescription:

    pass
class Customizable:

    pass
class viewpoint_BasicLabelStyle(Customizable):

    def __init__(self, labelSize: int, labelFormat: str, showIcon: bool, iconPath: str, labelColor: str):
        self.labelSize = labelSize
        self.labelFormat = labelFormat
        self.showIcon = showIcon
        self.iconPath = iconPath
        self.labelColor = labelColor
        
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
    def iconPath(self) -> str:
        return self.__iconPath

    @iconPath.setter
    def iconPath(self, iconPath: str):
        self.__iconPath = iconPath

    @property
    def showIcon(self) -> bool:
        return self.__showIcon

    @showIcon.setter
    def showIcon(self, showIcon: bool):
        self.__showIcon = showIcon

    @property
    def labelColor(self) -> str:
        return self.__labelColor

    @labelColor.setter
    def labelColor(self, labelColor: str):
        self.__labelColor = labelColor

class DSemanticDecorator:

    pass
class DStylizable:

    pass
class DMappingBased:

    pass
class viewpoint_UIState:

    def __init__(self, decorationImage: str, inverseSelectionOrder: bool, viewpoint_UIState: "viewpoint_DRepresentation" = None, viewpoint_UIState61: set["viewpoint_EObject"] = None):
        self.decorationImage = decorationImage
        self.inverseSelectionOrder = inverseSelectionOrder
        self.viewpoint_UIState = viewpoint_UIState
        self.viewpoint_UIState61 = viewpoint_UIState61 if viewpoint_UIState61 is not None else set()
        
    @property
    def inverseSelectionOrder(self) -> bool:
        return self.__inverseSelectionOrder

    @inverseSelectionOrder.setter
    def inverseSelectionOrder(self, inverseSelectionOrder: bool):
        self.__inverseSelectionOrder = inverseSelectionOrder

    @property
    def decorationImage(self) -> str:
        return self.__decorationImage

    @decorationImage.setter
    def decorationImage(self, decorationImage: str):
        self.__decorationImage = decorationImage

    @property
    def viewpoint_UIState(self):
        return self.__viewpoint_UIState

    @viewpoint_UIState.setter
    def viewpoint_UIState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_UIState__viewpoint_UIState", None)
        self.__viewpoint_UIState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DRepresentation31"):
                opp_val = getattr(old_value, "viewpoint_DRepresentation31", None)
                if opp_val == self:
                    setattr(old_value, "viewpoint_DRepresentation31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DRepresentation31"):
                opp_val = getattr(value, "viewpoint_DRepresentation31", None)
                setattr(value, "viewpoint_DRepresentation31", self)

    @property
    def viewpoint_UIState61(self):
        return self.__viewpoint_UIState61

    @viewpoint_UIState61.setter
    def viewpoint_UIState61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_UIState__viewpoint_UIState61", None)
        self.__viewpoint_UIState61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_EObject62"):
                    opp_val = getattr(item, "viewpoint_EObject62", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_EObject62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_EObject62"):
                    opp_val = getattr(item, "viewpoint_EObject62", None)
                    
                    setattr(item, "viewpoint_EObject62", self)
                    

class BasicLabelStyle:

    pass
class viewpoint_LabelStyle(BasicLabelStyle):

    def __init__(self, labelAlignment: str):
        self.labelAlignment = labelAlignment
        
    @property
    def labelAlignment(self) -> str:
        return self.__labelAlignment

    @labelAlignment.setter
    def labelAlignment(self, labelAlignment: str):
        self.__labelAlignment = labelAlignment

class viewpoint_DAnalysisCustomData:

    def __init__(self, key: str, viewpoint_DAnalysisCustomData: "viewpoint_EObject" = None):
        self.key = key
        self.viewpoint_DAnalysisCustomData = viewpoint_DAnalysisCustomData
        
    @property
    def key(self) -> str:
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
            if hasattr(old_value, "viewpoint_EObject50"):
                opp_val = getattr(old_value, "viewpoint_EObject50", None)
                if opp_val == self:
                    setattr(old_value, "viewpoint_EObject50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_EObject50"):
                opp_val = getattr(value, "viewpoint_EObject50", None)
                setattr(value, "viewpoint_EObject50", self)

class DecorationDescription:

    pass
class viewpoint_description_GenericDecorationDescription(DecorationDescription):

    pass
class viewpoint_description_SemanticBasedDecoration(DecorationDescription):

    def __init__(self, domainClass: str, DecorationDescription: "viewpoint_Decoration", DecorationDescription99: "viewpoint_description_DecorationDescriptionsSet"):
        self.domainClass = domainClass
        
    @property
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

class viewpoint_Decoration:

    pass
class viewpoint_MetaModelExtension:

    pass
class Viewpoint:

    pass
class viewpoint_DStylizable(ABC):

    def __init__(self):
        
    def getStyle(self) -> str:
        # TODO: Implement getStyle method
        pass

class FeatureExtensionDescription:

    pass
class viewpoint_DFeatureExtension(ABC):

    pass
class AnnotationEntry:

    pass
class description_DModelElement:

    pass
class DRefreshable:

    pass
class viewpoint_DRepresentationElement(DStylizable, DMappingBased, DRefreshable, DSemanticDecorator):

    def __init__(self, name: str, viewpoint_DRepresentationElement: "viewpoint_DRepresentation" = None, viewpoint_DRepresentationElement27: "viewpoint_DRepresentation" = None, viewpoint_DRepresentationElement33: set["viewpoint_EObject"] = None):
        self.name = name
        self.viewpoint_DRepresentationElement = viewpoint_DRepresentationElement
        self.viewpoint_DRepresentationElement27 = viewpoint_DRepresentationElement27
        self.viewpoint_DRepresentationElement33 = viewpoint_DRepresentationElement33 if viewpoint_DRepresentationElement33 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def viewpoint_DRepresentationElement27(self):
        return self.__viewpoint_DRepresentationElement27

    @viewpoint_DRepresentationElement27.setter
    def viewpoint_DRepresentationElement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationElement__viewpoint_DRepresentationElement27", None)
        self.__viewpoint_DRepresentationElement27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DRepresentation26"):
                opp_val = getattr(old_value, "viewpoint_DRepresentation26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DRepresentation26"):
                opp_val = getattr(value, "viewpoint_DRepresentation26", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DRepresentation26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def viewpoint_DRepresentationElement33(self):
        return self.__viewpoint_DRepresentationElement33

    @viewpoint_DRepresentationElement33.setter
    def viewpoint_DRepresentationElement33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationElement__viewpoint_DRepresentationElement33", None)
        self.__viewpoint_DRepresentationElement33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_EObject34"):
                    opp_val = getattr(item, "viewpoint_EObject34", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_EObject34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_EObject34"):
                    opp_val = getattr(item, "viewpoint_EObject34", None)
                    
                    setattr(item, "viewpoint_EObject34", self)
                    

class viewpoint_Style(DRefreshable, Customizable):

    pass
class description_DocumentedElement:

    pass
class viewpoint_description_Group(description_DocumentedElement, description_DModelElement):

    def __init__(self, name: str, version: str, viewpoint_description_Group: set["Viewpoint"] = None, viewpoint_description_Group66: "SytemColorsPalette" = None, viewpoint_description_Group68: set["UserColorsPalette"] = None, viewpoint_description_Group70: set["Extension"] = None):
        self.name = name
        self.version = version
        self.viewpoint_description_Group = viewpoint_description_Group if viewpoint_description_Group is not None else set()
        self.viewpoint_description_Group66 = viewpoint_description_Group66
        self.viewpoint_description_Group68 = viewpoint_description_Group68 if viewpoint_description_Group68 is not None else set()
        self.viewpoint_description_Group70 = viewpoint_description_Group70 if viewpoint_description_Group70 is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "Extension"):
                    opp_val = getattr(item, "Extension", None)
                    
                    if opp_val == self:
                        setattr(item, "Extension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Extension"):
                    opp_val = getattr(item, "Extension", None)
                    
                    setattr(item, "Extension", self)
                    

    @property
    def viewpoint_description_Group66(self):
        return self.__viewpoint_description_Group66

    @viewpoint_description_Group66.setter
    def viewpoint_description_Group66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Group__viewpoint_description_Group66", None)
        self.__viewpoint_description_Group66 = value
        
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
                if hasattr(item, "Viewpoint64"):
                    opp_val = getattr(item, "Viewpoint64", None)
                    
                    if opp_val == self:
                        setattr(item, "Viewpoint64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Viewpoint64"):
                    opp_val = getattr(item, "Viewpoint64", None)
                    
                    setattr(item, "Viewpoint64", self)
                    

    @property
    def viewpoint_description_Group68(self):
        return self.__viewpoint_description_Group68

    @viewpoint_description_Group68.setter
    def viewpoint_description_Group68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Group__viewpoint_description_Group68", None)
        self.__viewpoint_description_Group68 = value if value is not None else set()
        
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
                    

class viewpoint_description_Viewpoint(description_EndUserDocumentedElement, description_IdentifiedElement, description_Component, description_DocumentedElement):

    def __init__(self, modelFileExtension: str, icon: str, conflicts: str, reuses: str, customizes: str, viewpoint_description_Viewpoint78: set["JavaExtension"] = None, viewpoint_description_Viewpoint80: set["MetamodelExtensionSetting"] = None, viewpoint_description_Viewpoint82: set["FeatureExtensionDescription"] = None, viewpoint_description_Viewpoint85: set["RepresentationTemplate"] = None, viewpoint_description_Viewpoint: "validation_ValidationSet" = None, viewpoint_description_Viewpoint73: set["RepresentationDescription"] = None, viewpoint_description_Viewpoint76: set["RepresentationExtensionDescription"] = None):
        self.modelFileExtension = modelFileExtension
        self.icon = icon
        self.conflicts = conflicts
        self.reuses = reuses
        self.customizes = customizes
        self.viewpoint_description_Viewpoint78 = viewpoint_description_Viewpoint78 if viewpoint_description_Viewpoint78 is not None else set()
        self.viewpoint_description_Viewpoint80 = viewpoint_description_Viewpoint80 if viewpoint_description_Viewpoint80 is not None else set()
        self.viewpoint_description_Viewpoint82 = viewpoint_description_Viewpoint82 if viewpoint_description_Viewpoint82 is not None else set()
        self.viewpoint_description_Viewpoint85 = viewpoint_description_Viewpoint85 if viewpoint_description_Viewpoint85 is not None else set()
        self.viewpoint_description_Viewpoint = viewpoint_description_Viewpoint
        self.viewpoint_description_Viewpoint73 = viewpoint_description_Viewpoint73 if viewpoint_description_Viewpoint73 is not None else set()
        self.viewpoint_description_Viewpoint76 = viewpoint_description_Viewpoint76 if viewpoint_description_Viewpoint76 is not None else set()
        
    @property
    def customizes(self) -> str:
        return self.__customizes

    @customizes.setter
    def customizes(self, customizes: str):
        self.__customizes = customizes

    @property
    def modelFileExtension(self) -> str:
        return self.__modelFileExtension

    @modelFileExtension.setter
    def modelFileExtension(self, modelFileExtension: str):
        self.__modelFileExtension = modelFileExtension

    @property
    def reuses(self) -> str:
        return self.__reuses

    @reuses.setter
    def reuses(self, reuses: str):
        self.__reuses = reuses

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def conflicts(self) -> str:
        return self.__conflicts

    @conflicts.setter
    def conflicts(self, conflicts: str):
        self.__conflicts = conflicts

    @property
    def viewpoint_description_Viewpoint82(self):
        return self.__viewpoint_description_Viewpoint82

    @viewpoint_description_Viewpoint82.setter
    def viewpoint_description_Viewpoint82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint82", None)
        self.__viewpoint_description_Viewpoint82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FeatureExtensionDescription83"):
                    opp_val = getattr(item, "FeatureExtensionDescription83", None)
                    
                    if opp_val == self:
                        setattr(item, "FeatureExtensionDescription83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FeatureExtensionDescription83"):
                    opp_val = getattr(item, "FeatureExtensionDescription83", None)
                    
                    setattr(item, "FeatureExtensionDescription83", self)
                    

    @property
    def viewpoint_description_Viewpoint80(self):
        return self.__viewpoint_description_Viewpoint80

    @viewpoint_description_Viewpoint80.setter
    def viewpoint_description_Viewpoint80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint80", None)
        self.__viewpoint_description_Viewpoint80 = value if value is not None else set()
        
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
    def viewpoint_description_Viewpoint85(self):
        return self.__viewpoint_description_Viewpoint85

    @viewpoint_description_Viewpoint85.setter
    def viewpoint_description_Viewpoint85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint85", None)
        self.__viewpoint_description_Viewpoint85 = value if value is not None else set()
        
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
    def viewpoint_description_Viewpoint76(self):
        return self.__viewpoint_description_Viewpoint76

    @viewpoint_description_Viewpoint76.setter
    def viewpoint_description_Viewpoint76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint76", None)
        self.__viewpoint_description_Viewpoint76 = value if value is not None else set()
        
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
    def viewpoint_description_Viewpoint78(self):
        return self.__viewpoint_description_Viewpoint78

    @viewpoint_description_Viewpoint78.setter
    def viewpoint_description_Viewpoint78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_description_Viewpoint__viewpoint_description_Viewpoint78", None)
        self.__viewpoint_description_Viewpoint78 = value if value is not None else set()
        
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
                if hasattr(item, "RepresentationDescription74"):
                    opp_val = getattr(item, "RepresentationDescription74", None)
                    
                    if opp_val == self:
                        setattr(item, "RepresentationDescription74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepresentationDescription74"):
                    opp_val = getattr(item, "RepresentationDescription74", None)
                    
                    setattr(item, "RepresentationDescription74", self)
                    

    def initView(self, model: str):
        # TODO: Implement initView method
        pass

class viewpoint_description_RepresentationDescription(description_EndUserDocumentedElement, description_IdentifiedElement, description_DocumentedElement):

    def __init__(self, titleExpression: str, initialisation: bool, showOnStartup: bool, viewpoint_description_RepresentationDescription: set["description_viewpoint_EPackage"] = None):
        self.titleExpression = titleExpression
        self.initialisation = initialisation
        self.showOnStartup = showOnStartup
        self.viewpoint_description_RepresentationDescription = viewpoint_description_RepresentationDescription if viewpoint_description_RepresentationDescription is not None else set()
        
    @property
    def titleExpression(self) -> str:
        return self.__titleExpression

    @titleExpression.setter
    def titleExpression(self, titleExpression: str):
        self.__titleExpression = titleExpression

    @property
    def initialisation(self) -> bool:
        return self.__initialisation

    @initialisation.setter
    def initialisation(self, initialisation: bool):
        self.__initialisation = initialisation

    @property
    def showOnStartup(self) -> bool:
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
                    

class viewpoint_tool_ToolEntry(description_IdentifiedElement, description_DocumentedElement):

    pass
class viewpoint_DRepresentation(description_DModelElement, DRefreshable, description_DocumentedElement):

    def __init__(self, name: str, viewpoint_DRepresentation: "viewpoint_DRepresentationDescriptor" = None, viewpoint_DRepresentation24: set["viewpoint_DRepresentationElement"] = None, viewpoint_DRepresentation26: set["viewpoint_DRepresentationElement"] = None, viewpoint_DRepresentation29: set["AnnotationEntry"] = None, viewpoint_DRepresentation31: "viewpoint_UIState" = None):
        self.name = name
        self.viewpoint_DRepresentation = viewpoint_DRepresentation
        self.viewpoint_DRepresentation24 = viewpoint_DRepresentation24 if viewpoint_DRepresentation24 is not None else set()
        self.viewpoint_DRepresentation26 = viewpoint_DRepresentation26 if viewpoint_DRepresentation26 is not None else set()
        self.viewpoint_DRepresentation29 = viewpoint_DRepresentation29 if viewpoint_DRepresentation29 is not None else set()
        self.viewpoint_DRepresentation31 = viewpoint_DRepresentation31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def viewpoint_DRepresentation26(self):
        return self.__viewpoint_DRepresentation26

    @viewpoint_DRepresentation26.setter
    def viewpoint_DRepresentation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation26", None)
        self.__viewpoint_DRepresentation26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "viewpoint_DRepresentationElement27"):
                    opp_val = getattr(item, "viewpoint_DRepresentationElement27", None)
                    
                    if opp_val == self:
                        setattr(item, "viewpoint_DRepresentationElement27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "viewpoint_DRepresentationElement27"):
                    opp_val = getattr(item, "viewpoint_DRepresentationElement27", None)
                    
                    setattr(item, "viewpoint_DRepresentationElement27", self)
                    

    @property
    def viewpoint_DRepresentation31(self):
        return self.__viewpoint_DRepresentation31

    @viewpoint_DRepresentation31.setter
    def viewpoint_DRepresentation31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation31", None)
        self.__viewpoint_DRepresentation31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_UIState"):
                opp_val = getattr(old_value, "viewpoint_UIState", None)
                if opp_val == self:
                    setattr(old_value, "viewpoint_UIState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_UIState"):
                opp_val = getattr(value, "viewpoint_UIState", None)
                setattr(value, "viewpoint_UIState", self)

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
    def viewpoint_DRepresentation29(self):
        return self.__viewpoint_DRepresentation29

    @viewpoint_DRepresentation29.setter
    def viewpoint_DRepresentation29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation29", None)
        self.__viewpoint_DRepresentation29 = value if value is not None else set()
        
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
                    

    @property
    def viewpoint_DRepresentation(self):
        return self.__viewpoint_DRepresentation

    @viewpoint_DRepresentation.setter
    def viewpoint_DRepresentation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentation__viewpoint_DRepresentation", None)
        self.__viewpoint_DRepresentation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DRepresentationDescriptor22"):
                opp_val = getattr(old_value, "viewpoint_DRepresentationDescriptor22", None)
                if opp_val == self:
                    setattr(old_value, "viewpoint_DRepresentationDescriptor22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DRepresentationDescriptor22"):
                opp_val = getattr(value, "viewpoint_DRepresentationDescriptor22", None)
                setattr(value, "viewpoint_DRepresentationDescriptor22", self)

class RepresentationDescription:

    pass
class viewpoint_description_RepresentationImportDescription(RepresentationDescription):

    pass
class viewpoint_DRepresentationDescriptor:

    def __init__(self, name: str, viewpoint_DRepresentationDescriptor: "RepresentationDescription" = None, viewpoint_DRepresentationDescriptor19: "viewpoint_EObject" = None, viewpoint_DRepresentationDescriptor22: "viewpoint_DRepresentation" = None, viewpoint_DRepresentationDescriptor39: "viewpoint_DView" = None):
        self.name = name
        self.viewpoint_DRepresentationDescriptor = viewpoint_DRepresentationDescriptor
        self.viewpoint_DRepresentationDescriptor19 = viewpoint_DRepresentationDescriptor19
        self.viewpoint_DRepresentationDescriptor22 = viewpoint_DRepresentationDescriptor22
        self.viewpoint_DRepresentationDescriptor39 = viewpoint_DRepresentationDescriptor39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def viewpoint_DRepresentationDescriptor(self):
        return self.__viewpoint_DRepresentationDescriptor

    @viewpoint_DRepresentationDescriptor.setter
    def viewpoint_DRepresentationDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationDescriptor__viewpoint_DRepresentationDescriptor", None)
        self.__viewpoint_DRepresentationDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RepresentationDescription"):
                opp_val = getattr(old_value, "RepresentationDescription", None)
                if opp_val == self:
                    setattr(old_value, "RepresentationDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RepresentationDescription"):
                opp_val = getattr(value, "RepresentationDescription", None)
                setattr(value, "RepresentationDescription", self)

    @property
    def viewpoint_DRepresentationDescriptor19(self):
        return self.__viewpoint_DRepresentationDescriptor19

    @viewpoint_DRepresentationDescriptor19.setter
    def viewpoint_DRepresentationDescriptor19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationDescriptor__viewpoint_DRepresentationDescriptor19", None)
        self.__viewpoint_DRepresentationDescriptor19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_EObject20"):
                opp_val = getattr(old_value, "viewpoint_EObject20", None)
                if opp_val == self:
                    setattr(old_value, "viewpoint_EObject20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_EObject20"):
                opp_val = getattr(value, "viewpoint_EObject20", None)
                setattr(value, "viewpoint_EObject20", self)

    @property
    def viewpoint_DRepresentationDescriptor22(self):
        return self.__viewpoint_DRepresentationDescriptor22

    @viewpoint_DRepresentationDescriptor22.setter
    def viewpoint_DRepresentationDescriptor22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationDescriptor__viewpoint_DRepresentationDescriptor22", None)
        self.__viewpoint_DRepresentationDescriptor22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DRepresentation"):
                opp_val = getattr(old_value, "viewpoint_DRepresentation", None)
                if opp_val == self:
                    setattr(old_value, "viewpoint_DRepresentation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DRepresentation"):
                opp_val = getattr(value, "viewpoint_DRepresentation", None)
                setattr(value, "viewpoint_DRepresentation", self)

    @property
    def viewpoint_DRepresentationDescriptor39(self):
        return self.__viewpoint_DRepresentationDescriptor39

    @viewpoint_DRepresentationDescriptor39.setter
    def viewpoint_DRepresentationDescriptor39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DRepresentationDescriptor__viewpoint_DRepresentationDescriptor39", None)
        self.__viewpoint_DRepresentationDescriptor39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DView38"):
                opp_val = getattr(old_value, "viewpoint_DView38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DView38"):
                opp_val = getattr(value, "viewpoint_DView38", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DView38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class viewpoint_DSemanticDecorator(ABC):

    pass
class viewpoint_DMappingBased(ABC):

    def __init__(self):
        
    def getMapping(self) -> str:
        # TODO: Implement getMapping method
        pass

class viewpoint_DRefreshable(ABC):

    def __init__(self):
        
    def refresh(self):
        # TODO: Implement refresh method
        pass

class viewpoint_DView(DRefreshable):

    pass
class DAnnotationEntry:

    pass
class viewpoint_EObject:

    pass
class viewpoint_DAnalysis:

    def __init__(self, semanticResources: str, version: str, viewpoint_DAnalysis: "viewpoint_DAnalysis" = None, viewpoint_DAnalysis0: set["viewpoint_DAnalysis"] = None, viewpoint_DAnalysis3: set["viewpoint_EObject"] = None, viewpoint_DAnalysis5: set["DAnnotationEntry"] = None, viewpoint_DAnalysis7: set["viewpoint_DView"] = None, viewpoint_DAnalysis9: set["viewpoint_DView"] = None, viewpoint_DAnalysis12: set["viewpoint_DFeatureExtension"] = None, viewpoint_DAnalysis56: "viewpoint_DAnalysisSessionEObject" = None):
        self.semanticResources = semanticResources
        self.version = version
        self.viewpoint_DAnalysis = viewpoint_DAnalysis
        self.viewpoint_DAnalysis0 = viewpoint_DAnalysis0 if viewpoint_DAnalysis0 is not None else set()
        self.viewpoint_DAnalysis3 = viewpoint_DAnalysis3 if viewpoint_DAnalysis3 is not None else set()
        self.viewpoint_DAnalysis5 = viewpoint_DAnalysis5 if viewpoint_DAnalysis5 is not None else set()
        self.viewpoint_DAnalysis7 = viewpoint_DAnalysis7 if viewpoint_DAnalysis7 is not None else set()
        self.viewpoint_DAnalysis9 = viewpoint_DAnalysis9 if viewpoint_DAnalysis9 is not None else set()
        self.viewpoint_DAnalysis12 = viewpoint_DAnalysis12 if viewpoint_DAnalysis12 is not None else set()
        self.viewpoint_DAnalysis56 = viewpoint_DAnalysis56
        
    @property
    def semanticResources(self) -> str:
        return self.__semanticResources

    @semanticResources.setter
    def semanticResources(self, semanticResources: str):
        self.__semanticResources = semanticResources

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def viewpoint_DAnalysis56(self):
        return self.__viewpoint_DAnalysis56

    @viewpoint_DAnalysis56.setter
    def viewpoint_DAnalysis56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_viewpoint_DAnalysis__viewpoint_DAnalysis56", None)
        self.__viewpoint_DAnalysis56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "viewpoint_DAnalysisSessionEObject55"):
                opp_val = getattr(old_value, "viewpoint_DAnalysisSessionEObject55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "viewpoint_DAnalysisSessionEObject55"):
                opp_val = getattr(value, "viewpoint_DAnalysisSessionEObject55", None)
                if opp_val is None:
                    setattr(value, "viewpoint_DAnalysisSessionEObject55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    
