from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class WorkSequenceType(Enum):
    start2start = "start2start"
    finish2start = "finish2start"
    start2finish = "start2finish"
    finish2finish = "finish2finish"


############################################
# Definition of Classes
############################################

class pDL1_Process:

    def __init__(self, name: str, pDL1_Process: set["pDL1_ProcessElement"] = None):
        self.name = name
        self.pDL1_Process = pDL1_Process if pDL1_Process is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pDL1_Process(self):
        return self.__pDL1_Process

    @pDL1_Process.setter
    def pDL1_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL1_Process__pDL1_Process", None)
        self.__pDL1_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pDL1_ProcessElement"):
                    opp_val = getattr(item, "pDL1_ProcessElement", None)
                    
                    if opp_val == self:
                        setattr(item, "pDL1_ProcessElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pDL1_ProcessElement"):
                    opp_val = getattr(item, "pDL1_ProcessElement", None)
                    
                    setattr(item, "pDL1_ProcessElement", self)
                    

class ProcessElement:

    pass
class pDL1_WorkSequence(ProcessElement):

    def __init__(self, linkType: str, pDL1_WorkSequence: "pDL1_WorkDefinition" = None, pDL1_WorkSequence3: "pDL1_WorkDefinition" = None):
        self.linkType = linkType
        self.pDL1_WorkSequence = pDL1_WorkSequence
        self.pDL1_WorkSequence3 = pDL1_WorkSequence3
        
    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def pDL1_WorkSequence3(self):
        return self.__pDL1_WorkSequence3

    @pDL1_WorkSequence3.setter
    def pDL1_WorkSequence3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL1_WorkSequence__pDL1_WorkSequence3", None)
        self.__pDL1_WorkSequence3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pDL1_WorkDefinition4"):
                opp_val = getattr(old_value, "pDL1_WorkDefinition4", None)
                if opp_val == self:
                    setattr(old_value, "pDL1_WorkDefinition4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL1_WorkDefinition4"):
                opp_val = getattr(value, "pDL1_WorkDefinition4", None)
                setattr(value, "pDL1_WorkDefinition4", self)

    @property
    def pDL1_WorkSequence(self):
        return self.__pDL1_WorkSequence

    @pDL1_WorkSequence.setter
    def pDL1_WorkSequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL1_WorkSequence__pDL1_WorkSequence", None)
        self.__pDL1_WorkSequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pDL1_WorkDefinition"):
                opp_val = getattr(old_value, "pDL1_WorkDefinition", None)
                if opp_val == self:
                    setattr(old_value, "pDL1_WorkDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL1_WorkDefinition"):
                opp_val = getattr(value, "pDL1_WorkDefinition", None)
                setattr(value, "pDL1_WorkDefinition", self)

class pDL1_Guidance(ProcessElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class pDL1_WorkDefinition(ProcessElement):

    def __init__(self, name: str, pDL1_WorkDefinition: "pDL1_WorkSequence" = None, pDL1_WorkDefinition4: "pDL1_WorkSequence" = None):
        self.name = name
        self.pDL1_WorkDefinition = pDL1_WorkDefinition
        self.pDL1_WorkDefinition4 = pDL1_WorkDefinition4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pDL1_WorkDefinition4(self):
        return self.__pDL1_WorkDefinition4

    @pDL1_WorkDefinition4.setter
    def pDL1_WorkDefinition4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL1_WorkDefinition__pDL1_WorkDefinition4", None)
        self.__pDL1_WorkDefinition4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pDL1_WorkSequence3"):
                opp_val = getattr(old_value, "pDL1_WorkSequence3", None)
                if opp_val == self:
                    setattr(old_value, "pDL1_WorkSequence3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL1_WorkSequence3"):
                opp_val = getattr(value, "pDL1_WorkSequence3", None)
                setattr(value, "pDL1_WorkSequence3", self)

    @property
    def pDL1_WorkDefinition(self):
        return self.__pDL1_WorkDefinition

    @pDL1_WorkDefinition.setter
    def pDL1_WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL1_WorkDefinition__pDL1_WorkDefinition", None)
        self.__pDL1_WorkDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pDL1_WorkSequence"):
                opp_val = getattr(old_value, "pDL1_WorkSequence", None)
                if opp_val == self:
                    setattr(old_value, "pDL1_WorkSequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL1_WorkSequence"):
                opp_val = getattr(value, "pDL1_WorkSequence", None)
                setattr(value, "pDL1_WorkSequence", self)

class pDL1_ProcessElement:

    pass