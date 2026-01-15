from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dtmc_NamedEntity(ABC):

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
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

class NamedEntity:

    pass
class dtmc_Module(NamedEntity):

    def __init__(self, isAutonomous: bool, Module: "dtmc_Node" = None, Module9: "dtmc_Transition" = None, module: set["dtmc_Node"] = None, dtmc_Module: "dtmc_Dtmc" = None, module18: set["dtmc_Transition"] = None):
        self.isAutonomous = isAutonomous
        self.Module = Module
        self.Module9 = Module9
        self.module = module if module is not None else set()
        self.dtmc_Module = dtmc_Module
        self.module18 = module18 if module18 is not None else set()
        
    @property
    def isAutonomous(self) -> bool:
        return self.__isAutonomous

    @isAutonomous.setter
    def isAutonomous(self, isAutonomous: bool):
        self.__isAutonomous = isAutonomous

    @property
    def Module9(self):
        return self.__Module9

    @Module9.setter
    def Module9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Module__Module9", None)
        self.__Module9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transitions"):
                opp_val = getattr(old_value, "transitions", None)
                if opp_val == self:
                    setattr(old_value, "transitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transitions"):
                opp_val = getattr(value, "transitions", None)
                setattr(value, "transitions", self)

    @property
    def module18(self):
        return self.__module18

    @module18.setter
    def module18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Module__module18", None)
        self.__module18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition19"):
                    opp_val = getattr(item, "Transition19", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition19"):
                    opp_val = getattr(item, "Transition19", None)
                    
                    setattr(item, "Transition19", self)
                    

    @property
    def Module(self):
        return self.__Module

    @Module.setter
    def Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Module__Module", None)
        self.__Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nodes"):
                opp_val = getattr(old_value, "nodes", None)
                if opp_val == self:
                    setattr(old_value, "nodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nodes"):
                opp_val = getattr(value, "nodes", None)
                setattr(value, "nodes", self)

    @property
    def module(self):
        return self.__module

    @module.setter
    def module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Module__module", None)
        self.__module = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node16"):
                    opp_val = getattr(item, "Node16", None)
                    
                    if opp_val == self:
                        setattr(item, "Node16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node16"):
                    opp_val = getattr(item, "Node16", None)
                    
                    setattr(item, "Node16", self)
                    

    @property
    def dtmc_Module(self):
        return self.__dtmc_Module

    @dtmc_Module.setter
    def dtmc_Module(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Module__dtmc_Module", None)
        self.__dtmc_Module = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dtmc_Dtmc"):
                opp_val = getattr(old_value, "dtmc_Dtmc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dtmc_Dtmc"):
                opp_val = getattr(value, "dtmc_Dtmc", None)
                if opp_val is None:
                    setattr(value, "dtmc_Dtmc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dtmc_Dtmc(NamedEntity):

    pass
class Transition:

    pass
class dtmc_StandardTransition(Transition):

    pass
class dtmc_InvokedTransition(Transition):

    pass
class dtmc_CallTransition(Transition):

    pass
class dtmc_SynchronizedTransition(Transition):

    pass
class dtmc_Transition(NamedEntity):

    def __init__(self, probability: str, Transition: "dtmc_Node" = None, Transition4: "dtmc_Node" = None, outTransitions: "dtmc_Node" = None, inTransitions: "dtmc_Node" = None, transitions: "dtmc_Module" = None, Transition19: "dtmc_Module" = None):
        self.probability = probability
        self.Transition = Transition
        self.Transition4 = Transition4
        self.outTransitions = outTransitions
        self.inTransitions = inTransitions
        self.transitions = transitions
        self.Transition19 = Transition19
        
    @property
    def probability(self) -> str:
        return self.__probability

    @probability.setter
    def probability(self, probability: str):
        self.__probability = probability

    @property
    def inTransitions(self):
        return self.__inTransitions

    @inTransitions.setter
    def inTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Transition__inTransitions", None)
        self.__inTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node7"):
                opp_val = getattr(old_value, "Node7", None)
                if opp_val == self:
                    setattr(old_value, "Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node7"):
                opp_val = getattr(value, "Node7", None)
                setattr(value, "Node7", self)

    @property
    def outTransitions(self):
        return self.__outTransitions

    @outTransitions.setter
    def outTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Transition__outTransitions", None)
        self.__outTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module9"):
                opp_val = getattr(old_value, "Module9", None)
                if opp_val == self:
                    setattr(old_value, "Module9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module9"):
                opp_val = getattr(value, "Module9", None)
                setattr(value, "Module9", self)

    @property
    def Transition19(self):
        return self.__Transition19

    @Transition19.setter
    def Transition19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Transition__Transition19", None)
        self.__Transition19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "module18"):
                opp_val = getattr(old_value, "module18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "module18"):
                opp_val = getattr(value, "module18", None)
                if opp_val is None:
                    setattr(value, "module18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_from"):
                opp_val = getattr(old_value, "_from", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_from"):
                opp_val = getattr(value, "_from", None)
                if opp_val is None:
                    setattr(value, "_from", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Transition4(self):
        return self.__Transition4

    @Transition4.setter
    def Transition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Transition__Transition4", None)
        self.__Transition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_to"):
                opp_val = getattr(old_value, "_to", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_to"):
                opp_val = getattr(value, "_to", None)
                if opp_val is None:
                    setattr(value, "_to", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dtmc_Node(NamedEntity):

    def __init__(self, isStart: bool, isEnd: bool, isFail: bool, nodes: "dtmc_Module" = None, _from: set["dtmc_Transition"] = None, _to: set["dtmc_Transition"] = None, Node: "dtmc_Transition" = None, Node7: "dtmc_Transition" = None, Node16: "dtmc_Module" = None):
        self.isStart = isStart
        self.isEnd = isEnd
        self.isFail = isFail
        self.nodes = nodes
        self._from = _from if _from is not None else set()
        self._to = _to if _to is not None else set()
        self.Node = Node
        self.Node7 = Node7
        self.Node16 = Node16
        
    @property
    def isStart(self) -> bool:
        return self.__isStart

    @isStart.setter
    def isStart(self, isStart: bool):
        self.__isStart = isStart

    @property
    def isEnd(self) -> bool:
        return self.__isEnd

    @isEnd.setter
    def isEnd(self, isEnd: bool):
        self.__isEnd = isEnd

    @property
    def isFail(self) -> bool:
        return self.__isFail

    @isFail.setter
    def isFail(self, isFail: bool):
        self.__isFail = isFail

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outTransitions"):
                opp_val = getattr(old_value, "outTransitions", None)
                if opp_val == self:
                    setattr(old_value, "outTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outTransitions"):
                opp_val = getattr(value, "outTransitions", None)
                setattr(value, "outTransitions", self)

    @property
    def _from(self):
        return self.___from

    @_from.setter
    def _from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Node___from", None)
        self.___from = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition"):
                    opp_val = getattr(item, "Transition", None)
                    
                    setattr(item, "Transition", self)
                    

    @property
    def Node16(self):
        return self.__Node16

    @Node16.setter
    def Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Node__Node16", None)
        self.__Node16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "module"):
                opp_val = getattr(old_value, "module", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "module"):
                opp_val = getattr(value, "module", None)
                if opp_val is None:
                    setattr(value, "module", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Node__nodes", None)
        self.__nodes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Module"):
                opp_val = getattr(old_value, "Module", None)
                if opp_val == self:
                    setattr(old_value, "Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Module"):
                opp_val = getattr(value, "Module", None)
                setattr(value, "Module", self)

    @property
    def Node7(self):
        return self.__Node7

    @Node7.setter
    def Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Node__Node7", None)
        self.__Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inTransitions"):
                opp_val = getattr(old_value, "inTransitions", None)
                if opp_val == self:
                    setattr(old_value, "inTransitions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inTransitions"):
                opp_val = getattr(value, "inTransitions", None)
                setattr(value, "inTransitions", self)

    @property
    def _to(self):
        return self.___to

    @_to.setter
    def _to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dtmc_Node___to", None)
        self.___to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition4"):
                    opp_val = getattr(item, "Transition4", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition4"):
                    opp_val = getattr(item, "Transition4", None)
                    
                    setattr(item, "Transition4", self)
                    
