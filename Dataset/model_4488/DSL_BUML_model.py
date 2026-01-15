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
MAEnum: Enumeration = Enumeration(
    name="MAEnum",
    literals={
            EnumerationLiteral(name="MEASURE")
    }
)

LREnum: Enumeration = Enumeration(
    name="LREnum",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

FBEnum: Enumeration = Enumeration(
    name="FBEnum",
    literals={
            EnumerationLiteral(name="FORWARD"),
			EnumerationLiteral(name="BACKWARD")
    }
)

ActionEnum: Enumeration = Enumeration(
    name="ActionEnum",
    literals={
            EnumerationLiteral(name="FORWARD"),
			EnumerationLiteral(name="BACKWARD"),
			EnumerationLiteral(name="STOP")
    }
)

Tenum: Enumeration = Enumeration(
    name="Tenum",
    literals={
            EnumerationLiteral(name="TRUE")
    }
)

BackEnum: Enumeration = Enumeration(
    name="BackEnum",
    literals={
            EnumerationLiteral(name="BACK")
    }
)

EdgeEnum: Enumeration = Enumeration(
    name="EdgeEnum",
    literals={
            EnumerationLiteral(name="FRONTLEFT"),
			EnumerationLiteral(name="FRONTRIGHT"),
			EnumerationLiteral(name="BACK")
    }
)

TouchEnum: Enumeration = Enumeration(
    name="TouchEnum",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

ColorEnum: Enumeration = Enumeration(
    name="ColorEnum",
    literals={
            EnumerationLiteral(name="NONE"),
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
dSL_MarsRoverExpedition = Class(name="dSL::MarsRoverExpedition")
dSL_Mission = Class(name="dSL::Mission")
dSL_Behavior = Class(name="dSL::Behavior")
dSL_BehaviorName = Class(name="dSL::BehaviorName")
dSL_EndCondition = Class(name="dSL::EndCondition")
dSL_EndWhen = Class(name="dSL::EndWhen")
dSL_EndAfter = Class(name="dSL::EndAfter")
EndCondition = Class(name="EndCondition")
dSL_Expression = Class(name="dSL::Expression")
dSL_Actions = Class(name="dSL::Actions")
dSL_MoveAction = Class(name="dSL::MoveAction")
Actions = Class(name="Actions")
dSL_MeasurementAction = Class(name="dSL::MeasurementAction")
dSL_LeftMovementAction = Class(name="dSL::LeftMovementAction")
dSL_MovementAction = Class(name="dSL::MovementAction")
dSL_RightMovementAction = Class(name="dSL::RightMovementAction")
dSL_RotateMovementAction = Class(name="dSL::RotateMovementAction")
dSL_RotatePoints = Class(name="dSL::RotatePoints")
RotateMovementAction = Class(name="RotateMovementAction")
dSL_LeftRotatePoint = Class(name="dSL::LeftRotatePoint")
RotatePoints = Class(name="RotatePoints")
dSL_RightRotatePoint = Class(name="dSL::RightRotatePoint")
dSL_MiddleRotatePoint = Class(name="dSL::MiddleRotatePoint")
dSL_TrueLiteral = Class(name="dSL::TrueLiteral")
Expression = Class(name="Expression")
dSL_ExpressionBracket = Class(name="dSL::ExpressionBracket")
dSL_DepthLiteral = Class(name="dSL::DepthLiteral")
dSL_TouchLiteral = Class(name="dSL::TouchLiteral")
dSL_ColorLiteral = Class(name="dSL::ColorLiteral")
dSL_DistanceLiteral = Class(name="dSL::DistanceLiteral")
dSL_EdgeLiteral = Class(name="dSL::EdgeLiteral")
dSL_ANDexpression = Class(name="dSL::ANDexpression")
dSL_ORexpression = Class(name="dSL::ORexpression")

# dSL_MarsRoverExpedition class attributes and methods

# dSL_Mission class attributes and methods
dSL_Mission_name: Property = Property(name="name", type=StringType)
dSL_Mission.attributes={dSL_Mission_name}

# dSL_Behavior class attributes and methods
dSL_Behavior_name: Property = Property(name="name", type=StringType)
dSL_Behavior.attributes={dSL_Behavior_name}

# dSL_BehaviorName class attributes and methods
dSL_BehaviorName_name: Property = Property(name="name", type=StringType)
dSL_BehaviorName.attributes={dSL_BehaviorName_name}

# dSL_EndCondition class attributes and methods

# dSL_EndWhen class attributes and methods
dSL_EndWhen_name: Property = Property(name="name", type=StringType)
dSL_EndWhen_times: Property = Property(name="times", type=IntegerType)
dSL_EndWhen.attributes={dSL_EndWhen_name, dSL_EndWhen_times}

# dSL_EndAfter class attributes and methods
dSL_EndAfter_time: Property = Property(name="time", type=IntegerType)
dSL_EndAfter.attributes={dSL_EndAfter_time}

# EndCondition class attributes and methods

# dSL_Expression class attributes and methods

# dSL_Actions class attributes and methods

# dSL_MoveAction class attributes and methods
dSL_MoveAction_dir: Property = Property(name="dir", type=StringType)
dSL_MoveAction.attributes={dSL_MoveAction_dir}

# Actions class attributes and methods

# dSL_MeasurementAction class attributes and methods
dSL_MeasurementAction_measure: Property = Property(name="measure", type=StringType)
dSL_MeasurementAction.attributes={dSL_MeasurementAction_measure}

# dSL_LeftMovementAction class attributes and methods

# dSL_MovementAction class attributes and methods
dSL_MovementAction_actionenum: Property = Property(name="actionenum", type=StringType)
dSL_MovementAction.attributes={dSL_MovementAction_actionenum}

# dSL_RightMovementAction class attributes and methods

# dSL_RotateMovementAction class attributes and methods

# dSL_RotatePoints class attributes and methods
dSL_RotatePoints_degrees: Property = Property(name="degrees", type=IntegerType)
dSL_RotatePoints.attributes={dSL_RotatePoints_degrees}

# RotateMovementAction class attributes and methods

# dSL_LeftRotatePoint class attributes and methods
dSL_LeftRotatePoint_leftdir: Property = Property(name="leftdir", type=StringType)
dSL_LeftRotatePoint.attributes={dSL_LeftRotatePoint_leftdir}

# RotatePoints class attributes and methods

# dSL_RightRotatePoint class attributes and methods
dSL_RightRotatePoint_rightdir: Property = Property(name="rightdir", type=StringType)
dSL_RightRotatePoint.attributes={dSL_RightRotatePoint_rightdir}

# dSL_MiddleRotatePoint class attributes and methods
dSL_MiddleRotatePoint_middledir: Property = Property(name="middledir", type=StringType)
dSL_MiddleRotatePoint.attributes={dSL_MiddleRotatePoint_middledir}

# dSL_TrueLiteral class attributes and methods
dSL_TrueLiteral_t: Property = Property(name="t", type=StringType)
dSL_TrueLiteral.attributes={dSL_TrueLiteral_t}

# Expression class attributes and methods

# dSL_ExpressionBracket class attributes and methods

# dSL_DepthLiteral class attributes and methods
dSL_DepthLiteral_back: Property = Property(name="back", type=StringType)
dSL_DepthLiteral.attributes={dSL_DepthLiteral_back}

# dSL_TouchLiteral class attributes and methods
dSL_TouchLiteral_touch: Property = Property(name="touch", type=StringType)
dSL_TouchLiteral.attributes={dSL_TouchLiteral_touch}

# dSL_ColorLiteral class attributes and methods
dSL_ColorLiteral_color: Property = Property(name="color", type=StringType)
dSL_ColorLiteral.attributes={dSL_ColorLiteral_color}

# dSL_DistanceLiteral class attributes and methods
dSL_DistanceLiteral_distance: Property = Property(name="distance", type=IntegerType)
dSL_DistanceLiteral.attributes={dSL_DistanceLiteral_distance}

# dSL_EdgeLiteral class attributes and methods
dSL_EdgeLiteral_edge: Property = Property(name="edge", type=StringType)
dSL_EdgeLiteral.attributes={dSL_EdgeLiteral_edge}

# dSL_ANDexpression class attributes and methods

# dSL_ORexpression class attributes and methods

# Relationships
missionlist0: BinaryAssociation = BinaryAssociation(
    name="missionlist0",
    ends={
        Property(name="dSL_Mission", type=dSL_MarsRoverExpedition, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_MarsRoverExpedition", type=dSL_Mission, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasklist1: BinaryAssociation = BinaryAssociation(
    name="tasklist1",
    ends={
        Property(name="dSL_Behavior", type=dSL_MarsRoverExpedition, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_MarsRoverExpedition2", type=dSL_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviorlist3: BinaryAssociation = BinaryAssociation(
    name="behaviorlist3",
    ends={
        Property(name="dSL_BehaviorName", type=dSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Mission4", type=dSL_BehaviorName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endcondition5: BinaryAssociation = BinaryAssociation(
    name="endcondition5",
    ends={
        Property(name="dSL_EndCondition", type=dSL_Mission, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Mission6", type=dSL_EndCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endwhenlist7: BinaryAssociation = BinaryAssociation(
    name="endwhenlist7",
    ends={
        Property(name="dSL_EndWhen", type=dSL_EndCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_EndCondition8", type=dSL_EndWhen, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensorExpression9: BinaryAssociation = BinaryAssociation(
    name="sensorExpression9",
    ends={
        Property(name="dSL_Expression", type=dSL_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Behavior10", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionlist11: BinaryAssociation = BinaryAssociation(
    name="actionlist11",
    ends={
        Property(name="dSL_Actions", type=dSL_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Behavior12", type=dSL_Actions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftmove13: BinaryAssociation = BinaryAssociation(
    name="leftmove13",
    ends={
        Property(name="dSL_MovementAction", type=dSL_LeftMovementAction, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_LeftMovementAction", type=dSL_MovementAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightmove14: BinaryAssociation = BinaryAssociation(
    name="rightmove14",
    ends={
        Property(name="dSL_MovementAction15", type=dSL_RightMovementAction, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_RightMovementAction", type=dSL_MovementAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp16: BinaryAssociation = BinaryAssociation(
    name="exp16",
    ends={
        Property(name="dSL_Expression17", type=dSL_ExpressionBracket, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ExpressionBracket", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left18: BinaryAssociation = BinaryAssociation(
    name="left18",
    ends={
        Property(name="dSL_Expression19", type=dSL_ANDexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ANDexpression", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right20: BinaryAssociation = BinaryAssociation(
    name="right20",
    ends={
        Property(name="dSL_Expression22", type=dSL_ANDexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ANDexpression21", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left23: BinaryAssociation = BinaryAssociation(
    name="left23",
    ends={
        Property(name="dSL_Expression24", type=dSL_ORexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ORexpression", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right25: BinaryAssociation = BinaryAssociation(
    name="right25",
    ends={
        Property(name="dSL_Expression27", type=dSL_ORexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ORexpression26", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dSL_EndAfter_EndCondition = Generalization(general=EndCondition, specific=dSL_EndAfter)
gen_dSL_MoveAction_Actions = Generalization(general=Actions, specific=dSL_MoveAction)
gen_dSL_MeasurementAction_Actions = Generalization(general=Actions, specific=dSL_MeasurementAction)
gen_dSL_LeftMovementAction_Actions = Generalization(general=Actions, specific=dSL_LeftMovementAction)
gen_dSL_RightMovementAction_Actions = Generalization(general=Actions, specific=dSL_RightMovementAction)
gen_dSL_RotateMovementAction_Actions = Generalization(general=Actions, specific=dSL_RotateMovementAction)
gen_dSL_RotatePoints_RotateMovementAction = Generalization(general=RotateMovementAction, specific=dSL_RotatePoints)
gen_dSL_LeftRotatePoint_RotatePoints = Generalization(general=RotatePoints, specific=dSL_LeftRotatePoint)
gen_dSL_RightRotatePoint_RotatePoints = Generalization(general=RotatePoints, specific=dSL_RightRotatePoint)
gen_dSL_MiddleRotatePoint_RotatePoints = Generalization(general=RotatePoints, specific=dSL_MiddleRotatePoint)
gen_dSL_TrueLiteral_Expression = Generalization(general=Expression, specific=dSL_TrueLiteral)
gen_dSL_ExpressionBracket_Expression = Generalization(general=Expression, specific=dSL_ExpressionBracket)
gen_dSL_DepthLiteral_Expression = Generalization(general=Expression, specific=dSL_DepthLiteral)
gen_dSL_TouchLiteral_Expression = Generalization(general=Expression, specific=dSL_TouchLiteral)
gen_dSL_ColorLiteral_Expression = Generalization(general=Expression, specific=dSL_ColorLiteral)
gen_dSL_DistanceLiteral_Expression = Generalization(general=Expression, specific=dSL_DistanceLiteral)
gen_dSL_EdgeLiteral_Expression = Generalization(general=Expression, specific=dSL_EdgeLiteral)
gen_dSL_ANDexpression_Expression = Generalization(general=Expression, specific=dSL_ANDexpression)
gen_dSL_ORexpression_Expression = Generalization(general=Expression, specific=dSL_ORexpression)

# Domain Model
domain_model = DomainModel(
    name="dSL",
    types={dSL_MarsRoverExpedition, dSL_Mission, dSL_Behavior, dSL_BehaviorName, dSL_EndCondition, dSL_EndWhen, dSL_EndAfter, EndCondition, dSL_Expression, dSL_Actions, dSL_MoveAction, Actions, dSL_MeasurementAction, dSL_LeftMovementAction, dSL_MovementAction, dSL_RightMovementAction, dSL_RotateMovementAction, dSL_RotatePoints, RotateMovementAction, dSL_LeftRotatePoint, RotatePoints, dSL_RightRotatePoint, dSL_MiddleRotatePoint, dSL_TrueLiteral, Expression, dSL_ExpressionBracket, dSL_DepthLiteral, dSL_TouchLiteral, dSL_ColorLiteral, dSL_DistanceLiteral, dSL_EdgeLiteral, dSL_ANDexpression, dSL_ORexpression, MAEnum, LREnum, FBEnum, ActionEnum, Tenum, BackEnum, EdgeEnum, TouchEnum, ColorEnum},
    associations={missionlist0, tasklist1, behaviorlist3, endcondition5, endwhenlist7, sensorExpression9, actionlist11, leftmove13, rightmove14, exp16, left18, right20, left23, right25},
    generalizations={gen_dSL_EndAfter_EndCondition, gen_dSL_MoveAction_Actions, gen_dSL_MeasurementAction_Actions, gen_dSL_LeftMovementAction_Actions, gen_dSL_RightMovementAction_Actions, gen_dSL_RotateMovementAction_Actions, gen_dSL_RotatePoints_RotateMovementAction, gen_dSL_LeftRotatePoint_RotatePoints, gen_dSL_RightRotatePoint_RotatePoints, gen_dSL_MiddleRotatePoint_RotatePoints, gen_dSL_TrueLiteral_Expression, gen_dSL_ExpressionBracket_Expression, gen_dSL_DepthLiteral_Expression, gen_dSL_TouchLiteral_Expression, gen_dSL_ColorLiteral_Expression, gen_dSL_DistanceLiteral_Expression, gen_dSL_EdgeLiteral_Expression, gen_dSL_ANDexpression_Expression, gen_dSL_ORexpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)