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

# Classes
dSL_RightMovementAction = Class(name="dSL::RightMovementAction")
dSL_RotateMovementAction = Class(name="dSL::RotateMovementAction")
dSL_RotatePoints = Class(name="dSL::RotatePoints")
dSL_RobotBehavior = Class(name="dSL::RobotBehavior")
dSL_Behaviors = Class(name="dSL::Behaviors")
dSL_Expression = Class(name="dSL::Expression")
dSL_Actions = Class(name="dSL::Actions")
dSL_LeftMovementAction = Class(name="dSL::LeftMovementAction")
Actions = Class(name="Actions")
dSL_MovementAction = Class(name="dSL::MovementAction")
RotateMovementAction = Class(name="RotateMovementAction")
dSL_LeftRotatePoint = Class(name="dSL::LeftRotatePoint")
RotatePoints = Class(name="RotatePoints")
dSL_RightRotatePoint = Class(name="dSL::RightRotatePoint")
dSL_MiddleRotatePoint = Class(name="dSL::MiddleRotatePoint")
dSL_ExpressionBracket = Class(name="dSL::ExpressionBracket")
Expression = Class(name="Expression")
dSL_TouchLiteral = Class(name="dSL::TouchLiteral")
dSL_ColorLiteral = Class(name="dSL::ColorLiteral")
dSL_DistanceLiteral = Class(name="dSL::DistanceLiteral")
dSL_EdgeLiteral = Class(name="dSL::EdgeLiteral")
dSL_ANDexpression = Class(name="dSL::ANDexpression")
dSL_ORexpression = Class(name="dSL::ORexpression")

# dSL_RightMovementAction class attributes and methods

# dSL_RotateMovementAction class attributes and methods

# dSL_RotatePoints class attributes and methods
dSL_RotatePoints_degrees: Property = Property(name="degrees", type=IntegerType)
dSL_RotatePoints.attributes={dSL_RotatePoints_degrees}

# dSL_RobotBehavior class attributes and methods

# dSL_Behaviors class attributes and methods
dSL_Behaviors_name: Property = Property(name="name", type=StringType)
dSL_Behaviors.attributes={dSL_Behaviors_name}

# dSL_Expression class attributes and methods

# dSL_Actions class attributes and methods

# dSL_LeftMovementAction class attributes and methods

# Actions class attributes and methods

# dSL_MovementAction class attributes and methods
dSL_MovementAction_actionenum: Property = Property(name="actionenum", type=StringType)
dSL_MovementAction.attributes={dSL_MovementAction_actionenum}

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

# dSL_ExpressionBracket class attributes and methods

