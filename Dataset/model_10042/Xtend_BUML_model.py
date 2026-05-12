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
JvmVisibility: Enumeration = Enumeration(
    name="JvmVisibility",
    literals={
            EnumerationLiteral(name="DEFAULT"),
			EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PUBLIC")
    }
)

# Classes
xtend_XtendFile = Class(name="xtend_XtendFile")
xtend_XtendTypeDeclaration = Class(name="xtend_XtendTypeDeclaration")
xtend_JvmTypeParameter = Class(name="xtend_JvmTypeParameter")
xtend_XExpression = Class(name="xtend_XExpression", is_abstract=True)
xtend_XtendAnnotationTarget = Class(name="xtend_XtendAnnotationTarget", is_abstract=True)
xtend_XAnnotation = Class(name="xtend_XAnnotation")
xtend_XtendParameter = Class(name="xtend_XtendParameter")
xtend_XtendMember = Class(name="xtend_XtendMember")
XtendAnnotationTarget = Class(name="XtendAnnotationTarget")
xtend_XtendFunction = Class(name="xtend_XtendFunction")
XtendExecutable = Class(name="XtendExecutable")
xtend_CreateExtensionInfo = Class(name="xtend_CreateExtensionInfo")
xtend_XtendClass = Class(name="xtend_XtendClass")
XtendTypeDeclaration = Class(name="XtendTypeDeclaration")
xtend_XtendField = Class(name="xtend_XtendField")
XtendMember = Class(name="XtendMember")
xtend_JvmTypeReference = Class(name="xtend_JvmTypeReference", is_abstract=True)
xtend_XtendConstructor = Class(name="xtend_XtendConstructor")
xtend_XtendAnnotationType = Class(name="xtend_XtendAnnotationType")
xtend_XtendInterface = Class(name="xtend_XtendInterface")
xtend_RichString = Class(name="xtend_RichString")
XBlockExpression = Class(name="XBlockExpression")
xtend_RichStringLiteral = Class(name="xtend_RichStringLiteral")
XStringLiteral = Class(name="XStringLiteral")
xtend_RichStringForLoop = Class(name="xtend_RichStringForLoop")
XForLoopExpression = Class(name="XForLoopExpression")
xtend_XtendEnum = Class(name="xtend_XtendEnum")
xtend_XtendEnumLiteral = Class(name="xtend_XtendEnumLiteral")
xtend_XtendVariableDeclaration = Class(name="xtend_XtendVariableDeclaration")
XVariableDeclaration = Class(name="XVariableDeclaration")
xtend_XtendFormalParameter = Class(name="xtend_XtendFormalParameter")
JvmFormalParameter = Class(name="JvmFormalParameter")
xtend_RichStringIf = Class(name="xtend_RichStringIf")
XExpression = Class(name="XExpression")
xtend_XIfExpression = Class(name="xtend_XIfExpression")
xtend_RichStringElseIf = Class(name="xtend_RichStringElseIf")
xtend_XSwitchExpression = Class(name="xtend_XSwitchExpression")
JvmIdentifiableElement = Class(name="JvmIdentifiableElement")
xtend_XCasePart = Class(name="xtend_XCasePart")
xtend_XVariableDeclaration = Class(name="xtend_XVariableDeclaration")
xtend_XAbstractFeatureCall = Class(name="xtend_XAbstractFeatureCall", is_abstract=True)
xtend_JvmIdentifiableElement = Class(name="xtend_JvmIdentifiableElement", is_abstract=True)
xtend_XBlockExpression = Class(name="xtend_XBlockExpression")
xtend_XMemberFeatureCall = Class(name="xtend_XMemberFeatureCall")
XAbstractFeatureCall = Class(name="XAbstractFeatureCall")
xtend_XFeatureCall = Class(name="xtend_XFeatureCall")
xtend_JvmDeclaredType = Class(name="xtend_JvmDeclaredType", is_abstract=True)
xtend_XConstructorCall = Class(name="xtend_XConstructorCall")
xtend_JvmConstructor = Class(name="xtend_JvmConstructor")
xtend_JvmFormalParameter = Class(name="xtend_JvmFormalParameter")
xtend_XCastedExpression = Class(name="xtend_XCastedExpression")
xtend_XBinaryOperation = Class(name="xtend_XBinaryOperation")
xtend_XBooleanLiteral = Class(name="xtend_XBooleanLiteral")
xtend_XNullLiteral = Class(name="xtend_XNullLiteral")
xtend_XNumberLiteral = Class(name="xtend_XNumberLiteral")
xtend_XStringLiteral = Class(name="xtend_XStringLiteral")
xtend_XClosure = Class(name="xtend_XClosure")
xtend_XAbstractWhileExpression = Class(name="xtend_XAbstractWhileExpression", is_abstract=True)
xtend_XDoWhileExpression = Class(name="xtend_XDoWhileExpression")
XAbstractWhileExpression = Class(name="XAbstractWhileExpression")
xtend_XWhileExpression = Class(name="xtend_XWhileExpression")
xtend_XTypeLiteral = Class(name="xtend_XTypeLiteral")
xtend_JvmType = Class(name="xtend_JvmType", is_abstract=True)
xtend_XUnaryOperation = Class(name="xtend_XUnaryOperation")
xtend_XInstanceOfExpression = Class(name="xtend_XInstanceOfExpression")
xtend_XForLoopExpression = Class(name="xtend_XForLoopExpression")
xtend_XThrowExpression = Class(name="xtend_XThrowExpression")
xtend_XTryCatchFinallyExpression = Class(name="xtend_XTryCatchFinallyExpression")
xtend_XAssignment = Class(name="xtend_XAssignment")
xtend_XReturnExpression = Class(name="xtend_XReturnExpression")
xtend_XCatchClause = Class(name="xtend_XCatchClause")
xtend_AnonymousClass = Class(name="xtend_AnonymousClass")
xtend_XtendExecutable = Class(name="xtend_XtendExecutable", is_abstract=True)
JvmType = Class(name="JvmType")
xtend_JvmComponentType = Class(name="xtend_JvmComponentType", is_abstract=True)
xtend_JvmArrayType = Class(name="xtend_JvmArrayType")
xtend_JvmPrimitiveType = Class(name="xtend_JvmPrimitiveType")
JvmComponentType = Class(name="JvmComponentType")
JvmMember = Class(name="JvmMember")
xtend_JvmVoid = Class(name="xtend_JvmVoid")
xtend_JvmMember = Class(name="xtend_JvmMember", is_abstract=True)
JvmConstraintOwner = Class(name="JvmConstraintOwner")
xtend_JvmTypeParameterDeclarator = Class(name="xtend_JvmTypeParameterDeclarator", is_abstract=True)
xtend_JvmConstraintOwner = Class(name="xtend_JvmConstraintOwner", is_abstract=True)
xtend_JvmTypeConstraint = Class(name="xtend_JvmTypeConstraint", is_abstract=True)
xtend_JvmUpperBound = Class(name="xtend_JvmUpperBound")
JvmTypeConstraint = Class(name="JvmTypeConstraint")
xtend_JvmLowerBound = Class(name="xtend_JvmLowerBound")
xtend_JvmAnnotationType = Class(name="xtend_JvmAnnotationType")
JvmDeclaredType = Class(name="JvmDeclaredType")
xtend_JvmEnumerationType = Class(name="xtend_JvmEnumerationType")
JvmField = Class(name="JvmField")
xtend_JvmGenericType = Class(name="xtend_JvmGenericType")
JvmTypeParameterDeclarator = Class(name="JvmTypeParameterDeclarator")
xtend_JvmEnumerationLiteral = Class(name="xtend_JvmEnumerationLiteral")
xtend_JvmParameterizedTypeReference = Class(name="xtend_JvmParameterizedTypeReference")
JvmTypeReference = Class(name="JvmTypeReference")
xtend_JvmGenericArrayTypeReference = Class(name="xtend_JvmGenericArrayTypeReference")
xtend_JvmAnyTypeReference = Class(name="xtend_JvmAnyTypeReference")
xtend_JvmMultiTypeReference = Class(name="xtend_JvmMultiTypeReference")
JvmCompoundTypeReference = Class(name="JvmCompoundTypeReference")
JvmAnnotationTarget = Class(name="JvmAnnotationTarget")
xtend_JvmFeature = Class(name="xtend_JvmFeature", is_abstract=True)
xtend_JvmWildcardTypeReference = Class(name="xtend_JvmWildcardTypeReference")
xtend_JvmField = Class(name="xtend_JvmField")
JvmFeature = Class(name="JvmFeature")
xtend_JvmExecutable = Class(name="xtend_JvmExecutable", is_abstract=True)
JvmExecutable = Class(name="JvmExecutable")
xtend_JvmOperation = Class(name="xtend_JvmOperation")
xtend_JvmAnnotationValue = Class(name="xtend_JvmAnnotationValue", is_abstract=True)
xtend_JvmAnnotationTarget = Class(name="xtend_JvmAnnotationTarget", is_abstract=True)
xtend_JvmAnnotationReference = Class(name="xtend_JvmAnnotationReference")
xtend_JvmIntAnnotationValue = Class(name="xtend_JvmIntAnnotationValue")
JvmAnnotationValue = Class(name="JvmAnnotationValue")
xtend_JvmBooleanAnnotationValue = Class(name="xtend_JvmBooleanAnnotationValue")
xtend_JvmByteAnnotationValue = Class(name="xtend_JvmByteAnnotationValue")
xtend_JvmShortAnnotationValue = Class(name="xtend_JvmShortAnnotationValue")
xtend_JvmLongAnnotationValue = Class(name="xtend_JvmLongAnnotationValue")
xtend_JvmDoubleAnnotationValue = Class(name="xtend_JvmDoubleAnnotationValue")
xtend_JvmFloatAnnotationValue = Class(name="xtend_JvmFloatAnnotationValue")
xtend_JvmCharAnnotationValue = Class(name="xtend_JvmCharAnnotationValue")
xtend_JvmStringAnnotationValue = Class(name="xtend_JvmStringAnnotationValue")
xtend_JvmTypeAnnotationValue = Class(name="xtend_JvmTypeAnnotationValue")
xtend_JvmAnnotationAnnotationValue = Class(name="xtend_JvmAnnotationAnnotationValue")
xtend_JvmEnumAnnotationValue = Class(name="xtend_JvmEnumAnnotationValue")
xtend_JvmDelegateTypeReference = Class(name="xtend_JvmDelegateTypeReference")
xtend_JvmSpecializedTypeReference = Class(name="xtend_JvmSpecializedTypeReference", is_abstract=True)
xtend_JvmSynonymTypeReference = Class(name="xtend_JvmSynonymTypeReference")
xtend_JvmUnknownTypeReference = Class(name="xtend_JvmUnknownTypeReference")
xtend_JvmCompoundTypeReference = Class(name="xtend_JvmCompoundTypeReference", is_abstract=True)
xtend_JvmCustomAnnotationValue = Class(name="xtend_JvmCustomAnnotationValue")

