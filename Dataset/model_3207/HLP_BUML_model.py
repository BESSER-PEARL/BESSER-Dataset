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
            EnumerationLiteral(name="UNEQUAL"),
			EnumerationLiteral(name="LESS_THAN"),
			EnumerationLiteral(name="LESS_THAN_OR_EQUAL"),
			EnumerationLiteral(name="GREATER_THAN_OR_EQUAL"),
			EnumerationLiteral(name="GREATER_THAN"),
			EnumerationLiteral(name="EQUAL")
    }
)

# Classes
hlp_ScheduleInstruction = Class(name="hlp::ScheduleInstruction")
hlp_VariableDeclaration = Class(name="hlp::VariableDeclaration")
hlp_Variable = Class(name="hlp::Variable")
hlp_Expression = Class(name="hlp::Expression", is_abstract=True)
hlp_Assignment = Class(name="hlp::Assignment")
Statement = Class(name="Statement")
hlp_HighLevelProgram = Class(name="hlp::HighLevelProgram")
VariableDeclarationScope = Class(name="VariableDeclarationScope")
Nameable = Class(name="Nameable")
hlp_Task = Class(name="hlp::Task")
hlp_AddExpression = Class(name="hlp::AddExpression")
ArithmeticExpression = Class(name="ArithmeticExpression")
hlp_AtomicExpression = Class(name="hlp::AtomicExpression", is_abstract=True)
Expression = Class(name="Expression")
hlp_BinaryExpression = Class(name="hlp::BinaryExpression", is_abstract=True)
hlp_VariableReference = Class(name="hlp::VariableReference")
hlp_Statement = Class(name="hlp::Statement", is_abstract=True)
hlp_LiteralValue = Class(name="hlp::LiteralValue")
AtomicExpression = Class(name="AtomicExpression")
hlp_Block = Class(name="hlp::Block")
hlp_IfStatement = Class(name="hlp::IfStatement")
hlp_SubtractExpression = Class(name="hlp::SubtractExpression")
hlp_MultiplyExpression = Class(name="hlp::MultiplyExpression")
hlp_DivideExpression = Class(name="hlp::DivideExpression")
hlp_ParenthesisExpression = Class(name="hlp::ParenthesisExpression")
hlp_VariableDeclarationScope = Class(name="hlp::VariableDeclarationScope", is_abstract=True)
hlp_Loop = Class(name="hlp::Loop", is_abstract=True)
hlp_Condition = Class(name="hlp::Condition")
hlp_ConditionalLoop = Class(name="hlp::ConditionalLoop", is_abstract=True)
hlp_Nameable = Class(name="hlp::Nameable", is_abstract=True)
hlp_ExpressionStatement = Class(name="hlp::ExpressionStatement")
Loop = Class(name="Loop")
hlp_WhileLoop = Class(name="hlp::WhileLoop")
ConditionalLoop = Class(name="ConditionalLoop")
hlp_ForLoop = Class(name="hlp::ForLoop")
hlp_UnaryExpression = Class(name="hlp::UnaryExpression", is_abstract=True)
hlp_UnaryMinusExpression = Class(name="hlp::UnaryMinusExpression")
UnaryExpression = Class(name="UnaryExpression")
hlp_ArithmeticExpression = Class(name="hlp::ArithmeticExpression", is_abstract=True)
BinaryExpression = Class(name="BinaryExpression")
hlp_SynchronizedStatement = Class(name="hlp::SynchronizedStatement")

# hlp_ScheduleInstruction class attributes and methods

# hlp_VariableDeclaration class attributes and methods

# hlp_Variable class attributes and methods

# hlp_Expression class attributes and methods

# hlp_Assignment class attributes and methods

# Statement class attributes and methods

# hlp_HighLevelProgram class attributes and methods

# VariableDeclarationScope class attributes and methods

# Nameable class attributes and methods

# hlp_Task class attributes and methods

# hlp_AddExpression class attributes and methods

# ArithmeticExpression class attributes and methods

# hlp_AtomicExpression class attributes and methods

# Expression class attributes and methods

# hlp_BinaryExpression class attributes and methods

# hlp_VariableReference class attributes and methods

# hlp_Statement class attributes and methods

# hlp_LiteralValue class attributes and methods
hlp_LiteralValue_rawValue: Property = Property(name="rawValue", type=StringType)
hlp_LiteralValue.attributes={hlp_LiteralValue_rawValue}

