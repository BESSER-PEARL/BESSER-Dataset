from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

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
            if hasattr(old_value, "pycom_LogicExp55"):
                opp_val = getattr(old_value, "pycom_LogicExp55", None)
                if opp_val == self:
                    setattr(old_value, "pycom_LogicExp55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_LogicExp55"):
                opp_val = getattr(value, "pycom_LogicExp55", None)
                setattr(value, "pycom_LogicExp55", self)

class pycom_LogicExp:

    pass
class pycom_Expression:

    def __init__(self, outputValue: int, pycom_Expression: "pycom_ComparisonExp" = None, pycom_Expression62: "pycom_ComparisonExp" = None, pycom_Expression64: "pycom_Function" = None):
        self.outputValue = outputValue
        self.pycom_Expression = pycom_Expression
        self.pycom_Expression62 = pycom_Expression62
        self.pycom_Expression64 = pycom_Expression64
        
    @property
    def outputValue(self) -> int:
        return self.__outputValue

    @outputValue.setter
    def outputValue(self, outputValue: int):
        self.__outputValue = outputValue

    @property
    def pycom_Expression64(self):
        return self.__pycom_Expression64

    @pycom_Expression64.setter
    def pycom_Expression64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Expression__pycom_Expression64", None)
        self.__pycom_Expression64 = value
        
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
    def pycom_Expression62(self):
        return self.__pycom_Expression62

    @pycom_Expression62.setter
    def pycom_Expression62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Expression__pycom_Expression62", None)
        self.__pycom_Expression62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_ComparisonExp61"):
                opp_val = getattr(old_value, "pycom_ComparisonExp61", None)
                if opp_val == self:
                    setattr(old_value, "pycom_ComparisonExp61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_ComparisonExp61"):
                opp_val = getattr(value, "pycom_ComparisonExp61", None)
                setattr(value, "pycom_ComparisonExp61", self)

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
            if hasattr(old_value, "pycom_ComparisonExp59"):
                opp_val = getattr(old_value, "pycom_ComparisonExp59", None)
                if opp_val == self:
                    setattr(old_value, "pycom_ComparisonExp59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_ComparisonExp59"):
                opp_val = getattr(value, "pycom_ComparisonExp59", None)
                setattr(value, "pycom_ComparisonExp59", self)

