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
limp_Specification = Class(name="limp::Specification")
limp_Declaration = Class(name="limp::Declaration")
limp_Comment = Class(name="limp::Comment")
Declaration = Class(name="Declaration")
limp_Import = Class(name="limp::Import")
limp_OutputArgList = Class(name="limp::OutputArgList")
limp_AttributeBlock = Class(name="limp::AttributeBlock")
limp_LocalFunction = Class(name="limp::LocalFunction")
limp_VarBlock = Class(name="limp::VarBlock")
limp_EquationBlock = Class(name="limp::EquationBlock")
limp_LocalProcedure = Class(name="limp::LocalProcedure")
limp_StatementBlock = Class(name="limp::StatementBlock")
limp_ExternalFunction = Class(name="limp::ExternalFunction")
FunctionRef = Class(name="FunctionRef")
limp_InputArgList = Class(name="limp::InputArgList")
limp_OutputArg = Class(name="limp::OutputArg")
limp_ExternalProcedure = Class(name="limp::ExternalProcedure")
limp_ArrayTypeDef = Class(name="limp::ArrayTypeDef")
limp_Type = Class(name="limp::Type")
limp_AbstractTypeDef = Class(name="limp::AbstractTypeDef")
limp_ConstantDeclaration = Class(name="limp::ConstantDeclaration")
limp_Expr = Class(name="limp::Expr")
limp_GlobalDeclaration = Class(name="limp::GlobalDeclaration")
limp_VariableRef = Class(name="limp::VariableRef")
limp_InputArg = Class(name="limp::InputArg")
limp_LocalArg = Class(name="limp::LocalArg")
limp_TypeDeclaration = Class(name="limp::TypeDeclaration")
limp_EnumTypeDef = Class(name="limp::EnumTypeDef")
TypeDeclaration = Class(name="TypeDeclaration")
limp_EnumValue = Class(name="limp::EnumValue")
VariableRef = Class(name="VariableRef")
limp_RecordTypeDef = Class(name="limp::RecordTypeDef")
limp_RecordFieldType = Class(name="limp::RecordFieldType")
limp_DefineUseRef = Class(name="limp::DefineUseRef")
limp_Define = Class(name="limp::Define")
limp_Uses = Class(name="limp::Uses")
limp_Statement = Class(name="limp::Statement")
limp_VoidStatement = Class(name="limp::VoidStatement")
Statement = Class(name="Statement")
Equation = Class(name="Equation")
limp_AssignmentStatement = Class(name="limp::AssignmentStatement")
limp_IdList = Class(name="limp::IdList")
limp_IfThenElseStatement = Class(name="limp::IfThenElseStatement")
limp_Else = Class(name="limp::Else")
limp_Attribute = Class(name="limp::Attribute")
limp_Precondition = Class(name="limp::Precondition")
Attribute = Class(name="Attribute")
limp_Postcondition = Class(name="limp::Postcondition")
limp_LabelStatement = Class(name="limp::LabelStatement")
limp_GotoStatement = Class(name="limp::GotoStatement")
limp_Equation = Class(name="limp::Equation")
limp_FunctionRef = Class(name="limp::FunctionRef")
limp_ArrayExpr = Class(name="limp::ArrayExpr")
Expr = Class(name="Expr")
limp_RecordExpr = Class(name="limp::RecordExpr")
limp_RecordFieldExpr = Class(name="limp::RecordFieldExpr")
limp_WhileStatement = Class(name="limp::WhileStatement")
limp_ForStatement = Class(name="limp::ForStatement")
limp_VoidType = Class(name="limp::VoidType")
Type = Class(name="Type")
limp_BoolType = Class(name="limp::BoolType")
limp_IntegerType = Class(name="limp::IntegerType")
limp_RealType = Class(name="limp::RealType")
limp_StringType = Class(name="limp::StringType")
limp_EnumType = Class(name="limp::EnumType")
limp_RecordType = Class(name="limp::RecordType")
limp_ArrayType = Class(name="limp::ArrayType")
limp_AbstractType = Class(name="limp::AbstractType")
limp_NamedType = Class(name="limp::NamedType")
limp_SomeAttributeBlock = Class(name="limp::SomeAttributeBlock")
AttributeBlock = Class(name="AttributeBlock")
limp_NoAttributeBlock = Class(name="limp::NoAttributeBlock")
limp_BreakStatement = Class(name="limp::BreakStatement")
limp_ContinueStatement = Class(name="limp::ContinueStatement")
limp_ReturnStatement = Class(name="limp::ReturnStatement")
limp_ElseBlock = Class(name="limp::ElseBlock")
Else = Class(name="Else")
limp_ExprList = Class(name="limp::ExprList")
limp_TypeAlias = Class(name="limp::TypeAlias")
limp_SomeVarBlock = Class(name="limp::SomeVarBlock")
VarBlock = Class(name="VarBlock")
limp_NoVarBlock = Class(name="limp::NoVarBlock")
limp_ChoiceExpr = Class(name="limp::ChoiceExpr")
limp_BinaryExpr = Class(name="limp::BinaryExpr")
limp_UnaryNegationExpr = Class(name="limp::UnaryNegationExpr")
limp_UnaryMinusExpr = Class(name="limp::UnaryMinusExpr")
limp_RecordAccessExpr = Class(name="limp::RecordAccessExpr")
limp_RecordUpdateExpr = Class(name="limp::RecordUpdateExpr")
limp_ElseIf = Class(name="limp::ElseIf")
limp_NoElse = Class(name="limp::NoElse")
limp_IfThenElseExpr = Class(name="limp::IfThenElseExpr")
limp_BooleanLiteralExpr = Class(name="limp::BooleanLiteralExpr")
limp_IntegerLiteralExpr = Class(name="limp::IntegerLiteralExpr")
limp_IntegerWildCardExpr = Class(name="limp::IntegerWildCardExpr")
limp_RealLiteralExpr = Class(name="limp::RealLiteralExpr")
limp_StringLiteralExpr = Class(name="limp::StringLiteralExpr")
limp_InitExpr = Class(name="limp::InitExpr")
limp_SecondInit = Class(name="limp::SecondInit")
limp_IdExpr = Class(name="limp::IdExpr")
limp_FcnCallExpr = Class(name="limp::FcnCallExpr")
limp_TupleType = Class(name="limp::TupleType")
limp_ArrayAccessExpr = Class(name="limp::ArrayAccessExpr")
limp_ArrayUpdateExpr = Class(name="limp::ArrayUpdateExpr")
limp_FreshVariable = Class(name="limp::FreshVariable")

