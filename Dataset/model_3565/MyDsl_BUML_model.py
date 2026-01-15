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
myDsl_Type = Class(name="myDsl::Type")
myDsl_TypeName = Class(name="myDsl::TypeName")
myDsl_TypeLit = Class(name="myDsl::TypeLit")
myDsl_Model = Class(name="myDsl::Model")
myDsl_SourceFile = Class(name="myDsl::SourceFile")
myDsl_MapType = Class(name="myDsl::MapType")
myDsl_ChannelType = Class(name="myDsl::ChannelType")
myDsl_ArrayLength = Class(name="myDsl::ArrayLength")
myDsl_ElementType = Class(name="myDsl::ElementType")
myDsl_TypeNameLinha = Class(name="myDsl::TypeNameLinha")
myDsl_TypeLitLinha = Class(name="myDsl::TypeLitLinha")
myDsl_StructType = Class(name="myDsl::StructType")
myDsl_PointerType = Class(name="myDsl::PointerType")
myDsl_FunctionType = Class(name="myDsl::FunctionType")
myDsl_InterfaceType = Class(name="myDsl::InterfaceType")
myDsl_IdentifierList = Class(name="myDsl::IdentifierList")
myDsl_Expression = Class(name="myDsl::Expression")
myDsl_FieldDecl = Class(name="myDsl::FieldDecl")
myDsl_BaseType = Class(name="myDsl::BaseType")
myDsl_EmbeddedField = Class(name="myDsl::EmbeddedField")
myDsl_Tag = Class(name="myDsl::Tag")
myDsl_Parameters = Class(name="myDsl::Parameters")
myDsl_Result = Class(name="myDsl::Result")
myDsl_Signature = Class(name="myDsl::Signature")
myDsl_ParameterList = Class(name="myDsl::ParameterList")
myDsl_ParameterDecl = Class(name="myDsl::ParameterDecl")
myDsl_MethodSpec = Class(name="myDsl::MethodSpec")
myDsl_MethodName = Class(name="myDsl::MethodName")
myDsl_KeyType = Class(name="myDsl::KeyType")
myDsl_InterfaceTypeName = Class(name="myDsl::InterfaceTypeName")
myDsl_ChannelTypeLinha = Class(name="myDsl::ChannelTypeLinha")
myDsl_Declaration = Class(name="myDsl::Declaration")
myDsl_ConstDecl = Class(name="myDsl::ConstDecl")
myDsl_TypeDecl = Class(name="myDsl::TypeDecl")
myDsl_VarDecl = Class(name="myDsl::VarDecl")
myDsl_Block = Class(name="myDsl::Block")
myDsl_StatementList = Class(name="myDsl::StatementList")
myDsl_Statement = Class(name="myDsl::Statement")
myDsl_MethodDecl = Class(name="myDsl::MethodDecl")
myDsl_ConstSpec = Class(name="myDsl::ConstSpec")
myDsl_TopLevelDecl = Class(name="myDsl::TopLevelDecl")
myDsl_FunctionDecl = Class(name="myDsl::FunctionDecl")
myDsl_ExpressionList = Class(name="myDsl::ExpressionList")
myDsl_TypeSpec = Class(name="myDsl::TypeSpec")
myDsl_AliasDecl = Class(name="myDsl::AliasDecl")
myDsl_TypeDef = Class(name="myDsl::TypeDef")
myDsl_VarSpec = Class(name="myDsl::VarSpec")
myDsl_FunctionName = Class(name="myDsl::FunctionName")
myDsl_FunctionBody = Class(name="myDsl::FunctionBody")
myDsl_ShortVarDecl = Class(name="myDsl::ShortVarDecl")
myDsl_Receiver = Class(name="myDsl::Receiver")
myDsl_OperandName = Class(name="myDsl::OperandName")
myDsl_BasicLit = Class(name="myDsl::BasicLit")
myDsl_Operand = Class(name="myDsl::Operand")
myDsl_Literal = Class(name="myDsl::Literal")
myDsl_CompositeLit = Class(name="myDsl::CompositeLit")
myDsl_FunctionLit = Class(name="myDsl::FunctionLit")
myDsl_LiteralTypeLinha = Class(name="myDsl::LiteralTypeLinha")
myDsl_LiteralType = Class(name="myDsl::LiteralType")
myDsl_LiteralValue = Class(name="myDsl::LiteralValue")
myDsl_KeyedElement = Class(name="myDsl::KeyedElement")
myDsl_ElementList = Class(name="myDsl::ElementList")
myDsl_FieldName = Class(name="myDsl::FieldName")
myDsl_Key = Class(name="myDsl::Key")
myDsl_Element = Class(name="myDsl::Element")
myDsl_PrimaryExprLinha = Class(name="myDsl::PrimaryExprLinha")
myDsl_Conversion = Class(name="myDsl::Conversion")
myDsl_MethodExpr = Class(name="myDsl::MethodExpr")
myDsl_Selector = Class(name="myDsl::Selector")
myDsl_PrimaryExpr = Class(name="myDsl::PrimaryExpr")
myDsl_Index = Class(name="myDsl::Index")
myDsl_Slice = Class(name="myDsl::Slice")
myDsl_TypeAssertion = Class(name="myDsl::TypeAssertion")
myDsl_Arguments = Class(name="myDsl::Arguments")
myDsl_UnaryExpr = Class(name="myDsl::UnaryExpr")
myDsl_Expression_Linha = Class(name="myDsl::Expression::Linha")
myDsl_Expression1 = Class(name="myDsl::Expression1")
myDsl_ReceiverType = Class(name="myDsl::ReceiverType")
myDsl_LabeledStmt = Class(name="myDsl::LabeledStmt")
myDsl_BINARY_OP = Class(name="myDsl::BINARY::OP")
myDsl_GotoStmt = Class(name="myDsl::GotoStmt")
myDsl_FallthroughStmt = Class(name="myDsl::FallthroughStmt")
myDsl_IfStmt = Class(name="myDsl::IfStmt")
myDsl_SwitchStmt = Class(name="myDsl::SwitchStmt")
myDsl_SimpleStmt = Class(name="myDsl::SimpleStmt")
myDsl_GoStmt = Class(name="myDsl::GoStmt")
myDsl_ReturnStmt = Class(name="myDsl::ReturnStmt")
myDsl_BreakStmt = Class(name="myDsl::BreakStmt")
myDsl_ContinueStmt = Class(name="myDsl::ContinueStmt")
myDsl_SimpleStmtLinha = Class(name="myDsl::SimpleStmtLinha")
myDsl_SelectStmt = Class(name="myDsl::SelectStmt")
myDsl_ForStmt = Class(name="myDsl::ForStmt")
myDsl_DeferStmt = Class(name="myDsl::DeferStmt")
myDsl_EmptyStmt = Class(name="myDsl::EmptyStmt")
myDsl_IfStmtLinha = Class(name="myDsl::IfStmtLinha")
myDsl_assign_op = Class(name="myDsl::assign::op")
myDsl_Label = Class(name="myDsl::Label")
myDsl_ExprCaseClause = Class(name="myDsl::ExprCaseClause")
myDsl_ExprSwitchCase = Class(name="myDsl::ExprSwitchCase")
myDsl_ExprSwitchStmt = Class(name="myDsl::ExprSwitchStmt")
myDsl_TypeSwitchStmt = Class(name="myDsl::TypeSwitchStmt")
myDsl_TypeSwitchCase = Class(name="myDsl::TypeSwitchCase")
myDsl_TypeSwitchGuard = Class(name="myDsl::TypeSwitchGuard")
myDsl_TypeCaseClause = Class(name="myDsl::TypeCaseClause")
myDsl_ForStmtLinha = Class(name="myDsl::ForStmtLinha")
myDsl_Condition = Class(name="myDsl::Condition")
myDsl_PostStmt = Class(name="myDsl::PostStmt")
myDsl_TypeList = Class(name="myDsl::TypeList")
myDsl_ForStmtLinhaLinha = Class(name="myDsl::ForStmtLinhaLinha")
myDsl_CommCase = Class(name="myDsl::CommCase")
myDsl_CommCaseLinha = Class(name="myDsl::CommCaseLinha")
myDsl_CommClause = Class(name="myDsl::CommClause")
myDsl_RecvExpr = Class(name="myDsl::RecvExpr")
myDsl_PackageClause = Class(name="myDsl::PackageClause")
myDsl_ImportDecl = Class(name="myDsl::ImportDecl")
myDsl_PackageName = Class(name="myDsl::PackageName")
myDsl_ImportSpec = Class(name="myDsl::ImportSpec")

# myDsl_Type class attributes and methods

# myDsl_TypeName class attributes and methods
myDsl_TypeName_id: Property = Property(name="id", type=StringType)
myDsl_TypeName.attributes={myDsl_TypeName_id}

# myDsl_TypeLit class attributes and methods

# myDsl_Model class attributes and methods

# myDsl_SourceFile class attributes and methods

# myDsl_MapType class attributes and methods
myDsl_MapType_map: Property = Property(name="map", type=StringType)
myDsl_MapType.attributes={myDsl_MapType_map}

# myDsl_ChannelType class attributes and methods
myDsl_ChannelType_chan: Property = Property(name="chan", type=StringType)
myDsl_ChannelType.attributes={myDsl_ChannelType_chan}

# myDsl_ArrayLength class attributes and methods

# myDsl_ElementType class attributes and methods

# myDsl_TypeNameLinha class attributes and methods
myDsl_TypeNameLinha_id: Property = Property(name="id", type=StringType)
myDsl_TypeNameLinha.attributes={myDsl_TypeNameLinha_id}

# myDsl_TypeLitLinha class attributes and methods

# myDsl_StructType class attributes and methods
myDsl_StructType_struct: Property = Property(name="struct", type=StringType)
myDsl_StructType.attributes={myDsl_StructType_struct}

# myDsl_PointerType class attributes and methods

