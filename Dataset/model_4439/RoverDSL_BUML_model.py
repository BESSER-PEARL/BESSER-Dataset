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
Sensor: Enumeration = Enumeration(
    name="Sensor",
    literals={
            EnumerationLiteral(name="COLORIDSENSOR"),
			EnumerationLiteral(name="LEFTLIGHTSENSOR"),
			EnumerationLiteral(name="RIGHTLIGHTSENSOR"),
			EnumerationLiteral(name="FRONTULTRASONICSENSOR"),
			EnumerationLiteral(name="REARULTRASONICSENSOR"),
			EnumerationLiteral(name="TOUCHSENSORL"),
			EnumerationLiteral(name="TOUCHSENSORR"),
			EnumerationLiteral(name="ANGLESENSOR")
    }
)

EMotor: Enumeration = Enumeration(
    name="EMotor",
    literals={
            EnumerationLiteral(name="LEFTMOTOR"),
			EnumerationLiteral(name="RIGHTMOTOR")
    }
)

Sound: Enumeration = Enumeration(
    name="Sound",
    literals={
            EnumerationLiteral(name="BEEP"),
			EnumerationLiteral(name="BUZZ")
    }
)

BBinaryOp: Enumeration = Enumeration(
    name="BBinaryOp",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

CompareOp: Enumeration = Enumeration(
    name="CompareOp",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NEQ"),
			EnumerationLiteral(name="GEQ"),
			EnumerationLiteral(name="GT"),
			EnumerationLiteral(name="LEQ"),
			EnumerationLiteral(name="LT")
    }
)

Color: Enumeration = Enumeration(
    name="Color",
    literals={
            EnumerationLiteral(name="BLACK"),
			EnumerationLiteral(name="BLUE"),
			EnumerationLiteral(name="BROWN"),
			EnumerationLiteral(name="CYAN"),
			EnumerationLiteral(name="DARK_GRAY"),
			EnumerationLiteral(name="GRAY"),
			EnumerationLiteral(name="GREEN"),
			EnumerationLiteral(name="LIGHT_GRAY"),
			EnumerationLiteral(name="MAGENTA"),
			EnumerationLiteral(name="ORANGE"),
			EnumerationLiteral(name="PINK"),
			EnumerationLiteral(name="RED"),
			EnumerationLiteral(name="WHITE"),
			EnumerationLiteral(name="YELLOW")
    }
)

# Classes
roverDSL_Robot = Class(name="roverDSL::Robot")
roverDSL_BehaviorName = Class(name="roverDSL::BehaviorName")
roverDSL_Global = Class(name="roverDSL::Global")
roverDSL_Static = Class(name="roverDSL::Static")
roverDSL_ValueExpression = Class(name="roverDSL::ValueExpression")
roverDSL_Implementation = Class(name="roverDSL::Implementation")
roverDSL_SubRoutine = Class(name="roverDSL::SubRoutine")
roverDSL_Motor = Class(name="roverDSL::Motor")
roverDSL_ValExpr = Class(name="roverDSL::ValExpr")
Expression = Class(name="Expression")
roverDSL_IFExpression = Class(name="roverDSL::IFExpression")
roverDSL_WHILEExpression = Class(name="roverDSL::WHILEExpression")
roverDSL_AssignExpression = Class(name="roverDSL::AssignExpression")
roverDSL_Action = Class(name="roverDSL::Action")
roverDSL_ForwardAction = Class(name="roverDSL::ForwardAction")
Action = Class(name="Action")
roverDSL_RotateAction = Class(name="roverDSL::RotateAction")
roverDSL_Expression = Class(name="roverDSL::Expression")
roverDSL_SubRoutineAction = Class(name="roverDSL::SubRoutineAction")
roverDSL_MeasureAction = Class(name="roverDSL::MeasureAction")
roverDSL_ShowAction = Class(name="roverDSL::ShowAction")
roverDSL_SoundAction = Class(name="roverDSL::SoundAction")
roverDSL_FreeAction = Class(name="roverDSL::FreeAction")
roverDSL_BNotExpr = Class(name="roverDSL::BNotExpr")
ValueExpression = Class(name="ValueExpression")
roverDSL_BVLiteral = Class(name="roverDSL::BVLiteral")
roverDSL_BBLiteral = Class(name="roverDSL::BBLiteral")
roverDSL_BVarLiteral = Class(name="roverDSL::BVarLiteral")
roverDSL_BSensorLiteral = Class(name="roverDSL::BSensorLiteral")
roverDSL_BVBracket = Class(name="roverDSL::BVBracket")
roverDSL_ColorLiteral = Class(name="roverDSL::ColorLiteral")
roverDSL_StopAction = Class(name="roverDSL::StopAction")
roverDSL_SAccelerationAction = Class(name="roverDSL::SAccelerationAction")
roverDSL_SSpeedAction = Class(name="roverDSL::SSpeedAction")
roverDSL_ExpressionBinOp = Class(name="roverDSL::ExpressionBinOp")
roverDSL_ExpressionBinComp = Class(name="roverDSL::ExpressionBinComp")

