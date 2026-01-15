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
CppQualifierType: Enumeration = Enumeration(
    name="CppQualifierType",
    literals={
            EnumerationLiteral(name="CONST"),
			EnumerationLiteral(name="VOLATILE"),
			EnumerationLiteral(name="RESTRICT"),
			EnumerationLiteral(name="ATOMIC")
    }
)

CppOperator: Enumeration = Enumeration(
    name="CppOperator",
    literals={
            EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="XOR_EQ"),
			EnumerationLiteral(name="LESS_EQUALS"),
			EnumerationLiteral(name="EQUALS"),
			EnumerationLiteral(name="NOT_EQUALS"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="GREATER_THAN"),
			EnumerationLiteral(name="LESS_THAN"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="DIVISION"),
			EnumerationLiteral(name="SHIFT_LEFT"),
			EnumerationLiteral(name="SHIFT_RIGHT"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="BIT_OR"),
			EnumerationLiteral(name="REMAINDER"),
			EnumerationLiteral(name="BIT_AND")
    }
)

CppVarType: Enumeration = Enumeration(
    name="CppVarType",
    literals={
            EnumerationLiteral(name="OBJECT"),
			EnumerationLiteral(name="REFERENCE"),
			EnumerationLiteral(name="POINTER")
    }
)

CppAccessSpecifier: Enumeration = Enumeration(
    name="CppAccessSpecifier",
    literals={
            EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PUBLIC")
    }
)

CppClassKey: Enumeration = Enumeration(
    name="CppClassKey",
    literals={
            EnumerationLiteral(name="CLASS"),
			EnumerationLiteral(name="STRUCT"),
			EnumerationLiteral(name="UNION")
    }
)

CppLinkageSpecifier: Enumeration = Enumeration(
    name="CppLinkageSpecifier",
    literals={
            EnumerationLiteral(name="STATIC"),
			EnumerationLiteral(name="EXTERN")
    }
)

CppStorageType: Enumeration = Enumeration(
    name="CppStorageType",
    literals={
            EnumerationLiteral(name="AUTO"),
			EnumerationLiteral(name="REGISTER"),
			EnumerationLiteral(name="STATIC"),
			EnumerationLiteral(name="EXTERN"),
			EnumerationLiteral(name="TYPEDEF"),
			EnumerationLiteral(name="THREAD_LOCAL"),
			EnumerationLiteral(name="MUTABLE")
    }
)

CppUnaryOperator: Enumeration = Enumeration(
    name="CppUnaryOperator",
    literals={
            EnumerationLiteral(name="AMPERSAND"),
			EnumerationLiteral(name="ASTERISK"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="BIT_NOT"),
			EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT")
    }
)

CppAssignmentOperator: Enumeration = Enumeration(
    name="CppAssignmentOperator",
    literals={
            EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="TIMES_ASSIGN"),
			EnumerationLiteral(name="DIVISSION_ASSIGN"),
			EnumerationLiteral(name="MODULO_ASSIGN"),
			EnumerationLiteral(name="PLUS_ASSIGN"),
			EnumerationLiteral(name="MINUS_ASSIGN"),
			EnumerationLiteral(name="SHIFT_LEFT_ASSIGN"),
			EnumerationLiteral(name="SHIFT_RIGHT_ASSIGN"),
			EnumerationLiteral(name="AND_ASSIGN"),
			EnumerationLiteral(name="XOR_ASSIGN"),
			EnumerationLiteral(name="OR_ASSIGN")
    }
)

CppPostfixOperator: Enumeration = Enumeration(
    name="CppPostfixOperator",
    literals={
            EnumerationLiteral(name="DECREMENT"),
			EnumerationLiteral(name="INCREMENT")
    }
)

