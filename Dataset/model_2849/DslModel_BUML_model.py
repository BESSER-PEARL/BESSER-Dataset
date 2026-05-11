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
            EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PUBLIC")
    }
)

# Classes
model_types_JvmIdentifiableElement = Class(name="model_types_JvmIdentifiableElement", is_abstract=True)
model_types_JvmModule = Class(name="model_types_JvmModule")
JvmIdentifiableElement = Class(name="JvmIdentifiableElement")
XImportSection1 = Class(name="XImportSection1")
types_model_EObject = Class(name="types_model_EObject")
XExportSection = Class(name="XExportSection")
model_types_JvmNoModule = Class(name="model_types_JvmNoModule")
model_types_JvmType = Class(name="model_types_JvmType", is_abstract=True)
model_types_JvmVoid = Class(name="model_types_JvmVoid")
JvmType = Class(name="JvmType")
JvmArrayType = Class(name="JvmArrayType")
model_types_JvmPrimitiveType = Class(name="model_types_JvmPrimitiveType")
JvmComponentType = Class(name="JvmComponentType")
model_types_JvmArrayType = Class(name="model_types_JvmArrayType")
model_types_JvmDeclaredType = Class(name="model_types_JvmDeclaredType")
types_JvmMember = Class(name="types_JvmMember")
types_JvmComponentType = Class(name="types_JvmComponentType")
model_types_JvmComponentType = Class(name="model_types_JvmComponentType", is_abstract=True)
JvmTypeReference = Class(name="JvmTypeReference")
JvmMember = Class(name="JvmMember")
model_types_JvmTypeParameter = Class(name="model_types_JvmTypeParameter")
types_JvmConstraintOwner = Class(name="types_JvmConstraintOwner")
JvmTypeParameterDeclarator = Class(name="JvmTypeParameterDeclarator")
model_types_JvmTypeParameterDeclarator = Class(name="model_types_JvmTypeParameterDeclarator", is_abstract=True)
model_types_JvmUpperBound = Class(name="model_types_JvmUpperBound")
model_types_JvmLowerBound = Class(name="model_types_JvmLowerBound")
model_types_JvmAnnotationType = Class(name="model_types_JvmAnnotationType")
JvmDeclaredType = Class(name="JvmDeclaredType")
model_types_JvmEnumerationType = Class(name="model_types_JvmEnumerationType")
JvmEnumerationLiteral = Class(name="JvmEnumerationLiteral")
model_types_JvmEnumerationLiteral = Class(name="model_types_JvmEnumerationLiteral")
JvmField = Class(name="JvmField")
model_types_JvmGenericType = Class(name="model_types_JvmGenericType")
types_JvmDeclaredType = Class(name="types_JvmDeclaredType")
types_JvmTypeParameterDeclarator = Class(name="types_JvmTypeParameterDeclarator")
JvmTypeParameter = Class(name="JvmTypeParameter")
JvmParameterizedTypeReference = Class(name="JvmParameterizedTypeReference")
model_types_JvmConstraintOwner = Class(name="model_types_JvmConstraintOwner", is_abstract=True)
JvmTypeConstraint = Class(name="JvmTypeConstraint")
model_types_JvmTypeConstraint = Class(name="model_types_JvmTypeConstraint", is_abstract=True)
JvmConstraintOwner = Class(name="JvmConstraintOwner")
model_types_JvmParameterizedTypeReference = Class(name="model_types_JvmParameterizedTypeReference")
model_types_JvmGenericArrayTypeReference = Class(name="model_types_JvmGenericArrayTypeReference")
model_types_JvmWildcardTypeReference = Class(name="model_types_JvmWildcardTypeReference")
types_JvmTypeReference = Class(name="types_JvmTypeReference")
model_types_JvmAnyTypeReference = Class(name="model_types_JvmAnyTypeReference")
model_types_JvmTypeReference = Class(name="model_types_JvmTypeReference", is_abstract=True)
model_types_JvmFeature = Class(name="model_types_JvmFeature", is_abstract=True)
model_types_JvmField = Class(name="model_types_JvmField")
JvmFeature = Class(name="JvmFeature")
XExpression = Class(name="XExpression")
model_types_JvmExecutable = Class(name="model_types_JvmExecutable", is_abstract=True)
types_JvmFeature = Class(name="types_JvmFeature")
JvmFormalParameter = Class(name="JvmFormalParameter")
model_types_JvmConstructor = Class(name="model_types_JvmConstructor")
JvmExecutable = Class(name="JvmExecutable")
model_types_JvmMultiTypeReference = Class(name="model_types_JvmMultiTypeReference")
JvmCompoundTypeReference = Class(name="JvmCompoundTypeReference")
model_types_JvmMember = Class(name="model_types_JvmMember")
JvmAnnotationTarget = Class(name="JvmAnnotationTarget")
model_types_JvmFormalParameter = Class(name="model_types_JvmFormalParameter")
model_types_JvmAnnotationTarget = Class(name="model_types_JvmAnnotationTarget", is_abstract=True)
JvmAnnotationReference = Class(name="JvmAnnotationReference")
model_types_JvmAnnotationReference = Class(name="model_types_JvmAnnotationReference")
JvmAnnotationType = Class(name="JvmAnnotationType")
model_types_JvmAnnotationValue = Class(name="model_types_JvmAnnotationValue")
JvmOperation = Class(name="JvmOperation")
model_types_JvmIntAnnotationValue = Class(name="model_types_JvmIntAnnotationValue")
model_types_JvmBooleanAnnotationValue = Class(name="model_types_JvmBooleanAnnotationValue")
model_types_JvmByteAnnotationValue = Class(name="model_types_JvmByteAnnotationValue")
model_types_JvmOperation = Class(name="model_types_JvmOperation")
JvmAnnotationValue = Class(name="JvmAnnotationValue")
model_types_JvmStringAnnotationValue = Class(name="model_types_JvmStringAnnotationValue")
model_types_JvmTypeAnnotationValue = Class(name="model_types_JvmTypeAnnotationValue")
model_types_JvmAnnotationAnnotationValue = Class(name="model_types_JvmAnnotationAnnotationValue")
model_types_JvmEnumAnnotationValue = Class(name="model_types_JvmEnumAnnotationValue")
model_types_JvmDelegateTypeReference = Class(name="model_types_JvmDelegateTypeReference")
model_types_JvmSpecializedTypeReference = Class(name="model_types_JvmSpecializedTypeReference", is_abstract=True)
model_types_JvmSynonymTypeReference = Class(name="model_types_JvmSynonymTypeReference")
model_types_JvmUnknownTypeReference = Class(name="model_types_JvmUnknownTypeReference")
model_types_JvmCompoundTypeReference = Class(name="model_types_JvmCompoundTypeReference", is_abstract=True)
model_types_JvmShortAnnotationValue = Class(name="model_types_JvmShortAnnotationValue")
model_types_JvmLongAnnotationValue = Class(name="model_types_JvmLongAnnotationValue")
model_types_JvmDoubleAnnotationValue = Class(name="model_types_JvmDoubleAnnotationValue")
model_types_JvmFloatAnnotationValue = Class(name="model_types_JvmFloatAnnotationValue")
model_types_JvmCharAnnotationValue = Class(name="model_types_JvmCharAnnotationValue")
model_xbase_XSwitchExpression = Class(name="model_xbase_XSwitchExpression")
xbase_XExpression = Class(name="xbase_XExpression")
types_JvmIdentifiableElement = Class(name="types_JvmIdentifiableElement")
XCasePart = Class(name="XCasePart")
model_xbase_XCasePart = Class(name="model_xbase_XCasePart")
model_xbase_XBlockExpression = Class(name="model_xbase_XBlockExpression")
model_xbase_XVariableDeclaration = Class(name="model_xbase_XVariableDeclaration")
model_types_JvmCustomAnnotationValue = Class(name="model_types_JvmCustomAnnotationValue")
model_xbase_XExpression = Class(name="model_xbase_XExpression", is_abstract=True)
model_xbase_XIfExpression = Class(name="model_xbase_XIfExpression")
model_xbase_XMemberFeatureCall = Class(name="model_xbase_XMemberFeatureCall")
XAbstractFeatureCall = Class(name="XAbstractFeatureCall")
model_xbase_XVariableDeclarationList = Class(name="model_xbase_XVariableDeclarationList")
model_xbase_XAbstractFeatureCall = Class(name="model_xbase_XAbstractFeatureCall", is_abstract=True)
model_xbase_XFeatureCall = Class(name="model_xbase_XFeatureCall")
model_xbase_XConstructorCall = Class(name="model_xbase_XConstructorCall")
JvmConstructor = Class(name="JvmConstructor")
model_xbase_XMemberFeatureCall1 = Class(name="model_xbase_XMemberFeatureCall1")
model_xbase_XSetLiteral = Class(name="model_xbase_XSetLiteral")
model_xbase_XClosure = Class(name="model_xbase_XClosure")
model_xbase_XCastedExpression = Class(name="model_xbase_XCastedExpression")
model_xbase_XBooleanLiteral = Class(name="model_xbase_XBooleanLiteral")
model_xbase_XNullLiteral = Class(name="model_xbase_XNullLiteral")
model_xbase_XNumberLiteral = Class(name="model_xbase_XNumberLiteral")
model_xbase_XStringLiteral = Class(name="model_xbase_XStringLiteral")
model_xbase_XCollectionLiteral = Class(name="model_xbase_XCollectionLiteral", is_abstract=True)
model_xbase_XListLiteral = Class(name="model_xbase_XListLiteral")
XCollectionLiteral = Class(name="XCollectionLiteral")
model_xbase_XKeyValuePair = Class(name="model_xbase_XKeyValuePair")
model_xbase_XForLoopExpression = Class(name="model_xbase_XForLoopExpression")
model_xbase_XForEachExpression = Class(name="model_xbase_XForEachExpression")
model_xbase_XBinaryOperation = Class(name="model_xbase_XBinaryOperation")
model_xbase_XUnaryOperation = Class(name="model_xbase_XUnaryOperation")
model_xbase_XWhileExpression = Class(name="model_xbase_XWhileExpression")
model_xbase_XTypeLiteral = Class(name="model_xbase_XTypeLiteral")
model_xbase_XInstanceOfExpression = Class(name="model_xbase_XInstanceOfExpression")
model_xbase_XThrowExpression = Class(name="model_xbase_XThrowExpression")
model_xbase_XTryCatchFinallyExpression = Class(name="model_xbase_XTryCatchFinallyExpression")
model_xbase_XAbstractWhileExpression = Class(name="model_xbase_XAbstractWhileExpression", is_abstract=True)
model_xbase_XDoWhileExpression = Class(name="model_xbase_XDoWhileExpression")
XAbstractWhileExpression = Class(name="XAbstractWhileExpression")
model_xbase_XReturnExpression = Class(name="model_xbase_XReturnExpression")
model_xbase_XBreakExpression = Class(name="model_xbase_XBreakExpression")
model_xbase_XContinueExpression = Class(name="model_xbase_XContinueExpression")
model_xbase_XPrefixOperation = Class(name="model_xbase_XPrefixOperation")
model_xbase_XPostfixOperation = Class(name="model_xbase_XPostfixOperation")
XCatchClause = Class(name="XCatchClause")
model_xbase_XCatchClause = Class(name="model_xbase_XCatchClause")
model_xbase_XAssignment = Class(name="model_xbase_XAssignment")
model_xbase_XIndexOperation = Class(name="model_xbase_XIndexOperation")
model_xbase_XFunctionDeclaration = Class(name="model_xbase_XFunctionDeclaration")
model_xbase_XTernaryOperation = Class(name="model_xbase_XTernaryOperation")
model_xbase_XObjectLiteralPart = Class(name="model_xbase_XObjectLiteralPart")
model_xbase_XArrayLiteral = Class(name="model_xbase_XArrayLiteral")
model_ss_XtendFile = Class(name="model_ss_XtendFile")
XtendTypeDeclaration = Class(name="XtendTypeDeclaration")
ss_model_EObject = Class(name="ss_model_EObject")
model_ss_XtendClass = Class(name="model_ss_XtendClass")
model_xbase_XObjectLiteral = Class(name="model_xbase_XObjectLiteral")
XObjectLiteralPart = Class(name="XObjectLiteralPart")
model_ss_XtendAnnotationTarget = Class(name="model_ss_XtendAnnotationTarget", is_abstract=True)
XAnnotation = Class(name="XAnnotation")
model_ss_XtendMember = Class(name="model_ss_XtendMember")
XtendAnnotationTarget = Class(name="XtendAnnotationTarget")
model_ss_XtendFunction = Class(name="model_ss_XtendFunction")
XtendMember = Class(name="XtendMember")
model_ss_XtendField = Class(name="model_ss_XtendField")
XtendParameter = Class(name="XtendParameter")
CreateExtensionInfo = Class(name="CreateExtensionInfo")
model_ss_RichStringLiteral = Class(name="model_ss_RichStringLiteral")
XStringLiteral = Class(name="XStringLiteral")
model_ss_RichStringForLoop = Class(name="model_ss_RichStringForLoop")
XForEachExpression = Class(name="XForEachExpression")
model_ss_RichStringIf = Class(name="model_ss_RichStringIf")
model_ss_XtendParameter = Class(name="model_ss_XtendParameter")
model_ss_RichString = Class(name="model_ss_RichString")
XBlockExpression = Class(name="XBlockExpression")
RichStringElseIf = Class(name="RichStringElseIf")
model_ss_RichStringElseIf = Class(name="model_ss_RichStringElseIf")
model_ss_CreateExtensionInfo = Class(name="model_ss_CreateExtensionInfo")
model_ss_XtendConstructor = Class(name="model_ss_XtendConstructor")
model_ss_XtendAnnotationType = Class(name="model_ss_XtendAnnotationType")
model_ss_XtendInterface = Class(name="model_ss_XtendInterface")
model_ss_XtendEnum = Class(name="model_ss_XtendEnum")
model_ss_XtendEnumLiteral = Class(name="model_ss_XtendEnumLiteral")
model_ss_XtendVariableDeclaration = Class(name="model_ss_XtendVariableDeclaration")
XVariableDeclaration = Class(name="XVariableDeclaration")
model_ss_XtendFormalParameter = Class(name="model_ss_XtendFormalParameter")
model_ss_XtendDelegate = Class(name="model_ss_XtendDelegate")
model_ss_XtendEvent = Class(name="model_ss_XtendEvent")
model_ss_XtendTypeDeclaration = Class(name="model_ss_XtendTypeDeclaration")
model_xannotation_XAnnotationElementValuePair = Class(name="model_xannotation_XAnnotationElementValuePair")
model_xtype_XFunctionTypeRef = Class(name="model_xtype_XFunctionTypeRef")
JvmSpecializedTypeReference = Class(name="JvmSpecializedTypeReference")
model_xtype_XComputedTypeReference = Class(name="model_xtype_XComputedTypeReference")
model_xtype_XImportSection = Class(name="model_xtype_XImportSection")
model_xannotation_XAnnotation = Class(name="model_xannotation_XAnnotation")
XAnnotationElementValuePair = Class(name="XAnnotationElementValuePair")
model_xtype_XImportDeclaration1 = Class(name="model_xtype_XImportDeclaration1")
XImportItem = Class(name="XImportItem")
model_xtype_XImportItem = Class(name="model_xtype_XImportItem")
model_xtype_XExportSection = Class(name="model_xtype_XExportSection")
XExportDeclaration = Class(name="XExportDeclaration")
model_xtype_XExportDeclaration = Class(name="model_xtype_XExportDeclaration")
XExportItem = Class(name="XExportItem")
XImportDeclaration = Class(name="XImportDeclaration")
model_xtype_XImportDeclaration = Class(name="model_xtype_XImportDeclaration")
model_xtype_XImportSection1 = Class(name="model_xtype_XImportSection1")
XImportDeclaration1 = Class(name="XImportDeclaration1")
model_richstring_Line = Class(name="model_richstring_Line")
LinePart = Class(name="LinePart")
ProcessedRichString = Class(name="ProcessedRichString")
model_richstring_LinePart = Class(name="model_richstring_LinePart")
model_richstring_Literal = Class(name="model_richstring_Literal")
RichStringLiteral = Class(name="RichStringLiteral")
model_richstring_LineBreak = Class(name="model_richstring_LineBreak")
Literal = Class(name="Literal")
model_richstring_ForLoopStart = Class(name="model_richstring_ForLoopStart")
RichStringForLoop = Class(name="RichStringForLoop")
ForLoopEnd = Class(name="ForLoopEnd")
model_richstring_ForLoopEnd = Class(name="model_richstring_ForLoopEnd")
ForLoopStart = Class(name="ForLoopStart")
model_richstring_PrintedExpression = Class(name="model_richstring_PrintedExpression")
model_richstring_IfConditionStart = Class(name="model_richstring_IfConditionStart")
RichStringIf = Class(name="RichStringIf")
ElseStart = Class(name="ElseStart")
ElseIfCondition = Class(name="ElseIfCondition")
EndIf = Class(name="EndIf")
model_xtype_XExportItem = Class(name="model_xtype_XExportItem")
model_richstring_ProcessedRichString = Class(name="model_richstring_ProcessedRichString")
RichString = Class(name="RichString")
Line = Class(name="Line")
model_richstring_ElseIfCondition = Class(name="model_richstring_ElseIfCondition")
IfConditionStart = Class(name="IfConditionStart")
model_richstring_ElseStart = Class(name="model_richstring_ElseStart")
model_richstring_EndIf = Class(name="model_richstring_EndIf")

