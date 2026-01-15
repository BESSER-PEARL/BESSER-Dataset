####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
Weekdays: Enumeration = Enumeration(
    name="Weekdays",
    literals={
            EnumerationLiteral(name="MONDAY"),
			EnumerationLiteral(name="TUESDAY"),
			EnumerationLiteral(name="WEDNESDAY"),
			EnumerationLiteral(name="THURSDAY"),
			EnumerationLiteral(name="FRIDAY"),
			EnumerationLiteral(name="SATURDAY"),
			EnumerationLiteral(name="SUNDAY")
    }
)

CompOps: Enumeration = Enumeration(
    name="CompOps",
    literals={
            EnumerationLiteral(name="GREATER"),
			EnumerationLiteral(name="GREATEROREQUAL"),
			EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="LESSOREQUAL"),
			EnumerationLiteral(name="LESS"),
			EnumerationLiteral(name="NOTEQUAL")
    }
)

# Classes
PolicyEngine_Building = Class(name="PolicyEngine::Building")
NamedElement = Class(name="NamedElement")
PolicyEngine_CTS = Class(name="PolicyEngine::CTS")
PolicyEngine_AccessControl = Class(name="PolicyEngine::AccessControl")
PolicyEngine_CalendarSystem = Class(name="PolicyEngine::CalendarSystem")
PolicyEngine_MeetingScheduleSystem = Class(name="PolicyEngine::MeetingScheduleSystem")
PolicyEngine_Schedule = Class(name="PolicyEngine::Schedule")
PolicyEngine_LightSwitchActuator = Class(name="PolicyEngine::LightSwitchActuator")
Actuator = Class(name="Actuator")
PolicyEngine_Sensor = Class(name="PolicyEngine::Sensor", is_abstract=True)
HasIntegerValue = Class(name="HasIntegerValue")
PolicyEngine_Actuator = Class(name="PolicyEngine::Actuator", is_abstract=True)
PolicyEngine_SensorComponent = Class(name="PolicyEngine::SensorComponent")
HasSensors = Class(name="HasSensors")
PolicyEngine_MotionSensor = Class(name="PolicyEngine::MotionSensor")
Sensor = Class(name="Sensor")
PolicyEngine_TemperatureSensor = Class(name="PolicyEngine::TemperatureSensor")
PolicyEngine_PressureSensor = Class(name="PolicyEngine::PressureSensor")
PolicyEngine_TouchSensor = Class(name="PolicyEngine::TouchSensor")
PolicyEngine_WindowActuator = Class(name="PolicyEngine::WindowActuator")
PolicyEngine_HumidifierActuator = Class(name="PolicyEngine::HumidifierActuator")
PolicyEngine_LightSensor = Class(name="PolicyEngine::LightSensor")
PolicyEngine_Floor = Class(name="PolicyEngine::Floor")
PolicyEngine_Timer = Class(name="PolicyEngine::Timer")
PolicyEngine_Model = Class(name="PolicyEngine::Model")
PolicyEngine_Room = Class(name="PolicyEngine::Room")
PolicyEngine_Policy = Class(name="PolicyEngine::Policy")
PolicyEngine_State = Class(name="PolicyEngine::State")
PolicyEngine_HasIntegerValue = Class(name="PolicyEngine::HasIntegerValue")
PolicyEngine_ActuatorComponent = Class(name="PolicyEngine::ActuatorComponent")
HasActuators = Class(name="HasActuators")
PolicyEngine_DoorActuator = Class(name="PolicyEngine::DoorActuator")
PolicyEngine_NamedElement = Class(name="PolicyEngine::NamedElement", is_abstract=True)
PolicyEngine_RadiatorActuator = Class(name="PolicyEngine::RadiatorActuator")
PolicyEngine_SmokeSensor = Class(name="PolicyEngine::SmokeSensor")
PolicyEngine_HasSensors = Class(name="PolicyEngine::HasSensors")
PolicyEngine_HasActuators = Class(name="PolicyEngine::HasActuators")
PolicyEngine_CO2Sensor = Class(name="PolicyEngine::CO2Sensor")
PolicyEngine_InfraredLightSensor = Class(name="PolicyEngine::InfraredLightSensor")
PolicyEngine_HumiditySensor = Class(name="PolicyEngine::HumiditySensor")
PolicyEngine_AudioAlarmActuator = Class(name="PolicyEngine::AudioAlarmActuator")
PolicyEngine_Expression = Class(name="PolicyEngine::Expression", is_abstract=True)
PolicyEngine_Time = Class(name="PolicyEngine::Time")
PolicyEngine_If = Class(name="PolicyEngine::If")
PolicyEngine_BinaryOps = Class(name="PolicyEngine::BinaryOps")
PolicyEngine_UnaryOp = Class(name="PolicyEngine::UnaryOp")
PolicyEngine_Id = Class(name="PolicyEngine::Id")
PolicyEngine_RoomActuators = Class(name="PolicyEngine::RoomActuators")
PolicyEngine_TimeExpression = Class(name="PolicyEngine::TimeExpression")
Expression = Class(name="Expression")
PolicyEngine_ResetExpression = Class(name="PolicyEngine::ResetExpression")
PolicyEngine_RoomUsage = Class(name="PolicyEngine::RoomUsage")
PolicyEngine_Constant = Class(name="PolicyEngine::Constant")

