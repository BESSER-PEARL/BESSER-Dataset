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
Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PROTECTED")
    }
)

# Classes
dsl_CompilationUnit = Class(name="dsl::CompilationUnit")
dsl_TypeBodyModifier = Class(name="dsl::TypeBodyModifier")
dsl_PackageDeclaration = Class(name="dsl::PackageDeclaration")
dsl_ImportDeclaration = Class(name="dsl::ImportDeclaration")
dsl_TypeDeclaration = Class(name="dsl::TypeDeclaration")
dsl_Name = Class(name="dsl::Name")
dsl_CommonModifier = Class(name="dsl::CommonModifier")
dsl_TypeParameters = Class(name="dsl::TypeParameters")
dsl_ExtendsList = Class(name="dsl::ExtendsList")
dsl_ImplementsList = Class(name="dsl::ImplementsList")
dsl_ClassOrInterfaceDeclaration = Class(name="dsl::ClassOrInterfaceDeclaration")
dsl_EnumDeclaration = Class(name="dsl::EnumDeclaration")
dsl_AnnotationTypeDeclaration = Class(name="dsl::AnnotationTypeDeclaration")
dsl_ClassOrInterfaceBodyDeclaration = Class(name="dsl::ClassOrInterfaceBodyDeclaration")
dsl_Arguments = Class(name="dsl::Arguments")
dsl_ClassOrInterfaceBody = Class(name="dsl::ClassOrInterfaceBody")
dsl_ClassOrInterfaceType = Class(name="dsl::ClassOrInterfaceType")
dsl_EnumBody = Class(name="dsl::EnumBody")
dsl_EnumConstant = Class(name="dsl::EnumConstant")
dsl_TypeParameter = Class(name="dsl::TypeParameter")
dsl_TypeBound = Class(name="dsl::TypeBound")
dsl_Initializer = Class(name="dsl::Initializer")
dsl_ArrayInitializer = Class(name="dsl::ArrayInitializer")
dsl_Expression = Class(name="dsl::Expression")
dsl_MethodOrCtorDeclaration = Class(name="dsl::MethodOrCtorDeclaration")
dsl_FieldDeclaration = Class(name="dsl::FieldDeclaration")
dsl_Type = Class(name="dsl::Type")
dsl_VariableDeclarator = Class(name="dsl::VariableDeclarator")
dsl_VariableDeclaratorId = Class(name="dsl::VariableDeclaratorId")
dsl_VariableInitializer = Class(name="dsl::VariableInitializer")
dsl_Block = Class(name="dsl::Block")
dsl_FormalParameters = Class(name="dsl::FormalParameters")
dsl_NameList = Class(name="dsl::NameList")
dsl_ExplicitConstructorInvocation = Class(name="dsl::ExplicitConstructorInvocation")
dsl_BlockStatement = Class(name="dsl::BlockStatement")
dsl_ResultType = Class(name="dsl::ResultType")
dsl_MethodDeclarator = Class(name="dsl::MethodDeclarator")
dsl_FormalParameter = Class(name="dsl::FormalParameter")
dsl_PrimaryExpression = Class(name="dsl::PrimaryExpression")
dsl_TypeArgument = Class(name="dsl::TypeArgument")
dsl_ReferenceType = Class(name="dsl::ReferenceType")
dsl_TypeArguments = Class(name="dsl::TypeArguments")
IfStatement = Class(name="IfStatement")
dsl_WildcardBounds = Class(name="dsl::WildcardBounds")
dsl_ConditionalAndExpression = Class(name="dsl::ConditionalAndExpression")
dsl_ConditionalExpression = Class(name="dsl::ConditionalExpression")
dsl_Statement = Class(name="dsl::Statement")
dsl_ConditionalOrExpression = Class(name="dsl::ConditionalOrExpression")
dsl_InstanceOfExpression = Class(name="dsl::InstanceOfExpression")
dsl_RelationalExpression = Class(name="dsl::RelationalExpression")
dsl_InclusiveOrExpression = Class(name="dsl::InclusiveOrExpression")
dsl_ExclusiveOrExpression = Class(name="dsl::ExclusiveOrExpression")
dsl_AndExpression = Class(name="dsl::AndExpression")
dsl_EqualityExpression = Class(name="dsl::EqualityExpression")
dsl_MultiplicativeExpression = Class(name="dsl::MultiplicativeExpression")
dsl_UnaryExpression = Class(name="dsl::UnaryExpression")
dsl_ShiftExpression = Class(name="dsl::ShiftExpression")
dsl_AdditiveExpression = Class(name="dsl::AdditiveExpression")
dsl_PreIncrementExpression = Class(name="dsl::PreIncrementExpression")
dsl_PreDecrementExpression = Class(name="dsl::PreDecrementExpression")
dsl_UnaryExpressionNotPlusMinus = Class(name="dsl::UnaryExpressionNotPlusMinus")
dsl_CastExpression = Class(name="dsl::CastExpression")
dsl_PostfixExpression = Class(name="dsl::PostfixExpression")
dsl_CastLookahead = Class(name="dsl::CastLookahead")
dsl_EObject = Class(name="dsl::EObject")
dsl_Literal = Class(name="dsl::Literal")
dsl_MemberSelector = Class(name="dsl::MemberSelector")
dsl_PrimaryPrefix = Class(name="dsl::PrimaryPrefix")
dsl_AllocationExpression = Class(name="dsl::AllocationExpression")
dsl_BaseLiteral = Class(name="dsl::BaseLiteral")
dsl_PrimarySuffix = Class(name="dsl::PrimarySuffix")
dsl_DecimalNumber = Class(name="dsl::DecimalNumber")
dsl_FloatLiteral = Class(name="dsl::FloatLiteral")
dsl_UnsignedIntLiteral = Class(name="dsl::UnsignedIntLiteral")
dsl_SignedIntLiteral = Class(name="dsl::SignedIntLiteral")
dsl_IntegerLiteral = Class(name="dsl::IntegerLiteral")
dsl_ArgumentList = Class(name="dsl::ArgumentList")
dsl_BooleanLiteral = Class(name="dsl::BooleanLiteral")
dsl_ArrayDimsAndInits = Class(name="dsl::ArrayDimsAndInits")
dsl_StatementExpression = Class(name="dsl::StatementExpression")
dsl_LabeledStatement = Class(name="dsl::LabeledStatement")
dsl_AssertStatement = Class(name="dsl::AssertStatement")
dsl_BreakStatement = Class(name="dsl::BreakStatement")
dsl_ContinueStatement = Class(name="dsl::ContinueStatement")
dsl_SwitchStatement = Class(name="dsl::SwitchStatement")
dsl_IfStatement = Class(name="dsl::IfStatement")
dsl_WhileStatement = Class(name="dsl::WhileStatement")
dsl_DoStatement = Class(name="dsl::DoStatement")
dsl_ForStatement = Class(name="dsl::ForStatement")
dsl_ReturnStatement = Class(name="dsl::ReturnStatement")
dsl_ThrowStatement = Class(name="dsl::ThrowStatement")
dsl_SynchronizedStatement = Class(name="dsl::SynchronizedStatement")
dsl_TryStatement = Class(name="dsl::TryStatement")
dsl_LocalVariableDeclaration = Class(name="dsl::LocalVariableDeclaration")
dsl_SwitchLabel = Class(name="dsl::SwitchLabel")
dsl_ForInit = Class(name="dsl::ForInit")
dsl_ForUpdate = Class(name="dsl::ForUpdate")
dsl_StatementExpressionList = Class(name="dsl::StatementExpressionList")
dsl_Annotation = Class(name="dsl::Annotation")
dsl_MemberValuePairs = Class(name="dsl::MemberValuePairs")
dsl_MemberValue = Class(name="dsl::MemberValue")
dsl_MemberValuePair = Class(name="dsl::MemberValuePair")
DefaultValue = Class(name="DefaultValue")
dsl_MemberValueArrayInitializer = Class(name="dsl::MemberValueArrayInitializer")
dsl_AnnotationTypeBody = Class(name="dsl::AnnotationTypeBody")
dsl_AnnotationTypeMemberDeclaration = Class(name="dsl::AnnotationTypeMemberDeclaration")
dsl_DefaultValue = Class(name="dsl::DefaultValue")

# dsl_CompilationUnit class attributes and methods

# dsl_TypeBodyModifier class attributes and methods
dsl_TypeBodyModifier_native: Property = Property(name="native", type=BooleanType)
dsl_TypeBodyModifier_transient: Property = Property(name="transient", type=BooleanType)
dsl_TypeBodyModifier_volatile: Property = Property(name="volatile", type=BooleanType)
dsl_TypeBodyModifier_strictfp: Property = Property(name="strictfp", type=BooleanType)
dsl_TypeBodyModifier_synchronized: Property = Property(name="synchronized", type=BooleanType)
dsl_TypeBodyModifier.attributes={dsl_TypeBodyModifier_native, dsl_TypeBodyModifier_strictfp, dsl_TypeBodyModifier_transient, dsl_TypeBodyModifier_volatile, dsl_TypeBodyModifier_synchronized}

# dsl_PackageDeclaration class attributes and methods

# dsl_ImportDeclaration class attributes and methods

# dsl_TypeDeclaration class attributes and methods

# dsl_Name class attributes and methods
dsl_Name_ids: Property = Property(name="ids", type=StringType)
dsl_Name.attributes={dsl_Name_ids}

