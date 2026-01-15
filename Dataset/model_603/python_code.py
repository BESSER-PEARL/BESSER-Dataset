from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AssociationType(Enum):


############################################
# Definition of Classes
############################################

class UIComponent:

    pass
class mvc_UIActions(UIComponent):

    pass
class mvc_UIInput(UIComponent):

    pass
class mvc_UILayout(UIComponent):

    def __init__(self, orientation: str, columns: int, mvc_UILayout: "mvc_View" = None, mvc_UILayout59: set["mvc_View"] = None, mvc_UILayout57: set["mvc_UIComponent"] = None):
        self.orientation = orientation
        self.columns = columns
        self.mvc_UILayout = mvc_UILayout
        self.mvc_UILayout59 = mvc_UILayout59 if mvc_UILayout59 is not None else set()
        self.mvc_UILayout57 = mvc_UILayout57 if mvc_UILayout57 is not None else set()
        
    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

    @property
    def mvc_UILayout59(self):
        return self.__mvc_UILayout59

    @mvc_UILayout59.setter
    def mvc_UILayout59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_UILayout__mvc_UILayout59", None)
        self.__mvc_UILayout59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_View60"):
                    opp_val = getattr(item, "mvc_View60", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_View60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_View60"):
                    opp_val = getattr(item, "mvc_View60", None)
                    
                    setattr(item, "mvc_View60", self)
                    

    @property
    def mvc_UILayout57(self):
        return self.__mvc_UILayout57

    @mvc_UILayout57.setter
    def mvc_UILayout57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_UILayout__mvc_UILayout57", None)
        self.__mvc_UILayout57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_UIComponent"):
                    opp_val = getattr(item, "mvc_UIComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_UIComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_UIComponent"):
                    opp_val = getattr(item, "mvc_UIComponent", None)
                    
                    setattr(item, "mvc_UIComponent", self)
                    

    @property
    def mvc_UILayout(self):
        return self.__mvc_UILayout

    @mvc_UILayout.setter
    def mvc_UILayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_UILayout__mvc_UILayout", None)
        self.__mvc_UILayout = value
        
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

class Annotable:

    pass
class mvc_EventAction(Annotable):

    pass
class mvc_Component(Annotable):

    def __init__(self, name: str, mvc_Component: "mvc_MVCModel" = None, mvc_Component48: set["mvc_Controller"] = None):
        self.name = name
        self.mvc_Component = mvc_Component
        self.mvc_Component48 = mvc_Component48 if mvc_Component48 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Component48(self):
        return self.__mvc_Component48

    @mvc_Component48.setter
    def mvc_Component48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Component__mvc_Component48", None)
        self.__mvc_Component48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Controller49"):
                    opp_val = getattr(item, "mvc_Controller49", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Controller49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Controller49"):
                    opp_val = getattr(item, "mvc_Controller49", None)
                    
                    setattr(item, "mvc_Controller49", self)
                    

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
            if hasattr(old_value, "mvc_MVCModel25"):
                opp_val = getattr(old_value, "mvc_MVCModel25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MVCModel25"):
                opp_val = getattr(value, "mvc_MVCModel25", None)
                if opp_val is None:
                    setattr(value, "mvc_MVCModel25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_View(Annotable):

    def __init__(self, name: str, mvc_View19: "mvc_MVCModel" = None, mvc_View: "mvc_UILayout" = None, mvc_View43: "mvc_ControllerView" = None, mvc_View60: "mvc_UILayout" = None):
        self.name = name
        self.mvc_View19 = mvc_View19
        self.mvc_View = mvc_View
        self.mvc_View43 = mvc_View43
        self.mvc_View60 = mvc_View60
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_View19(self):
        return self.__mvc_View19

    @mvc_View19.setter
    def mvc_View19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_View__mvc_View19", None)
        self.__mvc_View19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_MVCModel18"):
                opp_val = getattr(old_value, "mvc_MVCModel18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MVCModel18"):
                opp_val = getattr(value, "mvc_MVCModel18", None)
                if opp_val is None:
                    setattr(value, "mvc_MVCModel18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_View43(self):
        return self.__mvc_View43

    @mvc_View43.setter
    def mvc_View43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_View__mvc_View43", None)
        self.__mvc_View43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_ControllerView42"):
                opp_val = getattr(old_value, "mvc_ControllerView42", None)
                if opp_val == self:
                    setattr(old_value, "mvc_ControllerView42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_ControllerView42"):
                opp_val = getattr(value, "mvc_ControllerView42", None)
                setattr(value, "mvc_ControllerView42", self)

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
            if hasattr(old_value, "mvc_UILayout"):
                opp_val = getattr(old_value, "mvc_UILayout", None)
                if opp_val == self:
                    setattr(old_value, "mvc_UILayout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_UILayout"):
                opp_val = getattr(value, "mvc_UILayout", None)
                setattr(value, "mvc_UILayout", self)

    @property
    def mvc_View60(self):
        return self.__mvc_View60

    @mvc_View60.setter
    def mvc_View60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_View__mvc_View60", None)
        self.__mvc_View60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_UILayout59"):
                opp_val = getattr(old_value, "mvc_UILayout59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_UILayout59"):
                opp_val = getattr(value, "mvc_UILayout59", None)
                if opp_val is None:
                    setattr(value, "mvc_UILayout59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_Controller(Annotable):

    def __init__(self, name: str, mvc_Controller: "mvc_MVCModel" = None, mvc_Controller27: set["mvc_Action"] = None, mvc_Controller49: "mvc_Component" = None, mvc_Controller29: set["mvc_ControllerView"] = None, mvc_Controller31: set["mvc_EventAction"] = None):
        self.name = name
        self.mvc_Controller = mvc_Controller
        self.mvc_Controller27 = mvc_Controller27 if mvc_Controller27 is not None else set()
        self.mvc_Controller49 = mvc_Controller49
        self.mvc_Controller29 = mvc_Controller29 if mvc_Controller29 is not None else set()
        self.mvc_Controller31 = mvc_Controller31 if mvc_Controller31 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Controller27(self):
        return self.__mvc_Controller27

    @mvc_Controller27.setter
    def mvc_Controller27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__mvc_Controller27", None)
        self.__mvc_Controller27 = value if value is not None else set()
        
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
    def mvc_Controller31(self):
        return self.__mvc_Controller31

    @mvc_Controller31.setter
    def mvc_Controller31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__mvc_Controller31", None)
        self.__mvc_Controller31 = value if value is not None else set()
        
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
    def mvc_Controller49(self):
        return self.__mvc_Controller49

    @mvc_Controller49.setter
    def mvc_Controller49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__mvc_Controller49", None)
        self.__mvc_Controller49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Component48"):
                opp_val = getattr(old_value, "mvc_Component48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Component48"):
                opp_val = getattr(value, "mvc_Component48", None)
                if opp_val is None:
                    setattr(value, "mvc_Component48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Controller29(self):
        return self.__mvc_Controller29

    @mvc_Controller29.setter
    def mvc_Controller29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Controller__mvc_Controller29", None)
        self.__mvc_Controller29 = value if value is not None else set()
        
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

class mvc_ControllerView(Annotable):

    pass
class mvc_Event(Annotable):

    def __init__(self, name: str, mvc_Event: "mvc_MVCModel" = None, mvc_Event34: "mvc_Action" = None, mvc_Event37: "mvc_Action" = None, mvc_Event40: "mvc_Action" = None, mvc_Event55: "mvc_EventAction" = None, mvc_Event64: "mvc_UIActions" = None):
        self.name = name
        self.mvc_Event = mvc_Event
        self.mvc_Event34 = mvc_Event34
        self.mvc_Event37 = mvc_Event37
        self.mvc_Event40 = mvc_Event40
        self.mvc_Event55 = mvc_Event55
        self.mvc_Event64 = mvc_Event64
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Event37(self):
        return self.__mvc_Event37

    @mvc_Event37.setter
    def mvc_Event37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Event__mvc_Event37", None)
        self.__mvc_Event37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Action36"):
                opp_val = getattr(old_value, "mvc_Action36", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Action36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Action36"):
                opp_val = getattr(value, "mvc_Action36", None)
                setattr(value, "mvc_Action36", self)

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Action39"):
                opp_val = getattr(value, "mvc_Action39", None)
                if opp_val is None:
                    setattr(value, "mvc_Action39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Event64(self):
        return self.__mvc_Event64

    @mvc_Event64.setter
    def mvc_Event64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Event__mvc_Event64", None)
        self.__mvc_Event64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_UIActions"):
                opp_val = getattr(old_value, "mvc_UIActions", None)
                if opp_val == self:
                    setattr(old_value, "mvc_UIActions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_UIActions"):
                opp_val = getattr(value, "mvc_UIActions", None)
                setattr(value, "mvc_UIActions", self)

    @property
    def mvc_Event55(self):
        return self.__mvc_Event55

    @mvc_Event55.setter
    def mvc_Event55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Event__mvc_Event55", None)
        self.__mvc_Event55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_EventAction54"):
                opp_val = getattr(old_value, "mvc_EventAction54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_EventAction54"):
                opp_val = getattr(value, "mvc_EventAction54", None)
                if opp_val is None:
                    setattr(value, "mvc_EventAction54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Event34(self):
        return self.__mvc_Event34

    @mvc_Event34.setter
    def mvc_Event34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Event__mvc_Event34", None)
        self.__mvc_Event34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Action33"):
                opp_val = getattr(old_value, "mvc_Action33", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Action33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Action33"):
                opp_val = getattr(value, "mvc_Action33", None)
                setattr(value, "mvc_Action33", self)

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
            if hasattr(old_value, "mvc_MVCModel21"):
                opp_val = getattr(old_value, "mvc_MVCModel21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_MVCModel21"):
                opp_val = getattr(value, "mvc_MVCModel21", None)
                if opp_val is None:
                    setattr(value, "mvc_MVCModel21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_Action(Annotable):

    def __init__(self, name: str, mvc_Action: "mvc_Controller" = None, mvc_Action33: "mvc_Event" = None, mvc_Action36: "mvc_Event" = None, mvc_Action39: set["mvc_Event"] = None, mvc_Action52: "mvc_EventAction" = None):
        self.name = name
        self.mvc_Action = mvc_Action
        self.mvc_Action33 = mvc_Action33
        self.mvc_Action36 = mvc_Action36
        self.mvc_Action39 = mvc_Action39 if mvc_Action39 is not None else set()
        self.mvc_Action52 = mvc_Action52
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "mvc_Controller27"):
                opp_val = getattr(old_value, "mvc_Controller27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Controller27"):
                opp_val = getattr(value, "mvc_Controller27", None)
                if opp_val is None:
                    setattr(value, "mvc_Controller27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mvc_Action52(self):
        return self.__mvc_Action52

    @mvc_Action52.setter
    def mvc_Action52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Action__mvc_Action52", None)
        self.__mvc_Action52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_EventAction51"):
                opp_val = getattr(old_value, "mvc_EventAction51", None)
                if opp_val == self:
                    setattr(old_value, "mvc_EventAction51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_EventAction51"):
                opp_val = getattr(value, "mvc_EventAction51", None)
                setattr(value, "mvc_EventAction51", self)

    @property
    def mvc_Action39(self):
        return self.__mvc_Action39

    @mvc_Action39.setter
    def mvc_Action39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Action__mvc_Action39", None)
        self.__mvc_Action39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_Event40"):
                    opp_val = getattr(item, "mvc_Event40", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Event40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Event40"):
                    opp_val = getattr(item, "mvc_Event40", None)
                    
                    setattr(item, "mvc_Event40", self)
                    

    @property
    def mvc_Action33(self):
        return self.__mvc_Action33

    @mvc_Action33.setter
    def mvc_Action33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Action__mvc_Action33", None)
        self.__mvc_Action33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Event34"):
                opp_val = getattr(old_value, "mvc_Event34", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Event34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Event34"):
                opp_val = getattr(value, "mvc_Event34", None)
                setattr(value, "mvc_Event34", self)

    @property
    def mvc_Action36(self):
        return self.__mvc_Action36

    @mvc_Action36.setter
    def mvc_Action36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Action__mvc_Action36", None)
        self.__mvc_Action36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_Event37"):
                opp_val = getattr(old_value, "mvc_Event37", None)
                if opp_val == self:
                    setattr(old_value, "mvc_Event37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_Event37"):
                opp_val = getattr(value, "mvc_Event37", None)
                setattr(value, "mvc_Event37", self)

class mvc_MVCModel(Annotable):

    def __init__(self, name: str, version: str, mvc_MVCModel: set["mvc_Model"] = None, mvc_MVCModel18: set["mvc_View"] = None, mvc_MVCModel21: set["mvc_Event"] = None, mvc_MVCModel23: set["mvc_Controller"] = None, mvc_MVCModel25: set["mvc_Component"] = None):
        self.name = name
        self.version = version
        self.mvc_MVCModel = mvc_MVCModel if mvc_MVCModel is not None else set()
        self.mvc_MVCModel18 = mvc_MVCModel18 if mvc_MVCModel18 is not None else set()
        self.mvc_MVCModel21 = mvc_MVCModel21 if mvc_MVCModel21 is not None else set()
        self.mvc_MVCModel23 = mvc_MVCModel23 if mvc_MVCModel23 is not None else set()
        self.mvc_MVCModel25 = mvc_MVCModel25 if mvc_MVCModel25 is not None else set()
        
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
                if hasattr(item, "mvc_Model16"):
                    opp_val = getattr(item, "mvc_Model16", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_Model16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_Model16"):
                    opp_val = getattr(item, "mvc_Model16", None)
                    
                    setattr(item, "mvc_Model16", self)
                    

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
                    

    @property
    def mvc_MVCModel18(self):
        return self.__mvc_MVCModel18

    @mvc_MVCModel18.setter
    def mvc_MVCModel18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MVCModel__mvc_MVCModel18", None)
        self.__mvc_MVCModel18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mvc_View19"):
                    opp_val = getattr(item, "mvc_View19", None)
                    
                    if opp_val == self:
                        setattr(item, "mvc_View19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mvc_View19"):
                    opp_val = getattr(item, "mvc_View19", None)
                    
                    setattr(item, "mvc_View19", self)
                    

    @property
    def mvc_MVCModel25(self):
        return self.__mvc_MVCModel25

    @mvc_MVCModel25.setter
    def mvc_MVCModel25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MVCModel__mvc_MVCModel25", None)
        self.__mvc_MVCModel25 = value if value is not None else set()
        
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
    def mvc_MVCModel21(self):
        return self.__mvc_MVCModel21

    @mvc_MVCModel21.setter
    def mvc_MVCModel21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_MVCModel__mvc_MVCModel21", None)
        self.__mvc_MVCModel21 = value if value is not None else set()
        
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
                    

class mvc_UIComponent(Annotable):

    def __init__(self, name: str, type: str, mvc_UIComponent: "mvc_UILayout" = None):
        self.name = name
        self.type = type
        self.mvc_UIComponent = mvc_UIComponent
        
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
    def mvc_UIComponent(self):
        return self.__mvc_UIComponent

    @mvc_UIComponent.setter
    def mvc_UIComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_UIComponent__mvc_UIComponent", None)
        self.__mvc_UIComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_UILayout57"):
                opp_val = getattr(old_value, "mvc_UILayout57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_UILayout57"):
                opp_val = getattr(value, "mvc_UILayout57", None)
                if opp_val is None:
                    setattr(value, "mvc_UILayout57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mvc_Model(Annotable):

    def __init__(self, name: str, mvc_Model: "mvc_Entity" = None, mvc_Model2: set["mvc_Association"] = None, mvc_Model16: "mvc_MVCModel" = None, mvc_Model46: "mvc_ControllerView" = None):
        self.name = name
        self.mvc_Model = mvc_Model
        self.mvc_Model2 = mvc_Model2 if mvc_Model2 is not None else set()
        self.mvc_Model16 = mvc_Model16
        self.mvc_Model46 = mvc_Model46
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mvc_Model46(self):
        return self.__mvc_Model46

    @mvc_Model46.setter
    def mvc_Model46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Model__mvc_Model46", None)
        self.__mvc_Model46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_ControllerView45"):
                opp_val = getattr(old_value, "mvc_ControllerView45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_ControllerView45"):
                opp_val = getattr(value, "mvc_ControllerView45", None)
                if opp_val is None:
                    setattr(value, "mvc_ControllerView45", set([self]))
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
    def mvc_Model16(self):
        return self.__mvc_Model16

    @mvc_Model16.setter
    def mvc_Model16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Model__mvc_Model16", None)
        self.__mvc_Model16 = value
        
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

class mvc_Attribute(Annotable):

    def __init__(self, name: str, type: str, mvc_Attribute: "mvc_Entity" = None, mvc_Attribute62: "mvc_UIInput" = None):
        self.name = name
        self.type = type
        self.mvc_Attribute = mvc_Attribute
        self.mvc_Attribute62 = mvc_Attribute62
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mvc_Attribute62(self):
        return self.__mvc_Attribute62

    @mvc_Attribute62.setter
    def mvc_Attribute62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mvc_Attribute__mvc_Attribute62", None)
        self.__mvc_Attribute62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mvc_UIInput"):
                opp_val = getattr(old_value, "mvc_UIInput", None)
                if opp_val == self:
                    setattr(old_value, "mvc_UIInput", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mvc_UIInput"):
                opp_val = getattr(value, "mvc_UIInput", None)
                setattr(value, "mvc_UIInput", self)

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

class mvc_Association(Annotable):

    def __init__(self, name: str, containment: bool, lowerBound: int, upperBound: int, type: str, mvc_Association: "mvc_Model" = None, mvc_Association9: "mvc_Entity" = None, mvc_Association12: "mvc_Entity" = None):
        self.name = name
        self.containment = containment
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.type = type
        self.mvc_Association = mvc_Association
        self.mvc_Association9 = mvc_Association9
        self.mvc_Association12 = mvc_Association12
        
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
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class mvc_Entity(Annotable):

    def __init__(self, name: str, mvc_Entity: "mvc_Model" = None, mvc_Entity4: set["mvc_Attribute"] = None, mvc_Entity7: "mvc_Entity" = None, mvc_Entity5: set["mvc_Entity"] = None, mvc_Entity10: "mvc_Association" = None, mvc_Entity13: "mvc_Association" = None):
        self.name = name
        self.mvc_Entity = mvc_Entity
        self.mvc_Entity4 = mvc_Entity4 if mvc_Entity4 is not None else set()
        self.mvc_Entity7 = mvc_Entity7
        self.mvc_Entity5 = mvc_Entity5 if mvc_Entity5 is not None else set()
        self.mvc_Entity10 = mvc_Entity10
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
