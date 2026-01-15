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
HaxeTarget: Enumeration = Enumeration(
    name="HaxeTarget",
    literals={
            EnumerationLiteral(name="neko"),
			EnumerationLiteral(name="cpp"),
			EnumerationLiteral(name="java"),
			EnumerationLiteral(name="flash"),
			EnumerationLiteral(name="cs"),
			EnumerationLiteral(name="js")
    }
)

HaxeAttributeProperty: Enumeration = Enumeration(
    name="HaxeAttributeProperty",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="method"),
			EnumerationLiteral(name="null"),
			EnumerationLiteral(name="dynamic")
    }
)

HaxePrefixOperators: Enumeration = Enumeration(
    name="HaxePrefixOperators",
    literals={
            EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="INCREMENT"),
			EnumerationLiteral(name="DECREMENT"),
			EnumerationLiteral(name="ONECOMPLEMENT")
    }
)

HaxeAssignmentOperator: Enumeration = Enumeration(
    name="HaxeAssignmentOperator",
    literals={
            EnumerationLiteral(name="ASSIGN"),
			EnumerationLiteral(name="PLUS_ASSIGN"),
			EnumerationLiteral(name="MINUS_ASSIGN"),
			EnumerationLiteral(name="DIVISION_ASSIGN"),
			EnumerationLiteral(name="TIMES_ASSIGN"),
			EnumerationLiteral(name="SHIFT_LEFT_ASSIGN"),
			EnumerationLiteral(name="SHIFT_RIGTH_ASSIGN"),
			EnumerationLiteral(name="SHIFT_ARITH_ASSIGN"),
			EnumerationLiteral(name="BITWISE_OR_ASSIGN"),
			EnumerationLiteral(name="BITWISE_AND_ASSIGN"),
			EnumerationLiteral(name="XOR_ASSIGN"),
			EnumerationLiteral(name="REMAINDER_ASSIGN")
    }
)

HaxeInfixOperators: Enumeration = Enumeration(
    name="HaxeInfixOperators",
    literals={
            EnumerationLiteral(name="PLUS"),
			EnumerationLiteral(name="TIMES"),
			EnumerationLiteral(name="MINUS"),
			EnumerationLiteral(name="DIVISION"),
			EnumerationLiteral(name="REMAINDER"),
			EnumerationLiteral(name="SHIFT_RIGTH"),
			EnumerationLiteral(name="SHIFT_LEFT"),
			EnumerationLiteral(name="SHIFT_ARITH"),
			EnumerationLiteral(name="LESS_THAN"),
			EnumerationLiteral(name="GREATER_THAN"),
			EnumerationLiteral(name="LESS_EQUALS"),
			EnumerationLiteral(name="GREATER_EQUALS"),
			EnumerationLiteral(name="BITWISE_OR"),
			EnumerationLiteral(name="BITWISE_AND"),
			EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="NEQ"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="RANGE")
    }
)

# Classes
haxe_HaxeClass = Class(name="haxe::HaxeClass")
haxe_HaxePathReferentiable = Class(name="haxe::HaxePathReferentiable", is_abstract=True)
haxe_HaxeModule = Class(name="haxe::HaxeModule")
haxe_HaxeModelElement = Class(name="haxe::HaxeModelElement", is_abstract=True)
haxe_HaxeModel = Class(name="haxe::HaxeModel")
haxe_HaxeHaxedocComment = Class(name="haxe::HaxeHaxedocComment")
HaxeComment = Class(name="HaxeComment")
haxe_HaxeASTNode = Class(name="haxe::HaxeASTNode", is_abstract=True)
HaxeModelElement = Class(name="HaxeModelElement")
haxe_HaxeComment = Class(name="haxe::HaxeComment")
haxe_HaxeNamedElement = Class(name="haxe::HaxeNamedElement", is_abstract=True)
HaxeASTNode = Class(name="HaxeASTNode")
haxe_HaxeTagElement = Class(name="haxe::HaxeTagElement")
haxe_HaxeTextElement = Class(name="haxe::HaxeTextElement")
haxe_HaxeFieldContainer = Class(name="haxe::HaxeFieldContainer", is_abstract=True)
haxe_HaxeField = Class(name="haxe::HaxeField", is_abstract=True)
haxe_HaxeExpression = Class(name="haxe::HaxeExpression", is_abstract=True)
haxe_HaxeLoopStatement = Class(name="haxe::HaxeLoopStatement", is_abstract=True)
HaxeExpression = Class(name="HaxeExpression")
HaxeNamedElement = Class(name="HaxeNamedElement")
haxe_HaxePackage = Class(name="haxe::HaxePackage")
haxe_HaxePathReference = Class(name="haxe::HaxePathReference", is_abstract=True)
haxe_HaxeBlock = Class(name="haxe::HaxeBlock")
haxe_HaxeConditionalExpression = Class(name="haxe::HaxeConditionalExpression", is_abstract=True)
haxe_HaxeUnaryExpression = Class(name="haxe::HaxeUnaryExpression", is_abstract=True)
haxe_HaxeBinaryExpression = Class(name="haxe::HaxeBinaryExpression", is_abstract=True)
haxe_HaxeForStatement = Class(name="haxe::HaxeForStatement")
HaxeLoopStatement = Class(name="HaxeLoopStatement")
haxe_HaxeSingleVariableDeclaration = Class(name="haxe::HaxeSingleVariableDeclaration")
haxe_HaxeWhileStatement = Class(name="haxe::HaxeWhileStatement")
haxe_HaxeInExpression = Class(name="haxe::HaxeInExpression")
haxe_HaxeIfStatement = Class(name="haxe::HaxeIfStatement")
HaxeConditionalExpression = Class(name="HaxeConditionalExpression")
haxe_HaxeTernaryExpression = Class(name="haxe::HaxeTernaryExpression")
haxe_HaxePostfixExpression = Class(name="haxe::HaxePostfixExpression")
haxe_HaxeReturn = Class(name="haxe::HaxeReturn")
HaxeExpressionStatement = Class(name="HaxeExpressionStatement")
haxe_HaxeBreak = Class(name="haxe::HaxeBreak")
haxe_HaxeContinue = Class(name="haxe::HaxeContinue")
haxe_HaxeThisExpression = Class(name="haxe::HaxeThisExpression")
haxe_HaxeDoWhileStatement = Class(name="haxe::HaxeDoWhileStatement")
haxe_HaxePrefixExpression = Class(name="haxe::HaxePrefixExpression")
HaxeUnaryExpression = Class(name="HaxeUnaryExpression")
haxe_HaxeInfixExpression = Class(name="haxe::HaxeInfixExpression")
HaxeBinaryExpression = Class(name="HaxeBinaryExpression")
haxe_HaxeNumberLiteral = Class(name="haxe::HaxeNumberLiteral")
haxe_HaxeIdentifierLiteral = Class(name="haxe::HaxeIdentifierLiteral")
haxe_HaxeRegexLiteral = Class(name="haxe::HaxeRegexLiteral")
haxe_HaxeFieldAccess = Class(name="haxe::HaxeFieldAccess")
haxe_HaxeEmptyStatement = Class(name="haxe::HaxeEmptyStatement")
haxe_HaxeConstant = Class(name="haxe::HaxeConstant", is_abstract=True)
haxe_HaxeStringLiteral = Class(name="haxe::HaxeStringLiteral")
HaxeConstant = Class(name="HaxeConstant")
haxe_HaxeNullLiteral = Class(name="haxe::HaxeNullLiteral")
haxe_HaxeBooleanLiteral = Class(name="haxe::HaxeBooleanLiteral")
haxe_HaxeArrayCreation = Class(name="haxe::HaxeArrayCreation")
haxe_HaxeTypeAccess = Class(name="haxe::HaxeTypeAccess", is_abstract=True)
haxe_HaxeArrayAccess = Class(name="haxe::HaxeArrayAccess")
haxe_HaxeSingleVariableAccess = Class(name="haxe::HaxeSingleVariableAccess")
haxe_HaxeParenthizedExpression = Class(name="haxe::HaxeParenthizedExpression")
haxe_HaxeArrayInitializer = Class(name="haxe::HaxeArrayInitializer")
haxe_HaxeFunctionExpression = Class(name="haxe::HaxeFunctionExpression")
HaxeAbstractFunction = Class(name="HaxeAbstractFunction")
haxe_HaxeCallExpression = Class(name="haxe::HaxeCallExpression")
haxe_HaxeSwitch = Class(name="haxe::HaxeSwitch")
haxe_HaxeCase = Class(name="haxe::HaxeCase")
HaxeTypedElement = Class(name="HaxeTypedElement")
haxe_HaxeTryExpression = Class(name="haxe::HaxeTryExpression")
haxe_HaxeCatchClause = Class(name="haxe::HaxeCatchClause")
haxe_HaxeObjectDeclaration = Class(name="haxe::HaxeObjectDeclaration")
haxe_HaxeFieldDeclaration = Class(name="haxe::HaxeFieldDeclaration")
haxe_HaxeCastingExpression = Class(name="haxe::HaxeCastingExpression")
haxe_HaxeUnsafeCastExpression = Class(name="haxe::HaxeUnsafeCastExpression")
haxe_HaxeTypeCheckExpression = Class(name="haxe::HaxeTypeCheckExpression")
haxe_HaxeThrowExpression = Class(name="haxe::HaxeThrowExpression")
haxe_HaxeExpressionStatement = Class(name="haxe::HaxeExpressionStatement")
haxe_HaxeSuperConstructorInvocation = Class(name="haxe::HaxeSuperConstructorInvocation")
HaxeMethodInvocation = Class(name="HaxeMethodInvocation")
haxe_HaxeVariableDeclaration = Class(name="haxe::HaxeVariableDeclaration", is_abstract=True)
haxe_HaxePackageAccess = Class(name="haxe::HaxePackageAccess")
HaxePathReference = Class(name="HaxePathReference")
haxe_HaxeAssignment = Class(name="haxe::HaxeAssignment")
haxe_HaxeSuperMethodInvocation = Class(name="haxe::HaxeSuperMethodInvocation")
HaxeAbstractMethodInvocation = Class(name="HaxeAbstractMethodInvocation")
haxe_HaxeMethodInvocation = Class(name="haxe::HaxeMethodInvocation")
haxe_HaxeVariableDeclarationGroup = Class(name="haxe::HaxeVariableDeclarationGroup")
haxe_HaxeVariableDeclarationExpression = Class(name="haxe::HaxeVariableDeclarationExpression")
haxe_HaxeAbstractMethodInvocation = Class(name="haxe::HaxeAbstractMethodInvocation", is_abstract=True)
haxe_HaxeAbstractOperation = Class(name="haxe::HaxeAbstractOperation", is_abstract=True)
HaxePathReferentiable = Class(name="HaxePathReferentiable")
haxe_HaxeVariableDeclarationFragment = Class(name="haxe::HaxeVariableDeclarationFragment")
HaxeVariableDeclaration = Class(name="HaxeVariableDeclaration")
haxe_HaxeDependencyDeclaration = Class(name="haxe::HaxeDependencyDeclaration", is_abstract=True)
haxe_HaxeType = Class(name="haxe::HaxeType", is_abstract=True)
HaxeMetadataContainer = Class(name="HaxeMetadataContainer")
haxe_HaxeOperation = Class(name="haxe::HaxeOperation")
haxe_HaxeAttribute = Class(name="haxe::HaxeAttribute")
haxe_HaxeConstructor = Class(name="haxe::HaxeConstructor")
haxe_HaxeTypeParameter = Class(name="haxe::HaxeTypeParameter")
haxe_HaxeClassifier = Class(name="haxe::HaxeClassifier", is_abstract=True)
HaxeType = Class(name="HaxeType")
HaxeFieldContainer = Class(name="HaxeFieldContainer")
haxe_HaxeClassifierAccess = Class(name="haxe::HaxeClassifierAccess")
haxe_HaxeTypedElement = Class(name="haxe::HaxeTypedElement", is_abstract=True)
HaxeClassifier = Class(name="HaxeClassifier")
haxe_HaxeFunctionTypeAccess = Class(name="haxe::HaxeFunctionTypeAccess")
HaxeTypeAccess = Class(name="HaxeTypeAccess")
haxe_HaxeAbstract = Class(name="haxe::HaxeAbstract")
haxe_HaxeEnum = Class(name="haxe::HaxeEnum")
HaxeField = Class(name="HaxeField")
HaxeSingleVariableDeclaration = Class(name="HaxeSingleVariableDeclaration")
haxe_HaxeEnumConstructor = Class(name="haxe::HaxeEnumConstructor")
haxe_HaxeTypedef = Class(name="haxe::HaxeTypedef")
HaxeAbstractOperation = Class(name="HaxeAbstractOperation")
haxe_HaxeAbstractFunction = Class(name="haxe::HaxeAbstractFunction", is_abstract=True)
haxe_HaxeImportDeclaration = Class(name="haxe::HaxeImportDeclaration")
HaxeDependencyDeclaration = Class(name="HaxeDependencyDeclaration")
haxe_HaxeUsingDeclaration = Class(name="haxe::HaxeUsingDeclaration")
haxe_HaxeMetadata = Class(name="haxe::HaxeMetadata")
haxe_HaxeMetadataContainer = Class(name="haxe::HaxeMetadataContainer", is_abstract=True)

