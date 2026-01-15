from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pDL2_WorkSequenceKindFinish:

    def __init__(self, Finished2Start: str, Finished2Finish: str, pDL2_WorkSequenceKindFinish: "pDL2_DependanceFinish" = None):
        self.Finished2Start = Finished2Start
        self.Finished2Finish = Finished2Finish
        self.pDL2_WorkSequenceKindFinish = pDL2_WorkSequenceKindFinish
        
    @property
    def Finished2Finish(self) -> str:
        return self.__Finished2Finish

    @Finished2Finish.setter
    def Finished2Finish(self, Finished2Finish: str):
        self.__Finished2Finish = Finished2Finish

    @property
    def Finished2Start(self) -> str:
        return self.__Finished2Start

    @Finished2Start.setter
    def Finished2Start(self, Finished2Start: str):
        self.__Finished2Start = Finished2Start

    @property
    def pDL2_WorkSequenceKindFinish(self):
        return self.__pDL2_WorkSequenceKindFinish

    @pDL2_WorkSequenceKindFinish.setter
    def pDL2_WorkSequenceKindFinish(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL2_WorkSequenceKindFinish__pDL2_WorkSequenceKindFinish", None)
        self.__pDL2_WorkSequenceKindFinish = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pDL2_DependanceFinish13"):
                opp_val = getattr(old_value, "pDL2_DependanceFinish13", None)
                if opp_val == self:
                    setattr(old_value, "pDL2_DependanceFinish13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL2_DependanceFinish13"):
                opp_val = getattr(value, "pDL2_DependanceFinish13", None)
                setattr(value, "pDL2_DependanceFinish13", self)

class pDL2_WorkSequenceKindStart:

    def __init__(self, Started2Start: str, Started2Finish: str, pDL2_WorkSequenceKindStart: "pDL2_DependanceStart" = None):
        self.Started2Start = Started2Start
        self.Started2Finish = Started2Finish
        self.pDL2_WorkSequenceKindStart = pDL2_WorkSequenceKindStart
        
    @property
    def Started2Finish(self) -> str:
        return self.__Started2Finish

    @Started2Finish.setter
    def Started2Finish(self, Started2Finish: str):
        self.__Started2Finish = Started2Finish

    @property
    def Started2Start(self) -> str:
        return self.__Started2Start

    @Started2Start.setter
    def Started2Start(self, Started2Start: str):
        self.__Started2Start = Started2Start

    @property
    def pDL2_WorkSequenceKindStart(self):
        return self.__pDL2_WorkSequenceKindStart

    @pDL2_WorkSequenceKindStart.setter
    def pDL2_WorkSequenceKindStart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL2_WorkSequenceKindStart__pDL2_WorkSequenceKindStart", None)
        self.__pDL2_WorkSequenceKindStart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pDL2_DependanceStart8"):
                opp_val = getattr(old_value, "pDL2_DependanceStart8", None)
                if opp_val == self:
                    setattr(old_value, "pDL2_DependanceStart8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL2_DependanceStart8"):
                opp_val = getattr(value, "pDL2_DependanceStart8", None)
                setattr(value, "pDL2_DependanceStart8", self)

class pDL2_DependanceFinish:

    pass
class pDL2_DependanceStart:

    pass
class ProcessElement:

    pass
class pDL2_Guidance(ProcessElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class pDL2_WorkDefinition(ProcessElement):

    def __init__(self, name: str, pDL2_WorkDefinition: set["pDL2_DependanceStart"] = None, pDL2_WorkDefinition3: set["pDL2_DependanceFinish"] = None, pDL2_WorkDefinition6: "pDL2_DependanceStart" = None, pDL2_WorkDefinition11: "pDL2_DependanceFinish" = None):
        self.name = name
        self.pDL2_WorkDefinition = pDL2_WorkDefinition if pDL2_WorkDefinition is not None else set()
        self.pDL2_WorkDefinition3 = pDL2_WorkDefinition3 if pDL2_WorkDefinition3 is not None else set()
        self.pDL2_WorkDefinition6 = pDL2_WorkDefinition6
        self.pDL2_WorkDefinition11 = pDL2_WorkDefinition11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pDL2_WorkDefinition11(self):
        return self.__pDL2_WorkDefinition11

    @pDL2_WorkDefinition11.setter
    def pDL2_WorkDefinition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL2_WorkDefinition__pDL2_WorkDefinition11", None)
        self.__pDL2_WorkDefinition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pDL2_DependanceFinish10"):
                opp_val = getattr(old_value, "pDL2_DependanceFinish10", None)
                if opp_val == self:
                    setattr(old_value, "pDL2_DependanceFinish10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL2_DependanceFinish10"):
                opp_val = getattr(value, "pDL2_DependanceFinish10", None)
                setattr(value, "pDL2_DependanceFinish10", self)

    @property
    def pDL2_WorkDefinition6(self):
        return self.__pDL2_WorkDefinition6

    @pDL2_WorkDefinition6.setter
    def pDL2_WorkDefinition6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL2_WorkDefinition__pDL2_WorkDefinition6", None)
        self.__pDL2_WorkDefinition6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pDL2_DependanceStart5"):
                opp_val = getattr(old_value, "pDL2_DependanceStart5", None)
                if opp_val == self:
                    setattr(old_value, "pDL2_DependanceStart5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL2_DependanceStart5"):
                opp_val = getattr(value, "pDL2_DependanceStart5", None)
                setattr(value, "pDL2_DependanceStart5", self)

    @property
    def pDL2_WorkDefinition3(self):
        return self.__pDL2_WorkDefinition3

    @pDL2_WorkDefinition3.setter
    def pDL2_WorkDefinition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL2_WorkDefinition__pDL2_WorkDefinition3", None)
        self.__pDL2_WorkDefinition3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pDL2_DependanceFinish"):
                    opp_val = getattr(item, "pDL2_DependanceFinish", None)
                    
                    if opp_val == self:
                        setattr(item, "pDL2_DependanceFinish", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pDL2_DependanceFinish"):
                    opp_val = getattr(item, "pDL2_DependanceFinish", None)
                    
                    setattr(item, "pDL2_DependanceFinish", self)
                    

    @property
    def pDL2_WorkDefinition(self):
        return self.__pDL2_WorkDefinition

    @pDL2_WorkDefinition.setter
    def pDL2_WorkDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL2_WorkDefinition__pDL2_WorkDefinition", None)
        self.__pDL2_WorkDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pDL2_DependanceStart"):
                    opp_val = getattr(item, "pDL2_DependanceStart", None)
                    
                    if opp_val == self:
                        setattr(item, "pDL2_DependanceStart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pDL2_DependanceStart"):
                    opp_val = getattr(item, "pDL2_DependanceStart", None)
                    
                    setattr(item, "pDL2_DependanceStart", self)
                    

class pDL2_ProcessElement:

    pass
class pDL2_Process:

    def __init__(self, name: str, pDL2_Process: set["pDL2_ProcessElement"] = None):
        self.name = name
        self.pDL2_Process = pDL2_Process if pDL2_Process is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pDL2_Process(self):
        return self.__pDL2_Process

    @pDL2_Process.setter
    def pDL2_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL2_Process__pDL2_Process", None)
        self.__pDL2_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pDL2_ProcessElement"):
                    opp_val = getattr(item, "pDL2_ProcessElement", None)
                    
                    if opp_val == self:
                        setattr(item, "pDL2_ProcessElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pDL2_ProcessElement"):
                    opp_val = getattr(item, "pDL2_ProcessElement", None)
                    
                    setattr(item, "pDL2_ProcessElement", self)
                    
