from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class WorkSequenceType(Enum):
    startToStart = "startToStart"
    finishToStart = "finishToStart"
    startToFinish = "startToFinish"
    finishToFinish = "finishToFinish"


############################################
# Definition of Classes
############################################

class simplepdl_WorkSequence:

    def __init__(self, linkType: str, linksToSuccessors: "simplepdl_WorkDefinition" = None, linksToPredecessors: "simplepdl_WorkDefinition" = None, simplepdl_WorkSequence: "simplepdl_Process" = None, WorkSequence: "simplepdl_WorkDefinition" = None, WorkSequence5: "simplepdl_WorkDefinition" = None):
        self.linkType = linkType
        self.linksToSuccessors = linksToSuccessors
        self.linksToPredecessors = linksToPredecessors
        self.simplepdl_WorkSequence = simplepdl_WorkSequence
        self.WorkSequence = WorkSequence
        self.WorkSequence5 = WorkSequence5
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def simplepdl_WorkSequence(self):
        return self.__simplepdl_WorkSequence

    @simplepdl_WorkSequence.setter
    def simplepdl_WorkSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__simplepdl_WorkSequence", None)
        self.__simplepdl_WorkSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_Process2"):
                opp_val = getattr(old_value, "simplepdl_Process2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Process2"):
                opp_val = getattr(value, "simplepdl_Process2", None)
                if opp_val is None:
                    setattr(value, "simplepdl_Process2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linksToPredecessors(self):
        return self.__linksToPredecessors

    @linksToPredecessors.setter
    def linksToPredecessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__linksToPredecessors", None)
        self.__linksToPredecessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition8"):
                opp_val = getattr(old_value, "WorkDefinition8", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition8"):
                opp_val = getattr(value, "WorkDefinition8", None)
                setattr(value, "WorkDefinition8", self)

    @property
    def WorkSequence5(self):
        return self.__WorkSequence5

    @WorkSequence5.setter
    def WorkSequence5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence5", None)
        self.__WorkSequence5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecessor"):
                opp_val = getattr(old_value, "predecessor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecessor"):
                opp_val = getattr(value, "predecessor", None)
                if opp_val is None:
                    setattr(value, "predecessor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorkSequence(self):
        return self.__WorkSequence

    @WorkSequence.setter
    def WorkSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__WorkSequence", None)
        self.__WorkSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successor"):
                opp_val = getattr(old_value, "successor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successor"):
                opp_val = getattr(value, "successor", None)
                if opp_val is None:
                    setattr(value, "successor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def linksToSuccessors(self):
        return self.__linksToSuccessors

    @linksToSuccessors.setter
    def linksToSuccessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkSequence__linksToSuccessors", None)
        self.__linksToSuccessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkDefinition"):
                opp_val = getattr(old_value, "WorkDefinition", None)
                if opp_val == self:
                    setattr(old_value, "WorkDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkDefinition"):
                opp_val = getattr(value, "WorkDefinition", None)
                setattr(value, "WorkDefinition", self)

class simplepdl_WorkDefinition:

    def __init__(self, name: str, predecessor: set["simplepdl_WorkSequence"] = None, WorkDefinition: "simplepdl_WorkSequence" = None, WorkDefinition8: "simplepdl_WorkSequence" = None, simplepdl_WorkDefinition: "simplepdl_Process" = None, successor: set["simplepdl_WorkSequence"] = None):
        self.name = name
        self.predecessor = predecessor if predecessor is not None else set()
        self.WorkDefinition = WorkDefinition
        self.WorkDefinition8 = WorkDefinition8
        self.simplepdl_WorkDefinition = simplepdl_WorkDefinition
        self.successor = successor if successor is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__successor", None)
        self.__successor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence"):
                    opp_val = getattr(item, "WorkSequence", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence"):
                    opp_val = getattr(item, "WorkSequence", None)
                    
                    setattr(item, "WorkSequence", self)
                    

    @property
    def WorkDefinition(self):
        return self.__WorkDefinition

    @WorkDefinition.setter
    def WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition", None)
        self.__WorkDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linksToSuccessors"):
                opp_val = getattr(old_value, "linksToSuccessors", None)
                if opp_val == self:
                    setattr(old_value, "linksToSuccessors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linksToSuccessors"):
                opp_val = getattr(value, "linksToSuccessors", None)
                setattr(value, "linksToSuccessors", self)

    @property
    def WorkDefinition8(self):
        return self.__WorkDefinition8

    @WorkDefinition8.setter
    def WorkDefinition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__WorkDefinition8", None)
        self.__WorkDefinition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linksToPredecessors"):
                opp_val = getattr(old_value, "linksToPredecessors", None)
                if opp_val == self:
                    setattr(old_value, "linksToPredecessors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linksToPredecessors"):
                opp_val = getattr(value, "linksToPredecessors", None)
                setattr(value, "linksToPredecessors", self)

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence5"):
                    opp_val = getattr(item, "WorkSequence5", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence5"):
                    opp_val = getattr(item, "WorkSequence5", None)
                    
                    setattr(item, "WorkSequence5", self)
                    

    @property
    def simplepdl_WorkDefinition(self):
        return self.__simplepdl_WorkDefinition

    @simplepdl_WorkDefinition.setter
    def simplepdl_WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_WorkDefinition__simplepdl_WorkDefinition", None)
        self.__simplepdl_WorkDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplepdl_Process"):
                opp_val = getattr(old_value, "simplepdl_Process", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplepdl_Process"):
                opp_val = getattr(value, "simplepdl_Process", None)
                if opp_val is None:
                    setattr(value, "simplepdl_Process", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class simplepdl_Process:

    def __init__(self, name: str, simplepdl_Process: set["simplepdl_WorkDefinition"] = None, simplepdl_Process2: set["simplepdl_WorkSequence"] = None):
        self.name = name
        self.simplepdl_Process = simplepdl_Process if simplepdl_Process is not None else set()
        self.simplepdl_Process2 = simplepdl_Process2 if simplepdl_Process2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplepdl_Process2(self):
        return self.__simplepdl_Process2

    @simplepdl_Process2.setter
    def simplepdl_Process2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Process__simplepdl_Process2", None)
        self.__simplepdl_Process2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplepdl_WorkSequence"):
                    opp_val = getattr(item, "simplepdl_WorkSequence", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_WorkSequence", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_WorkSequence"):
                    opp_val = getattr(item, "simplepdl_WorkSequence", None)
                    
                    setattr(item, "simplepdl_WorkSequence", self)
                    

    @property
    def simplepdl_Process(self):
        return self.__simplepdl_Process

    @simplepdl_Process.setter
    def simplepdl_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplepdl_Process__simplepdl_Process", None)
        self.__simplepdl_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplepdl_WorkDefinition"):
                    opp_val = getattr(item, "simplepdl_WorkDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "simplepdl_WorkDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplepdl_WorkDefinition"):
                    opp_val = getattr(item, "simplepdl_WorkDefinition", None)
                    
                    setattr(item, "simplepdl_WorkDefinition", self)
                    