# haxe_HaxeClass class attributes and methods
haxe_HaxeClass_isInterface: Property = Property(name="isInterface", type=BooleanType)
haxe_HaxeClass.attributes={haxe_HaxeClass_isInterface}

# haxe_HaxePathReferentiable class attributes and methods

# haxe_HaxeModule class attributes and methods

# haxe_HaxeModelElement class attributes and methods

# haxe_HaxeModel class attributes and methods
haxe_HaxeModel_target: Property = Property(name="target", type=StringType)
haxe_HaxeModel_name: Property = Property(name="name", type=StringType)
haxe_HaxeModel_sourceFolder: Property = Property(name="sourceFolder", type=StringType)
haxe_HaxeModel_targetFolder: Property = Property(name="targetFolder", type=StringType)
haxe_HaxeModel.attributes={haxe_HaxeModel_sourceFolder, haxe_HaxeModel_target, haxe_HaxeModel_targetFolder, haxe_HaxeModel_name}

# haxe_HaxeHaxedocComment class attributes and methods

# HaxeComment class attributes and methods

# haxe_HaxeASTNode class attributes and methods

# HaxeModelElement class attributes and methods

# haxe_HaxeComment class attributes and methods
haxe_HaxeComment_enclosedByParent: Property = Property(name="enclosedByParent", type=BooleanType)
haxe_HaxeComment_prefixOfParent: Property = Property(name="prefixOfParent", type=BooleanType)
haxe_HaxeComment_content: Property = Property(name="content", type=StringType)
haxe_HaxeComment_lineComment: Property = Property(name="lineComment", type=BooleanType)
haxe_HaxeComment.attributes={haxe_HaxeComment_content, haxe_HaxeComment_lineComment, haxe_HaxeComment_enclosedByParent, haxe_HaxeComment_prefixOfParent}

# haxe_HaxeNamedElement class attributes and methods
haxe_HaxeNamedElement_name: Property = Property(name="name", type=StringType)
haxe_HaxeNamedElement.attributes={haxe_HaxeNamedElement_name}

# HaxeASTNode class attributes and methods

# haxe_HaxeTagElement class attributes and methods
haxe_HaxeTagElement_tagName: Property = Property(name="tagName", type=StringType)
haxe_HaxeTagElement.attributes={haxe_HaxeTagElement_tagName}

# haxe_HaxeTextElement class attributes and methods
haxe_HaxeTextElement_text: Property = Property(name="text", type=StringType)
haxe_HaxeTextElement.attributes={haxe_HaxeTextElement_text}

# haxe_HaxeFieldContainer class attributes and methods

# haxe_HaxeField class attributes and methods
haxe_HaxeField_isStatic: Property = Property(name="isStatic", type=BooleanType)
haxe_HaxeField_isPrivate: Property = Property(name="isPrivate", type=BooleanType)
haxe_HaxeField.attributes={haxe_HaxeField_isPrivate, haxe_HaxeField_isStatic}

# haxe_HaxeExpression class attributes and methods

# haxe_HaxeLoopStatement class attributes and methods

# HaxeExpression class attributes and methods

# HaxeNamedElement class attributes and methods

# haxe_HaxePackage class attributes and methods

# haxe_HaxePathReference class attributes and methods

# haxe_HaxeBlock class attributes and methods
haxe_HaxeBlock_m_isEmpty: Method = Method(name="isEmpty", parameters={}, type=BooleanType)
haxe_HaxeBlock.methods={haxe_HaxeBlock_m_isEmpty}

# haxe_HaxeConditionalExpression class attributes and methods

# haxe_HaxeUnaryExpression class attributes and methods

# haxe_HaxeBinaryExpression class attributes and methods

# haxe_HaxeForStatement class attributes and methods

# HaxeLoopStatement class attributes and methods

# haxe_HaxeSingleVariableDeclaration class attributes and methods
haxe_HaxeSingleVariableDeclaration_isOptional: Property = Property(name="isOptional", type=BooleanType)
haxe_HaxeSingleVariableDeclaration.attributes={haxe_HaxeSingleVariableDeclaration_isOptional}

# haxe_HaxeWhileStatement class attributes and methods

# haxe_HaxeInExpression class attributes and methods

# haxe_HaxeIfStatement class attributes and methods

# HaxeConditionalExpression class attributes and methods

# haxe_HaxeTernaryExpression class attributes and methods

# haxe_HaxePostfixExpression class attributes and methods
haxe_HaxePostfixExpression_isIncrement: Property = Property(name="isIncrement", type=BooleanType)
haxe_HaxePostfixExpression.attributes={haxe_HaxePostfixExpression_isIncrement}

# haxe_HaxeReturn class attributes and methods

# HaxeExpressionStatement class attributes and methods

# haxe_HaxeBreak class attributes and methods

# haxe_HaxeContinue class attributes and methods

# haxe_HaxeThisExpression class attributes and methods

# haxe_HaxeDoWhileStatement class attributes and methods

# haxe_HaxePrefixExpression class attributes and methods
haxe_HaxePrefixExpression_operator: Property = Property(name="operator", type=StringType)
haxe_HaxePrefixExpression.attributes={haxe_HaxePrefixExpression_operator}

# HaxeUnaryExpression class attributes and methods

# haxe_HaxeInfixExpression class attributes and methods
haxe_HaxeInfixExpression_operator: Property = Property(name="operator", type=StringType)
haxe_HaxeInfixExpression.attributes={haxe_HaxeInfixExpression_operator}

# HaxeBinaryExpression class attributes and methods

# haxe_HaxeNumberLiteral class attributes and methods
haxe_HaxeNumberLiteral_value: Property = Property(name="value", type=StringType)
haxe_HaxeNumberLiteral.attributes={haxe_HaxeNumberLiteral_value}

# haxe_HaxeIdentifierLiteral class attributes and methods
haxe_HaxeIdentifierLiteral_value: Property = Property(name="value", type=StringType)
haxe_HaxeIdentifierLiteral.attributes={haxe_HaxeIdentifierLiteral_value}

# haxe_HaxeRegexLiteral class attributes and methods
haxe_HaxeRegexLiteral_pattern: Property = Property(name="pattern", type=StringType)
haxe_HaxeRegexLiteral_options: Property = Property(name="options", type=StringType)
haxe_HaxeRegexLiteral.attributes={haxe_HaxeRegexLiteral_pattern, haxe_HaxeRegexLiteral_options}

# haxe_HaxeFieldAccess class attributes and methods

