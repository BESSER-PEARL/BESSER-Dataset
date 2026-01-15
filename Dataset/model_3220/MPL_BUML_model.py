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
ComparisonOperator: Enumeration = Enumeration(
    name="ComparisonOperator",
    literals={
            EnumerationLiteral(name="EQUAL"),
			EnumerationLiteral(name="INEQUAL"),
			EnumerationLiteral(name="LESS_THAN"),
			EnumerationLiteral(name="LESS_THAN_EQUAL"),
			EnumerationLiteral(name="GREATER_THAN"),
			EnumerationLiteral(name="GREATER_THAN_EQUAL")
    }
)

ForLoopDirection: Enumeration = Enumeration(
    name="ForLoopDirection",
    literals={
            EnumerationLiteral(name="UP"),
			EnumerationLiteral(name="DOWN")
    }
)

# Classes
mpl_Operation = Class(name="mpl::Operation", is_abstract=True)
mpl_FunctionalUnit = Class(name="mpl::FunctionalUnit", is_abstract=True)
mpl_MPLModel = Class(name="mpl::MPLModel")
mpl_Program = Class(name="mpl::Program")
mpl_Procedure = Class(name="mpl::Procedure")
mpl_VariableDeclaration = Class(name="mpl::VariableDeclaration")
mpl_Block = Class(name="mpl::Block")
FunctionalUnit = Class(name="FunctionalUnit")
mpl_Variable = Class(name="mpl::Variable")
mpl_Function = Class(name="mpl::Function")
Operation = Class(name="Operation")
mpl_VariableReference = Class(name="mpl::VariableReference")
mpl_IfStatement = Class(name="mpl::IfStatement")
mpl_ComparisonExpression = Class(name="mpl::ComparisonExpression")
mpl_Expression = Class(name="mpl::Expression", is_abstract=True)
mpl_Statement = Class(name="mpl::Statement", is_abstract=True)
mpl_Assignment = Class(name="mpl::Assignment")
Statement = Class(name="Statement")
mpl_AtomicExpression = Class(name="mpl::AtomicExpression", is_abstract=True)
Expression = Class(name="Expression")
mpl_LiteralValue = Class(name="mpl::LiteralValue")
AtomicExpression = Class(name="AtomicExpression")
mpl_WhileLoop = Class(name="mpl::WhileLoop")
mpl_ForLoop = Class(name="mpl::ForLoop")
mpl_Trace = Class(name="mpl::Trace")
mpl_ReturnStatement = Class(name="mpl::ReturnStatement")
mpl_ExpressionStatement = Class(name="mpl::ExpressionStatement")
mpl_SubExpression = Class(name="mpl::SubExpression")
mpl_DivExpression = Class(name="mpl::DivExpression")
mpl_MulExpression = Class(name="mpl::MulExpression")
mpl_UnaryExpression = Class(name="mpl::UnaryExpression", is_abstract=True)
mpl_ArithmeticExpression = Class(name="mpl::ArithmeticExpression", is_abstract=True)
mpl_AddExpression = Class(name="mpl::AddExpression")
ArithmeticExpression = Class(name="ArithmeticExpression")
mpl_UnaryMinusExpression = Class(name="mpl::UnaryMinusExpression")
UnaryExpression = Class(name="UnaryExpression")
mpl_ParenthesisExpression = Class(name="mpl::ParenthesisExpression")
mpl_OperationExpression = Class(name="mpl::OperationExpression")

# mpl_Operation class attributes and methods

# mpl_FunctionalUnit class attributes and methods
mpl_FunctionalUnit_name: Property = Property(name="name", type=StringType)
mpl_FunctionalUnit.attributes={mpl_FunctionalUnit_name}

# mpl_MPLModel class attributes and methods

# mpl_Program class attributes and methods

# mpl_Procedure class attributes and methods

# mpl_VariableDeclaration class attributes and methods

# mpl_Block class attributes and methods

# FunctionalUnit class attributes and methods

# mpl_Variable class attributes and methods
mpl_Variable_name: Property = Property(name="name", type=StringType)
mpl_Variable.attributes={mpl_Variable_name}

