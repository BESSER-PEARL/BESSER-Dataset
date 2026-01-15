from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class metamodel_Condition(ABC):

    pass
class UnaryOperator:

    pass
class metamodel_Positive(UnaryOperator):

    pass
class metamodel_Negative(UnaryOperator):

    pass
class BinaryOperator:

    pass
class metamodel_Different(BinaryOperator):

    pass
class metamodel_MoreOrEqual(BinaryOperator):

    pass
class metamodel_Less(BinaryOperator):

    pass
class metamodel_LessOrEqual(BinaryOperator):

    pass
class metamodel_Sub(BinaryOperator):

    pass
class metamodel_Add(BinaryOperator):

    pass
class metamodel_More(BinaryOperator):

    pass
class metamodel_Equal(BinaryOperator):

    pass
class UnaryCond:

    pass
class metamodel_Negation(UnaryCond):

    pass
class BinaryCond:

    pass
class metamodel_And(BinaryCond):

    pass
class metamodel_Or(BinaryCond):

    pass
class Condition:

    pass
class metamodel_UnaryCond(Condition):

    pass
class metamodel_BinaryCond(Condition):

    pass
class metamodel_Operator(Condition):

    pass
class Operator:

    pass
class metamodel_BinaryOperator(Operator):

    pass
class metamodel_UnaryOperator(Operator):

    pass
