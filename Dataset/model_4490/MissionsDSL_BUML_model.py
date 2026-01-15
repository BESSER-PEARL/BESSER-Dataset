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
Relation: Enumeration = Enumeration(
    name="Relation",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="LT"),
			EnumerationLiteral(name="LE"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="GE")
    }
)

MissionType: Enumeration = Enumeration(
    name="MissionType",
    literals={
            EnumerationLiteral(name="AVOID"),
			EnumerationLiteral(name="FIND"),
			EnumerationLiteral(name="FINDINORDER"),
			EnumerationLiteral(name="FINDSIMULTANEOUS")
    }
)

Sensor: Enumeration = Enumeration(
    name="Sensor",
    literals={
            EnumerationLiteral(name="proximity"),
			EnumerationLiteral(name="touch"),
			EnumerationLiteral(name="color")
    }
)

EV3_ACTION: Enumeration = Enumeration(
    name="EV3_ACTION",
    literals={
            EnumerationLiteral(name="STOP"),
			EnumerationLiteral(name="REVERSE"),
			EnumerationLiteral(name="PLAY"),
			EnumerationLiteral(name="ROTATE"),
			EnumerationLiteral(name="HALT")
    }
)

Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="YELLOW"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="BROWN")
    }
)

# Classes
missionsDSL_Robot = Class(name="missionsDSL::Robot")
missionsDSL_Mission = Class(name="missionsDSL::Mission")
missionsDSL_Condition = Class(name="missionsDSL::Condition")
missionsDSL_Action = Class(name="missionsDSL::Action")
missionsDSL_NewMissions = Class(name="missionsDSL::NewMissions")
missionsDSL_Value = Class(name="missionsDSL::Value")

# missionsDSL_Robot class attributes and methods
missionsDSL_Robot_slaveAddress: Property = Property(name="slaveAddress", type=StringType)
missionsDSL_Robot_refreshRate: Property = Property(name="refreshRate", type=IntegerType)
missionsDSL_Robot_defaultSpeed: Property = Property(name="defaultSpeed", type=IntegerType)
missionsDSL_Robot_slowSpeed: Property = Property(name="slowSpeed", type=IntegerType)
missionsDSL_Robot_minAngle: Property = Property(name="minAngle", type=IntegerType)
missionsDSL_Robot_maxAngle: Property = Property(name="maxAngle", type=IntegerType)
missionsDSL_Robot.attributes={missionsDSL_Robot_minAngle, missionsDSL_Robot_defaultSpeed, missionsDSL_Robot_slaveAddress, missionsDSL_Robot_slowSpeed, missionsDSL_Robot_maxAngle, missionsDSL_Robot_refreshRate}

# missionsDSL_Mission class attributes and methods
missionsDSL_Mission_name: Property = Property(name="name", type=StringType)
missionsDSL_Mission_priority: Property = Property(name="priority", type=IntegerType)
missionsDSL_Mission_type: Property = Property(name="type", type=StringType)
missionsDSL_Mission.attributes={missionsDSL_Mission_type, missionsDSL_Mission_name, missionsDSL_Mission_priority}

# missionsDSL_Condition class attributes and methods
missionsDSL_Condition_sensor: Property = Property(name="sensor", type=StringType)
missionsDSL_Condition_relation: Property = Property(name="relation", type=StringType)
missionsDSL_Condition.attributes={missionsDSL_Condition_sensor, missionsDSL_Condition_relation}

# missionsDSL_Action class attributes and methods
missionsDSL_Action_action: Property = Property(name="action", type=StringType)
missionsDSL_Action_value: Property = Property(name="value", type=IntegerType)
missionsDSL_Action_duration: Property = Property(name="duration", type=IntegerType)
missionsDSL_Action.attributes={missionsDSL_Action_value, missionsDSL_Action_duration, missionsDSL_Action_action}

# missionsDSL_NewMissions class attributes and methods

# missionsDSL_Value class attributes and methods
missionsDSL_Value_color: Property = Property(name="color", type=StringType)
missionsDSL_Value_integer: Property = Property(name="integer", type=IntegerType)
missionsDSL_Value_bool: Property = Property(name="bool", type=StringType)
missionsDSL_Value.attributes={missionsDSL_Value_color, missionsDSL_Value_bool, missionsDSL_Value_integer}

# Relationships
startMissions0: BinaryAssociation = BinaryAssociation(
    name="startMissions0",
    ends={
        Property(name="missionsDSL_Mission", type=missionsDSL_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="missionsDSL_Robot", type=missionsDSL_Mission, multiplicity=Multiplicity(0, 9999))
    }
)
availableMissions1: BinaryAssociation = BinaryAssociation(
    name="availableMissions1",
    ends={
        Property(name="missionsDSL_Mission3", type=missionsDSL_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="missionsDSL_Robot2", type=missionsDSL_Mission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cond4: BinaryAssociation = BinaryAssociation(
    name="cond4",
    ends={
        Property(name="missionsDSL_Condition", type=missionsDSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="missionsDSL_Mission5", type=missionsDSL_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionsAfterSetOfConditions6: BinaryAssociation = BinaryAssociation(
    name="actionsAfterSetOfConditions6",
    ends={
        Property(name="missionsDSL_Action", type=missionsDSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="missionsDSL_Mission7", type=missionsDSL_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
newMission8: BinaryAssociation = BinaryAssociation(
    name="newMission8",
    ends={
        Property(name="missionsDSL_NewMissions", type=missionsDSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="missionsDSL_Mission9", type=missionsDSL_NewMissions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value10: BinaryAssociation = BinaryAssociation(
    name="value10",
    ends={
        Property(name="missionsDSL_Value", type=missionsDSL_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="missionsDSL_Condition11", type=missionsDSL_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifConditionTrue12: BinaryAssociation = BinaryAssociation(
    name="ifConditionTrue12",
    ends={
        Property(name="missionsDSL_Action14", type=missionsDSL_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="missionsDSL_Condition13", type=missionsDSL_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
missions15: BinaryAssociation = BinaryAssociation(
    name="missions15",
    ends={
        Property(name="missionsDSL_Mission17", type=missionsDSL_NewMissions, multiplicity=Multiplicity(1, 1)),
        Property(name="missionsDSL_NewMissions16", type=missionsDSL_Mission, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="missionsDSL",
    types={missionsDSL_Robot, missionsDSL_Mission, missionsDSL_Condition, missionsDSL_Action, missionsDSL_NewMissions, missionsDSL_Value, Relation, MissionType, Sensor, EV3_ACTION, Color},
    associations={startMissions0, availableMissions1, cond4, actionsAfterSetOfConditions6, newMission8, value10, ifConditionTrue12, missions15},
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