# dsl_CommonModifier class attributes and methods
dsl_CommonModifier_visibility: Property = Property(name="visibility", type=StringType)
dsl_CommonModifier_static: Property = Property(name="static", type=BooleanType)
dsl_CommonModifier_final: Property = Property(name="final", type=BooleanType)
dsl_CommonModifier_abstract: Property = Property(name="abstract", type=BooleanType)
dsl_CommonModifier.attributes={dsl_CommonModifier_final, dsl_CommonModifier_static, dsl_CommonModifier_visibility, dsl_CommonModifier_abstract}

# dsl_TypeParameters class attributes and methods

# dsl_ExtendsList class attributes and methods

# dsl_ImplementsList class attributes and methods

# dsl_ClassOrInterfaceDeclaration class attributes and methods
dsl_ClassOrInterfaceDeclaration_typeCategory: Property = Property(name="typeCategory", type=StringType)
dsl_ClassOrInterfaceDeclaration_id: Property = Property(name="id", type=StringType)
dsl_ClassOrInterfaceDeclaration.attributes={dsl_ClassOrInterfaceDeclaration_typeCategory, dsl_ClassOrInterfaceDeclaration_id}

# dsl_EnumDeclaration class attributes and methods
dsl_EnumDeclaration_id: Property = Property(name="id", type=StringType)
dsl_EnumDeclaration.attributes={dsl_EnumDeclaration_id}

# dsl_AnnotationTypeDeclaration class attributes and methods
dsl_AnnotationTypeDeclaration_id: Property = Property(name="id", type=StringType)
dsl_AnnotationTypeDeclaration.attributes={dsl_AnnotationTypeDeclaration_id}

# dsl_ClassOrInterfaceBodyDeclaration class attributes and methods

# dsl_Arguments class attributes and methods

# dsl_ClassOrInterfaceBody class attributes and methods

# dsl_ClassOrInterfaceType class attributes and methods
dsl_ClassOrInterfaceType_ids: Property = Property(name="ids", type=StringType)
dsl_ClassOrInterfaceType.attributes={dsl_ClassOrInterfaceType_ids}

# dsl_EnumBody class attributes and methods

# dsl_EnumConstant class attributes and methods
dsl_EnumConstant_id: Property = Property(name="id", type=StringType)
dsl_EnumConstant.attributes={dsl_EnumConstant_id}

# dsl_TypeParameter class attributes and methods
dsl_TypeParameter_id: Property = Property(name="id", type=StringType)
dsl_TypeParameter.attributes={dsl_TypeParameter_id}

# dsl_TypeBound class attributes and methods

# dsl_Initializer class attributes and methods
dsl_Initializer_static: Property = Property(name="static", type=BooleanType)
dsl_Initializer.attributes={dsl_Initializer_static}

# dsl_ArrayInitializer class attributes and methods

# dsl_Expression class attributes and methods
dsl_Expression_assignOp: Property = Property(name="assignOp", type=StringType)
dsl_Expression.attributes={dsl_Expression_assignOp}

# dsl_MethodOrCtorDeclaration class attributes and methods
dsl_MethodOrCtorDeclaration_id: Property = Property(name="id", type=StringType)
dsl_MethodOrCtorDeclaration.attributes={dsl_MethodOrCtorDeclaration_id}

# dsl_FieldDeclaration class attributes and methods

# dsl_Type class attributes and methods
dsl_Type_primType: Property = Property(name="primType", type=StringType)
dsl_Type.attributes={dsl_Type_primType}

# dsl_VariableDeclarator class attributes and methods

# dsl_VariableDeclaratorId class attributes and methods
dsl_VariableDeclaratorId_id: Property = Property(name="id", type=StringType)
dsl_VariableDeclaratorId_squareBrackets: Property = Property(name="squareBrackets", type=StringType)
dsl_VariableDeclaratorId.attributes={dsl_VariableDeclaratorId_id, dsl_VariableDeclaratorId_squareBrackets}

# dsl_VariableInitializer class attributes and methods

# dsl_Block class attributes and methods

# dsl_FormalParameters class attributes and methods

# dsl_NameList class attributes and methods

# dsl_ExplicitConstructorInvocation class attributes and methods
dsl_ExplicitConstructorInvocation_parent: Property = Property(name="parent", type=StringType)
dsl_ExplicitConstructorInvocation_self: Property = Property(name="self", type=BooleanType)
dsl_ExplicitConstructorInvocation.attributes={dsl_ExplicitConstructorInvocation_self, dsl_ExplicitConstructorInvocation_parent}

# dsl_BlockStatement class attributes and methods

# dsl_ResultType class attributes and methods

# dsl_MethodDeclarator class attributes and methods
dsl_MethodDeclarator_id: Property = Property(name="id", type=StringType)
dsl_MethodDeclarator_squareBrackets: Property = Property(name="squareBrackets", type=StringType)
dsl_MethodDeclarator.attributes={dsl_MethodDeclarator_id, dsl_MethodDeclarator_squareBrackets}

# dsl_FormalParameter class attributes and methods
dsl_FormalParameter_final: Property = Property(name="final", type=BooleanType)
dsl_FormalParameter.attributes={dsl_FormalParameter_final}

# dsl_PrimaryExpression class attributes and methods

# dsl_TypeArgument class attributes and methods

# dsl_ReferenceType class attributes and methods
dsl_ReferenceType_primType: Property = Property(name="primType", type=StringType)
dsl_ReferenceType_squareBracketsAlpha: Property = Property(name="squareBracketsAlpha", type=StringType)
dsl_ReferenceType_squareBracketsBeta: Property = Property(name="squareBracketsBeta", type=StringType)
dsl_ReferenceType.attributes={dsl_ReferenceType_primType, dsl_ReferenceType_squareBracketsBeta, dsl_ReferenceType_squareBracketsAlpha}

# dsl_TypeArguments class attributes and methods

# IfStatement class attributes and methods

# dsl_WildcardBounds class attributes and methods
dsl_WildcardBounds_ext: Property = Property(name="ext", type=BooleanType)
dsl_WildcardBounds_sup: Property = Property(name="sup", type=BooleanType)
dsl_WildcardBounds.attributes={dsl_WildcardBounds_sup, dsl_WildcardBounds_ext}

# dsl_ConditionalAndExpression class attributes and methods

# dsl_ConditionalExpression class attributes and methods

# dsl_Statement class attributes and methods

# dsl_ConditionalOrExpression class attributes and methods

# dsl_InstanceOfExpression class attributes and methods

# dsl_RelationalExpression class attributes and methods
dsl_RelationalExpression_ops: Property = Property(name="ops", type=StringType)
dsl_RelationalExpression.attributes={dsl_RelationalExpression_ops}

# dsl_InclusiveOrExpression class attributes and methods

# dsl_ExclusiveOrExpression class attributes and methods

# dsl_AndExpression class attributes and methods

# dsl_EqualityExpression class attributes and methods

# dsl_MultiplicativeExpression class attributes and methods
dsl_MultiplicativeExpression_ops: Property = Property(name="ops", type=StringType)
dsl_MultiplicativeExpression.attributes={dsl_MultiplicativeExpression_ops}

# dsl_UnaryExpression class attributes and methods
dsl_UnaryExpression_sign: Property = Property(name="sign", type=StringType)
dsl_UnaryExpression.attributes={dsl_UnaryExpression_sign}

# dsl_ShiftExpression class attributes and methods
dsl_ShiftExpression_ops: Property = Property(name="ops", type=StringType)
dsl_ShiftExpression.attributes={dsl_ShiftExpression_ops}

# dsl_AdditiveExpression class attributes and methods
dsl_AdditiveExpression_ops: Property = Property(name="ops", type=StringType)
dsl_AdditiveExpression.attributes={dsl_AdditiveExpression_ops}

# dsl_PreIncrementExpression class attributes and methods

# dsl_PreDecrementExpression class attributes and methods

# dsl_UnaryExpressionNotPlusMinus class attributes and methods
dsl_UnaryExpressionNotPlusMinus_negOp: Property = Property(name="negOp", type=StringType)
dsl_UnaryExpressionNotPlusMinus.attributes={dsl_UnaryExpressionNotPlusMinus_negOp}

# dsl_CastExpression class attributes and methods

# dsl_PostfixExpression class attributes and methods
dsl_PostfixExpression_op: Property = Property(name="op", type=StringType)
dsl_PostfixExpression.attributes={dsl_PostfixExpression_op}

# dsl_CastLookahead class attributes and methods
dsl_CastLookahead_bitNegOp: Property = Property(name="bitNegOp", type=StringType)
dsl_CastLookahead_negOp: Property = Property(name="negOp", type=StringType)
dsl_CastLookahead_primType: Property = Property(name="primType", type=StringType)
dsl_CastLookahead_openBracket: Property = Property(name="openBracket", type=StringType)
dsl_CastLookahead_id: Property = Property(name="id", type=StringType)
dsl_CastLookahead_thisOp: Property = Property(name="thisOp", type=StringType)
dsl_CastLookahead_superOp: Property = Property(name="superOp", type=StringType)
dsl_CastLookahead_newOp: Property = Property(name="newOp", type=StringType)
dsl_CastLookahead.attributes={dsl_CastLookahead_bitNegOp, dsl_CastLookahead_thisOp, dsl_CastLookahead_openBracket, dsl_CastLookahead_superOp, dsl_CastLookahead_newOp, dsl_CastLookahead_negOp, dsl_CastLookahead_primType, dsl_CastLookahead_id}