# myDsl_FunctionType class attributes and methods
myDsl_FunctionType_func: Property = Property(name="func", type=StringType)
myDsl_FunctionType.attributes={myDsl_FunctionType_func}

# myDsl_InterfaceType class attributes and methods
myDsl_InterfaceType_interface: Property = Property(name="interface", type=StringType)
myDsl_InterfaceType.attributes={myDsl_InterfaceType_interface}

# myDsl_IdentifierList class attributes and methods
myDsl_IdentifierList_id: Property = Property(name="id", type=StringType)
myDsl_IdentifierList_id1: Property = Property(name="id1", type=StringType)
myDsl_IdentifierList.attributes={myDsl_IdentifierList_id, myDsl_IdentifierList_id1}

# myDsl_Expression class attributes and methods

# myDsl_FieldDecl class attributes and methods

# myDsl_BaseType class attributes and methods

# myDsl_EmbeddedField class attributes and methods

# myDsl_Tag class attributes and methods
myDsl_Tag_string_lit: Property = Property(name="string_lit", type=StringType)
myDsl_Tag.attributes={myDsl_Tag_string_lit}

# myDsl_Parameters class attributes and methods

# myDsl_Result class attributes and methods

# myDsl_Signature class attributes and methods

# myDsl_ParameterList class attributes and methods

# myDsl_ParameterDecl class attributes and methods

# myDsl_MethodSpec class attributes and methods

# myDsl_MethodName class attributes and methods
myDsl_MethodName_id: Property = Property(name="id", type=StringType)
myDsl_MethodName.attributes={myDsl_MethodName_id}

# myDsl_KeyType class attributes and methods

# myDsl_InterfaceTypeName class attributes and methods

# myDsl_ChannelTypeLinha class attributes and methods
myDsl_ChannelTypeLinha_aNY_OTHER: Property = Property(name="aNY_OTHER", type=StringType)
myDsl_ChannelTypeLinha.attributes={myDsl_ChannelTypeLinha_aNY_OTHER}

# myDsl_Declaration class attributes and methods

# myDsl_ConstDecl class attributes and methods
myDsl_ConstDecl_const: Property = Property(name="const", type=StringType)
myDsl_ConstDecl.attributes={myDsl_ConstDecl_const}

# myDsl_TypeDecl class attributes and methods
myDsl_TypeDecl_typekeyword: Property = Property(name="typekeyword", type=StringType)
myDsl_TypeDecl.attributes={myDsl_TypeDecl_typekeyword}

# myDsl_VarDecl class attributes and methods
myDsl_VarDecl_var: Property = Property(name="var", type=StringType)
myDsl_VarDecl.attributes={myDsl_VarDecl_var}

# myDsl_Block class attributes and methods

# myDsl_StatementList class attributes and methods

# myDsl_Statement class attributes and methods

# myDsl_MethodDecl class attributes and methods

# myDsl_ConstSpec class attributes and methods

# myDsl_TopLevelDecl class attributes and methods

# myDsl_FunctionDecl class attributes and methods

# myDsl_ExpressionList class attributes and methods

# myDsl_TypeSpec class attributes and methods

# myDsl_AliasDecl class attributes and methods
myDsl_AliasDecl_id: Property = Property(name="id", type=StringType)
myDsl_AliasDecl.attributes={myDsl_AliasDecl_id}

# myDsl_TypeDef class attributes and methods
myDsl_TypeDef_id: Property = Property(name="id", type=StringType)
myDsl_TypeDef.attributes={myDsl_TypeDef_id}

# myDsl_VarSpec class attributes and methods

# myDsl_FunctionName class attributes and methods
myDsl_FunctionName_id: Property = Property(name="id", type=StringType)
myDsl_FunctionName.attributes={myDsl_FunctionName_id}

# myDsl_FunctionBody class attributes and methods

# myDsl_ShortVarDecl class attributes and methods

# myDsl_Receiver class attributes and methods

# myDsl_OperandName class attributes and methods
myDsl_OperandName_id: Property = Property(name="id", type=StringType)
myDsl_OperandName.attributes={myDsl_OperandName_id}

# myDsl_BasicLit class attributes and methods
myDsl_BasicLit_float_lit: Property = Property(name="float_lit", type=StringType)
myDsl_BasicLit_imaginary_lit: Property = Property(name="imaginary_lit", type=StringType)
myDsl_BasicLit_rune_lit: Property = Property(name="rune_lit", type=StringType)
myDsl_BasicLit_string_lit: Property = Property(name="string_lit", type=StringType)
myDsl_BasicLit_int_lit: Property = Property(name="int_lit", type=StringType)
myDsl_BasicLit.attributes={myDsl_BasicLit_int_lit, myDsl_BasicLit_float_lit, myDsl_BasicLit_rune_lit, myDsl_BasicLit_string_lit, myDsl_BasicLit_imaginary_lit}

# myDsl_Operand class attributes and methods

# myDsl_Literal class attributes and methods

# myDsl_CompositeLit class attributes and methods

# myDsl_FunctionLit class attributes and methods
myDsl_FunctionLit_func: Property = Property(name="func", type=StringType)
myDsl_FunctionLit.attributes={myDsl_FunctionLit_func}

# myDsl_LiteralTypeLinha class attributes and methods

# myDsl_LiteralType class attributes and methods

# myDsl_LiteralValue class attributes and methods

# myDsl_KeyedElement class attributes and methods

# myDsl_ElementList class attributes and methods

# myDsl_FieldName class attributes and methods
myDsl_FieldName_id: Property = Property(name="id", type=StringType)
myDsl_FieldName.attributes={myDsl_FieldName_id}

# myDsl_Key class attributes and methods

# myDsl_Element class attributes and methods

# myDsl_PrimaryExprLinha class attributes and methods

# myDsl_Conversion class attributes and methods

# myDsl_MethodExpr class attributes and methods

# myDsl_Selector class attributes and methods
myDsl_Selector_id: Property = Property(name="id", type=StringType)
myDsl_Selector.attributes={myDsl_Selector_id}

# myDsl_PrimaryExpr class attributes and methods

# myDsl_Index class attributes and methods

# myDsl_Slice class attributes and methods

# myDsl_TypeAssertion class attributes and methods

# myDsl_Arguments class attributes and methods

# myDsl_UnaryExpr class attributes and methods

# myDsl_Expression_Linha class attributes and methods

# myDsl_Expression1 class attributes and methods

# myDsl_ReceiverType class attributes and methods

# myDsl_LabeledStmt class attributes and methods

# myDsl_BINARY_OP class attributes and methods
myDsl_BINARY_OP_rEL_OP: Property = Property(name="rEL_OP", type=StringType)
myDsl_BINARY_OP_aDD_OP: Property = Property(name="aDD_OP", type=StringType)
myDsl_BINARY_OP.attributes={myDsl_BINARY_OP_aDD_OP, myDsl_BINARY_OP_rEL_OP}

# myDsl_GotoStmt class attributes and methods
myDsl_GotoStmt_goto: Property = Property(name="goto", type=StringType)
myDsl_GotoStmt.attributes={myDsl_GotoStmt_goto}

# myDsl_FallthroughStmt class attributes and methods
myDsl_FallthroughStmt_fallthrough: Property = Property(name="fallthrough", type=StringType)
myDsl_FallthroughStmt.attributes={myDsl_FallthroughStmt_fallthrough}

# myDsl_IfStmt class attributes and methods
myDsl_IfStmt_if: Property = Property(name="if", type=StringType)
myDsl_IfStmt_else: Property = Property(name="else", type=StringType)
myDsl_IfStmt.attributes={myDsl_IfStmt_else, myDsl_IfStmt_if}

# myDsl_SwitchStmt class attributes and methods

# myDsl_SimpleStmt class attributes and methods

# myDsl_GoStmt class attributes and methods
myDsl_GoStmt_go: Property = Property(name="go", type=StringType)
myDsl_GoStmt.attributes={myDsl_GoStmt_go}

# myDsl_ReturnStmt class attributes and methods
myDsl_ReturnStmt_return: Property = Property(name="return", type=StringType)
myDsl_ReturnStmt.attributes={myDsl_ReturnStmt_return}

# myDsl_BreakStmt class attributes and methods
myDsl_BreakStmt_break: Property = Property(name="break", type=StringType)
myDsl_BreakStmt.attributes={myDsl_BreakStmt_break}

# myDsl_ContinueStmt class attributes and methods
myDsl_ContinueStmt_continue: Property = Property(name="continue", type=StringType)
myDsl_ContinueStmt.attributes={myDsl_ContinueStmt_continue}

# myDsl_SimpleStmtLinha class attributes and methods
myDsl_SimpleStmtLinha_aNY_OTHER: Property = Property(name="aNY_OTHER", type=StringType)
myDsl_SimpleStmtLinha.attributes={myDsl_SimpleStmtLinha_aNY_OTHER}

# myDsl_SelectStmt class attributes and methods
myDsl_SelectStmt_select: Property = Property(name="select", type=StringType)
myDsl_SelectStmt.attributes={myDsl_SelectStmt_select}

# myDsl_ForStmt class attributes and methods
myDsl_ForStmt_for: Property = Property(name="for", type=StringType)
myDsl_ForStmt_range: Property = Property(name="range", type=StringType)
myDsl_ForStmt.attributes={myDsl_ForStmt_range, myDsl_ForStmt_for}

# myDsl_DeferStmt class attributes and methods
myDsl_DeferStmt_defer: Property = Property(name="defer", type=StringType)
myDsl_DeferStmt.attributes={myDsl_DeferStmt_defer}

# myDsl_EmptyStmt class attributes and methods
myDsl_EmptyStmt_aNY_OTHER: Property = Property(name="aNY_OTHER", type=StringType)
myDsl_EmptyStmt.attributes={myDsl_EmptyStmt_aNY_OTHER}

