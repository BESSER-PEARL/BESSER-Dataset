from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class WT_DocumentElt(ABC):

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class Port:

    pass
class WT_OutPort(Port):

    pass
class WT_InPort(Port):

    pass
class DocumentElt:

    pass
class WT_Edge(DocumentElt):

    pass
class WT_Vertex(DocumentElt):

    pass
class WT_Port(ABC):

    def __init__(self, label: str, WT_Port: "WT_Component" = None):
        self.label = label
        self.WT_Port = WT_Port
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def WT_Port(self):
        return self.__WT_Port

    @WT_Port.setter
    def WT_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Port__WT_Port", None)
        self.__WT_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WT_Component23"):
                opp_val = getattr(old_value, "WT_Component23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WT_Component23"):
                opp_val = getattr(value, "WT_Component23", None)
                if opp_val is None:
                    setattr(value, "WT_Component23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Vertex:

    pass
class WT_SimpleState(Vertex):

    pass
class WT_InitialState(Vertex):

    pass
class WT_ControlSubsystem:

    def __init__(self, name: str, WT_ControlSubsystem11: set["WT_StateMachine"] = None, WT_ControlSubsystem: "WT_Subsystem" = None):
        self.name = name
        self.WT_ControlSubsystem11 = WT_ControlSubsystem11 if WT_ControlSubsystem11 is not None else set()
        self.WT_ControlSubsystem = WT_ControlSubsystem
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WT_ControlSubsystem(self):
        return self.__WT_ControlSubsystem

    @WT_ControlSubsystem.setter
    def WT_ControlSubsystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_ControlSubsystem__WT_ControlSubsystem", None)
        self.__WT_ControlSubsystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WT_Subsystem7"):
                opp_val = getattr(old_value, "WT_Subsystem7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WT_Subsystem7"):
                opp_val = getattr(value, "WT_Subsystem7", None)
                if opp_val is None:
                    setattr(value, "WT_Subsystem7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WT_ControlSubsystem11(self):
        return self.__WT_ControlSubsystem11

    @WT_ControlSubsystem11.setter
    def WT_ControlSubsystem11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_ControlSubsystem__WT_ControlSubsystem11", None)
        self.__WT_ControlSubsystem11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WT_StateMachine"):
                    opp_val = getattr(item, "WT_StateMachine", None)
                    
                    if opp_val == self:
                        setattr(item, "WT_StateMachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WT_StateMachine"):
                    opp_val = getattr(item, "WT_StateMachine", None)
                    
                    setattr(item, "WT_StateMachine", self)
                    

class WT_Architecture:

    def __init__(self, name: str, WT_Architecture9: set["WT_Component"] = None, WT_Architecture: "WT_Subsystem" = None):
        self.name = name
        self.WT_Architecture9 = WT_Architecture9 if WT_Architecture9 is not None else set()
        self.WT_Architecture = WT_Architecture
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WT_Architecture(self):
        return self.__WT_Architecture

    @WT_Architecture.setter
    def WT_Architecture(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Architecture__WT_Architecture", None)
        self.__WT_Architecture = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WT_Subsystem5"):
                opp_val = getattr(old_value, "WT_Subsystem5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WT_Subsystem5"):
                opp_val = getattr(value, "WT_Subsystem5", None)
                if opp_val is None:
                    setattr(value, "WT_Subsystem5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WT_Architecture9(self):
        return self.__WT_Architecture9

    @WT_Architecture9.setter
    def WT_Architecture9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Architecture__WT_Architecture9", None)
        self.__WT_Architecture9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WT_Component"):
                    opp_val = getattr(item, "WT_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "WT_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WT_Component"):
                    opp_val = getattr(item, "WT_Component", None)
                    
                    setattr(item, "WT_Component", self)
                    

class WT_StateMachine:

    def __init__(self, name: str, WT_StateMachine: "WT_ControlSubsystem" = None, WT_StateMachine13: set["WT_Vertex"] = None, WT_StateMachine15: set["WT_Edge"] = None, WT_StateMachine26: "WT_Component" = None):
        self.name = name
        self.WT_StateMachine = WT_StateMachine
        self.WT_StateMachine13 = WT_StateMachine13 if WT_StateMachine13 is not None else set()
        self.WT_StateMachine15 = WT_StateMachine15 if WT_StateMachine15 is not None else set()
        self.WT_StateMachine26 = WT_StateMachine26
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WT_StateMachine26(self):
        return self.__WT_StateMachine26

    @WT_StateMachine26.setter
    def WT_StateMachine26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_StateMachine__WT_StateMachine26", None)
        self.__WT_StateMachine26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WT_Component25"):
                opp_val = getattr(old_value, "WT_Component25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WT_Component25"):
                opp_val = getattr(value, "WT_Component25", None)
                if opp_val is None:
                    setattr(value, "WT_Component25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WT_StateMachine13(self):
        return self.__WT_StateMachine13

    @WT_StateMachine13.setter
    def WT_StateMachine13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_StateMachine__WT_StateMachine13", None)
        self.__WT_StateMachine13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WT_Vertex"):
                    opp_val = getattr(item, "WT_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "WT_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WT_Vertex"):
                    opp_val = getattr(item, "WT_Vertex", None)
                    
                    setattr(item, "WT_Vertex", self)
                    

    @property
    def WT_StateMachine(self):
        return self.__WT_StateMachine

    @WT_StateMachine.setter
    def WT_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_StateMachine__WT_StateMachine", None)
        self.__WT_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WT_ControlSubsystem11"):
                opp_val = getattr(old_value, "WT_ControlSubsystem11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WT_ControlSubsystem11"):
                opp_val = getattr(value, "WT_ControlSubsystem11", None)
                if opp_val is None:
                    setattr(value, "WT_ControlSubsystem11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WT_StateMachine15(self):
        return self.__WT_StateMachine15

    @WT_StateMachine15.setter
    def WT_StateMachine15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_StateMachine__WT_StateMachine15", None)
        self.__WT_StateMachine15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WT_Edge"):
                    opp_val = getattr(item, "WT_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "WT_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WT_Edge"):
                    opp_val = getattr(item, "WT_Edge", None)
                    
                    setattr(item, "WT_Edge", self)
                    

class WT_Component:

    def __init__(self, label: str, WT_Component: "WT_Architecture" = None, WT_Component23: set["WT_Port"] = None, WT_Component25: set["WT_StateMachine"] = None):
        self.label = label
        self.WT_Component = WT_Component
        self.WT_Component23 = WT_Component23 if WT_Component23 is not None else set()
        self.WT_Component25 = WT_Component25 if WT_Component25 is not None else set()
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def WT_Component25(self):
        return self.__WT_Component25

    @WT_Component25.setter
    def WT_Component25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Component__WT_Component25", None)
        self.__WT_Component25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WT_StateMachine26"):
                    opp_val = getattr(item, "WT_StateMachine26", None)
                    
                    if opp_val == self:
                        setattr(item, "WT_StateMachine26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WT_StateMachine26"):
                    opp_val = getattr(item, "WT_StateMachine26", None)
                    
                    setattr(item, "WT_StateMachine26", self)
                    

    @property
    def WT_Component23(self):
        return self.__WT_Component23

    @WT_Component23.setter
    def WT_Component23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Component__WT_Component23", None)
        self.__WT_Component23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WT_Port"):
                    opp_val = getattr(item, "WT_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "WT_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WT_Port"):
                    opp_val = getattr(item, "WT_Port", None)
                    
                    setattr(item, "WT_Port", self)
                    

    @property
    def WT_Component(self):
        return self.__WT_Component

    @WT_Component.setter
    def WT_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Component__WT_Component", None)
        self.__WT_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WT_Architecture9"):
                opp_val = getattr(old_value, "WT_Architecture9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WT_Architecture9"):
                opp_val = getattr(value, "WT_Architecture9", None)
                if opp_val is None:
                    setattr(value, "WT_Architecture9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class WT_Subsystem:

    def __init__(self, name: str, WT_Subsystem: "WT_WTComponents" = None, WT_Subsystem3: "WT_Subsystem" = None, WT_Subsystem1: set["WT_Subsystem"] = None, WT_Subsystem5: set["WT_Architecture"] = None, WT_Subsystem7: set["WT_ControlSubsystem"] = None):
        self.name = name
        self.WT_Subsystem = WT_Subsystem
        self.WT_Subsystem3 = WT_Subsystem3
        self.WT_Subsystem1 = WT_Subsystem1 if WT_Subsystem1 is not None else set()
        self.WT_Subsystem5 = WT_Subsystem5 if WT_Subsystem5 is not None else set()
        self.WT_Subsystem7 = WT_Subsystem7 if WT_Subsystem7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WT_Subsystem1(self):
        return self.__WT_Subsystem1

    @WT_Subsystem1.setter
    def WT_Subsystem1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Subsystem__WT_Subsystem1", None)
        self.__WT_Subsystem1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WT_Subsystem3"):
                    opp_val = getattr(item, "WT_Subsystem3", None)
                    
                    if opp_val == self:
                        setattr(item, "WT_Subsystem3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WT_Subsystem3"):
                    opp_val = getattr(item, "WT_Subsystem3", None)
                    
                    setattr(item, "WT_Subsystem3", self)
                    

    @property
    def WT_Subsystem3(self):
        return self.__WT_Subsystem3

    @WT_Subsystem3.setter
    def WT_Subsystem3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Subsystem__WT_Subsystem3", None)
        self.__WT_Subsystem3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WT_Subsystem1"):
                opp_val = getattr(old_value, "WT_Subsystem1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WT_Subsystem1"):
                opp_val = getattr(value, "WT_Subsystem1", None)
                if opp_val is None:
                    setattr(value, "WT_Subsystem1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WT_Subsystem(self):
        return self.__WT_Subsystem

    @WT_Subsystem.setter
    def WT_Subsystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Subsystem__WT_Subsystem", None)
        self.__WT_Subsystem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WT_WTComponents"):
                opp_val = getattr(old_value, "WT_WTComponents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WT_WTComponents"):
                opp_val = getattr(value, "WT_WTComponents", None)
                if opp_val is None:
                    setattr(value, "WT_WTComponents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WT_Subsystem7(self):
        return self.__WT_Subsystem7

    @WT_Subsystem7.setter
    def WT_Subsystem7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Subsystem__WT_Subsystem7", None)
        self.__WT_Subsystem7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WT_ControlSubsystem"):
                    opp_val = getattr(item, "WT_ControlSubsystem", None)
                    
                    if opp_val == self:
                        setattr(item, "WT_ControlSubsystem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WT_ControlSubsystem"):
                    opp_val = getattr(item, "WT_ControlSubsystem", None)
                    
                    setattr(item, "WT_ControlSubsystem", self)
                    

    @property
    def WT_Subsystem5(self):
        return self.__WT_Subsystem5

    @WT_Subsystem5.setter
    def WT_Subsystem5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_Subsystem__WT_Subsystem5", None)
        self.__WT_Subsystem5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WT_Architecture"):
                    opp_val = getattr(item, "WT_Architecture", None)
                    
                    if opp_val == self:
                        setattr(item, "WT_Architecture", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WT_Architecture"):
                    opp_val = getattr(item, "WT_Architecture", None)
                    
                    setattr(item, "WT_Architecture", self)
                    

class WT_WTComponents:

    def __init__(self, name: str, WT_WTComponents: set["WT_Subsystem"] = None):
        self.name = name
        self.WT_WTComponents = WT_WTComponents if WT_WTComponents is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WT_WTComponents(self):
        return self.__WT_WTComponents

    @WT_WTComponents.setter
    def WT_WTComponents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WT_WTComponents__WT_WTComponents", None)
        self.__WT_WTComponents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WT_Subsystem"):
                    opp_val = getattr(item, "WT_Subsystem", None)
                    
                    if opp_val == self:
                        setattr(item, "WT_Subsystem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WT_Subsystem"):
                    opp_val = getattr(item, "WT_Subsystem", None)
                    
                    setattr(item, "WT_Subsystem", self)
                    
