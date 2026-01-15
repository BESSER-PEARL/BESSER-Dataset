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

# Classes
kmLogo_Instruction = Class(name="kmLogo::Instruction", is_abstract=True)
kmLogo_Primitive = Class(name="kmLogo::Primitive", is_abstract=True)
Instruction = Class(name="Instruction")
kmLogo_Back = Class(name="kmLogo::Back")
Primitive = Class(name="Primitive")
kmLogo_Expression = Class(name="kmLogo::Expression", is_abstract=True)
kmLogo_UnaryExpression = Class(name="kmLogo::UnaryExpression", is_abstract=True)
kmLogo_Constant = Class(name="kmLogo::Constant")
kmLogo_ProcCall = Class(name="kmLogo::ProcCall")
kmLogo_ProcDeclaration = Class(name="kmLogo::ProcDeclaration")
kmLogo_Parameter = Class(name="kmLogo::Parameter")
kmLogo_Forward = Class(name="kmLogo::Forward")
kmLogo_Left = Class(name="kmLogo::Left")
kmLogo_Right = Class(name="kmLogo::Right")
kmLogo_PenDown = Class(name="kmLogo::PenDown")
kmLogo_PenUp = Class(name="kmLogo::PenUp")
kmLogo_Clear = Class(name="kmLogo::Clear")
kmLogo_BinaryExp = Class(name="kmLogo::BinaryExp", is_abstract=True)
Expression = Class(name="Expression")
kmLogo_Repeat = Class(name="kmLogo::Repeat")
kmLogo_While = Class(name="kmLogo::While")
kmLogo_ParameterCall = Class(name="kmLogo::ParameterCall")
kmLogo_Plus = Class(name="kmLogo::Plus")
BinaryExp = Class(name="BinaryExp")
kmLogo_Minus = Class(name="kmLogo::Minus")
kmLogo_Mult = Class(name="kmLogo::Mult")
kmLogo_Div = Class(name="kmLogo::Div")
kmLogo_Equals = Class(name="kmLogo::Equals")
kmLogo_Greater = Class(name="kmLogo::Greater")
kmLogo_Lower = Class(name="kmLogo::Lower")
kmLogo_Cos = Class(name="kmLogo::Cos")
UnaryExpression = Class(name="UnaryExpression")
kmLogo_Block = Class(name="kmLogo::Block")
kmLogo_If = Class(name="kmLogo::If")
ControlStructure = Class(name="ControlStructure")
kmLogo_ControlStructure = Class(name="kmLogo::ControlStructure")
kmLogo_StackFrame = Class(name="kmLogo::StackFrame")
kmLogo_Variable = Class(name="kmLogo::Variable")
kmLogo_Sin = Class(name="kmLogo::Sin")
kmLogo_Tan = Class(name="kmLogo::Tan")
kmLogo_LogoProgram = Class(name="kmLogo::LogoProgram")
kmLogo_Turtle = Class(name="kmLogo::Turtle")
kmLogo_Point = Class(name="kmLogo::Point")
kmLogo_Segment = Class(name="kmLogo::Segment")
kmLogo_CallStack = Class(name="kmLogo::CallStack")

# kmLogo_Instruction class attributes and methods

# kmLogo_Primitive class attributes and methods

# Instruction class attributes and methods

# kmLogo_Back class attributes and methods

# Primitive class attributes and methods

# kmLogo_Expression class attributes and methods

# kmLogo_UnaryExpression class attributes and methods

# kmLogo_Constant class attributes and methods
kmLogo_Constant_value: Property = Property(name="value", type=FloatType)
kmLogo_Constant.attributes={kmLogo_Constant_value}

# kmLogo_ProcCall class attributes and methods

# kmLogo_ProcDeclaration class attributes and methods
kmLogo_ProcDeclaration_name: Property = Property(name="name", type=StringType)
kmLogo_ProcDeclaration.attributes={kmLogo_ProcDeclaration_name}

# kmLogo_Parameter class attributes and methods
kmLogo_Parameter_name: Property = Property(name="name", type=StringType)
kmLogo_Parameter.attributes={kmLogo_Parameter_name}

# kmLogo_Forward class attributes and methods

# kmLogo_Left class attributes and methods

# kmLogo_Right class attributes and methods

# kmLogo_PenDown class attributes and methods