class pycom_ComparisonExp:

    def __init__(self, op: str, pycom_ComparisonExp: "pycom_LogicExp" = None, pycom_ComparisonExp59: "pycom_Expression" = None, pycom_ComparisonExp61: "pycom_Expression" = None):
        self.op = op
        self.pycom_ComparisonExp = pycom_ComparisonExp
        self.pycom_ComparisonExp59 = pycom_ComparisonExp59
        self.pycom_ComparisonExp61 = pycom_ComparisonExp61
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def pycom_ComparisonExp59(self):
        return self.__pycom_ComparisonExp59

    @pycom_ComparisonExp59.setter
    def pycom_ComparisonExp59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ComparisonExp__pycom_ComparisonExp59", None)
        self.__pycom_ComparisonExp59 = value
        
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
            if hasattr(old_value, "pycom_LogicExp57"):
                opp_val = getattr(old_value, "pycom_LogicExp57", None)
                if opp_val == self:
                    setattr(old_value, "pycom_LogicExp57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_LogicExp57"):
                opp_val = getattr(value, "pycom_LogicExp57", None)
                setattr(value, "pycom_LogicExp57", self)

    @property
    def pycom_ComparisonExp61(self):
        return self.__pycom_ComparisonExp61

    @pycom_ComparisonExp61.setter
    def pycom_ComparisonExp61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ComparisonExp__pycom_ComparisonExp61", None)
        self.__pycom_ComparisonExp61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Expression62"):
                opp_val = getattr(old_value, "pycom_Expression62", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Expression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Expression62"):
                opp_val = getattr(value, "pycom_Expression62", None)
                setattr(value, "pycom_Expression62", self)

class pycom_CommunicationType:

    def __init__(self, name: str, ssid: str, password: str, pycom_CommunicationType: "pycom_Communication" = None):
        self.name = name
        self.ssid = ssid
        self.password = password
        self.pycom_CommunicationType = pycom_CommunicationType
        
    @property
    def ssid(self) -> str:
        return self.__ssid

    @ssid.setter
    def ssid(self, ssid: str):
        self.__ssid = ssid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def pycom_CommunicationType(self):
        return self.__pycom_CommunicationType

    @pycom_CommunicationType.setter
    def pycom_CommunicationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_CommunicationType__pycom_CommunicationType", None)
        self.__pycom_CommunicationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Communication"):
                opp_val = getattr(old_value, "pycom_Communication", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Communication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Communication"):
                opp_val = getattr(value, "pycom_Communication", None)
                setattr(value, "pycom_Communication", self)

class pycom_PinName:

    def __init__(self, name: str, pycom_PinName: "pycom_Pin" = None, pycom_PinName48: "pycom_Pin" = None):
        self.name = name
        self.pycom_PinName = pycom_PinName
        self.pycom_PinName48 = pycom_PinName48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pycom_PinName48(self):
        return self.__pycom_PinName48

    @pycom_PinName48.setter
    def pycom_PinName48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_PinName__pycom_PinName48", None)
        self.__pycom_PinName48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Pin47"):
                opp_val = getattr(old_value, "pycom_Pin47", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Pin47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Pin47"):
                opp_val = getattr(value, "pycom_Pin47", None)
                setattr(value, "pycom_Pin47", self)

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
            if hasattr(old_value, "pycom_Pin45"):
                opp_val = getattr(old_value, "pycom_Pin45", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Pin45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Pin45"):
                opp_val = getattr(value, "pycom_Pin45", None)
                setattr(value, "pycom_Pin45", self)

class pycom_ExpMember:

    pass
class pycom_Condition:

    def __init__(self, operator: str, pycom_Condition: "pycom_ConditionalAction" = None, pycom_Condition50: "pycom_LogicExp" = None, pycom_Condition53: "pycom_Condition" = None, pycom_Condition51: "pycom_Condition" = None):
        self.operator = operator
        self.pycom_Condition = pycom_Condition
        self.pycom_Condition50 = pycom_Condition50
        self.pycom_Condition53 = pycom_Condition53
        self.pycom_Condition51 = pycom_Condition51
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

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
            if hasattr(old_value, "pycom_ConditionalAction26"):
                opp_val = getattr(old_value, "pycom_ConditionalAction26", None)
                if opp_val == self:
                    setattr(old_value, "pycom_ConditionalAction26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_ConditionalAction26"):
                opp_val = getattr(value, "pycom_ConditionalAction26", None)
                setattr(value, "pycom_ConditionalAction26", self)

    @property
    def pycom_Condition51(self):
        return self.__pycom_Condition51

    @pycom_Condition51.setter
    def pycom_Condition51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Condition__pycom_Condition51", None)
        self.__pycom_Condition51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Condition53"):
                opp_val = getattr(old_value, "pycom_Condition53", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Condition53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Condition53"):
                opp_val = getattr(value, "pycom_Condition53", None)
                setattr(value, "pycom_Condition53", self)

    @property
    def pycom_Condition50(self):
        return self.__pycom_Condition50

    @pycom_Condition50.setter
    def pycom_Condition50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Condition__pycom_Condition50", None)
        self.__pycom_Condition50 = value
        
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

    @property
    def pycom_Condition53(self):
        return self.__pycom_Condition53

    @pycom_Condition53.setter
    def pycom_Condition53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Condition__pycom_Condition53", None)
        self.__pycom_Condition53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Condition51"):
                opp_val = getattr(old_value, "pycom_Condition51", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Condition51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Condition51"):
                opp_val = getattr(value, "pycom_Condition51", None)
                setattr(value, "pycom_Condition51", self)

class ExpMember:

    pass
class pycom_Function(ExpMember):

    pass
class pycom_Sensor:

    pass
class BoardMember:

    pass
class pycom_Communication(BoardMember):

    pass
class pycom_Actuator(BoardMember):

    pass
class pycom_Pin:

    pass
class pycom_ModuleName:

    def __init__(self, name: str, pycom_ModuleName: "pycom_Sensor" = None, pycom_ModuleName39: "pycom_Actuator" = None):
        self.name = name
        self.pycom_ModuleName = pycom_ModuleName
        self.pycom_ModuleName39 = pycom_ModuleName39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pycom_ModuleName39(self):
        return self.__pycom_ModuleName39

    @pycom_ModuleName39.setter
    def pycom_ModuleName39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ModuleName__pycom_ModuleName39", None)
        self.__pycom_ModuleName39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Actuator38"):
                opp_val = getattr(old_value, "pycom_Actuator38", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Actuator38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Actuator38"):
                opp_val = getattr(value, "pycom_Actuator38", None)
                setattr(value, "pycom_Actuator38", self)

    @property
    def pycom_ModuleName(self):
        return self.__pycom_ModuleName

    @pycom_ModuleName.setter
    def pycom_ModuleName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ModuleName__pycom_ModuleName", None)
        self.__pycom_ModuleName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Sensor32"):
                opp_val = getattr(old_value, "pycom_Sensor32", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Sensor32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Sensor32"):
                opp_val = getattr(value, "pycom_Sensor32", None)
                setattr(value, "pycom_Sensor32", self)

class pycom_ModuleType:

    def __init__(self, name: str, pycom_ModuleType: "pycom_Sensor" = None, pycom_ModuleType36: "pycom_Actuator" = None):
        self.name = name
        self.pycom_ModuleType = pycom_ModuleType
        self.pycom_ModuleType36 = pycom_ModuleType36
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pycom_ModuleType36(self):
        return self.__pycom_ModuleType36

    @pycom_ModuleType36.setter
    def pycom_ModuleType36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ModuleType__pycom_ModuleType36", None)
        self.__pycom_ModuleType36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Actuator"):
                opp_val = getattr(old_value, "pycom_Actuator", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Actuator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Actuator"):
                opp_val = getattr(value, "pycom_Actuator", None)
                setattr(value, "pycom_Actuator", self)

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
            if hasattr(old_value, "pycom_Sensor30"):
                opp_val = getattr(old_value, "pycom_Sensor30", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Sensor30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Sensor30"):
                opp_val = getattr(value, "pycom_Sensor30", None)
                setattr(value, "pycom_Sensor30", self)

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
            if hasattr(old_value, "pycom_Connection17"):
                opp_val = getattr(old_value, "pycom_Connection17", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Connection17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Connection17"):
                opp_val = getattr(value, "pycom_Connection17", None)
                setattr(value, "pycom_Connection17", self)

class pycom_ConditionalAction(ExpMember):

    def __init__(self, type: str, pycom_ConditionalAction: "pycom_Server" = None, pycom_ConditionalAction26: "pycom_Condition" = None, pycom_ConditionalAction28: set["pycom_ExpMember"] = None):
        self.type = type
        self.pycom_ConditionalAction = pycom_ConditionalAction
        self.pycom_ConditionalAction26 = pycom_ConditionalAction26
        self.pycom_ConditionalAction28 = pycom_ConditionalAction28 if pycom_ConditionalAction28 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def pycom_ConditionalAction26(self):
        return self.__pycom_ConditionalAction26

    @pycom_ConditionalAction26.setter
    def pycom_ConditionalAction26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ConditionalAction__pycom_ConditionalAction26", None)
        self.__pycom_ConditionalAction26 = value
        
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
            if hasattr(old_value, "pycom_Server15"):
                opp_val = getattr(old_value, "pycom_Server15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Server15"):
                opp_val = getattr(value, "pycom_Server15", None)
                if opp_val is None:
                    setattr(value, "pycom_Server15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pycom_ConditionalAction28(self):
        return self.__pycom_ConditionalAction28

    @pycom_ConditionalAction28.setter
    def pycom_ConditionalAction28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ConditionalAction__pycom_ConditionalAction28", None)
        self.__pycom_ConditionalAction28 = value if value is not None else set()
        
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

    def __init__(self, portnumber: int, pycom_Connection: "pycom_Server" = None, pycom_Connection17: "pycom_Host" = None):
        self.portnumber = portnumber
        self.pycom_Connection = pycom_Connection
        self.pycom_Connection17 = pycom_Connection17
        
    @property
    def portnumber(self) -> int:
        return self.__portnumber

    @portnumber.setter
    def portnumber(self, portnumber: int):
        self.__portnumber = portnumber

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
            if hasattr(old_value, "pycom_Server13"):
                opp_val = getattr(old_value, "pycom_Server13", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Server13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Server13"):
                opp_val = getattr(value, "pycom_Server13", None)
                setattr(value, "pycom_Server13", self)

    @property
    def pycom_Connection17(self):
        return self.__pycom_Connection17

    @pycom_Connection17.setter
    def pycom_Connection17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Connection__pycom_Connection17", None)
        self.__pycom_Connection17 = value
        
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

class pycom_BoardMember:

    pass
class pycom_Server:

    def __init__(self, name: str, pycom_Server: "pycom_System" = None, pycom_Server13: "pycom_Connection" = None, pycom_Server15: set["pycom_ConditionalAction"] = None):
        self.name = name
        self.pycom_Server = pycom_Server
        self.pycom_Server13 = pycom_Server13
        self.pycom_Server15 = pycom_Server15 if pycom_Server15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "pycom_System6"):
                opp_val = getattr(old_value, "pycom_System6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_System6"):
                opp_val = getattr(value, "pycom_System6", None)
                if opp_val is None:
                    setattr(value, "pycom_System6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pycom_Server15(self):
        return self.__pycom_Server15

    @pycom_Server15.setter
    def pycom_Server15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Server__pycom_Server15", None)
        self.__pycom_Server15 = value if value is not None else set()
        
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
    def pycom_Server13(self):
        return self.__pycom_Server13

    @pycom_Server13.setter
    def pycom_Server13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Server__pycom_Server13", None)
        self.__pycom_Server13 = value
        
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

    def __init__(self, name: str, boardType: str, communicationRate: int, pycom_Board: "pycom_System" = None, pycom_Board19: set["pycom_Library"] = None, pycom_Board22: set["pycom_BoardMember"] = None, pycom_Board67: "pycom_Function" = None):
        self.name = name
        self.boardType = boardType
        self.communicationRate = communicationRate
        self.pycom_Board = pycom_Board
        self.pycom_Board19 = pycom_Board19 if pycom_Board19 is not None else set()
        self.pycom_Board22 = pycom_Board22 if pycom_Board22 is not None else set()
        self.pycom_Board67 = pycom_Board67
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def communicationRate(self) -> int:
        return self.__communicationRate

    @communicationRate.setter
    def communicationRate(self, communicationRate: int):
        self.__communicationRate = communicationRate

    @property
    def boardType(self) -> str:
        return self.__boardType

    @boardType.setter
    def boardType(self, boardType: str):
        self.__boardType = boardType

    @property
    def pycom_Board22(self):
        return self.__pycom_Board22

    @pycom_Board22.setter
    def pycom_Board22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Board__pycom_Board22", None)
        self.__pycom_Board22 = value if value is not None else set()
        
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
    def pycom_Board19(self):
        return self.__pycom_Board19

    @pycom_Board19.setter
    def pycom_Board19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Board__pycom_Board19", None)
        self.__pycom_Board19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pycom_Library20"):
                    opp_val = getattr(item, "pycom_Library20", None)
                    
                    if opp_val == self:
                        setattr(item, "pycom_Library20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pycom_Library20"):
                    opp_val = getattr(item, "pycom_Library20", None)
                    
                    setattr(item, "pycom_Library20", self)
                    

    @property
    def pycom_Board67(self):
        return self.__pycom_Board67

    @pycom_Board67.setter
    def pycom_Board67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Board__pycom_Board67", None)
        self.__pycom_Board67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Function66"):
                opp_val = getattr(old_value, "pycom_Function66", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Function66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Function66"):
                opp_val = getattr(value, "pycom_Function66", None)
                setattr(value, "pycom_Function66", self)

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
            if hasattr(old_value, "pycom_System4"):
                opp_val = getattr(old_value, "pycom_System4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_System4"):
                opp_val = getattr(value, "pycom_System4", None)
                if opp_val is None:
                    setattr(value, "pycom_System4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pycom_Import:

    def __init__(self, name: str, path: str, pycom_Import9: "pycom_Library" = None, pycom_Import11: set["pycom_ParameterType"] = None, pycom_Import: "pycom_System" = None, pycom_Import70: "pycom_Function" = None):
        self.name = name
        self.path = path
        self.pycom_Import9 = pycom_Import9
        self.pycom_Import11 = pycom_Import11 if pycom_Import11 is not None else set()
        self.pycom_Import = pycom_Import
        self.pycom_Import70 = pycom_Import70
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def pycom_Import(self):
        return self.__pycom_Import

    @pycom_Import.setter
    def pycom_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Import__pycom_Import", None)
        self.__pycom_Import = value
        
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
    def pycom_Import11(self):
        return self.__pycom_Import11

    @pycom_Import11.setter
    def pycom_Import11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Import__pycom_Import11", None)
        self.__pycom_Import11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pycom_ParameterType"):
                    opp_val = getattr(item, "pycom_ParameterType", None)
                    
                    if opp_val == self:
                        setattr(item, "pycom_ParameterType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pycom_ParameterType"):
                    opp_val = getattr(item, "pycom_ParameterType", None)
                    
                    setattr(item, "pycom_ParameterType", self)
                    

    @property
    def pycom_Import70(self):
        return self.__pycom_Import70

    @pycom_Import70.setter
    def pycom_Import70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Import__pycom_Import70", None)
        self.__pycom_Import70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Function69"):
                opp_val = getattr(old_value, "pycom_Function69", None)
                if opp_val == self:
                    setattr(old_value, "pycom_Function69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Function69"):
                opp_val = getattr(value, "pycom_Function69", None)
                setattr(value, "pycom_Function69", self)

    @property
    def pycom_Import9(self):
        return self.__pycom_Import9

    @pycom_Import9.setter
    def pycom_Import9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Import__pycom_Import9", None)
        self.__pycom_Import9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Library8"):
                opp_val = getattr(old_value, "pycom_Library8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Library8"):
                opp_val = getattr(value, "pycom_Library8", None)
                if opp_val is None:
                    setattr(value, "pycom_Library8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pycom_Library:

    def __init__(self, name: str, pycom_Library8: set["pycom_Import"] = None, pycom_Library: "pycom_System" = None, pycom_Library20: "pycom_Board" = None):
        self.name = name
        self.pycom_Library8 = pycom_Library8 if pycom_Library8 is not None else set()
        self.pycom_Library = pycom_Library
        self.pycom_Library20 = pycom_Library20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pycom_Library8(self):
        return self.__pycom_Library8

    @pycom_Library8.setter
    def pycom_Library8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Library__pycom_Library8", None)
        self.__pycom_Library8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pycom_Import9"):
                    opp_val = getattr(item, "pycom_Import9", None)
                    
                    if opp_val == self:
                        setattr(item, "pycom_Import9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pycom_Import9"):
                    opp_val = getattr(item, "pycom_Import9", None)
                    
                    setattr(item, "pycom_Import9", self)
                    

    @property
    def pycom_Library20(self):
        return self.__pycom_Library20

    @pycom_Library20.setter
    def pycom_Library20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Library__pycom_Library20", None)
        self.__pycom_Library20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Board19"):
                opp_val = getattr(old_value, "pycom_Board19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Board19"):
                opp_val = getattr(value, "pycom_Board19", None)
                if opp_val is None:
                    setattr(value, "pycom_Board19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pycom_Library(self):
        return self.__pycom_Library

    @pycom_Library.setter
    def pycom_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_Library__pycom_Library", None)
        self.__pycom_Library = value
        
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

class pycom_ParameterType:

    def __init__(self, number: int, text: str, pycom_ParameterType: "pycom_Import" = None):
        self.number = number
        self.text = text
        self.pycom_ParameterType = pycom_ParameterType
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def pycom_ParameterType(self):
        return self.__pycom_ParameterType

    @pycom_ParameterType.setter
    def pycom_ParameterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pycom_ParameterType__pycom_ParameterType", None)
        self.__pycom_ParameterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pycom_Import11"):
                opp_val = getattr(old_value, "pycom_Import11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pycom_Import11"):
                opp_val = getattr(value, "pycom_Import11", None)
                if opp_val is None:
                    setattr(value, "pycom_Import11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pycom_System:

    pass