# PolicyEngine_Building class attributes and methods

# NamedElement class attributes and methods

# PolicyEngine_CTS class attributes and methods

# PolicyEngine_AccessControl class attributes and methods

# PolicyEngine_CalendarSystem class attributes and methods

# PolicyEngine_MeetingScheduleSystem class attributes and methods

# PolicyEngine_Schedule class attributes and methods
PolicyEngine_Schedule_weekdays: Property = Property(name="weekdays", type=StringType)
PolicyEngine_Schedule.attributes={PolicyEngine_Schedule_weekdays}

# PolicyEngine_LightSwitchActuator class attributes and methods

# Actuator class attributes and methods

# PolicyEngine_Sensor class attributes and methods

# HasIntegerValue class attributes and methods

# PolicyEngine_Actuator class attributes and methods

# PolicyEngine_SensorComponent class attributes and methods

# HasSensors class attributes and methods

# PolicyEngine_MotionSensor class attributes and methods

# Sensor class attributes and methods

# PolicyEngine_TemperatureSensor class attributes and methods

# PolicyEngine_PressureSensor class attributes and methods

# PolicyEngine_TouchSensor class attributes and methods

# PolicyEngine_WindowActuator class attributes and methods

# PolicyEngine_HumidifierActuator class attributes and methods

# PolicyEngine_LightSensor class attributes and methods

# PolicyEngine_Floor class attributes and methods

# PolicyEngine_Timer class attributes and methods

# PolicyEngine_Model class attributes and methods

# PolicyEngine_Room class attributes and methods

# PolicyEngine_Policy class attributes and methods

# PolicyEngine_State class attributes and methods
PolicyEngine_State_valueState: Property = Property(name="valueState", type=BooleanType)
PolicyEngine_State.attributes={PolicyEngine_State_valueState}

# PolicyEngine_HasIntegerValue class attributes and methods
PolicyEngine_HasIntegerValue_valueState: Property = Property(name="valueState", type=IntegerType)
PolicyEngine_HasIntegerValue.attributes={PolicyEngine_HasIntegerValue_valueState}

# PolicyEngine_ActuatorComponent class attributes and methods

# HasActuators class attributes and methods

# PolicyEngine_DoorActuator class attributes and methods

# PolicyEngine_NamedElement class attributes and methods
PolicyEngine_NamedElement_name: Property = Property(name="name", type=StringType)
PolicyEngine_NamedElement.attributes={PolicyEngine_NamedElement_name}

# PolicyEngine_RadiatorActuator class attributes and methods

