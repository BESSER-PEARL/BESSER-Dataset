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
Languages: Enumeration = Enumeration(
    name="Languages",
    literals={
            EnumerationLiteral(name="Java"),
			EnumerationLiteral(name="CS"),
			EnumerationLiteral(name="Python"),
			EnumerationLiteral(name="CPP")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="int"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="void")
    }
)

AccessModifiers: Enumeration = Enumeration(
    name="AccessModifiers",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="protected"),
			EnumerationLiteral(name="private")
    }
)

# Classes
workflow_CompilationUnit = Class(name="workflow::CompilationUnit")
workflow_ProcedureDeclaration = Class(name="workflow::ProcedureDeclaration", is_abstract=True)
workflow_Statement = Class(name="workflow::Statement", is_abstract=True)
workflow_Block = Class(name="workflow::Block")
Statement = Class(name="Statement")
workflow_VariableAssignment = Class(name="workflow::VariableAssignment")
workflow_Variable = Class(name="workflow::Variable")
workflow_ProcedureReturn = Class(name="workflow::ProcedureReturn")
workflow_Write = Class(name="workflow::Write")
workflow_Read = Class(name="workflow::Read")
workflow_If = Class(name="workflow::If")
workflow_Expression = Class(name="workflow::Expression", is_abstract=True)
workflow_While = Class(name="workflow::While")
workflow_ProcedureCall = Class(name="workflow::ProcedureCall")
workflow_UnaryExpression = Class(name="workflow::UnaryExpression", is_abstract=True)
workflow_Not = Class(name="workflow::Not")
UnaryExpression = Class(name="UnaryExpression")
workflow_UMinus = Class(name="workflow::UMinus")
workflow_BinaryExpression = Class(name="workflow::BinaryExpression", is_abstract=True)
workflow_Declaration = Class(name="workflow::Declaration", is_abstract=True)
workflow_VariableDeclaration = Class(name="workflow::VariableDeclaration")
Declaration = Class(name="Declaration")
workflow_ParameterDeclaration = Class(name="workflow::ParameterDeclaration")
workflow_Constant = Class(name="workflow::Constant")
Expression = Class(name="Expression")
workflow_Division = Class(name="workflow::Division")
workflow_NotEqual = Class(name="workflow::NotEqual")
workflow_LogicExpression = Class(name="workflow::LogicExpression", is_abstract=True)
BinaryExpression = Class(name="BinaryExpression")
workflow_And = Class(name="workflow::And")
LogicExpression = Class(name="LogicExpression")
workflow_Or = Class(name="workflow::Or")
workflow_EqualityExpression = Class(name="workflow::EqualityExpression", is_abstract=True)
workflow_Equal = Class(name="workflow::Equal")
EqualityExpression = Class(name="EqualityExpression")
workflow_GreaterThan = Class(name="workflow::GreaterThan")
workflow_LessThan = Class(name="workflow::LessThan")
workflow_GreaterThanOrEqual = Class(name="workflow::GreaterThanOrEqual")
workflow_LessThanOrEqual = Class(name="workflow::LessThanOrEqual")
workflow_ArithmeticExpression = Class(name="workflow::ArithmeticExpression", is_abstract=True)
workflow_Addition = Class(name="workflow::Addition")
ArithmeticExpression = Class(name="ArithmeticExpression")
workflow_Subtraction = Class(name="workflow::Subtraction")
workflow_Multiplication = Class(name="workflow::Multiplication")

# workflow_CompilationUnit class attributes and methods
workflow_CompilationUnit_name: Property = Property(name="name", type=StringType)
workflow_CompilationUnit_language: Property = Property(name="language", type=StringType)
workflow_CompilationUnit.attributes={workflow_CompilationUnit_name, workflow_CompilationUnit_language}

# workflow_ProcedureDeclaration class attributes and methods
workflow_ProcedureDeclaration_returnType: Property = Property(name="returnType", type=StringType)
workflow_ProcedureDeclaration_accessModifier: Property = Property(name="accessModifier", type=StringType)
workflow_ProcedureDeclaration.attributes={workflow_ProcedureDeclaration_returnType, workflow_ProcedureDeclaration_accessModifier}

# workflow_Statement class attributes and methods

# workflow_Block class attributes and methods

# Statement class attributes and methods

# workflow_VariableAssignment class attributes and methods