# xtend_XtendFile class attributes and methods
xtend_XtendFile_package: Property = Property(name="package", type=StringType)
xtend_XtendFile.attributes={xtend_XtendFile_package}

# xtend_XtendTypeDeclaration class attributes and methods
xtend_XtendTypeDeclaration_name: Property = Property(name="name", type=StringType)
xtend_XtendTypeDeclaration_m_isAnonymous: Method = Method(name="isAnonymous", parameters={}, type=BooleanType)
xtend_XtendTypeDeclaration_m_isLocal: Method = Method(name="isLocal", parameters={}, type=BooleanType)
xtend_XtendTypeDeclaration.attributes={xtend_XtendTypeDeclaration_name}
xtend_XtendTypeDeclaration.methods={xtend_XtendTypeDeclaration_m_isLocal, xtend_XtendTypeDeclaration_m_isAnonymous}

# xtend_JvmTypeParameter class attributes and methods
xtend_JvmTypeParameter_name: Property = Property(name="name", type=StringType)
xtend_JvmTypeParameter.attributes={xtend_JvmTypeParameter_name}

# xtend_XExpression class attributes and methods

# xtend_XtendAnnotationTarget class attributes and methods

# xtend_XAnnotation class attributes and methods

# xtend_XtendParameter class attributes and methods
xtend_XtendParameter_name: Property = Property(name="name", type=StringType)
xtend_XtendParameter_varArg: Property = Property(name="varArg", type=BooleanType)
xtend_XtendParameter_extension: Property = Property(name="extension", type=BooleanType)
xtend_XtendParameter.attributes={xtend_XtendParameter_extension, xtend_XtendParameter_varArg, xtend_XtendParameter_name}

# xtend_XtendMember class attributes and methods
xtend_XtendMember_modifiers: Property = Property(name="modifiers", type=StringType)
xtend_XtendMember_m_getVisibility: Method = Method(name="getVisibility", parameters={}, type=StringType)
xtend_XtendMember_m_getDeclaredVisibility: Method = Method(name="getDeclaredVisibility", parameters={}, type=StringType)
xtend_XtendMember_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
xtend_XtendMember_m_isFinal: Method = Method(name="isFinal", parameters={}, type=BooleanType)
xtend_XtendMember.attributes={xtend_XtendMember_modifiers}
xtend_XtendMember.methods={xtend_XtendMember_m_getVisibility, xtend_XtendMember_m_isStatic, xtend_XtendMember_m_isFinal, xtend_XtendMember_m_getDeclaredVisibility}

# XtendAnnotationTarget class attributes and methods

# xtend_XtendFunction class attributes and methods
xtend_XtendFunction_name: Property = Property(name="name", type=StringType)
xtend_XtendFunction_m_isAbstract: Method = Method(name="isAbstract", parameters={}, type=BooleanType)
xtend_XtendFunction_m_isOverride: Method = Method(name="isOverride", parameters={}, type=BooleanType)
xtend_XtendFunction_m_isDispatch: Method = Method(name="isDispatch", parameters={}, type=BooleanType)
xtend_XtendFunction_m_isStrictFloatingPoint: Method = Method(name="isStrictFloatingPoint", parameters={}, type=BooleanType)
xtend_XtendFunction_m_isNative: Method = Method(name="isNative", parameters={}, type=BooleanType)
xtend_XtendFunction_m_isSynchonized: Method = Method(name="isSynchonized", parameters={}, type=BooleanType)
xtend_XtendFunction.attributes={xtend_XtendFunction_name}
xtend_XtendFunction.methods={xtend_XtendFunction_m_isOverride, xtend_XtendFunction_m_isNative, xtend_XtendFunction_m_isDispatch, xtend_XtendFunction_m_isStrictFloatingPoint, xtend_XtendFunction_m_isSynchonized, xtend_XtendFunction_m_isAbstract}

# XtendExecutable class attributes and methods

# xtend_CreateExtensionInfo class attributes and methods
xtend_CreateExtensionInfo_name: Property = Property(name="name", type=StringType)
xtend_CreateExtensionInfo.attributes={xtend_CreateExtensionInfo_name}

# xtend_XtendClass class attributes and methods
xtend_XtendClass_m_isAbstract: Method = Method(name="isAbstract", parameters={}, type=BooleanType)
xtend_XtendClass_m_isStrictFloatingPoint: Method = Method(name="isStrictFloatingPoint", parameters={}, type=BooleanType)
xtend_XtendClass.methods={xtend_XtendClass_m_isAbstract, xtend_XtendClass_m_isStrictFloatingPoint}

# XtendTypeDeclaration class attributes and methods

# xtend_XtendField class attributes and methods
xtend_XtendField_name: Property = Property(name="name", type=StringType)
xtend_XtendField_m_isExtension: Method = Method(name="isExtension", parameters={}, type=BooleanType)
xtend_XtendField_m_isVolatile: Method = Method(name="isVolatile", parameters={}, type=BooleanType)
xtend_XtendField_m_isTransient: Method = Method(name="isTransient", parameters={}, type=BooleanType)
xtend_XtendField.attributes={xtend_XtendField_name}
xtend_XtendField.methods={xtend_XtendField_m_isVolatile, xtend_XtendField_m_isExtension, xtend_XtendField_m_isTransient}

# XtendMember class attributes and methods

# xtend_JvmTypeReference class attributes and methods
xtend_JvmTypeReference_m_getType: Method = Method(name="getType", parameters={}, type=JvmType)
xtend_JvmTypeReference_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
xtend_JvmTypeReference_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
xtend_JvmTypeReference_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
xtend_JvmTypeReference_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='xtend_innerClassDelimiter', type=StringType)}, type=StringType)
xtend_JvmTypeReference_m_accept1: Method = Method(name="accept1", parameters={Parameter(name='xtend_visitor', type=StringType)})
xtend_JvmTypeReference_m_accept2: Method = Method(name="accept2", parameters={Parameter(name='xtend_parameter', type=StringType), Parameter(name='xtend_visitor', type=StringType)})
xtend_JvmTypeReference.methods={xtend_JvmTypeReference_m_getIdentifier, xtend_JvmTypeReference_m_accept1, xtend_JvmTypeReference_m_accept2, xtend_JvmTypeReference_m_getType, xtend_JvmTypeReference_m_getQualifiedName, xtend_JvmTypeReference_m_getSimpleName, xtend_JvmTypeReference_m_getQualifiedName}

# xtend_XtendConstructor class attributes and methods

# xtend_XtendAnnotationType class attributes and methods

# xtend_XtendInterface class attributes and methods
xtend_XtendInterface_m_isStrictFloatingPoint: Method = Method(name="isStrictFloatingPoint", parameters={}, type=BooleanType)
xtend_XtendInterface.methods={xtend_XtendInterface_m_isStrictFloatingPoint}

# xtend_RichString class attributes and methods

# XBlockExpression class attributes and methods

# xtend_RichStringLiteral class attributes and methods

# XStringLiteral class attributes and methods

# xtend_RichStringForLoop class attributes and methods

# XForLoopExpression class attributes and methods

# xtend_XtendEnum class attributes and methods

# xtend_XtendEnumLiteral class attributes and methods
xtend_XtendEnumLiteral_name: Property = Property(name="name", type=StringType)
xtend_XtendEnumLiteral.attributes={xtend_XtendEnumLiteral_name}

# xtend_XtendVariableDeclaration class attributes and methods
xtend_XtendVariableDeclaration_extension: Property = Property(name="extension", type=BooleanType)
xtend_XtendVariableDeclaration.attributes={xtend_XtendVariableDeclaration_extension}

# XVariableDeclaration class attributes and methods

# xtend_XtendFormalParameter class attributes and methods
xtend_XtendFormalParameter_extension: Property = Property(name="extension", type=BooleanType)
xtend_XtendFormalParameter.attributes={xtend_XtendFormalParameter_extension}

# JvmFormalParameter class attributes and methods

# xtend_RichStringIf class attributes and methods

# XExpression class attributes and methods

# xtend_XIfExpression class attributes and methods

# xtend_RichStringElseIf class attributes and methods

# xtend_XSwitchExpression class attributes and methods
xtend_XSwitchExpression_localVarName: Property = Property(name="localVarName", type=StringType)
xtend_XSwitchExpression.attributes={xtend_XSwitchExpression_localVarName}

# JvmIdentifiableElement class attributes and methods

# xtend_XCasePart class attributes and methods

# xtend_XVariableDeclaration class attributes and methods
xtend_XVariableDeclaration_name: Property = Property(name="name", type=StringType)
xtend_XVariableDeclaration_writeable: Property = Property(name="writeable", type=BooleanType)
xtend_XVariableDeclaration.attributes={xtend_XVariableDeclaration_writeable, xtend_XVariableDeclaration_name}

# xtend_XAbstractFeatureCall class attributes and methods
xtend_XAbstractFeatureCall_invalidFeatureIssueCode: Property = Property(name="invalidFeatureIssueCode", type=StringType)
xtend_XAbstractFeatureCall_validFeature: Property = Property(name="validFeature", type=BooleanType)
xtend_XAbstractFeatureCall_m_getConcreteSyntaxFeatureName: Method = Method(name="getConcreteSyntaxFeatureName", parameters={}, type=StringType)
xtend_XAbstractFeatureCall_m_getExplicitArguments: Method = Method(name="getExplicitArguments", parameters={}, type=XExpression)
xtend_XAbstractFeatureCall_m_isExplicitOperationCallOrBuilderSyntax: Method = Method(name="isExplicitOperationCallOrBuilderSyntax", parameters={}, type=BooleanType)
xtend_XAbstractFeatureCall.attributes={xtend_XAbstractFeatureCall_validFeature, xtend_XAbstractFeatureCall_invalidFeatureIssueCode}
xtend_XAbstractFeatureCall.methods={xtend_XAbstractFeatureCall_m_getExplicitArguments, xtend_XAbstractFeatureCall_m_getConcreteSyntaxFeatureName, xtend_XAbstractFeatureCall_m_isExplicitOperationCallOrBuilderSyntax}