# Classes
CppNamedElement = Class(name="CppNamedElement")
Metamodelo_Cpp_CppPackage = Class(name="Metamodelo::Cpp::CppPackage")
Metamodelo_Cpp_CppPathReference = Class(name="Metamodelo::Cpp::CppPathReference", is_abstract=True)
CppModelElement = Class(name="CppModelElement")
CppPathReferentiable = Class(name="CppPathReferentiable")
Metamodelo_Cpp_CppModel = Class(name="Metamodelo::Cpp::CppModel")
Metamodelo_Cpp_CppClass = Class(name="Metamodelo::Cpp::CppClass")
Metamodelo_Cpp_CppPathReferentiable = Class(name="Metamodelo::Cpp::CppPathReferentiable", is_abstract=True)
Metamodelo_Cpp_CppType = Class(name="Metamodelo::Cpp::CppType", is_abstract=True)
Metamodelo_Cpp_CppClassFile = Class(name="Metamodelo::Cpp::CppClassFile")
Metamodelo_Cpp_CppModelElement = Class(name="Metamodelo::Cpp::CppModelElement", is_abstract=True)
Metamodelo_Cpp_CppNamedElement = Class(name="Metamodelo::Cpp::CppNamedElement", is_abstract=True)
Metamodelo_Cpp_CppVariable = Class(name="Metamodelo::Cpp::CppVariable")
Metamodelo_Cpp_CppImportDeclaration = Class(name="Metamodelo::Cpp::CppImportDeclaration")
Metamodelo_Cpp_CppTypeAccess = Class(name="Metamodelo::Cpp::CppTypeAccess")
Metamodelo_Cpp_CppTypeParameter = Class(name="Metamodelo::Cpp::CppTypeParameter")
CppType = Class(name="CppType")
Metamodelo_Cpp_CppClassifier = Class(name="Metamodelo::Cpp::CppClassifier", is_abstract=True)
CppFieldContainer = Class(name="CppFieldContainer")
Metamodelo_Cpp_CppMemberFunction = Class(name="Metamodelo::Cpp::CppMemberFunction", is_abstract=True)
Metamodelo_Cpp_CppShortType = Class(name="Metamodelo::Cpp::CppShortType")
Metamodelo_Cpp_CppIntType = Class(name="Metamodelo::Cpp::CppIntType")
Metamodelo_Cpp_CppLongType = Class(name="Metamodelo::Cpp::CppLongType")
Metamodelo_Cpp_CppFloatType = Class(name="Metamodelo::Cpp::CppFloatType")
Metamodelo_Cpp_CppDoubleType = Class(name="Metamodelo::Cpp::CppDoubleType")
Metamodelo_Cpp_CppSignedType = Class(name="Metamodelo::Cpp::CppSignedType")
Metamodelo_Cpp_CppUnsignedType = Class(name="Metamodelo::Cpp::CppUnsignedType")
CppClassifier = Class(name="CppClassifier")
Metamodelo_Cpp_CppEnum = Class(name="Metamodelo::Cpp::CppEnum")
Metamodelo_Cpp_CppEnumConstructor = Class(name="Metamodelo::Cpp::CppEnumConstructor")
Metamodelo_Cpp_CppExpression = Class(name="Metamodelo::Cpp::CppExpression", is_abstract=True)
Metamodelo_Cpp_CppComment = Class(name="Metamodelo::Cpp::CppComment")
Metamodelo_Cpp_CppPrimitiveType = Class(name="Metamodelo::Cpp::CppPrimitiveType", is_abstract=True)
Metamodelo_Cpp_CppBooleanType = Class(name="Metamodelo::Cpp::CppBooleanType")
CppPrimitiveType = Class(name="CppPrimitiveType")
Metamodelo_Cpp_CppVoidType = Class(name="Metamodelo::Cpp::CppVoidType")
Metamodelo_Cpp_CppCharType = Class(name="Metamodelo::Cpp::CppCharType")
Metamodelo_Cpp_CppArrayInitializer = Class(name="Metamodelo::Cpp::CppArrayInitializer")
CppExpression = Class(name="CppExpression")
Metamodelo_Cpp_CppTypedElement = Class(name="Metamodelo::Cpp::CppTypedElement", is_abstract=True)
CppVariableDeclaration = Class(name="CppVariableDeclaration")
Metamodelo_Cpp_CppDestructor = Class(name="Metamodelo::Cpp::CppDestructor")
CppField = Class(name="CppField")
CppTypedElement = Class(name="CppTypedElement")
Metamodelo_Cpp_CppMethod = Class(name="Metamodelo::Cpp::CppMethod")
Metamodelo_Cpp_CppFunction = Class(name="Metamodelo::Cpp::CppFunction", is_abstract=True)
Metamodelo_Cpp_CppSingleVariableDeclaration = Class(name="Metamodelo::Cpp::CppSingleVariableDeclaration")
Metamodelo_Cpp_CppBlock = Class(name="Metamodelo::Cpp::CppBlock")
CppFunction = Class(name="CppFunction")
Metamodelo_Cpp_CppConstructor = Class(name="Metamodelo::Cpp::CppConstructor")
CppMemberFunction = Class(name="CppMemberFunction")
Metamodelo_Cpp_CppIterationStatement = Class(name="Metamodelo::Cpp::CppIterationStatement", is_abstract=True)
Metamodelo_Cpp_CppAbstractMethodInvocation = Class(name="Metamodelo::Cpp::CppAbstractMethodInvocation", is_abstract=True)
Metamodelo_Cpp_CppMethodInvocation = Class(name="Metamodelo::Cpp::CppMethodInvocation")
CppAbstractMethodInvocation = Class(name="CppAbstractMethodInvocation")
Metamodelo_Cpp_CppSuperMethodInvocation = Class(name="Metamodelo::Cpp::CppSuperMethodInvocation")
Metamodelo_Cpp_CppSuperConstructorInvocation = Class(name="Metamodelo::Cpp::CppSuperConstructorInvocation")
CppMethodInvocation = Class(name="CppMethodInvocation")
Metamodelo_Cpp_CppLabeledStatement = Class(name="Metamodelo::Cpp::CppLabeledStatement")
Metamodelo_Cpp_CppSelectionStatement = Class(name="Metamodelo::Cpp::CppSelectionStatement", is_abstract=True)
Metamodelo_Cpp_CppJumpStatement = Class(name="Metamodelo::Cpp::CppJumpStatement", is_abstract=True)
Metamodelo_Cpp_CppIfStatement = Class(name="Metamodelo::Cpp::CppIfStatement")
CppSelectionStatement = Class(name="CppSelectionStatement")
Metamodelo_Cpp_CppIfElseStatement = Class(name="Metamodelo::Cpp::CppIfElseStatement")
Metamodelo_Cpp_CppSwitchExpression = Class(name="Metamodelo::Cpp::CppSwitchExpression")
Metamodelo_Cpp_CppCase = Class(name="Metamodelo::Cpp::CppCase")
Metamodelo_Cpp_CppGotoStatement = Class(name="Metamodelo::Cpp::CppGotoStatement")
Metamodelo_Cpp_CppContinueStatement = Class(name="Metamodelo::Cpp::CppContinueStatement")
Metamodelo_Cpp_CppAssignamentStatement = Class(name="Metamodelo::Cpp::CppAssignamentStatement")
CppBinaryExpression = Class(name="CppBinaryExpression")
Metamodelo_Cpp_CppWhileStatement = Class(name="Metamodelo::Cpp::CppWhileStatement")
CppIterationStatement = Class(name="CppIterationStatement")
Metamodelo_Cpp_CppDoWhileStatement = Class(name="Metamodelo::Cpp::CppDoWhileStatement")
Metamodelo_Cpp_CppForStatement = Class(name="Metamodelo::Cpp::CppForStatement")
Metamodelo_Cpp_CppBreakStatement = Class(name="Metamodelo::Cpp::CppBreakStatement")
CppJumpStatement = Class(name="CppJumpStatement")
Metamodelo_Cpp_CppReturnStatement = Class(name="Metamodelo::Cpp::CppReturnStatement")
Metamodelo_Cpp_CppDeclarationExpression = Class(name="Metamodelo::Cpp::CppDeclarationExpression")
Metamodelo_Cpp_CppVariableDeclarationGroup = Class(name="Metamodelo::Cpp::CppVariableDeclarationGroup")
Metamodelo_Cpp_CppNullLiteral = Class(name="Metamodelo::Cpp::CppNullLiteral")
Metamodelo_Cpp_CppBooleanLiteral = Class(name="Metamodelo::Cpp::CppBooleanLiteral")
Metamodelo_Cpp_CppCharacterLiteral = Class(name="Metamodelo::Cpp::CppCharacterLiteral")
Metamodelo_Cpp_CppNumberLiteral = Class(name="Metamodelo::Cpp::CppNumberLiteral")
Metamodelo_Cpp_CppStringLiteral = Class(name="Metamodelo::Cpp::CppStringLiteral")
Metamodelo_Cpp_CppRegexLiteral = Class(name="Metamodelo::Cpp::CppRegexLiteral")
Metamodelo_Cpp_CppParenthizedExpression = Class(name="Metamodelo::Cpp::CppParenthizedExpression")
Metamodelo_Cpp_CppCastExpression = Class(name="Metamodelo::Cpp::CppCastExpression")
Metamodelo_Cpp_CppBinaryExpression = Class(name="Metamodelo::Cpp::CppBinaryExpression", is_abstract=True)
Metamodelo_Cpp_CppInfixExpression = Class(name="Metamodelo::Cpp::CppInfixExpression")
Metamodelo_Cpp_CppUnaryExpression = Class(name="Metamodelo::Cpp::CppUnaryExpression", is_abstract=True)
Metamodelo_Cpp_CppPostfixExpression = Class(name="Metamodelo::Cpp::CppPostfixExpression")
CppUnaryExpression = Class(name="CppUnaryExpression")
Metamodelo_Cpp_CppPrefixExpression = Class(name="Metamodelo::Cpp::CppPrefixExpression")
Metamodelo_Cpp_CppThrowExpression = Class(name="Metamodelo::Cpp::CppThrowExpression")
Metamodelo_Cpp_CppThisExpression = Class(name="Metamodelo::Cpp::CppThisExpression")
Metamodelo_Cpp_CppFieldAccess = Class(name="Metamodelo::Cpp::CppFieldAccess")
Metamodelo_Cpp_CppVariableAccess = Class(name="Metamodelo::Cpp::CppVariableAccess")
Metamodelo_Cpp_CppConstantExpression = Class(name="Metamodelo::Cpp::CppConstantExpression")
Metamodelo_Cpp_CppArrayAccess = Class(name="Metamodelo::Cpp::CppArrayAccess")
Metamodelo_Cpp_CppField = Class(name="Metamodelo::Cpp::CppField", is_abstract=True)
Metamodelo_Cpp_CppFieldContainer = Class(name="Metamodelo::Cpp::CppFieldContainer")
Metamodelo_Cpp_CppTryExpression = Class(name="Metamodelo::Cpp::CppTryExpression")
Metamodelo_Cpp_CppCatchClause = Class(name="Metamodelo::Cpp::CppCatchClause")
Metamodelo_Cpp_CppVariableDeclarationFragment = Class(name="Metamodelo::Cpp::CppVariableDeclarationFragment")
Metamodelo_Cpp_CppVariableDeclaration = Class(name="Metamodelo::Cpp::CppVariableDeclaration", is_abstract=True)

# CppNamedElement class attributes and methods

# Metamodelo_Cpp_CppPackage class attributes and methods

# Metamodelo_Cpp_CppPathReference class attributes and methods

# CppModelElement class attributes and methods

# CppPathReferentiable class attributes and methods

# Metamodelo_Cpp_CppModel class attributes and methods
Metamodelo_Cpp_CppModel_name: Property = Property(name="name", type=StringType)
Metamodelo_Cpp_CppModel_sourceFolder: Property = Property(name="sourceFolder", type=StringType)
Metamodelo_Cpp_CppModel_targetFolder: Property = Property(name="targetFolder", type=StringType)
Metamodelo_Cpp_CppModel.attributes={Metamodelo_Cpp_CppModel_name, Metamodelo_Cpp_CppModel_sourceFolder, Metamodelo_Cpp_CppModel_targetFolder}

# Metamodelo_Cpp_CppClass class attributes and methods
Metamodelo_Cpp_CppClass_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
Metamodelo_Cpp_CppClass_classkey: Property = Property(name="classkey", type=StringType)
Metamodelo_Cpp_CppClass_isGeneric: Property = Property(name="isGeneric", type=BooleanType)
Metamodelo_Cpp_CppClass_isFinal: Property = Property(name="isFinal", type=BooleanType)
Metamodelo_Cpp_CppClass.attributes={Metamodelo_Cpp_CppClass_classkey, Metamodelo_Cpp_CppClass_isGeneric, Metamodelo_Cpp_CppClass_isFinal, Metamodelo_Cpp_CppClass_isAbstract}

# Metamodelo_Cpp_CppPathReferentiable class attributes and methods

# Metamodelo_Cpp_CppType class attributes and methods

# Metamodelo_Cpp_CppClassFile class attributes and methods

# Metamodelo_Cpp_CppModelElement class attributes and methods

# Metamodelo_Cpp_CppNamedElement class attributes and methods
Metamodelo_Cpp_CppNamedElement_name: Property = Property(name="name", type=StringType)
Metamodelo_Cpp_CppNamedElement.attributes={Metamodelo_Cpp_CppNamedElement_name}

# Metamodelo_Cpp_CppVariable class attributes and methods
Metamodelo_Cpp_CppVariable_isConst: Property = Property(name="isConst", type=BooleanType)
Metamodelo_Cpp_CppVariable_storage: Property = Property(name="storage", type=StringType)
Metamodelo_Cpp_CppVariable.attributes={Metamodelo_Cpp_CppVariable_isConst, Metamodelo_Cpp_CppVariable_storage}

# Metamodelo_Cpp_CppImportDeclaration class attributes and methods

# Metamodelo_Cpp_CppTypeAccess class attributes and methods

# Metamodelo_Cpp_CppTypeParameter class attributes and methods

# CppType class attributes and methods

# Metamodelo_Cpp_CppClassifier class attributes and methods

# CppFieldContainer class attributes and methods

# Metamodelo_Cpp_CppMemberFunction class attributes and methods

# Metamodelo_Cpp_CppShortType class attributes and methods

# Metamodelo_Cpp_CppIntType class attributes and methods

# Metamodelo_Cpp_CppLongType class attributes and methods

# Metamodelo_Cpp_CppFloatType class attributes and methods

# Metamodelo_Cpp_CppDoubleType class attributes and methods

# Metamodelo_Cpp_CppSignedType class attributes and methods

# Metamodelo_Cpp_CppUnsignedType class attributes and methods

