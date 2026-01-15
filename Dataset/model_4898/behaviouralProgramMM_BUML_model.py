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
behaviouralProgramMM_FunctionCall = Class(name="behaviouralProgramMM::FunctionCall")
Expression = Class(name="Expression")
behaviouralProgramMM_Instantiation = Class(name="behaviouralProgramMM::Instantiation")
behaviouralProgramMM_Behaviour = Class(name="behaviouralProgramMM::Behaviour")
behaviouralProgramMM_Function = Class(name="behaviouralProgramMM::Function")
behaviouralProgramMM_Statement = Class(name="behaviouralProgramMM::Statement", is_abstract=True)
behaviouralProgramMM_Assignment = Class(name="behaviouralProgramMM::Assignment")
Statement = Class(name="Statement")
behaviouralProgramMM_Expression = Class(name="behaviouralProgramMM::Expression", is_abstract=True)
behaviouralProgramMM_ConditionalBranch = Class(name="behaviouralProgramMM::ConditionalBranch")
behaviouralProgramMM_Loop = Class(name="behaviouralProgramMM::Loop")
behaviouralProgramMM_Literal = Class(name="behaviouralProgramMM::Literal")
behaviouralProgramMM_BinaryOperator = Class(name="behaviouralProgramMM::BinaryOperator", is_abstract=True)
behaviouralProgramMM_Return = Class(name="behaviouralProgramMM::Return")
behaviouralProgramMM_TryCatch = Class(name="behaviouralProgramMM::TryCatch")
behaviouralProgramMM_RaiseException = Class(name="behaviouralProgramMM::RaiseException")
behaviouralProgramMM_ReadLine = Class(name="behaviouralProgramMM::ReadLine")
behaviouralProgramMM_ArithmeticInfixOperator = Class(name="behaviouralProgramMM::ArithmeticInfixOperator", is_abstract=True)
BinaryOperator = Class(name="BinaryOperator")
behaviouralProgramMM_Plus = Class(name="behaviouralProgramMM::Plus")
ArithmeticInfixOperator = Class(name="ArithmeticInfixOperator")
behaviouralProgramMM_FunctionCallStatement = Class(name="behaviouralProgramMM::FunctionCallStatement")
behaviouralProgramMM_ReadLineStatement = Class(name="behaviouralProgramMM::ReadLineStatement")
FunctionCallStatement = Class(name="FunctionCallStatement")
behaviouralProgramMM_WriteLineStatement = Class(name="behaviouralProgramMM::WriteLineStatement")
behaviouralProgramMM_ComparsionOperator = Class(name="behaviouralProgramMM::ComparsionOperator", is_abstract=True)
behaviouralProgramMM_Equals = Class(name="behaviouralProgramMM::Equals")
ComparsionOperator = Class(name="ComparsionOperator")
behaviouralProgramMM_Variable = Class(name="behaviouralProgramMM::Variable")

# behaviouralProgramMM_FunctionCall class attributes and methods
behaviouralProgramMM_FunctionCall_FuncName: Property = Property(name="FuncName", type=StringType)
behaviouralProgramMM_FunctionCall.attributes={behaviouralProgramMM_FunctionCall_FuncName}

# Expression class attributes and methods

# behaviouralProgramMM_Instantiation class attributes and methods
behaviouralProgramMM_Instantiation_VarName: Property = Property(name="VarName", type=StringType)
behaviouralProgramMM_Instantiation_VarType: Property = Property(name="VarType", type=StringType)
behaviouralProgramMM_Instantiation.attributes={behaviouralProgramMM_Instantiation_VarType, behaviouralProgramMM_Instantiation_VarName}

# behaviouralProgramMM_Behaviour class attributes and methods

# behaviouralProgramMM_Function class attributes and methods
behaviouralProgramMM_Function_Name: Property = Property(name="Name", type=StringType)
behaviouralProgramMM_Function.attributes={behaviouralProgramMM_Function_Name}

# behaviouralProgramMM_Statement class attributes and methods

# behaviouralProgramMM_Assignment class attributes and methods
behaviouralProgramMM_Assignment_VariableName: Property = Property(name="VariableName", type=StringType)
behaviouralProgramMM_Assignment.attributes={behaviouralProgramMM_Assignment_VariableName}