# kmLogo_PenUp class attributes and methods

# kmLogo_Clear class attributes and methods

# kmLogo_BinaryExp class attributes and methods

# Expression class attributes and methods

# kmLogo_Repeat class attributes and methods

# kmLogo_While class attributes and methods

# kmLogo_ParameterCall class attributes and methods

# kmLogo_Plus class attributes and methods

# BinaryExp class attributes and methods

# kmLogo_Minus class attributes and methods

# kmLogo_Mult class attributes and methods

# kmLogo_Div class attributes and methods

# kmLogo_Equals class attributes and methods

# kmLogo_Greater class attributes and methods

# kmLogo_Lower class attributes and methods

# kmLogo_Cos class attributes and methods

# UnaryExpression class attributes and methods

# kmLogo_Block class attributes and methods

# kmLogo_If class attributes and methods

# ControlStructure class attributes and methods

# kmLogo_ControlStructure class attributes and methods

# kmLogo_StackFrame class attributes and methods

# kmLogo_Variable class attributes and methods
kmLogo_Variable_name: Property = Property(name="name", type=StringType)
kmLogo_Variable_value: Property = Property(name="value", type=FloatType)
kmLogo_Variable.attributes={kmLogo_Variable_value, kmLogo_Variable_name}

# kmLogo_Sin class attributes and methods

# kmLogo_Tan class attributes and methods

# kmLogo_LogoProgram class attributes and methods

# kmLogo_Turtle class attributes and methods
kmLogo_Turtle_heading: Property = Property(name="heading", type=FloatType)
kmLogo_Turtle_penUp: Property = Property(name="penUp", type=BooleanType)
kmLogo_Turtle.attributes={kmLogo_Turtle_penUp, kmLogo_Turtle_heading}

# kmLogo_Point class attributes and methods
kmLogo_Point_x: Property = Property(name="x", type=FloatType)
kmLogo_Point_y: Property = Property(name="y", type=FloatType)
kmLogo_Point.attributes={kmLogo_Point_x, kmLogo_Point_y}

# kmLogo_Segment class attributes and methods

# kmLogo_CallStack class attributes and methods