# workflow_Variable class attributes and methods
workflow_Variable_name: Property = Property(name="name", type=StringType)
workflow_Variable.attributes={workflow_Variable_name}

# workflow_ProcedureReturn class attributes and methods

# workflow_Write class attributes and methods

# workflow_Read class attributes and methods
workflow_Read_type: Property = Property(name="type", type=StringType)
workflow_Read.attributes={workflow_Read_type}

# workflow_If class attributes and methods

# workflow_Expression class attributes and methods

# workflow_While class attributes and methods

# workflow_ProcedureCall class attributes and methods
workflow_ProcedureCall_name: Property = Property(name="name", type=StringType)
workflow_ProcedureCall.attributes={workflow_ProcedureCall_name}

# workflow_UnaryExpression class attributes and methods

# workflow_Not class attributes and methods

# UnaryExpression class attributes and methods

# workflow_UMinus class attributes and methods

# workflow_BinaryExpression class attributes and methods

# workflow_Declaration class attributes and methods
workflow_Declaration_name: Property = Property(name="name", type=StringType)
workflow_Declaration.attributes={workflow_Declaration_name}

# workflow_VariableDeclaration class attributes and methods
workflow_VariableDeclaration_type: Property = Property(name="type", type=StringType)
workflow_VariableDeclaration_isConstant: Property = Property(name="isConstant", type=StringType)
workflow_VariableDeclaration.attributes={workflow_VariableDeclaration_type, workflow_VariableDeclaration_isConstant}

# Declaration class attributes and methods

# workflow_ParameterDeclaration class attributes and methods
workflow_ParameterDeclaration_type: Property = Property(name="type", type=StringType)
workflow_ParameterDeclaration.attributes={workflow_ParameterDeclaration_type}

# workflow_Constant class attributes and methods
workflow_Constant_asBoolean: Property = Property(name="asBoolean", type=StringType)
workflow_Constant_asInteger: Property = Property(name="asInteger", type=StringType)
workflow_Constant_asReal: Property = Property(name="asReal", type=StringType)
workflow_Constant_asString: Property = Property(name="asString", type=StringType)
workflow_Constant.attributes={workflow_Constant_asString, workflow_Constant_asReal, workflow_Constant_asBoolean, workflow_Constant_asInteger}

# Expression class attributes and methods

# workflow_Division class attributes and methods

# workflow_NotEqual class attributes and methods

# workflow_LogicExpression class attributes and methods

# BinaryExpression class attributes and methods

# workflow_And class attributes and methods

# LogicExpression class attributes and methods

# workflow_Or class attributes and methods

# workflow_EqualityExpression class attributes and methods

# workflow_Equal class attributes and methods

# EqualityExpression class attributes and methods

# workflow_GreaterThan class attributes and methods

# workflow_LessThan class attributes and methods

# workflow_GreaterThanOrEqual class attributes and methods

# workflow_LessThanOrEqual class attributes and methods

# workflow_ArithmeticExpression class attributes and methods

# workflow_Addition class attributes and methods

# ArithmeticExpression class attributes and methods

# workflow_Subtraction class attributes and methods

# workflow_Multiplication class attributes and methods

