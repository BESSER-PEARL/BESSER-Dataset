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
codemodel_CMElement = Class(name="codemodel::CMElement", is_abstract=True)
codemodel_CodeModule = Class(name="codemodel::CodeModule")
CMElement = Class(name="CMElement")
codemodel_GlobalVariable = Class(name="codemodel::GlobalVariable")
codemodel_Function = Class(name="codemodel::Function")
codemodel_DataType = Class(name="codemodel::DataType", is_abstract=True)
codemodel_Variable = Class(name="codemodel::Variable", is_abstract=True)
codemodel_FunctionArgument = Class(name="codemodel::FunctionArgument")
codemodel_LocalVariable = Class(name="codemodel::LocalVariable")
Statement = Class(name="Statement")
Variable = Class(name="Variable")
codemodel_MatrixType = Class(name="codemodel::MatrixType")
DataType = Class(name="DataType")
codemodel_VectorType = Class(name="codemodel::VectorType")
codemodel_ScalarType = Class(name="codemodel::ScalarType")
codemodel_expressions_Expression = Class(name="codemodel::expressions::Expression", is_abstract=True)
codemodel_expressions_VariableExp = Class(name="codemodel::expressions::VariableExp")
Expression = Class(name="Expression")
expressions_codemodel_Variable = Class(name="expressions::codemodel::Variable")
codemodel_expressions_BinaryExp = Class(name="codemodel::expressions::BinaryExp")
codemodel_expressions_LiteralExp = Class(name="codemodel::expressions::LiteralExp")
codemodel_statements_Statement = Class(name="codemodel::statements::Statement", is_abstract=True)
codemodel_statements_AssignmentStmt = Class(name="codemodel::statements::AssignmentStmt")
codemodel_statements_CompositeStmt = Class(name="codemodel::statements::CompositeStmt")
codemodel_statements_IfStmt = Class(name="codemodel::statements::IfStmt")
codemodel_statements_ForStmt = Class(name="codemodel::statements::ForStmt")
AssignmentStmt = Class(name="AssignmentStmt")

# codemodel_CMElement class attributes and methods
codemodel_CMElement_name: Property = Property(name="name", type=StringType)
codemodel_CMElement.attributes={codemodel_CMElement_name}

# codemodel_CodeModule class attributes and methods

# CMElement class attributes and methods

# codemodel_GlobalVariable class attributes and methods

# codemodel_Function class attributes and methods
codemodel_Function_identifier: Property = Property(name="identifier", type=StringType)
codemodel_Function.attributes={codemodel_Function_identifier}

# codemodel_DataType class attributes and methods
codemodel_DataType_basetype: Property = Property(name="basetype", type=StringType)
codemodel_DataType.attributes={codemodel_DataType_basetype}

# codemodel_Variable class attributes and methods
codemodel_Variable_constant: Property = Property(name="constant", type=BooleanType)
codemodel_Variable_identifier: Property = Property(name="identifier", type=StringType)
codemodel_Variable.attributes={codemodel_Variable_constant, codemodel_Variable_identifier}

# codemodel_FunctionArgument class attributes and methods

# codemodel_LocalVariable class attributes and methods

# Statement class attributes and methods

# Variable class attributes and methods

# codemodel_MatrixType class attributes and methods
codemodel_MatrixType_rows: Property = Property(name="rows", type=StringType)
codemodel_MatrixType_columns: Property = Property(name="columns", type=StringType)
codemodel_MatrixType.attributes={codemodel_MatrixType_columns, codemodel_MatrixType_rows}

# DataType class attributes and methods

# codemodel_VectorType class attributes and methods
codemodel_VectorType_size: Property = Property(name="size", type=StringType)
codemodel_VectorType.attributes={codemodel_VectorType_size}

# codemodel_ScalarType class attributes and methods

# codemodel_expressions_Expression class attributes and methods

# codemodel_expressions_VariableExp class attributes and methods

# Expression class attributes and methods

# expressions_codemodel_Variable class attributes and methods

# codemodel_expressions_BinaryExp class attributes and methods
codemodel_expressions_BinaryExp_operator: Property = Property(name="operator", type=StringType)
codemodel_expressions_BinaryExp.attributes={codemodel_expressions_BinaryExp_operator}

