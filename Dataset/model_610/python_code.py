from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssociationType(Enum):


############################################
# Definition of Classes
############################################

class Annotable:

    pass
class mvc_EventAction(Annotable):

    pass
class mvc_ControllerView(Annotable):

    pass
class mvc_UIComponent(Annotable):

    def __init__(self, layout: str, id: str, name: str, type: str, mvc_UIComponent19: set["mvc_Event"] = None, mvc_UIComponent: "mvc_View" = None, mvc_UIComponent17: "mvc_UIComponent" = None, mvc_UIComponent15: set["mvc_UIComponent"] = None):
        self.layout = layout
        self.id = id
        self.name = name
        self.type = type
        self.mvc_UIComponent19 = mvc_UIComponent19 if mvc_UIComponent19 is not None else set()
        self.mvc_UIComponent = mvc_UIComponent
        self.mvc_UIComponent17 = mvc_UIComponent17
        self.mvc_UIComponent15 = mvc_UIComponent15 if mvc_UIComponent15 is not None else set()
        
    @property
    def layout(self) -> str:
        return self.__layout

    @layout.setter
    def layout(self, layout: str):
        self.__layout = layout

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def mvc_UIComponent17(self):
        return self.__mvc_UIComponent17

    @mvc_UIComponent17.setter
    def mvc_UIComponent17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_UIComponent__mvc_UIComponent17", None)
        self.__mvc_UIComponent17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_UIComponent15"):
                opp_val = getattr(old_value, "mvc_UIComponent15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_UIComponent15"):
                opp_val = getattr(value, "mvc_UIComponent15", None)
                if opp_val is None:
                    setattr(value, "mvc_UIComponent15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_UIComponent(self):
        return self.__mvc_UIComponent

    @mvc_UIComponent.setter
    def mvc_UIComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_UIComponent__mvc_UIComponent", None)
        self.__mvc_UIComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_View"):
                opp_val = getattr(old_value, "mvc_View", None)
                if opp_val == self:
                    setattr(old_value, "mvc_View", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_View"):
                opp_val = getattr(value, "mvc_View", None)
                setattr(value, "mvc_View", self)

    @property
    def mvc_UIComponent19(self):
        return self.__mvc_UIComponent19

    @mvc_UIComponent19.setter
    def mvc_UIComponent19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_UIComponent__mvc_UIComponent19", None)
        self.__mvc_UIComponent19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Event"):
                    opp_val = getattr(item, "mvc_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Event"):
                    opp_val = getattr(item, "mvc_Event", None)
                    
                    setattr(item, "mvc_Event", self)
                    

    @property
    def mvc_UIComponent15(self):
        return self.__mvc_UIComponent15

    @mvc_UIComponent15.setter
    def mvc_UIComponent15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_UIComponent__mvc_UIComponent15", None)
        self.__mvc_UIComponent15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_UIComponent17"):
                    opp_val = getattr(item, "mvc_UIComponent17", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_UIComponent17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_UIComponent17"):
                    opp_val = getattr(item, "mvc_UIComponent17", None)
                    
                    setattr(item, "mvc_UIComponent17", self)
                    

class mvc_View(Annotable):

    def __init__(self, name: str, mvc_View24: "mvc_MVCModel" = None, mvc_View: "mvc_UIComponent" = None, mvc_View49: "mvc_ControllerView" = None):
        self.name = name
        self.mvc_View24 = mvc_View24
        self.mvc_View = mvc_View
        self.mvc_View49 = mvc_View49
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_View49(self):
        return self.__mvc_View49

    @mvc_View49.setter
    def mvc_View49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_View__mvc_View49", None)
        self.__mvc_View49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_ControllerView48"):
                opp_val = getattr(old_value, "mvc_ControllerView48", None)
                if opp_val == self:
                    setattr(old_value, "mvc_ControllerView48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_ControllerView48"):
                opp_val = getattr(value, "mvc_ControllerView48", None)
                setattr(value, "mvc_ControllerView48", self)

    @property
    def mvc_View(self):
        return self.__mvc_View

    @mvc_View.setter
    def mvc_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_View__mvc_View", None)
        self.__mvc_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_UIComponent"):
                opp_val = getattr(old_value, "mvc_UIComponent", None)
                if opp_val == self:
                    setattr(old_value, "mvc_UIComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_UIComponent"):
                opp_val = getattr(value, "mvc_UIComponent", None)
                setattr(value, "mvc_UIComponent", self)

    @property
    def mvc_View24(self):
        return self.__mvc_View24

    @mvc_View24.setter
    def mvc_View24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_View__mvc_View24", None)
        self.__mvc_View24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_MVCModel23"):
                opp_val = getattr(old_value, "mvc_MVCModel23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MVCModel23"):
                opp_val = getattr(value, "mvc_MVCModel23", None)
                if opp_val is None:
                    setattr(value, "mvc_MVCModel23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_Association(Annotable):

    def __init__(self, name: str, containment: bool, lowerBound: int, upperBound: int, type: str, mvc_Association9: "mvc_Entity" = None, mvc_Association: "mvc_Model" = None, mvc_Association12: "mvc_Entity" = None):
        self.name = name
        self.containment = containment
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.type = type
        self.mvc_Association9 = mvc_Association9
        self.mvc_Association = mvc_Association
        self.mvc_Association12 = mvc_Association12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def containment(self) -> bool:
        return self.__containment

    @containment.setter
    def containment(self, containment: bool):
        self.__containment = containment

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mvc_Association(self):
        return self.__mvc_Association

    @mvc_Association.setter
    def mvc_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Association__mvc_Association", None)
        self.__mvc_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Model2"):
                opp_val = getattr(old_value, "mvc_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Model2"):
                opp_val = getattr(value, "mvc_Model2", None)
                if opp_val is None:
                    setattr(value, "mvc_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Association12(self):
        return self.__mvc_Association12

    @mvc_Association12.setter
    def mvc_Association12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Association__mvc_Association12", None)
        self.__mvc_Association12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Entity13"):
                opp_val = getattr(old_value, "mvc_Entity13", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Entity13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Entity13"):
                opp_val = getattr(value, "mvc_Entity13", None)
                setattr(value, "mvc_Entity13", self)

    @property
    def mvc_Association9(self):
        return self.__mvc_Association9

    @mvc_Association9.setter
    def mvc_Association9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Association__mvc_Association9", None)
        self.__mvc_Association9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Entity10"):
                opp_val = getattr(old_value, "mvc_Entity10", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Entity10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Entity10"):
                opp_val = getattr(value, "mvc_Entity10", None)
                setattr(value, "mvc_Entity10", self)

class mvc_Attribute(Annotable):

    def __init__(self, name: str, type: str, mvc_Attribute: "mvc_Entity" = None):
        self.name = name
        self.type = type
        self.mvc_Attribute = mvc_Attribute
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Attribute(self):
        return self.__mvc_Attribute

    @mvc_Attribute.setter
    def mvc_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Attribute__mvc_Attribute", None)
        self.__mvc_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Entity4"):
                opp_val = getattr(old_value, "mvc_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Entity4"):
                opp_val = getattr(value, "mvc_Entity4", None)
                if opp_val is None:
                    setattr(value, "mvc_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_Action(Annotable):

    def __init__(self, name: str, mvc_Action39: "mvc_Event" = None, mvc_Action42: "mvc_Event" = None, mvc_Action45: set["mvc_Event"] = None, mvc_Action: "mvc_Controller" = None, mvc_Action58: "mvc_EventAction" = None):
        self.name = name
        self.mvc_Action39 = mvc_Action39
        self.mvc_Action42 = mvc_Action42
        self.mvc_Action45 = mvc_Action45 if mvc_Action45 is not None else set()
        self.mvc_Action = mvc_Action
        self.mvc_Action58 = mvc_Action58
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Action39(self):
        return self.__mvc_Action39

    @mvc_Action39.setter
    def mvc_Action39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Action__mvc_Action39", None)
        self.__mvc_Action39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Event40"):
                opp_val = getattr(old_value, "mvc_Event40", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Event40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Event40"):
                opp_val = getattr(value, "mvc_Event40", None)
                setattr(value, "mvc_Event40", self)

    @property
    def mvc_Action42(self):
        return self.__mvc_Action42

    @mvc_Action42.setter
    def mvc_Action42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Action__mvc_Action42", None)
        self.__mvc_Action42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Event43"):
                opp_val = getattr(old_value, "mvc_Event43", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Event43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Event43"):
                opp_val = getattr(value, "mvc_Event43", None)
                setattr(value, "mvc_Event43", self)

    @property
    def mvc_Action45(self):
        return self.__mvc_Action45

    @mvc_Action45.setter
    def mvc_Action45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Action__mvc_Action45", None)
        self.__mvc_Action45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Event46"):
                    opp_val = getattr(item, "mvc_Event46", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Event46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Event46"):
                    opp_val = getattr(item, "mvc_Event46", None)
                    
                    setattr(item, "mvc_Event46", self)
                    

    @property
    def mvc_Action(self):
        return self.__mvc_Action

    @mvc_Action.setter
    def mvc_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Action__mvc_Action", None)
        self.__mvc_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Controller33"):
                opp_val = getattr(old_value, "mvc_Controller33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Controller33"):
                opp_val = getattr(value, "mvc_Controller33", None)
                if opp_val is None:
                    setattr(value, "mvc_Controller33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Action58(self):
        return self.__mvc_Action58

    @mvc_Action58.setter
    def mvc_Action58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Action__mvc_Action58", None)
        self.__mvc_Action58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_EventAction57"):
                opp_val = getattr(old_value, "mvc_EventAction57", None)
                if opp_val == self:
                    setattr(old_value, "mvc_EventAction57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_EventAction57"):
                opp_val = getattr(value, "mvc_EventAction57", None)
                setattr(value, "mvc_EventAction57", self)

class mvc_Event(Annotable):

    def __init__(self, name: str, mvc_Event: "mvc_UIComponent" = None, mvc_Event27: "mvc_MVCModel" = None, mvc_Event40: "mvc_Action" = None, mvc_Event43: "mvc_Action" = None, mvc_Event46: "mvc_Action" = None, mvc_Event61: "mvc_EventAction" = None):
        self.name = name
        self.mvc_Event = mvc_Event
        self.mvc_Event27 = mvc_Event27
        self.mvc_Event40 = mvc_Event40
        self.mvc_Event43 = mvc_Event43
        self.mvc_Event46 = mvc_Event46
        self.mvc_Event61 = mvc_Event61
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Event40(self):
        return self.__mvc_Event40

    @mvc_Event40.setter
    def mvc_Event40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Event__mvc_Event40", None)
        self.__mvc_Event40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Action39"):
                opp_val = getattr(old_value, "mvc_Action39", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Action39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Action39"):
                opp_val = getattr(value, "mvc_Action39", None)
                setattr(value, "mvc_Action39", self)

    @property
    def mvc_Event43(self):
        return self.__mvc_Event43

    @mvc_Event43.setter
    def mvc_Event43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Event__mvc_Event43", None)
        self.__mvc_Event43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Action42"):
                opp_val = getattr(old_value, "mvc_Action42", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Action42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Action42"):
                opp_val = getattr(value, "mvc_Action42", None)
                setattr(value, "mvc_Action42", self)

    @property
    def mvc_Event46(self):
        return self.__mvc_Event46

    @mvc_Event46.setter
    def mvc_Event46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Event__mvc_Event46", None)
        self.__mvc_Event46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Action45"):
                opp_val = getattr(old_value, "mvc_Action45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Action45"):
                opp_val = getattr(value, "mvc_Action45", None)
                if opp_val is None:
                    setattr(value, "mvc_Action45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Event(self):
        return self.__mvc_Event

    @mvc_Event.setter
    def mvc_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Event__mvc_Event", None)
        self.__mvc_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_UIComponent19"):
                opp_val = getattr(old_value, "mvc_UIComponent19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_UIComponent19"):
                opp_val = getattr(value, "mvc_UIComponent19", None)
                if opp_val is None:
                    setattr(value, "mvc_UIComponent19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Event61(self):
        return self.__mvc_Event61

    @mvc_Event61.setter
    def mvc_Event61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Event__mvc_Event61", None)
        self.__mvc_Event61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_EventAction60"):
                opp_val = getattr(old_value, "mvc_EventAction60", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_EventAction60"):
                opp_val = getattr(value, "mvc_EventAction60", None)
                if opp_val is None:
                    setattr(value, "mvc_EventAction60", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Event27(self):
        return self.__mvc_Event27

    @mvc_Event27.setter
    def mvc_Event27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Event__mvc_Event27", None)
        self.__mvc_Event27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_MVCModel26"):
                opp_val = getattr(old_value, "mvc_MVCModel26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MVCModel26"):
                opp_val = getattr(value, "mvc_MVCModel26", None)
                if opp_val is None:
                    setattr(value, "mvc_MVCModel26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_Component(Annotable):

    def __init__(self, name: str, mvc_Component: "mvc_MVCModel" = None, mvc_Component54: set["mvc_Controller"] = None):
        self.name = name
        self.mvc_Component = mvc_Component
        self.mvc_Component54 = mvc_Component54 if mvc_Component54 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Component(self):
        return self.__mvc_Component

    @mvc_Component.setter
    def mvc_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Component__mvc_Component", None)
        self.__mvc_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_MVCModel31"):
                opp_val = getattr(old_value, "mvc_MVCModel31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MVCModel31"):
                opp_val = getattr(value, "mvc_MVCModel31", None)
                if opp_val is None:
                    setattr(value, "mvc_MVCModel31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Component54(self):
        return self.__mvc_Component54

    @mvc_Component54.setter
    def mvc_Component54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Component__mvc_Component54", None)
        self.__mvc_Component54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Controller55"):
                    opp_val = getattr(item, "mvc_Controller55", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Controller55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Controller55"):
                    opp_val = getattr(item, "mvc_Controller55", None)
                    
                    setattr(item, "mvc_Controller55", self)
                    

class mvc_MVCModel(Annotable):

    def __init__(self, name: str, version: str, mvc_MVCModel: set["mvc_Model"] = None, mvc_MVCModel23: set["mvc_View"] = None, mvc_MVCModel26: set["mvc_Event"] = None, mvc_MVCModel29: set["mvc_Controller"] = None, mvc_MVCModel31: set["mvc_Component"] = None):
        self.name = name
        self.version = version
        self.mvc_MVCModel = mvc_MVCModel if mvc_MVCModel is not None else set()
        self.mvc_MVCModel23 = mvc_MVCModel23 if mvc_MVCModel23 is not None else set()
        self.mvc_MVCModel26 = mvc_MVCModel26 if mvc_MVCModel26 is not None else set()
        self.mvc_MVCModel29 = mvc_MVCModel29 if mvc_MVCModel29 is not None else set()
        self.mvc_MVCModel31 = mvc_MVCModel31 if mvc_MVCModel31 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def mvc_MVCModel26(self):
        return self.__mvc_MVCModel26

    @mvc_MVCModel26.setter
    def mvc_MVCModel26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MVCModel__mvc_MVCModel26", None)
        self.__mvc_MVCModel26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Event27"):
                    opp_val = getattr(item, "mvc_Event27", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Event27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Event27"):
                    opp_val = getattr(item, "mvc_Event27", None)
                    
                    setattr(item, "mvc_Event27", self)
                    

    @property
    def mvc_MVCModel31(self):
        return self.__mvc_MVCModel31

    @mvc_MVCModel31.setter
    def mvc_MVCModel31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MVCModel__mvc_MVCModel31", None)
        self.__mvc_MVCModel31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Component"):
                    opp_val = getattr(item, "mvc_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Component"):
                    opp_val = getattr(item, "mvc_Component", None)
                    
                    setattr(item, "mvc_Component", self)
                    

    @property
    def mvc_MVCModel(self):
        return self.__mvc_MVCModel

    @mvc_MVCModel.setter
    def mvc_MVCModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MVCModel__mvc_MVCModel", None)
        self.__mvc_MVCModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Model21"):
                    opp_val = getattr(item, "mvc_Model21", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Model21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Model21"):
                    opp_val = getattr(item, "mvc_Model21", None)
                    
                    setattr(item, "mvc_Model21", self)
                    

    @property
    def mvc_MVCModel23(self):
        return self.__mvc_MVCModel23

    @mvc_MVCModel23.setter
    def mvc_MVCModel23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MVCModel__mvc_MVCModel23", None)
        self.__mvc_MVCModel23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_View24"):
                    opp_val = getattr(item, "mvc_View24", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_View24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_View24"):
                    opp_val = getattr(item, "mvc_View24", None)
                    
                    setattr(item, "mvc_View24", self)
                    

    @property
    def mvc_MVCModel29(self):
        return self.__mvc_MVCModel29

    @mvc_MVCModel29.setter
    def mvc_MVCModel29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MVCModel__mvc_MVCModel29", None)
        self.__mvc_MVCModel29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Controller"):
                    opp_val = getattr(item, "mvc_Controller", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Controller", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Controller"):
                    opp_val = getattr(item, "mvc_Controller", None)
                    
                    setattr(item, "mvc_Controller", self)
                    

class mvc_Controller(Annotable):

    def __init__(self, name: str, mvc_Controller37: set["mvc_EventAction"] = None, mvc_Controller: "mvc_MVCModel" = None, mvc_Controller33: set["mvc_Action"] = None, mvc_Controller35: set["mvc_ControllerView"] = None, mvc_Controller55: "mvc_Component" = None):
        self.name = name
        self.mvc_Controller37 = mvc_Controller37 if mvc_Controller37 is not None else set()
        self.mvc_Controller = mvc_Controller
        self.mvc_Controller33 = mvc_Controller33 if mvc_Controller33 is not None else set()
        self.mvc_Controller35 = mvc_Controller35 if mvc_Controller35 is not None else set()
        self.mvc_Controller55 = mvc_Controller55
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Controller37(self):
        return self.__mvc_Controller37

    @mvc_Controller37.setter
    def mvc_Controller37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__mvc_Controller37", None)
        self.__mvc_Controller37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_EventAction"):
                    opp_val = getattr(item, "mvc_EventAction", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_EventAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_EventAction"):
                    opp_val = getattr(item, "mvc_EventAction", None)
                    
                    setattr(item, "mvc_EventAction", self)
                    

    @property
    def mvc_Controller33(self):
        return self.__mvc_Controller33

    @mvc_Controller33.setter
    def mvc_Controller33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__mvc_Controller33", None)
        self.__mvc_Controller33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Action"):
                    opp_val = getattr(item, "mvc_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Action"):
                    opp_val = getattr(item, "mvc_Action", None)
                    
                    setattr(item, "mvc_Action", self)
                    

    @property
    def mvc_Controller35(self):
        return self.__mvc_Controller35

    @mvc_Controller35.setter
    def mvc_Controller35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__mvc_Controller35", None)
        self.__mvc_Controller35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_ControllerView"):
                    opp_val = getattr(item, "mvc_ControllerView", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_ControllerView", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_ControllerView"):
                    opp_val = getattr(item, "mvc_ControllerView", None)
                    
                    setattr(item, "mvc_ControllerView", self)
                    

    @property
    def mvc_Controller(self):
        return self.__mvc_Controller

    @mvc_Controller.setter
    def mvc_Controller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__mvc_Controller", None)
        self.__mvc_Controller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_MVCModel29"):
                opp_val = getattr(old_value, "mvc_MVCModel29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MVCModel29"):
                opp_val = getattr(value, "mvc_MVCModel29", None)
                if opp_val is None:
                    setattr(value, "mvc_MVCModel29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Controller55(self):
        return self.__mvc_Controller55

    @mvc_Controller55.setter
    def mvc_Controller55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__mvc_Controller55", None)
        self.__mvc_Controller55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Component54"):
                opp_val = getattr(old_value, "mvc_Component54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Component54"):
                opp_val = getattr(value, "mvc_Component54", None)
                if opp_val is None:
                    setattr(value, "mvc_Component54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_Entity(Annotable):

    def __init__(self, name: str, mvc_Entity7: "mvc_Entity" = None, mvc_Entity5: set["mvc_Entity"] = None, mvc_Entity10: "mvc_Association" = None, mvc_Entity: "mvc_Model" = None, mvc_Entity4: set["mvc_Attribute"] = None, mvc_Entity13: "mvc_Association" = None):
        self.name = name
        self.mvc_Entity7 = mvc_Entity7
        self.mvc_Entity5 = mvc_Entity5 if mvc_Entity5 is not None else set()
        self.mvc_Entity10 = mvc_Entity10
        self.mvc_Entity = mvc_Entity
        self.mvc_Entity4 = mvc_Entity4 if mvc_Entity4 is not None else set()
        self.mvc_Entity13 = mvc_Entity13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Entity5(self):
        return self.__mvc_Entity5

    @mvc_Entity5.setter
    def mvc_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Entity__mvc_Entity5", None)
        self.__mvc_Entity5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Entity7"):
                    opp_val = getattr(item, "mvc_Entity7", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Entity7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Entity7"):
                    opp_val = getattr(item, "mvc_Entity7", None)
                    
                    setattr(item, "mvc_Entity7", self)
                    

    @property
    def mvc_Entity(self):
        return self.__mvc_Entity

    @mvc_Entity.setter
    def mvc_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Entity__mvc_Entity", None)
        self.__mvc_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Model"):
                opp_val = getattr(old_value, "mvc_Model", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Model"):
                opp_val = getattr(value, "mvc_Model", None)
                setattr(value, "mvc_Model", self)

    @property
    def mvc_Entity7(self):
        return self.__mvc_Entity7

    @mvc_Entity7.setter
    def mvc_Entity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Entity__mvc_Entity7", None)
        self.__mvc_Entity7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Entity5"):
                opp_val = getattr(old_value, "mvc_Entity5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Entity5"):
                opp_val = getattr(value, "mvc_Entity5", None)
                if opp_val is None:
                    setattr(value, "mvc_Entity5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Entity10(self):
        return self.__mvc_Entity10

    @mvc_Entity10.setter
    def mvc_Entity10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Entity__mvc_Entity10", None)
        self.__mvc_Entity10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Association9"):
                opp_val = getattr(old_value, "mvc_Association9", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Association9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Association9"):
                opp_val = getattr(value, "mvc_Association9", None)
                setattr(value, "mvc_Association9", self)

    @property
    def mvc_Entity4(self):
        return self.__mvc_Entity4

    @mvc_Entity4.setter
    def mvc_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Entity__mvc_Entity4", None)
        self.__mvc_Entity4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Attribute"):
                    opp_val = getattr(item, "mvc_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Attribute"):
                    opp_val = getattr(item, "mvc_Attribute", None)
                    
                    setattr(item, "mvc_Attribute", self)
                    

    @property
    def mvc_Entity13(self):
        return self.__mvc_Entity13

    @mvc_Entity13.setter
    def mvc_Entity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Entity__mvc_Entity13", None)
        self.__mvc_Entity13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Association12"):
                opp_val = getattr(old_value, "mvc_Association12", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Association12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Association12"):
                opp_val = getattr(value, "mvc_Association12", None)
                setattr(value, "mvc_Association12", self)

class mvc_Model(Annotable):

    def __init__(self, name: str, mvc_Model: "mvc_Entity" = None, mvc_Model2: set["mvc_Association"] = None, mvc_Model21: "mvc_MVCModel" = None, mvc_Model52: "mvc_ControllerView" = None):
        self.name = name
        self.mvc_Model = mvc_Model
        self.mvc_Model2 = mvc_Model2 if mvc_Model2 is not None else set()
        self.mvc_Model21 = mvc_Model21
        self.mvc_Model52 = mvc_Model52
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Model52(self):
        return self.__mvc_Model52

    @mvc_Model52.setter
    def mvc_Model52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Model__mvc_Model52", None)
        self.__mvc_Model52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_ControllerView51"):
                opp_val = getattr(old_value, "mvc_ControllerView51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_ControllerView51"):
                opp_val = getattr(value, "mvc_ControllerView51", None)
                if opp_val is None:
                    setattr(value, "mvc_ControllerView51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Model2(self):
        return self.__mvc_Model2

    @mvc_Model2.setter
    def mvc_Model2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Model__mvc_Model2", None)
        self.__mvc_Model2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Association"):
                    opp_val = getattr(item, "mvc_Association", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Association", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Association"):
                    opp_val = getattr(item, "mvc_Association", None)
                    
                    setattr(item, "mvc_Association", self)
                    

    @property
    def mvc_Model21(self):
        return self.__mvc_Model21

    @mvc_Model21.setter
    def mvc_Model21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Model__mvc_Model21", None)
        self.__mvc_Model21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_MVCModel"):
                opp_val = getattr(old_value, "mvc_MVCModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MVCModel"):
                opp_val = getattr(value, "mvc_MVCModel", None)
                if opp_val is None:
                    setattr(value, "mvc_MVCModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Model(self):
        return self.__mvc_Model

    @mvc_Model.setter
    def mvc_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Model__mvc_Model", None)
        self.__mvc_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Entity"):
                opp_val = getattr(old_value, "mvc_Entity", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Entity"):
                opp_val = getattr(value, "mvc_Entity", None)
                setattr(value, "mvc_Entity", self)