# haxe_HaxeEmptyStatement class attributes and methods

# haxe_HaxeConstant class attributes and methods

# haxe_HaxeStringLiteral class attributes and methods
haxe_HaxeStringLiteral_escapedValue: Property = Property(name="escapedValue", type=StringType)
haxe_HaxeStringLiteral.attributes={haxe_HaxeStringLiteral_escapedValue}

# HaxeConstant class attributes and methods

# haxe_HaxeNullLiteral class attributes and methods

# haxe_HaxeBooleanLiteral class attributes and methods
haxe_HaxeBooleanLiteral_value: Property = Property(name="value", type=BooleanType)
haxe_HaxeBooleanLiteral.attributes={haxe_HaxeBooleanLiteral_value}

# haxe_HaxeArrayCreation class attributes and methods

# haxe_HaxeTypeAccess class attributes and methods

# haxe_HaxeArrayAccess class attributes and methods

# haxe_HaxeSingleVariableAccess class attributes and methods

# haxe_HaxeParenthizedExpression class attributes and methods

# haxe_HaxeArrayInitializer class attributes and methods

# haxe_HaxeFunctionExpression class attributes and methods

# HaxeAbstractFunction class attributes and methods

# haxe_HaxeCallExpression class attributes and methods

# haxe_HaxeSwitch class attributes and methods

# haxe_HaxeCase class attributes and methods

# HaxeTypedElement class attributes and methods

# haxe_HaxeTryExpression class attributes and methods

# haxe_HaxeCatchClause class attributes and methods

# haxe_HaxeObjectDeclaration class attributes and methods

# haxe_HaxeFieldDeclaration class attributes and methods

# haxe_HaxeCastingExpression class attributes and methods

# haxe_HaxeUnsafeCastExpression class attributes and methods

# haxe_HaxeTypeCheckExpression class attributes and methods

# haxe_HaxeThrowExpression class attributes and methods

# haxe_HaxeExpressionStatement class attributes and methods

# haxe_HaxeSuperConstructorInvocation class attributes and methods

# HaxeMethodInvocation class attributes and methods

# haxe_HaxeVariableDeclaration class attributes and methods

# haxe_HaxePackageAccess class attributes and methods

# HaxePathReference class attributes and methods

# haxe_HaxeAssignment class attributes and methods
haxe_HaxeAssignment_operator: Property = Property(name="operator", type=StringType)
haxe_HaxeAssignment.attributes={haxe_HaxeAssignment_operator}

# haxe_HaxeSuperMethodInvocation class attributes and methods

# HaxeAbstractMethodInvocation class attributes and methods

# haxe_HaxeMethodInvocation class attributes and methods

# haxe_HaxeVariableDeclarationGroup class attributes and methods

# haxe_HaxeVariableDeclarationExpression class attributes and methods

# haxe_HaxeAbstractMethodInvocation class attributes and methods

# haxe_HaxeAbstractOperation class attributes and methods
haxe_HaxeAbstractOperation_isInline: Property = Property(name="isInline", type=BooleanType)
haxe_HaxeAbstractOperation_overrides: Property = Property(name="overrides", type=BooleanType)
haxe_HaxeAbstractOperation.attributes={haxe_HaxeAbstractOperation_overrides, haxe_HaxeAbstractOperation_isInline}

# HaxePathReferentiable class attributes and methods

# haxe_HaxeVariableDeclarationFragment class attributes and methods

# HaxeVariableDeclaration class attributes and methods

# haxe_HaxeDependencyDeclaration class attributes and methods

# haxe_HaxeType class attributes and methods
haxe_HaxeType_private: Property = Property(name="private", type=BooleanType)
haxe_HaxeType_extern: Property = Property(name="extern", type=BooleanType)
haxe_HaxeType.attributes={haxe_HaxeType_private, haxe_HaxeType_extern}

# HaxeMetadataContainer class attributes and methods

# haxe_HaxeOperation class attributes and methods
haxe_HaxeOperation_macro: Property = Property(name="macro", type=BooleanType)
haxe_HaxeOperation.attributes={haxe_HaxeOperation_macro}

# haxe_HaxeAttribute class attributes and methods
haxe_HaxeAttribute_getterProperty: Property = Property(name="getterProperty", type=StringType)
haxe_HaxeAttribute_setterProperty: Property = Property(name="setterProperty", type=StringType)
haxe_HaxeAttribute.attributes={haxe_HaxeAttribute_setterProperty, haxe_HaxeAttribute_getterProperty}

# haxe_HaxeConstructor class attributes and methods

# haxe_HaxeTypeParameter class attributes and methods

# haxe_HaxeClassifier class attributes and methods

# HaxeType class attributes and methods

# HaxeFieldContainer class attributes and methods

# haxe_HaxeClassifierAccess class attributes and methods

# haxe_HaxeTypedElement class attributes and methods

# HaxeClassifier class attributes and methods

# haxe_HaxeFunctionTypeAccess class attributes and methods

# HaxeTypeAccess class attributes and methods

# haxe_HaxeAbstract class attributes and methods

# haxe_HaxeEnum class attributes and methods

# HaxeField class attributes and methods

# HaxeSingleVariableDeclaration class attributes and methods

# haxe_HaxeEnumConstructor class attributes and methods

# haxe_HaxeTypedef class attributes and methods

# HaxeAbstractOperation class attributes and methods

# haxe_HaxeAbstractFunction class attributes and methods

# haxe_HaxeImportDeclaration class attributes and methods

# HaxeDependencyDeclaration class attributes and methods

# haxe_HaxeUsingDeclaration class attributes and methods

# haxe_HaxeMetadata class attributes and methods
haxe_HaxeMetadata_compilerMetadata: Property = Property(name="compilerMetadata", type=BooleanType)
haxe_HaxeMetadata.attributes={haxe_HaxeMetadata_compilerMetadata}

# haxe_HaxeMetadataContainer class attributes and methods