# model_types_JvmIdentifiableElement class attributes and methods
model_types_JvmIdentifiableElement_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
model_types_JvmIdentifiableElement_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
model_types_JvmIdentifiableElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
model_types_JvmIdentifiableElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='model_innerClassDelimiter', type=StringType)}, type=StringType)
model_types_JvmIdentifiableElement_m_isExported: Method = Method(name="isExported", parameters={}, type=BooleanType)
model_types_JvmIdentifiableElement.methods={model_types_JvmIdentifiableElement_m_getQualifiedName, model_types_JvmIdentifiableElement_m_getSimpleName, model_types_JvmIdentifiableElement_m_isExported, model_types_JvmIdentifiableElement_m_getQualifiedName, model_types_JvmIdentifiableElement_m_getIdentifier}

# model_types_JvmModule class attributes and methods
model_types_JvmModule_simpleName: Property = Property(name="simpleName", type=StringType)
model_types_JvmModule.attributes={model_types_JvmModule_simpleName}

# JvmIdentifiableElement class attributes and methods

# XImportSection1 class attributes and methods

# types_model_EObject class attributes and methods

# XExportSection class attributes and methods

# model_types_JvmNoModule class attributes and methods

# model_types_JvmType class attributes and methods

# model_types_JvmVoid class attributes and methods

# JvmType class attributes and methods

# JvmArrayType class attributes and methods

# model_types_JvmPrimitiveType class attributes and methods
model_types_JvmPrimitiveType_simpleName: Property = Property(name="simpleName", type=StringType)
model_types_JvmPrimitiveType.attributes={model_types_JvmPrimitiveType_simpleName}

# JvmComponentType class attributes and methods

# model_types_JvmArrayType class attributes and methods
model_types_JvmArrayType_m_getDimensions: Method = Method(name="getDimensions", parameters={}, type=IntegerType)
model_types_JvmArrayType.methods={model_types_JvmArrayType_m_getDimensions}

# model_types_JvmDeclaredType class attributes and methods
model_types_JvmDeclaredType_abstract: Property = Property(name="abstract", type=BooleanType)
model_types_JvmDeclaredType_static: Property = Property(name="static", type=BooleanType)
model_types_JvmDeclaredType_final: Property = Property(name="final", type=BooleanType)
model_types_JvmDeclaredType_packageName: Property = Property(name="packageName", type=StringType)
model_types_JvmDeclaredType_exported: Property = Property(name="exported", type=BooleanType)
model_types_JvmDeclaredType_m_getDeclaredOperations: Method = Method(name="getDeclaredOperations", parameters={})
model_types_JvmDeclaredType_m_getDeclaredFields: Method = Method(name="getDeclaredFields", parameters={})
model_types_JvmDeclaredType_m_findAllFeaturesByName: Method = Method(name="findAllFeaturesByName", parameters={Parameter(name='model_simpleName', type=StringType)})
model_types_JvmDeclaredType_m_getAllFeatures: Method = Method(name="getAllFeatures", parameters={})
model_types_JvmDeclaredType.attributes={model_types_JvmDeclaredType_exported, model_types_JvmDeclaredType_final, model_types_JvmDeclaredType_static, model_types_JvmDeclaredType_abstract, model_types_JvmDeclaredType_packageName}
model_types_JvmDeclaredType.methods={model_types_JvmDeclaredType_m_getAllFeatures, model_types_JvmDeclaredType_m_getDeclaredOperations, model_types_JvmDeclaredType_m_findAllFeaturesByName, model_types_JvmDeclaredType_m_getDeclaredFields}

# types_JvmMember class attributes and methods

# types_JvmComponentType class attributes and methods

# model_types_JvmComponentType class attributes and methods

# JvmTypeReference class attributes and methods

# JvmMember class attributes and methods

# model_types_JvmTypeParameter class attributes and methods
model_types_JvmTypeParameter_name: Property = Property(name="name", type=StringType)
model_types_JvmTypeParameter.attributes={model_types_JvmTypeParameter_name}

# types_JvmConstraintOwner class attributes and methods

# JvmTypeParameterDeclarator class attributes and methods

# model_types_JvmTypeParameterDeclarator class attributes and methods

# model_types_JvmUpperBound class attributes and methods

# model_types_JvmLowerBound class attributes and methods

# model_types_JvmAnnotationType class attributes and methods

# JvmDeclaredType class attributes and methods

# model_types_JvmEnumerationType class attributes and methods

# JvmEnumerationLiteral class attributes and methods

# model_types_JvmEnumerationLiteral class attributes and methods
model_types_JvmEnumerationLiteral_m_getEnumType: Method = Method(name="getEnumType", parameters={}, type=StringType)
model_types_JvmEnumerationLiteral.methods={model_types_JvmEnumerationLiteral_m_getEnumType}

# JvmField class attributes and methods

# model_types_JvmGenericType class attributes and methods
model_types_JvmGenericType_interface: Property = Property(name="interface", type=BooleanType)
model_types_JvmGenericType_strictFloatingPoint: Property = Property(name="strictFloatingPoint", type=BooleanType)
model_types_JvmGenericType_m_getExtendedInterfaces: Method = Method(name="getExtendedInterfaces", parameters={})
model_types_JvmGenericType_m_getExtendedClass: Method = Method(name="getExtendedClass", parameters={}, type=StringType)
model_types_JvmGenericType_m_isInstantiateable: Method = Method(name="isInstantiateable", parameters={}, type=BooleanType)
model_types_JvmGenericType_m_getDeclaredConstructors: Method = Method(name="getDeclaredConstructors", parameters={})
model_types_JvmGenericType.attributes={model_types_JvmGenericType_strictFloatingPoint, model_types_JvmGenericType_interface}
model_types_JvmGenericType.methods={model_types_JvmGenericType_m_getExtendedClass, model_types_JvmGenericType_m_getExtendedInterfaces, model_types_JvmGenericType_m_isInstantiateable, model_types_JvmGenericType_m_getDeclaredConstructors}

# types_JvmDeclaredType class attributes and methods

# types_JvmTypeParameterDeclarator class attributes and methods

# JvmTypeParameter class attributes and methods

# JvmParameterizedTypeReference class attributes and methods

# model_types_JvmConstraintOwner class attributes and methods

# JvmTypeConstraint class attributes and methods

# model_types_JvmTypeConstraint class attributes and methods
model_types_JvmTypeConstraint_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
model_types_JvmTypeConstraint_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
model_types_JvmTypeConstraint_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
model_types_JvmTypeConstraint_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='model_innerClassDelimiter', type=StringType)}, type=StringType)
model_types_JvmTypeConstraint.methods={model_types_JvmTypeConstraint_m_getQualifiedName, model_types_JvmTypeConstraint_m_getSimpleName, model_types_JvmTypeConstraint_m_getQualifiedName, model_types_JvmTypeConstraint_m_getIdentifier}

# JvmConstraintOwner class attributes and methods

# model_types_JvmParameterizedTypeReference class attributes and methods

# model_types_JvmGenericArrayTypeReference class attributes and methods
model_types_JvmGenericArrayTypeReference_m_getDimensions: Method = Method(name="getDimensions", parameters={}, type=IntegerType)
model_types_JvmGenericArrayTypeReference_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
model_types_JvmGenericArrayTypeReference.methods={model_types_JvmGenericArrayTypeReference_m_getType, model_types_JvmGenericArrayTypeReference_m_getDimensions}

# model_types_JvmWildcardTypeReference class attributes and methods

# types_JvmTypeReference class attributes and methods

# model_types_JvmAnyTypeReference class attributes and methods

# model_types_JvmTypeReference class attributes and methods
model_types_JvmTypeReference_m_accept: Method = Method(name="accept", parameters={Parameter(name='model_parameter', type=StringType), Parameter(name='model_visitor', type=StringType)})
model_types_JvmTypeReference_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
model_types_JvmTypeReference_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
model_types_JvmTypeReference_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
model_types_JvmTypeReference_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
model_types_JvmTypeReference_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='model_innerClassDelimiter', type=StringType)}, type=StringType)
model_types_JvmTypeReference_m_accept: Method = Method(name="accept", parameters={Parameter(name='model_visitor', type=StringType)})
model_types_JvmTypeReference.methods={model_types_JvmTypeReference_m_getType, model_types_JvmTypeReference_m_getQualifiedName, model_types_JvmTypeReference_m_accept, model_types_JvmTypeReference_m_getIdentifier, model_types_JvmTypeReference_m_getSimpleName, model_types_JvmTypeReference_m_getQualifiedName, model_types_JvmTypeReference_m_accept}

# model_types_JvmFeature class attributes and methods
model_types_JvmFeature_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
model_types_JvmFeature.methods={model_types_JvmFeature_m_isStatic}

# model_types_JvmField class attributes and methods
model_types_JvmField_static: Property = Property(name="static", type=BooleanType)
model_types_JvmField_final: Property = Property(name="final", type=BooleanType)
model_types_JvmField_volatile: Property = Property(name="volatile", type=BooleanType)
model_types_JvmField_transient: Property = Property(name="transient", type=BooleanType)
model_types_JvmField.attributes={model_types_JvmField_static, model_types_JvmField_volatile, model_types_JvmField_final, model_types_JvmField_transient}

# JvmFeature class attributes and methods

# XExpression class attributes and methods

# model_types_JvmExecutable class attributes and methods
model_types_JvmExecutable_varArgs: Property = Property(name="varArgs", type=BooleanType)
model_types_JvmExecutable.attributes={model_types_JvmExecutable_varArgs}

# types_JvmFeature class attributes and methods

# JvmFormalParameter class attributes and methods

# model_types_JvmConstructor class attributes and methods

# JvmExecutable class attributes and methods

# model_types_JvmMultiTypeReference class attributes and methods

# JvmCompoundTypeReference class attributes and methods

# model_types_JvmMember class attributes and methods
model_types_JvmMember_modifiers: Property = Property(name="modifiers", type=StringType)
model_types_JvmMember_visibility: Property = Property(name="visibility", type=StringType)
model_types_JvmMember_simpleName: Property = Property(name="simpleName", type=StringType)
model_types_JvmMember_identifier: Property = Property(name="identifier", type=StringType)
model_types_JvmMember_m_internalSetIdentifier: Method = Method(name="internalSetIdentifier", parameters={Parameter(name='model_identifier', type=StringType)})
model_types_JvmMember.attributes={model_types_JvmMember_visibility, model_types_JvmMember_modifiers, model_types_JvmMember_identifier, model_types_JvmMember_simpleName}
model_types_JvmMember.methods={model_types_JvmMember_m_internalSetIdentifier}

# JvmAnnotationTarget class attributes and methods

# model_types_JvmFormalParameter class attributes and methods
model_types_JvmFormalParameter_name: Property = Property(name="name", type=StringType)
model_types_JvmFormalParameter_varArg: Property = Property(name="varArg", type=BooleanType)
model_types_JvmFormalParameter.attributes={model_types_JvmFormalParameter_varArg, model_types_JvmFormalParameter_name}

# model_types_JvmAnnotationTarget class attributes and methods

# JvmAnnotationReference class attributes and methods

# model_types_JvmAnnotationReference class attributes and methods

# JvmAnnotationType class attributes and methods

# model_types_JvmAnnotationValue class attributes and methods
model_types_JvmAnnotationValue_m_getValueName: Method = Method(name="getValueName", parameters={}, type=StringType)
model_types_JvmAnnotationValue.methods={model_types_JvmAnnotationValue_m_getValueName}

# JvmOperation class attributes and methods

# model_types_JvmIntAnnotationValue class attributes and methods
model_types_JvmIntAnnotationValue_values: Property = Property(name="values", type=IntegerType)
model_types_JvmIntAnnotationValue.attributes={model_types_JvmIntAnnotationValue_values}

# model_types_JvmBooleanAnnotationValue class attributes and methods
model_types_JvmBooleanAnnotationValue_values: Property = Property(name="values", type=BooleanType)
model_types_JvmBooleanAnnotationValue.attributes={model_types_JvmBooleanAnnotationValue_values}

# model_types_JvmByteAnnotationValue class attributes and methods
model_types_JvmByteAnnotationValue_values: Property = Property(name="values", type=StringType)
model_types_JvmByteAnnotationValue.attributes={model_types_JvmByteAnnotationValue_values}

# model_types_JvmOperation class attributes and methods
model_types_JvmOperation_static: Property = Property(name="static", type=BooleanType)
model_types_JvmOperation_final: Property = Property(name="final", type=BooleanType)
model_types_JvmOperation_abstract: Property = Property(name="abstract", type=BooleanType)
model_types_JvmOperation_synchronized: Property = Property(name="synchronized", type=BooleanType)
model_types_JvmOperation_default: Property = Property(name="default", type=BooleanType)
model_types_JvmOperation_native: Property = Property(name="native", type=BooleanType)
model_types_JvmOperation_strictFloatingPoint: Property = Property(name="strictFloatingPoint", type=BooleanType)
model_types_JvmOperation.attributes={model_types_JvmOperation_abstract, model_types_JvmOperation_synchronized, model_types_JvmOperation_static, model_types_JvmOperation_default, model_types_JvmOperation_strictFloatingPoint, model_types_JvmOperation_native, model_types_JvmOperation_final}

# JvmAnnotationValue class attributes and methods

# model_types_JvmStringAnnotationValue class attributes and methods
model_types_JvmStringAnnotationValue_values: Property = Property(name="values", type=StringType)
model_types_JvmStringAnnotationValue.attributes={model_types_JvmStringAnnotationValue_values}

# model_types_JvmTypeAnnotationValue class attributes and methods

# model_types_JvmAnnotationAnnotationValue class attributes and methods

# model_types_JvmEnumAnnotationValue class attributes and methods

# model_types_JvmDelegateTypeReference class attributes and methods

# model_types_JvmSpecializedTypeReference class attributes and methods

# model_types_JvmSynonymTypeReference class attributes and methods

# model_types_JvmUnknownTypeReference class attributes and methods
model_types_JvmUnknownTypeReference_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
model_types_JvmUnknownTypeReference.attributes={model_types_JvmUnknownTypeReference_qualifiedName}