# AtomicExpression class attributes and methods

# hlp_Block class attributes and methods

# hlp_IfStatement class attributes and methods

# hlp_SubtractExpression class attributes and methods

# hlp_MultiplyExpression class attributes and methods

# hlp_DivideExpression class attributes and methods

# hlp_ParenthesisExpression class attributes and methods

# hlp_VariableDeclarationScope class attributes and methods

# hlp_Loop class attributes and methods

# hlp_Condition class attributes and methods
hlp_Condition_operator: Property = Property(name="operator", type=StringType)
hlp_Condition.attributes={hlp_Condition_operator}

# hlp_ConditionalLoop class attributes and methods

# hlp_Nameable class attributes and methods
hlp_Nameable_name: Property = Property(name="name", type=StringType)
hlp_Nameable.attributes={hlp_Nameable_name}

# hlp_ExpressionStatement class attributes and methods

# Loop class attributes and methods

# hlp_WhileLoop class attributes and methods

# ConditionalLoop class attributes and methods

# hlp_ForLoop class attributes and methods
hlp_ForLoop_incrementing: Property = Property(name="incrementing", type=BooleanType)
hlp_ForLoop.attributes={hlp_ForLoop_incrementing}

# hlp_UnaryExpression class attributes and methods

# hlp_UnaryMinusExpression class attributes and methods

# UnaryExpression class attributes and methods

# hlp_ArithmeticExpression class attributes and methods

# BinaryExpression class attributes and methods

# hlp_SynchronizedStatement class attributes and methods

