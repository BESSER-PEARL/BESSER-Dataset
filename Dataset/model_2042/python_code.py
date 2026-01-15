from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Behaviour_TransitionFunction:

    def __init__(self, transitionFunction: str, Behaviour_TransitionFunction: "Behaviour_ConditionalTransition" = None, Behaviour_TransitionFunction21: "Behaviour_StochasticTransition" = None, Behaviour_TransitionFunction44: "Behaviour_PostTransitionConnection" = None, Behaviour_TransitionFunction47: set["Behaviour_Token"] = None):
        self.transitionFunction = transitionFunction
        self.Behaviour_TransitionFunction = Behaviour_TransitionFunction
        self.Behaviour_TransitionFunction21 = Behaviour_TransitionFunction21
        self.Behaviour_TransitionFunction44 = Behaviour_TransitionFunction44
        self.Behaviour_TransitionFunction47 = Behaviour_TransitionFunction47 if Behaviour_TransitionFunction47 is not None else set()
        
    @property
    def transitionFunction(self) -> str:
        return self.__transitionFunction

    @transitionFunction.setter
    def transitionFunction(self, transitionFunction: str):
        self.__transitionFunction = transitionFunction

    @property
    def Behaviour_TransitionFunction21(self):
        return self.__Behaviour_TransitionFunction21

    @Behaviour_TransitionFunction21.setter
    def Behaviour_TransitionFunction21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_TransitionFunction__Behaviour_TransitionFunction21", None)
        self.__Behaviour_TransitionFunction21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_StochasticTransition"):
                opp_val = getattr(old_value, "Behaviour_StochasticTransition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_StochasticTransition"):
                opp_val = getattr(value, "Behaviour_StochasticTransition", None)
                if opp_val is None:
                    setattr(value, "Behaviour_StochasticTransition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Behaviour_TransitionFunction44(self):
        return self.__Behaviour_TransitionFunction44

    @Behaviour_TransitionFunction44.setter
    def Behaviour_TransitionFunction44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_TransitionFunction__Behaviour_TransitionFunction44", None)
        self.__Behaviour_TransitionFunction44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_PostTransitionConnection45"):
                opp_val = getattr(old_value, "Behaviour_PostTransitionConnection45", None)
                if opp_val == self:
                    setattr(old_value, "Behaviour_PostTransitionConnection45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_PostTransitionConnection45"):
                opp_val = getattr(value, "Behaviour_PostTransitionConnection45", None)
                setattr(value, "Behaviour_PostTransitionConnection45", self)

    @property
    def Behaviour_TransitionFunction47(self):
        return self.__Behaviour_TransitionFunction47

    @Behaviour_TransitionFunction47.setter
    def Behaviour_TransitionFunction47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_TransitionFunction__Behaviour_TransitionFunction47", None)
        self.__Behaviour_TransitionFunction47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Behaviour_Token48"):
                    opp_val = getattr(item, "Behaviour_Token48", None)
                    
                    if opp_val == self:
                        setattr(item, "Behaviour_Token48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Behaviour_Token48"):
                    opp_val = getattr(item, "Behaviour_Token48", None)
                    
                    setattr(item, "Behaviour_Token48", self)
                    

    @property
    def Behaviour_TransitionFunction(self):
        return self.__Behaviour_TransitionFunction

    @Behaviour_TransitionFunction.setter
    def Behaviour_TransitionFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_TransitionFunction__Behaviour_TransitionFunction", None)
        self.__Behaviour_TransitionFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_ConditionalTransition"):
                opp_val = getattr(old_value, "Behaviour_ConditionalTransition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_ConditionalTransition"):
                opp_val = getattr(value, "Behaviour_ConditionalTransition", None)
                if opp_val is None:
                    setattr(value, "Behaviour_ConditionalTransition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Transition:

    pass
class Behaviour_StochasticTransition(Transition):

    pass
class Behaviour_ConditionalTransition(Transition):

    pass
class Place:

    pass
class Behaviour_QueuePlace(Place):

    pass
class Behaviour_Server(Place):

    def __init__(self, capacity: int, Behaviour_Server: "Behaviour_QueuePlace" = None, server: "Behaviour_WaitingLine" = None, Behaviour_Server24: "Behaviour_PreTransitionConnection" = None, Server: "Behaviour_WaitingLine" = None):
        self.capacity = capacity
        self.Behaviour_Server = Behaviour_Server
        self.server = server
        self.Behaviour_Server24 = Behaviour_Server24
        self.Server = Server
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def server(self):
        return self.__server

    @server.setter
    def server(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_Server__server", None)
        self.__server = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WaitingLine"):
                opp_val = getattr(old_value, "WaitingLine", None)
                if opp_val == self:
                    setattr(old_value, "WaitingLine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WaitingLine"):
                opp_val = getattr(value, "WaitingLine", None)
                setattr(value, "WaitingLine", self)

    @property
    def Server(self):
        return self.__Server

    @Server.setter
    def Server(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_Server__Server", None)
        self.__Server = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "waitingLine"):
                opp_val = getattr(old_value, "waitingLine", None)
                if opp_val == self:
                    setattr(old_value, "waitingLine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "waitingLine"):
                opp_val = getattr(value, "waitingLine", None)
                setattr(value, "waitingLine", self)

    @property
    def Behaviour_Server(self):
        return self.__Behaviour_Server

    @Behaviour_Server.setter
    def Behaviour_Server(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_Server__Behaviour_Server", None)
        self.__Behaviour_Server = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_QueuePlace"):
                opp_val = getattr(old_value, "Behaviour_QueuePlace", None)
                if opp_val == self:
                    setattr(old_value, "Behaviour_QueuePlace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_QueuePlace"):
                opp_val = getattr(value, "Behaviour_QueuePlace", None)
                setattr(value, "Behaviour_QueuePlace", self)

    @property
    def Behaviour_Server24(self):
        return self.__Behaviour_Server24

    @Behaviour_Server24.setter
    def Behaviour_Server24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_Server__Behaviour_Server24", None)
        self.__Behaviour_Server24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_PreTransitionConnection25"):
                opp_val = getattr(old_value, "Behaviour_PreTransitionConnection25", None)
                if opp_val == self:
                    setattr(old_value, "Behaviour_PreTransitionConnection25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_PreTransitionConnection25"):
                opp_val = getattr(value, "Behaviour_PreTransitionConnection25", None)
                setattr(value, "Behaviour_PreTransitionConnection25", self)

class Behaviour_StartPlace(Place):

    def __init__(self, spawnPolicy: str, Behaviour_StartPlace: set["Behaviour_PreTransitionConnection"] = None):
        self.spawnPolicy = spawnPolicy
        self.Behaviour_StartPlace = Behaviour_StartPlace if Behaviour_StartPlace is not None else set()
        
    @property
    def spawnPolicy(self) -> str:
        return self.__spawnPolicy

    @spawnPolicy.setter
    def spawnPolicy(self, spawnPolicy: str):
        self.__spawnPolicy = spawnPolicy

    @property
    def Behaviour_StartPlace(self):
        return self.__Behaviour_StartPlace

    @Behaviour_StartPlace.setter
    def Behaviour_StartPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_StartPlace__Behaviour_StartPlace", None)
        self.__Behaviour_StartPlace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Behaviour_PreTransitionConnection18"):
                    opp_val = getattr(item, "Behaviour_PreTransitionConnection18", None)
                    
                    if opp_val == self:
                        setattr(item, "Behaviour_PreTransitionConnection18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Behaviour_PreTransitionConnection18"):
                    opp_val = getattr(item, "Behaviour_PreTransitionConnection18", None)
                    
                    setattr(item, "Behaviour_PreTransitionConnection18", self)
                    

class Behaviour_WaitingLine(Place):

    def __init__(self, schedulingPolicy: str, Behaviour_WaitingLine: "Behaviour_QueuePlace" = None, WaitingLine: "Behaviour_Server" = None, waitingLine: "Behaviour_Server" = None, Behaviour_WaitingLine28: set["Behaviour_PostTransitionConnection"] = None):
        self.schedulingPolicy = schedulingPolicy
        self.Behaviour_WaitingLine = Behaviour_WaitingLine
        self.WaitingLine = WaitingLine
        self.waitingLine = waitingLine
        self.Behaviour_WaitingLine28 = Behaviour_WaitingLine28 if Behaviour_WaitingLine28 is not None else set()
        
    @property
    def schedulingPolicy(self) -> str:
        return self.__schedulingPolicy

    @schedulingPolicy.setter
    def schedulingPolicy(self, schedulingPolicy: str):
        self.__schedulingPolicy = schedulingPolicy

    @property
    def WaitingLine(self):
        return self.__WaitingLine

    @WaitingLine.setter
    def WaitingLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_WaitingLine__WaitingLine", None)
        self.__WaitingLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "server"):
                opp_val = getattr(old_value, "server", None)
                if opp_val == self:
                    setattr(old_value, "server", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "server"):
                opp_val = getattr(value, "server", None)
                setattr(value, "server", self)

    @property
    def Behaviour_WaitingLine28(self):
        return self.__Behaviour_WaitingLine28

    @Behaviour_WaitingLine28.setter
    def Behaviour_WaitingLine28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_WaitingLine__Behaviour_WaitingLine28", None)
        self.__Behaviour_WaitingLine28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Behaviour_PostTransitionConnection29"):
                    opp_val = getattr(item, "Behaviour_PostTransitionConnection29", None)
                    
                    if opp_val == self:
                        setattr(item, "Behaviour_PostTransitionConnection29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Behaviour_PostTransitionConnection29"):
                    opp_val = getattr(item, "Behaviour_PostTransitionConnection29", None)
                    
                    setattr(item, "Behaviour_PostTransitionConnection29", self)
                    

    @property
    def waitingLine(self):
        return self.__waitingLine

    @waitingLine.setter
    def waitingLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_WaitingLine__waitingLine", None)
        self.__waitingLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Server"):
                opp_val = getattr(old_value, "Server", None)
                if opp_val == self:
                    setattr(old_value, "Server", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Server"):
                opp_val = getattr(value, "Server", None)
                setattr(value, "Server", self)

    @property
    def Behaviour_WaitingLine(self):
        return self.__Behaviour_WaitingLine

    @Behaviour_WaitingLine.setter
    def Behaviour_WaitingLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_WaitingLine__Behaviour_WaitingLine", None)
        self.__Behaviour_WaitingLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_QueuePlace16"):
                opp_val = getattr(old_value, "Behaviour_QueuePlace16", None)
                if opp_val == self:
                    setattr(old_value, "Behaviour_QueuePlace16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_QueuePlace16"):
                opp_val = getattr(value, "Behaviour_QueuePlace16", None)
                setattr(value, "Behaviour_QueuePlace16", self)

class Behaviour_DefaultPlace(Place):

    pass
class Connection:

    pass
class Behaviour_PostTransitionConnection(Connection):

    pass
class Identifier:

    pass
class Behaviour_Token(Identifier):

    pass
class Behaviour_Colour(Identifier):

    def __init__(self, attribute: str, Behaviour_Colour: "Behaviour_Token" = None):
        self.attribute = attribute
        self.Behaviour_Colour = Behaviour_Colour
        
    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Behaviour_Colour(self):
        return self.__Behaviour_Colour

    @Behaviour_Colour.setter
    def Behaviour_Colour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_Colour__Behaviour_Colour", None)
        self.__Behaviour_Colour = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_Token31"):
                opp_val = getattr(old_value, "Behaviour_Token31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_Token31"):
                opp_val = getattr(value, "Behaviour_Token31", None)
                if opp_val is None:
                    setattr(value, "Behaviour_Token31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Behaviour_Transition(Identifier):

    pass
class Behaviour_Description(Identifier):

    pass
class Behaviour_Place(Identifier):

    pass
class Behaviour_Connection(Identifier):

    pass
class Behaviour_PreTransitionConnection(Connection):

    def __init__(self, requiredTokenAmount: int, Behaviour_PreTransitionConnection: "Behaviour_Transition" = None, Behaviour_PreTransitionConnection10: "Behaviour_DefaultPlace" = None, Behaviour_PreTransitionConnection18: "Behaviour_StartPlace" = None, Behaviour_PreTransitionConnection25: "Behaviour_Server" = None):
        self.requiredTokenAmount = requiredTokenAmount
        self.Behaviour_PreTransitionConnection = Behaviour_PreTransitionConnection
        self.Behaviour_PreTransitionConnection10 = Behaviour_PreTransitionConnection10
        self.Behaviour_PreTransitionConnection18 = Behaviour_PreTransitionConnection18
        self.Behaviour_PreTransitionConnection25 = Behaviour_PreTransitionConnection25
        
    @property
    def requiredTokenAmount(self) -> int:
        return self.__requiredTokenAmount

    @requiredTokenAmount.setter
    def requiredTokenAmount(self, requiredTokenAmount: int):
        self.__requiredTokenAmount = requiredTokenAmount

    @property
    def Behaviour_PreTransitionConnection18(self):
        return self.__Behaviour_PreTransitionConnection18

    @Behaviour_PreTransitionConnection18.setter
    def Behaviour_PreTransitionConnection18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_PreTransitionConnection__Behaviour_PreTransitionConnection18", None)
        self.__Behaviour_PreTransitionConnection18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_StartPlace"):
                opp_val = getattr(old_value, "Behaviour_StartPlace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_StartPlace"):
                opp_val = getattr(value, "Behaviour_StartPlace", None)
                if opp_val is None:
                    setattr(value, "Behaviour_StartPlace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Behaviour_PreTransitionConnection25(self):
        return self.__Behaviour_PreTransitionConnection25

    @Behaviour_PreTransitionConnection25.setter
    def Behaviour_PreTransitionConnection25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_PreTransitionConnection__Behaviour_PreTransitionConnection25", None)
        self.__Behaviour_PreTransitionConnection25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_Server24"):
                opp_val = getattr(old_value, "Behaviour_Server24", None)
                if opp_val == self:
                    setattr(old_value, "Behaviour_Server24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_Server24"):
                opp_val = getattr(value, "Behaviour_Server24", None)
                setattr(value, "Behaviour_Server24", self)

    @property
    def Behaviour_PreTransitionConnection(self):
        return self.__Behaviour_PreTransitionConnection

    @Behaviour_PreTransitionConnection.setter
    def Behaviour_PreTransitionConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_PreTransitionConnection__Behaviour_PreTransitionConnection", None)
        self.__Behaviour_PreTransitionConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_Transition3"):
                opp_val = getattr(old_value, "Behaviour_Transition3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_Transition3"):
                opp_val = getattr(value, "Behaviour_Transition3", None)
                if opp_val is None:
                    setattr(value, "Behaviour_Transition3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Behaviour_PreTransitionConnection10(self):
        return self.__Behaviour_PreTransitionConnection10

    @Behaviour_PreTransitionConnection10.setter
    def Behaviour_PreTransitionConnection10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Behaviour_PreTransitionConnection__Behaviour_PreTransitionConnection10", None)
        self.__Behaviour_PreTransitionConnection10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Behaviour_DefaultPlace"):
                opp_val = getattr(old_value, "Behaviour_DefaultPlace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Behaviour_DefaultPlace"):
                opp_val = getattr(value, "Behaviour_DefaultPlace", None)
                if opp_val is None:
                    setattr(value, "Behaviour_DefaultPlace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
