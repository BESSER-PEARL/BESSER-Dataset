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
go_Type = Class(name="go::Type")
go_TypeName = Class(name="go::TypeName")
go_TypeLit = Class(name="go::TypeLit")
go_identifier = Class(name="go::identifier")
go_TypeNameLinha = Class(name="go::TypeNameLinha")
go_QualifiedIdent = Class(name="go::QualifiedIdent")
go_TypeLitLinha = Class(name="go::TypeLitLinha")
go_SouceFile = Class(name="go::SouceFile")
go_PackageClause = Class(name="go::PackageClause")
go_ImportDecl = Class(name="go::ImportDecl")
go_TopLevelDecl = Class(name="go::TopLevelDecl")
go_StructType = Class(name="go::StructType")
go_PointerType = Class(name="go::PointerType")
go_FunctionType = Class(name="go::FunctionType")
go_InterfaceType = Class(name="go::InterfaceType")
go_MapType = Class(name="go::MapType")
go_ChannelType = Class(name="go::ChannelType")
go_EmbeddedField = Class(name="go::EmbeddedField")
go_Tag = Class(name="go::Tag")
go_string_lit = Class(name="go::string::lit")
go_Signature = Class(name="go::Signature")
go_Parameters = Class(name="go::Parameters")
go_Result = Class(name="go::Result")
go_ArrayLength = Class(name="go::ArrayLength")
go_ElementType = Class(name="go::ElementType")
go_Expression = Class(name="go::Expression")
go_FieldDecl = Class(name="go::FieldDecl")
go_IdentifierList = Class(name="go::IdentifierList")
go_MethodName = Class(name="go::MethodName")
go_InterfaceTypeName = Class(name="go::InterfaceTypeName")
go_KeyType = Class(name="go::KeyType")
go_Block = Class(name="go::Block")
go_StatementList = Class(name="go::StatementList")
Receiver = Class(name="Receiver")
go_ParameterList = Class(name="go::ParameterList")
go_ParameterDecl = Class(name="go::ParameterDecl")
go_MethodSpec = Class(name="go::MethodSpec")
go_FunctionBody = Class(name="go::FunctionBody")
go_Receiver = Class(name="go::Receiver")
go_ConstSpec = Class(name="go::ConstSpec")
go_ExpressionList = Class(name="go::ExpressionList")
go_TypeSpec = Class(name="go::TypeSpec")
go_Statement = Class(name="go::Statement")
go_Declaration = Class(name="go::Declaration")
go_ConstDecl = Class(name="go::ConstDecl")
go_TypeDecl = Class(name="go::TypeDecl")
go_VarDecl = Class(name="go::VarDecl")
go_topLevelDeclLinha = Class(name="go::topLevelDeclLinha")
go_VarSpec = Class(name="go::VarSpec")
go_FunctionName = Class(name="go::FunctionName")
go_ShortVarDecl = Class(name="go::ShortVarDecl")
go_FunctionDecl = Class(name="go::FunctionDecl")
go_AliasDecl = Class(name="go::AliasDecl")
TypeSpec = Class(name="TypeSpec")
go_OperandName = Class(name="go::OperandName")
go_TypeDef = Class(name="go::TypeDef")
go_BasicLit = Class(name="go::BasicLit")
go_float_lit = Class(name="go::float::lit")
go_rune_lit = Class(name="go::rune::lit")
OperandName = Class(name="OperandName")
go_PackageName = Class(name="go::PackageName")
go_MethodDecl = Class(name="go::MethodDecl")
go_Operand = Class(name="go::Operand")
go_Literal = Class(name="go::Literal")
go_ElementList = Class(name="go::ElementList")
go_KeyedElement = Class(name="go::KeyedElement")
go_Element = Class(name="go::Element")
go_Key = Class(name="go::Key")
go_CompositeLit = Class(name="go::CompositeLit")
Literal = Class(name="Literal")
go_LiteralType = Class(name="go::LiteralType")
go_LiteralValue = Class(name="go::LiteralValue")
go_LiteralTypeLinha = Class(name="go::LiteralTypeLinha")
go_Conversion = Class(name="go::Conversion")
go_MethodExpr = Class(name="go::MethodExpr")
go_Arguments = Class(name="go::Arguments")
go_ponto = Class(name="go::ponto")
go_cochetes = Class(name="go::cochetes")
go_Selector = Class(name="go::Selector")
go_TypeAssertion = Class(name="go::TypeAssertion")
go_FieldName = Class(name="go::FieldName")
go_FunctionLit = Class(name="go::FunctionLit")
go_PrimaryExpr = Class(name="go::PrimaryExpr")
go_PrimaryExprLinha = Class(name="go::PrimaryExprLinha")
go_ReceiverType = Class(name="go::ReceiverType")
go_UnaryExpr = Class(name="go::UnaryExpr")
go_ExpressionLinha = Class(name="go::ExpressionLinha")
go_binary_op = Class(name="go::binary::op")
go_Index = Class(name="go::Index")
go_Slice = Class(name="go::Slice")
go_decimals = Class(name="go::decimals")
go_LabeledStmt = Class(name="go::LabeledStmt")
go_SimpleStmt = Class(name="go::SimpleStmt")
go_GoStmt = Class(name="go::GoStmt")
go_ReturnStmt = Class(name="go::ReturnStmt")
go_BreakStmt = Class(name="go::BreakStmt")
go_ContinueStmt = Class(name="go::ContinueStmt")
go_ExpressionStmt = Class(name="go::ExpressionStmt")
go_SendStmt = Class(name="go::SendStmt")
go_IncDecStmt = Class(name="go::IncDecStmt")
go_Assignment = Class(name="go::Assignment")
go_Label = Class(name="go::Label")
go_GotoStmt = Class(name="go::GotoStmt")
go_IfStmt = Class(name="go::IfStmt")
go_SwitchStmt = Class(name="go::SwitchStmt")
go_SelectStmt = Class(name="go::SelectStmt")
go_ForStmt = Class(name="go::ForStmt")
go_DeferStmt = Class(name="go::DeferStmt")
SwitchStmt = Class(name="SwitchStmt")
go_switch_stmt_linha = Class(name="go::switch::stmt::linha")
go_ExprCaseClause = Class(name="go::ExprCaseClause")
go_ExprSwitchCase = Class(name="go::ExprSwitchCase")
go_TypeSwitchGuard = Class(name="go::TypeSwitchGuard")
go_TypeCaseClause = Class(name="go::TypeCaseClause")
go_Channel = Class(name="go::Channel")
go_RangeClause = Class(name="go::RangeClause")
go_InitStmt = Class(name="go::InitStmt")
go_PostStmt = Class(name="go::PostStmt")
go_TypeSwitchCase = Class(name="go::TypeSwitchCase")
go_TypeList = Class(name="go::TypeList")
go_Condition = Class(name="go::Condition")
go_ForClause = Class(name="go::ForClause")
go_RecvStmt = Class(name="go::RecvStmt")
go_RecvExpr = Class(name="go::RecvExpr")
go_CommClause = Class(name="go::CommClause")
go_CommCase = Class(name="go::CommCase")
float_lit = Class(name="float::lit")
go_exponent = Class(name="go::exponent")
go_ImportSpec = Class(name="go::ImportSpec")
go_ImportPath = Class(name="go::ImportPath")
go_imaginary_lit = Class(name="go::imaginary::lit")

# go_Type class attributes and methods

# go_TypeName class attributes and methods

# go_TypeLit class attributes and methods

# go_identifier class attributes and methods
go_identifier_LETTER: Property = Property(name="LETTER", type=StringType)
go_identifier_DECIMAL_DIGIT: Property = Property(name="DECIMAL_DIGIT", type=StringType)
go_identifier.attributes={go_identifier_DECIMAL_DIGIT, go_identifier_LETTER}

# go_TypeNameLinha class attributes and methods

# go_QualifiedIdent class attributes and methods

# go_TypeLitLinha class attributes and methods

# go_SouceFile class attributes and methods

# go_PackageClause class attributes and methods

# go_ImportDecl class attributes and methods

# go_TopLevelDecl class attributes and methods

# go_StructType class attributes and methods

# go_PointerType class attributes and methods

# go_FunctionType class attributes and methods

# go_InterfaceType class attributes and methods

# go_MapType class attributes and methods

# go_ChannelType class attributes and methods

# go_EmbeddedField class attributes and methods

# go_Tag class attributes and methods

# go_string_lit class attributes and methods
go_string_lit_raw_string_lit: Property = Property(name="raw_string_lit", type=StringType)
go_string_lit_interpreted_string_lit: Property = Property(name="interpreted_string_lit", type=StringType)
go_string_lit.attributes={go_string_lit_raw_string_lit, go_string_lit_interpreted_string_lit}

