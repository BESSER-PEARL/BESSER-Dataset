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
klangexpr_WhileLoop = Class(name="klangexpr::WhileLoop")
Statement = Class(name="Statement")
klangexpr_Expression = Class(name="klangexpr::Expression")
klangexpr_Statement = Class(name="klangexpr::Statement")
klangexpr_FunctionCall = Class(name="klangexpr::FunctionCall")
klangexpr_ForeverLoop = Class(name="klangexpr::ForeverLoop")
klangexpr_Yield = Class(name="klangexpr::Yield")
klangexpr_VariableAssignment = Class(name="klangexpr::VariableAssignment")
klangexpr_Or = Class(name="klangexpr::Or")
BinaryOperator = Class(name="BinaryOperator")
klangexpr_And = Class(name="klangexpr::And")
klangexpr_Plus = Class(name="klangexpr::Plus")
klangexpr_Minus = Class(name="klangexpr::Minus")
klangexpr_Multiply = Class(name="klangexpr::Multiply")
klangexpr_Divide = Class(name="klangexpr::Divide")
klangexpr_LessThan = Class(name="klangexpr::LessThan")
klangexpr_Equal = Class(name="klangexpr::Equal")
klangexpr_GreaterThan = Class(name="klangexpr::GreaterThan")
klangexpr_Not = Class(name="klangexpr::Not")
UnaryOperator = Class(name="UnaryOperator")
klangexpr_BooleanLiteral = Class(name="klangexpr::BooleanLiteral")
Expression = Class(name="Expression")
klangexpr_DoubleLiteral = Class(name="klangexpr::DoubleLiteral")
klangexpr_StringLiteral = Class(name="klangexpr::StringLiteral")
klangexpr_VariableReference = Class(name="klangexpr::VariableReference")
klangexpr_UnaryOperator = Class(name="klangexpr::UnaryOperator")
Operator = Class(name="Operator")
klangexpr_If = Class(name="klangexpr::If")
klangexpr_BinaryOperator = Class(name="klangexpr::BinaryOperator")
klangexpr_IntegerLiteral = Class(name="klangexpr::IntegerLiteral")
klangexpr_UnaryMinus = Class(name="klangexpr::UnaryMinus")
klangexpr_ToDouble = Class(name="klangexpr::ToDouble")
klangexpr_ToInt = Class(name="klangexpr::ToInt")
klangexpr_Operator = Class(name="klangexpr::Operator", is_abstract=True)
klangexpr_Sleep = Class(name="klangexpr::Sleep")
klangexpr_SendMessage = Class(name="klangexpr::SendMessage")
klangexpr_LessThanOrEqual = Class(name="klangexpr::LessThanOrEqual")
klangexpr_GreaterThanOrEqual = Class(name="klangexpr::GreaterThanOrEqual")

# klangexpr_WhileLoop class attributes and methods

# Statement class attributes and methods

# klangexpr_Expression class attributes and methods

# klangexpr_Statement class attributes and methods

# klangexpr_FunctionCall class attributes and methods
klangexpr_FunctionCall_name: Property = Property(name="name", type=StringType)
klangexpr_FunctionCall.attributes={klangexpr_FunctionCall_name}

# klangexpr_ForeverLoop class attributes and methods

# klangexpr_Yield class attributes and methods

# klangexpr_VariableAssignment class attributes and methods
klangexpr_VariableAssignment_variableName: Property = Property(name="variableName", type=StringType)
klangexpr_VariableAssignment.attributes={klangexpr_VariableAssignment_variableName}

# klangexpr_Or class attributes and methods

# BinaryOperator class attributes and methods

# klangexpr_And class attributes and methods

# klangexpr_Plus class attributes and methods

# klangexpr_Minus class attributes and methods

# klangexpr_Multiply class attributes and methods

# klangexpr_Divide class attributes and methods

# klangexpr_LessThan class attributes and methods

# klangexpr_Equal class attributes and methods

# klangexpr_GreaterThan class attributes and methods

# klangexpr_Not class attributes and methods

# UnaryOperator class attributes and methods

# klangexpr_BooleanLiteral class attributes and methods
klangexpr_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
klangexpr_BooleanLiteral.attributes={klangexpr_BooleanLiteral_value}

# Expression class attributes and methods

# klangexpr_DoubleLiteral class attributes and methods
klangexpr_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
klangexpr_DoubleLiteral.attributes={klangexpr_DoubleLiteral_value}

# klangexpr_StringLiteral class attributes and methods
klangexpr_StringLiteral_value: Property = Property(name="value", type=StringType)
klangexpr_StringLiteral.attributes={klangexpr_StringLiteral_value}

# klangexpr_VariableReference class attributes and methods
klangexpr_VariableReference_variableName: Property = Property(name="variableName", type=StringType)
klangexpr_VariableReference.attributes={klangexpr_VariableReference_variableName}

