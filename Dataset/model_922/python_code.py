from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class WorkSequenceKind(Enum):
    finishToFinish = "finishToFinish"
    finishToStart = "finishToStart"
    startToStart = "startToStart"
    startToFinish = "startToFinish"


############################################
# Definition of Classes
############################################

class spem_WorkSequence:

    def __init__(self, kind: str, WorkSequence4: "spem_Activity" = None, WorkSequence6: "spem_Activity" = None, linkToPredecessor: "spem_Activity" = None, WorkSequence: "spem_Process" = None, linkToSuccessor: "spem_Activity" = None, workSquences: "spem_Process" = None):
        self.kind = kind
        self.WorkSequence4 = WorkSequence4
        self.WorkSequence6 = WorkSequence6
        self.linkToPredecessor = linkToPredecessor
        self.WorkSequence = WorkSequence
        self.linkToSuccessor = linkToSuccessor
        self.workSquences = workSquences
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def WorkSequence4(self):
        return self.__WorkSequence4

    @WorkSequence4.setter
    def WorkSequence4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__WorkSequence4", None)
        self.__WorkSequence4 = value
        
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
        old_value = getattr(self, f"_spem_WorkSequence__WorkSequence", None)
        self.__WorkSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process2"):
                opp_val = getattr(old_value, "process2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process2"):
                opp_val = getattr(value, "process2", None)
                if opp_val is None:
                    setattr(value, "process2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workSquences(self):
        return self.__workSquences

    @workSquences.setter
    def workSquences(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__workSquences", None)
        self.__workSquences = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Process13"):
                opp_val = getattr(old_value, "Process13", None)
                if opp_val == self:
                    setattr(old_value, "Process13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Process13"):
                opp_val = getattr(value, "Process13", None)
                setattr(value, "Process13", self)

    @property
    def linkToPredecessor(self):
        return self.__linkToPredecessor

    @linkToPredecessor.setter
    def linkToPredecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__linkToPredecessor", None)
        self.__linkToPredecessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity9"):
                opp_val = getattr(old_value, "Activity9", None)
                if opp_val == self:
                    setattr(old_value, "Activity9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity9"):
                opp_val = getattr(value, "Activity9", None)
                setattr(value, "Activity9", self)

    @property
    def WorkSequence6(self):
        return self.__WorkSequence6

    @WorkSequence6.setter
    def WorkSequence6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__WorkSequence6", None)
        self.__WorkSequence6 = value
        
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
    def linkToSuccessor(self):
        return self.__linkToSuccessor

    @linkToSuccessor.setter
    def linkToSuccessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_WorkSequence__linkToSuccessor", None)
        self.__linkToSuccessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Activity11"):
                opp_val = getattr(old_value, "Activity11", None)
                if opp_val == self:
                    setattr(old_value, "Activity11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Activity11"):
                opp_val = getattr(value, "Activity11", None)
                setattr(value, "Activity11", self)

class spem_Activity:

    def __init__(self, name: str, durationmin: int, durationmax: int, predecessor: set["spem_WorkSequence"] = None, successor: set["spem_WorkSequence"] = None, activities: "spem_Process" = None, Activity9: "spem_WorkSequence" = None, Activity: "spem_Process" = None, Activity11: "spem_WorkSequence" = None):
        self.name = name
        self.durationmin = durationmin
        self.durationmax = durationmax
        self.predecessor = predecessor if predecessor is not None else set()
        self.successor = successor if successor is not None else set()
        self.activities = activities
        self.Activity9 = Activity9
        self.Activity = Activity
        self.Activity11 = Activity11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def durationmin(self) -> int:
        return self.__durationmin

    @durationmin.setter
    def durationmin(self, durationmin: int):
        self.__durationmin = durationmin

    @property
    def durationmax(self) -> int:
        return self.__durationmax

    @durationmax.setter
    def durationmax(self, durationmax: int):
        self.__durationmax = durationmax

    @property
    def activities(self):
        return self.__activities

    @activities.setter
    def activities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__activities", None)
        self.__activities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Process"):
                opp_val = getattr(old_value, "Process", None)
                if opp_val == self:
                    setattr(old_value, "Process", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Process"):
                opp_val = getattr(value, "Process", None)
                setattr(value, "Process", self)

    @property
    def Activity9(self):
        return self.__Activity9

    @Activity9.setter
    def Activity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__Activity9", None)
        self.__Activity9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linkToPredecessor"):
                opp_val = getattr(old_value, "linkToPredecessor", None)
                if opp_val == self:
                    setattr(old_value, "linkToPredecessor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linkToPredecessor"):
                opp_val = getattr(value, "linkToPredecessor", None)
                setattr(value, "linkToPredecessor", self)

    @property
    def Activity11(self):
        return self.__Activity11

    @Activity11.setter
    def Activity11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__Activity11", None)
        self.__Activity11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linkToSuccessor"):
                opp_val = getattr(old_value, "linkToSuccessor", None)
                if opp_val == self:
                    setattr(old_value, "linkToSuccessor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linkToSuccessor"):
                opp_val = getattr(value, "linkToSuccessor", None)
                setattr(value, "linkToSuccessor", self)

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process"):
                opp_val = getattr(old_value, "process", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process"):
                opp_val = getattr(value, "process", None)
                if opp_val is None:
                    setattr(value, "process", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__successor", None)
        self.__successor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence6"):
                    opp_val = getattr(item, "WorkSequence6", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence6"):
                    opp_val = getattr(item, "WorkSequence6", None)
                    
                    setattr(item, "WorkSequence6", self)
                    

    @property
    def predecessor(self):
        return self.__predecessor

    @predecessor.setter
    def predecessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_spem_Activity__predecessor", None)
        self.__predecessor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WorkSequence4"):
                    opp_val = getattr(item, "WorkSequence4", None)
                    
                    if opp_val == self:
                        setattr(item, "WorkSequence4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WorkSequence4"):
                    opp_val = getattr(item, "WorkSequence4", None)
                    
                    setattr(item, "WorkSequence4", self)
                    

class spem_Process:

    pass