class metamodel_Transition:

    def __init__(self, nameIn: str, metamodel_Transition: "metamodel_State" = None, metamodel_Transition33: "metamodel_State" = None, metamodel_Transition36: "metamodel_Condition" = None):
        self.nameIn = nameIn
        self.metamodel_Transition = metamodel_Transition
        self.metamodel_Transition33 = metamodel_Transition33
        self.metamodel_Transition36 = metamodel_Transition36
        
    @property
    def nameIn(self) -> str:
        return self.__nameIn

    @nameIn.setter
    def nameIn(self, nameIn: str):
        self.__nameIn = nameIn

    @property
    def metamodel_Transition(self):
        return self.__metamodel_Transition

    @metamodel_Transition.setter
    def metamodel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Transition__metamodel_Transition", None)
        self.__metamodel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_State22"):
                opp_val = getattr(old_value, "metamodel_State22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_State22"):
                opp_val = getattr(value, "metamodel_State22", None)
                if opp_val is None:
                    setattr(value, "metamodel_State22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_Transition33(self):
        return self.__metamodel_Transition33

    @metamodel_Transition33.setter
    def metamodel_Transition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Transition__metamodel_Transition33", None)
        self.__metamodel_Transition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_State34"):
                opp_val = getattr(old_value, "metamodel_State34", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_State34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_State34"):
                opp_val = getattr(value, "metamodel_State34", None)
                setattr(value, "metamodel_State34", self)

    @property
    def metamodel_Transition36(self):
        return self.__metamodel_Transition36

    @metamodel_Transition36.setter
    def metamodel_Transition36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Transition__metamodel_Transition36", None)
        self.__metamodel_Transition36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Condition"):
                opp_val = getattr(old_value, "metamodel_Condition", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Condition"):
                opp_val = getattr(value, "metamodel_Condition", None)
                setattr(value, "metamodel_Condition", self)

class metamodel_State:

    def __init__(self, name: str, isInitial: bool, uid: int, metamodel_State: "metamodel_StateMachine" = None, metamodel_State22: set["metamodel_Transition"] = None, metamodel_State24: "metamodel_Action" = None, metamodel_State27: "metamodel_Action" = None, metamodel_State30: "metamodel_Action" = None, metamodel_State34: "metamodel_Transition" = None):
        self.name = name
        self.isInitial = isInitial
        self.uid = uid
        self.metamodel_State = metamodel_State
        self.metamodel_State22 = metamodel_State22 if metamodel_State22 is not None else set()
        self.metamodel_State24 = metamodel_State24
        self.metamodel_State27 = metamodel_State27
        self.metamodel_State30 = metamodel_State30
        self.metamodel_State34 = metamodel_State34
        
    @property
    def uid(self) -> int:
        return self.__uid

    @uid.setter
    def uid(self, uid: int):
        self.__uid = uid

    @property
    def isInitial(self) -> bool:
        return self.__isInitial

    @isInitial.setter
    def isInitial(self, isInitial: bool):
        self.__isInitial = isInitial

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_State24(self):
        return self.__metamodel_State24

    @metamodel_State24.setter
    def metamodel_State24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_State__metamodel_State24", None)
        self.__metamodel_State24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Action25"):
                opp_val = getattr(old_value, "metamodel_Action25", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Action25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Action25"):
                opp_val = getattr(value, "metamodel_Action25", None)
                setattr(value, "metamodel_Action25", self)

    @property
    def metamodel_State30(self):
        return self.__metamodel_State30

    @metamodel_State30.setter
    def metamodel_State30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_State__metamodel_State30", None)
        self.__metamodel_State30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Action31"):
                opp_val = getattr(old_value, "metamodel_Action31", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Action31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Action31"):
                opp_val = getattr(value, "metamodel_Action31", None)
                setattr(value, "metamodel_Action31", self)

    @property
    def metamodel_State22(self):
        return self.__metamodel_State22

    @metamodel_State22.setter
    def metamodel_State22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_State__metamodel_State22", None)
        self.__metamodel_State22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Transition"):
                    opp_val = getattr(item, "metamodel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Transition"):
                    opp_val = getattr(item, "metamodel_Transition", None)
                    
                    setattr(item, "metamodel_Transition", self)
                    

    @property
    def metamodel_State(self):
        return self.__metamodel_State

    @metamodel_State.setter
    def metamodel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_State__metamodel_State", None)
        self.__metamodel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_StateMachine17"):
                opp_val = getattr(old_value, "metamodel_StateMachine17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_StateMachine17"):
                opp_val = getattr(value, "metamodel_StateMachine17", None)
                if opp_val is None:
                    setattr(value, "metamodel_StateMachine17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_State27(self):
        return self.__metamodel_State27

    @metamodel_State27.setter
    def metamodel_State27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_State__metamodel_State27", None)
        self.__metamodel_State27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Action28"):
                opp_val = getattr(old_value, "metamodel_Action28", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Action28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Action28"):
                opp_val = getattr(value, "metamodel_Action28", None)
                setattr(value, "metamodel_Action28", self)

    @property
    def metamodel_State34(self):
        return self.__metamodel_State34

    @metamodel_State34.setter
    def metamodel_State34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_State__metamodel_State34", None)
        self.__metamodel_State34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Transition33"):
                opp_val = getattr(old_value, "metamodel_Transition33", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Transition33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Transition33"):
                opp_val = getattr(value, "metamodel_Transition33", None)
                setattr(value, "metamodel_Transition33", self)

class metamodel_StateMachine:

    def __init__(self, name: str, metamodel_StateMachine: "metamodel_Behaviour" = None, metamodel_StateMachine17: set["metamodel_State"] = None, metamodel_StateMachine19: set["metamodel_Value"] = None):
        self.name = name
        self.metamodel_StateMachine = metamodel_StateMachine
        self.metamodel_StateMachine17 = metamodel_StateMachine17 if metamodel_StateMachine17 is not None else set()
        self.metamodel_StateMachine19 = metamodel_StateMachine19 if metamodel_StateMachine19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_StateMachine19(self):
        return self.__metamodel_StateMachine19

    @metamodel_StateMachine19.setter
    def metamodel_StateMachine19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_StateMachine__metamodel_StateMachine19", None)
        self.__metamodel_StateMachine19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Value20"):
                    opp_val = getattr(item, "metamodel_Value20", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Value20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Value20"):
                    opp_val = getattr(item, "metamodel_Value20", None)
                    
                    setattr(item, "metamodel_Value20", self)
                    

    @property
    def metamodel_StateMachine17(self):
        return self.__metamodel_StateMachine17

    @metamodel_StateMachine17.setter
    def metamodel_StateMachine17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_StateMachine__metamodel_StateMachine17", None)
        self.__metamodel_StateMachine17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_State"):
                    opp_val = getattr(item, "metamodel_State", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_State"):
                    opp_val = getattr(item, "metamodel_State", None)
                    
                    setattr(item, "metamodel_State", self)
                    

    @property
    def metamodel_StateMachine(self):
        return self.__metamodel_StateMachine

    @metamodel_StateMachine.setter
    def metamodel_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_StateMachine__metamodel_StateMachine", None)
        self.__metamodel_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Behaviour15"):
                opp_val = getattr(old_value, "metamodel_Behaviour15", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Behaviour15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Behaviour15"):
                opp_val = getattr(value, "metamodel_Behaviour15", None)
                setattr(value, "metamodel_Behaviour15", self)

class Type:

    pass
class metamodel_FloatVal(Type):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class metamodel_IntVal(Type):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class metamodel_BoolVal(Type):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class metamodel_Type(ABC):

    pass
class metamodel_Value:

    def __init__(self, name: str, metamodel_Value: "metamodel_Sensor" = None, metamodel_Value13: "metamodel_Type" = None, metamodel_Value20: "metamodel_StateMachine" = None, metamodel_Value38: "metamodel_UnaryOperator" = None):
        self.name = name
        self.metamodel_Value = metamodel_Value
        self.metamodel_Value13 = metamodel_Value13
        self.metamodel_Value20 = metamodel_Value20
        self.metamodel_Value38 = metamodel_Value38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Value20(self):
        return self.__metamodel_Value20

    @metamodel_Value20.setter
    def metamodel_Value20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Value__metamodel_Value20", None)
        self.__metamodel_Value20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_StateMachine19"):
                opp_val = getattr(old_value, "metamodel_StateMachine19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_StateMachine19"):
                opp_val = getattr(value, "metamodel_StateMachine19", None)
                if opp_val is None:
                    setattr(value, "metamodel_StateMachine19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodel_Value13(self):
        return self.__metamodel_Value13

    @metamodel_Value13.setter
    def metamodel_Value13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Value__metamodel_Value13", None)
        self.__metamodel_Value13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Type"):
                opp_val = getattr(old_value, "metamodel_Type", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Type"):
                opp_val = getattr(value, "metamodel_Type", None)
                setattr(value, "metamodel_Type", self)

    @property
    def metamodel_Value(self):
        return self.__metamodel_Value

    @metamodel_Value.setter
    def metamodel_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Value__metamodel_Value", None)
        self.__metamodel_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Sensor11"):
                opp_val = getattr(old_value, "metamodel_Sensor11", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Sensor11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Sensor11"):
                opp_val = getattr(value, "metamodel_Sensor11", None)
                setattr(value, "metamodel_Sensor11", self)

    @property
    def metamodel_Value38(self):
        return self.__metamodel_Value38

    @metamodel_Value38.setter
    def metamodel_Value38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Value__metamodel_Value38", None)
        self.__metamodel_Value38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_UnaryOperator"):
                opp_val = getattr(old_value, "metamodel_UnaryOperator", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_UnaryOperator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_UnaryOperator"):
                opp_val = getattr(value, "metamodel_UnaryOperator", None)
                setattr(value, "metamodel_UnaryOperator", self)

class Sensor:

    pass
class metamodel_LightSensor(Sensor):

    pass
class metamodel_DistanceSensor(Sensor):

    pass
class ActionWheel:

    pass
class metamodel_Backward(ActionWheel):

    pass
class metamodel_Forward(ActionWheel):

    pass
class metamodel_TurnRight(ActionWheel):

    pass
class metamodel_Stopping(ActionWheel):

    pass
class metamodel_TurnLeft(ActionWheel):

    pass
class Action:

    pass
class metamodel_ActionWheel(Action):

    def __init__(self, speed: int, metamodel_ActionWheel: "metamodel_Group" = None):
        self.speed = speed
        self.metamodel_ActionWheel = metamodel_ActionWheel
        
    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def metamodel_ActionWheel(self):
        return self.__metamodel_ActionWheel

    @metamodel_ActionWheel.setter
    def metamodel_ActionWheel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_ActionWheel__metamodel_ActionWheel", None)
        self.__metamodel_ActionWheel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Group9"):
                opp_val = getattr(old_value, "metamodel_Group9", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Group9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Group9"):
                opp_val = getattr(value, "metamodel_Group9", None)
                setattr(value, "metamodel_Group9", self)

class Actuator:

    pass
class metamodel_Group(Actuator):

    pass
class metamodel_DifferentialWheel(Actuator):

    def __init__(self, isLeft: bool, speed: int, metamodel_DifferentialWheel: "metamodel_Group" = None):
        self.isLeft = isLeft
        self.speed = speed
        self.metamodel_DifferentialWheel = metamodel_DifferentialWheel
        
    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def isLeft(self) -> bool:
        return self.__isLeft

    @isLeft.setter
    def isLeft(self, isLeft: bool):
        self.__isLeft = isLeft

    @property
    def metamodel_DifferentialWheel(self):
        return self.__metamodel_DifferentialWheel

    @metamodel_DifferentialWheel.setter
    def metamodel_DifferentialWheel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_DifferentialWheel__metamodel_DifferentialWheel", None)
        self.__metamodel_DifferentialWheel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Group"):
                opp_val = getattr(old_value, "metamodel_Group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Group"):
                opp_val = getattr(value, "metamodel_Group", None)
                if opp_val is None:
                    setattr(value, "metamodel_Group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Action(ABC):

    pass
class metamodel_Actuator(ABC):

    def __init__(self, name: str, metamodel_Actuator: "metamodel_Robot" = None):
        self.name = name
        self.metamodel_Actuator = metamodel_Actuator
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Actuator(self):
        return self.__metamodel_Actuator

    @metamodel_Actuator.setter
    def metamodel_Actuator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Actuator__metamodel_Actuator", None)
        self.__metamodel_Actuator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Robot4"):
                opp_val = getattr(old_value, "metamodel_Robot4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Robot4"):
                opp_val = getattr(value, "metamodel_Robot4", None)
                if opp_val is None:
                    setattr(value, "metamodel_Robot4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Sensor(ABC):

    def __init__(self, name: str, sensorName: str, metamodel_Sensor: "metamodel_Robot" = None, metamodel_Sensor11: "metamodel_Value" = None):
        self.name = name
        self.sensorName = sensorName
        self.metamodel_Sensor = metamodel_Sensor
        self.metamodel_Sensor11 = metamodel_Sensor11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sensorName(self) -> str:
        return self.__sensorName

    @sensorName.setter
    def sensorName(self, sensorName: str):
        self.__sensorName = sensorName

    @property
    def metamodel_Sensor11(self):
        return self.__metamodel_Sensor11

    @metamodel_Sensor11.setter
    def metamodel_Sensor11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Sensor__metamodel_Sensor11", None)
        self.__metamodel_Sensor11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Value"):
                opp_val = getattr(old_value, "metamodel_Value", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Value"):
                opp_val = getattr(value, "metamodel_Value", None)
                setattr(value, "metamodel_Value", self)

    @property
    def metamodel_Sensor(self):
        return self.__metamodel_Sensor

    @metamodel_Sensor.setter
    def metamodel_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Sensor__metamodel_Sensor", None)
        self.__metamodel_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Robot2"):
                opp_val = getattr(old_value, "metamodel_Robot2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Robot2"):
                opp_val = getattr(value, "metamodel_Robot2", None)
                if opp_val is None:
                    setattr(value, "metamodel_Robot2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Behaviour:

    def __init__(self, name: str, priority: int, metamodel_Behaviour: "metamodel_Robot" = None, metamodel_Behaviour15: "metamodel_StateMachine" = None):
        self.name = name
        self.priority = priority
        self.metamodel_Behaviour = metamodel_Behaviour
        self.metamodel_Behaviour15 = metamodel_Behaviour15
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Behaviour15(self):
        return self.__metamodel_Behaviour15

    @metamodel_Behaviour15.setter
    def metamodel_Behaviour15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Behaviour__metamodel_Behaviour15", None)
        self.__metamodel_Behaviour15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_StateMachine"):
                opp_val = getattr(old_value, "metamodel_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "metamodel_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_StateMachine"):
                opp_val = getattr(value, "metamodel_StateMachine", None)
                setattr(value, "metamodel_StateMachine", self)

    @property
    def metamodel_Behaviour(self):
        return self.__metamodel_Behaviour

    @metamodel_Behaviour.setter
    def metamodel_Behaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Behaviour__metamodel_Behaviour", None)
        self.__metamodel_Behaviour = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodel_Robot"):
                opp_val = getattr(old_value, "metamodel_Robot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodel_Robot"):
                opp_val = getattr(value, "metamodel_Robot", None)
                if opp_val is None:
                    setattr(value, "metamodel_Robot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodel_Robot:

    def __init__(self, name: str, metamodel_Robot: set["metamodel_Behaviour"] = None, metamodel_Robot2: set["metamodel_Sensor"] = None, metamodel_Robot4: set["metamodel_Actuator"] = None, metamodel_Robot6: set["metamodel_Action"] = None):
        self.name = name
        self.metamodel_Robot = metamodel_Robot if metamodel_Robot is not None else set()
        self.metamodel_Robot2 = metamodel_Robot2 if metamodel_Robot2 is not None else set()
        self.metamodel_Robot4 = metamodel_Robot4 if metamodel_Robot4 is not None else set()
        self.metamodel_Robot6 = metamodel_Robot6 if metamodel_Robot6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodel_Robot2(self):
        return self.__metamodel_Robot2

    @metamodel_Robot2.setter
    def metamodel_Robot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Robot__metamodel_Robot2", None)
        self.__metamodel_Robot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Sensor"):
                    opp_val = getattr(item, "metamodel_Sensor", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Sensor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Sensor"):
                    opp_val = getattr(item, "metamodel_Sensor", None)
                    
                    setattr(item, "metamodel_Sensor", self)
                    

    @property
    def metamodel_Robot(self):
        return self.__metamodel_Robot

    @metamodel_Robot.setter
    def metamodel_Robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Robot__metamodel_Robot", None)
        self.__metamodel_Robot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Behaviour"):
                    opp_val = getattr(item, "metamodel_Behaviour", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Behaviour", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Behaviour"):
                    opp_val = getattr(item, "metamodel_Behaviour", None)
                    
                    setattr(item, "metamodel_Behaviour", self)
                    

    @property
    def metamodel_Robot4(self):
        return self.__metamodel_Robot4

    @metamodel_Robot4.setter
    def metamodel_Robot4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Robot__metamodel_Robot4", None)
        self.__metamodel_Robot4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Actuator"):
                    opp_val = getattr(item, "metamodel_Actuator", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Actuator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Actuator"):
                    opp_val = getattr(item, "metamodel_Actuator", None)
                    
                    setattr(item, "metamodel_Actuator", self)
                    

    @property
    def metamodel_Robot6(self):
        return self.__metamodel_Robot6

    @metamodel_Robot6.setter
    def metamodel_Robot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodel_Robot__metamodel_Robot6", None)
        self.__metamodel_Robot6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodel_Action"):
                    opp_val = getattr(item, "metamodel_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodel_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodel_Action"):
                    opp_val = getattr(item, "metamodel_Action", None)
                    
                    setattr(item, "metamodel_Action", self)
                    
