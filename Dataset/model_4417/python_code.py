from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class arduino_IP:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class InAcquireOperation:

    pass
class arduino_GrantRequest(InAcquireOperation):

    pass
class OutOperation:

    pass
class arduino_AskInvitation(OutOperation):

    pass
class arduino_ForwardDispatch(OutOperation):

    pass
class arduino_DemandRequest(OutOperation):

    pass
class arduino_SupportSpecification:

    def __init__(self, supportType: str, arduino_SupportSpecification: "arduino_InAcquireOperation" = None):
        self.supportType = supportType
        self.arduino_SupportSpecification = arduino_SupportSpecification
        
    @property
    def supportType(self) -> str:
        return self.__supportType

    @supportType.setter
    def supportType(self, supportType: str):
        self.__supportType = supportType

    @property
    def arduino_SupportSpecification(self):
        return self.__arduino_SupportSpecification

    @arduino_SupportSpecification.setter
    def arduino_SupportSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_SupportSpecification__arduino_SupportSpecification", None)
        self.__arduino_SupportSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_InAcquireOperation50"):
                opp_val = getattr(old_value, "arduino_InAcquireOperation50", None)
                if opp_val == self:
                    setattr(old_value, "arduino_InAcquireOperation50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_InAcquireOperation50"):
                opp_val = getattr(value, "arduino_InAcquireOperation50", None)
                setattr(value, "arduino_InAcquireOperation50", self)

class InOperation:

    pass
class arduino_InAcquireOperation(InOperation):

    pass
class HighLevelOperation:

    pass
class arduino_InOperation(HighLevelOperation):

    pass
class arduino_OutOperation(HighLevelOperation):

    pass
class SupportData:

    pass
class arduino_ExplicitSupportData(SupportData):

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def host(self, host: str):
        self.__host = host

class arduino_SupportData:

    pass
class SupportSpecification:

    pass
class arduino_TCP(SupportSpecification):

    pass
class arduino_Serial(SupportSpecification):

    pass
class arduino_AcceptInvitation(InAcquireOperation):

    pass
class arduino_ServeDispatch(InAcquireOperation):

    pass
class AbstractDevice:

    pass
class arduino_Actuator(AbstractDevice):

    pass
