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
mpl_Variable = Class(name="mpl_Variable")
mpl_Expression = Class(name="mpl_Expression", is_abstract=True)
mpl_Statement = Class(name="mpl_Statement", is_abstract=True)
mpl_Assignment = Class(name="mpl_Assignment")
mpl_VariableReference = Class(name="mpl_VariableReference")
mpl_ExpressionStatement = Class(name="mpl_ExpressionStatement")
Statement = Class(name="Statement")
mpl_AtomicExpression = Class(name="mpl_AtomicExpression", is_abstract=True)
Expression = Class(name="Expression")
mpl_Program = Class(name="mpl_Program")
Operation = Class(name="Operation")
mpl_VariableDeclaration = Class(name="mpl_VariableDeclaration")
mpl_SubExpression = Class(name="mpl_SubExpression")
mpl_DivExpression = Class(name="mpl_DivExpression")
mpl_UnaryMinusExpression = Class(name="mpl_UnaryMinusExpression")
UnaryExpression = Class(name="UnaryExpression")
mpl_UnaryExpression = Class(name="mpl_UnaryExpression", is_abstract=True)
mpl_ParenthesisExpression = Class(name="mpl_ParenthesisExpression")
mpl_BinaryExpression = Class(name="mpl_BinaryExpression", is_abstract=True)
mpl_Block = Class(name="mpl_Block")
mpl_LiteralValue = Class(name="mpl_LiteralValue")
AtomicExpression = Class(name="AtomicExpression")
mpl_AddExpression = Class(name="mpl_AddExpression")
BinaryExpression = Class(name="BinaryExpression")
mpl_MultExpression = Class(name="mpl_MultExpression")
mpl_WhileLoop = Class(name="mpl_WhileLoop")
mpl_ForLoop = Class(name="mpl_ForLoop")
mpl_IfStatement = Class(name="mpl_IfStatement")
mpl_Comparison = Class(name="mpl_Comparison")
mpl_ReturnStatement = Class(name="mpl_ReturnStatement")
mpl_OperationCall = Class(name="mpl_OperationCall")
mpl_MPLModel = Class(name="mpl_MPLModel")
mpl_TraceStatement = Class(name="mpl_TraceStatement")
mpl_AssignmentStatement = Class(name="mpl_AssignmentStatement")
mpl_Function = Class(name="mpl_Function")
mpl_Procedure = Class(name="mpl_Procedure")
mpl_Operation = Class(name="mpl_Operation", is_abstract=True)

# mpl_Variable class attributes and methods
mpl_Variable_name: Property = Property(name="name", type=StringType)
mpl_Variable_value: Property = Property(name="value", type=IntegerType)
mpl_Variable.attributes={mpl_Variable_name, mpl_Variable_value}

# mpl_Expression class attributes and methods

# mpl_Statement class attributes and methods

# mpl_Assignment class attributes and methods

# mpl_VariableReference class attributes and methods

# mpl_ExpressionStatement class attributes and methods

# Statement class attributes and methods

# mpl_AtomicExpression class attributes and methods

# Expression class attributes and methods

# mpl_Program class attributes and methods

# Operation class attributes and methods

# mpl_VariableDeclaration class attributes and methods

# mpl_SubExpression class attributes and methods

# mpl_DivExpression class attributes and methods

# mpl_UnaryMinusExpression class attributes and methods

# UnaryExpression class attributes and methods

# mpl_UnaryExpression class attributes and methods

# mpl_ParenthesisExpression class attributes and methods

# mpl_BinaryExpression class attributes and methods

# mpl_Block class attributes and methods

# mpl_LiteralValue class attributes and methods
mpl_LiteralValue_rawValue: Property = Property(name="rawValue", type=IntegerType)
mpl_LiteralValue.attributes={mpl_LiteralValue_rawValue}

# AtomicExpression class attributes and methods

# mpl_AddExpression class attributes and methods

# BinaryExpression class attributes and methods

# mpl_MultExpression class attributes and methods

# mpl_WhileLoop class attributes and methods

# mpl_ForLoop class attributes and methods
mpl_ForLoop_increment: Property = Property(name="increment", type=BooleanType)
mpl_ForLoop.attributes={mpl_ForLoop_increment}

# mpl_IfStatement class attributes and methods

# mpl_Comparison class attributes and methods
mpl_Comparison_operator: Property = Property(name="operator", type=StringType)
mpl_Comparison.attributes={mpl_Comparison_operator}

# mpl_ReturnStatement class attributes and methods

# mpl_OperationCall class attributes and methods

# mpl_MPLModel class attributes and methods

# mpl_TraceStatement class attributes and methods

# mpl_AssignmentStatement class attributes and methods

# mpl_Function class attributes and methods

# mpl_Procedure class attributes and methods

# mpl_Operation class attributes and methods
mpl_Operation_name: Property = Property(name="name", type=StringType)
mpl_Operation.attributes={mpl_Operation_name}