# dsl_EObject class attributes and methods

# dsl_Literal class attributes and methods
dsl_Literal_nullLit: Property = Property(name="nullLit", type=StringType)
dsl_Literal_charLit: Property = Property(name="charLit", type=StringType)
dsl_Literal_stringLit: Property = Property(name="stringLit", type=StringType)
dsl_Literal.attributes={dsl_Literal_charLit, dsl_Literal_stringLit, dsl_Literal_nullLit}

# dsl_MemberSelector class attributes and methods
dsl_MemberSelector_id: Property = Property(name="id", type=StringType)
dsl_MemberSelector.attributes={dsl_MemberSelector_id}

# dsl_PrimaryPrefix class attributes and methods
dsl_PrimaryPrefix_thisOp: Property = Property(name="thisOp", type=StringType)
dsl_PrimaryPrefix_superOp: Property = Property(name="superOp", type=StringType)
dsl_PrimaryPrefix_id: Property = Property(name="id", type=StringType)
dsl_PrimaryPrefix.attributes={dsl_PrimaryPrefix_superOp, dsl_PrimaryPrefix_id, dsl_PrimaryPrefix_thisOp}

# dsl_AllocationExpression class attributes and methods
dsl_AllocationExpression_primType: Property = Property(name="primType", type=StringType)
dsl_AllocationExpression.attributes={dsl_AllocationExpression_primType}

# dsl_BaseLiteral class attributes and methods
dsl_BaseLiteral_binDigitsUnderscore: Property = Property(name="binDigitsUnderscore", type=StringType)
dsl_BaseLiteral_decDigitsUnderscore: Property = Property(name="decDigitsUnderscore", type=StringType)
dsl_BaseLiteral_hexDigitsUnderscore: Property = Property(name="hexDigitsUnderscore", type=StringType)
dsl_BaseLiteral.attributes={dsl_BaseLiteral_decDigitsUnderscore, dsl_BaseLiteral_binDigitsUnderscore, dsl_BaseLiteral_hexDigitsUnderscore}

# dsl_PrimarySuffix class attributes and methods
dsl_PrimarySuffix_thisOp: Property = Property(name="thisOp", type=BooleanType)
dsl_PrimarySuffix_id: Property = Property(name="id", type=StringType)
dsl_PrimarySuffix.attributes={dsl_PrimarySuffix_thisOp, dsl_PrimarySuffix_id}

# dsl_DecimalNumber class attributes and methods
dsl_DecimalNumber_decDigitsUnderscore: Property = Property(name="decDigitsUnderscore", type=StringType)
dsl_DecimalNumber_decDigits: Property = Property(name="decDigits", type=IntegerType)
dsl_DecimalNumber.attributes={dsl_DecimalNumber_decDigitsUnderscore, dsl_DecimalNumber_decDigits}

# dsl_FloatLiteral class attributes and methods
dsl_FloatLiteral_digits: Property = Property(name="digits", type=StringType)
dsl_FloatLiteral.attributes={dsl_FloatLiteral_digits}

# dsl_UnsignedIntLiteral class attributes and methods
dsl_UnsignedIntLiteral_sign: Property = Property(name="sign", type=StringType)
dsl_UnsignedIntLiteral.attributes={dsl_UnsignedIntLiteral_sign}

# dsl_SignedIntLiteral class attributes and methods
dsl_SignedIntLiteral_bitWidth: Property = Property(name="bitWidth", type=IntegerType)
dsl_SignedIntLiteral.attributes={dsl_SignedIntLiteral_bitWidth}

# dsl_IntegerLiteral class attributes and methods
dsl_IntegerLiteral_zero: Property = Property(name="zero", type=StringType)
dsl_IntegerLiteral_one: Property = Property(name="one", type=StringType)
dsl_IntegerLiteral.attributes={dsl_IntegerLiteral_zero, dsl_IntegerLiteral_one}

# dsl_ArgumentList class attributes and methods

# dsl_BooleanLiteral class attributes and methods
dsl_BooleanLiteral_truthiness: Property = Property(name="truthiness", type=StringType)
dsl_BooleanLiteral.attributes={dsl_BooleanLiteral_truthiness}

# dsl_ArrayDimsAndInits class attributes and methods
dsl_ArrayDimsAndInits_squareBrackets: Property = Property(name="squareBrackets", type=StringType)
dsl_ArrayDimsAndInits.attributes={dsl_ArrayDimsAndInits_squareBrackets}

# dsl_StatementExpression class attributes and methods
dsl_StatementExpression_plusOp: Property = Property(name="plusOp", type=StringType)
dsl_StatementExpression_minOp: Property = Property(name="minOp", type=StringType)
dsl_StatementExpression_assignOp: Property = Property(name="assignOp", type=StringType)
dsl_StatementExpression.attributes={dsl_StatementExpression_assignOp, dsl_StatementExpression_plusOp, dsl_StatementExpression_minOp}

# dsl_LabeledStatement class attributes and methods
dsl_LabeledStatement_id: Property = Property(name="id", type=StringType)
dsl_LabeledStatement.attributes={dsl_LabeledStatement_id}

# dsl_AssertStatement class attributes and methods

# dsl_BreakStatement class attributes and methods
dsl_BreakStatement_id: Property = Property(name="id", type=StringType)
dsl_BreakStatement.attributes={dsl_BreakStatement_id}

# dsl_ContinueStatement class attributes and methods
dsl_ContinueStatement_id: Property = Property(name="id", type=StringType)
dsl_ContinueStatement.attributes={dsl_ContinueStatement_id}

# dsl_SwitchStatement class attributes and methods

# dsl_IfStatement class attributes and methods

# dsl_WhileStatement class attributes and methods

# dsl_DoStatement class attributes and methods

# dsl_ForStatement class attributes and methods
dsl_ForStatement_id: Property = Property(name="id", type=StringType)
dsl_ForStatement.attributes={dsl_ForStatement_id}

# dsl_ReturnStatement class attributes and methods

# dsl_ThrowStatement class attributes and methods

# dsl_SynchronizedStatement class attributes and methods

# dsl_TryStatement class attributes and methods

# dsl_LocalVariableDeclaration class attributes and methods
dsl_LocalVariableDeclaration_finality: Property = Property(name="finality", type=StringType)
dsl_LocalVariableDeclaration.attributes={dsl_LocalVariableDeclaration_finality}

# dsl_SwitchLabel class attributes and methods
dsl_SwitchLabel_defaultOp: Property = Property(name="defaultOp", type=StringType)
dsl_SwitchLabel.attributes={dsl_SwitchLabel_defaultOp}

# dsl_ForInit class attributes and methods

# dsl_ForUpdate class attributes and methods

# dsl_StatementExpressionList class attributes and methods

# dsl_Annotation class attributes and methods

# dsl_MemberValuePairs class attributes and methods

# dsl_MemberValue class attributes and methods

# dsl_MemberValuePair class attributes and methods
dsl_MemberValuePair_id: Property = Property(name="id", type=StringType)
dsl_MemberValuePair.attributes={dsl_MemberValuePair_id}

# DefaultValue class attributes and methods

# dsl_MemberValueArrayInitializer class attributes and methods

# dsl_AnnotationTypeBody class attributes and methods

# dsl_AnnotationTypeMemberDeclaration class attributes and methods
dsl_AnnotationTypeMemberDeclaration_id: Property = Property(name="id", type=StringType)
dsl_AnnotationTypeMemberDeclaration.attributes={dsl_AnnotationTypeMemberDeclaration_id}

# dsl_DefaultValue class attributes and methods

