from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Split:

    pass
class apromore_ANDSplit(Split):

    pass
class apromore_XORSplit(Split):

    pass
class apromore_ORSplit(Split):

    pass
class Routing:

    pass
class apromore_State(Routing):

    pass
class apromore_Join(Routing):

    pass
class apromore_Split(Routing):

    pass
class Event:

    pass
class apromore_Time(Event):

    pass
class apromore_Message(Event):

    pass
class Join:

    pass
class apromore_XORJoin(Join):

    pass
class apromore_ANDJoin(Join):

    pass
class apromore_ORJoin(Join):

    pass
class apromore_Edge:

    def __init__(self, ident: int, condition: str, default: bool, apromore_Edge12: "apromore_Node" = None, apromore_Edge: "apromore_Net" = None, apromore_Edge9: "apromore_Node" = None):
        self.ident = ident
        self.condition = condition
        self.default = default
        self.apromore_Edge12 = apromore_Edge12
        self.apromore_Edge = apromore_Edge
        self.apromore_Edge9 = apromore_Edge9
        
    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def ident(self) -> int:
        return self.__ident

    @ident.setter
    def ident(self, ident: int):
        self.__ident = ident

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def apromore_Edge(self):
        return self.__apromore_Edge

    @apromore_Edge.setter
    def apromore_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Edge__apromore_Edge", None)
        self.__apromore_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apromore_Net7"):
                opp_val = getattr(old_value, "apromore_Net7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apromore_Net7"):
                opp_val = getattr(value, "apromore_Net7", None)
                if opp_val is None:
                    setattr(value, "apromore_Net7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def apromore_Edge9(self):
        return self.__apromore_Edge9

    @apromore_Edge9.setter
    def apromore_Edge9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Edge__apromore_Edge9", None)
        self.__apromore_Edge9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apromore_Node10"):
                opp_val = getattr(old_value, "apromore_Node10", None)
                if opp_val == self:
                    setattr(old_value, "apromore_Node10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apromore_Node10"):
                opp_val = getattr(value, "apromore_Node10", None)
                setattr(value, "apromore_Node10", self)

    @property
    def apromore_Edge12(self):
        return self.__apromore_Edge12

    @apromore_Edge12.setter
    def apromore_Edge12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Edge__apromore_Edge12", None)
        self.__apromore_Edge12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apromore_Node13"):
                opp_val = getattr(old_value, "apromore_Node13", None)
                if opp_val == self:
                    setattr(old_value, "apromore_Node13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apromore_Node13"):
                opp_val = getattr(value, "apromore_Node13", None)
                setattr(value, "apromore_Node13", self)

class apromore_Node(ABC):

    def __init__(self, ident: int, name: str, configurable: bool, apromore_Node13: "apromore_Edge" = None, apromore_Node: "apromore_Net" = None, apromore_Node10: "apromore_Edge" = None):
        self.ident = ident
        self.name = name
        self.configurable = configurable
        self.apromore_Node13 = apromore_Node13
        self.apromore_Node = apromore_Node
        self.apromore_Node10 = apromore_Node10
        
    @property
    def configurable(self) -> bool:
        return self.__configurable

    @configurable.setter
    def configurable(self, configurable: bool):
        self.__configurable = configurable

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ident(self) -> int:
        return self.__ident

    @ident.setter
    def ident(self, ident: int):
        self.__ident = ident

    @property
    def apromore_Node13(self):
        return self.__apromore_Node13

    @apromore_Node13.setter
    def apromore_Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Node__apromore_Node13", None)
        self.__apromore_Node13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apromore_Edge12"):
                opp_val = getattr(old_value, "apromore_Edge12", None)
                if opp_val == self:
                    setattr(old_value, "apromore_Edge12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apromore_Edge12"):
                opp_val = getattr(value, "apromore_Edge12", None)
                setattr(value, "apromore_Edge12", self)

    @property
    def apromore_Node(self):
        return self.__apromore_Node

    @apromore_Node.setter
    def apromore_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Node__apromore_Node", None)
        self.__apromore_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apromore_Net5"):
                opp_val = getattr(old_value, "apromore_Net5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apromore_Net5"):
                opp_val = getattr(value, "apromore_Net5", None)
                if opp_val is None:
                    setattr(value, "apromore_Net5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def apromore_Node10(self):
        return self.__apromore_Node10

    @apromore_Node10.setter
    def apromore_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Node__apromore_Node10", None)
        self.__apromore_Node10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apromore_Edge9"):
                opp_val = getattr(old_value, "apromore_Edge9", None)
                if opp_val == self:
                    setattr(old_value, "apromore_Edge9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apromore_Edge9"):
                opp_val = getattr(value, "apromore_Edge9", None)
                setattr(value, "apromore_Edge9", self)

class Work:

    pass
class apromore_Task(Work):

    pass
class apromore_Event(Work):

    pass
class Node:

    pass
class apromore_Routing(Node):

    pass
class apromore_Work(Node):

    pass
class apromore_CanonicalProcess:

    def __init__(self, uri: str, version: str, author: str, apromore_CanonicalProcess: set["apromore_Net"] = None, apromore_CanonicalProcess2: "apromore_Net" = None):
        self.uri = uri
        self.version = version
        self.author = author
        self.apromore_CanonicalProcess = apromore_CanonicalProcess if apromore_CanonicalProcess is not None else set()
        self.apromore_CanonicalProcess2 = apromore_CanonicalProcess2
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def apromore_CanonicalProcess(self):
        return self.__apromore_CanonicalProcess

    @apromore_CanonicalProcess.setter
    def apromore_CanonicalProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_CanonicalProcess__apromore_CanonicalProcess", None)
        self.__apromore_CanonicalProcess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "apromore_Net"):
                    opp_val = getattr(item, "apromore_Net", None)
                    
                    if opp_val == self:
                        setattr(item, "apromore_Net", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "apromore_Net"):
                    opp_val = getattr(item, "apromore_Net", None)
                    
                    setattr(item, "apromore_Net", self)
                    

    @property
    def apromore_CanonicalProcess2(self):
        return self.__apromore_CanonicalProcess2

    @apromore_CanonicalProcess2.setter
    def apromore_CanonicalProcess2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_CanonicalProcess__apromore_CanonicalProcess2", None)
        self.__apromore_CanonicalProcess2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apromore_Net3"):
                opp_val = getattr(old_value, "apromore_Net3", None)
                if opp_val == self:
                    setattr(old_value, "apromore_Net3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apromore_Net3"):
                opp_val = getattr(value, "apromore_Net3", None)
                setattr(value, "apromore_Net3", self)

class apromore_Net:

    def __init__(self, ident: int, apromore_Net: "apromore_CanonicalProcess" = None, apromore_Net3: "apromore_CanonicalProcess" = None, apromore_Net5: set["apromore_Node"] = None, apromore_Net7: set["apromore_Edge"] = None, apromore_Net15: "apromore_Task" = None):
        self.ident = ident
        self.apromore_Net = apromore_Net
        self.apromore_Net3 = apromore_Net3
        self.apromore_Net5 = apromore_Net5 if apromore_Net5 is not None else set()
        self.apromore_Net7 = apromore_Net7 if apromore_Net7 is not None else set()
        self.apromore_Net15 = apromore_Net15
        
    @property
    def ident(self) -> int:
        return self.__ident

    @ident.setter
    def ident(self, ident: int):
        self.__ident = ident

    @property
    def apromore_Net5(self):
        return self.__apromore_Net5

    @apromore_Net5.setter
    def apromore_Net5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Net__apromore_Net5", None)
        self.__apromore_Net5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "apromore_Node"):
                    opp_val = getattr(item, "apromore_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "apromore_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "apromore_Node"):
                    opp_val = getattr(item, "apromore_Node", None)
                    
                    setattr(item, "apromore_Node", self)
                    

    @property
    def apromore_Net15(self):
        return self.__apromore_Net15

    @apromore_Net15.setter
    def apromore_Net15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Net__apromore_Net15", None)
        self.__apromore_Net15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apromore_Task"):
                opp_val = getattr(old_value, "apromore_Task", None)
                if opp_val == self:
                    setattr(old_value, "apromore_Task", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apromore_Task"):
                opp_val = getattr(value, "apromore_Task", None)
                setattr(value, "apromore_Task", self)

    @property
    def apromore_Net(self):
        return self.__apromore_Net

    @apromore_Net.setter
    def apromore_Net(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Net__apromore_Net", None)
        self.__apromore_Net = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apromore_CanonicalProcess"):
                opp_val = getattr(old_value, "apromore_CanonicalProcess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apromore_CanonicalProcess"):
                opp_val = getattr(value, "apromore_CanonicalProcess", None)
                if opp_val is None:
                    setattr(value, "apromore_CanonicalProcess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def apromore_Net7(self):
        return self.__apromore_Net7

    @apromore_Net7.setter
    def apromore_Net7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Net__apromore_Net7", None)
        self.__apromore_Net7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "apromore_Edge"):
                    opp_val = getattr(item, "apromore_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "apromore_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "apromore_Edge"):
                    opp_val = getattr(item, "apromore_Edge", None)
                    
                    setattr(item, "apromore_Edge", self)
                    

    @property
    def apromore_Net3(self):
        return self.__apromore_Net3

    @apromore_Net3.setter
    def apromore_Net3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_apromore_Net__apromore_Net3", None)
        self.__apromore_Net3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "apromore_CanonicalProcess2"):
                opp_val = getattr(old_value, "apromore_CanonicalProcess2", None)
                if opp_val == self:
                    setattr(old_value, "apromore_CanonicalProcess2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "apromore_CanonicalProcess2"):
                opp_val = getattr(value, "apromore_CanonicalProcess2", None)
                setattr(value, "apromore_CanonicalProcess2", self)