# Relationships
variable0: BinaryAssociation = BinaryAssociation(
    name="variable0",
    ends={
        Property(name="mpl_Variable", type=mpl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableDeclaration", type=mpl_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialValue1: BinaryAssociation = BinaryAssociation(
    name="initialValue1",
    ends={
        Property(name="mpl_Expression", type=mpl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableDeclaration2", type=mpl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftHandSide3: BinaryAssociation = BinaryAssociation(
    name="leftHandSide3",
    ends={
        Property(name="mpl_VariableReference", type=mpl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Assignment", type=mpl_VariableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide4: BinaryAssociation = BinaryAssociation(
    name="rightHandSide4",
    ends={
        Property(name="mpl_Expression6", type=mpl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Assignment5", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression7: BinaryAssociation = BinaryAssociation(
    name="expression7",
    ends={
        Property(name="mpl_Expression8", type=mpl_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ExpressionStatement", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand12: BinaryAssociation = BinaryAssociation(
    name="operand12",
    ends={
        Property(name="mpl_Expression13", type=mpl_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_UnaryExpression", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand114: BinaryAssociation = BinaryAssociation(
    name="operand114",
    ends={
        Property(name="mpl_Expression15", type=mpl_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_BinaryExpression", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand216: BinaryAssociation = BinaryAssociation(
    name="operand216",
    ends={
        Property(name="mpl_Expression18", type=mpl_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_BinaryExpression17", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable9: BinaryAssociation = BinaryAssociation(
    name="variable9",
    ends={
        Property(name="mpl_Variable11", type=mpl_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableReference10", type=mpl_Variable, multiplicity=Multiplicity(1, 1))
    }
)
operand227: BinaryAssociation = BinaryAssociation(
    name="operand227",
    ends={
        Property(name="mpl_Expression29", type=mpl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Comparison28", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand130: BinaryAssociation = BinaryAssociation(
    name="operand130",
    ends={
        Property(name="mpl_Expression32", type=mpl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Comparison31", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block33: BinaryAssociation = BinaryAssociation(
    name="block33",
    ends={
        Property(name="mpl_Block34", type=mpl_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_WhileLoop", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition35: BinaryAssociation = BinaryAssociation(
    name="condition35",
    ends={
        Property(name="mpl_Comparison37", type=mpl_WhileLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_WhileLoop36", type=mpl_Comparison, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block38: BinaryAssociation = BinaryAssociation(
    name="block38",
    ends={
        Property(name="mpl_Block39", type=mpl_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ForLoop", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index40: BinaryAssociation = BinaryAssociation(
    name="index40",
    ends={
        Property(name="mpl_Assignment42", type=mpl_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ForLoop41", type=mpl_Assignment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperBound43: BinaryAssociation = BinaryAssociation(
    name="upperBound43",
    ends={
        Property(name="mpl_Expression45", type=mpl_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ForLoop44", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements19: BinaryAssociation = BinaryAssociation(
    name="statements19",
    ends={
        Property(name="mpl_Statement", type=mpl_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Block", type=mpl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
then20: BinaryAssociation = BinaryAssociation(
    name="then20",
    ends={
        Property(name="mpl_Block21", type=mpl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_IfStatement", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else_22: BinaryAssociation = BinaryAssociation(
    name="else_22",
    ends={
        Property(name="mpl_Block24", type=mpl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_IfStatement23", type=mpl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition25: BinaryAssociation = BinaryAssociation(
    name="condition25",
    ends={
        Property(name="mpl_Comparison", type=mpl_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_IfStatement26", type=mpl_Comparison, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableDeclarations50: BinaryAssociation = BinaryAssociation(
    name="variableDeclarations50",
    ends={
        Property(name="mpl_VariableDeclaration52", type=mpl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Operation51", type=mpl_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block53: BinaryAssociation = BinaryAssociation(
    name="block53",
    ends={
        Property(name="mpl_Block55", type=mpl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Operation54", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value56: BinaryAssociation = BinaryAssociation(
    name="value56",
    ends={
        Property(name="mpl_Expression57", type=mpl_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ReturnStatement", type=mpl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters58: BinaryAssociation = BinaryAssociation(
    name="parameters58",
    ends={
        Property(name="mpl_Expression59", type=mpl_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_OperationCall", type=mpl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation60: BinaryAssociation = BinaryAssociation(
    name="operation60",
    ends={
        Property(name="mpl_Operation62", type=mpl_OperationCall, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_OperationCall61", type=mpl_Operation, multiplicity=Multiplicity(1, 1))
    }
)
program63: BinaryAssociation = BinaryAssociation(
    name="program63",
    ends={
        Property(name="mpl_Program", type=mpl_MPLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_MPLModel", type=mpl_Program, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operations64: BinaryAssociation = BinaryAssociation(
    name="operations64",
    ends={
        Property(name="mpl_Operation66", type=mpl_MPLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_MPLModel65", type=mpl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment46: BinaryAssociation = BinaryAssociation(
    name="assignment46",
    ends={
        Property(name="mpl_Assignment47", type=mpl_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_AssignmentStatement", type=mpl_Assignment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters48: BinaryAssociation = BinaryAssociation(
    name="parameters48",
    ends={
        Property(name="mpl_VariableDeclaration49", type=mpl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Operation", type=mpl_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableReference67: BinaryAssociation = BinaryAssociation(
    name="variableReference67",
    ends={
        Property(name="mpl_VariableReference68", type=mpl_TraceStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_TraceStatement", type=mpl_VariableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_mpl_ExpressionStatement_Statement = Generalization(general=Statement, specific=mpl_ExpressionStatement)
gen_mpl_Program_Operation = Generalization(general=Operation, specific=mpl_Program)
gen_mpl_MultExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=mpl_MultExpression)
gen_mpl_SubExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=mpl_SubExpression)
gen_mpl_DivExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=mpl_DivExpression)
gen_mpl_UnaryMinusExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=mpl_UnaryMinusExpression)
gen_mpl_UnaryExpression_Expression = Generalization(general=Expression, specific=mpl_UnaryExpression)
gen_mpl_ParenthesisExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=mpl_ParenthesisExpression)
gen_mpl_BinaryExpression_Expression = Generalization(general=Expression, specific=mpl_BinaryExpression)
gen_mpl_AtomicExpression_Expression = Generalization(general=Expression, specific=mpl_AtomicExpression)
gen_mpl_LiteralValue_AtomicExpression = Generalization(general=AtomicExpression, specific=mpl_LiteralValue)
gen_mpl_VariableReference_AtomicExpression = Generalization(general=AtomicExpression, specific=mpl_VariableReference)
gen_mpl_AddExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=mpl_AddExpression)
gen_mpl_WhileLoop_Statement = Generalization(general=Statement, specific=mpl_WhileLoop)
gen_mpl_ForLoop_Statement = Generalization(general=Statement, specific=mpl_ForLoop)
gen_mpl_IfStatement_Statement = Generalization(general=Statement, specific=mpl_IfStatement)
gen_mpl_ReturnStatement_Statement = Generalization(general=Statement, specific=mpl_ReturnStatement)
gen_mpl_OperationCall_AtomicExpression = Generalization(general=AtomicExpression, specific=mpl_OperationCall)
gen_mpl_TraceStatement_Statement = Generalization(general=Statement, specific=mpl_TraceStatement)
gen_mpl_AssignmentStatement_Statement = Generalization(general=Statement, specific=mpl_AssignmentStatement)
gen_mpl_Function_Operation = Generalization(general=Operation, specific=mpl_Function)
gen_mpl_Procedure_Operation = Generalization(general=Operation, specific=mpl_Procedure)

# Domain Model
domain_model = DomainModel(
    name="mpl",
    types={mpl_Variable, mpl_Expression, mpl_Statement, mpl_Assignment, mpl_VariableReference, mpl_ExpressionStatement, Statement, mpl_AtomicExpression, Expression, mpl_Program, Operation, mpl_VariableDeclaration, mpl_SubExpression, mpl_DivExpression, mpl_UnaryMinusExpression, UnaryExpression, mpl_UnaryExpression, mpl_ParenthesisExpression, mpl_BinaryExpression, mpl_Block, mpl_LiteralValue, AtomicExpression, mpl_AddExpression, BinaryExpression, mpl_MultExpression, mpl_WhileLoop, mpl_ForLoop, mpl_IfStatement, mpl_Comparison, mpl_ReturnStatement, mpl_OperationCall, mpl_MPLModel, mpl_TraceStatement, mpl_AssignmentStatement, mpl_Function, mpl_Procedure, mpl_Operation},
    associations={variable0, initialValue1, leftHandSide3, rightHandSide4, expression7, operand12, operand114, operand216, variable9, operand227, operand130, block33, condition35, block38, index40, upperBound43, statements19, then20, else_22, condition25, variableDeclarations50, block53, value56, parameters58, operation60, program63, operations64, assignment46, parameters48, variableReference67},
    generalizations={gen_mpl_ExpressionStatement_Statement, gen_mpl_Program_Operation, gen_mpl_MultExpression_BinaryExpression, gen_mpl_SubExpression_BinaryExpression, gen_mpl_DivExpression_BinaryExpression, gen_mpl_UnaryMinusExpression_UnaryExpression, gen_mpl_UnaryExpression_Expression, gen_mpl_ParenthesisExpression_UnaryExpression, gen_mpl_BinaryExpression_Expression, gen_mpl_AtomicExpression_Expression, gen_mpl_LiteralValue_AtomicExpression, gen_mpl_VariableReference_AtomicExpression, gen_mpl_AddExpression_BinaryExpression, gen_mpl_WhileLoop_Statement, gen_mpl_ForLoop_Statement, gen_mpl_IfStatement_Statement, gen_mpl_ReturnStatement_Statement, gen_mpl_OperationCall_AtomicExpression, gen_mpl_TraceStatement_Statement, gen_mpl_AssignmentStatement_Statement, gen_mpl_Function_Operation, gen_mpl_Procedure_Operation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)