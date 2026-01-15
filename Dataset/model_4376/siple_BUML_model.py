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
siple_CompilationUnit = Class(name="siple::CompilationUnit")
siple_Expression = Class(name="siple::Expression", is_abstract=True)
siple_While = Class(name="siple::While")
siple_Declaration = Class(name="siple::Declaration", is_abstract=True)
siple_VariableAssignment = Class(name="siple::VariableAssignment")
siple_ProcedureDeclaration = Class(name="siple::ProcedureDeclaration")
siple_Statement = Class(name="siple::Statement", is_abstract=True)
siple_Block = Class(name="siple::Block")
Statement = Class(name="Statement")
siple_If = Class(name="siple::If")
siple_Read = Class(name="siple::Read")
siple_ProcedureReturn = Class(name="siple::ProcedureReturn")
siple_Write = Class(name="siple::Write")
siple_Constant = Class(name="siple::Constant")
Expression = Class(name="Expression")
siple_Reference = Class(name="siple::Reference")
siple_ProcedureCall = Class(name="siple::ProcedureCall")
siple_NestedExpression = Class(name="siple::NestedExpression")
siple_VariableDeclaration = Class(name="siple::VariableDeclaration")
Declaration = Class(name="Declaration")
siple_LogicExpression = Class(name="siple::LogicExpression", is_abstract=True)
BinaryExpression = Class(name="BinaryExpression")
siple_And = Class(name="siple::And")
LogicExpression = Class(name="LogicExpression")
siple_Or = Class(name="siple::Or")
siple_EqualityExpression = Class(name="siple::EqualityExpression", is_abstract=True)
siple_Equal = Class(name="siple::Equal")
EqualityExpression = Class(name="EqualityExpression")
siple_GreaterThan = Class(name="siple::GreaterThan")
siple_LesserThan = Class(name="siple::LesserThan")
siple_GreaterThanEqual = Class(name="siple::GreaterThanEqual")
siple_LesserThanEqual = Class(name="siple::LesserThanEqual")
siple_UnaryExpression = Class(name="siple::UnaryExpression", is_abstract=True)
siple_Not = Class(name="siple::Not")
UnaryExpression = Class(name="UnaryExpression")
siple_UMinus = Class(name="siple::UMinus")
siple_RealCoercion = Class(name="siple::RealCoercion")
siple_Dereference = Class(name="siple::Dereference")
siple_BinaryExpression = Class(name="siple::BinaryExpression", is_abstract=True)
siple_ArithmeticExpression = Class(name="siple::ArithmeticExpression", is_abstract=True)
siple_Addition = Class(name="siple::Addition")
ArithmeticExpression = Class(name="ArithmeticExpression")
siple_Subtraction = Class(name="siple::Subtraction")
siple_Multiplication = Class(name="siple::Multiplication")
siple_Division = Class(name="siple::Division")

# siple_CompilationUnit class attributes and methods
siple_CompilationUnit_m_Interpret: Method = Method(name="Interpret", parameters={}, type=StringType)
siple_CompilationUnit.methods={siple_CompilationUnit_m_Interpret}

# siple_Expression class attributes and methods
siple_Expression_Type: Property = Property(name="Type", type=StringType)
siple_Expression_m_Value: Method = Method(name="Value", parameters={Parameter(name='vm')}, type=StringType)
siple_Expression.attributes={siple_Expression_Type}
siple_Expression.methods={siple_Expression_m_Value}

# siple_While class attributes and methods

# siple_Declaration class attributes and methods
siple_Declaration_Name: Property = Property(name="Name", type=StringType)
siple_Declaration_IsParameterDeclaration: Property = Property(name="IsParameterDeclaration", type=BooleanType)
siple_Declaration_Type: Property = Property(name="Type", type=StringType)
siple_Declaration.attributes={siple_Declaration_Name, siple_Declaration_Type, siple_Declaration_IsParameterDeclaration}

# siple_VariableAssignment class attributes and methods
siple_VariableAssignment_Type: Property = Property(name="Type", type=StringType)
siple_VariableAssignment.attributes={siple_VariableAssignment_Type}

# siple_ProcedureDeclaration class attributes and methods
siple_ProcedureDeclaration_ReturnType: Property = Property(name="ReturnType", type=StringType)
siple_ProcedureDeclaration.attributes={siple_ProcedureDeclaration_ReturnType}

# siple_Statement class attributes and methods
siple_Statement_m_Interpret: Method = Method(name="Interpret", parameters={Parameter(name='vm')})
siple_Statement.methods={siple_Statement_m_Interpret}

# siple_Block class attributes and methods