# Statement class attributes and methods

# behaviouralProgramMM_Expression class attributes and methods

# behaviouralProgramMM_ConditionalBranch class attributes and methods

# behaviouralProgramMM_Loop class attributes and methods

# behaviouralProgramMM_Literal class attributes and methods
behaviouralProgramMM_Literal_Value: Property = Property(name="Value", type=StringType)
behaviouralProgramMM_Literal.attributes={behaviouralProgramMM_Literal_Value}

# behaviouralProgramMM_BinaryOperator class attributes and methods

# behaviouralProgramMM_Return class attributes and methods

# behaviouralProgramMM_TryCatch class attributes and methods

# behaviouralProgramMM_RaiseException class attributes and methods

# behaviouralProgramMM_ReadLine class attributes and methods

# behaviouralProgramMM_ArithmeticInfixOperator class attributes and methods

# BinaryOperator class attributes and methods

# behaviouralProgramMM_Plus class attributes and methods

# ArithmeticInfixOperator class attributes and methods

# behaviouralProgramMM_FunctionCallStatement class attributes and methods
behaviouralProgramMM_FunctionCallStatement_FuncName: Property = Property(name="FuncName", type=StringType)
behaviouralProgramMM_FunctionCallStatement.attributes={behaviouralProgramMM_FunctionCallStatement_FuncName}

# behaviouralProgramMM_ReadLineStatement class attributes and methods

# FunctionCallStatement class attributes and methods

# behaviouralProgramMM_WriteLineStatement class attributes and methods

# behaviouralProgramMM_ComparsionOperator class attributes and methods

# behaviouralProgramMM_Equals class attributes and methods

# ComparsionOperator class attributes and methods

# behaviouralProgramMM_Variable class attributes and methods
behaviouralProgramMM_Variable_VarName: Property = Property(name="VarName", type=StringType)
behaviouralProgramMM_Variable.attributes={behaviouralProgramMM_Variable_VarName}