# xtend_JvmIdentifiableElement class attributes and methods
xtend_JvmIdentifiableElement_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
xtend_JvmIdentifiableElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
xtend_JvmIdentifiableElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='xtend_innerClassDelimiter', type=StringType)}, type=StringType)
xtend_JvmIdentifiableElement_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
xtend_JvmIdentifiableElement.methods={xtend_JvmIdentifiableElement_m_getSimpleName, xtend_JvmIdentifiableElement_m_getIdentifier, xtend_JvmIdentifiableElement_m_getQualifiedName, xtend_JvmIdentifiableElement_m_getQualifiedName}

# xtend_XBlockExpression class attributes and methods

# xtend_XMemberFeatureCall class attributes and methods
xtend_XMemberFeatureCall_nullSafe: Property = Property(name="nullSafe", type=BooleanType)
xtend_XMemberFeatureCall_explicitOperationCall: Property = Property(name="explicitOperationCall", type=BooleanType)
xtend_XMemberFeatureCall_spreading: Property = Property(name="spreading", type=BooleanType)
xtend_XMemberFeatureCall.attributes={xtend_XMemberFeatureCall_explicitOperationCall, xtend_XMemberFeatureCall_nullSafe, xtend_XMemberFeatureCall_spreading}

# XAbstractFeatureCall class attributes and methods

# xtend_XFeatureCall class attributes and methods
xtend_XFeatureCall_explicitOperationCall: Property = Property(name="explicitOperationCall", type=BooleanType)
xtend_XFeatureCall.attributes={xtend_XFeatureCall_explicitOperationCall}

# xtend_JvmDeclaredType class attributes and methods
xtend_JvmDeclaredType_abstract: Property = Property(name="abstract", type=BooleanType)
xtend_JvmDeclaredType_static: Property = Property(name="static", type=BooleanType)
xtend_JvmDeclaredType_final: Property = Property(name="final", type=BooleanType)
xtend_JvmDeclaredType_packageName: Property = Property(name="packageName", type=StringType)
xtend_JvmDeclaredType_m_getDeclaredOperations: Method = Method(name="getDeclaredOperations", parameters={})
xtend_JvmDeclaredType_m_getDeclaredFields: Method = Method(name="getDeclaredFields", parameters={})
xtend_JvmDeclaredType_m_getAllFeatures: Method = Method(name="getAllFeatures", parameters={})
xtend_JvmDeclaredType_m_findAllFeaturesByName: Method = Method(name="findAllFeaturesByName", parameters={Parameter(name='xtend_simpleName', type=StringType)})
xtend_JvmDeclaredType.attributes={xtend_JvmDeclaredType_abstract, xtend_JvmDeclaredType_final, xtend_JvmDeclaredType_packageName, xtend_JvmDeclaredType_static}
xtend_JvmDeclaredType.methods={xtend_JvmDeclaredType_m_getDeclaredFields, xtend_JvmDeclaredType_m_getAllFeatures, xtend_JvmDeclaredType_m_findAllFeaturesByName, xtend_JvmDeclaredType_m_getDeclaredOperations}

# xtend_XConstructorCall class attributes and methods
xtend_XConstructorCall_invalidFeatureIssueCode: Property = Property(name="invalidFeatureIssueCode", type=StringType)
xtend_XConstructorCall_validFeature: Property = Property(name="validFeature", type=BooleanType)
xtend_XConstructorCall.attributes={xtend_XConstructorCall_invalidFeatureIssueCode, xtend_XConstructorCall_validFeature}

# xtend_JvmConstructor class attributes and methods

# xtend_JvmFormalParameter class attributes and methods
xtend_JvmFormalParameter_name: Property = Property(name="name", type=StringType)
xtend_JvmFormalParameter.attributes={xtend_JvmFormalParameter_name}

# xtend_XCastedExpression class attributes and methods

# xtend_XBinaryOperation class attributes and methods

# xtend_XBooleanLiteral class attributes and methods
xtend_XBooleanLiteral_isTrue: Property = Property(name="isTrue", type=BooleanType)
xtend_XBooleanLiteral.attributes={xtend_XBooleanLiteral_isTrue}

# xtend_XNullLiteral class attributes and methods

# xtend_XNumberLiteral class attributes and methods
xtend_XNumberLiteral_value: Property = Property(name="value", type=StringType)
xtend_XNumberLiteral.attributes={xtend_XNumberLiteral_value}

# xtend_XStringLiteral class attributes and methods
xtend_XStringLiteral_value: Property = Property(name="value", type=StringType)
xtend_XStringLiteral.attributes={xtend_XStringLiteral_value}

# xtend_XClosure class attributes and methods
xtend_XClosure_explicitSyntax: Property = Property(name="explicitSyntax", type=BooleanType)
xtend_XClosure_m_getFormalParameters: Method = Method(name="getFormalParameters", parameters={}, type=JvmFormalParameter)
xtend_XClosure.attributes={xtend_XClosure_explicitSyntax}
xtend_XClosure.methods={xtend_XClosure_m_getFormalParameters}

# xtend_XAbstractWhileExpression class attributes and methods

# xtend_XDoWhileExpression class attributes and methods

# XAbstractWhileExpression class attributes and methods

# xtend_XWhileExpression class attributes and methods

# xtend_XTypeLiteral class attributes and methods

# xtend_JvmType class attributes and methods

# xtend_XUnaryOperation class attributes and methods

# xtend_XInstanceOfExpression class attributes and methods

# xtend_XForLoopExpression class attributes and methods

# xtend_XThrowExpression class attributes and methods

# xtend_XTryCatchFinallyExpression class attributes and methods

# xtend_XAssignment class attributes and methods

# xtend_XReturnExpression class attributes and methods

# xtend_XCatchClause class attributes and methods

# xtend_AnonymousClass class attributes and methods

# xtend_XtendExecutable class attributes and methods

# JvmType class attributes and methods

# xtend_JvmComponentType class attributes and methods

# xtend_JvmArrayType class attributes and methods
xtend_JvmArrayType_m_getDimensions: Method = Method(name="getDimensions", parameters={}, type=IntegerType)
xtend_JvmArrayType.methods={xtend_JvmArrayType_m_getDimensions}

# xtend_JvmPrimitiveType class attributes and methods
xtend_JvmPrimitiveType_simpleName: Property = Property(name="simpleName", type=StringType)
xtend_JvmPrimitiveType.attributes={xtend_JvmPrimitiveType_simpleName}

# JvmComponentType class attributes and methods

# JvmMember class attributes and methods

# xtend_JvmVoid class attributes and methods

# xtend_JvmMember class attributes and methods
xtend_JvmMember_visibility: Property = Property(name="visibility", type=StringType)
xtend_JvmMember_simpleName: Property = Property(name="simpleName", type=StringType)
xtend_JvmMember_identifier: Property = Property(name="identifier", type=StringType)
xtend_JvmMember_m_internalSetIdentifier: Method = Method(name="internalSetIdentifier", parameters={Parameter(name='xtend_identifier', type=StringType)})
xtend_JvmMember.attributes={xtend_JvmMember_identifier, xtend_JvmMember_simpleName, xtend_JvmMember_visibility}
xtend_JvmMember.methods={xtend_JvmMember_m_internalSetIdentifier}

# JvmConstraintOwner class attributes and methods

# xtend_JvmTypeParameterDeclarator class attributes and methods

# xtend_JvmConstraintOwner class attributes and methods

# xtend_JvmTypeConstraint class attributes and methods
xtend_JvmTypeConstraint_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
xtend_JvmTypeConstraint_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
xtend_JvmTypeConstraint_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
xtend_JvmTypeConstraint_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='xtend_innerClassDelimiter', type=StringType)}, type=StringType)
xtend_JvmTypeConstraint.methods={xtend_JvmTypeConstraint_m_getQualifiedName, xtend_JvmTypeConstraint_m_getSimpleName, xtend_JvmTypeConstraint_m_getIdentifier, xtend_JvmTypeConstraint_m_getQualifiedName}

# xtend_JvmUpperBound class attributes and methods

# JvmTypeConstraint class attributes and methods

# xtend_JvmLowerBound class attributes and methods

# xtend_JvmAnnotationType class attributes and methods

# JvmDeclaredType class attributes and methods

# xtend_JvmEnumerationType class attributes and methods

# JvmField class attributes and methods

# xtend_JvmGenericType class attributes and methods
xtend_JvmGenericType_interface: Property = Property(name="interface", type=BooleanType)
xtend_JvmGenericType_m_getExtendedInterfaces: Method = Method(name="getExtendedInterfaces", parameters={})
xtend_JvmGenericType_m_getExtendedClass: Method = Method(name="getExtendedClass", parameters={}, type=StringType)
xtend_JvmGenericType_m_isInstantiateable: Method = Method(name="isInstantiateable", parameters={}, type=BooleanType)
xtend_JvmGenericType_m_getDeclaredConstructors: Method = Method(name="getDeclaredConstructors", parameters={})
xtend_JvmGenericType.attributes={xtend_JvmGenericType_interface}
xtend_JvmGenericType.methods={xtend_JvmGenericType_m_getExtendedClass, xtend_JvmGenericType_m_getDeclaredConstructors, xtend_JvmGenericType_m_isInstantiateable, xtend_JvmGenericType_m_getExtendedInterfaces}

# JvmTypeParameterDeclarator class attributes and methods

# xtend_JvmEnumerationLiteral class attributes and methods
xtend_JvmEnumerationLiteral_m_getEnumType: Method = Method(name="getEnumType", parameters={}, type=StringType)
xtend_JvmEnumerationLiteral.methods={xtend_JvmEnumerationLiteral_m_getEnumType}

# xtend_JvmParameterizedTypeReference class attributes and methods

# JvmTypeReference class attributes and methods

# xtend_JvmGenericArrayTypeReference class attributes and methods
xtend_JvmGenericArrayTypeReference_m_getDimensions: Method = Method(name="getDimensions", parameters={}, type=IntegerType)
xtend_JvmGenericArrayTypeReference_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
xtend_JvmGenericArrayTypeReference.methods={xtend_JvmGenericArrayTypeReference_m_getType, xtend_JvmGenericArrayTypeReference_m_getDimensions}