# Relationships
packageDecl0: BinaryAssociation = BinaryAssociation(
    name="packageDecl0",
    ends={
        Property(name="dsl_PackageDeclaration", type=dsl_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_CompilationUnit", type=dsl_PackageDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importDecls1: BinaryAssociation = BinaryAssociation(
    name="importDecls1",
    ends={
        Property(name="dsl_ImportDeclaration", type=dsl_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_CompilationUnit2", type=dsl_ImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDecls3: BinaryAssociation = BinaryAssociation(
    name="typeDecls3",
    ends={
        Property(name="dsl_TypeDeclaration", type=dsl_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_CompilationUnit4", type=dsl_TypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name5: BinaryAssociation = BinaryAssociation(
    name="name5",
    ends={
        Property(name="dsl_Name", type=dsl_PackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PackageDeclaration6", type=dsl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name7: BinaryAssociation = BinaryAssociation(
    name="name7",
    ends={
        Property(name="dsl_Name9", type=dsl_ImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ImportDeclaration8", type=dsl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParams20: BinaryAssociation = BinaryAssociation(
    name="typeParams20",
    ends={
        Property(name="dsl_TypeParameters", type=dsl_ClassOrInterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceDeclaration21", type=dsl_TypeParameters, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exts22: BinaryAssociation = BinaryAssociation(
    name="exts22",
    ends={
        Property(name="dsl_ExtendsList", type=dsl_ClassOrInterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceDeclaration23", type=dsl_ExtendsList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
impls24: BinaryAssociation = BinaryAssociation(
    name="impls24",
    ends={
        Property(name="dsl_ImplementsList", type=dsl_ClassOrInterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceDeclaration25", type=dsl_ImplementsList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mod10: BinaryAssociation = BinaryAssociation(
    name="mod10",
    ends={
        Property(name="dsl_CommonModifier", type=dsl_TypeBodyModifier, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeBodyModifier", type=dsl_CommonModifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mod11: BinaryAssociation = BinaryAssociation(
    name="mod11",
    ends={
        Property(name="dsl_CommonModifier13", type=dsl_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeDeclaration12", type=dsl_CommonModifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
classInterfDecl14: BinaryAssociation = BinaryAssociation(
    name="classInterfDecl14",
    ends={
        Property(name="dsl_ClassOrInterfaceDeclaration", type=dsl_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeDeclaration15", type=dsl_ClassOrInterfaceDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumDecl16: BinaryAssociation = BinaryAssociation(
    name="enumDecl16",
    ends={
        Property(name="dsl_EnumDeclaration", type=dsl_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeDeclaration17", type=dsl_EnumDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotDecl18: BinaryAssociation = BinaryAssociation(
    name="annotDecl18",
    ends={
        Property(name="dsl_AnnotationTypeDeclaration", type=dsl_TypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeDeclaration19", type=dsl_AnnotationTypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constants41: BinaryAssociation = BinaryAssociation(
    name="constants41",
    ends={
        Property(name="dsl_EnumConstant", type=dsl_EnumBody, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EnumBody42", type=dsl_EnumConstant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodies43: BinaryAssociation = BinaryAssociation(
    name="bodies43",
    ends={
        Property(name="dsl_ClassOrInterfaceBodyDeclaration", type=dsl_EnumBody, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EnumBody44", type=dsl_ClassOrInterfaceBodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body26: BinaryAssociation = BinaryAssociation(
    name="body26",
    ends={
        Property(name="dsl_ClassOrInterfaceBody", type=dsl_ClassOrInterfaceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceDeclaration27", type=dsl_ClassOrInterfaceBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exts28: BinaryAssociation = BinaryAssociation(
    name="exts28",
    ends={
        Property(name="dsl_ClassOrInterfaceType", type=dsl_ExtendsList, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ExtendsList29", type=dsl_ClassOrInterfaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
impls30: BinaryAssociation = BinaryAssociation(
    name="impls30",
    ends={
        Property(name="dsl_ClassOrInterfaceType32", type=dsl_ExtendsList, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ExtendsList31", type=dsl_ClassOrInterfaceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeKind33: BinaryAssociation = BinaryAssociation(
    name="typeKind33",
    ends={
        Property(name="dsl_ClassOrInterfaceType35", type=dsl_ImplementsList, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ImplementsList34", type=dsl_ClassOrInterfaceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
impls36: BinaryAssociation = BinaryAssociation(
    name="impls36",
    ends={
        Property(name="dsl_ImplementsList38", type=dsl_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EnumDeclaration37", type=dsl_ImplementsList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body39: BinaryAssociation = BinaryAssociation(
    name="body39",
    ends={
        Property(name="dsl_EnumBody", type=dsl_EnumDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EnumDeclaration40", type=dsl_EnumBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mods62: BinaryAssociation = BinaryAssociation(
    name="mods62",
    ends={
        Property(name="dsl_TypeBodyModifier64", type=dsl_ClassOrInterfaceBodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceBodyDeclaration63", type=dsl_TypeBodyModifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedClassEnumType65: BinaryAssociation = BinaryAssociation(
    name="nestedClassEnumType65",
    ends={
        Property(name="dsl_ClassOrInterfaceDeclaration67", type=dsl_ClassOrInterfaceBodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceBodyDeclaration66", type=dsl_ClassOrInterfaceDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumDecl68: BinaryAssociation = BinaryAssociation(
    name="enumDecl68",
    ends={
        Property(name="dsl_EnumDeclaration70", type=dsl_ClassOrInterfaceBodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceBodyDeclaration69", type=dsl_EnumDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args45: BinaryAssociation = BinaryAssociation(
    name="args45",
    ends={
        Property(name="dsl_Arguments", type=dsl_EnumConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EnumConstant46", type=dsl_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body47: BinaryAssociation = BinaryAssociation(
    name="body47",
    ends={
        Property(name="dsl_ClassOrInterfaceBody49", type=dsl_EnumConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EnumConstant48", type=dsl_ClassOrInterfaceBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParams50: BinaryAssociation = BinaryAssociation(
    name="typeParams50",
    ends={
        Property(name="dsl_TypeParameter", type=dsl_TypeParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeParameters51", type=dsl_TypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type52: BinaryAssociation = BinaryAssociation(
    name="type52",
    ends={
        Property(name="dsl_TypeBound", type=dsl_TypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeParameter53", type=dsl_TypeBound, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeKind54: BinaryAssociation = BinaryAssociation(
    name="typeKind54",
    ends={
        Property(name="dsl_ClassOrInterfaceType56", type=dsl_TypeBound, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeBound55", type=dsl_ClassOrInterfaceType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body57: BinaryAssociation = BinaryAssociation(
    name="body57",
    ends={
        Property(name="dsl_ClassOrInterfaceBodyDeclaration59", type=dsl_ClassOrInterfaceBody, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceBody58", type=dsl_ClassOrInterfaceBodyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init60: BinaryAssociation = BinaryAssociation(
    name="init60",
    ends={
        Property(name="dsl_Initializer", type=dsl_ClassOrInterfaceBodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceBodyDeclaration61", type=dsl_Initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayInit83: BinaryAssociation = BinaryAssociation(
    name="arrayInit83",
    ends={
        Property(name="dsl_ArrayInitializer", type=dsl_VariableInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_VariableInitializer84", type=dsl_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr85: BinaryAssociation = BinaryAssociation(
    name="expr85",
    ends={
        Property(name="dsl_Expression", type=dsl_VariableInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_VariableInitializer86", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ctorOrMethod71: BinaryAssociation = BinaryAssociation(
    name="ctorOrMethod71",
    ends={
        Property(name="dsl_MethodOrCtorDeclaration", type=dsl_ClassOrInterfaceBodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceBodyDeclaration72", type=dsl_MethodOrCtorDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field73: BinaryAssociation = BinaryAssociation(
    name="field73",
    ends={
        Property(name="dsl_FieldDeclaration", type=dsl_ClassOrInterfaceBodyDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceBodyDeclaration74", type=dsl_FieldDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type75: BinaryAssociation = BinaryAssociation(
    name="type75",
    ends={
        Property(name="dsl_Type", type=dsl_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_FieldDeclaration76", type=dsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varDecl77: BinaryAssociation = BinaryAssociation(
    name="varDecl77",
    ends={
        Property(name="dsl_VariableDeclarator", type=dsl_FieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_FieldDeclaration78", type=dsl_VariableDeclarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varDeclId79: BinaryAssociation = BinaryAssociation(
    name="varDeclId79",
    ends={
        Property(name="dsl_VariableDeclaratorId", type=dsl_VariableDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_VariableDeclarator80", type=dsl_VariableDeclaratorId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varInit81: BinaryAssociation = BinaryAssociation(
    name="varInit81",
    ends={
        Property(name="dsl_VariableInitializer", type=dsl_VariableDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_VariableDeclarator82", type=dsl_VariableInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block105: BinaryAssociation = BinaryAssociation(
    name="block105",
    ends={
        Property(name="dsl_Block", type=dsl_MethodOrCtorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodOrCtorDeclaration106", type=dsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParams107: BinaryAssociation = BinaryAssociation(
    name="formalParams107",
    ends={
        Property(name="dsl_FormalParameters109", type=dsl_MethodDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodDeclarator108", type=dsl_FormalParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varInit87: BinaryAssociation = BinaryAssociation(
    name="varInit87",
    ends={
        Property(name="dsl_VariableInitializer89", type=dsl_ArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ArrayInitializer88", type=dsl_VariableInitializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParams90: BinaryAssociation = BinaryAssociation(
    name="typeParams90",
    ends={
        Property(name="dsl_TypeParameters92", type=dsl_MethodOrCtorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodOrCtorDeclaration91", type=dsl_TypeParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParams93: BinaryAssociation = BinaryAssociation(
    name="formalParams93",
    ends={
        Property(name="dsl_FormalParameters", type=dsl_MethodOrCtorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodOrCtorDeclaration94", type=dsl_FormalParameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throwsList95: BinaryAssociation = BinaryAssociation(
    name="throwsList95",
    ends={
        Property(name="dsl_NameList", type=dsl_MethodOrCtorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodOrCtorDeclaration96", type=dsl_NameList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ctorInvoc97: BinaryAssociation = BinaryAssociation(
    name="ctorInvoc97",
    ends={
        Property(name="dsl_ExplicitConstructorInvocation", type=dsl_MethodOrCtorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodOrCtorDeclaration98", type=dsl_ExplicitConstructorInvocation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements99: BinaryAssociation = BinaryAssociation(
    name="statements99",
    ends={
        Property(name="dsl_BlockStatement", type=dsl_MethodOrCtorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodOrCtorDeclaration100", type=dsl_BlockStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultType101: BinaryAssociation = BinaryAssociation(
    name="resultType101",
    ends={
        Property(name="dsl_ResultType", type=dsl_MethodOrCtorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodOrCtorDeclaration102", type=dsl_ResultType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodDecl103: BinaryAssociation = BinaryAssociation(
    name="methodDecl103",
    ends={
        Property(name="dsl_MethodDeclarator", type=dsl_MethodOrCtorDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodOrCtorDeclaration104", type=dsl_MethodDeclarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block123: BinaryAssociation = BinaryAssociation(
    name="block123",
    ends={
        Property(name="dsl_Block125", type=dsl_Initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Initializer124", type=dsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
params110: BinaryAssociation = BinaryAssociation(
    name="params110",
    ends={
        Property(name="dsl_FormalParameter", type=dsl_FormalParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_FormalParameters111", type=dsl_FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type112: BinaryAssociation = BinaryAssociation(
    name="type112",
    ends={
        Property(name="dsl_Type114", type=dsl_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_FormalParameter113", type=dsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varDeclId115: BinaryAssociation = BinaryAssociation(
    name="varDeclId115",
    ends={
        Property(name="dsl_VariableDeclaratorId117", type=dsl_FormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_FormalParameter116", type=dsl_VariableDeclaratorId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args118: BinaryAssociation = BinaryAssociation(
    name="args118",
    ends={
        Property(name="dsl_Arguments120", type=dsl_ExplicitConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ExplicitConstructorInvocation119", type=dsl_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr121: BinaryAssociation = BinaryAssociation(
    name="expr121",
    ends={
        Property(name="dsl_PrimaryExpression", type=dsl_ExplicitConstructorInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ExplicitConstructorInvocation122", type=dsl_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArgs133: BinaryAssociation = BinaryAssociation(
    name="typeArgs133",
    ends={
        Property(name="dsl_TypeArgument", type=dsl_TypeArguments, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeArguments134", type=dsl_TypeArgument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refType126: BinaryAssociation = BinaryAssociation(
    name="refType126",
    ends={
        Property(name="dsl_ReferenceType", type=dsl_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Type127", type=dsl_ReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeKind128: BinaryAssociation = BinaryAssociation(
    name="typeKind128",
    ends={
        Property(name="dsl_ClassOrInterfaceType130", type=dsl_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ReferenceType129", type=dsl_ClassOrInterfaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
names146: BinaryAssociation = BinaryAssociation(
    name="names146",
    ends={
        Property(name="dsl_Name148", type=dsl_NameList, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_NameList147", type=dsl_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArgs131: BinaryAssociation = BinaryAssociation(
    name="typeArgs131",
    ends={
        Property(name="dsl_TypeArguments", type=dsl_ClassOrInterfaceType, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ClassOrInterfaceType132", type=dsl_TypeArguments, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refType135: BinaryAssociation = BinaryAssociation(
    name="refType135",
    ends={
        Property(name="dsl_ReferenceType137", type=dsl_TypeArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeArgument136", type=dsl_ReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wildCard138: BinaryAssociation = BinaryAssociation(
    name="wildCard138",
    ends={
        Property(name="dsl_WildcardBounds", type=dsl_TypeArgument, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TypeArgument139", type=dsl_WildcardBounds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refType140: BinaryAssociation = BinaryAssociation(
    name="refType140",
    ends={
        Property(name="dsl_ReferenceType142", type=dsl_WildcardBounds, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_WildcardBounds141", type=dsl_ReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type143: BinaryAssociation = BinaryAssociation(
    name="type143",
    ends={
        Property(name="dsl_Type145", type=dsl_ResultType, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ResultType144", type=dsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprAlpha161: BinaryAssociation = BinaryAssociation(
    name="exprAlpha161",
    ends={
        Property(name="dsl_Expression163", type=dsl_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ConditionalExpression162", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprBeta164: BinaryAssociation = BinaryAssociation(
    name="exprBeta164",
    ends={
        Property(name="dsl_Expression166", type=dsl_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ConditionalExpression165", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condExpr149: BinaryAssociation = BinaryAssociation(
    name="condExpr149",
    ends={
        Property(name="dsl_ConditionalExpression", type=dsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Expression150", type=dsl_ConditionalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr152: BinaryAssociation = BinaryAssociation(
    name="expr152",
    ends={
        Property(name="dsl_Expression153", type=dsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Expression151", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifSt154: BinaryAssociation = BinaryAssociation(
    name="ifSt154",
    ends={
        Property(name="dsl_Statement", type=dsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Expression155", type=dsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseSt156: BinaryAssociation = BinaryAssociation(
    name="elseSt156",
    ends={
        Property(name="dsl_Statement158", type=dsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Expression157", type=dsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr159: BinaryAssociation = BinaryAssociation(
    name="expr159",
    ends={
        Property(name="dsl_ConditionalOrExpression", type=dsl_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ConditionalExpression160", type=dsl_ConditionalOrExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr177: BinaryAssociation = BinaryAssociation(
    name="expr177",
    ends={
        Property(name="dsl_InstanceOfExpression", type=dsl_EqualityExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_EqualityExpression178", type=dsl_InstanceOfExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr167: BinaryAssociation = BinaryAssociation(
    name="expr167",
    ends={
        Property(name="dsl_ConditionalAndExpression", type=dsl_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ConditionalOrExpression168", type=dsl_ConditionalAndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr169: BinaryAssociation = BinaryAssociation(
    name="expr169",
    ends={
        Property(name="dsl_InclusiveOrExpression", type=dsl_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ConditionalAndExpression170", type=dsl_InclusiveOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr171: BinaryAssociation = BinaryAssociation(
    name="expr171",
    ends={
        Property(name="dsl_ExclusiveOrExpression", type=dsl_InclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_InclusiveOrExpression172", type=dsl_ExclusiveOrExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr173: BinaryAssociation = BinaryAssociation(
    name="expr173",
    ends={
        Property(name="dsl_AndExpression", type=dsl_ExclusiveOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ExclusiveOrExpression174", type=dsl_AndExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr175: BinaryAssociation = BinaryAssociation(
    name="expr175",
    ends={
        Property(name="dsl_EqualityExpression", type=dsl_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AndExpression176", type=dsl_EqualityExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr188: BinaryAssociation = BinaryAssociation(
    name="expr188",
    ends={
        Property(name="dsl_MultiplicativeExpression", type=dsl_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AdditiveExpression189", type=dsl_MultiplicativeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr179: BinaryAssociation = BinaryAssociation(
    name="expr179",
    ends={
        Property(name="dsl_RelationalExpression", type=dsl_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_InstanceOfExpression180", type=dsl_RelationalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type181: BinaryAssociation = BinaryAssociation(
    name="type181",
    ends={
        Property(name="dsl_Type183", type=dsl_InstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_InstanceOfExpression182", type=dsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr184: BinaryAssociation = BinaryAssociation(
    name="expr184",
    ends={
        Property(name="dsl_ShiftExpression", type=dsl_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_RelationalExpression185", type=dsl_ShiftExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr186: BinaryAssociation = BinaryAssociation(
    name="expr186",
    ends={
        Property(name="dsl_AdditiveExpression", type=dsl_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ShiftExpression187", type=dsl_AdditiveExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr201: BinaryAssociation = BinaryAssociation(
    name="expr201",
    ends={
        Property(name="dsl_PrimaryExpression203", type=dsl_PreIncrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PreIncrementExpression202", type=dsl_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr190: BinaryAssociation = BinaryAssociation(
    name="expr190",
    ends={
        Property(name="dsl_UnaryExpression", type=dsl_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MultiplicativeExpression191", type=dsl_UnaryExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unaryExpr193: BinaryAssociation = BinaryAssociation(
    name="unaryExpr193",
    ends={
        Property(name="dsl_UnaryExpression194", type=dsl_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnaryExpression192", type=dsl_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preIncrExpr195: BinaryAssociation = BinaryAssociation(
    name="preIncrExpr195",
    ends={
        Property(name="dsl_PreIncrementExpression", type=dsl_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnaryExpression196", type=dsl_PreIncrementExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preDecrExpr197: BinaryAssociation = BinaryAssociation(
    name="preDecrExpr197",
    ends={
        Property(name="dsl_PreDecrementExpression", type=dsl_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnaryExpression198", type=dsl_PreDecrementExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpNeg199: BinaryAssociation = BinaryAssociation(
    name="unaryExpNeg199",
    ends={
        Property(name="dsl_UnaryExpressionNotPlusMinus", type=dsl_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnaryExpression200", type=dsl_UnaryExpressionNotPlusMinus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
castType216: BinaryAssociation = BinaryAssociation(
    name="castType216",
    ends={
        Property(name="dsl_Type218", type=dsl_CastLookahead, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_CastLookahead217", type=dsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr204: BinaryAssociation = BinaryAssociation(
    name="expr204",
    ends={
        Property(name="dsl_PrimaryExpression206", type=dsl_PreDecrementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PreDecrementExpression205", type=dsl_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unaryExpr207: BinaryAssociation = BinaryAssociation(
    name="unaryExpr207",
    ends={
        Property(name="dsl_UnaryExpression209", type=dsl_UnaryExpressionNotPlusMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnaryExpressionNotPlusMinus208", type=dsl_UnaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
castExpr210: BinaryAssociation = BinaryAssociation(
    name="castExpr210",
    ends={
        Property(name="dsl_CastExpression", type=dsl_UnaryExpressionNotPlusMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnaryExpressionNotPlusMinus211", type=dsl_CastExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postfixExpr212: BinaryAssociation = BinaryAssociation(
    name="postfixExpr212",
    ends={
        Property(name="dsl_PostfixExpression", type=dsl_UnaryExpressionNotPlusMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnaryExpressionNotPlusMinus213", type=dsl_PostfixExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
indexerType214: BinaryAssociation = BinaryAssociation(
    name="indexerType214",
    ends={
        Property(name="dsl_Type215", type=dsl_CastLookahead, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_CastLookahead", type=dsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr227: BinaryAssociation = BinaryAssociation(
    name="expr227",
    ends={
        Property(name="dsl_EObject", type=dsl_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_CastExpression228", type=dsl_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suffixes229: BinaryAssociation = BinaryAssociation(
    name="suffixes229",
    ends={
        Property(name="dsl_EObject231", type=dsl_PrimaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PrimaryExpression230", type=dsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal219: BinaryAssociation = BinaryAssociation(
    name="literal219",
    ends={
        Property(name="dsl_Literal", type=dsl_CastLookahead, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_CastLookahead220", type=dsl_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr221: BinaryAssociation = BinaryAssociation(
    name="expr221",
    ends={
        Property(name="dsl_PrimaryExpression223", type=dsl_PostfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PostfixExpression222", type=dsl_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
castType224: BinaryAssociation = BinaryAssociation(
    name="castType224",
    ends={
        Property(name="dsl_Type226", type=dsl_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_CastExpression225", type=dsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allocExpr239: BinaryAssociation = BinaryAssociation(
    name="allocExpr239",
    ends={
        Property(name="dsl_AllocationExpression", type=dsl_PrimaryPrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PrimaryPrefix240", type=dsl_AllocationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultType241: BinaryAssociation = BinaryAssociation(
    name="resultType241",
    ends={
        Property(name="dsl_ResultType243", type=dsl_PrimaryPrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PrimaryPrefix242", type=dsl_ResultType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name244: BinaryAssociation = BinaryAssociation(
    name="name244",
    ends={
        Property(name="dsl_Name246", type=dsl_PrimaryPrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PrimaryPrefix245", type=dsl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args232: BinaryAssociation = BinaryAssociation(
    name="args232",
    ends={
        Property(name="dsl_TypeArguments233", type=dsl_MemberSelector, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MemberSelector", type=dsl_TypeArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal234: BinaryAssociation = BinaryAssociation(
    name="literal234",
    ends={
        Property(name="dsl_Literal235", type=dsl_PrimaryPrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PrimaryPrefix", type=dsl_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr236: BinaryAssociation = BinaryAssociation(
    name="expr236",
    ends={
        Property(name="dsl_Expression238", type=dsl_PrimaryPrefix, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PrimaryPrefix237", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
allocExpr247: BinaryAssociation = BinaryAssociation(
    name="allocExpr247",
    ends={
        Property(name="dsl_AllocationExpression248", type=dsl_PrimarySuffix, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PrimarySuffix", type=dsl_AllocationExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selector249: BinaryAssociation = BinaryAssociation(
    name="selector249",
    ends={
        Property(name="dsl_MemberSelector251", type=dsl_PrimarySuffix, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PrimarySuffix250", type=dsl_MemberSelector, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bracketExpr252: BinaryAssociation = BinaryAssociation(
    name="bracketExpr252",
    ends={
        Property(name="dsl_Expression254", type=dsl_PrimarySuffix, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PrimarySuffix253", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args255: BinaryAssociation = BinaryAssociation(
    name="args255",
    ends={
        Property(name="dsl_Arguments257", type=dsl_PrimarySuffix, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_PrimarySuffix256", type=dsl_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signedLiteral263: BinaryAssociation = BinaryAssociation(
    name="signedLiteral263",
    ends={
        Property(name="dsl_SignedIntLiteral264", type=dsl_IntegerLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_IntegerLiteral", type=dsl_SignedIntLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unsignedLiteral265: BinaryAssociation = BinaryAssociation(
    name="unsignedLiteral265",
    ends={
        Property(name="dsl_UnsignedIntLiteral267", type=dsl_IntegerLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_IntegerLiteral266", type=dsl_UnsignedIntLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decNum258: BinaryAssociation = BinaryAssociation(
    name="decNum258",
    ends={
        Property(name="dsl_DecimalNumber", type=dsl_UnsignedIntLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnsignedIntLiteral", type=dsl_DecimalNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal259: BinaryAssociation = BinaryAssociation(
    name="literal259",
    ends={
        Property(name="dsl_BaseLiteral", type=dsl_UnsignedIntLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_UnsignedIntLiteral260", type=dsl_BaseLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
baseLiteral261: BinaryAssociation = BinaryAssociation(
    name="baseLiteral261",
    ends={
        Property(name="dsl_BaseLiteral262", type=dsl_SignedIntLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SignedIntLiteral", type=dsl_BaseLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decNumAlpha268: BinaryAssociation = BinaryAssociation(
    name="decNumAlpha268",
    ends={
        Property(name="dsl_DecimalNumber269", type=dsl_FloatLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_FloatLiteral", type=dsl_DecimalNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decNumBeta270: BinaryAssociation = BinaryAssociation(
    name="decNumBeta270",
    ends={
        Property(name="dsl_DecimalNumber272", type=dsl_FloatLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_FloatLiteral271", type=dsl_DecimalNumber, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
intLit273: BinaryAssociation = BinaryAssociation(
    name="intLit273",
    ends={
        Property(name="dsl_IntegerLiteral275", type=dsl_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Literal274", type=dsl_IntegerLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
floatLit276: BinaryAssociation = BinaryAssociation(
    name="floatLit276",
    ends={
        Property(name="dsl_FloatLiteral278", type=dsl_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Literal277", type=dsl_FloatLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boolLit279: BinaryAssociation = BinaryAssociation(
    name="boolLit279",
    ends={
        Property(name="dsl_BooleanLiteral", type=dsl_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Literal280", type=dsl_BooleanLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args294: BinaryAssociation = BinaryAssociation(
    name="args294",
    ends={
        Property(name="dsl_Arguments296", type=dsl_AllocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AllocationExpression295", type=dsl_Arguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body297: BinaryAssociation = BinaryAssociation(
    name="body297",
    ends={
        Property(name="dsl_ClassOrInterfaceBody299", type=dsl_AllocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AllocationExpression298", type=dsl_ClassOrInterfaceBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args281: BinaryAssociation = BinaryAssociation(
    name="args281",
    ends={
        Property(name="dsl_ArgumentList", type=dsl_Arguments, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Arguments282", type=dsl_ArgumentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr283: BinaryAssociation = BinaryAssociation(
    name="expr283",
    ends={
        Property(name="dsl_Expression285", type=dsl_ArgumentList, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ArgumentList284", type=dsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayInits286: BinaryAssociation = BinaryAssociation(
    name="arrayInits286",
    ends={
        Property(name="dsl_ArrayDimsAndInits", type=dsl_AllocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AllocationExpression287", type=dsl_ArrayDimsAndInits, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nonPrimType288: BinaryAssociation = BinaryAssociation(
    name="nonPrimType288",
    ends={
        Property(name="dsl_ClassOrInterfaceType290", type=dsl_AllocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AllocationExpression289", type=dsl_ClassOrInterfaceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeArgs291: BinaryAssociation = BinaryAssociation(
    name="typeArgs291",
    ends={
        Property(name="dsl_TypeArguments293", type=dsl_AllocationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AllocationExpression292", type=dsl_TypeArguments, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block310: BinaryAssociation = BinaryAssociation(
    name="block310",
    ends={
        Property(name="dsl_Block312", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement311", type=dsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr313: BinaryAssociation = BinaryAssociation(
    name="expr313",
    ends={
        Property(name="dsl_StatementExpression", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement314", type=dsl_StatementExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr300: BinaryAssociation = BinaryAssociation(
    name="expr300",
    ends={
        Property(name="dsl_Expression302", type=dsl_ArrayDimsAndInits, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ArrayDimsAndInits301", type=dsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayInit303: BinaryAssociation = BinaryAssociation(
    name="arrayInit303",
    ends={
        Property(name="dsl_ArrayInitializer305", type=dsl_ArrayDimsAndInits, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ArrayDimsAndInits304", type=dsl_ArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labeledSt306: BinaryAssociation = BinaryAssociation(
    name="labeledSt306",
    ends={
        Property(name="dsl_LabeledStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement307", type=dsl_LabeledStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertSt308: BinaryAssociation = BinaryAssociation(
    name="assertSt308",
    ends={
        Property(name="dsl_AssertStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement309", type=dsl_AssertStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
breakSt325: BinaryAssociation = BinaryAssociation(
    name="breakSt325",
    ends={
        Property(name="dsl_BreakStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement326", type=dsl_BreakStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
continueSt327: BinaryAssociation = BinaryAssociation(
    name="continueSt327",
    ends={
        Property(name="dsl_ContinueStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement328", type=dsl_ContinueStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchSt315: BinaryAssociation = BinaryAssociation(
    name="switchSt315",
    ends={
        Property(name="dsl_SwitchStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement316", type=dsl_SwitchStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifSt317: BinaryAssociation = BinaryAssociation(
    name="ifSt317",
    ends={
        Property(name="dsl_IfStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement318", type=dsl_IfStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whileSt319: BinaryAssociation = BinaryAssociation(
    name="whileSt319",
    ends={
        Property(name="dsl_WhileStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement320", type=dsl_WhileStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doSt321: BinaryAssociation = BinaryAssociation(
    name="doSt321",
    ends={
        Property(name="dsl_DoStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement322", type=dsl_DoStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forSt323: BinaryAssociation = BinaryAssociation(
    name="forSt323",
    ends={
        Property(name="dsl_ForStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement324", type=dsl_ForStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprBeta340: BinaryAssociation = BinaryAssociation(
    name="exprBeta340",
    ends={
        Property(name="dsl_Expression342", type=dsl_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AssertStatement341", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnSt329: BinaryAssociation = BinaryAssociation(
    name="returnSt329",
    ends={
        Property(name="dsl_ReturnStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement330", type=dsl_ReturnStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
throwSt331: BinaryAssociation = BinaryAssociation(
    name="throwSt331",
    ends={
        Property(name="dsl_ThrowStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement332", type=dsl_ThrowStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
synchSt333: BinaryAssociation = BinaryAssociation(
    name="synchSt333",
    ends={
        Property(name="dsl_SynchronizedStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement334", type=dsl_SynchronizedStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trySt335: BinaryAssociation = BinaryAssociation(
    name="trySt335",
    ends={
        Property(name="dsl_TryStatement", type=dsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Statement336", type=dsl_TryStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprAlpha337: BinaryAssociation = BinaryAssociation(
    name="exprAlpha337",
    ends={
        Property(name="dsl_Expression339", type=dsl_AssertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AssertStatement338", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
st343: BinaryAssociation = BinaryAssociation(
    name="st343",
    ends={
        Property(name="dsl_Statement345", type=dsl_LabeledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LabeledStatement344", type=dsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blockSt346: BinaryAssociation = BinaryAssociation(
    name="blockSt346",
    ends={
        Property(name="dsl_BlockStatement348", type=dsl_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Block347", type=dsl_BlockStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localVarDecl349: BinaryAssociation = BinaryAssociation(
    name="localVarDecl349",
    ends={
        Property(name="dsl_LocalVariableDeclaration", type=dsl_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_BlockStatement350", type=dsl_LocalVariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type357: BinaryAssociation = BinaryAssociation(
    name="type357",
    ends={
        Property(name="dsl_Type359", type=dsl_LocalVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LocalVariableDeclaration358", type=dsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
st351: BinaryAssociation = BinaryAssociation(
    name="st351",
    ends={
        Property(name="dsl_Statement353", type=dsl_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_BlockStatement352", type=dsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varDecls360: BinaryAssociation = BinaryAssociation(
    name="varDecls360",
    ends={
        Property(name="dsl_VariableDeclarator362", type=dsl_LocalVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LocalVariableDeclaration361", type=dsl_VariableDeclarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDecl354: BinaryAssociation = BinaryAssociation(
    name="typeDecl354",
    ends={
        Property(name="dsl_ClassOrInterfaceDeclaration356", type=dsl_BlockStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_BlockStatement355", type=dsl_ClassOrInterfaceDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preIncrExpr363: BinaryAssociation = BinaryAssociation(
    name="preIncrExpr363",
    ends={
        Property(name="dsl_PreIncrementExpression365", type=dsl_StatementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_StatementExpression364", type=dsl_PreIncrementExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preDecrExpr366: BinaryAssociation = BinaryAssociation(
    name="preDecrExpr366",
    ends={
        Property(name="dsl_PreDecrementExpression368", type=dsl_StatementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_StatementExpression367", type=dsl_PreDecrementExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryExpr369: BinaryAssociation = BinaryAssociation(
    name="primaryExpr369",
    ends={
        Property(name="dsl_PrimaryExpression371", type=dsl_StatementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_StatementExpression370", type=dsl_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr372: BinaryAssociation = BinaryAssociation(
    name="expr372",
    ends={
        Property(name="dsl_Expression374", type=dsl_StatementExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_StatementExpression373", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr375: BinaryAssociation = BinaryAssociation(
    name="expr375",
    ends={
        Property(name="dsl_SwitchStatement376", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="dsl_Expression377", type=dsl_SwitchStatement, multiplicity=Multiplicity(1, 1))
    }
)
switchLabel378: BinaryAssociation = BinaryAssociation(
    name="switchLabel378",
    ends={
        Property(name="dsl_SwitchLabel", type=dsl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SwitchStatement379", type=dsl_SwitchLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block380: BinaryAssociation = BinaryAssociation(
    name="block380",
    ends={
        Property(name="dsl_BlockStatement382", type=dsl_SwitchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SwitchStatement381", type=dsl_BlockStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr383: BinaryAssociation = BinaryAssociation(
    name="expr383",
    ends={
        Property(name="dsl_Expression385", type=dsl_SwitchLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SwitchLabel384", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr386: BinaryAssociation = BinaryAssociation(
    name="expr386",
    ends={
        Property(name="dsl_Expression388", type=dsl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_WhileStatement387", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
st389: BinaryAssociation = BinaryAssociation(
    name="st389",
    ends={
        Property(name="dsl_Statement391", type=dsl_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_WhileStatement390", type=dsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
st392: BinaryAssociation = BinaryAssociation(
    name="st392",
    ends={
        Property(name="dsl_DoStatement393", type=dsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="dsl_Statement394", type=dsl_DoStatement, multiplicity=Multiplicity(1, 1))
    }
)
expr395: BinaryAssociation = BinaryAssociation(
    name="expr395",
    ends={
        Property(name="dsl_Expression397", type=dsl_DoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_DoStatement396", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type398: BinaryAssociation = BinaryAssociation(
    name="type398",
    ends={
        Property(name="dsl_Type400", type=dsl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ForStatement399", type=dsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr401: BinaryAssociation = BinaryAssociation(
    name="expr401",
    ends={
        Property(name="dsl_Expression403", type=dsl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ForStatement402", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forInit404: BinaryAssociation = BinaryAssociation(
    name="forInit404",
    ends={
        Property(name="dsl_ForInit", type=dsl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ForStatement405", type=dsl_ForInit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forExpr406: BinaryAssociation = BinaryAssociation(
    name="forExpr406",
    ends={
        Property(name="dsl_Expression408", type=dsl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ForStatement407", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forUpdate409: BinaryAssociation = BinaryAssociation(
    name="forUpdate409",
    ends={
        Property(name="dsl_ForUpdate", type=dsl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ForStatement410", type=dsl_ForUpdate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
st411: BinaryAssociation = BinaryAssociation(
    name="st411",
    ends={
        Property(name="dsl_Statement413", type=dsl_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ForStatement412", type=dsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decl414: BinaryAssociation = BinaryAssociation(
    name="decl414",
    ends={
        Property(name="dsl_LocalVariableDeclaration416", type=dsl_ForInit, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ForInit415", type=dsl_LocalVariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
st417: BinaryAssociation = BinaryAssociation(
    name="st417",
    ends={
        Property(name="dsl_StatementExpressionList", type=dsl_ForInit, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ForInit418", type=dsl_StatementExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr419: BinaryAssociation = BinaryAssociation(
    name="expr419",
    ends={
        Property(name="dsl_StatementExpression421", type=dsl_StatementExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_StatementExpressionList420", type=dsl_StatementExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
list422: BinaryAssociation = BinaryAssociation(
    name="list422",
    ends={
        Property(name="dsl_StatementExpressionList424", type=dsl_ForUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ForUpdate423", type=dsl_StatementExpressionList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr425: BinaryAssociation = BinaryAssociation(
    name="expr425",
    ends={
        Property(name="dsl_Expression427", type=dsl_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ReturnStatement426", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr428: BinaryAssociation = BinaryAssociation(
    name="expr428",
    ends={
        Property(name="dsl_Expression430", type=dsl_ThrowStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ThrowStatement429", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr431: BinaryAssociation = BinaryAssociation(
    name="expr431",
    ends={
        Property(name="dsl_Expression433", type=dsl_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SynchronizedStatement432", type=dsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block434: BinaryAssociation = BinaryAssociation(
    name="block434",
    ends={
        Property(name="dsl_Block436", type=dsl_SynchronizedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SynchronizedStatement435", type=dsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
block437: BinaryAssociation = BinaryAssociation(
    name="block437",
    ends={
        Property(name="dsl_Block439", type=dsl_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TryStatement438", type=dsl_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params440: BinaryAssociation = BinaryAssociation(
    name="params440",
    ends={
        Property(name="dsl_FormalParameter442", type=dsl_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TryStatement441", type=dsl_FormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finalBlock443: BinaryAssociation = BinaryAssociation(
    name="finalBlock443",
    ends={
        Property(name="dsl_Block445", type=dsl_TryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_TryStatement444", type=dsl_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name446: BinaryAssociation = BinaryAssociation(
    name="name446",
    ends={
        Property(name="dsl_Name447", type=dsl_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Annotation", type=dsl_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valuePairs448: BinaryAssociation = BinaryAssociation(
    name="valuePairs448",
    ends={
        Property(name="dsl_MemberValuePairs", type=dsl_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Annotation449", type=dsl_MemberValuePairs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value450: BinaryAssociation = BinaryAssociation(
    name="value450",
    ends={
        Property(name="dsl_MemberValue", type=dsl_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Annotation451", type=dsl_MemberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pairs452: BinaryAssociation = BinaryAssociation(
    name="pairs452",
    ends={
        Property(name="dsl_MemberValuePair", type=dsl_MemberValuePairs, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MemberValuePairs453", type=dsl_MemberValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value454: BinaryAssociation = BinaryAssociation(
    name="value454",
    ends={
        Property(name="dsl_MemberValue456", type=dsl_MemberValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MemberValuePair455", type=dsl_MemberValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init460: BinaryAssociation = BinaryAssociation(
    name="init460",
    ends={
        Property(name="dsl_MemberValueArrayInitializer", type=dsl_MemberValue, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MemberValue461", type=dsl_MemberValueArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condExpr462: BinaryAssociation = BinaryAssociation(
    name="condExpr462",
    ends={
        Property(name="dsl_ConditionalExpression464", type=dsl_MemberValue, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MemberValue463", type=dsl_ConditionalExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values465: BinaryAssociation = BinaryAssociation(
    name="values465",
    ends={
        Property(name="dsl_MemberValue467", type=dsl_MemberValueArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MemberValueArrayInitializer466", type=dsl_MemberValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body468: BinaryAssociation = BinaryAssociation(
    name="body468",
    ends={
        Property(name="dsl_AnnotationTypeBody", type=dsl_AnnotationTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AnnotationTypeDeclaration469", type=dsl_AnnotationTypeBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
decls470: BinaryAssociation = BinaryAssociation(
    name="decls470",
    ends={
        Property(name="dsl_AnnotationTypeMemberDeclaration", type=dsl_AnnotationTypeBody, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AnnotationTypeBody471", type=dsl_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mods472: BinaryAssociation = BinaryAssociation(
    name="mods472",
    ends={
        Property(name="dsl_TypeBodyModifier474", type=dsl_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AnnotationTypeMemberDeclaration473", type=dsl_TypeBodyModifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type475: BinaryAssociation = BinaryAssociation(
    name="type475",
    ends={
        Property(name="dsl_Type477", type=dsl_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AnnotationTypeMemberDeclaration476", type=dsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annot457: BinaryAssociation = BinaryAssociation(
    name="annot457",
    ends={
        Property(name="dsl_Annotation459", type=dsl_MemberValue, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MemberValue458", type=dsl_Annotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDecl480: BinaryAssociation = BinaryAssociation(
    name="typeDecl480",
    ends={
        Property(name="dsl_ClassOrInterfaceDeclaration482", type=dsl_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AnnotationTypeMemberDeclaration481", type=dsl_ClassOrInterfaceDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumDecl483: BinaryAssociation = BinaryAssociation(
    name="enumDecl483",
    ends={
        Property(name="dsl_EnumDeclaration485", type=dsl_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AnnotationTypeMemberDeclaration484", type=dsl_EnumDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotDecl486: BinaryAssociation = BinaryAssociation(
    name="annotDecl486",
    ends={
        Property(name="dsl_AnnotationTypeDeclaration488", type=dsl_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AnnotationTypeMemberDeclaration487", type=dsl_AnnotationTypeDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldDecl489: BinaryAssociation = BinaryAssociation(
    name="fieldDecl489",
    ends={
        Property(name="dsl_FieldDeclaration491", type=dsl_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AnnotationTypeMemberDeclaration490", type=dsl_FieldDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultVal478: BinaryAssociation = BinaryAssociation(
    name="defaultVal478",
    ends={
        Property(name="dsl_DefaultValue", type=dsl_AnnotationTypeMemberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AnnotationTypeMemberDeclaration479", type=dsl_DefaultValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dsl_Expression_IfStatement = Generalization(general=IfStatement, specific=dsl_Expression)
gen_dsl_MemberValue_DefaultValue = Generalization(general=DefaultValue, specific=dsl_MemberValue)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_CompilationUnit, dsl_TypeBodyModifier, dsl_PackageDeclaration, dsl_ImportDeclaration, dsl_TypeDeclaration, dsl_Name, dsl_CommonModifier, dsl_TypeParameters, dsl_ExtendsList, dsl_ImplementsList, dsl_ClassOrInterfaceDeclaration, dsl_EnumDeclaration, dsl_AnnotationTypeDeclaration, dsl_ClassOrInterfaceBodyDeclaration, dsl_Arguments, dsl_ClassOrInterfaceBody, dsl_ClassOrInterfaceType, dsl_EnumBody, dsl_EnumConstant, dsl_TypeParameter, dsl_TypeBound, dsl_Initializer, dsl_ArrayInitializer, dsl_Expression, dsl_MethodOrCtorDeclaration, dsl_FieldDeclaration, dsl_Type, dsl_VariableDeclarator, dsl_VariableDeclaratorId, dsl_VariableInitializer, dsl_Block, dsl_FormalParameters, dsl_NameList, dsl_ExplicitConstructorInvocation, dsl_BlockStatement, dsl_ResultType, dsl_MethodDeclarator, dsl_FormalParameter, dsl_PrimaryExpression, dsl_TypeArgument, dsl_ReferenceType, dsl_TypeArguments, IfStatement, dsl_WildcardBounds, dsl_ConditionalAndExpression, dsl_ConditionalExpression, dsl_Statement, dsl_ConditionalOrExpression, dsl_InstanceOfExpression, dsl_RelationalExpression, dsl_InclusiveOrExpression, dsl_ExclusiveOrExpression, dsl_AndExpression, dsl_EqualityExpression, dsl_MultiplicativeExpression, dsl_UnaryExpression, dsl_ShiftExpression, dsl_AdditiveExpression, dsl_PreIncrementExpression, dsl_PreDecrementExpression, dsl_UnaryExpressionNotPlusMinus, dsl_CastExpression, dsl_PostfixExpression, dsl_CastLookahead, dsl_EObject, dsl_Literal, dsl_MemberSelector, dsl_PrimaryPrefix, dsl_AllocationExpression, dsl_BaseLiteral, dsl_PrimarySuffix, dsl_DecimalNumber, dsl_FloatLiteral, dsl_UnsignedIntLiteral, dsl_SignedIntLiteral, dsl_IntegerLiteral, dsl_ArgumentList, dsl_BooleanLiteral, dsl_ArrayDimsAndInits, dsl_StatementExpression, dsl_LabeledStatement, dsl_AssertStatement, dsl_BreakStatement, dsl_ContinueStatement, dsl_SwitchStatement, dsl_IfStatement, dsl_WhileStatement, dsl_DoStatement, dsl_ForStatement, dsl_ReturnStatement, dsl_ThrowStatement, dsl_SynchronizedStatement, dsl_TryStatement, dsl_LocalVariableDeclaration, dsl_SwitchLabel, dsl_ForInit, dsl_ForUpdate, dsl_StatementExpressionList, dsl_Annotation, dsl_MemberValuePairs, dsl_MemberValue, dsl_MemberValuePair, DefaultValue, dsl_MemberValueArrayInitializer, dsl_AnnotationTypeBody, dsl_AnnotationTypeMemberDeclaration, dsl_DefaultValue, Visibility},
    associations={packageDecl0, importDecls1, typeDecls3, name5, name7, typeParams20, exts22, impls24, mod10, mod11, classInterfDecl14, enumDecl16, annotDecl18, constants41, bodies43, body26, exts28, impls30, typeKind33, impls36, body39, mods62, nestedClassEnumType65, enumDecl68, args45, body47, typeParams50, type52, typeKind54, body57, init60, arrayInit83, expr85, ctorOrMethod71, field73, type75, varDecl77, varDeclId79, varInit81, block105, formalParams107, varInit87, typeParams90, formalParams93, throwsList95, ctorInvoc97, statements99, resultType101, methodDecl103, block123, params110, type112, varDeclId115, args118, expr121, typeArgs133, refType126, typeKind128, names146, typeArgs131, refType135, wildCard138, refType140, type143, exprAlpha161, exprBeta164, condExpr149, expr152, ifSt154, elseSt156, expr159, expr177, expr167, expr169, expr171, expr173, expr175, expr188, expr179, type181, expr184, expr186, expr201, expr190, unaryExpr193, preIncrExpr195, preDecrExpr197, unaryExpNeg199, castType216, expr204, unaryExpr207, castExpr210, postfixExpr212, indexerType214, expr227, suffixes229, literal219, expr221, castType224, allocExpr239, resultType241, name244, args232, literal234, expr236, allocExpr247, selector249, bracketExpr252, args255, signedLiteral263, unsignedLiteral265, decNum258, literal259, baseLiteral261, decNumAlpha268, decNumBeta270, intLit273, floatLit276, boolLit279, args294, body297, args281, expr283, arrayInits286, nonPrimType288, typeArgs291, block310, expr313, expr300, arrayInit303, labeledSt306, assertSt308, breakSt325, continueSt327, switchSt315, ifSt317, whileSt319, doSt321, forSt323, exprBeta340, returnSt329, throwSt331, synchSt333, trySt335, exprAlpha337, st343, blockSt346, localVarDecl349, type357, st351, varDecls360, typeDecl354, preIncrExpr363, preDecrExpr366, primaryExpr369, expr372, expr375, switchLabel378, block380, expr383, expr386, st389, st392, expr395, type398, expr401, forInit404, forExpr406, forUpdate409, st411, decl414, st417, expr419, list422, expr425, expr428, expr431, block434, block437, params440, finalBlock443, name446, valuePairs448, value450, pairs452, value454, init460, condExpr462, values465, body468, decls470, mods472, type475, annot457, typeDecl480, enumDecl483, annotDecl486, fieldDecl489, defaultVal478},
    generalizations={gen_dsl_Expression_IfStatement, gen_dsl_MemberValue_DefaultValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)