# roverDSL_Robot class attributes and methods

# roverDSL_BehaviorName class attributes and methods
roverDSL_BehaviorName_name: Property = Property(name="name", type=StringType)
roverDSL_BehaviorName.attributes={roverDSL_BehaviorName_name}

# roverDSL_Global class attributes and methods
roverDSL_Global_name: Property = Property(name="name", type=StringType)
roverDSL_Global.attributes={roverDSL_Global_name}

# roverDSL_Static class attributes and methods
roverDSL_Static_name: Property = Property(name="name", type=StringType)
roverDSL_Static.attributes={roverDSL_Static_name}

# roverDSL_ValueExpression class attributes and methods

# roverDSL_Implementation class attributes and methods

# roverDSL_SubRoutine class attributes and methods
roverDSL_SubRoutine_name: Property = Property(name="name", type=StringType)
roverDSL_SubRoutine.attributes={roverDSL_SubRoutine_name}

# roverDSL_Motor class attributes and methods
roverDSL_Motor_m: Property = Property(name="m", type=StringType)
roverDSL_Motor.attributes={roverDSL_Motor_m}

# roverDSL_ValExpr class attributes and methods

# Expression class attributes and methods

# roverDSL_IFExpression class attributes and methods

# roverDSL_WHILEExpression class attributes and methods

# roverDSL_AssignExpression class attributes and methods

# roverDSL_Action class attributes and methods

# roverDSL_ForwardAction class attributes and methods

# Action class attributes and methods

# roverDSL_RotateAction class attributes and methods
roverDSL_RotateAction_blocking: Property = Property(name="blocking", type=BooleanType)
roverDSL_RotateAction.attributes={roverDSL_RotateAction_blocking}

# roverDSL_Expression class attributes and methods

# roverDSL_SubRoutineAction class attributes and methods

# roverDSL_MeasureAction class attributes and methods

# roverDSL_ShowAction class attributes and methods
roverDSL_ShowAction_string: Property = Property(name="string", type=StringType)
roverDSL_ShowAction_sensor: Property = Property(name="sensor", type=StringType)
roverDSL_ShowAction.attributes={roverDSL_ShowAction_string, roverDSL_ShowAction_sensor}

# roverDSL_SoundAction class attributes and methods
roverDSL_SoundAction_sound: Property = Property(name="sound", type=StringType)
roverDSL_SoundAction.attributes={roverDSL_SoundAction_sound}

# roverDSL_FreeAction class attributes and methods

# roverDSL_BNotExpr class attributes and methods

# ValueExpression class attributes and methods

# roverDSL_BVLiteral class attributes and methods
roverDSL_BVLiteral_neg: Property = Property(name="neg", type=BooleanType)
roverDSL_BVLiteral_aValue: Property = Property(name="aValue", type=IntegerType)
roverDSL_BVLiteral.attributes={roverDSL_BVLiteral_aValue, roverDSL_BVLiteral_neg}

# roverDSL_BBLiteral class attributes and methods
roverDSL_BBLiteral_bValue: Property = Property(name="bValue", type=BooleanType)
roverDSL_BBLiteral.attributes={roverDSL_BBLiteral_bValue}

# roverDSL_BVarLiteral class attributes and methods
roverDSL_BVarLiteral_var: Property = Property(name="var", type=StringType)
roverDSL_BVarLiteral.attributes={roverDSL_BVarLiteral_var}

# roverDSL_BSensorLiteral class attributes and methods
roverDSL_BSensorLiteral_sensor: Property = Property(name="sensor", type=StringType)
roverDSL_BSensorLiteral.attributes={roverDSL_BSensorLiteral_sensor}

# roverDSL_BVBracket class attributes and methods

# roverDSL_ColorLiteral class attributes and methods
roverDSL_ColorLiteral_color: Property = Property(name="color", type=StringType)
roverDSL_ColorLiteral.attributes={roverDSL_ColorLiteral_color}

# roverDSL_StopAction class attributes and methods

# roverDSL_SAccelerationAction class attributes and methods

# roverDSL_SSpeedAction class attributes and methods

