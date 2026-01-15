from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Comparison:

    pass
class ioT_EQL(Comparison):

    pass
class ioT_ItemInt(Comparison):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class ioT_ItemVariable(Comparison):

    pass
class ioT_AND(Comparison):

    pass
class ioT_OR(Comparison):

    pass
class Bool:

    pass
class ioT_False(Bool):

    pass
class ioT_True(Bool):

    pass
class ComparisonOp:

    pass
class ioT_EQ(ComparisonOp):

    pass
class ioT_LE(ComparisonOp):

    pass
class ioT_LT(ComparisonOp):

    pass
class ioT_GE(ComparisonOp):

    pass
class ioT_NE(ComparisonOp):

    pass
class ioT_GT(ComparisonOp):

    pass
class ioT_ItemBool(Comparison):

    pass
class Action:

    pass
class ioT_LEDAction(Action):

    def __init__(self, state: str):
        self.state = state
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

class ioT_ClearListAction(Action):

    pass
class SENSOR:

    pass
class ioT_HUMIDITY(SENSOR):

    pass
class ioT_TEMPERATURE(SENSOR):

    pass
class ioT_LIGHTSENSOR(SENSOR):

    pass
class TIMEUNIT:

    pass
class ioT_HOURS(TIMEUNIT):

    pass
class ioT_DAYS(TIMEUNIT):

    pass
class ioT_MINUTES(TIMEUNIT):

    pass
class ioT_SECONDS(TIMEUNIT):

    pass
class ioT_WEEKS(TIMEUNIT):

    pass
class ioT_MILLISECONDS(TIMEUNIT):

    pass
class VarOrList:

    pass
class ioT_PyList(VarOrList):

    pass
class Address:

    pass
class ioT_UnixSerialAddress(Address):

    pass
class ioT_WindowsSerialAddress(Address):

    pass
class ioT_IpAddress(Address):

    pass
class Config:

    pass
class ioT_DeviceConfig(Config):

    pass
class ioT_ComparisonOp:

    def __init__(self, op: str, ioT_ComparisonOp: "ioT_EQL" = None):
        self.op = op
        self.ioT_ComparisonOp = ioT_ComparisonOp
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def ioT_ComparisonOp(self):
        return self.__ioT_ComparisonOp

    @ioT_ComparisonOp.setter
    def ioT_ComparisonOp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_ComparisonOp__ioT_ComparisonOp", None)
        self.__ioT_ComparisonOp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_EQL89"):
                opp_val = getattr(old_value, "ioT_EQL89", None)
                if opp_val == self:
                    setattr(old_value, "ioT_EQL89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_EQL89"):
                opp_val = getattr(value, "ioT_EQL89", None)
                setattr(value, "ioT_EQL89", self)

class ioT_Comparison:

    pass
class ioT_ElseBlock:

    pass
class ioT_Variable(VarOrList):

    pass
class ioT_Bool:

    pass
class Expression:

    pass