# PolicyEngine_SmokeSensor class attributes and methods

# PolicyEngine_HasSensors class attributes and methods

# PolicyEngine_HasActuators class attributes and methods

# PolicyEngine_CO2Sensor class attributes and methods

# PolicyEngine_InfraredLightSensor class attributes and methods

# PolicyEngine_HumiditySensor class attributes and methods

# PolicyEngine_AudioAlarmActuator class attributes and methods

# PolicyEngine_Expression class attributes and methods

# PolicyEngine_Time class attributes and methods
PolicyEngine_Time_hours: Property = Property(name="hours", type=StringType)
PolicyEngine_Time_minutes: Property = Property(name="minutes", type=StringType)
PolicyEngine_Time.attributes={PolicyEngine_Time_minutes, PolicyEngine_Time_hours}

# PolicyEngine_If class attributes and methods

# PolicyEngine_BinaryOps class attributes and methods
PolicyEngine_BinaryOps_operator: Property = Property(name="operator", type=StringType)
PolicyEngine_BinaryOps.attributes={PolicyEngine_BinaryOps_operator}

# PolicyEngine_UnaryOp class attributes and methods
PolicyEngine_UnaryOp_operator: Property = Property(name="operator", type=StringType)
PolicyEngine_UnaryOp.attributes={PolicyEngine_UnaryOp_operator}

# PolicyEngine_Id class attributes and methods

# PolicyEngine_RoomActuators class attributes and methods

# PolicyEngine_TimeExpression class attributes and methods
PolicyEngine_TimeExpression_TimeBound: Property = Property(name="TimeBound", type=IntegerType)
PolicyEngine_TimeExpression.attributes={PolicyEngine_TimeExpression_TimeBound}

# Expression class attributes and methods

# PolicyEngine_ResetExpression class attributes and methods

# PolicyEngine_RoomUsage class attributes and methods

# PolicyEngine_Constant class attributes and methods