# mpl_Function class attributes and methods

# Operation class attributes and methods

# mpl_VariableReference class attributes and methods

# mpl_IfStatement class attributes and methods

# mpl_ComparisonExpression class attributes and methods
mpl_ComparisonExpression_comparisonOperator: Property = Property(name="comparisonOperator", type=StringType)
mpl_ComparisonExpression.attributes={mpl_ComparisonExpression_comparisonOperator}

# mpl_Expression class attributes and methods

# mpl_Statement class attributes and methods

# mpl_Assignment class attributes and methods

# Statement class attributes and methods

# mpl_AtomicExpression class attributes and methods

# Expression class attributes and methods

# mpl_LiteralValue class attributes and methods
mpl_LiteralValue_rawValue: Property = Property(name="rawValue", type=IntegerType)
mpl_LiteralValue.attributes={mpl_LiteralValue_rawValue}

# AtomicExpression class attributes and methods

# mpl_WhileLoop class attributes and methods

# mpl_ForLoop class attributes and methods
mpl_ForLoop_direction: Property = Property(name="direction", type=StringType)
mpl_ForLoop.attributes={mpl_ForLoop_direction}

# mpl_Trace class attributes and methods

# mpl_ReturnStatement class attributes and methods

# mpl_ExpressionStatement class attributes and methods

# mpl_SubExpression class attributes and methods

# mpl_DivExpression class attributes and methods

# mpl_MulExpression class attributes and methods

# mpl_UnaryExpression class attributes and methods

# mpl_ArithmeticExpression class attributes and methods

# mpl_AddExpression class attributes and methods

# ArithmeticExpression class attributes and methods

# mpl_UnaryMinusExpression class attributes and methods

# UnaryExpression class attributes and methods

# mpl_ParenthesisExpression class attributes and methods

# mpl_OperationExpression class attributes and methods