class ioT_IntExpression(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class ioT_VarAccess(Expression):

    pass
class ioT_BoolExpression(Expression):

    pass
class ExpressionLeft:

    pass
class ioT_ReadVariable(ExpressionLeft):

    pass
class ioT_ExpressionLeft:

    pass
class Command:

    pass
class ioT_IfStatement(Command):

    pass
class ioT_ArrowCommand(Command):

    pass
class ioT_Action(Command):

    pass
class ioT_Command:

    pass
class ioT_TIMEUNIT:

    pass
class ioT_Expression(ExpressionLeft):

    pass
class ExpressionRight:

    pass
class ioT_ExternalRight(ExpressionRight):

    pass
class ioT_SendCommand(ExpressionRight):

    pass
class ioT_AddToList(ExpressionRight):

    pass
class ioT_ToVar(ExpressionRight):

    pass
class ioT_Block(ExpressionRight):

    pass
class ioT_SENSOR:

    pass
class ioT_ReadSensor(ExpressionLeft):

    pass
class ioT_ExternalOf(ExpressionLeft):

    pass
class ioT_ReadConnection(ExpressionLeft):

    pass
class ioT_ListenStatement:

    def __init__(self, ip: str, port: int, ioT_ListenStatement20: "ioT_ExpressionRight" = None, ioT_ListenStatement: "ioT_Program" = None):
        self.ip = ip
        self.port = port
        self.ioT_ListenStatement20 = ioT_ListenStatement20
        self.ioT_ListenStatement = ioT_ListenStatement
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def ip(self) -> str:
        return self.__ip

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip

    @property
    def ioT_ListenStatement(self):
        return self.__ioT_ListenStatement

    @ioT_ListenStatement.setter
    def ioT_ListenStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_ListenStatement__ioT_ListenStatement", None)
        self.__ioT_ListenStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Program16"):
                opp_val = getattr(old_value, "ioT_Program16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Program16"):
                opp_val = getattr(value, "ioT_Program16", None)
                if opp_val is None:
                    setattr(value, "ioT_Program16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_ListenStatement20(self):
        return self.__ioT_ListenStatement20

    @ioT_ListenStatement20.setter
    def ioT_ListenStatement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_ListenStatement__ioT_ListenStatement20", None)
        self.__ioT_ListenStatement20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_ExpressionRight"):
                opp_val = getattr(old_value, "ioT_ExpressionRight", None)
                if opp_val == self:
                    setattr(old_value, "ioT_ExpressionRight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_ExpressionRight"):
                opp_val = getattr(value, "ioT_ExpressionRight", None)
                setattr(value, "ioT_ExpressionRight", self)

class ioT_VarOrList:

    def __init__(self, name: str, ioT_VarOrList: "ioT_Program" = None, ioT_VarOrList45: "ioT_ExternalOf" = None, ioT_VarOrList62: "ioT_VarAccess" = None):
        self.name = name
        self.ioT_VarOrList = ioT_VarOrList
        self.ioT_VarOrList45 = ioT_VarOrList45
        self.ioT_VarOrList62 = ioT_VarOrList62
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_VarOrList62(self):
        return self.__ioT_VarOrList62

    @ioT_VarOrList62.setter
    def ioT_VarOrList62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_VarOrList__ioT_VarOrList62", None)
        self.__ioT_VarOrList62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_VarAccess"):
                opp_val = getattr(old_value, "ioT_VarAccess", None)
                if opp_val == self:
                    setattr(old_value, "ioT_VarAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_VarAccess"):
                opp_val = getattr(value, "ioT_VarAccess", None)
                setattr(value, "ioT_VarAccess", self)

    @property
    def ioT_VarOrList45(self):
        return self.__ioT_VarOrList45

    @ioT_VarOrList45.setter
    def ioT_VarOrList45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_VarOrList__ioT_VarOrList45", None)
        self.__ioT_VarOrList45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_ExternalOf44"):
                opp_val = getattr(old_value, "ioT_ExternalOf44", None)
                if opp_val == self:
                    setattr(old_value, "ioT_ExternalOf44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_ExternalOf44"):
                opp_val = getattr(value, "ioT_ExternalOf44", None)
                setattr(value, "ioT_ExternalOf44", self)

    @property
    def ioT_VarOrList(self):
        return self.__ioT_VarOrList

    @ioT_VarOrList.setter
    def ioT_VarOrList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_VarOrList__ioT_VarOrList", None)
        self.__ioT_VarOrList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Program14"):
                opp_val = getattr(old_value, "ioT_Program14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Program14"):
                opp_val = getattr(value, "ioT_Program14", None)
                if opp_val is None:
                    setattr(value, "ioT_Program14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_ConnectStatement:

    pass
class ioT_WifiStatement:

    pass
class Device:

    pass
class ioT_IoTDevice(Device):

    pass
class ioT_ControllerDevice(Device):

    pass
class ioT_Program:

    pass
class ioT_Declaration:

    def __init__(self, key: str, value: str, ioT_Declaration: "ioT_Config" = None):
        self.key = key
        self.value = value
        self.ioT_Declaration = ioT_Declaration
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def ioT_Declaration(self):
        return self.__ioT_Declaration

    @ioT_Declaration.setter
    def ioT_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Declaration__ioT_Declaration", None)
        self.__ioT_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Config6"):
                opp_val = getattr(old_value, "ioT_Config6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Config6"):
                opp_val = getattr(value, "ioT_Config6", None)
                if opp_val is None:
                    setattr(value, "ioT_Config6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_Address:

    def __init__(self, value: str, ioT_Address: "ioT_ConnectStatement" = None):
        self.value = value
        self.ioT_Address = ioT_Address
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ioT_Address(self):
        return self.__ioT_Address

    @ioT_Address.setter
    def ioT_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Address__ioT_Address", None)
        self.__ioT_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_ConnectStatement27"):
                opp_val = getattr(old_value, "ioT_ConnectStatement27", None)
                if opp_val == self:
                    setattr(old_value, "ioT_ConnectStatement27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_ConnectStatement27"):
                opp_val = getattr(value, "ioT_ConnectStatement27", None)
                setattr(value, "ioT_ConnectStatement27", self)

class ioT_ConnectionConfig(Config):

    def __init__(self, type: str, ioT_ConnectionConfig: "ioT_WifiStatement" = None, ioT_ConnectionConfig30: "ioT_ConnectStatement" = None):
        self.type = type
        self.ioT_ConnectionConfig = ioT_ConnectionConfig
        self.ioT_ConnectionConfig30 = ioT_ConnectionConfig30
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ioT_ConnectionConfig30(self):
        return self.__ioT_ConnectionConfig30

    @ioT_ConnectionConfig30.setter
    def ioT_ConnectionConfig30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_ConnectionConfig__ioT_ConnectionConfig30", None)
        self.__ioT_ConnectionConfig30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_ConnectStatement29"):
                opp_val = getattr(old_value, "ioT_ConnectStatement29", None)
                if opp_val == self:
                    setattr(old_value, "ioT_ConnectStatement29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_ConnectStatement29"):
                opp_val = getattr(value, "ioT_ConnectStatement29", None)
                setattr(value, "ioT_ConnectStatement29", self)

    @property
    def ioT_ConnectionConfig(self):
        return self.__ioT_ConnectionConfig

    @ioT_ConnectionConfig.setter
    def ioT_ConnectionConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_ConnectionConfig__ioT_ConnectionConfig", None)
        self.__ioT_ConnectionConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_WifiStatement22"):
                opp_val = getattr(old_value, "ioT_WifiStatement22", None)
                if opp_val == self:
                    setattr(old_value, "ioT_WifiStatement22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_WifiStatement22"):
                opp_val = getattr(value, "ioT_WifiStatement22", None)
                setattr(value, "ioT_WifiStatement22", self)

class ioT_ExpressionRight:

    pass
class ioT_Loop:

    pass
class ioT_Device:

    def __init__(self, name: str, ioT_Device: "ioT_Model" = None, ioT_Device25: "ioT_ConnectStatement" = None, ioT_Device8: "ioT_Program" = None, ioT_Device40: "ioT_ReadConnection" = None, ioT_Device68: "ioT_SendCommand" = None):
        self.name = name
        self.ioT_Device = ioT_Device
        self.ioT_Device25 = ioT_Device25
        self.ioT_Device8 = ioT_Device8
        self.ioT_Device40 = ioT_Device40
        self.ioT_Device68 = ioT_Device68
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_Device(self):
        return self.__ioT_Device

    @ioT_Device.setter
    def ioT_Device(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Device__ioT_Device", None)
        self.__ioT_Device = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Model4"):
                opp_val = getattr(old_value, "ioT_Model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Model4"):
                opp_val = getattr(value, "ioT_Model4", None)
                if opp_val is None:
                    setattr(value, "ioT_Model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ioT_Device8(self):
        return self.__ioT_Device8

    @ioT_Device8.setter
    def ioT_Device8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Device__ioT_Device8", None)
        self.__ioT_Device8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Program"):
                opp_val = getattr(old_value, "ioT_Program", None)
                if opp_val == self:
                    setattr(old_value, "ioT_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Program"):
                opp_val = getattr(value, "ioT_Program", None)
                setattr(value, "ioT_Program", self)

    @property
    def ioT_Device68(self):
        return self.__ioT_Device68

    @ioT_Device68.setter
    def ioT_Device68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Device__ioT_Device68", None)
        self.__ioT_Device68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_SendCommand"):
                opp_val = getattr(old_value, "ioT_SendCommand", None)
                if opp_val == self:
                    setattr(old_value, "ioT_SendCommand", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_SendCommand"):
                opp_val = getattr(value, "ioT_SendCommand", None)
                setattr(value, "ioT_SendCommand", self)

    @property
    def ioT_Device40(self):
        return self.__ioT_Device40

    @ioT_Device40.setter
    def ioT_Device40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Device__ioT_Device40", None)
        self.__ioT_Device40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_ReadConnection"):
                opp_val = getattr(old_value, "ioT_ReadConnection", None)
                if opp_val == self:
                    setattr(old_value, "ioT_ReadConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_ReadConnection"):
                opp_val = getattr(value, "ioT_ReadConnection", None)
                setattr(value, "ioT_ReadConnection", self)

    @property
    def ioT_Device25(self):
        return self.__ioT_Device25

    @ioT_Device25.setter
    def ioT_Device25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Device__ioT_Device25", None)
        self.__ioT_Device25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_ConnectStatement24"):
                opp_val = getattr(old_value, "ioT_ConnectStatement24", None)
                if opp_val == self:
                    setattr(old_value, "ioT_ConnectStatement24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_ConnectStatement24"):
                opp_val = getattr(value, "ioT_ConnectStatement24", None)
                setattr(value, "ioT_ConnectStatement24", self)

class ioT_Config:

    def __init__(self, name: str, ioT_Config: "ioT_Model" = None, ioT_Config6: set["ioT_Declaration"] = None):
        self.name = name
        self.ioT_Config = ioT_Config
        self.ioT_Config6 = ioT_Config6 if ioT_Config6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_Config6(self):
        return self.__ioT_Config6

    @ioT_Config6.setter
    def ioT_Config6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Config__ioT_Config6", None)
        self.__ioT_Config6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ioT_Declaration"):
                    opp_val = getattr(item, "ioT_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "ioT_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ioT_Declaration"):
                    opp_val = getattr(item, "ioT_Declaration", None)
                    
                    setattr(item, "ioT_Declaration", self)
                    

    @property
    def ioT_Config(self):
        return self.__ioT_Config

    @ioT_Config.setter
    def ioT_Config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_Config__ioT_Config", None)
        self.__ioT_Config = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Model2"):
                opp_val = getattr(old_value, "ioT_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Model2"):
                opp_val = getattr(value, "ioT_Model2", None)
                if opp_val is None:
                    setattr(value, "ioT_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_ExternalDeclaration:

    def __init__(self, name: str, ioT_ExternalDeclaration: "ioT_Model" = None, ioT_ExternalDeclaration42: "ioT_ExternalOf" = None, ioT_ExternalDeclaration50: "ioT_ExternalRight" = None):
        self.name = name
        self.ioT_ExternalDeclaration = ioT_ExternalDeclaration
        self.ioT_ExternalDeclaration42 = ioT_ExternalDeclaration42
        self.ioT_ExternalDeclaration50 = ioT_ExternalDeclaration50
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ioT_ExternalDeclaration42(self):
        return self.__ioT_ExternalDeclaration42

    @ioT_ExternalDeclaration42.setter
    def ioT_ExternalDeclaration42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_ExternalDeclaration__ioT_ExternalDeclaration42", None)
        self.__ioT_ExternalDeclaration42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_ExternalOf"):
                opp_val = getattr(old_value, "ioT_ExternalOf", None)
                if opp_val == self:
                    setattr(old_value, "ioT_ExternalOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_ExternalOf"):
                opp_val = getattr(value, "ioT_ExternalOf", None)
                setattr(value, "ioT_ExternalOf", self)

    @property
    def ioT_ExternalDeclaration50(self):
        return self.__ioT_ExternalDeclaration50

    @ioT_ExternalDeclaration50.setter
    def ioT_ExternalDeclaration50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_ExternalDeclaration__ioT_ExternalDeclaration50", None)
        self.__ioT_ExternalDeclaration50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_ExternalRight"):
                opp_val = getattr(old_value, "ioT_ExternalRight", None)
                if opp_val == self:
                    setattr(old_value, "ioT_ExternalRight", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_ExternalRight"):
                opp_val = getattr(value, "ioT_ExternalRight", None)
                setattr(value, "ioT_ExternalRight", self)

    @property
    def ioT_ExternalDeclaration(self):
        return self.__ioT_ExternalDeclaration

    @ioT_ExternalDeclaration.setter
    def ioT_ExternalDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ioT_ExternalDeclaration__ioT_ExternalDeclaration", None)
        self.__ioT_ExternalDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ioT_Model"):
                opp_val = getattr(old_value, "ioT_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ioT_Model"):
                opp_val = getattr(value, "ioT_Model", None)
                if opp_val is None:
                    setattr(value, "ioT_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ioT_Model:

    pass