# myDsl_IfStmtLinha class attributes and methods
myDsl_IfStmtLinha_else: Property = Property(name="else", type=StringType)
myDsl_IfStmtLinha.attributes={myDsl_IfStmtLinha_else}

# myDsl_assign_op class attributes and methods
myDsl_assign_op_aDD_OP: Property = Property(name="aDD_OP", type=StringType)
myDsl_assign_op_mUL_OP: Property = Property(name="mUL_OP", type=StringType)
myDsl_assign_op.attributes={myDsl_assign_op_aDD_OP, myDsl_assign_op_mUL_OP}

# myDsl_Label class attributes and methods
myDsl_Label_id: Property = Property(name="id", type=StringType)
myDsl_Label.attributes={myDsl_Label_id}

# myDsl_ExprCaseClause class attributes and methods

# myDsl_ExprSwitchCase class attributes and methods
myDsl_ExprSwitchCase_case: Property = Property(name="case", type=StringType)
myDsl_ExprSwitchCase_default: Property = Property(name="default", type=StringType)
myDsl_ExprSwitchCase.attributes={myDsl_ExprSwitchCase_case, myDsl_ExprSwitchCase_default}

# myDsl_ExprSwitchStmt class attributes and methods
myDsl_ExprSwitchStmt_switch: Property = Property(name="switch", type=StringType)
myDsl_ExprSwitchStmt.attributes={myDsl_ExprSwitchStmt_switch}

# myDsl_TypeSwitchStmt class attributes and methods
myDsl_TypeSwitchStmt_switch: Property = Property(name="switch", type=StringType)
myDsl_TypeSwitchStmt.attributes={myDsl_TypeSwitchStmt_switch}

# myDsl_TypeSwitchCase class attributes and methods
myDsl_TypeSwitchCase_case: Property = Property(name="case", type=StringType)
myDsl_TypeSwitchCase_default: Property = Property(name="default", type=StringType)
myDsl_TypeSwitchCase.attributes={myDsl_TypeSwitchCase_default, myDsl_TypeSwitchCase_case}

# myDsl_TypeSwitchGuard class attributes and methods
myDsl_TypeSwitchGuard_id: Property = Property(name="id", type=StringType)
myDsl_TypeSwitchGuard_type: Property = Property(name="type", type=StringType)
myDsl_TypeSwitchGuard.attributes={myDsl_TypeSwitchGuard_type, myDsl_TypeSwitchGuard_id}

# myDsl_TypeCaseClause class attributes and methods

# myDsl_ForStmtLinha class attributes and methods
myDsl_ForStmtLinha_vazio: Property = Property(name="vazio", type=StringType)
myDsl_ForStmtLinha.attributes={myDsl_ForStmtLinha_vazio}

# myDsl_Condition class attributes and methods

# myDsl_PostStmt class attributes and methods

# myDsl_TypeList class attributes and methods

# myDsl_ForStmtLinhaLinha class attributes and methods
myDsl_ForStmtLinhaLinha_range: Property = Property(name="range", type=StringType)
myDsl_ForStmtLinhaLinha.attributes={myDsl_ForStmtLinhaLinha_range}

# myDsl_CommCase class attributes and methods
myDsl_CommCase_case: Property = Property(name="case", type=StringType)
myDsl_CommCase_default: Property = Property(name="default", type=StringType)
myDsl_CommCase.attributes={myDsl_CommCase_case, myDsl_CommCase_default}

# myDsl_CommCaseLinha class attributes and methods

# myDsl_CommClause class attributes and methods

# myDsl_RecvExpr class attributes and methods

# myDsl_PackageClause class attributes and methods
myDsl_PackageClause_package: Property = Property(name="package", type=StringType)
myDsl_PackageClause.attributes={myDsl_PackageClause_package}

# myDsl_ImportDecl class attributes and methods
myDsl_ImportDecl_importt: Property = Property(name="importt", type=StringType)
myDsl_ImportDecl.attributes={myDsl_ImportDecl_importt}

# myDsl_PackageName class attributes and methods
myDsl_PackageName_id: Property = Property(name="id", type=StringType)
myDsl_PackageName.attributes={myDsl_PackageName_id}

# myDsl_ImportSpec class attributes and methods
myDsl_ImportSpec_sTRING_LIT: Property = Property(name="sTRING_LIT", type=StringType)
myDsl_ImportSpec.attributes={myDsl_ImportSpec_sTRING_LIT}