# roverDSL_ExpressionBinOp class attributes and methods
roverDSL_ExpressionBinOp_bop: Property = Property(name="bop", type=StringType)
roverDSL_ExpressionBinOp.attributes={roverDSL_ExpressionBinOp_bop}

# roverDSL_ExpressionBinComp class attributes and methods
roverDSL_ExpressionBinComp_bcomp: Property = Property(name="bcomp", type=StringType)
roverDSL_ExpressionBinComp.attributes={roverDSL_ExpressionBinComp_bcomp}

# Relationships
behaviorOrder0: BinaryAssociation = BinaryAssociation(
    name="behaviorOrder0",
    ends={
        Property(name="roverDSL_BehaviorName", type=roverDSL_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Robot", type=roverDSL_BehaviorName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globals1: BinaryAssociation = BinaryAssociation(
    name="globals1",
    ends={
        Property(name="roverDSL_Global", type=roverDSL_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Robot2", type=roverDSL_Global, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statics3: BinaryAssociation = BinaryAssociation(
    name="statics3",
    ends={
        Property(name="roverDSL_Static", type=roverDSL_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Robot4", type=roverDSL_Static, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stopBehaviour5: BinaryAssociation = BinaryAssociation(
    name="stopBehaviour5",
    ends={
        Property(name="roverDSL_ValueExpression", type=roverDSL_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Robot6", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
behaviors7: BinaryAssociation = BinaryAssociation(
    name="behaviors7",
    ends={
        Property(name="roverDSL_Implementation", type=roverDSL_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Robot8", type=roverDSL_Implementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subRoutines9: BinaryAssociation = BinaryAssociation(
    name="subRoutines9",
    ends={
        Property(name="roverDSL_SubRoutine", type=roverDSL_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Robot10", type=roverDSL_SubRoutine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions22: BinaryAssociation = BinaryAssociation(
    name="expressions22",
    ends={
        Property(name="roverDSL_Expression24", type=roverDSL_SubRoutine, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_SubRoutine23", type=roverDSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vExpr25: BinaryAssociation = BinaryAssociation(
    name="vExpr25",
    ends={
        Property(name="roverDSL_ValueExpression26", type=roverDSL_ValExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_ValExpr", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c27: BinaryAssociation = BinaryAssociation(
    name="c27",
    ends={
        Property(name="roverDSL_ValueExpression28", type=roverDSL_IFExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_IFExpression", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t29: BinaryAssociation = BinaryAssociation(
    name="t29",
    ends={
        Property(name="roverDSL_Expression31", type=roverDSL_IFExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_IFExpression30", type=roverDSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
e32: BinaryAssociation = BinaryAssociation(
    name="e32",
    ends={
        Property(name="roverDSL_Expression34", type=roverDSL_IFExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_IFExpression33", type=roverDSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c35: BinaryAssociation = BinaryAssociation(
    name="c35",
    ends={
        Property(name="roverDSL_ValueExpression36", type=roverDSL_WHILEExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_WHILEExpression", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
b37: BinaryAssociation = BinaryAssociation(
    name="b37",
    ends={
        Property(name="roverDSL_Expression39", type=roverDSL_WHILEExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_WHILEExpression38", type=roverDSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
global40: BinaryAssociation = BinaryAssociation(
    name="global40",
    ends={
        Property(name="roverDSL_Global41", type=roverDSL_AssignExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_AssignExpression", type=roverDSL_Global, multiplicity=Multiplicity(0, 1))
    }
)
v42: BinaryAssociation = BinaryAssociation(
    name="v42",
    ends={
        Property(name="roverDSL_ValueExpression44", type=roverDSL_AssignExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_AssignExpression43", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
motor45: BinaryAssociation = BinaryAssociation(
    name="motor45",
    ends={
        Property(name="roverDSL_Motor", type=roverDSL_ForwardAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_ForwardAction", type=roverDSL_Motor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
motor46: BinaryAssociation = BinaryAssociation(
    name="motor46",
    ends={
        Property(name="roverDSL_Motor47", type=roverDSL_RotateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_RotateAction", type=roverDSL_Motor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
degrees48: BinaryAssociation = BinaryAssociation(
    name="degrees48",
    ends={
        Property(name="roverDSL_ValueExpression50", type=roverDSL_RotateAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_RotateAction49", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value11: BinaryAssociation = BinaryAssociation(
    name="value11",
    ends={
        Property(name="roverDSL_ValueExpression13", type=roverDSL_Static, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Static12", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
for14: BinaryAssociation = BinaryAssociation(
    name="for14",
    ends={
        Property(name="roverDSL_BehaviorName16", type=roverDSL_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Implementation15", type=roverDSL_BehaviorName, multiplicity=Multiplicity(0, 1))
    }
)
controlCheck17: BinaryAssociation = BinaryAssociation(
    name="controlCheck17",
    ends={
        Property(name="roverDSL_ValueExpression19", type=roverDSL_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Implementation18", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions20: BinaryAssociation = BinaryAssociation(
    name="expressions20",
    ends={
        Property(name="roverDSL_Expression", type=roverDSL_Implementation, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_Implementation21", type=roverDSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
motor58: BinaryAssociation = BinaryAssociation(
    name="motor58",
    ends={
        Property(name="roverDSL_Motor59", type=roverDSL_SSpeedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_SSpeedAction", type=roverDSL_Motor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
v60: BinaryAssociation = BinaryAssociation(
    name="v60",
    ends={
        Property(name="roverDSL_ValueExpression62", type=roverDSL_SSpeedAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_SSpeedAction61", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
routine63: BinaryAssociation = BinaryAssociation(
    name="routine63",
    ends={
        Property(name="roverDSL_SubRoutine64", type=roverDSL_SubRoutineAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_SubRoutineAction", type=roverDSL_SubRoutine, multiplicity=Multiplicity(0, 1))
    }
)
motor65: BinaryAssociation = BinaryAssociation(
    name="motor65",
    ends={
        Property(name="roverDSL_Motor66", type=roverDSL_FreeAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_FreeAction", type=roverDSL_Motor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sub67: BinaryAssociation = BinaryAssociation(
    name="sub67",
    ends={
        Property(name="roverDSL_ValueExpression68", type=roverDSL_BNotExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_BNotExpr", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bsub69: BinaryAssociation = BinaryAssociation(
    name="bsub69",
    ends={
        Property(name="roverDSL_ValueExpression70", type=roverDSL_BVBracket, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_BVBracket", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
motor51: BinaryAssociation = BinaryAssociation(
    name="motor51",
    ends={
        Property(name="roverDSL_Motor52", type=roverDSL_StopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_StopAction", type=roverDSL_Motor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
motor53: BinaryAssociation = BinaryAssociation(
    name="motor53",
    ends={
        Property(name="roverDSL_Motor54", type=roverDSL_SAccelerationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_SAccelerationAction", type=roverDSL_Motor, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
v55: BinaryAssociation = BinaryAssociation(
    name="v55",
    ends={
        Property(name="roverDSL_ValueExpression57", type=roverDSL_SAccelerationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_SAccelerationAction56", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left71: BinaryAssociation = BinaryAssociation(
    name="left71",
    ends={
        Property(name="roverDSL_ValueExpression72", type=roverDSL_ExpressionBinOp, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_ExpressionBinOp", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right73: BinaryAssociation = BinaryAssociation(
    name="right73",
    ends={
        Property(name="roverDSL_ValueExpression75", type=roverDSL_ExpressionBinOp, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_ExpressionBinOp74", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left76: BinaryAssociation = BinaryAssociation(
    name="left76",
    ends={
        Property(name="roverDSL_ValueExpression77", type=roverDSL_ExpressionBinComp, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_ExpressionBinComp", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right78: BinaryAssociation = BinaryAssociation(
    name="right78",
    ends={
        Property(name="roverDSL_ValueExpression80", type=roverDSL_ExpressionBinComp, multiplicity=Multiplicity(1, 1)),
        Property(name="roverDSL_ExpressionBinComp79", type=roverDSL_ValueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_roverDSL_ValExpr_Expression = Generalization(general=Expression, specific=roverDSL_ValExpr)
gen_roverDSL_IFExpression_Expression = Generalization(general=Expression, specific=roverDSL_IFExpression)
gen_roverDSL_WHILEExpression_Expression = Generalization(general=Expression, specific=roverDSL_WHILEExpression)
gen_roverDSL_AssignExpression_Expression = Generalization(general=Expression, specific=roverDSL_AssignExpression)
gen_roverDSL_Action_Expression = Generalization(general=Expression, specific=roverDSL_Action)
gen_roverDSL_ForwardAction_Action = Generalization(general=Action, specific=roverDSL_ForwardAction)
gen_roverDSL_RotateAction_Action = Generalization(general=Action, specific=roverDSL_RotateAction)
gen_roverDSL_SubRoutineAction_Action = Generalization(general=Action, specific=roverDSL_SubRoutineAction)
gen_roverDSL_MeasureAction_Action = Generalization(general=Action, specific=roverDSL_MeasureAction)
gen_roverDSL_ShowAction_Action = Generalization(general=Action, specific=roverDSL_ShowAction)
gen_roverDSL_SoundAction_Action = Generalization(general=Action, specific=roverDSL_SoundAction)
gen_roverDSL_FreeAction_Action = Generalization(general=Action, specific=roverDSL_FreeAction)
gen_roverDSL_BNotExpr_ValueExpression = Generalization(general=ValueExpression, specific=roverDSL_BNotExpr)
gen_roverDSL_BVLiteral_ValueExpression = Generalization(general=ValueExpression, specific=roverDSL_BVLiteral)
gen_roverDSL_BBLiteral_ValueExpression = Generalization(general=ValueExpression, specific=roverDSL_BBLiteral)
gen_roverDSL_BVarLiteral_ValueExpression = Generalization(general=ValueExpression, specific=roverDSL_BVarLiteral)
gen_roverDSL_BSensorLiteral_ValueExpression = Generalization(general=ValueExpression, specific=roverDSL_BSensorLiteral)
gen_roverDSL_BVBracket_ValueExpression = Generalization(general=ValueExpression, specific=roverDSL_BVBracket)
gen_roverDSL_ColorLiteral_ValueExpression = Generalization(general=ValueExpression, specific=roverDSL_ColorLiteral)
gen_roverDSL_StopAction_Action = Generalization(general=Action, specific=roverDSL_StopAction)
gen_roverDSL_SAccelerationAction_Action = Generalization(general=Action, specific=roverDSL_SAccelerationAction)
gen_roverDSL_SSpeedAction_Action = Generalization(general=Action, specific=roverDSL_SSpeedAction)
gen_roverDSL_ExpressionBinOp_ValueExpression = Generalization(general=ValueExpression, specific=roverDSL_ExpressionBinOp)
gen_roverDSL_ExpressionBinComp_ValueExpression = Generalization(general=ValueExpression, specific=roverDSL_ExpressionBinComp)

# Domain Model
domain_model = DomainModel(
    name="roverDSL",
    types={roverDSL_Robot, roverDSL_BehaviorName, roverDSL_Global, roverDSL_Static, roverDSL_ValueExpression, roverDSL_Implementation, roverDSL_SubRoutine, roverDSL_Motor, roverDSL_ValExpr, Expression, roverDSL_IFExpression, roverDSL_WHILEExpression, roverDSL_AssignExpression, roverDSL_Action, roverDSL_ForwardAction, Action, roverDSL_RotateAction, roverDSL_Expression, roverDSL_SubRoutineAction, roverDSL_MeasureAction, roverDSL_ShowAction, roverDSL_SoundAction, roverDSL_FreeAction, roverDSL_BNotExpr, ValueExpression, roverDSL_BVLiteral, roverDSL_BBLiteral, roverDSL_BVarLiteral, roverDSL_BSensorLiteral, roverDSL_BVBracket, roverDSL_ColorLiteral, roverDSL_StopAction, roverDSL_SAccelerationAction, roverDSL_SSpeedAction, roverDSL_ExpressionBinOp, roverDSL_ExpressionBinComp, Sensor, EMotor, Sound, BBinaryOp, CompareOp, Color},
    associations={behaviorOrder0, globals1, statics3, stopBehaviour5, behaviors7, subRoutines9, expressions22, vExpr25, c27, t29, e32, c35, b37, global40, v42, motor45, motor46, degrees48, value11, for14, controlCheck17, expressions20, motor58, v60, routine63, motor65, sub67, bsub69, motor51, motor53, v55, left71, right73, left76, right78},
    generalizations={gen_roverDSL_ValExpr_Expression, gen_roverDSL_IFExpression_Expression, gen_roverDSL_WHILEExpression_Expression, gen_roverDSL_AssignExpression_Expression, gen_roverDSL_Action_Expression, gen_roverDSL_ForwardAction_Action, gen_roverDSL_RotateAction_Action, gen_roverDSL_SubRoutineAction_Action, gen_roverDSL_MeasureAction_Action, gen_roverDSL_ShowAction_Action, gen_roverDSL_SoundAction_Action, gen_roverDSL_FreeAction_Action, gen_roverDSL_BNotExpr_ValueExpression, gen_roverDSL_BVLiteral_ValueExpression, gen_roverDSL_BBLiteral_ValueExpression, gen_roverDSL_BVarLiteral_ValueExpression, gen_roverDSL_BSensorLiteral_ValueExpression, gen_roverDSL_BVBracket_ValueExpression, gen_roverDSL_ColorLiteral_ValueExpression, gen_roverDSL_StopAction_Action, gen_roverDSL_SAccelerationAction_Action, gen_roverDSL_SSpeedAction_Action, gen_roverDSL_ExpressionBinOp_ValueExpression, gen_roverDSL_ExpressionBinComp_ValueExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)