# Statement class attributes and methods

# siple_If class attributes and methods

# siple_Read class attributes and methods
siple_Read_Type: Property = Property(name="Type", type=StringType)
siple_Read.attributes={siple_Read_Type}

# siple_ProcedureReturn class attributes and methods
siple_ProcedureReturn_Type: Property = Property(name="Type", type=StringType)
siple_ProcedureReturn.attributes={siple_ProcedureReturn_Type}

# siple_Write class attributes and methods
siple_Write_Type: Property = Property(name="Type", type=StringType)
siple_Write.attributes={siple_Write_Type}

# siple_Constant class attributes and methods
siple_Constant_Lexem: Property = Property(name="Lexem", type=StringType)
siple_Constant_AsBoolean: Property = Property(name="AsBoolean", type=StringType)
siple_Constant_AsInteger: Property = Property(name="AsInteger", type=StringType)
siple_Constant_AsReal: Property = Property(name="AsReal", type=StringType)
siple_Constant.attributes={siple_Constant_AsInteger, siple_Constant_AsReal, siple_Constant_AsBoolean, siple_Constant_Lexem}

# Expression class attributes and methods

# siple_Reference class attributes and methods
siple_Reference_Name: Property = Property(name="Name", type=StringType)
siple_Reference.attributes={siple_Reference_Name}

# siple_ProcedureCall class attributes and methods

# siple_NestedExpression class attributes and methods

# siple_VariableDeclaration class attributes and methods
siple_VariableDeclaration_DeclaredType: Property = Property(name="DeclaredType", type=StringType)
siple_VariableDeclaration.attributes={siple_VariableDeclaration_DeclaredType}

# Declaration class attributes and methods

# siple_LogicExpression class attributes and methods

# BinaryExpression class attributes and methods

# siple_And class attributes and methods

# LogicExpression class attributes and methods

# siple_Or class attributes and methods

# siple_EqualityExpression class attributes and methods

# siple_Equal class attributes and methods

# EqualityExpression class attributes and methods

# siple_GreaterThan class attributes and methods

# siple_LesserThan class attributes and methods

# siple_GreaterThanEqual class attributes and methods

# siple_LesserThanEqual class attributes and methods

# siple_UnaryExpression class attributes and methods

# siple_Not class attributes and methods

# UnaryExpression class attributes and methods

# siple_UMinus class attributes and methods

# siple_RealCoercion class attributes and methods

# siple_Dereference class attributes and methods

# siple_BinaryExpression class attributes and methods

# siple_ArithmeticExpression class attributes and methods

# siple_Addition class attributes and methods

# ArithmeticExpression class attributes and methods

# siple_Subtraction class attributes and methods

# siple_Multiplication class attributes and methods

# siple_Division class attributes and methods