# go_Signature class attributes and methods

# go_Parameters class attributes and methods

# go_Result class attributes and methods

# go_ArrayLength class attributes and methods

# go_ElementType class attributes and methods

# go_Expression class attributes and methods

# go_FieldDecl class attributes and methods

# go_IdentifierList class attributes and methods

# go_MethodName class attributes and methods

# go_InterfaceTypeName class attributes and methods

# go_KeyType class attributes and methods

# go_Block class attributes and methods

# go_StatementList class attributes and methods

# Receiver class attributes and methods

# go_ParameterList class attributes and methods

# go_ParameterDecl class attributes and methods

# go_MethodSpec class attributes and methods

# go_FunctionBody class attributes and methods

# go_Receiver class attributes and methods

# go_ConstSpec class attributes and methods

# go_ExpressionList class attributes and methods

# go_TypeSpec class attributes and methods

# go_Statement class attributes and methods
go_Statement_FallthroughStmt: Property = Property(name="FallthroughStmt", type=StringType)
go_Statement.attributes={go_Statement_FallthroughStmt}

# go_Declaration class attributes and methods

# go_ConstDecl class attributes and methods

# go_TypeDecl class attributes and methods

# go_VarDecl class attributes and methods

# go_topLevelDeclLinha class attributes and methods

# go_VarSpec class attributes and methods

# go_FunctionName class attributes and methods

# go_ShortVarDecl class attributes and methods

# go_FunctionDecl class attributes and methods

# go_AliasDecl class attributes and methods

# TypeSpec class attributes and methods

# go_OperandName class attributes and methods

# go_TypeDef class attributes and methods

# go_BasicLit class attributes and methods
go_BasicLit_int_lit: Property = Property(name="int_lit", type=StringType)
go_BasicLit.attributes={go_BasicLit_int_lit}

# go_float_lit class attributes and methods

# go_rune_lit class attributes and methods
go_rune_lit_unicode_value: Property = Property(name="unicode_value", type=StringType)
go_rune_lit_byte_value: Property = Property(name="byte_value", type=StringType)
go_rune_lit.attributes={go_rune_lit_byte_value, go_rune_lit_unicode_value}

# OperandName class attributes and methods

# go_PackageName class attributes and methods

# go_MethodDecl class attributes and methods

# go_Operand class attributes and methods

# go_Literal class attributes and methods

# go_ElementList class attributes and methods

# go_KeyedElement class attributes and methods

# go_Element class attributes and methods

# go_Key class attributes and methods

# go_CompositeLit class attributes and methods

# Literal class attributes and methods

# go_LiteralType class attributes and methods

# go_LiteralValue class attributes and methods

# go_LiteralTypeLinha class attributes and methods

# go_Conversion class attributes and methods

# go_MethodExpr class attributes and methods

# go_Arguments class attributes and methods

# go_ponto class attributes and methods

# go_cochetes class attributes and methods

# go_Selector class attributes and methods

# go_TypeAssertion class attributes and methods

# go_FieldName class attributes and methods

# go_FunctionLit class attributes and methods

# go_PrimaryExpr class attributes and methods

# go_PrimaryExprLinha class attributes and methods

# go_ReceiverType class attributes and methods

# go_UnaryExpr class attributes and methods
go_UnaryExpr_unary_op: Property = Property(name="unary_op", type=StringType)
go_UnaryExpr.attributes={go_UnaryExpr_unary_op}

# go_ExpressionLinha class attributes and methods

# go_binary_op class attributes and methods
go_binary_op_rel_op: Property = Property(name="rel_op", type=StringType)
go_binary_op_add_op: Property = Property(name="add_op", type=StringType)
go_binary_op_mul_op: Property = Property(name="mul_op", type=StringType)
go_binary_op.attributes={go_binary_op_mul_op, go_binary_op_add_op, go_binary_op_rel_op}

# go_Index class attributes and methods

# go_Slice class attributes and methods

# go_decimals class attributes and methods
go_decimals_DECIMAL_DIGIT: Property = Property(name="DECIMAL_DIGIT", type=StringType)
go_decimals.attributes={go_decimals_DECIMAL_DIGIT}

# go_LabeledStmt class attributes and methods

# go_SimpleStmt class attributes and methods
go_SimpleStmt_EmptyStmt: Property = Property(name="EmptyStmt", type=StringType)
go_SimpleStmt.attributes={go_SimpleStmt_EmptyStmt}

# go_GoStmt class attributes and methods

# go_ReturnStmt class attributes and methods

# go_BreakStmt class attributes and methods

# go_ContinueStmt class attributes and methods

# go_ExpressionStmt class attributes and methods

# go_SendStmt class attributes and methods

# go_IncDecStmt class attributes and methods

# go_Assignment class attributes and methods
go_Assignment_assign_op: Property = Property(name="assign_op", type=StringType)
go_Assignment.attributes={go_Assignment_assign_op}

# go_Label class attributes and methods

# go_GotoStmt class attributes and methods

# go_IfStmt class attributes and methods

# go_SwitchStmt class attributes and methods

# go_SelectStmt class attributes and methods

# go_ForStmt class attributes and methods

# go_DeferStmt class attributes and methods

# SwitchStmt class attributes and methods

# go_switch_stmt_linha class attributes and methods

# go_ExprCaseClause class attributes and methods

# go_ExprSwitchCase class attributes and methods

# go_TypeSwitchGuard class attributes and methods

# go_TypeCaseClause class attributes and methods

# go_Channel class attributes and methods

# go_RangeClause class attributes and methods

# go_InitStmt class attributes and methods

# go_PostStmt class attributes and methods

# go_TypeSwitchCase class attributes and methods

# go_TypeList class attributes and methods

# go_Condition class attributes and methods

# go_ForClause class attributes and methods

# go_RecvStmt class attributes and methods

# go_RecvExpr class attributes and methods

# go_CommClause class attributes and methods

# go_CommCase class attributes and methods

# float_lit class attributes and methods

# go_exponent class attributes and methods

# go_ImportSpec class attributes and methods

# go_ImportPath class attributes and methods

# go_imaginary_lit class attributes and methods

