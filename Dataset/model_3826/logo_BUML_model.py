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
logo_Statement = Class(name="logo::Statement", is_abstract=True)
logo_Expression = Class(name="logo::Expression", is_abstract=True)
logo_Parameter = Class(name="logo::Parameter")
logo_Symbol = Class(name="logo::Symbol", is_abstract=True)
logo_Logo = Class(name="logo::Logo")
logo_statement_PenDown = Class(name="logo::statement::PenDown")
logo_statement_PenUp = Class(name="logo::statement::PenUp")
logo_statement_ProcedureDefinition = Class(name="logo::statement::ProcedureDefinition")
statement_logo_Parameter = Class(name="statement::logo::Parameter")
logo_Value = Class(name="logo::Value", is_abstract=True)
logo_statement_Right = Class(name="logo::statement::Right")
Statement = Class(name="Statement")
statement_logo_Expression = Class(name="statement::logo::Expression")
logo_statement_Left = Class(name="logo::statement::Left")
logo_statement_Forward = Class(name="logo::statement::Forward")
logo_statement_Block = Class(name="logo::statement::Block")
logo_statement_ControlStatement = Class(name="logo::statement::ControlStatement", is_abstract=True)
logo_control_If = Class(name="logo::control::If")
ControlStatement = Class(name="ControlStatement")
statement_logo_Statement = Class(name="statement::logo::Statement")
logo_statement_ProcedureCall = Class(name="logo::statement::ProcedureCall")
ProcedureDefinition = Class(name="ProcedureDefinition")
logo_expression_BinaryExpression = Class(name="logo::expression::BinaryExpression", is_abstract=True)
Expression = Class(name="Expression")
expression_logo_Expression = Class(name="expression::logo::Expression")
logo_expression_UnaryExpression = Class(name="logo::expression::UnaryExpression", is_abstract=True)
Block = Class(name="Block")
logo_control_While = Class(name="logo::control::While")
logo_control_Repeat = Class(name="logo::control::Repeat")
logo_constant_IntValue = Class(name="logo::constant::IntValue")
Constant = Class(name="Constant")
logo_constant_BoolValue = Class(name="logo::constant::BoolValue")
logo_unary_Not = Class(name="logo::unary::Not")
UnaryExpression = Class(name="UnaryExpression")
logo_unary_Opposite = Class(name="logo::unary::Opposite")
logo_expression_Constant = Class(name="logo::expression::Constant", is_abstract=True)
logo_expression_ExtendedExpression = Class(name="logo::expression::ExtendedExpression", is_abstract=True)
logo_expression_VariableRead = Class(name="logo::expression::VariableRead")
logo_binary_Lower = Class(name="logo::binary::Lower")
logo_extended_And = Class(name="logo::extended::And")
ExtendedExpression = Class(name="ExtendedExpression")
logo_extended_Or = Class(name="logo::extended::Or")
logo_symbol_Variable = Class(name="logo::symbol::Variable")
Symbol = Class(name="Symbol")
logo_symbol_Procedure = Class(name="logo::symbol::Procedure")
logo_binary_Minus = Class(name="logo::binary::Minus")
BinaryExpression = Class(name="BinaryExpression")
logo_binary_Plus = Class(name="logo::binary::Plus")
logo_binary_Mult = Class(name="logo::binary::Mult")
logo_binary_Div = Class(name="logo::binary::Div")
logo_binary_Equals = Class(name="logo::binary::Equals")
logo_binary_Greater = Class(name="logo::binary::Greater")
logo_value_IntValue = Class(name="logo::value::IntValue")
Value = Class(name="Value")
logo_value_BoolValue = Class(name="logo::value::BoolValue")

# logo_Statement class attributes and methods

# logo_Expression class attributes and methods

# logo_Parameter class attributes and methods
logo_Parameter_name: Property = Property(name="name", type=StringType)
logo_Parameter.attributes={logo_Parameter_name}

# logo_Symbol class attributes and methods
logo_Symbol_name: Property = Property(name="name", type=StringType)
logo_Symbol.attributes={logo_Symbol_name}

# logo_Logo class attributes and methods

# logo_statement_PenDown class attributes and methods

# logo_statement_PenUp class attributes and methods

# logo_statement_ProcedureDefinition class attributes and methods
logo_statement_ProcedureDefinition_name: Property = Property(name="name", type=StringType)
logo_statement_ProcedureDefinition.attributes={logo_statement_ProcedureDefinition_name}

# statement_logo_Parameter class attributes and methods

# logo_Value class attributes and methods

