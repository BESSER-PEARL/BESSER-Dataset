from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pDL2_DependanceFinish:

    pass
class pDL2_WorkSequenceKindStart:

    def __init__(self, Started2Start: str, Started2Finish: str, pDL2_WorkSequenceKindStart: "pDL2_DependanceStart" = None):
        self.Started2Start = Started2Start
        self.Started2Finish = Started2Finish
        self.pDL2_WorkSequenceKindStart = pDL2_WorkSequenceKindStart
        
    @property
    def Started2Start(self) -> str:
        return self.__Started2Start

    @Started2Start.setter
    def Started2Start(self, Started2Start: str):
        self.__Started2Start = Started2Start

    @property
    def Started2Finish(self) -> str:
        return self.__Started2Finish

    @Started2Finish.setter
    def Started2Finish(self, Started2Finish: str):
        self.__Started2Finish = Started2Finish

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
            if hasattr(old_value, "pDL2_DependanceStart5"):
                opp_val = getattr(old_value, "pDL2_DependanceStart5", None)
                if opp_val == self:
                    setattr(old_value, "pDL2_DependanceStart5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL2_DependanceStart5"):
                opp_val = getattr(value, "pDL2_DependanceStart5", None)
                setattr(value, "pDL2_DependanceStart5", self)

class pDL2_DependanceStart:

    pass
class pDL2_EObject:

    pass
class ProcessElement:

    pass
class pDL2_WorkDefinition(ProcessElement):

    def __init__(self, name: str, pDL2_WorkDefinition: set["pDL2_EObject"] = None, pDL2_WorkDefinition3: "pDL2_DependanceStart" = None, pDL2_WorkDefinition7: "pDL2_DependanceFinish" = None):
        self.name = name
        self.pDL2_WorkDefinition = pDL2_WorkDefinition if pDL2_WorkDefinition is not None else set()
        self.pDL2_WorkDefinition3 = pDL2_WorkDefinition3
        self.pDL2_WorkDefinition7 = pDL2_WorkDefinition7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pDL2_WorkDefinition7(self):
        return self.__pDL2_WorkDefinition7

    @pDL2_WorkDefinition7.setter
    def pDL2_WorkDefinition7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL2_WorkDefinition__pDL2_WorkDefinition7", None)
        self.__pDL2_WorkDefinition7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pDL2_DependanceFinish"):
                opp_val = getattr(old_value, "pDL2_DependanceFinish", None)
                if opp_val == self:
                    setattr(old_value, "pDL2_DependanceFinish", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL2_DependanceFinish"):
                opp_val = getattr(value, "pDL2_DependanceFinish", None)
                setattr(value, "pDL2_DependanceFinish", self)

    @property
    def pDL2_WorkDefinition3(self):
        return self.__pDL2_WorkDefinition3

    @pDL2_WorkDefinition3.setter
    def pDL2_WorkDefinition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pDL2_WorkDefinition__pDL2_WorkDefinition3", None)
        self.__pDL2_WorkDefinition3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pDL2_DependanceStart"):
                opp_val = getattr(old_value, "pDL2_DependanceStart", None)
                if opp_val == self:
                    setattr(old_value, "pDL2_DependanceStart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL2_DependanceStart"):
                opp_val = getattr(value, "pDL2_DependanceStart", None)
                setattr(value, "pDL2_DependanceStart", self)

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
                if hasattr(item, "pDL2_EObject"):
                    opp_val = getattr(item, "pDL2_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "pDL2_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pDL2_EObject"):
                    opp_val = getattr(item, "pDL2_EObject", None)
                    
                    setattr(item, "pDL2_EObject", self)
                    

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
                    

class pDL2_Guidance(ProcessElement):

    def __init__(self, texte: str):
        self.texte = texte
        
    @property
    def texte(self) -> str:
        return self.__texte

    @texte.setter
    def texte(self, texte: str):
        self.__texte = texte

class pDL2_WorkSequenceKindFinish:

    def __init__(self, Finished2Start: str, Finished2Finish: str, pDL2_WorkSequenceKindFinish: "pDL2_DependanceFinish" = None):
        self.Finished2Start = Finished2Start
        self.Finished2Finish = Finished2Finish
        self.pDL2_WorkSequenceKindFinish = pDL2_WorkSequenceKindFinish
        
    @property
    def Finished2Start(self) -> str:
        return self.__Finished2Start

    @Finished2Start.setter
    def Finished2Start(self, Finished2Start: str):
        self.__Finished2Start = Finished2Start

    @property
    def Finished2Finish(self) -> str:
        return self.__Finished2Finish

    @Finished2Finish.setter
    def Finished2Finish(self, Finished2Finish: str):
        self.__Finished2Finish = Finished2Finish

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
            if hasattr(old_value, "pDL2_DependanceFinish9"):
                opp_val = getattr(old_value, "pDL2_DependanceFinish9", None)
                if opp_val == self:
                    setattr(old_value, "pDL2_DependanceFinish9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pDL2_DependanceFinish9"):
                opp_val = getattr(value, "pDL2_DependanceFinish9", None)
                setattr(value, "pDL2_DependanceFinish9", self)
