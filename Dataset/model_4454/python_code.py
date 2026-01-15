from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class iOTConnector_SendAction:

    def __init__(self, number: int, iOTConnector_SendAction: "iOTConnector_Send" = None, iOTConnector_SendAction60: "iOTConnector_ReadingName" = None, iOTConnector_SendAction63: "iOTConnector_RelationalOperator" = None):
        self.number = number
        self.iOTConnector_SendAction = iOTConnector_SendAction
        self.iOTConnector_SendAction60 = iOTConnector_SendAction60
        self.iOTConnector_SendAction63 = iOTConnector_SendAction63
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def iOTConnector_SendAction60(self):
        return self.__iOTConnector_SendAction60

    @iOTConnector_SendAction60.setter
    def iOTConnector_SendAction60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_SendAction__iOTConnector_SendAction60", None)
        self.__iOTConnector_SendAction60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_ReadingName61"):
                opp_val = getattr(old_value, "iOTConnector_ReadingName61", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_ReadingName61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_ReadingName61"):
                opp_val = getattr(value, "iOTConnector_ReadingName61", None)
                setattr(value, "iOTConnector_ReadingName61", self)

    @property
    def iOTConnector_SendAction63(self):
        return self.__iOTConnector_SendAction63

    @iOTConnector_SendAction63.setter
    def iOTConnector_SendAction63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_SendAction__iOTConnector_SendAction63", None)
        self.__iOTConnector_SendAction63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_RelationalOperator64"):
                opp_val = getattr(old_value, "iOTConnector_RelationalOperator64", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_RelationalOperator64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_RelationalOperator64"):
                opp_val = getattr(value, "iOTConnector_RelationalOperator64", None)
                setattr(value, "iOTConnector_RelationalOperator64", self)

    @property
    def iOTConnector_SendAction(self):
        return self.__iOTConnector_SendAction

    @iOTConnector_SendAction.setter
    def iOTConnector_SendAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_SendAction__iOTConnector_SendAction", None)
        self.__iOTConnector_SendAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Send58"):
                opp_val = getattr(old_value, "iOTConnector_Send58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Send58"):
                opp_val = getattr(value, "iOTConnector_Send58", None)
                if opp_val is None:
                    setattr(value, "iOTConnector_Send58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Expression:

    pass
class iOTConnector_Var(Expression):

    pass
class iOTConnector_Div(Expression):

    pass
class iOTConnector_Mult(Expression):

    pass
class iOTConnector_Num(Expression):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class iOTConnector_Minus(Expression):

    pass
class iOTConnector_Plus(Expression):

    pass
class iOTConnector_FilterExp:

    def __init__(self, number: int, iOTConnector_FilterExp41: "iOTConnector_ReadingNameWithConfigScope" = None, iOTConnector_FilterExp44: "iOTConnector_RelationalOperator" = None, iOTConnector_FilterExp47: "iOTConnector_BitwiseOperator" = None, iOTConnector_FilterExp50: "iOTConnector_FilterExp" = None, iOTConnector_FilterExp48: "iOTConnector_FilterExp" = None, iOTConnector_FilterExp: "iOTConnector_FilterAction" = None):
        self.number = number
        self.iOTConnector_FilterExp41 = iOTConnector_FilterExp41
        self.iOTConnector_FilterExp44 = iOTConnector_FilterExp44
        self.iOTConnector_FilterExp47 = iOTConnector_FilterExp47
        self.iOTConnector_FilterExp50 = iOTConnector_FilterExp50
        self.iOTConnector_FilterExp48 = iOTConnector_FilterExp48
        self.iOTConnector_FilterExp = iOTConnector_FilterExp
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def iOTConnector_FilterExp44(self):
        return self.__iOTConnector_FilterExp44

    @iOTConnector_FilterExp44.setter
    def iOTConnector_FilterExp44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterExp__iOTConnector_FilterExp44", None)
        self.__iOTConnector_FilterExp44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_RelationalOperator45"):
                opp_val = getattr(old_value, "iOTConnector_RelationalOperator45", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_RelationalOperator45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_RelationalOperator45"):
                opp_val = getattr(value, "iOTConnector_RelationalOperator45", None)
                setattr(value, "iOTConnector_RelationalOperator45", self)

    @property
    def iOTConnector_FilterExp48(self):
        return self.__iOTConnector_FilterExp48

    @iOTConnector_FilterExp48.setter
    def iOTConnector_FilterExp48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterExp__iOTConnector_FilterExp48", None)
        self.__iOTConnector_FilterExp48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_FilterExp50"):
                opp_val = getattr(old_value, "iOTConnector_FilterExp50", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_FilterExp50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_FilterExp50"):
                opp_val = getattr(value, "iOTConnector_FilterExp50", None)
                setattr(value, "iOTConnector_FilterExp50", self)

    @property
    def iOTConnector_FilterExp47(self):
        return self.__iOTConnector_FilterExp47

    @iOTConnector_FilterExp47.setter
    def iOTConnector_FilterExp47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterExp__iOTConnector_FilterExp47", None)
        self.__iOTConnector_FilterExp47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_BitwiseOperator"):
                opp_val = getattr(old_value, "iOTConnector_BitwiseOperator", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_BitwiseOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_BitwiseOperator"):
                opp_val = getattr(value, "iOTConnector_BitwiseOperator", None)
                setattr(value, "iOTConnector_BitwiseOperator", self)

    @property
    def iOTConnector_FilterExp(self):
        return self.__iOTConnector_FilterExp

    @iOTConnector_FilterExp.setter
    def iOTConnector_FilterExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterExp__iOTConnector_FilterExp", None)
        self.__iOTConnector_FilterExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_FilterAction39"):
                opp_val = getattr(old_value, "iOTConnector_FilterAction39", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_FilterAction39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_FilterAction39"):
                opp_val = getattr(value, "iOTConnector_FilterAction39", None)
                setattr(value, "iOTConnector_FilterAction39", self)

    @property
    def iOTConnector_FilterExp41(self):
        return self.__iOTConnector_FilterExp41

    @iOTConnector_FilterExp41.setter
    def iOTConnector_FilterExp41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterExp__iOTConnector_FilterExp41", None)
        self.__iOTConnector_FilterExp41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_ReadingNameWithConfigScope42"):
                opp_val = getattr(old_value, "iOTConnector_ReadingNameWithConfigScope42", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_ReadingNameWithConfigScope42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_ReadingNameWithConfigScope42"):
                opp_val = getattr(value, "iOTConnector_ReadingNameWithConfigScope42", None)
                setattr(value, "iOTConnector_ReadingNameWithConfigScope42", self)

    @property
    def iOTConnector_FilterExp50(self):
        return self.__iOTConnector_FilterExp50

    @iOTConnector_FilterExp50.setter
    def iOTConnector_FilterExp50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterExp__iOTConnector_FilterExp50", None)
        self.__iOTConnector_FilterExp50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_FilterExp48"):
                opp_val = getattr(old_value, "iOTConnector_FilterExp48", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_FilterExp48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_FilterExp48"):
                opp_val = getattr(value, "iOTConnector_FilterExp48", None)
                setattr(value, "iOTConnector_FilterExp48", self)

class iOTConnector_FilterType:

    def __init__(self, value: str, iOTConnector_FilterType: "iOTConnector_FilterAction" = None):
        self.value = value
        self.iOTConnector_FilterType = iOTConnector_FilterType
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def iOTConnector_FilterType(self):
        return self.__iOTConnector_FilterType

    @iOTConnector_FilterType.setter
    def iOTConnector_FilterType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterType__iOTConnector_FilterType", None)
        self.__iOTConnector_FilterType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_FilterAction37"):
                opp_val = getattr(old_value, "iOTConnector_FilterAction37", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_FilterAction37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_FilterAction37"):
                opp_val = getattr(value, "iOTConnector_FilterAction37", None)
                setattr(value, "iOTConnector_FilterAction37", self)

class iOTConnector_FilterAction:

    def __init__(self, number: int, iOTConnector_FilterAction39: "iOTConnector_FilterExp" = None, iOTConnector_FilterAction: "iOTConnector_Filter" = None, iOTConnector_FilterAction34: "iOTConnector_ReadingName" = None, iOTConnector_FilterAction37: "iOTConnector_FilterType" = None):
        self.number = number
        self.iOTConnector_FilterAction39 = iOTConnector_FilterAction39
        self.iOTConnector_FilterAction = iOTConnector_FilterAction
        self.iOTConnector_FilterAction34 = iOTConnector_FilterAction34
        self.iOTConnector_FilterAction37 = iOTConnector_FilterAction37
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def iOTConnector_FilterAction34(self):
        return self.__iOTConnector_FilterAction34

    @iOTConnector_FilterAction34.setter
    def iOTConnector_FilterAction34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterAction__iOTConnector_FilterAction34", None)
        self.__iOTConnector_FilterAction34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_ReadingName35"):
                opp_val = getattr(old_value, "iOTConnector_ReadingName35", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_ReadingName35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_ReadingName35"):
                opp_val = getattr(value, "iOTConnector_ReadingName35", None)
                setattr(value, "iOTConnector_ReadingName35", self)

    @property
    def iOTConnector_FilterAction(self):
        return self.__iOTConnector_FilterAction

    @iOTConnector_FilterAction.setter
    def iOTConnector_FilterAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterAction__iOTConnector_FilterAction", None)
        self.__iOTConnector_FilterAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Filter"):
                opp_val = getattr(old_value, "iOTConnector_Filter", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Filter"):
                opp_val = getattr(value, "iOTConnector_Filter", None)
                if opp_val is None:
                    setattr(value, "iOTConnector_Filter", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iOTConnector_FilterAction39(self):
        return self.__iOTConnector_FilterAction39

    @iOTConnector_FilterAction39.setter
    def iOTConnector_FilterAction39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterAction__iOTConnector_FilterAction39", None)
        self.__iOTConnector_FilterAction39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_FilterExp"):
                opp_val = getattr(old_value, "iOTConnector_FilterExp", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_FilterExp", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_FilterExp"):
                opp_val = getattr(value, "iOTConnector_FilterExp", None)
                setattr(value, "iOTConnector_FilterExp", self)

    @property
    def iOTConnector_FilterAction37(self):
        return self.__iOTConnector_FilterAction37

    @iOTConnector_FilterAction37.setter
    def iOTConnector_FilterAction37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_FilterAction__iOTConnector_FilterAction37", None)
        self.__iOTConnector_FilterAction37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_FilterType"):
                opp_val = getattr(old_value, "iOTConnector_FilterType", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_FilterType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_FilterType"):
                opp_val = getattr(value, "iOTConnector_FilterType", None)
                setattr(value, "iOTConnector_FilterType", self)

class iOTConnector_TimeUnit:

    def __init__(self, value: str, iOTConnector_TimeUnit: "iOTConnector_SampleAction" = None):
        self.value = value
        self.iOTConnector_TimeUnit = iOTConnector_TimeUnit
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def iOTConnector_TimeUnit(self):
        return self.__iOTConnector_TimeUnit

    @iOTConnector_TimeUnit.setter
    def iOTConnector_TimeUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_TimeUnit__iOTConnector_TimeUnit", None)
        self.__iOTConnector_TimeUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_SampleAction31"):
                opp_val = getattr(old_value, "iOTConnector_SampleAction31", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_SampleAction31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_SampleAction31"):
                opp_val = getattr(value, "iOTConnector_SampleAction31", None)
                setattr(value, "iOTConnector_SampleAction31", self)

class iOTConnector_RelationalOperator:

    def __init__(self, value: str, iOTConnector_RelationalOperator45: "iOTConnector_FilterExp" = None, iOTConnector_RelationalOperator: "iOTConnector_SampleAction" = None, iOTConnector_RelationalOperator64: "iOTConnector_SendAction" = None):
        self.value = value
        self.iOTConnector_RelationalOperator45 = iOTConnector_RelationalOperator45
        self.iOTConnector_RelationalOperator = iOTConnector_RelationalOperator
        self.iOTConnector_RelationalOperator64 = iOTConnector_RelationalOperator64
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def iOTConnector_RelationalOperator(self):
        return self.__iOTConnector_RelationalOperator

    @iOTConnector_RelationalOperator.setter
    def iOTConnector_RelationalOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_RelationalOperator__iOTConnector_RelationalOperator", None)
        self.__iOTConnector_RelationalOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_SampleAction29"):
                opp_val = getattr(old_value, "iOTConnector_SampleAction29", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_SampleAction29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_SampleAction29"):
                opp_val = getattr(value, "iOTConnector_SampleAction29", None)
                setattr(value, "iOTConnector_SampleAction29", self)

    @property
    def iOTConnector_RelationalOperator64(self):
        return self.__iOTConnector_RelationalOperator64

    @iOTConnector_RelationalOperator64.setter
    def iOTConnector_RelationalOperator64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_RelationalOperator__iOTConnector_RelationalOperator64", None)
        self.__iOTConnector_RelationalOperator64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_SendAction63"):
                opp_val = getattr(old_value, "iOTConnector_SendAction63", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_SendAction63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_SendAction63"):
                opp_val = getattr(value, "iOTConnector_SendAction63", None)
                setattr(value, "iOTConnector_SendAction63", self)

    @property
    def iOTConnector_RelationalOperator45(self):
        return self.__iOTConnector_RelationalOperator45

    @iOTConnector_RelationalOperator45.setter
    def iOTConnector_RelationalOperator45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_RelationalOperator__iOTConnector_RelationalOperator45", None)
        self.__iOTConnector_RelationalOperator45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_FilterExp44"):
                opp_val = getattr(old_value, "iOTConnector_FilterExp44", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_FilterExp44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_FilterExp44"):
                opp_val = getattr(value, "iOTConnector_FilterExp44", None)
                setattr(value, "iOTConnector_FilterExp44", self)

class iOTConnector_Expression:

    pass
class iOTConnector_ProcessAction:

    pass
class iOTConnector_BitwiseOperator:

    def __init__(self, value: str, iOTConnector_BitwiseOperator: "iOTConnector_FilterExp" = None):
        self.value = value
        self.iOTConnector_BitwiseOperator = iOTConnector_BitwiseOperator
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def iOTConnector_BitwiseOperator(self):
        return self.__iOTConnector_BitwiseOperator

    @iOTConnector_BitwiseOperator.setter
    def iOTConnector_BitwiseOperator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_BitwiseOperator__iOTConnector_BitwiseOperator", None)
        self.__iOTConnector_BitwiseOperator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_FilterExp47"):
                opp_val = getattr(old_value, "iOTConnector_FilterExp47", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_FilterExp47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_FilterExp47"):
                opp_val = getattr(value, "iOTConnector_FilterExp47", None)
                setattr(value, "iOTConnector_FilterExp47", self)

class iOTConnector_SensorConfig:

    def __init__(self, pinOut: str, name: str, pinIn: str, iOTConnector_SensorConfig: "iOTConnector_Board" = None):
        self.pinOut = pinOut
        self.name = name
        self.pinIn = pinIn
        self.iOTConnector_SensorConfig = iOTConnector_SensorConfig
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pinIn(self) -> str:
        return self.__pinIn

    @pinIn.setter
    def pinIn(self, pinIn: str):
        self.__pinIn = pinIn

    @property
    def pinOut(self) -> str:
        return self.__pinOut

    @pinOut.setter
    def pinOut(self, pinOut: str):
        self.__pinOut = pinOut

    @property
    def iOTConnector_SensorConfig(self):
        return self.__iOTConnector_SensorConfig

    @iOTConnector_SensorConfig.setter
    def iOTConnector_SensorConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_SensorConfig__iOTConnector_SensorConfig", None)
        self.__iOTConnector_SensorConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Board10"):
                opp_val = getattr(old_value, "iOTConnector_Board10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Board10"):
                opp_val = getattr(value, "iOTConnector_Board10", None)
                if opp_val is None:
                    setattr(value, "iOTConnector_Board10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iOTConnector_Sensor:

    def __init__(self, name: str, type: str, iOTConnector_Sensor15: "iOTConnector_Output" = None, iOTConnector_Sensor17: set["iOTConnector_Function"] = None, iOTConnector_Sensor19: "iOTConnector_Send" = None, iOTConnector_Sensor: "iOTConnector_Config" = None):
        self.name = name
        self.type = type
        self.iOTConnector_Sensor15 = iOTConnector_Sensor15
        self.iOTConnector_Sensor17 = iOTConnector_Sensor17 if iOTConnector_Sensor17 is not None else set()
        self.iOTConnector_Sensor19 = iOTConnector_Sensor19
        self.iOTConnector_Sensor = iOTConnector_Sensor
        
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
    def iOTConnector_Sensor17(self):
        return self.__iOTConnector_Sensor17

    @iOTConnector_Sensor17.setter
    def iOTConnector_Sensor17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Sensor__iOTConnector_Sensor17", None)
        self.__iOTConnector_Sensor17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iOTConnector_Function"):
                    opp_val = getattr(item, "iOTConnector_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "iOTConnector_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iOTConnector_Function"):
                    opp_val = getattr(item, "iOTConnector_Function", None)
                    
                    setattr(item, "iOTConnector_Function", self)
                    

    @property
    def iOTConnector_Sensor15(self):
        return self.__iOTConnector_Sensor15

    @iOTConnector_Sensor15.setter
    def iOTConnector_Sensor15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Sensor__iOTConnector_Sensor15", None)
        self.__iOTConnector_Sensor15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Output"):
                opp_val = getattr(old_value, "iOTConnector_Output", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_Output", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Output"):
                opp_val = getattr(value, "iOTConnector_Output", None)
                setattr(value, "iOTConnector_Output", self)

    @property
    def iOTConnector_Sensor(self):
        return self.__iOTConnector_Sensor

    @iOTConnector_Sensor.setter
    def iOTConnector_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Sensor__iOTConnector_Sensor", None)
        self.__iOTConnector_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Config8"):
                opp_val = getattr(old_value, "iOTConnector_Config8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Config8"):
                opp_val = getattr(value, "iOTConnector_Config8", None)
                if opp_val is None:
                    setattr(value, "iOTConnector_Config8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iOTConnector_Sensor19(self):
        return self.__iOTConnector_Sensor19

    @iOTConnector_Sensor19.setter
    def iOTConnector_Sensor19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Sensor__iOTConnector_Sensor19", None)
        self.__iOTConnector_Sensor19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Send"):
                opp_val = getattr(old_value, "iOTConnector_Send", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_Send", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Send"):
                opp_val = getattr(value, "iOTConnector_Send", None)
                setattr(value, "iOTConnector_Send", self)

class iOTConnector_ReadingNameWithConfigScope:

    pass
class iOTConnector_SampleAction:

    def __init__(self, number: int, amountOfTime: int, iOTConnector_SampleAction: "iOTConnector_Sample" = None, iOTConnector_SampleAction24: "iOTConnector_ReadingName" = None, iOTConnector_SampleAction27: "iOTConnector_ReadingNameWithConfigScope" = None, iOTConnector_SampleAction29: "iOTConnector_RelationalOperator" = None, iOTConnector_SampleAction31: "iOTConnector_TimeUnit" = None):
        self.number = number
        self.amountOfTime = amountOfTime
        self.iOTConnector_SampleAction = iOTConnector_SampleAction
        self.iOTConnector_SampleAction24 = iOTConnector_SampleAction24
        self.iOTConnector_SampleAction27 = iOTConnector_SampleAction27
        self.iOTConnector_SampleAction29 = iOTConnector_SampleAction29
        self.iOTConnector_SampleAction31 = iOTConnector_SampleAction31
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def amountOfTime(self) -> int:
        return self.__amountOfTime

    @amountOfTime.setter
    def amountOfTime(self, amountOfTime: int):
        self.__amountOfTime = amountOfTime

    @property
    def iOTConnector_SampleAction29(self):
        return self.__iOTConnector_SampleAction29

    @iOTConnector_SampleAction29.setter
    def iOTConnector_SampleAction29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_SampleAction__iOTConnector_SampleAction29", None)
        self.__iOTConnector_SampleAction29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_RelationalOperator"):
                opp_val = getattr(old_value, "iOTConnector_RelationalOperator", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_RelationalOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_RelationalOperator"):
                opp_val = getattr(value, "iOTConnector_RelationalOperator", None)
                setattr(value, "iOTConnector_RelationalOperator", self)

    @property
    def iOTConnector_SampleAction24(self):
        return self.__iOTConnector_SampleAction24

    @iOTConnector_SampleAction24.setter
    def iOTConnector_SampleAction24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_SampleAction__iOTConnector_SampleAction24", None)
        self.__iOTConnector_SampleAction24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_ReadingName25"):
                opp_val = getattr(old_value, "iOTConnector_ReadingName25", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_ReadingName25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_ReadingName25"):
                opp_val = getattr(value, "iOTConnector_ReadingName25", None)
                setattr(value, "iOTConnector_ReadingName25", self)

    @property
    def iOTConnector_SampleAction27(self):
        return self.__iOTConnector_SampleAction27

    @iOTConnector_SampleAction27.setter
    def iOTConnector_SampleAction27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_SampleAction__iOTConnector_SampleAction27", None)
        self.__iOTConnector_SampleAction27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_ReadingNameWithConfigScope"):
                opp_val = getattr(old_value, "iOTConnector_ReadingNameWithConfigScope", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_ReadingNameWithConfigScope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_ReadingNameWithConfigScope"):
                opp_val = getattr(value, "iOTConnector_ReadingNameWithConfigScope", None)
                setattr(value, "iOTConnector_ReadingNameWithConfigScope", self)

    @property
    def iOTConnector_SampleAction31(self):
        return self.__iOTConnector_SampleAction31

    @iOTConnector_SampleAction31.setter
    def iOTConnector_SampleAction31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_SampleAction__iOTConnector_SampleAction31", None)
        self.__iOTConnector_SampleAction31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_TimeUnit"):
                opp_val = getattr(old_value, "iOTConnector_TimeUnit", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_TimeUnit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_TimeUnit"):
                opp_val = getattr(value, "iOTConnector_TimeUnit", None)
                setattr(value, "iOTConnector_TimeUnit", self)

    @property
    def iOTConnector_SampleAction(self):
        return self.__iOTConnector_SampleAction

    @iOTConnector_SampleAction.setter
    def iOTConnector_SampleAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_SampleAction__iOTConnector_SampleAction", None)
        self.__iOTConnector_SampleAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Sample"):
                opp_val = getattr(old_value, "iOTConnector_Sample", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Sample"):
                opp_val = getattr(value, "iOTConnector_Sample", None)
                if opp_val is None:
                    setattr(value, "iOTConnector_Sample", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Function:

    pass
class iOTConnector_Filter(Function):

    pass
class iOTConnector_Process(Function):

    pass
class iOTConnector_Sample(Function):

    pass
class iOTConnector_ReadingName:

    def __init__(self, name: str, iOTConnector_ReadingName: "iOTConnector_Output" = None, iOTConnector_ReadingName25: "iOTConnector_SampleAction" = None, iOTConnector_ReadingName54: "iOTConnector_ProcessAction" = None, iOTConnector_ReadingName35: "iOTConnector_FilterAction" = None, iOTConnector_ReadingName61: "iOTConnector_SendAction" = None, iOTConnector_ReadingName67: "iOTConnector_ReadingNameWithConfigScope" = None):
        self.name = name
        self.iOTConnector_ReadingName = iOTConnector_ReadingName
        self.iOTConnector_ReadingName25 = iOTConnector_ReadingName25
        self.iOTConnector_ReadingName54 = iOTConnector_ReadingName54
        self.iOTConnector_ReadingName35 = iOTConnector_ReadingName35
        self.iOTConnector_ReadingName61 = iOTConnector_ReadingName61
        self.iOTConnector_ReadingName67 = iOTConnector_ReadingName67
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iOTConnector_ReadingName35(self):
        return self.__iOTConnector_ReadingName35

    @iOTConnector_ReadingName35.setter
    def iOTConnector_ReadingName35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_ReadingName__iOTConnector_ReadingName35", None)
        self.__iOTConnector_ReadingName35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_FilterAction34"):
                opp_val = getattr(old_value, "iOTConnector_FilterAction34", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_FilterAction34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_FilterAction34"):
                opp_val = getattr(value, "iOTConnector_FilterAction34", None)
                setattr(value, "iOTConnector_FilterAction34", self)

    @property
    def iOTConnector_ReadingName(self):
        return self.__iOTConnector_ReadingName

    @iOTConnector_ReadingName.setter
    def iOTConnector_ReadingName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_ReadingName__iOTConnector_ReadingName", None)
        self.__iOTConnector_ReadingName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Output21"):
                opp_val = getattr(old_value, "iOTConnector_Output21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Output21"):
                opp_val = getattr(value, "iOTConnector_Output21", None)
                if opp_val is None:
                    setattr(value, "iOTConnector_Output21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iOTConnector_ReadingName67(self):
        return self.__iOTConnector_ReadingName67

    @iOTConnector_ReadingName67.setter
    def iOTConnector_ReadingName67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_ReadingName__iOTConnector_ReadingName67", None)
        self.__iOTConnector_ReadingName67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_ReadingNameWithConfigScope66"):
                opp_val = getattr(old_value, "iOTConnector_ReadingNameWithConfigScope66", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_ReadingNameWithConfigScope66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_ReadingNameWithConfigScope66"):
                opp_val = getattr(value, "iOTConnector_ReadingNameWithConfigScope66", None)
                setattr(value, "iOTConnector_ReadingNameWithConfigScope66", self)

    @property
    def iOTConnector_ReadingName61(self):
        return self.__iOTConnector_ReadingName61

    @iOTConnector_ReadingName61.setter
    def iOTConnector_ReadingName61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_ReadingName__iOTConnector_ReadingName61", None)
        self.__iOTConnector_ReadingName61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_SendAction60"):
                opp_val = getattr(old_value, "iOTConnector_SendAction60", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_SendAction60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_SendAction60"):
                opp_val = getattr(value, "iOTConnector_SendAction60", None)
                setattr(value, "iOTConnector_SendAction60", self)

    @property
    def iOTConnector_ReadingName54(self):
        return self.__iOTConnector_ReadingName54

    @iOTConnector_ReadingName54.setter
    def iOTConnector_ReadingName54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_ReadingName__iOTConnector_ReadingName54", None)
        self.__iOTConnector_ReadingName54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_ProcessAction53"):
                opp_val = getattr(old_value, "iOTConnector_ProcessAction53", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_ProcessAction53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_ProcessAction53"):
                opp_val = getattr(value, "iOTConnector_ProcessAction53", None)
                setattr(value, "iOTConnector_ProcessAction53", self)

    @property
    def iOTConnector_ReadingName25(self):
        return self.__iOTConnector_ReadingName25

    @iOTConnector_ReadingName25.setter
    def iOTConnector_ReadingName25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_ReadingName__iOTConnector_ReadingName25", None)
        self.__iOTConnector_ReadingName25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_SampleAction24"):
                opp_val = getattr(old_value, "iOTConnector_SampleAction24", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_SampleAction24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_SampleAction24"):
                opp_val = getattr(value, "iOTConnector_SampleAction24", None)
                setattr(value, "iOTConnector_SampleAction24", self)

class iOTConnector_Send:

    pass
class iOTConnector_Function:

    pass
class iOTConnector_Output:

    pass
class iOTConnector_Board:

    def __init__(self, name: str, iOTConnector_Board: "iOTConnector_Program" = None, iOTConnector_Board10: set["iOTConnector_SensorConfig"] = None, iOTConnector_Board12: "iOTConnector_Config" = None):
        self.name = name
        self.iOTConnector_Board = iOTConnector_Board
        self.iOTConnector_Board10 = iOTConnector_Board10 if iOTConnector_Board10 is not None else set()
        self.iOTConnector_Board12 = iOTConnector_Board12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iOTConnector_Board(self):
        return self.__iOTConnector_Board

    @iOTConnector_Board.setter
    def iOTConnector_Board(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Board__iOTConnector_Board", None)
        self.__iOTConnector_Board = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Program6"):
                opp_val = getattr(old_value, "iOTConnector_Program6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Program6"):
                opp_val = getattr(value, "iOTConnector_Program6", None)
                if opp_val is None:
                    setattr(value, "iOTConnector_Program6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iOTConnector_Board12(self):
        return self.__iOTConnector_Board12

    @iOTConnector_Board12.setter
    def iOTConnector_Board12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Board__iOTConnector_Board12", None)
        self.__iOTConnector_Board12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Config13"):
                opp_val = getattr(old_value, "iOTConnector_Config13", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_Config13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Config13"):
                opp_val = getattr(value, "iOTConnector_Config13", None)
                setattr(value, "iOTConnector_Config13", self)

    @property
    def iOTConnector_Board10(self):
        return self.__iOTConnector_Board10

    @iOTConnector_Board10.setter
    def iOTConnector_Board10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Board__iOTConnector_Board10", None)
        self.__iOTConnector_Board10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iOTConnector_SensorConfig"):
                    opp_val = getattr(item, "iOTConnector_SensorConfig", None)
                    
                    if opp_val == self:
                        setattr(item, "iOTConnector_SensorConfig", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iOTConnector_SensorConfig"):
                    opp_val = getattr(item, "iOTConnector_SensorConfig", None)
                    
                    setattr(item, "iOTConnector_SensorConfig", self)
                    

class iOTConnector_Config:

    def __init__(self, name: str, iOTConnector_Config: "iOTConnector_Program" = None, iOTConnector_Config8: set["iOTConnector_Sensor"] = None, iOTConnector_Config13: "iOTConnector_Board" = None):
        self.name = name
        self.iOTConnector_Config = iOTConnector_Config
        self.iOTConnector_Config8 = iOTConnector_Config8 if iOTConnector_Config8 is not None else set()
        self.iOTConnector_Config13 = iOTConnector_Config13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iOTConnector_Config8(self):
        return self.__iOTConnector_Config8

    @iOTConnector_Config8.setter
    def iOTConnector_Config8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Config__iOTConnector_Config8", None)
        self.__iOTConnector_Config8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "iOTConnector_Sensor"):
                    opp_val = getattr(item, "iOTConnector_Sensor", None)
                    
                    if opp_val == self:
                        setattr(item, "iOTConnector_Sensor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "iOTConnector_Sensor"):
                    opp_val = getattr(item, "iOTConnector_Sensor", None)
                    
                    setattr(item, "iOTConnector_Sensor", self)
                    

    @property
    def iOTConnector_Config(self):
        return self.__iOTConnector_Config

    @iOTConnector_Config.setter
    def iOTConnector_Config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Config__iOTConnector_Config", None)
        self.__iOTConnector_Config = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Program4"):
                opp_val = getattr(old_value, "iOTConnector_Program4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Program4"):
                opp_val = getattr(value, "iOTConnector_Program4", None)
                if opp_val is None:
                    setattr(value, "iOTConnector_Program4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def iOTConnector_Config13(self):
        return self.__iOTConnector_Config13

    @iOTConnector_Config13.setter
    def iOTConnector_Config13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Config__iOTConnector_Config13", None)
        self.__iOTConnector_Config13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Board12"):
                opp_val = getattr(old_value, "iOTConnector_Board12", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_Board12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Board12"):
                opp_val = getattr(value, "iOTConnector_Board12", None)
                setattr(value, "iOTConnector_Board12", self)

class iOTConnector_Wifi:

    def __init__(self, ssid: str, password: str, iOTConnector_Wifi: "iOTConnector_Program" = None):
        self.ssid = ssid
        self.password = password
        self.iOTConnector_Wifi = iOTConnector_Wifi
        
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def ssid(self) -> str:
        return self.__ssid

    @ssid.setter
    def ssid(self, ssid: str):
        self.__ssid = ssid

    @property
    def iOTConnector_Wifi(self):
        return self.__iOTConnector_Wifi

    @iOTConnector_Wifi.setter
    def iOTConnector_Wifi(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Wifi__iOTConnector_Wifi", None)
        self.__iOTConnector_Wifi = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Program2"):
                opp_val = getattr(old_value, "iOTConnector_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Program2"):
                opp_val = getattr(value, "iOTConnector_Program2", None)
                if opp_val is None:
                    setattr(value, "iOTConnector_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class iOTConnector_Webserver:

    def __init__(self, url: str, port: int, iOTConnector_Webserver: "iOTConnector_Program" = None):
        self.url = url
        self.port = port
        self.iOTConnector_Webserver = iOTConnector_Webserver
        
    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def iOTConnector_Webserver(self):
        return self.__iOTConnector_Webserver

    @iOTConnector_Webserver.setter
    def iOTConnector_Webserver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iOTConnector_Webserver__iOTConnector_Webserver", None)
        self.__iOTConnector_Webserver = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "iOTConnector_Program"):
                opp_val = getattr(old_value, "iOTConnector_Program", None)
                if opp_val == self:
                    setattr(old_value, "iOTConnector_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "iOTConnector_Program"):
                opp_val = getattr(value, "iOTConnector_Program", None)
                setattr(value, "iOTConnector_Program", self)

class iOTConnector_Program:

    pass