# limp_Specification class attributes and methods

# limp_Declaration class attributes and methods

# limp_Comment class attributes and methods
limp_Comment_comment: Property = Property(name="comment", type=StringType)
limp_Comment.attributes={limp_Comment_comment}

# Declaration class attributes and methods

# limp_Import class attributes and methods
limp_Import_importURI: Property = Property(name="importURI", type=StringType)
limp_Import.attributes={limp_Import_importURI}

# limp_OutputArgList class attributes and methods

# limp_AttributeBlock class attributes and methods

# limp_LocalFunction class attributes and methods
limp_LocalFunction_name: Property = Property(name="name", type=StringType)
limp_LocalFunction.attributes={limp_LocalFunction_name}

# limp_VarBlock class attributes and methods

# limp_EquationBlock class attributes and methods

# limp_LocalProcedure class attributes and methods
limp_LocalProcedure_name: Property = Property(name="name", type=StringType)
limp_LocalProcedure.attributes={limp_LocalProcedure_name}

# limp_StatementBlock class attributes and methods

# limp_ExternalFunction class attributes and methods
limp_ExternalFunction_name: Property = Property(name="name", type=StringType)
limp_ExternalFunction.attributes={limp_ExternalFunction_name}

# FunctionRef class attributes and methods

# limp_InputArgList class attributes and methods

# limp_OutputArg class attributes and methods

# limp_ExternalProcedure class attributes and methods
limp_ExternalProcedure_name: Property = Property(name="name", type=StringType)
limp_ExternalProcedure.attributes={limp_ExternalProcedure_name}

# limp_ArrayTypeDef class attributes and methods
limp_ArrayTypeDef_size: Property = Property(name="size", type=StringType)
limp_ArrayTypeDef.attributes={limp_ArrayTypeDef_size}

# limp_Type class attributes and methods

# limp_AbstractTypeDef class attributes and methods

# limp_ConstantDeclaration class attributes and methods

# limp_Expr class attributes and methods

# limp_GlobalDeclaration class attributes and methods

# limp_VariableRef class attributes and methods
limp_VariableRef_name: Property = Property(name="name", type=StringType)
limp_VariableRef.attributes={limp_VariableRef_name}

# limp_InputArg class attributes and methods

# limp_LocalArg class attributes and methods

# limp_TypeDeclaration class attributes and methods
limp_TypeDeclaration_name: Property = Property(name="name", type=StringType)
limp_TypeDeclaration.attributes={limp_TypeDeclaration_name}

# limp_EnumTypeDef class attributes and methods

# TypeDeclaration class attributes and methods

# limp_EnumValue class attributes and methods

# VariableRef class attributes and methods

# limp_RecordTypeDef class attributes and methods

# limp_RecordFieldType class attributes and methods
limp_RecordFieldType_fieldName: Property = Property(name="fieldName", type=StringType)
limp_RecordFieldType.attributes={limp_RecordFieldType_fieldName}

# limp_DefineUseRef class attributes and methods

# limp_Define class attributes and methods

# limp_Uses class attributes and methods

# limp_Statement class attributes and methods

# limp_VoidStatement class attributes and methods

# Statement class attributes and methods

# Equation class attributes and methods

# limp_AssignmentStatement class attributes and methods

# limp_IdList class attributes and methods

# limp_IfThenElseStatement class attributes and methods

# limp_Else class attributes and methods

# limp_Attribute class attributes and methods

# limp_Precondition class attributes and methods
limp_Precondition_name: Property = Property(name="name", type=StringType)
limp_Precondition.attributes={limp_Precondition_name}

# Attribute class attributes and methods

# limp_Postcondition class attributes and methods
limp_Postcondition_name: Property = Property(name="name", type=StringType)
limp_Postcondition.attributes={limp_Postcondition_name}

# limp_LabelStatement class attributes and methods
limp_LabelStatement_name: Property = Property(name="name", type=StringType)
limp_LabelStatement.attributes={limp_LabelStatement_name}

# limp_GotoStatement class attributes and methods

# limp_Equation class attributes and methods

# limp_FunctionRef class attributes and methods

# limp_ArrayExpr class attributes and methods

# Expr class attributes and methods

# limp_RecordExpr class attributes and methods

# limp_RecordFieldExpr class attributes and methods
limp_RecordFieldExpr_fieldName: Property = Property(name="fieldName", type=StringType)
limp_RecordFieldExpr.attributes={limp_RecordFieldExpr_fieldName}

# limp_WhileStatement class attributes and methods

# limp_ForStatement class attributes and methods

# limp_VoidType class attributes and methods

# Type class attributes and methods

# limp_BoolType class attributes and methods

# limp_IntegerType class attributes and methods

# limp_RealType class attributes and methods

# limp_StringType class attributes and methods

# limp_EnumType class attributes and methods

# limp_RecordType class attributes and methods

# limp_ArrayType class attributes and methods

# limp_AbstractType class attributes and methods

# limp_NamedType class attributes and methods

# limp_SomeAttributeBlock class attributes and methods

# AttributeBlock class attributes and methods

# limp_NoAttributeBlock class attributes and methods

# limp_BreakStatement class attributes and methods

# limp_ContinueStatement class attributes and methods

# limp_ReturnStatement class attributes and methods

# limp_ElseBlock class attributes and methods

# Else class attributes and methods

# limp_ExprList class attributes and methods

# limp_TypeAlias class attributes and methods

# limp_SomeVarBlock class attributes and methods

# VarBlock class attributes and methods

# limp_NoVarBlock class attributes and methods

# limp_ChoiceExpr class attributes and methods

