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
behaviour_Behaviour = Class(name="behaviour::Behaviour")
behaviour_Function = Class(name="behaviour::Function")
behaviour_Statement = Class(name="behaviour::Statement", is_abstract=True)
behaviour_CondionalStatement = Class(name="behaviour::CondionalStatement")
Statement = Class(name="Statement")
behaviour_Expression = Class(name="behaviour::Expression", is_abstract=True)
behaviour_LoopStatement = Class(name="behaviour::LoopStatement")
behaviour_CallFunctionStatement = Class(name="behaviour::CallFunctionStatement")
behaviour_TryCatchStatement = Class(name="behaviour::TryCatchStatement")
behaviour_ExceptionStatement = Class(name="behaviour::ExceptionStatement")
behaviour_Literal = Class(name="behaviour::Literal")
Expression = Class(name="Expression")
behaviour_Variable = Class(name="behaviour::Variable")
behaviour_FunctionCall = Class(name="behaviour::FunctionCall")
behaviour_ReadLine = Class(name="behaviour::ReadLine")
behaviour_BinaryExpression = Class(name="behaviour::BinaryExpression", is_abstract=True)
behaviour_AssignmentStatement = Class(name="behaviour::AssignmentStatement")
behaviour_DeclarationStatement = Class(name="behaviour::DeclarationStatement")
behaviour_ReturnStatement = Class(name="behaviour::ReturnStatement")
behaviour_ArithmeticOperation = Class(name="behaviour::ArithmeticOperation", is_abstract=True)
BinaryExpression = Class(name="BinaryExpression")
behaviour_ComparisonOperator = Class(name="behaviour::ComparisonOperator", is_abstract=True)
behaviour_Plus = Class(name="behaviour::Plus")
ArithmeticOperation = Class(name="ArithmeticOperation")
behaviour_Equals = Class(name="behaviour::Equals")
ComparisonOperator = Class(name="ComparisonOperator")

# behaviour_Behaviour class attributes and methods

# behaviour_Function class attributes and methods
behaviour_Function_name: Property = Property(name="name", type=StringType)
behaviour_Function.attributes={behaviour_Function_name}

# behaviour_Statement class attributes and methods

# behaviour_CondionalStatement class attributes and methods

# Statement class attributes and methods

# behaviour_Expression class attributes and methods

# behaviour_LoopStatement class attributes and methods

# behaviour_CallFunctionStatement class attributes and methods
behaviour_CallFunctionStatement_nameFunc: Property = Property(name="nameFunc", type=StringType)
behaviour_CallFunctionStatement.attributes={behaviour_CallFunctionStatement_nameFunc}

# behaviour_TryCatchStatement class attributes and methods

# behaviour_ExceptionStatement class attributes and methods

# behaviour_Literal class attributes and methods
behaviour_Literal_vlaue: Property = Property(name="vlaue", type=StringType)
behaviour_Literal.attributes={behaviour_Literal_vlaue}

# Expression class attributes and methods

# behaviour_Variable class attributes and methods
behaviour_Variable_varName: Property = Property(name="varName", type=StringType)
behaviour_Variable.attributes={behaviour_Variable_varName}

# behaviour_FunctionCall class attributes and methods
behaviour_FunctionCall_funcName: Property = Property(name="funcName", type=StringType)
behaviour_FunctionCall.attributes={behaviour_FunctionCall_funcName}

# behaviour_ReadLine class attributes and methods

# behaviour_BinaryExpression class attributes and methods

# behaviour_AssignmentStatement class attributes and methods
behaviour_AssignmentStatement_varName: Property = Property(name="varName", type=StringType)
behaviour_AssignmentStatement.attributes={behaviour_AssignmentStatement_varName}

# behaviour_DeclarationStatement class attributes and methods
behaviour_DeclarationStatement_varName: Property = Property(name="varName", type=StringType)
behaviour_DeclarationStatement_varType: Property = Property(name="varType", type=StringType)
behaviour_DeclarationStatement.attributes={behaviour_DeclarationStatement_varType, behaviour_DeclarationStatement_varName}

# behaviour_ReturnStatement class attributes and methods

# behaviour_ArithmeticOperation class attributes and methods

