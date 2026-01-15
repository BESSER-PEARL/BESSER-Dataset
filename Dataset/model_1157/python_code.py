from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class EModelElement:

    pass
class fiacremm_Transition(EModelElement):

    def __init__(self, Name: str, Transition: "fiacremm_State" = None, Transition2: "fiacremm_State" = None, outTransitions: "fiacremm_State" = None, inTransitions: "fiacremm_State" = None, fiacremm_Transition18: "fiacremm_Guard" = None, fiacremm_Transition20: "fiacremm_Trigger" = None, fiacremm_Transition23: "fiacremm_Action" = None, fiacremm_Transition: "fiacremm_Process" = None):
        self.Name = Name
        self.Transition = Transition
        self.Transition2 = Transition2
        self.outTransitions = outTransitions
        self.inTransitions = inTransitions
        self.fiacremm_Transition18 = fiacremm_Transition18
        self.fiacremm_Transition20 = fiacremm_Transition20
        self.fiacremm_Transition23 = fiacremm_Transition23
        self.fiacremm_Transition = fiacremm_Transition
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def fiacremm_Transition18(self):
        return self.__fiacremm_Transition18

    @fiacremm_Transition18.setter
    def fiacremm_Transition18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Transition__fiacremm_Transition18", None)
        self.__fiacremm_Transition18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Guard"):
                opp_val = getattr(old_value, "fiacremm_Guard", None)
                if opp_val == self:
                    setattr(old_value, "fiacremm_Guard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Guard"):
                opp_val = getattr(value, "fiacremm_Guard", None)
                setattr(value, "fiacremm_Guard", self)

    @property
    def outTransitions(self):
        return self.__outTransitions

    @outTransitions.setter
    def outTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Transition__outTransitions", None)
        self.__outTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State14"):
                opp_val = getattr(old_value, "State14", None)
                if opp_val == self:
                    setattr(old_value, "State14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State14"):
                opp_val = getattr(value, "State14", None)
                setattr(value, "State14", self)

    @property
    def fiacremm_Transition(self):
        return self.__fiacremm_Transition

    @fiacremm_Transition.setter
    def fiacremm_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Transition__fiacremm_Transition", None)
        self.__fiacremm_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Process"):
                opp_val = getattr(old_value, "fiacremm_Process", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Process"):
                opp_val = getattr(value, "fiacremm_Process", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Process", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inTransitions(self):
        return self.__inTransitions

    @inTransitions.setter
    def inTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Transition__inTransitions", None)
        self.__inTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State16"):
                opp_val = getattr(old_value, "State16", None)
                if opp_val == self:
                    setattr(old_value, "State16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State16"):
                opp_val = getattr(value, "State16", None)
                setattr(value, "State16", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacremm_Transition23(self):
        return self.__fiacremm_Transition23

    @fiacremm_Transition23.setter
    def fiacremm_Transition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Transition__fiacremm_Transition23", None)
        self.__fiacremm_Transition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Action"):
                opp_val = getattr(old_value, "fiacremm_Action", None)
                if opp_val == self:
                    setattr(old_value, "fiacremm_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Action"):
                opp_val = getattr(value, "fiacremm_Action", None)
                setattr(value, "fiacremm_Action", self)

    @property
    def Transition2(self):
        return self.__Transition2

    @Transition2.setter
    def Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Transition__Transition2", None)
        self.__Transition2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacremm_Transition20(self):
        return self.__fiacremm_Transition20

    @fiacremm_Transition20.setter
    def fiacremm_Transition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Transition__fiacremm_Transition20", None)
        self.__fiacremm_Transition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Trigger21"):
                opp_val = getattr(old_value, "fiacremm_Trigger21", None)
                if opp_val == self:
                    setattr(old_value, "fiacremm_Trigger21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Trigger21"):
                opp_val = getattr(value, "fiacremm_Trigger21", None)
                setattr(value, "fiacremm_Trigger21", self)

class fiacremm_Program(EModelElement):

    def __init__(self, Name: str, ComponentSize: int, fiacremm_Program: set["fiacremm_Component"] = None, fiacremm_Program39: set["fiacremm_Variable"] = None, fiacremm_Program42: set["fiacremm_Process"] = None, fiacremm_Program45: set["fiacremm_DataType"] = None):
        self.Name = Name
        self.ComponentSize = ComponentSize
        self.fiacremm_Program = fiacremm_Program if fiacremm_Program is not None else set()
        self.fiacremm_Program39 = fiacremm_Program39 if fiacremm_Program39 is not None else set()
        self.fiacremm_Program42 = fiacremm_Program42 if fiacremm_Program42 is not None else set()
        self.fiacremm_Program45 = fiacremm_Program45 if fiacremm_Program45 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ComponentSize(self) -> int:
        return self.__ComponentSize

    @ComponentSize.setter
    def ComponentSize(self, ComponentSize: int):
        self.__ComponentSize = ComponentSize

    @property
    def fiacremm_Program45(self):
        return self.__fiacremm_Program45

    @fiacremm_Program45.setter
    def fiacremm_Program45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Program__fiacremm_Program45", None)
        self.__fiacremm_Program45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_DataType46"):
                    opp_val = getattr(item, "fiacremm_DataType46", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_DataType46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_DataType46"):
                    opp_val = getattr(item, "fiacremm_DataType46", None)
                    
                    setattr(item, "fiacremm_DataType46", self)
                    

    @property
    def fiacremm_Program(self):
        return self.__fiacremm_Program

    @fiacremm_Program.setter
    def fiacremm_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Program__fiacremm_Program", None)
        self.__fiacremm_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_Component37"):
                    opp_val = getattr(item, "fiacremm_Component37", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_Component37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_Component37"):
                    opp_val = getattr(item, "fiacremm_Component37", None)
                    
                    setattr(item, "fiacremm_Component37", self)
                    

    @property
    def fiacremm_Program42(self):
        return self.__fiacremm_Program42

    @fiacremm_Program42.setter
    def fiacremm_Program42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Program__fiacremm_Program42", None)
        self.__fiacremm_Program42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_Process43"):
                    opp_val = getattr(item, "fiacremm_Process43", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_Process43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_Process43"):
                    opp_val = getattr(item, "fiacremm_Process43", None)
                    
                    setattr(item, "fiacremm_Process43", self)
                    

    @property
    def fiacremm_Program39(self):
        return self.__fiacremm_Program39

    @fiacremm_Program39.setter
    def fiacremm_Program39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Program__fiacremm_Program39", None)
        self.__fiacremm_Program39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_Variable40"):
                    opp_val = getattr(item, "fiacremm_Variable40", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_Variable40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_Variable40"):
                    opp_val = getattr(item, "fiacremm_Variable40", None)
                    
                    setattr(item, "fiacremm_Variable40", self)
                    

class fiacremm_DataType(EModelElement):

    def __init__(self, Name: str, fiacremm_DataType: "fiacremm_Variable" = None, fiacremm_DataType46: "fiacremm_Program" = None):
        self.Name = Name
        self.fiacremm_DataType = fiacremm_DataType
        self.fiacremm_DataType46 = fiacremm_DataType46
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def fiacremm_DataType46(self):
        return self.__fiacremm_DataType46

    @fiacremm_DataType46.setter
    def fiacremm_DataType46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_DataType__fiacremm_DataType46", None)
        self.__fiacremm_DataType46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Program45"):
                opp_val = getattr(old_value, "fiacremm_Program45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Program45"):
                opp_val = getattr(value, "fiacremm_Program45", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Program45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacremm_DataType(self):
        return self.__fiacremm_DataType

    @fiacremm_DataType.setter
    def fiacremm_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_DataType__fiacremm_DataType", None)
        self.__fiacremm_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Variable"):
                opp_val = getattr(old_value, "fiacremm_Variable", None)
                if opp_val == self:
                    setattr(old_value, "fiacremm_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Variable"):
                opp_val = getattr(value, "fiacremm_Variable", None)
                setattr(value, "fiacremm_Variable", self)

class fiacremm_Variable(EModelElement):

    def __init__(self, initVal: str, Name: str, Variable: "fiacremm_Process" = None, variables28: set["fiacremm_Component"] = None, Variable32: "fiacremm_Component" = None, fiacremm_Variable40: "fiacremm_Program" = None, fiacremm_Variable: "fiacremm_DataType" = None, variables: set["fiacremm_Process"] = None, fiacremm_Variable49: "fiacremm_Trigger" = None):
        self.initVal = initVal
        self.Name = Name
        self.Variable = Variable
        self.variables28 = variables28 if variables28 is not None else set()
        self.Variable32 = Variable32
        self.fiacremm_Variable40 = fiacremm_Variable40
        self.fiacremm_Variable = fiacremm_Variable
        self.variables = variables if variables is not None else set()
        self.fiacremm_Variable49 = fiacremm_Variable49
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def initVal(self) -> str:
        return self.__initVal

    @initVal.setter
    def initVal(self, initVal: str):
        self.__initVal = initVal

    @property
    def fiacremm_Variable(self):
        return self.__fiacremm_Variable

    @fiacremm_Variable.setter
    def fiacremm_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Variable__fiacremm_Variable", None)
        self.__fiacremm_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_DataType"):
                opp_val = getattr(old_value, "fiacremm_DataType", None)
                if opp_val == self:
                    setattr(old_value, "fiacremm_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_DataType"):
                opp_val = getattr(value, "fiacremm_DataType", None)
                setattr(value, "fiacremm_DataType", self)

    @property
    def variables28(self):
        return self.__variables28

    @variables28.setter
    def variables28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Variable__variables28", None)
        self.__variables28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Component"):
                    opp_val = getattr(item, "Component", None)
                    
                    if opp_val == self:
                        setattr(item, "Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Component"):
                    opp_val = getattr(item, "Component", None)
                    
                    setattr(item, "Component", self)
                    

    @property
    def fiacremm_Variable40(self):
        return self.__fiacremm_Variable40

    @fiacremm_Variable40.setter
    def fiacremm_Variable40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Variable__fiacremm_Variable40", None)
        self.__fiacremm_Variable40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Program39"):
                opp_val = getattr(old_value, "fiacremm_Program39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Program39"):
                opp_val = getattr(value, "fiacremm_Program39", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Program39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Variable32(self):
        return self.__Variable32

    @Variable32.setter
    def Variable32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Variable__Variable32", None)
        self.__Variable32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "components"):
                opp_val = getattr(old_value, "components", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "components"):
                opp_val = getattr(value, "components", None)
                if opp_val is None:
                    setattr(value, "components", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Variable(self):
        return self.__Variable

    @Variable.setter
    def Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Variable__Variable", None)
        self.__Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "processes"):
                opp_val = getattr(old_value, "processes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "processes"):
                opp_val = getattr(value, "processes", None)
                if opp_val is None:
                    setattr(value, "processes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def variables(self):
        return self.__variables

    @variables.setter
    def variables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Variable__variables", None)
        self.__variables = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Process26"):
                    opp_val = getattr(item, "Process26", None)
                    
                    if opp_val == self:
                        setattr(item, "Process26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Process26"):
                    opp_val = getattr(item, "Process26", None)
                    
                    setattr(item, "Process26", self)
                    

    @property
    def fiacremm_Variable49(self):
        return self.__fiacremm_Variable49

    @fiacremm_Variable49.setter
    def fiacremm_Variable49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Variable__fiacremm_Variable49", None)
        self.__fiacremm_Variable49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Trigger48"):
                opp_val = getattr(old_value, "fiacremm_Trigger48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Trigger48"):
                opp_val = getattr(value, "fiacremm_Trigger48", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Trigger48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fiacremm_Action(EModelElement):

    def __init__(self, Name: str, Body: str, codeFiacre: str, fiacremm_Action: "fiacremm_Transition" = None):
        self.Name = Name
        self.Body = Body
        self.codeFiacre = codeFiacre
        self.fiacremm_Action = fiacremm_Action
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Body(self) -> str:
        return self.__Body

    @Body.setter
    def Body(self, Body: str):
        self.__Body = Body

    @property
    def codeFiacre(self) -> str:
        return self.__codeFiacre

    @codeFiacre.setter
    def codeFiacre(self, codeFiacre: str):
        self.__codeFiacre = codeFiacre

    @property
    def fiacremm_Action(self):
        return self.__fiacremm_Action

    @fiacremm_Action.setter
    def fiacremm_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Action__fiacremm_Action", None)
        self.__fiacremm_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Transition23"):
                opp_val = getattr(old_value, "fiacremm_Transition23", None)
                if opp_val == self:
                    setattr(old_value, "fiacremm_Transition23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Transition23"):
                opp_val = getattr(value, "fiacremm_Transition23", None)
                setattr(value, "fiacremm_Transition23", self)

class fiacremm_Guard(EModelElement):

    def __init__(self, Name: str, Body: str, codeFiacre: str, fiacremm_Guard: "fiacremm_Transition" = None):
        self.Name = Name
        self.Body = Body
        self.codeFiacre = codeFiacre
        self.fiacremm_Guard = fiacremm_Guard
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def codeFiacre(self) -> str:
        return self.__codeFiacre

    @codeFiacre.setter
    def codeFiacre(self, codeFiacre: str):
        self.__codeFiacre = codeFiacre

    @property
    def Body(self) -> str:
        return self.__Body

    @Body.setter
    def Body(self, Body: str):
        self.__Body = Body

    @property
    def fiacremm_Guard(self):
        return self.__fiacremm_Guard

    @fiacremm_Guard.setter
    def fiacremm_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Guard__fiacremm_Guard", None)
        self.__fiacremm_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Transition18"):
                opp_val = getattr(old_value, "fiacremm_Transition18", None)
                if opp_val == self:
                    setattr(old_value, "fiacremm_Transition18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Transition18"):
                opp_val = getattr(value, "fiacremm_Transition18", None)
                setattr(value, "fiacremm_Transition18", self)

class fiacremm_Process(EModelElement):

    def __init__(self, StateSize: int, VarSize: int, Name: str, Process: "fiacremm_State" = None, fiacremm_Process7: set["fiacremm_State"] = None, process: "fiacremm_State" = None, fiacremm_Process10: "fiacremm_Port" = None, fiacremm_Process12: set["fiacremm_Trigger"] = None, fiacremm_Process: set["fiacremm_Transition"] = None, processes: set["fiacremm_Variable"] = None, fiacremm_Process30: "fiacremm_Component" = None, fiacremm_Process43: "fiacremm_Program" = None, Process26: "fiacremm_Variable" = None):
        self.StateSize = StateSize
        self.VarSize = VarSize
        self.Name = Name
        self.Process = Process
        self.fiacremm_Process7 = fiacremm_Process7 if fiacremm_Process7 is not None else set()
        self.process = process
        self.fiacremm_Process10 = fiacremm_Process10
        self.fiacremm_Process12 = fiacremm_Process12 if fiacremm_Process12 is not None else set()
        self.fiacremm_Process = fiacremm_Process if fiacremm_Process is not None else set()
        self.processes = processes if processes is not None else set()
        self.fiacremm_Process30 = fiacremm_Process30
        self.fiacremm_Process43 = fiacremm_Process43
        self.Process26 = Process26
        
    @property
    def StateSize(self) -> int:
        return self.__StateSize

    @StateSize.setter
    def StateSize(self, StateSize: int):
        self.__StateSize = StateSize

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def VarSize(self) -> int:
        return self.__VarSize

    @VarSize.setter
    def VarSize(self, VarSize: int):
        self.__VarSize = VarSize

    @property
    def fiacremm_Process10(self):
        return self.__fiacremm_Process10

    @fiacremm_Process10.setter
    def fiacremm_Process10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Process__fiacremm_Process10", None)
        self.__fiacremm_Process10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Port"):
                opp_val = getattr(old_value, "fiacremm_Port", None)
                if opp_val == self:
                    setattr(old_value, "fiacremm_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Port"):
                opp_val = getattr(value, "fiacremm_Port", None)
                setattr(value, "fiacremm_Port", self)

    @property
    def processes(self):
        return self.__processes

    @processes.setter
    def processes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Process__processes", None)
        self.__processes = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable"):
                    opp_val = getattr(item, "Variable", None)
                    
                    setattr(item, "Variable", self)
                    

    @property
    def Process(self):
        return self.__Process

    @Process.setter
    def Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Process__Process", None)
        self.__Process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "initState"):
                opp_val = getattr(old_value, "initState", None)
                if opp_val == self:
                    setattr(old_value, "initState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "initState"):
                opp_val = getattr(value, "initState", None)
                setattr(value, "initState", self)

    @property
    def fiacremm_Process12(self):
        return self.__fiacremm_Process12

    @fiacremm_Process12.setter
    def fiacremm_Process12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Process__fiacremm_Process12", None)
        self.__fiacremm_Process12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_Trigger"):
                    opp_val = getattr(item, "fiacremm_Trigger", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_Trigger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_Trigger"):
                    opp_val = getattr(item, "fiacremm_Trigger", None)
                    
                    setattr(item, "fiacremm_Trigger", self)
                    

    @property
    def fiacremm_Process(self):
        return self.__fiacremm_Process

    @fiacremm_Process.setter
    def fiacremm_Process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Process__fiacremm_Process", None)
        self.__fiacremm_Process = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_Transition"):
                    opp_val = getattr(item, "fiacremm_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_Transition"):
                    opp_val = getattr(item, "fiacremm_Transition", None)
                    
                    setattr(item, "fiacremm_Transition", self)
                    

    @property
    def fiacremm_Process43(self):
        return self.__fiacremm_Process43

    @fiacremm_Process43.setter
    def fiacremm_Process43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Process__fiacremm_Process43", None)
        self.__fiacremm_Process43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Program42"):
                opp_val = getattr(old_value, "fiacremm_Program42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Program42"):
                opp_val = getattr(value, "fiacremm_Program42", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Program42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacremm_Process7(self):
        return self.__fiacremm_Process7

    @fiacremm_Process7.setter
    def fiacremm_Process7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Process__fiacremm_Process7", None)
        self.__fiacremm_Process7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_State"):
                    opp_val = getattr(item, "fiacremm_State", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_State"):
                    opp_val = getattr(item, "fiacremm_State", None)
                    
                    setattr(item, "fiacremm_State", self)
                    

    @property
    def Process26(self):
        return self.__Process26

    @Process26.setter
    def Process26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Process__Process26", None)
        self.__Process26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variables"):
                opp_val = getattr(old_value, "variables", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variables"):
                opp_val = getattr(value, "variables", None)
                if opp_val is None:
                    setattr(value, "variables", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def process(self):
        return self.__process

    @process.setter
    def process(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Process__process", None)
        self.__process = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State"):
                opp_val = getattr(old_value, "State", None)
                if opp_val == self:
                    setattr(old_value, "State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State"):
                opp_val = getattr(value, "State", None)
                setattr(value, "State", self)

    @property
    def fiacremm_Process30(self):
        return self.__fiacremm_Process30

    @fiacremm_Process30.setter
    def fiacremm_Process30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Process__fiacremm_Process30", None)
        self.__fiacremm_Process30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Component"):
                opp_val = getattr(old_value, "fiacremm_Component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Component"):
                opp_val = getattr(value, "fiacremm_Component", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fiacremm_Port(EModelElement):

    def __init__(self, Name: str, fiacremm_Port: "fiacremm_Process" = None, fiacremm_Port35: "fiacremm_Component" = None, fiacremm_Port51: set["fiacremm_Component"] = None):
        self.Name = Name
        self.fiacremm_Port = fiacremm_Port
        self.fiacremm_Port35 = fiacremm_Port35
        self.fiacremm_Port51 = fiacremm_Port51 if fiacremm_Port51 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def fiacremm_Port35(self):
        return self.__fiacremm_Port35

    @fiacremm_Port35.setter
    def fiacremm_Port35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Port__fiacremm_Port35", None)
        self.__fiacremm_Port35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Component34"):
                opp_val = getattr(old_value, "fiacremm_Component34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Component34"):
                opp_val = getattr(value, "fiacremm_Component34", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Component34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacremm_Port(self):
        return self.__fiacremm_Port

    @fiacremm_Port.setter
    def fiacremm_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Port__fiacremm_Port", None)
        self.__fiacremm_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Process10"):
                opp_val = getattr(old_value, "fiacremm_Process10", None)
                if opp_val == self:
                    setattr(old_value, "fiacremm_Process10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Process10"):
                opp_val = getattr(value, "fiacremm_Process10", None)
                setattr(value, "fiacremm_Process10", self)

    @property
    def fiacremm_Port51(self):
        return self.__fiacremm_Port51

    @fiacremm_Port51.setter
    def fiacremm_Port51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Port__fiacremm_Port51", None)
        self.__fiacremm_Port51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_Component52"):
                    opp_val = getattr(item, "fiacremm_Component52", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_Component52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_Component52"):
                    opp_val = getattr(item, "fiacremm_Component52", None)
                    
                    setattr(item, "fiacremm_Component52", self)
                    

class fiacremm_Component(EModelElement):

    def __init__(self, Name: str, ProcessSize: int, VarSize: int, Component: "fiacremm_Variable" = None, fiacremm_Component: set["fiacremm_Process"] = None, components: set["fiacremm_Variable"] = None, fiacremm_Component34: set["fiacremm_Port"] = None, fiacremm_Component37: "fiacremm_Program" = None, fiacremm_Component52: "fiacremm_Port" = None):
        self.Name = Name
        self.ProcessSize = ProcessSize
        self.VarSize = VarSize
        self.Component = Component
        self.fiacremm_Component = fiacremm_Component if fiacremm_Component is not None else set()
        self.components = components if components is not None else set()
        self.fiacremm_Component34 = fiacremm_Component34 if fiacremm_Component34 is not None else set()
        self.fiacremm_Component37 = fiacremm_Component37
        self.fiacremm_Component52 = fiacremm_Component52
        
    @property
    def VarSize(self) -> int:
        return self.__VarSize

    @VarSize.setter
    def VarSize(self, VarSize: int):
        self.__VarSize = VarSize

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ProcessSize(self) -> int:
        return self.__ProcessSize

    @ProcessSize.setter
    def ProcessSize(self, ProcessSize: int):
        self.__ProcessSize = ProcessSize

    @property
    def fiacremm_Component37(self):
        return self.__fiacremm_Component37

    @fiacremm_Component37.setter
    def fiacremm_Component37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Component__fiacremm_Component37", None)
        self.__fiacremm_Component37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Program"):
                opp_val = getattr(old_value, "fiacremm_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Program"):
                opp_val = getattr(value, "fiacremm_Program", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacremm_Component52(self):
        return self.__fiacremm_Component52

    @fiacremm_Component52.setter
    def fiacremm_Component52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Component__fiacremm_Component52", None)
        self.__fiacremm_Component52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Port51"):
                opp_val = getattr(old_value, "fiacremm_Port51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Port51"):
                opp_val = getattr(value, "fiacremm_Port51", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Port51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Component(self):
        return self.__Component

    @Component.setter
    def Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Component__Component", None)
        self.__Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variables28"):
                opp_val = getattr(old_value, "variables28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variables28"):
                opp_val = getattr(value, "variables28", None)
                if opp_val is None:
                    setattr(value, "variables28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacremm_Component(self):
        return self.__fiacremm_Component

    @fiacremm_Component.setter
    def fiacremm_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Component__fiacremm_Component", None)
        self.__fiacremm_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_Process30"):
                    opp_val = getattr(item, "fiacremm_Process30", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_Process30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_Process30"):
                    opp_val = getattr(item, "fiacremm_Process30", None)
                    
                    setattr(item, "fiacremm_Process30", self)
                    

    @property
    def components(self):
        return self.__components

    @components.setter
    def components(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Component__components", None)
        self.__components = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variable32"):
                    opp_val = getattr(item, "Variable32", None)
                    
                    if opp_val == self:
                        setattr(item, "Variable32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variable32"):
                    opp_val = getattr(item, "Variable32", None)
                    
                    setattr(item, "Variable32", self)
                    

    @property
    def fiacremm_Component34(self):
        return self.__fiacremm_Component34

    @fiacremm_Component34.setter
    def fiacremm_Component34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Component__fiacremm_Component34", None)
        self.__fiacremm_Component34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_Port35"):
                    opp_val = getattr(item, "fiacremm_Port35", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_Port35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_Port35"):
                    opp_val = getattr(item, "fiacremm_Port35", None)
                    
                    setattr(item, "fiacremm_Port35", self)
                    

class fiacremm_Trigger(EModelElement):

    def __init__(self, Name: str, Body: str, codeFiacre: str, ArgSize: int, fiacremm_Trigger: "fiacremm_Process" = None, fiacremm_Trigger21: "fiacremm_Transition" = None, fiacremm_Trigger48: set["fiacremm_Variable"] = None):
        self.Name = Name
        self.Body = Body
        self.codeFiacre = codeFiacre
        self.ArgSize = ArgSize
        self.fiacremm_Trigger = fiacremm_Trigger
        self.fiacremm_Trigger21 = fiacremm_Trigger21
        self.fiacremm_Trigger48 = fiacremm_Trigger48 if fiacremm_Trigger48 is not None else set()
        
    @property
    def Body(self) -> str:
        return self.__Body

    @Body.setter
    def Body(self, Body: str):
        self.__Body = Body

    @property
    def codeFiacre(self) -> str:
        return self.__codeFiacre

    @codeFiacre.setter
    def codeFiacre(self, codeFiacre: str):
        self.__codeFiacre = codeFiacre

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ArgSize(self) -> int:
        return self.__ArgSize

    @ArgSize.setter
    def ArgSize(self, ArgSize: int):
        self.__ArgSize = ArgSize

    @property
    def fiacremm_Trigger48(self):
        return self.__fiacremm_Trigger48

    @fiacremm_Trigger48.setter
    def fiacremm_Trigger48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Trigger__fiacremm_Trigger48", None)
        self.__fiacremm_Trigger48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fiacremm_Variable49"):
                    opp_val = getattr(item, "fiacremm_Variable49", None)
                    
                    if opp_val == self:
                        setattr(item, "fiacremm_Variable49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fiacremm_Variable49"):
                    opp_val = getattr(item, "fiacremm_Variable49", None)
                    
                    setattr(item, "fiacremm_Variable49", self)
                    

    @property
    def fiacremm_Trigger(self):
        return self.__fiacremm_Trigger

    @fiacremm_Trigger.setter
    def fiacremm_Trigger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Trigger__fiacremm_Trigger", None)
        self.__fiacremm_Trigger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Process12"):
                opp_val = getattr(old_value, "fiacremm_Process12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Process12"):
                opp_val = getattr(value, "fiacremm_Process12", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Process12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fiacremm_Trigger21(self):
        return self.__fiacremm_Trigger21

    @fiacremm_Trigger21.setter
    def fiacremm_Trigger21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_Trigger__fiacremm_Trigger21", None)
        self.__fiacremm_Trigger21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Transition20"):
                opp_val = getattr(old_value, "fiacremm_Transition20", None)
                if opp_val == self:
                    setattr(old_value, "fiacremm_Transition20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Transition20"):
                opp_val = getattr(value, "fiacremm_Transition20", None)
                setattr(value, "fiacremm_Transition20", self)

class fiacremm_State(EModelElement):

    def __init__(self, Name: str, source: set["fiacremm_Transition"] = None, target: set["fiacremm_Transition"] = None, initState: "fiacremm_Process" = None, fiacremm_State: "fiacremm_Process" = None, State: "fiacremm_Process" = None, State14: "fiacremm_Transition" = None, State16: "fiacremm_Transition" = None):
        self.Name = Name
        self.source = source if source is not None else set()
        self.target = target if target is not None else set()
        self.initState = initState
        self.fiacremm_State = fiacremm_State
        self.State = State
        self.State14 = State14
        self.State16 = State16
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def State16(self):
        return self.__State16

    @State16.setter
    def State16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_State__State16", None)
        self.__State16 = value
        
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
    def initState(self):
        return self.__initState

    @initState.setter
    def initState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_State__initState", None)
        self.__initState = value
        
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
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_State__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transition2"):
                    opp_val = getattr(item, "Transition2", None)
                    
                    if opp_val == self:
                        setattr(item, "Transition2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transition2"):
                    opp_val = getattr(item, "Transition2", None)
                    
                    setattr(item, "Transition2", self)
                    

    @property
    def fiacremm_State(self):
        return self.__fiacremm_State

    @fiacremm_State.setter
    def fiacremm_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_State__fiacremm_State", None)
        self.__fiacremm_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fiacremm_Process7"):
                opp_val = getattr(old_value, "fiacremm_Process7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fiacremm_Process7"):
                opp_val = getattr(value, "fiacremm_Process7", None)
                if opp_val is None:
                    setattr(value, "fiacremm_Process7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_State__source", None)
        self.__source = value if value is not None else set()
        
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
    def State14(self):
        return self.__State14

    @State14.setter
    def State14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_State__State14", None)
        self.__State14 = value
        
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
    def State(self):
        return self.__State

    @State.setter
    def State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fiacremm_State__State", None)
        self.__State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "process"):
                opp_val = getattr(old_value, "process", None)
                if opp_val == self:
                    setattr(old_value, "process", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "process"):
                opp_val = getattr(value, "process", None)
                setattr(value, "process", self)
