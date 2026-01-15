from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sensinact_DSL_CEP_MIN:

    pass
class DSL_Expression:

    pass
class sensinact_DSL_Expression_Multiplication(DSL_Expression):

    pass
class sensinact_DSL_Expression_Plus(DSL_Expression):

    pass
class sensinact_DSL_Object_Boolean(DSL_Expression):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class sensinact_DSL_Object_Number(DSL_Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sensinact_DSL_Expression_Equal(DSL_Expression):

    pass
class sensinact_DSL_Expression_Smaller(DSL_Expression):

    pass
class sensinact_DSL_Expression_And(DSL_Expression):

    pass
class sensinact_DSL_Expression_Larger(DSL_Expression):

    pass
class sensinact_DSL_Expression_Modulo(DSL_Expression):

    pass
class sensinact_DSL_Expression_Negate(DSL_Expression):

    pass
class sensinact_DSL_Object_Ref(DSL_Expression):

    pass
class sensinact_DSL_Object_String(DSL_Expression):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class sensinact_DSL_Expression_Smaller_Equal(DSL_Expression):

    pass
class sensinact_DSL_Expression_Division(DSL_Expression):

    pass
class sensinact_DSL_Expression_Minus(DSL_Expression):

    pass
class sensinact_DSL_Expression_Larger_Equal(DSL_Expression):

    pass
class sensinact_DSL_Expression_Diff(DSL_Expression):

    pass
class sensinact_DSL_Expression_Or(DSL_Expression):

    pass
class sensinact_DSL_ListParam:

    pass
class sensinact_DSL_ResourceAction:

    def __init__(self, variable: str, actiontype: str, sensinact_DSL_ResourceAction: "sensinact_DSL_ListActions" = None, sensinact_DSL_ResourceAction96: "sensinact_DSL_REF" = None, sensinact_DSL_ResourceAction99: "sensinact_DSL_ListParam" = None):
        self.variable = variable
        self.actiontype = actiontype
        self.sensinact_DSL_ResourceAction = sensinact_DSL_ResourceAction
        self.sensinact_DSL_ResourceAction96 = sensinact_DSL_ResourceAction96
        self.sensinact_DSL_ResourceAction99 = sensinact_DSL_ResourceAction99
        
    @property
    def actiontype(self) -> str:
        return self.__actiontype

    @actiontype.setter
    def actiontype(self, actiontype: str):
        self.__actiontype = actiontype

    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def sensinact_DSL_ResourceAction96(self):
        return self.__sensinact_DSL_ResourceAction96

    @sensinact_DSL_ResourceAction96.setter
    def sensinact_DSL_ResourceAction96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sensinact_DSL_ResourceAction__sensinact_DSL_ResourceAction96", None)
        self.__sensinact_DSL_ResourceAction96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensinact_DSL_REF97"):
                opp_val = getattr(old_value, "sensinact_DSL_REF97", None)
                if opp_val == self:
                    setattr(old_value, "sensinact_DSL_REF97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensinact_DSL_REF97"):
                opp_val = getattr(value, "sensinact_DSL_REF97", None)
                setattr(value, "sensinact_DSL_REF97", self)

    @property
    def sensinact_DSL_ResourceAction(self):
        return self.__sensinact_DSL_ResourceAction

    @sensinact_DSL_ResourceAction.setter
    def sensinact_DSL_ResourceAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sensinact_DSL_ResourceAction__sensinact_DSL_ResourceAction", None)
        self.__sensinact_DSL_ResourceAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensinact_DSL_ListActions94"):
                opp_val = getattr(old_value, "sensinact_DSL_ListActions94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensinact_DSL_ListActions94"):
                opp_val = getattr(value, "sensinact_DSL_ListActions94", None)
                if opp_val is None:
                    setattr(value, "sensinact_DSL_ListActions94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sensinact_DSL_ResourceAction99(self):
        return self.__sensinact_DSL_ResourceAction99

    @sensinact_DSL_ResourceAction99.setter
    def sensinact_DSL_ResourceAction99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sensinact_DSL_ResourceAction__sensinact_DSL_ResourceAction99", None)
        self.__sensinact_DSL_ResourceAction99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensinact_DSL_ListParam"):
                opp_val = getattr(old_value, "sensinact_DSL_ListParam", None)
                if opp_val == self:
                    setattr(old_value, "sensinact_DSL_ListParam", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensinact_DSL_ListParam"):
                opp_val = getattr(value, "sensinact_DSL_ListParam", None)
                setattr(value, "sensinact_DSL_ListParam", self)

class sensinact_DSL_CEP_DURATION_SEC:

    def __init__(self, sec: str):
        self.sec = sec
        
    @property
    def sec(self) -> str:
        return self.__sec

    @sec.setter
    def sec(self, sec: str):
        self.__sec = sec

class sensinact_DSL_CEP_DURATION_MIN:

    def __init__(self, min: str):
        self.min = min
        
    @property
    def min(self) -> str:
        return self.__min

    @min.setter
    def min(self, min: str):
        self.__min = min

class sensinact_DSL_CEP_COUNT:

    pass
class sensinact_DSL_CEP_SUM:

    pass
class sensinact_DSL_CEP_AVG:

    pass
class sensinact_DSL_CEP_MAX:

    pass
class sensinact_DSL_ElseDo:

    pass
class sensinact_DSL_ElseIfDo:

    pass
class sensinact_DSL_IfDo:

    pass
class sensinact_DSL_CEP_COINCIDE:

    pass
class sensinact_DSL_REF_CONDITION:

    pass
class sensinact_DSL_CEP_BEFORE:

    pass
class sensinact_DSL_CEP_DURATION:

    pass
class sensinact_DSL_CEP_AFTER:

    pass
class sensinact_EObject:

    pass
class sensinact_DSL_REF:

    def __init__(self, name: str, sensinact_DSL_REF: "sensinact_DSL_REF_CONDITION" = None, sensinact_DSL_REF97: "sensinact_DSL_ResourceAction" = None, sensinact_DSL_REF169: "sensinact_DSL_Object_Ref" = None):
        self.name = name
        self.sensinact_DSL_REF = sensinact_DSL_REF
        self.sensinact_DSL_REF97 = sensinact_DSL_REF97
        self.sensinact_DSL_REF169 = sensinact_DSL_REF169
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sensinact_DSL_REF169(self):
        return self.__sensinact_DSL_REF169

    @sensinact_DSL_REF169.setter
    def sensinact_DSL_REF169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sensinact_DSL_REF__sensinact_DSL_REF169", None)
        self.__sensinact_DSL_REF169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensinact_DSL_Object_Ref"):
                opp_val = getattr(old_value, "sensinact_DSL_Object_Ref", None)
                if opp_val == self:
                    setattr(old_value, "sensinact_DSL_Object_Ref", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensinact_DSL_Object_Ref"):
                opp_val = getattr(value, "sensinact_DSL_Object_Ref", None)
                setattr(value, "sensinact_DSL_Object_Ref", self)

    @property
    def sensinact_DSL_REF97(self):
        return self.__sensinact_DSL_REF97

    @sensinact_DSL_REF97.setter
    def sensinact_DSL_REF97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sensinact_DSL_REF__sensinact_DSL_REF97", None)
        self.__sensinact_DSL_REF97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensinact_DSL_ResourceAction96"):
                opp_val = getattr(old_value, "sensinact_DSL_ResourceAction96", None)
                if opp_val == self:
                    setattr(old_value, "sensinact_DSL_ResourceAction96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensinact_DSL_ResourceAction96"):
                opp_val = getattr(value, "sensinact_DSL_ResourceAction96", None)
                setattr(value, "sensinact_DSL_ResourceAction96", self)

    @property
    def sensinact_DSL_REF(self):
        return self.__sensinact_DSL_REF

    @sensinact_DSL_REF.setter
    def sensinact_DSL_REF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sensinact_DSL_REF__sensinact_DSL_REF", None)
        self.__sensinact_DSL_REF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensinact_DSL_REF_CONDITION33"):
                opp_val = getattr(old_value, "sensinact_DSL_REF_CONDITION33", None)
                if opp_val == self:
                    setattr(old_value, "sensinact_DSL_REF_CONDITION33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensinact_DSL_REF_CONDITION33"):
                opp_val = getattr(value, "sensinact_DSL_REF_CONDITION33", None)
                setattr(value, "sensinact_DSL_REF_CONDITION33", self)

class sensinact_DSL_ListActions:

    pass
class sensinact_DSL_Expression:

    pass
class DSL_REF:

    pass
class sensinact_DSL_ECA_STATEMENT:

    pass
class sensinact_DSL_On:

    pass
class sensinact_DSL_CEP_STATEMENT(DSL_REF):

    pass
class sensinact_DSL_Resource(DSL_REF):

    def __init__(self, gatewayID: str, deviceID: str, serviceID: str, resourceID: str, sensinact_DSL_Resource: "sensinact_DSL_SENSINACT" = None):
        self.gatewayID = gatewayID
        self.deviceID = deviceID
        self.serviceID = serviceID
        self.resourceID = resourceID
        self.sensinact_DSL_Resource = sensinact_DSL_Resource
        
    @property
    def resourceID(self) -> str:
        return self.__resourceID

    @resourceID.setter
    def resourceID(self, resourceID: str):
        self.__resourceID = resourceID

    @property
    def serviceID(self) -> str:
        return self.__serviceID

    @serviceID.setter
    def serviceID(self, serviceID: str):
        self.__serviceID = serviceID

    @property
    def gatewayID(self) -> str:
        return self.__gatewayID

    @gatewayID.setter
    def gatewayID(self, gatewayID: str):
        self.__gatewayID = gatewayID

    @property
    def deviceID(self) -> str:
        return self.__deviceID

    @deviceID.setter
    def deviceID(self, deviceID: str):
        self.__deviceID = deviceID

    @property
    def sensinact_DSL_Resource(self):
        return self.__sensinact_DSL_Resource

    @sensinact_DSL_Resource.setter
    def sensinact_DSL_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sensinact_DSL_Resource__sensinact_DSL_Resource", None)
        self.__sensinact_DSL_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensinact_DSL_SENSINACT4"):
                opp_val = getattr(old_value, "sensinact_DSL_SENSINACT4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensinact_DSL_SENSINACT4"):
                opp_val = getattr(value, "sensinact_DSL_SENSINACT4", None)
                if opp_val is None:
                    setattr(value, "sensinact_DSL_SENSINACT4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sensinact_DSL_FLAG_AUTOSTART:

    def __init__(self, activated: bool, sensinact_DSL_FLAG_AUTOSTART: "sensinact_DSL_SENSINACT" = None):
        self.activated = activated
        self.sensinact_DSL_FLAG_AUTOSTART = sensinact_DSL_FLAG_AUTOSTART
        
    @property
    def activated(self) -> bool:
        return self.__activated

    @activated.setter
    def activated(self, activated: bool):
        self.__activated = activated

    @property
    def sensinact_DSL_FLAG_AUTOSTART(self):
        return self.__sensinact_DSL_FLAG_AUTOSTART

    @sensinact_DSL_FLAG_AUTOSTART.setter
    def sensinact_DSL_FLAG_AUTOSTART(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sensinact_DSL_FLAG_AUTOSTART__sensinact_DSL_FLAG_AUTOSTART", None)
        self.__sensinact_DSL_FLAG_AUTOSTART = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sensinact_DSL_SENSINACT2"):
                opp_val = getattr(old_value, "sensinact_DSL_SENSINACT2", None)
                if opp_val == self:
                    setattr(old_value, "sensinact_DSL_SENSINACT2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sensinact_DSL_SENSINACT2"):
                opp_val = getattr(value, "sensinact_DSL_SENSINACT2", None)
                setattr(value, "sensinact_DSL_SENSINACT2", self)

class sensinact_DSL_SENSINACT:

    pass
class sensinact_Sensinact:

    pass