# Relationships
mainClass0: BinaryAssociation = BinaryAssociation(
    name="mainClass0",
    ends={
        Property(name="haxe_HaxeClass", type=haxe_HaxeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeModel", type=haxe_HaxeClass, multiplicity=Multiplicity(1, 1))
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="haxe_HaxePathReferentiable", type=haxe_HaxeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeModel2", type=haxe_HaxePathReferentiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenced3: BinaryAssociation = BinaryAssociation(
    name="referenced3",
    ends={
        Property(name="haxe_HaxePathReferentiable5", type=haxe_HaxeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeModel4", type=haxe_HaxePathReferentiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
haxeModules6: BinaryAssociation = BinaryAssociation(
    name="haxeModules6",
    ends={
        Property(name="haxe_HaxeModule", type=haxe_HaxeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeModel7", type=haxe_HaxeModule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments8: BinaryAssociation = BinaryAssociation(
    name="comments8",
    ends={
        Property(name="haxe_HaxeComment", type=haxe_HaxeASTNode, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeASTNode", type=haxe_HaxeComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags9: BinaryAssociation = BinaryAssociation(
    name="tags9",
    ends={
        Property(name="haxe_HaxeTagElement", type=haxe_HaxeHaxedocComment, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeHaxedocComment", type=haxe_HaxeTagElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fragments10: BinaryAssociation = BinaryAssociation(
    name="fragments10",
    ends={
        Property(name="haxe_HaxeASTNode12", type=haxe_HaxeTagElement, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeTagElement11", type=haxe_HaxeASTNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedTerminal15: BinaryAssociation = BinaryAssociation(
    name="referencedTerminal15",
    ends={
        Property(name="HaxePathReferentiable", type=haxe_HaxePathReference, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedIn", type=haxe_HaxePathReferentiable, multiplicity=Multiplicity(0, 1))
    }
)
haxeFields16: BinaryAssociation = BinaryAssociation(
    name="haxeFields16",
    ends={
        Property(name="HaxeField", type=haxe_HaxeFieldContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="fieldContainer", type=haxe_HaxeField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
theBody17: BinaryAssociation = BinaryAssociation(
    name="theBody17",
    ends={
        Property(name="haxe_HaxeExpression", type=haxe_HaxeLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeLoopStatement", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parentReference13: BinaryAssociation = BinaryAssociation(
    name="parentReference13",
    ends={
        Property(name="HaxePackage", type=haxe_HaxePathReferentiable, multiplicity=Multiplicity(1, 1)),
        Property(name="childrenReferences", type=haxe_HaxePackage, multiplicity=Multiplicity(0, 1))
    }
)
referencedIn14: BinaryAssociation = BinaryAssociation(
    name="referencedIn14",
    ends={
        Property(name="HaxePathReference", type=haxe_HaxePathReferentiable, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedTerminal", type=haxe_HaxePathReference, multiplicity=Multiplicity(0, 9999))
    }
)
rightSide25: BinaryAssociation = BinaryAssociation(
    name="rightSide25",
    ends={
        Property(name="haxe_HaxeExpression27", type=haxe_HaxeBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeBinaryExpression26", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements28: BinaryAssociation = BinaryAssociation(
    name="statements28",
    ends={
        Property(name="haxe_HaxeExpression29", type=haxe_HaxeBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeBlock", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression30: BinaryAssociation = BinaryAssociation(
    name="expression30",
    ends={
        Property(name="haxe_HaxeExpression31", type=haxe_HaxeConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeConditionalExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression18: BinaryAssociation = BinaryAssociation(
    name="expression18",
    ends={
        Property(name="haxe_HaxeExpression20", type=haxe_HaxeLoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeLoopStatement19", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand21: BinaryAssociation = BinaryAssociation(
    name="operand21",
    ends={
        Property(name="haxe_HaxeExpression22", type=haxe_HaxeUnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeUnaryExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftSide23: BinaryAssociation = BinaryAssociation(
    name="leftSide23",
    ends={
        Property(name="haxe_HaxeExpression24", type=haxe_HaxeBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeBinaryExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression37: BinaryAssociation = BinaryAssociation(
    name="elseExpression37",
    ends={
        Property(name="haxe_HaxeExpression38", type=haxe_HaxeTernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeTernaryExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter39: BinaryAssociation = BinaryAssociation(
    name="parameter39",
    ends={
        Property(name="haxe_HaxeSingleVariableDeclaration", type=haxe_HaxeForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeForStatement", type=haxe_HaxeSingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatement32: BinaryAssociation = BinaryAssociation(
    name="thenStatement32",
    ends={
        Property(name="haxe_HaxeExpression34", type=haxe_HaxeConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeConditionalExpression33", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement35: BinaryAssociation = BinaryAssociation(
    name="elseStatement35",
    ends={
        Property(name="haxe_HaxeExpression36", type=haxe_HaxeIfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeIfStatement", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedSide45: BinaryAssociation = BinaryAssociation(
    name="extendedSide45",
    ends={
        Property(name="haxe_HaxeExpression46", type=haxe_HaxeInfixExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeInfixExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable40: BinaryAssociation = BinaryAssociation(
    name="variable40",
    ends={
        Property(name="haxe_HaxeSingleVariableDeclaration41", type=haxe_HaxeInExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeInExpression", type=haxe_HaxeSingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression42: BinaryAssociation = BinaryAssociation(
    name="expression42",
    ends={
        Property(name="haxe_HaxeExpression44", type=haxe_HaxeInExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeInExpression43", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dimensions55: BinaryAssociation = BinaryAssociation(
    name="dimensions55",
    ends={
        Property(name="haxe_HaxeExpression56", type=haxe_HaxeArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeArrayCreation", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer57: BinaryAssociation = BinaryAssociation(
    name="initializer57",
    ends={
        Property(name="haxe_HaxeArrayInitializer59", type=haxe_HaxeArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeArrayCreation58", type=haxe_HaxeArrayInitializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type60: BinaryAssociation = BinaryAssociation(
    name="type60",
    ends={
        Property(name="haxe_HaxeTypeAccess", type=haxe_HaxeArrayCreation, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeArrayCreation61", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array62: BinaryAssociation = BinaryAssociation(
    name="array62",
    ends={
        Property(name="haxe_HaxeExpression63", type=haxe_HaxeArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeArrayAccess", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
field47: BinaryAssociation = BinaryAssociation(
    name="field47",
    ends={
        Property(name="haxe_HaxeSingleVariableAccess", type=haxe_HaxeFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeFieldAccess", type=haxe_HaxeSingleVariableAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression48: BinaryAssociation = BinaryAssociation(
    name="expression48",
    ends={
        Property(name="haxe_HaxeExpression50", type=haxe_HaxeFieldAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeFieldAccess49", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression51: BinaryAssociation = BinaryAssociation(
    name="expression51",
    ends={
        Property(name="haxe_HaxeExpression52", type=haxe_HaxeParenthizedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeParenthizedExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions53: BinaryAssociation = BinaryAssociation(
    name="expressions53",
    ends={
        Property(name="haxe_HaxeExpression54", type=haxe_HaxeArrayInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeArrayInitializer", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
values74: BinaryAssociation = BinaryAssociation(
    name="values74",
    ends={
        Property(name="haxe_HaxeExpression76", type=haxe_HaxeCase, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeCase75", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression77: BinaryAssociation = BinaryAssociation(
    name="expression77",
    ends={
        Property(name="haxe_HaxeExpression79", type=haxe_HaxeCase, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeCase78", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression80: BinaryAssociation = BinaryAssociation(
    name="expression80",
    ends={
        Property(name="haxe_HaxeExpression81", type=haxe_HaxeCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeCallExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index64: BinaryAssociation = BinaryAssociation(
    name="index64",
    ends={
        Property(name="haxe_HaxeExpression66", type=haxe_HaxeArrayAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeArrayAccess65", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression67: BinaryAssociation = BinaryAssociation(
    name="expression67",
    ends={
        Property(name="haxe_HaxeExpression68", type=haxe_HaxeSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeSwitch", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cases69: BinaryAssociation = BinaryAssociation(
    name="cases69",
    ends={
        Property(name="haxe_HaxeCase", type=haxe_HaxeSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeSwitch70", type=haxe_HaxeCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default71: BinaryAssociation = BinaryAssociation(
    name="default71",
    ends={
        Property(name="haxe_HaxeExpression73", type=haxe_HaxeSwitch, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeSwitch72", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value89: BinaryAssociation = BinaryAssociation(
    name="value89",
    ends={
        Property(name="haxe_HaxeExpression91", type=haxe_HaxeFieldDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeFieldDeclaration90", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
theBody92: BinaryAssociation = BinaryAssociation(
    name="theBody92",
    ends={
        Property(name="haxe_HaxeExpression93", type=haxe_HaxeTryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeTryExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
catchClauses94: BinaryAssociation = BinaryAssociation(
    name="catchClauses94",
    ends={
        Property(name="haxe_HaxeCatchClause", type=haxe_HaxeTryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeTryExpression95", type=haxe_HaxeCatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception96: BinaryAssociation = BinaryAssociation(
    name="exception96",
    ends={
        Property(name="HaxeSingleVariableDeclaration", type=haxe_HaxeCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="catchClause", type=haxe_HaxeSingleVariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments82: BinaryAssociation = BinaryAssociation(
    name="arguments82",
    ends={
        Property(name="haxe_HaxeExpression84", type=haxe_HaxeCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeCallExpression83", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendsType85: BinaryAssociation = BinaryAssociation(
    name="extendsType85",
    ends={
        Property(name="haxe_HaxeTypeAccess86", type=haxe_HaxeObjectDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeObjectDeclaration", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields87: BinaryAssociation = BinaryAssociation(
    name="fields87",
    ends={
        Property(name="haxe_HaxeFieldDeclaration", type=haxe_HaxeObjectDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeObjectDeclaration88", type=haxe_HaxeFieldDeclaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression102: BinaryAssociation = BinaryAssociation(
    name="expression102",
    ends={
        Property(name="haxe_HaxeExpression103", type=haxe_HaxeCastingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeCastingExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type104: BinaryAssociation = BinaryAssociation(
    name="type104",
    ends={
        Property(name="haxe_HaxeTypeAccess106", type=haxe_HaxeCastingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeCastingExpression105", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression107: BinaryAssociation = BinaryAssociation(
    name="expression107",
    ends={
        Property(name="haxe_HaxeExpression108", type=haxe_HaxeUnsafeCastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeUnsafeCastExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
theBody97: BinaryAssociation = BinaryAssociation(
    name="theBody97",
    ends={
        Property(name="haxe_HaxeExpression99", type=haxe_HaxeCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeCatchClause98", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression100: BinaryAssociation = BinaryAssociation(
    name="expression100",
    ends={
        Property(name="haxe_HaxeExpression101", type=haxe_HaxeExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeExpressionStatement", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifier116: BinaryAssociation = BinaryAssociation(
    name="qualifier116",
    ends={
        Property(name="haxe_HaxeExpression118", type=haxe_HaxeSingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeSingleVariableAccess117", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable119: BinaryAssociation = BinaryAssociation(
    name="variable119",
    ends={
        Property(name="HaxeVariableDeclaration", type=haxe_HaxeSingleVariableAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="usageInVariableAccess", type=haxe_HaxeVariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
qualifier121: BinaryAssociation = BinaryAssociation(
    name="qualifier121",
    ends={
        Property(name="haxe_HaxePackageAccess", type=haxe_HaxePackageAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxePackageAccess120", type=haxe_HaxePackageAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression109: BinaryAssociation = BinaryAssociation(
    name="expression109",
    ends={
        Property(name="haxe_HaxeExpression110", type=haxe_HaxeTypeCheckExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeTypeCheckExpression", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type111: BinaryAssociation = BinaryAssociation(
    name="type111",
    ends={
        Property(name="haxe_HaxeTypeAccess113", type=haxe_HaxeTypeCheckExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeTypeCheckExpression112", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression114: BinaryAssociation = BinaryAssociation(
    name="expression114",
    ends={
        Property(name="haxe_HaxeExpression115", type=haxe_HaxeMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeMethodInvocation", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usageInVariableAccess129: BinaryAssociation = BinaryAssociation(
    name="usageInVariableAccess129",
    ends={
        Property(name="HaxeSingleVariableAccess", type=haxe_HaxeVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=haxe_HaxeSingleVariableAccess, multiplicity=Multiplicity(0, 9999))
    }
)
initializer130: BinaryAssociation = BinaryAssociation(
    name="initializer130",
    ends={
        Property(name="haxe_HaxeExpression131", type=haxe_HaxeVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeVariableDeclaration", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
container132: BinaryAssociation = BinaryAssociation(
    name="container132",
    ends={
        Property(name="HaxeVariableDeclarationExpression", type=haxe_HaxeVariableDeclarationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="groups", type=haxe_HaxeVariableDeclarationExpression, multiplicity=Multiplicity(1, 1))
    }
)
method122: BinaryAssociation = BinaryAssociation(
    name="method122",
    ends={
        Property(name="haxe_HaxeAbstractOperation", type=haxe_HaxeAbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeAbstractMethodInvocation", type=haxe_HaxeAbstractOperation, multiplicity=Multiplicity(1, 1))
    }
)
arguments123: BinaryAssociation = BinaryAssociation(
    name="arguments123",
    ends={
        Property(name="haxe_HaxeExpression125", type=haxe_HaxeAbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeAbstractMethodInvocation124", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments126: BinaryAssociation = BinaryAssociation(
    name="typeArguments126",
    ends={
        Property(name="haxe_HaxeTypeAccess128", type=haxe_HaxeAbstractMethodInvocation, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeAbstractMethodInvocation127", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups137: BinaryAssociation = BinaryAssociation(
    name="groups137",
    ends={
        Property(name="HaxeVariableDeclarationGroup138", type=haxe_HaxeVariableDeclarationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=haxe_HaxeVariableDeclarationGroup, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
catchClause139: BinaryAssociation = BinaryAssociation(
    name="catchClause139",
    ends={
        Property(name="HaxeCatchClause", type=haxe_HaxeSingleVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="exception", type=haxe_HaxeCatchClause, multiplicity=Multiplicity(0, 1))
    }
)
childrenReferences140: BinaryAssociation = BinaryAssociation(
    name="childrenReferences140",
    ends={
        Property(name="HaxePathReferentiable141", type=haxe_HaxePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="parentReference", type=haxe_HaxePathReferentiable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer133: BinaryAssociation = BinaryAssociation(
    name="initializer133",
    ends={
        Property(name="haxe_HaxeExpression134", type=haxe_HaxeVariableDeclarationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeVariableDeclarationGroup", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fragments135: BinaryAssociation = BinaryAssociation(
    name="fragments135",
    ends={
        Property(name="HaxeVariableDeclarationFragment", type=haxe_HaxeVariableDeclarationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="variablesContainer", type=haxe_HaxeVariableDeclarationFragment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variablesContainer136: BinaryAssociation = BinaryAssociation(
    name="variablesContainer136",
    ends={
        Property(name="HaxeVariableDeclarationGroup", type=haxe_HaxeVariableDeclarationFragment, multiplicity=Multiplicity(1, 1)),
        Property(name="fragments", type=haxe_HaxeVariableDeclarationGroup, multiplicity=Multiplicity(0, 1))
    }
)
commentList146: BinaryAssociation = BinaryAssociation(
    name="commentList146",
    ends={
        Property(name="haxe_HaxeComment148", type=haxe_HaxeModule, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeModule147", type=haxe_HaxeComment, multiplicity=Multiplicity(0, 9999))
    }
)
dependencies149: BinaryAssociation = BinaryAssociation(
    name="dependencies149",
    ends={
        Property(name="haxe_HaxeDependencyDeclaration", type=haxe_HaxeModule, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeModule150", type=haxe_HaxeDependencyDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thePackage151: BinaryAssociation = BinaryAssociation(
    name="thePackage151",
    ends={
        Property(name="haxe_HaxePackage153", type=haxe_HaxeModule, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeModule152", type=haxe_HaxePackage, multiplicity=Multiplicity(0, 1))
    }
)
theElements154: BinaryAssociation = BinaryAssociation(
    name="theElements154",
    ends={
        Property(name="HaxeType", type=haxe_HaxeModule, multiplicity=Multiplicity(1, 1)),
        Property(name="containerModule", type=haxe_HaxeType, multiplicity=Multiplicity(0, 9999))
    }
)
childrenPackages143: BinaryAssociation = BinaryAssociation(
    name="childrenPackages143",
    ends={
        Property(name="haxe_HaxePackage", type=haxe_HaxePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxePackage142", type=haxe_HaxePackage, multiplicity=Multiplicity(0, 9999))
    }
)
containedTypes144: BinaryAssociation = BinaryAssociation(
    name="containedTypes144",
    ends={
        Property(name="haxe_HaxeType", type=haxe_HaxePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxePackage145", type=haxe_HaxeType, multiplicity=Multiplicity(0, 9999))
    }
)
containerPackage164: BinaryAssociation = BinaryAssociation(
    name="containerPackage164",
    ends={
        Property(name="haxe_HaxePackage165", type=haxe_HaxeClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeClassifier", type=haxe_HaxePackage, multiplicity=Multiplicity(0, 1))
    }
)
haxeOperations166: BinaryAssociation = BinaryAssociation(
    name="haxeOperations166",
    ends={
        Property(name="haxe_HaxeOperation", type=haxe_HaxeClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeClassifier167", type=haxe_HaxeOperation, multiplicity=Multiplicity(0, 9999))
    }
)
haxeAttribute168: BinaryAssociation = BinaryAssociation(
    name="haxeAttribute168",
    ends={
        Property(name="haxe_HaxeAttribute", type=haxe_HaxeClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeClassifier169", type=haxe_HaxeAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
containerModule155: BinaryAssociation = BinaryAssociation(
    name="containerModule155",
    ends={
        Property(name="HaxeModule", type=haxe_HaxeType, multiplicity=Multiplicity(1, 1)),
        Property(name="theElements", type=haxe_HaxeModule, multiplicity=Multiplicity(0, 1))
    }
)
commentsAfterDeclaration156: BinaryAssociation = BinaryAssociation(
    name="commentsAfterDeclaration156",
    ends={
        Property(name="haxe_HaxeComment158", type=haxe_HaxeType, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeType157", type=haxe_HaxeComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commentsBeforeDeclaration159: BinaryAssociation = BinaryAssociation(
    name="commentsBeforeDeclaration159",
    ends={
        Property(name="haxe_HaxeComment161", type=haxe_HaxeType, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeType160", type=haxe_HaxeComment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters162: BinaryAssociation = BinaryAssociation(
    name="typeParameters162",
    ends={
        Property(name="haxe_HaxeTypeParameter", type=haxe_HaxeType, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeType163", type=haxe_HaxeTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argumentTypes177: BinaryAssociation = BinaryAssociation(
    name="argumentTypes177",
    ends={
        Property(name="haxe_HaxeTypeAccess179", type=haxe_HaxeFunctionTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeFunctionTypeAccess178", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(0, 9999))
    }
)
parameterMapping180: BinaryAssociation = BinaryAssociation(
    name="parameterMapping180",
    ends={
        Property(name="haxe_HaxeTypeAccess181", type=haxe_HaxeClassifierAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeClassifierAccess", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type182: BinaryAssociation = BinaryAssociation(
    name="type182",
    ends={
        Property(name="haxe_HaxeTypeAccess183", type=haxe_HaxeTypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeTypedElement", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
haxeConstructors170: BinaryAssociation = BinaryAssociation(
    name="haxeConstructors170",
    ends={
        Property(name="haxe_HaxeConstructor", type=haxe_HaxeClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeClassifier171", type=haxe_HaxeConstructor, multiplicity=Multiplicity(0, 9999))
    }
)
bounds172: BinaryAssociation = BinaryAssociation(
    name="bounds172",
    ends={
        Property(name="haxe_HaxeTypeAccess174", type=haxe_HaxeTypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeTypeParameter173", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType175: BinaryAssociation = BinaryAssociation(
    name="returnType175",
    ends={
        Property(name="haxe_HaxeTypeAccess176", type=haxe_HaxeFunctionTypeAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeFunctionTypeAccess", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(1, 1))
    }
)
underlyingType190: BinaryAssociation = BinaryAssociation(
    name="underlyingType190",
    ends={
        Property(name="haxe_HaxeTypeAccess191", type=haxe_HaxeAbstract, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeAbstract", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
directCastingFromType192: BinaryAssociation = BinaryAssociation(
    name="directCastingFromType192",
    ends={
        Property(name="haxe_HaxeTypeAccess194", type=haxe_HaxeAbstract, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeAbstract193", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
directCastingToType195: BinaryAssociation = BinaryAssociation(
    name="directCastingToType195",
    ends={
        Property(name="haxe_HaxeTypeAccess197", type=haxe_HaxeAbstract, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeAbstract196", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generalization184: BinaryAssociation = BinaryAssociation(
    name="generalization184",
    ends={
        Property(name="haxe_HaxeClassifierAccess186", type=haxe_HaxeClass, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeClass185", type=haxe_HaxeClassifierAccess, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementation187: BinaryAssociation = BinaryAssociation(
    name="implementation187",
    ends={
        Property(name="haxe_HaxeClassifierAccess189", type=haxe_HaxeClass, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeClass188", type=haxe_HaxeClassifierAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldContainer201: BinaryAssociation = BinaryAssociation(
    name="fieldContainer201",
    ends={
        Property(name="HaxeFieldContainer", type=haxe_HaxeField, multiplicity=Multiplicity(1, 1)),
        Property(name="haxeFields", type=haxe_HaxeFieldContainer, multiplicity=Multiplicity(1, 1))
    }
)
getter202: BinaryAssociation = BinaryAssociation(
    name="getter202",
    ends={
        Property(name="haxe_HaxeOperation204", type=haxe_HaxeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeAttribute203", type=haxe_HaxeOperation, multiplicity=Multiplicity(0, 1))
    }
)
setter205: BinaryAssociation = BinaryAssociation(
    name="setter205",
    ends={
        Property(name="haxe_HaxeOperation207", type=haxe_HaxeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeAttribute206", type=haxe_HaxeOperation, multiplicity=Multiplicity(0, 1))
    }
)
literals198: BinaryAssociation = BinaryAssociation(
    name="literals198",
    ends={
        Property(name="haxe_HaxeEnumConstructor", type=haxe_HaxeEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeEnum", type=haxe_HaxeEnumConstructor, multiplicity=Multiplicity(0, 9999))
    }
)
refType199: BinaryAssociation = BinaryAssociation(
    name="refType199",
    ends={
        Property(name="haxe_HaxeTypeAccess200", type=haxe_HaxeTypedef, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeTypedef", type=haxe_HaxeTypeAccess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeParameters210: BinaryAssociation = BinaryAssociation(
    name="typeParameters210",
    ends={
        Property(name="haxe_HaxeAbstractFunction211", type=haxe_HaxeTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="haxe_HaxeTypeParameter212", type=haxe_HaxeAbstractFunction, multiplicity=Multiplicity(1, 1))
    }
)
theBody213: BinaryAssociation = BinaryAssociation(
    name="theBody213",
    ends={
        Property(name="haxe_HaxeExpression215", type=haxe_HaxeAbstractFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeAbstractFunction214", type=haxe_HaxeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
formalParameters208: BinaryAssociation = BinaryAssociation(
    name="formalParameters208",
    ends={
        Property(name="haxe_HaxeSingleVariableDeclaration209", type=haxe_HaxeAbstractFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeAbstractFunction", type=haxe_HaxeSingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters219: BinaryAssociation = BinaryAssociation(
    name="parameters219",
    ends={
        Property(name="haxe_HaxeSingleVariableDeclaration221", type=haxe_HaxeEnumConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeEnumConstructor220", type=haxe_HaxeSingleVariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticElement222: BinaryAssociation = BinaryAssociation(
    name="staticElement222",
    ends={
        Property(name="haxe_HaxeField", type=haxe_HaxeImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeImportDeclaration", type=haxe_HaxeField, multiplicity=Multiplicity(0, 1))
    }
)
constructedClass216: BinaryAssociation = BinaryAssociation(
    name="constructedClass216",
    ends={
        Property(name="haxe_HaxeClass218", type=haxe_HaxeConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeConstructor217", type=haxe_HaxeClass, multiplicity=Multiplicity(1, 1))
    }
)
metadata228: BinaryAssociation = BinaryAssociation(
    name="metadata228",
    ends={
        Property(name="HaxeMetadata", type=haxe_HaxeMetadataContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="usedIn", type=haxe_HaxeMetadata, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticField223: BinaryAssociation = BinaryAssociation(
    name="staticField223",
    ends={
        Property(name="haxe_HaxeField224", type=haxe_HaxeUsingDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeUsingDeclaration", type=haxe_HaxeField, multiplicity=Multiplicity(1, 1))
    }
)
usedIn225: BinaryAssociation = BinaryAssociation(
    name="usedIn225",
    ends={
        Property(name="HaxeMetadataContainer", type=haxe_HaxeMetadata, multiplicity=Multiplicity(1, 1)),
        Property(name="metadata", type=haxe_HaxeMetadataContainer, multiplicity=Multiplicity(1, 1))
    }
)
parameters226: BinaryAssociation = BinaryAssociation(
    name="parameters226",
    ends={
        Property(name="haxe_HaxeExpression227", type=haxe_HaxeMetadata, multiplicity=Multiplicity(1, 1)),
        Property(name="haxe_HaxeMetadata", type=haxe_HaxeExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_haxe_HaxeComment_HaxeASTNode = Generalization(general=HaxeASTNode, specific=haxe_HaxeComment)
gen_haxe_HaxeHaxedocComment_HaxeComment = Generalization(general=HaxeComment, specific=haxe_HaxeHaxedocComment)
gen_haxe_HaxeASTNode_HaxeModelElement = Generalization(general=HaxeModelElement, specific=haxe_HaxeASTNode)
gen_haxe_HaxeNamedElement_HaxeASTNode = Generalization(general=HaxeASTNode, specific=haxe_HaxeNamedElement)
gen_haxe_HaxeTagElement_HaxeASTNode = Generalization(general=HaxeASTNode, specific=haxe_HaxeTagElement)
gen_haxe_HaxeTextElement_HaxeASTNode = Generalization(general=HaxeASTNode, specific=haxe_HaxeTextElement)
gen_haxe_HaxeFieldContainer_HaxeModelElement = Generalization(general=HaxeModelElement, specific=haxe_HaxeFieldContainer)
gen_haxe_HaxeExpression_HaxeASTNode = Generalization(general=HaxeASTNode, specific=haxe_HaxeExpression)
gen_haxe_HaxeLoopStatement_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeLoopStatement)
gen_haxe_HaxePathReferentiable_HaxeNamedElement = Generalization(general=HaxeNamedElement, specific=haxe_HaxePathReferentiable)
gen_haxe_HaxePathReference_HaxeModelElement = Generalization(general=HaxeModelElement, specific=haxe_HaxePathReference)
gen_haxe_HaxeBlock_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeBlock)
gen_haxe_HaxeConditionalExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeConditionalExpression)
gen_haxe_HaxeUnaryExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeUnaryExpression)
gen_haxe_HaxeBinaryExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeBinaryExpression)
gen_haxe_HaxeForStatement_HaxeLoopStatement = Generalization(general=HaxeLoopStatement, specific=haxe_HaxeForStatement)
gen_haxe_HaxeWhileStatement_HaxeLoopStatement = Generalization(general=HaxeLoopStatement, specific=haxe_HaxeWhileStatement)
gen_haxe_HaxeInExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeInExpression)
gen_haxe_HaxeIfStatement_HaxeConditionalExpression = Generalization(general=HaxeConditionalExpression, specific=haxe_HaxeIfStatement)
gen_haxe_HaxeTernaryExpression_HaxeConditionalExpression = Generalization(general=HaxeConditionalExpression, specific=haxe_HaxeTernaryExpression)
gen_haxe_HaxePostfixExpression_HaxeUnaryExpression = Generalization(general=HaxeUnaryExpression, specific=haxe_HaxePostfixExpression)
gen_haxe_HaxeReturn_HaxeExpressionStatement = Generalization(general=HaxeExpressionStatement, specific=haxe_HaxeReturn)
gen_haxe_HaxeBreak_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeBreak)
gen_haxe_HaxeContinue_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeContinue)
gen_haxe_HaxeThisExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeThisExpression)
gen_haxe_HaxeDoWhileStatement_HaxeLoopStatement = Generalization(general=HaxeLoopStatement, specific=haxe_HaxeDoWhileStatement)
gen_haxe_HaxePrefixExpression_HaxeUnaryExpression = Generalization(general=HaxeUnaryExpression, specific=haxe_HaxePrefixExpression)
gen_haxe_HaxeInfixExpression_HaxeBinaryExpression = Generalization(general=HaxeBinaryExpression, specific=haxe_HaxeInfixExpression)
gen_haxe_HaxeNumberLiteral_HaxeConstant = Generalization(general=HaxeConstant, specific=haxe_HaxeNumberLiteral)
gen_haxe_HaxeIdentifierLiteral_HaxeConstant = Generalization(general=HaxeConstant, specific=haxe_HaxeIdentifierLiteral)
gen_haxe_HaxeRegexLiteral_HaxeConstant = Generalization(general=HaxeConstant, specific=haxe_HaxeRegexLiteral)
gen_haxe_HaxeFieldAccess_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeFieldAccess)
gen_haxe_HaxeEmptyStatement_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeEmptyStatement)
gen_haxe_HaxeConstant_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeConstant)
gen_haxe_HaxeStringLiteral_HaxeConstant = Generalization(general=HaxeConstant, specific=haxe_HaxeStringLiteral)
gen_haxe_HaxeNullLiteral_HaxeConstant = Generalization(general=HaxeConstant, specific=haxe_HaxeNullLiteral)
gen_haxe_HaxeBooleanLiteral_HaxeConstant = Generalization(general=HaxeConstant, specific=haxe_HaxeBooleanLiteral)
gen_haxe_HaxeArrayCreation_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeArrayCreation)
gen_haxe_HaxeArrayAccess_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeArrayAccess)
gen_haxe_HaxeParenthizedExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeParenthizedExpression)
gen_haxe_HaxeArrayInitializer_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeArrayInitializer)
gen_haxe_HaxeCase_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeCase)
gen_haxe_HaxeFunctionExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeFunctionExpression)
gen_haxe_HaxeFunctionExpression_HaxeAbstractFunction = Generalization(general=HaxeAbstractFunction, specific=haxe_HaxeFunctionExpression)
gen_haxe_HaxeCallExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeCallExpression)
gen_haxe_HaxeSwitch_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeSwitch)
gen_haxe_HaxeFieldDeclaration_HaxeTypedElement = Generalization(general=HaxeTypedElement, specific=haxe_HaxeFieldDeclaration)
gen_haxe_HaxeTryExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeTryExpression)
gen_haxe_HaxeCatchClause_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeCatchClause)
gen_haxe_HaxeObjectDeclaration_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeObjectDeclaration)
gen_haxe_HaxeFieldDeclaration_HaxeNamedElement = Generalization(general=HaxeNamedElement, specific=haxe_HaxeFieldDeclaration)
gen_haxe_HaxeCastingExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeCastingExpression)
gen_haxe_HaxeUnsafeCastExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeUnsafeCastExpression)
gen_haxe_HaxeTypeCheckExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeTypeCheckExpression)
gen_haxe_HaxeThrowExpression_HaxeExpressionStatement = Generalization(general=HaxeExpressionStatement, specific=haxe_HaxeThrowExpression)
gen_haxe_HaxeExpressionStatement_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeExpressionStatement)
gen_haxe_HaxeSuperConstructorInvocation_HaxeMethodInvocation = Generalization(general=HaxeMethodInvocation, specific=haxe_HaxeSuperConstructorInvocation)
gen_haxe_HaxeSingleVariableAccess_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeSingleVariableAccess)
gen_haxe_HaxePackageAccess_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxePackageAccess)
gen_haxe_HaxePackageAccess_HaxePathReference = Generalization(general=HaxePathReference, specific=haxe_HaxePackageAccess)
gen_haxe_HaxeAssignment_HaxeBinaryExpression = Generalization(general=HaxeBinaryExpression, specific=haxe_HaxeAssignment)
gen_haxe_HaxeSuperMethodInvocation_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeSuperMethodInvocation)
gen_haxe_HaxeSuperMethodInvocation_HaxeAbstractMethodInvocation = Generalization(general=HaxeAbstractMethodInvocation, specific=haxe_HaxeSuperMethodInvocation)
gen_haxe_HaxeMethodInvocation_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeMethodInvocation)
gen_haxe_HaxeMethodInvocation_HaxeAbstractMethodInvocation = Generalization(general=HaxeAbstractMethodInvocation, specific=haxe_HaxeMethodInvocation)
gen_haxe_HaxeVariableDeclaration_HaxeNamedElement = Generalization(general=HaxeNamedElement, specific=haxe_HaxeVariableDeclaration)
gen_haxe_HaxeVariableDeclarationGroup_HaxeTypedElement = Generalization(general=HaxeTypedElement, specific=haxe_HaxeVariableDeclarationGroup)
gen_haxe_HaxeAbstractMethodInvocation_HaxeASTNode = Generalization(general=HaxeASTNode, specific=haxe_HaxeAbstractMethodInvocation)
gen_haxe_HaxeSingleVariableDeclaration_HaxeVariableDeclaration = Generalization(general=HaxeVariableDeclaration, specific=haxe_HaxeSingleVariableDeclaration)
gen_haxe_HaxeSingleVariableDeclaration_HaxeTypedElement = Generalization(general=HaxeTypedElement, specific=haxe_HaxeSingleVariableDeclaration)
gen_haxe_HaxePackage_HaxePathReferentiable = Generalization(general=HaxePathReferentiable, specific=haxe_HaxePackage)
gen_haxe_HaxeVariableDeclarationFragment_HaxeVariableDeclaration = Generalization(general=HaxeVariableDeclaration, specific=haxe_HaxeVariableDeclarationFragment)
gen_haxe_HaxeVariableDeclarationExpression_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeVariableDeclarationExpression)
gen_haxe_HaxeType_HaxePathReferentiable = Generalization(general=HaxePathReferentiable, specific=haxe_HaxeType)
gen_haxe_HaxeType_HaxeASTNode = Generalization(general=HaxeASTNode, specific=haxe_HaxeType)
gen_haxe_HaxeModule_HaxeNamedElement = Generalization(general=HaxeNamedElement, specific=haxe_HaxeModule)
gen_haxe_HaxeClassifier_HaxeMetadataContainer = Generalization(general=HaxeMetadataContainer, specific=haxe_HaxeClassifier)
gen_haxe_HaxeClassifier_HaxeType = Generalization(general=HaxeType, specific=haxe_HaxeClassifier)
gen_haxe_HaxeClassifier_HaxeFieldContainer = Generalization(general=HaxeFieldContainer, specific=haxe_HaxeClassifier)
gen_haxe_HaxeClassifierAccess_HaxePathReference = Generalization(general=HaxePathReference, specific=haxe_HaxeClassifierAccess)
gen_haxe_HaxeClassifierAccess_HaxeTypeAccess = Generalization(general=HaxeTypeAccess, specific=haxe_HaxeClassifierAccess)
gen_haxe_HaxeTypedElement_HaxeModelElement = Generalization(general=HaxeModelElement, specific=haxe_HaxeTypedElement)
gen_haxe_HaxeClass_HaxeClassifier = Generalization(general=HaxeClassifier, specific=haxe_HaxeClass)
gen_haxe_HaxeTypeParameter_HaxeType = Generalization(general=HaxeType, specific=haxe_HaxeTypeParameter)
gen_haxe_HaxeTypeAccess_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeTypeAccess)
gen_haxe_HaxeFunctionTypeAccess_HaxeTypeAccess = Generalization(general=HaxeTypeAccess, specific=haxe_HaxeFunctionTypeAccess)
gen_haxe_HaxeAbstract_HaxeClassifier = Generalization(general=HaxeClassifier, specific=haxe_HaxeAbstract)
gen_haxe_HaxeEnum_HaxeClassifier = Generalization(general=HaxeClassifier, specific=haxe_HaxeEnum)
gen_haxe_HaxeAttribute_HaxeField = Generalization(general=HaxeField, specific=haxe_HaxeAttribute)
gen_haxe_HaxeAttribute_HaxeSingleVariableDeclaration = Generalization(general=HaxeSingleVariableDeclaration, specific=haxe_HaxeAttribute)
gen_haxe_HaxeTypedef_HaxeType = Generalization(general=HaxeType, specific=haxe_HaxeTypedef)
gen_haxe_HaxeField_HaxeNamedElement = Generalization(general=HaxeNamedElement, specific=haxe_HaxeField)
gen_haxe_HaxeField_HaxeMetadataContainer = Generalization(general=HaxeMetadataContainer, specific=haxe_HaxeField)
gen_haxe_HaxeAbstractOperation_HaxeAbstractFunction = Generalization(general=HaxeAbstractFunction, specific=haxe_HaxeAbstractOperation)
gen_haxe_HaxeOperation_HaxeAbstractOperation = Generalization(general=HaxeAbstractOperation, specific=haxe_HaxeOperation)
gen_haxe_HaxeOperation_HaxeField = Generalization(general=HaxeField, specific=haxe_HaxeOperation)
gen_haxe_HaxeOperation_HaxeTypedElement = Generalization(general=HaxeTypedElement, specific=haxe_HaxeOperation)
gen_haxe_HaxeAbstractFunction_HaxeASTNode = Generalization(general=HaxeASTNode, specific=haxe_HaxeAbstractFunction)
gen_haxe_HaxeDependencyDeclaration_HaxePathReference = Generalization(general=HaxePathReference, specific=haxe_HaxeDependencyDeclaration)
gen_haxe_HaxeDependencyDeclaration_HaxeASTNode = Generalization(general=HaxeASTNode, specific=haxe_HaxeDependencyDeclaration)
gen_haxe_HaxeImportDeclaration_HaxeDependencyDeclaration = Generalization(general=HaxeDependencyDeclaration, specific=haxe_HaxeImportDeclaration)
gen_haxe_HaxeUsingDeclaration_HaxeDependencyDeclaration = Generalization(general=HaxeDependencyDeclaration, specific=haxe_HaxeUsingDeclaration)
gen_haxe_HaxeConstructor_HaxeAbstractOperation = Generalization(general=HaxeAbstractOperation, specific=haxe_HaxeConstructor)
gen_haxe_HaxeConstructor_HaxeField = Generalization(general=HaxeField, specific=haxe_HaxeConstructor)
gen_haxe_HaxeEnumConstructor_HaxeVariableDeclaration = Generalization(general=HaxeVariableDeclaration, specific=haxe_HaxeEnumConstructor)
gen_haxe_HaxeEnumConstructor_HaxeField = Generalization(general=HaxeField, specific=haxe_HaxeEnumConstructor)
gen_haxe_HaxeMetadataContainer_HaxeModelElement = Generalization(general=HaxeModelElement, specific=haxe_HaxeMetadataContainer)
gen_haxe_HaxeMetadata_HaxeNamedElement = Generalization(general=HaxeNamedElement, specific=haxe_HaxeMetadata)
gen_haxe_HaxeMetadata_HaxeExpression = Generalization(general=HaxeExpression, specific=haxe_HaxeMetadata)

# Domain Model
domain_model = DomainModel(
    name="haxe",
    types={haxe_HaxeClass, haxe_HaxePathReferentiable, haxe_HaxeModule, haxe_HaxeModelElement, haxe_HaxeModel, haxe_HaxeHaxedocComment, HaxeComment, haxe_HaxeASTNode, HaxeModelElement, haxe_HaxeComment, haxe_HaxeNamedElement, HaxeASTNode, haxe_HaxeTagElement, haxe_HaxeTextElement, haxe_HaxeFieldContainer, haxe_HaxeField, haxe_HaxeExpression, haxe_HaxeLoopStatement, HaxeExpression, HaxeNamedElement, haxe_HaxePackage, haxe_HaxePathReference, haxe_HaxeBlock, haxe_HaxeConditionalExpression, haxe_HaxeUnaryExpression, haxe_HaxeBinaryExpression, haxe_HaxeForStatement, HaxeLoopStatement, haxe_HaxeSingleVariableDeclaration, haxe_HaxeWhileStatement, haxe_HaxeInExpression, haxe_HaxeIfStatement, HaxeConditionalExpression, haxe_HaxeTernaryExpression, haxe_HaxePostfixExpression, haxe_HaxeReturn, HaxeExpressionStatement, haxe_HaxeBreak, haxe_HaxeContinue, haxe_HaxeThisExpression, haxe_HaxeDoWhileStatement, haxe_HaxePrefixExpression, HaxeUnaryExpression, haxe_HaxeInfixExpression, HaxeBinaryExpression, haxe_HaxeNumberLiteral, haxe_HaxeIdentifierLiteral, haxe_HaxeRegexLiteral, haxe_HaxeFieldAccess, haxe_HaxeEmptyStatement, haxe_HaxeConstant, haxe_HaxeStringLiteral, HaxeConstant, haxe_HaxeNullLiteral, haxe_HaxeBooleanLiteral, haxe_HaxeArrayCreation, haxe_HaxeTypeAccess, haxe_HaxeArrayAccess, haxe_HaxeSingleVariableAccess, haxe_HaxeParenthizedExpression, haxe_HaxeArrayInitializer, haxe_HaxeFunctionExpression, HaxeAbstractFunction, haxe_HaxeCallExpression, haxe_HaxeSwitch, haxe_HaxeCase, HaxeTypedElement, haxe_HaxeTryExpression, haxe_HaxeCatchClause, haxe_HaxeObjectDeclaration, haxe_HaxeFieldDeclaration, haxe_HaxeCastingExpression, haxe_HaxeUnsafeCastExpression, haxe_HaxeTypeCheckExpression, haxe_HaxeThrowExpression, haxe_HaxeExpressionStatement, haxe_HaxeSuperConstructorInvocation, HaxeMethodInvocation, haxe_HaxeVariableDeclaration, haxe_HaxePackageAccess, HaxePathReference, haxe_HaxeAssignment, haxe_HaxeSuperMethodInvocation, HaxeAbstractMethodInvocation, haxe_HaxeMethodInvocation, haxe_HaxeVariableDeclarationGroup, haxe_HaxeVariableDeclarationExpression, haxe_HaxeAbstractMethodInvocation, haxe_HaxeAbstractOperation, HaxePathReferentiable, haxe_HaxeVariableDeclarationFragment, HaxeVariableDeclaration, haxe_HaxeDependencyDeclaration, haxe_HaxeType, HaxeMetadataContainer, haxe_HaxeOperation, haxe_HaxeAttribute, haxe_HaxeConstructor, haxe_HaxeTypeParameter, haxe_HaxeClassifier, HaxeType, HaxeFieldContainer, haxe_HaxeClassifierAccess, haxe_HaxeTypedElement, HaxeClassifier, haxe_HaxeFunctionTypeAccess, HaxeTypeAccess, haxe_HaxeAbstract, haxe_HaxeEnum, HaxeField, HaxeSingleVariableDeclaration, haxe_HaxeEnumConstructor, haxe_HaxeTypedef, HaxeAbstractOperation, haxe_HaxeAbstractFunction, haxe_HaxeImportDeclaration, HaxeDependencyDeclaration, haxe_HaxeUsingDeclaration, haxe_HaxeMetadata, haxe_HaxeMetadataContainer, HaxeTarget, HaxeAttributeProperty, HaxePrefixOperators, HaxeAssignmentOperator, HaxeInfixOperators},
    associations={mainClass0, elements1, referenced3, haxeModules6, comments8, tags9, fragments10, referencedTerminal15, haxeFields16, theBody17, parentReference13, referencedIn14, rightSide25, statements28, expression30, expression18, operand21, leftSide23, elseExpression37, parameter39, thenStatement32, elseStatement35, extendedSide45, variable40, expression42, dimensions55, initializer57, type60, array62, field47, expression48, expression51, expressions53, values74, expression77, expression80, index64, expression67, cases69, default71, value89, theBody92, catchClauses94, exception96, arguments82, extendsType85, fields87, expression102, type104, expression107, theBody97, expression100, qualifier116, variable119, qualifier121, expression109, type111, expression114, usageInVariableAccess129, initializer130, container132, method122, arguments123, typeArguments126, groups137, catchClause139, childrenReferences140, initializer133, fragments135, variablesContainer136, commentList146, dependencies149, thePackage151, theElements154, childrenPackages143, containedTypes144, containerPackage164, haxeOperations166, haxeAttribute168, containerModule155, commentsAfterDeclaration156, commentsBeforeDeclaration159, typeParameters162, argumentTypes177, parameterMapping180, type182, haxeConstructors170, bounds172, returnType175, underlyingType190, directCastingFromType192, directCastingToType195, generalization184, implementation187, fieldContainer201, getter202, setter205, literals198, refType199, typeParameters210, theBody213, formalParameters208, parameters219, staticElement222, constructedClass216, metadata228, staticField223, usedIn225, parameters226},
    generalizations={gen_haxe_HaxeComment_HaxeASTNode, gen_haxe_HaxeHaxedocComment_HaxeComment, gen_haxe_HaxeASTNode_HaxeModelElement, gen_haxe_HaxeNamedElement_HaxeASTNode, gen_haxe_HaxeTagElement_HaxeASTNode, gen_haxe_HaxeTextElement_HaxeASTNode, gen_haxe_HaxeFieldContainer_HaxeModelElement, gen_haxe_HaxeExpression_HaxeASTNode, gen_haxe_HaxeLoopStatement_HaxeExpression, gen_haxe_HaxePathReferentiable_HaxeNamedElement, gen_haxe_HaxePathReference_HaxeModelElement, gen_haxe_HaxeBlock_HaxeExpression, gen_haxe_HaxeConditionalExpression_HaxeExpression, gen_haxe_HaxeUnaryExpression_HaxeExpression, gen_haxe_HaxeBinaryExpression_HaxeExpression, gen_haxe_HaxeForStatement_HaxeLoopStatement, gen_haxe_HaxeWhileStatement_HaxeLoopStatement, gen_haxe_HaxeInExpression_HaxeExpression, gen_haxe_HaxeIfStatement_HaxeConditionalExpression, gen_haxe_HaxeTernaryExpression_HaxeConditionalExpression, gen_haxe_HaxePostfixExpression_HaxeUnaryExpression, gen_haxe_HaxeReturn_HaxeExpressionStatement, gen_haxe_HaxeBreak_HaxeExpression, gen_haxe_HaxeContinue_HaxeExpression, gen_haxe_HaxeThisExpression_HaxeExpression, gen_haxe_HaxeDoWhileStatement_HaxeLoopStatement, gen_haxe_HaxePrefixExpression_HaxeUnaryExpression, gen_haxe_HaxeInfixExpression_HaxeBinaryExpression, gen_haxe_HaxeNumberLiteral_HaxeConstant, gen_haxe_HaxeIdentifierLiteral_HaxeConstant, gen_haxe_HaxeRegexLiteral_HaxeConstant, gen_haxe_HaxeFieldAccess_HaxeExpression, gen_haxe_HaxeEmptyStatement_HaxeExpression, gen_haxe_HaxeConstant_HaxeExpression, gen_haxe_HaxeStringLiteral_HaxeConstant, gen_haxe_HaxeNullLiteral_HaxeConstant, gen_haxe_HaxeBooleanLiteral_HaxeConstant, gen_haxe_HaxeArrayCreation_HaxeExpression, gen_haxe_HaxeArrayAccess_HaxeExpression, gen_haxe_HaxeParenthizedExpression_HaxeExpression, gen_haxe_HaxeArrayInitializer_HaxeExpression, gen_haxe_HaxeCase_HaxeExpression, gen_haxe_HaxeFunctionExpression_HaxeExpression, gen_haxe_HaxeFunctionExpression_HaxeAbstractFunction, gen_haxe_HaxeCallExpression_HaxeExpression, gen_haxe_HaxeSwitch_HaxeExpression, gen_haxe_HaxeFieldDeclaration_HaxeTypedElement, gen_haxe_HaxeTryExpression_HaxeExpression, gen_haxe_HaxeCatchClause_HaxeExpression, gen_haxe_HaxeObjectDeclaration_HaxeExpression, gen_haxe_HaxeFieldDeclaration_HaxeNamedElement, gen_haxe_HaxeCastingExpression_HaxeExpression, gen_haxe_HaxeUnsafeCastExpression_HaxeExpression, gen_haxe_HaxeTypeCheckExpression_HaxeExpression, gen_haxe_HaxeThrowExpression_HaxeExpressionStatement, gen_haxe_HaxeExpressionStatement_HaxeExpression, gen_haxe_HaxeSuperConstructorInvocation_HaxeMethodInvocation, gen_haxe_HaxeSingleVariableAccess_HaxeExpression, gen_haxe_HaxePackageAccess_HaxeExpression, gen_haxe_HaxePackageAccess_HaxePathReference, gen_haxe_HaxeAssignment_HaxeBinaryExpression, gen_haxe_HaxeSuperMethodInvocation_HaxeExpression, gen_haxe_HaxeSuperMethodInvocation_HaxeAbstractMethodInvocation, gen_haxe_HaxeMethodInvocation_HaxeExpression, gen_haxe_HaxeMethodInvocation_HaxeAbstractMethodInvocation, gen_haxe_HaxeVariableDeclaration_HaxeNamedElement, gen_haxe_HaxeVariableDeclarationGroup_HaxeTypedElement, gen_haxe_HaxeAbstractMethodInvocation_HaxeASTNode, gen_haxe_HaxeSingleVariableDeclaration_HaxeVariableDeclaration, gen_haxe_HaxeSingleVariableDeclaration_HaxeTypedElement, gen_haxe_HaxePackage_HaxePathReferentiable, gen_haxe_HaxeVariableDeclarationFragment_HaxeVariableDeclaration, gen_haxe_HaxeVariableDeclarationExpression_HaxeExpression, gen_haxe_HaxeType_HaxePathReferentiable, gen_haxe_HaxeType_HaxeASTNode, gen_haxe_HaxeModule_HaxeNamedElement, gen_haxe_HaxeClassifier_HaxeMetadataContainer, gen_haxe_HaxeClassifier_HaxeType, gen_haxe_HaxeClassifier_HaxeFieldContainer, gen_haxe_HaxeClassifierAccess_HaxePathReference, gen_haxe_HaxeClassifierAccess_HaxeTypeAccess, gen_haxe_HaxeTypedElement_HaxeModelElement, gen_haxe_HaxeClass_HaxeClassifier, gen_haxe_HaxeTypeParameter_HaxeType, gen_haxe_HaxeTypeAccess_HaxeExpression, gen_haxe_HaxeFunctionTypeAccess_HaxeTypeAccess, gen_haxe_HaxeAbstract_HaxeClassifier, gen_haxe_HaxeEnum_HaxeClassifier, gen_haxe_HaxeAttribute_HaxeField, gen_haxe_HaxeAttribute_HaxeSingleVariableDeclaration, gen_haxe_HaxeTypedef_HaxeType, gen_haxe_HaxeField_HaxeNamedElement, gen_haxe_HaxeField_HaxeMetadataContainer, gen_haxe_HaxeAbstractOperation_HaxeAbstractFunction, gen_haxe_HaxeOperation_HaxeAbstractOperation, gen_haxe_HaxeOperation_HaxeField, gen_haxe_HaxeOperation_HaxeTypedElement, gen_haxe_HaxeAbstractFunction_HaxeASTNode, gen_haxe_HaxeDependencyDeclaration_HaxePathReference, gen_haxe_HaxeDependencyDeclaration_HaxeASTNode, gen_haxe_HaxeImportDeclaration_HaxeDependencyDeclaration, gen_haxe_HaxeUsingDeclaration_HaxeDependencyDeclaration, gen_haxe_HaxeConstructor_HaxeAbstractOperation, gen_haxe_HaxeConstructor_HaxeField, gen_haxe_HaxeEnumConstructor_HaxeVariableDeclaration, gen_haxe_HaxeEnumConstructor_HaxeField, gen_haxe_HaxeMetadataContainer_HaxeModelElement, gen_haxe_HaxeMetadata_HaxeNamedElement, gen_haxe_HaxeMetadata_HaxeExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)