# codemodel_expressions_LiteralExp class attributes and methods
codemodel_expressions_LiteralExp_value: Property = Property(name="value", type=StringType)
codemodel_expressions_LiteralExp.attributes={codemodel_expressions_LiteralExp_value}

# codemodel_statements_Statement class attributes and methods

# codemodel_statements_AssignmentStmt class attributes and methods

# codemodel_statements_CompositeStmt class attributes and methods

# codemodel_statements_IfStmt class attributes and methods

# codemodel_statements_ForStmt class attributes and methods

# AssignmentStmt class attributes and methods

# Relationships
globalVariables0: BinaryAssociation = BinaryAssociation(
    name="globalVariables0",
    ends={
        Property(name="codemodel_GlobalVariable", type=codemodel_CodeModule, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_CodeModule", type=codemodel_GlobalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions1: BinaryAssociation = BinaryAssociation(
    name="functions1",
    ends={
        Property(name="codemodel_Function", type=codemodel_CodeModule, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_CodeModule2", type=codemodel_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes3: BinaryAssociation = BinaryAssociation(
    name="dataTypes3",
    ends={
        Property(name="codemodel_DataType", type=codemodel_CodeModule, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_CodeModule4", type=codemodel_DataType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="codemodel_DataType6", type=codemodel_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_Variable", type=codemodel_DataType, multiplicity=Multiplicity(1, 1))
    }
)
arguments7: BinaryAssociation = BinaryAssociation(
    name="arguments7",
    ends={
        Property(name="codemodel_FunctionArgument", type=codemodel_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_Function8", type=codemodel_FunctionArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVariables9: BinaryAssociation = BinaryAssociation(
    name="localVariables9",
    ends={
        Property(name="codemodel_LocalVariable", type=codemodel_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_Function10", type=codemodel_LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body11: BinaryAssociation = BinaryAssociation(
    name="body11",
    ends={
        Property(name="Statement", type=codemodel_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_Function12", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedVariable13: BinaryAssociation = BinaryAssociation(
    name="referencedVariable13",
    ends={
        Property(name="expressions_codemodel_Variable", type=codemodel_expressions_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_expressions_VariableExp", type=expressions_codemodel_Variable, multiplicity=Multiplicity(1, 1))
    }
)
left14: BinaryAssociation = BinaryAssociation(
    name="left14",
    ends={
        Property(name="Expression", type=codemodel_expressions_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_expressions_BinaryExp", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right15: BinaryAssociation = BinaryAssociation(
    name="right15",
    ends={
        Property(name="Expression17", type=codemodel_expressions_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_expressions_BinaryExp16", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExp20: BinaryAssociation = BinaryAssociation(
    name="rightExp20",
    ends={
        Property(name="Expression22", type=codemodel_statements_AssignmentStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_AssignmentStmt21", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements23: BinaryAssociation = BinaryAssociation(
    name="statements23",
    ends={
        Property(name="Statement24", type=codemodel_statements_CompositeStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_CompositeStmt", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition25: BinaryAssociation = BinaryAssociation(
    name="condition25",
    ends={
        Property(name="Expression26", type=codemodel_statements_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_IfStmt", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStmt27: BinaryAssociation = BinaryAssociation(
    name="thenStmt27",
    ends={
        Property(name="Statement29", type=codemodel_statements_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_IfStmt28", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStmt30: BinaryAssociation = BinaryAssociation(
    name="elseStmt30",
    ends={
        Property(name="Statement32", type=codemodel_statements_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_IfStmt31", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init33: BinaryAssociation = BinaryAssociation(
    name="init33",
    ends={
        Property(name="AssignmentStmt", type=codemodel_statements_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_ForStmt", type=AssignmentStmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition34: BinaryAssociation = BinaryAssociation(
    name="condition34",
    ends={
        Property(name="Expression36", type=codemodel_statements_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_ForStmt35", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
increment37: BinaryAssociation = BinaryAssociation(
    name="increment37",
    ends={
        Property(name="Expression39", type=codemodel_statements_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_ForStmt38", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
forStmt40: BinaryAssociation = BinaryAssociation(
    name="forStmt40",
    ends={
        Property(name="Statement42", type=codemodel_statements_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_ForStmt41", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftExp18: BinaryAssociation = BinaryAssociation(
    name="leftExp18",
    ends={
        Property(name="Expression19", type=codemodel_statements_AssignmentStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_AssignmentStmt", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_codemodel_CodeModule_CMElement = Generalization(general=CMElement, specific=codemodel_CodeModule)
gen_codemodel_Variable_CMElement = Generalization(general=CMElement, specific=codemodel_Variable)
gen_codemodel_Function_CMElement = Generalization(general=CMElement, specific=codemodel_Function)
gen_codemodel_GlobalVariable_Variable = Generalization(general=Variable, specific=codemodel_GlobalVariable)
gen_codemodel_FunctionArgument_Variable = Generalization(general=Variable, specific=codemodel_FunctionArgument)
gen_codemodel_LocalVariable_Variable = Generalization(general=Variable, specific=codemodel_LocalVariable)
gen_codemodel_MatrixType_DataType = Generalization(general=DataType, specific=codemodel_MatrixType)
gen_codemodel_DataType_CMElement = Generalization(general=CMElement, specific=codemodel_DataType)
gen_codemodel_VectorType_DataType = Generalization(general=DataType, specific=codemodel_VectorType)
gen_codemodel_ScalarType_DataType = Generalization(general=DataType, specific=codemodel_ScalarType)
gen_codemodel_expressions_Expression_CMElement = Generalization(general=CMElement, specific=codemodel_expressions_Expression)
gen_codemodel_expressions_VariableExp_Expression = Generalization(general=Expression, specific=codemodel_expressions_VariableExp)
gen_codemodel_expressions_BinaryExp_Expression = Generalization(general=Expression, specific=codemodel_expressions_BinaryExp)
gen_codemodel_expressions_LiteralExp_Expression = Generalization(general=Expression, specific=codemodel_expressions_LiteralExp)
gen_codemodel_statements_Statement_CMElement = Generalization(general=CMElement, specific=codemodel_statements_Statement)
gen_codemodel_statements_AssignmentStmt_Statement = Generalization(general=Statement, specific=codemodel_statements_AssignmentStmt)
gen_codemodel_statements_CompositeStmt_Statement = Generalization(general=Statement, specific=codemodel_statements_CompositeStmt)
gen_codemodel_statements_IfStmt_Statement = Generalization(general=Statement, specific=codemodel_statements_IfStmt)
gen_codemodel_statements_ForStmt_Statement = Generalization(general=Statement, specific=codemodel_statements_ForStmt)

# Domain Model
domain_model = DomainModel(
    name="codemodel",
    types={codemodel_CMElement, codemodel_CodeModule, CMElement, codemodel_GlobalVariable, codemodel_Function, codemodel_DataType, codemodel_Variable, codemodel_FunctionArgument, codemodel_LocalVariable, Statement, Variable, codemodel_MatrixType, DataType, codemodel_VectorType, codemodel_ScalarType, codemodel_expressions_Expression, codemodel_expressions_VariableExp, Expression, expressions_codemodel_Variable, codemodel_expressions_BinaryExp, codemodel_expressions_LiteralExp, codemodel_statements_Statement, codemodel_statements_AssignmentStmt, codemodel_statements_CompositeStmt, codemodel_statements_IfStmt, codemodel_statements_ForStmt, AssignmentStmt},
    associations={globalVariables0, functions1, dataTypes3, type5, arguments7, localVariables9, body11, referencedVariable13, left14, right15, rightExp20, statements23, condition25, thenStmt27, elseStmt30, init33, condition34, increment37, forStmt40, leftExp18},
    generalizations={gen_codemodel_CodeModule_CMElement, gen_codemodel_Variable_CMElement, gen_codemodel_Function_CMElement, gen_codemodel_GlobalVariable_Variable, gen_codemodel_FunctionArgument_Variable, gen_codemodel_LocalVariable_Variable, gen_codemodel_MatrixType_DataType, gen_codemodel_DataType_CMElement, gen_codemodel_VectorType_DataType, gen_codemodel_ScalarType_DataType, gen_codemodel_expressions_Expression_CMElement, gen_codemodel_expressions_VariableExp_Expression, gen_codemodel_expressions_BinaryExp_Expression, gen_codemodel_expressions_LiteralExp_Expression, gen_codemodel_statements_Statement_CMElement, gen_codemodel_statements_AssignmentStmt_Statement, gen_codemodel_statements_CompositeStmt_Statement, gen_codemodel_statements_IfStmt_Statement, gen_codemodel_statements_ForStmt_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)