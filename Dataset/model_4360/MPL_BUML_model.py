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
mpl_Assignment = Class(name="mpl::Assignment")
Form = Class(name="Form")
mpl_VariableReference = Class(name="mpl::VariableReference")
mpl_ExpressionStatement = Class(name="mpl::ExpressionStatement")
mpl_MPLModel = Class(name="mpl::MPLModel")
mpl_Program = Class(name="mpl::Program")
mpl_Operation = Class(name="mpl::Operation", is_abstract=True)
mpl_FunctionalUnit = Class(name="mpl::FunctionalUnit", is_abstract=True)
mpl_VariableDeclaration = Class(name="mpl::VariableDeclaration")
mpl_Block = Class(name="mpl::Block")
FunctionalUnit = Class(name="FunctionalUnit")
mpl_Variable = Class(name="mpl::Variable")
mpl_Expression = Class(name="mpl::Expression", is_abstract=True)
mpl_Statement = Class(name="mpl::Statement")
mpl_Form = Class(name="mpl::Form", is_abstract=True)
mpl_ParenExpression = Class(name="mpl::ParenExpression")
mpl_InputExpression = Class(name="mpl::InputExpression")
mpl_AtomicExpression = Class(name="mpl::AtomicExpression", is_abstract=True)
Expression = Class(name="Expression")
mpl_LiteralValue = Class(name="mpl::LiteralValue")
AtomicExpression = Class(name="AtomicExpression")
mpl_ArithmeticExpression = Class(name="mpl::ArithmeticExpression", is_abstract=True)
mpl_AddExpression = Class(name="mpl::AddExpression")
ArithmeticExpression = Class(name="ArithmeticExpression")
mpl_SubtractExpression = Class(name="mpl::SubtractExpression")
mpl_MultiplyExpression = Class(name="mpl::MultiplyExpression")
mpl_DivisionExpression = Class(name="mpl::DivisionExpression")
mpl_UnaryExpression = Class(name="mpl::UnaryExpression", is_abstract=True)
mpl_NegateExpression = Class(name="mpl::NegateExpression")
UnaryExpression = Class(name="UnaryExpression")
Loop = Class(name="Loop")
mpl_For = Class(name="mpl::For")
mpl_Comparison = Class(name="mpl::Comparison")
mpl_ComparisonOperator = Class(name="mpl::ComparisonOperator", is_abstract=True)
mpl_EQ = Class(name="mpl::EQ")
ComparisonOperator = Class(name="ComparisonOperator")
mpl_NE = Class(name="mpl::NE")
mpl_GT = Class(name="mpl::GT")
mpl_LT = Class(name="mpl::LT")
mpl_GE = Class(name="mpl::GE")
mpl_LE = Class(name="mpl::LE")
mpl_If = Class(name="mpl::If")
mpl_Loop = Class(name="mpl::Loop", is_abstract=True)
mpl_While = Class(name="mpl::While")
mpl_Function = Class(name="mpl::Function")
Operation = Class(name="Operation")
mpl_Procedure = Class(name="mpl::Procedure")
mpl_Return = Class(name="mpl::Return")
mpl_OperationExpression = Class(name="mpl::OperationExpression")
mpl_TraceCall = Class(name="mpl::TraceCall")

# mpl_Assignment class attributes and methods

# Form class attributes and methods

# mpl_VariableReference class attributes and methods

# mpl_ExpressionStatement class attributes and methods

# mpl_MPLModel class attributes and methods

# mpl_Program class attributes and methods

# mpl_Operation class attributes and methods

# mpl_FunctionalUnit class attributes and methods
mpl_FunctionalUnit_name: Property = Property(name="name", type=StringType)
mpl_FunctionalUnit.attributes={mpl_FunctionalUnit_name}

# mpl_VariableDeclaration class attributes and methods

# mpl_Block class attributes and methods

# FunctionalUnit class attributes and methods

# mpl_Variable class attributes and methods
mpl_Variable_name: Property = Property(name="name", type=StringType)
mpl_Variable.attributes={mpl_Variable_name}

# mpl_Expression class attributes and methods

# mpl_Statement class attributes and methods

# mpl_Form class attributes and methods

# mpl_ParenExpression class attributes and methods

# mpl_InputExpression class attributes and methods

# mpl_AtomicExpression class attributes and methods

# Expression class attributes and methods

# mpl_LiteralValue class attributes and methods
mpl_LiteralValue_rawValue: Property = Property(name="rawValue", type=IntegerType)
mpl_LiteralValue.attributes={mpl_LiteralValue_rawValue}

# AtomicExpression class attributes and methods

