from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Port:

    pass
class dslComponent_OutPort(Port):

    pass
class dslComponent_InPort(Port):

    pass
class dslComponent_DocumElt(ABC):

    def __init__(self, name: str, desc: str):
        self.name = name
        self.desc = desc
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def desc(self) -> str:
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc

class Vertex:

    pass
class dslComponent_InitialState(Vertex):

    pass
class dslComponent_SimpleState(Vertex):

    pass
class dslComponent_Port(ABC):

    def __init__(self, name: str, dslComponent_Port: "dslComponent_Component" = None):
        self.name = name
        self.dslComponent_Port = dslComponent_Port
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dslComponent_Port(self):
        return self.__dslComponent_Port

    @dslComponent_Port.setter
    def dslComponent_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_Port__dslComponent_Port", None)
        self.__dslComponent_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dslComponent_Component9"):
                opp_val = getattr(old_value, "dslComponent_Component9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dslComponent_Component9"):
                opp_val = getattr(value, "dslComponent_Component9", None)
                if opp_val is None:
                    setattr(value, "dslComponent_Component9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dslComponent_Component:

    def __init__(self, id: str, name: str, dslComponent_Component11: set["dslComponent_StateMachine"] = None, dslComponent_Component: "dslComponent_Subsystem" = None, dslComponent_Component9: set["dslComponent_Port"] = None):
        self.id = id
        self.name = name
        self.dslComponent_Component11 = dslComponent_Component11 if dslComponent_Component11 is not None else set()
        self.dslComponent_Component = dslComponent_Component
        self.dslComponent_Component9 = dslComponent_Component9 if dslComponent_Component9 is not None else set()
        
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
    def dslComponent_Component11(self):
        return self.__dslComponent_Component11

    @dslComponent_Component11.setter
    def dslComponent_Component11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_Component__dslComponent_Component11", None)
        self.__dslComponent_Component11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dslComponent_StateMachine"):
                    opp_val = getattr(item, "dslComponent_StateMachine", None)
                    
                    if opp_val == self:
                        setattr(item, "dslComponent_StateMachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dslComponent_StateMachine"):
                    opp_val = getattr(item, "dslComponent_StateMachine", None)
                    
                    setattr(item, "dslComponent_StateMachine", self)
                    

    @property
    def dslComponent_Component9(self):
        return self.__dslComponent_Component9

    @dslComponent_Component9.setter
    def dslComponent_Component9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_Component__dslComponent_Component9", None)
        self.__dslComponent_Component9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dslComponent_Port"):
                    opp_val = getattr(item, "dslComponent_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "dslComponent_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dslComponent_Port"):
                    opp_val = getattr(item, "dslComponent_Port", None)
                    
                    setattr(item, "dslComponent_Port", self)
                    

    @property
    def dslComponent_Component(self):
        return self.__dslComponent_Component

    @dslComponent_Component.setter
    def dslComponent_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_Component__dslComponent_Component", None)
        self.__dslComponent_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dslComponent_Subsystem4"):
                opp_val = getattr(old_value, "dslComponent_Subsystem4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dslComponent_Subsystem4"):
                opp_val = getattr(value, "dslComponent_Subsystem4", None)
                if opp_val is None:
                    setattr(value, "dslComponent_Subsystem4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dslComponent_ControlSubsystem:

    def __init__(self, name: str, dslComponent_ControlSubsystem: "dslComponent_Subsystem" = None, dslComponent_ControlSubsystem23: set["dslComponent_StateMachine"] = None):
        self.name = name
        self.dslComponent_ControlSubsystem = dslComponent_ControlSubsystem
        self.dslComponent_ControlSubsystem23 = dslComponent_ControlSubsystem23 if dslComponent_ControlSubsystem23 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dslComponent_ControlSubsystem23(self):
        return self.__dslComponent_ControlSubsystem23

    @dslComponent_ControlSubsystem23.setter
    def dslComponent_ControlSubsystem23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_ControlSubsystem__dslComponent_ControlSubsystem23", None)
        self.__dslComponent_ControlSubsystem23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dslComponent_StateMachine24"):
                    opp_val = getattr(item, "dslComponent_StateMachine24", None)
                    
                    if opp_val == self:
                        setattr(item, "dslComponent_StateMachine24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dslComponent_StateMachine24"):
                    opp_val = getattr(item, "dslComponent_StateMachine24", None)
                    
                    setattr(item, "dslComponent_StateMachine24", self)
                    

    @property
    def dslComponent_ControlSubsystem(self):
        return self.__dslComponent_ControlSubsystem

    @dslComponent_ControlSubsystem.setter
    def dslComponent_ControlSubsystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_ControlSubsystem__dslComponent_ControlSubsystem", None)
        self.__dslComponent_ControlSubsystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dslComponent_Subsystem2"):
                opp_val = getattr(old_value, "dslComponent_Subsystem2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dslComponent_Subsystem2"):
                opp_val = getattr(value, "dslComponent_Subsystem2", None)
                if opp_val is None:
                    setattr(value, "dslComponent_Subsystem2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dslComponent_Subsystem:

    def __init__(self, name: str, description: str, dslComponent_Subsystem: "dslComponent_WTComponents" = None, dslComponent_Subsystem2: set["dslComponent_ControlSubsystem"] = None, dslComponent_Subsystem4: set["dslComponent_Component"] = None, dslComponent_Subsystem7: "dslComponent_Subsystem" = None, dslComponent_Subsystem5: set["dslComponent_Subsystem"] = None):
        self.name = name
        self.description = description
        self.dslComponent_Subsystem = dslComponent_Subsystem
        self.dslComponent_Subsystem2 = dslComponent_Subsystem2 if dslComponent_Subsystem2 is not None else set()
        self.dslComponent_Subsystem4 = dslComponent_Subsystem4 if dslComponent_Subsystem4 is not None else set()
        self.dslComponent_Subsystem7 = dslComponent_Subsystem7
        self.dslComponent_Subsystem5 = dslComponent_Subsystem5 if dslComponent_Subsystem5 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dslComponent_Subsystem7(self):
        return self.__dslComponent_Subsystem7

    @dslComponent_Subsystem7.setter
    def dslComponent_Subsystem7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_Subsystem__dslComponent_Subsystem7", None)
        self.__dslComponent_Subsystem7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dslComponent_Subsystem5"):
                opp_val = getattr(old_value, "dslComponent_Subsystem5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dslComponent_Subsystem5"):
                opp_val = getattr(value, "dslComponent_Subsystem5", None)
                if opp_val is None:
                    setattr(value, "dslComponent_Subsystem5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dslComponent_Subsystem(self):
        return self.__dslComponent_Subsystem

    @dslComponent_Subsystem.setter
    def dslComponent_Subsystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_Subsystem__dslComponent_Subsystem", None)
        self.__dslComponent_Subsystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dslComponent_WTComponents"):
                opp_val = getattr(old_value, "dslComponent_WTComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dslComponent_WTComponents"):
                opp_val = getattr(value, "dslComponent_WTComponents", None)
                if opp_val is None:
                    setattr(value, "dslComponent_WTComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dslComponent_Subsystem2(self):
        return self.__dslComponent_Subsystem2

    @dslComponent_Subsystem2.setter
    def dslComponent_Subsystem2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_Subsystem__dslComponent_Subsystem2", None)
        self.__dslComponent_Subsystem2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dslComponent_ControlSubsystem"):
                    opp_val = getattr(item, "dslComponent_ControlSubsystem", None)
                    
                    if opp_val == self:
                        setattr(item, "dslComponent_ControlSubsystem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dslComponent_ControlSubsystem"):
                    opp_val = getattr(item, "dslComponent_ControlSubsystem", None)
                    
                    setattr(item, "dslComponent_ControlSubsystem", self)
                    

    @property
    def dslComponent_Subsystem4(self):
        return self.__dslComponent_Subsystem4

    @dslComponent_Subsystem4.setter
    def dslComponent_Subsystem4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_Subsystem__dslComponent_Subsystem4", None)
        self.__dslComponent_Subsystem4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dslComponent_Component"):
                    opp_val = getattr(item, "dslComponent_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "dslComponent_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dslComponent_Component"):
                    opp_val = getattr(item, "dslComponent_Component", None)
                    
                    setattr(item, "dslComponent_Component", self)
                    

    @property
    def dslComponent_Subsystem5(self):
        return self.__dslComponent_Subsystem5

    @dslComponent_Subsystem5.setter
    def dslComponent_Subsystem5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_Subsystem__dslComponent_Subsystem5", None)
        self.__dslComponent_Subsystem5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dslComponent_Subsystem7"):
                    opp_val = getattr(item, "dslComponent_Subsystem7", None)
                    
                    if opp_val == self:
                        setattr(item, "dslComponent_Subsystem7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dslComponent_Subsystem7"):
                    opp_val = getattr(item, "dslComponent_Subsystem7", None)
                    
                    setattr(item, "dslComponent_Subsystem7", self)
                    

class dslComponent_WTComponents:

    def __init__(self, id: str, author: str, dslComponent_WTComponents: set["dslComponent_Subsystem"] = None):
        self.id = id
        self.author = author
        self.dslComponent_WTComponents = dslComponent_WTComponents if dslComponent_WTComponents is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def dslComponent_WTComponents(self):
        return self.__dslComponent_WTComponents

    @dslComponent_WTComponents.setter
    def dslComponent_WTComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_WTComponents__dslComponent_WTComponents", None)
        self.__dslComponent_WTComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dslComponent_Subsystem"):
                    opp_val = getattr(item, "dslComponent_Subsystem", None)
                    
                    if opp_val == self:
                        setattr(item, "dslComponent_Subsystem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dslComponent_Subsystem"):
                    opp_val = getattr(item, "dslComponent_Subsystem", None)
                    
                    setattr(item, "dslComponent_Subsystem", self)
                    

class DocumElt:

    pass
class dslComponent_Edge(DocumElt):

    pass
class dslComponent_Vertex(DocumElt):

    pass
class dslComponent_StateMachine:

    def __init__(self, name: str, dslComponent_StateMachine: "dslComponent_Component" = None, dslComponent_StateMachine13: set["dslComponent_Vertex"] = None, dslComponent_StateMachine15: set["dslComponent_Edge"] = None, dslComponent_StateMachine24: "dslComponent_ControlSubsystem" = None):
        self.name = name
        self.dslComponent_StateMachine = dslComponent_StateMachine
        self.dslComponent_StateMachine13 = dslComponent_StateMachine13 if dslComponent_StateMachine13 is not None else set()
        self.dslComponent_StateMachine15 = dslComponent_StateMachine15 if dslComponent_StateMachine15 is not None else set()
        self.dslComponent_StateMachine24 = dslComponent_StateMachine24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dslComponent_StateMachine13(self):
        return self.__dslComponent_StateMachine13

    @dslComponent_StateMachine13.setter
    def dslComponent_StateMachine13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_StateMachine__dslComponent_StateMachine13", None)
        self.__dslComponent_StateMachine13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dslComponent_Vertex"):
                    opp_val = getattr(item, "dslComponent_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "dslComponent_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dslComponent_Vertex"):
                    opp_val = getattr(item, "dslComponent_Vertex", None)
                    
                    setattr(item, "dslComponent_Vertex", self)
                    

    @property
    def dslComponent_StateMachine15(self):
        return self.__dslComponent_StateMachine15

    @dslComponent_StateMachine15.setter
    def dslComponent_StateMachine15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_StateMachine__dslComponent_StateMachine15", None)
        self.__dslComponent_StateMachine15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dslComponent_Edge"):
                    opp_val = getattr(item, "dslComponent_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "dslComponent_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dslComponent_Edge"):
                    opp_val = getattr(item, "dslComponent_Edge", None)
                    
                    setattr(item, "dslComponent_Edge", self)
                    

    @property
    def dslComponent_StateMachine24(self):
        return self.__dslComponent_StateMachine24

    @dslComponent_StateMachine24.setter
    def dslComponent_StateMachine24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_StateMachine__dslComponent_StateMachine24", None)
        self.__dslComponent_StateMachine24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dslComponent_ControlSubsystem23"):
                opp_val = getattr(old_value, "dslComponent_ControlSubsystem23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dslComponent_ControlSubsystem23"):
                opp_val = getattr(value, "dslComponent_ControlSubsystem23", None)
                if opp_val is None:
                    setattr(value, "dslComponent_ControlSubsystem23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dslComponent_StateMachine(self):
        return self.__dslComponent_StateMachine

    @dslComponent_StateMachine.setter
    def dslComponent_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dslComponent_StateMachine__dslComponent_StateMachine", None)
        self.__dslComponent_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dslComponent_Component11"):
                opp_val = getattr(old_value, "dslComponent_Component11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dslComponent_Component11"):
                opp_val = getattr(value, "dslComponent_Component11", None)
                if opp_val is None:
                    setattr(value, "dslComponent_Component11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