# klangexpr_UnaryOperator class attributes and methods

# Operator class attributes and methods

# klangexpr_If class attributes and methods

# klangexpr_BinaryOperator class attributes and methods

# klangexpr_IntegerLiteral class attributes and methods
klangexpr_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
klangexpr_IntegerLiteral.attributes={klangexpr_IntegerLiteral_value}

# klangexpr_UnaryMinus class attributes and methods

# klangexpr_ToDouble class attributes and methods

# klangexpr_ToInt class attributes and methods

# klangexpr_Operator class attributes and methods

# klangexpr_Sleep class attributes and methods

# klangexpr_SendMessage class attributes and methods
klangexpr_SendMessage_name: Property = Property(name="name", type=StringType)
klangexpr_SendMessage.attributes={klangexpr_SendMessage_name}

# klangexpr_LessThanOrEqual class attributes and methods

# klangexpr_GreaterThanOrEqual class attributes and methods

# Relationships
predicate0: BinaryAssociation = BinaryAssociation(
    name="predicate0",
    ends={
        Property(name="klangexpr_Expression", type=klangexpr_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_WhileLoop", type=klangexpr_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements1: BinaryAssociation = BinaryAssociation(
    name="statements1",
    ends={
        Property(name="klangexpr_Statement", type=klangexpr_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_WhileLoop2", type=klangexpr_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements11: BinaryAssociation = BinaryAssociation(
    name="statements11",
    ends={
        Property(name="klangexpr_Statement12", type=klangexpr_ForeverLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_ForeverLoop", type=klangexpr_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression13: BinaryAssociation = BinaryAssociation(
    name="expression13",
    ends={
        Property(name="klangexpr_Expression14", type=klangexpr_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_VariableAssignment", type=klangexpr_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression15: BinaryAssociation = BinaryAssociation(
    name="expression15",
    ends={
        Property(name="klangexpr_Expression16", type=klangexpr_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_UnaryOperator", type=klangexpr_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predicate3: BinaryAssociation = BinaryAssociation(
    name="predicate3",
    ends={
        Property(name="klangexpr_Expression4", type=klangexpr_If, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_If", type=klangexpr_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifBlock5: BinaryAssociation = BinaryAssociation(
    name="ifBlock5",
    ends={
        Property(name="klangexpr_Statement7", type=klangexpr_If, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_If6", type=klangexpr_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left17: BinaryAssociation = BinaryAssociation(
    name="left17",
    ends={
        Property(name="klangexpr_Expression18", type=klangexpr_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_BinaryOperator", type=klangexpr_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right19: BinaryAssociation = BinaryAssociation(
    name="right19",
    ends={
        Property(name="klangexpr_Expression21", type=klangexpr_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_BinaryOperator20", type=klangexpr_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock8: BinaryAssociation = BinaryAssociation(
    name="elseBlock8",
    ends={
        Property(name="klangexpr_Statement10", type=klangexpr_If, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_If9", type=klangexpr_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters22: BinaryAssociation = BinaryAssociation(
    name="parameters22",
    ends={
        Property(name="klangexpr_Expression23", type=klangexpr_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_FunctionCall", type=klangexpr_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duration24: BinaryAssociation = BinaryAssociation(
    name="duration24",
    ends={
        Property(name="klangexpr_Expression25", type=klangexpr_Sleep, multiplicity=Multiplicity(1, 1)),
        Property(name="klangexpr_Sleep", type=klangexpr_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_klangexpr_WhileLoop_Statement = Generalization(general=Statement, specific=klangexpr_WhileLoop)
gen_klangexpr_FunctionCall_Expression = Generalization(general=Expression, specific=klangexpr_FunctionCall)
gen_klangexpr_FunctionCall_Statement = Generalization(general=Statement, specific=klangexpr_FunctionCall)
gen_klangexpr_ForeverLoop_Statement = Generalization(general=Statement, specific=klangexpr_ForeverLoop)
gen_klangexpr_Yield_Statement = Generalization(general=Statement, specific=klangexpr_Yield)
gen_klangexpr_VariableAssignment_Statement = Generalization(general=Statement, specific=klangexpr_VariableAssignment)
gen_klangexpr_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_Or)
gen_klangexpr_And_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_And)
gen_klangexpr_Plus_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_Plus)
gen_klangexpr_Minus_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_Minus)
gen_klangexpr_Multiply_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_Multiply)
gen_klangexpr_Divide_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_Divide)
gen_klangexpr_LessThan_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_LessThan)
gen_klangexpr_Equal_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_Equal)
gen_klangexpr_GreaterThan_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_GreaterThan)
gen_klangexpr_Not_UnaryOperator = Generalization(general=UnaryOperator, specific=klangexpr_Not)
gen_klangexpr_BooleanLiteral_Expression = Generalization(general=Expression, specific=klangexpr_BooleanLiteral)
gen_klangexpr_DoubleLiteral_Expression = Generalization(general=Expression, specific=klangexpr_DoubleLiteral)
gen_klangexpr_StringLiteral_Expression = Generalization(general=Expression, specific=klangexpr_StringLiteral)
gen_klangexpr_VariableReference_Expression = Generalization(general=Expression, specific=klangexpr_VariableReference)
gen_klangexpr_UnaryOperator_Operator = Generalization(general=Operator, specific=klangexpr_UnaryOperator)
gen_klangexpr_If_Statement = Generalization(general=Statement, specific=klangexpr_If)
gen_klangexpr_BinaryOperator_Operator = Generalization(general=Operator, specific=klangexpr_BinaryOperator)
gen_klangexpr_IntegerLiteral_Expression = Generalization(general=Expression, specific=klangexpr_IntegerLiteral)
gen_klangexpr_UnaryMinus_UnaryOperator = Generalization(general=UnaryOperator, specific=klangexpr_UnaryMinus)
gen_klangexpr_ToDouble_UnaryOperator = Generalization(general=UnaryOperator, specific=klangexpr_ToDouble)
gen_klangexpr_ToInt_UnaryOperator = Generalization(general=UnaryOperator, specific=klangexpr_ToInt)
gen_klangexpr_Operator_Expression = Generalization(general=Expression, specific=klangexpr_Operator)
gen_klangexpr_Sleep_Statement = Generalization(general=Statement, specific=klangexpr_Sleep)
gen_klangexpr_SendMessage_Statement = Generalization(general=Statement, specific=klangexpr_SendMessage)
gen_klangexpr_LessThanOrEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_LessThanOrEqual)
gen_klangexpr_GreaterThanOrEqual_BinaryOperator = Generalization(general=BinaryOperator, specific=klangexpr_GreaterThanOrEqual)

# Domain Model
domain_model = DomainModel(
    name="klangexpr",
    types={klangexpr_WhileLoop, Statement, klangexpr_Expression, klangexpr_Statement, klangexpr_FunctionCall, klangexpr_ForeverLoop, klangexpr_Yield, klangexpr_VariableAssignment, klangexpr_Or, BinaryOperator, klangexpr_And, klangexpr_Plus, klangexpr_Minus, klangexpr_Multiply, klangexpr_Divide, klangexpr_LessThan, klangexpr_Equal, klangexpr_GreaterThan, klangexpr_Not, UnaryOperator, klangexpr_BooleanLiteral, Expression, klangexpr_DoubleLiteral, klangexpr_StringLiteral, klangexpr_VariableReference, klangexpr_UnaryOperator, Operator, klangexpr_If, klangexpr_BinaryOperator, klangexpr_IntegerLiteral, klangexpr_UnaryMinus, klangexpr_ToDouble, klangexpr_ToInt, klangexpr_Operator, klangexpr_Sleep, klangexpr_SendMessage, klangexpr_LessThanOrEqual, klangexpr_GreaterThanOrEqual},
    associations={predicate0, statements1, statements11, expression13, expression15, predicate3, ifBlock5, left17, right19, elseBlock8, parameters22, duration24},
    generalizations={gen_klangexpr_WhileLoop_Statement, gen_klangexpr_FunctionCall_Expression, gen_klangexpr_FunctionCall_Statement, gen_klangexpr_ForeverLoop_Statement, gen_klangexpr_Yield_Statement, gen_klangexpr_VariableAssignment_Statement, gen_klangexpr_Or_BinaryOperator, gen_klangexpr_And_BinaryOperator, gen_klangexpr_Plus_BinaryOperator, gen_klangexpr_Minus_BinaryOperator, gen_klangexpr_Multiply_BinaryOperator, gen_klangexpr_Divide_BinaryOperator, gen_klangexpr_LessThan_BinaryOperator, gen_klangexpr_Equal_BinaryOperator, gen_klangexpr_GreaterThan_BinaryOperator, gen_klangexpr_Not_UnaryOperator, gen_klangexpr_BooleanLiteral_Expression, gen_klangexpr_DoubleLiteral_Expression, gen_klangexpr_StringLiteral_Expression, gen_klangexpr_VariableReference_Expression, gen_klangexpr_UnaryOperator_Operator, gen_klangexpr_If_Statement, gen_klangexpr_BinaryOperator_Operator, gen_klangexpr_IntegerLiteral_Expression, gen_klangexpr_UnaryMinus_UnaryOperator, gen_klangexpr_ToDouble_UnaryOperator, gen_klangexpr_ToInt_UnaryOperator, gen_klangexpr_Operator_Expression, gen_klangexpr_Sleep_Statement, gen_klangexpr_SendMessage_Statement, gen_klangexpr_LessThanOrEqual_BinaryOperator, gen_klangexpr_GreaterThanOrEqual_BinaryOperator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)