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
kmLogo_UnaryExpression = Class(name="kmLogo::UnaryExpression", is_abstract=True)
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
kmLogo_Sin = Class(name="kmLogo::Sin")
kmLogo_Tan = Class(name="kmLogo::Tan")
kmLogo_LogoProgram = Class(name="kmLogo::LogoProgram")
kmLogo_Turtle = Class(name="kmLogo::Turtle")
kmLogo_Point = Class(name="kmLogo::Point")
kmLogo_Block = Class(name="kmLogo::Block")
kmLogo_If = Class(name="kmLogo::If")
ControlStructure = Class(name="ControlStructure")
kmLogo_ControlStructure = Class(name="kmLogo::ControlStructure")
kmLogo_Repeat = Class(name="kmLogo::Repeat")
kmLogo_While = Class(name="kmLogo::While")
kmLogo_Segment = Class(name="kmLogo::Segment")
kmLogo_CallStack = Class(name="kmLogo::CallStack")
kmLogo_StackFrame = Class(name="kmLogo::StackFrame")
kmLogo_Variable = Class(name="kmLogo::Variable")

# kmLogo_Instruction class attributes and methods

# kmLogo_Primitive class attributes and methods

# Instruction class attributes and methods

# kmLogo_Back class attributes and methods

# Primitive class attributes and methods

# kmLogo_Expression class attributes and methods

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

# kmLogo_UnaryExpression class attributes and methods

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
kmLogo_Point.attributes={kmLogo_Point_y, kmLogo_Point_x}

# kmLogo_Block class attributes and methods

# kmLogo_If class attributes and methods

# ControlStructure class attributes and methods

# kmLogo_ControlStructure class attributes and methods

# kmLogo_Repeat class attributes and methods

# kmLogo_While class attributes and methods

# kmLogo_Segment class attributes and methods

# kmLogo_CallStack class attributes and methods

# kmLogo_StackFrame class attributes and methods

# kmLogo_Variable class attributes and methods
kmLogo_Variable_value: Property = Property(name="value", type=FloatType)
kmLogo_Variable_name: Property = Property(name="name", type=StringType)
kmLogo_Variable.attributes={kmLogo_Variable_value, kmLogo_Variable_name}