class arduino_SensorValuePrecondition:

    def __init__(self, cond: str, value: str, arduino_SensorValuePrecondition: "arduino_Sensor" = None):
        self.cond = cond
        self.value = value
        self.arduino_SensorValuePrecondition = arduino_SensorValuePrecondition
        
    @property
    def cond(self) -> str:
        return self.__cond

    @cond.setter
    def cond(self, cond: str):
        self.__cond = cond

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def arduino_SensorValuePrecondition(self):
        return self.__arduino_SensorValuePrecondition

    @arduino_SensorValuePrecondition.setter
    def arduino_SensorValuePrecondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_SensorValuePrecondition__arduino_SensorValuePrecondition", None)
        self.__arduino_SensorValuePrecondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sensor44"):
                opp_val = getattr(old_value, "arduino_Sensor44", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Sensor44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sensor44"):
                opp_val = getattr(value, "arduino_Sensor44", None)
                setattr(value, "arduino_Sensor44", self)

class arduino_EmptyPrecondition:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class arduino_EObject:

    pass
class arduino_Precondition1:

    pass
class arduino_PortConnectionData:

    def __init__(self, host: str, port: int, arduino_PortConnectionData: "arduino_PortTCP" = None):
        self.host = host
        self.port = port
        self.arduino_PortConnectionData = arduino_PortConnectionData
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def host(self) -> str:
        return self.__host

    @host.setter
    def host(self, host: str):
        self.__host = host

    @property
    def arduino_PortConnectionData(self):
        return self.__arduino_PortConnectionData

    @arduino_PortConnectionData.setter
    def arduino_PortConnectionData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_PortConnectionData__arduino_PortConnectionData", None)
        self.__arduino_PortConnectionData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_PortTCP"):
                opp_val = getattr(old_value, "arduino_PortTCP", None)
                if opp_val == self:
                    setattr(old_value, "arduino_PortTCP", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_PortTCP"):
                opp_val = getattr(value, "arduino_PortTCP", None)
                setattr(value, "arduino_PortTCP", self)

class PortProtocol:

    pass
class arduino_PortTCP(PortProtocol):

    def __init__(self, supportType: str, arduino_PortTCP: "arduino_PortConnectionData" = None):
        self.supportType = supportType
        self.arduino_PortTCP = arduino_PortTCP
        
    @property
    def supportType(self) -> str:
        return self.__supportType

    @supportType.setter
    def supportType(self, supportType: str):
        self.__supportType = supportType

    @property
    def arduino_PortTCP(self):
        return self.__arduino_PortTCP

    @arduino_PortTCP.setter
    def arduino_PortTCP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_PortTCP__arduino_PortTCP", None)
        self.__arduino_PortTCP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_PortConnectionData"):
                opp_val = getattr(old_value, "arduino_PortConnectionData", None)
                if opp_val == self:
                    setattr(old_value, "arduino_PortConnectionData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_PortConnectionData"):
                opp_val = getattr(value, "arduino_PortConnectionData", None)
                setattr(value, "arduino_PortConnectionData", self)

class arduino_PortProtocol:

    pass
class OutInMessage:

    pass
class arduino_Invitation(OutInMessage):

    pass
class arduino_Request(OutInMessage):

    pass
class OutOnlyMessage:

    pass
class arduino_Dispatch(OutOnlyMessage):

    def __init__(self, name: str, arduino_Dispatch66: "arduino_ServeDispatch" = None, arduino_Dispatch: "arduino_ForwardDispatch" = None):
        self.name = name
        self.arduino_Dispatch66 = arduino_Dispatch66
        self.arduino_Dispatch = arduino_Dispatch
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduino_Dispatch(self):
        return self.__arduino_Dispatch

    @arduino_Dispatch.setter
    def arduino_Dispatch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Dispatch__arduino_Dispatch", None)
        self.__arduino_Dispatch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_ForwardDispatch"):
                opp_val = getattr(old_value, "arduino_ForwardDispatch", None)
                if opp_val == self:
                    setattr(old_value, "arduino_ForwardDispatch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_ForwardDispatch"):
                opp_val = getattr(value, "arduino_ForwardDispatch", None)
                setattr(value, "arduino_ForwardDispatch", self)

    @property
    def arduino_Dispatch66(self):
        return self.__arduino_Dispatch66

    @arduino_Dispatch66.setter
    def arduino_Dispatch66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Dispatch__arduino_Dispatch66", None)
        self.__arduino_Dispatch66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_ServeDispatch"):
                opp_val = getattr(old_value, "arduino_ServeDispatch", None)
                if opp_val == self:
                    setattr(old_value, "arduino_ServeDispatch", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_ServeDispatch"):
                opp_val = getattr(value, "arduino_ServeDispatch", None)
                setattr(value, "arduino_ServeDispatch", self)

class Message:

    pass
class arduino_OutInMessage(Message):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class arduino_OutOnlyMessage(Message):

    pass
class arduino_IODevice(AbstractDevice):

    def __init__(self, analog: bool, pullup: bool):
        self.analog = analog
        self.pullup = pullup
        
    @property
    def analog(self) -> bool:
        return self.__analog

    @analog.setter
    def analog(self, analog: bool):
        self.__analog = analog

    @property
    def pullup(self) -> bool:
        return self.__pullup

    @pullup.setter
    def pullup(self, pullup: bool):
        self.__pullup = pullup

class arduino_HighLevelOperation:

    pass
class arduino_Message:

    pass
class arduino_CommunicationParams:

    def __init__(self, type: str, mac: str, ip: str, dns: str, gateway: str, subnet: str, baudrate: int, arduino_CommunicationParams: "arduino_SystemDefinition" = None):
        self.type = type
        self.mac = mac
        self.ip = ip
        self.dns = dns
        self.gateway = gateway
        self.subnet = subnet
        self.baudrate = baudrate
        self.arduino_CommunicationParams = arduino_CommunicationParams
        
    @property
    def mac(self) -> str:
        return self.__mac

    @mac.setter
    def mac(self, mac: str):
        self.__mac = mac

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def gateway(self) -> str:
        return self.__gateway

    @gateway.setter
    def gateway(self, gateway: str):
        self.__gateway = gateway

    @property
    def ip(self) -> str:
        return self.__ip

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip

    @property
    def dns(self) -> str:
        return self.__dns

    @dns.setter
    def dns(self, dns: str):
        self.__dns = dns

    @property
    def baudrate(self) -> int:
        return self.__baudrate

    @baudrate.setter
    def baudrate(self, baudrate: int):
        self.__baudrate = baudrate

    @property
    def subnet(self) -> str:
        return self.__subnet

    @subnet.setter
    def subnet(self, subnet: str):
        self.__subnet = subnet

    @property
    def arduino_CommunicationParams(self):
        return self.__arduino_CommunicationParams

    @arduino_CommunicationParams.setter
    def arduino_CommunicationParams(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_CommunicationParams__arduino_CommunicationParams", None)
        self.__arduino_CommunicationParams = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_SystemDefinition14"):
                opp_val = getattr(old_value, "arduino_SystemDefinition14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_SystemDefinition14"):
                opp_val = getattr(value, "arduino_SystemDefinition14", None)
                if opp_val is None:
                    setattr(value, "arduino_SystemDefinition14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduino_SystemDefinition:

    pass
class arduino_LoopItem:

    pass
class arduino_Task:

    def __init__(self, name: str, external: bool, arduino_Task: "arduino_Sketch" = None, arduino_Task21: "arduino_LoopItem" = None, arduino_Task46: "arduino_OutOperation" = None, arduino_Task48: "arduino_InAcquireOperation" = None, arduino_Task54: "arduino_DemandRequest" = None, arduino_Task58: "arduino_ForwardDispatch" = None, arduino_Task62: "arduino_AskInvitation" = None):
        self.name = name
        self.external = external
        self.arduino_Task = arduino_Task
        self.arduino_Task21 = arduino_Task21
        self.arduino_Task46 = arduino_Task46
        self.arduino_Task48 = arduino_Task48
        self.arduino_Task54 = arduino_Task54
        self.arduino_Task58 = arduino_Task58
        self.arduino_Task62 = arduino_Task62
        
    @property
    def external(self) -> bool:
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduino_Task54(self):
        return self.__arduino_Task54

    @arduino_Task54.setter
    def arduino_Task54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Task__arduino_Task54", None)
        self.__arduino_Task54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_DemandRequest53"):
                opp_val = getattr(old_value, "arduino_DemandRequest53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_DemandRequest53"):
                opp_val = getattr(value, "arduino_DemandRequest53", None)
                if opp_val is None:
                    setattr(value, "arduino_DemandRequest53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Task(self):
        return self.__arduino_Task

    @arduino_Task.setter
    def arduino_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Task__arduino_Task", None)
        self.__arduino_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch8"):
                opp_val = getattr(old_value, "arduino_Sketch8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch8"):
                opp_val = getattr(value, "arduino_Sketch8", None)
                if opp_val is None:
                    setattr(value, "arduino_Sketch8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Task21(self):
        return self.__arduino_Task21

    @arduino_Task21.setter
    def arduino_Task21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Task__arduino_Task21", None)
        self.__arduino_Task21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_LoopItem20"):
                opp_val = getattr(old_value, "arduino_LoopItem20", None)
                if opp_val == self:
                    setattr(old_value, "arduino_LoopItem20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_LoopItem20"):
                opp_val = getattr(value, "arduino_LoopItem20", None)
                setattr(value, "arduino_LoopItem20", self)

    @property
    def arduino_Task58(self):
        return self.__arduino_Task58

    @arduino_Task58.setter
    def arduino_Task58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Task__arduino_Task58", None)
        self.__arduino_Task58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_ForwardDispatch57"):
                opp_val = getattr(old_value, "arduino_ForwardDispatch57", None)
                if opp_val == self:
                    setattr(old_value, "arduino_ForwardDispatch57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_ForwardDispatch57"):
                opp_val = getattr(value, "arduino_ForwardDispatch57", None)
                setattr(value, "arduino_ForwardDispatch57", self)

    @property
    def arduino_Task46(self):
        return self.__arduino_Task46

    @arduino_Task46.setter
    def arduino_Task46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Task__arduino_Task46", None)
        self.__arduino_Task46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_OutOperation"):
                opp_val = getattr(old_value, "arduino_OutOperation", None)
                if opp_val == self:
                    setattr(old_value, "arduino_OutOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_OutOperation"):
                opp_val = getattr(value, "arduino_OutOperation", None)
                setattr(value, "arduino_OutOperation", self)

    @property
    def arduino_Task62(self):
        return self.__arduino_Task62

    @arduino_Task62.setter
    def arduino_Task62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Task__arduino_Task62", None)
        self.__arduino_Task62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_AskInvitation61"):
                opp_val = getattr(old_value, "arduino_AskInvitation61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_AskInvitation61"):
                opp_val = getattr(value, "arduino_AskInvitation61", None)
                if opp_val is None:
                    setattr(value, "arduino_AskInvitation61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Task48(self):
        return self.__arduino_Task48

    @arduino_Task48.setter
    def arduino_Task48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Task__arduino_Task48", None)
        self.__arduino_Task48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_InAcquireOperation"):
                opp_val = getattr(old_value, "arduino_InAcquireOperation", None)
                if opp_val == self:
                    setattr(old_value, "arduino_InAcquireOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_InAcquireOperation"):
                opp_val = getattr(value, "arduino_InAcquireOperation", None)
                setattr(value, "arduino_InAcquireOperation", self)

class arduino_Poll:

    def __init__(self, type: str, l: int, h: int, arduino_Poll30: "arduino_Sensor" = None, arduino_Poll: "arduino_Sketch" = None, arduino_Poll33: "arduino_Handler" = None):
        self.type = type
        self.l = l
        self.h = h
        self.arduino_Poll30 = arduino_Poll30
        self.arduino_Poll = arduino_Poll
        self.arduino_Poll33 = arduino_Poll33
        
    @property
    def h(self) -> int:
        return self.__h

    @h.setter
    def h(self, h: int):
        self.__h = h

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def l(self) -> int:
        return self.__l

    @l.setter
    def l(self, l: int):
        self.__l = l

    @property
    def arduino_Poll33(self):
        return self.__arduino_Poll33

    @arduino_Poll33.setter
    def arduino_Poll33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Poll__arduino_Poll33", None)
        self.__arduino_Poll33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Handler34"):
                opp_val = getattr(old_value, "arduino_Handler34", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Handler34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Handler34"):
                opp_val = getattr(value, "arduino_Handler34", None)
                setattr(value, "arduino_Handler34", self)

    @property
    def arduino_Poll(self):
        return self.__arduino_Poll

    @arduino_Poll.setter
    def arduino_Poll(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Poll__arduino_Poll", None)
        self.__arduino_Poll = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch6"):
                opp_val = getattr(old_value, "arduino_Sketch6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch6"):
                opp_val = getattr(value, "arduino_Sketch6", None)
                if opp_val is None:
                    setattr(value, "arduino_Sketch6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Poll30(self):
        return self.__arduino_Poll30

    @arduino_Poll30.setter
    def arduino_Poll30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Poll__arduino_Poll30", None)
        self.__arduino_Poll30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sensor31"):
                opp_val = getattr(old_value, "arduino_Sensor31", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Sensor31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sensor31"):
                opp_val = getattr(value, "arduino_Sensor31", None)
                setattr(value, "arduino_Sensor31", self)

class arduino_Interrupt:

    def __init__(self, name: str, interruptKind: str, eventKind: str, arduino_Interrupt25: "arduino_Sensor" = None, arduino_Interrupt27: "arduino_Handler" = None, arduino_Interrupt: "arduino_Sketch" = None):
        self.name = name
        self.interruptKind = interruptKind
        self.eventKind = eventKind
        self.arduino_Interrupt25 = arduino_Interrupt25
        self.arduino_Interrupt27 = arduino_Interrupt27
        self.arduino_Interrupt = arduino_Interrupt
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def interruptKind(self) -> str:
        return self.__interruptKind

    @interruptKind.setter
    def interruptKind(self, interruptKind: str):
        self.__interruptKind = interruptKind

    @property
    def eventKind(self) -> str:
        return self.__eventKind

    @eventKind.setter
    def eventKind(self, eventKind: str):
        self.__eventKind = eventKind

    @property
    def arduino_Interrupt25(self):
        return self.__arduino_Interrupt25

    @arduino_Interrupt25.setter
    def arduino_Interrupt25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Interrupt__arduino_Interrupt25", None)
        self.__arduino_Interrupt25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sensor"):
                opp_val = getattr(old_value, "arduino_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sensor"):
                opp_val = getattr(value, "arduino_Sensor", None)
                setattr(value, "arduino_Sensor", self)

    @property
    def arduino_Interrupt(self):
        return self.__arduino_Interrupt

    @arduino_Interrupt.setter
    def arduino_Interrupt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Interrupt__arduino_Interrupt", None)
        self.__arduino_Interrupt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch4"):
                opp_val = getattr(old_value, "arduino_Sketch4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch4"):
                opp_val = getattr(value, "arduino_Sketch4", None)
                if opp_val is None:
                    setattr(value, "arduino_Sketch4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def arduino_Interrupt27(self):
        return self.__arduino_Interrupt27

    @arduino_Interrupt27.setter
    def arduino_Interrupt27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Interrupt__arduino_Interrupt27", None)
        self.__arduino_Interrupt27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Handler28"):
                opp_val = getattr(old_value, "arduino_Handler28", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Handler28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Handler28"):
                opp_val = getattr(value, "arduino_Handler28", None)
                setattr(value, "arduino_Handler28", self)

class arduino_Handler:

    def __init__(self, name: str, arduino_Handler28: "arduino_Interrupt" = None, arduino_Handler: "arduino_Sketch" = None, arduino_Handler34: "arduino_Poll" = None):
        self.name = name
        self.arduino_Handler28 = arduino_Handler28
        self.arduino_Handler = arduino_Handler
        self.arduino_Handler34 = arduino_Handler34
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def arduino_Handler28(self):
        return self.__arduino_Handler28

    @arduino_Handler28.setter
    def arduino_Handler28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Handler__arduino_Handler28", None)
        self.__arduino_Handler28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Interrupt27"):
                opp_val = getattr(old_value, "arduino_Interrupt27", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Interrupt27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Interrupt27"):
                opp_val = getattr(value, "arduino_Interrupt27", None)
                setattr(value, "arduino_Interrupt27", self)

    @property
    def arduino_Handler34(self):
        return self.__arduino_Handler34

    @arduino_Handler34.setter
    def arduino_Handler34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Handler__arduino_Handler34", None)
        self.__arduino_Handler34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Poll33"):
                opp_val = getattr(old_value, "arduino_Poll33", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Poll33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Poll33"):
                opp_val = getattr(value, "arduino_Poll33", None)
                setattr(value, "arduino_Poll33", self)

    @property
    def arduino_Handler(self):
        return self.__arduino_Handler

    @arduino_Handler.setter
    def arduino_Handler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Handler__arduino_Handler", None)
        self.__arduino_Handler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch2"):
                opp_val = getattr(old_value, "arduino_Sketch2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch2"):
                opp_val = getattr(value, "arduino_Sketch2", None)
                if opp_val is None:
                    setattr(value, "arduino_Sketch2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduino_Sensor(AbstractDevice):

    def __init__(self, analog: bool, pullup: bool, arduino_Sensor: "arduino_Interrupt" = None, arduino_Sensor31: "arduino_Poll" = None, arduino_Sensor44: "arduino_SensorValuePrecondition" = None):
        self.analog = analog
        self.pullup = pullup
        self.arduino_Sensor = arduino_Sensor
        self.arduino_Sensor31 = arduino_Sensor31
        self.arduino_Sensor44 = arduino_Sensor44
        
    @property
    def analog(self) -> bool:
        return self.__analog

    @analog.setter
    def analog(self, analog: bool):
        self.__analog = analog

    @property
    def pullup(self) -> bool:
        return self.__pullup

    @pullup.setter
    def pullup(self, pullup: bool):
        self.__pullup = pullup

    @property
    def arduino_Sensor31(self):
        return self.__arduino_Sensor31

    @arduino_Sensor31.setter
    def arduino_Sensor31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sensor__arduino_Sensor31", None)
        self.__arduino_Sensor31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Poll30"):
                opp_val = getattr(old_value, "arduino_Poll30", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Poll30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Poll30"):
                opp_val = getattr(value, "arduino_Poll30", None)
                setattr(value, "arduino_Poll30", self)

    @property
    def arduino_Sensor44(self):
        return self.__arduino_Sensor44

    @arduino_Sensor44.setter
    def arduino_Sensor44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sensor__arduino_Sensor44", None)
        self.__arduino_Sensor44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_SensorValuePrecondition"):
                opp_val = getattr(old_value, "arduino_SensorValuePrecondition", None)
                if opp_val == self:
                    setattr(old_value, "arduino_SensorValuePrecondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_SensorValuePrecondition"):
                opp_val = getattr(value, "arduino_SensorValuePrecondition", None)
                setattr(value, "arduino_SensorValuePrecondition", self)

    @property
    def arduino_Sensor(self):
        return self.__arduino_Sensor

    @arduino_Sensor.setter
    def arduino_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sensor__arduino_Sensor", None)
        self.__arduino_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Interrupt25"):
                opp_val = getattr(old_value, "arduino_Interrupt25", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Interrupt25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Interrupt25"):
                opp_val = getattr(value, "arduino_Interrupt25", None)
                setattr(value, "arduino_Interrupt25", self)

class arduino_Precondition:

    def __init__(self, op: str, arduino_Precondition: "arduino_LoopItem" = None, arduino_Precondition37: "arduino_Precondition1" = None, arduino_Precondition40: "arduino_Precondition" = None, arduino_Precondition38: "arduino_Precondition" = None):
        self.op = op
        self.arduino_Precondition = arduino_Precondition
        self.arduino_Precondition37 = arduino_Precondition37
        self.arduino_Precondition40 = arduino_Precondition40
        self.arduino_Precondition38 = arduino_Precondition38
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def arduino_Precondition(self):
        return self.__arduino_Precondition

    @arduino_Precondition.setter
    def arduino_Precondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Precondition__arduino_Precondition", None)
        self.__arduino_Precondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_LoopItem23"):
                opp_val = getattr(old_value, "arduino_LoopItem23", None)
                if opp_val == self:
                    setattr(old_value, "arduino_LoopItem23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_LoopItem23"):
                opp_val = getattr(value, "arduino_LoopItem23", None)
                setattr(value, "arduino_LoopItem23", self)

    @property
    def arduino_Precondition40(self):
        return self.__arduino_Precondition40

    @arduino_Precondition40.setter
    def arduino_Precondition40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Precondition__arduino_Precondition40", None)
        self.__arduino_Precondition40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Precondition38"):
                opp_val = getattr(old_value, "arduino_Precondition38", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Precondition38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Precondition38"):
                opp_val = getattr(value, "arduino_Precondition38", None)
                setattr(value, "arduino_Precondition38", self)

    @property
    def arduino_Precondition38(self):
        return self.__arduino_Precondition38

    @arduino_Precondition38.setter
    def arduino_Precondition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Precondition__arduino_Precondition38", None)
        self.__arduino_Precondition38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Precondition40"):
                opp_val = getattr(old_value, "arduino_Precondition40", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Precondition40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Precondition40"):
                opp_val = getattr(value, "arduino_Precondition40", None)
                setattr(value, "arduino_Precondition40", self)

    @property
    def arduino_Precondition37(self):
        return self.__arduino_Precondition37

    @arduino_Precondition37.setter
    def arduino_Precondition37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Precondition__arduino_Precondition37", None)
        self.__arduino_Precondition37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Precondition1"):
                opp_val = getattr(old_value, "arduino_Precondition1", None)
                if opp_val == self:
                    setattr(old_value, "arduino_Precondition1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Precondition1"):
                opp_val = getattr(value, "arduino_Precondition1", None)
                setattr(value, "arduino_Precondition1", self)

class arduino_AbstractDevice:

    def __init__(self, name: str, pin: str, arduino_AbstractDevice: "arduino_Sketch" = None):
        self.name = name
        self.pin = pin
        self.arduino_AbstractDevice = arduino_AbstractDevice
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pin(self) -> str:
        return self.__pin

    @pin.setter
    def pin(self, pin: str):
        self.__pin = pin

    @property
    def arduino_AbstractDevice(self):
        return self.__arduino_AbstractDevice

    @arduino_AbstractDevice.setter
    def arduino_AbstractDevice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_AbstractDevice__arduino_AbstractDevice", None)
        self.__arduino_AbstractDevice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_Sketch"):
                opp_val = getattr(old_value, "arduino_Sketch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_Sketch"):
                opp_val = getattr(value, "arduino_Sketch", None)
                if opp_val is None:
                    setattr(value, "arduino_Sketch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class arduino_Sketch:

    def __init__(self, name: str, hardware: str, defineSystem: bool, arduino_Sketch: set["arduino_AbstractDevice"] = None, arduino_Sketch2: set["arduino_Handler"] = None, arduino_Sketch4: set["arduino_Interrupt"] = None, arduino_Sketch6: set["arduino_Poll"] = None, arduino_Sketch8: set["arduino_Task"] = None, arduino_Sketch10: set["arduino_LoopItem"] = None, arduino_Sketch12: "arduino_SystemDefinition" = None):
        self.name = name
        self.hardware = hardware
        self.defineSystem = defineSystem
        self.arduino_Sketch = arduino_Sketch if arduino_Sketch is not None else set()
        self.arduino_Sketch2 = arduino_Sketch2 if arduino_Sketch2 is not None else set()
        self.arduino_Sketch4 = arduino_Sketch4 if arduino_Sketch4 is not None else set()
        self.arduino_Sketch6 = arduino_Sketch6 if arduino_Sketch6 is not None else set()
        self.arduino_Sketch8 = arduino_Sketch8 if arduino_Sketch8 is not None else set()
        self.arduino_Sketch10 = arduino_Sketch10 if arduino_Sketch10 is not None else set()
        self.arduino_Sketch12 = arduino_Sketch12
        
    @property
    def hardware(self) -> str:
        return self.__hardware

    @hardware.setter
    def hardware(self, hardware: str):
        self.__hardware = hardware

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def defineSystem(self) -> bool:
        return self.__defineSystem

    @defineSystem.setter
    def defineSystem(self, defineSystem: bool):
        self.__defineSystem = defineSystem

    @property
    def arduino_Sketch(self):
        return self.__arduino_Sketch

    @arduino_Sketch.setter
    def arduino_Sketch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch", None)
        self.__arduino_Sketch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_AbstractDevice"):
                    opp_val = getattr(item, "arduino_AbstractDevice", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_AbstractDevice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_AbstractDevice"):
                    opp_val = getattr(item, "arduino_AbstractDevice", None)
                    
                    setattr(item, "arduino_AbstractDevice", self)
                    

    @property
    def arduino_Sketch8(self):
        return self.__arduino_Sketch8

    @arduino_Sketch8.setter
    def arduino_Sketch8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch8", None)
        self.__arduino_Sketch8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Task"):
                    opp_val = getattr(item, "arduino_Task", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Task"):
                    opp_val = getattr(item, "arduino_Task", None)
                    
                    setattr(item, "arduino_Task", self)
                    

    @property
    def arduino_Sketch10(self):
        return self.__arduino_Sketch10

    @arduino_Sketch10.setter
    def arduino_Sketch10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch10", None)
        self.__arduino_Sketch10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_LoopItem"):
                    opp_val = getattr(item, "arduino_LoopItem", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_LoopItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_LoopItem"):
                    opp_val = getattr(item, "arduino_LoopItem", None)
                    
                    setattr(item, "arduino_LoopItem", self)
                    

    @property
    def arduino_Sketch12(self):
        return self.__arduino_Sketch12

    @arduino_Sketch12.setter
    def arduino_Sketch12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch12", None)
        self.__arduino_Sketch12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "arduino_SystemDefinition"):
                opp_val = getattr(old_value, "arduino_SystemDefinition", None)
                if opp_val == self:
                    setattr(old_value, "arduino_SystemDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "arduino_SystemDefinition"):
                opp_val = getattr(value, "arduino_SystemDefinition", None)
                setattr(value, "arduino_SystemDefinition", self)

    @property
    def arduino_Sketch6(self):
        return self.__arduino_Sketch6

    @arduino_Sketch6.setter
    def arduino_Sketch6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch6", None)
        self.__arduino_Sketch6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Poll"):
                    opp_val = getattr(item, "arduino_Poll", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Poll", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Poll"):
                    opp_val = getattr(item, "arduino_Poll", None)
                    
                    setattr(item, "arduino_Poll", self)
                    

    @property
    def arduino_Sketch2(self):
        return self.__arduino_Sketch2

    @arduino_Sketch2.setter
    def arduino_Sketch2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch2", None)
        self.__arduino_Sketch2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Handler"):
                    opp_val = getattr(item, "arduino_Handler", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Handler", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Handler"):
                    opp_val = getattr(item, "arduino_Handler", None)
                    
                    setattr(item, "arduino_Handler", self)
                    

    @property
    def arduino_Sketch4(self):
        return self.__arduino_Sketch4

    @arduino_Sketch4.setter
    def arduino_Sketch4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_arduino_Sketch__arduino_Sketch4", None)
        self.__arduino_Sketch4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "arduino_Interrupt"):
                    opp_val = getattr(item, "arduino_Interrupt", None)
                    
                    if opp_val == self:
                        setattr(item, "arduino_Interrupt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "arduino_Interrupt"):
                    opp_val = getattr(item, "arduino_Interrupt", None)
                    
                    setattr(item, "arduino_Interrupt", self)
                    