# CppClassifier class attributes and methods

# Metamodelo_Cpp_CppEnum class attributes and methods

# Metamodelo_Cpp_CppEnumConstructor class attributes and methods

# Metamodelo_Cpp_CppExpression class attributes and methods

# Metamodelo_Cpp_CppComment class attributes and methods
Metamodelo_Cpp_CppComment_singleLine: Property = Property(name="singleLine", type=BooleanType)
Metamodelo_Cpp_CppComment_multiLine: Property = Property(name="multiLine", type=BooleanType)
Metamodelo_Cpp_CppComment_content: Property = Property(name="content", type=StringType)
Metamodelo_Cpp_CppComment.attributes={Metamodelo_Cpp_CppComment_content, Metamodelo_Cpp_CppComment_singleLine, Metamodelo_Cpp_CppComment_multiLine}

# Metamodelo_Cpp_CppPrimitiveType class attributes and methods

# Metamodelo_Cpp_CppBooleanType class attributes and methods

# CppPrimitiveType class attributes and methods

# Metamodelo_Cpp_CppVoidType class attributes and methods

# Metamodelo_Cpp_CppCharType class attributes and methods

# Metamodelo_Cpp_CppArrayInitializer class attributes and methods

# CppExpression class attributes and methods

# Metamodelo_Cpp_CppTypedElement class attributes and methods

# CppVariableDeclaration class attributes and methods

# Metamodelo_Cpp_CppDestructor class attributes and methods
Metamodelo_Cpp_CppDestructor_isVirtual: Property = Property(name="isVirtual", type=BooleanType)
Metamodelo_Cpp_CppDestructor.attributes={Metamodelo_Cpp_CppDestructor_isVirtual}

# CppField class attributes and methods

# CppTypedElement class attributes and methods

# Metamodelo_Cpp_CppMethod class attributes and methods
Metamodelo_Cpp_CppMethod_isFinal: Property = Property(name="isFinal", type=BooleanType)
Metamodelo_Cpp_CppMethod_isConst: Property = Property(name="isConst", type=BooleanType)
Metamodelo_Cpp_CppMethod_isVirtual: Property = Property(name="isVirtual", type=BooleanType)
Metamodelo_Cpp_CppMethod_isPureVirtual: Property = Property(name="isPureVirtual", type=BooleanType)
Metamodelo_Cpp_CppMethod.attributes={Metamodelo_Cpp_CppMethod_isPureVirtual, Metamodelo_Cpp_CppMethod_isConst, Metamodelo_Cpp_CppMethod_isVirtual, Metamodelo_Cpp_CppMethod_isFinal}

# Metamodelo_Cpp_CppFunction class attributes and methods
Metamodelo_Cpp_CppFunction_isVarArg: Property = Property(name="isVarArg", type=BooleanType)
Metamodelo_Cpp_CppFunction_linkage: Property = Property(name="linkage", type=StringType)
Metamodelo_Cpp_CppFunction_isInline: Property = Property(name="isInline", type=BooleanType)
Metamodelo_Cpp_CppFunction.attributes={Metamodelo_Cpp_CppFunction_isVarArg, Metamodelo_Cpp_CppFunction_linkage, Metamodelo_Cpp_CppFunction_isInline}

# Metamodelo_Cpp_CppSingleVariableDeclaration class attributes and methods

# Metamodelo_Cpp_CppBlock class attributes and methods

# CppFunction class attributes and methods

# Metamodelo_Cpp_CppConstructor class attributes and methods

# CppMemberFunction class attributes and methods

# Metamodelo_Cpp_CppIterationStatement class attributes and methods

# Metamodelo_Cpp_CppAbstractMethodInvocation class attributes and methods

# Metamodelo_Cpp_CppMethodInvocation class attributes and methods

# CppAbstractMethodInvocation class attributes and methods

# Metamodelo_Cpp_CppSuperMethodInvocation class attributes and methods

# Metamodelo_Cpp_CppSuperConstructorInvocation class attributes and methods

# CppMethodInvocation class attributes and methods

# Metamodelo_Cpp_CppLabeledStatement class attributes and methods

# Metamodelo_Cpp_CppSelectionStatement class attributes and methods

# Metamodelo_Cpp_CppJumpStatement class attributes and methods

# Metamodelo_Cpp_CppIfStatement class attributes and methods

# CppSelectionStatement class attributes and methods

# Metamodelo_Cpp_CppIfElseStatement class attributes and methods
Metamodelo_Cpp_CppIfElseStatement_inLine: Property = Property(name="inLine", type=BooleanType)
Metamodelo_Cpp_CppIfElseStatement.attributes={Metamodelo_Cpp_CppIfElseStatement_inLine}

# Metamodelo_Cpp_CppSwitchExpression class attributes and methods

# Metamodelo_Cpp_CppCase class attributes and methods

# Metamodelo_Cpp_CppGotoStatement class attributes and methods

# Metamodelo_Cpp_CppContinueStatement class attributes and methods

# Metamodelo_Cpp_CppAssignamentStatement class attributes and methods
Metamodelo_Cpp_CppAssignamentStatement_operator: Property = Property(name="operator", type=StringType)
Metamodelo_Cpp_CppAssignamentStatement.attributes={Metamodelo_Cpp_CppAssignamentStatement_operator}

# CppBinaryExpression class attributes and methods

# Metamodelo_Cpp_CppWhileStatement class attributes and methods

# CppIterationStatement class attributes and methods

# Metamodelo_Cpp_CppDoWhileStatement class attributes and methods

# Metamodelo_Cpp_CppForStatement class attributes and methods

# Metamodelo_Cpp_CppBreakStatement class attributes and methods

# CppJumpStatement class attributes and methods

# Metamodelo_Cpp_CppReturnStatement class attributes and methods

# Metamodelo_Cpp_CppDeclarationExpression class attributes and methods

# Metamodelo_Cpp_CppVariableDeclarationGroup class attributes and methods

# Metamodelo_Cpp_CppNullLiteral class attributes and methods

# Metamodelo_Cpp_CppBooleanLiteral class attributes and methods
Metamodelo_Cpp_CppBooleanLiteral_booleanValue: Property = Property(name="booleanValue", type=BooleanType)
Metamodelo_Cpp_CppBooleanLiteral.attributes={Metamodelo_Cpp_CppBooleanLiteral_booleanValue}

# Metamodelo_Cpp_CppCharacterLiteral class attributes and methods
Metamodelo_Cpp_CppCharacterLiteral_charValue: Property = Property(name="charValue", type=StringType)
Metamodelo_Cpp_CppCharacterLiteral.attributes={Metamodelo_Cpp_CppCharacterLiteral_charValue}

# Metamodelo_Cpp_CppNumberLiteral class attributes and methods
Metamodelo_Cpp_CppNumberLiteral_token: Property = Property(name="token", type=StringType)
Metamodelo_Cpp_CppNumberLiteral.attributes={Metamodelo_Cpp_CppNumberLiteral_token}

# Metamodelo_Cpp_CppStringLiteral class attributes and methods
Metamodelo_Cpp_CppStringLiteral_literalValue: Property = Property(name="literalValue", type=StringType)
Metamodelo_Cpp_CppStringLiteral.attributes={Metamodelo_Cpp_CppStringLiteral_literalValue}

# Metamodelo_Cpp_CppRegexLiteral class attributes and methods
Metamodelo_Cpp_CppRegexLiteral_options: Property = Property(name="options", type=StringType)
Metamodelo_Cpp_CppRegexLiteral_pattern: Property = Property(name="pattern", type=StringType)
Metamodelo_Cpp_CppRegexLiteral.attributes={Metamodelo_Cpp_CppRegexLiteral_pattern, Metamodelo_Cpp_CppRegexLiteral_options}

# Metamodelo_Cpp_CppParenthizedExpression class attributes and methods

# Metamodelo_Cpp_CppCastExpression class attributes and methods

# Metamodelo_Cpp_CppBinaryExpression class attributes and methods

# Metamodelo_Cpp_CppInfixExpression class attributes and methods
Metamodelo_Cpp_CppInfixExpression_operator: Property = Property(name="operator", type=StringType)
Metamodelo_Cpp_CppInfixExpression.attributes={Metamodelo_Cpp_CppInfixExpression_operator}

# Metamodelo_Cpp_CppUnaryExpression class attributes and methods

# Metamodelo_Cpp_CppPostfixExpression class attributes and methods
Metamodelo_Cpp_CppPostfixExpression_operator: Property = Property(name="operator", type=StringType)
Metamodelo_Cpp_CppPostfixExpression.attributes={Metamodelo_Cpp_CppPostfixExpression_operator}

# CppUnaryExpression class attributes and methods

# Metamodelo_Cpp_CppPrefixExpression class attributes and methods
Metamodelo_Cpp_CppPrefixExpression_operator: Property = Property(name="operator", type=StringType)
Metamodelo_Cpp_CppPrefixExpression.attributes={Metamodelo_Cpp_CppPrefixExpression_operator}

# Metamodelo_Cpp_CppThrowExpression class attributes and methods

# Metamodelo_Cpp_CppThisExpression class attributes and methods

# Metamodelo_Cpp_CppFieldAccess class attributes and methods

# Metamodelo_Cpp_CppVariableAccess class attributes and methods

