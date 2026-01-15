from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Comparator(Enum):
    GT = "GT"
    GE = "GE"
    LT = "LT"
    LE = "LE"


############################################
# Definition of Classes
############################################

class majordomo_PreparedValue:

    def __init__(self, name: str, PreparedValue: "majordomo_Program" = None, constants: "majordomo_Program" = None, majordomo_PreparedValue: "majordomo_ValueExpression" = None, majordomo_PreparedValue54: "majordomo_ValueReference" = None):
        self.name = name
        self.PreparedValue = PreparedValue
        self.constants = constants
        self.majordomo_PreparedValue = majordomo_PreparedValue
        self.majordomo_PreparedValue54 = majordomo_PreparedValue54
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def majordomo_PreparedValue54(self):
        return self.__majordomo_PreparedValue54

    @majordomo_PreparedValue54.setter
    def majordomo_PreparedValue54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedValue__majordomo_PreparedValue54", None)
        self.__majordomo_PreparedValue54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_ValueReference"):
                opp_val = getattr(old_value, "majordomo_ValueReference", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_ValueReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_ValueReference"):
                opp_val = getattr(value, "majordomo_ValueReference", None)
                setattr(value, "majordomo_ValueReference", self)

    @property
    def majordomo_PreparedValue(self):
        return self.__majordomo_PreparedValue

    @majordomo_PreparedValue.setter
    def majordomo_PreparedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedValue__majordomo_PreparedValue", None)
        self.__majordomo_PreparedValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_ValueExpression52"):
                opp_val = getattr(old_value, "majordomo_ValueExpression52", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_ValueExpression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_ValueExpression52"):
                opp_val = getattr(value, "majordomo_ValueExpression52", None)
                setattr(value, "majordomo_ValueExpression52", self)

    @property
    def PreparedValue(self):
        return self.__PreparedValue

    @PreparedValue.setter
    def PreparedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedValue__PreparedValue", None)
        self.__PreparedValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctx31"):
                opp_val = getattr(old_value, "ctx31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctx31"):
                opp_val = getattr(value, "ctx31", None)
                if opp_val is None:
                    setattr(value, "ctx31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def constants(self):
        return self.__constants

    @constants.setter
    def constants(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedValue__constants", None)
        self.__constants = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program50"):
                opp_val = getattr(old_value, "Program50", None)
                if opp_val == self:
                    setattr(old_value, "Program50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program50"):
                opp_val = getattr(value, "Program50", None)
                setattr(value, "Program50", self)

class majordomo_PreparedStatement:

    def __init__(self, name: str, PreparedStatement: "majordomo_Program" = None, preparedStatements: "majordomo_Program" = None, majordomo_PreparedStatement41: "majordomo_Statement" = None, majordomo_PreparedStatement: "majordomo_StatementReference" = None):
        self.name = name
        self.PreparedStatement = PreparedStatement
        self.preparedStatements = preparedStatements
        self.majordomo_PreparedStatement41 = majordomo_PreparedStatement41
        self.majordomo_PreparedStatement = majordomo_PreparedStatement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PreparedStatement(self):
        return self.__PreparedStatement

    @PreparedStatement.setter
    def PreparedStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedStatement__PreparedStatement", None)
        self.__PreparedStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctx33"):
                opp_val = getattr(old_value, "ctx33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctx33"):
                opp_val = getattr(value, "ctx33", None)
                if opp_val is None:
                    setattr(value, "ctx33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def majordomo_PreparedStatement41(self):
        return self.__majordomo_PreparedStatement41

    @majordomo_PreparedStatement41.setter
    def majordomo_PreparedStatement41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedStatement__majordomo_PreparedStatement41", None)
        self.__majordomo_PreparedStatement41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_Statement42"):
                opp_val = getattr(old_value, "majordomo_Statement42", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_Statement42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_Statement42"):
                opp_val = getattr(value, "majordomo_Statement42", None)
                setattr(value, "majordomo_Statement42", self)

    @property
    def majordomo_PreparedStatement(self):
        return self.__majordomo_PreparedStatement

    @majordomo_PreparedStatement.setter
    def majordomo_PreparedStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedStatement__majordomo_PreparedStatement", None)
        self.__majordomo_PreparedStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_StatementReference"):
                opp_val = getattr(old_value, "majordomo_StatementReference", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_StatementReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_StatementReference"):
                opp_val = getattr(value, "majordomo_StatementReference", None)
                setattr(value, "majordomo_StatementReference", self)

    @property
    def preparedStatements(self):
        return self.__preparedStatements

    @preparedStatements.setter
    def preparedStatements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedStatement__preparedStatements", None)
        self.__preparedStatements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program"):
                opp_val = getattr(old_value, "Program", None)
                if opp_val == self:
                    setattr(old_value, "Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program"):
                opp_val = getattr(value, "Program", None)
                setattr(value, "Program", self)

class ValueExpression:

    pass
class majordomo_ValueReference(ValueExpression):

    pass
class majordomo_SensorValue(ValueExpression):

    pass
class majordomo_ConstantValue(ValueExpression):

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class BinaryOperation:

    pass
class majordomo_BinaryOrOperation(BinaryOperation):

    pass
class majordomo_BinaryAndOperation(BinaryOperation):

    pass
class majordomo_PreparedActionSet:

    def __init__(self, name: str, PreparedActionSet: "majordomo_Program" = None, preparedActionSets: "majordomo_Program" = None, majordomo_PreparedActionSet: set["majordomo_Action"] = None, majordomo_PreparedActionSet48: "majordomo_ActionSetReference" = None):
        self.name = name
        self.PreparedActionSet = PreparedActionSet
        self.preparedActionSets = preparedActionSets
        self.majordomo_PreparedActionSet = majordomo_PreparedActionSet if majordomo_PreparedActionSet is not None else set()
        self.majordomo_PreparedActionSet48 = majordomo_PreparedActionSet48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def majordomo_PreparedActionSet(self):
        return self.__majordomo_PreparedActionSet

    @majordomo_PreparedActionSet.setter
    def majordomo_PreparedActionSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedActionSet__majordomo_PreparedActionSet", None)
        self.__majordomo_PreparedActionSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "majordomo_Action46"):
                    opp_val = getattr(item, "majordomo_Action46", None)
                    
                    if opp_val == self:
                        setattr(item, "majordomo_Action46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "majordomo_Action46"):
                    opp_val = getattr(item, "majordomo_Action46", None)
                    
                    setattr(item, "majordomo_Action46", self)
                    

    @property
    def majordomo_PreparedActionSet48(self):
        return self.__majordomo_PreparedActionSet48

    @majordomo_PreparedActionSet48.setter
    def majordomo_PreparedActionSet48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedActionSet__majordomo_PreparedActionSet48", None)
        self.__majordomo_PreparedActionSet48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_ActionSetReference"):
                opp_val = getattr(old_value, "majordomo_ActionSetReference", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_ActionSetReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_ActionSetReference"):
                opp_val = getattr(value, "majordomo_ActionSetReference", None)
                setattr(value, "majordomo_ActionSetReference", self)

    @property
    def preparedActionSets(self):
        return self.__preparedActionSets

    @preparedActionSets.setter
    def preparedActionSets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedActionSet__preparedActionSets", None)
        self.__preparedActionSets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program44"):
                opp_val = getattr(old_value, "Program44", None)
                if opp_val == self:
                    setattr(old_value, "Program44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program44"):
                opp_val = getattr(value, "Program44", None)
                setattr(value, "Program44", self)

    @property
    def PreparedActionSet(self):
        return self.__PreparedActionSet

    @PreparedActionSet.setter
    def PreparedActionSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_PreparedActionSet__PreparedActionSet", None)
        self.__PreparedActionSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ctx35"):
                opp_val = getattr(old_value, "ctx35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ctx35"):
                opp_val = getattr(value, "ctx35", None)
                if opp_val is None:
                    setattr(value, "ctx35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Action:

    pass
class majordomo_ActionSetReference(Action):

    pass
class majordomo_FloatAction(Action):

    def __init__(self, value: float, majordomo_FloatAction: "majordomo_FloatActor" = None):
        self.value = value
        self.majordomo_FloatAction = majordomo_FloatAction
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def majordomo_FloatAction(self):
        return self.__majordomo_FloatAction

    @majordomo_FloatAction.setter
    def majordomo_FloatAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_FloatAction__majordomo_FloatAction", None)
        self.__majordomo_FloatAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_FloatActor"):
                opp_val = getattr(old_value, "majordomo_FloatActor", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_FloatActor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_FloatActor"):
                opp_val = getattr(value, "majordomo_FloatActor", None)
                setattr(value, "majordomo_FloatActor", self)

class Actor:

    pass
class majordomo_FloatActor(Actor):

    def __init__(self, majordomo_FloatActor: "majordomo_FloatAction" = None):
        self.majordomo_FloatActor = majordomo_FloatActor
        
    @property
    def majordomo_FloatActor(self):
        return self.__majordomo_FloatActor

    @majordomo_FloatActor.setter
    def majordomo_FloatActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_FloatActor__majordomo_FloatActor", None)
        self.__majordomo_FloatActor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_FloatAction"):
                opp_val = getattr(old_value, "majordomo_FloatAction", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_FloatAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_FloatAction"):
                opp_val = getattr(value, "majordomo_FloatAction", None)
                setattr(value, "majordomo_FloatAction", self)

    def setValue(self, value: float):
        # TODO: Implement setValue method
        pass

class majordomo_BooleanActor(Actor):

    def __init__(self, majordomo_BooleanActor: "majordomo_BooleanAction" = None):
        self.majordomo_BooleanActor = majordomo_BooleanActor
        
    @property
    def majordomo_BooleanActor(self):
        return self.__majordomo_BooleanActor

    @majordomo_BooleanActor.setter
    def majordomo_BooleanActor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_BooleanActor__majordomo_BooleanActor", None)
        self.__majordomo_BooleanActor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_BooleanAction"):
                opp_val = getattr(old_value, "majordomo_BooleanAction", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_BooleanAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_BooleanAction"):
                opp_val = getattr(value, "majordomo_BooleanAction", None)
                setattr(value, "majordomo_BooleanAction", self)

    def setValue(self, value: bool):
        # TODO: Implement setValue method
        pass

class majordomo_ValueExpression(ABC):

    pass
class Statement:

    pass
class majordomo_NotOperation(Statement):

    pass
class majordomo_CompareOperation(Statement):

    def __init__(self, comparator: str, majordomo_CompareOperation: "majordomo_ValueExpression" = None, majordomo_CompareOperation25: "majordomo_ValueExpression" = None):
        self.comparator = comparator
        self.majordomo_CompareOperation = majordomo_CompareOperation
        self.majordomo_CompareOperation25 = majordomo_CompareOperation25
        
    @property
    def comparator(self) -> str:
        return self.__comparator

    @comparator.setter
    def comparator(self, comparator: str):
        self.__comparator = comparator

    @property
    def majordomo_CompareOperation25(self):
        return self.__majordomo_CompareOperation25

    @majordomo_CompareOperation25.setter
    def majordomo_CompareOperation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_CompareOperation__majordomo_CompareOperation25", None)
        self.__majordomo_CompareOperation25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_ValueExpression26"):
                opp_val = getattr(old_value, "majordomo_ValueExpression26", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_ValueExpression26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_ValueExpression26"):
                opp_val = getattr(value, "majordomo_ValueExpression26", None)
                setattr(value, "majordomo_ValueExpression26", self)

    @property
    def majordomo_CompareOperation(self):
        return self.__majordomo_CompareOperation

    @majordomo_CompareOperation.setter
    def majordomo_CompareOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_CompareOperation__majordomo_CompareOperation", None)
        self.__majordomo_CompareOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_ValueExpression"):
                opp_val = getattr(old_value, "majordomo_ValueExpression", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_ValueExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_ValueExpression"):
                opp_val = getattr(value, "majordomo_ValueExpression", None)
                setattr(value, "majordomo_ValueExpression", self)

class majordomo_BooleanSensorStatement(Statement):

    pass
class majordomo_StatementReference(Statement):

    pass
class majordomo_BinaryOperation(Statement):

    pass
class majordomo_BooleanAction(Action):

    def __init__(self, value: bool, majordomo_BooleanAction: "majordomo_BooleanActor" = None):
        self.value = value
        self.majordomo_BooleanAction = majordomo_BooleanAction
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

    @property
    def majordomo_BooleanAction(self):
        return self.__majordomo_BooleanAction

    @majordomo_BooleanAction.setter
    def majordomo_BooleanAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_BooleanAction__majordomo_BooleanAction", None)
        self.__majordomo_BooleanAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_BooleanActor"):
                opp_val = getattr(old_value, "majordomo_BooleanActor", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_BooleanActor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_BooleanActor"):
                opp_val = getattr(value, "majordomo_BooleanActor", None)
                setattr(value, "majordomo_BooleanActor", self)

class majordomo_Extension(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class majordomo_Action(ABC):

    pass
class majordomo_Statement(ABC):

    pass
class majordomo_Rule:

    pass
class Extension:

    pass
class Sensor:

    pass
class majordomo_FloatSensor(Sensor):

    def __init__(self, majordomo_FloatSensor: "majordomo_SensorValue" = None):
        self.majordomo_FloatSensor = majordomo_FloatSensor
        
    @property
    def majordomo_FloatSensor(self):
        return self.__majordomo_FloatSensor

    @majordomo_FloatSensor.setter
    def majordomo_FloatSensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_FloatSensor__majordomo_FloatSensor", None)
        self.__majordomo_FloatSensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_SensorValue"):
                opp_val = getattr(old_value, "majordomo_SensorValue", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_SensorValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_SensorValue"):
                opp_val = getattr(value, "majordomo_SensorValue", None)
                setattr(value, "majordomo_SensorValue", self)

    def getValue(self) -> float:
        # TODO: Implement getValue method
        pass

class majordomo_BooleanSensor(Sensor):

    def __init__(self, majordomo_BooleanSensor: "majordomo_BooleanSensorStatement" = None):
        self.majordomo_BooleanSensor = majordomo_BooleanSensor
        
    @property
    def majordomo_BooleanSensor(self):
        return self.__majordomo_BooleanSensor

    @majordomo_BooleanSensor.setter
    def majordomo_BooleanSensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_BooleanSensor__majordomo_BooleanSensor", None)
        self.__majordomo_BooleanSensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_BooleanSensorStatement"):
                opp_val = getattr(old_value, "majordomo_BooleanSensorStatement", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_BooleanSensorStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_BooleanSensorStatement"):
                opp_val = getattr(value, "majordomo_BooleanSensorStatement", None)
                setattr(value, "majordomo_BooleanSensorStatement", self)

    def getValue(self) -> bool:
        # TODO: Implement getValue method
        pass

class majordomo_HouseMountable(ABC):

    pass
class majordomo_RoomMountable(ABC):

    pass
class BooleanActor:

    pass
class FloatActor:

    pass
class BooleanSensor:

    pass
class FloatSensor:

    pass
class RoomMountable:

    pass
class majordomo_NumberSensor(RoomMountable, FloatSensor):

    pass
class majordomo_SwitchSensor(RoomMountable, BooleanSensor):

    pass
class majordomo_RollerActor(RoomMountable, BooleanActor):

    pass
class majordomo_CoffeeActor(RoomMountable, BooleanActor):

    pass
class majordomo_RoofWindowActor(RoomMountable, BooleanActor):

    pass
class majordomo_RadiatorActor(RoomMountable, BooleanActor):

    pass
class HouseMountable:

    pass
class majordomo_ClockSensor(FloatSensor, HouseMountable):

    pass
class majordomo_LampActor(RoomMountable, FloatActor, HouseMountable):

    pass
class majordomo_TemperatureSensor(RoomMountable, FloatSensor, HouseMountable):

    pass
class majordomo_BoilerActor(HouseMountable, BooleanActor):

    pass
class majordomo_RainSensor(BooleanSensor, HouseMountable):

    pass
class majordomo_LightSensor(RoomMountable, FloatSensor, HouseMountable):

    pass
class majordomo_Actor(Extension):

    pass
class majordomo_Sensor(Extension):

    pass
class majordomo_Extendable(ABC):

    pass
class Extendable:

    pass
class majordomo_Program:

    pass
class majordomo_Room(Extendable):

    def __init__(self, name: str, majordomo_Room: "majordomo_Majordomo" = None):
        self.name = name
        self.majordomo_Room = majordomo_Room
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def majordomo_Room(self):
        return self.__majordomo_Room

    @majordomo_Room.setter
    def majordomo_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_Room__majordomo_Room", None)
        self.__majordomo_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_Majordomo2"):
                opp_val = getattr(old_value, "majordomo_Majordomo2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_Majordomo2"):
                opp_val = getattr(value, "majordomo_Majordomo2", None)
                if opp_val is None:
                    setattr(value, "majordomo_Majordomo2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class majordomo_House(Extendable):

    pass
class majordomo_Majordomo:

    def __init__(self, name: str, majordomo_Majordomo: "majordomo_House" = None, majordomo_Majordomo2: set["majordomo_Room"] = None, majordomo_Majordomo4: "majordomo_Program" = None):
        self.name = name
        self.majordomo_Majordomo = majordomo_Majordomo
        self.majordomo_Majordomo2 = majordomo_Majordomo2 if majordomo_Majordomo2 is not None else set()
        self.majordomo_Majordomo4 = majordomo_Majordomo4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def majordomo_Majordomo(self):
        return self.__majordomo_Majordomo

    @majordomo_Majordomo.setter
    def majordomo_Majordomo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_Majordomo__majordomo_Majordomo", None)
        self.__majordomo_Majordomo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_House"):
                opp_val = getattr(old_value, "majordomo_House", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_House", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_House"):
                opp_val = getattr(value, "majordomo_House", None)
                setattr(value, "majordomo_House", self)

    @property
    def majordomo_Majordomo2(self):
        return self.__majordomo_Majordomo2

    @majordomo_Majordomo2.setter
    def majordomo_Majordomo2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_Majordomo__majordomo_Majordomo2", None)
        self.__majordomo_Majordomo2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "majordomo_Room"):
                    opp_val = getattr(item, "majordomo_Room", None)
                    
                    if opp_val == self:
                        setattr(item, "majordomo_Room", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "majordomo_Room"):
                    opp_val = getattr(item, "majordomo_Room", None)
                    
                    setattr(item, "majordomo_Room", self)
                    

    @property
    def majordomo_Majordomo4(self):
        return self.__majordomo_Majordomo4

    @majordomo_Majordomo4.setter
    def majordomo_Majordomo4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_majordomo_Majordomo__majordomo_Majordomo4", None)
        self.__majordomo_Majordomo4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "majordomo_Program"):
                opp_val = getattr(old_value, "majordomo_Program", None)
                if opp_val == self:
                    setattr(old_value, "majordomo_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "majordomo_Program"):
                opp_val = getattr(value, "majordomo_Program", None)
                setattr(value, "majordomo_Program", self)