# Relationships
operations1: BinaryAssociation = BinaryAssociation(
    name="operations1",
    ends={
        Property(name="mpl_Operation", type=mpl_MPLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_MPLModel2", type=mpl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="mpl_Program", type=mpl_MPLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_MPLModel", type=mpl_Program, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable8: BinaryAssociation = BinaryAssociation(
    name="variable8",
    ends={
        Property(name="mpl_Variable10", type=mpl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableDeclaration9", type=mpl_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableDeclarations3: BinaryAssociation = BinaryAssociation(
    name="variableDeclarations3",
    ends={
        Property(name="mpl_VariableDeclaration", type=mpl_FunctionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_FunctionalUnit", type=mpl_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionalBody4: BinaryAssociation = BinaryAssociation(
    name="functionalBody4",
    ends={
        Property(name="mpl_Block", type=mpl_FunctionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_FunctionalUnit5", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters6: BinaryAssociation = BinaryAssociation(
    name="parameters6",
    ends={
        Property(name="mpl_Variable", type=mpl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Operation7", type=mpl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rightHandSide15: BinaryAssociation = BinaryAssociation(
    name="rightHandSide15",
    ends={
        Property(name="mpl_Expression16", type=mpl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Assignment", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide17: BinaryAssociation = BinaryAssociation(
    name="leftHandSide17",
    ends={
        Property(name="mpl_VariableReference", type=mpl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Assignment18", type=mpl_VariableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition19: BinaryAssociation = BinaryAssociation(
    name="condition19",
    ends={
        Property(name="mpl_ComparisonExpression", type=mpl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_IfStatement", type=mpl_ComparisonExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableInitialization11: BinaryAssociation = BinaryAssociation(
    name="variableInitialization11",
    ends={
        Property(name="mpl_Expression", type=mpl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableDeclaration12", type=mpl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements13: BinaryAssociation = BinaryAssociation(
    name="statements13",
    ends={
        Property(name="mpl_Statement", type=mpl_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Block14", type=mpl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable45: BinaryAssociation = BinaryAssociation(
    name="variable45",
    ends={
        Property(name="mpl_Variable47", type=mpl_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableReference46", type=mpl_Variable, multiplicity=Multiplicity(1, 1))
    }
)
thenBlock20: BinaryAssociation = BinaryAssociation(
    name="thenBlock20",
    ends={
        Property(name="mpl_Block22", type=mpl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_IfStatement21", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBlock23: BinaryAssociation = BinaryAssociation(
    name="elseBlock23",
    ends={
        Property(name="mpl_Block25", type=mpl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_IfStatement24", type=mpl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition26: BinaryAssociation = BinaryAssociation(
    name="condition26",
    ends={
        Property(name="mpl_ComparisonExpression27", type=mpl_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_WhileLoop", type=mpl_ComparisonExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body28: BinaryAssociation = BinaryAssociation(
    name="body28",
    ends={
        Property(name="mpl_Block30", type=mpl_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_WhileLoop29", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
counter31: BinaryAssociation = BinaryAssociation(
    name="counter31",
    ends={
        Property(name="mpl_Assignment32", type=mpl_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ForLoop", type=mpl_Assignment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bound33: BinaryAssociation = BinaryAssociation(
    name="bound33",
    ends={
        Property(name="mpl_Expression35", type=mpl_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ForLoop34", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body36: BinaryAssociation = BinaryAssociation(
    name="body36",
    ends={
        Property(name="mpl_Block38", type=mpl_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ForLoop37", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varToPrint39: BinaryAssociation = BinaryAssociation(
    name="varToPrint39",
    ends={
        Property(name="mpl_VariableReference40", type=mpl_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Trace", type=mpl_VariableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnValue41: BinaryAssociation = BinaryAssociation(
    name="returnValue41",
    ends={
        Property(name="mpl_Expression42", type=mpl_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ReturnStatement", type=mpl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression43: BinaryAssociation = BinaryAssociation(
    name="expression43",
    ends={
        Property(name="mpl_Expression44", type=mpl_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ExpressionStatement", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide48: BinaryAssociation = BinaryAssociation(
    name="leftHandSide48",
    ends={
        Property(name="mpl_Expression50", type=mpl_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ComparisonExpression49", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide51: BinaryAssociation = BinaryAssociation(
    name="rightHandSide51",
    ends={
        Property(name="mpl_Expression53", type=mpl_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ComparisonExpression52", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand154: BinaryAssociation = BinaryAssociation(
    name="operand154",
    ends={
        Property(name="mpl_Expression55", type=mpl_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ArithmeticExpression", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand256: BinaryAssociation = BinaryAssociation(
    name="operand256",
    ends={
        Property(name="mpl_Expression58", type=mpl_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ArithmeticExpression57", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand59: BinaryAssociation = BinaryAssociation(
    name="operand59",
    ends={
        Property(name="mpl_Expression60", type=mpl_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_UnaryExpression", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation61: BinaryAssociation = BinaryAssociation(
    name="operation61",
    ends={
        Property(name="mpl_Operation62", type=mpl_OperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_OperationExpression", type=mpl_Operation, multiplicity=Multiplicity(1, 1))
    }
)
parameters63: BinaryAssociation = BinaryAssociation(
    name="parameters63",
    ends={
        Property(name="mpl_Expression65", type=mpl_OperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_OperationExpression64", type=mpl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mpl_Procedure_Operation = Generalization(general=Operation, specific=mpl_Procedure)
gen_mpl_Program_FunctionalUnit = Generalization(general=FunctionalUnit, specific=mpl_Program)
gen_mpl_Operation_FunctionalUnit = Generalization(general=FunctionalUnit, specific=mpl_Operation)
gen_mpl_Function_Operation = Generalization(general=Operation, specific=mpl_Function)
gen_mpl_IfStatement_Statement = Generalization(general=Statement, specific=mpl_IfStatement)
gen_mpl_Assignment_Statement = Generalization(general=Statement, specific=mpl_Assignment)
gen_mpl_AtomicExpression_Expression = Generalization(general=Expression, specific=mpl_AtomicExpression)
gen_mpl_LiteralValue_AtomicExpression = Generalization(general=AtomicExpression, specific=mpl_LiteralValue)
gen_mpl_VariableReference_AtomicExpression = Generalization(general=AtomicExpression, specific=mpl_VariableReference)
gen_mpl_WhileLoop_Statement = Generalization(general=Statement, specific=mpl_WhileLoop)
gen_mpl_ForLoop_Statement = Generalization(general=Statement, specific=mpl_ForLoop)
gen_mpl_Trace_Statement = Generalization(general=Statement, specific=mpl_Trace)
gen_mpl_ReturnStatement_Statement = Generalization(general=Statement, specific=mpl_ReturnStatement)
gen_mpl_ExpressionStatement_Statement = Generalization(general=Statement, specific=mpl_ExpressionStatement)
gen_mpl_SubExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=mpl_SubExpression)
gen_mpl_DivExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=mpl_DivExpression)
gen_mpl_MulExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=mpl_MulExpression)
gen_mpl_UnaryExpression_Expression = Generalization(general=Expression, specific=mpl_UnaryExpression)
gen_mpl_ArithmeticExpression_Expression = Generalization(general=Expression, specific=mpl_ArithmeticExpression)
gen_mpl_AddExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=mpl_AddExpression)
gen_mpl_UnaryMinusExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=mpl_UnaryMinusExpression)
gen_mpl_ParenthesisExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=mpl_ParenthesisExpression)
gen_mpl_OperationExpression_Expression = Generalization(general=Expression, specific=mpl_OperationExpression)

# Domain Model
domain_model = DomainModel(
    name="mpl",
    types={mpl_Operation, mpl_FunctionalUnit, mpl_MPLModel, mpl_Program, mpl_Procedure, mpl_VariableDeclaration, mpl_Block, FunctionalUnit, mpl_Variable, mpl_Function, Operation, mpl_VariableReference, mpl_IfStatement, mpl_ComparisonExpression, mpl_Expression, mpl_Statement, mpl_Assignment, Statement, mpl_AtomicExpression, Expression, mpl_LiteralValue, AtomicExpression, mpl_WhileLoop, mpl_ForLoop, mpl_Trace, mpl_ReturnStatement, mpl_ExpressionStatement, mpl_SubExpression, mpl_DivExpression, mpl_MulExpression, mpl_UnaryExpression, mpl_ArithmeticExpression, mpl_AddExpression, ArithmeticExpression, mpl_UnaryMinusExpression, UnaryExpression, mpl_ParenthesisExpression, mpl_OperationExpression, ComparisonOperator, ForLoopDirection},
    associations={operations1, program0, variable8, variableDeclarations3, functionalBody4, parameters6, rightHandSide15, leftHandSide17, condition19, variableInitialization11, statements13, variable45, thenBlock20, elseBlock23, condition26, body28, counter31, bound33, body36, varToPrint39, returnValue41, expression43, leftHandSide48, rightHandSide51, operand154, operand256, operand59, operation61, parameters63},
    generalizations={gen_mpl_Procedure_Operation, gen_mpl_Program_FunctionalUnit, gen_mpl_Operation_FunctionalUnit, gen_mpl_Function_Operation, gen_mpl_IfStatement_Statement, gen_mpl_Assignment_Statement, gen_mpl_AtomicExpression_Expression, gen_mpl_LiteralValue_AtomicExpression, gen_mpl_VariableReference_AtomicExpression, gen_mpl_WhileLoop_Statement, gen_mpl_ForLoop_Statement, gen_mpl_Trace_Statement, gen_mpl_ReturnStatement_Statement, gen_mpl_ExpressionStatement_Statement, gen_mpl_SubExpression_ArithmeticExpression, gen_mpl_DivExpression_ArithmeticExpression, gen_mpl_MulExpression_ArithmeticExpression, gen_mpl_UnaryExpression_Expression, gen_mpl_ArithmeticExpression_Expression, gen_mpl_AddExpression_ArithmeticExpression, gen_mpl_UnaryMinusExpression_UnaryExpression, gen_mpl_ParenthesisExpression_UnaryExpression, gen_mpl_OperationExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)