# Metamodelo_Cpp_CppConstantExpression class attributes and methods

# Metamodelo_Cpp_CppArrayAccess class attributes and methods

# Metamodelo_Cpp_CppField class attributes and methods
Metamodelo_Cpp_CppField_accessSpecifier: Property = Property(name="accessSpecifier", type=StringType)
Metamodelo_Cpp_CppField.attributes={Metamodelo_Cpp_CppField_accessSpecifier}

# Metamodelo_Cpp_CppFieldContainer class attributes and methods

# Metamodelo_Cpp_CppTryExpression class attributes and methods

# Metamodelo_Cpp_CppCatchClause class attributes and methods

# Metamodelo_Cpp_CppVariableDeclarationFragment class attributes and methods

# Metamodelo_Cpp_CppVariableDeclaration class attributes and methods
Metamodelo_Cpp_CppVariableDeclaration_vartype: Property = Property(name="vartype", type=StringType)
Metamodelo_Cpp_CppVariableDeclaration_isArray: Property = Property(name="isArray", type=BooleanType)
Metamodelo_Cpp_CppVariableDeclaration.attributes={Metamodelo_Cpp_CppVariableDeclaration_vartype, Metamodelo_Cpp_CppVariableDeclaration_isArray}

# Relationships
parentReference7: BinaryAssociation = BinaryAssociation(
    name="parentReference7",
    ends={
        Property(name="CppPackage", type=Metamodelo_Cpp_CppPathReferentiable, multiplicity=Multiplicity(1, 1)),
        Property(name="childrenReferences", type=Metamodelo_Cpp_CppPackage, multiplicity=Multiplicity(0, 1))
    }
)
referencedIn8: BinaryAssociation = BinaryAssociation(
    name="referencedIn8",
    ends={
        Property(name="CppPathReference", type=Metamodelo_Cpp_CppPathReferentiable, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedTerminal", type=Metamodelo_Cpp_CppPathReference, multiplicity=Multiplicity(0, 9999))
    }
)
referencedTerminal9: BinaryAssociation = BinaryAssociation(
    name="referencedTerminal9",
    ends={
        Property(name="CppPathReferentiable", type=Metamodelo_Cpp_CppPathReference, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedIn", type=Metamodelo_Cpp_CppPathReferentiable, multiplicity=Multiplicity(0, 1))
    }
)
mainClass0: BinaryAssociation = BinaryAssociation(
    name="mainClass0",
    ends={
        Property(name="Metamodelo_Cpp_CppClass", type=Metamodelo_Cpp_CppModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppModel", type=Metamodelo_Cpp_CppClass, multiplicity=Multiplicity(1, 1))
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="Metamodelo_Cpp_CppPathReferentiable", type=Metamodelo_Cpp_CppModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppModel2", type=Metamodelo_Cpp_CppPathReferentiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orphanTypes3: BinaryAssociation = BinaryAssociation(
    name="orphanTypes3",
    ends={
        Property(name="Metamodelo_Cpp_CppType", type=Metamodelo_Cpp_CppModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppModel4", type=Metamodelo_Cpp_CppType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules5: BinaryAssociation = BinaryAssociation(
    name="modules5",
    ends={
        Property(name="Metamodelo_Cpp_CppClassFile", type=Metamodelo_Cpp_CppModel, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppModel6", type=Metamodelo_Cpp_CppClassFile, multiplicity=Multiplicity(0, 9999))
    }
)
childrenReferences10: BinaryAssociation = BinaryAssociation(
    name="childrenReferences10",
    ends={
        Property(name="CppPathReferentiable11", type=Metamodelo_Cpp_CppPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="parentReference", type=Metamodelo_Cpp_CppPathReferentiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenPackages13: BinaryAssociation = BinaryAssociation(
    name="childrenPackages13",
    ends={
        Property(name="Metamodelo_Cpp_CppPackage", type=Metamodelo_Cpp_CppPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppPackage12", type=Metamodelo_Cpp_CppPackage, multiplicity=Multiplicity(0, 9999))
    }
)
containedTypes14: BinaryAssociation = BinaryAssociation(
    name="containedTypes14",
    ends={
        Property(name="Metamodelo_Cpp_CppType16", type=Metamodelo_Cpp_CppPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppPackage15", type=Metamodelo_Cpp_CppType, multiplicity=Multiplicity(0, 9999))
    }
)
cppDestructor28: BinaryAssociation = BinaryAssociation(
    name="cppDestructor28",
    ends={
        Property(name="Metamodelo_Cpp_CppMemberFunction30", type=Metamodelo_Cpp_CppClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppClassifier29", type=Metamodelo_Cpp_CppMemberFunction, multiplicity=Multiplicity(0, 9999))
    }
)
cppConstructor31: BinaryAssociation = BinaryAssociation(
    name="cppConstructor31",
    ends={
        Property(name="Metamodelo_Cpp_CppMemberFunction33", type=Metamodelo_Cpp_CppClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppClassifier32", type=Metamodelo_Cpp_CppMemberFunction, multiplicity=Multiplicity(0, 9999))
    }
)
cppAttributes34: BinaryAssociation = BinaryAssociation(
    name="cppAttributes34",
    ends={
        Property(name="Metamodelo_Cpp_CppVariable", type=Metamodelo_Cpp_CppClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppClassifier35", type=Metamodelo_Cpp_CppVariable, multiplicity=Multiplicity(0, 9999))
    }
)
elements17: BinaryAssociation = BinaryAssociation(
    name="elements17",
    ends={
        Property(name="Metamodelo_Cpp_CppPathReferentiable19", type=Metamodelo_Cpp_CppClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppClassFile18", type=Metamodelo_Cpp_CppPathReferentiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports20: BinaryAssociation = BinaryAssociation(
    name="imports20",
    ends={
        Property(name="Metamodelo_Cpp_CppImportDeclaration", type=Metamodelo_Cpp_CppClassFile, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppClassFile21", type=Metamodelo_Cpp_CppImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usagesInTypeAccess22: BinaryAssociation = BinaryAssociation(
    name="usagesInTypeAccess22",
    ends={
        Property(name="CppTypeAccess", type=Metamodelo_Cpp_CppType, multiplicity=Multiplicity(1, 1)),
        Property(name="access", type=Metamodelo_Cpp_CppTypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
typeParameters23: BinaryAssociation = BinaryAssociation(
    name="typeParameters23",
    ends={
        Property(name="Metamodelo_Cpp_CppTypeParameter", type=Metamodelo_Cpp_CppType, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppType24", type=Metamodelo_Cpp_CppTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bounds25: BinaryAssociation = BinaryAssociation(
    name="bounds25",
    ends={
        Property(name="Metamodelo_Cpp_CppTypeAccess", type=Metamodelo_Cpp_CppTypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppTypeParameter26", type=Metamodelo_Cpp_CppTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cppOperations27: BinaryAssociation = BinaryAssociation(
    name="cppOperations27",
    ends={
        Property(name="Metamodelo_Cpp_CppMemberFunction", type=Metamodelo_Cpp_CppClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppClassifier", type=Metamodelo_Cpp_CppMemberFunction, multiplicity=Multiplicity(0, 9999))
    }
)
literals36: BinaryAssociation = BinaryAssociation(
    name="literals36",
    ends={
        Property(name="Metamodelo_Cpp_CppEnumConstructor", type=Metamodelo_Cpp_CppEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppEnum", type=Metamodelo_Cpp_CppEnumConstructor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression37: BinaryAssociation = BinaryAssociation(
    name="expression37",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression", type=Metamodelo_Cpp_CppEnumConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppEnumConstructor38", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions47: BinaryAssociation = BinaryAssociation(
    name="expressions47",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression48", type=Metamodelo_Cpp_CppArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppArrayInitializer", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
superClass40: BinaryAssociation = BinaryAssociation(
    name="superClass40",
    ends={
        Property(name="Metamodelo_Cpp_CppClass41", type=Metamodelo_Cpp_CppClass, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppClass39", type=Metamodelo_Cpp_CppClass, multiplicity=Multiplicity(0, 9999))
    }
)
pathImport42: BinaryAssociation = BinaryAssociation(
    name="pathImport42",
    ends={
        Property(name="Metamodelo_Cpp_CppClassFile44", type=Metamodelo_Cpp_CppImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppImportDeclaration43", type=Metamodelo_Cpp_CppClassFile, multiplicity=Multiplicity(0, 1))
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="Metamodelo_Cpp_CppTypeAccess46", type=Metamodelo_Cpp_CppTypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppTypedElement", type=Metamodelo_Cpp_CppTypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedParameters49: BinaryAssociation = BinaryAssociation(
    name="ownedParameters49",
    ends={
        Property(name="Metamodelo_Cpp_CppSingleVariableDeclaration", type=Metamodelo_Cpp_CppFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppFunction", type=Metamodelo_Cpp_CppSingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionBody50: BinaryAssociation = BinaryAssociation(
    name="functionBody50",
    ends={
        Property(name="Metamodelo_Cpp_CppBlock", type=Metamodelo_Cpp_CppFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppFunction51", type=Metamodelo_Cpp_CppBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements52: BinaryAssociation = BinaryAssociation(
    name="statements52",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression54", type=Metamodelo_Cpp_CppBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppBlock53", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition62: BinaryAssociation = BinaryAssociation(
    name="condition62",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression63", type=Metamodelo_Cpp_CppSelectionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppSelectionStatement", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement64: BinaryAssociation = BinaryAssociation(
    name="statement64",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression66", type=Metamodelo_Cpp_CppSelectionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppSelectionStatement65", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
theBody67: BinaryAssociation = BinaryAssociation(
    name="theBody67",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression68", type=Metamodelo_Cpp_CppIterationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppIterationStatement", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
method55: BinaryAssociation = BinaryAssociation(
    name="method55",
    ends={
        Property(name="Metamodelo_Cpp_CppMemberFunction56", type=Metamodelo_Cpp_CppAbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppAbstractMethodInvocation", type=Metamodelo_Cpp_CppMemberFunction, multiplicity=Multiplicity(1, 1))
    }
)
arguments57: BinaryAssociation = BinaryAssociation(
    name="arguments57",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression59", type=Metamodelo_Cpp_CppAbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppAbstractMethodInvocation58", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression60: BinaryAssociation = BinaryAssociation(
    name="expression60",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression61", type=Metamodelo_Cpp_CppMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppMethodInvocation", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases76: BinaryAssociation = BinaryAssociation(
    name="cases76",
    ends={
        Property(name="Metamodelo_Cpp_CppCase", type=Metamodelo_Cpp_CppSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppSwitchExpression77", type=Metamodelo_Cpp_CppCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default78: BinaryAssociation = BinaryAssociation(
    name="default78",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression80", type=Metamodelo_Cpp_CppSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppSwitchExpression79", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value81: BinaryAssociation = BinaryAssociation(
    name="value81",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression83", type=Metamodelo_Cpp_CppCase, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppCase82", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition69: BinaryAssociation = BinaryAssociation(
    name="condition69",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression71", type=Metamodelo_Cpp_CppIterationStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppIterationStatement70", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement72: BinaryAssociation = BinaryAssociation(
    name="elseStatement72",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression73", type=Metamodelo_Cpp_CppIfElseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppIfElseStatement", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression74: BinaryAssociation = BinaryAssociation(
    name="expression74",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression75", type=Metamodelo_Cpp_CppSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppSwitchExpression", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label94: BinaryAssociation = BinaryAssociation(
    name="label94",
    ends={
        Property(name="Metamodelo_Cpp_CppLabeledStatement", type=Metamodelo_Cpp_CppGotoStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppGotoStatement", type=Metamodelo_Cpp_CppLabeledStatement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression84: BinaryAssociation = BinaryAssociation(
    name="expression84",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression86", type=Metamodelo_Cpp_CppCase, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppCase85", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initializer87: BinaryAssociation = BinaryAssociation(
    name="initializer87",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression88", type=Metamodelo_Cpp_CppForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppForStatement", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
updater89: BinaryAssociation = BinaryAssociation(
    name="updater89",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression91", type=Metamodelo_Cpp_CppForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppForStatement90", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnExpression92: BinaryAssociation = BinaryAssociation(
    name="returnExpression92",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression93", type=Metamodelo_Cpp_CppReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppReturnStatement", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groups95: BinaryAssociation = BinaryAssociation(
    name="groups95",
    ends={
        Property(name="CppVariableDeclarationGroup", type=Metamodelo_Cpp_CppDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=Metamodelo_Cpp_CppVariableDeclarationGroup, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression103: BinaryAssociation = BinaryAssociation(
    name="expression103",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression104", type=Metamodelo_Cpp_CppParenthizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppParenthizedExpression", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type105: BinaryAssociation = BinaryAssociation(
    name="type105",
    ends={
        Property(name="Metamodelo_Cpp_CppTypeAccess106", type=Metamodelo_Cpp_CppCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppCastExpression", type=Metamodelo_Cpp_CppTypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftOperand96: BinaryAssociation = BinaryAssociation(
    name="leftOperand96",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression97", type=Metamodelo_Cpp_CppBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppBinaryExpression", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightOperand98: BinaryAssociation = BinaryAssociation(
    name="rightOperand98",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression100", type=Metamodelo_Cpp_CppBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppBinaryExpression99", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression101: BinaryAssociation = BinaryAssociation(
    name="expression101",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression102", type=Metamodelo_Cpp_CppUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppUnaryExpression", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression125: BinaryAssociation = BinaryAssociation(
    name="expression125",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression126", type=Metamodelo_Cpp_CppThrowExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppThrowExpression", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field127: BinaryAssociation = BinaryAssociation(
    name="field127",
    ends={
        Property(name="Metamodelo_Cpp_CppVariableAccess", type=Metamodelo_Cpp_CppFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppFieldAccess", type=Metamodelo_Cpp_CppVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression107: BinaryAssociation = BinaryAssociation(
    name="expression107",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression109", type=Metamodelo_Cpp_CppCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppCastExpression108", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index110: BinaryAssociation = BinaryAssociation(
    name="index110",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression111", type=Metamodelo_Cpp_CppArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppArrayAccess", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array112: BinaryAssociation = BinaryAssociation(
    name="array112",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression114", type=Metamodelo_Cpp_CppArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppArrayAccess113", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fieldContainer115: BinaryAssociation = BinaryAssociation(
    name="fieldContainer115",
    ends={
        Property(name="CppFieldContainer", type=Metamodelo_Cpp_CppField, multiplicity=Multiplicity(1, 1)),
        Property(name="cppFields", type=Metamodelo_Cpp_CppFieldContainer, multiplicity=Multiplicity(1, 1))
    }
)
cppFields116: BinaryAssociation = BinaryAssociation(
    name="cppFields116",
    ends={
        Property(name="CppField", type=Metamodelo_Cpp_CppFieldContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="fieldContainer", type=Metamodelo_Cpp_CppField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
theBody117: BinaryAssociation = BinaryAssociation(
    name="theBody117",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression118", type=Metamodelo_Cpp_CppTryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppTryExpression", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catchClause119: BinaryAssociation = BinaryAssociation(
    name="catchClause119",
    ends={
        Property(name="Metamodelo_Cpp_CppCatchClause", type=Metamodelo_Cpp_CppTryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppTryExpression120", type=Metamodelo_Cpp_CppCatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception121: BinaryAssociation = BinaryAssociation(
    name="exception121",
    ends={
        Property(name="CppSingleVariableDeclaration", type=Metamodelo_Cpp_CppCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="catchClause", type=Metamodelo_Cpp_CppSingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
theBody122: BinaryAssociation = BinaryAssociation(
    name="theBody122",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression124", type=Metamodelo_Cpp_CppCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppCatchClause123", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
container143: BinaryAssociation = BinaryAssociation(
    name="container143",
    ends={
        Property(name="CppDeclarationExpression", type=Metamodelo_Cpp_CppVariableDeclarationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=Metamodelo_Cpp_CppDeclarationExpression, multiplicity=Multiplicity(1, 1))
    }
)
fragments144: BinaryAssociation = BinaryAssociation(
    name="fragments144",
    ends={
        Property(name="CppVariableDeclarationFragment", type=Metamodelo_Cpp_CppVariableDeclarationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="variablesContainer", type=Metamodelo_Cpp_CppVariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variablesContainer145: BinaryAssociation = BinaryAssociation(
    name="variablesContainer145",
    ends={
        Property(name="CppVariableDeclarationGroup146", type=Metamodelo_Cpp_CppVariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=Metamodelo_Cpp_CppVariableDeclarationGroup, multiplicity=Multiplicity(0, 1))
    }
)
expression128: BinaryAssociation = BinaryAssociation(
    name="expression128",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression130", type=Metamodelo_Cpp_CppFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppFieldAccess129", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable131: BinaryAssociation = BinaryAssociation(
    name="variable131",
    ends={
        Property(name="CppVariableDeclaration", type=Metamodelo_Cpp_CppVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usageInVariableAccess", type=Metamodelo_Cpp_CppVariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
access132: BinaryAssociation = BinaryAssociation(
    name="access132",
    ends={
        Property(name="CppType", type=Metamodelo_Cpp_CppTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usagesInTypeAccess", type=Metamodelo_Cpp_CppType, multiplicity=Multiplicity(1, 1))
    }
)
parameterMapping134: BinaryAssociation = BinaryAssociation(
    name="parameterMapping134",
    ends={
        Property(name="Metamodelo_Cpp_CppTypeAccess135", type=Metamodelo_Cpp_CppTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppTypeAccess133", type=Metamodelo_Cpp_CppTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usageInVariableAccess136: BinaryAssociation = BinaryAssociation(
    name="usageInVariableAccess136",
    ends={
        Property(name="CppVariableAccess", type=Metamodelo_Cpp_CppVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=Metamodelo_Cpp_CppVariableAccess, multiplicity=Multiplicity(0, 9999))
    }
)
initializer137: BinaryAssociation = BinaryAssociation(
    name="initializer137",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression138", type=Metamodelo_Cpp_CppVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppVariableDeclaration", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dimensions139: BinaryAssociation = BinaryAssociation(
    name="dimensions139",
    ends={
        Property(name="Metamodelo_Cpp_CppExpression141", type=Metamodelo_Cpp_CppVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Metamodelo_Cpp_CppVariableDeclaration140", type=Metamodelo_Cpp_CppExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchClause142: BinaryAssociation = BinaryAssociation(
    name="catchClause142",
    ends={
        Property(name="CppCatchClause", type=Metamodelo_Cpp_CppSingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="exception", type=Metamodelo_Cpp_CppCatchClause, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Metamodelo_Cpp_CppPathReferentiable_CppNamedElement = Generalization(general=CppNamedElement, specific=Metamodelo_Cpp_CppPathReferentiable)
gen_Metamodelo_Cpp_CppPathReference_CppModelElement = Generalization(general=CppModelElement, specific=Metamodelo_Cpp_CppPathReference)
gen_Metamodelo_Cpp_CppNamedElement_CppModelElement = Generalization(general=CppModelElement, specific=Metamodelo_Cpp_CppNamedElement)
gen_Metamodelo_Cpp_CppPackage_CppPathReferentiable = Generalization(general=CppPathReferentiable, specific=Metamodelo_Cpp_CppPackage)
gen_Metamodelo_Cpp_CppClassFile_CppPathReferentiable = Generalization(general=CppPathReferentiable, specific=Metamodelo_Cpp_CppClassFile)
gen_Metamodelo_Cpp_CppType_CppPathReferentiable = Generalization(general=CppPathReferentiable, specific=Metamodelo_Cpp_CppType)
gen_Metamodelo_Cpp_CppTypeParameter_CppType = Generalization(general=CppType, specific=Metamodelo_Cpp_CppTypeParameter)
gen_Metamodelo_Cpp_CppClassifier_CppType = Generalization(general=CppType, specific=Metamodelo_Cpp_CppClassifier)
gen_Metamodelo_Cpp_CppClassifier_CppFieldContainer = Generalization(general=CppFieldContainer, specific=Metamodelo_Cpp_CppClassifier)
gen_Metamodelo_Cpp_CppCharType_CppPrimitiveType = Generalization(general=CppPrimitiveType, specific=Metamodelo_Cpp_CppCharType)
gen_Metamodelo_Cpp_CppShortType_CppPrimitiveType = Generalization(general=CppPrimitiveType, specific=Metamodelo_Cpp_CppShortType)
gen_Metamodelo_Cpp_CppIntType_CppPrimitiveType = Generalization(general=CppPrimitiveType, specific=Metamodelo_Cpp_CppIntType)
gen_Metamodelo_Cpp_CppLongType_CppPrimitiveType = Generalization(general=CppPrimitiveType, specific=Metamodelo_Cpp_CppLongType)
gen_Metamodelo_Cpp_CppFloatType_CppPrimitiveType = Generalization(general=CppPrimitiveType, specific=Metamodelo_Cpp_CppFloatType)
gen_Metamodelo_Cpp_CppDoubleType_CppPrimitiveType = Generalization(general=CppPrimitiveType, specific=Metamodelo_Cpp_CppDoubleType)
gen_Metamodelo_Cpp_CppSignedType_CppPrimitiveType = Generalization(general=CppPrimitiveType, specific=Metamodelo_Cpp_CppSignedType)
gen_Metamodelo_Cpp_CppUnsignedType_CppPrimitiveType = Generalization(general=CppPrimitiveType, specific=Metamodelo_Cpp_CppUnsignedType)
gen_Metamodelo_Cpp_CppEnum_CppType = Generalization(general=CppType, specific=Metamodelo_Cpp_CppEnum)
gen_Metamodelo_Cpp_CppEnumConstructor_CppNamedElement = Generalization(general=CppNamedElement, specific=Metamodelo_Cpp_CppEnumConstructor)
gen_Metamodelo_Cpp_CppComment_CppModelElement = Generalization(general=CppModelElement, specific=Metamodelo_Cpp_CppComment)
gen_Metamodelo_Cpp_CppPrimitiveType_CppType = Generalization(general=CppType, specific=Metamodelo_Cpp_CppPrimitiveType)
gen_Metamodelo_Cpp_CppBooleanType_CppPrimitiveType = Generalization(general=CppPrimitiveType, specific=Metamodelo_Cpp_CppBooleanType)
gen_Metamodelo_Cpp_CppVoidType_CppPrimitiveType = Generalization(general=CppPrimitiveType, specific=Metamodelo_Cpp_CppVoidType)
gen_Metamodelo_Cpp_CppArrayInitializer_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppArrayInitializer)
gen_Metamodelo_Cpp_CppClass_CppClassifier = Generalization(general=CppClassifier, specific=Metamodelo_Cpp_CppClass)
gen_Metamodelo_Cpp_CppImportDeclaration_CppModelElement = Generalization(general=CppModelElement, specific=Metamodelo_Cpp_CppImportDeclaration)
gen_Metamodelo_Cpp_CppTypedElement_CppModelElement = Generalization(general=CppModelElement, specific=Metamodelo_Cpp_CppTypedElement)
gen_Metamodelo_Cpp_CppExpression_CppModelElement = Generalization(general=CppModelElement, specific=Metamodelo_Cpp_CppExpression)
gen_Metamodelo_Cpp_CppVariable_CppVariableDeclaration = Generalization(general=CppVariableDeclaration, specific=Metamodelo_Cpp_CppVariable)
gen_Metamodelo_Cpp_CppVariable_CppField = Generalization(general=CppField, specific=Metamodelo_Cpp_CppVariable)
gen_Metamodelo_Cpp_CppDestructor_CppMemberFunction = Generalization(general=CppMemberFunction, specific=Metamodelo_Cpp_CppDestructor)
gen_Metamodelo_Cpp_CppVariable_CppTypedElement = Generalization(general=CppTypedElement, specific=Metamodelo_Cpp_CppVariable)
gen_Metamodelo_Cpp_CppVariable_CppType = Generalization(general=CppType, specific=Metamodelo_Cpp_CppVariable)
gen_Metamodelo_Cpp_CppMethod_CppMemberFunction = Generalization(general=CppMemberFunction, specific=Metamodelo_Cpp_CppMethod)
gen_Metamodelo_Cpp_CppMethod_CppTypedElement = Generalization(general=CppTypedElement, specific=Metamodelo_Cpp_CppMethod)
gen_Metamodelo_Cpp_CppFunction_CppModelElement = Generalization(general=CppModelElement, specific=Metamodelo_Cpp_CppFunction)
gen_Metamodelo_Cpp_CppFunction_CppType = Generalization(general=CppType, specific=Metamodelo_Cpp_CppFunction)
gen_Metamodelo_Cpp_CppBlock_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppBlock)
gen_Metamodelo_Cpp_CppMemberFunction_CppFunction = Generalization(general=CppFunction, specific=Metamodelo_Cpp_CppMemberFunction)
gen_Metamodelo_Cpp_CppMemberFunction_CppField = Generalization(general=CppField, specific=Metamodelo_Cpp_CppMemberFunction)
gen_Metamodelo_Cpp_CppConstructor_CppMemberFunction = Generalization(general=CppMemberFunction, specific=Metamodelo_Cpp_CppConstructor)
gen_Metamodelo_Cpp_CppIterationStatement_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppIterationStatement)
gen_Metamodelo_Cpp_CppAbstractMethodInvocation_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppAbstractMethodInvocation)
gen_Metamodelo_Cpp_CppMethodInvocation_CppAbstractMethodInvocation = Generalization(general=CppAbstractMethodInvocation, specific=Metamodelo_Cpp_CppMethodInvocation)
gen_Metamodelo_Cpp_CppSuperMethodInvocation_CppAbstractMethodInvocation = Generalization(general=CppAbstractMethodInvocation, specific=Metamodelo_Cpp_CppSuperMethodInvocation)
gen_Metamodelo_Cpp_CppSuperConstructorInvocation_CppMethodInvocation = Generalization(general=CppMethodInvocation, specific=Metamodelo_Cpp_CppSuperConstructorInvocation)
gen_Metamodelo_Cpp_CppLabeledStatement_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppLabeledStatement)
gen_Metamodelo_Cpp_CppLabeledStatement_CppNamedElement = Generalization(general=CppNamedElement, specific=Metamodelo_Cpp_CppLabeledStatement)
gen_Metamodelo_Cpp_CppSelectionStatement_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppSelectionStatement)
gen_Metamodelo_Cpp_CppCase_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppCase)
gen_Metamodelo_Cpp_CppJumpStatement_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppJumpStatement)
gen_Metamodelo_Cpp_CppIfStatement_CppSelectionStatement = Generalization(general=CppSelectionStatement, specific=Metamodelo_Cpp_CppIfStatement)
gen_Metamodelo_Cpp_CppIfElseStatement_CppSelectionStatement = Generalization(general=CppSelectionStatement, specific=Metamodelo_Cpp_CppIfElseStatement)
gen_Metamodelo_Cpp_CppSwitchExpression_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppSwitchExpression)
gen_Metamodelo_Cpp_CppGotoStatement_CppJumpStatement = Generalization(general=CppJumpStatement, specific=Metamodelo_Cpp_CppGotoStatement)
gen_Metamodelo_Cpp_CppContinueStatement_CppJumpStatement = Generalization(general=CppJumpStatement, specific=Metamodelo_Cpp_CppContinueStatement)
gen_Metamodelo_Cpp_CppAssignamentStatement_CppBinaryExpression = Generalization(general=CppBinaryExpression, specific=Metamodelo_Cpp_CppAssignamentStatement)
gen_Metamodelo_Cpp_CppWhileStatement_CppIterationStatement = Generalization(general=CppIterationStatement, specific=Metamodelo_Cpp_CppWhileStatement)
gen_Metamodelo_Cpp_CppDoWhileStatement_CppIterationStatement = Generalization(general=CppIterationStatement, specific=Metamodelo_Cpp_CppDoWhileStatement)
gen_Metamodelo_Cpp_CppForStatement_CppIterationStatement = Generalization(general=CppIterationStatement, specific=Metamodelo_Cpp_CppForStatement)
gen_Metamodelo_Cpp_CppBreakStatement_CppJumpStatement = Generalization(general=CppJumpStatement, specific=Metamodelo_Cpp_CppBreakStatement)
gen_Metamodelo_Cpp_CppReturnStatement_CppJumpStatement = Generalization(general=CppJumpStatement, specific=Metamodelo_Cpp_CppReturnStatement)
gen_Metamodelo_Cpp_CppDeclarationExpression_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppDeclarationExpression)
gen_Metamodelo_Cpp_CppNullLiteral_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppNullLiteral)
gen_Metamodelo_Cpp_CppBooleanLiteral_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppBooleanLiteral)
gen_Metamodelo_Cpp_CppCharacterLiteral_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppCharacterLiteral)
gen_Metamodelo_Cpp_CppNumberLiteral_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppNumberLiteral)
gen_Metamodelo_Cpp_CppStringLiteral_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppStringLiteral)
gen_Metamodelo_Cpp_CppRegexLiteral_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppRegexLiteral)
gen_Metamodelo_Cpp_CppParenthizedExpression_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppParenthizedExpression)
gen_Metamodelo_Cpp_CppCastExpression_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppCastExpression)
gen_Metamodelo_Cpp_CppBinaryExpression_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppBinaryExpression)
gen_Metamodelo_Cpp_CppInfixExpression_CppBinaryExpression = Generalization(general=CppBinaryExpression, specific=Metamodelo_Cpp_CppInfixExpression)
gen_Metamodelo_Cpp_CppUnaryExpression_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppUnaryExpression)
gen_Metamodelo_Cpp_CppPostfixExpression_CppUnaryExpression = Generalization(general=CppUnaryExpression, specific=Metamodelo_Cpp_CppPostfixExpression)
gen_Metamodelo_Cpp_CppPrefixExpression_CppUnaryExpression = Generalization(general=CppUnaryExpression, specific=Metamodelo_Cpp_CppPrefixExpression)
gen_Metamodelo_Cpp_CppThrowExpression_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppThrowExpression)
gen_Metamodelo_Cpp_CppThisExpression_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppThisExpression)
gen_Metamodelo_Cpp_CppFieldAccess_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppFieldAccess)
gen_Metamodelo_Cpp_CppConstantExpression_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppConstantExpression)
gen_Metamodelo_Cpp_CppConstantExpression_CppNamedElement = Generalization(general=CppNamedElement, specific=Metamodelo_Cpp_CppConstantExpression)
gen_Metamodelo_Cpp_CppArrayAccess_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppArrayAccess)
gen_Metamodelo_Cpp_CppField_CppNamedElement = Generalization(general=CppNamedElement, specific=Metamodelo_Cpp_CppField)
gen_Metamodelo_Cpp_CppFieldContainer_CppModelElement = Generalization(general=CppModelElement, specific=Metamodelo_Cpp_CppFieldContainer)
gen_Metamodelo_Cpp_CppTryExpression_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppTryExpression)
gen_Metamodelo_Cpp_CppCatchClause_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppCatchClause)
gen_Metamodelo_Cpp_CppVariableDeclarationFragment_CppVariableDeclaration = Generalization(general=CppVariableDeclaration, specific=Metamodelo_Cpp_CppVariableDeclarationFragment)
gen_Metamodelo_Cpp_CppVariableAccess_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppVariableAccess)
gen_Metamodelo_Cpp_CppTypeAccess_CppExpression = Generalization(general=CppExpression, specific=Metamodelo_Cpp_CppTypeAccess)
gen_Metamodelo_Cpp_CppVariableDeclaration_CppNamedElement = Generalization(general=CppNamedElement, specific=Metamodelo_Cpp_CppVariableDeclaration)
gen_Metamodelo_Cpp_CppSingleVariableDeclaration_CppVariableDeclaration = Generalization(general=CppVariableDeclaration, specific=Metamodelo_Cpp_CppSingleVariableDeclaration)
gen_Metamodelo_Cpp_CppSingleVariableDeclaration_CppTypedElement = Generalization(general=CppTypedElement, specific=Metamodelo_Cpp_CppSingleVariableDeclaration)
gen_Metamodelo_Cpp_CppVariableDeclarationGroup_CppTypedElement = Generalization(general=CppTypedElement, specific=Metamodelo_Cpp_CppVariableDeclarationGroup)

# Domain Model
domain_model = DomainModel(
    name="Metamodelo_Cpp",
    types={CppNamedElement, Metamodelo_Cpp_CppPackage, Metamodelo_Cpp_CppPathReference, CppModelElement, CppPathReferentiable, Metamodelo_Cpp_CppModel, Metamodelo_Cpp_CppClass, Metamodelo_Cpp_CppPathReferentiable, Metamodelo_Cpp_CppType, Metamodelo_Cpp_CppClassFile, Metamodelo_Cpp_CppModelElement, Metamodelo_Cpp_CppNamedElement, Metamodelo_Cpp_CppVariable, Metamodelo_Cpp_CppImportDeclaration, Metamodelo_Cpp_CppTypeAccess, Metamodelo_Cpp_CppTypeParameter, CppType, Metamodelo_Cpp_CppClassifier, CppFieldContainer, Metamodelo_Cpp_CppMemberFunction, Metamodelo_Cpp_CppShortType, Metamodelo_Cpp_CppIntType, Metamodelo_Cpp_CppLongType, Metamodelo_Cpp_CppFloatType, Metamodelo_Cpp_CppDoubleType, Metamodelo_Cpp_CppSignedType, Metamodelo_Cpp_CppUnsignedType, CppClassifier, Metamodelo_Cpp_CppEnum, Metamodelo_Cpp_CppEnumConstructor, Metamodelo_Cpp_CppExpression, Metamodelo_Cpp_CppComment, Metamodelo_Cpp_CppPrimitiveType, Metamodelo_Cpp_CppBooleanType, CppPrimitiveType, Metamodelo_Cpp_CppVoidType, Metamodelo_Cpp_CppCharType, Metamodelo_Cpp_CppArrayInitializer, CppExpression, Metamodelo_Cpp_CppTypedElement, CppVariableDeclaration, Metamodelo_Cpp_CppDestructor, CppField, CppTypedElement, Metamodelo_Cpp_CppMethod, Metamodelo_Cpp_CppFunction, Metamodelo_Cpp_CppSingleVariableDeclaration, Metamodelo_Cpp_CppBlock, CppFunction, Metamodelo_Cpp_CppConstructor, CppMemberFunction, Metamodelo_Cpp_CppIterationStatement, Metamodelo_Cpp_CppAbstractMethodInvocation, Metamodelo_Cpp_CppMethodInvocation, CppAbstractMethodInvocation, Metamodelo_Cpp_CppSuperMethodInvocation, Metamodelo_Cpp_CppSuperConstructorInvocation, CppMethodInvocation, Metamodelo_Cpp_CppLabeledStatement, Metamodelo_Cpp_CppSelectionStatement, Metamodelo_Cpp_CppJumpStatement, Metamodelo_Cpp_CppIfStatement, CppSelectionStatement, Metamodelo_Cpp_CppIfElseStatement, Metamodelo_Cpp_CppSwitchExpression, Metamodelo_Cpp_CppCase, Metamodelo_Cpp_CppGotoStatement, Metamodelo_Cpp_CppContinueStatement, Metamodelo_Cpp_CppAssignamentStatement, CppBinaryExpression, Metamodelo_Cpp_CppWhileStatement, CppIterationStatement, Metamodelo_Cpp_CppDoWhileStatement, Metamodelo_Cpp_CppForStatement, Metamodelo_Cpp_CppBreakStatement, CppJumpStatement, Metamodelo_Cpp_CppReturnStatement, Metamodelo_Cpp_CppDeclarationExpression, Metamodelo_Cpp_CppVariableDeclarationGroup, Metamodelo_Cpp_CppNullLiteral, Metamodelo_Cpp_CppBooleanLiteral, Metamodelo_Cpp_CppCharacterLiteral, Metamodelo_Cpp_CppNumberLiteral, Metamodelo_Cpp_CppStringLiteral, Metamodelo_Cpp_CppRegexLiteral, Metamodelo_Cpp_CppParenthizedExpression, Metamodelo_Cpp_CppCastExpression, Metamodelo_Cpp_CppBinaryExpression, Metamodelo_Cpp_CppInfixExpression, Metamodelo_Cpp_CppUnaryExpression, Metamodelo_Cpp_CppPostfixExpression, CppUnaryExpression, Metamodelo_Cpp_CppPrefixExpression, Metamodelo_Cpp_CppThrowExpression, Metamodelo_Cpp_CppThisExpression, Metamodelo_Cpp_CppFieldAccess, Metamodelo_Cpp_CppVariableAccess, Metamodelo_Cpp_CppConstantExpression, Metamodelo_Cpp_CppArrayAccess, Metamodelo_Cpp_CppField, Metamodelo_Cpp_CppFieldContainer, Metamodelo_Cpp_CppTryExpression, Metamodelo_Cpp_CppCatchClause, Metamodelo_Cpp_CppVariableDeclarationFragment, Metamodelo_Cpp_CppVariableDeclaration, CppQualifierType, CppOperator, CppVarType, CppAccessSpecifier, CppClassKey, CppLinkageSpecifier, CppStorageType, CppUnaryOperator, CppAssignmentOperator, CppPostfixOperator},
    associations={parentReference7, referencedIn8, referencedTerminal9, mainClass0, elements1, orphanTypes3, modules5, childrenReferences10, childrenPackages13, containedTypes14, cppDestructor28, cppConstructor31, cppAttributes34, elements17, imports20, usagesInTypeAccess22, typeParameters23, bounds25, cppOperations27, literals36, expression37, expressions47, superClass40, pathImport42, type45, ownedParameters49, functionBody50, statements52, condition62, statement64, theBody67, method55, arguments57, expression60, cases76, default78, value81, condition69, elseStatement72, expression74, label94, expression84, initializer87, updater89, returnExpression92, groups95, expression103, type105, leftOperand96, rightOperand98, expression101, expression125, field127, expression107, index110, array112, fieldContainer115, cppFields116, theBody117, catchClause119, exception121, theBody122, container143, fragments144, variablesContainer145, expression128, variable131, access132, parameterMapping134, usageInVariableAccess136, initializer137, dimensions139, catchClause142},
    generalizations={gen_Metamodelo_Cpp_CppPathReferentiable_CppNamedElement, gen_Metamodelo_Cpp_CppPathReference_CppModelElement, gen_Metamodelo_Cpp_CppNamedElement_CppModelElement, gen_Metamodelo_Cpp_CppPackage_CppPathReferentiable, gen_Metamodelo_Cpp_CppClassFile_CppPathReferentiable, gen_Metamodelo_Cpp_CppType_CppPathReferentiable, gen_Metamodelo_Cpp_CppTypeParameter_CppType, gen_Metamodelo_Cpp_CppClassifier_CppType, gen_Metamodelo_Cpp_CppClassifier_CppFieldContainer, gen_Metamodelo_Cpp_CppCharType_CppPrimitiveType, gen_Metamodelo_Cpp_CppShortType_CppPrimitiveType, gen_Metamodelo_Cpp_CppIntType_CppPrimitiveType, gen_Metamodelo_Cpp_CppLongType_CppPrimitiveType, gen_Metamodelo_Cpp_CppFloatType_CppPrimitiveType, gen_Metamodelo_Cpp_CppDoubleType_CppPrimitiveType, gen_Metamodelo_Cpp_CppSignedType_CppPrimitiveType, gen_Metamodelo_Cpp_CppUnsignedType_CppPrimitiveType, gen_Metamodelo_Cpp_CppEnum_CppType, gen_Metamodelo_Cpp_CppEnumConstructor_CppNamedElement, gen_Metamodelo_Cpp_CppComment_CppModelElement, gen_Metamodelo_Cpp_CppPrimitiveType_CppType, gen_Metamodelo_Cpp_CppBooleanType_CppPrimitiveType, gen_Metamodelo_Cpp_CppVoidType_CppPrimitiveType, gen_Metamodelo_Cpp_CppArrayInitializer_CppExpression, gen_Metamodelo_Cpp_CppClass_CppClassifier, gen_Metamodelo_Cpp_CppImportDeclaration_CppModelElement, gen_Metamodelo_Cpp_CppTypedElement_CppModelElement, gen_Metamodelo_Cpp_CppExpression_CppModelElement, gen_Metamodelo_Cpp_CppVariable_CppVariableDeclaration, gen_Metamodelo_Cpp_CppVariable_CppField, gen_Metamodelo_Cpp_CppDestructor_CppMemberFunction, gen_Metamodelo_Cpp_CppVariable_CppTypedElement, gen_Metamodelo_Cpp_CppVariable_CppType, gen_Metamodelo_Cpp_CppMethod_CppMemberFunction, gen_Metamodelo_Cpp_CppMethod_CppTypedElement, gen_Metamodelo_Cpp_CppFunction_CppModelElement, gen_Metamodelo_Cpp_CppFunction_CppType, gen_Metamodelo_Cpp_CppBlock_CppExpression, gen_Metamodelo_Cpp_CppMemberFunction_CppFunction, gen_Metamodelo_Cpp_CppMemberFunction_CppField, gen_Metamodelo_Cpp_CppConstructor_CppMemberFunction, gen_Metamodelo_Cpp_CppIterationStatement_CppExpression, gen_Metamodelo_Cpp_CppAbstractMethodInvocation_CppExpression, gen_Metamodelo_Cpp_CppMethodInvocation_CppAbstractMethodInvocation, gen_Metamodelo_Cpp_CppSuperMethodInvocation_CppAbstractMethodInvocation, gen_Metamodelo_Cpp_CppSuperConstructorInvocation_CppMethodInvocation, gen_Metamodelo_Cpp_CppLabeledStatement_CppExpression, gen_Metamodelo_Cpp_CppLabeledStatement_CppNamedElement, gen_Metamodelo_Cpp_CppSelectionStatement_CppExpression, gen_Metamodelo_Cpp_CppCase_CppExpression, gen_Metamodelo_Cpp_CppJumpStatement_CppExpression, gen_Metamodelo_Cpp_CppIfStatement_CppSelectionStatement, gen_Metamodelo_Cpp_CppIfElseStatement_CppSelectionStatement, gen_Metamodelo_Cpp_CppSwitchExpression_CppExpression, gen_Metamodelo_Cpp_CppGotoStatement_CppJumpStatement, gen_Metamodelo_Cpp_CppContinueStatement_CppJumpStatement, gen_Metamodelo_Cpp_CppAssignamentStatement_CppBinaryExpression, gen_Metamodelo_Cpp_CppWhileStatement_CppIterationStatement, gen_Metamodelo_Cpp_CppDoWhileStatement_CppIterationStatement, gen_Metamodelo_Cpp_CppForStatement_CppIterationStatement, gen_Metamodelo_Cpp_CppBreakStatement_CppJumpStatement, gen_Metamodelo_Cpp_CppReturnStatement_CppJumpStatement, gen_Metamodelo_Cpp_CppDeclarationExpression_CppExpression, gen_Metamodelo_Cpp_CppNullLiteral_CppExpression, gen_Metamodelo_Cpp_CppBooleanLiteral_CppExpression, gen_Metamodelo_Cpp_CppCharacterLiteral_CppExpression, gen_Metamodelo_Cpp_CppNumberLiteral_CppExpression, gen_Metamodelo_Cpp_CppStringLiteral_CppExpression, gen_Metamodelo_Cpp_CppRegexLiteral_CppExpression, gen_Metamodelo_Cpp_CppParenthizedExpression_CppExpression, gen_Metamodelo_Cpp_CppCastExpression_CppExpression, gen_Metamodelo_Cpp_CppBinaryExpression_CppExpression, gen_Metamodelo_Cpp_CppInfixExpression_CppBinaryExpression, gen_Metamodelo_Cpp_CppUnaryExpression_CppExpression, gen_Metamodelo_Cpp_CppPostfixExpression_CppUnaryExpression, gen_Metamodelo_Cpp_CppPrefixExpression_CppUnaryExpression, gen_Metamodelo_Cpp_CppThrowExpression_CppExpression, gen_Metamodelo_Cpp_CppThisExpression_CppExpression, gen_Metamodelo_Cpp_CppFieldAccess_CppExpression, gen_Metamodelo_Cpp_CppConstantExpression_CppExpression, gen_Metamodelo_Cpp_CppConstantExpression_CppNamedElement, gen_Metamodelo_Cpp_CppArrayAccess_CppExpression, gen_Metamodelo_Cpp_CppField_CppNamedElement, gen_Metamodelo_Cpp_CppFieldContainer_CppModelElement, gen_Metamodelo_Cpp_CppTryExpression_CppExpression, gen_Metamodelo_Cpp_CppCatchClause_CppExpression, gen_Metamodelo_Cpp_CppVariableDeclarationFragment_CppVariableDeclaration, gen_Metamodelo_Cpp_CppVariableAccess_CppExpression, gen_Metamodelo_Cpp_CppTypeAccess_CppExpression, gen_Metamodelo_Cpp_CppVariableDeclaration_CppNamedElement, gen_Metamodelo_Cpp_CppSingleVariableDeclaration_CppVariableDeclaration, gen_Metamodelo_Cpp_CppSingleVariableDeclaration_CppTypedElement, gen_Metamodelo_Cpp_CppVariableDeclarationGroup_CppTypedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)