# Relationships
loopstatements15: BinaryAssociation = BinaryAssociation(
    name="loopstatements15",
    ends={
        Property(name="behaviouralProgramMM_Statement16", type=behaviouralProgramMM_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_Loop", type=behaviouralProgramMM_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loopexpression17: BinaryAssociation = BinaryAssociation(
    name="loopexpression17",
    ends={
        Property(name="behaviouralProgramMM_Expression19", type=behaviouralProgramMM_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_Loop18", type=behaviouralProgramMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments20: BinaryAssociation = BinaryAssociation(
    name="arguments20",
    ends={
        Property(name="behaviouralProgramMM_Expression21", type=behaviouralProgramMM_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_FunctionCall", type=behaviouralProgramMM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions0: BinaryAssociation = BinaryAssociation(
    name="functions0",
    ends={
        Property(name="behaviouralProgramMM_Function", type=behaviouralProgramMM_Behaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_Behaviour", type=behaviouralProgramMM_Function, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
startfunction1: BinaryAssociation = BinaryAssociation(
    name="startfunction1",
    ends={
        Property(name="behaviouralProgramMM_Function3", type=behaviouralProgramMM_Behaviour, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_Behaviour2", type=behaviouralProgramMM_Function, multiplicity=Multiplicity(1, 1))
    }
)
functionBody4: BinaryAssociation = BinaryAssociation(
    name="functionBody4",
    ends={
        Property(name="behaviouralProgramMM_Statement", type=behaviouralProgramMM_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_Function5", type=behaviouralProgramMM_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignexpression6: BinaryAssociation = BinaryAssociation(
    name="assignexpression6",
    ends={
        Property(name="behaviouralProgramMM_Expression", type=behaviouralProgramMM_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_Assignment", type=behaviouralProgramMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Ifstatements7: BinaryAssociation = BinaryAssociation(
    name="Ifstatements7",
    ends={
        Property(name="behaviouralProgramMM_Statement8", type=behaviouralProgramMM_ConditionalBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_ConditionalBranch", type=behaviouralProgramMM_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsestatements9: BinaryAssociation = BinaryAssociation(
    name="elsestatements9",
    ends={
        Property(name="behaviouralProgramMM_Statement11", type=behaviouralProgramMM_ConditionalBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_ConditionalBranch10", type=behaviouralProgramMM_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ifexpression12: BinaryAssociation = BinaryAssociation(
    name="ifexpression12",
    ends={
        Property(name="behaviouralProgramMM_Expression14", type=behaviouralProgramMM_ConditionalBranch, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_ConditionalBranch13", type=behaviouralProgramMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftSide35: BinaryAssociation = BinaryAssociation(
    name="leftSide35",
    ends={
        Property(name="behaviouralProgramMM_Expression36", type=behaviouralProgramMM_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_BinaryOperator", type=behaviouralProgramMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightSide37: BinaryAssociation = BinaryAssociation(
    name="rightSide37",
    ends={
        Property(name="behaviouralProgramMM_Expression39", type=behaviouralProgramMM_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_BinaryOperator38", type=behaviouralProgramMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
InitiationExpression22: BinaryAssociation = BinaryAssociation(
    name="InitiationExpression22",
    ends={
        Property(name="behaviouralProgramMM_Expression23", type=behaviouralProgramMM_Instantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_Instantiation", type=behaviouralProgramMM_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression24: BinaryAssociation = BinaryAssociation(
    name="expression24",
    ends={
        Property(name="behaviouralProgramMM_Expression25", type=behaviouralProgramMM_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_Return", type=behaviouralProgramMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catch26: BinaryAssociation = BinaryAssociation(
    name="catch26",
    ends={
        Property(name="behaviouralProgramMM_Statement27", type=behaviouralProgramMM_TryCatch, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_TryCatch", type=behaviouralProgramMM_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
try28: BinaryAssociation = BinaryAssociation(
    name="try28",
    ends={
        Property(name="behaviouralProgramMM_Statement30", type=behaviouralProgramMM_TryCatch, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_TryCatch29", type=behaviouralProgramMM_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression31: BinaryAssociation = BinaryAssociation(
    name="expression31",
    ends={
        Property(name="behaviouralProgramMM_Expression32", type=behaviouralProgramMM_RaiseException, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_RaiseException", type=behaviouralProgramMM_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments33: BinaryAssociation = BinaryAssociation(
    name="arguments33",
    ends={
        Property(name="behaviouralProgramMM_Expression34", type=behaviouralProgramMM_FunctionCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="behaviouralProgramMM_FunctionCallStatement", type=behaviouralProgramMM_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_behaviouralProgramMM_FunctionCall_Expression = Generalization(general=Expression, specific=behaviouralProgramMM_FunctionCall)
gen_behaviouralProgramMM_Instantiation_Statement = Generalization(general=Statement, specific=behaviouralProgramMM_Instantiation)
gen_behaviouralProgramMM_Assignment_Statement = Generalization(general=Statement, specific=behaviouralProgramMM_Assignment)
gen_behaviouralProgramMM_ConditionalBranch_Statement = Generalization(general=Statement, specific=behaviouralProgramMM_ConditionalBranch)
gen_behaviouralProgramMM_Loop_Statement = Generalization(general=Statement, specific=behaviouralProgramMM_Loop)
gen_behaviouralProgramMM_Literal_Expression = Generalization(general=Expression, specific=behaviouralProgramMM_Literal)
gen_behaviouralProgramMM_BinaryOperator_Expression = Generalization(general=Expression, specific=behaviouralProgramMM_BinaryOperator)
gen_behaviouralProgramMM_Return_Statement = Generalization(general=Statement, specific=behaviouralProgramMM_Return)
gen_behaviouralProgramMM_TryCatch_Statement = Generalization(general=Statement, specific=behaviouralProgramMM_TryCatch)
gen_behaviouralProgramMM_RaiseException_Statement = Generalization(general=Statement, specific=behaviouralProgramMM_RaiseException)
gen_behaviouralProgramMM_ReadLine_Expression = Generalization(general=Expression, specific=behaviouralProgramMM_ReadLine)
gen_behaviouralProgramMM_ArithmeticInfixOperator_BinaryOperator = Generalization(general=BinaryOperator, specific=behaviouralProgramMM_ArithmeticInfixOperator)
gen_behaviouralProgramMM_Plus_ArithmeticInfixOperator = Generalization(general=ArithmeticInfixOperator, specific=behaviouralProgramMM_Plus)
gen_behaviouralProgramMM_FunctionCallStatement_Statement = Generalization(general=Statement, specific=behaviouralProgramMM_FunctionCallStatement)
gen_behaviouralProgramMM_ReadLineStatement_FunctionCallStatement = Generalization(general=FunctionCallStatement, specific=behaviouralProgramMM_ReadLineStatement)
gen_behaviouralProgramMM_WriteLineStatement_FunctionCallStatement = Generalization(general=FunctionCallStatement, specific=behaviouralProgramMM_WriteLineStatement)
gen_behaviouralProgramMM_ComparsionOperator_BinaryOperator = Generalization(general=BinaryOperator, specific=behaviouralProgramMM_ComparsionOperator)
gen_behaviouralProgramMM_Equals_ComparsionOperator = Generalization(general=ComparsionOperator, specific=behaviouralProgramMM_Equals)
gen_behaviouralProgramMM_Variable_Expression = Generalization(general=Expression, specific=behaviouralProgramMM_Variable)

# Domain Model
domain_model = DomainModel(
    name="behaviouralProgramMM",
    types={behaviouralProgramMM_FunctionCall, Expression, behaviouralProgramMM_Instantiation, behaviouralProgramMM_Behaviour, behaviouralProgramMM_Function, behaviouralProgramMM_Statement, behaviouralProgramMM_Assignment, Statement, behaviouralProgramMM_Expression, behaviouralProgramMM_ConditionalBranch, behaviouralProgramMM_Loop, behaviouralProgramMM_Literal, behaviouralProgramMM_BinaryOperator, behaviouralProgramMM_Return, behaviouralProgramMM_TryCatch, behaviouralProgramMM_RaiseException, behaviouralProgramMM_ReadLine, behaviouralProgramMM_ArithmeticInfixOperator, BinaryOperator, behaviouralProgramMM_Plus, ArithmeticInfixOperator, behaviouralProgramMM_FunctionCallStatement, behaviouralProgramMM_ReadLineStatement, FunctionCallStatement, behaviouralProgramMM_WriteLineStatement, behaviouralProgramMM_ComparsionOperator, behaviouralProgramMM_Equals, ComparsionOperator, behaviouralProgramMM_Variable},
    associations={loopstatements15, loopexpression17, arguments20, functions0, startfunction1, functionBody4, assignexpression6, Ifstatements7, elsestatements9, ifexpression12, leftSide35, rightSide37, InitiationExpression22, expression24, catch26, try28, expression31, arguments33},
    generalizations={gen_behaviouralProgramMM_FunctionCall_Expression, gen_behaviouralProgramMM_Instantiation_Statement, gen_behaviouralProgramMM_Assignment_Statement, gen_behaviouralProgramMM_ConditionalBranch_Statement, gen_behaviouralProgramMM_Loop_Statement, gen_behaviouralProgramMM_Literal_Expression, gen_behaviouralProgramMM_BinaryOperator_Expression, gen_behaviouralProgramMM_Return_Statement, gen_behaviouralProgramMM_TryCatch_Statement, gen_behaviouralProgramMM_RaiseException_Statement, gen_behaviouralProgramMM_ReadLine_Expression, gen_behaviouralProgramMM_ArithmeticInfixOperator_BinaryOperator, gen_behaviouralProgramMM_Plus_ArithmeticInfixOperator, gen_behaviouralProgramMM_FunctionCallStatement_Statement, gen_behaviouralProgramMM_ReadLineStatement_FunctionCallStatement, gen_behaviouralProgramMM_WriteLineStatement_FunctionCallStatement, gen_behaviouralProgramMM_ComparsionOperator_BinaryOperator, gen_behaviouralProgramMM_Equals_ComparsionOperator, gen_behaviouralProgramMM_Variable_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)