# Relationships
steps0: BinaryAssociation = BinaryAssociation(
    name="steps0",
    ends={
        Property(name="kmLogo_Expression", type=kmLogo_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Back", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
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
        Property(name="ProcDeclaration", type=kmLogo_ProcCall, multiplicity=Multiplicity(1, 1)),
        Property(name="procCall", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
args17: BinaryAssociation = BinaryAssociation(
    name="args17",
    ends={
        Property(name="kmLogo_Parameter", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ProcDeclaration", type=kmLogo_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procCall18: BinaryAssociation = BinaryAssociation(
    name="procCall18",
    ends={
        Property(name="ProcCall", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaration", type=kmLogo_ProcCall, multiplicity=Multiplicity(0, 9999))
    }
)
instructions19: BinaryAssociation = BinaryAssociation(
    name="instructions19",
    ends={
        Property(name="kmLogo_Instruction", type=kmLogo_ProcDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ProcDeclaration20", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
parameter34: BinaryAssociation = BinaryAssociation(
    name="parameter34",
    ends={
        Property(name="kmLogo_Parameter35", type=kmLogo_ParameterCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ParameterCall", type=kmLogo_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
instructions36: BinaryAssociation = BinaryAssociation(
    name="instructions36",
    ends={
        Property(name="kmLogo_Instruction37", type=kmLogo_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_LogoProgram", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions21: BinaryAssociation = BinaryAssociation(
    name="instructions21",
    ends={
        Property(name="kmLogo_Instruction22", type=kmLogo_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Block", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenPart23: BinaryAssociation = BinaryAssociation(
    name="thenPart23",
    ends={
        Property(name="kmLogo_Block24", type=kmLogo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_If", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elsePart25: BinaryAssociation = BinaryAssociation(
    name="elsePart25",
    ends={
        Property(name="kmLogo_Block27", type=kmLogo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_If26", type=kmLogo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition28: BinaryAssociation = BinaryAssociation(
    name="condition28",
    ends={
        Property(name="kmLogo_Expression29", type=kmLogo_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ControlStructure", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block30: BinaryAssociation = BinaryAssociation(
    name="block30",
    ends={
        Property(name="kmLogo_Block31", type=kmLogo_Repeat, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Repeat", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block32: BinaryAssociation = BinaryAssociation(
    name="block32",
    ends={
        Property(name="kmLogo_Block33", type=kmLogo_While, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_While", type=kmLogo_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
position38: BinaryAssociation = BinaryAssociation(
    name="position38",
    ends={
        Property(name="kmLogo_Point", type=kmLogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Turtle", type=kmLogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
drawings39: BinaryAssociation = BinaryAssociation(
    name="drawings39",
    ends={
        Property(name="kmLogo_Segment", type=kmLogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Turtle40", type=kmLogo_Segment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callStack41: BinaryAssociation = BinaryAssociation(
    name="callStack41",
    ends={
        Property(name="kmLogo_CallStack", type=kmLogo_Turtle, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Turtle42", type=kmLogo_CallStack, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
begin43: BinaryAssociation = BinaryAssociation(
    name="begin43",
    ends={
        Property(name="kmLogo_Point45", type=kmLogo_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Segment44", type=kmLogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end46: BinaryAssociation = BinaryAssociation(
    name="end46",
    ends={
        Property(name="kmLogo_Point48", type=kmLogo_Segment, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Segment47", type=kmLogo_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
frames49: BinaryAssociation = BinaryAssociation(
    name="frames49",
    ends={
        Property(name="kmLogo_StackFrame", type=kmLogo_CallStack, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_CallStack50", type=kmLogo_StackFrame, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables51: BinaryAssociation = BinaryAssociation(
    name="variables51",
    ends={
        Property(name="kmLogo_Variable", type=kmLogo_StackFrame, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_StackFrame52", type=kmLogo_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_kmLogo_Primitive_Instruction = Generalization(general=Instruction, specific=kmLogo_Primitive)
gen_kmLogo_Back_Primitive = Generalization(general=Primitive, specific=kmLogo_Back)
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
gen_kmLogo_UnaryExpression_Expression = Generalization(general=Expression, specific=kmLogo_UnaryExpression)
gen_kmLogo_ParameterCall_Expression = Generalization(general=Expression, specific=kmLogo_ParameterCall)
gen_kmLogo_Plus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Plus)
gen_kmLogo_Minus_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Minus)
gen_kmLogo_Mult_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Mult)
gen_kmLogo_Div_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Div)
gen_kmLogo_Equals_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Equals)
gen_kmLogo_Greater_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Greater)
gen_kmLogo_Lower_BinaryExp = Generalization(general=BinaryExp, specific=kmLogo_Lower)
gen_kmLogo_Cos_UnaryExpression = Generalization(general=UnaryExpression, specific=kmLogo_Cos)
gen_kmLogo_Sin_UnaryExpression = Generalization(general=UnaryExpression, specific=kmLogo_Sin)
gen_kmLogo_Tan_UnaryExpression = Generalization(general=UnaryExpression, specific=kmLogo_Tan)
gen_kmLogo_Block_Instruction = Generalization(general=Instruction, specific=kmLogo_Block)
gen_kmLogo_If_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_If)
gen_kmLogo_ControlStructure_Instruction = Generalization(general=Instruction, specific=kmLogo_ControlStructure)
gen_kmLogo_Repeat_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_Repeat)
gen_kmLogo_While_ControlStructure = Generalization(general=ControlStructure, specific=kmLogo_While)

# Domain Model
domain_model = DomainModel(
    name="kmLogo",
    types={kmLogo_Instruction, kmLogo_Primitive, Instruction, kmLogo_Back, Primitive, kmLogo_Expression, kmLogo_Constant, kmLogo_ProcCall, kmLogo_ProcDeclaration, kmLogo_Parameter, kmLogo_Forward, kmLogo_Left, kmLogo_Right, kmLogo_PenDown, kmLogo_PenUp, kmLogo_Clear, kmLogo_BinaryExp, Expression, kmLogo_UnaryExpression, kmLogo_ParameterCall, kmLogo_Plus, BinaryExp, kmLogo_Minus, kmLogo_Mult, kmLogo_Div, kmLogo_Equals, kmLogo_Greater, kmLogo_Lower, kmLogo_Cos, UnaryExpression, kmLogo_Sin, kmLogo_Tan, kmLogo_LogoProgram, kmLogo_Turtle, kmLogo_Point, kmLogo_Block, kmLogo_If, ControlStructure, kmLogo_ControlStructure, kmLogo_Repeat, kmLogo_While, kmLogo_Segment, kmLogo_CallStack, kmLogo_StackFrame, kmLogo_Variable},
    associations={steps0, expression12, actualArgs14, declaration16, args17, procCall18, instructions19, steps1, angle3, angle5, lhs7, rhs9, parameter34, instructions36, instructions21, thenPart23, elsePart25, condition28, block30, block32, position38, drawings39, callStack41, begin43, end46, frames49, variables51},
    generalizations={gen_kmLogo_Primitive_Instruction, gen_kmLogo_Back_Primitive, gen_kmLogo_Constant_Expression, gen_kmLogo_ProcCall_Expression, gen_kmLogo_ProcDeclaration_Instruction, gen_kmLogo_Forward_Primitive, gen_kmLogo_Left_Primitive, gen_kmLogo_Right_Primitive, gen_kmLogo_PenDown_Primitive, gen_kmLogo_PenUp_Primitive, gen_kmLogo_Clear_Primitive, gen_kmLogo_Expression_Instruction, gen_kmLogo_BinaryExp_Expression, gen_kmLogo_UnaryExpression_Expression, gen_kmLogo_ParameterCall_Expression, gen_kmLogo_Plus_BinaryExp, gen_kmLogo_Minus_BinaryExp, gen_kmLogo_Mult_BinaryExp, gen_kmLogo_Div_BinaryExp, gen_kmLogo_Equals_BinaryExp, gen_kmLogo_Greater_BinaryExp, gen_kmLogo_Lower_BinaryExp, gen_kmLogo_Cos_UnaryExpression, gen_kmLogo_Sin_UnaryExpression, gen_kmLogo_Tan_UnaryExpression, gen_kmLogo_Block_Instruction, gen_kmLogo_If_ControlStructure, gen_kmLogo_ControlStructure_Instruction, gen_kmLogo_Repeat_ControlStructure, gen_kmLogo_While_ControlStructure},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)