# xtend_JvmAnyTypeReference class attributes and methods

# xtend_JvmMultiTypeReference class attributes and methods

# JvmCompoundTypeReference class attributes and methods

# JvmAnnotationTarget class attributes and methods

# xtend_JvmFeature class attributes and methods

# xtend_JvmWildcardTypeReference class attributes and methods

# xtend_JvmField class attributes and methods
xtend_JvmField_static: Property = Property(name="static", type=BooleanType)
xtend_JvmField_final: Property = Property(name="final", type=BooleanType)
xtend_JvmField.attributes={xtend_JvmField_static, xtend_JvmField_final}

# JvmFeature class attributes and methods

# xtend_JvmExecutable class attributes and methods
xtend_JvmExecutable_varArgs: Property = Property(name="varArgs", type=BooleanType)
xtend_JvmExecutable.attributes={xtend_JvmExecutable_varArgs}

# JvmExecutable class attributes and methods

# xtend_JvmOperation class attributes and methods
xtend_JvmOperation_static: Property = Property(name="static", type=BooleanType)
xtend_JvmOperation_final: Property = Property(name="final", type=BooleanType)
xtend_JvmOperation_abstract: Property = Property(name="abstract", type=BooleanType)
xtend_JvmOperation.attributes={xtend_JvmOperation_static, xtend_JvmOperation_final, xtend_JvmOperation_abstract}

# xtend_JvmAnnotationValue class attributes and methods
xtend_JvmAnnotationValue_m_getValueName: Method = Method(name="getValueName", parameters={}, type=StringType)
xtend_JvmAnnotationValue.methods={xtend_JvmAnnotationValue_m_getValueName}

# xtend_JvmAnnotationTarget class attributes and methods

# xtend_JvmAnnotationReference class attributes and methods

# xtend_JvmIntAnnotationValue class attributes and methods
xtend_JvmIntAnnotationValue_values: Property = Property(name="values", type=IntegerType)
xtend_JvmIntAnnotationValue.attributes={xtend_JvmIntAnnotationValue_values}

# JvmAnnotationValue class attributes and methods

# xtend_JvmBooleanAnnotationValue class attributes and methods
xtend_JvmBooleanAnnotationValue_values: Property = Property(name="values", type=BooleanType)
xtend_JvmBooleanAnnotationValue.attributes={xtend_JvmBooleanAnnotationValue_values}

# xtend_JvmByteAnnotationValue class attributes and methods
xtend_JvmByteAnnotationValue_values: Property = Property(name="values", type=StringType)
xtend_JvmByteAnnotationValue.attributes={xtend_JvmByteAnnotationValue_values}

# xtend_JvmShortAnnotationValue class attributes and methods
xtend_JvmShortAnnotationValue_values: Property = Property(name="values", type=StringType)
xtend_JvmShortAnnotationValue.attributes={xtend_JvmShortAnnotationValue_values}

# xtend_JvmLongAnnotationValue class attributes and methods
xtend_JvmLongAnnotationValue_values: Property = Property(name="values", type=StringType)
xtend_JvmLongAnnotationValue.attributes={xtend_JvmLongAnnotationValue_values}

# xtend_JvmDoubleAnnotationValue class attributes and methods
xtend_JvmDoubleAnnotationValue_values: Property = Property(name="values", type=FloatType)
xtend_JvmDoubleAnnotationValue.attributes={xtend_JvmDoubleAnnotationValue_values}

# xtend_JvmFloatAnnotationValue class attributes and methods
xtend_JvmFloatAnnotationValue_values: Property = Property(name="values", type=FloatType)
xtend_JvmFloatAnnotationValue.attributes={xtend_JvmFloatAnnotationValue_values}

# xtend_JvmCharAnnotationValue class attributes and methods
xtend_JvmCharAnnotationValue_values: Property = Property(name="values", type=StringType)
xtend_JvmCharAnnotationValue.attributes={xtend_JvmCharAnnotationValue_values}

# xtend_JvmStringAnnotationValue class attributes and methods
xtend_JvmStringAnnotationValue_values: Property = Property(name="values", type=StringType)
xtend_JvmStringAnnotationValue.attributes={xtend_JvmStringAnnotationValue_values}

# xtend_JvmTypeAnnotationValue class attributes and methods

# xtend_JvmAnnotationAnnotationValue class attributes and methods

# xtend_JvmEnumAnnotationValue class attributes and methods

# xtend_JvmDelegateTypeReference class attributes and methods

# xtend_JvmSpecializedTypeReference class attributes and methods

# xtend_JvmSynonymTypeReference class attributes and methods

# xtend_JvmUnknownTypeReference class attributes and methods
xtend_JvmUnknownTypeReference_exception: Property = Property(name="exception", type=StringType)
xtend_JvmUnknownTypeReference.attributes={xtend_JvmUnknownTypeReference_exception}

# xtend_JvmCompoundTypeReference class attributes and methods

# xtend_JvmCustomAnnotationValue class attributes and methods
xtend_JvmCustomAnnotationValue_values: Property = Property(name="values", type=StringType)
xtend_JvmCustomAnnotationValue.attributes={xtend_JvmCustomAnnotationValue_values}