# Expression class attributes and methods

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
rightmove6: BinaryAssociation = BinaryAssociation(
    name="rightmove6",
    ends={
        Property(name="dSL_MovementAction7", type=dSL_RightMovementAction, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_RightMovementAction", type=dSL_MovementAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
behaviorlist0: BinaryAssociation = BinaryAssociation(
    name="behaviorlist0",
    ends={
        Property(name="dSL_Behaviors", type=dSL_RobotBehavior, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_RobotBehavior", type=dSL_Behaviors, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sensorExpression1: BinaryAssociation = BinaryAssociation(
    name="sensorExpression1",
    ends={
        Property(name="dSL_Expression", type=dSL_Behaviors, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Behaviors2", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actionlist3: BinaryAssociation = BinaryAssociation(
    name="actionlist3",
    ends={
        Property(name="dSL_Actions", type=dSL_Behaviors, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_Behaviors4", type=dSL_Actions, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftmove5: BinaryAssociation = BinaryAssociation(
    name="leftmove5",
    ends={
        Property(name="dSL_MovementAction", type=dSL_LeftMovementAction, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_LeftMovementAction", type=dSL_MovementAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp8: BinaryAssociation = BinaryAssociation(
    name="exp8",
    ends={
        Property(name="dSL_Expression9", type=dSL_ExpressionBracket, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ExpressionBracket", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left10: BinaryAssociation = BinaryAssociation(
    name="left10",
    ends={
        Property(name="dSL_Expression11", type=dSL_ANDexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ANDexpression", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right12: BinaryAssociation = BinaryAssociation(
    name="right12",
    ends={
        Property(name="dSL_Expression14", type=dSL_ANDexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ANDexpression13", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left15: BinaryAssociation = BinaryAssociation(
    name="left15",
    ends={
        Property(name="dSL_Expression16", type=dSL_ORexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ORexpression", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right17: BinaryAssociation = BinaryAssociation(
    name="right17",
    ends={
        Property(name="dSL_Expression19", type=dSL_ORexpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dSL_ORexpression18", type=dSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dSL_RightMovementAction_Actions = Generalization(general=Actions, specific=dSL_RightMovementAction)
gen_dSL_RotateMovementAction_Actions = Generalization(general=Actions, specific=dSL_RotateMovementAction)
gen_dSL_LeftMovementAction_Actions = Generalization(general=Actions, specific=dSL_LeftMovementAction)
gen_dSL_RotatePoints_RotateMovementAction = Generalization(general=RotateMovementAction, specific=dSL_RotatePoints)
gen_dSL_LeftRotatePoint_RotatePoints = Generalization(general=RotatePoints, specific=dSL_LeftRotatePoint)
gen_dSL_RightRotatePoint_RotatePoints = Generalization(general=RotatePoints, specific=dSL_RightRotatePoint)
gen_dSL_MiddleRotatePoint_RotatePoints = Generalization(general=RotatePoints, specific=dSL_MiddleRotatePoint)
gen_dSL_ExpressionBracket_Expression = Generalization(general=Expression, specific=dSL_ExpressionBracket)
gen_dSL_TouchLiteral_Expression = Generalization(general=Expression, specific=dSL_TouchLiteral)
gen_dSL_ColorLiteral_Expression = Generalization(general=Expression, specific=dSL_ColorLiteral)
gen_dSL_DistanceLiteral_Expression = Generalization(general=Expression, specific=dSL_DistanceLiteral)
gen_dSL_EdgeLiteral_Expression = Generalization(general=Expression, specific=dSL_EdgeLiteral)
gen_dSL_ANDexpression_Expression = Generalization(general=Expression, specific=dSL_ANDexpression)
gen_dSL_ORexpression_Expression = Generalization(general=Expression, specific=dSL_ORexpression)

# Domain Model
domain_model = DomainModel(
    name="dSL",
    types={dSL_RightMovementAction, dSL_RotateMovementAction, dSL_RotatePoints, dSL_RobotBehavior, dSL_Behaviors, dSL_Expression, dSL_Actions, dSL_LeftMovementAction, Actions, dSL_MovementAction, RotateMovementAction, dSL_LeftRotatePoint, RotatePoints, dSL_RightRotatePoint, dSL_MiddleRotatePoint, dSL_ExpressionBracket, Expression, dSL_TouchLiteral, dSL_ColorLiteral, dSL_DistanceLiteral, dSL_EdgeLiteral, dSL_ANDexpression, dSL_ORexpression, ColorEnum, LREnum, FBEnum, ActionEnum, EdgeEnum, TouchEnum},
    associations={rightmove6, behaviorlist0, sensorExpression1, actionlist3, leftmove5, exp8, left10, right12, left15, right17},
    generalizations={gen_dSL_RightMovementAction_Actions, gen_dSL_RotateMovementAction_Actions, gen_dSL_LeftMovementAction_Actions, gen_dSL_RotatePoints_RotateMovementAction, gen_dSL_LeftRotatePoint_RotatePoints, gen_dSL_RightRotatePoint_RotatePoints, gen_dSL_MiddleRotatePoint_RotatePoints, gen_dSL_ExpressionBracket_Expression, gen_dSL_TouchLiteral_Expression, gen_dSL_ColorLiteral_Expression, gen_dSL_DistanceLiteral_Expression, gen_dSL_EdgeLiteral_Expression, gen_dSL_ANDexpression_Expression, gen_dSL_ORexpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)