# logo_statement_Right class attributes and methods

# Statement class attributes and methods

# statement_logo_Expression class attributes and methods

# logo_statement_Left class attributes and methods

# logo_statement_Forward class attributes and methods

# logo_statement_Block class attributes and methods

# logo_statement_ControlStatement class attributes and methods

# logo_control_If class attributes and methods

# ControlStatement class attributes and methods

# statement_logo_Statement class attributes and methods

# logo_statement_ProcedureCall class attributes and methods

# ProcedureDefinition class attributes and methods

# logo_expression_BinaryExpression class attributes and methods

# Expression class attributes and methods

# expression_logo_Expression class attributes and methods

# logo_expression_UnaryExpression class attributes and methods

# Block class attributes and methods

# logo_control_While class attributes and methods

# logo_control_Repeat class attributes and methods

# logo_constant_IntValue class attributes and methods
logo_constant_IntValue_value: Property = Property(name="value", type=IntegerType)
logo_constant_IntValue.attributes={logo_constant_IntValue_value}

# Constant class attributes and methods

# logo_constant_BoolValue class attributes and methods
logo_constant_BoolValue_value: Property = Property(name="value", type=BooleanType)
logo_constant_BoolValue.attributes={logo_constant_BoolValue_value}

# logo_unary_Not class attributes and methods

# UnaryExpression class attributes and methods

# logo_unary_Opposite class attributes and methods

# logo_expression_Constant class attributes and methods

# logo_expression_ExtendedExpression class attributes and methods

# logo_expression_VariableRead class attributes and methods
logo_expression_VariableRead_name: Property = Property(name="name", type=StringType)
logo_expression_VariableRead.attributes={logo_expression_VariableRead_name}

# logo_binary_Lower class attributes and methods

# logo_extended_And class attributes and methods

# ExtendedExpression class attributes and methods

# logo_extended_Or class attributes and methods

# logo_symbol_Variable class attributes and methods

# Symbol class attributes and methods

# logo_symbol_Procedure class attributes and methods

# logo_binary_Minus class attributes and methods

# BinaryExpression class attributes and methods

# logo_binary_Plus class attributes and methods

# logo_binary_Mult class attributes and methods

# logo_binary_Div class attributes and methods

# logo_binary_Equals class attributes and methods

# logo_binary_Greater class attributes and methods

# logo_value_IntValue class attributes and methods
logo_value_IntValue_value: Property = Property(name="value", type=IntegerType)
logo_value_IntValue.attributes={logo_value_IntValue_value}

# Value class attributes and methods

# logo_value_BoolValue class attributes and methods
logo_value_BoolValue_value: Property = Property(name="value", type=BooleanType)
logo_value_BoolValue.attributes={logo_value_BoolValue_value}