# Relationships
xtendTypes0: BinaryAssociation = BinaryAssociation(
    name="xtendTypes0",
    ends={
        Property(name="xtend_XtendTypeDeclaration", type=xtend_XtendFile, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendFile", type=xtend_XtendTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements2: BinaryAssociation = BinaryAssociation(
    name="implements2",
    ends={
        Property(name="xtend_JvmTypeReference4", type=xtend_XtendClass, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendClass3", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="xtend_JvmTypeReference16", type=xtend_XtendField, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendField", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters5: BinaryAssociation = BinaryAssociation(
    name="typeParameters5",
    ends={
        Property(name="xtend_JvmTypeParameter", type=xtend_XtendClass, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendClass6", type=xtend_JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue17: BinaryAssociation = BinaryAssociation(
    name="initialValue17",
    ends={
        Property(name="xtend_XExpression", type=xtend_XtendField, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendField18", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations7: BinaryAssociation = BinaryAssociation(
    name="annotations7",
    ends={
        Property(name="xtend_XAnnotation", type=xtend_XtendAnnotationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendAnnotationTarget", type=xtend_XAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationInfo8: BinaryAssociation = BinaryAssociation(
    name="annotationInfo8",
    ends={
        Property(name="xtend_XtendAnnotationTarget9", type=xtend_XtendMember, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendMember", type=xtend_XtendAnnotationTarget, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaringType10: BinaryAssociation = BinaryAssociation(
    name="declaringType10",
    ends={
        Property(name="XtendTypeDeclaration", type=xtend_XtendMember, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=xtend_XtendTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
returnType11: BinaryAssociation = BinaryAssociation(
    name="returnType11",
    ends={
        Property(name="xtend_JvmTypeReference12", type=xtend_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendFunction", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createExtensionInfo13: BinaryAssociation = BinaryAssociation(
    name="createExtensionInfo13",
    ends={
        Property(name="xtend_CreateExtensionInfo", type=xtend_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendFunction14", type=xtend_CreateExtensionInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends1: BinaryAssociation = BinaryAssociation(
    name="extends1",
    ends={
        Property(name="xtend_JvmTypeReference", type=xtend_XtendClass, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendClass", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createExpression45: BinaryAssociation = BinaryAssociation(
    name="createExpression45",
    ends={
        Property(name="xtend_XExpression47", type=xtend_CreateExtensionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_CreateExtensionInfo46", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members48: BinaryAssociation = BinaryAssociation(
    name="members48",
    ends={
        Property(name="XtendMember", type=xtend_XtendTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaringType", type=xtend_XtendMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterType19: BinaryAssociation = BinaryAssociation(
    name="parameterType19",
    ends={
        Property(name="xtend_JvmTypeReference20", type=xtend_XtendParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendParameter", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends49: BinaryAssociation = BinaryAssociation(
    name="extends49",
    ends={
        Property(name="xtend_JvmTypeReference50", type=xtend_XtendInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendInterface", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters51: BinaryAssociation = BinaryAssociation(
    name="typeParameters51",
    ends={
        Property(name="xtend_JvmTypeParameter53", type=xtend_XtendInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendInterface52", type=xtend_JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
separator21: BinaryAssociation = BinaryAssociation(
    name="separator21",
    ends={
        Property(name="xtend_XExpression22", type=xtend_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_RichStringForLoop", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
before23: BinaryAssociation = BinaryAssociation(
    name="before23",
    ends={
        Property(name="xtend_XExpression25", type=xtend_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_RichStringForLoop24", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after26: BinaryAssociation = BinaryAssociation(
    name="after26",
    ends={
        Property(name="xtend_XExpression28", type=xtend_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_RichStringForLoop27", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if_29: BinaryAssociation = BinaryAssociation(
    name="if_29",
    ends={
        Property(name="xtend_XExpression30", type=xtend_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_RichStringIf", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then31: BinaryAssociation = BinaryAssociation(
    name="then31",
    ends={
        Property(name="xtend_XExpression33", type=xtend_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_RichStringIf32", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIfs34: BinaryAssociation = BinaryAssociation(
    name="elseIfs34",
    ends={
        Property(name="xtend_RichStringElseIf", type=xtend_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_RichStringIf35", type=xtend_RichStringElseIf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else_36: BinaryAssociation = BinaryAssociation(
    name="else_36",
    ends={
        Property(name="xtend_XExpression38", type=xtend_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_RichStringIf37", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if_39: BinaryAssociation = BinaryAssociation(
    name="if_39",
    ends={
        Property(name="xtend_XExpression41", type=xtend_RichStringElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_RichStringElseIf40", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then42: BinaryAssociation = BinaryAssociation(
    name="then42",
    ends={
        Property(name="xtend_XExpression44", type=xtend_RichStringElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_RichStringElseIf43", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases64: BinaryAssociation = BinaryAssociation(
    name="cases64",
    ends={
        Property(name="xtend_XSwitchExpression65", type=xtend_XCasePart, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="xtend_XCasePart", type=xtend_XSwitchExpression, multiplicity=Multiplicity(1, 1))
    }
)
default66: BinaryAssociation = BinaryAssociation(
    name="default66",
    ends={
        Property(name="xtend_XExpression68", type=xtend_XSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XSwitchExpression67", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case69: BinaryAssociation = BinaryAssociation(
    name="case69",
    ends={
        Property(name="xtend_XExpression71", type=xtend_XCasePart, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XCasePart70", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then72: BinaryAssociation = BinaryAssociation(
    name="then72",
    ends={
        Property(name="xtend_XExpression74", type=xtend_XCasePart, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XCasePart73", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if_54: BinaryAssociation = BinaryAssociation(
    name="if_54",
    ends={
        Property(name="xtend_XExpression55", type=xtend_XIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XIfExpression", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then56: BinaryAssociation = BinaryAssociation(
    name="then56",
    ends={
        Property(name="xtend_XExpression58", type=xtend_XIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XIfExpression57", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else_59: BinaryAssociation = BinaryAssociation(
    name="else_59",
    ends={
        Property(name="xtend_XExpression61", type=xtend_XIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XIfExpression60", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switch62: BinaryAssociation = BinaryAssociation(
    name="switch62",
    ends={
        Property(name="xtend_XExpression63", type=xtend_XSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XSwitchExpression", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type80: BinaryAssociation = BinaryAssociation(
    name="type80",
    ends={
        Property(name="xtend_JvmTypeReference81", type=xtend_XVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XVariableDeclaration", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right82: BinaryAssociation = BinaryAssociation(
    name="right82",
    ends={
        Property(name="xtend_XExpression84", type=xtend_XVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XVariableDeclaration83", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeGuard75: BinaryAssociation = BinaryAssociation(
    name="typeGuard75",
    ends={
        Property(name="xtend_JvmTypeReference77", type=xtend_XCasePart, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XCasePart76", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions78: BinaryAssociation = BinaryAssociation(
    name="expressions78",
    ends={
        Property(name="xtend_XExpression79", type=xtend_XBlockExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XBlockExpression", type=xtend_XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implicitFirstArgument92: BinaryAssociation = BinaryAssociation(
    name="implicitFirstArgument92",
    ends={
        Property(name="xtend_XExpression94", type=xtend_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XAbstractFeatureCall93", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualTypeArguments95: BinaryAssociation = BinaryAssociation(
    name="actualTypeArguments95",
    ends={
        Property(name="xtend_JvmTypeReference97", type=xtend_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XAbstractFeatureCall96", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberCallTarget98: BinaryAssociation = BinaryAssociation(
    name="memberCallTarget98",
    ends={
        Property(name="xtend_XExpression99", type=xtend_XMemberFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XMemberFeatureCall", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature85: BinaryAssociation = BinaryAssociation(
    name="feature85",
    ends={
        Property(name="xtend_JvmIdentifiableElement", type=xtend_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XAbstractFeatureCall", type=xtend_JvmIdentifiableElement, multiplicity=Multiplicity(0, 1))
    }
)
typeArguments86: BinaryAssociation = BinaryAssociation(
    name="typeArguments86",
    ends={
        Property(name="xtend_JvmTypeReference88", type=xtend_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XAbstractFeatureCall87", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implicitReceiver89: BinaryAssociation = BinaryAssociation(
    name="implicitReceiver89",
    ends={
        Property(name="xtend_XExpression91", type=xtend_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XAbstractFeatureCall90", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureCallArguments103: BinaryAssociation = BinaryAssociation(
    name="featureCallArguments103",
    ends={
        Property(name="xtend_XExpression104", type=xtend_XFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XFeatureCall", type=xtend_XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaringType105: BinaryAssociation = BinaryAssociation(
    name="declaringType105",
    ends={
        Property(name="xtend_JvmDeclaredType", type=xtend_XFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XFeatureCall106", type=xtend_JvmDeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
constructor107: BinaryAssociation = BinaryAssociation(
    name="constructor107",
    ends={
        Property(name="xtend_JvmConstructor", type=xtend_XConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XConstructorCall", type=xtend_JvmConstructor, multiplicity=Multiplicity(0, 1))
    }
)
arguments108: BinaryAssociation = BinaryAssociation(
    name="arguments108",
    ends={
        Property(name="xtend_XExpression110", type=xtend_XConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XConstructorCall109", type=xtend_XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments111: BinaryAssociation = BinaryAssociation(
    name="typeArguments111",
    ends={
        Property(name="xtend_JvmTypeReference113", type=xtend_XConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XConstructorCall112", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberCallArguments100: BinaryAssociation = BinaryAssociation(
    name="memberCallArguments100",
    ends={
        Property(name="xtend_XExpression102", type=xtend_XMemberFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XMemberFeatureCall101", type=xtend_XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaredFormalParameters114: BinaryAssociation = BinaryAssociation(
    name="declaredFormalParameters114",
    ends={
        Property(name="xtend_JvmFormalParameter", type=xtend_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XClosure", type=xtend_JvmFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression115: BinaryAssociation = BinaryAssociation(
    name="expression115",
    ends={
        Property(name="xtend_XExpression117", type=xtend_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XClosure116", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implicitParameter118: BinaryAssociation = BinaryAssociation(
    name="implicitParameter118",
    ends={
        Property(name="xtend_JvmFormalParameter120", type=xtend_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XClosure119", type=xtend_JvmFormalParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type121: BinaryAssociation = BinaryAssociation(
    name="type121",
    ends={
        Property(name="xtend_JvmTypeReference122", type=xtend_XCastedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XCastedExpression", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target123: BinaryAssociation = BinaryAssociation(
    name="target123",
    ends={
        Property(name="xtend_XExpression125", type=xtend_XCastedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XCastedExpression124", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand126: BinaryAssociation = BinaryAssociation(
    name="leftOperand126",
    ends={
        Property(name="xtend_XExpression127", type=xtend_XBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XBinaryOperation", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eachExpression135: BinaryAssociation = BinaryAssociation(
    name="eachExpression135",
    ends={
        Property(name="xtend_XExpression137", type=xtend_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XForLoopExpression136", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredParam138: BinaryAssociation = BinaryAssociation(
    name="declaredParam138",
    ends={
        Property(name="xtend_JvmFormalParameter140", type=xtend_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XForLoopExpression139", type=xtend_JvmFormalParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predicate141: BinaryAssociation = BinaryAssociation(
    name="predicate141",
    ends={
        Property(name="xtend_XExpression142", type=xtend_XAbstractWhileExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XAbstractWhileExpression", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body143: BinaryAssociation = BinaryAssociation(
    name="body143",
    ends={
        Property(name="xtend_XExpression145", type=xtend_XAbstractWhileExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XAbstractWhileExpression144", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand128: BinaryAssociation = BinaryAssociation(
    name="rightOperand128",
    ends={
        Property(name="xtend_XExpression130", type=xtend_XBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XBinaryOperation129", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type146: BinaryAssociation = BinaryAssociation(
    name="type146",
    ends={
        Property(name="xtend_JvmType", type=xtend_XTypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XTypeLiteral", type=xtend_JvmType, multiplicity=Multiplicity(1, 1))
    }
)
operand131: BinaryAssociation = BinaryAssociation(
    name="operand131",
    ends={
        Property(name="xtend_XExpression132", type=xtend_XUnaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XUnaryOperation", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forExpression133: BinaryAssociation = BinaryAssociation(
    name="forExpression133",
    ends={
        Property(name="xtend_XExpression134", type=xtend_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XForLoopExpression", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression149: BinaryAssociation = BinaryAssociation(
    name="expression149",
    ends={
        Property(name="xtend_XExpression151", type=xtend_XInstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XInstanceOfExpression150", type=xtend_XExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression152: BinaryAssociation = BinaryAssociation(
    name="expression152",
    ends={
        Property(name="xtend_XExpression153", type=xtend_XThrowExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XThrowExpression", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression154: BinaryAssociation = BinaryAssociation(
    name="expression154",
    ends={
        Property(name="xtend_XExpression155", type=xtend_XTryCatchFinallyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XTryCatchFinallyExpression", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finallyExpression156: BinaryAssociation = BinaryAssociation(
    name="finallyExpression156",
    ends={
        Property(name="xtend_XExpression158", type=xtend_XTryCatchFinallyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XTryCatchFinallyExpression157", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type147: BinaryAssociation = BinaryAssociation(
    name="type147",
    ends={
        Property(name="xtend_JvmTypeReference148", type=xtend_XInstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XInstanceOfExpression", type=xtend_JvmTypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression161: BinaryAssociation = BinaryAssociation(
    name="expression161",
    ends={
        Property(name="xtend_XExpression163", type=xtend_XCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XCatchClause162", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredParam164: BinaryAssociation = BinaryAssociation(
    name="declaredParam164",
    ends={
        Property(name="xtend_JvmFormalParameter166", type=xtend_XCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XCatchClause165", type=xtend_JvmFormalParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignable167: BinaryAssociation = BinaryAssociation(
    name="assignable167",
    ends={
        Property(name="xtend_XExpression168", type=xtend_XAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XAssignment", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value169: BinaryAssociation = BinaryAssociation(
    name="value169",
    ends={
        Property(name="xtend_XExpression171", type=xtend_XAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XAssignment170", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression172: BinaryAssociation = BinaryAssociation(
    name="expression172",
    ends={
        Property(name="xtend_XExpression173", type=xtend_XReturnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XReturnExpression", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses159: BinaryAssociation = BinaryAssociation(
    name="catchClauses159",
    ends={
        Property(name="xtend_XCatchClause", type=xtend_XTryCatchFinallyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XTryCatchFinallyExpression160", type=xtend_XCatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters176: BinaryAssociation = BinaryAssociation(
    name="typeParameters176",
    ends={
        Property(name="xtend_JvmTypeParameter178", type=xtend_XtendExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendExecutable177", type=xtend_JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression179: BinaryAssociation = BinaryAssociation(
    name="expression179",
    ends={
        Property(name="xtend_XExpression181", type=xtend_XtendExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendExecutable180", type=xtend_XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters182: BinaryAssociation = BinaryAssociation(
    name="parameters182",
    ends={
        Property(name="xtend_XtendParameter184", type=xtend_XtendExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendExecutable183", type=xtend_XtendParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructorCall185: BinaryAssociation = BinaryAssociation(
    name="constructorCall185",
    ends={
        Property(name="xtend_XConstructorCall186", type=xtend_AnonymousClass, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_AnonymousClass", type=xtend_XConstructorCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions174: BinaryAssociation = BinaryAssociation(
    name="exceptions174",
    ends={
        Property(name="xtend_JvmTypeReference175", type=xtend_XtendExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_XtendExecutable", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayType187: BinaryAssociation = BinaryAssociation(
    name="arrayType187",
    ends={
        Property(name="JvmArrayType", type=xtend_JvmComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="componentType", type=xtend_JvmArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentType188: BinaryAssociation = BinaryAssociation(
    name="componentType188",
    ends={
        Property(name="JvmComponentType", type=xtend_JvmArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="arrayType", type=xtend_JvmComponentType, multiplicity=Multiplicity(0, 1))
    }
)
superTypes189: BinaryAssociation = BinaryAssociation(
    name="superTypes189",
    ends={
        Property(name="xtend_JvmTypeReference191", type=xtend_JvmDeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmDeclaredType190", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members192: BinaryAssociation = BinaryAssociation(
    name="members192",
    ends={
        Property(name="JvmMember", type=xtend_JvmDeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="declaringType193", type=xtend_JvmMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarator194: BinaryAssociation = BinaryAssociation(
    name="declarator194",
    ends={
        Property(name="JvmTypeParameterDeclarator", type=xtend_JvmTypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="typeParameters", type=xtend_JvmTypeParameterDeclarator, multiplicity=Multiplicity(0, 1))
    }
)
typeParameters195: BinaryAssociation = BinaryAssociation(
    name="typeParameters195",
    ends={
        Property(name="JvmTypeParameter", type=xtend_JvmTypeParameterDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="declarator", type=xtend_JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeReference197: BinaryAssociation = BinaryAssociation(
    name="typeReference197",
    ends={
        Property(name="xtend_JvmTypeReference198", type=xtend_JvmTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmTypeConstraint", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner199: BinaryAssociation = BinaryAssociation(
    name="owner199",
    ends={
        Property(name="JvmConstraintOwner", type=xtend_JvmTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=xtend_JvmConstraintOwner, multiplicity=Multiplicity(0, 1))
    }
)
constraints196: BinaryAssociation = BinaryAssociation(
    name="constraints196",
    ends={
        Property(name="JvmTypeConstraint", type=xtend_JvmConstraintOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=xtend_JvmTypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literals200: BinaryAssociation = BinaryAssociation(
    name="literals200",
    ends={
        Property(name="xtend_JvmEnumerationLiteral", type=xtend_JvmEnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmEnumerationType", type=xtend_JvmEnumerationLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
arguments201: BinaryAssociation = BinaryAssociation(
    name="arguments201",
    ends={
        Property(name="xtend_JvmTypeReference202", type=xtend_JvmParameterizedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmParameterizedTypeReference", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type203: BinaryAssociation = BinaryAssociation(
    name="type203",
    ends={
        Property(name="xtend_JvmType205", type=xtend_JvmParameterizedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmParameterizedTypeReference204", type=xtend_JvmType, multiplicity=Multiplicity(0, 1))
    }
)
componentType206: BinaryAssociation = BinaryAssociation(
    name="componentType206",
    ends={
        Property(name="xtend_JvmTypeReference207", type=xtend_JvmGenericArrayTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmGenericArrayTypeReference", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type208: BinaryAssociation = BinaryAssociation(
    name="type208",
    ends={
        Property(name="xtend_JvmType209", type=xtend_JvmAnyTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmAnyTypeReference", type=xtend_JvmType, multiplicity=Multiplicity(0, 1))
    }
)
declaringType210: BinaryAssociation = BinaryAssociation(
    name="declaringType210",
    ends={
        Property(name="JvmDeclaredType", type=xtend_JvmMember, multiplicity=Multiplicity(1, 1)),
        Property(name="members211", type=xtend_JvmDeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
type212: BinaryAssociation = BinaryAssociation(
    name="type212",
    ends={
        Property(name="xtend_JvmTypeReference213", type=xtend_JvmField, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmField", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters214: BinaryAssociation = BinaryAssociation(
    name="parameters214",
    ends={
        Property(name="xtend_JvmFormalParameter215", type=xtend_JvmExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmExecutable", type=xtend_JvmFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions216: BinaryAssociation = BinaryAssociation(
    name="exceptions216",
    ends={
        Property(name="xtend_JvmTypeReference218", type=xtend_JvmExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmExecutable217", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType219: BinaryAssociation = BinaryAssociation(
    name="returnType219",
    ends={
        Property(name="xtend_JvmTypeReference220", type=xtend_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmOperation", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue221: BinaryAssociation = BinaryAssociation(
    name="defaultValue221",
    ends={
        Property(name="xtend_JvmAnnotationValue", type=xtend_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmOperation222", type=xtend_JvmAnnotationValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterType223: BinaryAssociation = BinaryAssociation(
    name="parameterType223",
    ends={
        Property(name="xtend_JvmTypeReference225", type=xtend_JvmFormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmFormalParameter224", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations226: BinaryAssociation = BinaryAssociation(
    name="annotations226",
    ends={
        Property(name="JvmAnnotationReference", type=xtend_JvmAnnotationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=xtend_JvmAnnotationReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation227: BinaryAssociation = BinaryAssociation(
    name="annotation227",
    ends={
        Property(name="xtend_JvmAnnotationType", type=xtend_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmAnnotationReference", type=xtend_JvmAnnotationType, multiplicity=Multiplicity(0, 1))
    }
)
target228: BinaryAssociation = BinaryAssociation(
    name="target228",
    ends={
        Property(name="JvmAnnotationTarget", type=xtend_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations", type=xtend_JvmAnnotationTarget, multiplicity=Multiplicity(0, 1))
    }
)
values229: BinaryAssociation = BinaryAssociation(
    name="values229",
    ends={
        Property(name="xtend_JvmAnnotationValue231", type=xtend_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmAnnotationReference230", type=xtend_JvmAnnotationValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation232: BinaryAssociation = BinaryAssociation(
    name="operation232",
    ends={
        Property(name="xtend_JvmOperation234", type=xtend_JvmAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmAnnotationValue233", type=xtend_JvmOperation, multiplicity=Multiplicity(0, 1))
    }
)
values235: BinaryAssociation = BinaryAssociation(
    name="values235",
    ends={
        Property(name="xtend_JvmTypeReference236", type=xtend_JvmTypeAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmTypeAnnotationValue", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values237: BinaryAssociation = BinaryAssociation(
    name="values237",
    ends={
        Property(name="xtend_JvmAnnotationReference238", type=xtend_JvmAnnotationAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmAnnotationAnnotationValue", type=xtend_JvmAnnotationReference, multiplicity=Multiplicity(0, 9999))
    }
)
values239: BinaryAssociation = BinaryAssociation(
    name="values239",
    ends={
        Property(name="xtend_JvmEnumerationLiteral240", type=xtend_JvmEnumAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmEnumAnnotationValue", type=xtend_JvmEnumerationLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
delegate241: BinaryAssociation = BinaryAssociation(
    name="delegate241",
    ends={
        Property(name="xtend_JvmTypeReference242", type=xtend_JvmDelegateTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmDelegateTypeReference", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1))
    }
)
equivalent243: BinaryAssociation = BinaryAssociation(
    name="equivalent243",
    ends={
        Property(name="xtend_JvmTypeReference244", type=xtend_JvmSpecializedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmSpecializedTypeReference", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type245: BinaryAssociation = BinaryAssociation(
    name="type245",
    ends={
        Property(name="xtend_JvmType246", type=xtend_JvmCompoundTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmCompoundTypeReference", type=xtend_JvmType, multiplicity=Multiplicity(0, 1))
    }
)
references247: BinaryAssociation = BinaryAssociation(
    name="references247",
    ends={
        Property(name="xtend_JvmTypeReference249", type=xtend_JvmCompoundTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="xtend_JvmCompoundTypeReference248", type=xtend_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_xtend_XtendParameter_XtendAnnotationTarget = Generalization(general=XtendAnnotationTarget, specific=xtend_XtendParameter)
gen_xtend_XtendMember_XtendAnnotationTarget = Generalization(general=XtendAnnotationTarget, specific=xtend_XtendMember)
gen_xtend_XtendFunction_XtendExecutable = Generalization(general=XtendExecutable, specific=xtend_XtendFunction)
gen_xtend_XtendClass_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=xtend_XtendClass)
gen_xtend_XtendField_XtendMember = Generalization(general=XtendMember, specific=xtend_XtendField)
gen_xtend_XtendConstructor_XtendExecutable = Generalization(general=XtendExecutable, specific=xtend_XtendConstructor)
gen_xtend_XtendTypeDeclaration_XtendMember = Generalization(general=XtendMember, specific=xtend_XtendTypeDeclaration)
gen_xtend_XtendAnnotationType_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=xtend_XtendAnnotationType)
gen_xtend_XtendInterface_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=xtend_XtendInterface)
gen_xtend_RichString_XBlockExpression = Generalization(general=XBlockExpression, specific=xtend_RichString)
gen_xtend_RichStringLiteral_XStringLiteral = Generalization(general=XStringLiteral, specific=xtend_RichStringLiteral)
gen_xtend_RichStringForLoop_XForLoopExpression = Generalization(general=XForLoopExpression, specific=xtend_RichStringForLoop)
gen_xtend_XtendEnum_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=xtend_XtendEnum)
gen_xtend_XtendEnumLiteral_XtendMember = Generalization(general=XtendMember, specific=xtend_XtendEnumLiteral)
gen_xtend_XtendVariableDeclaration_XVariableDeclaration = Generalization(general=XVariableDeclaration, specific=xtend_XtendVariableDeclaration)
gen_xtend_XtendFormalParameter_JvmFormalParameter = Generalization(general=JvmFormalParameter, specific=xtend_XtendFormalParameter)
gen_xtend_RichStringIf_XExpression = Generalization(general=XExpression, specific=xtend_RichStringIf)
gen_xtend_XIfExpression_XExpression = Generalization(general=XExpression, specific=xtend_XIfExpression)
gen_xtend_XCasePart_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=xtend_XCasePart)
gen_xtend_XSwitchExpression_XExpression = Generalization(general=XExpression, specific=xtend_XSwitchExpression)
gen_xtend_XSwitchExpression_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=xtend_XSwitchExpression)
gen_xtend_XVariableDeclaration_XExpression = Generalization(general=XExpression, specific=xtend_XVariableDeclaration)
gen_xtend_XVariableDeclaration_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=xtend_XVariableDeclaration)
gen_xtend_XAbstractFeatureCall_XExpression = Generalization(general=XExpression, specific=xtend_XAbstractFeatureCall)
gen_xtend_XBlockExpression_XExpression = Generalization(general=XExpression, specific=xtend_XBlockExpression)
gen_xtend_XMemberFeatureCall_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=xtend_XMemberFeatureCall)
gen_xtend_XFeatureCall_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=xtend_XFeatureCall)
gen_xtend_XConstructorCall_XExpression = Generalization(general=XExpression, specific=xtend_XConstructorCall)
gen_xtend_XCastedExpression_XExpression = Generalization(general=XExpression, specific=xtend_XCastedExpression)
gen_xtend_XBinaryOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=xtend_XBinaryOperation)
gen_xtend_XBooleanLiteral_XExpression = Generalization(general=XExpression, specific=xtend_XBooleanLiteral)
gen_xtend_XNullLiteral_XExpression = Generalization(general=XExpression, specific=xtend_XNullLiteral)
gen_xtend_XNumberLiteral_XExpression = Generalization(general=XExpression, specific=xtend_XNumberLiteral)
gen_xtend_XStringLiteral_XExpression = Generalization(general=XExpression, specific=xtend_XStringLiteral)
gen_xtend_XClosure_XExpression = Generalization(general=XExpression, specific=xtend_XClosure)
gen_xtend_XAbstractWhileExpression_XExpression = Generalization(general=XExpression, specific=xtend_XAbstractWhileExpression)
gen_xtend_XDoWhileExpression_XAbstractWhileExpression = Generalization(general=XAbstractWhileExpression, specific=xtend_XDoWhileExpression)
gen_xtend_XWhileExpression_XAbstractWhileExpression = Generalization(general=XAbstractWhileExpression, specific=xtend_XWhileExpression)
gen_xtend_XTypeLiteral_XExpression = Generalization(general=XExpression, specific=xtend_XTypeLiteral)
gen_xtend_XUnaryOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=xtend_XUnaryOperation)
gen_xtend_XInstanceOfExpression_XExpression = Generalization(general=XExpression, specific=xtend_XInstanceOfExpression)
gen_xtend_XForLoopExpression_XExpression = Generalization(general=XExpression, specific=xtend_XForLoopExpression)
gen_xtend_XThrowExpression_XExpression = Generalization(general=XExpression, specific=xtend_XThrowExpression)
gen_xtend_XTryCatchFinallyExpression_XExpression = Generalization(general=XExpression, specific=xtend_XTryCatchFinallyExpression)
gen_xtend_XAssignment_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=xtend_XAssignment)
gen_xtend_XReturnExpression_XExpression = Generalization(general=XExpression, specific=xtend_XReturnExpression)
gen_xtend_AnonymousClass_XExpression = Generalization(general=XExpression, specific=xtend_AnonymousClass)
gen_xtend_AnonymousClass_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=xtend_AnonymousClass)
gen_xtend_XtendExecutable_XtendMember = Generalization(general=XtendMember, specific=xtend_XtendExecutable)
gen_xtend_JvmType_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=xtend_JvmType)
gen_xtend_JvmVoid_JvmType = Generalization(general=JvmType, specific=xtend_JvmVoid)
gen_xtend_JvmComponentType_JvmType = Generalization(general=JvmType, specific=xtend_JvmComponentType)
gen_xtend_JvmPrimitiveType_JvmComponentType = Generalization(general=JvmComponentType, specific=xtend_JvmPrimitiveType)
gen_xtend_JvmArrayType_JvmComponentType = Generalization(general=JvmComponentType, specific=xtend_JvmArrayType)
gen_xtend_JvmDeclaredType_JvmMember = Generalization(general=JvmMember, specific=xtend_JvmDeclaredType)
gen_xtend_JvmDeclaredType_JvmComponentType = Generalization(general=JvmComponentType, specific=xtend_JvmDeclaredType)
gen_xtend_JvmTypeParameter_JvmComponentType = Generalization(general=JvmComponentType, specific=xtend_JvmTypeParameter)
gen_xtend_JvmTypeParameter_JvmConstraintOwner = Generalization(general=JvmConstraintOwner, specific=xtend_JvmTypeParameter)
gen_xtend_JvmUpperBound_JvmTypeConstraint = Generalization(general=JvmTypeConstraint, specific=xtend_JvmUpperBound)
gen_xtend_JvmLowerBound_JvmTypeConstraint = Generalization(general=JvmTypeConstraint, specific=xtend_JvmLowerBound)
gen_xtend_JvmAnnotationType_JvmDeclaredType = Generalization(general=JvmDeclaredType, specific=xtend_JvmAnnotationType)
gen_xtend_JvmEnumerationType_JvmDeclaredType = Generalization(general=JvmDeclaredType, specific=xtend_JvmEnumerationType)
gen_xtend_JvmEnumerationLiteral_JvmField = Generalization(general=JvmField, specific=xtend_JvmEnumerationLiteral)
gen_xtend_JvmGenericType_JvmDeclaredType = Generalization(general=JvmDeclaredType, specific=xtend_JvmGenericType)
gen_xtend_JvmGenericType_JvmTypeParameterDeclarator = Generalization(general=JvmTypeParameterDeclarator, specific=xtend_JvmGenericType)
gen_xtend_JvmParameterizedTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=xtend_JvmParameterizedTypeReference)
gen_xtend_JvmGenericArrayTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=xtend_JvmGenericArrayTypeReference)
gen_xtend_JvmWildcardTypeReference_JvmConstraintOwner = Generalization(general=JvmConstraintOwner, specific=xtend_JvmWildcardTypeReference)
gen_xtend_JvmAnyTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=xtend_JvmAnyTypeReference)
gen_xtend_JvmMultiTypeReference_JvmCompoundTypeReference = Generalization(general=JvmCompoundTypeReference, specific=xtend_JvmMultiTypeReference)
gen_xtend_JvmMember_JvmAnnotationTarget = Generalization(general=JvmAnnotationTarget, specific=xtend_JvmMember)
gen_xtend_JvmMember_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=xtend_JvmMember)
gen_xtend_JvmFeature_JvmMember = Generalization(general=JvmMember, specific=xtend_JvmFeature)
gen_xtend_JvmWildcardTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=xtend_JvmWildcardTypeReference)
gen_xtend_JvmField_JvmFeature = Generalization(general=JvmFeature, specific=xtend_JvmField)
gen_xtend_JvmExecutable_JvmFeature = Generalization(general=JvmFeature, specific=xtend_JvmExecutable)
gen_xtend_JvmExecutable_JvmTypeParameterDeclarator = Generalization(general=JvmTypeParameterDeclarator, specific=xtend_JvmExecutable)
gen_xtend_JvmConstructor_JvmExecutable = Generalization(general=JvmExecutable, specific=xtend_JvmConstructor)
gen_xtend_JvmOperation_JvmExecutable = Generalization(general=JvmExecutable, specific=xtend_JvmOperation)
gen_xtend_JvmFormalParameter_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=xtend_JvmFormalParameter)
gen_xtend_JvmFormalParameter_JvmAnnotationTarget = Generalization(general=JvmAnnotationTarget, specific=xtend_JvmFormalParameter)
gen_xtend_JvmIntAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmIntAnnotationValue)
gen_xtend_JvmBooleanAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmBooleanAnnotationValue)
gen_xtend_JvmByteAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmByteAnnotationValue)
gen_xtend_JvmShortAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmShortAnnotationValue)
gen_xtend_JvmLongAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmLongAnnotationValue)
gen_xtend_JvmDoubleAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmDoubleAnnotationValue)
gen_xtend_JvmFloatAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmFloatAnnotationValue)
gen_xtend_JvmCharAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmCharAnnotationValue)
gen_xtend_JvmStringAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmStringAnnotationValue)
gen_xtend_JvmTypeAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmTypeAnnotationValue)
gen_xtend_JvmAnnotationAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmAnnotationAnnotationValue)
gen_xtend_JvmAnnotationAnnotationValue_JvmAnnotationTarget = Generalization(general=JvmAnnotationTarget, specific=xtend_JvmAnnotationAnnotationValue)
gen_xtend_JvmEnumAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmEnumAnnotationValue)
gen_xtend_JvmDelegateTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=xtend_JvmDelegateTypeReference)
gen_xtend_JvmSpecializedTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=xtend_JvmSpecializedTypeReference)
gen_xtend_JvmSynonymTypeReference_JvmCompoundTypeReference = Generalization(general=JvmCompoundTypeReference, specific=xtend_JvmSynonymTypeReference)
gen_xtend_JvmUnknownTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=xtend_JvmUnknownTypeReference)
gen_xtend_JvmCompoundTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=xtend_JvmCompoundTypeReference)
gen_xtend_JvmCustomAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=xtend_JvmCustomAnnotationValue)

# Domain Model
domain_model = DomainModel(
    name="xtend",
    types={xtend_XtendFile, xtend_XtendTypeDeclaration, xtend_JvmTypeParameter, xtend_XExpression, xtend_XtendAnnotationTarget, xtend_XAnnotation, xtend_XtendParameter, xtend_XtendMember, XtendAnnotationTarget, xtend_XtendFunction, XtendExecutable, xtend_CreateExtensionInfo, xtend_XtendClass, XtendTypeDeclaration, xtend_XtendField, XtendMember, xtend_JvmTypeReference, xtend_XtendConstructor, xtend_XtendAnnotationType, xtend_XtendInterface, xtend_RichString, XBlockExpression, xtend_RichStringLiteral, XStringLiteral, xtend_RichStringForLoop, XForLoopExpression, xtend_XtendEnum, xtend_XtendEnumLiteral, xtend_XtendVariableDeclaration, XVariableDeclaration, xtend_XtendFormalParameter, JvmFormalParameter, xtend_RichStringIf, XExpression, xtend_XIfExpression, xtend_RichStringElseIf, xtend_XSwitchExpression, JvmIdentifiableElement, xtend_XCasePart, xtend_XVariableDeclaration, xtend_XAbstractFeatureCall, xtend_JvmIdentifiableElement, xtend_XBlockExpression, xtend_XMemberFeatureCall, XAbstractFeatureCall, xtend_XFeatureCall, xtend_JvmDeclaredType, xtend_XConstructorCall, xtend_JvmConstructor, xtend_JvmFormalParameter, xtend_XCastedExpression, xtend_XBinaryOperation, xtend_XBooleanLiteral, xtend_XNullLiteral, xtend_XNumberLiteral, xtend_XStringLiteral, xtend_XClosure, xtend_XAbstractWhileExpression, xtend_XDoWhileExpression, XAbstractWhileExpression, xtend_XWhileExpression, xtend_XTypeLiteral, xtend_JvmType, xtend_XUnaryOperation, xtend_XInstanceOfExpression, xtend_XForLoopExpression, xtend_XThrowExpression, xtend_XTryCatchFinallyExpression, xtend_XAssignment, xtend_XReturnExpression, xtend_XCatchClause, xtend_AnonymousClass, xtend_XtendExecutable, JvmType, xtend_JvmComponentType, xtend_JvmArrayType, xtend_JvmPrimitiveType, JvmComponentType, JvmMember, xtend_JvmVoid, xtend_JvmMember, JvmConstraintOwner, xtend_JvmTypeParameterDeclarator, xtend_JvmConstraintOwner, xtend_JvmTypeConstraint, xtend_JvmUpperBound, JvmTypeConstraint, xtend_JvmLowerBound, xtend_JvmAnnotationType, JvmDeclaredType, xtend_JvmEnumerationType, JvmField, xtend_JvmGenericType, JvmTypeParameterDeclarator, xtend_JvmEnumerationLiteral, xtend_JvmParameterizedTypeReference, JvmTypeReference, xtend_JvmGenericArrayTypeReference, xtend_JvmAnyTypeReference, xtend_JvmMultiTypeReference, JvmCompoundTypeReference, JvmAnnotationTarget, xtend_JvmFeature, xtend_JvmWildcardTypeReference, xtend_JvmField, JvmFeature, xtend_JvmExecutable, JvmExecutable, xtend_JvmOperation, xtend_JvmAnnotationValue, xtend_JvmAnnotationTarget, xtend_JvmAnnotationReference, xtend_JvmIntAnnotationValue, JvmAnnotationValue, xtend_JvmBooleanAnnotationValue, xtend_JvmByteAnnotationValue, xtend_JvmShortAnnotationValue, xtend_JvmLongAnnotationValue, xtend_JvmDoubleAnnotationValue, xtend_JvmFloatAnnotationValue, xtend_JvmCharAnnotationValue, xtend_JvmStringAnnotationValue, xtend_JvmTypeAnnotationValue, xtend_JvmAnnotationAnnotationValue, xtend_JvmEnumAnnotationValue, xtend_JvmDelegateTypeReference, xtend_JvmSpecializedTypeReference, xtend_JvmSynonymTypeReference, xtend_JvmUnknownTypeReference, xtend_JvmCompoundTypeReference, xtend_JvmCustomAnnotationValue, JvmVisibility},
    associations={xtendTypes0, implements2, type15, typeParameters5, initialValue17, annotations7, annotationInfo8, declaringType10, returnType11, createExtensionInfo13, extends1, createExpression45, members48, parameterType19, extends49, typeParameters51, separator21, before23, after26, if_29, then31, elseIfs34, else_36, if_39, then42, cases64, default66, case69, then72, if_54, then56, else_59, switch62, type80, right82, typeGuard75, expressions78, implicitFirstArgument92, actualTypeArguments95, memberCallTarget98, feature85, typeArguments86, implicitReceiver89, featureCallArguments103, declaringType105, constructor107, arguments108, typeArguments111, memberCallArguments100, declaredFormalParameters114, expression115, implicitParameter118, type121, target123, leftOperand126, eachExpression135, declaredParam138, predicate141, body143, rightOperand128, type146, operand131, forExpression133, expression149, expression152, expression154, finallyExpression156, type147, expression161, declaredParam164, assignable167, value169, expression172, catchClauses159, typeParameters176, expression179, parameters182, constructorCall185, exceptions174, arrayType187, componentType188, superTypes189, members192, declarator194, typeParameters195, typeReference197, owner199, constraints196, literals200, arguments201, type203, componentType206, type208, declaringType210, type212, parameters214, exceptions216, returnType219, defaultValue221, parameterType223, annotations226, annotation227, target228, values229, operation232, values235, values237, values239, delegate241, equivalent243, type245, references247},
    generalizations={gen_xtend_XtendParameter_XtendAnnotationTarget, gen_xtend_XtendMember_XtendAnnotationTarget, gen_xtend_XtendFunction_XtendExecutable, gen_xtend_XtendClass_XtendTypeDeclaration, gen_xtend_XtendField_XtendMember, gen_xtend_XtendConstructor_XtendExecutable, gen_xtend_XtendTypeDeclaration_XtendMember, gen_xtend_XtendAnnotationType_XtendTypeDeclaration, gen_xtend_XtendInterface_XtendTypeDeclaration, gen_xtend_RichString_XBlockExpression, gen_xtend_RichStringLiteral_XStringLiteral, gen_xtend_RichStringForLoop_XForLoopExpression, gen_xtend_XtendEnum_XtendTypeDeclaration, gen_xtend_XtendEnumLiteral_XtendMember, gen_xtend_XtendVariableDeclaration_XVariableDeclaration, gen_xtend_XtendFormalParameter_JvmFormalParameter, gen_xtend_RichStringIf_XExpression, gen_xtend_XIfExpression_XExpression, gen_xtend_XCasePart_JvmIdentifiableElement, gen_xtend_XSwitchExpression_XExpression, gen_xtend_XSwitchExpression_JvmIdentifiableElement, gen_xtend_XVariableDeclaration_XExpression, gen_xtend_XVariableDeclaration_JvmIdentifiableElement, gen_xtend_XAbstractFeatureCall_XExpression, gen_xtend_XBlockExpression_XExpression, gen_xtend_XMemberFeatureCall_XAbstractFeatureCall, gen_xtend_XFeatureCall_XAbstractFeatureCall, gen_xtend_XConstructorCall_XExpression, gen_xtend_XCastedExpression_XExpression, gen_xtend_XBinaryOperation_XAbstractFeatureCall, gen_xtend_XBooleanLiteral_XExpression, gen_xtend_XNullLiteral_XExpression, gen_xtend_XNumberLiteral_XExpression, gen_xtend_XStringLiteral_XExpression, gen_xtend_XClosure_XExpression, gen_xtend_XAbstractWhileExpression_XExpression, gen_xtend_XDoWhileExpression_XAbstractWhileExpression, gen_xtend_XWhileExpression_XAbstractWhileExpression, gen_xtend_XTypeLiteral_XExpression, gen_xtend_XUnaryOperation_XAbstractFeatureCall, gen_xtend_XInstanceOfExpression_XExpression, gen_xtend_XForLoopExpression_XExpression, gen_xtend_XThrowExpression_XExpression, gen_xtend_XTryCatchFinallyExpression_XExpression, gen_xtend_XAssignment_XAbstractFeatureCall, gen_xtend_XReturnExpression_XExpression, gen_xtend_AnonymousClass_XExpression, gen_xtend_AnonymousClass_XtendTypeDeclaration, gen_xtend_XtendExecutable_XtendMember, gen_xtend_JvmType_JvmIdentifiableElement, gen_xtend_JvmVoid_JvmType, gen_xtend_JvmComponentType_JvmType, gen_xtend_JvmPrimitiveType_JvmComponentType, gen_xtend_JvmArrayType_JvmComponentType, gen_xtend_JvmDeclaredType_JvmMember, gen_xtend_JvmDeclaredType_JvmComponentType, gen_xtend_JvmTypeParameter_JvmComponentType, gen_xtend_JvmTypeParameter_JvmConstraintOwner, gen_xtend_JvmUpperBound_JvmTypeConstraint, gen_xtend_JvmLowerBound_JvmTypeConstraint, gen_xtend_JvmAnnotationType_JvmDeclaredType, gen_xtend_JvmEnumerationType_JvmDeclaredType, gen_xtend_JvmEnumerationLiteral_JvmField, gen_xtend_JvmGenericType_JvmDeclaredType, gen_xtend_JvmGenericType_JvmTypeParameterDeclarator, gen_xtend_JvmParameterizedTypeReference_JvmTypeReference, gen_xtend_JvmGenericArrayTypeReference_JvmTypeReference, gen_xtend_JvmWildcardTypeReference_JvmConstraintOwner, gen_xtend_JvmAnyTypeReference_JvmTypeReference, gen_xtend_JvmMultiTypeReference_JvmCompoundTypeReference, gen_xtend_JvmMember_JvmAnnotationTarget, gen_xtend_JvmMember_JvmIdentifiableElement, gen_xtend_JvmFeature_JvmMember, gen_xtend_JvmWildcardTypeReference_JvmTypeReference, gen_xtend_JvmField_JvmFeature, gen_xtend_JvmExecutable_JvmFeature, gen_xtend_JvmExecutable_JvmTypeParameterDeclarator, gen_xtend_JvmConstructor_JvmExecutable, gen_xtend_JvmOperation_JvmExecutable, gen_xtend_JvmFormalParameter_JvmIdentifiableElement, gen_xtend_JvmFormalParameter_JvmAnnotationTarget, gen_xtend_JvmIntAnnotationValue_JvmAnnotationValue, gen_xtend_JvmBooleanAnnotationValue_JvmAnnotationValue, gen_xtend_JvmByteAnnotationValue_JvmAnnotationValue, gen_xtend_JvmShortAnnotationValue_JvmAnnotationValue, gen_xtend_JvmLongAnnotationValue_JvmAnnotationValue, gen_xtend_JvmDoubleAnnotationValue_JvmAnnotationValue, gen_xtend_JvmFloatAnnotationValue_JvmAnnotationValue, gen_xtend_JvmCharAnnotationValue_JvmAnnotationValue, gen_xtend_JvmStringAnnotationValue_JvmAnnotationValue, gen_xtend_JvmTypeAnnotationValue_JvmAnnotationValue, gen_xtend_JvmAnnotationAnnotationValue_JvmAnnotationValue, gen_xtend_JvmAnnotationAnnotationValue_JvmAnnotationTarget, gen_xtend_JvmEnumAnnotationValue_JvmAnnotationValue, gen_xtend_JvmDelegateTypeReference_JvmTypeReference, gen_xtend_JvmSpecializedTypeReference_JvmTypeReference, gen_xtend_JvmSynonymTypeReference_JvmCompoundTypeReference, gen_xtend_JvmUnknownTypeReference_JvmTypeReference, gen_xtend_JvmCompoundTypeReference_JvmTypeReference, gen_xtend_JvmCustomAnnotationValue_JvmAnnotationValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)