# BinaryExpression class attributes and methods

# behaviour_ComparisonOperator class attributes and methods

# behaviour_Plus class attributes and methods

# ArithmeticOperation class attributes and methods

# behaviour_Equals class attributes and methods

# ComparisonOperator class attributes and methods

# Relationships
functions0: BinaryAssociation = BinaryAssociation(
    name="functions0",
    ends={
        Property(name="behaviour_Function", type=behaviour_Behaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Behaviour", type=behaviour_Function, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entryFunction1: BinaryAssociation = BinaryAssociation(
    name="entryFunction1",
    ends={
        Property(name="behaviour_Function3", type=behaviour_Behaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Behaviour2", type=behaviour_Function, multiplicity=Multiplicity(1, 1))
    }
)
functionBody4: BinaryAssociation = BinaryAssociation(
    name="functionBody4",
    ends={
        Property(name="behaviour_Statement", type=behaviour_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_Function5", type=behaviour_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifStatements6: BinaryAssociation = BinaryAssociation(
    name="ifStatements6",
    ends={
        Property(name="behaviour_Statement7", type=behaviour_CondionalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_CondionalStatement", type=behaviour_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements8: BinaryAssociation = BinaryAssociation(
    name="elseStatements8",
    ends={
        Property(name="behaviour_Statement10", type=behaviour_CondionalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_CondionalStatement9", type=behaviour_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifExpression11: BinaryAssociation = BinaryAssociation(
    name="ifExpression11",
    ends={
        Property(name="behaviour_Expression", type=behaviour_CondionalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_CondionalStatement12", type=behaviour_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loopExpression13: BinaryAssociation = BinaryAssociation(
    name="loopExpression13",
    ends={
        Property(name="behaviour_Expression14", type=behaviour_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_LoopStatement", type=behaviour_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnExpression22: BinaryAssociation = BinaryAssociation(
    name="returnExpression22",
    ends={
        Property(name="behaviour_Expression23", type=behaviour_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_ReturnStatement", type=behaviour_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments24: BinaryAssociation = BinaryAssociation(
    name="arguments24",
    ends={
        Property(name="behaviour_Expression25", type=behaviour_CallFunctionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_CallFunctionStatement", type=behaviour_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tryStatements26: BinaryAssociation = BinaryAssociation(
    name="tryStatements26",
    ends={
        Property(name="behaviour_Statement27", type=behaviour_TryCatchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TryCatchStatement", type=behaviour_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchStatements28: BinaryAssociation = BinaryAssociation(
    name="catchStatements28",
    ends={
        Property(name="behaviour_Statement30", type=behaviour_TryCatchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_TryCatchStatement29", type=behaviour_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
throwsExpression31: BinaryAssociation = BinaryAssociation(
    name="throwsExpression31",
    ends={
        Property(name="behaviour_Expression32", type=behaviour_ExceptionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_ExceptionStatement", type=behaviour_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments33: BinaryAssociation = BinaryAssociation(
    name="arguments33",
    ends={
        Property(name="behaviour_Expression34", type=behaviour_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_FunctionCall", type=behaviour_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopBodyStatements15: BinaryAssociation = BinaryAssociation(
    name="loopBodyStatements15",
    ends={
        Property(name="behaviour_Statement17", type=behaviour_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_LoopStatement16", type=behaviour_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignExpression18: BinaryAssociation = BinaryAssociation(
    name="assignExpression18",
    ends={
        Property(name="behaviour_Expression19", type=behaviour_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_AssignmentStatement", type=behaviour_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialExpression20: BinaryAssociation = BinaryAssociation(
    name="initialExpression20",
    ends={
        Property(name="behaviour_Expression21", type=behaviour_DeclarationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_DeclarationStatement", type=behaviour_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftSideExpression35: BinaryAssociation = BinaryAssociation(
    name="leftSideExpression35",
    ends={
        Property(name="behaviour_Expression36", type=behaviour_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_BinaryExpression", type=behaviour_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightSideExpression37: BinaryAssociation = BinaryAssociation(
    name="rightSideExpression37",
    ends={
        Property(name="behaviour_Expression39", type=behaviour_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviour_BinaryExpression38", type=behaviour_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_behaviour_CondionalStatement_Statement = Generalization(general=Statement, specific=behaviour_CondionalStatement)
gen_behaviour_LoopStatement_Statement = Generalization(general=Statement, specific=behaviour_LoopStatement)
gen_behaviour_ReturnStatement_Statement = Generalization(general=Statement, specific=behaviour_ReturnStatement)
gen_behaviour_CallFunctionStatement_Statement = Generalization(general=Statement, specific=behaviour_CallFunctionStatement)
gen_behaviour_TryCatchStatement_Statement = Generalization(general=Statement, specific=behaviour_TryCatchStatement)
gen_behaviour_ExceptionStatement_Statement = Generalization(general=Statement, specific=behaviour_ExceptionStatement)
gen_behaviour_Literal_Expression = Generalization(general=Expression, specific=behaviour_Literal)
gen_behaviour_Variable_Expression = Generalization(general=Expression, specific=behaviour_Variable)
gen_behaviour_FunctionCall_Expression = Generalization(general=Expression, specific=behaviour_FunctionCall)
gen_behaviour_ReadLine_Expression = Generalization(general=Expression, specific=behaviour_ReadLine)
gen_behaviour_BinaryExpression_Expression = Generalization(general=Expression, specific=behaviour_BinaryExpression)
gen_behaviour_AssignmentStatement_Statement = Generalization(general=Statement, specific=behaviour_AssignmentStatement)
gen_behaviour_DeclarationStatement_Statement = Generalization(general=Statement, specific=behaviour_DeclarationStatement)
gen_behaviour_ArithmeticOperation_BinaryExpression = Generalization(general=BinaryExpression, specific=behaviour_ArithmeticOperation)
gen_behaviour_ComparisonOperator_BinaryExpression = Generalization(general=BinaryExpression, specific=behaviour_ComparisonOperator)
gen_behaviour_Plus_ArithmeticOperation = Generalization(general=ArithmeticOperation, specific=behaviour_Plus)
gen_behaviour_Equals_ComparisonOperator = Generalization(general=ComparisonOperator, specific=behaviour_Equals)

# Domain Model
domain_model = DomainModel(
    name="behaviour",
    types={behaviour_Behaviour, behaviour_Function, behaviour_Statement, behaviour_CondionalStatement, Statement, behaviour_Expression, behaviour_LoopStatement, behaviour_CallFunctionStatement, behaviour_TryCatchStatement, behaviour_ExceptionStatement, behaviour_Literal, Expression, behaviour_Variable, behaviour_FunctionCall, behaviour_ReadLine, behaviour_BinaryExpression, behaviour_AssignmentStatement, behaviour_DeclarationStatement, behaviour_ReturnStatement, behaviour_ArithmeticOperation, BinaryExpression, behaviour_ComparisonOperator, behaviour_Plus, ArithmeticOperation, behaviour_Equals, ComparisonOperator},
    associations={functions0, entryFunction1, functionBody4, ifStatements6, elseStatements8, ifExpression11, loopExpression13, returnExpression22, arguments24, tryStatements26, catchStatements28, throwsExpression31, arguments33, loopBodyStatements15, assignExpression18, initialExpression20, leftSideExpression35, rightSideExpression37},
    generalizations={gen_behaviour_CondionalStatement_Statement, gen_behaviour_LoopStatement_Statement, gen_behaviour_ReturnStatement_Statement, gen_behaviour_CallFunctionStatement_Statement, gen_behaviour_TryCatchStatement_Statement, gen_behaviour_ExceptionStatement_Statement, gen_behaviour_Literal_Expression, gen_behaviour_Variable_Expression, gen_behaviour_FunctionCall_Expression, gen_behaviour_ReadLine_Expression, gen_behaviour_BinaryExpression_Expression, gen_behaviour_AssignmentStatement_Statement, gen_behaviour_DeclarationStatement_Statement, gen_behaviour_ArithmeticOperation_BinaryExpression, gen_behaviour_ComparisonOperator_BinaryExpression, gen_behaviour_Plus_ArithmeticOperation, gen_behaviour_Equals_ComparisonOperator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)