# Relationships
Condition10: BinaryAssociation = BinaryAssociation(
    name="Condition10",
    ends={
        Property(name="siple_Expression", type=siple_If, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_If", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Body11: BinaryAssociation = BinaryAssociation(
    name="Body11",
    ends={
        Property(name="siple_Block13", type=siple_If, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_If12", type=siple_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Alternative14: BinaryAssociation = BinaryAssociation(
    name="Alternative14",
    ends={
        Property(name="siple_Block16", type=siple_If, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_If15", type=siple_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Condition17: BinaryAssociation = BinaryAssociation(
    name="Condition17",
    ends={
        Property(name="siple_Expression18", type=siple_While, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_While", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Body19: BinaryAssociation = BinaryAssociation(
    name="Body19",
    ends={
        Property(name="siple_Block21", type=siple_While, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_While20", type=siple_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Declaration0: BinaryAssociation = BinaryAssociation(
    name="Declaration0",
    ends={
        Property(name="siple_Declaration", type=siple_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_CompilationUnit", type=siple_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
MainProcedure1: BinaryAssociation = BinaryAssociation(
    name="MainProcedure1",
    ends={
        Property(name="siple_ProcedureDeclaration", type=siple_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_CompilationUnit2", type=siple_ProcedureDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
ProcedureInContext3: BinaryAssociation = BinaryAssociation(
    name="ProcedureInContext3",
    ends={
        Property(name="siple_ProcedureDeclaration4", type=siple_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_Statement", type=siple_ProcedureDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
Statement5: BinaryAssociation = BinaryAssociation(
    name="Statement5",
    ends={
        Property(name="siple_Statement6", type=siple_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_Block", type=siple_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IsProcedureBody7: BinaryAssociation = BinaryAssociation(
    name="IsProcedureBody7",
    ends={
        Property(name="siple_ProcedureDeclaration9", type=siple_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_Block8", type=siple_ProcedureDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
Expression29: BinaryAssociation = BinaryAssociation(
    name="Expression29",
    ends={
        Property(name="siple_Expression30", type=siple_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_Write", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Expression31: BinaryAssociation = BinaryAssociation(
    name="Expression31",
    ends={
        Property(name="siple_Expression32", type=siple_Read, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_Read", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
LValue22: BinaryAssociation = BinaryAssociation(
    name="LValue22",
    ends={
        Property(name="siple_Expression23", type=siple_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_VariableAssignment", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
RValue24: BinaryAssociation = BinaryAssociation(
    name="RValue24",
    ends={
        Property(name="siple_Expression26", type=siple_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_VariableAssignment25", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Expression27: BinaryAssociation = BinaryAssociation(
    name="Expression27",
    ends={
        Property(name="siple_Expression28", type=siple_ProcedureReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_ProcedureReturn", type=siple_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Body35: BinaryAssociation = BinaryAssociation(
    name="Body35",
    ends={
        Property(name="siple_Block37", type=siple_ProcedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_ProcedureDeclaration36", type=siple_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Declaration38: BinaryAssociation = BinaryAssociation(
    name="Declaration38",
    ends={
        Property(name="siple_Declaration39", type=siple_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_Reference", type=siple_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
Procedure40: BinaryAssociation = BinaryAssociation(
    name="Procedure40",
    ends={
        Property(name="siple_Expression41", type=siple_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_ProcedureCall", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Argument42: BinaryAssociation = BinaryAssociation(
    name="Argument42",
    ends={
        Property(name="siple_Expression44", type=siple_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_ProcedureCall43", type=siple_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Declaration45: BinaryAssociation = BinaryAssociation(
    name="Declaration45",
    ends={
        Property(name="siple_ProcedureDeclaration47", type=siple_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_ProcedureCall46", type=siple_ProcedureDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
Parameter33: BinaryAssociation = BinaryAssociation(
    name="Parameter33",
    ends={
        Property(name="siple_VariableDeclaration", type=siple_ProcedureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_ProcedureDeclaration34", type=siple_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Operand152: BinaryAssociation = BinaryAssociation(
    name="Operand152",
    ends={
        Property(name="siple_Expression53", type=siple_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_BinaryExpression", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Operand254: BinaryAssociation = BinaryAssociation(
    name="Operand254",
    ends={
        Property(name="siple_Expression56", type=siple_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_BinaryExpression55", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Expression48: BinaryAssociation = BinaryAssociation(
    name="Expression48",
    ends={
        Property(name="siple_Expression49", type=siple_NestedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_NestedExpression", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Operand50: BinaryAssociation = BinaryAssociation(
    name="Operand50",
    ends={
        Property(name="siple_Expression51", type=siple_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="siple_UnaryExpression", type=siple_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_siple_If_Statement = Generalization(general=Statement, specific=siple_If)
gen_siple_While_Statement = Generalization(general=Statement, specific=siple_While)
gen_siple_VariableAssignment_Statement = Generalization(general=Statement, specific=siple_VariableAssignment)
gen_siple_Block_Statement = Generalization(general=Statement, specific=siple_Block)
gen_siple_Read_Statement = Generalization(general=Statement, specific=siple_Read)
gen_siple_ProcedureReturn_Statement = Generalization(general=Statement, specific=siple_ProcedureReturn)
gen_siple_Write_Statement = Generalization(general=Statement, specific=siple_Write)
gen_siple_Expression_Statement = Generalization(general=Statement, specific=siple_Expression)
gen_siple_Constant_Expression = Generalization(general=Expression, specific=siple_Constant)
gen_siple_Reference_Expression = Generalization(general=Expression, specific=siple_Reference)
gen_siple_ProcedureCall_Expression = Generalization(general=Expression, specific=siple_ProcedureCall)
gen_siple_NestedExpression_Expression = Generalization(general=Expression, specific=siple_NestedExpression)
gen_siple_Declaration_Statement = Generalization(general=Statement, specific=siple_Declaration)
gen_siple_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=siple_VariableDeclaration)
gen_siple_ProcedureDeclaration_Declaration = Generalization(general=Declaration, specific=siple_ProcedureDeclaration)
gen_siple_LogicExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=siple_LogicExpression)
gen_siple_And_LogicExpression = Generalization(general=LogicExpression, specific=siple_And)
gen_siple_Or_LogicExpression = Generalization(general=LogicExpression, specific=siple_Or)
gen_siple_EqualityExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=siple_EqualityExpression)
gen_siple_Equal_EqualityExpression = Generalization(general=EqualityExpression, specific=siple_Equal)
gen_siple_GreaterThan_EqualityExpression = Generalization(general=EqualityExpression, specific=siple_GreaterThan)
gen_siple_LesserThan_EqualityExpression = Generalization(general=EqualityExpression, specific=siple_LesserThan)
gen_siple_GreaterThanEqual_EqualityExpression = Generalization(general=EqualityExpression, specific=siple_GreaterThanEqual)
gen_siple_LesserThanEqual_EqualityExpression = Generalization(general=EqualityExpression, specific=siple_LesserThanEqual)
gen_siple_UnaryExpression_Expression = Generalization(general=Expression, specific=siple_UnaryExpression)
gen_siple_Not_UnaryExpression = Generalization(general=UnaryExpression, specific=siple_Not)
gen_siple_UMinus_UnaryExpression = Generalization(general=UnaryExpression, specific=siple_UMinus)
gen_siple_RealCoercion_UnaryExpression = Generalization(general=UnaryExpression, specific=siple_RealCoercion)
gen_siple_Dereference_UnaryExpression = Generalization(general=UnaryExpression, specific=siple_Dereference)
gen_siple_BinaryExpression_Expression = Generalization(general=Expression, specific=siple_BinaryExpression)
gen_siple_ArithmeticExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=siple_ArithmeticExpression)
gen_siple_Addition_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=siple_Addition)
gen_siple_Subtraction_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=siple_Subtraction)
gen_siple_Multiplication_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=siple_Multiplication)
gen_siple_Division_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=siple_Division)

# Domain Model
domain_model = DomainModel(
    name="siple",
    types={siple_CompilationUnit, siple_Expression, siple_While, siple_Declaration, siple_VariableAssignment, siple_ProcedureDeclaration, siple_Statement, siple_Block, Statement, siple_If, siple_Read, siple_ProcedureReturn, siple_Write, siple_Constant, Expression, siple_Reference, siple_ProcedureCall, siple_NestedExpression, siple_VariableDeclaration, Declaration, siple_LogicExpression, BinaryExpression, siple_And, LogicExpression, siple_Or, siple_EqualityExpression, siple_Equal, EqualityExpression, siple_GreaterThan, siple_LesserThan, siple_GreaterThanEqual, siple_LesserThanEqual, siple_UnaryExpression, siple_Not, UnaryExpression, siple_UMinus, siple_RealCoercion, siple_Dereference, siple_BinaryExpression, siple_ArithmeticExpression, siple_Addition, ArithmeticExpression, siple_Subtraction, siple_Multiplication, siple_Division},
    associations={Condition10, Body11, Alternative14, Condition17, Body19, Declaration0, MainProcedure1, ProcedureInContext3, Statement5, IsProcedureBody7, Expression29, Expression31, LValue22, RValue24, Expression27, Body35, Declaration38, Procedure40, Argument42, Declaration45, Parameter33, Operand152, Operand254, Expression48, Operand50},
    generalizations={gen_siple_If_Statement, gen_siple_While_Statement, gen_siple_VariableAssignment_Statement, gen_siple_Block_Statement, gen_siple_Read_Statement, gen_siple_ProcedureReturn_Statement, gen_siple_Write_Statement, gen_siple_Expression_Statement, gen_siple_Constant_Expression, gen_siple_Reference_Expression, gen_siple_ProcedureCall_Expression, gen_siple_NestedExpression_Expression, gen_siple_Declaration_Statement, gen_siple_VariableDeclaration_Declaration, gen_siple_ProcedureDeclaration_Declaration, gen_siple_LogicExpression_BinaryExpression, gen_siple_And_LogicExpression, gen_siple_Or_LogicExpression, gen_siple_EqualityExpression_BinaryExpression, gen_siple_Equal_EqualityExpression, gen_siple_GreaterThan_EqualityExpression, gen_siple_LesserThan_EqualityExpression, gen_siple_GreaterThanEqual_EqualityExpression, gen_siple_LesserThanEqual_EqualityExpression, gen_siple_UnaryExpression_Expression, gen_siple_Not_UnaryExpression, gen_siple_UMinus_UnaryExpression, gen_siple_RealCoercion_UnaryExpression, gen_siple_Dereference_UnaryExpression, gen_siple_BinaryExpression_Expression, gen_siple_ArithmeticExpression_BinaryExpression, gen_siple_Addition_ArithmeticExpression, gen_siple_Subtraction_ArithmeticExpression, gen_siple_Multiplication_ArithmeticExpression, gen_siple_Division_ArithmeticExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)