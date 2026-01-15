from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FunctionDomain(Enum):
    time = "time"
    space = "space"
    form = "form"


############################################
# Definition of Classes
############################################

class myffbd_Item:

    def __init__(self, name: str, myffbd_Item: "myffbd_Flow" = None):
        self.name = name
        self.myffbd_Item = myffbd_Item
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myffbd_Item(self):
        return self.__myffbd_Item

    @myffbd_Item.setter
    def myffbd_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Item__myffbd_Item", None)
        self.__myffbd_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myffbd_Flow25"):
                opp_val = getattr(old_value, "myffbd_Flow25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myffbd_Flow25"):
                opp_val = getattr(value, "myffbd_Flow25", None)
                if opp_val is None:
                    setattr(value, "myffbd_Flow25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myffbd_Flow:

    pass
class myffbd_Port(ABC):

    def __init__(self, id: str, myffbd_Port: set["myffbd_Flow"] = None, myffbd_Port19: "myffbd_PortType" = None, myffbd_Port23: "myffbd_Flow" = None, myffbd_Port28: "myffbd_Flow" = None):
        self.id = id
        self.myffbd_Port = myffbd_Port if myffbd_Port is not None else set()
        self.myffbd_Port19 = myffbd_Port19
        self.myffbd_Port23 = myffbd_Port23
        self.myffbd_Port28 = myffbd_Port28
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def myffbd_Port19(self):
        return self.__myffbd_Port19

    @myffbd_Port19.setter
    def myffbd_Port19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Port__myffbd_Port19", None)
        self.__myffbd_Port19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myffbd_PortType20"):
                opp_val = getattr(old_value, "myffbd_PortType20", None)
                if opp_val == self:
                    setattr(old_value, "myffbd_PortType20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myffbd_PortType20"):
                opp_val = getattr(value, "myffbd_PortType20", None)
                setattr(value, "myffbd_PortType20", self)

    @property
    def myffbd_Port23(self):
        return self.__myffbd_Port23

    @myffbd_Port23.setter
    def myffbd_Port23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Port__myffbd_Port23", None)
        self.__myffbd_Port23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myffbd_Flow22"):
                opp_val = getattr(old_value, "myffbd_Flow22", None)
                if opp_val == self:
                    setattr(old_value, "myffbd_Flow22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myffbd_Flow22"):
                opp_val = getattr(value, "myffbd_Flow22", None)
                setattr(value, "myffbd_Flow22", self)

    @property
    def myffbd_Port(self):
        return self.__myffbd_Port

    @myffbd_Port.setter
    def myffbd_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Port__myffbd_Port", None)
        self.__myffbd_Port = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myffbd_Flow"):
                    opp_val = getattr(item, "myffbd_Flow", None)
                    
                    if opp_val == self:
                        setattr(item, "myffbd_Flow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myffbd_Flow"):
                    opp_val = getattr(item, "myffbd_Flow", None)
                    
                    setattr(item, "myffbd_Flow", self)
                    

    @property
    def myffbd_Port28(self):
        return self.__myffbd_Port28

    @myffbd_Port28.setter
    def myffbd_Port28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Port__myffbd_Port28", None)
        self.__myffbd_Port28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myffbd_Flow27"):
                opp_val = getattr(old_value, "myffbd_Flow27", None)
                if opp_val == self:
                    setattr(old_value, "myffbd_Flow27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myffbd_Flow27"):
                opp_val = getattr(value, "myffbd_Flow27", None)
                setattr(value, "myffbd_Flow27", self)

class Port:

    pass
class myffbd_PortType:

    def __init__(self, type: str, myffbd_PortType: "myffbd_Function" = None, myffbd_PortType20: "myffbd_Port" = None):
        self.type = type
        self.myffbd_PortType = myffbd_PortType
        self.myffbd_PortType20 = myffbd_PortType20
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def myffbd_PortType(self):
        return self.__myffbd_PortType

    @myffbd_PortType.setter
    def myffbd_PortType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_PortType__myffbd_PortType", None)
        self.__myffbd_PortType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myffbd_Function13"):
                opp_val = getattr(old_value, "myffbd_Function13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myffbd_Function13"):
                opp_val = getattr(value, "myffbd_Function13", None)
                if opp_val is None:
                    setattr(value, "myffbd_Function13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myffbd_PortType20(self):
        return self.__myffbd_PortType20

    @myffbd_PortType20.setter
    def myffbd_PortType20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_PortType__myffbd_PortType20", None)
        self.__myffbd_PortType20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myffbd_Port19"):
                opp_val = getattr(old_value, "myffbd_Port19", None)
                if opp_val == self:
                    setattr(old_value, "myffbd_Port19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myffbd_Port19"):
                opp_val = getattr(value, "myffbd_Port19", None)
                setattr(value, "myffbd_Port19", self)

class myffbd_Token:

    pass
class myffbd_Description:

    def __init__(self, content: str, myffbd_Description: "myffbd_Function" = None):
        self.content = content
        self.myffbd_Description = myffbd_Description
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def myffbd_Description(self):
        return self.__myffbd_Description

    @myffbd_Description.setter
    def myffbd_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Description__myffbd_Description", None)
        self.__myffbd_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myffbd_Function9"):
                opp_val = getattr(old_value, "myffbd_Function9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myffbd_Function9"):
                opp_val = getattr(value, "myffbd_Function9", None)
                if opp_val is None:
                    setattr(value, "myffbd_Function9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class myffbd_InputPort(Port):

    pass
class myffbd_OutputPort(Port):

    pass
class myffbd_SequenceNode(ABC):

    def __init__(self, name: str, myffbd_SequenceNode: "myffbd_Function" = None, myffbd_SequenceNode16: "myffbd_SequenceNode" = None, myffbd_SequenceNode14: set["myffbd_SequenceNode"] = None):
        self.name = name
        self.myffbd_SequenceNode = myffbd_SequenceNode
        self.myffbd_SequenceNode16 = myffbd_SequenceNode16
        self.myffbd_SequenceNode14 = myffbd_SequenceNode14 if myffbd_SequenceNode14 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myffbd_SequenceNode16(self):
        return self.__myffbd_SequenceNode16

    @myffbd_SequenceNode16.setter
    def myffbd_SequenceNode16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_SequenceNode__myffbd_SequenceNode16", None)
        self.__myffbd_SequenceNode16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myffbd_SequenceNode14"):
                opp_val = getattr(old_value, "myffbd_SequenceNode14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myffbd_SequenceNode14"):
                opp_val = getattr(value, "myffbd_SequenceNode14", None)
                if opp_val is None:
                    setattr(value, "myffbd_SequenceNode14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myffbd_SequenceNode14(self):
        return self.__myffbd_SequenceNode14

    @myffbd_SequenceNode14.setter
    def myffbd_SequenceNode14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_SequenceNode__myffbd_SequenceNode14", None)
        self.__myffbd_SequenceNode14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myffbd_SequenceNode16"):
                    opp_val = getattr(item, "myffbd_SequenceNode16", None)
                    
                    if opp_val == self:
                        setattr(item, "myffbd_SequenceNode16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myffbd_SequenceNode16"):
                    opp_val = getattr(item, "myffbd_SequenceNode16", None)
                    
                    setattr(item, "myffbd_SequenceNode16", self)
                    

    @property
    def myffbd_SequenceNode(self):
        return self.__myffbd_SequenceNode

    @myffbd_SequenceNode.setter
    def myffbd_SequenceNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_SequenceNode__myffbd_SequenceNode", None)
        self.__myffbd_SequenceNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myffbd_Function3"):
                opp_val = getattr(old_value, "myffbd_Function3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myffbd_Function3"):
                opp_val = getattr(value, "myffbd_Function3", None)
                if opp_val is None:
                    setattr(value, "myffbd_Function3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SequenceNode:

    pass
class myffbd_LoopExit(SequenceNode):

    pass
class myffbd_Start(SequenceNode):

    pass
class myffbd_Or(SequenceNode):

    pass
class myffbd_Final(SequenceNode):

    pass
class myffbd_Loop(SequenceNode):

    pass
class myffbd_Iteration(SequenceNode):

    pass
class myffbd_And(SequenceNode):

    pass
class myffbd_Function(SequenceNode):

    def __init__(self, domain: str, tMin: int, tMax: int, myffbd_Function: "myffbd_Function" = None, myffbd_Function0: set["myffbd_Function"] = None, myffbd_Function3: set["myffbd_SequenceNode"] = None, myffbd_Function5: set["myffbd_OutputPort"] = None, myffbd_Function7: set["myffbd_InputPort"] = None, myffbd_Function9: set["myffbd_Description"] = None, myffbd_Function11: set["myffbd_Token"] = None, myffbd_Function13: set["myffbd_PortType"] = None):
        self.domain = domain
        self.tMin = tMin
        self.tMax = tMax
        self.myffbd_Function = myffbd_Function
        self.myffbd_Function0 = myffbd_Function0 if myffbd_Function0 is not None else set()
        self.myffbd_Function3 = myffbd_Function3 if myffbd_Function3 is not None else set()
        self.myffbd_Function5 = myffbd_Function5 if myffbd_Function5 is not None else set()
        self.myffbd_Function7 = myffbd_Function7 if myffbd_Function7 is not None else set()
        self.myffbd_Function9 = myffbd_Function9 if myffbd_Function9 is not None else set()
        self.myffbd_Function11 = myffbd_Function11 if myffbd_Function11 is not None else set()
        self.myffbd_Function13 = myffbd_Function13 if myffbd_Function13 is not None else set()
        
    @property
    def tMax(self) -> int:
        return self.__tMax

    @tMax.setter
    def tMax(self, tMax: int):
        self.__tMax = tMax

    @property
    def tMin(self) -> int:
        return self.__tMin

    @tMin.setter
    def tMin(self, tMin: int):
        self.__tMin = tMin

    @property
    def domain(self) -> str:
        return self.__domain

    @domain.setter
    def domain(self, domain: str):
        self.__domain = domain

    @property
    def myffbd_Function13(self):
        return self.__myffbd_Function13

    @myffbd_Function13.setter
    def myffbd_Function13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Function__myffbd_Function13", None)
        self.__myffbd_Function13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myffbd_PortType"):
                    opp_val = getattr(item, "myffbd_PortType", None)
                    
                    if opp_val == self:
                        setattr(item, "myffbd_PortType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myffbd_PortType"):
                    opp_val = getattr(item, "myffbd_PortType", None)
                    
                    setattr(item, "myffbd_PortType", self)
                    

    @property
    def myffbd_Function11(self):
        return self.__myffbd_Function11

    @myffbd_Function11.setter
    def myffbd_Function11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Function__myffbd_Function11", None)
        self.__myffbd_Function11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myffbd_Token"):
                    opp_val = getattr(item, "myffbd_Token", None)
                    
                    if opp_val == self:
                        setattr(item, "myffbd_Token", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myffbd_Token"):
                    opp_val = getattr(item, "myffbd_Token", None)
                    
                    setattr(item, "myffbd_Token", self)
                    

    @property
    def myffbd_Function7(self):
        return self.__myffbd_Function7

    @myffbd_Function7.setter
    def myffbd_Function7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Function__myffbd_Function7", None)
        self.__myffbd_Function7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myffbd_InputPort"):
                    opp_val = getattr(item, "myffbd_InputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "myffbd_InputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myffbd_InputPort"):
                    opp_val = getattr(item, "myffbd_InputPort", None)
                    
                    setattr(item, "myffbd_InputPort", self)
                    

    @property
    def myffbd_Function3(self):
        return self.__myffbd_Function3

    @myffbd_Function3.setter
    def myffbd_Function3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Function__myffbd_Function3", None)
        self.__myffbd_Function3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myffbd_SequenceNode"):
                    opp_val = getattr(item, "myffbd_SequenceNode", None)
                    
                    if opp_val == self:
                        setattr(item, "myffbd_SequenceNode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myffbd_SequenceNode"):
                    opp_val = getattr(item, "myffbd_SequenceNode", None)
                    
                    setattr(item, "myffbd_SequenceNode", self)
                    

    @property
    def myffbd_Function9(self):
        return self.__myffbd_Function9

    @myffbd_Function9.setter
    def myffbd_Function9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Function__myffbd_Function9", None)
        self.__myffbd_Function9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myffbd_Description"):
                    opp_val = getattr(item, "myffbd_Description", None)
                    
                    if opp_val == self:
                        setattr(item, "myffbd_Description", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myffbd_Description"):
                    opp_val = getattr(item, "myffbd_Description", None)
                    
                    setattr(item, "myffbd_Description", self)
                    

    @property
    def myffbd_Function5(self):
        return self.__myffbd_Function5

    @myffbd_Function5.setter
    def myffbd_Function5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Function__myffbd_Function5", None)
        self.__myffbd_Function5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myffbd_OutputPort"):
                    opp_val = getattr(item, "myffbd_OutputPort", None)
                    
                    if opp_val == self:
                        setattr(item, "myffbd_OutputPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myffbd_OutputPort"):
                    opp_val = getattr(item, "myffbd_OutputPort", None)
                    
                    setattr(item, "myffbd_OutputPort", self)
                    

    @property
    def myffbd_Function(self):
        return self.__myffbd_Function

    @myffbd_Function.setter
    def myffbd_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Function__myffbd_Function", None)
        self.__myffbd_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myffbd_Function0"):
                opp_val = getattr(old_value, "myffbd_Function0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myffbd_Function0"):
                opp_val = getattr(value, "myffbd_Function0", None)
                if opp_val is None:
                    setattr(value, "myffbd_Function0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myffbd_Function0(self):
        return self.__myffbd_Function0

    @myffbd_Function0.setter
    def myffbd_Function0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myffbd_Function__myffbd_Function0", None)
        self.__myffbd_Function0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myffbd_Function"):
                    opp_val = getattr(item, "myffbd_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "myffbd_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myffbd_Function"):
                    opp_val = getattr(item, "myffbd_Function", None)
                    
                    setattr(item, "myffbd_Function", self)
                    