# limp_BinaryExpr class attributes and methods
limp_BinaryExpr_op: Property = Property(name="op", type=StringType)
limp_BinaryExpr.attributes={limp_BinaryExpr_op}

# limp_UnaryNegationExpr class attributes and methods

# limp_UnaryMinusExpr class attributes and methods

# limp_RecordAccessExpr class attributes and methods
limp_RecordAccessExpr_field: Property = Property(name="field", type=StringType)
limp_RecordAccessExpr.attributes={limp_RecordAccessExpr_field}

# limp_RecordUpdateExpr class attributes and methods
limp_RecordUpdateExpr_field: Property = Property(name="field", type=StringType)
limp_RecordUpdateExpr.attributes={limp_RecordUpdateExpr_field}

# limp_ElseIf class attributes and methods

# limp_NoElse class attributes and methods

# limp_IfThenElseExpr class attributes and methods

# limp_BooleanLiteralExpr class attributes and methods
limp_BooleanLiteralExpr_boolVal: Property = Property(name="boolVal", type=StringType)
limp_BooleanLiteralExpr.attributes={limp_BooleanLiteralExpr_boolVal}

# limp_IntegerLiteralExpr class attributes and methods
limp_IntegerLiteralExpr_intVal: Property = Property(name="intVal", type=StringType)
limp_IntegerLiteralExpr.attributes={limp_IntegerLiteralExpr_intVal}

# limp_IntegerWildCardExpr class attributes and methods

# limp_RealLiteralExpr class attributes and methods
limp_RealLiteralExpr_realVal: Property = Property(name="realVal", type=StringType)
limp_RealLiteralExpr.attributes={limp_RealLiteralExpr_realVal}

# limp_StringLiteralExpr class attributes and methods
limp_StringLiteralExpr_stringVal: Property = Property(name="stringVal", type=StringType)
limp_StringLiteralExpr.attributes={limp_StringLiteralExpr_stringVal}

# limp_InitExpr class attributes and methods

# limp_SecondInit class attributes and methods

# limp_IdExpr class attributes and methods

# limp_FcnCallExpr class attributes and methods

# limp_TupleType class attributes and methods

# limp_ArrayAccessExpr class attributes and methods

# limp_ArrayUpdateExpr class attributes and methods

# limp_FreshVariable class attributes and methods
limp_FreshVariable_value: Property = Property(name="value", type=StringType)
limp_FreshVariable.attributes={limp_FreshVariable_value}