# Relationships
scheduleInstruction1: BinaryAssociation = BinaryAssociation(
    name="scheduleInstruction1",
    ends={
        Property(name="hlp_ScheduleInstruction", type=hlp_HighLevelProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_HighLevelProgram2", type=hlp_ScheduleInstruction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable3: BinaryAssociation = BinaryAssociation(
    name="variable3",
    ends={
        Property(name="hlp_Variable", type=hlp_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_VariableDeclaration", type=hlp_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialValue4: BinaryAssociation = BinaryAssociation(
    name="initialValue4",
    ends={
        Property(name="hlp_Expression", type=hlp_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_VariableDeclaration5", type=hlp_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tasks0: BinaryAssociation = BinaryAssociation(
    name="tasks0",
    ends={
        Property(name="hlp_Task", type=hlp_HighLevelProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_HighLevelProgram", type=hlp_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable10: BinaryAssociation = BinaryAssociation(
    name="variable10",
    ends={
        Property(name="hlp_Variable12", type=hlp_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_VariableReference11", type=hlp_Variable, multiplicity=Multiplicity(1, 1))
    }
)
leftHandSide13: BinaryAssociation = BinaryAssociation(
    name="leftHandSide13",
    ends={
        Property(name="hlp_Expression14", type=hlp_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_BinaryExpression", type=hlp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide6: BinaryAssociation = BinaryAssociation(
    name="leftHandSide6",
    ends={
        Property(name="hlp_VariableReference", type=hlp_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_Assignment", type=hlp_VariableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide7: BinaryAssociation = BinaryAssociation(
    name="rightHandSide7",
    ends={
        Property(name="hlp_Expression9", type=hlp_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_Assignment8", type=hlp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand18: BinaryAssociation = BinaryAssociation(
    name="operand18",
    ends={
        Property(name="hlp_ParenthesisExpression", type=hlp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="hlp_Expression19", type=hlp_ParenthesisExpression, multiplicity=Multiplicity(1, 1))
    }
)
statements20: BinaryAssociation = BinaryAssociation(
    name="statements20",
    ends={
        Property(name="hlp_Statement", type=hlp_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_Block", type=hlp_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenBlock21: BinaryAssociation = BinaryAssociation(
    name="thenBlock21",
    ends={
        Property(name="hlp_Block22", type=hlp_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_IfStatement", type=hlp_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBlock23: BinaryAssociation = BinaryAssociation(
    name="elseBlock23",
    ends={
        Property(name="hlp_Block25", type=hlp_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_IfStatement24", type=hlp_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightHandSide15: BinaryAssociation = BinaryAssociation(
    name="rightHandSide15",
    ends={
        Property(name="hlp_Expression17", type=hlp_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_BinaryExpression16", type=hlp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableDeclarations34: BinaryAssociation = BinaryAssociation(
    name="variableDeclarations34",
    ends={
        Property(name="hlp_VariableDeclaration35", type=hlp_VariableDeclarationScope, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_VariableDeclarationScope", type=hlp_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block36: BinaryAssociation = BinaryAssociation(
    name="block36",
    ends={
        Property(name="hlp_Block37", type=hlp_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_Loop", type=hlp_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition26: BinaryAssociation = BinaryAssociation(
    name="condition26",
    ends={
        Property(name="hlp_Condition", type=hlp_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_IfStatement27", type=hlp_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide28: BinaryAssociation = BinaryAssociation(
    name="leftHandSide28",
    ends={
        Property(name="hlp_Expression30", type=hlp_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_Condition29", type=hlp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide31: BinaryAssociation = BinaryAssociation(
    name="rightHandSide31",
    ends={
        Property(name="hlp_Expression33", type=hlp_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_Condition32", type=hlp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableReference40: BinaryAssociation = BinaryAssociation(
    name="variableReference40",
    ends={
        Property(name="hlp_VariableReference41", type=hlp_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_ForLoop", type=hlp_VariableReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bound142: BinaryAssociation = BinaryAssociation(
    name="bound142",
    ends={
        Property(name="hlp_Expression44", type=hlp_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_ForLoop43", type=hlp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bound245: BinaryAssociation = BinaryAssociation(
    name="bound245",
    ends={
        Property(name="hlp_Expression47", type=hlp_ForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_ForLoop46", type=hlp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression48: BinaryAssociation = BinaryAssociation(
    name="expression48",
    ends={
        Property(name="hlp_Expression49", type=hlp_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_ExpressionStatement", type=hlp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition38: BinaryAssociation = BinaryAssociation(
    name="condition38",
    ends={
        Property(name="hlp_Condition39", type=hlp_ConditionalLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_ConditionalLoop", type=hlp_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
block52: BinaryAssociation = BinaryAssociation(
    name="block52",
    ends={
        Property(name="hlp_Block53", type=hlp_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_SynchronizedStatement", type=hlp_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variableReferences54: BinaryAssociation = BinaryAssociation(
    name="variableReferences54",
    ends={
        Property(name="hlp_VariableReference56", type=hlp_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_SynchronizedStatement55", type=hlp_VariableReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
block57: BinaryAssociation = BinaryAssociation(
    name="block57",
    ends={
        Property(name="hlp_Block59", type=hlp_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_Task58", type=hlp_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tasks60: BinaryAssociation = BinaryAssociation(
    name="tasks60",
    ends={
        Property(name="hlp_Task62", type=hlp_ScheduleInstruction, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_ScheduleInstruction61", type=hlp_Task, multiplicity=Multiplicity(1, 9999))
    }
)
expression50: BinaryAssociation = BinaryAssociation(
    name="expression50",
    ends={
        Property(name="hlp_Expression51", type=hlp_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="hlp_UnaryExpression", type=hlp_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_hlp_Variable_Nameable = Generalization(general=Nameable, specific=hlp_Variable)
gen_hlp_Assignment_Statement = Generalization(general=Statement, specific=hlp_Assignment)
gen_hlp_HighLevelProgram_VariableDeclarationScope = Generalization(general=VariableDeclarationScope, specific=hlp_HighLevelProgram)
gen_hlp_HighLevelProgram_Nameable = Generalization(general=Nameable, specific=hlp_HighLevelProgram)
gen_hlp_AddExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=hlp_AddExpression)
gen_hlp_VariableReference_AtomicExpression = Generalization(general=AtomicExpression, specific=hlp_VariableReference)
gen_hlp_AtomicExpression_Expression = Generalization(general=Expression, specific=hlp_AtomicExpression)
gen_hlp_BinaryExpression_Expression = Generalization(general=Expression, specific=hlp_BinaryExpression)
gen_hlp_LiteralValue_AtomicExpression = Generalization(general=AtomicExpression, specific=hlp_LiteralValue)
gen_hlp_IfStatement_Statement = Generalization(general=Statement, specific=hlp_IfStatement)
gen_hlp_SubtractExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=hlp_SubtractExpression)
gen_hlp_MultiplyExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=hlp_MultiplyExpression)
gen_hlp_DivideExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=hlp_DivideExpression)
gen_hlp_ParenthesisExpression_Expression = Generalization(general=Expression, specific=hlp_ParenthesisExpression)
gen_hlp_Loop_Statement = Generalization(general=Statement, specific=hlp_Loop)
gen_hlp_ExpressionStatement_Statement = Generalization(general=Statement, specific=hlp_ExpressionStatement)
gen_hlp_ConditionalLoop_Loop = Generalization(general=Loop, specific=hlp_ConditionalLoop)
gen_hlp_WhileLoop_ConditionalLoop = Generalization(general=ConditionalLoop, specific=hlp_WhileLoop)
gen_hlp_ForLoop_Loop = Generalization(general=Loop, specific=hlp_ForLoop)
gen_hlp_SynchronizedStatement_Statement = Generalization(general=Statement, specific=hlp_SynchronizedStatement)
gen_hlp_Task_VariableDeclarationScope = Generalization(general=VariableDeclarationScope, specific=hlp_Task)
gen_hlp_Task_Nameable = Generalization(general=Nameable, specific=hlp_Task)
gen_hlp_UnaryExpression_Expression = Generalization(general=Expression, specific=hlp_UnaryExpression)
gen_hlp_UnaryMinusExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=hlp_UnaryMinusExpression)
gen_hlp_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=hlp_ArithmeticExpression)

# Domain Model
domain_model = DomainModel(
    name="hlp",
    types={hlp_ScheduleInstruction, hlp_VariableDeclaration, hlp_Variable, hlp_Expression, hlp_Assignment, Statement, hlp_HighLevelProgram, VariableDeclarationScope, Nameable, hlp_Task, hlp_AddExpression, ArithmeticExpression, hlp_AtomicExpression, Expression, hlp_BinaryExpression, hlp_VariableReference, hlp_Statement, hlp_LiteralValue, AtomicExpression, hlp_Block, hlp_IfStatement, hlp_SubtractExpression, hlp_MultiplyExpression, hlp_DivideExpression, hlp_ParenthesisExpression, hlp_VariableDeclarationScope, hlp_Loop, hlp_Condition, hlp_ConditionalLoop, hlp_Nameable, hlp_ExpressionStatement, Loop, hlp_WhileLoop, ConditionalLoop, hlp_ForLoop, hlp_UnaryExpression, hlp_UnaryMinusExpression, UnaryExpression, hlp_ArithmeticExpression, BinaryExpression, hlp_SynchronizedStatement, ComparisonOperator},
    associations={scheduleInstruction1, variable3, initialValue4, tasks0, variable10, leftHandSide13, leftHandSide6, rightHandSide7, operand18, statements20, thenBlock21, elseBlock23, rightHandSide15, variableDeclarations34, block36, condition26, leftHandSide28, rightHandSide31, variableReference40, bound142, bound245, expression48, condition38, block52, variableReferences54, block57, tasks60, expression50},
    generalizations={gen_hlp_Variable_Nameable, gen_hlp_Assignment_Statement, gen_hlp_HighLevelProgram_VariableDeclarationScope, gen_hlp_HighLevelProgram_Nameable, gen_hlp_AddExpression_ArithmeticExpression, gen_hlp_VariableReference_AtomicExpression, gen_hlp_AtomicExpression_Expression, gen_hlp_BinaryExpression_Expression, gen_hlp_LiteralValue_AtomicExpression, gen_hlp_IfStatement_Statement, gen_hlp_SubtractExpression_ArithmeticExpression, gen_hlp_MultiplyExpression_ArithmeticExpression, gen_hlp_DivideExpression_ArithmeticExpression, gen_hlp_ParenthesisExpression_Expression, gen_hlp_Loop_Statement, gen_hlp_ExpressionStatement_Statement, gen_hlp_ConditionalLoop_Loop, gen_hlp_WhileLoop_ConditionalLoop, gen_hlp_ForLoop_Loop, gen_hlp_SynchronizedStatement_Statement, gen_hlp_Task_VariableDeclarationScope, gen_hlp_Task_Nameable, gen_hlp_UnaryExpression_Expression, gen_hlp_UnaryMinusExpression_UnaryExpression, gen_hlp_ArithmeticExpression_BinaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)