# Relationships
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="logo_Statement", type=logo_Logo, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_Logo", type=logo_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
step4: BinaryAssociation = BinaryAssociation(
    name="step4",
    ends={
        Property(name="statement_logo_Expression5", type=logo_statement_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_statement_Forward", type=statement_logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters6: BinaryAssociation = BinaryAssociation(
    name="parameters6",
    ends={
        Property(name="statement_logo_Parameter", type=logo_statement_ProcedureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_statement_ProcedureDefinition", type=statement_logo_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
angle1: BinaryAssociation = BinaryAssociation(
    name="angle1",
    ends={
        Property(name="statement_logo_Expression", type=logo_statement_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_statement_Right", type=statement_logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle2: BinaryAssociation = BinaryAssociation(
    name="angle2",
    ends={
        Property(name="statement_logo_Expression3", type=logo_statement_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_statement_Left", type=statement_logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements13: BinaryAssociation = BinaryAssociation(
    name="statements13",
    ends={
        Property(name="statement_logo_Statement14", type=logo_statement_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_statement_Block", type=statement_logo_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="statement_logo_Expression16", type=logo_statement_ControlStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_statement_ControlStatement", type=statement_logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements7: BinaryAssociation = BinaryAssociation(
    name="statements7",
    ends={
        Property(name="statement_logo_Statement", type=logo_statement_ProcedureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_statement_ProcedureDefinition8", type=statement_logo_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
parameterValues9: BinaryAssociation = BinaryAssociation(
    name="parameterValues9",
    ends={
        Property(name="statement_logo_Expression10", type=logo_statement_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_statement_ProcedureCall", type=statement_logo_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definition11: BinaryAssociation = BinaryAssociation(
    name="definition11",
    ends={
        Property(name="ProcedureDefinition", type=logo_statement_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_statement_ProcedureCall12", type=ProcedureDefinition, multiplicity=Multiplicity(1, 1))
    }
)
block23: BinaryAssociation = BinaryAssociation(
    name="block23",
    ends={
        Property(name="logo_control_Repeat", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Block24", type=logo_control_Repeat, multiplicity=Multiplicity(1, 1))
    }
)
leftExpression25: BinaryAssociation = BinaryAssociation(
    name="leftExpression25",
    ends={
        Property(name="expression_logo_Expression", type=logo_expression_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_expression_BinaryExpression", type=expression_logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExpression26: BinaryAssociation = BinaryAssociation(
    name="rightExpression26",
    ends={
        Property(name="expression_logo_Expression28", type=logo_expression_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_expression_BinaryExpression27", type=expression_logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifBlock17: BinaryAssociation = BinaryAssociation(
    name="ifBlock17",
    ends={
        Property(name="Block", type=logo_control_If, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_control_If", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBlock18: BinaryAssociation = BinaryAssociation(
    name="elseBlock18",
    ends={
        Property(name="Block20", type=logo_control_If, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_control_If19", type=Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block21: BinaryAssociation = BinaryAssociation(
    name="block21",
    ends={
        Property(name="Block22", type=logo_control_While, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_control_While", type=Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression29: BinaryAssociation = BinaryAssociation(
    name="expression29",
    ends={
        Property(name="expression_logo_Expression30", type=logo_expression_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_expression_UnaryExpression", type=expression_logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions31: BinaryAssociation = BinaryAssociation(
    name="expressions31",
    ends={
        Property(name="expression_logo_Expression32", type=logo_expression_ExtendedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="logo_expression_ExtendedExpression", type=expression_logo_Expression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)

# Generalizations
gen_logo_statement_PenDown_Statement = Generalization(general=Statement, specific=logo_statement_PenDown)
gen_logo_statement_PenUp_Statement = Generalization(general=Statement, specific=logo_statement_PenUp)
gen_logo_statement_ProcedureDefinition_Statement = Generalization(general=Statement, specific=logo_statement_ProcedureDefinition)
gen_logo_statement_Right_Statement = Generalization(general=Statement, specific=logo_statement_Right)
gen_logo_statement_Left_Statement = Generalization(general=Statement, specific=logo_statement_Left)
gen_logo_statement_Forward_Statement = Generalization(general=Statement, specific=logo_statement_Forward)
gen_logo_statement_Block_Statement = Generalization(general=Statement, specific=logo_statement_Block)
gen_logo_statement_ControlStatement_Statement = Generalization(general=Statement, specific=logo_statement_ControlStatement)
gen_logo_control_If_ControlStatement = Generalization(general=ControlStatement, specific=logo_control_If)
gen_logo_statement_ProcedureCall_Statement = Generalization(general=Statement, specific=logo_statement_ProcedureCall)
gen_logo_expression_BinaryExpression_Expression = Generalization(general=Expression, specific=logo_expression_BinaryExpression)
gen_logo_control_While_ControlStatement = Generalization(general=ControlStatement, specific=logo_control_While)
gen_logo_control_Repeat_ControlStatement = Generalization(general=ControlStatement, specific=logo_control_Repeat)
gen_logo_constant_IntValue_Constant = Generalization(general=Constant, specific=logo_constant_IntValue)
gen_logo_constant_BoolValue_Constant = Generalization(general=Constant, specific=logo_constant_BoolValue)
gen_logo_unary_Not_UnaryExpression = Generalization(general=UnaryExpression, specific=logo_unary_Not)
gen_logo_unary_Opposite_UnaryExpression = Generalization(general=UnaryExpression, specific=logo_unary_Opposite)
gen_logo_expression_UnaryExpression_Expression = Generalization(general=Expression, specific=logo_expression_UnaryExpression)
gen_logo_expression_Constant_Expression = Generalization(general=Expression, specific=logo_expression_Constant)
gen_logo_expression_ExtendedExpression_Expression = Generalization(general=Expression, specific=logo_expression_ExtendedExpression)
gen_logo_expression_VariableRead_Expression = Generalization(general=Expression, specific=logo_expression_VariableRead)
gen_logo_binary_Lower_BinaryExpression = Generalization(general=BinaryExpression, specific=logo_binary_Lower)
gen_logo_extended_And_ExtendedExpression = Generalization(general=ExtendedExpression, specific=logo_extended_And)
gen_logo_extended_Or_ExtendedExpression = Generalization(general=ExtendedExpression, specific=logo_extended_Or)
gen_logo_symbol_Variable_Symbol = Generalization(general=Symbol, specific=logo_symbol_Variable)
gen_logo_symbol_Procedure_Symbol = Generalization(general=Symbol, specific=logo_symbol_Procedure)
gen_logo_binary_Minus_BinaryExpression = Generalization(general=BinaryExpression, specific=logo_binary_Minus)
gen_logo_binary_Plus_BinaryExpression = Generalization(general=BinaryExpression, specific=logo_binary_Plus)
gen_logo_binary_Mult_BinaryExpression = Generalization(general=BinaryExpression, specific=logo_binary_Mult)
gen_logo_binary_Div_BinaryExpression = Generalization(general=BinaryExpression, specific=logo_binary_Div)
gen_logo_binary_Equals_BinaryExpression = Generalization(general=BinaryExpression, specific=logo_binary_Equals)
gen_logo_binary_Greater_BinaryExpression = Generalization(general=BinaryExpression, specific=logo_binary_Greater)
gen_logo_value_IntValue_Value = Generalization(general=Value, specific=logo_value_IntValue)
gen_logo_value_BoolValue_Value = Generalization(general=Value, specific=logo_value_BoolValue)

# Domain Model
domain_model = DomainModel(
    name="logo",
    types={logo_Statement, logo_Expression, logo_Parameter, logo_Symbol, logo_Logo, logo_statement_PenDown, logo_statement_PenUp, logo_statement_ProcedureDefinition, statement_logo_Parameter, logo_Value, logo_statement_Right, Statement, statement_logo_Expression, logo_statement_Left, logo_statement_Forward, logo_statement_Block, logo_statement_ControlStatement, logo_control_If, ControlStatement, statement_logo_Statement, logo_statement_ProcedureCall, ProcedureDefinition, logo_expression_BinaryExpression, Expression, expression_logo_Expression, logo_expression_UnaryExpression, Block, logo_control_While, logo_control_Repeat, logo_constant_IntValue, Constant, logo_constant_BoolValue, logo_unary_Not, UnaryExpression, logo_unary_Opposite, logo_expression_Constant, logo_expression_ExtendedExpression, logo_expression_VariableRead, logo_binary_Lower, logo_extended_And, ExtendedExpression, logo_extended_Or, logo_symbol_Variable, Symbol, logo_symbol_Procedure, logo_binary_Minus, BinaryExpression, logo_binary_Plus, logo_binary_Mult, logo_binary_Div, logo_binary_Equals, logo_binary_Greater, logo_value_IntValue, Value, logo_value_BoolValue},
    associations={statements0, step4, parameters6, angle1, angle2, statements13, condition15, statements7, parameterValues9, definition11, block23, leftExpression25, rightExpression26, ifBlock17, elseBlock18, block21, expression29, expressions31},
    generalizations={gen_logo_statement_PenDown_Statement, gen_logo_statement_PenUp_Statement, gen_logo_statement_ProcedureDefinition_Statement, gen_logo_statement_Right_Statement, gen_logo_statement_Left_Statement, gen_logo_statement_Forward_Statement, gen_logo_statement_Block_Statement, gen_logo_statement_ControlStatement_Statement, gen_logo_control_If_ControlStatement, gen_logo_statement_ProcedureCall_Statement, gen_logo_expression_BinaryExpression_Expression, gen_logo_control_While_ControlStatement, gen_logo_control_Repeat_ControlStatement, gen_logo_constant_IntValue_Constant, gen_logo_constant_BoolValue_Constant, gen_logo_unary_Not_UnaryExpression, gen_logo_unary_Opposite_UnaryExpression, gen_logo_expression_UnaryExpression_Expression, gen_logo_expression_Constant_Expression, gen_logo_expression_ExtendedExpression_Expression, gen_logo_expression_VariableRead_Expression, gen_logo_binary_Lower_BinaryExpression, gen_logo_extended_And_ExtendedExpression, gen_logo_extended_Or_ExtendedExpression, gen_logo_symbol_Variable_Symbol, gen_logo_symbol_Procedure_Symbol, gen_logo_binary_Minus_BinaryExpression, gen_logo_binary_Plus_BinaryExpression, gen_logo_binary_Mult_BinaryExpression, gen_logo_binary_Div_BinaryExpression, gen_logo_binary_Equals_BinaryExpression, gen_logo_binary_Greater_BinaryExpression, gen_logo_value_IntValue_Value, gen_logo_value_BoolValue_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)