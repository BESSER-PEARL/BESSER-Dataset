from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pycom_Expression:

    def __init__(self, outputValue: int, pycom_Expression40: "pycom_Function" = None, pycom_Expression: "pycom_ComparisonExp" = None, pycom_Expression38: "pycom_ComparisonExp" = None):
        self.outputValue = outputValue
        self.pycom_Expression40 = pycom_Expression40
        self.pycom_Expression = pycom_Expression
        self.pycom_Expression38 = pycom_Expression38
        
    @property
    def outputValue(self) -> int:
        return self.__outputValue

    @outputValue.setter
    def outputValue(self, outputValue: int):
        self.__outputValue = outputValue

    @property
    def pycom_Expression38(self):
        return self.__pycom_Expression38

    @pycom_Expression38.setter
    def pycom_Expression38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Expression__pycom_Expression38", None)
        self.__pycom_Expression38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_ComparisonExp37"):
                opp_val = getattr(old_value, "pycom_ComparisonExp37", None)
                if opp_val == self:
                    setattr(old_value, "pycom_ComparisonExp37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_ComparisonExp37"):
                opp_val = getattr(value, "pycom_ComparisonExp37", None)
                setattr(value, "pycom_ComparisonExp37", self)

    @property
    def pycom_Expression40(self):
        return self.__pycom_Expression40

    @pycom_Expression40.setter
    def pycom_Expression40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Expression__pycom_Expression40", None)
        self.__pycom_Expression40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Function"):
                opp_val = getattr(old_value, "pycom_Function", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Function"):
                opp_val = getattr(value, "pycom_Function", None)
                setattr(value, "pycom_Function", self)

    @property
    def pycom_Expression(self):
        return self.__pycom_Expression

    @pycom_Expression.setter
    def pycom_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Expression__pycom_Expression", None)
        self.__pycom_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_ComparisonExp35"):
                opp_val = getattr(old_value, "pycom_ComparisonExp35", None)
                if opp_val == self:
                    setattr(old_value, "pycom_ComparisonExp35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_ComparisonExp35"):
                opp_val = getattr(value, "pycom_ComparisonExp35", None)
                setattr(value, "pycom_ComparisonExp35", self)

class pycom_ComparisonExp:

    def __init__(self, op: str, pycom_ComparisonExp: "pycom_LogicExp" = None, pycom_ComparisonExp35: "pycom_Expression" = None, pycom_ComparisonExp37: "pycom_Expression" = None):
        self.op = op
        self.pycom_ComparisonExp = pycom_ComparisonExp
        self.pycom_ComparisonExp35 = pycom_ComparisonExp35
        self.pycom_ComparisonExp37 = pycom_ComparisonExp37
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def pycom_ComparisonExp37(self):
        return self.__pycom_ComparisonExp37

    @pycom_ComparisonExp37.setter
    def pycom_ComparisonExp37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ComparisonExp__pycom_ComparisonExp37", None)
        self.__pycom_ComparisonExp37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Expression38"):
                opp_val = getattr(old_value, "pycom_Expression38", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Expression38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Expression38"):
                opp_val = getattr(value, "pycom_Expression38", None)
                setattr(value, "pycom_Expression38", self)

    @property
    def pycom_ComparisonExp(self):
        return self.__pycom_ComparisonExp

    @pycom_ComparisonExp.setter
    def pycom_ComparisonExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ComparisonExp__pycom_ComparisonExp", None)
        self.__pycom_ComparisonExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_LogicExp33"):
                opp_val = getattr(old_value, "pycom_LogicExp33", None)
                if opp_val == self:
                    setattr(old_value, "pycom_LogicExp33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_LogicExp33"):
                opp_val = getattr(value, "pycom_LogicExp33", None)
                setattr(value, "pycom_LogicExp33", self)

    @property
    def pycom_ComparisonExp35(self):
        return self.__pycom_ComparisonExp35

    @pycom_ComparisonExp35.setter
    def pycom_ComparisonExp35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ComparisonExp__pycom_ComparisonExp35", None)
        self.__pycom_ComparisonExp35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Expression"):
                opp_val = getattr(old_value, "pycom_Expression", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Expression"):
                opp_val = getattr(value, "pycom_Expression", None)
                setattr(value, "pycom_Expression", self)

class pycom_Boolean:

    def __init__(self, value: str, pycom_Boolean: "pycom_LogicExp" = None):
        self.value = value
        self.pycom_Boolean = pycom_Boolean
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def pycom_Boolean(self):
        return self.__pycom_Boolean

    @pycom_Boolean.setter
    def pycom_Boolean(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Boolean__pycom_Boolean", None)
        self.__pycom_Boolean = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_LogicExp31"):
                opp_val = getattr(old_value, "pycom_LogicExp31", None)
                if opp_val == self:
                    setattr(old_value, "pycom_LogicExp31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_LogicExp31"):
                opp_val = getattr(value, "pycom_LogicExp31", None)
                setattr(value, "pycom_LogicExp31", self)

class pycom_LogicExp:

    pass
class ModuleType:

    pass
class pycom_SensorType(ModuleType):

    pass
class pycom_ActuatorType(ModuleType):

    pass
class Function:

    pass
class pycom_ModuleFunction(Function):

    pass
class pycom_FunctionName:

    def __init__(self, name: str, pycom_FunctionName: "pycom_Function" = None):
        self.name = name
        self.pycom_FunctionName = pycom_FunctionName
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pycom_FunctionName(self):
        return self.__pycom_FunctionName

    @pycom_FunctionName.setter
    def pycom_FunctionName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_FunctionName__pycom_FunctionName", None)
        self.__pycom_FunctionName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Function45"):
                opp_val = getattr(old_value, "pycom_Function45", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Function45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Function45"):
                opp_val = getattr(value, "pycom_Function45", None)
                setattr(value, "pycom_Function45", self)

class pycom_ModuleType:

    def __init__(self, typeName: str, name: str, pycom_ModuleType: "pycom_Sensor" = None, pycom_ModuleType17: "pycom_Actuator" = None, pycom_ModuleType19: "pycom_Pin" = None, pycom_ModuleType47: "pycom_ModuleFunction" = None):
        self.typeName = typeName
        self.name = name
        self.pycom_ModuleType = pycom_ModuleType
        self.pycom_ModuleType17 = pycom_ModuleType17
        self.pycom_ModuleType19 = pycom_ModuleType19
        self.pycom_ModuleType47 = pycom_ModuleType47
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pycom_ModuleType17(self):
        return self.__pycom_ModuleType17

    @pycom_ModuleType17.setter
    def pycom_ModuleType17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ModuleType__pycom_ModuleType17", None)
        self.__pycom_ModuleType17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Actuator"):
                opp_val = getattr(old_value, "pycom_Actuator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Actuator"):
                opp_val = getattr(value, "pycom_Actuator", None)
                if opp_val is None:
                    setattr(value, "pycom_Actuator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pycom_ModuleType19(self):
        return self.__pycom_ModuleType19

    @pycom_ModuleType19.setter
    def pycom_ModuleType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ModuleType__pycom_ModuleType19", None)
        self.__pycom_ModuleType19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Pin"):
                opp_val = getattr(old_value, "pycom_Pin", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Pin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Pin"):
                opp_val = getattr(value, "pycom_Pin", None)
                setattr(value, "pycom_Pin", self)

    @property
    def pycom_ModuleType(self):
        return self.__pycom_ModuleType

    @pycom_ModuleType.setter
    def pycom_ModuleType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ModuleType__pycom_ModuleType", None)
        self.__pycom_ModuleType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Sensor"):
                opp_val = getattr(old_value, "pycom_Sensor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Sensor"):
                opp_val = getattr(value, "pycom_Sensor", None)
                if opp_val is None:
                    setattr(value, "pycom_Sensor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pycom_ModuleType47(self):
        return self.__pycom_ModuleType47

    @pycom_ModuleType47.setter
    def pycom_ModuleType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ModuleType__pycom_ModuleType47", None)
        self.__pycom_ModuleType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_ModuleFunction"):
                opp_val = getattr(old_value, "pycom_ModuleFunction", None)
                if opp_val == self:
                    setattr(old_value, "pycom_ModuleFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_ModuleFunction"):
                opp_val = getattr(value, "pycom_ModuleFunction", None)
                setattr(value, "pycom_ModuleFunction", self)

class BoardMember:

    pass
class pycom_Sensor(BoardMember):

    pass
class pycom_ExpMember:

    pass
class pycom_Condition:

    def __init__(self, operator: str, pycom_Condition: "pycom_ConditionalAction" = None, pycom_Condition26: "pycom_LogicExp" = None, pycom_Condition29: "pycom_Condition" = None, pycom_Condition27: "pycom_Condition" = None):
        self.operator = operator
        self.pycom_Condition = pycom_Condition
        self.pycom_Condition26 = pycom_Condition26
        self.pycom_Condition29 = pycom_Condition29
        self.pycom_Condition27 = pycom_Condition27
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def pycom_Condition29(self):
        return self.__pycom_Condition29

    @pycom_Condition29.setter
    def pycom_Condition29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Condition__pycom_Condition29", None)
        self.__pycom_Condition29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Condition27"):
                opp_val = getattr(old_value, "pycom_Condition27", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Condition27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Condition27"):
                opp_val = getattr(value, "pycom_Condition27", None)
                setattr(value, "pycom_Condition27", self)

    @property
    def pycom_Condition(self):
        return self.__pycom_Condition

    @pycom_Condition.setter
    def pycom_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Condition__pycom_Condition", None)
        self.__pycom_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_ConditionalAction12"):
                opp_val = getattr(old_value, "pycom_ConditionalAction12", None)
                if opp_val == self:
                    setattr(old_value, "pycom_ConditionalAction12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_ConditionalAction12"):
                opp_val = getattr(value, "pycom_ConditionalAction12", None)
                setattr(value, "pycom_ConditionalAction12", self)

    @property
    def pycom_Condition27(self):
        return self.__pycom_Condition27

    @pycom_Condition27.setter
    def pycom_Condition27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Condition__pycom_Condition27", None)
        self.__pycom_Condition27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Condition29"):
                opp_val = getattr(old_value, "pycom_Condition29", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Condition29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Condition29"):
                opp_val = getattr(value, "pycom_Condition29", None)
                setattr(value, "pycom_Condition29", self)

    @property
    def pycom_Condition26(self):
        return self.__pycom_Condition26

    @pycom_Condition26.setter
    def pycom_Condition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Condition__pycom_Condition26", None)
        self.__pycom_Condition26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_LogicExp"):
                opp_val = getattr(old_value, "pycom_LogicExp", None)
                if opp_val == self:
                    setattr(old_value, "pycom_LogicExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_LogicExp"):
                opp_val = getattr(value, "pycom_LogicExp", None)
                setattr(value, "pycom_LogicExp", self)

class ExpMember:

    pass
class pycom_Function(ExpMember):

    pass
class pycom_BoardMember:

    pass
class pycom_Host:

    def __init__(self, ipAdr: str, website: str, pycom_Host: "pycom_Connection" = None):
        self.ipAdr = ipAdr
        self.website = website
        self.pycom_Host = pycom_Host
        
    @property
    def ipAdr(self) -> str:
        return self.__ipAdr

    @ipAdr.setter
    def ipAdr(self, ipAdr: str):
        self.__ipAdr = ipAdr

    @property
    def website(self) -> str:
        return self.__website

    @website.setter
    def website(self, website: str):
        self.__website = website

    @property
    def pycom_Host(self):
        return self.__pycom_Host

    @pycom_Host.setter
    def pycom_Host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Host__pycom_Host", None)
        self.__pycom_Host = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Connection8"):
                opp_val = getattr(old_value, "pycom_Connection8", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Connection8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Connection8"):
                opp_val = getattr(value, "pycom_Connection8", None)
                setattr(value, "pycom_Connection8", self)

class pycom_PinName:

    def __init__(self, name: str, pycom_PinName: "pycom_Pin" = None, pycom_PinName24: "pycom_Pin" = None):
        self.name = name
        self.pycom_PinName = pycom_PinName
        self.pycom_PinName24 = pycom_PinName24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pycom_PinName(self):
        return self.__pycom_PinName

    @pycom_PinName.setter
    def pycom_PinName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_PinName__pycom_PinName", None)
        self.__pycom_PinName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Pin21"):
                opp_val = getattr(old_value, "pycom_Pin21", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Pin21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Pin21"):
                opp_val = getattr(value, "pycom_Pin21", None)
                setattr(value, "pycom_Pin21", self)

    @property
    def pycom_PinName24(self):
        return self.__pycom_PinName24

    @pycom_PinName24.setter
    def pycom_PinName24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_PinName__pycom_PinName24", None)
        self.__pycom_PinName24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Pin23"):
                opp_val = getattr(old_value, "pycom_Pin23", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Pin23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Pin23"):
                opp_val = getattr(value, "pycom_Pin23", None)
                setattr(value, "pycom_Pin23", self)

class pycom_Pin:

    pass
class pycom_Communication(BoardMember):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class pycom_Actuator(BoardMember):

    pass
class pycom_ConditionalAction(ExpMember):

    def __init__(self, type: str, pycom_ConditionalAction: "pycom_Server" = None, pycom_ConditionalAction12: "pycom_Condition" = None, pycom_ConditionalAction14: set["pycom_ExpMember"] = None):
        self.type = type
        self.pycom_ConditionalAction = pycom_ConditionalAction
        self.pycom_ConditionalAction12 = pycom_ConditionalAction12
        self.pycom_ConditionalAction14 = pycom_ConditionalAction14 if pycom_ConditionalAction14 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def pycom_ConditionalAction12(self):
        return self.__pycom_ConditionalAction12

    @pycom_ConditionalAction12.setter
    def pycom_ConditionalAction12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ConditionalAction__pycom_ConditionalAction12", None)
        self.__pycom_ConditionalAction12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Condition"):
                opp_val = getattr(old_value, "pycom_Condition", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Condition"):
                opp_val = getattr(value, "pycom_Condition", None)
                setattr(value, "pycom_Condition", self)

    @property
    def pycom_ConditionalAction(self):
        return self.__pycom_ConditionalAction

    @pycom_ConditionalAction.setter
    def pycom_ConditionalAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ConditionalAction__pycom_ConditionalAction", None)
        self.__pycom_ConditionalAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Server6"):
                opp_val = getattr(old_value, "pycom_Server6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Server6"):
                opp_val = getattr(value, "pycom_Server6", None)
                if opp_val is None:
                    setattr(value, "pycom_Server6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pycom_ConditionalAction14(self):
        return self.__pycom_ConditionalAction14

    @pycom_ConditionalAction14.setter
    def pycom_ConditionalAction14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ConditionalAction__pycom_ConditionalAction14", None)
        self.__pycom_ConditionalAction14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pycom_ExpMember"):
                    opp_val = getattr(item, "pycom_ExpMember", None)
                    
                    if opp_val == self:
                        setattr(item, "pycom_ExpMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pycom_ExpMember"):
                    opp_val = getattr(item, "pycom_ExpMember", None)
                    
                    setattr(item, "pycom_ExpMember", self)
                    

class pycom_Connection:

    def __init__(self, portnumber: str, pycom_Connection: "pycom_Server" = None, pycom_Connection8: "pycom_Host" = None):
        self.portnumber = portnumber
        self.pycom_Connection = pycom_Connection
        self.pycom_Connection8 = pycom_Connection8
        
    @property
    def portnumber(self) -> str:
        return self.__portnumber

    @portnumber.setter
    def portnumber(self, portnumber: str):
        self.__portnumber = portnumber

    @property
    def pycom_Connection8(self):
        return self.__pycom_Connection8

    @pycom_Connection8.setter
    def pycom_Connection8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Connection__pycom_Connection8", None)
        self.__pycom_Connection8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Host"):
                opp_val = getattr(old_value, "pycom_Host", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Host", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Host"):
                opp_val = getattr(value, "pycom_Host", None)
                setattr(value, "pycom_Host", self)

    @property
    def pycom_Connection(self):
        return self.__pycom_Connection

    @pycom_Connection.setter
    def pycom_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Connection__pycom_Connection", None)
        self.__pycom_Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Server4"):
                opp_val = getattr(old_value, "pycom_Server4", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Server4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Server4"):
                opp_val = getattr(value, "pycom_Server4", None)
                setattr(value, "pycom_Server4", self)

class pycom_Server:

    def __init__(self, name: str, pycom_Server: "pycom_System" = None, pycom_Server4: "pycom_Connection" = None, pycom_Server6: set["pycom_ConditionalAction"] = None):
        self.name = name
        self.pycom_Server = pycom_Server
        self.pycom_Server4 = pycom_Server4
        self.pycom_Server6 = pycom_Server6 if pycom_Server6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pycom_Server6(self):
        return self.__pycom_Server6

    @pycom_Server6.setter
    def pycom_Server6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Server__pycom_Server6", None)
        self.__pycom_Server6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pycom_ConditionalAction"):
                    opp_val = getattr(item, "pycom_ConditionalAction", None)
                    
                    if opp_val == self:
                        setattr(item, "pycom_ConditionalAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pycom_ConditionalAction"):
                    opp_val = getattr(item, "pycom_ConditionalAction", None)
                    
                    setattr(item, "pycom_ConditionalAction", self)
                    

    @property
    def pycom_Server(self):
        return self.__pycom_Server

    @pycom_Server.setter
    def pycom_Server(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Server__pycom_Server", None)
        self.__pycom_Server = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_System2"):
                opp_val = getattr(old_value, "pycom_System2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_System2"):
                opp_val = getattr(value, "pycom_System2", None)
                if opp_val is None:
                    setattr(value, "pycom_System2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pycom_Server4(self):
        return self.__pycom_Server4

    @pycom_Server4.setter
    def pycom_Server4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Server__pycom_Server4", None)
        self.__pycom_Server4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Connection"):
                opp_val = getattr(old_value, "pycom_Connection", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Connection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Connection"):
                opp_val = getattr(value, "pycom_Connection", None)
                setattr(value, "pycom_Connection", self)

class pycom_Board:

    def __init__(self, name: str, pycom_Board: "pycom_System" = None, pycom_Board10: set["pycom_BoardMember"] = None, pycom_Board43: "pycom_Function" = None):
        self.name = name
        self.pycom_Board = pycom_Board
        self.pycom_Board10 = pycom_Board10 if pycom_Board10 is not None else set()
        self.pycom_Board43 = pycom_Board43
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pycom_Board10(self):
        return self.__pycom_Board10

    @pycom_Board10.setter
    def pycom_Board10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Board__pycom_Board10", None)
        self.__pycom_Board10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pycom_BoardMember"):
                    opp_val = getattr(item, "pycom_BoardMember", None)
                    
                    if opp_val == self:
                        setattr(item, "pycom_BoardMember", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pycom_BoardMember"):
                    opp_val = getattr(item, "pycom_BoardMember", None)
                    
                    setattr(item, "pycom_BoardMember", self)
                    

    @property
    def pycom_Board(self):
        return self.__pycom_Board

    @pycom_Board.setter
    def pycom_Board(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Board__pycom_Board", None)
        self.__pycom_Board = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_System"):
                opp_val = getattr(old_value, "pycom_System", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_System"):
                opp_val = getattr(value, "pycom_System", None)
                if opp_val is None:
                    setattr(value, "pycom_System", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pycom_Board43(self):
        return self.__pycom_Board43

    @pycom_Board43.setter
    def pycom_Board43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Board__pycom_Board43", None)
        self.__pycom_Board43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Function42"):
                opp_val = getattr(old_value, "pycom_Function42", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Function42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Function42"):
                opp_val = getattr(value, "pycom_Function42", None)
                setattr(value, "pycom_Function42", self)

class pycom_System:

    pass