# Relationships
typeName1: BinaryAssociation = BinaryAssociation(
    name="typeName1",
    ends={
        Property(name="myDsl_TypeName", type=myDsl_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Type", type=myDsl_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeLit2: BinaryAssociation = BinaryAssociation(
    name="typeLit2",
    ends={
        Property(name="myDsl_TypeLit", type=myDsl_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Type3", type=myDsl_TypeLit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="myDsl_Type6", type=myDsl_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Type4", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_SourceFile", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_SourceFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mapType17: BinaryAssociation = BinaryAssociation(
    name="mapType17",
    ends={
        Property(name="myDsl_MapType", type=myDsl_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeLit18", type=myDsl_MapType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
channelType19: BinaryAssociation = BinaryAssociation(
    name="channelType19",
    ends={
        Property(name="myDsl_ChannelType", type=myDsl_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeLit20", type=myDsl_ChannelType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayLength21: BinaryAssociation = BinaryAssociation(
    name="arrayLength21",
    ends={
        Property(name="myDsl_ArrayLength", type=myDsl_TypeLitLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeLitLinha22", type=myDsl_ArrayLength, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType23: BinaryAssociation = BinaryAssociation(
    name="elementType23",
    ends={
        Property(name="myDsl_ElementType", type=myDsl_TypeLitLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeLitLinha24", type=myDsl_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeLitLinha7: BinaryAssociation = BinaryAssociation(
    name="typeLitLinha7",
    ends={
        Property(name="myDsl_TypeLitLinha", type=myDsl_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeLit8", type=myDsl_TypeLitLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
srtuctType9: BinaryAssociation = BinaryAssociation(
    name="srtuctType9",
    ends={
        Property(name="myDsl_StructType", type=myDsl_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeLit10", type=myDsl_StructType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointerType11: BinaryAssociation = BinaryAssociation(
    name="pointerType11",
    ends={
        Property(name="myDsl_PointerType", type=myDsl_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeLit12", type=myDsl_PointerType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionType13: BinaryAssociation = BinaryAssociation(
    name="functionType13",
    ends={
        Property(name="myDsl_FunctionType", type=myDsl_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeLit14", type=myDsl_FunctionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceType15: BinaryAssociation = BinaryAssociation(
    name="interfaceType15",
    ends={
        Property(name="myDsl_InterfaceType", type=myDsl_TypeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeLit16", type=myDsl_InterfaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList32: BinaryAssociation = BinaryAssociation(
    name="identifierList32",
    ends={
        Property(name="myDsl_IdentifierList", type=myDsl_FieldDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FieldDecl33", type=myDsl_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type34: BinaryAssociation = BinaryAssociation(
    name="type34",
    ends={
        Property(name="myDsl_Type36", type=myDsl_FieldDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FieldDecl35", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression25: BinaryAssociation = BinaryAssociation(
    name="expression25",
    ends={
        Property(name="myDsl_Expression", type=myDsl_ArrayLength, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArrayLength26", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="myDsl_Type29", type=myDsl_ElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ElementType28", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldDecl30: BinaryAssociation = BinaryAssociation(
    name="fieldDecl30",
    ends={
        Property(name="myDsl_FieldDecl", type=myDsl_StructType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_StructType31", type=myDsl_FieldDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeName41: BinaryAssociation = BinaryAssociation(
    name="typeName41",
    ends={
        Property(name="myDsl_TypeName43", type=myDsl_EmbeddedField, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_EmbeddedField42", type=myDsl_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embeddedField37: BinaryAssociation = BinaryAssociation(
    name="embeddedField37",
    ends={
        Property(name="myDsl_EmbeddedField", type=myDsl_FieldDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FieldDecl38", type=myDsl_EmbeddedField, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tag39: BinaryAssociation = BinaryAssociation(
    name="tag39",
    ends={
        Property(name="myDsl_Tag", type=myDsl_FieldDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FieldDecl40", type=myDsl_Tag, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature49: BinaryAssociation = BinaryAssociation(
    name="signature49",
    ends={
        Property(name="myDsl_FunctionType50", type=myDsl_Signature, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="myDsl_Signature", type=myDsl_FunctionType, multiplicity=Multiplicity(1, 1))
    }
)
parameters51: BinaryAssociation = BinaryAssociation(
    name="parameters51",
    ends={
        Property(name="myDsl_Parameters", type=myDsl_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Signature52", type=myDsl_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseType44: BinaryAssociation = BinaryAssociation(
    name="baseType44",
    ends={
        Property(name="myDsl_BaseType", type=myDsl_PointerType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PointerType45", type=myDsl_BaseType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="myDsl_Type48", type=myDsl_BaseType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_BaseType47", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterList61: BinaryAssociation = BinaryAssociation(
    name="parameterList61",
    ends={
        Property(name="myDsl_ParameterList", type=myDsl_Parameters, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Parameters62", type=myDsl_ParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterDecl63: BinaryAssociation = BinaryAssociation(
    name="parameterDecl63",
    ends={
        Property(name="myDsl_ParameterDecl", type=myDsl_ParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ParameterList64", type=myDsl_ParameterDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result53: BinaryAssociation = BinaryAssociation(
    name="result53",
    ends={
        Property(name="myDsl_Result", type=myDsl_Signature, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Signature54", type=myDsl_Result, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters55: BinaryAssociation = BinaryAssociation(
    name="parameters55",
    ends={
        Property(name="myDsl_Parameters57", type=myDsl_Result, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Result56", type=myDsl_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type58: BinaryAssociation = BinaryAssociation(
    name="type58",
    ends={
        Property(name="myDsl_Type60", type=myDsl_Result, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Result59", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodSpec74: BinaryAssociation = BinaryAssociation(
    name="methodSpec74",
    ends={
        Property(name="myDsl_MethodSpec", type=myDsl_InterfaceType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_InterfaceType75", type=myDsl_MethodSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterDecl165: BinaryAssociation = BinaryAssociation(
    name="parameterDecl165",
    ends={
        Property(name="myDsl_ParameterDecl67", type=myDsl_ParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ParameterList66", type=myDsl_ParameterDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifierList68: BinaryAssociation = BinaryAssociation(
    name="identifierList68",
    ends={
        Property(name="myDsl_IdentifierList70", type=myDsl_ParameterDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ParameterDecl69", type=myDsl_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type71: BinaryAssociation = BinaryAssociation(
    name="type71",
    ends={
        Property(name="myDsl_Type73", type=myDsl_ParameterDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ParameterDecl72", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName83: BinaryAssociation = BinaryAssociation(
    name="typeName83",
    ends={
        Property(name="myDsl_TypeName85", type=myDsl_InterfaceTypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_InterfaceTypeName84", type=myDsl_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyType86: BinaryAssociation = BinaryAssociation(
    name="keyType86",
    ends={
        Property(name="myDsl_KeyType", type=myDsl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MapType87", type=myDsl_KeyType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodName76: BinaryAssociation = BinaryAssociation(
    name="methodName76",
    ends={
        Property(name="myDsl_MethodName", type=myDsl_MethodSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MethodSpec77", type=myDsl_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Signature78: BinaryAssociation = BinaryAssociation(
    name="Signature78",
    ends={
        Property(name="myDsl_Signature80", type=myDsl_MethodSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MethodSpec79", type=myDsl_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceTypeName81: BinaryAssociation = BinaryAssociation(
    name="interfaceTypeName81",
    ends={
        Property(name="myDsl_InterfaceTypeName", type=myDsl_MethodSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MethodSpec82", type=myDsl_InterfaceTypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
channelTypeLinha94: BinaryAssociation = BinaryAssociation(
    name="channelTypeLinha94",
    ends={
        Property(name="myDsl_ChannelTypeLinha", type=myDsl_ChannelType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ChannelType95", type=myDsl_ChannelTypeLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType96: BinaryAssociation = BinaryAssociation(
    name="elementType96",
    ends={
        Property(name="myDsl_ElementType98", type=myDsl_ChannelType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ChannelType97", type=myDsl_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType88: BinaryAssociation = BinaryAssociation(
    name="elementType88",
    ends={
        Property(name="myDsl_ElementType90", type=myDsl_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MapType89", type=myDsl_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type91: BinaryAssociation = BinaryAssociation(
    name="type91",
    ends={
        Property(name="myDsl_Type93", type=myDsl_KeyType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_KeyType92", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constDecl102: BinaryAssociation = BinaryAssociation(
    name="constDecl102",
    ends={
        Property(name="myDsl_ConstDecl", type=myDsl_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Declaration", type=myDsl_ConstDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDecl103: BinaryAssociation = BinaryAssociation(
    name="typeDecl103",
    ends={
        Property(name="myDsl_TypeDecl", type=myDsl_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Declaration104", type=myDsl_TypeDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementList99: BinaryAssociation = BinaryAssociation(
    name="statementList99",
    ends={
        Property(name="myDsl_StatementList", type=myDsl_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Block", type=myDsl_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements100: BinaryAssociation = BinaryAssociation(
    name="statements100",
    ends={
        Property(name="myDsl_Statement", type=myDsl_StatementList, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_StatementList101", type=myDsl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodDecl111: BinaryAssociation = BinaryAssociation(
    name="methodDecl111",
    ends={
        Property(name="myDsl_MethodDecl", type=myDsl_TopLevelDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TopLevelDecl112", type=myDsl_MethodDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constSpec113: BinaryAssociation = BinaryAssociation(
    name="constSpec113",
    ends={
        Property(name="myDsl_ConstSpec", type=myDsl_ConstDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ConstDecl114", type=myDsl_ConstSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varDecl105: BinaryAssociation = BinaryAssociation(
    name="varDecl105",
    ends={
        Property(name="myDsl_VarDecl", type=myDsl_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Declaration106", type=myDsl_VarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration107: BinaryAssociation = BinaryAssociation(
    name="declaration107",
    ends={
        Property(name="myDsl_Declaration108", type=myDsl_TopLevelDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TopLevelDecl", type=myDsl_Declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionDecl109: BinaryAssociation = BinaryAssociation(
    name="functionDecl109",
    ends={
        Property(name="myDsl_FunctionDecl", type=myDsl_TopLevelDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TopLevelDecl110", type=myDsl_FunctionDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList124: BinaryAssociation = BinaryAssociation(
    name="expressionList124",
    ends={
        Property(name="myDsl_ExpressionList", type=myDsl_ConstSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ConstSpec125", type=myDsl_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constSpec1115: BinaryAssociation = BinaryAssociation(
    name="constSpec1115",
    ends={
        Property(name="myDsl_ConstSpec117", type=myDsl_ConstDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ConstDecl116", type=myDsl_ConstSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifierList118: BinaryAssociation = BinaryAssociation(
    name="identifierList118",
    ends={
        Property(name="myDsl_IdentifierList120", type=myDsl_ConstSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ConstSpec119", type=myDsl_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type121: BinaryAssociation = BinaryAssociation(
    name="type121",
    ends={
        Property(name="myDsl_Type123", type=myDsl_ConstSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ConstSpec122", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeSpec132: BinaryAssociation = BinaryAssociation(
    name="typeSpec132",
    ends={
        Property(name="myDsl_TypeSpec", type=myDsl_TypeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeDecl133", type=myDsl_TypeSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeSpec1134: BinaryAssociation = BinaryAssociation(
    name="typeSpec1134",
    ends={
        Property(name="myDsl_TypeSpec136", type=myDsl_TypeDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeDecl135", type=myDsl_TypeSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="myDsl_Expression128", type=myDsl_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExpressionList127", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1129: BinaryAssociation = BinaryAssociation(
    name="expression1129",
    ends={
        Property(name="myDsl_Expression131", type=myDsl_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExpressionList130", type=myDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type141: BinaryAssociation = BinaryAssociation(
    name="type141",
    ends={
        Property(name="myDsl_Type143", type=myDsl_AliasDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AliasDecl142", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aliasDecl137: BinaryAssociation = BinaryAssociation(
    name="aliasDecl137",
    ends={
        Property(name="myDsl_AliasDecl", type=myDsl_TypeSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeSpec138", type=myDsl_AliasDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDef139: BinaryAssociation = BinaryAssociation(
    name="typeDef139",
    ends={
        Property(name="myDsl_TypeDef", type=myDsl_TypeSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeSpec140", type=myDsl_TypeDef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IdentifierList152: BinaryAssociation = BinaryAssociation(
    name="IdentifierList152",
    ends={
        Property(name="myDsl_IdentifierList154", type=myDsl_VarSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_VarSpec153", type=myDsl_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type155: BinaryAssociation = BinaryAssociation(
    name="type155",
    ends={
        Property(name="myDsl_Type157", type=myDsl_VarSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_VarSpec156", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type144: BinaryAssociation = BinaryAssociation(
    name="type144",
    ends={
        Property(name="myDsl_Type146", type=myDsl_TypeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeDef145", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varSpec147: BinaryAssociation = BinaryAssociation(
    name="varSpec147",
    ends={
        Property(name="myDsl_VarSpec", type=myDsl_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_VarDecl148", type=myDsl_VarSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varSpec1149: BinaryAssociation = BinaryAssociation(
    name="varSpec1149",
    ends={
        Property(name="myDsl_VarSpec151", type=myDsl_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_VarDecl150", type=myDsl_VarSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionName166: BinaryAssociation = BinaryAssociation(
    name="functionName166",
    ends={
        Property(name="myDsl_FunctionName", type=myDsl_FunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FunctionDecl167", type=myDsl_FunctionName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature168: BinaryAssociation = BinaryAssociation(
    name="signature168",
    ends={
        Property(name="myDsl_Signature170", type=myDsl_FunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FunctionDecl169", type=myDsl_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionBody171: BinaryAssociation = BinaryAssociation(
    name="functionBody171",
    ends={
        Property(name="myDsl_FunctionBody", type=myDsl_FunctionDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FunctionDecl172", type=myDsl_FunctionBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList158: BinaryAssociation = BinaryAssociation(
    name="expressionList158",
    ends={
        Property(name="myDsl_ExpressionList160", type=myDsl_VarSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_VarSpec159", type=myDsl_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList161: BinaryAssociation = BinaryAssociation(
    name="identifierList161",
    ends={
        Property(name="myDsl_IdentifierList162", type=myDsl_ShortVarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ShortVarDecl", type=myDsl_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList163: BinaryAssociation = BinaryAssociation(
    name="expressionList163",
    ends={
        Property(name="myDsl_ExpressionList165", type=myDsl_ShortVarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ShortVarDecl164", type=myDsl_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver176: BinaryAssociation = BinaryAssociation(
    name="receiver176",
    ends={
        Property(name="myDsl_MethodDecl177", type=myDsl_Receiver, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="myDsl_Receiver", type=myDsl_MethodDecl, multiplicity=Multiplicity(1, 1))
    }
)
methodName178: BinaryAssociation = BinaryAssociation(
    name="methodName178",
    ends={
        Property(name="myDsl_MethodName180", type=myDsl_MethodDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MethodDecl179", type=myDsl_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature181: BinaryAssociation = BinaryAssociation(
    name="signature181",
    ends={
        Property(name="myDsl_Signature183", type=myDsl_MethodDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MethodDecl182", type=myDsl_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block173: BinaryAssociation = BinaryAssociation(
    name="block173",
    ends={
        Property(name="myDsl_Block175", type=myDsl_FunctionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FunctionBody174", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operandName191: BinaryAssociation = BinaryAssociation(
    name="operandName191",
    ends={
        Property(name="myDsl_OperandName", type=myDsl_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Operand192", type=myDsl_OperandName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression193: BinaryAssociation = BinaryAssociation(
    name="expression193",
    ends={
        Property(name="myDsl_Expression195", type=myDsl_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Operand194", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionBody184: BinaryAssociation = BinaryAssociation(
    name="functionBody184",
    ends={
        Property(name="myDsl_FunctionBody186", type=myDsl_MethodDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MethodDecl185", type=myDsl_FunctionBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters187: BinaryAssociation = BinaryAssociation(
    name="parameters187",
    ends={
        Property(name="myDsl_Parameters189", type=myDsl_Receiver, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Receiver188", type=myDsl_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal190: BinaryAssociation = BinaryAssociation(
    name="literal190",
    ends={
        Property(name="myDsl_Literal", type=myDsl_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Operand", type=myDsl_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicLit196: BinaryAssociation = BinaryAssociation(
    name="basicLit196",
    ends={
        Property(name="myDsl_BasicLit", type=myDsl_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Literal197", type=myDsl_BasicLit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compositeLit198: BinaryAssociation = BinaryAssociation(
    name="compositeLit198",
    ends={
        Property(name="myDsl_CompositeLit", type=myDsl_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Literal199", type=myDsl_CompositeLit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionLit200: BinaryAssociation = BinaryAssociation(
    name="functionLit200",
    ends={
        Property(name="myDsl_FunctionLit", type=myDsl_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Literal201", type=myDsl_FunctionLit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapType209: BinaryAssociation = BinaryAssociation(
    name="mapType209",
    ends={
        Property(name="myDsl_MapType211", type=myDsl_LiteralType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LiteralType210", type=myDsl_MapType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName212: BinaryAssociation = BinaryAssociation(
    name="typeName212",
    ends={
        Property(name="myDsl_TypeName214", type=myDsl_LiteralType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LiteralType213", type=myDsl_TypeName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literalTypeLinha215: BinaryAssociation = BinaryAssociation(
    name="literalTypeLinha215",
    ends={
        Property(name="myDsl_LiteralTypeLinha", type=myDsl_LiteralType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LiteralType216", type=myDsl_LiteralTypeLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literalType202: BinaryAssociation = BinaryAssociation(
    name="literalType202",
    ends={
        Property(name="myDsl_LiteralType", type=myDsl_CompositeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CompositeLit203", type=myDsl_LiteralType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literalValue204: BinaryAssociation = BinaryAssociation(
    name="literalValue204",
    ends={
        Property(name="myDsl_LiteralValue", type=myDsl_CompositeLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CompositeLit205", type=myDsl_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structType206: BinaryAssociation = BinaryAssociation(
    name="structType206",
    ends={
        Property(name="myDsl_StructType208", type=myDsl_LiteralType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LiteralType207", type=myDsl_StructType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementList223: BinaryAssociation = BinaryAssociation(
    name="elementList223",
    ends={
        Property(name="myDsl_LiteralValue224", type=myDsl_ElementList, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="myDsl_ElementList", type=myDsl_LiteralValue, multiplicity=Multiplicity(1, 1))
    }
)
keyedElement225: BinaryAssociation = BinaryAssociation(
    name="keyedElement225",
    ends={
        Property(name="myDsl_KeyedElement", type=myDsl_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ElementList226", type=myDsl_KeyedElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyedElement1227: BinaryAssociation = BinaryAssociation(
    name="keyedElement1227",
    ends={
        Property(name="myDsl_KeyedElement229", type=myDsl_ElementList, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ElementList228", type=myDsl_KeyedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayLength217: BinaryAssociation = BinaryAssociation(
    name="arrayLength217",
    ends={
        Property(name="myDsl_ArrayLength219", type=myDsl_LiteralTypeLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LiteralTypeLinha218", type=myDsl_ArrayLength, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType220: BinaryAssociation = BinaryAssociation(
    name="elementType220",
    ends={
        Property(name="myDsl_ElementType222", type=myDsl_LiteralTypeLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LiteralTypeLinha221", type=myDsl_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldName234: BinaryAssociation = BinaryAssociation(
    name="fieldName234",
    ends={
        Property(name="myDsl_FieldName", type=myDsl_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Key235", type=myDsl_FieldName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression236: BinaryAssociation = BinaryAssociation(
    name="expression236",
    ends={
        Property(name="myDsl_Expression238", type=myDsl_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Key237", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literalValue239: BinaryAssociation = BinaryAssociation(
    name="literalValue239",
    ends={
        Property(name="myDsl_LiteralValue241", type=myDsl_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Key240", type=myDsl_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key230: BinaryAssociation = BinaryAssociation(
    name="key230",
    ends={
        Property(name="myDsl_Key", type=myDsl_KeyedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_KeyedElement231", type=myDsl_Key, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element232: BinaryAssociation = BinaryAssociation(
    name="element232",
    ends={
        Property(name="myDsl_Element", type=myDsl_KeyedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_KeyedElement233", type=myDsl_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExprLinha256: BinaryAssociation = BinaryAssociation(
    name="primaryExprLinha256",
    ends={
        Property(name="myDsl_PrimaryExprLinha", type=myDsl_PrimaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PrimaryExpr257", type=myDsl_PrimaryExprLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conversion258: BinaryAssociation = BinaryAssociation(
    name="conversion258",
    ends={
        Property(name="myDsl_Conversion", type=myDsl_PrimaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PrimaryExpr259", type=myDsl_Conversion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodExpr260: BinaryAssociation = BinaryAssociation(
    name="methodExpr260",
    ends={
        Property(name="myDsl_MethodExpr", type=myDsl_PrimaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PrimaryExpr261", type=myDsl_MethodExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selector262: BinaryAssociation = BinaryAssociation(
    name="selector262",
    ends={
        Property(name="myDsl_Selector", type=myDsl_PrimaryExprLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PrimaryExprLinha263", type=myDsl_Selector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression242: BinaryAssociation = BinaryAssociation(
    name="expression242",
    ends={
        Property(name="myDsl_Expression244", type=myDsl_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Element243", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literalValue245: BinaryAssociation = BinaryAssociation(
    name="literalValue245",
    ends={
        Property(name="myDsl_LiteralValue247", type=myDsl_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Element246", type=myDsl_LiteralValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signature248: BinaryAssociation = BinaryAssociation(
    name="signature248",
    ends={
        Property(name="myDsl_Signature250", type=myDsl_FunctionLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FunctionLit249", type=myDsl_Signature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functionBody251: BinaryAssociation = BinaryAssociation(
    name="functionBody251",
    ends={
        Property(name="myDsl_FunctionBody253", type=myDsl_FunctionLit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_FunctionLit252", type=myDsl_FunctionBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand254: BinaryAssociation = BinaryAssociation(
    name="operand254",
    ends={
        Property(name="myDsl_Operand255", type=myDsl_PrimaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PrimaryExpr", type=myDsl_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression275: BinaryAssociation = BinaryAssociation(
    name="expression275",
    ends={
        Property(name="myDsl_Expression277", type=myDsl_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Index276", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression278: BinaryAssociation = BinaryAssociation(
    name="expression278",
    ends={
        Property(name="myDsl_Expression280", type=myDsl_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Slice279", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1281: BinaryAssociation = BinaryAssociation(
    name="expression1281",
    ends={
        Property(name="myDsl_Expression283", type=myDsl_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Slice282", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2284: BinaryAssociation = BinaryAssociation(
    name="expression2284",
    ends={
        Property(name="myDsl_Expression286", type=myDsl_Slice, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Slice285", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExprLinha265: BinaryAssociation = BinaryAssociation(
    name="primaryExprLinha265",
    ends={
        Property(name="myDsl_PrimaryExprLinha266", type=myDsl_PrimaryExprLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PrimaryExprLinha264", type=myDsl_PrimaryExprLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index267: BinaryAssociation = BinaryAssociation(
    name="index267",
    ends={
        Property(name="myDsl_Index", type=myDsl_PrimaryExprLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PrimaryExprLinha268", type=myDsl_Index, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
slice269: BinaryAssociation = BinaryAssociation(
    name="slice269",
    ends={
        Property(name="myDsl_Slice", type=myDsl_PrimaryExprLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PrimaryExprLinha270", type=myDsl_Slice, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeAssertion271: BinaryAssociation = BinaryAssociation(
    name="typeAssertion271",
    ends={
        Property(name="myDsl_TypeAssertion", type=myDsl_PrimaryExprLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PrimaryExprLinha272", type=myDsl_TypeAssertion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments273: BinaryAssociation = BinaryAssociation(
    name="arguments273",
    ends={
        Property(name="myDsl_Arguments", type=myDsl_PrimaryExprLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PrimaryExprLinha274", type=myDsl_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type301: BinaryAssociation = BinaryAssociation(
    name="type301",
    ends={
        Property(name="myDsl_Type303", type=myDsl_ReceiverType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReceiverType302", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpr304: BinaryAssociation = BinaryAssociation(
    name="unaryExpr304",
    ends={
        Property(name="myDsl_UnaryExpr", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression305", type=myDsl_UnaryExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_Linha306: BinaryAssociation = BinaryAssociation(
    name="expression_Linha306",
    ends={
        Property(name="myDsl_Expression_Linha", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression307", type=myDsl_Expression_Linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpr308: BinaryAssociation = BinaryAssociation(
    name="unaryExpr308",
    ends={
        Property(name="myDsl_UnaryExpr309", type=myDsl_Expression1, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression1", type=myDsl_UnaryExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type287: BinaryAssociation = BinaryAssociation(
    name="type287",
    ends={
        Property(name="myDsl_Type289", type=myDsl_TypeAssertion, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeAssertion288", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList290: BinaryAssociation = BinaryAssociation(
    name="expressionList290",
    ends={
        Property(name="myDsl_ExpressionList292", type=myDsl_Arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Arguments291", type=myDsl_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type293: BinaryAssociation = BinaryAssociation(
    name="type293",
    ends={
        Property(name="myDsl_Type295", type=myDsl_Arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Arguments294", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiverType296: BinaryAssociation = BinaryAssociation(
    name="receiverType296",
    ends={
        Property(name="myDsl_ReceiverType", type=myDsl_MethodExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MethodExpr297", type=myDsl_ReceiverType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodName298: BinaryAssociation = BinaryAssociation(
    name="methodName298",
    ends={
        Property(name="myDsl_MethodName300", type=myDsl_MethodExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MethodExpr299", type=myDsl_MethodName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type324: BinaryAssociation = BinaryAssociation(
    name="type324",
    ends={
        Property(name="myDsl_Type326", type=myDsl_Conversion, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Conversion325", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression327: BinaryAssociation = BinaryAssociation(
    name="expression327",
    ends={
        Property(name="myDsl_Expression329", type=myDsl_Conversion, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Conversion328", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration330: BinaryAssociation = BinaryAssociation(
    name="declaration330",
    ends={
        Property(name="myDsl_Declaration332", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement331", type=myDsl_Declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_Linha310: BinaryAssociation = BinaryAssociation(
    name="expression_Linha310",
    ends={
        Property(name="myDsl_Expression_Linha312", type=myDsl_Expression1, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression1311", type=myDsl_Expression_Linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BINARY_OP313: BinaryAssociation = BinaryAssociation(
    name="BINARY_OP313",
    ends={
        Property(name="myDsl_BINARY_OP", type=myDsl_Expression_Linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_Linha314", type=myDsl_BINARY_OP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1315: BinaryAssociation = BinaryAssociation(
    name="expression1315",
    ends={
        Property(name="myDsl_Expression1317", type=myDsl_Expression_Linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_Linha316", type=myDsl_Expression1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression_Linha319: BinaryAssociation = BinaryAssociation(
    name="expression_Linha319",
    ends={
        Property(name="myDsl_Expression_Linha320", type=myDsl_Expression_Linha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_Linha318", type=myDsl_Expression_Linha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExpr321: BinaryAssociation = BinaryAssociation(
    name="primaryExpr321",
    ends={
        Property(name="myDsl_PrimaryExpr323", type=myDsl_UnaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_UnaryExpr322", type=myDsl_PrimaryExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
gotoStmt345: BinaryAssociation = BinaryAssociation(
    name="gotoStmt345",
    ends={
        Property(name="myDsl_GotoStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement346", type=myDsl_GotoStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fallthroughStmt347: BinaryAssociation = BinaryAssociation(
    name="fallthroughStmt347",
    ends={
        Property(name="myDsl_FallthroughStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement348", type=myDsl_FallthroughStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block349: BinaryAssociation = BinaryAssociation(
    name="block349",
    ends={
        Property(name="myDsl_Block351", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement350", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStmt352: BinaryAssociation = BinaryAssociation(
    name="ifStmt352",
    ends={
        Property(name="myDsl_IfStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement353", type=myDsl_IfStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labeledStmt333: BinaryAssociation = BinaryAssociation(
    name="labeledStmt333",
    ends={
        Property(name="myDsl_LabeledStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement334", type=myDsl_LabeledStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleStmt335: BinaryAssociation = BinaryAssociation(
    name="simpleStmt335",
    ends={
        Property(name="myDsl_SimpleStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement336", type=myDsl_SimpleStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
goStmt337: BinaryAssociation = BinaryAssociation(
    name="goStmt337",
    ends={
        Property(name="myDsl_GoStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement338", type=myDsl_GoStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnStmt339: BinaryAssociation = BinaryAssociation(
    name="returnStmt339",
    ends={
        Property(name="myDsl_ReturnStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement340", type=myDsl_ReturnStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
breakStmt341: BinaryAssociation = BinaryAssociation(
    name="breakStmt341",
    ends={
        Property(name="myDsl_BreakStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement342", type=myDsl_BreakStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
continueStmt343: BinaryAssociation = BinaryAssociation(
    name="continueStmt343",
    ends={
        Property(name="myDsl_ContinueStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement344", type=myDsl_ContinueStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression364: BinaryAssociation = BinaryAssociation(
    name="expression364",
    ends={
        Property(name="myDsl_Expression366", type=myDsl_SimpleStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SimpleStmt365", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleStmtLinha367: BinaryAssociation = BinaryAssociation(
    name="simpleStmtLinha367",
    ends={
        Property(name="myDsl_SimpleStmtLinha", type=myDsl_SimpleStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SimpleStmt368", type=myDsl_SimpleStmtLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shortVarDecl369: BinaryAssociation = BinaryAssociation(
    name="shortVarDecl369",
    ends={
        Property(name="myDsl_ShortVarDecl371", type=myDsl_SimpleStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SimpleStmt370", type=myDsl_ShortVarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression372: BinaryAssociation = BinaryAssociation(
    name="expression372",
    ends={
        Property(name="myDsl_Expression374", type=myDsl_SimpleStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SimpleStmtLinha373", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1375: BinaryAssociation = BinaryAssociation(
    name="expression1375",
    ends={
        Property(name="myDsl_Expression377", type=myDsl_SimpleStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SimpleStmtLinha376", type=myDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
switchStmt354: BinaryAssociation = BinaryAssociation(
    name="switchStmt354",
    ends={
        Property(name="myDsl_SwitchStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement355", type=myDsl_SwitchStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectStmt356: BinaryAssociation = BinaryAssociation(
    name="selectStmt356",
    ends={
        Property(name="myDsl_SelectStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement357", type=myDsl_SelectStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forStmt358: BinaryAssociation = BinaryAssociation(
    name="forStmt358",
    ends={
        Property(name="myDsl_ForStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement359", type=myDsl_ForStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deferStmt360: BinaryAssociation = BinaryAssociation(
    name="deferStmt360",
    ends={
        Property(name="myDsl_DeferStmt", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement361", type=myDsl_DeferStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emptyStmt362: BinaryAssociation = BinaryAssociation(
    name="emptyStmt362",
    ends={
        Property(name="myDsl_EmptyStmt", type=myDsl_SimpleStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SimpleStmt363", type=myDsl_EmptyStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression388: BinaryAssociation = BinaryAssociation(
    name="expression388",
    ends={
        Property(name="myDsl_Expression390", type=myDsl_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmt389", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStmtLinha391: BinaryAssociation = BinaryAssociation(
    name="ifStmtLinha391",
    ends={
        Property(name="myDsl_IfStmtLinha", type=myDsl_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmt392", type=myDsl_IfStmtLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assign_op378: BinaryAssociation = BinaryAssociation(
    name="assign_op378",
    ends={
        Property(name="myDsl_assign_op", type=myDsl_SimpleStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SimpleStmtLinha379", type=myDsl_assign_op, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList380: BinaryAssociation = BinaryAssociation(
    name="expressionList380",
    ends={
        Property(name="myDsl_ExpressionList382", type=myDsl_SimpleStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SimpleStmtLinha381", type=myDsl_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label383: BinaryAssociation = BinaryAssociation(
    name="label383",
    ends={
        Property(name="myDsl_Label", type=myDsl_LabeledStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LabeledStmt384", type=myDsl_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement385: BinaryAssociation = BinaryAssociation(
    name="statement385",
    ends={
        Property(name="myDsl_Statement387", type=myDsl_LabeledStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LabeledStmt386", type=myDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStmt403: BinaryAssociation = BinaryAssociation(
    name="ifStmt403",
    ends={
        Property(name="myDsl_IfStmt404", type=myDsl_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmt402", type=myDsl_IfStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block1405: BinaryAssociation = BinaryAssociation(
    name="block1405",
    ends={
        Property(name="myDsl_Block407", type=myDsl_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmt406", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleStmtLinha408: BinaryAssociation = BinaryAssociation(
    name="simpleStmtLinha408",
    ends={
        Property(name="myDsl_SimpleStmtLinha410", type=myDsl_IfStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmtLinha409", type=myDsl_SimpleStmtLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression411: BinaryAssociation = BinaryAssociation(
    name="expression411",
    ends={
        Property(name="myDsl_Expression413", type=myDsl_IfStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmtLinha412", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emptyStmt393: BinaryAssociation = BinaryAssociation(
    name="emptyStmt393",
    ends={
        Property(name="myDsl_EmptyStmt395", type=myDsl_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmt394", type=myDsl_EmptyStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shortVarDecl396: BinaryAssociation = BinaryAssociation(
    name="shortVarDecl396",
    ends={
        Property(name="myDsl_ShortVarDecl398", type=myDsl_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmt397", type=myDsl_ShortVarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block399: BinaryAssociation = BinaryAssociation(
    name="block399",
    ends={
        Property(name="myDsl_Block401", type=myDsl_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmt400", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleStmt427: BinaryAssociation = BinaryAssociation(
    name="simpleStmt427",
    ends={
        Property(name="myDsl_SimpleStmt429", type=myDsl_ExprSwitchStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSwitchStmt428", type=myDsl_SimpleStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression430: BinaryAssociation = BinaryAssociation(
    name="expression430",
    ends={
        Property(name="myDsl_Expression432", type=myDsl_ExprSwitchStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSwitchStmt431", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprCaseClause433: BinaryAssociation = BinaryAssociation(
    name="exprCaseClause433",
    ends={
        Property(name="myDsl_ExprCaseClause", type=myDsl_ExprSwitchStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSwitchStmt434", type=myDsl_ExprCaseClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exprSwitchCase435: BinaryAssociation = BinaryAssociation(
    name="exprSwitchCase435",
    ends={
        Property(name="myDsl_ExprSwitchCase", type=myDsl_ExprCaseClause, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprCaseClause436", type=myDsl_ExprSwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementList437: BinaryAssociation = BinaryAssociation(
    name="statementList437",
    ends={
        Property(name="myDsl_StatementList439", type=myDsl_ExprCaseClause, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprCaseClause438", type=myDsl_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block414: BinaryAssociation = BinaryAssociation(
    name="block414",
    ends={
        Property(name="myDsl_Block416", type=myDsl_IfStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmtLinha415", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStmt417: BinaryAssociation = BinaryAssociation(
    name="ifStmt417",
    ends={
        Property(name="myDsl_IfStmt419", type=myDsl_IfStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmtLinha418", type=myDsl_IfStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block1420: BinaryAssociation = BinaryAssociation(
    name="block1420",
    ends={
        Property(name="myDsl_Block422", type=myDsl_IfStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_IfStmtLinha421", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprSwitchStmt423: BinaryAssociation = BinaryAssociation(
    name="exprSwitchStmt423",
    ends={
        Property(name="myDsl_ExprSwitchStmt", type=myDsl_SwitchStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SwitchStmt424", type=myDsl_ExprSwitchStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeSwitchStmt425: BinaryAssociation = BinaryAssociation(
    name="typeSwitchStmt425",
    ends={
        Property(name="myDsl_TypeSwitchStmt", type=myDsl_SwitchStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SwitchStmt426", type=myDsl_TypeSwitchStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExpr450: BinaryAssociation = BinaryAssociation(
    name="primaryExpr450",
    ends={
        Property(name="myDsl_PrimaryExpr452", type=myDsl_TypeSwitchGuard, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeSwitchGuard451", type=myDsl_PrimaryExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeSwitchCase453: BinaryAssociation = BinaryAssociation(
    name="typeSwitchCase453",
    ends={
        Property(name="myDsl_TypeSwitchCase", type=myDsl_TypeCaseClause, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeCaseClause454", type=myDsl_TypeSwitchCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementList455: BinaryAssociation = BinaryAssociation(
    name="statementList455",
    ends={
        Property(name="myDsl_StatementList457", type=myDsl_TypeCaseClause, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeCaseClause456", type=myDsl_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList440: BinaryAssociation = BinaryAssociation(
    name="expressionList440",
    ends={
        Property(name="myDsl_ExpressionList442", type=myDsl_ExprSwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ExprSwitchCase441", type=myDsl_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleStmt443: BinaryAssociation = BinaryAssociation(
    name="simpleStmt443",
    ends={
        Property(name="myDsl_SimpleStmt445", type=myDsl_TypeSwitchStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeSwitchStmt444", type=myDsl_SimpleStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeSwitchGuard446: BinaryAssociation = BinaryAssociation(
    name="typeSwitchGuard446",
    ends={
        Property(name="myDsl_TypeSwitchGuard", type=myDsl_TypeSwitchStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeSwitchStmt447", type=myDsl_TypeSwitchGuard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeCaseClause448: BinaryAssociation = BinaryAssociation(
    name="typeCaseClause448",
    ends={
        Property(name="myDsl_TypeCaseClause", type=myDsl_TypeSwitchStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeSwitchStmt449", type=myDsl_TypeCaseClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forStmtLinha469: BinaryAssociation = BinaryAssociation(
    name="forStmtLinha469",
    ends={
        Property(name="myDsl_ForStmtLinha", type=myDsl_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmt470", type=myDsl_ForStmtLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
emptyStmt471: BinaryAssociation = BinaryAssociation(
    name="emptyStmt471",
    ends={
        Property(name="myDsl_EmptyStmt473", type=myDsl_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmt472", type=myDsl_EmptyStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
shortVarDecl474: BinaryAssociation = BinaryAssociation(
    name="shortVarDecl474",
    ends={
        Property(name="myDsl_ShortVarDecl476", type=myDsl_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmt475", type=myDsl_ShortVarDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition477: BinaryAssociation = BinaryAssociation(
    name="condition477",
    ends={
        Property(name="myDsl_Condition", type=myDsl_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmt478", type=myDsl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postStmt479: BinaryAssociation = BinaryAssociation(
    name="postStmt479",
    ends={
        Property(name="myDsl_PostStmt", type=myDsl_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmt480", type=myDsl_PostStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifierList481: BinaryAssociation = BinaryAssociation(
    name="identifierList481",
    ends={
        Property(name="myDsl_IdentifierList483", type=myDsl_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmt482", type=myDsl_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeList458: BinaryAssociation = BinaryAssociation(
    name="typeList458",
    ends={
        Property(name="myDsl_TypeList", type=myDsl_TypeSwitchCase, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeSwitchCase459", type=myDsl_TypeList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type460: BinaryAssociation = BinaryAssociation(
    name="type460",
    ends={
        Property(name="myDsl_Type462", type=myDsl_TypeList, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeList461", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type1463: BinaryAssociation = BinaryAssociation(
    name="type1463",
    ends={
        Property(name="myDsl_Type465", type=myDsl_TypeList, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_TypeList464", type=myDsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression466: BinaryAssociation = BinaryAssociation(
    name="expression466",
    ends={
        Property(name="myDsl_Expression468", type=myDsl_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmt467", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postStmt498: BinaryAssociation = BinaryAssociation(
    name="postStmt498",
    ends={
        Property(name="myDsl_PostStmt500", type=myDsl_ForStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmtLinha499", type=myDsl_PostStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assign_op501: BinaryAssociation = BinaryAssociation(
    name="assign_op501",
    ends={
        Property(name="myDsl_assign_op503", type=myDsl_ForStmtLinhaLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmtLinhaLinha502", type=myDsl_assign_op, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList504: BinaryAssociation = BinaryAssociation(
    name="expressionList504",
    ends={
        Property(name="myDsl_ExpressionList506", type=myDsl_ForStmtLinhaLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmtLinhaLinha505", type=myDsl_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition507: BinaryAssociation = BinaryAssociation(
    name="condition507",
    ends={
        Property(name="myDsl_Condition509", type=myDsl_ForStmtLinhaLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmtLinhaLinha508", type=myDsl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postStmt510: BinaryAssociation = BinaryAssociation(
    name="postStmt510",
    ends={
        Property(name="myDsl_PostStmt512", type=myDsl_ForStmtLinhaLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmtLinhaLinha511", type=myDsl_PostStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block484: BinaryAssociation = BinaryAssociation(
    name="block484",
    ends={
        Property(name="myDsl_Block486", type=myDsl_ForStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmt485", type=myDsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression487: BinaryAssociation = BinaryAssociation(
    name="expression487",
    ends={
        Property(name="myDsl_Expression489", type=myDsl_ForStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmtLinha488", type=myDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forStmtLinhaLinha490: BinaryAssociation = BinaryAssociation(
    name="forStmtLinhaLinha490",
    ends={
        Property(name="myDsl_ForStmtLinhaLinha", type=myDsl_ForStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmtLinha491", type=myDsl_ForStmtLinhaLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1492: BinaryAssociation = BinaryAssociation(
    name="expression1492",
    ends={
        Property(name="myDsl_Expression494", type=myDsl_ForStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmtLinha493", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition495: BinaryAssociation = BinaryAssociation(
    name="condition495",
    ends={
        Property(name="myDsl_Condition497", type=myDsl_ForStmtLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmtLinha496", type=myDsl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commClause525: BinaryAssociation = BinaryAssociation(
    name="commClause525",
    ends={
        Property(name="myDsl_CommClause", type=myDsl_SelectStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SelectStmt526", type=myDsl_CommClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commCase527: BinaryAssociation = BinaryAssociation(
    name="commCase527",
    ends={
        Property(name="myDsl_CommCase", type=myDsl_CommClause, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CommClause528", type=myDsl_CommCase, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementList529: BinaryAssociation = BinaryAssociation(
    name="statementList529",
    ends={
        Property(name="myDsl_StatementList531", type=myDsl_CommClause, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CommClause530", type=myDsl_StatementList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression532: BinaryAssociation = BinaryAssociation(
    name="expression532",
    ends={
        Property(name="myDsl_Expression534", type=myDsl_CommCase, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CommCase533", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression513: BinaryAssociation = BinaryAssociation(
    name="expression513",
    ends={
        Property(name="myDsl_Expression515", type=myDsl_ForStmtLinhaLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ForStmtLinhaLinha514", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression516: BinaryAssociation = BinaryAssociation(
    name="expression516",
    ends={
        Property(name="myDsl_Expression518", type=myDsl_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Condition517", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simpleStmt519: BinaryAssociation = BinaryAssociation(
    name="simpleStmt519",
    ends={
        Property(name="myDsl_SimpleStmt521", type=myDsl_PostStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PostStmt520", type=myDsl_SimpleStmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression522: BinaryAssociation = BinaryAssociation(
    name="expression522",
    ends={
        Property(name="myDsl_Expression524", type=myDsl_GoStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GoStmt523", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionList551: BinaryAssociation = BinaryAssociation(
    name="expressionList551",
    ends={
        Property(name="myDsl_ExpressionList553", type=myDsl_ReturnStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReturnStmt552", type=myDsl_ExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commCaseLinha535: BinaryAssociation = BinaryAssociation(
    name="commCaseLinha535",
    ends={
        Property(name="myDsl_CommCaseLinha", type=myDsl_CommCase, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CommCase536", type=myDsl_CommCaseLinha, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression537: BinaryAssociation = BinaryAssociation(
    name="expression537",
    ends={
        Property(name="myDsl_Expression539", type=myDsl_CommCaseLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CommCaseLinha538", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression1540: BinaryAssociation = BinaryAssociation(
    name="expression1540",
    ends={
        Property(name="myDsl_Expression542", type=myDsl_CommCaseLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CommCaseLinha541", type=myDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifierList543: BinaryAssociation = BinaryAssociation(
    name="identifierList543",
    ends={
        Property(name="myDsl_IdentifierList545", type=myDsl_CommCaseLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CommCaseLinha544", type=myDsl_IdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recvExpr546: BinaryAssociation = BinaryAssociation(
    name="recvExpr546",
    ends={
        Property(name="myDsl_RecvExpr", type=myDsl_CommCaseLinha, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_CommCaseLinha547", type=myDsl_RecvExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression548: BinaryAssociation = BinaryAssociation(
    name="expression548",
    ends={
        Property(name="myDsl_Expression550", type=myDsl_RecvExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RecvExpr549", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
packageClause566: BinaryAssociation = BinaryAssociation(
    name="packageClause566",
    ends={
        Property(name="myDsl_PackageClause", type=myDsl_SourceFile, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SourceFile567", type=myDsl_PackageClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importDecl568: BinaryAssociation = BinaryAssociation(
    name="importDecl568",
    ends={
        Property(name="myDsl_ImportDecl", type=myDsl_SourceFile, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SourceFile569", type=myDsl_ImportDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
topLevelDecl570: BinaryAssociation = BinaryAssociation(
    name="topLevelDecl570",
    ends={
        Property(name="myDsl_TopLevelDecl572", type=myDsl_SourceFile, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SourceFile571", type=myDsl_TopLevelDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageName573: BinaryAssociation = BinaryAssociation(
    name="packageName573",
    ends={
        Property(name="myDsl_PackageName", type=myDsl_PackageClause, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_PackageClause574", type=myDsl_PackageName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label554: BinaryAssociation = BinaryAssociation(
    name="label554",
    ends={
        Property(name="myDsl_Label556", type=myDsl_BreakStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_BreakStmt555", type=myDsl_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label557: BinaryAssociation = BinaryAssociation(
    name="label557",
    ends={
        Property(name="myDsl_Label559", type=myDsl_ContinueStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ContinueStmt558", type=myDsl_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label560: BinaryAssociation = BinaryAssociation(
    name="label560",
    ends={
        Property(name="myDsl_Label562", type=myDsl_GotoStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GotoStmt561", type=myDsl_Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression563: BinaryAssociation = BinaryAssociation(
    name="expression563",
    ends={
        Property(name="myDsl_Expression565", type=myDsl_DeferStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_DeferStmt564", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importSpec575: BinaryAssociation = BinaryAssociation(
    name="importSpec575",
    ends={
        Property(name="myDsl_ImportSpec", type=myDsl_ImportDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ImportDecl576", type=myDsl_ImportSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importSpec1577: BinaryAssociation = BinaryAssociation(
    name="importSpec1577",
    ends={
        Property(name="myDsl_ImportSpec579", type=myDsl_ImportDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ImportDecl578", type=myDsl_ImportSpec, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageName580: BinaryAssociation = BinaryAssociation(
    name="packageName580",
    ends={
        Property(name="myDsl_PackageName582", type=myDsl_ImportSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ImportSpec581", type=myDsl_PackageName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Type, myDsl_TypeName, myDsl_TypeLit, myDsl_Model, myDsl_SourceFile, myDsl_MapType, myDsl_ChannelType, myDsl_ArrayLength, myDsl_ElementType, myDsl_TypeNameLinha, myDsl_TypeLitLinha, myDsl_StructType, myDsl_PointerType, myDsl_FunctionType, myDsl_InterfaceType, myDsl_IdentifierList, myDsl_Expression, myDsl_FieldDecl, myDsl_BaseType, myDsl_EmbeddedField, myDsl_Tag, myDsl_Parameters, myDsl_Result, myDsl_Signature, myDsl_ParameterList, myDsl_ParameterDecl, myDsl_MethodSpec, myDsl_MethodName, myDsl_KeyType, myDsl_InterfaceTypeName, myDsl_ChannelTypeLinha, myDsl_Declaration, myDsl_ConstDecl, myDsl_TypeDecl, myDsl_VarDecl, myDsl_Block, myDsl_StatementList, myDsl_Statement, myDsl_MethodDecl, myDsl_ConstSpec, myDsl_TopLevelDecl, myDsl_FunctionDecl, myDsl_ExpressionList, myDsl_TypeSpec, myDsl_AliasDecl, myDsl_TypeDef, myDsl_VarSpec, myDsl_FunctionName, myDsl_FunctionBody, myDsl_ShortVarDecl, myDsl_Receiver, myDsl_OperandName, myDsl_BasicLit, myDsl_Operand, myDsl_Literal, myDsl_CompositeLit, myDsl_FunctionLit, myDsl_LiteralTypeLinha, myDsl_LiteralType, myDsl_LiteralValue, myDsl_KeyedElement, myDsl_ElementList, myDsl_FieldName, myDsl_Key, myDsl_Element, myDsl_PrimaryExprLinha, myDsl_Conversion, myDsl_MethodExpr, myDsl_Selector, myDsl_PrimaryExpr, myDsl_Index, myDsl_Slice, myDsl_TypeAssertion, myDsl_Arguments, myDsl_UnaryExpr, myDsl_Expression_Linha, myDsl_Expression1, myDsl_ReceiverType, myDsl_LabeledStmt, myDsl_BINARY_OP, myDsl_GotoStmt, myDsl_FallthroughStmt, myDsl_IfStmt, myDsl_SwitchStmt, myDsl_SimpleStmt, myDsl_GoStmt, myDsl_ReturnStmt, myDsl_BreakStmt, myDsl_ContinueStmt, myDsl_SimpleStmtLinha, myDsl_SelectStmt, myDsl_ForStmt, myDsl_DeferStmt, myDsl_EmptyStmt, myDsl_IfStmtLinha, myDsl_assign_op, myDsl_Label, myDsl_ExprCaseClause, myDsl_ExprSwitchCase, myDsl_ExprSwitchStmt, myDsl_TypeSwitchStmt, myDsl_TypeSwitchCase, myDsl_TypeSwitchGuard, myDsl_TypeCaseClause, myDsl_ForStmtLinha, myDsl_Condition, myDsl_PostStmt, myDsl_TypeList, myDsl_ForStmtLinhaLinha, myDsl_CommCase, myDsl_CommCaseLinha, myDsl_CommClause, myDsl_RecvExpr, myDsl_PackageClause, myDsl_ImportDecl, myDsl_PackageName, myDsl_ImportSpec},
    associations={typeName1, typeLit2, type5, greetings0, mapType17, channelType19, arrayLength21, elementType23, typeLitLinha7, srtuctType9, pointerType11, functionType13, interfaceType15, identifierList32, type34, expression25, type27, fieldDecl30, typeName41, embeddedField37, tag39, signature49, parameters51, baseType44, type46, parameterList61, parameterDecl63, result53, parameters55, type58, methodSpec74, parameterDecl165, identifierList68, type71, typeName83, keyType86, methodName76, Signature78, interfaceTypeName81, channelTypeLinha94, elementType96, elementType88, type91, constDecl102, typeDecl103, statementList99, statements100, methodDecl111, constSpec113, varDecl105, declaration107, functionDecl109, expressionList124, constSpec1115, identifierList118, type121, typeSpec132, typeSpec1134, expression126, expression1129, type141, aliasDecl137, typeDef139, IdentifierList152, type155, type144, varSpec147, varSpec1149, functionName166, signature168, functionBody171, expressionList158, identifierList161, expressionList163, receiver176, methodName178, signature181, block173, operandName191, expression193, functionBody184, parameters187, literal190, basicLit196, compositeLit198, functionLit200, mapType209, typeName212, literalTypeLinha215, literalType202, literalValue204, structType206, elementList223, keyedElement225, keyedElement1227, arrayLength217, elementType220, fieldName234, expression236, literalValue239, key230, element232, primaryExprLinha256, conversion258, methodExpr260, selector262, expression242, literalValue245, signature248, functionBody251, operand254, expression275, expression278, expression1281, expression2284, primaryExprLinha265, index267, slice269, typeAssertion271, arguments273, type301, unaryExpr304, expression_Linha306, unaryExpr308, type287, expressionList290, type293, receiverType296, methodName298, type324, expression327, declaration330, expression_Linha310, BINARY_OP313, expression1315, expression_Linha319, primaryExpr321, gotoStmt345, fallthroughStmt347, block349, ifStmt352, labeledStmt333, simpleStmt335, goStmt337, returnStmt339, breakStmt341, continueStmt343, expression364, simpleStmtLinha367, shortVarDecl369, expression372, expression1375, switchStmt354, selectStmt356, forStmt358, deferStmt360, emptyStmt362, expression388, ifStmtLinha391, assign_op378, expressionList380, label383, statement385, ifStmt403, block1405, simpleStmtLinha408, expression411, emptyStmt393, shortVarDecl396, block399, simpleStmt427, expression430, exprCaseClause433, exprSwitchCase435, statementList437, block414, ifStmt417, block1420, exprSwitchStmt423, typeSwitchStmt425, primaryExpr450, typeSwitchCase453, statementList455, expressionList440, simpleStmt443, typeSwitchGuard446, typeCaseClause448, forStmtLinha469, emptyStmt471, shortVarDecl474, condition477, postStmt479, identifierList481, typeList458, type460, type1463, expression466, postStmt498, assign_op501, expressionList504, condition507, postStmt510, block484, expression487, forStmtLinhaLinha490, expression1492, condition495, commClause525, commCase527, statementList529, expression532, expression513, expression516, simpleStmt519, expression522, expressionList551, commCaseLinha535, expression537, expression1540, identifierList543, recvExpr546, expression548, packageClause566, importDecl568, topLevelDecl570, packageName573, label554, label557, label560, expression563, importSpec575, importSpec1577, packageName580},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)