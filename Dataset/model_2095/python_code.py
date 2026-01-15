from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TreeDragSource(Enum):
    TREE = "TREE"
    PROJECT_EXPLORER = "PROJECT_EXPLORER"
    BOTH = "BOTH"


############################################
# Definition of Classes
############################################

class tool_MenuItemOrRef:

    pass
class TreeItemContainerDropTool:

    pass
class tree_description_TreeItemMappingContainer(ABC):

    pass
class TreeItemEditionTool:

    pass
class tree_description_TreeItemUpdater:

    def __init__(self, tree_description_TreeItemUpdater: "TreeItemEditionTool" = None):
        self.tree_description_TreeItemUpdater = tree_description_TreeItemUpdater
        
    @property
    def tree_description_TreeItemUpdater(self):
        return self.__tree_description_TreeItemUpdater

    @tree_description_TreeItemUpdater.setter
    def tree_description_TreeItemUpdater(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemUpdater__tree_description_TreeItemUpdater", None)
        self.__tree_description_TreeItemUpdater = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeItemEditionTool"):
                opp_val = getattr(old_value, "TreeItemEditionTool", None)
                if opp_val == self:
                    setattr(old_value, "TreeItemEditionTool", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeItemEditionTool"):
                opp_val = getattr(value, "TreeItemEditionTool", None)
                setattr(value, "TreeItemEditionTool", self)

    def getCreateTreeItem(self) -> str:
        # TODO: Implement getCreateTreeItem method
        pass

    def getLabelComputationExpression(self) -> str:
        # TODO: Implement getLabelComputationExpression method
        pass

class tool_VariableContainer:

    pass
class description_AbstractVariable:

    pass
class tree_description_TreeVariable(tool_VariableContainer, description_AbstractVariable):

    def __init__(self, documentation: str):
        self.documentation = documentation
        
    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

class ConditionalTreeItemStyleDescription:

    pass
class tree_description_StyleUpdater:

    pass
class RepresentationElementMapping:

    pass
class tree_description_TreeMapping(RepresentationElementMapping):

    def __init__(self, semanticElements: str):
        self.semanticElements = semanticElements
        
    @property
    def semanticElements(self) -> str:
        return self.__semanticElements

    @semanticElements.setter
    def semanticElements(self, semanticElements: str):
        self.__semanticElements = semanticElements

class RepresentationNavigationDescription:

    pass
class tree_description_TreeNavigationDescription(RepresentationNavigationDescription):

    pass
class RepresentationCreationDescription:

    pass
class tree_description_TreeCreationDescription(RepresentationCreationDescription):

    pass
class tool_EditMaskVariables:

    pass
class TreeItemTool:

    pass
class tree_description_TreeItemDeletionTool(TreeItemTool):

    pass
class tree_description_TreeItemEditionTool(TreeItemTool):

    pass
class PrecedingSiblingsVariables:

    pass
class TreeItemMappingContainer:

    pass
class tool_ElementDropVariable:

    pass
class tool_DropContainerVariable:

    pass
class description_TreeItemTool:

    pass
class tool_MappingBasedToolDescription:

    pass
class tree_description_TreeItemCreationTool(tool_MappingBasedToolDescription, description_TreeItemTool):

    pass
class tree_description_TreeItemContainerDropTool(tool_MappingBasedToolDescription, description_TreeItemTool):

    def __init__(self, dragSource: str, tree_description_TreeItemContainerDropTool: "tool_DropContainerVariable" = None, tree_description_TreeItemContainerDropTool54: "tool_DropContainerVariable" = None, tree_description_TreeItemContainerDropTool57: "tool_ElementDropVariable" = None, tree_description_TreeItemContainerDropTool60: "tool_ContainerViewVariable" = None, tree_description_TreeItemContainerDropTool63: "PrecedingSiblingsVariables" = None):
        self.dragSource = dragSource
        self.tree_description_TreeItemContainerDropTool = tree_description_TreeItemContainerDropTool
        self.tree_description_TreeItemContainerDropTool54 = tree_description_TreeItemContainerDropTool54
        self.tree_description_TreeItemContainerDropTool57 = tree_description_TreeItemContainerDropTool57
        self.tree_description_TreeItemContainerDropTool60 = tree_description_TreeItemContainerDropTool60
        self.tree_description_TreeItemContainerDropTool63 = tree_description_TreeItemContainerDropTool63
        
    @property
    def dragSource(self) -> str:
        return self.__dragSource

    @dragSource.setter
    def dragSource(self, dragSource: str):
        self.__dragSource = dragSource

    @property
    def tree_description_TreeItemContainerDropTool60(self):
        return self.__tree_description_TreeItemContainerDropTool60

    @tree_description_TreeItemContainerDropTool60.setter
    def tree_description_TreeItemContainerDropTool60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemContainerDropTool__tree_description_TreeItemContainerDropTool60", None)
        self.__tree_description_TreeItemContainerDropTool60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ContainerViewVariable61"):
                opp_val = getattr(old_value, "tool_ContainerViewVariable61", None)
                if opp_val == self:
                    setattr(old_value, "tool_ContainerViewVariable61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ContainerViewVariable61"):
                opp_val = getattr(value, "tool_ContainerViewVariable61", None)
                setattr(value, "tool_ContainerViewVariable61", self)

    @property
    def tree_description_TreeItemContainerDropTool63(self):
        return self.__tree_description_TreeItemContainerDropTool63

    @tree_description_TreeItemContainerDropTool63.setter
    def tree_description_TreeItemContainerDropTool63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemContainerDropTool__tree_description_TreeItemContainerDropTool63", None)
        self.__tree_description_TreeItemContainerDropTool63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrecedingSiblingsVariables64"):
                opp_val = getattr(old_value, "PrecedingSiblingsVariables64", None)
                if opp_val == self:
                    setattr(old_value, "PrecedingSiblingsVariables64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrecedingSiblingsVariables64"):
                opp_val = getattr(value, "PrecedingSiblingsVariables64", None)
                setattr(value, "PrecedingSiblingsVariables64", self)

    @property
    def tree_description_TreeItemContainerDropTool(self):
        return self.__tree_description_TreeItemContainerDropTool

    @tree_description_TreeItemContainerDropTool.setter
    def tree_description_TreeItemContainerDropTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemContainerDropTool__tree_description_TreeItemContainerDropTool", None)
        self.__tree_description_TreeItemContainerDropTool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DropContainerVariable52"):
                opp_val = getattr(old_value, "tool_DropContainerVariable52", None)
                if opp_val == self:
                    setattr(old_value, "tool_DropContainerVariable52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DropContainerVariable52"):
                opp_val = getattr(value, "tool_DropContainerVariable52", None)
                setattr(value, "tool_DropContainerVariable52", self)

    @property
    def tree_description_TreeItemContainerDropTool57(self):
        return self.__tree_description_TreeItemContainerDropTool57

    @tree_description_TreeItemContainerDropTool57.setter
    def tree_description_TreeItemContainerDropTool57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemContainerDropTool__tree_description_TreeItemContainerDropTool57", None)
        self.__tree_description_TreeItemContainerDropTool57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_ElementDropVariable58"):
                opp_val = getattr(old_value, "tool_ElementDropVariable58", None)
                if opp_val == self:
                    setattr(old_value, "tool_ElementDropVariable58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_ElementDropVariable58"):
                opp_val = getattr(value, "tool_ElementDropVariable58", None)
                setattr(value, "tool_ElementDropVariable58", self)

    @property
    def tree_description_TreeItemContainerDropTool54(self):
        return self.__tree_description_TreeItemContainerDropTool54

    @tree_description_TreeItemContainerDropTool54.setter
    def tree_description_TreeItemContainerDropTool54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemContainerDropTool__tree_description_TreeItemContainerDropTool54", None)
        self.__tree_description_TreeItemContainerDropTool54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DropContainerVariable55"):
                opp_val = getattr(old_value, "tool_DropContainerVariable55", None)
                if opp_val == self:
                    setattr(old_value, "tool_DropContainerVariable55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DropContainerVariable55"):
                opp_val = getattr(value, "tool_DropContainerVariable55", None)
                setattr(value, "tool_DropContainerVariable55", self)

class tree_description_TreeItemDragTool(tool_MappingBasedToolDescription, description_TreeItemTool):

    def __init__(self, dragSourceType: str, tree_description_TreeItemDragTool46: "tool_ContainerViewVariable" = None, tree_description_TreeItemDragTool: "tool_DropContainerVariable" = None, tree_description_TreeItemDragTool41: "tool_DropContainerVariable" = None, tree_description_TreeItemDragTool44: "tool_ElementDropVariable" = None, tree_description_TreeItemDragTool48: set["TreeItemMappingContainer"] = None, tree_description_TreeItemDragTool50: "PrecedingSiblingsVariables" = None):
        self.dragSourceType = dragSourceType
        self.tree_description_TreeItemDragTool46 = tree_description_TreeItemDragTool46
        self.tree_description_TreeItemDragTool = tree_description_TreeItemDragTool
        self.tree_description_TreeItemDragTool41 = tree_description_TreeItemDragTool41
        self.tree_description_TreeItemDragTool44 = tree_description_TreeItemDragTool44
        self.tree_description_TreeItemDragTool48 = tree_description_TreeItemDragTool48 if tree_description_TreeItemDragTool48 is not None else set()
        self.tree_description_TreeItemDragTool50 = tree_description_TreeItemDragTool50
        
    @property
    def dragSourceType(self) -> str:
        return self.__dragSourceType

    @dragSourceType.setter
    def dragSourceType(self, dragSourceType: str):
        self.__dragSourceType = dragSourceType

    @property
    def tree_description_TreeItemDragTool50(self):
        return self.__tree_description_TreeItemDragTool50

    @tree_description_TreeItemDragTool50.setter
    def tree_description_TreeItemDragTool50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemDragTool__tree_description_TreeItemDragTool50", None)
        self.__tree_description_TreeItemDragTool50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PrecedingSiblingsVariables"):
                opp_val = getattr(old_value, "PrecedingSiblingsVariables", None)
                if opp_val == self:
                    setattr(old_value, "PrecedingSiblingsVariables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PrecedingSiblingsVariables"):
                opp_val = getattr(value, "PrecedingSiblingsVariables", None)
                setattr(value, "PrecedingSiblingsVariables", self)

    @property
    def tree_description_TreeItemDragTool44(self):
        return self.__tree_description_TreeItemDragTool44

    @tree_description_TreeItemDragTool44.setter
    def tree_description_TreeItemDragTool44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemDragTool__tree_description_TreeItemDragTool44", None)
        self.__tree_description_TreeItemDragTool44 = value
        
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
    def tree_description_TreeItemDragTool46(self):
        return self.__tree_description_TreeItemDragTool46

    @tree_description_TreeItemDragTool46.setter
    def tree_description_TreeItemDragTool46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemDragTool__tree_description_TreeItemDragTool46", None)
        self.__tree_description_TreeItemDragTool46 = value
        
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
    def tree_description_TreeItemDragTool(self):
        return self.__tree_description_TreeItemDragTool

    @tree_description_TreeItemDragTool.setter
    def tree_description_TreeItemDragTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemDragTool__tree_description_TreeItemDragTool", None)
        self.__tree_description_TreeItemDragTool = value
        
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
    def tree_description_TreeItemDragTool48(self):
        return self.__tree_description_TreeItemDragTool48

    @tree_description_TreeItemDragTool48.setter
    def tree_description_TreeItemDragTool48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemDragTool__tree_description_TreeItemDragTool48", None)
        self.__tree_description_TreeItemDragTool48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreeItemMappingContainer"):
                    opp_val = getattr(item, "TreeItemMappingContainer", None)
                    
                    if opp_val == self:
                        setattr(item, "TreeItemMappingContainer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreeItemMappingContainer"):
                    opp_val = getattr(item, "TreeItemMappingContainer", None)
                    
                    setattr(item, "TreeItemMappingContainer", self)
                    

    @property
    def tree_description_TreeItemDragTool41(self):
        return self.__tree_description_TreeItemDragTool41

    @tree_description_TreeItemDragTool41.setter
    def tree_description_TreeItemDragTool41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemDragTool__tree_description_TreeItemDragTool41", None)
        self.__tree_description_TreeItemDragTool41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tool_DropContainerVariable42"):
                opp_val = getattr(old_value, "tool_DropContainerVariable42", None)
                if opp_val == self:
                    setattr(old_value, "tool_DropContainerVariable42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tool_DropContainerVariable42"):
                opp_val = getattr(value, "tool_DropContainerVariable42", None)
                setattr(value, "tool_DropContainerVariable42", self)

    def getBestTreeItemMapping(self) -> str:
        # TODO: Implement getBestTreeItemMapping method
        pass

class TreeVariable:

    pass
class tree_description_PrecedingSiblingsVariables(TreeVariable):

    pass
class tool_ModelOperation:

    pass
class AbstractToolDescription:

    pass
class tree_description_TreePopupMenu(AbstractToolDescription):

    pass
class tree_description_TreeItemTool(AbstractToolDescription):

    pass
class TreeItemStyleDescription:

    pass
class ConditionalStyleDescription:

    pass
class tree_description_ConditionalTreeItemStyleDescription(ConditionalStyleDescription):

    pass
class ColorDescription:

    pass
class style_LabelStyleDescription:

    pass
class tool_ContainerViewVariable:

    pass
class TreePopupMenu:

    pass
class TreeItemDragTool:

    pass
class TreeItemDeletionTool:

    pass
class style_StyleDescription:

    pass
class tree_description_TreeItemStyleDescription(style_LabelStyleDescription, style_StyleDescription):

    pass
class description_TreeItemUpdater:

    pass
class description_StyleUpdater:

    pass
class description_TreeMapping:

    pass
class tool_RepresentationNavigationDescription:

    pass
class tool_RepresentationCreationDescription:

    pass
class TreeItemCreationTool:

    pass
class description_TreeItemMappingContainer:

    pass
class tree_description_TreeItemMapping(description_StyleUpdater, description_TreeMapping, description_TreeItemMappingContainer, description_TreeItemUpdater):

    def __init__(self, domainClass: str, preconditionExpression: str, semanticCandidatesExpression: str, tree_description_TreeItemMapping: set["TreeItemMapping"] = None, tree_description_TreeItemMapping21: set["TreeItemMapping"] = None, tree_description_TreeItemMapping24: "TreeItemMapping" = None, TreeItemDeletionTool: "TreeItemDeletionTool" = None, tree_description_TreeItemMapping28: set["TreeItemCreationTool"] = None, tree_description_TreeItemMapping31: set["TreeItemDragTool"] = None, tree_description_TreeItemMapping33: set["TreePopupMenu"] = None):
        self.domainClass = domainClass
        self.preconditionExpression = preconditionExpression
        self.semanticCandidatesExpression = semanticCandidatesExpression
        self.tree_description_TreeItemMapping = tree_description_TreeItemMapping if tree_description_TreeItemMapping is not None else set()
        self.tree_description_TreeItemMapping21 = tree_description_TreeItemMapping21 if tree_description_TreeItemMapping21 is not None else set()
        self.tree_description_TreeItemMapping24 = tree_description_TreeItemMapping24
        self.TreeItemDeletionTool = TreeItemDeletionTool
        self.tree_description_TreeItemMapping28 = tree_description_TreeItemMapping28 if tree_description_TreeItemMapping28 is not None else set()
        self.tree_description_TreeItemMapping31 = tree_description_TreeItemMapping31 if tree_description_TreeItemMapping31 is not None else set()
        self.tree_description_TreeItemMapping33 = tree_description_TreeItemMapping33 if tree_description_TreeItemMapping33 is not None else set()
        
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
    def domainClass(self) -> str:
        return self.__domainClass

    @domainClass.setter
    def domainClass(self, domainClass: str):
        self.__domainClass = domainClass

    @property
    def tree_description_TreeItemMapping33(self):
        return self.__tree_description_TreeItemMapping33

    @tree_description_TreeItemMapping33.setter
    def tree_description_TreeItemMapping33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemMapping__tree_description_TreeItemMapping33", None)
        self.__tree_description_TreeItemMapping33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreePopupMenu"):
                    opp_val = getattr(item, "TreePopupMenu", None)
                    
                    if opp_val == self:
                        setattr(item, "TreePopupMenu", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreePopupMenu"):
                    opp_val = getattr(item, "TreePopupMenu", None)
                    
                    setattr(item, "TreePopupMenu", self)
                    

    @property
    def TreeItemDeletionTool(self):
        return self.__TreeItemDeletionTool

    @TreeItemDeletionTool.setter
    def TreeItemDeletionTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemMapping__TreeItemDeletionTool", None)
        self.__TreeItemDeletionTool = value
        
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
    def tree_description_TreeItemMapping28(self):
        return self.__tree_description_TreeItemMapping28

    @tree_description_TreeItemMapping28.setter
    def tree_description_TreeItemMapping28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemMapping__tree_description_TreeItemMapping28", None)
        self.__tree_description_TreeItemMapping28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreeItemCreationTool29"):
                    opp_val = getattr(item, "TreeItemCreationTool29", None)
                    
                    if opp_val == self:
                        setattr(item, "TreeItemCreationTool29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreeItemCreationTool29"):
                    opp_val = getattr(item, "TreeItemCreationTool29", None)
                    
                    setattr(item, "TreeItemCreationTool29", self)
                    

    @property
    def tree_description_TreeItemMapping24(self):
        return self.__tree_description_TreeItemMapping24

    @tree_description_TreeItemMapping24.setter
    def tree_description_TreeItemMapping24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemMapping__tree_description_TreeItemMapping24", None)
        self.__tree_description_TreeItemMapping24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeItemMapping25"):
                opp_val = getattr(old_value, "TreeItemMapping25", None)
                if opp_val == self:
                    setattr(old_value, "TreeItemMapping25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeItemMapping25"):
                opp_val = getattr(value, "TreeItemMapping25", None)
                setattr(value, "TreeItemMapping25", self)

    @property
    def tree_description_TreeItemMapping31(self):
        return self.__tree_description_TreeItemMapping31

    @tree_description_TreeItemMapping31.setter
    def tree_description_TreeItemMapping31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemMapping__tree_description_TreeItemMapping31", None)
        self.__tree_description_TreeItemMapping31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreeItemDragTool"):
                    opp_val = getattr(item, "TreeItemDragTool", None)
                    
                    if opp_val == self:
                        setattr(item, "TreeItemDragTool", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreeItemDragTool"):
                    opp_val = getattr(item, "TreeItemDragTool", None)
                    
                    setattr(item, "TreeItemDragTool", self)
                    

    @property
    def tree_description_TreeItemMapping(self):
        return self.__tree_description_TreeItemMapping

    @tree_description_TreeItemMapping.setter
    def tree_description_TreeItemMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemMapping__tree_description_TreeItemMapping", None)
        self.__tree_description_TreeItemMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreeItemMapping19"):
                    opp_val = getattr(item, "TreeItemMapping19", None)
                    
                    if opp_val == self:
                        setattr(item, "TreeItemMapping19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreeItemMapping19"):
                    opp_val = getattr(item, "TreeItemMapping19", None)
                    
                    setattr(item, "TreeItemMapping19", self)
                    

    @property
    def tree_description_TreeItemMapping21(self):
        return self.__tree_description_TreeItemMapping21

    @tree_description_TreeItemMapping21.setter
    def tree_description_TreeItemMapping21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeItemMapping__tree_description_TreeItemMapping21", None)
        self.__tree_description_TreeItemMapping21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreeItemMapping22"):
                    opp_val = getattr(item, "TreeItemMapping22", None)
                    
                    if opp_val == self:
                        setattr(item, "TreeItemMapping22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreeItemMapping22"):
                    opp_val = getattr(item, "TreeItemMapping22", None)
                    
                    setattr(item, "TreeItemMapping22", self)
                    

class description_RepresentationDescription:

    pass
class tree_description_TreeDescription(description_RepresentationDescription, description_TreeItemMappingContainer):

    def __init__(self, domainClass: str, preconditionExpression: str, tree_description_TreeDescription: set["TreeItemCreationTool"] = None, tree_description_TreeDescription15: set["tool_RepresentationCreationDescription"] = None, tree_description_TreeDescription17: set["tool_RepresentationNavigationDescription"] = None):
        self.domainClass = domainClass
        self.preconditionExpression = preconditionExpression
        self.tree_description_TreeDescription = tree_description_TreeDescription if tree_description_TreeDescription is not None else set()
        self.tree_description_TreeDescription15 = tree_description_TreeDescription15 if tree_description_TreeDescription15 is not None else set()
        self.tree_description_TreeDescription17 = tree_description_TreeDescription17 if tree_description_TreeDescription17 is not None else set()
        
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
    def tree_description_TreeDescription17(self):
        return self.__tree_description_TreeDescription17

    @tree_description_TreeDescription17.setter
    def tree_description_TreeDescription17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeDescription__tree_description_TreeDescription17", None)
        self.__tree_description_TreeDescription17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_RepresentationNavigationDescription"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationNavigationDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationNavigationDescription"):
                    opp_val = getattr(item, "tool_RepresentationNavigationDescription", None)
                    
                    setattr(item, "tool_RepresentationNavigationDescription", self)
                    

    @property
    def tree_description_TreeDescription15(self):
        return self.__tree_description_TreeDescription15

    @tree_description_TreeDescription15.setter
    def tree_description_TreeDescription15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeDescription__tree_description_TreeDescription15", None)
        self.__tree_description_TreeDescription15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tool_RepresentationCreationDescription"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "tool_RepresentationCreationDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tool_RepresentationCreationDescription"):
                    opp_val = getattr(item, "tool_RepresentationCreationDescription", None)
                    
                    setattr(item, "tool_RepresentationCreationDescription", self)
                    

    @property
    def tree_description_TreeDescription(self):
        return self.__tree_description_TreeDescription

    @tree_description_TreeDescription.setter
    def tree_description_TreeDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_description_TreeDescription__tree_description_TreeDescription", None)
        self.__tree_description_TreeDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TreeItemCreationTool"):
                    opp_val = getattr(item, "TreeItemCreationTool", None)
                    
                    if opp_val == self:
                        setattr(item, "TreeItemCreationTool", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TreeItemCreationTool"):
                    opp_val = getattr(item, "TreeItemCreationTool", None)
                    
                    setattr(item, "TreeItemCreationTool", self)
                    

class tree_DTreeElementSynchronizer:

    def __init__(self):
        
    def refresh(self, DTreeItem: str):
        # TODO: Implement refresh method
        pass

class LabelStyle:

    pass
class Style:

    pass
class TreeItemUpdater:

    pass
class StyleUpdater:

    pass
class TreeItemMapping:

    pass
class tree_TreeItemStyle(Style, LabelStyle):

    def __init__(self, backgroundColor: str, tree_TreeItemStyle: "tree_DTreeItem" = None):
        self.backgroundColor = backgroundColor
        self.tree_TreeItemStyle = tree_TreeItemStyle
        
    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

    @property
    def tree_TreeItemStyle(self):
        return self.__tree_TreeItemStyle

    @tree_TreeItemStyle.setter
    def tree_TreeItemStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_TreeItemStyle__tree_TreeItemStyle", None)
        self.__tree_TreeItemStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_DTreeItem"):
                opp_val = getattr(old_value, "tree_DTreeItem", None)
                if opp_val == self:
                    setattr(old_value, "tree_DTreeItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_DTreeItem"):
                opp_val = getattr(value, "tree_DTreeItem", None)
                setattr(value, "tree_DTreeItem", self)

class DTreeElement:

    pass
class TreeMapping:

    pass
class DRepresentationElement:

    pass
class tree_DTreeElement(DRepresentationElement):

    pass
class TreeDescription:

    pass
class tree_EObject:

    pass
class DTreeItemContainer:

    pass
class tree_DTreeItem(DTreeElement, DTreeItemContainer):

    def __init__(self, expanded: bool, DTreeItem: "tree_DTreeItemContainer" = None, tree_DTreeItem: "tree_TreeItemStyle" = None, tree_DTreeItem7: "TreeItemMapping" = None, ownedTreeItems: "tree_DTreeItemContainer" = None, tree_DTreeItem10: "StyleUpdater" = None, tree_DTreeItem12: "TreeItemUpdater" = None):
        self.expanded = expanded
        self.DTreeItem = DTreeItem
        self.tree_DTreeItem = tree_DTreeItem
        self.tree_DTreeItem7 = tree_DTreeItem7
        self.ownedTreeItems = ownedTreeItems
        self.tree_DTreeItem10 = tree_DTreeItem10
        self.tree_DTreeItem12 = tree_DTreeItem12
        
    @property
    def expanded(self) -> bool:
        return self.__expanded

    @expanded.setter
    def expanded(self, expanded: bool):
        self.__expanded = expanded

    @property
    def tree_DTreeItem(self):
        return self.__tree_DTreeItem

    @tree_DTreeItem.setter
    def tree_DTreeItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_DTreeItem__tree_DTreeItem", None)
        self.__tree_DTreeItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tree_TreeItemStyle"):
                opp_val = getattr(old_value, "tree_TreeItemStyle", None)
                if opp_val == self:
                    setattr(old_value, "tree_TreeItemStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tree_TreeItemStyle"):
                opp_val = getattr(value, "tree_TreeItemStyle", None)
                setattr(value, "tree_TreeItemStyle", self)

    @property
    def DTreeItem(self):
        return self.__DTreeItem

    @DTreeItem.setter
    def DTreeItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_DTreeItem__DTreeItem", None)
        self.__DTreeItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tree_DTreeItem10(self):
        return self.__tree_DTreeItem10

    @tree_DTreeItem10.setter
    def tree_DTreeItem10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_DTreeItem__tree_DTreeItem10", None)
        self.__tree_DTreeItem10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StyleUpdater"):
                opp_val = getattr(old_value, "StyleUpdater", None)
                if opp_val == self:
                    setattr(old_value, "StyleUpdater", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StyleUpdater"):
                opp_val = getattr(value, "StyleUpdater", None)
                setattr(value, "StyleUpdater", self)

    @property
    def tree_DTreeItem12(self):
        return self.__tree_DTreeItem12

    @tree_DTreeItem12.setter
    def tree_DTreeItem12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_DTreeItem__tree_DTreeItem12", None)
        self.__tree_DTreeItem12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeItemUpdater"):
                opp_val = getattr(old_value, "TreeItemUpdater", None)
                if opp_val == self:
                    setattr(old_value, "TreeItemUpdater", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeItemUpdater"):
                opp_val = getattr(value, "TreeItemUpdater", None)
                setattr(value, "TreeItemUpdater", self)

    @property
    def tree_DTreeItem7(self):
        return self.__tree_DTreeItem7

    @tree_DTreeItem7.setter
    def tree_DTreeItem7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_DTreeItem__tree_DTreeItem7", None)
        self.__tree_DTreeItem7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TreeItemMapping"):
                opp_val = getattr(old_value, "TreeItemMapping", None)
                if opp_val == self:
                    setattr(old_value, "TreeItemMapping", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TreeItemMapping"):
                opp_val = getattr(value, "TreeItemMapping", None)
                setattr(value, "TreeItemMapping", self)

    @property
    def ownedTreeItems(self):
        return self.__ownedTreeItems

    @ownedTreeItems.setter
    def ownedTreeItems(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tree_DTreeItem__ownedTreeItems", None)
        self.__ownedTreeItems = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DTreeItemContainer"):
                opp_val = getattr(old_value, "DTreeItemContainer", None)
                if opp_val == self:
                    setattr(old_value, "DTreeItemContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DTreeItemContainer"):
                opp_val = getattr(value, "DTreeItemContainer", None)
                setattr(value, "DTreeItemContainer", self)

class DRepresentation:

    pass
class tree_DTree(DTreeItemContainer, DRepresentation):

    pass
class DSemanticDecorator:

    pass
class tree_DTreeItemContainer(DSemanticDecorator):

    pass