# model_types_JvmCompoundTypeReference class attributes and methods

# model_types_JvmShortAnnotationValue class attributes and methods
model_types_JvmShortAnnotationValue_values: Property = Property(name="values", type=StringType)
model_types_JvmShortAnnotationValue.attributes={model_types_JvmShortAnnotationValue_values}

# model_types_JvmLongAnnotationValue class attributes and methods
model_types_JvmLongAnnotationValue_values: Property = Property(name="values", type=StringType)
model_types_JvmLongAnnotationValue.attributes={model_types_JvmLongAnnotationValue_values}

# model_types_JvmDoubleAnnotationValue class attributes and methods
model_types_JvmDoubleAnnotationValue_values: Property = Property(name="values", type=FloatType)
model_types_JvmDoubleAnnotationValue.attributes={model_types_JvmDoubleAnnotationValue_values}

# model_types_JvmFloatAnnotationValue class attributes and methods
model_types_JvmFloatAnnotationValue_values: Property = Property(name="values", type=FloatType)
model_types_JvmFloatAnnotationValue.attributes={model_types_JvmFloatAnnotationValue_values}

# model_types_JvmCharAnnotationValue class attributes and methods
model_types_JvmCharAnnotationValue_values: Property = Property(name="values", type=StringType)
model_types_JvmCharAnnotationValue.attributes={model_types_JvmCharAnnotationValue_values}

# model_xbase_XSwitchExpression class attributes and methods
model_xbase_XSwitchExpression_localVarName: Property = Property(name="localVarName", type=StringType)
model_xbase_XSwitchExpression.attributes={model_xbase_XSwitchExpression_localVarName}

# xbase_XExpression class attributes and methods

# types_JvmIdentifiableElement class attributes and methods

# XCasePart class attributes and methods

# model_xbase_XCasePart class attributes and methods

# model_xbase_XBlockExpression class attributes and methods

# model_xbase_XVariableDeclaration class attributes and methods
model_xbase_XVariableDeclaration_name: Property = Property(name="name", type=StringType)
model_xbase_XVariableDeclaration_writeable: Property = Property(name="writeable", type=BooleanType)
model_xbase_XVariableDeclaration_exported: Property = Property(name="exported", type=BooleanType)
model_xbase_XVariableDeclaration.attributes={model_xbase_XVariableDeclaration_exported, model_xbase_XVariableDeclaration_name, model_xbase_XVariableDeclaration_writeable}

# model_types_JvmCustomAnnotationValue class attributes and methods
model_types_JvmCustomAnnotationValue_values: Property = Property(name="values", type=StringType)
model_types_JvmCustomAnnotationValue.attributes={model_types_JvmCustomAnnotationValue_values}

# model_xbase_XExpression class attributes and methods

# model_xbase_XIfExpression class attributes and methods

# model_xbase_XMemberFeatureCall class attributes and methods
model_xbase_XMemberFeatureCall_explicitOperationCall: Property = Property(name="explicitOperationCall", type=BooleanType)
model_xbase_XMemberFeatureCall_explicitStatic: Property = Property(name="explicitStatic", type=BooleanType)
model_xbase_XMemberFeatureCall_nullSafe: Property = Property(name="nullSafe", type=BooleanType)
model_xbase_XMemberFeatureCall_typeLiteral: Property = Property(name="typeLiteral", type=BooleanType)
model_xbase_XMemberFeatureCall_staticWithDeclaringType: Property = Property(name="staticWithDeclaringType", type=BooleanType)
model_xbase_XMemberFeatureCall_packageFragment: Property = Property(name="packageFragment", type=BooleanType)
model_xbase_XMemberFeatureCall_indexedOperation: Property = Property(name="indexedOperation", type=BooleanType)
model_xbase_XMemberFeatureCall.attributes={model_xbase_XMemberFeatureCall_nullSafe, model_xbase_XMemberFeatureCall_explicitOperationCall, model_xbase_XMemberFeatureCall_packageFragment, model_xbase_XMemberFeatureCall_explicitStatic, model_xbase_XMemberFeatureCall_staticWithDeclaringType, model_xbase_XMemberFeatureCall_indexedOperation, model_xbase_XMemberFeatureCall_typeLiteral}

# XAbstractFeatureCall class attributes and methods

# model_xbase_XVariableDeclarationList class attributes and methods
model_xbase_XVariableDeclarationList_writeable: Property = Property(name="writeable", type=BooleanType)
model_xbase_XVariableDeclarationList_exported: Property = Property(name="exported", type=BooleanType)
model_xbase_XVariableDeclarationList.attributes={model_xbase_XVariableDeclarationList_exported, model_xbase_XVariableDeclarationList_writeable}

# model_xbase_XAbstractFeatureCall class attributes and methods
model_xbase_XAbstractFeatureCall_invalidFeatureIssueCode: Property = Property(name="invalidFeatureIssueCode", type=StringType)
model_xbase_XAbstractFeatureCall_validFeature: Property = Property(name="validFeature", type=BooleanType)
model_xbase_XAbstractFeatureCall_m_isExplicitOperationCallOrBuilderSyntax: Method = Method(name="isExplicitOperationCallOrBuilderSyntax", parameters={}, type=BooleanType)
model_xbase_XAbstractFeatureCall_m_getActualReceiver: Method = Method(name="getActualReceiver", parameters={}, type=StringType)
model_xbase_XAbstractFeatureCall_m_getActualArguments: Method = Method(name="getActualArguments", parameters={}, type=StringType)
model_xbase_XAbstractFeatureCall_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
model_xbase_XAbstractFeatureCall_m_isExtension: Method = Method(name="isExtension", parameters={}, type=BooleanType)
model_xbase_XAbstractFeatureCall_m_isPackageFragment: Method = Method(name="isPackageFragment", parameters={}, type=BooleanType)
model_xbase_XAbstractFeatureCall_m_isTypeLiteral: Method = Method(name="isTypeLiteral", parameters={}, type=BooleanType)
model_xbase_XAbstractFeatureCall_m_getConcreteSyntaxFeatureName: Method = Method(name="getConcreteSyntaxFeatureName", parameters={}, type=StringType)
model_xbase_XAbstractFeatureCall_m_getExplicitArguments: Method = Method(name="getExplicitArguments", parameters={}, type=StringType)
model_xbase_XAbstractFeatureCall.attributes={model_xbase_XAbstractFeatureCall_validFeature, model_xbase_XAbstractFeatureCall_invalidFeatureIssueCode}
model_xbase_XAbstractFeatureCall.methods={model_xbase_XAbstractFeatureCall_m_getActualReceiver, model_xbase_XAbstractFeatureCall_m_isExtension, model_xbase_XAbstractFeatureCall_m_getExplicitArguments, model_xbase_XAbstractFeatureCall_m_getConcreteSyntaxFeatureName, model_xbase_XAbstractFeatureCall_m_isTypeLiteral, model_xbase_XAbstractFeatureCall_m_isExplicitOperationCallOrBuilderSyntax, model_xbase_XAbstractFeatureCall_m_isPackageFragment, model_xbase_XAbstractFeatureCall_m_getActualArguments, model_xbase_XAbstractFeatureCall_m_isStatic}

# model_xbase_XFeatureCall class attributes and methods
model_xbase_XFeatureCall_explicitOperationCall: Property = Property(name="explicitOperationCall", type=BooleanType)
model_xbase_XFeatureCall_typeLiteral: Property = Property(name="typeLiteral", type=BooleanType)
model_xbase_XFeatureCall_packageFragment: Property = Property(name="packageFragment", type=BooleanType)
model_xbase_XFeatureCall_indexedOperation: Property = Property(name="indexedOperation", type=BooleanType)
model_xbase_XFeatureCall.attributes={model_xbase_XFeatureCall_typeLiteral, model_xbase_XFeatureCall_indexedOperation, model_xbase_XFeatureCall_explicitOperationCall, model_xbase_XFeatureCall_packageFragment}

# model_xbase_XConstructorCall class attributes and methods
model_xbase_XConstructorCall_invalidFeatureIssueCode: Property = Property(name="invalidFeatureIssueCode", type=StringType)
model_xbase_XConstructorCall_validFeature: Property = Property(name="validFeature", type=BooleanType)
model_xbase_XConstructorCall.attributes={model_xbase_XConstructorCall_invalidFeatureIssueCode, model_xbase_XConstructorCall_validFeature}

# JvmConstructor class attributes and methods

# model_xbase_XMemberFeatureCall1 class attributes and methods
model_xbase_XMemberFeatureCall1_explicitOperationCall: Property = Property(name="explicitOperationCall", type=BooleanType)
model_xbase_XMemberFeatureCall1_explicitStatic: Property = Property(name="explicitStatic", type=BooleanType)
model_xbase_XMemberFeatureCall1_nullSafe: Property = Property(name="nullSafe", type=BooleanType)
model_xbase_XMemberFeatureCall1_typeLiteral: Property = Property(name="typeLiteral", type=BooleanType)
model_xbase_XMemberFeatureCall1_staticWithDeclaringType: Property = Property(name="staticWithDeclaringType", type=BooleanType)
model_xbase_XMemberFeatureCall1_packageFragment: Property = Property(name="packageFragment", type=BooleanType)
model_xbase_XMemberFeatureCall1_indexedOperation: Property = Property(name="indexedOperation", type=BooleanType)
model_xbase_XMemberFeatureCall1.attributes={model_xbase_XMemberFeatureCall1_explicitStatic, model_xbase_XMemberFeatureCall1_staticWithDeclaringType, model_xbase_XMemberFeatureCall1_packageFragment, model_xbase_XMemberFeatureCall1_explicitOperationCall, model_xbase_XMemberFeatureCall1_nullSafe, model_xbase_XMemberFeatureCall1_indexedOperation, model_xbase_XMemberFeatureCall1_typeLiteral}

# model_xbase_XSetLiteral class attributes and methods

# model_xbase_XClosure class attributes and methods
model_xbase_XClosure_explicitSyntax: Property = Property(name="explicitSyntax", type=BooleanType)
model_xbase_XClosure_name: Property = Property(name="name", type=StringType)
model_xbase_XClosure_operator: Property = Property(name="operator", type=BooleanType)
model_xbase_XClosure_exported: Property = Property(name="exported", type=BooleanType)
model_xbase_XClosure_m_getFormalParameters: Method = Method(name="getFormalParameters", parameters={}, type=StringType)
model_xbase_XClosure.attributes={model_xbase_XClosure_name, model_xbase_XClosure_exported, model_xbase_XClosure_operator, model_xbase_XClosure_explicitSyntax}
model_xbase_XClosure.methods={model_xbase_XClosure_m_getFormalParameters}

# model_xbase_XCastedExpression class attributes and methods

# model_xbase_XBooleanLiteral class attributes and methods
model_xbase_XBooleanLiteral_isTrue: Property = Property(name="isTrue", type=BooleanType)
model_xbase_XBooleanLiteral.attributes={model_xbase_XBooleanLiteral_isTrue}

# model_xbase_XNullLiteral class attributes and methods

# model_xbase_XNumberLiteral class attributes and methods
model_xbase_XNumberLiteral_value: Property = Property(name="value", type=StringType)
model_xbase_XNumberLiteral.attributes={model_xbase_XNumberLiteral_value}

# model_xbase_XStringLiteral class attributes and methods
model_xbase_XStringLiteral_value: Property = Property(name="value", type=StringType)
model_xbase_XStringLiteral.attributes={model_xbase_XStringLiteral_value}

# model_xbase_XCollectionLiteral class attributes and methods

# model_xbase_XListLiteral class attributes and methods

# XCollectionLiteral class attributes and methods

# model_xbase_XKeyValuePair class attributes and methods
model_xbase_XKeyValuePair_key1: Property = Property(name="key1", type=StringType)
model_xbase_XKeyValuePair.attributes={model_xbase_XKeyValuePair_key1}

# model_xbase_XForLoopExpression class attributes and methods

# model_xbase_XForEachExpression class attributes and methods

# model_xbase_XBinaryOperation class attributes and methods

# model_xbase_XUnaryOperation class attributes and methods

# model_xbase_XWhileExpression class attributes and methods

# model_xbase_XTypeLiteral class attributes and methods
model_xbase_XTypeLiteral_arrayDimensions: Property = Property(name="arrayDimensions", type=StringType)
model_xbase_XTypeLiteral.attributes={model_xbase_XTypeLiteral_arrayDimensions}

# model_xbase_XInstanceOfExpression class attributes and methods

# model_xbase_XThrowExpression class attributes and methods

# model_xbase_XTryCatchFinallyExpression class attributes and methods

# model_xbase_XAbstractWhileExpression class attributes and methods

# model_xbase_XDoWhileExpression class attributes and methods

# XAbstractWhileExpression class attributes and methods

# model_xbase_XReturnExpression class attributes and methods

# model_xbase_XBreakExpression class attributes and methods

# model_xbase_XContinueExpression class attributes and methods

# model_xbase_XPrefixOperation class attributes and methods

# model_xbase_XPostfixOperation class attributes and methods

# XCatchClause class attributes and methods

# model_xbase_XCatchClause class attributes and methods

# model_xbase_XAssignment class attributes and methods
model_xbase_XAssignment_explicitStatic: Property = Property(name="explicitStatic", type=BooleanType)
model_xbase_XAssignment.attributes={model_xbase_XAssignment_explicitStatic}

# model_xbase_XIndexOperation class attributes and methods

# model_xbase_XFunctionDeclaration class attributes and methods
model_xbase_XFunctionDeclaration_name: Property = Property(name="name", type=StringType)
model_xbase_XFunctionDeclaration.attributes={model_xbase_XFunctionDeclaration_name}

# model_xbase_XTernaryOperation class attributes and methods

# model_xbase_XObjectLiteralPart class attributes and methods
model_xbase_XObjectLiteralPart_name: Property = Property(name="name", type=StringType)
model_xbase_XObjectLiteralPart.attributes={model_xbase_XObjectLiteralPart_name}

# model_xbase_XArrayLiteral class attributes and methods

# model_ss_XtendFile class attributes and methods
model_ss_XtendFile_package: Property = Property(name="package", type=StringType)
model_ss_XtendFile.attributes={model_ss_XtendFile_package}

# XtendTypeDeclaration class attributes and methods

# ss_model_EObject class attributes and methods

# model_ss_XtendClass class attributes and methods
model_ss_XtendClass_m_isAbstract: Method = Method(name="isAbstract", parameters={}, type=BooleanType)
model_ss_XtendClass.methods={model_ss_XtendClass_m_isAbstract}

# model_xbase_XObjectLiteral class attributes and methods

# XObjectLiteralPart class attributes and methods

# model_ss_XtendAnnotationTarget class attributes and methods

# XAnnotation class attributes and methods

# model_ss_XtendMember class attributes and methods
model_ss_XtendMember_modifiers: Property = Property(name="modifiers", type=StringType)
model_ss_XtendMember_m_getVisibility: Method = Method(name="getVisibility", parameters={}, type=StringType)
model_ss_XtendMember_m_getDeclaredVisibility: Method = Method(name="getDeclaredVisibility", parameters={}, type=StringType)
model_ss_XtendMember_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
model_ss_XtendMember_m_isFinal: Method = Method(name="isFinal", parameters={}, type=BooleanType)
model_ss_XtendMember.attributes={model_ss_XtendMember_modifiers}
model_ss_XtendMember.methods={model_ss_XtendMember_m_isFinal, model_ss_XtendMember_m_isStatic, model_ss_XtendMember_m_getVisibility, model_ss_XtendMember_m_getDeclaredVisibility}

# XtendAnnotationTarget class attributes and methods