# Relationships
lhs7: BinaryAssociation = BinaryAssociation(
    name="lhs7",
    ends={
        Property(name="kmLogo_Expression8", type=kmLogo_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_BinaryExp", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs9: BinaryAssociation = BinaryAssociation(
    name="rhs9",
    ends={
        Property(name="kmLogo_Expression11", type=kmLogo_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_BinaryExp10", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression12: BinaryAssociation = BinaryAssociation(
    name="expression12",
    ends={
        Property(name="kmLogo_Expression13", type=kmLogo_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_UnaryExpression", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualArgs14: BinaryAssociation = BinaryAssociation(
    name="actualArgs14",
    ends={
        Property(name="kmLogo_Expression15", type=kmLogo_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ProcCall", type=kmLogo_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration16: BinaryAssociation = BinaryAssociation(
    name="declaration16",
    ends={
        Property(name="17", type=kmLogo_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
steps0: BinaryAssociation = BinaryAssociation(
    name="steps0",
    ends={
        Property(name="kmLogo_Expression", type=kmLogo_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Back", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
steps1: BinaryAssociation = BinaryAssociation(
    name="steps1",
    ends={
        Property(name="kmLogo_Expression2", type=kmLogo_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Forward", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle3: BinaryAssociation = BinaryAssociation(
    name="angle3",
    ends={
        Property(name="kmLogo_Expression4", type=kmLogo_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Left", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
angle5: BinaryAssociation = BinaryAssociation(
    name="angle5",
    ends={
        Property(name="kmLogo_Expression6", type=kmLogo_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Right", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block33: BinaryAssociation = BinaryAssociation(
    name="block33",
    ends={
        Property(name="kmLogo_Block34", type=kmLogo_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Repeat", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block35: BinaryAssociation = BinaryAssociation(
    name="block35",
    ends={
        Property(name="kmLogo_Block36", type=kmLogo_While, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_While", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter37: BinaryAssociation = BinaryAssociation(
    name="parameter37",
    ends={
        Property(name="kmLogo_Parameter38", type=kmLogo_ParameterCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ParameterCall", type=kmLogo_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
args18: BinaryAssociation = BinaryAssociation(
    name="args18",
    ends={
        Property(name="kmLogo_Parameter", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ProcDeclaration", type=kmLogo_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procCall19: BinaryAssociation = BinaryAssociation(
    name="procCall19",
    ends={
        Property(name="21", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="20", type=kmLogo_ProcCall, multiplicity=Multiplicity(0, 9999))
    }
)
instructions22: BinaryAssociation = BinaryAssociation(
    name="instructions22",
    ends={
        Property(name="kmLogo_Instruction", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ProcDeclaration23", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions24: BinaryAssociation = BinaryAssociation(
    name="instructions24",
    ends={
        Property(name="kmLogo_Instruction25", type=kmLogo_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Block", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenPart26: BinaryAssociation = BinaryAssociation(
    name="thenPart26",
    ends={
        Property(name="kmLogo_Block27", type=kmLogo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_If", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsePart28: BinaryAssociation = BinaryAssociation(
    name="elsePart28",
    ends={
        Property(name="kmLogo_Block30", type=kmLogo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_If29", type=kmLogo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition31: BinaryAssociation = BinaryAssociation(
    name="condition31",
    ends={
        Property(name="kmLogo_Expression32", type=kmLogo_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ControlStructure", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
begin46: BinaryAssociation = BinaryAssociation(
    name="begin46",
    ends={
        Property(name="kmLogo_Point48", type=kmLogo_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Segment47", type=kmLogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end49: BinaryAssociation = BinaryAssociation(
    name="end49",
    ends={
        Property(name="kmLogo_Point51", type=kmLogo_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Segment50", type=kmLogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
frames52: BinaryAssociation = BinaryAssociation(
    name="frames52",
    ends={
        Property(name="kmLogo_StackFrame", type=kmLogo_CallStack, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_CallStack53", type=kmLogo_StackFrame, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables54: BinaryAssociation = BinaryAssociation(
    name="variables54",
    ends={
        Property(name="kmLogo_Variable", type=kmLogo_StackFrame, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_StackFrame55", type=kmLogo_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions39: BinaryAssociation = BinaryAssociation(
    name="instructions39",
    ends={
        Property(name="kmLogo_Instruction40", type=kmLogo_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_LogoProgram", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position41: BinaryAssociation = BinaryAssociation(
    name="position41",
    ends={
        Property(name="kmLogo_Point", type=kmLogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Turtle", type=kmLogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
drawings42: BinaryAssociation = BinaryAssociation(
    name="drawings42",
    ends={
        Property(name="kmLogo_Segment", type=kmLogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Turtle43", type=kmLogo_Segment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callStack44: BinaryAssociation = BinaryAssociation(
    name="callStack44",
    ends={
        Property(name="kmLogo_CallStack", type=kmLogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Turtle45", type=kmLogo_CallStack, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_kmLogo_Primitive_Instruction = Generalization(general=Instruction, specific=kmLogo_Primitive)
gen_kmLogo_Back_Primitive = Generalization(general=Primitive, specific=kmLogo_Back)
gen_kmLogo_UnaryExpression_Expression = Generalization(general=Expression, specific=kmLogo_UnaryExpression)
gen_kmLogo_Constant_Expression = Generalization(general=Expression, specific=kmLogo_Constant)
gen_kmLogo_ProcCall_Expression = Generalization(general=Expression, specific=kmLogo_ProcCall)
gen_kmLogo_ProcDeclaration_Instruction = Generalization(general=Instruction, specific=kmLogo_ProcDeclaration)
gen_kmLogo_Forward_Primitive = Generalization(general=Primitive, specific=kmLogo_Forward)
gen_kmLogo_Left_Primitive = Generalization(general=Primitive, specific=kmLogo_Left)
gen_kmLogo_Right_Primitive = Generalization(general=Primitive, specific=kmLogo_Right)
gen_kmLogo_PenDown_Primitive = Generalization(general=Primitive, specific=kmLogo_PenDown)
gen_kmLogo_PenUp_Primitive = Generalization(general=Primitive, specific=kmLogo_PenUp)
gen_kmLogo_Clear_Primitive = Generalization(general=Primitive, specific=kmLogo_Clear)
gen_kmLogo_Expression_Instruction = Generalization(general=Instruction, specific=kmLogo_Expression)
gen_kmLogo_BinaryExp_Expression = Generalization(general=Expression, specific=kmLogo_BinaryExp)
gen_kmLogo_Repeat_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_Repeat)
gen_kmLogo_While_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_While)
gen_kmLogo_ParameterCall_Expression = Generalization(general=Expression, specific=kmLogo_ParameterCall)
gen_kmLogo_Plus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Plus)
gen_kmLogo_Minus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Minus)
gen_kmLogo_Mult_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Mult)
gen_kmLogo_Div_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Div)
gen_kmLogo_Equals_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Equals)
gen_kmLogo_Greater_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Greater)
gen_kmLogo_Lower_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Lower)
gen_kmLogo_Cos_UnaryExpression = Generalization(general=UnaryExpression, specific=kmLogo_Cos)
gen_kmLogo_Block_Instruction = Generalization(general=Instruction, specific=kmLogo_Block)
gen_kmLogo_If_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_If)
gen_kmLogo_ControlStructure_Instruction = Generalization(general=Instruction, specific=kmLogo_ControlStructure)
gen_kmLogo_Sin_UnaryExpression = Generalization(general=UnaryExpression, specific=kmLogo_Sin)
gen_kmLogo_Tan_UnaryExpression = Generalization(general=UnaryExpression, specific=kmLogo_Tan)

# Domain Model
domain_model = DomainModel(
    name="kmLogo",
    types={kmLogo_Instruction, kmLogo_Primitive, Instruction, kmLogo_Back, Primitive, kmLogo_Expression, kmLogo_UnaryExpression, kmLogo_Constant, kmLogo_ProcCall, kmLogo_ProcDeclaration, kmLogo_Parameter, kmLogo_Forward, kmLogo_Left, kmLogo_Right, kmLogo_PenDown, kmLogo_PenUp, kmLogo_Clear, kmLogo_BinaryExp, Expression, kmLogo_Repeat, kmLogo_While, kmLogo_ParameterCall, kmLogo_Plus, BinaryExp, kmLogo_Minus, kmLogo_Mult, kmLogo_Div, kmLogo_Equals, kmLogo_Greater, kmLogo_Lower, kmLogo_Cos, UnaryExpression, kmLogo_Block, kmLogo_If, ControlStructure, kmLogo_ControlStructure, kmLogo_StackFrame, kmLogo_Variable, kmLogo_Sin, kmLogo_Tan, kmLogo_LogoProgram, kmLogo_Turtle, kmLogo_Point, kmLogo_Segment, kmLogo_CallStack},
    associations={lhs7, rhs9, expression12, actualArgs14, declaration16, steps0, steps1, angle3, angle5, block33, block35, parameter37, args18, procCall19, instructions22, instructions24, thenPart26, elsePart28, condition31, begin46, end49, frames52, variables54, instructions39, position41, drawings42, callStack44},
    generalizations={gen_kmLogo_Primitive_Instruction, gen_kmLogo_Back_Primitive, gen_kmLogo_UnaryExpression_Expression, gen_kmLogo_Constant_Expression, gen_kmLogo_ProcCall_Expression, gen_kmLogo_ProcDeclaration_Instruction, gen_kmLogo_Forward_Primitive, gen_kmLogo_Left_Primitive, gen_kmLogo_Right_Primitive, gen_kmLogo_PenDown_Primitive, gen_kmLogo_PenUp_Primitive, gen_kmLogo_Clear_Primitive, gen_kmLogo_Expression_Instruction, gen_kmLogo_BinaryExp_Expression, gen_kmLogo_Repeat_ControlStructure, gen_kmLogo_While_ControlStructure, gen_kmLogo_ParameterCall_Expression, gen_kmLogo_Plus_BinaryExp, gen_kmLogo_Minus_BinaryExp, gen_kmLogo_Mult_BinaryExp, gen_kmLogo_Div_BinaryExp, gen_kmLogo_Equals_BinaryExp, gen_kmLogo_Greater_BinaryExp, gen_kmLogo_Lower_BinaryExp, gen_kmLogo_Cos_UnaryExpression, gen_kmLogo_Block_Instruction, gen_kmLogo_If_ControlStructure, gen_kmLogo_ControlStructure_Instruction, gen_kmLogo_Sin_UnaryExpression, gen_kmLogo_Tan_UnaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)