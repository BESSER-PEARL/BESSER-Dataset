from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Location:

    pass
class LayoutConstraint:

    pass
class notation_LayoutConstraint(ABC):

    pass
class NotationElement:

    pass
class notation_Location(NotationElement, LayoutConstraint):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


class notation_View(NotationElement):

    def __init__(self, viewDetails: str, viewType: str, notation_View: set["notation_Node"] = None, notation_View2: "notation_EObject" = None, source: set["notation_Edge"] = None, target: set["notation_Edge"] = None, View: "notation_Edge" = None, View10: "notation_Edge" = None):
        self.viewDetails = viewDetails
        self.viewType = viewType
        self.notation_View = notation_View if notation_View is not None else set()
        self.notation_View2 = notation_View2
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.View = View
        self.View10 = View10
        
        pass
    @property
    def viewType(self):
        return self.__viewType

    @viewType.setter
    def viewType(self, viewType: str):
        self.__viewType = viewType


    @property
    def viewDetails(self):
        return self.__viewDetails

    @viewDetails.setter
    def viewDetails(self, viewDetails: str):
        self.__viewDetails = viewDetails


    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__source", None)
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
                    

    @property
    def notation_View2(self):
        return self.__notation_View2

    @notation_View2.setter
    def notation_View2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__notation_View2", None)
        self.__notation_View2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_EObject"):
                opp_val = getattr(old_value, "notation_EObject", None)
                if opp_val == self:
                    setattr(old_value, "notation_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_EObject"):
                opp_val = getattr(value, "notation_EObject", None)
                setattr(value, "notation_EObject", self)

    @property
    def View10(self):
        return self.__View10

    @View10.setter
    def View10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__View10", None)
        self.__View10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetEdges"):
                opp_val = getattr(old_value, "targetEdges", None)
                if opp_val == self:
                    setattr(old_value, "targetEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetEdges"):
                opp_val = getattr(value, "targetEdges", None)
                setattr(value, "targetEdges", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Edge5"):
                    opp_val = getattr(item, "Edge5", None)
                    
                    if opp_val == self:
                        setattr(item, "Edge5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Edge5"):
                    opp_val = getattr(item, "Edge5", None)
                    
                    setattr(item, "Edge5", self)
                    

    @property
    def notation_View(self):
        return self.__notation_View

    @notation_View.setter
    def notation_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__notation_View", None)
        self.__notation_View = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_Node"):
                    opp_val = getattr(item, "notation_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_Node"):
                    opp_val = getattr(item, "notation_Node", None)
                    
                    setattr(item, "notation_Node", self)
                    

    @property
    def View(self):
        return self.__View

    @View.setter
    def View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_View__View", None)
        self.__View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceEdges"):
                opp_val = getattr(old_value, "sourceEdges", None)
                if opp_val == self:
                    setattr(old_value, "sourceEdges", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceEdges"):
                opp_val = getattr(value, "sourceEdges", None)
                setattr(value, "sourceEdges", self)

    def getAllChildren(self) :
        # TODO: Implement getAllChildren method
        pass

class Node:

    pass
class notation_MindMapNode(Node):

    pass
class notation_Note(Node):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class notation_ExpandableNode(Node):

    def __init__(self, expanded: bool, hasChildren: bool, template: str):
        self.expanded = expanded
        self.hasChildren = hasChildren
        self.template = template
        
        pass
    @property
    def expanded(self):
        return self.__expanded

    @expanded.setter
    def expanded(self, expanded: bool):
        self.__expanded = expanded


    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, template: str):
        self.__template = template


    @property
    def hasChildren(self):
        return self.__hasChildren

    @hasChildren.setter
    def hasChildren(self, hasChildren: bool):
        self.__hasChildren = hasChildren


class notation_CategorySeparator(Node):

    def __init__(self, category: str, newChildCodeSyncType: str, newChildIcon: str):
        self.category = category
        self.newChildCodeSyncType = newChildCodeSyncType
        self.newChildIcon = newChildIcon
        
        pass
    @property
    def newChildIcon(self):
        return self.__newChildIcon

    @newChildIcon.setter
    def newChildIcon(self, newChildIcon: str):
        self.__newChildIcon = newChildIcon


    @property
    def newChildCodeSyncType(self):
        return self.__newChildCodeSyncType

    @newChildCodeSyncType.setter
    def newChildCodeSyncType(self, newChildCodeSyncType: str):
        self.__newChildCodeSyncType = newChildCodeSyncType


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


class notation_Bounds(Location):

    def __init__(self, height: int, width: int, notation_Bounds: "notation_Node" = None):
        self.height = height
        self.width = width
        self.notation_Bounds = notation_Bounds
        
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


    @property
    def notation_Bounds(self):
        return self.__notation_Bounds

    @notation_Bounds.setter
    def notation_Bounds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Bounds__notation_Bounds", None)
        self.__notation_Bounds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Node7"):
                opp_val = getattr(old_value, "notation_Node7", None)
                if opp_val == self:
                    setattr(old_value, "notation_Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Node7"):
                opp_val = getattr(value, "notation_Node7", None)
                setattr(value, "notation_Node7", self)

class View:

    pass
class notation_Diagram(View):

    def __init__(self, name: str, locationForNewElements: str, showLocationForNewElementsDialog: bool, notation_Diagram: set["notation_Edge"] = None):
        self.name = name
        self.locationForNewElements = locationForNewElements
        self.showLocationForNewElementsDialog = showLocationForNewElementsDialog
        self.notation_Diagram = notation_Diagram if notation_Diagram is not None else set()
        
        pass
    @property
    def showLocationForNewElementsDialog(self):
        return self.__showLocationForNewElementsDialog

    @showLocationForNewElementsDialog.setter
    def showLocationForNewElementsDialog(self, showLocationForNewElementsDialog: bool):
        self.__showLocationForNewElementsDialog = showLocationForNewElementsDialog


    @property
    def locationForNewElements(self):
        return self.__locationForNewElements

    @locationForNewElements.setter
    def locationForNewElements(self, locationForNewElements: str):
        self.__locationForNewElements = locationForNewElements


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def notation_Diagram(self):
        return self.__notation_Diagram

    @notation_Diagram.setter
    def notation_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Diagram__notation_Diagram", None)
        self.__notation_Diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_Edge"):
                    opp_val = getattr(item, "notation_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_Edge"):
                    opp_val = getattr(item, "notation_Edge", None)
                    
                    setattr(item, "notation_Edge", self)
                    

class notation_Edge(View):

    pass
class notation_EObject:

    pass
class notation_Node(View):

    pass
class notation_NotationElement(ABC):

    def __init__(self, id: str, idBeforeRemoval: str):
        self.id = id
        self.idBeforeRemoval = idBeforeRemoval
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def idBeforeRemoval(self):
        return self.__idBeforeRemoval

    @idBeforeRemoval.setter
    def idBeforeRemoval(self, idBeforeRemoval: str):
        self.__idBeforeRemoval = idBeforeRemoval