# model_ss_XtendFunction class attributes and methods
model_ss_XtendFunction_name: Property = Property(name="name", type=StringType)
model_ss_XtendFunction_m_isAbstract: Method = Method(name="isAbstract", parameters={}, type=BooleanType)
model_ss_XtendFunction_m_isOverride: Method = Method(name="isOverride", parameters={}, type=BooleanType)
model_ss_XtendFunction_m_isDispatch: Method = Method(name="isDispatch", parameters={}, type=BooleanType)
model_ss_XtendFunction.attributes={model_ss_XtendFunction_name}
model_ss_XtendFunction.methods={model_ss_XtendFunction_m_isDispatch, model_ss_XtendFunction_m_isAbstract, model_ss_XtendFunction_m_isOverride}

# XtendMember class attributes and methods

# model_ss_XtendField class attributes and methods
model_ss_XtendField_name: Property = Property(name="name", type=StringType)
model_ss_XtendField_m_isExtension: Method = Method(name="isExtension", parameters={}, type=BooleanType)
model_ss_XtendField.attributes={model_ss_XtendField_name}
model_ss_XtendField.methods={model_ss_XtendField_m_isExtension}

# XtendParameter class attributes and methods

# CreateExtensionInfo class attributes and methods

# model_ss_RichStringLiteral class attributes and methods

# XStringLiteral class attributes and methods

# model_ss_RichStringForLoop class attributes and methods

# XForEachExpression class attributes and methods

# model_ss_RichStringIf class attributes and methods

# model_ss_XtendParameter class attributes and methods
model_ss_XtendParameter_name: Property = Property(name="name", type=StringType)
model_ss_XtendParameter_varArg: Property = Property(name="varArg", type=BooleanType)
model_ss_XtendParameter_extension: Property = Property(name="extension", type=BooleanType)
model_ss_XtendParameter.attributes={model_ss_XtendParameter_name, model_ss_XtendParameter_extension, model_ss_XtendParameter_varArg}

# model_ss_RichString class attributes and methods

# XBlockExpression class attributes and methods

# RichStringElseIf class attributes and methods

# model_ss_RichStringElseIf class attributes and methods

# model_ss_CreateExtensionInfo class attributes and methods
model_ss_CreateExtensionInfo_name: Property = Property(name="name", type=StringType)
model_ss_CreateExtensionInfo.attributes={model_ss_CreateExtensionInfo_name}

# model_ss_XtendConstructor class attributes and methods

# model_ss_XtendAnnotationType class attributes and methods

# model_ss_XtendInterface class attributes and methods

# model_ss_XtendEnum class attributes and methods

# model_ss_XtendEnumLiteral class attributes and methods
model_ss_XtendEnumLiteral_name: Property = Property(name="name", type=StringType)
model_ss_XtendEnumLiteral.attributes={model_ss_XtendEnumLiteral_name}

# model_ss_XtendVariableDeclaration class attributes and methods
model_ss_XtendVariableDeclaration_extension: Property = Property(name="extension", type=BooleanType)
model_ss_XtendVariableDeclaration.attributes={model_ss_XtendVariableDeclaration_extension}

# XVariableDeclaration class attributes and methods

# model_ss_XtendFormalParameter class attributes and methods
model_ss_XtendFormalParameter_extension: Property = Property(name="extension", type=BooleanType)
model_ss_XtendFormalParameter.attributes={model_ss_XtendFormalParameter_extension}

# model_ss_XtendDelegate class attributes and methods

# model_ss_XtendEvent class attributes and methods
model_ss_XtendEvent_name: Property = Property(name="name", type=StringType)
model_ss_XtendEvent_m_isExtension: Method = Method(name="isExtension", parameters={}, type=BooleanType)
model_ss_XtendEvent.attributes={model_ss_XtendEvent_name}
model_ss_XtendEvent.methods={model_ss_XtendEvent_m_isExtension}

# model_ss_XtendTypeDeclaration class attributes and methods
model_ss_XtendTypeDeclaration_name: Property = Property(name="name", type=StringType)
model_ss_XtendTypeDeclaration.attributes={model_ss_XtendTypeDeclaration_name}

# model_xannotation_XAnnotationElementValuePair class attributes and methods

# model_xtype_XFunctionTypeRef class attributes and methods
model_xtype_XFunctionTypeRef_instanceContext: Property = Property(name="instanceContext", type=BooleanType)
model_xtype_XFunctionTypeRef.attributes={model_xtype_XFunctionTypeRef_instanceContext}

# JvmSpecializedTypeReference class attributes and methods

# model_xtype_XComputedTypeReference class attributes and methods
model_xtype_XComputedTypeReference_typeProvider: Property = Property(name="typeProvider", type=StringType)
model_xtype_XComputedTypeReference.attributes={model_xtype_XComputedTypeReference_typeProvider}

# model_xtype_XImportSection class attributes and methods

# model_xannotation_XAnnotation class attributes and methods

# XAnnotationElementValuePair class attributes and methods

# model_xtype_XImportDeclaration1 class attributes and methods
model_xtype_XImportDeclaration1_alias: Property = Property(name="alias", type=StringType)
model_xtype_XImportDeclaration1_importURI: Property = Property(name="importURI", type=StringType)
model_xtype_XImportDeclaration1_m_isWildcard: Method = Method(name="isWildcard", parameters={}, type=BooleanType)
model_xtype_XImportDeclaration1.attributes={model_xtype_XImportDeclaration1_importURI, model_xtype_XImportDeclaration1_alias}
model_xtype_XImportDeclaration1.methods={model_xtype_XImportDeclaration1_m_isWildcard}

# XImportItem class attributes and methods

# model_xtype_XImportItem class attributes and methods
model_xtype_XImportItem_alias: Property = Property(name="alias", type=StringType)
model_xtype_XImportItem.attributes={model_xtype_XImportItem_alias}

# model_xtype_XExportSection class attributes and methods

# XExportDeclaration class attributes and methods

# model_xtype_XExportDeclaration class attributes and methods
model_xtype_XExportDeclaration_alias: Property = Property(name="alias", type=StringType)
model_xtype_XExportDeclaration_wildcard: Property = Property(name="wildcard", type=BooleanType)
model_xtype_XExportDeclaration_importURI: Property = Property(name="importURI", type=StringType)
model_xtype_XExportDeclaration.attributes={model_xtype_XExportDeclaration_wildcard, model_xtype_XExportDeclaration_alias, model_xtype_XExportDeclaration_importURI}

# XExportItem class attributes and methods

# XImportDeclaration class attributes and methods

# model_xtype_XImportDeclaration class attributes and methods
model_xtype_XImportDeclaration_extension: Property = Property(name="extension", type=BooleanType)
model_xtype_XImportDeclaration_static: Property = Property(name="static", type=BooleanType)
model_xtype_XImportDeclaration_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
model_xtype_XImportDeclaration_wildcard: Property = Property(name="wildcard", type=BooleanType)
model_xtype_XImportDeclaration_m_getImportedTypeName: Method = Method(name="getImportedTypeName", parameters={}, type=StringType)
model_xtype_XImportDeclaration.attributes={model_xtype_XImportDeclaration_importedNamespace, model_xtype_XImportDeclaration_extension, model_xtype_XImportDeclaration_wildcard, model_xtype_XImportDeclaration_static}
model_xtype_XImportDeclaration.methods={model_xtype_XImportDeclaration_m_getImportedTypeName}

# model_xtype_XImportSection1 class attributes and methods

# XImportDeclaration1 class attributes and methods

# model_richstring_Line class attributes and methods

# LinePart class attributes and methods

# ProcessedRichString class attributes and methods

# model_richstring_LinePart class attributes and methods

# model_richstring_Literal class attributes and methods
model_richstring_Literal_offset: Property = Property(name="offset", type=IntegerType)
model_richstring_Literal_length: Property = Property(name="length", type=IntegerType)
model_richstring_Literal.attributes={model_richstring_Literal_offset, model_richstring_Literal_length}

# RichStringLiteral class attributes and methods

# model_richstring_LineBreak class attributes and methods

# Literal class attributes and methods

# model_richstring_ForLoopStart class attributes and methods

# RichStringForLoop class attributes and methods

# ForLoopEnd class attributes and methods

# model_richstring_ForLoopEnd class attributes and methods

# ForLoopStart class attributes and methods

# model_richstring_PrintedExpression class attributes and methods

# model_richstring_IfConditionStart class attributes and methods

# RichStringIf class attributes and methods

# ElseStart class attributes and methods

# ElseIfCondition class attributes and methods

# EndIf class attributes and methods

# model_xtype_XExportItem class attributes and methods
model_xtype_XExportItem_alias: Property = Property(name="alias", type=StringType)
model_xtype_XExportItem.attributes={model_xtype_XExportItem_alias}

# model_richstring_ProcessedRichString class attributes and methods

# RichString class attributes and methods

# Line class attributes and methods

# model_richstring_ElseIfCondition class attributes and methods

# IfConditionStart class attributes and methods

# model_richstring_ElseStart class attributes and methods

# model_richstring_EndIf class attributes and methods

