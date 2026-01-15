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
DirectionVal: Enumeration = Enumeration(
    name="DirectionVal",
    literals={
            EnumerationLiteral(name="FORWARD"),
			EnumerationLiteral(name="BACKWARD"),
			EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

SensorType: Enumeration = Enumeration(
    name="SensorType",
    literals={
            EnumerationLiteral(name="COLOR"),
			EnumerationLiteral(name="LEFTLIGHT"),
			EnumerationLiteral(name="RIGHTLIGHT"),
			EnumerationLiteral(name="BACKUS"),
			EnumerationLiteral(name="FRONTUS"),
			EnumerationLiteral(name="LEFTTOUCH"),
			EnumerationLiteral(name="RIGHTTOUCH"),
			EnumerationLiteral(name="GYRO")
    }
)

ColorName: Enumeration = Enumeration(
    name="ColorName",
    literals={
            EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="BLUE")
    }
)

BoolType: Enumeration = Enumeration(
    name="BoolType",
    literals={
            EnumerationLiteral(name="L"),
			EnumerationLiteral(name="G"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="TRUE"),
			EnumerationLiteral(name="FALSE")
    }
)

SpeedVal: Enumeration = Enumeration(
    name="SpeedVal",
    literals={
            EnumerationLiteral(name="HIGH"),
			EnumerationLiteral(name="MED"),
			EnumerationLiteral(name="LOW")
    }
)

ArmOpType: Enumeration = Enumeration(
    name="ArmOpType",
    literals={
            EnumerationLiteral(name="UP"),
			EnumerationLiteral(name="DOWN")
    }
)

SoundName: Enumeration = Enumeration(
    name="SoundName",
    literals={
            EnumerationLiteral(name="FANFARE"),
			EnumerationLiteral(name="BUZZ")
    }
)

# Classes
robotDSL_Mission = Class(name="robotDSL::Mission")
robotDSL_Flag = Class(name="robotDSL::Flag")
robotDSL_Task = Class(name="robotDSL::Task")
robotDSL_Goal = Class(name="robotDSL::Goal")
robotDSL_Trigger = Class(name="robotDSL::Trigger")
robotDSL_Time = Class(name="robotDSL::Time")
robotDSL_Action = Class(name="robotDSL::Action")
robotDSL_Direction = Class(name="robotDSL::Direction")
robotDSL_Missions = Class(name="robotDSL::Missions")
robotDSL_Bool = Class(name="robotDSL::Bool")
robotDSL_Negation = Class(name="robotDSL::Negation")
robotDSL_Sensor = Class(name="robotDSL::Sensor")
robotDSL_Color = Class(name="robotDSL::Color")
robotDSL_Distance = Class(name="robotDSL::Distance")
robotDSL_Speed = Class(name="robotDSL::Speed")
robotDSL_ArmOp = Class(name="robotDSL::ArmOp")
robotDSL_Sound = Class(name="robotDSL::Sound")

# robotDSL_Mission class attributes and methods
robotDSL_Mission_name: Property = Property(name="name", type=StringType)
robotDSL_Mission.attributes={robotDSL_Mission_name}

# robotDSL_Flag class attributes and methods
robotDSL_Flag_name: Property = Property(name="name", type=StringType)
robotDSL_Flag.attributes={robotDSL_Flag_name}

# robotDSL_Task class attributes and methods
robotDSL_Task_name: Property = Property(name="name", type=StringType)
robotDSL_Task_prio: Property = Property(name="prio", type=IntegerType)
robotDSL_Task.attributes={robotDSL_Task_name, robotDSL_Task_prio}

# robotDSL_Goal class attributes and methods

# robotDSL_Trigger class attributes and methods
robotDSL_Trigger_touching: Property = Property(name="touching", type=StringType)
robotDSL_Trigger_degrees: Property = Property(name="degrees", type=IntegerType)
robotDSL_Trigger.attributes={robotDSL_Trigger_degrees, robotDSL_Trigger_touching}

# robotDSL_Time class attributes and methods
robotDSL_Time_sec: Property = Property(name="sec", type=IntegerType)
robotDSL_Time.attributes={robotDSL_Time_sec}

# robotDSL_Action class attributes and methods
robotDSL_Action_duration: Property = Property(name="duration", type=IntegerType)
robotDSL_Action_cent: Property = Property(name="cent", type=StringType)
robotDSL_Action_degr: Property = Property(name="degr", type=IntegerType)
robotDSL_Action.attributes={robotDSL_Action_duration, robotDSL_Action_degr, robotDSL_Action_cent}

# robotDSL_Direction class attributes and methods
robotDSL_Direction_dir: Property = Property(name="dir", type=StringType)
robotDSL_Direction.attributes={robotDSL_Direction_dir}

# robotDSL_Missions class attributes and methods
robotDSL_Missions_name: Property = Property(name="name", type=StringType)
robotDSL_Missions.attributes={robotDSL_Missions_name}

# robotDSL_Bool class attributes and methods
robotDSL_Bool_boolType: Property = Property(name="boolType", type=StringType)
robotDSL_Bool.attributes={robotDSL_Bool_boolType}

# robotDSL_Negation class attributes and methods
robotDSL_Negation_NOT: Property = Property(name="NOT", type=StringType)
robotDSL_Negation.attributes={robotDSL_Negation_NOT}

# robotDSL_Sensor class attributes and methods
robotDSL_Sensor_sensorType: Property = Property(name="sensorType", type=StringType)
robotDSL_Sensor.attributes={robotDSL_Sensor_sensorType}

# robotDSL_Color class attributes and methods
robotDSL_Color_colorName: Property = Property(name="colorName", type=StringType)
robotDSL_Color.attributes={robotDSL_Color_colorName}

# robotDSL_Distance class attributes and methods
robotDSL_Distance_distance: Property = Property(name="distance", type=IntegerType)
robotDSL_Distance.attributes={robotDSL_Distance_distance}

# robotDSL_Speed class attributes and methods
robotDSL_Speed_speed: Property = Property(name="speed", type=StringType)
robotDSL_Speed.attributes={robotDSL_Speed_speed}

# robotDSL_ArmOp class attributes and methods
robotDSL_ArmOp_opType: Property = Property(name="opType", type=StringType)
robotDSL_ArmOp.attributes={robotDSL_ArmOp_opType}

# robotDSL_Sound class attributes and methods
robotDSL_Sound_soundName: Property = Property(name="soundName", type=StringType)
robotDSL_Sound.attributes={robotDSL_Sound_soundName}

# Relationships
missionList0: BinaryAssociation = BinaryAssociation(
    name="missionList0",
    ends={
        Property(name="robotDSL_Mission", type=robotDSL_Missions, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Missions", type=robotDSL_Mission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
flagsList1: BinaryAssociation = BinaryAssociation(
    name="flagsList1",
    ends={
        Property(name="robotDSL_Flag", type=robotDSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Mission2", type=robotDSL_Flag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskList3: BinaryAssociation = BinaryAssociation(
    name="taskList3",
    ends={
        Property(name="robotDSL_Task", type=robotDSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Mission4", type=robotDSL_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goal5: BinaryAssociation = BinaryAssociation(
    name="goal5",
    ends={
        Property(name="robotDSL_Goal", type=robotDSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Mission6", type=robotDSL_Goal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
goalEvents7: BinaryAssociation = BinaryAssociation(
    name="goalEvents7",
    ends={
        Property(name="robotDSL_Trigger", type=robotDSL_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Goal8", type=robotDSL_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
timeout9: BinaryAssociation = BinaryAssociation(
    name="timeout9",
    ends={
        Property(name="robotDSL_Time", type=robotDSL_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Goal10", type=robotDSL_Time, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finishActions11: BinaryAssociation = BinaryAssociation(
    name="finishActions11",
    ends={
        Property(name="robotDSL_Action", type=robotDSL_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Goal12", type=robotDSL_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggerList13: BinaryAssociation = BinaryAssociation(
    name="triggerList13",
    ends={
        Property(name="robotDSL_Trigger15", type=robotDSL_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Task14", type=robotDSL_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionList16: BinaryAssociation = BinaryAssociation(
    name="actionList16",
    ends={
        Property(name="robotDSL_Action18", type=robotDSL_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Task17", type=robotDSL_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
moveDir19: BinaryAssociation = BinaryAssociation(
    name="moveDir19",
    ends={
        Property(name="robotDSL_Direction", type=robotDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Action20", type=robotDSL_Direction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bool36: BinaryAssociation = BinaryAssociation(
    name="bool36",
    ends={
        Property(name="robotDSL_Bool", type=robotDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Action37", type=robotDSL_Bool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boolType38: BinaryAssociation = BinaryAssociation(
    name="boolType38",
    ends={
        Property(name="robotDSL_Bool40", type=robotDSL_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Trigger39", type=robotDSL_Bool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
neg41: BinaryAssociation = BinaryAssociation(
    name="neg41",
    ends={
        Property(name="robotDSL_Negation", type=robotDSL_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Trigger42", type=robotDSL_Negation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flag43: BinaryAssociation = BinaryAssociation(
    name="flag43",
    ends={
        Property(name="robotDSL_Flag45", type=robotDSL_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Trigger44", type=robotDSL_Flag, multiplicity=Multiplicity(0, 1))
    }
)
sensor46: BinaryAssociation = BinaryAssociation(
    name="sensor46",
    ends={
        Property(name="robotDSL_Sensor", type=robotDSL_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Trigger47", type=robotDSL_Sensor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
color48: BinaryAssociation = BinaryAssociation(
    name="color48",
    ends={
        Property(name="robotDSL_Color", type=robotDSL_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Trigger49", type=robotDSL_Color, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dist50: BinaryAssociation = BinaryAssociation(
    name="dist50",
    ends={
        Property(name="robotDSL_Distance", type=robotDSL_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Trigger51", type=robotDSL_Distance, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rangeBool52: BinaryAssociation = BinaryAssociation(
    name="rangeBool52",
    ends={
        Property(name="robotDSL_Bool54", type=robotDSL_Distance, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Distance53", type=robotDSL_Bool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
speed21: BinaryAssociation = BinaryAssociation(
    name="speed21",
    ends={
        Property(name="robotDSL_Speed", type=robotDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Action22", type=robotDSL_Speed, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
turnDir23: BinaryAssociation = BinaryAssociation(
    name="turnDir23",
    ends={
        Property(name="robotDSL_Direction25", type=robotDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Action24", type=robotDSL_Direction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trig26: BinaryAssociation = BinaryAssociation(
    name="trig26",
    ends={
        Property(name="robotDSL_Trigger28", type=robotDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Action27", type=robotDSL_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op29: BinaryAssociation = BinaryAssociation(
    name="op29",
    ends={
        Property(name="robotDSL_ArmOp", type=robotDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Action30", type=robotDSL_ArmOp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sound31: BinaryAssociation = BinaryAssociation(
    name="sound31",
    ends={
        Property(name="robotDSL_Sound", type=robotDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Action32", type=robotDSL_Sound, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
flag33: BinaryAssociation = BinaryAssociation(
    name="flag33",
    ends={
        Property(name="robotDSL_Flag35", type=robotDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="robotDSL_Action34", type=robotDSL_Flag, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="robotDSL",
    types={robotDSL_Mission, robotDSL_Flag, robotDSL_Task, robotDSL_Goal, robotDSL_Trigger, robotDSL_Time, robotDSL_Action, robotDSL_Direction, robotDSL_Missions, robotDSL_Bool, robotDSL_Negation, robotDSL_Sensor, robotDSL_Color, robotDSL_Distance, robotDSL_Speed, robotDSL_ArmOp, robotDSL_Sound, DirectionVal, SensorType, ColorName, BoolType, SpeedVal, ArmOpType, SoundName},
    associations={missionList0, flagsList1, taskList3, goal5, goalEvents7, timeout9, finishActions11, triggerList13, actionList16, moveDir19, bool36, boolType38, neg41, flag43, sensor46, color48, dist50, rangeBool52, speed21, turnDir23, trig26, op29, sound31, flag33},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)