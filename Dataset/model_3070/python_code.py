from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class giraffeDSL_IntFeature:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class giraffeDSL_Features:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class giraffeDSL_ActionMethodType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_ActionMethodType: "giraffeDSL_Action" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_ActionMethodType = giraffeDSL_ActionMethodType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_ActionMethodType(self):
        return self.__giraffeDSL_ActionMethodType

    @giraffeDSL_ActionMethodType.setter
    def giraffeDSL_ActionMethodType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_ActionMethodType__giraffeDSL_ActionMethodType", None)
        self.__giraffeDSL_ActionMethodType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Action49"):
                opp_val = getattr(old_value, "giraffeDSL_Action49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Action49"):
                opp_val = getattr(value, "giraffeDSL_Action49", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Action49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_ActionClassType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_ActionClassType: "giraffeDSL_Action" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_ActionClassType = giraffeDSL_ActionClassType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_ActionClassType(self):
        return self.__giraffeDSL_ActionClassType

    @giraffeDSL_ActionClassType.setter
    def giraffeDSL_ActionClassType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_ActionClassType__giraffeDSL_ActionClassType", None)
        self.__giraffeDSL_ActionClassType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Action47"):
                opp_val = getattr(old_value, "giraffeDSL_Action47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Action47"):
                opp_val = getattr(value, "giraffeDSL_Action47", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Action47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_ActionRangeType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_ActionRangeType: "giraffeDSL_Action" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_ActionRangeType = giraffeDSL_ActionRangeType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def giraffeDSL_ActionRangeType(self):
        return self.__giraffeDSL_ActionRangeType

    @giraffeDSL_ActionRangeType.setter
    def giraffeDSL_ActionRangeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_ActionRangeType__giraffeDSL_ActionRangeType", None)
        self.__giraffeDSL_ActionRangeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Action"):
                opp_val = getattr(old_value, "giraffeDSL_Action", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Action"):
                opp_val = getattr(value, "giraffeDSL_Action", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Action", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_MonitoringType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_MonitoringType: "giraffeDSL_Monitor" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_MonitoringType = giraffeDSL_MonitoringType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def giraffeDSL_MonitoringType(self):
        return self.__giraffeDSL_MonitoringType

    @giraffeDSL_MonitoringType.setter
    def giraffeDSL_MonitoringType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_MonitoringType__giraffeDSL_MonitoringType", None)
        self.__giraffeDSL_MonitoringType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Monitor39"):
                opp_val = getattr(old_value, "giraffeDSL_Monitor39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Monitor39"):
                opp_val = getattr(value, "giraffeDSL_Monitor39", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Monitor39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_MonitorRangeType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_MonitorRangeType: "giraffeDSL_Monitor" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_MonitorRangeType = giraffeDSL_MonitorRangeType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def giraffeDSL_MonitorRangeType(self):
        return self.__giraffeDSL_MonitorRangeType

    @giraffeDSL_MonitorRangeType.setter
    def giraffeDSL_MonitorRangeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_MonitorRangeType__giraffeDSL_MonitorRangeType", None)
        self.__giraffeDSL_MonitorRangeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Monitor"):
                opp_val = getattr(old_value, "giraffeDSL_Monitor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Monitor"):
                opp_val = getattr(value, "giraffeDSL_Monitor", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Monitor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_DeployAppSlaveMethodType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_DeployAppSlaveMethodType: "giraffeDSL_DeployApp" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_DeployAppSlaveMethodType = giraffeDSL_DeployAppSlaveMethodType
        
    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def giraffeDSL_DeployAppSlaveMethodType(self):
        return self.__giraffeDSL_DeployAppSlaveMethodType

    @giraffeDSL_DeployAppSlaveMethodType.setter
    def giraffeDSL_DeployAppSlaveMethodType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_DeployAppSlaveMethodType__giraffeDSL_DeployAppSlaveMethodType", None)
        self.__giraffeDSL_DeployAppSlaveMethodType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_DeployApp36"):
                opp_val = getattr(old_value, "giraffeDSL_DeployApp36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_DeployApp36"):
                opp_val = getattr(value, "giraffeDSL_DeployApp36", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_DeployApp36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_DeployAppMasterMethodType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_DeployAppMasterMethodType: "giraffeDSL_DeployApp" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_DeployAppMasterMethodType = giraffeDSL_DeployAppMasterMethodType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_DeployAppMasterMethodType(self):
        return self.__giraffeDSL_DeployAppMasterMethodType

    @giraffeDSL_DeployAppMasterMethodType.setter
    def giraffeDSL_DeployAppMasterMethodType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_DeployAppMasterMethodType__giraffeDSL_DeployAppMasterMethodType", None)
        self.__giraffeDSL_DeployAppMasterMethodType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_DeployApp34"):
                opp_val = getattr(old_value, "giraffeDSL_DeployApp34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_DeployApp34"):
                opp_val = getattr(value, "giraffeDSL_DeployApp34", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_DeployApp34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_DeployAppClassType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_DeployAppClassType: "giraffeDSL_DeployApp" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_DeployAppClassType = giraffeDSL_DeployAppClassType
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_DeployAppClassType(self):
        return self.__giraffeDSL_DeployAppClassType

    @giraffeDSL_DeployAppClassType.setter
    def giraffeDSL_DeployAppClassType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_DeployAppClassType__giraffeDSL_DeployAppClassType", None)
        self.__giraffeDSL_DeployAppClassType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_DeployApp32"):
                opp_val = getattr(old_value, "giraffeDSL_DeployApp32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_DeployApp32"):
                opp_val = getattr(value, "giraffeDSL_DeployApp32", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_DeployApp32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_StressMethodType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_StressMethodType: "giraffeDSL_Stress" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_StressMethodType = giraffeDSL_StressMethodType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def giraffeDSL_StressMethodType(self):
        return self.__giraffeDSL_StressMethodType

    @giraffeDSL_StressMethodType.setter
    def giraffeDSL_StressMethodType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_StressMethodType__giraffeDSL_StressMethodType", None)
        self.__giraffeDSL_StressMethodType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Stress44"):
                opp_val = getattr(old_value, "giraffeDSL_Stress44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Stress44"):
                opp_val = getattr(value, "giraffeDSL_Stress44", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Stress44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_StressClassType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_StressClassType: "giraffeDSL_Stress" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_StressClassType = giraffeDSL_StressClassType
        
    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def giraffeDSL_StressClassType(self):
        return self.__giraffeDSL_StressClassType

    @giraffeDSL_StressClassType.setter
    def giraffeDSL_StressClassType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_StressClassType__giraffeDSL_StressClassType", None)
        self.__giraffeDSL_StressClassType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Stress42"):
                opp_val = getattr(old_value, "giraffeDSL_Stress42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Stress42"):
                opp_val = getattr(value, "giraffeDSL_Stress42", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Stress42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_StressRangeType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_StressRangeType: "giraffeDSL_Stress" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_StressRangeType = giraffeDSL_StressRangeType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def giraffeDSL_StressRangeType(self):
        return self.__giraffeDSL_StressRangeType

    @giraffeDSL_StressRangeType.setter
    def giraffeDSL_StressRangeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_StressRangeType__giraffeDSL_StressRangeType", None)
        self.__giraffeDSL_StressRangeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Stress"):
                opp_val = getattr(old_value, "giraffeDSL_Stress", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Stress"):
                opp_val = getattr(value, "giraffeDSL_Stress", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Stress", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_DeployAppFeature:

    def __init__(self, many: str, name: str, giraffeDSL_DeployAppFeature: "giraffeDSL_Deploy" = None, giraffeDSL_DeployAppFeature26: "giraffeDSL_DeployApp" = None):
        self.many = many
        self.name = name
        self.giraffeDSL_DeployAppFeature = giraffeDSL_DeployAppFeature
        self.giraffeDSL_DeployAppFeature26 = giraffeDSL_DeployAppFeature26
        
    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_DeployAppFeature(self):
        return self.__giraffeDSL_DeployAppFeature

    @giraffeDSL_DeployAppFeature.setter
    def giraffeDSL_DeployAppFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_DeployAppFeature__giraffeDSL_DeployAppFeature", None)
        self.__giraffeDSL_DeployAppFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Deploy"):
                opp_val = getattr(old_value, "giraffeDSL_Deploy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Deploy"):
                opp_val = getattr(value, "giraffeDSL_Deploy", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Deploy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def giraffeDSL_DeployAppFeature26(self):
        return self.__giraffeDSL_DeployAppFeature26

    @giraffeDSL_DeployAppFeature26.setter
    def giraffeDSL_DeployAppFeature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_DeployAppFeature__giraffeDSL_DeployAppFeature26", None)
        self.__giraffeDSL_DeployAppFeature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_DeployApp"):
                opp_val = getattr(old_value, "giraffeDSL_DeployApp", None)
                if opp_val == self:
                    setattr(old_value, "giraffeDSL_DeployApp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_DeployApp"):
                opp_val = getattr(value, "giraffeDSL_DeployApp", None)
                setattr(value, "giraffeDSL_DeployApp", self)

class CloudOptionalTypes:

    pass
class giraffeDSL_CloudUserType(CloudOptionalTypes):

    pass
class giraffeDSL_GeoZoneType(CloudOptionalTypes):

    pass
class giraffeDSL_CloudPasswordType(CloudOptionalTypes):

    pass
class giraffeDSL_ScriptType(CloudOptionalTypes):

    pass
class giraffeDSL_CloudOptionalTypes:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_CloudOptionalTypes: "giraffeDSL_CloudProvider" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_CloudOptionalTypes = giraffeDSL_CloudOptionalTypes
        
    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_CloudOptionalTypes(self):
        return self.__giraffeDSL_CloudOptionalTypes

    @giraffeDSL_CloudOptionalTypes.setter
    def giraffeDSL_CloudOptionalTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_CloudOptionalTypes__giraffeDSL_CloudOptionalTypes", None)
        self.__giraffeDSL_CloudOptionalTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_CloudProvider21"):
                opp_val = getattr(old_value, "giraffeDSL_CloudProvider21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_CloudProvider21"):
                opp_val = getattr(value, "giraffeDSL_CloudProvider21", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_CloudProvider21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_CloudCredentialType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_CloudCredentialType: "giraffeDSL_CloudProvider" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_CloudCredentialType = giraffeDSL_CloudCredentialType
        
    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def giraffeDSL_CloudCredentialType(self):
        return self.__giraffeDSL_CloudCredentialType

    @giraffeDSL_CloudCredentialType.setter
    def giraffeDSL_CloudCredentialType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_CloudCredentialType__giraffeDSL_CloudCredentialType", None)
        self.__giraffeDSL_CloudCredentialType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_CloudProvider19"):
                opp_val = getattr(old_value, "giraffeDSL_CloudProvider19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_CloudProvider19"):
                opp_val = getattr(value, "giraffeDSL_CloudProvider19", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_CloudProvider19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_MgmAddressType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_MgmAddressType: "giraffeDSL_CloudProvider" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_MgmAddressType = giraffeDSL_MgmAddressType
        
    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_MgmAddressType(self):
        return self.__giraffeDSL_MgmAddressType

    @giraffeDSL_MgmAddressType.setter
    def giraffeDSL_MgmAddressType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_MgmAddressType__giraffeDSL_MgmAddressType", None)
        self.__giraffeDSL_MgmAddressType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_CloudProvider17"):
                opp_val = getattr(old_value, "giraffeDSL_CloudProvider17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_CloudProvider17"):
                opp_val = getattr(value, "giraffeDSL_CloudProvider17", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_CloudProvider17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_CloudType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_CloudType: "giraffeDSL_CloudProvider" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_CloudType = giraffeDSL_CloudType
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def giraffeDSL_CloudType(self):
        return self.__giraffeDSL_CloudType

    @giraffeDSL_CloudType.setter
    def giraffeDSL_CloudType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_CloudType__giraffeDSL_CloudType", None)
        self.__giraffeDSL_CloudType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_CloudProvider15"):
                opp_val = getattr(old_value, "giraffeDSL_CloudProvider15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_CloudProvider15"):
                opp_val = getattr(value, "giraffeDSL_CloudProvider15", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_CloudProvider15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_DeployRangeType:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_DeployRangeType: "giraffeDSL_DeployType" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_DeployRangeType = giraffeDSL_DeployRangeType
        
    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_DeployRangeType(self):
        return self.__giraffeDSL_DeployRangeType

    @giraffeDSL_DeployRangeType.setter
    def giraffeDSL_DeployRangeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_DeployRangeType__giraffeDSL_DeployRangeType", None)
        self.__giraffeDSL_DeployRangeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_DeployType30"):
                opp_val = getattr(old_value, "giraffeDSL_DeployType30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_DeployType30"):
                opp_val = getattr(value, "giraffeDSL_DeployType30", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_DeployType30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_DeployTypeFeature:

    def __init__(self, many: str, name: str, giraffeDSL_DeployTypeFeature: "giraffeDSL_Deploy" = None, giraffeDSL_DeployTypeFeature28: "giraffeDSL_DeployType" = None):
        self.many = many
        self.name = name
        self.giraffeDSL_DeployTypeFeature = giraffeDSL_DeployTypeFeature
        self.giraffeDSL_DeployTypeFeature28 = giraffeDSL_DeployTypeFeature28
        
    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_DeployTypeFeature(self):
        return self.__giraffeDSL_DeployTypeFeature

    @giraffeDSL_DeployTypeFeature.setter
    def giraffeDSL_DeployTypeFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_DeployTypeFeature__giraffeDSL_DeployTypeFeature", None)
        self.__giraffeDSL_DeployTypeFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Deploy24"):
                opp_val = getattr(old_value, "giraffeDSL_Deploy24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Deploy24"):
                opp_val = getattr(value, "giraffeDSL_Deploy24", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Deploy24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def giraffeDSL_DeployTypeFeature28(self):
        return self.__giraffeDSL_DeployTypeFeature28

    @giraffeDSL_DeployTypeFeature28.setter
    def giraffeDSL_DeployTypeFeature28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_DeployTypeFeature__giraffeDSL_DeployTypeFeature28", None)
        self.__giraffeDSL_DeployTypeFeature28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_DeployType"):
                opp_val = getattr(old_value, "giraffeDSL_DeployType", None)
                if opp_val == self:
                    setattr(old_value, "giraffeDSL_DeployType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_DeployType"):
                opp_val = getattr(value, "giraffeDSL_DeployType", None)
                setattr(value, "giraffeDSL_DeployType", self)

class giraffeDSL_VirtualMachineTypeFeature:

    def __init__(self, many: str, name: str, type: str, giraffeDSL_VirtualMachineTypeFeature: "giraffeDSL_VirtualMachine" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_VirtualMachineTypeFeature = giraffeDSL_VirtualMachineTypeFeature
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def giraffeDSL_VirtualMachineTypeFeature(self):
        return self.__giraffeDSL_VirtualMachineTypeFeature

    @giraffeDSL_VirtualMachineTypeFeature.setter
    def giraffeDSL_VirtualMachineTypeFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_VirtualMachineTypeFeature__giraffeDSL_VirtualMachineTypeFeature", None)
        self.__giraffeDSL_VirtualMachineTypeFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_VirtualMachine9"):
                opp_val = getattr(old_value, "giraffeDSL_VirtualMachine9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_VirtualMachine9"):
                opp_val = getattr(value, "giraffeDSL_VirtualMachine9", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_VirtualMachine9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_DomainModel:

    pass
class giraffeDSL_InitIncrementFeature:

    def __init__(self, many: str, name: str, type: int, giraffeDSL_InitIncrementFeature: "giraffeDSL_Create" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_InitIncrementFeature = giraffeDSL_InitIncrementFeature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def giraffeDSL_InitIncrementFeature(self):
        return self.__giraffeDSL_InitIncrementFeature

    @giraffeDSL_InitIncrementFeature.setter
    def giraffeDSL_InitIncrementFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_InitIncrementFeature__giraffeDSL_InitIncrementFeature", None)
        self.__giraffeDSL_InitIncrementFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Create5"):
                opp_val = getattr(old_value, "giraffeDSL_Create5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Create5"):
                opp_val = getattr(value, "giraffeDSL_Create5", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Create5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_InitMachinesFeature:

    def __init__(self, many: str, name: str, type: int, giraffeDSL_InitMachinesFeature: "giraffeDSL_Create" = None):
        self.many = many
        self.name = name
        self.type = type
        self.giraffeDSL_InitMachinesFeature = giraffeDSL_InitMachinesFeature
        
    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_InitMachinesFeature(self):
        return self.__giraffeDSL_InitMachinesFeature

    @giraffeDSL_InitMachinesFeature.setter
    def giraffeDSL_InitMachinesFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_InitMachinesFeature__giraffeDSL_InitMachinesFeature", None)
        self.__giraffeDSL_InitMachinesFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Create3"):
                opp_val = getattr(old_value, "giraffeDSL_Create3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Create3"):
                opp_val = getattr(value, "giraffeDSL_Create3", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Create3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_VirtualMachineFeature:

    def __init__(self, many: str, name: str, giraffeDSL_VirtualMachineFeature: "giraffeDSL_Create" = None, giraffeDSL_VirtualMachineFeature7: "giraffeDSL_VirtualMachine" = None):
        self.many = many
        self.name = name
        self.giraffeDSL_VirtualMachineFeature = giraffeDSL_VirtualMachineFeature
        self.giraffeDSL_VirtualMachineFeature7 = giraffeDSL_VirtualMachineFeature7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def giraffeDSL_VirtualMachineFeature7(self):
        return self.__giraffeDSL_VirtualMachineFeature7

    @giraffeDSL_VirtualMachineFeature7.setter
    def giraffeDSL_VirtualMachineFeature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_VirtualMachineFeature__giraffeDSL_VirtualMachineFeature7", None)
        self.__giraffeDSL_VirtualMachineFeature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_VirtualMachine"):
                opp_val = getattr(old_value, "giraffeDSL_VirtualMachine", None)
                if opp_val == self:
                    setattr(old_value, "giraffeDSL_VirtualMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_VirtualMachine"):
                opp_val = getattr(value, "giraffeDSL_VirtualMachine", None)
                setattr(value, "giraffeDSL_VirtualMachine", self)

    @property
    def giraffeDSL_VirtualMachineFeature(self):
        return self.__giraffeDSL_VirtualMachineFeature

    @giraffeDSL_VirtualMachineFeature.setter
    def giraffeDSL_VirtualMachineFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_VirtualMachineFeature__giraffeDSL_VirtualMachineFeature", None)
        self.__giraffeDSL_VirtualMachineFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_Create"):
                opp_val = getattr(old_value, "giraffeDSL_Create", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_Create"):
                opp_val = getattr(value, "giraffeDSL_Create", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_Create", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class giraffeDSL_Monitor(Type):

    pass
class giraffeDSL_Action(Type):

    pass
class giraffeDSL_VirtualMachine(Type):

    pass
class giraffeDSL_DeployType(Type):

    pass
class giraffeDSL_Deploy(Type):

    pass
class giraffeDSL_DeployApp(Type):

    pass
class giraffeDSL_Stress(Type):

    pass
class giraffeDSL_CloudProvider(Type):

    pass
class giraffeDSL_Create(Type):

    pass
class giraffeDSL_Type:

    def __init__(self, name: str, giraffeDSL_Type: "giraffeDSL_DomainModel" = None):
        self.name = name
        self.giraffeDSL_Type = giraffeDSL_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def giraffeDSL_Type(self):
        return self.__giraffeDSL_Type

    @giraffeDSL_Type.setter
    def giraffeDSL_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_Type__giraffeDSL_Type", None)
        self.__giraffeDSL_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_DomainModel"):
                opp_val = getattr(old_value, "giraffeDSL_DomainModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_DomainModel"):
                opp_val = getattr(value, "giraffeDSL_DomainModel", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_DomainModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class giraffeDSL_CloudProviderType:

    def __init__(self, many: str, name: str, giraffeDSL_CloudProviderType: "giraffeDSL_VirtualMachine" = None, giraffeDSL_CloudProviderType13: "giraffeDSL_CloudProvider" = None):
        self.many = many
        self.name = name
        self.giraffeDSL_CloudProviderType = giraffeDSL_CloudProviderType
        self.giraffeDSL_CloudProviderType13 = giraffeDSL_CloudProviderType13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> str:
        return self.__many

    @many.setter
    def many(self, many: str):
        self.__many = many

    @property
    def giraffeDSL_CloudProviderType13(self):
        return self.__giraffeDSL_CloudProviderType13

    @giraffeDSL_CloudProviderType13.setter
    def giraffeDSL_CloudProviderType13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_CloudProviderType__giraffeDSL_CloudProviderType13", None)
        self.__giraffeDSL_CloudProviderType13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_CloudProvider"):
                opp_val = getattr(old_value, "giraffeDSL_CloudProvider", None)
                if opp_val == self:
                    setattr(old_value, "giraffeDSL_CloudProvider", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_CloudProvider"):
                opp_val = getattr(value, "giraffeDSL_CloudProvider", None)
                setattr(value, "giraffeDSL_CloudProvider", self)

    @property
    def giraffeDSL_CloudProviderType(self):
        return self.__giraffeDSL_CloudProviderType

    @giraffeDSL_CloudProviderType.setter
    def giraffeDSL_CloudProviderType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_giraffeDSL_CloudProviderType__giraffeDSL_CloudProviderType", None)
        self.__giraffeDSL_CloudProviderType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "giraffeDSL_VirtualMachine11"):
                opp_val = getattr(old_value, "giraffeDSL_VirtualMachine11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "giraffeDSL_VirtualMachine11"):
                opp_val = getattr(value, "giraffeDSL_VirtualMachine11", None)
                if opp_val is None:
                    setattr(value, "giraffeDSL_VirtualMachine11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