# Relationships
TypeName5: BinaryAssociation = BinaryAssociation(
    name="TypeName5",
    ends={
        Property(name="go_TypeName", type=go_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Type", type=go_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeLit6: BinaryAssociation = BinaryAssociation(
    name="TypeLit6",
    ends={
        Property(name="go_TypeLit", type=go_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Type7", type=go_TypeLit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type9: BinaryAssociation = BinaryAssociation(
    name="Type9",
    ends={
        Property(name="go_Type10", type=go_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Type8", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier11: BinaryAssociation = BinaryAssociation(
    name="identifier11",
    ends={
        Property(name="go_identifier", type=go_TypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeName12", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeNameLinha13: BinaryAssociation = BinaryAssociation(
    name="TypeNameLinha13",
    ends={
        Property(name="go_TypeNameLinha", type=go_TypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeName14", type=go_TypeNameLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier15: BinaryAssociation = BinaryAssociation(
    name="identifier15",
    ends={
        Property(name="go_identifier17", type=go_TypeNameLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeNameLinha16", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeNameLinha19: BinaryAssociation = BinaryAssociation(
    name="TypeNameLinha19",
    ends={
        Property(name="go_TypeNameLinha20", type=go_TypeNameLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeNameLinha18", type=go_TypeNameLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
QualifiedIdent21: BinaryAssociation = BinaryAssociation(
    name="QualifiedIdent21",
    ends={
        Property(name="go_QualifiedIdent", type=go_TypeNameLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeNameLinha22", type=go_QualifiedIdent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PackageClause0: BinaryAssociation = BinaryAssociation(
    name="PackageClause0",
    ends={
        Property(name="go_PackageClause", type=go_SouceFile, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SouceFile", type=go_PackageClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ImportDecl1: BinaryAssociation = BinaryAssociation(
    name="ImportDecl1",
    ends={
        Property(name="go_ImportDecl", type=go_SouceFile, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SouceFile2", type=go_ImportDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TopLevelDecl3: BinaryAssociation = BinaryAssociation(
    name="TopLevelDecl3",
    ends={
        Property(name="go_TopLevelDecl", type=go_SouceFile, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SouceFile4", type=go_TopLevelDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
StructType25: BinaryAssociation = BinaryAssociation(
    name="StructType25",
    ends={
        Property(name="go_StructType", type=go_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeLit26", type=go_StructType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PointerType27: BinaryAssociation = BinaryAssociation(
    name="PointerType27",
    ends={
        Property(name="go_PointerType", type=go_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeLit28", type=go_PointerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FunctionType29: BinaryAssociation = BinaryAssociation(
    name="FunctionType29",
    ends={
        Property(name="go_FunctionType", type=go_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeLit30", type=go_FunctionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
InterfaceType31: BinaryAssociation = BinaryAssociation(
    name="InterfaceType31",
    ends={
        Property(name="go_InterfaceType", type=go_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeLit32", type=go_InterfaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MapType33: BinaryAssociation = BinaryAssociation(
    name="MapType33",
    ends={
        Property(name="go_MapType", type=go_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeLit34", type=go_MapType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeLitLinha23: BinaryAssociation = BinaryAssociation(
    name="TypeLitLinha23",
    ends={
        Property(name="go_TypeLitLinha", type=go_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeLit24", type=go_TypeLitLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type53: BinaryAssociation = BinaryAssociation(
    name="Type53",
    ends={
        Property(name="go_Type55", type=go_FieldDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FieldDecl54", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
EmbeddedField56: BinaryAssociation = BinaryAssociation(
    name="EmbeddedField56",
    ends={
        Property(name="go_EmbeddedField", type=go_FieldDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FieldDecl57", type=go_EmbeddedField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Tag58: BinaryAssociation = BinaryAssociation(
    name="Tag58",
    ends={
        Property(name="go_Tag", type=go_FieldDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FieldDecl59", type=go_Tag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeName60: BinaryAssociation = BinaryAssociation(
    name="TypeName60",
    ends={
        Property(name="go_TypeName62", type=go_EmbeddedField, multiplicity=Multiplicity(1, 1)),
        Property(name="go_EmbeddedField61", type=go_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
string_lit63: BinaryAssociation = BinaryAssociation(
    name="string_lit63",
    ends={
        Property(name="go_string_lit", type=go_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Tag64", type=go_string_lit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type65: BinaryAssociation = BinaryAssociation(
    name="Type65",
    ends={
        Property(name="go_Type67", type=go_PointerType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PointerType66", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Signature68: BinaryAssociation = BinaryAssociation(
    name="Signature68",
    ends={
        Property(name="go_Signature", type=go_FunctionType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionType69", type=go_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Parameters70: BinaryAssociation = BinaryAssociation(
    name="Parameters70",
    ends={
        Property(name="go_Parameters", type=go_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Signature71", type=go_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ChannelType35: BinaryAssociation = BinaryAssociation(
    name="ChannelType35",
    ends={
        Property(name="go_ChannelType", type=go_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeLit36", type=go_ChannelType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Result72: BinaryAssociation = BinaryAssociation(
    name="Result72",
    ends={
        Property(name="go_Result", type=go_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Signature73", type=go_Result, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ArrayLength37: BinaryAssociation = BinaryAssociation(
    name="ArrayLength37",
    ends={
        Property(name="go_ArrayLength", type=go_TypeLitLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeLitLinha38", type=go_ArrayLength, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ElementType39: BinaryAssociation = BinaryAssociation(
    name="ElementType39",
    ends={
        Property(name="go_ElementType", type=go_TypeLitLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeLitLinha40", type=go_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeLitLinha42: BinaryAssociation = BinaryAssociation(
    name="TypeLitLinha42",
    ends={
        Property(name="go_TypeLitLinha43", type=go_TypeLitLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeLitLinha41", type=go_TypeLitLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression44: BinaryAssociation = BinaryAssociation(
    name="Expression44",
    ends={
        Property(name="go_Expression", type=go_ArrayLength, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ArrayLength45", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type46: BinaryAssociation = BinaryAssociation(
    name="Type46",
    ends={
        Property(name="go_Type48", type=go_ElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ElementType47", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FieldDecl49: BinaryAssociation = BinaryAssociation(
    name="FieldDecl49",
    ends={
        Property(name="go_FieldDecl", type=go_StructType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_StructType50", type=go_FieldDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IdentifierList51: BinaryAssociation = BinaryAssociation(
    name="IdentifierList51",
    ends={
        Property(name="go_IdentifierList", type=go_FieldDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FieldDecl52", type=go_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MethodName92: BinaryAssociation = BinaryAssociation(
    name="MethodName92",
    ends={
        Property(name="go_MethodName", type=go_MethodSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MethodSpec93", type=go_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Signature94: BinaryAssociation = BinaryAssociation(
    name="Signature94",
    ends={
        Property(name="go_Signature96", type=go_MethodSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MethodSpec95", type=go_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
InterfaceTypeName97: BinaryAssociation = BinaryAssociation(
    name="InterfaceTypeName97",
    ends={
        Property(name="go_InterfaceTypeName", type=go_MethodSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MethodSpec98", type=go_InterfaceTypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier99: BinaryAssociation = BinaryAssociation(
    name="identifier99",
    ends={
        Property(name="go_identifier101", type=go_MethodName, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MethodName100", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeName102: BinaryAssociation = BinaryAssociation(
    name="TypeName102",
    ends={
        Property(name="go_TypeName104", type=go_InterfaceTypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="go_InterfaceTypeName103", type=go_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
KeyType105: BinaryAssociation = BinaryAssociation(
    name="KeyType105",
    ends={
        Property(name="go_KeyType", type=go_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MapType106", type=go_KeyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ElementType107: BinaryAssociation = BinaryAssociation(
    name="ElementType107",
    ends={
        Property(name="go_ElementType109", type=go_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MapType108", type=go_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type110: BinaryAssociation = BinaryAssociation(
    name="Type110",
    ends={
        Property(name="go_Type112", type=go_KeyType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_KeyType111", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ElementType113: BinaryAssociation = BinaryAssociation(
    name="ElementType113",
    ends={
        Property(name="go_ElementType115", type=go_ChannelType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ChannelType114", type=go_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Parameters74: BinaryAssociation = BinaryAssociation(
    name="Parameters74",
    ends={
        Property(name="go_Parameters76", type=go_Result, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Result75", type=go_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
StatementList116: BinaryAssociation = BinaryAssociation(
    name="StatementList116",
    ends={
        Property(name="go_StatementList", type=go_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Block", type=go_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type77: BinaryAssociation = BinaryAssociation(
    name="Type77",
    ends={
        Property(name="go_Type79", type=go_Result, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Result78", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ParameterList80: BinaryAssociation = BinaryAssociation(
    name="ParameterList80",
    ends={
        Property(name="go_ParameterList", type=go_Parameters, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Parameters81", type=go_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ParameterDecl82: BinaryAssociation = BinaryAssociation(
    name="ParameterDecl82",
    ends={
        Property(name="go_ParameterDecl", type=go_ParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ParameterList83", type=go_ParameterDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IdentifierList84: BinaryAssociation = BinaryAssociation(
    name="IdentifierList84",
    ends={
        Property(name="go_IdentifierList86", type=go_ParameterDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ParameterDecl85", type=go_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type87: BinaryAssociation = BinaryAssociation(
    name="Type87",
    ends={
        Property(name="go_Type89", type=go_ParameterDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ParameterDecl88", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MethodSpec90: BinaryAssociation = BinaryAssociation(
    name="MethodSpec90",
    ends={
        Property(name="go_MethodSpec", type=go_InterfaceType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_InterfaceType91", type=go_MethodSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FunctionName129: BinaryAssociation = BinaryAssociation(
    name="FunctionName129",
    ends={
        Property(name="go_FunctionName", type=go_topLevelDeclLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_topLevelDeclLinha130", type=go_FunctionName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Signature131: BinaryAssociation = BinaryAssociation(
    name="Signature131",
    ends={
        Property(name="go_Signature133", type=go_topLevelDeclLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_topLevelDeclLinha132", type=go_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FunctionBody134: BinaryAssociation = BinaryAssociation(
    name="FunctionBody134",
    ends={
        Property(name="go_FunctionBody", type=go_topLevelDeclLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_topLevelDeclLinha135", type=go_FunctionBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Receiver136: BinaryAssociation = BinaryAssociation(
    name="Receiver136",
    ends={
        Property(name="go_Receiver", type=go_topLevelDeclLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_topLevelDeclLinha137", type=go_Receiver, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MethodName138: BinaryAssociation = BinaryAssociation(
    name="MethodName138",
    ends={
        Property(name="go_MethodName140", type=go_topLevelDeclLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_topLevelDeclLinha139", type=go_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ConstSpec141: BinaryAssociation = BinaryAssociation(
    name="ConstSpec141",
    ends={
        Property(name="go_ConstSpec", type=go_ConstDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ConstDecl142", type=go_ConstSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IdentifierList143: BinaryAssociation = BinaryAssociation(
    name="IdentifierList143",
    ends={
        Property(name="go_IdentifierList145", type=go_ConstSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ConstSpec144", type=go_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type146: BinaryAssociation = BinaryAssociation(
    name="Type146",
    ends={
        Property(name="go_Type148", type=go_ConstSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ConstSpec147", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionList149: BinaryAssociation = BinaryAssociation(
    name="ExpressionList149",
    ends={
        Property(name="go_ExpressionList", type=go_ConstSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ConstSpec150", type=go_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier151: BinaryAssociation = BinaryAssociation(
    name="identifier151",
    ends={
        Property(name="go_identifier153", type=go_IdentifierList, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IdentifierList152", type=go_identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Expression154: BinaryAssociation = BinaryAssociation(
    name="Expression154",
    ends={
        Property(name="go_Expression156", type=go_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ExpressionList155", type=go_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Statement117: BinaryAssociation = BinaryAssociation(
    name="Statement117",
    ends={
        Property(name="go_Statement", type=go_StatementList, multiplicity=Multiplicity(1, 1)),
        Property(name="go_StatementList118", type=go_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ConstDecl119: BinaryAssociation = BinaryAssociation(
    name="ConstDecl119",
    ends={
        Property(name="go_ConstDecl", type=go_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Declaration", type=go_ConstDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeDecl120: BinaryAssociation = BinaryAssociation(
    name="TypeDecl120",
    ends={
        Property(name="go_TypeDecl", type=go_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Declaration121", type=go_TypeDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
VarDecl122: BinaryAssociation = BinaryAssociation(
    name="VarDecl122",
    ends={
        Property(name="go_VarDecl", type=go_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Declaration123", type=go_VarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declaration124: BinaryAssociation = BinaryAssociation(
    name="Declaration124",
    ends={
        Property(name="go_Declaration126", type=go_TopLevelDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TopLevelDecl125", type=go_Declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
topLevelDeclLinha127: BinaryAssociation = BinaryAssociation(
    name="topLevelDeclLinha127",
    ends={
        Property(name="go_topLevelDeclLinha", type=go_TopLevelDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TopLevelDecl128", type=go_topLevelDeclLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
VarSpec165: BinaryAssociation = BinaryAssociation(
    name="VarSpec165",
    ends={
        Property(name="go_VarSpec", type=go_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_VarDecl166", type=go_VarSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IdentifierList167: BinaryAssociation = BinaryAssociation(
    name="IdentifierList167",
    ends={
        Property(name="go_IdentifierList169", type=go_VarSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_VarSpec168", type=go_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type170: BinaryAssociation = BinaryAssociation(
    name="Type170",
    ends={
        Property(name="go_Type172", type=go_VarSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_VarSpec171", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionList173: BinaryAssociation = BinaryAssociation(
    name="ExpressionList173",
    ends={
        Property(name="go_ExpressionList175", type=go_VarSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_VarSpec174", type=go_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IdentifierList176: BinaryAssociation = BinaryAssociation(
    name="IdentifierList176",
    ends={
        Property(name="go_IdentifierList177", type=go_ShortVarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ShortVarDecl", type=go_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionList178: BinaryAssociation = BinaryAssociation(
    name="ExpressionList178",
    ends={
        Property(name="go_ExpressionList180", type=go_ShortVarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ShortVarDecl179", type=go_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FunctionName181: BinaryAssociation = BinaryAssociation(
    name="FunctionName181",
    ends={
        Property(name="go_FunctionName182", type=go_FunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionDecl", type=go_FunctionName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Signature183: BinaryAssociation = BinaryAssociation(
    name="Signature183",
    ends={
        Property(name="go_Signature185", type=go_FunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionDecl184", type=go_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FunctionBody186: BinaryAssociation = BinaryAssociation(
    name="FunctionBody186",
    ends={
        Property(name="go_FunctionBody188", type=go_FunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionDecl187", type=go_FunctionBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeSpec157: BinaryAssociation = BinaryAssociation(
    name="TypeSpec157",
    ends={
        Property(name="go_TypeSpec", type=go_TypeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeDecl158", type=go_TypeSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier159: BinaryAssociation = BinaryAssociation(
    name="identifier159",
    ends={
        Property(name="go_identifier161", type=go_TypeSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeSpec160", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type162: BinaryAssociation = BinaryAssociation(
    name="Type162",
    ends={
        Property(name="go_Type164", type=go_TypeSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeSpec163", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OperandName207: BinaryAssociation = BinaryAssociation(
    name="OperandName207",
    ends={
        Property(name="go_OperandName", type=go_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Operand208", type=go_OperandName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression209: BinaryAssociation = BinaryAssociation(
    name="Expression209",
    ends={
        Property(name="go_Expression211", type=go_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Operand210", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BasicLit212: BinaryAssociation = BinaryAssociation(
    name="BasicLit212",
    ends={
        Property(name="go_BasicLit", type=go_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Literal213", type=go_BasicLit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
float_lit214: BinaryAssociation = BinaryAssociation(
    name="float_lit214",
    ends={
        Property(name="go_float_lit", type=go_BasicLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_BasicLit215", type=go_float_lit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rune_lit216: BinaryAssociation = BinaryAssociation(
    name="rune_lit216",
    ends={
        Property(name="go_rune_lit", type=go_BasicLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_BasicLit217", type=go_rune_lit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
string_lit218: BinaryAssociation = BinaryAssociation(
    name="string_lit218",
    ends={
        Property(name="go_string_lit220", type=go_BasicLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_BasicLit219", type=go_string_lit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PackageName221: BinaryAssociation = BinaryAssociation(
    name="PackageName221",
    ends={
        Property(name="go_PackageName", type=go_QualifiedIdent, multiplicity=Multiplicity(1, 1)),
        Property(name="go_QualifiedIdent222", type=go_PackageName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier189: BinaryAssociation = BinaryAssociation(
    name="identifier189",
    ends={
        Property(name="go_identifier191", type=go_FunctionName, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionName190", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Block192: BinaryAssociation = BinaryAssociation(
    name="Block192",
    ends={
        Property(name="go_Block194", type=go_FunctionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionBody193", type=go_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Receiver195: BinaryAssociation = BinaryAssociation(
    name="Receiver195",
    ends={
        Property(name="go_Receiver196", type=go_MethodDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MethodDecl", type=go_Receiver, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MethodName197: BinaryAssociation = BinaryAssociation(
    name="MethodName197",
    ends={
        Property(name="go_MethodName199", type=go_MethodDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MethodDecl198", type=go_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Signature200: BinaryAssociation = BinaryAssociation(
    name="Signature200",
    ends={
        Property(name="go_Signature202", type=go_MethodDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MethodDecl201", type=go_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FunctionBody203: BinaryAssociation = BinaryAssociation(
    name="FunctionBody203",
    ends={
        Property(name="go_FunctionBody205", type=go_MethodDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MethodDecl204", type=go_FunctionBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Literal206: BinaryAssociation = BinaryAssociation(
    name="Literal206",
    ends={
        Property(name="go_Literal", type=go_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Operand", type=go_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ArrayLength243: BinaryAssociation = BinaryAssociation(
    name="ArrayLength243",
    ends={
        Property(name="go_ArrayLength245", type=go_LiteralTypeLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LiteralTypeLinha244", type=go_ArrayLength, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ElementType246: BinaryAssociation = BinaryAssociation(
    name="ElementType246",
    ends={
        Property(name="go_ElementType248", type=go_LiteralTypeLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LiteralTypeLinha247", type=go_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ElementList249: BinaryAssociation = BinaryAssociation(
    name="ElementList249",
    ends={
        Property(name="go_ElementList", type=go_LiteralValue, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LiteralValue250", type=go_ElementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
KeyedElement251: BinaryAssociation = BinaryAssociation(
    name="KeyedElement251",
    ends={
        Property(name="go_KeyedElement", type=go_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ElementList252", type=go_KeyedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Expression253: BinaryAssociation = BinaryAssociation(
    name="Expression253",
    ends={
        Property(name="go_Expression254", type=go_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Element", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LiteralValue255: BinaryAssociation = BinaryAssociation(
    name="LiteralValue255",
    ends={
        Property(name="go_LiteralValue257", type=go_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Element256", type=go_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Key258: BinaryAssociation = BinaryAssociation(
    name="Key258",
    ends={
        Property(name="go_Key", type=go_KeyedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_KeyedElement259", type=go_Key, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Element260: BinaryAssociation = BinaryAssociation(
    name="Element260",
    ends={
        Property(name="go_Element262", type=go_KeyedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_KeyedElement261", type=go_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier223: BinaryAssociation = BinaryAssociation(
    name="identifier223",
    ends={
        Property(name="go_identifier225", type=go_QualifiedIdent, multiplicity=Multiplicity(1, 1)),
        Property(name="go_QualifiedIdent224", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LiteralType226: BinaryAssociation = BinaryAssociation(
    name="LiteralType226",
    ends={
        Property(name="go_LiteralType", type=go_CompositeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_CompositeLit", type=go_LiteralType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LiteralValue227: BinaryAssociation = BinaryAssociation(
    name="LiteralValue227",
    ends={
        Property(name="go_LiteralValue", type=go_CompositeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_CompositeLit228", type=go_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
StructType229: BinaryAssociation = BinaryAssociation(
    name="StructType229",
    ends={
        Property(name="go_StructType231", type=go_LiteralType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LiteralType230", type=go_StructType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LiteralTypeLinha232: BinaryAssociation = BinaryAssociation(
    name="LiteralTypeLinha232",
    ends={
        Property(name="go_LiteralTypeLinha", type=go_LiteralType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LiteralType233", type=go_LiteralTypeLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ElementType234: BinaryAssociation = BinaryAssociation(
    name="ElementType234",
    ends={
        Property(name="go_ElementType236", type=go_LiteralType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LiteralType235", type=go_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MapType237: BinaryAssociation = BinaryAssociation(
    name="MapType237",
    ends={
        Property(name="go_MapType239", type=go_LiteralType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LiteralType238", type=go_MapType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeName240: BinaryAssociation = BinaryAssociation(
    name="TypeName240",
    ends={
        Property(name="go_TypeName242", type=go_LiteralType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LiteralType241", type=go_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Conversion283: BinaryAssociation = BinaryAssociation(
    name="Conversion283",
    ends={
        Property(name="go_Conversion", type=go_PrimaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PrimaryExpr284", type=go_Conversion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MethodExpr285: BinaryAssociation = BinaryAssociation(
    name="MethodExpr285",
    ends={
        Property(name="go_MethodExpr", type=go_PrimaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PrimaryExpr286", type=go_MethodExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Arguments287: BinaryAssociation = BinaryAssociation(
    name="Arguments287",
    ends={
        Property(name="go_Arguments", type=go_PrimaryExprLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PrimaryExprLinha288", type=go_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PrimaryExprLinha290: BinaryAssociation = BinaryAssociation(
    name="PrimaryExprLinha290",
    ends={
        Property(name="go_PrimaryExprLinha291", type=go_PrimaryExprLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PrimaryExprLinha289", type=go_PrimaryExprLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ponto292: BinaryAssociation = BinaryAssociation(
    name="ponto292",
    ends={
        Property(name="go_ponto", type=go_PrimaryExprLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PrimaryExprLinha293", type=go_ponto, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cochetes294: BinaryAssociation = BinaryAssociation(
    name="cochetes294",
    ends={
        Property(name="go_cochetes", type=go_PrimaryExprLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PrimaryExprLinha295", type=go_cochetes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Selector296: BinaryAssociation = BinaryAssociation(
    name="Selector296",
    ends={
        Property(name="go_Selector", type=go_ponto, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ponto297", type=go_Selector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PrimaryExprLinha298: BinaryAssociation = BinaryAssociation(
    name="PrimaryExprLinha298",
    ends={
        Property(name="go_PrimaryExprLinha300", type=go_ponto, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ponto299", type=go_PrimaryExprLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeAssertion301: BinaryAssociation = BinaryAssociation(
    name="TypeAssertion301",
    ends={
        Property(name="go_TypeAssertion", type=go_ponto, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ponto302", type=go_TypeAssertion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FieldName263: BinaryAssociation = BinaryAssociation(
    name="FieldName263",
    ends={
        Property(name="go_FieldName", type=go_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Key264", type=go_FieldName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression265: BinaryAssociation = BinaryAssociation(
    name="Expression265",
    ends={
        Property(name="go_Expression267", type=go_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Key266", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LiteralValue268: BinaryAssociation = BinaryAssociation(
    name="LiteralValue268",
    ends={
        Property(name="go_LiteralValue270", type=go_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Key269", type=go_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier271: BinaryAssociation = BinaryAssociation(
    name="identifier271",
    ends={
        Property(name="go_identifier273", type=go_FieldName, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FieldName272", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Signature274: BinaryAssociation = BinaryAssociation(
    name="Signature274",
    ends={
        Property(name="go_Signature275", type=go_FunctionLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionLit", type=go_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FunctionBody276: BinaryAssociation = BinaryAssociation(
    name="FunctionBody276",
    ends={
        Property(name="go_FunctionBody278", type=go_FunctionLit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionLit277", type=go_FunctionBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Operand279: BinaryAssociation = BinaryAssociation(
    name="Operand279",
    ends={
        Property(name="go_Operand280", type=go_PrimaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PrimaryExpr", type=go_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PrimaryExprLinha281: BinaryAssociation = BinaryAssociation(
    name="PrimaryExprLinha281",
    ends={
        Property(name="go_PrimaryExprLinha", type=go_PrimaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PrimaryExpr282", type=go_PrimaryExprLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionList321: BinaryAssociation = BinaryAssociation(
    name="ExpressionList321",
    ends={
        Property(name="go_ExpressionList323", type=go_Arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Arguments322", type=go_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type324: BinaryAssociation = BinaryAssociation(
    name="Type324",
    ends={
        Property(name="go_Type326", type=go_Arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Arguments325", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ReceiverType327: BinaryAssociation = BinaryAssociation(
    name="ReceiverType327",
    ends={
        Property(name="go_ReceiverType", type=go_MethodExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MethodExpr328", type=go_ReceiverType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MethodName329: BinaryAssociation = BinaryAssociation(
    name="MethodName329",
    ends={
        Property(name="go_MethodName331", type=go_MethodExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MethodExpr330", type=go_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type332: BinaryAssociation = BinaryAssociation(
    name="Type332",
    ends={
        Property(name="go_Type334", type=go_ReceiverType, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ReceiverType333", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
UnaryExpr335: BinaryAssociation = BinaryAssociation(
    name="UnaryExpr335",
    ends={
        Property(name="go_UnaryExpr", type=go_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Expression336", type=go_UnaryExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionLinha337: BinaryAssociation = BinaryAssociation(
    name="ExpressionLinha337",
    ends={
        Property(name="go_ExpressionLinha", type=go_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Expression338", type=go_ExpressionLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
binary_op339: BinaryAssociation = BinaryAssociation(
    name="binary_op339",
    ends={
        Property(name="go_binary_op", type=go_ExpressionLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ExpressionLinha340", type=go_binary_op, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Index303: BinaryAssociation = BinaryAssociation(
    name="Index303",
    ends={
        Property(name="go_Index", type=go_cochetes, multiplicity=Multiplicity(1, 1)),
        Property(name="go_cochetes304", type=go_Index, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PrimaryExprLinha305: BinaryAssociation = BinaryAssociation(
    name="PrimaryExprLinha305",
    ends={
        Property(name="go_PrimaryExprLinha307", type=go_cochetes, multiplicity=Multiplicity(1, 1)),
        Property(name="go_cochetes306", type=go_PrimaryExprLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Slice308: BinaryAssociation = BinaryAssociation(
    name="Slice308",
    ends={
        Property(name="go_Slice", type=go_cochetes, multiplicity=Multiplicity(1, 1)),
        Property(name="go_cochetes309", type=go_Slice, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier310: BinaryAssociation = BinaryAssociation(
    name="identifier310",
    ends={
        Property(name="go_identifier312", type=go_Selector, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Selector311", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Slice313: BinaryAssociation = BinaryAssociation(
    name="Slice313",
    ends={
        Property(name="go_Slice315", type=go_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Index314", type=go_Slice, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decimals316: BinaryAssociation = BinaryAssociation(
    name="decimals316",
    ends={
        Property(name="go_decimals", type=go_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Slice317", type=go_decimals, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Type318: BinaryAssociation = BinaryAssociation(
    name="Type318",
    ends={
        Property(name="go_Type320", type=go_TypeAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeAssertion319", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression356: BinaryAssociation = BinaryAssociation(
    name="Expression356",
    ends={
        Property(name="go_Expression358", type=go_Conversion, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Conversion357", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Declaration359: BinaryAssociation = BinaryAssociation(
    name="Declaration359",
    ends={
        Property(name="go_Declaration361", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement360", type=go_Declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LabeledStmt362: BinaryAssociation = BinaryAssociation(
    name="LabeledStmt362",
    ends={
        Property(name="go_LabeledStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement363", type=go_LabeledStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SimpleStmt364: BinaryAssociation = BinaryAssociation(
    name="SimpleStmt364",
    ends={
        Property(name="go_SimpleStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement365", type=go_SimpleStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GoStmt366: BinaryAssociation = BinaryAssociation(
    name="GoStmt366",
    ends={
        Property(name="go_GoStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement367", type=go_GoStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ReturnStmt368: BinaryAssociation = BinaryAssociation(
    name="ReturnStmt368",
    ends={
        Property(name="go_ReturnStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement369", type=go_ReturnStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BreakStmt370: BinaryAssociation = BinaryAssociation(
    name="BreakStmt370",
    ends={
        Property(name="go_BreakStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement371", type=go_BreakStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression341: BinaryAssociation = BinaryAssociation(
    name="Expression341",
    ends={
        Property(name="go_Expression343", type=go_ExpressionLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ExpressionLinha342", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionLinha345: BinaryAssociation = BinaryAssociation(
    name="ExpressionLinha345",
    ends={
        Property(name="go_ExpressionLinha346", type=go_ExpressionLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ExpressionLinha344", type=go_ExpressionLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PrimaryExpr347: BinaryAssociation = BinaryAssociation(
    name="PrimaryExpr347",
    ends={
        Property(name="go_PrimaryExpr349", type=go_UnaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="go_UnaryExpr348", type=go_PrimaryExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
UnaryExpr351: BinaryAssociation = BinaryAssociation(
    name="UnaryExpr351",
    ends={
        Property(name="go_UnaryExpr352", type=go_UnaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="go_UnaryExpr350", type=go_UnaryExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type353: BinaryAssociation = BinaryAssociation(
    name="Type353",
    ends={
        Property(name="go_Type355", type=go_Conversion, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Conversion354", type=go_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionStmt389: BinaryAssociation = BinaryAssociation(
    name="ExpressionStmt389",
    ends={
        Property(name="go_ExpressionStmt", type=go_SimpleStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SimpleStmt390", type=go_ExpressionStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SendStmt391: BinaryAssociation = BinaryAssociation(
    name="SendStmt391",
    ends={
        Property(name="go_SendStmt", type=go_SimpleStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SimpleStmt392", type=go_SendStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IncDecStmt393: BinaryAssociation = BinaryAssociation(
    name="IncDecStmt393",
    ends={
        Property(name="go_IncDecStmt", type=go_SimpleStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SimpleStmt394", type=go_IncDecStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Assignment395: BinaryAssociation = BinaryAssociation(
    name="Assignment395",
    ends={
        Property(name="go_Assignment", type=go_SimpleStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SimpleStmt396", type=go_Assignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ShortVarDecl397: BinaryAssociation = BinaryAssociation(
    name="ShortVarDecl397",
    ends={
        Property(name="go_ShortVarDecl399", type=go_SimpleStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SimpleStmt398", type=go_ShortVarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Label400: BinaryAssociation = BinaryAssociation(
    name="Label400",
    ends={
        Property(name="go_Label", type=go_LabeledStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LabeledStmt401", type=go_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Statement402: BinaryAssociation = BinaryAssociation(
    name="Statement402",
    ends={
        Property(name="go_Statement404", type=go_LabeledStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_LabeledStmt403", type=go_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier405: BinaryAssociation = BinaryAssociation(
    name="identifier405",
    ends={
        Property(name="go_identifier407", type=go_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Label406", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression408: BinaryAssociation = BinaryAssociation(
    name="Expression408",
    ends={
        Property(name="go_Expression410", type=go_ExpressionStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ExpressionStmt409", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ContinueStmt372: BinaryAssociation = BinaryAssociation(
    name="ContinueStmt372",
    ends={
        Property(name="go_ContinueStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement373", type=go_ContinueStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GotoStmt374: BinaryAssociation = BinaryAssociation(
    name="GotoStmt374",
    ends={
        Property(name="go_GotoStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement375", type=go_GotoStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Block376: BinaryAssociation = BinaryAssociation(
    name="Block376",
    ends={
        Property(name="go_Block378", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement377", type=go_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IfStmt379: BinaryAssociation = BinaryAssociation(
    name="IfStmt379",
    ends={
        Property(name="go_IfStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement380", type=go_IfStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SwitchStmt381: BinaryAssociation = BinaryAssociation(
    name="SwitchStmt381",
    ends={
        Property(name="go_SwitchStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement382", type=go_SwitchStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SelectStmt383: BinaryAssociation = BinaryAssociation(
    name="SelectStmt383",
    ends={
        Property(name="go_SelectStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement384", type=go_SelectStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ForStmt385: BinaryAssociation = BinaryAssociation(
    name="ForStmt385",
    ends={
        Property(name="go_ForStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement386", type=go_ForStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DeferStmt387: BinaryAssociation = BinaryAssociation(
    name="DeferStmt387",
    ends={
        Property(name="go_DeferStmt", type=go_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Statement388", type=go_DeferStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IfStmt435: BinaryAssociation = BinaryAssociation(
    name="IfStmt435",
    ends={
        Property(name="go_IfStmt436", type=go_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfStmt434", type=go_IfStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switch_stmt_linha437: BinaryAssociation = BinaryAssociation(
    name="switch_stmt_linha437",
    ends={
        Property(name="go_switch_stmt_linha", type=go_SwitchStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SwitchStmt438", type=go_switch_stmt_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExprSwitchCase439: BinaryAssociation = BinaryAssociation(
    name="ExprSwitchCase439",
    ends={
        Property(name="go_ExprSwitchCase", type=go_ExprCaseClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ExprCaseClause", type=go_ExprSwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
StatementList440: BinaryAssociation = BinaryAssociation(
    name="StatementList440",
    ends={
        Property(name="go_StatementList442", type=go_ExprCaseClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ExprCaseClause441", type=go_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionList443: BinaryAssociation = BinaryAssociation(
    name="ExpressionList443",
    ends={
        Property(name="go_ExpressionList445", type=go_ExprSwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ExprSwitchCase444", type=go_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeSwitchGuard446: BinaryAssociation = BinaryAssociation(
    name="TypeSwitchGuard446",
    ends={
        Property(name="go_TypeSwitchGuard", type=go_switch_stmt_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_switch_stmt_linha447", type=go_TypeSwitchGuard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeCaseClause448: BinaryAssociation = BinaryAssociation(
    name="TypeCaseClause448",
    ends={
        Property(name="go_TypeCaseClause", type=go_switch_stmt_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_switch_stmt_linha449", type=go_TypeCaseClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
switch_stmt_linha451: BinaryAssociation = BinaryAssociation(
    name="switch_stmt_linha451",
    ends={
        Property(name="go_switch_stmt_linha452", type=go_switch_stmt_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_switch_stmt_linha450", type=go_switch_stmt_linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression453: BinaryAssociation = BinaryAssociation(
    name="Expression453",
    ends={
        Property(name="go_Expression455", type=go_switch_stmt_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_switch_stmt_linha454", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExprCaseClause456: BinaryAssociation = BinaryAssociation(
    name="ExprCaseClause456",
    ends={
        Property(name="go_ExprCaseClause458", type=go_switch_stmt_linha, multiplicity=Multiplicity(1, 1)),
        Property(name="go_switch_stmt_linha457", type=go_ExprCaseClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Channel411: BinaryAssociation = BinaryAssociation(
    name="Channel411",
    ends={
        Property(name="go_Channel", type=go_SendStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SendStmt412", type=go_Channel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression413: BinaryAssociation = BinaryAssociation(
    name="Expression413",
    ends={
        Property(name="go_Expression415", type=go_SendStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SendStmt414", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression416: BinaryAssociation = BinaryAssociation(
    name="Expression416",
    ends={
        Property(name="go_Expression418", type=go_Channel, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Channel417", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression419: BinaryAssociation = BinaryAssociation(
    name="Expression419",
    ends={
        Property(name="go_Expression421", type=go_IncDecStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IncDecStmt420", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionList422: BinaryAssociation = BinaryAssociation(
    name="ExpressionList422",
    ends={
        Property(name="go_ExpressionList424", type=go_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Assignment423", type=go_ExpressionList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
SimpleStmt425: BinaryAssociation = BinaryAssociation(
    name="SimpleStmt425",
    ends={
        Property(name="go_SimpleStmt427", type=go_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfStmt426", type=go_SimpleStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression428: BinaryAssociation = BinaryAssociation(
    name="Expression428",
    ends={
        Property(name="go_Expression430", type=go_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfStmt429", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Block431: BinaryAssociation = BinaryAssociation(
    name="Block431",
    ends={
        Property(name="go_Block433", type=go_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfStmt432", type=go_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
RangeClause479: BinaryAssociation = BinaryAssociation(
    name="RangeClause479",
    ends={
        Property(name="go_RangeClause", type=go_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForStmt480", type=go_RangeClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Block481: BinaryAssociation = BinaryAssociation(
    name="Block481",
    ends={
        Property(name="go_Block483", type=go_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForStmt482", type=go_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression484: BinaryAssociation = BinaryAssociation(
    name="Expression484",
    ends={
        Property(name="go_Expression486", type=go_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Condition485", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
InitStmt487: BinaryAssociation = BinaryAssociation(
    name="InitStmt487",
    ends={
        Property(name="go_InitStmt", type=go_ForClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForClause488", type=go_InitStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Condition489: BinaryAssociation = BinaryAssociation(
    name="Condition489",
    ends={
        Property(name="go_Condition491", type=go_ForClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForClause490", type=go_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PostStmt492: BinaryAssociation = BinaryAssociation(
    name="PostStmt492",
    ends={
        Property(name="go_PostStmt", type=go_ForClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForClause493", type=go_PostStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SimpleStmt494: BinaryAssociation = BinaryAssociation(
    name="SimpleStmt494",
    ends={
        Property(name="go_SimpleStmt496", type=go_InitStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_InitStmt495", type=go_SimpleStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SimpleStmt497: BinaryAssociation = BinaryAssociation(
    name="SimpleStmt497",
    ends={
        Property(name="go_SimpleStmt499", type=go_PostStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PostStmt498", type=go_SimpleStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionList500: BinaryAssociation = BinaryAssociation(
    name="ExpressionList500",
    ends={
        Property(name="go_ExpressionList502", type=go_RangeClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RangeClause501", type=go_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier459: BinaryAssociation = BinaryAssociation(
    name="identifier459",
    ends={
        Property(name="go_identifier461", type=go_TypeSwitchGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeSwitchGuard460", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PrimaryExpr462: BinaryAssociation = BinaryAssociation(
    name="PrimaryExpr462",
    ends={
        Property(name="go_PrimaryExpr464", type=go_TypeSwitchGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeSwitchGuard463", type=go_PrimaryExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeSwitchCase465: BinaryAssociation = BinaryAssociation(
    name="TypeSwitchCase465",
    ends={
        Property(name="go_TypeSwitchCase", type=go_TypeCaseClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeCaseClause466", type=go_TypeSwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
StatementList467: BinaryAssociation = BinaryAssociation(
    name="StatementList467",
    ends={
        Property(name="go_StatementList469", type=go_TypeCaseClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeCaseClause468", type=go_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TypeList470: BinaryAssociation = BinaryAssociation(
    name="TypeList470",
    ends={
        Property(name="go_TypeList", type=go_TypeSwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeSwitchCase471", type=go_TypeList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Type472: BinaryAssociation = BinaryAssociation(
    name="Type472",
    ends={
        Property(name="go_Type474", type=go_TypeList, multiplicity=Multiplicity(1, 1)),
        Property(name="go_TypeList473", type=go_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Condition475: BinaryAssociation = BinaryAssociation(
    name="Condition475",
    ends={
        Property(name="go_Condition", type=go_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForStmt476", type=go_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ForClause477: BinaryAssociation = BinaryAssociation(
    name="ForClause477",
    ends={
        Property(name="go_ForClause", type=go_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ForStmt478", type=go_ForClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
RecvStmt522: BinaryAssociation = BinaryAssociation(
    name="RecvStmt522",
    ends={
        Property(name="go_RecvStmt", type=go_CommCase, multiplicity=Multiplicity(1, 1)),
        Property(name="go_CommCase523", type=go_RecvStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionList524: BinaryAssociation = BinaryAssociation(
    name="ExpressionList524",
    ends={
        Property(name="go_ExpressionList526", type=go_RecvStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RecvStmt525", type=go_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IdentifierList527: BinaryAssociation = BinaryAssociation(
    name="IdentifierList527",
    ends={
        Property(name="go_IdentifierList529", type=go_RecvStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RecvStmt528", type=go_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
RecvExpr530: BinaryAssociation = BinaryAssociation(
    name="RecvExpr530",
    ends={
        Property(name="go_RecvExpr", type=go_RecvStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RecvStmt531", type=go_RecvExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression532: BinaryAssociation = BinaryAssociation(
    name="Expression532",
    ends={
        Property(name="go_Expression534", type=go_RecvExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RecvExpr533", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExpressionList535: BinaryAssociation = BinaryAssociation(
    name="ExpressionList535",
    ends={
        Property(name="go_ExpressionList537", type=go_ReturnStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ReturnStmt536", type=go_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Label538: BinaryAssociation = BinaryAssociation(
    name="Label538",
    ends={
        Property(name="go_Label540", type=go_BreakStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_BreakStmt539", type=go_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Label541: BinaryAssociation = BinaryAssociation(
    name="Label541",
    ends={
        Property(name="go_Label543", type=go_ContinueStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ContinueStmt542", type=go_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IdentifierList503: BinaryAssociation = BinaryAssociation(
    name="IdentifierList503",
    ends={
        Property(name="go_IdentifierList505", type=go_RangeClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RangeClause504", type=go_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression506: BinaryAssociation = BinaryAssociation(
    name="Expression506",
    ends={
        Property(name="go_Expression508", type=go_RangeClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_RangeClause507", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression509: BinaryAssociation = BinaryAssociation(
    name="Expression509",
    ends={
        Property(name="go_Expression511", type=go_GoStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_GoStmt510", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
CommClause512: BinaryAssociation = BinaryAssociation(
    name="CommClause512",
    ends={
        Property(name="go_CommClause", type=go_SelectStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_SelectStmt513", type=go_CommClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CommCase514: BinaryAssociation = BinaryAssociation(
    name="CommCase514",
    ends={
        Property(name="go_CommCase", type=go_CommClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_CommClause515", type=go_CommCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
StatementList516: BinaryAssociation = BinaryAssociation(
    name="StatementList516",
    ends={
        Property(name="go_StatementList518", type=go_CommClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_CommClause517", type=go_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SendStmt519: BinaryAssociation = BinaryAssociation(
    name="SendStmt519",
    ends={
        Property(name="go_SendStmt521", type=go_CommCase, multiplicity=Multiplicity(1, 1)),
        Property(name="go_CommCase520", type=go_SendStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ImportPath561: BinaryAssociation = BinaryAssociation(
    name="ImportPath561",
    ends={
        Property(name="go_ImportPath", type=go_ImportSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ImportSpec562", type=go_ImportPath, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
string_lit563: BinaryAssociation = BinaryAssociation(
    name="string_lit563",
    ends={
        Property(name="go_string_lit565", type=go_ImportPath, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ImportPath564", type=go_string_lit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decimals567: BinaryAssociation = BinaryAssociation(
    name="decimals567",
    ends={
        Property(name="go_decimals568", type=go_decimals, multiplicity=Multiplicity(1, 1)),
        Property(name="go_decimals566", type=go_decimals, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exponent569: BinaryAssociation = BinaryAssociation(
    name="exponent569",
    ends={
        Property(name="go_exponent", type=go_decimals, multiplicity=Multiplicity(1, 1)),
        Property(name="go_decimals570", type=go_exponent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exponen571: BinaryAssociation = BinaryAssociation(
    name="exponen571",
    ends={
        Property(name="go_exponent573", type=go_decimals, multiplicity=Multiplicity(1, 1)),
        Property(name="go_decimals572", type=go_exponent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Label544: BinaryAssociation = BinaryAssociation(
    name="Label544",
    ends={
        Property(name="go_Label546", type=go_GotoStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_GotoStmt545", type=go_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expression547: BinaryAssociation = BinaryAssociation(
    name="Expression547",
    ends={
        Property(name="go_Expression549", type=go_DeferStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="go_DeferStmt548", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PackageName550: BinaryAssociation = BinaryAssociation(
    name="PackageName550",
    ends={
        Property(name="go_PackageName552", type=go_PackageClause, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PackageClause551", type=go_PackageName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifier553: BinaryAssociation = BinaryAssociation(
    name="identifier553",
    ends={
        Property(name="go_identifier555", type=go_PackageName, multiplicity=Multiplicity(1, 1)),
        Property(name="go_PackageName554", type=go_identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ImportSpec556: BinaryAssociation = BinaryAssociation(
    name="ImportSpec556",
    ends={
        Property(name="go_ImportSpec", type=go_ImportDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ImportDecl557", type=go_ImportSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PackageName558: BinaryAssociation = BinaryAssociation(
    name="PackageName558",
    ends={
        Property(name="go_PackageName560", type=go_ImportSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ImportSpec559", type=go_PackageName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decimals574: BinaryAssociation = BinaryAssociation(
    name="decimals574",
    ends={
        Property(name="go_decimals576", type=go_exponent, multiplicity=Multiplicity(1, 1)),
        Property(name="go_exponent575", type=go_decimals, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decimals577: BinaryAssociation = BinaryAssociation(
    name="decimals577",
    ends={
        Property(name="go_decimals578", type=go_imaginary_lit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_imaginary_lit", type=go_decimals, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
float_lit579: BinaryAssociation = BinaryAssociation(
    name="float_lit579",
    ends={
        Property(name="go_float_lit581", type=go_imaginary_lit, multiplicity=Multiplicity(1, 1)),
        Property(name="go_imaginary_lit580", type=go_float_lit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_go_Parameters_Receiver = Generalization(general=Receiver, specific=go_Parameters)
gen_go_AliasDecl_TypeSpec = Generalization(general=TypeSpec, specific=go_AliasDecl)
gen_go_TypeDef_TypeSpec = Generalization(general=TypeSpec, specific=go_TypeDef)
gen_go_QualifiedIdent_OperandName = Generalization(general=OperandName, specific=go_QualifiedIdent)
gen_go_CompositeLit_Literal = Generalization(general=Literal, specific=go_CompositeLit)
gen_go_FunctionLit_Literal = Generalization(general=Literal, specific=go_FunctionLit)
gen_go_SimpleStmt_SwitchStmt = Generalization(general=SwitchStmt, specific=go_SimpleStmt)
gen_go_identifier_OperandName = Generalization(general=OperandName, specific=go_identifier)
gen_go_decimals_float_lit = Generalization(general=float_lit, specific=go_decimals)

# Domain Model
domain_model = DomainModel(
    name="go",
    types={go_Type, go_TypeName, go_TypeLit, go_identifier, go_TypeNameLinha, go_QualifiedIdent, go_TypeLitLinha, go_SouceFile, go_PackageClause, go_ImportDecl, go_TopLevelDecl, go_StructType, go_PointerType, go_FunctionType, go_InterfaceType, go_MapType, go_ChannelType, go_EmbeddedField, go_Tag, go_string_lit, go_Signature, go_Parameters, go_Result, go_ArrayLength, go_ElementType, go_Expression, go_FieldDecl, go_IdentifierList, go_MethodName, go_InterfaceTypeName, go_KeyType, go_Block, go_StatementList, Receiver, go_ParameterList, go_ParameterDecl, go_MethodSpec, go_FunctionBody, go_Receiver, go_ConstSpec, go_ExpressionList, go_TypeSpec, go_Statement, go_Declaration, go_ConstDecl, go_TypeDecl, go_VarDecl, go_topLevelDeclLinha, go_VarSpec, go_FunctionName, go_ShortVarDecl, go_FunctionDecl, go_AliasDecl, TypeSpec, go_OperandName, go_TypeDef, go_BasicLit, go_float_lit, go_rune_lit, OperandName, go_PackageName, go_MethodDecl, go_Operand, go_Literal, go_ElementList, go_KeyedElement, go_Element, go_Key, go_CompositeLit, Literal, go_LiteralType, go_LiteralValue, go_LiteralTypeLinha, go_Conversion, go_MethodExpr, go_Arguments, go_ponto, go_cochetes, go_Selector, go_TypeAssertion, go_FieldName, go_FunctionLit, go_PrimaryExpr, go_PrimaryExprLinha, go_ReceiverType, go_UnaryExpr, go_ExpressionLinha, go_binary_op, go_Index, go_Slice, go_decimals, go_LabeledStmt, go_SimpleStmt, go_GoStmt, go_ReturnStmt, go_BreakStmt, go_ContinueStmt, go_ExpressionStmt, go_SendStmt, go_IncDecStmt, go_Assignment, go_Label, go_GotoStmt, go_IfStmt, go_SwitchStmt, go_SelectStmt, go_ForStmt, go_DeferStmt, SwitchStmt, go_switch_stmt_linha, go_ExprCaseClause, go_ExprSwitchCase, go_TypeSwitchGuard, go_TypeCaseClause, go_Channel, go_RangeClause, go_InitStmt, go_PostStmt, go_TypeSwitchCase, go_TypeList, go_Condition, go_ForClause, go_RecvStmt, go_RecvExpr, go_CommClause, go_CommCase, float_lit, go_exponent, go_ImportSpec, go_ImportPath, go_imaginary_lit},
    associations={TypeName5, TypeLit6, Type9, identifier11, TypeNameLinha13, identifier15, TypeNameLinha19, QualifiedIdent21, PackageClause0, ImportDecl1, TopLevelDecl3, StructType25, PointerType27, FunctionType29, InterfaceType31, MapType33, TypeLitLinha23, Type53, EmbeddedField56, Tag58, TypeName60, string_lit63, Type65, Signature68, Parameters70, ChannelType35, Result72, ArrayLength37, ElementType39, TypeLitLinha42, Expression44, Type46, FieldDecl49, IdentifierList51, MethodName92, Signature94, InterfaceTypeName97, identifier99, TypeName102, KeyType105, ElementType107, Type110, ElementType113, Parameters74, StatementList116, Type77, ParameterList80, ParameterDecl82, IdentifierList84, Type87, MethodSpec90, FunctionName129, Signature131, FunctionBody134, Receiver136, MethodName138, ConstSpec141, IdentifierList143, Type146, ExpressionList149, identifier151, Expression154, Statement117, ConstDecl119, TypeDecl120, VarDecl122, Declaration124, topLevelDeclLinha127, VarSpec165, IdentifierList167, Type170, ExpressionList173, IdentifierList176, ExpressionList178, FunctionName181, Signature183, FunctionBody186, TypeSpec157, identifier159, Type162, OperandName207, Expression209, BasicLit212, float_lit214, rune_lit216, string_lit218, PackageName221, identifier189, Block192, Receiver195, MethodName197, Signature200, FunctionBody203, Literal206, ArrayLength243, ElementType246, ElementList249, KeyedElement251, Expression253, LiteralValue255, Key258, Element260, identifier223, LiteralType226, LiteralValue227, StructType229, LiteralTypeLinha232, ElementType234, MapType237, TypeName240, Conversion283, MethodExpr285, Arguments287, PrimaryExprLinha290, ponto292, cochetes294, Selector296, PrimaryExprLinha298, TypeAssertion301, FieldName263, Expression265, LiteralValue268, identifier271, Signature274, FunctionBody276, Operand279, PrimaryExprLinha281, ExpressionList321, Type324, ReceiverType327, MethodName329, Type332, UnaryExpr335, ExpressionLinha337, binary_op339, Index303, PrimaryExprLinha305, Slice308, identifier310, Slice313, decimals316, Type318, Expression356, Declaration359, LabeledStmt362, SimpleStmt364, GoStmt366, ReturnStmt368, BreakStmt370, Expression341, ExpressionLinha345, PrimaryExpr347, UnaryExpr351, Type353, ExpressionStmt389, SendStmt391, IncDecStmt393, Assignment395, ShortVarDecl397, Label400, Statement402, identifier405, Expression408, ContinueStmt372, GotoStmt374, Block376, IfStmt379, SwitchStmt381, SelectStmt383, ForStmt385, DeferStmt387, IfStmt435, switch_stmt_linha437, ExprSwitchCase439, StatementList440, ExpressionList443, TypeSwitchGuard446, TypeCaseClause448, switch_stmt_linha451, Expression453, ExprCaseClause456, Channel411, Expression413, Expression416, Expression419, ExpressionList422, SimpleStmt425, Expression428, Block431, RangeClause479, Block481, Expression484, InitStmt487, Condition489, PostStmt492, SimpleStmt494, SimpleStmt497, ExpressionList500, identifier459, PrimaryExpr462, TypeSwitchCase465, StatementList467, TypeList470, Type472, Condition475, ForClause477, RecvStmt522, ExpressionList524, IdentifierList527, RecvExpr530, Expression532, ExpressionList535, Label538, Label541, IdentifierList503, Expression506, Expression509, CommClause512, CommCase514, StatementList516, SendStmt519, ImportPath561, string_lit563, decimals567, exponent569, exponen571, Label544, Expression547, PackageName550, identifier553, ImportSpec556, PackageName558, decimals574, decimals577, float_lit579},
    generalizations={gen_go_Parameters_Receiver, gen_go_AliasDecl_TypeSpec, gen_go_TypeDef_TypeSpec, gen_go_QualifiedIdent_OperandName, gen_go_CompositeLit_Literal, gen_go_FunctionLit_Literal, gen_go_SimpleStmt_SwitchStmt, gen_go_identifier_OperandName, gen_go_decimals_float_lit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)