# Relationships
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="workflow_ProcedureDeclaration", type=workflow_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_CompilationUnit", type=workflow_ProcedureDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Condition9: BinaryAssociation = BinaryAssociation(
    name="Condition9",
    ends={
        Property(name="workflow_Expression10", type=workflow_While, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_While", type=workflow_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Body11: BinaryAssociation = BinaryAssociation(
    name="Body11",
    ends={
        Property(name="workflow_Block13", type=workflow_While, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_While12", type=workflow_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LValue14: BinaryAssociation = BinaryAssociation(
    name="LValue14",
    ends={
        Property(name="workflow_Variable", type=workflow_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_VariableAssignment", type=workflow_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
RValue15: BinaryAssociation = BinaryAssociation(
    name="RValue15",
    ends={
        Property(name="workflow_Expression17", type=workflow_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_VariableAssignment16", type=workflow_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Expression18: BinaryAssociation = BinaryAssociation(
    name="Expression18",
    ends={
        Property(name="workflow_Expression19", type=workflow_ProcedureReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ProcedureReturn", type=workflow_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wVar20: BinaryAssociation = BinaryAssociation(
    name="wVar20",
    ends={
        Property(name="workflow_Variable21", type=workflow_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Write", type=workflow_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rVar22: BinaryAssociation = BinaryAssociation(
    name="rVar22",
    ends={
        Property(name="workflow_Variable23", type=workflow_Read, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Read", type=workflow_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Statement1: BinaryAssociation = BinaryAssociation(
    name="Statement1",
    ends={
        Property(name="workflow_Statement", type=workflow_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Block", type=workflow_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Condition2: BinaryAssociation = BinaryAssociation(
    name="Condition2",
    ends={
        Property(name="workflow_Expression", type=workflow_If, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_If", type=workflow_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Body3: BinaryAssociation = BinaryAssociation(
    name="Body3",
    ends={
        Property(name="workflow_Block5", type=workflow_If, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_If4", type=workflow_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Alternative6: BinaryAssociation = BinaryAssociation(
    name="Alternative6",
    ends={
        Property(name="workflow_Block8", type=workflow_If, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_If7", type=workflow_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Argument31: BinaryAssociation = BinaryAssociation(
    name="Argument31",
    ends={
        Property(name="workflow_Expression32", type=workflow_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ProcedureCall", type=workflow_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Operand33: BinaryAssociation = BinaryAssociation(
    name="Operand33",
    ends={
        Property(name="workflow_Expression34", type=workflow_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_UnaryExpression", type=workflow_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Operand135: BinaryAssociation = BinaryAssociation(
    name="Operand135",
    ends={
        Property(name="workflow_Expression36", type=workflow_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_BinaryExpression", type=workflow_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Variables24: BinaryAssociation = BinaryAssociation(
    name="Variables24",
    ends={
        Property(name="workflow_VariableDeclaration", type=workflow_ProcedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ProcedureDeclaration25", type=workflow_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Body26: BinaryAssociation = BinaryAssociation(
    name="Body26",
    ends={
        Property(name="workflow_Block28", type=workflow_ProcedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ProcedureDeclaration27", type=workflow_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Parameter29: BinaryAssociation = BinaryAssociation(
    name="Parameter29",
    ends={
        Property(name="workflow_ParameterDeclaration", type=workflow_ProcedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ProcedureDeclaration30", type=workflow_ParameterDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Operand237: BinaryAssociation = BinaryAssociation(
    name="Operand237",
    ends={
        Property(name="workflow_Expression39", type=workflow_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_BinaryExpression38", type=workflow_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_workflow_Block_Statement = Generalization(general=Statement, specific=workflow_Block)
gen_workflow_VariableAssignment_Statement = Generalization(general=Statement, specific=workflow_VariableAssignment)
gen_workflow_ProcedureReturn_Statement = Generalization(general=Statement, specific=workflow_ProcedureReturn)
gen_workflow_Write_Statement = Generalization(general=Statement, specific=workflow_Write)
gen_workflow_Read_Statement = Generalization(general=Statement, specific=workflow_Read)
gen_workflow_If_Statement = Generalization(general=Statement, specific=workflow_If)
gen_workflow_While_Statement = Generalization(general=Statement, specific=workflow_While)
gen_workflow_ProcedureCall_Expression = Generalization(general=Expression, specific=workflow_ProcedureCall)
gen_workflow_UnaryExpression_Expression = Generalization(general=Expression, specific=workflow_UnaryExpression)
gen_workflow_Not_UnaryExpression = Generalization(general=UnaryExpression, specific=workflow_Not)
gen_workflow_UMinus_UnaryExpression = Generalization(general=UnaryExpression, specific=workflow_UMinus)
gen_workflow_BinaryExpression_Expression = Generalization(general=Expression, specific=workflow_BinaryExpression)
gen_workflow_Declaration_Statement = Generalization(general=Statement, specific=workflow_Declaration)
gen_workflow_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=workflow_VariableDeclaration)
gen_workflow_ProcedureDeclaration_Declaration = Generalization(general=Declaration, specific=workflow_ProcedureDeclaration)
gen_workflow_Expression_Statement = Generalization(general=Statement, specific=workflow_Expression)
gen_workflow_Constant_Expression = Generalization(general=Expression, specific=workflow_Constant)
gen_workflow_Division_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=workflow_Division)
gen_workflow_ParameterDeclaration_Declaration = Generalization(general=Declaration, specific=workflow_ParameterDeclaration)
gen_workflow_Variable_Expression = Generalization(general=Expression, specific=workflow_Variable)
gen_workflow_NotEqual_EqualityExpression = Generalization(general=EqualityExpression, specific=workflow_NotEqual)
gen_workflow_LogicExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=workflow_LogicExpression)
gen_workflow_And_LogicExpression = Generalization(general=LogicExpression, specific=workflow_And)
gen_workflow_Or_LogicExpression = Generalization(general=LogicExpression, specific=workflow_Or)
gen_workflow_EqualityExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=workflow_EqualityExpression)
gen_workflow_Equal_EqualityExpression = Generalization(general=EqualityExpression, specific=workflow_Equal)
gen_workflow_GreaterThan_EqualityExpression = Generalization(general=EqualityExpression, specific=workflow_GreaterThan)
gen_workflow_LessThan_EqualityExpression = Generalization(general=EqualityExpression, specific=workflow_LessThan)
gen_workflow_GreaterThanOrEqual_EqualityExpression = Generalization(general=EqualityExpression, specific=workflow_GreaterThanOrEqual)
gen_workflow_LessThanOrEqual_EqualityExpression = Generalization(general=EqualityExpression, specific=workflow_LessThanOrEqual)
gen_workflow_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=workflow_ArithmeticExpression)
gen_workflow_Addition_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=workflow_Addition)
gen_workflow_Subtraction_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=workflow_Subtraction)
gen_workflow_Multiplication_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=workflow_Multiplication)

# Domain Model
domain_model = DomainModel(
    name="workflow",
    types={workflow_CompilationUnit, workflow_ProcedureDeclaration, workflow_Statement, workflow_Block, Statement, workflow_VariableAssignment, workflow_Variable, workflow_ProcedureReturn, workflow_Write, workflow_Read, workflow_If, workflow_Expression, workflow_While, workflow_ProcedureCall, workflow_UnaryExpression, workflow_Not, UnaryExpression, workflow_UMinus, workflow_BinaryExpression, workflow_Declaration, workflow_VariableDeclaration, Declaration, workflow_ParameterDeclaration, workflow_Constant, Expression, workflow_Division, workflow_NotEqual, workflow_LogicExpression, BinaryExpression, workflow_And, LogicExpression, workflow_Or, workflow_EqualityExpression, workflow_Equal, EqualityExpression, workflow_GreaterThan, workflow_LessThan, workflow_GreaterThanOrEqual, workflow_LessThanOrEqual, workflow_ArithmeticExpression, workflow_Addition, ArithmeticExpression, workflow_Subtraction, workflow_Multiplication, Languages, Type, AccessModifiers},
    associations={declarations0, Condition9, Body11, LValue14, RValue15, Expression18, wVar20, rVar22, Statement1, Condition2, Body3, Alternative6, Argument31, Operand33, Operand135, Variables24, Body26, Parameter29, Operand237},
    generalizations={gen_workflow_Block_Statement, gen_workflow_VariableAssignment_Statement, gen_workflow_ProcedureReturn_Statement, gen_workflow_Write_Statement, gen_workflow_Read_Statement, gen_workflow_If_Statement, gen_workflow_While_Statement, gen_workflow_ProcedureCall_Expression, gen_workflow_UnaryExpression_Expression, gen_workflow_Not_UnaryExpression, gen_workflow_UMinus_UnaryExpression, gen_workflow_BinaryExpression_Expression, gen_workflow_Declaration_Statement, gen_workflow_VariableDeclaration_Declaration, gen_workflow_ProcedureDeclaration_Declaration, gen_workflow_Expression_Statement, gen_workflow_Constant_Expression, gen_workflow_Division_ArithmeticExpression, gen_workflow_ParameterDeclaration_Declaration, gen_workflow_Variable_Expression, gen_workflow_NotEqual_EqualityExpression, gen_workflow_LogicExpression_BinaryExpression, gen_workflow_And_LogicExpression, gen_workflow_Or_LogicExpression, gen_workflow_EqualityExpression_BinaryExpression, gen_workflow_Equal_EqualityExpression, gen_workflow_GreaterThan_EqualityExpression, gen_workflow_LessThan_EqualityExpression, gen_workflow_GreaterThanOrEqual_EqualityExpression, gen_workflow_LessThanOrEqual_EqualityExpression, gen_workflow_ArithmeticExpression_BinaryExpression, gen_workflow_Addition_ArithmeticExpression, gen_workflow_Subtraction_ArithmeticExpression, gen_workflow_Multiplication_ArithmeticExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)