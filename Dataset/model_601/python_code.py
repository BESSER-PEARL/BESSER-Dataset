from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class GraphicControl:

    pass
class Arch_TextBox(GraphicControl):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Arch_DropDownList(GraphicControl):

    def __init__(self, items: str):
        self.items = items
        
    @property
    def items(self) -> str:
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items

class Arch_Div(GraphicControl):

    pass
class Arch_Label(GraphicControl):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class Arch_Parameter:

    def __init__(self, name: str, type: str, Arch_Parameter: "Arch_Method" = None):
        self.name = name
        self.type = type
        self.Arch_Parameter = Arch_Parameter
        
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
    def Arch_Parameter(self):
        return self.__Arch_Parameter

    @Arch_Parameter.setter
    def Arch_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Parameter__Arch_Parameter", None)
        self.__Arch_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_Method34"):
                opp_val = getattr(old_value, "Arch_Method34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_Method34"):
                opp_val = getattr(value, "Arch_Method34", None)
                if opp_val is None:
                    setattr(value, "Arch_Method34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Arch_Event:

    def __init__(self, name: str, Arch_Event: "Arch_Controller" = None, Arch_Event37: "Arch_GraphicControl" = None):
        self.name = name
        self.Arch_Event = Arch_Event
        self.Arch_Event37 = Arch_Event37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arch_Event(self):
        return self.__Arch_Event

    @Arch_Event.setter
    def Arch_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Event__Arch_Event", None)
        self.__Arch_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_Controller22"):
                opp_val = getattr(old_value, "Arch_Controller22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_Controller22"):
                opp_val = getattr(value, "Arch_Controller22", None)
                if opp_val is None:
                    setattr(value, "Arch_Controller22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arch_Event37(self):
        return self.__Arch_Event37

    @Arch_Event37.setter
    def Arch_Event37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Event__Arch_Event37", None)
        self.__Arch_Event37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_GraphicControl36"):
                opp_val = getattr(old_value, "Arch_GraphicControl36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_GraphicControl36"):
                opp_val = getattr(value, "Arch_GraphicControl36", None)
                if opp_val is None:
                    setattr(value, "Arch_GraphicControl36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Arch_Attribute:

    def __init__(self, name: str, type: str, Arch_Attribute: "Arch_Entity" = None):
        self.name = name
        self.type = type
        self.Arch_Attribute = Arch_Attribute
        
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
    def Arch_Attribute(self):
        return self.__Arch_Attribute

    @Arch_Attribute.setter
    def Arch_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Attribute__Arch_Attribute", None)
        self.__Arch_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_Entity29"):
                opp_val = getattr(old_value, "Arch_Entity29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_Entity29"):
                opp_val = getattr(value, "Arch_Entity29", None)
                if opp_val is None:
                    setattr(value, "Arch_Entity29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Arch_Method:

    def __init__(self, returntype: str, name: str, Arch_Method: "Arch_Service" = None, Arch_Method27: "Arch_Logic" = None, Arch_Method34: set["Arch_Parameter"] = None, Arch_Method32: "Arch_Entity" = None):
        self.returntype = returntype
        self.name = name
        self.Arch_Method = Arch_Method
        self.Arch_Method27 = Arch_Method27
        self.Arch_Method34 = Arch_Method34 if Arch_Method34 is not None else set()
        self.Arch_Method32 = Arch_Method32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def returntype(self) -> str:
        return self.__returntype

    @returntype.setter
    def returntype(self, returntype: str):
        self.__returntype = returntype

    @property
    def Arch_Method(self):
        return self.__Arch_Method

    @Arch_Method.setter
    def Arch_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Method__Arch_Method", None)
        self.__Arch_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_Service24"):
                opp_val = getattr(old_value, "Arch_Service24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_Service24"):
                opp_val = getattr(value, "Arch_Service24", None)
                if opp_val is None:
                    setattr(value, "Arch_Service24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arch_Method34(self):
        return self.__Arch_Method34

    @Arch_Method34.setter
    def Arch_Method34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Method__Arch_Method34", None)
        self.__Arch_Method34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Parameter"):
                    opp_val = getattr(item, "Arch_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Parameter"):
                    opp_val = getattr(item, "Arch_Parameter", None)
                    
                    setattr(item, "Arch_Parameter", self)
                    

    @property
    def Arch_Method27(self):
        return self.__Arch_Method27

    @Arch_Method27.setter
    def Arch_Method27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Method__Arch_Method27", None)
        self.__Arch_Method27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_Logic26"):
                opp_val = getattr(old_value, "Arch_Logic26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_Logic26"):
                opp_val = getattr(value, "Arch_Logic26", None)
                if opp_val is None:
                    setattr(value, "Arch_Logic26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arch_Method32(self):
        return self.__Arch_Method32

    @Arch_Method32.setter
    def Arch_Method32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Method__Arch_Method32", None)
        self.__Arch_Method32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_Entity31"):
                opp_val = getattr(old_value, "Arch_Entity31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_Entity31"):
                opp_val = getattr(value, "Arch_Entity31", None)
                if opp_val is None:
                    setattr(value, "Arch_Entity31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Arch_Controller:

    def __init__(self, name: str, Arch_Controller: "Arch_FrontEnd" = None, Arch_Controller17: "Arch_View" = None, Arch_Controller19: set["Arch_View"] = None, Arch_Controller22: set["Arch_Event"] = None):
        self.name = name
        self.Arch_Controller = Arch_Controller
        self.Arch_Controller17 = Arch_Controller17
        self.Arch_Controller19 = Arch_Controller19 if Arch_Controller19 is not None else set()
        self.Arch_Controller22 = Arch_Controller22 if Arch_Controller22 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arch_Controller19(self):
        return self.__Arch_Controller19

    @Arch_Controller19.setter
    def Arch_Controller19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Controller__Arch_Controller19", None)
        self.__Arch_Controller19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_View20"):
                    opp_val = getattr(item, "Arch_View20", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_View20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_View20"):
                    opp_val = getattr(item, "Arch_View20", None)
                    
                    setattr(item, "Arch_View20", self)
                    

    @property
    def Arch_Controller17(self):
        return self.__Arch_Controller17

    @Arch_Controller17.setter
    def Arch_Controller17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Controller__Arch_Controller17", None)
        self.__Arch_Controller17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_View16"):
                opp_val = getattr(old_value, "Arch_View16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_View16"):
                opp_val = getattr(value, "Arch_View16", None)
                if opp_val is None:
                    setattr(value, "Arch_View16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arch_Controller22(self):
        return self.__Arch_Controller22

    @Arch_Controller22.setter
    def Arch_Controller22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Controller__Arch_Controller22", None)
        self.__Arch_Controller22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Event"):
                    opp_val = getattr(item, "Arch_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Event"):
                    opp_val = getattr(item, "Arch_Event", None)
                    
                    setattr(item, "Arch_Event", self)
                    

    @property
    def Arch_Controller(self):
        return self.__Arch_Controller

    @Arch_Controller.setter
    def Arch_Controller(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Controller__Arch_Controller", None)
        self.__Arch_Controller = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_FrontEnd6"):
                opp_val = getattr(old_value, "Arch_FrontEnd6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_FrontEnd6"):
                opp_val = getattr(value, "Arch_FrontEnd6", None)
                if opp_val is None:
                    setattr(value, "Arch_FrontEnd6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Arch_View:

    def __init__(self, name: str, Arch_View14: set["Arch_GraphicControl"] = None, Arch_View: "Arch_FrontEnd" = None, Arch_View16: set["Arch_Controller"] = None, Arch_View20: "Arch_Controller" = None):
        self.name = name
        self.Arch_View14 = Arch_View14 if Arch_View14 is not None else set()
        self.Arch_View = Arch_View
        self.Arch_View16 = Arch_View16 if Arch_View16 is not None else set()
        self.Arch_View20 = Arch_View20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arch_View20(self):
        return self.__Arch_View20

    @Arch_View20.setter
    def Arch_View20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_View__Arch_View20", None)
        self.__Arch_View20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_Controller19"):
                opp_val = getattr(old_value, "Arch_Controller19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_Controller19"):
                opp_val = getattr(value, "Arch_Controller19", None)
                if opp_val is None:
                    setattr(value, "Arch_Controller19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arch_View16(self):
        return self.__Arch_View16

    @Arch_View16.setter
    def Arch_View16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_View__Arch_View16", None)
        self.__Arch_View16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Controller17"):
                    opp_val = getattr(item, "Arch_Controller17", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Controller17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Controller17"):
                    opp_val = getattr(item, "Arch_Controller17", None)
                    
                    setattr(item, "Arch_Controller17", self)
                    

    @property
    def Arch_View(self):
        return self.__Arch_View

    @Arch_View.setter
    def Arch_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_View__Arch_View", None)
        self.__Arch_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_FrontEnd4"):
                opp_val = getattr(old_value, "Arch_FrontEnd4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_FrontEnd4"):
                opp_val = getattr(value, "Arch_FrontEnd4", None)
                if opp_val is None:
                    setattr(value, "Arch_FrontEnd4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arch_View14(self):
        return self.__Arch_View14

    @Arch_View14.setter
    def Arch_View14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_View__Arch_View14", None)
        self.__Arch_View14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_GraphicControl"):
                    opp_val = getattr(item, "Arch_GraphicControl", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_GraphicControl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_GraphicControl"):
                    opp_val = getattr(item, "Arch_GraphicControl", None)
                    
                    setattr(item, "Arch_GraphicControl", self)
                    

class Arch_GraphicControl(ABC):

    def __init__(self, name: str, Arch_GraphicControl: "Arch_View" = None, Arch_GraphicControl36: set["Arch_Event"] = None, Arch_GraphicControl39: "Arch_Div" = None):
        self.name = name
        self.Arch_GraphicControl = Arch_GraphicControl
        self.Arch_GraphicControl36 = Arch_GraphicControl36 if Arch_GraphicControl36 is not None else set()
        self.Arch_GraphicControl39 = Arch_GraphicControl39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arch_GraphicControl39(self):
        return self.__Arch_GraphicControl39

    @Arch_GraphicControl39.setter
    def Arch_GraphicControl39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_GraphicControl__Arch_GraphicControl39", None)
        self.__Arch_GraphicControl39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_Div"):
                opp_val = getattr(old_value, "Arch_Div", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_Div"):
                opp_val = getattr(value, "Arch_Div", None)
                if opp_val is None:
                    setattr(value, "Arch_Div", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arch_GraphicControl36(self):
        return self.__Arch_GraphicControl36

    @Arch_GraphicControl36.setter
    def Arch_GraphicControl36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_GraphicControl__Arch_GraphicControl36", None)
        self.__Arch_GraphicControl36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Event37"):
                    opp_val = getattr(item, "Arch_Event37", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Event37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Event37"):
                    opp_val = getattr(item, "Arch_Event37", None)
                    
                    setattr(item, "Arch_Event37", self)
                    

    @property
    def Arch_GraphicControl(self):
        return self.__Arch_GraphicControl

    @Arch_GraphicControl.setter
    def Arch_GraphicControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_GraphicControl__Arch_GraphicControl", None)
        self.__Arch_GraphicControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_View14"):
                opp_val = getattr(old_value, "Arch_View14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_View14"):
                opp_val = getattr(value, "Arch_View14", None)
                if opp_val is None:
                    setattr(value, "Arch_View14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Arch_Entity:

    def __init__(self, name: str, Arch_Entity: "Arch_BackEnd" = None, Arch_Entity29: set["Arch_Attribute"] = None, Arch_Entity31: set["Arch_Method"] = None):
        self.name = name
        self.Arch_Entity = Arch_Entity
        self.Arch_Entity29 = Arch_Entity29 if Arch_Entity29 is not None else set()
        self.Arch_Entity31 = Arch_Entity31 if Arch_Entity31 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arch_Entity(self):
        return self.__Arch_Entity

    @Arch_Entity.setter
    def Arch_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Entity__Arch_Entity", None)
        self.__Arch_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_BackEnd12"):
                opp_val = getattr(old_value, "Arch_BackEnd12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_BackEnd12"):
                opp_val = getattr(value, "Arch_BackEnd12", None)
                if opp_val is None:
                    setattr(value, "Arch_BackEnd12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arch_Entity31(self):
        return self.__Arch_Entity31

    @Arch_Entity31.setter
    def Arch_Entity31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Entity__Arch_Entity31", None)
        self.__Arch_Entity31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Method32"):
                    opp_val = getattr(item, "Arch_Method32", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Method32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Method32"):
                    opp_val = getattr(item, "Arch_Method32", None)
                    
                    setattr(item, "Arch_Method32", self)
                    

    @property
    def Arch_Entity29(self):
        return self.__Arch_Entity29

    @Arch_Entity29.setter
    def Arch_Entity29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Entity__Arch_Entity29", None)
        self.__Arch_Entity29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Attribute"):
                    opp_val = getattr(item, "Arch_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Attribute"):
                    opp_val = getattr(item, "Arch_Attribute", None)
                    
                    setattr(item, "Arch_Attribute", self)
                    

class Arch_Logic:

    def __init__(self, name: str, Arch_Logic: "Arch_BackEnd" = None, Arch_Logic26: set["Arch_Method"] = None):
        self.name = name
        self.Arch_Logic = Arch_Logic
        self.Arch_Logic26 = Arch_Logic26 if Arch_Logic26 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arch_Logic(self):
        return self.__Arch_Logic

    @Arch_Logic.setter
    def Arch_Logic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Logic__Arch_Logic", None)
        self.__Arch_Logic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_BackEnd10"):
                opp_val = getattr(old_value, "Arch_BackEnd10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_BackEnd10"):
                opp_val = getattr(value, "Arch_BackEnd10", None)
                if opp_val is None:
                    setattr(value, "Arch_BackEnd10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Arch_Logic26(self):
        return self.__Arch_Logic26

    @Arch_Logic26.setter
    def Arch_Logic26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Logic__Arch_Logic26", None)
        self.__Arch_Logic26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Method27"):
                    opp_val = getattr(item, "Arch_Method27", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Method27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Method27"):
                    opp_val = getattr(item, "Arch_Method27", None)
                    
                    setattr(item, "Arch_Method27", self)
                    

class Arch_Service:

    def __init__(self, name: str, Arch_Service: "Arch_BackEnd" = None, Arch_Service24: set["Arch_Method"] = None):
        self.name = name
        self.Arch_Service = Arch_Service
        self.Arch_Service24 = Arch_Service24 if Arch_Service24 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arch_Service24(self):
        return self.__Arch_Service24

    @Arch_Service24.setter
    def Arch_Service24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Service__Arch_Service24", None)
        self.__Arch_Service24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Method"):
                    opp_val = getattr(item, "Arch_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Method"):
                    opp_val = getattr(item, "Arch_Method", None)
                    
                    setattr(item, "Arch_Method", self)
                    

    @property
    def Arch_Service(self):
        return self.__Arch_Service

    @Arch_Service.setter
    def Arch_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Service__Arch_Service", None)
        self.__Arch_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_BackEnd8"):
                opp_val = getattr(old_value, "Arch_BackEnd8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_BackEnd8"):
                opp_val = getattr(value, "Arch_BackEnd8", None)
                if opp_val is None:
                    setattr(value, "Arch_BackEnd8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Arch_BackEnd:

    def __init__(self, name: str, Arch_BackEnd: "Arch_Application" = None, Arch_BackEnd8: set["Arch_Service"] = None, Arch_BackEnd10: set["Arch_Logic"] = None, Arch_BackEnd12: set["Arch_Entity"] = None):
        self.name = name
        self.Arch_BackEnd = Arch_BackEnd
        self.Arch_BackEnd8 = Arch_BackEnd8 if Arch_BackEnd8 is not None else set()
        self.Arch_BackEnd10 = Arch_BackEnd10 if Arch_BackEnd10 is not None else set()
        self.Arch_BackEnd12 = Arch_BackEnd12 if Arch_BackEnd12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arch_BackEnd10(self):
        return self.__Arch_BackEnd10

    @Arch_BackEnd10.setter
    def Arch_BackEnd10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_BackEnd__Arch_BackEnd10", None)
        self.__Arch_BackEnd10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Logic"):
                    opp_val = getattr(item, "Arch_Logic", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Logic", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Logic"):
                    opp_val = getattr(item, "Arch_Logic", None)
                    
                    setattr(item, "Arch_Logic", self)
                    

    @property
    def Arch_BackEnd(self):
        return self.__Arch_BackEnd

    @Arch_BackEnd.setter
    def Arch_BackEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_BackEnd__Arch_BackEnd", None)
        self.__Arch_BackEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_Application2"):
                opp_val = getattr(old_value, "Arch_Application2", None)
                if opp_val == self:
                    setattr(old_value, "Arch_Application2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_Application2"):
                opp_val = getattr(value, "Arch_Application2", None)
                setattr(value, "Arch_Application2", self)

    @property
    def Arch_BackEnd8(self):
        return self.__Arch_BackEnd8

    @Arch_BackEnd8.setter
    def Arch_BackEnd8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_BackEnd__Arch_BackEnd8", None)
        self.__Arch_BackEnd8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Service"):
                    opp_val = getattr(item, "Arch_Service", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Service"):
                    opp_val = getattr(item, "Arch_Service", None)
                    
                    setattr(item, "Arch_Service", self)
                    

    @property
    def Arch_BackEnd12(self):
        return self.__Arch_BackEnd12

    @Arch_BackEnd12.setter
    def Arch_BackEnd12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_BackEnd__Arch_BackEnd12", None)
        self.__Arch_BackEnd12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Entity"):
                    opp_val = getattr(item, "Arch_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Entity"):
                    opp_val = getattr(item, "Arch_Entity", None)
                    
                    setattr(item, "Arch_Entity", self)
                    

class Arch_FrontEnd:

    def __init__(self, name: str, Arch_FrontEnd: "Arch_Application" = None, Arch_FrontEnd4: set["Arch_View"] = None, Arch_FrontEnd6: set["Arch_Controller"] = None):
        self.name = name
        self.Arch_FrontEnd = Arch_FrontEnd
        self.Arch_FrontEnd4 = Arch_FrontEnd4 if Arch_FrontEnd4 is not None else set()
        self.Arch_FrontEnd6 = Arch_FrontEnd6 if Arch_FrontEnd6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arch_FrontEnd(self):
        return self.__Arch_FrontEnd

    @Arch_FrontEnd.setter
    def Arch_FrontEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_FrontEnd__Arch_FrontEnd", None)
        self.__Arch_FrontEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_Application"):
                opp_val = getattr(old_value, "Arch_Application", None)
                if opp_val == self:
                    setattr(old_value, "Arch_Application", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_Application"):
                opp_val = getattr(value, "Arch_Application", None)
                setattr(value, "Arch_Application", self)

    @property
    def Arch_FrontEnd6(self):
        return self.__Arch_FrontEnd6

    @Arch_FrontEnd6.setter
    def Arch_FrontEnd6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_FrontEnd__Arch_FrontEnd6", None)
        self.__Arch_FrontEnd6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_Controller"):
                    opp_val = getattr(item, "Arch_Controller", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_Controller", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_Controller"):
                    opp_val = getattr(item, "Arch_Controller", None)
                    
                    setattr(item, "Arch_Controller", self)
                    

    @property
    def Arch_FrontEnd4(self):
        return self.__Arch_FrontEnd4

    @Arch_FrontEnd4.setter
    def Arch_FrontEnd4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_FrontEnd__Arch_FrontEnd4", None)
        self.__Arch_FrontEnd4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Arch_View"):
                    opp_val = getattr(item, "Arch_View", None)
                    
                    if opp_val == self:
                        setattr(item, "Arch_View", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Arch_View"):
                    opp_val = getattr(item, "Arch_View", None)
                    
                    setattr(item, "Arch_View", self)
                    

class Arch_Application:

    def __init__(self, name: str, Arch_Application: "Arch_FrontEnd" = None, Arch_Application2: "Arch_BackEnd" = None):
        self.name = name
        self.Arch_Application = Arch_Application
        self.Arch_Application2 = Arch_Application2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Arch_Application2(self):
        return self.__Arch_Application2

    @Arch_Application2.setter
    def Arch_Application2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Application__Arch_Application2", None)
        self.__Arch_Application2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_BackEnd"):
                opp_val = getattr(old_value, "Arch_BackEnd", None)
                if opp_val == self:
                    setattr(old_value, "Arch_BackEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_BackEnd"):
                opp_val = getattr(value, "Arch_BackEnd", None)
                setattr(value, "Arch_BackEnd", self)

    @property
    def Arch_Application(self):
        return self.__Arch_Application

    @Arch_Application.setter
    def Arch_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Arch_Application__Arch_Application", None)
        self.__Arch_Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arch_FrontEnd"):
                opp_val = getattr(old_value, "Arch_FrontEnd", None)
                if opp_val == self:
                    setattr(old_value, "Arch_FrontEnd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arch_FrontEnd"):
                opp_val = getattr(value, "Arch_FrontEnd", None)
                setattr(value, "Arch_FrontEnd", self)