# Relationships
importSection0: BinaryAssociation = BinaryAssociation(
    name="importSection0",
    ends={
        Property(name="XImportSection1", type=model_types_JvmModule, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmModule", type=XImportSection1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents1: BinaryAssociation = BinaryAssociation(
    name="contents1",
    ends={
        Property(name="types_model_EObject", type=model_types_JvmModule, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmModule2", type=types_model_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exportSection3: BinaryAssociation = BinaryAssociation(
    name="exportSection3",
    ends={
        Property(name="XExportSection", type=model_types_JvmModule, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmModule4", type=XExportSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importSection5: BinaryAssociation = BinaryAssociation(
    name="importSection5",
    ends={
        Property(name="XImportSection16", type=model_types_JvmNoModule, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmNoModule", type=XImportSection1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents7: BinaryAssociation = BinaryAssociation(
    name="contents7",
    ends={
        Property(name="types_model_EObject9", type=model_types_JvmNoModule, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmNoModule8", type=types_model_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arrayType10: BinaryAssociation = BinaryAssociation(
    name="arrayType10",
    ends={
        Property(name="JvmArrayType", type=model_types_JvmComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="componentType", type=JvmArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentType11: BinaryAssociation = BinaryAssociation(
    name="componentType11",
    ends={
        Property(name="JvmComponentType", type=model_types_JvmArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="arrayType", type=JvmComponentType, multiplicity=Multiplicity(0, 1))
    }
)
superTypes12: BinaryAssociation = BinaryAssociation(
    name="superTypes12",
    ends={
        Property(name="JvmTypeReference", type=model_types_JvmDeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmDeclaredType", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members13: BinaryAssociation = BinaryAssociation(
    name="members13",
    ends={
        Property(name="JvmMember", type=model_types_JvmDeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="declaringType", type=JvmMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarator14: BinaryAssociation = BinaryAssociation(
    name="declarator14",
    ends={
        Property(name="JvmTypeParameterDeclarator", type=model_types_JvmTypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="typeParameters", type=JvmTypeParameterDeclarator, multiplicity=Multiplicity(0, 1))
    }
)
owner19: BinaryAssociation = BinaryAssociation(
    name="owner19",
    ends={
        Property(name="JvmConstraintOwner", type=model_types_JvmTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=JvmConstraintOwner, multiplicity=Multiplicity(0, 1))
    }
)
literals20: BinaryAssociation = BinaryAssociation(
    name="literals20",
    ends={
        Property(name="JvmEnumerationLiteral", type=model_types_JvmEnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmEnumerationType", type=JvmEnumerationLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
typeParameters15: BinaryAssociation = BinaryAssociation(
    name="typeParameters15",
    ends={
        Property(name="JvmTypeParameter", type=model_types_JvmTypeParameterDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="declarator", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints16: BinaryAssociation = BinaryAssociation(
    name="constraints16",
    ends={
        Property(name="JvmTypeConstraint", type=model_types_JvmConstraintOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=JvmTypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeReference17: BinaryAssociation = BinaryAssociation(
    name="typeReference17",
    ends={
        Property(name="JvmTypeReference18", type=model_types_JvmTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmTypeConstraint", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments25: BinaryAssociation = BinaryAssociation(
    name="arguments25",
    ends={
        Property(name="JvmTypeReference26", type=model_types_JvmParameterizedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmParameterizedTypeReference", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="JvmType", type=model_types_JvmParameterizedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmParameterizedTypeReference28", type=JvmType, multiplicity=Multiplicity(0, 1))
    }
)
componentType29: BinaryAssociation = BinaryAssociation(
    name="componentType29",
    ends={
        Property(name="JvmTypeReference30", type=model_types_JvmGenericArrayTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmGenericArrayTypeReference", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends21: BinaryAssociation = BinaryAssociation(
    name="extends21",
    ends={
        Property(name="JvmParameterizedTypeReference", type=model_types_JvmGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmGenericType", type=JvmParameterizedTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implements22: BinaryAssociation = BinaryAssociation(
    name="implements22",
    ends={
        Property(name="JvmParameterizedTypeReference24", type=model_types_JvmGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmGenericType23", type=JvmParameterizedTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationInfo34: BinaryAssociation = BinaryAssociation(
    name="annotationInfo34",
    ends={
        Property(name="JvmAnnotationTarget", type=model_types_JvmMember, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmMember", type=JvmAnnotationTarget, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="JvmTypeReference36", type=model_types_JvmField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmField", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue37: BinaryAssociation = BinaryAssociation(
    name="defaultValue37",
    ends={
        Property(name="XExpression", type=model_types_JvmField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmField38", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set39: BinaryAssociation = BinaryAssociation(
    name="set39",
    ends={
        Property(name="XExpression41", type=model_types_JvmField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmField40", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
get42: BinaryAssociation = BinaryAssociation(
    name="get42",
    ends={
        Property(name="XExpression44", type=model_types_JvmField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmField43", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters45: BinaryAssociation = BinaryAssociation(
    name="parameters45",
    ends={
        Property(name="JvmFormalParameter", type=model_types_JvmExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmExecutable", type=JvmFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions46: BinaryAssociation = BinaryAssociation(
    name="exceptions46",
    ends={
        Property(name="JvmTypeReference48", type=model_types_JvmExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmExecutable47", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type31: BinaryAssociation = BinaryAssociation(
    name="type31",
    ends={
        Property(name="JvmType32", type=model_types_JvmAnyTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnyTypeReference", type=JvmType, multiplicity=Multiplicity(0, 1))
    }
)
declaringType33: BinaryAssociation = BinaryAssociation(
    name="declaringType33",
    ends={
        Property(name="JvmDeclaredType", type=model_types_JvmMember, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=JvmDeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
expression55: BinaryAssociation = BinaryAssociation(
    name="expression55",
    ends={
        Property(name="XExpression57", type=model_types_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmOperation56", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function58: BinaryAssociation = BinaryAssociation(
    name="function58",
    ends={
        Property(name="XExpression60", type=model_types_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmOperation59", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterType61: BinaryAssociation = BinaryAssociation(
    name="parameterType61",
    ends={
        Property(name="JvmTypeReference62", type=model_types_JvmFormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmFormalParameter", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue63: BinaryAssociation = BinaryAssociation(
    name="defaultValue63",
    ends={
        Property(name="XExpression65", type=model_types_JvmFormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmFormalParameter64", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations66: BinaryAssociation = BinaryAssociation(
    name="annotations66",
    ends={
        Property(name="JvmAnnotationReference", type=model_types_JvmAnnotationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationTarget", type=JvmAnnotationReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation67: BinaryAssociation = BinaryAssociation(
    name="annotation67",
    ends={
        Property(name="JvmAnnotationType", type=model_types_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationReference", type=JvmAnnotationType, multiplicity=Multiplicity(0, 1))
    }
)
values68: BinaryAssociation = BinaryAssociation(
    name="values68",
    ends={
        Property(name="JvmAnnotationValue70", type=model_types_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationReference69", type=JvmAnnotationValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value71: BinaryAssociation = BinaryAssociation(
    name="value71",
    ends={
        Property(name="XExpression73", type=model_types_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationReference72", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation74: BinaryAssociation = BinaryAssociation(
    name="operation74",
    ends={
        Property(name="JvmOperation", type=model_types_JvmAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationValue", type=JvmOperation, multiplicity=Multiplicity(0, 1))
    }
)
value75: BinaryAssociation = BinaryAssociation(
    name="value75",
    ends={
        Property(name="XExpression77", type=model_types_JvmAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationValue76", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression49: BinaryAssociation = BinaryAssociation(
    name="expression49",
    ends={
        Property(name="XExpression50", type=model_types_JvmConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmConstructor", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType51: BinaryAssociation = BinaryAssociation(
    name="returnType51",
    ends={
        Property(name="JvmTypeReference52", type=model_types_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmOperation", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue53: BinaryAssociation = BinaryAssociation(
    name="defaultValue53",
    ends={
        Property(name="JvmAnnotationValue", type=model_types_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmOperation54", type=JvmAnnotationValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values78: BinaryAssociation = BinaryAssociation(
    name="values78",
    ends={
        Property(name="JvmTypeReference79", type=model_types_JvmTypeAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmTypeAnnotationValue", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values80: BinaryAssociation = BinaryAssociation(
    name="values80",
    ends={
        Property(name="JvmAnnotationReference81", type=model_types_JvmAnnotationAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationAnnotationValue", type=JvmAnnotationReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values82: BinaryAssociation = BinaryAssociation(
    name="values82",
    ends={
        Property(name="JvmEnumerationLiteral83", type=model_types_JvmEnumAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmEnumAnnotationValue", type=JvmEnumerationLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
delegate84: BinaryAssociation = BinaryAssociation(
    name="delegate84",
    ends={
        Property(name="JvmTypeReference85", type=model_types_JvmDelegateTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmDelegateTypeReference", type=JvmTypeReference, multiplicity=Multiplicity(0, 1))
    }
)
equivalent86: BinaryAssociation = BinaryAssociation(
    name="equivalent86",
    ends={
        Property(name="JvmTypeReference87", type=model_types_JvmSpecializedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmSpecializedTypeReference", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then95: BinaryAssociation = BinaryAssociation(
    name="then95",
    ends={
        Property(name="model_xbase_XIfExpression96", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="XExpression97", type=model_xbase_XIfExpression, multiplicity=Multiplicity(1, 1))
    }
)
else_98: BinaryAssociation = BinaryAssociation(
    name="else_98",
    ends={
        Property(name="XExpression100", type=model_xbase_XIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XIfExpression99", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switch101: BinaryAssociation = BinaryAssociation(
    name="switch101",
    ends={
        Property(name="XExpression102", type=model_xbase_XSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XSwitchExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases103: BinaryAssociation = BinaryAssociation(
    name="cases103",
    ends={
        Property(name="XCasePart", type=model_xbase_XSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XSwitchExpression104", type=XCasePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default105: BinaryAssociation = BinaryAssociation(
    name="default105",
    ends={
        Property(name="XExpression107", type=model_xbase_XSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XSwitchExpression106", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case108: BinaryAssociation = BinaryAssociation(
    name="case108",
    ends={
        Property(name="XExpression109", type=model_xbase_XCasePart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCasePart", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then110: BinaryAssociation = BinaryAssociation(
    name="then110",
    ends={
        Property(name="XExpression112", type=model_xbase_XCasePart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCasePart111", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeGuard113: BinaryAssociation = BinaryAssociation(
    name="typeGuard113",
    ends={
        Property(name="JvmTypeReference115", type=model_xbase_XCasePart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCasePart114", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions116: BinaryAssociation = BinaryAssociation(
    name="expressions116",
    ends={
        Property(name="XExpression117", type=model_xbase_XBlockExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XBlockExpression", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type118: BinaryAssociation = BinaryAssociation(
    name="type118",
    ends={
        Property(name="JvmTypeReference119", type=model_xbase_XVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XVariableDeclaration", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type88: BinaryAssociation = BinaryAssociation(
    name="type88",
    ends={
        Property(name="JvmType89", type=model_types_JvmCompoundTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmCompoundTypeReference", type=JvmType, multiplicity=Multiplicity(0, 1))
    }
)
references90: BinaryAssociation = BinaryAssociation(
    name="references90",
    ends={
        Property(name="JvmTypeReference92", type=model_types_JvmCompoundTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmCompoundTypeReference91", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if_93: BinaryAssociation = BinaryAssociation(
    name="if_93",
    ends={
        Property(name="XExpression94", type=model_xbase_XIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XIfExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature125: BinaryAssociation = BinaryAssociation(
    name="feature125",
    ends={
        Property(name="JvmIdentifiableElement", type=model_xbase_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractFeatureCall", type=JvmIdentifiableElement, multiplicity=Multiplicity(0, 1))
    }
)
typeArguments126: BinaryAssociation = BinaryAssociation(
    name="typeArguments126",
    ends={
        Property(name="JvmTypeReference128", type=model_xbase_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractFeatureCall127", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implicitReceiver129: BinaryAssociation = BinaryAssociation(
    name="implicitReceiver129",
    ends={
        Property(name="XExpression131", type=model_xbase_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractFeatureCall130", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implicitFirstArgument132: BinaryAssociation = BinaryAssociation(
    name="implicitFirstArgument132",
    ends={
        Property(name="XExpression134", type=model_xbase_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractFeatureCall133", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right120: BinaryAssociation = BinaryAssociation(
    name="right120",
    ends={
        Property(name="XExpression122", type=model_xbase_XVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XVariableDeclaration121", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations123: BinaryAssociation = BinaryAssociation(
    name="declarations123",
    ends={
        Property(name="XExpression124", type=model_xbase_XVariableDeclarationList, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XVariableDeclarationList", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberCallArguments142: BinaryAssociation = BinaryAssociation(
    name="memberCallArguments142",
    ends={
        Property(name="XExpression144", type=model_xbase_XMemberFeatureCall1, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XMemberFeatureCall1143", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureCallArguments145: BinaryAssociation = BinaryAssociation(
    name="featureCallArguments145",
    ends={
        Property(name="XExpression146", type=model_xbase_XFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XFeatureCall", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value147: BinaryAssociation = BinaryAssociation(
    name="value147",
    ends={
        Property(name="XExpression149", type=model_xbase_XFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XFeatureCall148", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constructor150: BinaryAssociation = BinaryAssociation(
    name="constructor150",
    ends={
        Property(name="JvmConstructor", type=model_xbase_XConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XConstructorCall", type=JvmConstructor, multiplicity=Multiplicity(0, 1))
    }
)
arguments151: BinaryAssociation = BinaryAssociation(
    name="arguments151",
    ends={
        Property(name="XExpression153", type=model_xbase_XConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XConstructorCall152", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments154: BinaryAssociation = BinaryAssociation(
    name="typeArguments154",
    ends={
        Property(name="JvmTypeReference156", type=model_xbase_XConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XConstructorCall155", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberCallTarget135: BinaryAssociation = BinaryAssociation(
    name="memberCallTarget135",
    ends={
        Property(name="XExpression136", type=model_xbase_XMemberFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XMemberFeatureCall", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberCallArguments137: BinaryAssociation = BinaryAssociation(
    name="memberCallArguments137",
    ends={
        Property(name="XExpression139", type=model_xbase_XMemberFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XMemberFeatureCall138", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberCallTarget140: BinaryAssociation = BinaryAssociation(
    name="memberCallTarget140",
    ends={
        Property(name="XExpression141", type=model_xbase_XMemberFeatureCall1, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XMemberFeatureCall1", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value159: BinaryAssociation = BinaryAssociation(
    name="value159",
    ends={
        Property(name="XExpression160", type=model_xbase_XKeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XKeyValuePair", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key161: BinaryAssociation = BinaryAssociation(
    name="key161",
    ends={
        Property(name="XExpression163", type=model_xbase_XKeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XKeyValuePair162", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredFormalParameters164: BinaryAssociation = BinaryAssociation(
    name="declaredFormalParameters164",
    ends={
        Property(name="JvmFormalParameter165", type=model_xbase_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XClosure", type=JvmFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression166: BinaryAssociation = BinaryAssociation(
    name="expression166",
    ends={
        Property(name="XExpression168", type=model_xbase_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XClosure167", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implicitParameter169: BinaryAssociation = BinaryAssociation(
    name="implicitParameter169",
    ends={
        Property(name="JvmFormalParameter171", type=model_xbase_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XClosure170", type=JvmFormalParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType172: BinaryAssociation = BinaryAssociation(
    name="returnType172",
    ends={
        Property(name="JvmTypeReference174", type=model_xbase_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XClosure173", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters175: BinaryAssociation = BinaryAssociation(
    name="typeParameters175",
    ends={
        Property(name="JvmTypeParameter177", type=model_xbase_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XClosure176", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements157: BinaryAssociation = BinaryAssociation(
    name="elements157",
    ends={
        Property(name="XExpression158", type=model_xbase_XCollectionLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCollectionLiteral", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand188: BinaryAssociation = BinaryAssociation(
    name="operand188",
    ends={
        Property(name="XExpression189", type=model_xbase_XUnaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XUnaryOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition190: BinaryAssociation = BinaryAssociation(
    name="condition190",
    ends={
        Property(name="XExpression191", type=model_xbase_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForLoopExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loop192: BinaryAssociation = BinaryAssociation(
    name="loop192",
    ends={
        Property(name="XExpression194", type=model_xbase_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForLoopExpression193", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init195: BinaryAssociation = BinaryAssociation(
    name="init195",
    ends={
        Property(name="XExpression197", type=model_xbase_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForLoopExpression196", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eachExpression198: BinaryAssociation = BinaryAssociation(
    name="eachExpression198",
    ends={
        Property(name="XExpression200", type=model_xbase_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForLoopExpression199", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forExpression201: BinaryAssociation = BinaryAssociation(
    name="forExpression201",
    ends={
        Property(name="XExpression202", type=model_xbase_XForEachExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForEachExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eachExpression203: BinaryAssociation = BinaryAssociation(
    name="eachExpression203",
    ends={
        Property(name="XExpression205", type=model_xbase_XForEachExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForEachExpression204", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type178: BinaryAssociation = BinaryAssociation(
    name="type178",
    ends={
        Property(name="JvmTypeReference179", type=model_xbase_XCastedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCastedExpression", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target180: BinaryAssociation = BinaryAssociation(
    name="target180",
    ends={
        Property(name="XExpression182", type=model_xbase_XCastedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCastedExpression181", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand183: BinaryAssociation = BinaryAssociation(
    name="leftOperand183",
    ends={
        Property(name="XExpression184", type=model_xbase_XBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XBinaryOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand185: BinaryAssociation = BinaryAssociation(
    name="rightOperand185",
    ends={
        Property(name="XExpression187", type=model_xbase_XBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XBinaryOperation186", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type214: BinaryAssociation = BinaryAssociation(
    name="type214",
    ends={
        Property(name="JvmType215", type=model_xbase_XTypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTypeLiteral", type=JvmType, multiplicity=Multiplicity(1, 1))
    }
)
type216: BinaryAssociation = BinaryAssociation(
    name="type216",
    ends={
        Property(name="JvmTypeReference217", type=model_xbase_XInstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XInstanceOfExpression", type=JvmTypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression218: BinaryAssociation = BinaryAssociation(
    name="expression218",
    ends={
        Property(name="XExpression220", type=model_xbase_XInstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XInstanceOfExpression219", type=XExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression221: BinaryAssociation = BinaryAssociation(
    name="expression221",
    ends={
        Property(name="XExpression222", type=model_xbase_XThrowExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XThrowExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression223: BinaryAssociation = BinaryAssociation(
    name="expression223",
    ends={
        Property(name="XExpression224", type=model_xbase_XTryCatchFinallyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTryCatchFinallyExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredParam206: BinaryAssociation = BinaryAssociation(
    name="declaredParam206",
    ends={
        Property(name="JvmFormalParameter208", type=model_xbase_XForEachExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForEachExpression207", type=JvmFormalParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predicate209: BinaryAssociation = BinaryAssociation(
    name="predicate209",
    ends={
        Property(name="XExpression210", type=model_xbase_XAbstractWhileExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractWhileExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body211: BinaryAssociation = BinaryAssociation(
    name="body211",
    ends={
        Property(name="XExpression213", type=model_xbase_XAbstractWhileExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractWhileExpression212", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignable235: BinaryAssociation = BinaryAssociation(
    name="assignable235",
    ends={
        Property(name="XExpression236", type=model_xbase_XAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAssignment", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value237: BinaryAssociation = BinaryAssociation(
    name="value237",
    ends={
        Property(name="XExpression239", type=model_xbase_XAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAssignment238", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression240: BinaryAssociation = BinaryAssociation(
    name="expression240",
    ends={
        Property(name="XExpression241", type=model_xbase_XReturnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XReturnExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand242: BinaryAssociation = BinaryAssociation(
    name="operand242",
    ends={
        Property(name="XExpression243", type=model_xbase_XPrefixOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XPrefixOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand244: BinaryAssociation = BinaryAssociation(
    name="operand244",
    ends={
        Property(name="XExpression245", type=model_xbase_XPostfixOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XPostfixOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finallyExpression225: BinaryAssociation = BinaryAssociation(
    name="finallyExpression225",
    ends={
        Property(name="XExpression227", type=model_xbase_XTryCatchFinallyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTryCatchFinallyExpression226", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses228: BinaryAssociation = BinaryAssociation(
    name="catchClauses228",
    ends={
        Property(name="XCatchClause", type=model_xbase_XTryCatchFinallyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTryCatchFinallyExpression229", type=XCatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression230: BinaryAssociation = BinaryAssociation(
    name="expression230",
    ends={
        Property(name="XExpression231", type=model_xbase_XCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCatchClause", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredParam232: BinaryAssociation = BinaryAssociation(
    name="declaredParam232",
    ends={
        Property(name="JvmFormalParameter234", type=model_xbase_XCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCatchClause233", type=JvmFormalParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition251: BinaryAssociation = BinaryAssociation(
    name="condition251",
    ends={
        Property(name="XExpression253", type=model_xbase_XTernaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTernaryOperation252", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression254: BinaryAssociation = BinaryAssociation(
    name="expression254",
    ends={
        Property(name="XExpression255", type=model_xbase_XIndexOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XIndexOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index256: BinaryAssociation = BinaryAssociation(
    name="index256",
    ends={
        Property(name="XExpression258", type=model_xbase_XIndexOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XIndexOperation257", type=XExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body259: BinaryAssociation = BinaryAssociation(
    name="body259",
    ends={
        Property(name="XExpression260", type=model_xbase_XFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XFunctionDeclaration", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trueOperand246: BinaryAssociation = BinaryAssociation(
    name="trueOperand246",
    ends={
        Property(name="XExpression247", type=model_xbase_XTernaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTernaryOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
falseOperand248: BinaryAssociation = BinaryAssociation(
    name="falseOperand248",
    ends={
        Property(name="XExpression250", type=model_xbase_XTernaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTernaryOperation249", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type268: BinaryAssociation = BinaryAssociation(
    name="type268",
    ends={
        Property(name="JvmType270", type=model_xbase_XObjectLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XObjectLiteral269", type=JvmType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value271: BinaryAssociation = BinaryAssociation(
    name="value271",
    ends={
        Property(name="XExpression272", type=model_xbase_XObjectLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XObjectLiteralPart", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements273: BinaryAssociation = BinaryAssociation(
    name="elements273",
    ends={
        Property(name="XExpression274", type=model_xbase_XArrayLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XArrayLiteral", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importSection275: BinaryAssociation = BinaryAssociation(
    name="importSection275",
    ends={
        Property(name="XImportSection1276", type=model_ss_XtendFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFile", type=XImportSection1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xtendTypes277: BinaryAssociation = BinaryAssociation(
    name="xtendTypes277",
    ends={
        Property(name="XtendTypeDeclaration", type=model_ss_XtendFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFile278", type=XtendTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents279: BinaryAssociation = BinaryAssociation(
    name="contents279",
    ends={
        Property(name="ss_model_EObject", type=model_ss_XtendFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFile280", type=ss_model_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exportSection281: BinaryAssociation = BinaryAssociation(
    name="exportSection281",
    ends={
        Property(name="XExportSection283", type=model_ss_XtendFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFile282", type=XExportSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType261: BinaryAssociation = BinaryAssociation(
    name="returnType261",
    ends={
        Property(name="JvmTypeReference263", type=model_xbase_XFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XFunctionDeclaration262", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters264: BinaryAssociation = BinaryAssociation(
    name="parameters264",
    ends={
        Property(name="JvmFormalParameter266", type=model_xbase_XFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XFunctionDeclaration265", type=JvmFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties267: BinaryAssociation = BinaryAssociation(
    name="properties267",
    ends={
        Property(name="XObjectLiteralPart", type=model_xbase_XObjectLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XObjectLiteral", type=XObjectLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters289: BinaryAssociation = BinaryAssociation(
    name="typeParameters289",
    ends={
        Property(name="JvmTypeParameter291", type=model_ss_XtendClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendClass290", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations292: BinaryAssociation = BinaryAssociation(
    name="annotations292",
    ends={
        Property(name="XAnnotation", type=model_ss_XtendAnnotationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendAnnotationTarget", type=XAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationInfo293: BinaryAssociation = BinaryAssociation(
    name="annotationInfo293",
    ends={
        Property(name="XtendAnnotationTarget", type=model_ss_XtendMember, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendMember", type=XtendAnnotationTarget, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaringType294: BinaryAssociation = BinaryAssociation(
    name="declaringType294",
    ends={
        Property(name="XtendTypeDeclaration296", type=model_ss_XtendMember, multiplicity=Multiplicity(1, 1)),
        Property(name="members295", type=XtendTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
expression297: BinaryAssociation = BinaryAssociation(
    name="expression297",
    ends={
        Property(name="XExpression298", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends284: BinaryAssociation = BinaryAssociation(
    name="extends284",
    ends={
        Property(name="JvmTypeReference285", type=model_ss_XtendClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendClass", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implements286: BinaryAssociation = BinaryAssociation(
    name="implements286",
    ends={
        Property(name="JvmTypeReference288", type=model_ss_XtendClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendClass287", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters306: BinaryAssociation = BinaryAssociation(
    name="typeParameters306",
    ends={
        Property(name="JvmTypeParameter308", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction307", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions309: BinaryAssociation = BinaryAssociation(
    name="exceptions309",
    ends={
        Property(name="JvmTypeReference311", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction310", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type312: BinaryAssociation = BinaryAssociation(
    name="type312",
    ends={
        Property(name="JvmTypeReference313", type=model_ss_XtendField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendField", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue314: BinaryAssociation = BinaryAssociation(
    name="initialValue314",
    ends={
        Property(name="XExpression316", type=model_ss_XtendField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendField315", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType299: BinaryAssociation = BinaryAssociation(
    name="returnType299",
    ends={
        Property(name="JvmTypeReference301", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction300", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters302: BinaryAssociation = BinaryAssociation(
    name="parameters302",
    ends={
        Property(name="XtendParameter", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction303", type=XtendParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createExtensionInfo304: BinaryAssociation = BinaryAssociation(
    name="createExtensionInfo304",
    ends={
        Property(name="CreateExtensionInfo", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction305", type=CreateExtensionInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
separator319: BinaryAssociation = BinaryAssociation(
    name="separator319",
    ends={
        Property(name="XExpression320", type=model_ss_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringForLoop", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
before321: BinaryAssociation = BinaryAssociation(
    name="before321",
    ends={
        Property(name="XExpression323", type=model_ss_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringForLoop322", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after324: BinaryAssociation = BinaryAssociation(
    name="after324",
    ends={
        Property(name="XExpression326", type=model_ss_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringForLoop325", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterType317: BinaryAssociation = BinaryAssociation(
    name="parameterType317",
    ends={
        Property(name="JvmTypeReference318", type=model_ss_XtendParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendParameter", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIfs332: BinaryAssociation = BinaryAssociation(
    name="elseIfs332",
    ends={
        Property(name="RichStringElseIf", type=model_ss_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringIf333", type=RichStringElseIf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else_334: BinaryAssociation = BinaryAssociation(
    name="else_334",
    ends={
        Property(name="XExpression336", type=model_ss_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringIf335", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if_337: BinaryAssociation = BinaryAssociation(
    name="if_337",
    ends={
        Property(name="XExpression338", type=model_ss_RichStringElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringElseIf", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then339: BinaryAssociation = BinaryAssociation(
    name="then339",
    ends={
        Property(name="XExpression341", type=model_ss_RichStringElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringElseIf340", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
createExpression342: BinaryAssociation = BinaryAssociation(
    name="createExpression342",
    ends={
        Property(name="XExpression343", type=model_ss_CreateExtensionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_CreateExtensionInfo", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if_327: BinaryAssociation = BinaryAssociation(
    name="if_327",
    ends={
        Property(name="XExpression328", type=model_ss_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringIf", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression344: BinaryAssociation = BinaryAssociation(
    name="expression344",
    ends={
        Property(name="XExpression345", type=model_ss_XtendConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendConstructor", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then329: BinaryAssociation = BinaryAssociation(
    name="then329",
    ends={
        Property(name="XExpression331", type=model_ss_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringIf330", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members355: BinaryAssociation = BinaryAssociation(
    name="members355",
    ends={
        Property(name="XtendMember", type=model_ss_XtendTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="declaringType356", type=XtendMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends357: BinaryAssociation = BinaryAssociation(
    name="extends357",
    ends={
        Property(name="JvmTypeReference358", type=model_ss_XtendInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendInterface", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters359: BinaryAssociation = BinaryAssociation(
    name="typeParameters359",
    ends={
        Property(name="JvmTypeParameter361", type=model_ss_XtendInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendInterface360", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType362: BinaryAssociation = BinaryAssociation(
    name="returnType362",
    ends={
        Property(name="JvmTypeReference363", type=model_ss_XtendDelegate, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendDelegate", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters364: BinaryAssociation = BinaryAssociation(
    name="parameters364",
    ends={
        Property(name="XtendParameter366", type=model_ss_XtendDelegate, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendDelegate365", type=XtendParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters367: BinaryAssociation = BinaryAssociation(
    name="typeParameters367",
    ends={
        Property(name="JvmTypeParameter369", type=model_ss_XtendDelegate, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendDelegate368", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions370: BinaryAssociation = BinaryAssociation(
    name="exceptions370",
    ends={
        Property(name="JvmTypeReference372", type=model_ss_XtendDelegate, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendDelegate371", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type373: BinaryAssociation = BinaryAssociation(
    name="type373",
    ends={
        Property(name="JvmTypeReference374", type=model_ss_XtendEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendEvent", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters346: BinaryAssociation = BinaryAssociation(
    name="parameters346",
    ends={
        Property(name="XtendParameter348", type=model_ss_XtendConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendConstructor347", type=XtendParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters349: BinaryAssociation = BinaryAssociation(
    name="typeParameters349",
    ends={
        Property(name="JvmTypeParameter351", type=model_ss_XtendConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendConstructor350", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions352: BinaryAssociation = BinaryAssociation(
    name="exceptions352",
    ends={
        Property(name="JvmTypeReference354", type=model_ss_XtendConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendConstructor353", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationType379: BinaryAssociation = BinaryAssociation(
    name="annotationType379",
    ends={
        Property(name="JvmType381", type=model_xannotation_XAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xannotation_XAnnotation380", type=JvmType, multiplicity=Multiplicity(0, 1))
    }
)
value382: BinaryAssociation = BinaryAssociation(
    name="value382",
    ends={
        Property(name="XExpression384", type=model_xannotation_XAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xannotation_XAnnotation383", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value385: BinaryAssociation = BinaryAssociation(
    name="value385",
    ends={
        Property(name="XExpression386", type=model_xannotation_XAnnotationElementValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xannotation_XAnnotationElementValuePair", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element387: BinaryAssociation = BinaryAssociation(
    name="element387",
    ends={
        Property(name="JvmOperation389", type=model_xannotation_XAnnotationElementValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xannotation_XAnnotationElementValuePair388", type=JvmOperation, multiplicity=Multiplicity(0, 1))
    }
)
paramTypes390: BinaryAssociation = BinaryAssociation(
    name="paramTypes390",
    ends={
        Property(name="JvmTypeReference391", type=model_xtype_XFunctionTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XFunctionTypeRef", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType392: BinaryAssociation = BinaryAssociation(
    name="returnType392",
    ends={
        Property(name="JvmTypeReference394", type=model_xtype_XFunctionTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XFunctionTypeRef393", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type395: BinaryAssociation = BinaryAssociation(
    name="type395",
    ends={
        Property(name="JvmType397", type=model_xtype_XFunctionTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XFunctionTypeRef396", type=JvmType, multiplicity=Multiplicity(0, 1))
    }
)
initialValue375: BinaryAssociation = BinaryAssociation(
    name="initialValue375",
    ends={
        Property(name="XExpression377", type=model_ss_XtendEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendEvent376", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementValuePairs378: BinaryAssociation = BinaryAssociation(
    name="elementValuePairs378",
    ends={
        Property(name="XAnnotationElementValuePair", type=model_xannotation_XAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xannotation_XAnnotation", type=XAnnotationElementValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importItems402: BinaryAssociation = BinaryAssociation(
    name="importItems402",
    ends={
        Property(name="XImportItem", type=model_xtype_XImportDeclaration1, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XImportDeclaration1", type=XImportItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedId403: BinaryAssociation = BinaryAssociation(
    name="importedId403",
    ends={
        Property(name="JvmIdentifiableElement404", type=model_xtype_XImportItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XImportItem", type=JvmIdentifiableElement, multiplicity=Multiplicity(0, 1))
    }
)
exportDeclarations405: BinaryAssociation = BinaryAssociation(
    name="exportDeclarations405",
    ends={
        Property(name="XExportDeclaration", type=model_xtype_XExportSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XExportSection", type=XExportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importDeclarations398: BinaryAssociation = BinaryAssociation(
    name="importDeclarations398",
    ends={
        Property(name="XImportDeclaration", type=model_xtype_XImportSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XImportSection", type=XImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedType399: BinaryAssociation = BinaryAssociation(
    name="importedType399",
    ends={
        Property(name="JvmDeclaredType400", type=model_xtype_XImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XImportDeclaration", type=JvmDeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
importDeclarations401: BinaryAssociation = BinaryAssociation(
    name="importDeclarations401",
    ends={
        Property(name="XImportDeclaration1", type=model_xtype_XImportSection1, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XImportSection1", type=XImportDeclaration1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parts411: BinaryAssociation = BinaryAssociation(
    name="parts411",
    ends={
        Property(name="LinePart", type=model_richstring_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="line", type=LinePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
richString412: BinaryAssociation = BinaryAssociation(
    name="richString412",
    ends={
        Property(name="ProcessedRichString", type=model_richstring_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="lines", type=ProcessedRichString, multiplicity=Multiplicity(0, 1))
    }
)
line413: BinaryAssociation = BinaryAssociation(
    name="line413",
    ends={
        Property(name="Line414", type=model_richstring_LinePart, multiplicity=Multiplicity(1, 1)),
        Property(name="parts", type=Line, multiplicity=Multiplicity(0, 1))
    }
)
literal415: BinaryAssociation = BinaryAssociation(
    name="literal415",
    ends={
        Property(name="RichStringLiteral", type=model_richstring_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_Literal", type=RichStringLiteral, multiplicity=Multiplicity(0, 1))
    }
)
loop416: BinaryAssociation = BinaryAssociation(
    name="loop416",
    ends={
        Property(name="RichStringForLoop", type=model_richstring_ForLoopStart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_ForLoopStart", type=RichStringForLoop, multiplicity=Multiplicity(0, 1))
    }
)
end417: BinaryAssociation = BinaryAssociation(
    name="end417",
    ends={
        Property(name="ForLoopEnd", type=model_richstring_ForLoopStart, multiplicity=Multiplicity(1, 1)),
        Property(name="start", type=ForLoopEnd, multiplicity=Multiplicity(0, 1))
    }
)
start418: BinaryAssociation = BinaryAssociation(
    name="start418",
    ends={
        Property(name="ForLoopStart", type=model_richstring_ForLoopEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="end", type=ForLoopStart, multiplicity=Multiplicity(0, 1))
    }
)
expression419: BinaryAssociation = BinaryAssociation(
    name="expression419",
    ends={
        Property(name="XExpression420", type=model_richstring_PrintedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_PrintedExpression", type=XExpression, multiplicity=Multiplicity(0, 1))
    }
)
richStringIf421: BinaryAssociation = BinaryAssociation(
    name="richStringIf421",
    ends={
        Property(name="RichStringIf", type=model_richstring_IfConditionStart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_IfConditionStart", type=RichStringIf, multiplicity=Multiplicity(0, 1))
    }
)
elseStart422: BinaryAssociation = BinaryAssociation(
    name="elseStart422",
    ends={
        Property(name="ElseStart", type=model_richstring_IfConditionStart, multiplicity=Multiplicity(1, 1)),
        Property(name="ifConditionStart", type=ElseStart, multiplicity=Multiplicity(0, 1))
    }
)
elseIfConditions423: BinaryAssociation = BinaryAssociation(
    name="elseIfConditions423",
    ends={
        Property(name="ElseIfCondition", type=model_richstring_IfConditionStart, multiplicity=Multiplicity(1, 1)),
        Property(name="ifConditionStart424", type=ElseIfCondition, multiplicity=Multiplicity(0, 9999))
    }
)
exportItems406: BinaryAssociation = BinaryAssociation(
    name="exportItems406",
    ends={
        Property(name="XExportItem", type=model_xtype_XExportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XExportDeclaration", type=XExportItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exportedId407: BinaryAssociation = BinaryAssociation(
    name="exportedId407",
    ends={
        Property(name="JvmIdentifiableElement408", type=model_xtype_XExportItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XExportItem", type=JvmIdentifiableElement, multiplicity=Multiplicity(0, 1))
    }
)
richString409: BinaryAssociation = BinaryAssociation(
    name="richString409",
    ends={
        Property(name="RichString", type=model_richstring_ProcessedRichString, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_ProcessedRichString", type=RichString, multiplicity=Multiplicity(0, 1))
    }
)
lines410: BinaryAssociation = BinaryAssociation(
    name="lines410",
    ends={
        Property(name="Line", type=model_richstring_ProcessedRichString, multiplicity=Multiplicity(1, 1)),
        Property(name="richString", type=Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endIf425: BinaryAssociation = BinaryAssociation(
    name="endIf425",
    ends={
        Property(name="EndIf", type=model_richstring_IfConditionStart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_IfConditionStart426", type=EndIf, multiplicity=Multiplicity(0, 1))
    }
)
richStringElseIf427: BinaryAssociation = BinaryAssociation(
    name="richStringElseIf427",
    ends={
        Property(name="RichStringElseIf428", type=model_richstring_ElseIfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_ElseIfCondition", type=RichStringElseIf, multiplicity=Multiplicity(0, 1))
    }
)
ifConditionStart429: BinaryAssociation = BinaryAssociation(
    name="ifConditionStart429",
    ends={
        Property(name="IfConditionStart", type=model_richstring_ElseIfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="elseIfConditions", type=IfConditionStart, multiplicity=Multiplicity(0, 1))
    }
)
ifConditionStart430: BinaryAssociation = BinaryAssociation(
    name="ifConditionStart430",
    ends={
        Property(name="IfConditionStart431", type=model_richstring_ElseStart, multiplicity=Multiplicity(1, 1)),
        Property(name="elseStart", type=IfConditionStart, multiplicity=Multiplicity(0, 1))
    }
)
ifConditionStart432: BinaryAssociation = BinaryAssociation(
    name="ifConditionStart432",
    ends={
        Property(name="IfConditionStart433", type=model_richstring_EndIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_EndIf", type=IfConditionStart, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model_types_JvmModule_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=model_types_JvmModule)
gen_model_types_JvmType_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=model_types_JvmType)
gen_model_types_JvmVoid_JvmType = Generalization(general=JvmType, specific=model_types_JvmVoid)
gen_model_types_JvmPrimitiveType_JvmComponentType = Generalization(general=JvmComponentType, specific=model_types_JvmPrimitiveType)
gen_model_types_JvmArrayType_JvmComponentType = Generalization(general=JvmComponentType, specific=model_types_JvmArrayType)
gen_model_types_JvmDeclaredType_types_JvmMember = Generalization(general=types_JvmMember, specific=model_types_JvmDeclaredType)
gen_model_types_JvmDeclaredType_types_JvmComponentType = Generalization(general=types_JvmComponentType, specific=model_types_JvmDeclaredType)
gen_model_types_JvmComponentType_JvmType = Generalization(general=JvmType, specific=model_types_JvmComponentType)
gen_model_types_JvmTypeParameter_types_JvmComponentType = Generalization(general=types_JvmComponentType, specific=model_types_JvmTypeParameter)
gen_model_types_JvmTypeParameter_types_JvmConstraintOwner = Generalization(general=types_JvmConstraintOwner, specific=model_types_JvmTypeParameter)
gen_model_types_JvmUpperBound_JvmTypeConstraint = Generalization(general=JvmTypeConstraint, specific=model_types_JvmUpperBound)
gen_model_types_JvmLowerBound_JvmTypeConstraint = Generalization(general=JvmTypeConstraint, specific=model_types_JvmLowerBound)
gen_model_types_JvmAnnotationType_JvmDeclaredType = Generalization(general=JvmDeclaredType, specific=model_types_JvmAnnotationType)
gen_model_types_JvmEnumerationType_JvmDeclaredType = Generalization(general=JvmDeclaredType, specific=model_types_JvmEnumerationType)
gen_model_types_JvmEnumerationLiteral_JvmField = Generalization(general=JvmField, specific=model_types_JvmEnumerationLiteral)
gen_model_types_JvmGenericType_types_JvmDeclaredType = Generalization(general=types_JvmDeclaredType, specific=model_types_JvmGenericType)
gen_model_types_JvmGenericType_types_JvmTypeParameterDeclarator = Generalization(general=types_JvmTypeParameterDeclarator, specific=model_types_JvmGenericType)
gen_model_types_JvmParameterizedTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmParameterizedTypeReference)
gen_model_types_JvmGenericArrayTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmGenericArrayTypeReference)
gen_model_types_JvmWildcardTypeReference_types_JvmTypeReference = Generalization(general=types_JvmTypeReference, specific=model_types_JvmWildcardTypeReference)
gen_model_types_JvmWildcardTypeReference_types_JvmConstraintOwner = Generalization(general=types_JvmConstraintOwner, specific=model_types_JvmWildcardTypeReference)
gen_model_types_JvmAnyTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmAnyTypeReference)
gen_model_types_JvmFeature_JvmMember = Generalization(general=JvmMember, specific=model_types_JvmFeature)
gen_model_types_JvmField_JvmFeature = Generalization(general=JvmFeature, specific=model_types_JvmField)
gen_model_types_JvmExecutable_types_JvmFeature = Generalization(general=types_JvmFeature, specific=model_types_JvmExecutable)
gen_model_types_JvmExecutable_types_JvmTypeParameterDeclarator = Generalization(general=types_JvmTypeParameterDeclarator, specific=model_types_JvmExecutable)
gen_model_types_JvmConstructor_JvmExecutable = Generalization(general=JvmExecutable, specific=model_types_JvmConstructor)
gen_model_types_JvmMultiTypeReference_JvmCompoundTypeReference = Generalization(general=JvmCompoundTypeReference, specific=model_types_JvmMultiTypeReference)
gen_model_types_JvmMember_JvmAnnotationTarget = Generalization(general=JvmAnnotationTarget, specific=model_types_JvmMember)
gen_model_types_JvmFormalParameter_JvmAnnotationTarget = Generalization(general=JvmAnnotationTarget, specific=model_types_JvmFormalParameter)
gen_model_types_JvmAnnotationTarget_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=model_types_JvmAnnotationTarget)
gen_model_types_JvmIntAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmIntAnnotationValue)
gen_model_types_JvmBooleanAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmBooleanAnnotationValue)
gen_model_types_JvmOperation_JvmExecutable = Generalization(general=JvmExecutable, specific=model_types_JvmOperation)
gen_model_types_JvmStringAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmStringAnnotationValue)
gen_model_types_JvmTypeAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmTypeAnnotationValue)
gen_model_types_JvmAnnotationAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmAnnotationAnnotationValue)
gen_model_types_JvmEnumAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmEnumAnnotationValue)
gen_model_types_JvmDelegateTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmDelegateTypeReference)
gen_model_types_JvmSpecializedTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmSpecializedTypeReference)
gen_model_types_JvmSynonymTypeReference_JvmCompoundTypeReference = Generalization(general=JvmCompoundTypeReference, specific=model_types_JvmSynonymTypeReference)
gen_model_types_JvmUnknownTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmUnknownTypeReference)
gen_model_types_JvmCompoundTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmCompoundTypeReference)
gen_model_types_JvmByteAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmByteAnnotationValue)
gen_model_types_JvmShortAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmShortAnnotationValue)
gen_model_types_JvmLongAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmLongAnnotationValue)
gen_model_types_JvmDoubleAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmDoubleAnnotationValue)
gen_model_types_JvmFloatAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmFloatAnnotationValue)
gen_model_types_JvmCharAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmCharAnnotationValue)
gen_model_xbase_XSwitchExpression_xbase_XExpression = Generalization(general=xbase_XExpression, specific=model_xbase_XSwitchExpression)
gen_model_xbase_XSwitchExpression_types_JvmIdentifiableElement = Generalization(general=types_JvmIdentifiableElement, specific=model_xbase_XSwitchExpression)
gen_model_xbase_XBlockExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XBlockExpression)
gen_model_xbase_XVariableDeclaration_xbase_XExpression = Generalization(general=xbase_XExpression, specific=model_xbase_XVariableDeclaration)
gen_model_xbase_XVariableDeclaration_types_JvmIdentifiableElement = Generalization(general=types_JvmIdentifiableElement, specific=model_xbase_XVariableDeclaration)
gen_model_types_JvmCustomAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmCustomAnnotationValue)
gen_model_xbase_XIfExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XIfExpression)
gen_model_xbase_XMemberFeatureCall_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XMemberFeatureCall)
gen_model_xbase_XVariableDeclarationList_XExpression = Generalization(general=XExpression, specific=model_xbase_XVariableDeclarationList)
gen_model_xbase_XAbstractFeatureCall_XExpression = Generalization(general=XExpression, specific=model_xbase_XAbstractFeatureCall)
gen_model_xbase_XFeatureCall_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XFeatureCall)
gen_model_xbase_XConstructorCall_XExpression = Generalization(general=XExpression, specific=model_xbase_XConstructorCall)
gen_model_xbase_XMemberFeatureCall1_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XMemberFeatureCall1)
gen_model_xbase_XSetLiteral_XCollectionLiteral = Generalization(general=XCollectionLiteral, specific=model_xbase_XSetLiteral)
gen_model_xbase_XClosure_xbase_XExpression = Generalization(general=xbase_XExpression, specific=model_xbase_XClosure)
gen_model_xbase_XClosure_types_JvmIdentifiableElement = Generalization(general=types_JvmIdentifiableElement, specific=model_xbase_XClosure)
gen_model_xbase_XCastedExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XCastedExpression)
gen_model_xbase_XBooleanLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XBooleanLiteral)
gen_model_xbase_XNullLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XNullLiteral)
gen_model_xbase_XNumberLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XNumberLiteral)
gen_model_xbase_XStringLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XStringLiteral)
gen_model_xbase_XCollectionLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XCollectionLiteral)
gen_model_xbase_XListLiteral_XCollectionLiteral = Generalization(general=XCollectionLiteral, specific=model_xbase_XListLiteral)
gen_model_xbase_XKeyValuePair_XExpression = Generalization(general=XExpression, specific=model_xbase_XKeyValuePair)
gen_model_xbase_XForLoopExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XForLoopExpression)
gen_model_xbase_XForEachExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XForEachExpression)
gen_model_xbase_XBinaryOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XBinaryOperation)
gen_model_xbase_XUnaryOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XUnaryOperation)
gen_model_xbase_XWhileExpression_XAbstractWhileExpression = Generalization(general=XAbstractWhileExpression, specific=model_xbase_XWhileExpression)
gen_model_xbase_XTypeLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XTypeLiteral)
gen_model_xbase_XInstanceOfExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XInstanceOfExpression)
gen_model_xbase_XThrowExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XThrowExpression)
gen_model_xbase_XTryCatchFinallyExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XTryCatchFinallyExpression)
gen_model_xbase_XAbstractWhileExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XAbstractWhileExpression)
gen_model_xbase_XDoWhileExpression_XAbstractWhileExpression = Generalization(general=XAbstractWhileExpression, specific=model_xbase_XDoWhileExpression)
gen_model_xbase_XAssignment_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XAssignment)
gen_model_xbase_XReturnExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XReturnExpression)
gen_model_xbase_XBreakExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XBreakExpression)
gen_model_xbase_XContinueExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XContinueExpression)
gen_model_xbase_XPrefixOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XPrefixOperation)
gen_model_xbase_XPostfixOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XPostfixOperation)
gen_model_xbase_XIndexOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XIndexOperation)
gen_model_xbase_XFunctionDeclaration_XExpression = Generalization(general=XExpression, specific=model_xbase_XFunctionDeclaration)
gen_model_xbase_XTernaryOperation_XExpression = Generalization(general=XExpression, specific=model_xbase_XTernaryOperation)
gen_model_xbase_XArrayLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XArrayLiteral)
gen_model_ss_XtendClass_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=model_ss_XtendClass)
gen_model_xbase_XObjectLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XObjectLiteral)
gen_model_ss_XtendMember_XtendAnnotationTarget = Generalization(general=XtendAnnotationTarget, specific=model_ss_XtendMember)
gen_model_ss_XtendFunction_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendFunction)
gen_model_ss_XtendField_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendField)
gen_model_ss_RichString_XBlockExpression = Generalization(general=XBlockExpression, specific=model_ss_RichString)
gen_model_ss_RichStringLiteral_XStringLiteral = Generalization(general=XStringLiteral, specific=model_ss_RichStringLiteral)
gen_model_ss_RichStringForLoop_XForEachExpression = Generalization(general=XForEachExpression, specific=model_ss_RichStringForLoop)
gen_model_ss_RichStringIf_XExpression = Generalization(general=XExpression, specific=model_ss_RichStringIf)
gen_model_ss_XtendParameter_XtendAnnotationTarget = Generalization(general=XtendAnnotationTarget, specific=model_ss_XtendParameter)
gen_model_ss_XtendConstructor_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendConstructor)
gen_model_ss_XtendAnnotationType_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=model_ss_XtendAnnotationType)
gen_model_ss_XtendInterface_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=model_ss_XtendInterface)
gen_model_ss_XtendEnum_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=model_ss_XtendEnum)
gen_model_ss_XtendEnumLiteral_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendEnumLiteral)
gen_model_ss_XtendVariableDeclaration_XVariableDeclaration = Generalization(general=XVariableDeclaration, specific=model_ss_XtendVariableDeclaration)
gen_model_ss_XtendFormalParameter_JvmFormalParameter = Generalization(general=JvmFormalParameter, specific=model_ss_XtendFormalParameter)
gen_model_ss_XtendDelegate_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=model_ss_XtendDelegate)
gen_model_ss_XtendEvent_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendEvent)
gen_model_ss_XtendTypeDeclaration_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendTypeDeclaration)
gen_model_xtype_XFunctionTypeRef_JvmSpecializedTypeReference = Generalization(general=JvmSpecializedTypeReference, specific=model_xtype_XFunctionTypeRef)
gen_model_xtype_XComputedTypeReference_JvmSpecializedTypeReference = Generalization(general=JvmSpecializedTypeReference, specific=model_xtype_XComputedTypeReference)
gen_model_xannotation_XAnnotation_XExpression = Generalization(general=XExpression, specific=model_xannotation_XAnnotation)
gen_model_richstring_Literal_LinePart = Generalization(general=LinePart, specific=model_richstring_Literal)
gen_model_richstring_LineBreak_Literal = Generalization(general=Literal, specific=model_richstring_LineBreak)
gen_model_richstring_ForLoopStart_LinePart = Generalization(general=LinePart, specific=model_richstring_ForLoopStart)
gen_model_richstring_ForLoopEnd_LinePart = Generalization(general=LinePart, specific=model_richstring_ForLoopEnd)
gen_model_richstring_PrintedExpression_LinePart = Generalization(general=LinePart, specific=model_richstring_PrintedExpression)
gen_model_richstring_IfConditionStart_LinePart = Generalization(general=LinePart, specific=model_richstring_IfConditionStart)
gen_model_richstring_ElseIfCondition_LinePart = Generalization(general=LinePart, specific=model_richstring_ElseIfCondition)
gen_model_richstring_ElseStart_LinePart = Generalization(general=LinePart, specific=model_richstring_ElseStart)
gen_model_richstring_EndIf_LinePart = Generalization(general=LinePart, specific=model_richstring_EndIf)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_types_JvmIdentifiableElement, model_types_JvmModule, JvmIdentifiableElement, XImportSection1, types_model_EObject, XExportSection, model_types_JvmNoModule, model_types_JvmType, model_types_JvmVoid, JvmType, JvmArrayType, model_types_JvmPrimitiveType, JvmComponentType, model_types_JvmArrayType, model_types_JvmDeclaredType, types_JvmMember, types_JvmComponentType, model_types_JvmComponentType, JvmTypeReference, JvmMember, model_types_JvmTypeParameter, types_JvmConstraintOwner, JvmTypeParameterDeclarator, model_types_JvmTypeParameterDeclarator, model_types_JvmUpperBound, model_types_JvmLowerBound, model_types_JvmAnnotationType, JvmDeclaredType, model_types_JvmEnumerationType, JvmEnumerationLiteral, model_types_JvmEnumerationLiteral, JvmField, model_types_JvmGenericType, types_JvmDeclaredType, types_JvmTypeParameterDeclarator, JvmTypeParameter, JvmParameterizedTypeReference, model_types_JvmConstraintOwner, JvmTypeConstraint, model_types_JvmTypeConstraint, JvmConstraintOwner, model_types_JvmParameterizedTypeReference, model_types_JvmGenericArrayTypeReference, model_types_JvmWildcardTypeReference, types_JvmTypeReference, model_types_JvmAnyTypeReference, model_types_JvmTypeReference, model_types_JvmFeature, model_types_JvmField, JvmFeature, XExpression, model_types_JvmExecutable, types_JvmFeature, JvmFormalParameter, model_types_JvmConstructor, JvmExecutable, model_types_JvmMultiTypeReference, JvmCompoundTypeReference, model_types_JvmMember, JvmAnnotationTarget, model_types_JvmFormalParameter, model_types_JvmAnnotationTarget, JvmAnnotationReference, model_types_JvmAnnotationReference, JvmAnnotationType, model_types_JvmAnnotationValue, JvmOperation, model_types_JvmIntAnnotationValue, model_types_JvmBooleanAnnotationValue, model_types_JvmByteAnnotationValue, model_types_JvmOperation, JvmAnnotationValue, model_types_JvmStringAnnotationValue, model_types_JvmTypeAnnotationValue, model_types_JvmAnnotationAnnotationValue, model_types_JvmEnumAnnotationValue, model_types_JvmDelegateTypeReference, model_types_JvmSpecializedTypeReference, model_types_JvmSynonymTypeReference, model_types_JvmUnknownTypeReference, model_types_JvmCompoundTypeReference, model_types_JvmShortAnnotationValue, model_types_JvmLongAnnotationValue, model_types_JvmDoubleAnnotationValue, model_types_JvmFloatAnnotationValue, model_types_JvmCharAnnotationValue, model_xbase_XSwitchExpression, xbase_XExpression, types_JvmIdentifiableElement, XCasePart, model_xbase_XCasePart, model_xbase_XBlockExpression, model_xbase_XVariableDeclaration, model_types_JvmCustomAnnotationValue, model_xbase_XExpression, model_xbase_XIfExpression, model_xbase_XMemberFeatureCall, XAbstractFeatureCall, model_xbase_XVariableDeclarationList, model_xbase_XAbstractFeatureCall, model_xbase_XFeatureCall, model_xbase_XConstructorCall, JvmConstructor, model_xbase_XMemberFeatureCall1, model_xbase_XSetLiteral, model_xbase_XClosure, model_xbase_XCastedExpression, model_xbase_XBooleanLiteral, model_xbase_XNullLiteral, model_xbase_XNumberLiteral, model_xbase_XStringLiteral, model_xbase_XCollectionLiteral, model_xbase_XListLiteral, XCollectionLiteral, model_xbase_XKeyValuePair, model_xbase_XForLoopExpression, model_xbase_XForEachExpression, model_xbase_XBinaryOperation, model_xbase_XUnaryOperation, model_xbase_XWhileExpression, model_xbase_XTypeLiteral, model_xbase_XInstanceOfExpression, model_xbase_XThrowExpression, model_xbase_XTryCatchFinallyExpression, model_xbase_XAbstractWhileExpression, model_xbase_XDoWhileExpression, XAbstractWhileExpression, model_xbase_XReturnExpression, model_xbase_XBreakExpression, model_xbase_XContinueExpression, model_xbase_XPrefixOperation, model_xbase_XPostfixOperation, XCatchClause, model_xbase_XCatchClause, model_xbase_XAssignment, model_xbase_XIndexOperation, model_xbase_XFunctionDeclaration, model_xbase_XTernaryOperation, model_xbase_XObjectLiteralPart, model_xbase_XArrayLiteral, model_ss_XtendFile, XtendTypeDeclaration, ss_model_EObject, model_ss_XtendClass, model_xbase_XObjectLiteral, XObjectLiteralPart, model_ss_XtendAnnotationTarget, XAnnotation, model_ss_XtendMember, XtendAnnotationTarget, model_ss_XtendFunction, XtendMember, model_ss_XtendField, XtendParameter, CreateExtensionInfo, model_ss_RichStringLiteral, XStringLiteral, model_ss_RichStringForLoop, XForEachExpression, model_ss_RichStringIf, model_ss_XtendParameter, model_ss_RichString, XBlockExpression, RichStringElseIf, model_ss_RichStringElseIf, model_ss_CreateExtensionInfo, model_ss_XtendConstructor, model_ss_XtendAnnotationType, model_ss_XtendInterface, model_ss_XtendEnum, model_ss_XtendEnumLiteral, model_ss_XtendVariableDeclaration, XVariableDeclaration, model_ss_XtendFormalParameter, model_ss_XtendDelegate, model_ss_XtendEvent, model_ss_XtendTypeDeclaration, model_xannotation_XAnnotationElementValuePair, model_xtype_XFunctionTypeRef, JvmSpecializedTypeReference, model_xtype_XComputedTypeReference, model_xtype_XImportSection, model_xannotation_XAnnotation, XAnnotationElementValuePair, model_xtype_XImportDeclaration1, XImportItem, model_xtype_XImportItem, model_xtype_XExportSection, XExportDeclaration, model_xtype_XExportDeclaration, XExportItem, XImportDeclaration, model_xtype_XImportDeclaration, model_xtype_XImportSection1, XImportDeclaration1, model_richstring_Line, LinePart, ProcessedRichString, model_richstring_LinePart, model_richstring_Literal, RichStringLiteral, model_richstring_LineBreak, Literal, model_richstring_ForLoopStart, RichStringForLoop, ForLoopEnd, model_richstring_ForLoopEnd, ForLoopStart, model_richstring_PrintedExpression, model_richstring_IfConditionStart, RichStringIf, ElseStart, ElseIfCondition, EndIf, model_xtype_XExportItem, model_richstring_ProcessedRichString, RichString, Line, model_richstring_ElseIfCondition, IfConditionStart, model_richstring_ElseStart, model_richstring_EndIf, JvmVisibility},
    associations={importSection0, contents1, exportSection3, importSection5, contents7, arrayType10, componentType11, superTypes12, members13, declarator14, owner19, literals20, typeParameters15, constraints16, typeReference17, arguments25, type27, componentType29, extends21, implements22, annotationInfo34, type35, defaultValue37, set39, get42, parameters45, exceptions46, type31, declaringType33, expression55, function58, parameterType61, defaultValue63, annotations66, annotation67, values68, value71, operation74, value75, expression49, returnType51, defaultValue53, values78, values80, values82, delegate84, equivalent86, then95, else_98, switch101, cases103, default105, case108, then110, typeGuard113, expressions116, type118, type88, references90, if_93, feature125, typeArguments126, implicitReceiver129, implicitFirstArgument132, right120, declarations123, memberCallArguments142, featureCallArguments145, value147, constructor150, arguments151, typeArguments154, memberCallTarget135, memberCallArguments137, memberCallTarget140, value159, key161, declaredFormalParameters164, expression166, implicitParameter169, returnType172, typeParameters175, elements157, operand188, condition190, loop192, init195, eachExpression198, forExpression201, eachExpression203, type178, target180, leftOperand183, rightOperand185, type214, type216, expression218, expression221, expression223, declaredParam206, predicate209, body211, assignable235, value237, expression240, operand242, operand244, finallyExpression225, catchClauses228, expression230, declaredParam232, condition251, expression254, index256, body259, trueOperand246, falseOperand248, type268, value271, elements273, importSection275, xtendTypes277, contents279, exportSection281, returnType261, parameters264, properties267, typeParameters289, annotations292, annotationInfo293, declaringType294, expression297, extends284, implements286, typeParameters306, exceptions309, type312, initialValue314, returnType299, parameters302, createExtensionInfo304, separator319, before321, after324, parameterType317, elseIfs332, else_334, if_337, then339, createExpression342, if_327, expression344, then329, members355, extends357, typeParameters359, returnType362, parameters364, typeParameters367, exceptions370, type373, parameters346, typeParameters349, exceptions352, annotationType379, value382, value385, element387, paramTypes390, returnType392, type395, initialValue375, elementValuePairs378, importItems402, importedId403, exportDeclarations405, importDeclarations398, importedType399, importDeclarations401, parts411, richString412, line413, literal415, loop416, end417, start418, expression419, richStringIf421, elseStart422, elseIfConditions423, exportItems406, exportedId407, richString409, lines410, endIf425, richStringElseIf427, ifConditionStart429, ifConditionStart430, ifConditionStart432},
    generalizations={gen_model_types_JvmModule_JvmIdentifiableElement, gen_model_types_JvmType_JvmIdentifiableElement, gen_model_types_JvmVoid_JvmType, gen_model_types_JvmPrimitiveType_JvmComponentType, gen_model_types_JvmArrayType_JvmComponentType, gen_model_types_JvmDeclaredType_types_JvmMember, gen_model_types_JvmDeclaredType_types_JvmComponentType, gen_model_types_JvmComponentType_JvmType, gen_model_types_JvmTypeParameter_types_JvmComponentType, gen_model_types_JvmTypeParameter_types_JvmConstraintOwner, gen_model_types_JvmUpperBound_JvmTypeConstraint, gen_model_types_JvmLowerBound_JvmTypeConstraint, gen_model_types_JvmAnnotationType_JvmDeclaredType, gen_model_types_JvmEnumerationType_JvmDeclaredType, gen_model_types_JvmEnumerationLiteral_JvmField, gen_model_types_JvmGenericType_types_JvmDeclaredType, gen_model_types_JvmGenericType_types_JvmTypeParameterDeclarator, gen_model_types_JvmParameterizedTypeReference_JvmTypeReference, gen_model_types_JvmGenericArrayTypeReference_JvmTypeReference, gen_model_types_JvmWildcardTypeReference_types_JvmTypeReference, gen_model_types_JvmWildcardTypeReference_types_JvmConstraintOwner, gen_model_types_JvmAnyTypeReference_JvmTypeReference, gen_model_types_JvmFeature_JvmMember, gen_model_types_JvmField_JvmFeature, gen_model_types_JvmExecutable_types_JvmFeature, gen_model_types_JvmExecutable_types_JvmTypeParameterDeclarator, gen_model_types_JvmConstructor_JvmExecutable, gen_model_types_JvmMultiTypeReference_JvmCompoundTypeReference, gen_model_types_JvmMember_JvmAnnotationTarget, gen_model_types_JvmFormalParameter_JvmAnnotationTarget, gen_model_types_JvmAnnotationTarget_JvmIdentifiableElement, gen_model_types_JvmIntAnnotationValue_JvmAnnotationValue, gen_model_types_JvmBooleanAnnotationValue_JvmAnnotationValue, gen_model_types_JvmOperation_JvmExecutable, gen_model_types_JvmStringAnnotationValue_JvmAnnotationValue, gen_model_types_JvmTypeAnnotationValue_JvmAnnotationValue, gen_model_types_JvmAnnotationAnnotationValue_JvmAnnotationValue, gen_model_types_JvmEnumAnnotationValue_JvmAnnotationValue, gen_model_types_JvmDelegateTypeReference_JvmTypeReference, gen_model_types_JvmSpecializedTypeReference_JvmTypeReference, gen_model_types_JvmSynonymTypeReference_JvmCompoundTypeReference, gen_model_types_JvmUnknownTypeReference_JvmTypeReference, gen_model_types_JvmCompoundTypeReference_JvmTypeReference, gen_model_types_JvmByteAnnotationValue_JvmAnnotationValue, gen_model_types_JvmShortAnnotationValue_JvmAnnotationValue, gen_model_types_JvmLongAnnotationValue_JvmAnnotationValue, gen_model_types_JvmDoubleAnnotationValue_JvmAnnotationValue, gen_model_types_JvmFloatAnnotationValue_JvmAnnotationValue, gen_model_types_JvmCharAnnotationValue_JvmAnnotationValue, gen_model_xbase_XSwitchExpression_xbase_XExpression, gen_model_xbase_XSwitchExpression_types_JvmIdentifiableElement, gen_model_xbase_XBlockExpression_XExpression, gen_model_xbase_XVariableDeclaration_xbase_XExpression, gen_model_xbase_XVariableDeclaration_types_JvmIdentifiableElement, gen_model_types_JvmCustomAnnotationValue_JvmAnnotationValue, gen_model_xbase_XIfExpression_XExpression, gen_model_xbase_XMemberFeatureCall_XAbstractFeatureCall, gen_model_xbase_XVariableDeclarationList_XExpression, gen_model_xbase_XAbstractFeatureCall_XExpression, gen_model_xbase_XFeatureCall_XAbstractFeatureCall, gen_model_xbase_XConstructorCall_XExpression, gen_model_xbase_XMemberFeatureCall1_XAbstractFeatureCall, gen_model_xbase_XSetLiteral_XCollectionLiteral, gen_model_xbase_XClosure_xbase_XExpression, gen_model_xbase_XClosure_types_JvmIdentifiableElement, gen_model_xbase_XCastedExpression_XExpression, gen_model_xbase_XBooleanLiteral_XExpression, gen_model_xbase_XNullLiteral_XExpression, gen_model_xbase_XNumberLiteral_XExpression, gen_model_xbase_XStringLiteral_XExpression, gen_model_xbase_XCollectionLiteral_XExpression, gen_model_xbase_XListLiteral_XCollectionLiteral, gen_model_xbase_XKeyValuePair_XExpression, gen_model_xbase_XForLoopExpression_XExpression, gen_model_xbase_XForEachExpression_XExpression, gen_model_xbase_XBinaryOperation_XAbstractFeatureCall, gen_model_xbase_XUnaryOperation_XAbstractFeatureCall, gen_model_xbase_XWhileExpression_XAbstractWhileExpression, gen_model_xbase_XTypeLiteral_XExpression, gen_model_xbase_XInstanceOfExpression_XExpression, gen_model_xbase_XThrowExpression_XExpression, gen_model_xbase_XTryCatchFinallyExpression_XExpression, gen_model_xbase_XAbstractWhileExpression_XExpression, gen_model_xbase_XDoWhileExpression_XAbstractWhileExpression, gen_model_xbase_XAssignment_XAbstractFeatureCall, gen_model_xbase_XReturnExpression_XExpression, gen_model_xbase_XBreakExpression_XExpression, gen_model_xbase_XContinueExpression_XExpression, gen_model_xbase_XPrefixOperation_XAbstractFeatureCall, gen_model_xbase_XPostfixOperation_XAbstractFeatureCall, gen_model_xbase_XIndexOperation_XAbstractFeatureCall, gen_model_xbase_XFunctionDeclaration_XExpression, gen_model_xbase_XTernaryOperation_XExpression, gen_model_xbase_XArrayLiteral_XExpression, gen_model_ss_XtendClass_XtendTypeDeclaration, gen_model_xbase_XObjectLiteral_XExpression, gen_model_ss_XtendMember_XtendAnnotationTarget, gen_model_ss_XtendFunction_XtendMember, gen_model_ss_XtendField_XtendMember, gen_model_ss_RichString_XBlockExpression, gen_model_ss_RichStringLiteral_XStringLiteral, gen_model_ss_RichStringForLoop_XForEachExpression, gen_model_ss_RichStringIf_XExpression, gen_model_ss_XtendParameter_XtendAnnotationTarget, gen_model_ss_XtendConstructor_XtendMember, gen_model_ss_XtendAnnotationType_XtendTypeDeclaration, gen_model_ss_XtendInterface_XtendTypeDeclaration, gen_model_ss_XtendEnum_XtendTypeDeclaration, gen_model_ss_XtendEnumLiteral_XtendMember, gen_model_ss_XtendVariableDeclaration_XVariableDeclaration, gen_model_ss_XtendFormalParameter_JvmFormalParameter, gen_model_ss_XtendDelegate_XtendTypeDeclaration, gen_model_ss_XtendEvent_XtendMember, gen_model_ss_XtendTypeDeclaration_XtendMember, gen_model_xtype_XFunctionTypeRef_JvmSpecializedTypeReference, gen_model_xtype_XComputedTypeReference_JvmSpecializedTypeReference, gen_model_xannotation_XAnnotation_XExpression, gen_model_richstring_Literal_LinePart, gen_model_richstring_LineBreak_Literal, gen_model_richstring_ForLoopStart_LinePart, gen_model_richstring_ForLoopEnd_LinePart, gen_model_richstring_PrintedExpression_LinePart, gen_model_richstring_IfConditionStart_LinePart, gen_model_richstring_ElseIfCondition_LinePart, gen_model_richstring_ElseStart_LinePart, gen_model_richstring_EndIf_LinePart},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)