# Relationships
ctsSystem0: BinaryAssociation = BinaryAssociation(
    name="ctsSystem0",
    ends={
        Property(name="PolicyEngine_CTS", type=PolicyEngine_Building, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Building", type=PolicyEngine_CTS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessControl1: BinaryAssociation = BinaryAssociation(
    name="accessControl1",
    ends={
        Property(name="PolicyEngine_AccessControl", type=PolicyEngine_Building, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Building2", type=PolicyEngine_AccessControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
calendarSystem3: BinaryAssociation = BinaryAssociation(
    name="calendarSystem3",
    ends={
        Property(name="PolicyEngine_CalendarSystem", type=PolicyEngine_Building, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Building4", type=PolicyEngine_CalendarSystem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
meetingScheduleSystem5: BinaryAssociation = BinaryAssociation(
    name="meetingScheduleSystem5",
    ends={
        Property(name="PolicyEngine_MeetingScheduleSystem", type=PolicyEngine_Building, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Building6", type=PolicyEngine_MeetingScheduleSystem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timers19: BinaryAssociation = BinaryAssociation(
    name="timers19",
    ends={
        Property(name="PolicyEngine_Timer21", type=PolicyEngine_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Model20", type=PolicyEngine_Timer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schedules22: BinaryAssociation = BinaryAssociation(
    name="schedules22",
    ends={
        Property(name="PolicyEngine_Schedule", type=PolicyEngine_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Model23", type=PolicyEngine_Schedule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
temperatureSensors24: BinaryAssociation = BinaryAssociation(
    name="temperatureSensors24",
    ends={
        Property(name="PolicyEngine_Sensor", type=PolicyEngine_CTS, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_CTS25", type=PolicyEngine_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ctsActuators26: BinaryAssociation = BinaryAssociation(
    name="ctsActuators26",
    ends={
        Property(name="PolicyEngine_Actuator", type=PolicyEngine_CTS, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_CTS27", type=PolicyEngine_Actuator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
floors7: BinaryAssociation = BinaryAssociation(
    name="floors7",
    ends={
        Property(name="PolicyEngine_Floor", type=PolicyEngine_Building, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Building8", type=PolicyEngine_Floor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timers9: BinaryAssociation = BinaryAssociation(
    name="timers9",
    ends={
        Property(name="PolicyEngine_Timer", type=PolicyEngine_Building, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Building10", type=PolicyEngine_Timer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
buildings11: BinaryAssociation = BinaryAssociation(
    name="buildings11",
    ends={
        Property(name="PolicyEngine_Building12", type=PolicyEngine_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Model", type=PolicyEngine_Building, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predefinedRooms13: BinaryAssociation = BinaryAssociation(
    name="predefinedRooms13",
    ends={
        Property(name="PolicyEngine_Room", type=PolicyEngine_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Model14", type=PolicyEngine_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
policyDefinition15: BinaryAssociation = BinaryAssociation(
    name="policyDefinition15",
    ends={
        Property(name="PolicyEngine_Policy", type=PolicyEngine_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Model16", type=PolicyEngine_Policy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateDefinition17: BinaryAssociation = BinaryAssociation(
    name="stateDefinition17",
    ends={
        Property(name="PolicyEngine_State", type=PolicyEngine_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Model18", type=PolicyEngine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declareSensor38: BinaryAssociation = BinaryAssociation(
    name="declareSensor38",
    ends={
        Property(name="PolicyEngine_SensorComponent", type=PolicyEngine_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Room39", type=PolicyEngine_SensorComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declareActuator40: BinaryAssociation = BinaryAssociation(
    name="declareActuator40",
    ends={
        Property(name="PolicyEngine_ActuatorComponent", type=PolicyEngine_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Room41", type=PolicyEngine_ActuatorComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends43: BinaryAssociation = BinaryAssociation(
    name="extends43",
    ends={
        Property(name="PolicyEngine_Room44", type=PolicyEngine_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Room42", type=PolicyEngine_Room, multiplicity=Multiplicity(0, 9999))
    }
)
timers45: BinaryAssociation = BinaryAssociation(
    name="timers45",
    ends={
        Property(name="PolicyEngine_Timer47", type=PolicyEngine_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Room46", type=PolicyEngine_Timer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
policies48: BinaryAssociation = BinaryAssociation(
    name="policies48",
    ends={
        Property(name="PolicyEngine_Policy50", type=PolicyEngine_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Room49", type=PolicyEngine_Policy, multiplicity=Multiplicity(0, 9999))
    }
)
during51: BinaryAssociation = BinaryAssociation(
    name="during51",
    ends={
        Property(name="PolicyEngine_Schedule53", type=PolicyEngine_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Room52", type=PolicyEngine_Schedule, multiplicity=Multiplicity(0, 9999))
    }
)
rooms54: BinaryAssociation = BinaryAssociation(
    name="rooms54",
    ends={
        Property(name="PolicyEngine_Room56", type=PolicyEngine_Floor, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Floor55", type=PolicyEngine_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timers57: BinaryAssociation = BinaryAssociation(
    name="timers57",
    ends={
        Property(name="PolicyEngine_Timer59", type=PolicyEngine_Floor, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Floor58", type=PolicyEngine_Timer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessControlSensors28: BinaryAssociation = BinaryAssociation(
    name="accessControlSensors28",
    ends={
        Property(name="PolicyEngine_Sensor30", type=PolicyEngine_AccessControl, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_AccessControl29", type=PolicyEngine_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessControlDoorLockActuator31: BinaryAssociation = BinaryAssociation(
    name="accessControlDoorLockActuator31",
    ends={
        Property(name="PolicyEngine_Actuator33", type=PolicyEngine_AccessControl, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_AccessControl32", type=PolicyEngine_Actuator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensors34: BinaryAssociation = BinaryAssociation(
    name="sensors34",
    ends={
        Property(name="PolicyEngine_Sensor35", type=PolicyEngine_HasSensors, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_HasSensors", type=PolicyEngine_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actuators36: BinaryAssociation = BinaryAssociation(
    name="actuators36",
    ends={
        Property(name="PolicyEngine_Actuator37", type=PolicyEngine_HasActuators, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_HasActuators", type=PolicyEngine_Actuator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprStates83: BinaryAssociation = BinaryAssociation(
    name="exprStates83",
    ends={
        Property(name="PolicyEngine_Expression", type=PolicyEngine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_State84", type=PolicyEngine_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from85: BinaryAssociation = BinaryAssociation(
    name="from85",
    ends={
        Property(name="PolicyEngine_Time", type=PolicyEngine_Schedule, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Schedule86", type=PolicyEngine_Time, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to87: BinaryAssociation = BinaryAssociation(
    name="to87",
    ends={
        Property(name="PolicyEngine_Time89", type=PolicyEngine_Schedule, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Schedule88", type=PolicyEngine_Time, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond90: BinaryAssociation = BinaryAssociation(
    name="cond90",
    ends={
        Property(name="PolicyEngine_Expression92", type=PolicyEngine_If, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_If91", type=PolicyEngine_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then93: BinaryAssociation = BinaryAssociation(
    name="then93",
    ends={
        Property(name="PolicyEngine_Expression95", type=PolicyEngine_If, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_If94", type=PolicyEngine_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usesActuators60: BinaryAssociation = BinaryAssociation(
    name="usesActuators60",
    ends={
        Property(name="PolicyEngine_Actuator62", type=PolicyEngine_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Policy61", type=PolicyEngine_Actuator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usesSensors63: BinaryAssociation = BinaryAssociation(
    name="usesSensors63",
    ends={
        Property(name="PolicyEngine_Sensor65", type=PolicyEngine_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Policy64", type=PolicyEngine_Sensor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specifiedBy66: BinaryAssociation = BinaryAssociation(
    name="specifiedBy66",
    ends={
        Property(name="PolicyEngine_If", type=PolicyEngine_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Policy67", type=PolicyEngine_If, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
controlledBy68: BinaryAssociation = BinaryAssociation(
    name="controlledBy68",
    ends={
        Property(name="PolicyEngine_Timer70", type=PolicyEngine_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Policy69", type=PolicyEngine_Timer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defineState71: BinaryAssociation = BinaryAssociation(
    name="defineState71",
    ends={
        Property(name="PolicyEngine_State73", type=PolicyEngine_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Policy72", type=PolicyEngine_State, multiplicity=Multiplicity(0, 9999))
    }
)
during74: BinaryAssociation = BinaryAssociation(
    name="during74",
    ends={
        Property(name="PolicyEngine_Schedule76", type=PolicyEngine_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Policy75", type=PolicyEngine_Schedule, multiplicity=Multiplicity(0, 9999))
    }
)
usesRooms77: BinaryAssociation = BinaryAssociation(
    name="usesRooms77",
    ends={
        Property(name="PolicyEngine_Room79", type=PolicyEngine_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Policy78", type=PolicyEngine_Room, multiplicity=Multiplicity(0, 9999))
    }
)
defineLocalState80: BinaryAssociation = BinaryAssociation(
    name="defineLocalState80",
    ends={
        Property(name="PolicyEngine_State82", type=PolicyEngine_Policy, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_Policy81", type=PolicyEngine_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
act108: BinaryAssociation = BinaryAssociation(
    name="act108",
    ends={
        Property(name="PolicyEngine_Actuator110", type=PolicyEngine_RoomUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_RoomUsage109", type=PolicyEngine_Actuator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defineState111: BinaryAssociation = BinaryAssociation(
    name="defineState111",
    ends={
        Property(name="PolicyEngine_State113", type=PolicyEngine_RoomUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_RoomUsage112", type=PolicyEngine_State, multiplicity=Multiplicity(0, 1))
    }
)
lexpr114: BinaryAssociation = BinaryAssociation(
    name="lexpr114",
    ends={
        Property(name="PolicyEngine_Expression115", type=PolicyEngine_BinaryOps, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_BinaryOps", type=PolicyEngine_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rexpr116: BinaryAssociation = BinaryAssociation(
    name="rexpr116",
    ends={
        Property(name="PolicyEngine_Expression118", type=PolicyEngine_BinaryOps, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_BinaryOps117", type=PolicyEngine_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr119: BinaryAssociation = BinaryAssociation(
    name="expr119",
    ends={
        Property(name="PolicyEngine_Expression120", type=PolicyEngine_UnaryOp, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_UnaryOp", type=PolicyEngine_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
definedRoomActuator121: BinaryAssociation = BinaryAssociation(
    name="definedRoomActuator121",
    ends={
        Property(name="PolicyEngine_Room122", type=PolicyEngine_RoomActuators, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_RoomActuators", type=PolicyEngine_Room, multiplicity=Multiplicity(0, 1))
    }
)
elseif97: BinaryAssociation = BinaryAssociation(
    name="elseif97",
    ends={
        Property(name="PolicyEngine_If98", type=PolicyEngine_If, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_If96", type=PolicyEngine_If, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else99: BinaryAssociation = BinaryAssociation(
    name="else99",
    ends={
        Property(name="PolicyEngine_Expression101", type=PolicyEngine_If, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_If100", type=PolicyEngine_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
time102: BinaryAssociation = BinaryAssociation(
    name="time102",
    ends={
        Property(name="PolicyEngine_Timer103", type=PolicyEngine_TimeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_TimeExpression", type=PolicyEngine_Timer, multiplicity=Multiplicity(1, 1))
    }
)
reset104: BinaryAssociation = BinaryAssociation(
    name="reset104",
    ends={
        Property(name="PolicyEngine_Timer105", type=PolicyEngine_ResetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_ResetExpression", type=PolicyEngine_Timer, multiplicity=Multiplicity(1, 1))
    }
)
sen106: BinaryAssociation = BinaryAssociation(
    name="sen106",
    ends={
        Property(name="PolicyEngine_Sensor107", type=PolicyEngine_RoomUsage, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_RoomUsage", type=PolicyEngine_Sensor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definedActuator123: BinaryAssociation = BinaryAssociation(
    name="definedActuator123",
    ends={
        Property(name="PolicyEngine_ActuatorComponent125", type=PolicyEngine_RoomActuators, multiplicity=Multiplicity(1, 1)),
        Property(name="PolicyEngine_RoomActuators124", type=PolicyEngine_ActuatorComponent, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_PolicyEngine_Building_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_Building)
gen_PolicyEngine_LightSwitchActuator_Actuator = Generalization(general=Actuator, specific=PolicyEngine_LightSwitchActuator)
gen_PolicyEngine_Sensor_HasIntegerValue = Generalization(general=HasIntegerValue, specific=PolicyEngine_Sensor)
gen_PolicyEngine_Actuator_HasIntegerValue = Generalization(general=HasIntegerValue, specific=PolicyEngine_Actuator)
gen_PolicyEngine_SensorComponent_HasSensors = Generalization(general=HasSensors, specific=PolicyEngine_SensorComponent)
gen_PolicyEngine_SensorComponent_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_SensorComponent)
gen_PolicyEngine_MotionSensor_Sensor = Generalization(general=Sensor, specific=PolicyEngine_MotionSensor)
gen_PolicyEngine_TemperatureSensor_Sensor = Generalization(general=Sensor, specific=PolicyEngine_TemperatureSensor)
gen_PolicyEngine_PressureSensor_Sensor = Generalization(general=Sensor, specific=PolicyEngine_PressureSensor)
gen_PolicyEngine_TouchSensor_Sensor = Generalization(general=Sensor, specific=PolicyEngine_TouchSensor)
gen_PolicyEngine_WindowActuator_Actuator = Generalization(general=Actuator, specific=PolicyEngine_WindowActuator)
gen_PolicyEngine_HumidifierActuator_Actuator = Generalization(general=Actuator, specific=PolicyEngine_HumidifierActuator)
gen_PolicyEngine_LightSensor_Sensor = Generalization(general=Sensor, specific=PolicyEngine_LightSensor)
gen_PolicyEngine_Model_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_Model)
gen_PolicyEngine_AudioAlarmActuator_Actuator = Generalization(general=Actuator, specific=PolicyEngine_AudioAlarmActuator)
gen_PolicyEngine_Room_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_Room)
gen_PolicyEngine_Floor_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_Floor)
gen_PolicyEngine_ActuatorComponent_HasActuators = Generalization(general=HasActuators, specific=PolicyEngine_ActuatorComponent)
gen_PolicyEngine_ActuatorComponent_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_ActuatorComponent)
gen_PolicyEngine_Policy_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_Policy)
gen_PolicyEngine_DoorActuator_Actuator = Generalization(general=Actuator, specific=PolicyEngine_DoorActuator)
gen_PolicyEngine_RadiatorActuator_Actuator = Generalization(general=Actuator, specific=PolicyEngine_RadiatorActuator)
gen_PolicyEngine_SmokeSensor_Sensor = Generalization(general=Sensor, specific=PolicyEngine_SmokeSensor)
gen_PolicyEngine_CO2Sensor_Sensor = Generalization(general=Sensor, specific=PolicyEngine_CO2Sensor)
gen_PolicyEngine_InfraredLightSensor_Sensor = Generalization(general=Sensor, specific=PolicyEngine_InfraredLightSensor)
gen_PolicyEngine_HumiditySensor_Sensor = Generalization(general=Sensor, specific=PolicyEngine_HumiditySensor)
gen_PolicyEngine_Timer_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_Timer)
gen_PolicyEngine_Schedule_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_Schedule)
gen_PolicyEngine_State_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_State)
gen_PolicyEngine_BinaryOps_Expression = Generalization(general=Expression, specific=PolicyEngine_BinaryOps)
gen_PolicyEngine_UnaryOp_Expression = Generalization(general=Expression, specific=PolicyEngine_UnaryOp)
gen_PolicyEngine_Id_Expression = Generalization(general=Expression, specific=PolicyEngine_Id)
gen_PolicyEngine_Id_NamedElement = Generalization(general=NamedElement, specific=PolicyEngine_Id)
gen_PolicyEngine_RoomActuators_Expression = Generalization(general=Expression, specific=PolicyEngine_RoomActuators)
gen_PolicyEngine_TimeExpression_Expression = Generalization(general=Expression, specific=PolicyEngine_TimeExpression)
gen_PolicyEngine_ResetExpression_Expression = Generalization(general=Expression, specific=PolicyEngine_ResetExpression)
gen_PolicyEngine_RoomUsage_Expression = Generalization(general=Expression, specific=PolicyEngine_RoomUsage)
gen_PolicyEngine_Constant_Expression = Generalization(general=Expression, specific=PolicyEngine_Constant)

# Domain Model
domain_model = DomainModel(
    name="PolicyEngine",
    types={PolicyEngine_Building, NamedElement, PolicyEngine_CTS, PolicyEngine_AccessControl, PolicyEngine_CalendarSystem, PolicyEngine_MeetingScheduleSystem, PolicyEngine_Schedule, PolicyEngine_LightSwitchActuator, Actuator, PolicyEngine_Sensor, HasIntegerValue, PolicyEngine_Actuator, PolicyEngine_SensorComponent, HasSensors, PolicyEngine_MotionSensor, Sensor, PolicyEngine_TemperatureSensor, PolicyEngine_PressureSensor, PolicyEngine_TouchSensor, PolicyEngine_WindowActuator, PolicyEngine_HumidifierActuator, PolicyEngine_LightSensor, PolicyEngine_Floor, PolicyEngine_Timer, PolicyEngine_Model, PolicyEngine_Room, PolicyEngine_Policy, PolicyEngine_State, PolicyEngine_HasIntegerValue, PolicyEngine_ActuatorComponent, HasActuators, PolicyEngine_DoorActuator, PolicyEngine_NamedElement, PolicyEngine_RadiatorActuator, PolicyEngine_SmokeSensor, PolicyEngine_HasSensors, PolicyEngine_HasActuators, PolicyEngine_CO2Sensor, PolicyEngine_InfraredLightSensor, PolicyEngine_HumiditySensor, PolicyEngine_AudioAlarmActuator, PolicyEngine_Expression, PolicyEngine_Time, PolicyEngine_If, PolicyEngine_BinaryOps, PolicyEngine_UnaryOp, PolicyEngine_Id, PolicyEngine_RoomActuators, PolicyEngine_TimeExpression, Expression, PolicyEngine_ResetExpression, PolicyEngine_RoomUsage, PolicyEngine_Constant, Weekdays, CompOps},
    associations={ctsSystem0, accessControl1, calendarSystem3, meetingScheduleSystem5, timers19, schedules22, temperatureSensors24, ctsActuators26, floors7, timers9, buildings11, predefinedRooms13, policyDefinition15, stateDefinition17, declareSensor38, declareActuator40, extends43, timers45, policies48, during51, rooms54, timers57, accessControlSensors28, accessControlDoorLockActuator31, sensors34, actuators36, exprStates83, from85, to87, cond90, then93, usesActuators60, usesSensors63, specifiedBy66, controlledBy68, defineState71, during74, usesRooms77, defineLocalState80, act108, defineState111, lexpr114, rexpr116, expr119, definedRoomActuator121, elseif97, else99, time102, reset104, sen106, definedActuator123},
    generalizations={gen_PolicyEngine_Building_NamedElement, gen_PolicyEngine_LightSwitchActuator_Actuator, gen_PolicyEngine_Sensor_HasIntegerValue, gen_PolicyEngine_Actuator_HasIntegerValue, gen_PolicyEngine_SensorComponent_HasSensors, gen_PolicyEngine_SensorComponent_NamedElement, gen_PolicyEngine_MotionSensor_Sensor, gen_PolicyEngine_TemperatureSensor_Sensor, gen_PolicyEngine_PressureSensor_Sensor, gen_PolicyEngine_TouchSensor_Sensor, gen_PolicyEngine_WindowActuator_Actuator, gen_PolicyEngine_HumidifierActuator_Actuator, gen_PolicyEngine_LightSensor_Sensor, gen_PolicyEngine_Model_NamedElement, gen_PolicyEngine_AudioAlarmActuator_Actuator, gen_PolicyEngine_Room_NamedElement, gen_PolicyEngine_Floor_NamedElement, gen_PolicyEngine_ActuatorComponent_HasActuators, gen_PolicyEngine_ActuatorComponent_NamedElement, gen_PolicyEngine_Policy_NamedElement, gen_PolicyEngine_DoorActuator_Actuator, gen_PolicyEngine_RadiatorActuator_Actuator, gen_PolicyEngine_SmokeSensor_Sensor, gen_PolicyEngine_CO2Sensor_Sensor, gen_PolicyEngine_InfraredLightSensor_Sensor, gen_PolicyEngine_HumiditySensor_Sensor, gen_PolicyEngine_Timer_NamedElement, gen_PolicyEngine_Schedule_NamedElement, gen_PolicyEngine_State_NamedElement, gen_PolicyEngine_BinaryOps_Expression, gen_PolicyEngine_UnaryOp_Expression, gen_PolicyEngine_Id_Expression, gen_PolicyEngine_Id_NamedElement, gen_PolicyEngine_RoomActuators_Expression, gen_PolicyEngine_TimeExpression_Expression, gen_PolicyEngine_ResetExpression_Expression, gen_PolicyEngine_RoomUsage_Expression, gen_PolicyEngine_Constant_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)