# mpl_ArithmeticExpression class attributes and methods

# mpl_AddExpression class attributes and methods

# ArithmeticExpression class attributes and methods

# mpl_SubtractExpression class attributes and methods

# mpl_MultiplyExpression class attributes and methods

# mpl_DivisionExpression class attributes and methods

# mpl_UnaryExpression class attributes and methods

# mpl_NegateExpression class attributes and methods

# UnaryExpression class attributes and methods

# Loop class attributes and methods

# mpl_For class attributes and methods
mpl_For_downwards: Property = Property(name="downwards", type=StringType)
mpl_For.attributes={mpl_For_downwards}

# mpl_Comparison class attributes and methods

# mpl_ComparisonOperator class attributes and methods

# mpl_EQ class attributes and methods

# ComparisonOperator class attributes and methods

# mpl_NE class attributes and methods

# mpl_GT class attributes and methods

# mpl_LT class attributes and methods

# mpl_GE class attributes and methods

# mpl_LE class attributes and methods

# mpl_If class attributes and methods

# mpl_Loop class attributes and methods

# mpl_While class attributes and methods

# mpl_Function class attributes and methods

# Operation class attributes and methods

# mpl_Procedure class attributes and methods

# mpl_Return class attributes and methods

# mpl_OperationExpression class attributes and methods

# mpl_TraceCall class attributes and methods

