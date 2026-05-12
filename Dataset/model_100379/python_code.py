from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mmb_Modification:

    def __init__(self, VarName: str, VarType: str, mmb_Modification: "mmb_Mode" = None):
        self.VarName = VarName
        self.VarType = VarType
        self.mmb_Modification = mmb_Modification
        
        pass
    @property
    def VarName(self):
        return self.__VarName

    @VarName.setter
    def VarName(self, VarName: str):
        self.__VarName = VarName


    @property
    def VarType(self):
        return self.__VarType

    @VarType.setter
    def VarType(self, VarType: str):
        self.__VarType = VarType


    @property
    def mmb_Modification(self):
        return self.__mmb_Modification

    @mmb_Modification.setter
    def mmb_Modification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Modification__mmb_Modification", None)
        self.__mmb_Modification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mmb_Mode6"):
                opp_val = getattr(old_value, "mmb_Mode6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mmb_Mode6"):
                opp_val = getattr(value, "mmb_Mode6", None)
                if opp_val is None:
                    setattr(value, "mmb_Mode6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mmb_Transition:

    def __init__(self, Event: str, mmb_Transition11: "mmb_Mode" = None, mmb_Transition: "mmb_Automaton" = None, mmb_Transition8: "mmb_Mode" = None):
        self.Event = Event
        self.mmb_Transition11 = mmb_Transition11
        self.mmb_Transition = mmb_Transition
        self.mmb_Transition8 = mmb_Transition8
        
        pass
    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, Event: str):
        self.__Event = Event


    @property
    def mmb_Transition(self):
        return self.__mmb_Transition

    @mmb_Transition.setter
    def mmb_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Transition__mmb_Transition", None)
        self.__mmb_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mmb_Automaton4"):
                opp_val = getattr(old_value, "mmb_Automaton4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mmb_Automaton4"):
                opp_val = getattr(value, "mmb_Automaton4", None)
                if opp_val is None:
                    setattr(value, "mmb_Automaton4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mmb_Transition11(self):
        return self.__mmb_Transition11

    @mmb_Transition11.setter
    def mmb_Transition11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Transition__mmb_Transition11", None)
        self.__mmb_Transition11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mmb_Mode12"):
                opp_val = getattr(old_value, "mmb_Mode12", None)
                if opp_val == self:
                    setattr(old_value, "mmb_Mode12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mmb_Mode12"):
                opp_val = getattr(value, "mmb_Mode12", None)
                setattr(value, "mmb_Mode12", self)

    @property
    def mmb_Transition8(self):
        return self.__mmb_Transition8

    @mmb_Transition8.setter
    def mmb_Transition8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Transition__mmb_Transition8", None)
        self.__mmb_Transition8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mmb_Mode9"):
                opp_val = getattr(old_value, "mmb_Mode9", None)
                if opp_val == self:
                    setattr(old_value, "mmb_Mode9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mmb_Mode9"):
                opp_val = getattr(value, "mmb_Mode9", None)
                setattr(value, "mmb_Mode9", self)

class mmb_Mode:

    def __init__(self, Name: str, InitialState: bool, Shape: str, Dimension: float, mmb_Mode12: "mmb_Transition" = None, mmb_Mode: "mmb_Automaton" = None, mmb_Mode6: set["mmb_Modification"] = None, mmb_Mode9: "mmb_Transition" = None):
        self.Name = Name
        self.InitialState = InitialState
        self.Shape = Shape
        self.Dimension = Dimension
        self.mmb_Mode12 = mmb_Mode12
        self.mmb_Mode = mmb_Mode
        self.mmb_Mode6 = mmb_Mode6 if mmb_Mode6 is not None else set()
        self.mmb_Mode9 = mmb_Mode9
        
        pass
    @property
    def Shape(self):
        return self.__Shape

    @Shape.setter
    def Shape(self, Shape: str):
        self.__Shape = Shape


    @property
    def Dimension(self):
        return self.__Dimension

    @Dimension.setter
    def Dimension(self, Dimension: float):
        self.__Dimension = Dimension


    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def InitialState(self):
        return self.__InitialState

    @InitialState.setter
    def InitialState(self, InitialState: bool):
        self.__InitialState = InitialState


    @property
    def mmb_Mode9(self):
        return self.__mmb_Mode9

    @mmb_Mode9.setter
    def mmb_Mode9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Mode__mmb_Mode9", None)
        self.__mmb_Mode9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mmb_Transition8"):
                opp_val = getattr(old_value, "mmb_Transition8", None)
                if opp_val == self:
                    setattr(old_value, "mmb_Transition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mmb_Transition8"):
                opp_val = getattr(value, "mmb_Transition8", None)
                setattr(value, "mmb_Transition8", self)

    @property
    def mmb_Mode(self):
        return self.__mmb_Mode

    @mmb_Mode.setter
    def mmb_Mode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Mode__mmb_Mode", None)
        self.__mmb_Mode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mmb_Automaton2"):
                opp_val = getattr(old_value, "mmb_Automaton2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mmb_Automaton2"):
                opp_val = getattr(value, "mmb_Automaton2", None)
                if opp_val is None:
                    setattr(value, "mmb_Automaton2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mmb_Mode12(self):
        return self.__mmb_Mode12

    @mmb_Mode12.setter
    def mmb_Mode12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Mode__mmb_Mode12", None)
        self.__mmb_Mode12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mmb_Transition11"):
                opp_val = getattr(old_value, "mmb_Transition11", None)
                if opp_val == self:
                    setattr(old_value, "mmb_Transition11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mmb_Transition11"):
                opp_val = getattr(value, "mmb_Transition11", None)
                setattr(value, "mmb_Transition11", self)

    @property
    def mmb_Mode6(self):
        return self.__mmb_Mode6

    @mmb_Mode6.setter
    def mmb_Mode6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Mode__mmb_Mode6", None)
        self.__mmb_Mode6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mmb_Modification"):
                    opp_val = getattr(item, "mmb_Modification", None)
                    
                    if opp_val == self:
                        setattr(item, "mmb_Modification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mmb_Modification"):
                    opp_val = getattr(item, "mmb_Modification", None)
                    
                    setattr(item, "mmb_Modification", self)
                    

class mmb_Automaton:

    def __init__(self, Name: str, mmb_Automaton: "mmb_Model" = None, mmb_Automaton2: set["mmb_Mode"] = None, mmb_Automaton4: set["mmb_Transition"] = None):
        self.Name = Name
        self.mmb_Automaton = mmb_Automaton
        self.mmb_Automaton2 = mmb_Automaton2 if mmb_Automaton2 is not None else set()
        self.mmb_Automaton4 = mmb_Automaton4 if mmb_Automaton4 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def mmb_Automaton2(self):
        return self.__mmb_Automaton2

    @mmb_Automaton2.setter
    def mmb_Automaton2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Automaton__mmb_Automaton2", None)
        self.__mmb_Automaton2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mmb_Mode"):
                    opp_val = getattr(item, "mmb_Mode", None)
                    
                    if opp_val == self:
                        setattr(item, "mmb_Mode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mmb_Mode"):
                    opp_val = getattr(item, "mmb_Mode", None)
                    
                    setattr(item, "mmb_Mode", self)
                    

    @property
    def mmb_Automaton4(self):
        return self.__mmb_Automaton4

    @mmb_Automaton4.setter
    def mmb_Automaton4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Automaton__mmb_Automaton4", None)
        self.__mmb_Automaton4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mmb_Transition"):
                    opp_val = getattr(item, "mmb_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "mmb_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mmb_Transition"):
                    opp_val = getattr(item, "mmb_Transition", None)
                    
                    setattr(item, "mmb_Transition", self)
                    

    @property
    def mmb_Automaton(self):
        return self.__mmb_Automaton

    @mmb_Automaton.setter
    def mmb_Automaton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Automaton__mmb_Automaton", None)
        self.__mmb_Automaton = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mmb_Model"):
                opp_val = getattr(old_value, "mmb_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mmb_Model"):
                opp_val = getattr(value, "mmb_Model", None)
                if opp_val is None:
                    setattr(value, "mmb_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mmb_Model:

    def __init__(self, Name: str, mmb_Model: set["mmb_Automaton"] = None):
        self.Name = Name
        self.mmb_Model = mmb_Model if mmb_Model is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name


    @property
    def mmb_Model(self):
        return self.__mmb_Model

    @mmb_Model.setter
    def mmb_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mmb_Model__mmb_Model", None)
        self.__mmb_Model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mmb_Automaton"):
                    opp_val = getattr(item, "mmb_Automaton", None)
                    
                    if opp_val == self:
                        setattr(item, "mmb_Automaton", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mmb_Automaton"):
                    opp_val = getattr(item, "mmb_Automaton", None)
                    
                    setattr(item, "mmb_Automaton", self)
                    