# Relationships
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="limp_Declaration", type=limp_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_Specification", type=limp_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs4: BinaryAssociation = BinaryAssociation(
    name="inputs4",
    ends={
        Property(name="limp_InputArgList5", type=limp_ExternalProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ExternalProcedure", type=limp_InputArgList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputs6: BinaryAssociation = BinaryAssociation(
    name="outputs6",
    ends={
        Property(name="limp_OutputArgList", type=limp_ExternalProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ExternalProcedure7", type=limp_OutputArgList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeBlock8: BinaryAssociation = BinaryAssociation(
    name="attributeBlock8",
    ends={
        Property(name="limp_AttributeBlock", type=limp_ExternalProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ExternalProcedure9", type=limp_AttributeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputs10: BinaryAssociation = BinaryAssociation(
    name="inputs10",
    ends={
        Property(name="limp_InputArgList11", type=limp_LocalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_LocalFunction", type=limp_InputArgList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output12: BinaryAssociation = BinaryAssociation(
    name="output12",
    ends={
        Property(name="limp_OutputArg14", type=limp_LocalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_LocalFunction13", type=limp_OutputArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varBlock15: BinaryAssociation = BinaryAssociation(
    name="varBlock15",
    ends={
        Property(name="limp_VarBlock", type=limp_LocalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_LocalFunction16", type=limp_VarBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equationBlock17: BinaryAssociation = BinaryAssociation(
    name="equationBlock17",
    ends={
        Property(name="limp_EquationBlock", type=limp_LocalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_LocalFunction18", type=limp_EquationBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputs19: BinaryAssociation = BinaryAssociation(
    name="inputs19",
    ends={
        Property(name="limp_InputArgList20", type=limp_LocalProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_LocalProcedure", type=limp_InputArgList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputs21: BinaryAssociation = BinaryAssociation(
    name="outputs21",
    ends={
        Property(name="limp_OutputArgList23", type=limp_LocalProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_LocalProcedure22", type=limp_OutputArgList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varBlock24: BinaryAssociation = BinaryAssociation(
    name="varBlock24",
    ends={
        Property(name="limp_VarBlock26", type=limp_LocalProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_LocalProcedure25", type=limp_VarBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeBlock27: BinaryAssociation = BinaryAssociation(
    name="attributeBlock27",
    ends={
        Property(name="limp_AttributeBlock29", type=limp_LocalProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_LocalProcedure28", type=limp_AttributeBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementblock30: BinaryAssociation = BinaryAssociation(
    name="statementblock30",
    ends={
        Property(name="limp_StatementBlock", type=limp_LocalProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_LocalProcedure31", type=limp_StatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputs1: BinaryAssociation = BinaryAssociation(
    name="inputs1",
    ends={
        Property(name="limp_InputArgList", type=limp_ExternalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ExternalFunction", type=limp_InputArgList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output2: BinaryAssociation = BinaryAssociation(
    name="output2",
    ends={
        Property(name="limp_OutputArg", type=limp_ExternalFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ExternalFunction3", type=limp_OutputArg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseType34: BinaryAssociation = BinaryAssociation(
    name="baseType34",
    ends={
        Property(name="limp_Type", type=limp_ArrayTypeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ArrayTypeDef", type=limp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldType35: BinaryAssociation = BinaryAssociation(
    name="fieldType35",
    ends={
        Property(name="limp_Type37", type=limp_RecordFieldType, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_RecordFieldType36", type=limp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="limp_Type39", type=limp_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ConstantDeclaration", type=limp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr40: BinaryAssociation = BinaryAssociation(
    name="expr40",
    ends={
        Property(name="limp_Expr", type=limp_ConstantDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ConstantDeclaration41", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type42: BinaryAssociation = BinaryAssociation(
    name="type42",
    ends={
        Property(name="limp_Type43", type=limp_GlobalDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_GlobalDeclaration", type=limp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inputArgs44: BinaryAssociation = BinaryAssociation(
    name="inputArgs44",
    ends={
        Property(name="limp_InputArg", type=limp_InputArgList, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_InputArgList45", type=limp_InputArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="limp_Type48", type=limp_InputArg, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_InputArg47", type=limp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="limp_Type50", type=limp_LocalArg, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_LocalArg", type=limp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputArgs51: BinaryAssociation = BinaryAssociation(
    name="outputArgs51",
    ends={
        Property(name="limp_OutputArg53", type=limp_OutputArgList, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_OutputArgList52", type=limp_OutputArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerations32: BinaryAssociation = BinaryAssociation(
    name="enumerations32",
    ends={
        Property(name="limp_EnumValue", type=limp_EnumTypeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_EnumTypeDef", type=limp_EnumValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields33: BinaryAssociation = BinaryAssociation(
    name="fields33",
    ends={
        Property(name="limp_RecordFieldType", type=limp_RecordTypeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_RecordTypeDef", type=limp_RecordFieldType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr59: BinaryAssociation = BinaryAssociation(
    name="expr59",
    ends={
        Property(name="limp_Postcondition", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="limp_Expr60", type=limp_Postcondition, multiplicity=Multiplicity(1, 1))
    }
)
referenceExpr61: BinaryAssociation = BinaryAssociation(
    name="referenceExpr61",
    ends={
        Property(name="limp_Expr62", type=limp_DefineUseRef, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_DefineUseRef", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements63: BinaryAssociation = BinaryAssociation(
    name="elements63",
    ends={
        Property(name="limp_DefineUseRef64", type=limp_Define, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_Define", type=limp_DefineUseRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements65: BinaryAssociation = BinaryAssociation(
    name="elements65",
    ends={
        Property(name="limp_DefineUseRef66", type=limp_Uses, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_Uses", type=limp_DefineUseRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements67: BinaryAssociation = BinaryAssociation(
    name="statements67",
    ends={
        Property(name="limp_Statement", type=limp_StatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_StatementBlock68", type=limp_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr69: BinaryAssociation = BinaryAssociation(
    name="expr69",
    ends={
        Property(name="limp_Expr70", type=limp_VoidStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_VoidStatement", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ids71: BinaryAssociation = BinaryAssociation(
    name="ids71",
    ends={
        Property(name="limp_IdList", type=limp_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_AssignmentStatement", type=limp_IdList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs72: BinaryAssociation = BinaryAssociation(
    name="rhs72",
    ends={
        Property(name="limp_Expr74", type=limp_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_AssignmentStatement73", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond75: BinaryAssociation = BinaryAssociation(
    name="cond75",
    ends={
        Property(name="limp_Expr76", type=limp_IfThenElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_IfThenElseStatement", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBlock77: BinaryAssociation = BinaryAssociation(
    name="thenBlock77",
    ends={
        Property(name="limp_StatementBlock79", type=limp_IfThenElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_IfThenElseStatement78", type=limp_StatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else80: BinaryAssociation = BinaryAssociation(
    name="else80",
    ends={
        Property(name="limp_Else", type=limp_IfThenElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_IfThenElseStatement81", type=limp_Else, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type54: BinaryAssociation = BinaryAssociation(
    name="type54",
    ends={
        Property(name="limp_Type56", type=limp_OutputArg, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_OutputArg55", type=limp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr57: BinaryAssociation = BinaryAssociation(
    name="expr57",
    ends={
        Property(name="limp_Expr58", type=limp_Precondition, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_Precondition", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block95: BinaryAssociation = BinaryAssociation(
    name="block95",
    ends={
        Property(name="limp_StatementBlock97", type=limp_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ForStatement96", type=limp_StatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label98: BinaryAssociation = BinaryAssociation(
    name="label98",
    ends={
        Property(name="limp_LabelStatement", type=limp_GotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_GotoStatement", type=limp_LabelStatement, multiplicity=Multiplicity(0, 1))
    }
)
whenExpr99: BinaryAssociation = BinaryAssociation(
    name="whenExpr99",
    ends={
        Property(name="limp_Expr101", type=limp_GotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_GotoStatement100", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
equations102: BinaryAssociation = BinaryAssociation(
    name="equations102",
    ends={
        Property(name="limp_Equation", type=limp_EquationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_EquationBlock103", type=limp_Equation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ids104: BinaryAssociation = BinaryAssociation(
    name="ids104",
    ends={
        Property(name="limp_VariableRef", type=limp_IdList, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_IdList105", type=limp_VariableRef, multiplicity=Multiplicity(0, 9999))
    }
)
arrayDefinition106: BinaryAssociation = BinaryAssociation(
    name="arrayDefinition106",
    ends={
        Property(name="limp_ArrayTypeDef107", type=limp_ArrayExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ArrayExpr", type=limp_ArrayTypeDef, multiplicity=Multiplicity(0, 1))
    }
)
exprList108: BinaryAssociation = BinaryAssociation(
    name="exprList108",
    ends={
        Property(name="limp_Expr110", type=limp_ArrayExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ArrayExpr109", type=limp_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recordDefinition111: BinaryAssociation = BinaryAssociation(
    name="recordDefinition111",
    ends={
        Property(name="limp_RecordTypeDef112", type=limp_RecordExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_RecordExpr", type=limp_RecordTypeDef, multiplicity=Multiplicity(0, 1))
    }
)
fieldExprList113: BinaryAssociation = BinaryAssociation(
    name="fieldExprList113",
    ends={
        Property(name="limp_RecordFieldExpr", type=limp_RecordExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_RecordExpr114", type=limp_RecordFieldExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldExpr115: BinaryAssociation = BinaryAssociation(
    name="fieldExpr115",
    ends={
        Property(name="limp_Expr117", type=limp_RecordFieldExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_RecordFieldExpr116", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond82: BinaryAssociation = BinaryAssociation(
    name="cond82",
    ends={
        Property(name="limp_Expr83", type=limp_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_WhileStatement", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block84: BinaryAssociation = BinaryAssociation(
    name="block84",
    ends={
        Property(name="limp_StatementBlock86", type=limp_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_WhileStatement85", type=limp_StatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initStatement87: BinaryAssociation = BinaryAssociation(
    name="initStatement87",
    ends={
        Property(name="limp_AssignmentStatement88", type=limp_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ForStatement", type=limp_AssignmentStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
limitExpr89: BinaryAssociation = BinaryAssociation(
    name="limitExpr89",
    ends={
        Property(name="limp_Expr91", type=limp_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ForStatement90", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incrementStatement92: BinaryAssociation = BinaryAssociation(
    name="incrementStatement92",
    ends={
        Property(name="limp_AssignmentStatement94", type=limp_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ForStatement93", type=limp_AssignmentStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumDef124: BinaryAssociation = BinaryAssociation(
    name="enumDef124",
    ends={
        Property(name="limp_EnumTypeDef125", type=limp_EnumType, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_EnumType", type=limp_EnumTypeDef, multiplicity=Multiplicity(0, 1))
    }
)
recordDef126: BinaryAssociation = BinaryAssociation(
    name="recordDef126",
    ends={
        Property(name="limp_RecordTypeDef127", type=limp_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_RecordType", type=limp_RecordTypeDef, multiplicity=Multiplicity(0, 1))
    }
)
arrayDef128: BinaryAssociation = BinaryAssociation(
    name="arrayDef128",
    ends={
        Property(name="limp_ArrayTypeDef129", type=limp_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ArrayType", type=limp_ArrayTypeDef, multiplicity=Multiplicity(0, 1))
    }
)
abstractDef130: BinaryAssociation = BinaryAssociation(
    name="abstractDef130",
    ends={
        Property(name="limp_AbstractTypeDef", type=limp_AbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_AbstractType", type=limp_AbstractTypeDef, multiplicity=Multiplicity(0, 1))
    }
)
alias131: BinaryAssociation = BinaryAssociation(
    name="alias131",
    ends={
        Property(name="limp_TypeAlias132", type=limp_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_NamedType", type=limp_TypeAlias, multiplicity=Multiplicity(0, 1))
    }
)
attributeList133: BinaryAssociation = BinaryAssociation(
    name="attributeList133",
    ends={
        Property(name="limp_Attribute", type=limp_SomeAttributeBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_SomeAttributeBlock", type=limp_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprList118: BinaryAssociation = BinaryAssociation(
    name="exprList118",
    ends={
        Property(name="limp_Expr119", type=limp_ExprList, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ExprList", type=limp_Expr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type120: BinaryAssociation = BinaryAssociation(
    name="type120",
    ends={
        Property(name="limp_Type121", type=limp_TypeAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_TypeAlias", type=limp_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
locals122: BinaryAssociation = BinaryAssociation(
    name="locals122",
    ends={
        Property(name="limp_LocalArg123", type=limp_SomeVarBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_SomeVarBlock", type=limp_LocalArg, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseExpr143: BinaryAssociation = BinaryAssociation(
    name="elseExpr143",
    ends={
        Property(name="limp_Expr145", type=limp_IfThenElseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_IfThenElseExpr144", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first146: BinaryAssociation = BinaryAssociation(
    name="first146",
    ends={
        Property(name="limp_Expr147", type=limp_ChoiceExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ChoiceExpr", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
second148: BinaryAssociation = BinaryAssociation(
    name="second148",
    ends={
        Property(name="limp_Expr150", type=limp_ChoiceExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ChoiceExpr149", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left151: BinaryAssociation = BinaryAssociation(
    name="left151",
    ends={
        Property(name="limp_Expr152", type=limp_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_BinaryExpr", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right153: BinaryAssociation = BinaryAssociation(
    name="right153",
    ends={
        Property(name="limp_Expr155", type=limp_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_BinaryExpr154", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr156: BinaryAssociation = BinaryAssociation(
    name="expr156",
    ends={
        Property(name="limp_Expr157", type=limp_UnaryNegationExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_UnaryNegationExpr", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr158: BinaryAssociation = BinaryAssociation(
    name="expr158",
    ends={
        Property(name="limp_Expr159", type=limp_UnaryMinusExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_UnaryMinusExpr", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record160: BinaryAssociation = BinaryAssociation(
    name="record160",
    ends={
        Property(name="limp_Expr161", type=limp_RecordAccessExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_RecordAccessExpr", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
record162: BinaryAssociation = BinaryAssociation(
    name="record162",
    ends={
        Property(name="limp_Expr163", type=limp_RecordUpdateExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_RecordUpdateExpr", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block134: BinaryAssociation = BinaryAssociation(
    name="block134",
    ends={
        Property(name="limp_StatementBlock135", type=limp_ElseBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ElseBlock", type=limp_StatementBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifThenElse136: BinaryAssociation = BinaryAssociation(
    name="ifThenElse136",
    ends={
        Property(name="limp_IfThenElseStatement137", type=limp_ElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ElseIf", type=limp_IfThenElseStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condExpr138: BinaryAssociation = BinaryAssociation(
    name="condExpr138",
    ends={
        Property(name="limp_Expr139", type=limp_IfThenElseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_IfThenElseExpr", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenExpr140: BinaryAssociation = BinaryAssociation(
    name="thenExpr140",
    ends={
        Property(name="limp_Expr142", type=limp_IfThenElseExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_IfThenElseExpr141", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value174: BinaryAssociation = BinaryAssociation(
    name="value174",
    ends={
        Property(name="limp_Expr176", type=limp_ArrayUpdateExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ArrayUpdateExpr175", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id177: BinaryAssociation = BinaryAssociation(
    name="id177",
    ends={
        Property(name="limp_VariableRef178", type=limp_InitExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_InitExpr", type=limp_VariableRef, multiplicity=Multiplicity(0, 1))
    }
)
id179: BinaryAssociation = BinaryAssociation(
    name="id179",
    ends={
        Property(name="limp_VariableRef180", type=limp_SecondInit, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_SecondInit", type=limp_VariableRef, multiplicity=Multiplicity(0, 1))
    }
)
id181: BinaryAssociation = BinaryAssociation(
    name="id181",
    ends={
        Property(name="limp_VariableRef182", type=limp_IdExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_IdExpr", type=limp_VariableRef, multiplicity=Multiplicity(0, 1))
    }
)
id183: BinaryAssociation = BinaryAssociation(
    name="id183",
    ends={
        Property(name="limp_FunctionRef", type=limp_FcnCallExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_FcnCallExpr", type=limp_FunctionRef, multiplicity=Multiplicity(0, 1))
    }
)
exprs184: BinaryAssociation = BinaryAssociation(
    name="exprs184",
    ends={
        Property(name="limp_ExprList186", type=limp_FcnCallExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_FcnCallExpr185", type=limp_ExprList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeList187: BinaryAssociation = BinaryAssociation(
    name="typeList187",
    ends={
        Property(name="limp_Type188", type=limp_TupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_TupleType", type=limp_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value164: BinaryAssociation = BinaryAssociation(
    name="value164",
    ends={
        Property(name="limp_Expr166", type=limp_RecordUpdateExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_RecordUpdateExpr165", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array167: BinaryAssociation = BinaryAssociation(
    name="array167",
    ends={
        Property(name="limp_Expr168", type=limp_ArrayAccessExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ArrayAccessExpr", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index169: BinaryAssociation = BinaryAssociation(
    name="index169",
    ends={
        Property(name="limp_Expr171", type=limp_ArrayAccessExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ArrayAccessExpr170", type=limp_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
access172: BinaryAssociation = BinaryAssociation(
    name="access172",
    ends={
        Property(name="limp_ArrayAccessExpr173", type=limp_ArrayUpdateExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="limp_ArrayUpdateExpr", type=limp_ArrayAccessExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_limp_Comment_Declaration = Generalization(general=Declaration, specific=limp_Comment)
gen_limp_LocalFunction_Declaration = Generalization(general=Declaration, specific=limp_LocalFunction)
gen_limp_LocalFunction_FunctionRef = Generalization(general=FunctionRef, specific=limp_LocalFunction)
gen_limp_LocalProcedure_Declaration = Generalization(general=Declaration, specific=limp_LocalProcedure)
gen_limp_LocalProcedure_FunctionRef = Generalization(general=FunctionRef, specific=limp_LocalProcedure)
gen_limp_Import_Declaration = Generalization(general=Declaration, specific=limp_Import)
gen_limp_ExternalFunction_Declaration = Generalization(general=Declaration, specific=limp_ExternalFunction)
gen_limp_ExternalFunction_FunctionRef = Generalization(general=FunctionRef, specific=limp_ExternalFunction)
gen_limp_ExternalProcedure_Declaration = Generalization(general=Declaration, specific=limp_ExternalProcedure)
gen_limp_ExternalProcedure_FunctionRef = Generalization(general=FunctionRef, specific=limp_ExternalProcedure)
gen_limp_ArrayTypeDef_TypeDeclaration = Generalization(general=TypeDeclaration, specific=limp_ArrayTypeDef)
gen_limp_AbstractTypeDef_TypeDeclaration = Generalization(general=TypeDeclaration, specific=limp_AbstractTypeDef)
gen_limp_ConstantDeclaration_Declaration = Generalization(general=Declaration, specific=limp_ConstantDeclaration)
gen_limp_ConstantDeclaration_VariableRef = Generalization(general=VariableRef, specific=limp_ConstantDeclaration)
gen_limp_GlobalDeclaration_Declaration = Generalization(general=Declaration, specific=limp_GlobalDeclaration)
gen_limp_GlobalDeclaration_VariableRef = Generalization(general=VariableRef, specific=limp_GlobalDeclaration)
gen_limp_InputArg_VariableRef = Generalization(general=VariableRef, specific=limp_InputArg)
gen_limp_LocalArg_VariableRef = Generalization(general=VariableRef, specific=limp_LocalArg)
gen_limp_TypeDeclaration_Declaration = Generalization(general=Declaration, specific=limp_TypeDeclaration)
gen_limp_EnumTypeDef_TypeDeclaration = Generalization(general=TypeDeclaration, specific=limp_EnumTypeDef)
gen_limp_EnumValue_VariableRef = Generalization(general=VariableRef, specific=limp_EnumValue)
gen_limp_RecordTypeDef_TypeDeclaration = Generalization(general=TypeDeclaration, specific=limp_RecordTypeDef)
gen_limp_Define_Attribute = Generalization(general=Attribute, specific=limp_Define)
gen_limp_Uses_Attribute = Generalization(general=Attribute, specific=limp_Uses)
gen_limp_VoidStatement_Statement = Generalization(general=Statement, specific=limp_VoidStatement)
gen_limp_VoidStatement_Equation = Generalization(general=Equation, specific=limp_VoidStatement)
gen_limp_AssignmentStatement_Statement = Generalization(general=Statement, specific=limp_AssignmentStatement)
gen_limp_AssignmentStatement_Equation = Generalization(general=Equation, specific=limp_AssignmentStatement)
gen_limp_IfThenElseStatement_Statement = Generalization(general=Statement, specific=limp_IfThenElseStatement)
gen_limp_OutputArg_VariableRef = Generalization(general=VariableRef, specific=limp_OutputArg)
gen_limp_Precondition_Attribute = Generalization(general=Attribute, specific=limp_Precondition)
gen_limp_Postcondition_Attribute = Generalization(general=Attribute, specific=limp_Postcondition)
gen_limp_LabelStatement_Statement = Generalization(general=Statement, specific=limp_LabelStatement)
gen_limp_GotoStatement_Statement = Generalization(general=Statement, specific=limp_GotoStatement)
gen_limp_ArrayExpr_Expr = Generalization(general=Expr, specific=limp_ArrayExpr)
gen_limp_RecordExpr_Expr = Generalization(general=Expr, specific=limp_RecordExpr)
gen_limp_WhileStatement_Statement = Generalization(general=Statement, specific=limp_WhileStatement)
gen_limp_ForStatement_Statement = Generalization(general=Statement, specific=limp_ForStatement)
gen_limp_VoidType_Type = Generalization(general=Type, specific=limp_VoidType)
gen_limp_BoolType_Type = Generalization(general=Type, specific=limp_BoolType)
gen_limp_IntegerType_Type = Generalization(general=Type, specific=limp_IntegerType)
gen_limp_RealType_Type = Generalization(general=Type, specific=limp_RealType)
gen_limp_StringType_Type = Generalization(general=Type, specific=limp_StringType)
gen_limp_EnumType_Type = Generalization(general=Type, specific=limp_EnumType)
gen_limp_RecordType_Type = Generalization(general=Type, specific=limp_RecordType)
gen_limp_ArrayType_Type = Generalization(general=Type, specific=limp_ArrayType)
gen_limp_AbstractType_Type = Generalization(general=Type, specific=limp_AbstractType)
gen_limp_NamedType_Type = Generalization(general=Type, specific=limp_NamedType)
gen_limp_SomeAttributeBlock_AttributeBlock = Generalization(general=AttributeBlock, specific=limp_SomeAttributeBlock)
gen_limp_NoAttributeBlock_AttributeBlock = Generalization(general=AttributeBlock, specific=limp_NoAttributeBlock)
gen_limp_BreakStatement_Statement = Generalization(general=Statement, specific=limp_BreakStatement)
gen_limp_ContinueStatement_Statement = Generalization(general=Statement, specific=limp_ContinueStatement)
gen_limp_ReturnStatement_Statement = Generalization(general=Statement, specific=limp_ReturnStatement)
gen_limp_ElseBlock_Else = Generalization(general=Else, specific=limp_ElseBlock)
gen_limp_TypeAlias_TypeDeclaration = Generalization(general=TypeDeclaration, specific=limp_TypeAlias)
gen_limp_SomeVarBlock_VarBlock = Generalization(general=VarBlock, specific=limp_SomeVarBlock)
gen_limp_NoVarBlock_VarBlock = Generalization(general=VarBlock, specific=limp_NoVarBlock)
gen_limp_ChoiceExpr_Expr = Generalization(general=Expr, specific=limp_ChoiceExpr)
gen_limp_BinaryExpr_Expr = Generalization(general=Expr, specific=limp_BinaryExpr)
gen_limp_UnaryNegationExpr_Expr = Generalization(general=Expr, specific=limp_UnaryNegationExpr)
gen_limp_UnaryMinusExpr_Expr = Generalization(general=Expr, specific=limp_UnaryMinusExpr)
gen_limp_RecordAccessExpr_Expr = Generalization(general=Expr, specific=limp_RecordAccessExpr)
gen_limp_RecordUpdateExpr_Expr = Generalization(general=Expr, specific=limp_RecordUpdateExpr)
gen_limp_ElseIf_Else = Generalization(general=Else, specific=limp_ElseIf)
gen_limp_NoElse_Else = Generalization(general=Else, specific=limp_NoElse)
gen_limp_IfThenElseExpr_Expr = Generalization(general=Expr, specific=limp_IfThenElseExpr)
gen_limp_BooleanLiteralExpr_Expr = Generalization(general=Expr, specific=limp_BooleanLiteralExpr)
gen_limp_IntegerLiteralExpr_Expr = Generalization(general=Expr, specific=limp_IntegerLiteralExpr)
gen_limp_IntegerWildCardExpr_Expr = Generalization(general=Expr, specific=limp_IntegerWildCardExpr)
gen_limp_RealLiteralExpr_Expr = Generalization(general=Expr, specific=limp_RealLiteralExpr)
gen_limp_StringLiteralExpr_Expr = Generalization(general=Expr, specific=limp_StringLiteralExpr)
gen_limp_InitExpr_Expr = Generalization(general=Expr, specific=limp_InitExpr)
gen_limp_SecondInit_Expr = Generalization(general=Expr, specific=limp_SecondInit)
gen_limp_IdExpr_Expr = Generalization(general=Expr, specific=limp_IdExpr)
gen_limp_FcnCallExpr_Expr = Generalization(general=Expr, specific=limp_FcnCallExpr)
gen_limp_TupleType_Type = Generalization(general=Type, specific=limp_TupleType)
gen_limp_ArrayAccessExpr_Expr = Generalization(general=Expr, specific=limp_ArrayAccessExpr)
gen_limp_ArrayUpdateExpr_Expr = Generalization(general=Expr, specific=limp_ArrayUpdateExpr)
gen_limp_FreshVariable_Expr = Generalization(general=Expr, specific=limp_FreshVariable)

# Domain Model
domain_model = DomainModel(
    name="limp",
    types={limp_Specification, limp_Declaration, limp_Comment, Declaration, limp_Import, limp_OutputArgList, limp_AttributeBlock, limp_LocalFunction, limp_VarBlock, limp_EquationBlock, limp_LocalProcedure, limp_StatementBlock, limp_ExternalFunction, FunctionRef, limp_InputArgList, limp_OutputArg, limp_ExternalProcedure, limp_ArrayTypeDef, limp_Type, limp_AbstractTypeDef, limp_ConstantDeclaration, limp_Expr, limp_GlobalDeclaration, limp_VariableRef, limp_InputArg, limp_LocalArg, limp_TypeDeclaration, limp_EnumTypeDef, TypeDeclaration, limp_EnumValue, VariableRef, limp_RecordTypeDef, limp_RecordFieldType, limp_DefineUseRef, limp_Define, limp_Uses, limp_Statement, limp_VoidStatement, Statement, Equation, limp_AssignmentStatement, limp_IdList, limp_IfThenElseStatement, limp_Else, limp_Attribute, limp_Precondition, Attribute, limp_Postcondition, limp_LabelStatement, limp_GotoStatement, limp_Equation, limp_FunctionRef, limp_ArrayExpr, Expr, limp_RecordExpr, limp_RecordFieldExpr, limp_WhileStatement, limp_ForStatement, limp_VoidType, Type, limp_BoolType, limp_IntegerType, limp_RealType, limp_StringType, limp_EnumType, limp_RecordType, limp_ArrayType, limp_AbstractType, limp_NamedType, limp_SomeAttributeBlock, AttributeBlock, limp_NoAttributeBlock, limp_BreakStatement, limp_ContinueStatement, limp_ReturnStatement, limp_ElseBlock, Else, limp_ExprList, limp_TypeAlias, limp_SomeVarBlock, VarBlock, limp_NoVarBlock, limp_ChoiceExpr, limp_BinaryExpr, limp_UnaryNegationExpr, limp_UnaryMinusExpr, limp_RecordAccessExpr, limp_RecordUpdateExpr, limp_ElseIf, limp_NoElse, limp_IfThenElseExpr, limp_BooleanLiteralExpr, limp_IntegerLiteralExpr, limp_IntegerWildCardExpr, limp_RealLiteralExpr, limp_StringLiteralExpr, limp_InitExpr, limp_SecondInit, limp_IdExpr, limp_FcnCallExpr, limp_TupleType, limp_ArrayAccessExpr, limp_ArrayUpdateExpr, limp_FreshVariable},
    associations={declarations0, inputs4, outputs6, attributeBlock8, inputs10, output12, varBlock15, equationBlock17, inputs19, outputs21, varBlock24, attributeBlock27, statementblock30, inputs1, output2, baseType34, fieldType35, type38, expr40, type42, inputArgs44, type46, type49, outputArgs51, enumerations32, fields33, expr59, referenceExpr61, elements63, elements65, statements67, expr69, ids71, rhs72, cond75, thenBlock77, else80, type54, expr57, block95, label98, whenExpr99, equations102, ids104, arrayDefinition106, exprList108, recordDefinition111, fieldExprList113, fieldExpr115, cond82, block84, initStatement87, limitExpr89, incrementStatement92, enumDef124, recordDef126, arrayDef128, abstractDef130, alias131, attributeList133, exprList118, type120, locals122, elseExpr143, first146, second148, left151, right153, expr156, expr158, record160, record162, block134, ifThenElse136, condExpr138, thenExpr140, value174, id177, id179, id181, id183, exprs184, typeList187, value164, array167, index169, access172},
    generalizations={gen_limp_Comment_Declaration, gen_limp_LocalFunction_Declaration, gen_limp_LocalFunction_FunctionRef, gen_limp_LocalProcedure_Declaration, gen_limp_LocalProcedure_FunctionRef, gen_limp_Import_Declaration, gen_limp_ExternalFunction_Declaration, gen_limp_ExternalFunction_FunctionRef, gen_limp_ExternalProcedure_Declaration, gen_limp_ExternalProcedure_FunctionRef, gen_limp_ArrayTypeDef_TypeDeclaration, gen_limp_AbstractTypeDef_TypeDeclaration, gen_limp_ConstantDeclaration_Declaration, gen_limp_ConstantDeclaration_VariableRef, gen_limp_GlobalDeclaration_Declaration, gen_limp_GlobalDeclaration_VariableRef, gen_limp_InputArg_VariableRef, gen_limp_LocalArg_VariableRef, gen_limp_TypeDeclaration_Declaration, gen_limp_EnumTypeDef_TypeDeclaration, gen_limp_EnumValue_VariableRef, gen_limp_RecordTypeDef_TypeDeclaration, gen_limp_Define_Attribute, gen_limp_Uses_Attribute, gen_limp_VoidStatement_Statement, gen_limp_VoidStatement_Equation, gen_limp_AssignmentStatement_Statement, gen_limp_AssignmentStatement_Equation, gen_limp_IfThenElseStatement_Statement, gen_limp_OutputArg_VariableRef, gen_limp_Precondition_Attribute, gen_limp_Postcondition_Attribute, gen_limp_LabelStatement_Statement, gen_limp_GotoStatement_Statement, gen_limp_ArrayExpr_Expr, gen_limp_RecordExpr_Expr, gen_limp_WhileStatement_Statement, gen_limp_ForStatement_Statement, gen_limp_VoidType_Type, gen_limp_BoolType_Type, gen_limp_IntegerType_Type, gen_limp_RealType_Type, gen_limp_StringType_Type, gen_limp_EnumType_Type, gen_limp_RecordType_Type, gen_limp_ArrayType_Type, gen_limp_AbstractType_Type, gen_limp_NamedType_Type, gen_limp_SomeAttributeBlock_AttributeBlock, gen_limp_NoAttributeBlock_AttributeBlock, gen_limp_BreakStatement_Statement, gen_limp_ContinueStatement_Statement, gen_limp_ReturnStatement_Statement, gen_limp_ElseBlock_Else, gen_limp_TypeAlias_TypeDeclaration, gen_limp_SomeVarBlock_VarBlock, gen_limp_NoVarBlock_VarBlock, gen_limp_ChoiceExpr_Expr, gen_limp_BinaryExpr_Expr, gen_limp_UnaryNegationExpr_Expr, gen_limp_UnaryMinusExpr_Expr, gen_limp_RecordAccessExpr_Expr, gen_limp_RecordUpdateExpr_Expr, gen_limp_ElseIf_Else, gen_limp_NoElse_Else, gen_limp_IfThenElseExpr_Expr, gen_limp_BooleanLiteralExpr_Expr, gen_limp_IntegerLiteralExpr_Expr, gen_limp_IntegerWildCardExpr_Expr, gen_limp_RealLiteralExpr_Expr, gen_limp_StringLiteralExpr_Expr, gen_limp_InitExpr_Expr, gen_limp_SecondInit_Expr, gen_limp_IdExpr_Expr, gen_limp_FcnCallExpr_Expr, gen_limp_TupleType_Type, gen_limp_ArrayAccessExpr_Expr, gen_limp_ArrayUpdateExpr_Expr, gen_limp_FreshVariable_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)