# Relationships
leftHandSide14: BinaryAssociation = BinaryAssociation(
    name="leftHandSide14",
    ends={
        Property(name="mpl_VariableReference", type=mpl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Assignment", type=mpl_VariableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide15: BinaryAssociation = BinaryAssociation(
    name="rightHandSide15",
    ends={
        Property(name="mpl_Expression17", type=mpl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Assignment16", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression18: BinaryAssociation = BinaryAssociation(
    name="expression18",
    ends={
        Property(name="mpl_Expression19", type=mpl_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ExpressionStatement", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="mpl_Program", type=mpl_MPLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_MPLModel", type=mpl_Program, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operations1: BinaryAssociation = BinaryAssociation(
    name="operations1",
    ends={
        Property(name="mpl_Operation", type=mpl_MPLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_MPLModel2", type=mpl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDeclarations3: BinaryAssociation = BinaryAssociation(
    name="variableDeclarations3",
    ends={
        Property(name="mpl_VariableDeclaration", type=mpl_FunctionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_FunctionalUnit", type=mpl_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body4: BinaryAssociation = BinaryAssociation(
    name="body4",
    ends={
        Property(name="mpl_Block", type=mpl_FunctionalUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_FunctionalUnit5", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable6: BinaryAssociation = BinaryAssociation(
    name="variable6",
    ends={
        Property(name="mpl_Variable", type=mpl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableDeclaration7", type=mpl_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialValue8: BinaryAssociation = BinaryAssociation(
    name="initialValue8",
    ends={
        Property(name="mpl_Expression", type=mpl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableDeclaration9", type=mpl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements10: BinaryAssociation = BinaryAssociation(
    name="statements10",
    ends={
        Property(name="mpl_Statement", type=mpl_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Block11", type=mpl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
form12: BinaryAssociation = BinaryAssociation(
    name="form12",
    ends={
        Property(name="mpl_Form", type=mpl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Statement13", type=mpl_Form, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lowerBound30: BinaryAssociation = BinaryAssociation(
    name="lowerBound30",
    ends={
        Property(name="mpl_LiteralValue", type=mpl_InputExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_InputExpression", type=mpl_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable20: BinaryAssociation = BinaryAssociation(
    name="variable20",
    ends={
        Property(name="mpl_Variable22", type=mpl_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableReference21", type=mpl_Variable, multiplicity=Multiplicity(1, 1))
    }
)
operand123: BinaryAssociation = BinaryAssociation(
    name="operand123",
    ends={
        Property(name="mpl_Expression24", type=mpl_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ArithmeticExpression", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand225: BinaryAssociation = BinaryAssociation(
    name="operand225",
    ends={
        Property(name="mpl_Expression27", type=mpl_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ArithmeticExpression26", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand28: BinaryAssociation = BinaryAssociation(
    name="operand28",
    ends={
        Property(name="mpl_Expression29", type=mpl_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_UnaryExpression", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition51: BinaryAssociation = BinaryAssociation(
    name="condition51",
    ends={
        Property(name="mpl_Comparison52", type=mpl_While, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_While", type=mpl_Comparison, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from53: BinaryAssociation = BinaryAssociation(
    name="from53",
    ends={
        Property(name="mpl_Assignment54", type=mpl_For, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_For", type=mpl_Assignment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
to55: BinaryAssociation = BinaryAssociation(
    name="to55",
    ends={
        Property(name="mpl_Expression57", type=mpl_For, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_For56", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperBound31: BinaryAssociation = BinaryAssociation(
    name="upperBound31",
    ends={
        Property(name="mpl_LiteralValue33", type=mpl_InputExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_InputExpression32", type=mpl_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftHandSide34: BinaryAssociation = BinaryAssociation(
    name="leftHandSide34",
    ends={
        Property(name="mpl_Expression35", type=mpl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Comparison", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator36: BinaryAssociation = BinaryAssociation(
    name="operator36",
    ends={
        Property(name="mpl_ComparisonOperator", type=mpl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Comparison37", type=mpl_ComparisonOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide38: BinaryAssociation = BinaryAssociation(
    name="rightHandSide38",
    ends={
        Property(name="mpl_Expression40", type=mpl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Comparison39", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition41: BinaryAssociation = BinaryAssociation(
    name="condition41",
    ends={
        Property(name="mpl_Comparison42", type=mpl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_If", type=mpl_Comparison, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then43: BinaryAssociation = BinaryAssociation(
    name="then43",
    ends={
        Property(name="mpl_Block45", type=mpl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_If44", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else46: BinaryAssociation = BinaryAssociation(
    name="else46",
    ends={
        Property(name="mpl_Block48", type=mpl_If, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_If47", type=mpl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body49: BinaryAssociation = BinaryAssociation(
    name="body49",
    ends={
        Property(name="mpl_Block50", type=mpl_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Loop", type=mpl_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters58: BinaryAssociation = BinaryAssociation(
    name="parameters58",
    ends={
        Property(name="mpl_Variable60", type=mpl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Operation59", type=mpl_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preconditions61: BinaryAssociation = BinaryAssociation(
    name="preconditions61",
    ends={
        Property(name="mpl_Comparison63", type=mpl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Operation62", type=mpl_Comparison, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postconditions64: BinaryAssociation = BinaryAssociation(
    name="postconditions64",
    ends={
        Property(name="mpl_Comparison66", type=mpl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Operation65", type=mpl_Comparison, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value67: BinaryAssociation = BinaryAssociation(
    name="value67",
    ends={
        Property(name="mpl_Expression68", type=mpl_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Return", type=mpl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation69: BinaryAssociation = BinaryAssociation(
    name="operation69",
    ends={
        Property(name="mpl_Operation70", type=mpl_OperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_OperationExpression", type=mpl_Operation, multiplicity=Multiplicity(1, 1))
    }
)
parameterValues71: BinaryAssociation = BinaryAssociation(
    name="parameterValues71",
    ends={
        Property(name="mpl_Expression73", type=mpl_OperationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_OperationExpression72", type=mpl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable74: BinaryAssociation = BinaryAssociation(
    name="variable74",
    ends={
        Property(name="mpl_VariableReference75", type=mpl_TraceCall, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_TraceCall", type=mpl_VariableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_mpl_Assignment_Form = Generalization(general=Form, specific=mpl_Assignment)
gen_mpl_ExpressionStatement_Form = Generalization(general=Form, specific=mpl_ExpressionStatement)
gen_mpl_Program_FunctionalUnit = Generalization(general=FunctionalUnit, specific=mpl_Program)
gen_mpl_ParenExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=mpl_ParenExpression)
gen_mpl_InputExpression_Expression = Generalization(general=Expression, specific=mpl_InputExpression)
gen_mpl_AtomicExpression_Expression = Generalization(general=Expression, specific=mpl_AtomicExpression)
gen_mpl_LiteralValue_AtomicExpression = Generalization(general=AtomicExpression, specific=mpl_LiteralValue)
gen_mpl_VariableReference_AtomicExpression = Generalization(general=AtomicExpression, specific=mpl_VariableReference)
gen_mpl_ArithmeticExpression_Expression = Generalization(general=Expression, specific=mpl_ArithmeticExpression)
gen_mpl_AddExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=mpl_AddExpression)
gen_mpl_SubtractExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=mpl_SubtractExpression)
gen_mpl_MultiplyExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=mpl_MultiplyExpression)
gen_mpl_DivisionExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=mpl_DivisionExpression)
gen_mpl_UnaryExpression_Expression = Generalization(general=Expression, specific=mpl_UnaryExpression)
gen_mpl_NegateExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=mpl_NegateExpression)
gen_mpl_While_Loop = Generalization(general=Loop, specific=mpl_While)
gen_mpl_For_Loop = Generalization(general=Loop, specific=mpl_For)
gen_mpl_Operation_FunctionalUnit = Generalization(general=FunctionalUnit, specific=mpl_Operation)
gen_mpl_EQ_ComparisonOperator = Generalization(general=ComparisonOperator, specific=mpl_EQ)
gen_mpl_NE_ComparisonOperator = Generalization(general=ComparisonOperator, specific=mpl_NE)
gen_mpl_GT_ComparisonOperator = Generalization(general=ComparisonOperator, specific=mpl_GT)
gen_mpl_LT_ComparisonOperator = Generalization(general=ComparisonOperator, specific=mpl_LT)
gen_mpl_GE_ComparisonOperator = Generalization(general=ComparisonOperator, specific=mpl_GE)
gen_mpl_LE_ComparisonOperator = Generalization(general=ComparisonOperator, specific=mpl_LE)
gen_mpl_If_Form = Generalization(general=Form, specific=mpl_If)
gen_mpl_Loop_Form = Generalization(general=Form, specific=mpl_Loop)
gen_mpl_Function_Operation = Generalization(general=Operation, specific=mpl_Function)
gen_mpl_Procedure_Operation = Generalization(general=Operation, specific=mpl_Procedure)
gen_mpl_Return_Form = Generalization(general=Form, specific=mpl_Return)
gen_mpl_OperationExpression_Expression = Generalization(general=Expression, specific=mpl_OperationExpression)
gen_mpl_TraceCall_Form = Generalization(general=Form, specific=mpl_TraceCall)

# Domain Model
domain_model = DomainModel(
    name="mpl",
    types={mpl_Assignment, Form, mpl_VariableReference, mpl_ExpressionStatement, mpl_MPLModel, mpl_Program, mpl_Operation, mpl_FunctionalUnit, mpl_VariableDeclaration, mpl_Block, FunctionalUnit, mpl_Variable, mpl_Expression, mpl_Statement, mpl_Form, mpl_ParenExpression, mpl_InputExpression, mpl_AtomicExpression, Expression, mpl_LiteralValue, AtomicExpression, mpl_ArithmeticExpression, mpl_AddExpression, ArithmeticExpression, mpl_SubtractExpression, mpl_MultiplyExpression, mpl_DivisionExpression, mpl_UnaryExpression, mpl_NegateExpression, UnaryExpression, Loop, mpl_For, mpl_Comparison, mpl_ComparisonOperator, mpl_EQ, ComparisonOperator, mpl_NE, mpl_GT, mpl_LT, mpl_GE, mpl_LE, mpl_If, mpl_Loop, mpl_While, mpl_Function, Operation, mpl_Procedure, mpl_Return, mpl_OperationExpression, mpl_TraceCall},
    associations={leftHandSide14, rightHandSide15, expression18, program0, operations1, variableDeclarations3, body4, variable6, initialValue8, statements10, form12, lowerBound30, variable20, operand123, operand225, operand28, condition51, from53, to55, upperBound31, leftHandSide34, operator36, rightHandSide38, condition41, then43, else46, body49, parameters58, preconditions61, postconditions64, value67, operation69, parameterValues71, variable74},
    generalizations={gen_mpl_Assignment_Form, gen_mpl_ExpressionStatement_Form, gen_mpl_Program_FunctionalUnit, gen_mpl_ParenExpression_UnaryExpression, gen_mpl_InputExpression_Expression, gen_mpl_AtomicExpression_Expression, gen_mpl_LiteralValue_AtomicExpression, gen_mpl_VariableReference_AtomicExpression, gen_mpl_ArithmeticExpression_Expression, gen_mpl_AddExpression_ArithmeticExpression, gen_mpl_SubtractExpression_ArithmeticExpression, gen_mpl_MultiplyExpression_ArithmeticExpression, gen_mpl_DivisionExpression_ArithmeticExpression, gen_mpl_UnaryExpression_Expression, gen_mpl_NegateExpression_UnaryExpression, gen_mpl_While_Loop, gen_mpl_For_Loop, gen_mpl_Operation_FunctionalUnit, gen_mpl_EQ_ComparisonOperator, gen_mpl_NE_ComparisonOperator, gen_mpl_GT_ComparisonOperator, gen_mpl_LT_ComparisonOperator, gen_mpl_GE_ComparisonOperator, gen_mpl_LE_ComparisonOperator, gen_mpl_If_Form, gen_mpl_Loop_Form, gen_mpl_Function_Operation, gen_mpl_Procedure_Operation, gen_mpl_Return_Form, gen_mpl_OperationExpression_Expression, gen_mpl_TraceCall_Form},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)