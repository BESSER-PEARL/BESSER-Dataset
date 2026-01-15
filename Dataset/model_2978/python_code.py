from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class machine_Symbol:

    def __init__(self, value: str, name: str, position: str, machine_Symbol: "machine_Tape" = None, machine_Symbol34: "machine_Symbol" = None, machine_Symbol32: "machine_Symbol" = None, machine_Symbol37: "machine_Head" = None):
        self.value = value
        self.name = name
        self.position = position
        self.machine_Symbol = machine_Symbol
        self.machine_Symbol34 = machine_Symbol34
        self.machine_Symbol32 = machine_Symbol32
        self.machine_Symbol37 = machine_Symbol37
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def machine_Symbol37(self):
        return self.__machine_Symbol37

    @machine_Symbol37.setter
    def machine_Symbol37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Symbol__machine_Symbol37", None)
        self.__machine_Symbol37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Head36"):
                opp_val = getattr(old_value, "machine_Head36", None)
                if opp_val == self:
                    setattr(old_value, "machine_Head36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Head36"):
                opp_val = getattr(value, "machine_Head36", None)
                setattr(value, "machine_Head36", self)

    @property
    def machine_Symbol32(self):
        return self.__machine_Symbol32

    @machine_Symbol32.setter
    def machine_Symbol32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Symbol__machine_Symbol32", None)
        self.__machine_Symbol32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Symbol34"):
                opp_val = getattr(old_value, "machine_Symbol34", None)
                if opp_val == self:
                    setattr(old_value, "machine_Symbol34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Symbol34"):
                opp_val = getattr(value, "machine_Symbol34", None)
                setattr(value, "machine_Symbol34", self)

    @property
    def machine_Symbol34(self):
        return self.__machine_Symbol34

    @machine_Symbol34.setter
    def machine_Symbol34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Symbol__machine_Symbol34", None)
        self.__machine_Symbol34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Symbol32"):
                opp_val = getattr(old_value, "machine_Symbol32", None)
                if opp_val == self:
                    setattr(old_value, "machine_Symbol32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Symbol32"):
                opp_val = getattr(value, "machine_Symbol32", None)
                setattr(value, "machine_Symbol32", self)

    @property
    def machine_Symbol(self):
        return self.__machine_Symbol

    @machine_Symbol.setter
    def machine_Symbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Symbol__machine_Symbol", None)
        self.__machine_Symbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Tape"):
                opp_val = getattr(old_value, "machine_Tape", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Tape"):
                opp_val = getattr(value, "machine_Tape", None)
                if opp_val is None:
                    setattr(value, "machine_Tape", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class machine_Tape:

    pass
class machine_Head:

    def __init__(self, name: str, machine_Head: "machine_Machine" = None, machine_Head36: "machine_Symbol" = None):
        self.name = name
        self.machine_Head = machine_Head
        self.machine_Head36 = machine_Head36
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def machine_Head36(self):
        return self.__machine_Head36

    @machine_Head36.setter
    def machine_Head36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Head__machine_Head36", None)
        self.__machine_Head36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Symbol37"):
                opp_val = getattr(old_value, "machine_Symbol37", None)
                if opp_val == self:
                    setattr(old_value, "machine_Symbol37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Symbol37"):
                opp_val = getattr(value, "machine_Symbol37", None)
                setattr(value, "machine_Symbol37", self)

    @property
    def machine_Head(self):
        return self.__machine_Head

    @machine_Head.setter
    def machine_Head(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Head__machine_Head", None)
        self.__machine_Head = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Machine16"):
                opp_val = getattr(old_value, "machine_Machine16", None)
                if opp_val == self:
                    setattr(old_value, "machine_Machine16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Machine16"):
                opp_val = getattr(value, "machine_Machine16", None)
                setattr(value, "machine_Machine16", self)

class machine_Current:

    def __init__(self, name: str, machine_Current: "machine_Machine" = None, machine_Current18: "machine_State" = None):
        self.name = name
        self.machine_Current = machine_Current
        self.machine_Current18 = machine_Current18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def machine_Current18(self):
        return self.__machine_Current18

    @machine_Current18.setter
    def machine_Current18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Current__machine_Current18", None)
        self.__machine_Current18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_State19"):
                opp_val = getattr(old_value, "machine_State19", None)
                if opp_val == self:
                    setattr(old_value, "machine_State19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_State19"):
                opp_val = getattr(value, "machine_State19", None)
                setattr(value, "machine_State19", self)

    @property
    def machine_Current(self):
        return self.__machine_Current

    @machine_Current.setter
    def machine_Current(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Current__machine_Current", None)
        self.__machine_Current = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Machine8"):
                opp_val = getattr(old_value, "machine_Machine8", None)
                if opp_val == self:
                    setattr(old_value, "machine_Machine8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Machine8"):
                opp_val = getattr(value, "machine_Machine8", None)
                setattr(value, "machine_Machine8", self)

class machine_Final:

    def __init__(self, name: str, machine_Final: "machine_Machine" = None, machine_Final30: "machine_State" = None):
        self.name = name
        self.machine_Final = machine_Final
        self.machine_Final30 = machine_Final30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def machine_Final30(self):
        return self.__machine_Final30

    @machine_Final30.setter
    def machine_Final30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Final__machine_Final30", None)
        self.__machine_Final30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_State31"):
                opp_val = getattr(old_value, "machine_State31", None)
                if opp_val == self:
                    setattr(old_value, "machine_State31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_State31"):
                opp_val = getattr(value, "machine_State31", None)
                setattr(value, "machine_State31", self)

    @property
    def machine_Final(self):
        return self.__machine_Final

    @machine_Final.setter
    def machine_Final(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Final__machine_Final", None)
        self.__machine_Final = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Machine6"):
                opp_val = getattr(old_value, "machine_Machine6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Machine6"):
                opp_val = getattr(value, "machine_Machine6", None)
                if opp_val is None:
                    setattr(value, "machine_Machine6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class machine_TuringMachine:

    pass
class machine_Transition:

    def __init__(self, name: str, read: str, write: str, moveTo: str, machine_Transition2: "machine_State" = None, machine_Transition: "machine_State" = None, machine_Transition14: "machine_Machine" = None):
        self.name = name
        self.read = read
        self.write = write
        self.moveTo = moveTo
        self.machine_Transition2 = machine_Transition2
        self.machine_Transition = machine_Transition
        self.machine_Transition14 = machine_Transition14
        
    @property
    def write(self) -> str:
        return self.__write

    @write.setter
    def write(self, write: str):
        self.__write = write

    @property
    def moveTo(self) -> str:
        return self.__moveTo

    @moveTo.setter
    def moveTo(self, moveTo: str):
        self.__moveTo = moveTo

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def read(self) -> str:
        return self.__read

    @read.setter
    def read(self, read: str):
        self.__read = read

    @property
    def machine_Transition(self):
        return self.__machine_Transition

    @machine_Transition.setter
    def machine_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Transition__machine_Transition", None)
        self.__machine_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_State"):
                opp_val = getattr(old_value, "machine_State", None)
                if opp_val == self:
                    setattr(old_value, "machine_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_State"):
                opp_val = getattr(value, "machine_State", None)
                setattr(value, "machine_State", self)

    @property
    def machine_Transition14(self):
        return self.__machine_Transition14

    @machine_Transition14.setter
    def machine_Transition14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Transition__machine_Transition14", None)
        self.__machine_Transition14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Machine13"):
                opp_val = getattr(old_value, "machine_Machine13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Machine13"):
                opp_val = getattr(value, "machine_Machine13", None)
                if opp_val is None:
                    setattr(value, "machine_Machine13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def machine_Transition2(self):
        return self.__machine_Transition2

    @machine_Transition2.setter
    def machine_Transition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Transition__machine_Transition2", None)
        self.__machine_Transition2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_State3"):
                opp_val = getattr(old_value, "machine_State3", None)
                if opp_val == self:
                    setattr(old_value, "machine_State3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_State3"):
                opp_val = getattr(value, "machine_State3", None)
                setattr(value, "machine_State3", self)

class machine_State:

    def __init__(self, name: str, machine_State: "machine_Transition" = None, machine_State3: "machine_Transition" = None, machine_State11: "machine_Machine" = None, machine_State19: "machine_Current" = None, machine_State22: "machine_Initial" = None, machine_State31: "machine_Final" = None):
        self.name = name
        self.machine_State = machine_State
        self.machine_State3 = machine_State3
        self.machine_State11 = machine_State11
        self.machine_State19 = machine_State19
        self.machine_State22 = machine_State22
        self.machine_State31 = machine_State31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def machine_State22(self):
        return self.__machine_State22

    @machine_State22.setter
    def machine_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_State__machine_State22", None)
        self.__machine_State22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Initial21"):
                opp_val = getattr(old_value, "machine_Initial21", None)
                if opp_val == self:
                    setattr(old_value, "machine_Initial21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Initial21"):
                opp_val = getattr(value, "machine_Initial21", None)
                setattr(value, "machine_Initial21", self)

    @property
    def machine_State3(self):
        return self.__machine_State3

    @machine_State3.setter
    def machine_State3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_State__machine_State3", None)
        self.__machine_State3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Transition2"):
                opp_val = getattr(old_value, "machine_Transition2", None)
                if opp_val == self:
                    setattr(old_value, "machine_Transition2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Transition2"):
                opp_val = getattr(value, "machine_Transition2", None)
                setattr(value, "machine_Transition2", self)

    @property
    def machine_State(self):
        return self.__machine_State

    @machine_State.setter
    def machine_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_State__machine_State", None)
        self.__machine_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Transition"):
                opp_val = getattr(old_value, "machine_Transition", None)
                if opp_val == self:
                    setattr(old_value, "machine_Transition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Transition"):
                opp_val = getattr(value, "machine_Transition", None)
                setattr(value, "machine_Transition", self)

    @property
    def machine_State11(self):
        return self.__machine_State11

    @machine_State11.setter
    def machine_State11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_State__machine_State11", None)
        self.__machine_State11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Machine10"):
                opp_val = getattr(old_value, "machine_Machine10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Machine10"):
                opp_val = getattr(value, "machine_Machine10", None)
                if opp_val is None:
                    setattr(value, "machine_Machine10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def machine_State31(self):
        return self.__machine_State31

    @machine_State31.setter
    def machine_State31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_State__machine_State31", None)
        self.__machine_State31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Final30"):
                opp_val = getattr(old_value, "machine_Final30", None)
                if opp_val == self:
                    setattr(old_value, "machine_Final30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Final30"):
                opp_val = getattr(value, "machine_Final30", None)
                setattr(value, "machine_Final30", self)

    @property
    def machine_State19(self):
        return self.__machine_State19

    @machine_State19.setter
    def machine_State19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_State__machine_State19", None)
        self.__machine_State19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Current18"):
                opp_val = getattr(old_value, "machine_Current18", None)
                if opp_val == self:
                    setattr(old_value, "machine_Current18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Current18"):
                opp_val = getattr(value, "machine_Current18", None)
                setattr(value, "machine_Current18", self)

class machine_Initial:

    def __init__(self, name: str, machine_Initial: "machine_Machine" = None, machine_Initial21: "machine_State" = None):
        self.name = name
        self.machine_Initial = machine_Initial
        self.machine_Initial21 = machine_Initial21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def machine_Initial21(self):
        return self.__machine_Initial21

    @machine_Initial21.setter
    def machine_Initial21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Initial__machine_Initial21", None)
        self.__machine_Initial21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_State22"):
                opp_val = getattr(old_value, "machine_State22", None)
                if opp_val == self:
                    setattr(old_value, "machine_State22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_State22"):
                opp_val = getattr(value, "machine_State22", None)
                setattr(value, "machine_State22", self)

    @property
    def machine_Initial(self):
        return self.__machine_Initial

    @machine_Initial.setter
    def machine_Initial(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_machine_Initial__machine_Initial", None)
        self.__machine_Initial = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "machine_Machine"):
                opp_val = getattr(old_value, "machine_Machine", None)
                if opp_val == self:
                    setattr(old_value, "machine_Machine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "machine_Machine"):
                opp_val = getattr(value, "machine_Machine", None)
                setattr(value, "machine_Machine", self)

class machine_Machine:

    pass