from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Message:

    pass
class iot_Dispatch(Message):

    pass
class iot_Event(Message):

    pass
class iot_Message:

    def __init__(self, name: str, msg: str, iot_Message: "iot_IotSystemSpec" = None):
        self.name = name
        self.msg = msg
        self.iot_Message = iot_Message
        
    @property
    def msg(self) -> str:
        return self.__msg

    @msg.setter
    def msg(self, msg: str):
        self.__msg = msg

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot_Message(self):
        return self.__iot_Message

    @iot_Message.setter
    def iot_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_Message__iot_Message", None)
        self.__iot_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_IotSystemSpec4"):
                opp_val = getattr(old_value, "iot_IotSystemSpec4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_IotSystemSpec4"):
                opp_val = getattr(value, "iot_IotSystemSpec4", None)
                if opp_val is None:
                    setattr(value, "iot_IotSystemSpec4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iot_BrokerSpec:

    def __init__(self, brokerHost: str, brokerPort: int, iot_BrokerSpec: "iot_IotSystemSpec" = None):
        self.brokerHost = brokerHost
        self.brokerPort = brokerPort
        self.iot_BrokerSpec = iot_BrokerSpec
        
    @property
    def brokerHost(self) -> str:
        return self.__brokerHost

    @brokerHost.setter
    def brokerHost(self, brokerHost: str):
        self.__brokerHost = brokerHost

    @property
    def brokerPort(self) -> int:
        return self.__brokerPort

    @brokerPort.setter
    def brokerPort(self, brokerPort: int):
        self.__brokerPort = brokerPort

    @property
    def iot_BrokerSpec(self):
        return self.__iot_BrokerSpec

    @iot_BrokerSpec.setter
    def iot_BrokerSpec(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_BrokerSpec__iot_BrokerSpec", None)
        self.__iot_BrokerSpec = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_IotSystemSpec2"):
                opp_val = getattr(old_value, "iot_IotSystemSpec2", None)
                if opp_val == self:
                    setattr(old_value, "iot_IotSystemSpec2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_IotSystemSpec2"):
                opp_val = getattr(value, "iot_IotSystemSpec2", None)
                setattr(value, "iot_IotSystemSpec2", self)

class iot_IotSystemSpec:

    def __init__(self, name: str, iot_IotSystemSpec: "iot_IotSystem" = None, iot_IotSystemSpec2: "iot_BrokerSpec" = None, iot_IotSystemSpec4: set["iot_Message"] = None):
        self.name = name
        self.iot_IotSystemSpec = iot_IotSystemSpec
        self.iot_IotSystemSpec2 = iot_IotSystemSpec2
        self.iot_IotSystemSpec4 = iot_IotSystemSpec4 if iot_IotSystemSpec4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iot_IotSystemSpec4(self):
        return self.__iot_IotSystemSpec4

    @iot_IotSystemSpec4.setter
    def iot_IotSystemSpec4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_IotSystemSpec__iot_IotSystemSpec4", None)
        self.__iot_IotSystemSpec4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iot_Message"):
                    opp_val = getattr(item, "iot_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "iot_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iot_Message"):
                    opp_val = getattr(item, "iot_Message", None)
                    
                    setattr(item, "iot_Message", self)
                    

    @property
    def iot_IotSystemSpec(self):
        return self.__iot_IotSystemSpec

    @iot_IotSystemSpec.setter
    def iot_IotSystemSpec(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_IotSystemSpec__iot_IotSystemSpec", None)
        self.__iot_IotSystemSpec = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_IotSystem"):
                opp_val = getattr(old_value, "iot_IotSystem", None)
                if opp_val == self:
                    setattr(old_value, "iot_IotSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_IotSystem"):
                opp_val = getattr(value, "iot_IotSystem", None)
                setattr(value, "iot_IotSystem", self)

    @property
    def iot_IotSystemSpec2(self):
        return self.__iot_IotSystemSpec2

    @iot_IotSystemSpec2.setter
    def iot_IotSystemSpec2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iot_IotSystemSpec__iot_IotSystemSpec2", None)
        self.__iot_IotSystemSpec2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iot_BrokerSpec"):
                opp_val = getattr(old_value, "iot_BrokerSpec", None)
                if opp_val == self:
                    setattr(old_value, "iot_BrokerSpec", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iot_BrokerSpec"):
                opp_val = getattr(value, "iot_BrokerSpec", None)
                setattr(value, "iot_BrokerSpec", self)

class iot_IotSystem:

    pass