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
model_types_JvmModule = Class(name="model::types::JvmModule")
JvmIdentifiableElement = Class(name="JvmIdentifiableElement")
XImportSection1 = Class(name="XImportSection1")
types_model_EObject = Class(name="types::model::EObject")
XExportSection = Class(name="XExportSection")
model_types_JvmIdentifiableElement = Class(name="model::types::JvmIdentifiableElement", is_abstract=True)
model_types_JvmArrayType = Class(name="model::types::JvmArrayType")
model_types_JvmDeclaredType = Class(name="model::types::JvmDeclaredType")
types_JvmMember = Class(name="types::JvmMember")
types_JvmComponentType = Class(name="types::JvmComponentType")
JvmTypeReference = Class(name="JvmTypeReference")
model_types_JvmNoModule = Class(name="model::types::JvmNoModule")
model_types_JvmType = Class(name="model::types::JvmType", is_abstract=True)
model_types_JvmVoid = Class(name="model::types::JvmVoid")
JvmType = Class(name="JvmType")
model_types_JvmComponentType = Class(name="model::types::JvmComponentType", is_abstract=True)
JvmArrayType = Class(name="JvmArrayType")
model_types_JvmPrimitiveType = Class(name="model::types::JvmPrimitiveType")
JvmComponentType = Class(name="JvmComponentType")
model_types_JvmConstraintOwner = Class(name="model::types::JvmConstraintOwner", is_abstract=True)
JvmTypeConstraint = Class(name="JvmTypeConstraint")
model_types_JvmTypeConstraint = Class(name="model::types::JvmTypeConstraint", is_abstract=True)
JvmConstraintOwner = Class(name="JvmConstraintOwner")
model_types_JvmUpperBound = Class(name="model::types::JvmUpperBound")
model_types_JvmLowerBound = Class(name="model::types::JvmLowerBound")
model_types_JvmAnnotationType = Class(name="model::types::JvmAnnotationType")
JvmDeclaredType = Class(name="JvmDeclaredType")
JvmMember = Class(name="JvmMember")
model_types_JvmTypeParameter = Class(name="model::types::JvmTypeParameter")
types_JvmConstraintOwner = Class(name="types::JvmConstraintOwner")
JvmTypeParameterDeclarator = Class(name="JvmTypeParameterDeclarator")
model_types_JvmTypeParameterDeclarator = Class(name="model::types::JvmTypeParameterDeclarator", is_abstract=True)
JvmTypeParameter = Class(name="JvmTypeParameter")
model_types_JvmTypeReference = Class(name="model::types::JvmTypeReference", is_abstract=True)
model_types_JvmEnumerationType = Class(name="model::types::JvmEnumerationType")
JvmEnumerationLiteral = Class(name="JvmEnumerationLiteral")
model_types_JvmEnumerationLiteral = Class(name="model::types::JvmEnumerationLiteral")
JvmField = Class(name="JvmField")
model_types_JvmGenericType = Class(name="model::types::JvmGenericType")
types_JvmDeclaredType = Class(name="types::JvmDeclaredType")
types_JvmTypeParameterDeclarator = Class(name="types::JvmTypeParameterDeclarator")
JvmParameterizedTypeReference = Class(name="JvmParameterizedTypeReference")
model_types_JvmMultiTypeReference = Class(name="model::types::JvmMultiTypeReference")
JvmCompoundTypeReference = Class(name="JvmCompoundTypeReference")
model_types_JvmMember = Class(name="model::types::JvmMember")
JvmAnnotationTarget = Class(name="JvmAnnotationTarget")
model_types_JvmParameterizedTypeReference = Class(name="model::types::JvmParameterizedTypeReference")
model_types_JvmGenericArrayTypeReference = Class(name="model::types::JvmGenericArrayTypeReference")
model_types_JvmWildcardTypeReference = Class(name="model::types::JvmWildcardTypeReference")
types_JvmTypeReference = Class(name="types::JvmTypeReference")
model_types_JvmAnyTypeReference = Class(name="model::types::JvmAnyTypeReference")
model_types_JvmFeature = Class(name="model::types::JvmFeature", is_abstract=True)
model_types_JvmField = Class(name="model::types::JvmField")
JvmFeature = Class(name="JvmFeature")
model_types_JvmExecutable = Class(name="model::types::JvmExecutable", is_abstract=True)
types_JvmFeature = Class(name="types::JvmFeature")
XExpression = Class(name="XExpression")
model_types_JvmConstructor = Class(name="model::types::JvmConstructor")
JvmExecutable = Class(name="JvmExecutable")
JvmFormalParameter = Class(name="JvmFormalParameter")
JvmAnnotationValue = Class(name="JvmAnnotationValue")
model_types_JvmOperation = Class(name="model::types::JvmOperation")
model_types_JvmFormalParameter = Class(name="model::types::JvmFormalParameter")
model_types_JvmAnnotationReference = Class(name="model::types::JvmAnnotationReference")
JvmAnnotationType = Class(name="JvmAnnotationType")
model_types_JvmAnnotationValue = Class(name="model::types::JvmAnnotationValue")
JvmOperation = Class(name="JvmOperation")
model_types_JvmIntAnnotationValue = Class(name="model::types::JvmIntAnnotationValue")
model_types_JvmAnnotationTarget = Class(name="model::types::JvmAnnotationTarget", is_abstract=True)
JvmAnnotationReference = Class(name="JvmAnnotationReference")
model_types_JvmBooleanAnnotationValue = Class(name="model::types::JvmBooleanAnnotationValue")
model_types_JvmByteAnnotationValue = Class(name="model::types::JvmByteAnnotationValue")
model_types_JvmShortAnnotationValue = Class(name="model::types::JvmShortAnnotationValue")
model_types_JvmLongAnnotationValue = Class(name="model::types::JvmLongAnnotationValue")
model_types_JvmDoubleAnnotationValue = Class(name="model::types::JvmDoubleAnnotationValue")
model_types_JvmFloatAnnotationValue = Class(name="model::types::JvmFloatAnnotationValue")
model_types_JvmCharAnnotationValue = Class(name="model::types::JvmCharAnnotationValue")
model_types_JvmStringAnnotationValue = Class(name="model::types::JvmStringAnnotationValue")
model_types_JvmTypeAnnotationValue = Class(name="model::types::JvmTypeAnnotationValue")
model_types_JvmAnnotationAnnotationValue = Class(name="model::types::JvmAnnotationAnnotationValue")
model_types_JvmEnumAnnotationValue = Class(name="model::types::JvmEnumAnnotationValue")
model_types_JvmDelegateTypeReference = Class(name="model::types::JvmDelegateTypeReference")
model_types_JvmSpecializedTypeReference = Class(name="model::types::JvmSpecializedTypeReference", is_abstract=True)
model_types_JvmSynonymTypeReference = Class(name="model::types::JvmSynonymTypeReference")
model_types_JvmUnknownTypeReference = Class(name="model::types::JvmUnknownTypeReference")
model_types_JvmCompoundTypeReference = Class(name="model::types::JvmCompoundTypeReference", is_abstract=True)
model_types_JvmCustomAnnotationValue = Class(name="model::types::JvmCustomAnnotationValue")
model_xbase_XExpression = Class(name="model::xbase::XExpression", is_abstract=True)
model_xbase_XIfExpression = Class(name="model::xbase::XIfExpression")
model_xbase_XSwitchExpression = Class(name="model::xbase::XSwitchExpression")
xbase_XExpression = Class(name="xbase::XExpression")
types_JvmIdentifiableElement = Class(name="types::JvmIdentifiableElement")
XCasePart = Class(name="XCasePart")
model_xbase_XCasePart = Class(name="model::xbase::XCasePart")
model_xbase_XBlockExpression = Class(name="model::xbase::XBlockExpression")
model_xbase_XVariableDeclaration = Class(name="model::xbase::XVariableDeclaration")
model_xbase_XVariableDeclarationList = Class(name="model::xbase::XVariableDeclarationList")
model_xbase_XAbstractFeatureCall = Class(name="model::xbase::XAbstractFeatureCall", is_abstract=True)
model_xbase_XMemberFeatureCall = Class(name="model::xbase::XMemberFeatureCall")
XAbstractFeatureCall = Class(name="XAbstractFeatureCall")
model_xbase_XMemberFeatureCall1 = Class(name="model::xbase::XMemberFeatureCall1")
model_xbase_XFeatureCall = Class(name="model::xbase::XFeatureCall")
model_xbase_XConstructorCall = Class(name="model::xbase::XConstructorCall")
JvmConstructor = Class(name="JvmConstructor")
model_xbase_XBooleanLiteral = Class(name="model::xbase::XBooleanLiteral")
model_xbase_XNullLiteral = Class(name="model::xbase::XNullLiteral")
model_xbase_XNumberLiteral = Class(name="model::xbase::XNumberLiteral")
model_xbase_XStringLiteral = Class(name="model::xbase::XStringLiteral")
model_xbase_XCollectionLiteral = Class(name="model::xbase::XCollectionLiteral", is_abstract=True)
model_xbase_XListLiteral = Class(name="model::xbase::XListLiteral")
XCollectionLiteral = Class(name="XCollectionLiteral")
model_xbase_XKeyValuePair = Class(name="model::xbase::XKeyValuePair")
model_xbase_XSetLiteral = Class(name="model::xbase::XSetLiteral")
model_xbase_XClosure = Class(name="model::xbase::XClosure")
model_xbase_XCastedExpression = Class(name="model::xbase::XCastedExpression")
model_xbase_XBinaryOperation = Class(name="model::xbase::XBinaryOperation")
model_xbase_XUnaryOperation = Class(name="model::xbase::XUnaryOperation")
model_xbase_XForLoopExpression = Class(name="model::xbase::XForLoopExpression")
model_xbase_XForEachExpression = Class(name="model::xbase::XForEachExpression")
model_xbase_XAbstractWhileExpression = Class(name="model::xbase::XAbstractWhileExpression", is_abstract=True)
model_xbase_XDoWhileExpression = Class(name="model::xbase::XDoWhileExpression")
XAbstractWhileExpression = Class(name="XAbstractWhileExpression")
model_xbase_XWhileExpression = Class(name="model::xbase::XWhileExpression")
model_xbase_XTypeLiteral = Class(name="model::xbase::XTypeLiteral")
model_xbase_XInstanceOfExpression = Class(name="model::xbase::XInstanceOfExpression")
model_xbase_XThrowExpression = Class(name="model::xbase::XThrowExpression")
model_xbase_XTryCatchFinallyExpression = Class(name="model::xbase::XTryCatchFinallyExpression")
XCatchClause = Class(name="XCatchClause")
model_xbase_XCatchClause = Class(name="model::xbase::XCatchClause")
model_xbase_XAssignment = Class(name="model::xbase::XAssignment")
model_xbase_XReturnExpression = Class(name="model::xbase::XReturnExpression")
model_xbase_XBreakExpression = Class(name="model::xbase::XBreakExpression")
model_xbase_XContinueExpression = Class(name="model::xbase::XContinueExpression")
model_xbase_XPrefixOperation = Class(name="model::xbase::XPrefixOperation")
model_xbase_XPostfixOperation = Class(name="model::xbase::XPostfixOperation")
model_xbase_XTernaryOperation = Class(name="model::xbase::XTernaryOperation")
model_xbase_XIndexOperation = Class(name="model::xbase::XIndexOperation")
model_xbase_XFunctionDeclaration = Class(name="model::xbase::XFunctionDeclaration")
model_xbase_XObjectLiteralPart = Class(name="model::xbase::XObjectLiteralPart")
model_xbase_XObjectLiteral = Class(name="model::xbase::XObjectLiteral")
XObjectLiteralPart = Class(name="XObjectLiteralPart")
XtendTypeDeclaration = Class(name="XtendTypeDeclaration")
model_xbase_XArrayLiteral = Class(name="model::xbase::XArrayLiteral")
model_ss_XtendFile = Class(name="model::ss::XtendFile")
ss_model_EObject = Class(name="ss::model::EObject")
model_ss_XtendClass = Class(name="model::ss::XtendClass")
model_ss_XtendAnnotationTarget = Class(name="model::ss::XtendAnnotationTarget", is_abstract=True)
XAnnotation = Class(name="XAnnotation")
model_ss_XtendMember = Class(name="model::ss::XtendMember")
XtendAnnotationTarget = Class(name="XtendAnnotationTarget")
model_ss_XtendFunction = Class(name="model::ss::XtendFunction")
XtendMember = Class(name="XtendMember")
XtendParameter = Class(name="XtendParameter")
CreateExtensionInfo = Class(name="CreateExtensionInfo")
model_ss_XtendField = Class(name="model::ss::XtendField")
model_ss_XtendParameter = Class(name="model::ss::XtendParameter")
model_ss_RichString = Class(name="model::ss::RichString")
XBlockExpression = Class(name="XBlockExpression")
model_ss_RichStringLiteral = Class(name="model::ss::RichStringLiteral")
XStringLiteral = Class(name="XStringLiteral")
model_ss_RichStringForLoop = Class(name="model::ss::RichStringForLoop")
XForEachExpression = Class(name="XForEachExpression")
model_ss_RichStringIf = Class(name="model::ss::RichStringIf")
model_ss_RichStringElseIf = Class(name="model::ss::RichStringElseIf")
RichStringElseIf = Class(name="RichStringElseIf")
model_ss_XtendConstructor = Class(name="model::ss::XtendConstructor")
model_ss_CreateExtensionInfo = Class(name="model::ss::CreateExtensionInfo")
model_ss_XtendTypeDeclaration = Class(name="model::ss::XtendTypeDeclaration")
model_ss_XtendAnnotationType = Class(name="model::ss::XtendAnnotationType")
model_ss_XtendInterface = Class(name="model::ss::XtendInterface")
model_ss_XtendFormalParameter = Class(name="model::ss::XtendFormalParameter")
model_ss_XtendDelegate = Class(name="model::ss::XtendDelegate")
model_ss_XtendEnum = Class(name="model::ss::XtendEnum")
model_ss_XtendEnumLiteral = Class(name="model::ss::XtendEnumLiteral")
model_ss_XtendVariableDeclaration = Class(name="model::ss::XtendVariableDeclaration")
XVariableDeclaration = Class(name="XVariableDeclaration")
model_xannotation_XAnnotation = Class(name="model::xannotation::XAnnotation")
XAnnotationElementValuePair = Class(name="XAnnotationElementValuePair")
model_ss_XtendEvent = Class(name="model::ss::XtendEvent")
model_xannotation_XAnnotationElementValuePair = Class(name="model::xannotation::XAnnotationElementValuePair")
model_xtype_XComputedTypeReference = Class(name="model::xtype::XComputedTypeReference")
model_xtype_XImportSection = Class(name="model::xtype::XImportSection")
model_xtype_XFunctionTypeRef = Class(name="model::xtype::XFunctionTypeRef")
JvmSpecializedTypeReference = Class(name="JvmSpecializedTypeReference")
model_xtype_XImportSection1 = Class(name="model::xtype::XImportSection1")
XImportDeclaration1 = Class(name="XImportDeclaration1")
model_xtype_XImportDeclaration1 = Class(name="model::xtype::XImportDeclaration1")
XImportItem = Class(name="XImportItem")
model_xtype_XImportItem = Class(name="model::xtype::XImportItem")
XImportDeclaration = Class(name="XImportDeclaration")
model_xtype_XImportDeclaration = Class(name="model::xtype::XImportDeclaration")
model_xtype_XExportDeclaration = Class(name="model::xtype::XExportDeclaration")
XExportItem = Class(name="XExportItem")
model_xtype_XExportItem = Class(name="model::xtype::XExportItem")
model_richstring_ProcessedRichString = Class(name="model::richstring::ProcessedRichString")
RichString = Class(name="RichString")
model_xtype_XExportSection = Class(name="model::xtype::XExportSection")
XExportDeclaration = Class(name="XExportDeclaration")
LinePart = Class(name="LinePart")
ProcessedRichString = Class(name="ProcessedRichString")
model_richstring_LinePart = Class(name="model::richstring::LinePart")
model_richstring_Literal = Class(name="model::richstring::Literal")
RichStringLiteral = Class(name="RichStringLiteral")
Line = Class(name="Line")
model_richstring_ForLoopEnd = Class(name="model::richstring::ForLoopEnd")
model_richstring_Line = Class(name="model::richstring::Line")
ForLoopStart = Class(name="ForLoopStart")
model_richstring_PrintedExpression = Class(name="model::richstring::PrintedExpression")
model_richstring_LineBreak = Class(name="model::richstring::LineBreak")
Literal = Class(name="Literal")
model_richstring_ForLoopStart = Class(name="model::richstring::ForLoopStart")
RichStringForLoop = Class(name="RichStringForLoop")
ForLoopEnd = Class(name="ForLoopEnd")
EndIf = Class(name="EndIf")
model_richstring_ElseIfCondition = Class(name="model::richstring::ElseIfCondition")
IfConditionStart = Class(name="IfConditionStart")
model_richstring_ElseStart = Class(name="model::richstring::ElseStart")
model_richstring_IfConditionStart = Class(name="model::richstring::IfConditionStart")
RichStringIf = Class(name="RichStringIf")
ElseStart = Class(name="ElseStart")
ElseIfCondition = Class(name="ElseIfCondition")
model_richstring_EndIf = Class(name="model::richstring::EndIf")

# model_types_JvmModule class attributes and methods
model_types_JvmModule_simpleName: Property = Property(name="simpleName", type=StringType)
model_types_JvmModule.attributes={model_types_JvmModule_simpleName}

# JvmIdentifiableElement class attributes and methods

# XImportSection1 class attributes and methods

# types_model_EObject class attributes and methods

# XExportSection class attributes and methods

# model_types_JvmIdentifiableElement class attributes and methods
model_types_JvmIdentifiableElement_m_isExported: Method = Method(name="isExported", parameters={}, type=BooleanType)
model_types_JvmIdentifiableElement_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
model_types_JvmIdentifiableElement_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
model_types_JvmIdentifiableElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
model_types_JvmIdentifiableElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='innerClassDelimiter')}, type=StringType)
model_types_JvmIdentifiableElement.methods={model_types_JvmIdentifiableElement_m_getIdentifier, model_types_JvmIdentifiableElement_m_isExported, model_types_JvmIdentifiableElement_m_getQualifiedName, model_types_JvmIdentifiableElement_m_getSimpleName, model_types_JvmIdentifiableElement_m_getQualifiedName}

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
model_types_JvmDeclaredType_m_findAllFeaturesByName: Method = Method(name="findAllFeaturesByName", parameters={Parameter(name='simpleName')})
model_types_JvmDeclaredType_m_getAllFeatures: Method = Method(name="getAllFeatures", parameters={})
model_types_JvmDeclaredType.attributes={model_types_JvmDeclaredType_exported, model_types_JvmDeclaredType_packageName, model_types_JvmDeclaredType_static, model_types_JvmDeclaredType_final, model_types_JvmDeclaredType_abstract}
model_types_JvmDeclaredType.methods={model_types_JvmDeclaredType_m_getAllFeatures, model_types_JvmDeclaredType_m_getDeclaredFields, model_types_JvmDeclaredType_m_getDeclaredOperations, model_types_JvmDeclaredType_m_findAllFeaturesByName}

# types_JvmMember class attributes and methods

# types_JvmComponentType class attributes and methods

# JvmTypeReference class attributes and methods

# model_types_JvmNoModule class attributes and methods

# model_types_JvmType class attributes and methods

# model_types_JvmVoid class attributes and methods

# JvmType class attributes and methods

# model_types_JvmComponentType class attributes and methods

# JvmArrayType class attributes and methods

# model_types_JvmPrimitiveType class attributes and methods
model_types_JvmPrimitiveType_simpleName: Property = Property(name="simpleName", type=StringType)
model_types_JvmPrimitiveType.attributes={model_types_JvmPrimitiveType_simpleName}

# JvmComponentType class attributes and methods

# model_types_JvmConstraintOwner class attributes and methods

# JvmTypeConstraint class attributes and methods

# model_types_JvmTypeConstraint class attributes and methods
model_types_JvmTypeConstraint_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
model_types_JvmTypeConstraint_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
model_types_JvmTypeConstraint_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
model_types_JvmTypeConstraint_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='innerClassDelimiter')}, type=StringType)
model_types_JvmTypeConstraint.methods={model_types_JvmTypeConstraint_m_getQualifiedName, model_types_JvmTypeConstraint_m_getIdentifier, model_types_JvmTypeConstraint_m_getSimpleName, model_types_JvmTypeConstraint_m_getQualifiedName}

# JvmConstraintOwner class attributes and methods

# model_types_JvmUpperBound class attributes and methods

# model_types_JvmLowerBound class attributes and methods

# model_types_JvmAnnotationType class attributes and methods

# JvmDeclaredType class attributes and methods

# JvmMember class attributes and methods

# model_types_JvmTypeParameter class attributes and methods
model_types_JvmTypeParameter_name: Property = Property(name="name", type=StringType)
model_types_JvmTypeParameter.attributes={model_types_JvmTypeParameter_name}

# types_JvmConstraintOwner class attributes and methods

# JvmTypeParameterDeclarator class attributes and methods

# model_types_JvmTypeParameterDeclarator class attributes and methods

# JvmTypeParameter class attributes and methods

# model_types_JvmTypeReference class attributes and methods
model_types_JvmTypeReference_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
model_types_JvmTypeReference_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
model_types_JvmTypeReference_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
model_types_JvmTypeReference_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
model_types_JvmTypeReference_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='innerClassDelimiter')}, type=StringType)
model_types_JvmTypeReference_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
model_types_JvmTypeReference_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor'), Parameter(name='parameter')})
model_types_JvmTypeReference.methods={model_types_JvmTypeReference_m_getIdentifier, model_types_JvmTypeReference_m_getSimpleName, model_types_JvmTypeReference_m_accept, model_types_JvmTypeReference_m_getQualifiedName, model_types_JvmTypeReference_m_accept, model_types_JvmTypeReference_m_getType, model_types_JvmTypeReference_m_getQualifiedName}

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
model_types_JvmGenericType.methods={model_types_JvmGenericType_m_getDeclaredConstructors, model_types_JvmGenericType_m_getExtendedInterfaces, model_types_JvmGenericType_m_isInstantiateable, model_types_JvmGenericType_m_getExtendedClass}

# types_JvmDeclaredType class attributes and methods

# types_JvmTypeParameterDeclarator class attributes and methods

# JvmParameterizedTypeReference class attributes and methods

# model_types_JvmMultiTypeReference class attributes and methods

# JvmCompoundTypeReference class attributes and methods

# model_types_JvmMember class attributes and methods
model_types_JvmMember_modifiers: Property = Property(name="modifiers", type=StringType)
model_types_JvmMember_visibility: Property = Property(name="visibility", type=StringType)
model_types_JvmMember_simpleName: Property = Property(name="simpleName", type=StringType)
model_types_JvmMember_identifier: Property = Property(name="identifier", type=StringType)
model_types_JvmMember_m_internalSetIdentifier: Method = Method(name="internalSetIdentifier", parameters={Parameter(name='identifier')})
model_types_JvmMember.attributes={model_types_JvmMember_simpleName, model_types_JvmMember_visibility, model_types_JvmMember_modifiers, model_types_JvmMember_identifier}
model_types_JvmMember.methods={model_types_JvmMember_m_internalSetIdentifier}

# JvmAnnotationTarget class attributes and methods

# model_types_JvmParameterizedTypeReference class attributes and methods

# model_types_JvmGenericArrayTypeReference class attributes and methods
model_types_JvmGenericArrayTypeReference_m_getDimensions: Method = Method(name="getDimensions", parameters={}, type=IntegerType)
model_types_JvmGenericArrayTypeReference_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
model_types_JvmGenericArrayTypeReference.methods={model_types_JvmGenericArrayTypeReference_m_getDimensions, model_types_JvmGenericArrayTypeReference_m_getType}

# model_types_JvmWildcardTypeReference class attributes and methods

# types_JvmTypeReference class attributes and methods

# model_types_JvmAnyTypeReference class attributes and methods

# model_types_JvmFeature class attributes and methods
model_types_JvmFeature_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
model_types_JvmFeature.methods={model_types_JvmFeature_m_isStatic}

# model_types_JvmField class attributes and methods
model_types_JvmField_final: Property = Property(name="final", type=BooleanType)
model_types_JvmField_volatile: Property = Property(name="volatile", type=BooleanType)
model_types_JvmField_transient: Property = Property(name="transient", type=BooleanType)
model_types_JvmField_static: Property = Property(name="static", type=BooleanType)
model_types_JvmField.attributes={model_types_JvmField_volatile, model_types_JvmField_static, model_types_JvmField_final, model_types_JvmField_transient}

# JvmFeature class attributes and methods

# model_types_JvmExecutable class attributes and methods
model_types_JvmExecutable_varArgs: Property = Property(name="varArgs", type=BooleanType)
model_types_JvmExecutable.attributes={model_types_JvmExecutable_varArgs}

# types_JvmFeature class attributes and methods

# XExpression class attributes and methods

# model_types_JvmConstructor class attributes and methods

# JvmExecutable class attributes and methods

# JvmFormalParameter class attributes and methods

# JvmAnnotationValue class attributes and methods

# model_types_JvmOperation class attributes and methods
model_types_JvmOperation_static: Property = Property(name="static", type=BooleanType)
model_types_JvmOperation_final: Property = Property(name="final", type=BooleanType)
model_types_JvmOperation_abstract: Property = Property(name="abstract", type=BooleanType)
model_types_JvmOperation_default: Property = Property(name="default", type=BooleanType)
model_types_JvmOperation_native: Property = Property(name="native", type=BooleanType)
model_types_JvmOperation_strictFloatingPoint: Property = Property(name="strictFloatingPoint", type=BooleanType)
model_types_JvmOperation_synchronized: Property = Property(name="synchronized", type=BooleanType)
model_types_JvmOperation.attributes={model_types_JvmOperation_static, model_types_JvmOperation_abstract, model_types_JvmOperation_native, model_types_JvmOperation_strictFloatingPoint, model_types_JvmOperation_synchronized, model_types_JvmOperation_final, model_types_JvmOperation_default}

# model_types_JvmFormalParameter class attributes and methods
model_types_JvmFormalParameter_name: Property = Property(name="name", type=StringType)
model_types_JvmFormalParameter_varArg: Property = Property(name="varArg", type=BooleanType)
model_types_JvmFormalParameter.attributes={model_types_JvmFormalParameter_varArg, model_types_JvmFormalParameter_name}

# model_types_JvmAnnotationReference class attributes and methods

# JvmAnnotationType class attributes and methods

# model_types_JvmAnnotationValue class attributes and methods
model_types_JvmAnnotationValue_m_getValueName: Method = Method(name="getValueName", parameters={}, type=StringType)
model_types_JvmAnnotationValue.methods={model_types_JvmAnnotationValue_m_getValueName}

# JvmOperation class attributes and methods

# model_types_JvmIntAnnotationValue class attributes and methods
model_types_JvmIntAnnotationValue_values: Property = Property(name="values", type=IntegerType)
model_types_JvmIntAnnotationValue.attributes={model_types_JvmIntAnnotationValue_values}

# model_types_JvmAnnotationTarget class attributes and methods

# JvmAnnotationReference class attributes and methods

# model_types_JvmBooleanAnnotationValue class attributes and methods
model_types_JvmBooleanAnnotationValue_values: Property = Property(name="values", type=BooleanType)
model_types_JvmBooleanAnnotationValue.attributes={model_types_JvmBooleanAnnotationValue_values}

# model_types_JvmByteAnnotationValue class attributes and methods
model_types_JvmByteAnnotationValue_values: Property = Property(name="values", type=StringType)
model_types_JvmByteAnnotationValue.attributes={model_types_JvmByteAnnotationValue_values}

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

# model_types_JvmCustomAnnotationValue class attributes and methods
model_types_JvmCustomAnnotationValue_values: Property = Property(name="values", type=StringType)
model_types_JvmCustomAnnotationValue.attributes={model_types_JvmCustomAnnotationValue_values}

# model_xbase_XExpression class attributes and methods

# model_xbase_XIfExpression class attributes and methods

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
model_xbase_XVariableDeclaration.attributes={model_xbase_XVariableDeclaration_exported, model_xbase_XVariableDeclaration_writeable, model_xbase_XVariableDeclaration_name}

# model_xbase_XVariableDeclarationList class attributes and methods
model_xbase_XVariableDeclarationList_writeable: Property = Property(name="writeable", type=BooleanType)
model_xbase_XVariableDeclarationList_exported: Property = Property(name="exported", type=BooleanType)
model_xbase_XVariableDeclarationList.attributes={model_xbase_XVariableDeclarationList_writeable, model_xbase_XVariableDeclarationList_exported}

# model_xbase_XAbstractFeatureCall class attributes and methods
model_xbase_XAbstractFeatureCall_invalidFeatureIssueCode: Property = Property(name="invalidFeatureIssueCode", type=StringType)
model_xbase_XAbstractFeatureCall_validFeature: Property = Property(name="validFeature", type=BooleanType)
model_xbase_XAbstractFeatureCall_m_getConcreteSyntaxFeatureName: Method = Method(name="getConcreteSyntaxFeatureName", parameters={}, type=StringType)
model_xbase_XAbstractFeatureCall_m_getExplicitArguments: Method = Method(name="getExplicitArguments", parameters={}, type=StringType)
model_xbase_XAbstractFeatureCall_m_isExplicitOperationCallOrBuilderSyntax: Method = Method(name="isExplicitOperationCallOrBuilderSyntax", parameters={}, type=BooleanType)
model_xbase_XAbstractFeatureCall_m_getActualReceiver: Method = Method(name="getActualReceiver", parameters={}, type=StringType)
model_xbase_XAbstractFeatureCall_m_getActualArguments: Method = Method(name="getActualArguments", parameters={}, type=StringType)
model_xbase_XAbstractFeatureCall_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
model_xbase_XAbstractFeatureCall_m_isExtension: Method = Method(name="isExtension", parameters={}, type=BooleanType)
model_xbase_XAbstractFeatureCall_m_isPackageFragment: Method = Method(name="isPackageFragment", parameters={}, type=BooleanType)
model_xbase_XAbstractFeatureCall_m_isTypeLiteral: Method = Method(name="isTypeLiteral", parameters={}, type=BooleanType)
model_xbase_XAbstractFeatureCall.attributes={model_xbase_XAbstractFeatureCall_invalidFeatureIssueCode, model_xbase_XAbstractFeatureCall_validFeature}
model_xbase_XAbstractFeatureCall.methods={model_xbase_XAbstractFeatureCall_m_getActualReceiver, model_xbase_XAbstractFeatureCall_m_getConcreteSyntaxFeatureName, model_xbase_XAbstractFeatureCall_m_isPackageFragment, model_xbase_XAbstractFeatureCall_m_getExplicitArguments, model_xbase_XAbstractFeatureCall_m_isExtension, model_xbase_XAbstractFeatureCall_m_isTypeLiteral, model_xbase_XAbstractFeatureCall_m_getActualArguments, model_xbase_XAbstractFeatureCall_m_isStatic, model_xbase_XAbstractFeatureCall_m_isExplicitOperationCallOrBuilderSyntax}

# model_xbase_XMemberFeatureCall class attributes and methods
model_xbase_XMemberFeatureCall_nullSafe: Property = Property(name="nullSafe", type=BooleanType)
model_xbase_XMemberFeatureCall_explicitOperationCall: Property = Property(name="explicitOperationCall", type=BooleanType)
model_xbase_XMemberFeatureCall_explicitStatic: Property = Property(name="explicitStatic", type=BooleanType)
model_xbase_XMemberFeatureCall_typeLiteral: Property = Property(name="typeLiteral", type=BooleanType)
model_xbase_XMemberFeatureCall_staticWithDeclaringType: Property = Property(name="staticWithDeclaringType", type=BooleanType)
model_xbase_XMemberFeatureCall_packageFragment: Property = Property(name="packageFragment", type=BooleanType)
model_xbase_XMemberFeatureCall_indexedOperation: Property = Property(name="indexedOperation", type=BooleanType)
model_xbase_XMemberFeatureCall.attributes={model_xbase_XMemberFeatureCall_packageFragment, model_xbase_XMemberFeatureCall_staticWithDeclaringType, model_xbase_XMemberFeatureCall_explicitOperationCall, model_xbase_XMemberFeatureCall_nullSafe, model_xbase_XMemberFeatureCall_indexedOperation, model_xbase_XMemberFeatureCall_explicitStatic, model_xbase_XMemberFeatureCall_typeLiteral}

# XAbstractFeatureCall class attributes and methods

# model_xbase_XMemberFeatureCall1 class attributes and methods
model_xbase_XMemberFeatureCall1_explicitOperationCall: Property = Property(name="explicitOperationCall", type=BooleanType)
model_xbase_XMemberFeatureCall1_explicitStatic: Property = Property(name="explicitStatic", type=BooleanType)
model_xbase_XMemberFeatureCall1_nullSafe: Property = Property(name="nullSafe", type=BooleanType)
model_xbase_XMemberFeatureCall1_typeLiteral: Property = Property(name="typeLiteral", type=BooleanType)
model_xbase_XMemberFeatureCall1_staticWithDeclaringType: Property = Property(name="staticWithDeclaringType", type=BooleanType)
model_xbase_XMemberFeatureCall1_packageFragment: Property = Property(name="packageFragment", type=BooleanType)
model_xbase_XMemberFeatureCall1_indexedOperation: Property = Property(name="indexedOperation", type=BooleanType)
model_xbase_XMemberFeatureCall1.attributes={model_xbase_XMemberFeatureCall1_typeLiteral, model_xbase_XMemberFeatureCall1_staticWithDeclaringType, model_xbase_XMemberFeatureCall1_packageFragment, model_xbase_XMemberFeatureCall1_explicitStatic, model_xbase_XMemberFeatureCall1_nullSafe, model_xbase_XMemberFeatureCall1_indexedOperation, model_xbase_XMemberFeatureCall1_explicitOperationCall}

# model_xbase_XFeatureCall class attributes and methods
model_xbase_XFeatureCall_explicitOperationCall: Property = Property(name="explicitOperationCall", type=BooleanType)
model_xbase_XFeatureCall_typeLiteral: Property = Property(name="typeLiteral", type=BooleanType)
model_xbase_XFeatureCall_packageFragment: Property = Property(name="packageFragment", type=BooleanType)
model_xbase_XFeatureCall_indexedOperation: Property = Property(name="indexedOperation", type=BooleanType)
model_xbase_XFeatureCall.attributes={model_xbase_XFeatureCall_typeLiteral, model_xbase_XFeatureCall_explicitOperationCall, model_xbase_XFeatureCall_indexedOperation, model_xbase_XFeatureCall_packageFragment}

# model_xbase_XConstructorCall class attributes and methods
model_xbase_XConstructorCall_invalidFeatureIssueCode: Property = Property(name="invalidFeatureIssueCode", type=StringType)
model_xbase_XConstructorCall_validFeature: Property = Property(name="validFeature", type=BooleanType)
model_xbase_XConstructorCall.attributes={model_xbase_XConstructorCall_invalidFeatureIssueCode, model_xbase_XConstructorCall_validFeature}

# JvmConstructor class attributes and methods

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

# model_xbase_XBinaryOperation class attributes and methods

# model_xbase_XUnaryOperation class attributes and methods

# model_xbase_XForLoopExpression class attributes and methods

# model_xbase_XForEachExpression class attributes and methods

# model_xbase_XAbstractWhileExpression class attributes and methods

# model_xbase_XDoWhileExpression class attributes and methods

# XAbstractWhileExpression class attributes and methods

# model_xbase_XWhileExpression class attributes and methods

# model_xbase_XTypeLiteral class attributes and methods
model_xbase_XTypeLiteral_arrayDimensions: Property = Property(name="arrayDimensions", type=StringType)
model_xbase_XTypeLiteral.attributes={model_xbase_XTypeLiteral_arrayDimensions}

# model_xbase_XInstanceOfExpression class attributes and methods

# model_xbase_XThrowExpression class attributes and methods

# model_xbase_XTryCatchFinallyExpression class attributes and methods

# XCatchClause class attributes and methods

# model_xbase_XCatchClause class attributes and methods

# model_xbase_XAssignment class attributes and methods
model_xbase_XAssignment_explicitStatic: Property = Property(name="explicitStatic", type=BooleanType)
model_xbase_XAssignment.attributes={model_xbase_XAssignment_explicitStatic}

# model_xbase_XReturnExpression class attributes and methods

# model_xbase_XBreakExpression class attributes and methods

# model_xbase_XContinueExpression class attributes and methods

# model_xbase_XPrefixOperation class attributes and methods

# model_xbase_XPostfixOperation class attributes and methods

# model_xbase_XTernaryOperation class attributes and methods

# model_xbase_XIndexOperation class attributes and methods

# model_xbase_XFunctionDeclaration class attributes and methods
model_xbase_XFunctionDeclaration_name: Property = Property(name="name", type=StringType)
model_xbase_XFunctionDeclaration.attributes={model_xbase_XFunctionDeclaration_name}

# model_xbase_XObjectLiteralPart class attributes and methods
model_xbase_XObjectLiteralPart_name: Property = Property(name="name", type=StringType)
model_xbase_XObjectLiteralPart.attributes={model_xbase_XObjectLiteralPart_name}

# model_xbase_XObjectLiteral class attributes and methods

# XObjectLiteralPart class attributes and methods

# XtendTypeDeclaration class attributes and methods

# model_xbase_XArrayLiteral class attributes and methods

# model_ss_XtendFile class attributes and methods
model_ss_XtendFile_package: Property = Property(name="package", type=StringType)
model_ss_XtendFile.attributes={model_ss_XtendFile_package}

# ss_model_EObject class attributes and methods

# model_ss_XtendClass class attributes and methods
model_ss_XtendClass_m_isAbstract: Method = Method(name="isAbstract", parameters={}, type=BooleanType)
model_ss_XtendClass.methods={model_ss_XtendClass_m_isAbstract}

# model_ss_XtendAnnotationTarget class attributes and methods

# XAnnotation class attributes and methods

# model_ss_XtendMember class attributes and methods
model_ss_XtendMember_modifiers: Property = Property(name="modifiers", type=StringType)
model_ss_XtendMember_m_getVisibility: Method = Method(name="getVisibility", parameters={}, type=StringType)
model_ss_XtendMember_m_getDeclaredVisibility: Method = Method(name="getDeclaredVisibility", parameters={}, type=StringType)
model_ss_XtendMember_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
model_ss_XtendMember_m_isFinal: Method = Method(name="isFinal", parameters={}, type=BooleanType)
model_ss_XtendMember.attributes={model_ss_XtendMember_modifiers}
model_ss_XtendMember.methods={model_ss_XtendMember_m_isFinal, model_ss_XtendMember_m_isStatic, model_ss_XtendMember_m_getDeclaredVisibility, model_ss_XtendMember_m_getVisibility}

# XtendAnnotationTarget class attributes and methods

# model_ss_XtendFunction class attributes and methods
model_ss_XtendFunction_name: Property = Property(name="name", type=StringType)
model_ss_XtendFunction_m_isAbstract: Method = Method(name="isAbstract", parameters={}, type=BooleanType)
model_ss_XtendFunction_m_isOverride: Method = Method(name="isOverride", parameters={}, type=BooleanType)
model_ss_XtendFunction_m_isDispatch: Method = Method(name="isDispatch", parameters={}, type=BooleanType)
model_ss_XtendFunction.attributes={model_ss_XtendFunction_name}
model_ss_XtendFunction.methods={model_ss_XtendFunction_m_isOverride, model_ss_XtendFunction_m_isAbstract, model_ss_XtendFunction_m_isDispatch}

# XtendMember class attributes and methods

# XtendParameter class attributes and methods

# CreateExtensionInfo class attributes and methods

# model_ss_XtendField class attributes and methods
model_ss_XtendField_name: Property = Property(name="name", type=StringType)
model_ss_XtendField_m_isExtension: Method = Method(name="isExtension", parameters={}, type=BooleanType)
model_ss_XtendField.attributes={model_ss_XtendField_name}
model_ss_XtendField.methods={model_ss_XtendField_m_isExtension}

# model_ss_XtendParameter class attributes and methods
model_ss_XtendParameter_name: Property = Property(name="name", type=StringType)
model_ss_XtendParameter_varArg: Property = Property(name="varArg", type=BooleanType)
model_ss_XtendParameter_extension: Property = Property(name="extension", type=BooleanType)
model_ss_XtendParameter.attributes={model_ss_XtendParameter_extension, model_ss_XtendParameter_varArg, model_ss_XtendParameter_name}

# model_ss_RichString class attributes and methods

# XBlockExpression class attributes and methods

# model_ss_RichStringLiteral class attributes and methods

# XStringLiteral class attributes and methods

# model_ss_RichStringForLoop class attributes and methods

# XForEachExpression class attributes and methods

# model_ss_RichStringIf class attributes and methods

# model_ss_RichStringElseIf class attributes and methods

# RichStringElseIf class attributes and methods

# model_ss_XtendConstructor class attributes and methods

# model_ss_CreateExtensionInfo class attributes and methods
model_ss_CreateExtensionInfo_name: Property = Property(name="name", type=StringType)
model_ss_CreateExtensionInfo.attributes={model_ss_CreateExtensionInfo_name}

# model_ss_XtendTypeDeclaration class attributes and methods
model_ss_XtendTypeDeclaration_name: Property = Property(name="name", type=StringType)
model_ss_XtendTypeDeclaration.attributes={model_ss_XtendTypeDeclaration_name}

# model_ss_XtendAnnotationType class attributes and methods

# model_ss_XtendInterface class attributes and methods

# model_ss_XtendFormalParameter class attributes and methods
model_ss_XtendFormalParameter_extension: Property = Property(name="extension", type=BooleanType)
model_ss_XtendFormalParameter.attributes={model_ss_XtendFormalParameter_extension}

# model_ss_XtendDelegate class attributes and methods

# model_ss_XtendEnum class attributes and methods

# model_ss_XtendEnumLiteral class attributes and methods
model_ss_XtendEnumLiteral_name: Property = Property(name="name", type=StringType)
model_ss_XtendEnumLiteral.attributes={model_ss_XtendEnumLiteral_name}

# model_ss_XtendVariableDeclaration class attributes and methods
model_ss_XtendVariableDeclaration_extension: Property = Property(name="extension", type=BooleanType)
model_ss_XtendVariableDeclaration.attributes={model_ss_XtendVariableDeclaration_extension}

# XVariableDeclaration class attributes and methods

# model_xannotation_XAnnotation class attributes and methods

# XAnnotationElementValuePair class attributes and methods

# model_ss_XtendEvent class attributes and methods
model_ss_XtendEvent_name: Property = Property(name="name", type=StringType)
model_ss_XtendEvent_m_isExtension: Method = Method(name="isExtension", parameters={}, type=BooleanType)
model_ss_XtendEvent.attributes={model_ss_XtendEvent_name}
model_ss_XtendEvent.methods={model_ss_XtendEvent_m_isExtension}

# model_xannotation_XAnnotationElementValuePair class attributes and methods

# model_xtype_XComputedTypeReference class attributes and methods
model_xtype_XComputedTypeReference_typeProvider: Property = Property(name="typeProvider", type=StringType)
model_xtype_XComputedTypeReference.attributes={model_xtype_XComputedTypeReference_typeProvider}

# model_xtype_XImportSection class attributes and methods

# model_xtype_XFunctionTypeRef class attributes and methods
model_xtype_XFunctionTypeRef_instanceContext: Property = Property(name="instanceContext", type=BooleanType)
model_xtype_XFunctionTypeRef.attributes={model_xtype_XFunctionTypeRef_instanceContext}

# JvmSpecializedTypeReference class attributes and methods

# model_xtype_XImportSection1 class attributes and methods

# XImportDeclaration1 class attributes and methods

# model_xtype_XImportDeclaration1 class attributes and methods
model_xtype_XImportDeclaration1_alias: Property = Property(name="alias", type=StringType)
model_xtype_XImportDeclaration1_importURI: Property = Property(name="importURI", type=StringType)
model_xtype_XImportDeclaration1_m_isWildcard: Method = Method(name="isWildcard", parameters={}, type=BooleanType)
model_xtype_XImportDeclaration1.attributes={model_xtype_XImportDeclaration1_alias, model_xtype_XImportDeclaration1_importURI}
model_xtype_XImportDeclaration1.methods={model_xtype_XImportDeclaration1_m_isWildcard}

# XImportItem class attributes and methods

# model_xtype_XImportItem class attributes and methods
model_xtype_XImportItem_alias: Property = Property(name="alias", type=StringType)
model_xtype_XImportItem.attributes={model_xtype_XImportItem_alias}

# XImportDeclaration class attributes and methods

# model_xtype_XImportDeclaration class attributes and methods
model_xtype_XImportDeclaration_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
model_xtype_XImportDeclaration_wildcard: Property = Property(name="wildcard", type=BooleanType)
model_xtype_XImportDeclaration_extension: Property = Property(name="extension", type=BooleanType)
model_xtype_XImportDeclaration_static: Property = Property(name="static", type=BooleanType)
model_xtype_XImportDeclaration_m_getImportedTypeName: Method = Method(name="getImportedTypeName", parameters={}, type=StringType)
model_xtype_XImportDeclaration.attributes={model_xtype_XImportDeclaration_static, model_xtype_XImportDeclaration_importedNamespace, model_xtype_XImportDeclaration_wildcard, model_xtype_XImportDeclaration_extension}
model_xtype_XImportDeclaration.methods={model_xtype_XImportDeclaration_m_getImportedTypeName}

# model_xtype_XExportDeclaration class attributes and methods
model_xtype_XExportDeclaration_alias: Property = Property(name="alias", type=StringType)
model_xtype_XExportDeclaration_wildcard: Property = Property(name="wildcard", type=BooleanType)
model_xtype_XExportDeclaration_importURI: Property = Property(name="importURI", type=StringType)
model_xtype_XExportDeclaration.attributes={model_xtype_XExportDeclaration_importURI, model_xtype_XExportDeclaration_alias, model_xtype_XExportDeclaration_wildcard}

# XExportItem class attributes and methods

# model_xtype_XExportItem class attributes and methods
model_xtype_XExportItem_alias: Property = Property(name="alias", type=StringType)
model_xtype_XExportItem.attributes={model_xtype_XExportItem_alias}

# model_richstring_ProcessedRichString class attributes and methods

# RichString class attributes and methods

# model_xtype_XExportSection class attributes and methods

# XExportDeclaration class attributes and methods

# LinePart class attributes and methods

# ProcessedRichString class attributes and methods

# model_richstring_LinePart class attributes and methods

# model_richstring_Literal class attributes and methods
model_richstring_Literal_offset: Property = Property(name="offset", type=IntegerType)
model_richstring_Literal_length: Property = Property(name="length", type=IntegerType)
model_richstring_Literal.attributes={model_richstring_Literal_length, model_richstring_Literal_offset}

# RichStringLiteral class attributes and methods

# Line class attributes and methods

# model_richstring_ForLoopEnd class attributes and methods

# model_richstring_Line class attributes and methods

# ForLoopStart class attributes and methods

# model_richstring_PrintedExpression class attributes and methods

# model_richstring_LineBreak class attributes and methods

# Literal class attributes and methods

# model_richstring_ForLoopStart class attributes and methods

# RichStringForLoop class attributes and methods

# ForLoopEnd class attributes and methods

# EndIf class attributes and methods

# model_richstring_ElseIfCondition class attributes and methods

# IfConditionStart class attributes and methods

# model_richstring_ElseStart class attributes and methods

# model_richstring_IfConditionStart class attributes and methods

# RichStringIf class attributes and methods

# ElseStart class attributes and methods

# ElseIfCondition class attributes and methods

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
componentType11: BinaryAssociation = BinaryAssociation(
    name="componentType11",
    ends={
        Property(name="types12", type=model_types_JvmArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="JvmComponentType", type=JvmComponentType, multiplicity=Multiplicity(0, 1))
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
        Property(name="types", type=model_types_JvmComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="JvmArrayType", type=JvmArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints20: BinaryAssociation = BinaryAssociation(
    name="constraints20",
    ends={
        Property(name="types21", type=model_types_JvmConstraintOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="JvmTypeConstraint", type=JvmTypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeReference22: BinaryAssociation = BinaryAssociation(
    name="typeReference22",
    ends={
        Property(name="JvmTypeReference23", type=model_types_JvmTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmTypeConstraint", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owner24: BinaryAssociation = BinaryAssociation(
    name="owner24",
    ends={
        Property(name="types25", type=model_types_JvmTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="JvmConstraintOwner", type=JvmConstraintOwner, multiplicity=Multiplicity(0, 1))
    }
)
superTypes13: BinaryAssociation = BinaryAssociation(
    name="superTypes13",
    ends={
        Property(name="JvmTypeReference", type=model_types_JvmDeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmDeclaredType", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members14: BinaryAssociation = BinaryAssociation(
    name="members14",
    ends={
        Property(name="types15", type=model_types_JvmDeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="JvmMember", type=JvmMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarator16: BinaryAssociation = BinaryAssociation(
    name="declarator16",
    ends={
        Property(name="types17", type=model_types_JvmTypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="JvmTypeParameterDeclarator", type=JvmTypeParameterDeclarator, multiplicity=Multiplicity(0, 1))
    }
)
typeParameters18: BinaryAssociation = BinaryAssociation(
    name="typeParameters18",
    ends={
        Property(name="types19", type=model_types_JvmTypeParameterDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="JvmTypeParameter", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements28: BinaryAssociation = BinaryAssociation(
    name="implements28",
    ends={
        Property(name="JvmParameterizedTypeReference30", type=model_types_JvmGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmGenericType29", type=JvmParameterizedTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literals26: BinaryAssociation = BinaryAssociation(
    name="literals26",
    ends={
        Property(name="JvmEnumerationLiteral", type=model_types_JvmEnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmEnumerationType", type=JvmEnumerationLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
extends27: BinaryAssociation = BinaryAssociation(
    name="extends27",
    ends={
        Property(name="JvmParameterizedTypeReference", type=model_types_JvmGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmGenericType", type=JvmParameterizedTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaringType39: BinaryAssociation = BinaryAssociation(
    name="declaringType39",
    ends={
        Property(name="types40", type=model_types_JvmMember, multiplicity=Multiplicity(1, 1)),
        Property(name="JvmDeclaredType", type=JvmDeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
arguments31: BinaryAssociation = BinaryAssociation(
    name="arguments31",
    ends={
        Property(name="JvmTypeReference32", type=model_types_JvmParameterizedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmParameterizedTypeReference", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="JvmType", type=model_types_JvmParameterizedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmParameterizedTypeReference34", type=JvmType, multiplicity=Multiplicity(0, 1))
    }
)
componentType35: BinaryAssociation = BinaryAssociation(
    name="componentType35",
    ends={
        Property(name="JvmTypeReference36", type=model_types_JvmGenericArrayTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmGenericArrayTypeReference", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type37: BinaryAssociation = BinaryAssociation(
    name="type37",
    ends={
        Property(name="JvmType38", type=model_types_JvmAnyTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnyTypeReference", type=JvmType, multiplicity=Multiplicity(0, 1))
    }
)
annotationInfo41: BinaryAssociation = BinaryAssociation(
    name="annotationInfo41",
    ends={
        Property(name="model_types_JvmMember", type=JvmAnnotationTarget, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="JvmAnnotationTarget", type=model_types_JvmMember, multiplicity=Multiplicity(1, 1))
    }
)
type42: BinaryAssociation = BinaryAssociation(
    name="type42",
    ends={
        Property(name="JvmTypeReference43", type=model_types_JvmField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmField", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
get49: BinaryAssociation = BinaryAssociation(
    name="get49",
    ends={
        Property(name="XExpression51", type=model_types_JvmField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmField50", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue44: BinaryAssociation = BinaryAssociation(
    name="defaultValue44",
    ends={
        Property(name="XExpression", type=model_types_JvmField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmField45", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
set46: BinaryAssociation = BinaryAssociation(
    name="set46",
    ends={
        Property(name="XExpression48", type=model_types_JvmField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmField47", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression56: BinaryAssociation = BinaryAssociation(
    name="expression56",
    ends={
        Property(name="XExpression57", type=model_types_JvmConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmConstructor", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters52: BinaryAssociation = BinaryAssociation(
    name="parameters52",
    ends={
        Property(name="JvmFormalParameter", type=model_types_JvmExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmExecutable", type=JvmFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions53: BinaryAssociation = BinaryAssociation(
    name="exceptions53",
    ends={
        Property(name="JvmTypeReference55", type=model_types_JvmExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmExecutable54", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue60: BinaryAssociation = BinaryAssociation(
    name="defaultValue60",
    ends={
        Property(name="JvmAnnotationValue", type=model_types_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmOperation61", type=JvmAnnotationValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType58: BinaryAssociation = BinaryAssociation(
    name="returnType58",
    ends={
        Property(name="JvmTypeReference59", type=model_types_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmOperation", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression62: BinaryAssociation = BinaryAssociation(
    name="expression62",
    ends={
        Property(name="XExpression64", type=model_types_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmOperation63", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function65: BinaryAssociation = BinaryAssociation(
    name="function65",
    ends={
        Property(name="XExpression67", type=model_types_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmOperation66", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations73: BinaryAssociation = BinaryAssociation(
    name="annotations73",
    ends={
        Property(name="JvmAnnotationReference", type=model_types_JvmAnnotationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationTarget", type=JvmAnnotationReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation74: BinaryAssociation = BinaryAssociation(
    name="annotation74",
    ends={
        Property(name="JvmAnnotationType", type=model_types_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationReference", type=JvmAnnotationType, multiplicity=Multiplicity(0, 1))
    }
)
values75: BinaryAssociation = BinaryAssociation(
    name="values75",
    ends={
        Property(name="JvmAnnotationValue77", type=model_types_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationReference76", type=JvmAnnotationValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value78: BinaryAssociation = BinaryAssociation(
    name="value78",
    ends={
        Property(name="XExpression80", type=model_types_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationReference79", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterType68: BinaryAssociation = BinaryAssociation(
    name="parameterType68",
    ends={
        Property(name="JvmTypeReference69", type=model_types_JvmFormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmFormalParameter", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation81: BinaryAssociation = BinaryAssociation(
    name="operation81",
    ends={
        Property(name="JvmOperation", type=model_types_JvmAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationValue", type=JvmOperation, multiplicity=Multiplicity(0, 1))
    }
)
value82: BinaryAssociation = BinaryAssociation(
    name="value82",
    ends={
        Property(name="XExpression84", type=model_types_JvmAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationValue83", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue70: BinaryAssociation = BinaryAssociation(
    name="defaultValue70",
    ends={
        Property(name="XExpression72", type=model_types_JvmFormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmFormalParameter71", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values85: BinaryAssociation = BinaryAssociation(
    name="values85",
    ends={
        Property(name="JvmTypeReference86", type=model_types_JvmTypeAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmTypeAnnotationValue", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values87: BinaryAssociation = BinaryAssociation(
    name="values87",
    ends={
        Property(name="JvmAnnotationReference88", type=model_types_JvmAnnotationAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmAnnotationAnnotationValue", type=JvmAnnotationReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values89: BinaryAssociation = BinaryAssociation(
    name="values89",
    ends={
        Property(name="JvmEnumerationLiteral90", type=model_types_JvmEnumAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmEnumAnnotationValue", type=JvmEnumerationLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
delegate91: BinaryAssociation = BinaryAssociation(
    name="delegate91",
    ends={
        Property(name="JvmTypeReference92", type=model_types_JvmDelegateTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmDelegateTypeReference", type=JvmTypeReference, multiplicity=Multiplicity(0, 1))
    }
)
equivalent93: BinaryAssociation = BinaryAssociation(
    name="equivalent93",
    ends={
        Property(name="JvmTypeReference94", type=model_types_JvmSpecializedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmSpecializedTypeReference", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type95: BinaryAssociation = BinaryAssociation(
    name="type95",
    ends={
        Property(name="JvmType96", type=model_types_JvmCompoundTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmCompoundTypeReference", type=JvmType, multiplicity=Multiplicity(0, 1))
    }
)
references97: BinaryAssociation = BinaryAssociation(
    name="references97",
    ends={
        Property(name="JvmTypeReference99", type=model_types_JvmCompoundTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="model_types_JvmCompoundTypeReference98", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
if100: BinaryAssociation = BinaryAssociation(
    name="if100",
    ends={
        Property(name="XExpression101", type=model_xbase_XIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XIfExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then102: BinaryAssociation = BinaryAssociation(
    name="then102",
    ends={
        Property(name="XExpression104", type=model_xbase_XIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XIfExpression103", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else105: BinaryAssociation = BinaryAssociation(
    name="else105",
    ends={
        Property(name="XExpression107", type=model_xbase_XIfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XIfExpression106", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switch108: BinaryAssociation = BinaryAssociation(
    name="switch108",
    ends={
        Property(name="XExpression109", type=model_xbase_XSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XSwitchExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases110: BinaryAssociation = BinaryAssociation(
    name="cases110",
    ends={
        Property(name="XCasePart", type=model_xbase_XSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XSwitchExpression111", type=XCasePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
default112: BinaryAssociation = BinaryAssociation(
    name="default112",
    ends={
        Property(name="XExpression114", type=model_xbase_XSwitchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XSwitchExpression113", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case115: BinaryAssociation = BinaryAssociation(
    name="case115",
    ends={
        Property(name="XExpression116", type=model_xbase_XCasePart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCasePart", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then117: BinaryAssociation = BinaryAssociation(
    name="then117",
    ends={
        Property(name="XExpression119", type=model_xbase_XCasePart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCasePart118", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeGuard120: BinaryAssociation = BinaryAssociation(
    name="typeGuard120",
    ends={
        Property(name="JvmTypeReference122", type=model_xbase_XCasePart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCasePart121", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions123: BinaryAssociation = BinaryAssociation(
    name="expressions123",
    ends={
        Property(name="XExpression124", type=model_xbase_XBlockExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XBlockExpression", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type125: BinaryAssociation = BinaryAssociation(
    name="type125",
    ends={
        Property(name="JvmTypeReference126", type=model_xbase_XVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XVariableDeclaration", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right127: BinaryAssociation = BinaryAssociation(
    name="right127",
    ends={
        Property(name="XExpression129", type=model_xbase_XVariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XVariableDeclaration128", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarations130: BinaryAssociation = BinaryAssociation(
    name="declarations130",
    ends={
        Property(name="XExpression131", type=model_xbase_XVariableDeclarationList, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XVariableDeclarationList", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature132: BinaryAssociation = BinaryAssociation(
    name="feature132",
    ends={
        Property(name="JvmIdentifiableElement", type=model_xbase_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractFeatureCall", type=JvmIdentifiableElement, multiplicity=Multiplicity(0, 1))
    }
)
typeArguments133: BinaryAssociation = BinaryAssociation(
    name="typeArguments133",
    ends={
        Property(name="JvmTypeReference135", type=model_xbase_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractFeatureCall134", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implicitReceiver136: BinaryAssociation = BinaryAssociation(
    name="implicitReceiver136",
    ends={
        Property(name="XExpression138", type=model_xbase_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractFeatureCall137", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implicitFirstArgument139: BinaryAssociation = BinaryAssociation(
    name="implicitFirstArgument139",
    ends={
        Property(name="XExpression141", type=model_xbase_XAbstractFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractFeatureCall140", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberCallTarget142: BinaryAssociation = BinaryAssociation(
    name="memberCallTarget142",
    ends={
        Property(name="XExpression143", type=model_xbase_XMemberFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XMemberFeatureCall", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberCallArguments144: BinaryAssociation = BinaryAssociation(
    name="memberCallArguments144",
    ends={
        Property(name="XExpression146", type=model_xbase_XMemberFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XMemberFeatureCall145", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberCallTarget147: BinaryAssociation = BinaryAssociation(
    name="memberCallTarget147",
    ends={
        Property(name="XExpression148", type=model_xbase_XMemberFeatureCall1, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XMemberFeatureCall1", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberCallArguments149: BinaryAssociation = BinaryAssociation(
    name="memberCallArguments149",
    ends={
        Property(name="XExpression151", type=model_xbase_XMemberFeatureCall1, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XMemberFeatureCall1150", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureCallArguments152: BinaryAssociation = BinaryAssociation(
    name="featureCallArguments152",
    ends={
        Property(name="XExpression153", type=model_xbase_XFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XFeatureCall", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value154: BinaryAssociation = BinaryAssociation(
    name="value154",
    ends={
        Property(name="XExpression156", type=model_xbase_XFeatureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XFeatureCall155", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constructor157: BinaryAssociation = BinaryAssociation(
    name="constructor157",
    ends={
        Property(name="JvmConstructor", type=model_xbase_XConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XConstructorCall", type=JvmConstructor, multiplicity=Multiplicity(0, 1))
    }
)
arguments158: BinaryAssociation = BinaryAssociation(
    name="arguments158",
    ends={
        Property(name="XExpression160", type=model_xbase_XConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XConstructorCall159", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeArguments161: BinaryAssociation = BinaryAssociation(
    name="typeArguments161",
    ends={
        Property(name="JvmTypeReference163", type=model_xbase_XConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XConstructorCall162", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements164: BinaryAssociation = BinaryAssociation(
    name="elements164",
    ends={
        Property(name="XExpression165", type=model_xbase_XCollectionLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCollectionLiteral", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value166: BinaryAssociation = BinaryAssociation(
    name="value166",
    ends={
        Property(name="XExpression167", type=model_xbase_XKeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XKeyValuePair", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key168: BinaryAssociation = BinaryAssociation(
    name="key168",
    ends={
        Property(name="XExpression170", type=model_xbase_XKeyValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XKeyValuePair169", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredFormalParameters171: BinaryAssociation = BinaryAssociation(
    name="declaredFormalParameters171",
    ends={
        Property(name="JvmFormalParameter172", type=model_xbase_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XClosure", type=JvmFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression173: BinaryAssociation = BinaryAssociation(
    name="expression173",
    ends={
        Property(name="XExpression175", type=model_xbase_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XClosure174", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implicitParameter176: BinaryAssociation = BinaryAssociation(
    name="implicitParameter176",
    ends={
        Property(name="JvmFormalParameter178", type=model_xbase_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XClosure177", type=JvmFormalParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType179: BinaryAssociation = BinaryAssociation(
    name="returnType179",
    ends={
        Property(name="JvmTypeReference181", type=model_xbase_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XClosure180", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters182: BinaryAssociation = BinaryAssociation(
    name="typeParameters182",
    ends={
        Property(name="JvmTypeParameter184", type=model_xbase_XClosure, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XClosure183", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type185: BinaryAssociation = BinaryAssociation(
    name="type185",
    ends={
        Property(name="JvmTypeReference186", type=model_xbase_XCastedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCastedExpression", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target187: BinaryAssociation = BinaryAssociation(
    name="target187",
    ends={
        Property(name="XExpression189", type=model_xbase_XCastedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCastedExpression188", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftOperand190: BinaryAssociation = BinaryAssociation(
    name="leftOperand190",
    ends={
        Property(name="XExpression191", type=model_xbase_XBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XBinaryOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightOperand192: BinaryAssociation = BinaryAssociation(
    name="rightOperand192",
    ends={
        Property(name="XExpression194", type=model_xbase_XBinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XBinaryOperation193", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand195: BinaryAssociation = BinaryAssociation(
    name="operand195",
    ends={
        Property(name="XExpression196", type=model_xbase_XUnaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XUnaryOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition197: BinaryAssociation = BinaryAssociation(
    name="condition197",
    ends={
        Property(name="XExpression198", type=model_xbase_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForLoopExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loop199: BinaryAssociation = BinaryAssociation(
    name="loop199",
    ends={
        Property(name="XExpression201", type=model_xbase_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForLoopExpression200", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init202: BinaryAssociation = BinaryAssociation(
    name="init202",
    ends={
        Property(name="XExpression204", type=model_xbase_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForLoopExpression203", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eachExpression205: BinaryAssociation = BinaryAssociation(
    name="eachExpression205",
    ends={
        Property(name="XExpression207", type=model_xbase_XForLoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForLoopExpression206", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forExpression208: BinaryAssociation = BinaryAssociation(
    name="forExpression208",
    ends={
        Property(name="XExpression209", type=model_xbase_XForEachExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForEachExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eachExpression210: BinaryAssociation = BinaryAssociation(
    name="eachExpression210",
    ends={
        Property(name="XExpression212", type=model_xbase_XForEachExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForEachExpression211", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredParam213: BinaryAssociation = BinaryAssociation(
    name="declaredParam213",
    ends={
        Property(name="JvmFormalParameter215", type=model_xbase_XForEachExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XForEachExpression214", type=JvmFormalParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type223: BinaryAssociation = BinaryAssociation(
    name="type223",
    ends={
        Property(name="JvmTypeReference224", type=model_xbase_XInstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XInstanceOfExpression", type=JvmTypeReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body218: BinaryAssociation = BinaryAssociation(
    name="body218",
    ends={
        Property(name="XExpression220", type=model_xbase_XAbstractWhileExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractWhileExpression219", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type221: BinaryAssociation = BinaryAssociation(
    name="type221",
    ends={
        Property(name="JvmType222", type=model_xbase_XTypeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTypeLiteral", type=JvmType, multiplicity=Multiplicity(1, 1))
    }
)
predicate216: BinaryAssociation = BinaryAssociation(
    name="predicate216",
    ends={
        Property(name="XExpression217", type=model_xbase_XAbstractWhileExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAbstractWhileExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression230: BinaryAssociation = BinaryAssociation(
    name="expression230",
    ends={
        Property(name="XExpression231", type=model_xbase_XTryCatchFinallyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTryCatchFinallyExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression225: BinaryAssociation = BinaryAssociation(
    name="expression225",
    ends={
        Property(name="XExpression227", type=model_xbase_XInstanceOfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XInstanceOfExpression226", type=XExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression228: BinaryAssociation = BinaryAssociation(
    name="expression228",
    ends={
        Property(name="XExpression229", type=model_xbase_XThrowExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XThrowExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredParam239: BinaryAssociation = BinaryAssociation(
    name="declaredParam239",
    ends={
        Property(name="model_xbase_XCatchClause240", type=JvmFormalParameter, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="JvmFormalParameter241", type=model_xbase_XCatchClause, multiplicity=Multiplicity(1, 1))
    }
)
finallyExpression232: BinaryAssociation = BinaryAssociation(
    name="finallyExpression232",
    ends={
        Property(name="XExpression234", type=model_xbase_XTryCatchFinallyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTryCatchFinallyExpression233", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
catchClauses235: BinaryAssociation = BinaryAssociation(
    name="catchClauses235",
    ends={
        Property(name="XCatchClause", type=model_xbase_XTryCatchFinallyExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTryCatchFinallyExpression236", type=XCatchClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression237: BinaryAssociation = BinaryAssociation(
    name="expression237",
    ends={
        Property(name="XExpression238", type=model_xbase_XCatchClause, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XCatchClause", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignable242: BinaryAssociation = BinaryAssociation(
    name="assignable242",
    ends={
        Property(name="XExpression243", type=model_xbase_XAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAssignment", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value244: BinaryAssociation = BinaryAssociation(
    name="value244",
    ends={
        Property(name="XExpression246", type=model_xbase_XAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XAssignment245", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression247: BinaryAssociation = BinaryAssociation(
    name="expression247",
    ends={
        Property(name="XExpression248", type=model_xbase_XReturnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XReturnExpression", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand249: BinaryAssociation = BinaryAssociation(
    name="operand249",
    ends={
        Property(name="XExpression250", type=model_xbase_XPrefixOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XPrefixOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand251: BinaryAssociation = BinaryAssociation(
    name="operand251",
    ends={
        Property(name="XExpression252", type=model_xbase_XPostfixOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XPostfixOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trueOperand253: BinaryAssociation = BinaryAssociation(
    name="trueOperand253",
    ends={
        Property(name="XExpression254", type=model_xbase_XTernaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTernaryOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
falseOperand255: BinaryAssociation = BinaryAssociation(
    name="falseOperand255",
    ends={
        Property(name="XExpression257", type=model_xbase_XTernaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTernaryOperation256", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition258: BinaryAssociation = BinaryAssociation(
    name="condition258",
    ends={
        Property(name="XExpression260", type=model_xbase_XTernaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XTernaryOperation259", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression261: BinaryAssociation = BinaryAssociation(
    name="expression261",
    ends={
        Property(name="XExpression262", type=model_xbase_XIndexOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XIndexOperation", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index263: BinaryAssociation = BinaryAssociation(
    name="index263",
    ends={
        Property(name="XExpression265", type=model_xbase_XIndexOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XIndexOperation264", type=XExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body266: BinaryAssociation = BinaryAssociation(
    name="body266",
    ends={
        Property(name="XExpression267", type=model_xbase_XFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XFunctionDeclaration", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType268: BinaryAssociation = BinaryAssociation(
    name="returnType268",
    ends={
        Property(name="JvmTypeReference270", type=model_xbase_XFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XFunctionDeclaration269", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters271: BinaryAssociation = BinaryAssociation(
    name="parameters271",
    ends={
        Property(name="JvmFormalParameter273", type=model_xbase_XFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XFunctionDeclaration272", type=JvmFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties274: BinaryAssociation = BinaryAssociation(
    name="properties274",
    ends={
        Property(name="XObjectLiteralPart", type=model_xbase_XObjectLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XObjectLiteral", type=XObjectLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type275: BinaryAssociation = BinaryAssociation(
    name="type275",
    ends={
        Property(name="JvmType277", type=model_xbase_XObjectLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XObjectLiteral276", type=JvmType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value278: BinaryAssociation = BinaryAssociation(
    name="value278",
    ends={
        Property(name="XExpression279", type=model_xbase_XObjectLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XObjectLiteralPart", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements280: BinaryAssociation = BinaryAssociation(
    name="elements280",
    ends={
        Property(name="XExpression281", type=model_xbase_XArrayLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xbase_XArrayLiteral", type=XExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importSection282: BinaryAssociation = BinaryAssociation(
    name="importSection282",
    ends={
        Property(name="XImportSection1283", type=model_ss_XtendFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFile", type=XImportSection1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations299: BinaryAssociation = BinaryAssociation(
    name="annotations299",
    ends={
        Property(name="XAnnotation", type=model_ss_XtendAnnotationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendAnnotationTarget", type=XAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xtendTypes284: BinaryAssociation = BinaryAssociation(
    name="xtendTypes284",
    ends={
        Property(name="XtendTypeDeclaration", type=model_ss_XtendFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFile285", type=XtendTypeDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents286: BinaryAssociation = BinaryAssociation(
    name="contents286",
    ends={
        Property(name="ss_model_EObject", type=model_ss_XtendFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFile287", type=ss_model_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exportSection288: BinaryAssociation = BinaryAssociation(
    name="exportSection288",
    ends={
        Property(name="XExportSection290", type=model_ss_XtendFile, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFile289", type=XExportSection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends291: BinaryAssociation = BinaryAssociation(
    name="extends291",
    ends={
        Property(name="JvmTypeReference292", type=model_ss_XtendClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendClass", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implements293: BinaryAssociation = BinaryAssociation(
    name="implements293",
    ends={
        Property(name="JvmTypeReference295", type=model_ss_XtendClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendClass294", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters296: BinaryAssociation = BinaryAssociation(
    name="typeParameters296",
    ends={
        Property(name="JvmTypeParameter298", type=model_ss_XtendClass, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendClass297", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotationInfo300: BinaryAssociation = BinaryAssociation(
    name="annotationInfo300",
    ends={
        Property(name="XtendAnnotationTarget", type=model_ss_XtendMember, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendMember", type=XtendAnnotationTarget, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaringType301: BinaryAssociation = BinaryAssociation(
    name="declaringType301",
    ends={
        Property(name="ss", type=model_ss_XtendMember, multiplicity=Multiplicity(1, 1)),
        Property(name="XtendTypeDeclaration302", type=XtendTypeDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
expression303: BinaryAssociation = BinaryAssociation(
    name="expression303",
    ends={
        Property(name="XExpression304", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType305: BinaryAssociation = BinaryAssociation(
    name="returnType305",
    ends={
        Property(name="JvmTypeReference307", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction306", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters308: BinaryAssociation = BinaryAssociation(
    name="parameters308",
    ends={
        Property(name="XtendParameter", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction309", type=XtendParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createExtensionInfo310: BinaryAssociation = BinaryAssociation(
    name="createExtensionInfo310",
    ends={
        Property(name="CreateExtensionInfo", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction311", type=CreateExtensionInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeParameters312: BinaryAssociation = BinaryAssociation(
    name="typeParameters312",
    ends={
        Property(name="JvmTypeParameter314", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction313", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions315: BinaryAssociation = BinaryAssociation(
    name="exceptions315",
    ends={
        Property(name="JvmTypeReference317", type=model_ss_XtendFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendFunction316", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type318: BinaryAssociation = BinaryAssociation(
    name="type318",
    ends={
        Property(name="JvmTypeReference319", type=model_ss_XtendField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendField", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
separator325: BinaryAssociation = BinaryAssociation(
    name="separator325",
    ends={
        Property(name="XExpression326", type=model_ss_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringForLoop", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue320: BinaryAssociation = BinaryAssociation(
    name="initialValue320",
    ends={
        Property(name="XExpression322", type=model_ss_XtendField, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendField321", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterType323: BinaryAssociation = BinaryAssociation(
    name="parameterType323",
    ends={
        Property(name="JvmTypeReference324", type=model_ss_XtendParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendParameter", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
before327: BinaryAssociation = BinaryAssociation(
    name="before327",
    ends={
        Property(name="XExpression329", type=model_ss_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringForLoop328", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after330: BinaryAssociation = BinaryAssociation(
    name="after330",
    ends={
        Property(name="XExpression332", type=model_ss_RichStringForLoop, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringForLoop331", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if333: BinaryAssociation = BinaryAssociation(
    name="if333",
    ends={
        Property(name="XExpression334", type=model_ss_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringIf", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if343: BinaryAssociation = BinaryAssociation(
    name="if343",
    ends={
        Property(name="XExpression344", type=model_ss_RichStringElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringElseIf", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then335: BinaryAssociation = BinaryAssociation(
    name="then335",
    ends={
        Property(name="XExpression337", type=model_ss_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringIf336", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then345: BinaryAssociation = BinaryAssociation(
    name="then345",
    ends={
        Property(name="XExpression347", type=model_ss_RichStringElseIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringElseIf346", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseIfs338: BinaryAssociation = BinaryAssociation(
    name="elseIfs338",
    ends={
        Property(name="RichStringElseIf", type=model_ss_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringIf339", type=RichStringElseIf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
else340: BinaryAssociation = BinaryAssociation(
    name="else340",
    ends={
        Property(name="XExpression342", type=model_ss_RichStringIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_RichStringIf341", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression350: BinaryAssociation = BinaryAssociation(
    name="expression350",
    ends={
        Property(name="XExpression351", type=model_ss_XtendConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendConstructor", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters352: BinaryAssociation = BinaryAssociation(
    name="parameters352",
    ends={
        Property(name="XtendParameter354", type=model_ss_XtendConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendConstructor353", type=XtendParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
createExpression348: BinaryAssociation = BinaryAssociation(
    name="createExpression348",
    ends={
        Property(name="XExpression349", type=model_ss_CreateExtensionInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_CreateExtensionInfo", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
members361: BinaryAssociation = BinaryAssociation(
    name="members361",
    ends={
        Property(name="ss362", type=model_ss_XtendTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="XtendMember", type=XtendMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends363: BinaryAssociation = BinaryAssociation(
    name="extends363",
    ends={
        Property(name="JvmTypeReference364", type=model_ss_XtendInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendInterface", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters365: BinaryAssociation = BinaryAssociation(
    name="typeParameters365",
    ends={
        Property(name="JvmTypeParameter367", type=model_ss_XtendInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendInterface366", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters355: BinaryAssociation = BinaryAssociation(
    name="typeParameters355",
    ends={
        Property(name="JvmTypeParameter357", type=model_ss_XtendConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendConstructor356", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions358: BinaryAssociation = BinaryAssociation(
    name="exceptions358",
    ends={
        Property(name="JvmTypeReference360", type=model_ss_XtendConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendConstructor359", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType368: BinaryAssociation = BinaryAssociation(
    name="returnType368",
    ends={
        Property(name="JvmTypeReference369", type=model_ss_XtendDelegate, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendDelegate", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters370: BinaryAssociation = BinaryAssociation(
    name="parameters370",
    ends={
        Property(name="XtendParameter372", type=model_ss_XtendDelegate, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendDelegate371", type=XtendParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeParameters373: BinaryAssociation = BinaryAssociation(
    name="typeParameters373",
    ends={
        Property(name="JvmTypeParameter375", type=model_ss_XtendDelegate, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendDelegate374", type=JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type379: BinaryAssociation = BinaryAssociation(
    name="type379",
    ends={
        Property(name="model_ss_XtendEvent", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="JvmTypeReference380", type=model_ss_XtendEvent, multiplicity=Multiplicity(1, 1))
    }
)
initialValue381: BinaryAssociation = BinaryAssociation(
    name="initialValue381",
    ends={
        Property(name="XExpression383", type=model_ss_XtendEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendEvent382", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptions376: BinaryAssociation = BinaryAssociation(
    name="exceptions376",
    ends={
        Property(name="JvmTypeReference378", type=model_ss_XtendDelegate, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ss_XtendDelegate377", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementValuePairs384: BinaryAssociation = BinaryAssociation(
    name="elementValuePairs384",
    ends={
        Property(name="XAnnotationElementValuePair", type=model_xannotation_XAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xannotation_XAnnotation", type=XAnnotationElementValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value388: BinaryAssociation = BinaryAssociation(
    name="value388",
    ends={
        Property(name="XExpression390", type=model_xannotation_XAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xannotation_XAnnotation389", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value391: BinaryAssociation = BinaryAssociation(
    name="value391",
    ends={
        Property(name="XExpression392", type=model_xannotation_XAnnotationElementValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xannotation_XAnnotationElementValuePair", type=XExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotationType385: BinaryAssociation = BinaryAssociation(
    name="annotationType385",
    ends={
        Property(name="JvmType387", type=model_xannotation_XAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xannotation_XAnnotation386", type=JvmType, multiplicity=Multiplicity(0, 1))
    }
)
paramTypes396: BinaryAssociation = BinaryAssociation(
    name="paramTypes396",
    ends={
        Property(name="JvmTypeReference397", type=model_xtype_XFunctionTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XFunctionTypeRef", type=JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType398: BinaryAssociation = BinaryAssociation(
    name="returnType398",
    ends={
        Property(name="JvmTypeReference400", type=model_xtype_XFunctionTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XFunctionTypeRef399", type=JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type401: BinaryAssociation = BinaryAssociation(
    name="type401",
    ends={
        Property(name="JvmType403", type=model_xtype_XFunctionTypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XFunctionTypeRef402", type=JvmType, multiplicity=Multiplicity(0, 1))
    }
)
element393: BinaryAssociation = BinaryAssociation(
    name="element393",
    ends={
        Property(name="JvmOperation395", type=model_xannotation_XAnnotationElementValuePair, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xannotation_XAnnotationElementValuePair394", type=JvmOperation, multiplicity=Multiplicity(0, 1))
    }
)
importedType405: BinaryAssociation = BinaryAssociation(
    name="importedType405",
    ends={
        Property(name="JvmDeclaredType406", type=model_xtype_XImportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XImportDeclaration", type=JvmDeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
importDeclarations407: BinaryAssociation = BinaryAssociation(
    name="importDeclarations407",
    ends={
        Property(name="XImportDeclaration1", type=model_xtype_XImportSection1, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XImportSection1", type=XImportDeclaration1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importItems408: BinaryAssociation = BinaryAssociation(
    name="importItems408",
    ends={
        Property(name="XImportItem", type=model_xtype_XImportDeclaration1, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XImportDeclaration1", type=XImportItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importDeclarations404: BinaryAssociation = BinaryAssociation(
    name="importDeclarations404",
    ends={
        Property(name="XImportDeclaration", type=model_xtype_XImportSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XImportSection", type=XImportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exportItems412: BinaryAssociation = BinaryAssociation(
    name="exportItems412",
    ends={
        Property(name="XExportItem", type=model_xtype_XExportDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XExportDeclaration", type=XExportItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exportedId413: BinaryAssociation = BinaryAssociation(
    name="exportedId413",
    ends={
        Property(name="JvmIdentifiableElement414", type=model_xtype_XExportItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XExportItem", type=JvmIdentifiableElement, multiplicity=Multiplicity(0, 1))
    }
)
richString415: BinaryAssociation = BinaryAssociation(
    name="richString415",
    ends={
        Property(name="RichString", type=model_richstring_ProcessedRichString, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_ProcessedRichString", type=RichString, multiplicity=Multiplicity(0, 1))
    }
)
importedId409: BinaryAssociation = BinaryAssociation(
    name="importedId409",
    ends={
        Property(name="JvmIdentifiableElement410", type=model_xtype_XImportItem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XImportItem", type=JvmIdentifiableElement, multiplicity=Multiplicity(0, 1))
    }
)
exportDeclarations411: BinaryAssociation = BinaryAssociation(
    name="exportDeclarations411",
    ends={
        Property(name="XExportDeclaration", type=model_xtype_XExportSection, multiplicity=Multiplicity(1, 1)),
        Property(name="model_xtype_XExportSection", type=XExportDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parts417: BinaryAssociation = BinaryAssociation(
    name="parts417",
    ends={
        Property(name="richstring418", type=model_richstring_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="LinePart", type=LinePart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
richString419: BinaryAssociation = BinaryAssociation(
    name="richString419",
    ends={
        Property(name="richstring420", type=model_richstring_Line, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcessedRichString", type=ProcessedRichString, multiplicity=Multiplicity(0, 1))
    }
)
line421: BinaryAssociation = BinaryAssociation(
    name="line421",
    ends={
        Property(name="richstring423", type=model_richstring_LinePart, multiplicity=Multiplicity(1, 1)),
        Property(name="Line422", type=Line, multiplicity=Multiplicity(0, 1))
    }
)
literal424: BinaryAssociation = BinaryAssociation(
    name="literal424",
    ends={
        Property(name="RichStringLiteral", type=model_richstring_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_Literal", type=RichStringLiteral, multiplicity=Multiplicity(0, 1))
    }
)
end426: BinaryAssociation = BinaryAssociation(
    name="end426",
    ends={
        Property(name="richstring427", type=model_richstring_ForLoopStart, multiplicity=Multiplicity(1, 1)),
        Property(name="ForLoopEnd", type=ForLoopEnd, multiplicity=Multiplicity(0, 1))
    }
)
lines416: BinaryAssociation = BinaryAssociation(
    name="lines416",
    ends={
        Property(name="richstring", type=model_richstring_ProcessedRichString, multiplicity=Multiplicity(1, 1)),
        Property(name="Line", type=Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start428: BinaryAssociation = BinaryAssociation(
    name="start428",
    ends={
        Property(name="richstring429", type=model_richstring_ForLoopEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ForLoopStart", type=ForLoopStart, multiplicity=Multiplicity(0, 1))
    }
)
expression430: BinaryAssociation = BinaryAssociation(
    name="expression430",
    ends={
        Property(name="XExpression431", type=model_richstring_PrintedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_PrintedExpression", type=XExpression, multiplicity=Multiplicity(0, 1))
    }
)
loop425: BinaryAssociation = BinaryAssociation(
    name="loop425",
    ends={
        Property(name="RichStringForLoop", type=model_richstring_ForLoopStart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_ForLoopStart", type=RichStringForLoop, multiplicity=Multiplicity(0, 1))
    }
)
elseIfConditions435: BinaryAssociation = BinaryAssociation(
    name="elseIfConditions435",
    ends={
        Property(name="richstring436", type=model_richstring_IfConditionStart, multiplicity=Multiplicity(1, 1)),
        Property(name="ElseIfCondition", type=ElseIfCondition, multiplicity=Multiplicity(0, 9999))
    }
)
endIf437: BinaryAssociation = BinaryAssociation(
    name="endIf437",
    ends={
        Property(name="EndIf", type=model_richstring_IfConditionStart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_IfConditionStart438", type=EndIf, multiplicity=Multiplicity(0, 1))
    }
)
richStringElseIf439: BinaryAssociation = BinaryAssociation(
    name="richStringElseIf439",
    ends={
        Property(name="RichStringElseIf440", type=model_richstring_ElseIfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_ElseIfCondition", type=RichStringElseIf, multiplicity=Multiplicity(0, 1))
    }
)
ifConditionStart441: BinaryAssociation = BinaryAssociation(
    name="ifConditionStart441",
    ends={
        Property(name="richstring442", type=model_richstring_ElseIfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="IfConditionStart", type=IfConditionStart, multiplicity=Multiplicity(0, 1))
    }
)
ifConditionStart443: BinaryAssociation = BinaryAssociation(
    name="ifConditionStart443",
    ends={
        Property(name="richstring445", type=model_richstring_ElseStart, multiplicity=Multiplicity(1, 1)),
        Property(name="IfConditionStart444", type=IfConditionStart, multiplicity=Multiplicity(0, 1))
    }
)
richStringIf432: BinaryAssociation = BinaryAssociation(
    name="richStringIf432",
    ends={
        Property(name="RichStringIf", type=model_richstring_IfConditionStart, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_IfConditionStart", type=RichStringIf, multiplicity=Multiplicity(0, 1))
    }
)
elseStart433: BinaryAssociation = BinaryAssociation(
    name="elseStart433",
    ends={
        Property(name="richstring434", type=model_richstring_IfConditionStart, multiplicity=Multiplicity(1, 1)),
        Property(name="ElseStart", type=ElseStart, multiplicity=Multiplicity(0, 1))
    }
)
ifConditionStart446: BinaryAssociation = BinaryAssociation(
    name="ifConditionStart446",
    ends={
        Property(name="IfConditionStart447", type=model_richstring_EndIf, multiplicity=Multiplicity(1, 1)),
        Property(name="model_richstring_EndIf", type=IfConditionStart, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_model_types_JvmModule_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=model_types_JvmModule)
gen_model_types_JvmArrayType_JvmComponentType = Generalization(general=JvmComponentType, specific=model_types_JvmArrayType)
gen_model_types_JvmDeclaredType_types_JvmMember = Generalization(general=types_JvmMember, specific=model_types_JvmDeclaredType)
gen_model_types_JvmDeclaredType_types_JvmComponentType = Generalization(general=types_JvmComponentType, specific=model_types_JvmDeclaredType)
gen_model_types_JvmType_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=model_types_JvmType)
gen_model_types_JvmVoid_JvmType = Generalization(general=JvmType, specific=model_types_JvmVoid)
gen_model_types_JvmComponentType_JvmType = Generalization(general=JvmType, specific=model_types_JvmComponentType)
gen_model_types_JvmPrimitiveType_JvmComponentType = Generalization(general=JvmComponentType, specific=model_types_JvmPrimitiveType)
gen_model_types_JvmUpperBound_JvmTypeConstraint = Generalization(general=JvmTypeConstraint, specific=model_types_JvmUpperBound)
gen_model_types_JvmLowerBound_JvmTypeConstraint = Generalization(general=JvmTypeConstraint, specific=model_types_JvmLowerBound)
gen_model_types_JvmAnnotationType_JvmDeclaredType = Generalization(general=JvmDeclaredType, specific=model_types_JvmAnnotationType)
gen_model_types_JvmTypeParameter_types_JvmComponentType = Generalization(general=types_JvmComponentType, specific=model_types_JvmTypeParameter)
gen_model_types_JvmTypeParameter_types_JvmConstraintOwner = Generalization(general=types_JvmConstraintOwner, specific=model_types_JvmTypeParameter)
gen_model_types_JvmEnumerationType_JvmDeclaredType = Generalization(general=JvmDeclaredType, specific=model_types_JvmEnumerationType)
gen_model_types_JvmEnumerationLiteral_JvmField = Generalization(general=JvmField, specific=model_types_JvmEnumerationLiteral)
gen_model_types_JvmGenericType_types_JvmDeclaredType = Generalization(general=types_JvmDeclaredType, specific=model_types_JvmGenericType)
gen_model_types_JvmGenericType_types_JvmTypeParameterDeclarator = Generalization(general=types_JvmTypeParameterDeclarator, specific=model_types_JvmGenericType)
gen_model_types_JvmMultiTypeReference_JvmCompoundTypeReference = Generalization(general=JvmCompoundTypeReference, specific=model_types_JvmMultiTypeReference)
gen_model_types_JvmMember_JvmAnnotationTarget = Generalization(general=JvmAnnotationTarget, specific=model_types_JvmMember)
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
gen_model_types_JvmOperation_JvmExecutable = Generalization(general=JvmExecutable, specific=model_types_JvmOperation)
gen_model_types_JvmFormalParameter_JvmAnnotationTarget = Generalization(general=JvmAnnotationTarget, specific=model_types_JvmFormalParameter)
gen_model_types_JvmIntAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmIntAnnotationValue)
gen_model_types_JvmAnnotationTarget_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=model_types_JvmAnnotationTarget)
gen_model_types_JvmBooleanAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmBooleanAnnotationValue)
gen_model_types_JvmByteAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmByteAnnotationValue)
gen_model_types_JvmShortAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmShortAnnotationValue)
gen_model_types_JvmLongAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmLongAnnotationValue)
gen_model_types_JvmDoubleAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmDoubleAnnotationValue)
gen_model_types_JvmFloatAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmFloatAnnotationValue)
gen_model_types_JvmCharAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmCharAnnotationValue)
gen_model_types_JvmStringAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmStringAnnotationValue)
gen_model_types_JvmTypeAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmTypeAnnotationValue)
gen_model_types_JvmAnnotationAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmAnnotationAnnotationValue)
gen_model_types_JvmEnumAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmEnumAnnotationValue)
gen_model_types_JvmDelegateTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmDelegateTypeReference)
gen_model_types_JvmSpecializedTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmSpecializedTypeReference)
gen_model_types_JvmSynonymTypeReference_JvmCompoundTypeReference = Generalization(general=JvmCompoundTypeReference, specific=model_types_JvmSynonymTypeReference)
gen_model_types_JvmUnknownTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmUnknownTypeReference)
gen_model_types_JvmCompoundTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=model_types_JvmCompoundTypeReference)
gen_model_types_JvmCustomAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=model_types_JvmCustomAnnotationValue)
gen_model_xbase_XIfExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XIfExpression)
gen_model_xbase_XSwitchExpression_xbase_XExpression = Generalization(general=xbase_XExpression, specific=model_xbase_XSwitchExpression)
gen_model_xbase_XSwitchExpression_types_JvmIdentifiableElement = Generalization(general=types_JvmIdentifiableElement, specific=model_xbase_XSwitchExpression)
gen_model_xbase_XBlockExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XBlockExpression)
gen_model_xbase_XVariableDeclaration_xbase_XExpression = Generalization(general=xbase_XExpression, specific=model_xbase_XVariableDeclaration)
gen_model_xbase_XVariableDeclaration_types_JvmIdentifiableElement = Generalization(general=types_JvmIdentifiableElement, specific=model_xbase_XVariableDeclaration)
gen_model_xbase_XVariableDeclarationList_XExpression = Generalization(general=XExpression, specific=model_xbase_XVariableDeclarationList)
gen_model_xbase_XAbstractFeatureCall_XExpression = Generalization(general=XExpression, specific=model_xbase_XAbstractFeatureCall)
gen_model_xbase_XMemberFeatureCall_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XMemberFeatureCall)
gen_model_xbase_XMemberFeatureCall1_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XMemberFeatureCall1)
gen_model_xbase_XFeatureCall_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XFeatureCall)
gen_model_xbase_XConstructorCall_XExpression = Generalization(general=XExpression, specific=model_xbase_XConstructorCall)
gen_model_xbase_XBooleanLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XBooleanLiteral)
gen_model_xbase_XNullLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XNullLiteral)
gen_model_xbase_XNumberLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XNumberLiteral)
gen_model_xbase_XStringLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XStringLiteral)
gen_model_xbase_XCollectionLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XCollectionLiteral)
gen_model_xbase_XListLiteral_XCollectionLiteral = Generalization(general=XCollectionLiteral, specific=model_xbase_XListLiteral)
gen_model_xbase_XKeyValuePair_XExpression = Generalization(general=XExpression, specific=model_xbase_XKeyValuePair)
gen_model_xbase_XSetLiteral_XCollectionLiteral = Generalization(general=XCollectionLiteral, specific=model_xbase_XSetLiteral)
gen_model_xbase_XClosure_xbase_XExpression = Generalization(general=xbase_XExpression, specific=model_xbase_XClosure)
gen_model_xbase_XClosure_types_JvmIdentifiableElement = Generalization(general=types_JvmIdentifiableElement, specific=model_xbase_XClosure)
gen_model_xbase_XCastedExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XCastedExpression)
gen_model_xbase_XBinaryOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XBinaryOperation)
gen_model_xbase_XUnaryOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XUnaryOperation)
gen_model_xbase_XForLoopExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XForLoopExpression)
gen_model_xbase_XForEachExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XForEachExpression)
gen_model_xbase_XAbstractWhileExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XAbstractWhileExpression)
gen_model_xbase_XDoWhileExpression_XAbstractWhileExpression = Generalization(general=XAbstractWhileExpression, specific=model_xbase_XDoWhileExpression)
gen_model_xbase_XWhileExpression_XAbstractWhileExpression = Generalization(general=XAbstractWhileExpression, specific=model_xbase_XWhileExpression)
gen_model_xbase_XTypeLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XTypeLiteral)
gen_model_xbase_XInstanceOfExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XInstanceOfExpression)
gen_model_xbase_XThrowExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XThrowExpression)
gen_model_xbase_XTryCatchFinallyExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XTryCatchFinallyExpression)
gen_model_xbase_XAssignment_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XAssignment)
gen_model_xbase_XReturnExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XReturnExpression)
gen_model_xbase_XBreakExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XBreakExpression)
gen_model_xbase_XContinueExpression_XExpression = Generalization(general=XExpression, specific=model_xbase_XContinueExpression)
gen_model_xbase_XPrefixOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XPrefixOperation)
gen_model_xbase_XPostfixOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XPostfixOperation)
gen_model_xbase_XTernaryOperation_XExpression = Generalization(general=XExpression, specific=model_xbase_XTernaryOperation)
gen_model_xbase_XIndexOperation_XAbstractFeatureCall = Generalization(general=XAbstractFeatureCall, specific=model_xbase_XIndexOperation)
gen_model_xbase_XFunctionDeclaration_XExpression = Generalization(general=XExpression, specific=model_xbase_XFunctionDeclaration)
gen_model_xbase_XObjectLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XObjectLiteral)
gen_model_xbase_XArrayLiteral_XExpression = Generalization(general=XExpression, specific=model_xbase_XArrayLiteral)
gen_model_ss_XtendClass_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=model_ss_XtendClass)
gen_model_ss_XtendMember_XtendAnnotationTarget = Generalization(general=XtendAnnotationTarget, specific=model_ss_XtendMember)
gen_model_ss_XtendFunction_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendFunction)
gen_model_ss_XtendField_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendField)
gen_model_ss_XtendParameter_XtendAnnotationTarget = Generalization(general=XtendAnnotationTarget, specific=model_ss_XtendParameter)
gen_model_ss_RichString_XBlockExpression = Generalization(general=XBlockExpression, specific=model_ss_RichString)
gen_model_ss_RichStringLiteral_XStringLiteral = Generalization(general=XStringLiteral, specific=model_ss_RichStringLiteral)
gen_model_ss_RichStringForLoop_XForEachExpression = Generalization(general=XForEachExpression, specific=model_ss_RichStringForLoop)
gen_model_ss_RichStringIf_XExpression = Generalization(general=XExpression, specific=model_ss_RichStringIf)
gen_model_ss_XtendConstructor_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendConstructor)
gen_model_ss_XtendTypeDeclaration_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendTypeDeclaration)
gen_model_ss_XtendAnnotationType_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=model_ss_XtendAnnotationType)
gen_model_ss_XtendInterface_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=model_ss_XtendInterface)
gen_model_ss_XtendFormalParameter_JvmFormalParameter = Generalization(general=JvmFormalParameter, specific=model_ss_XtendFormalParameter)
gen_model_ss_XtendDelegate_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=model_ss_XtendDelegate)
gen_model_ss_XtendEnum_XtendTypeDeclaration = Generalization(general=XtendTypeDeclaration, specific=model_ss_XtendEnum)
gen_model_ss_XtendEnumLiteral_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendEnumLiteral)
gen_model_ss_XtendVariableDeclaration_XVariableDeclaration = Generalization(general=XVariableDeclaration, specific=model_ss_XtendVariableDeclaration)
gen_model_xannotation_XAnnotation_XExpression = Generalization(general=XExpression, specific=model_xannotation_XAnnotation)
gen_model_ss_XtendEvent_XtendMember = Generalization(general=XtendMember, specific=model_ss_XtendEvent)
gen_model_xtype_XComputedTypeReference_JvmSpecializedTypeReference = Generalization(general=JvmSpecializedTypeReference, specific=model_xtype_XComputedTypeReference)
gen_model_xtype_XFunctionTypeRef_JvmSpecializedTypeReference = Generalization(general=JvmSpecializedTypeReference, specific=model_xtype_XFunctionTypeRef)
gen_model_richstring_Literal_LinePart = Generalization(general=LinePart, specific=model_richstring_Literal)
gen_model_richstring_ForLoopEnd_LinePart = Generalization(general=LinePart, specific=model_richstring_ForLoopEnd)
gen_model_richstring_PrintedExpression_LinePart = Generalization(general=LinePart, specific=model_richstring_PrintedExpression)
gen_model_richstring_LineBreak_Literal = Generalization(general=Literal, specific=model_richstring_LineBreak)
gen_model_richstring_ForLoopStart_LinePart = Generalization(general=LinePart, specific=model_richstring_ForLoopStart)
gen_model_richstring_ElseIfCondition_LinePart = Generalization(general=LinePart, specific=model_richstring_ElseIfCondition)
gen_model_richstring_ElseStart_LinePart = Generalization(general=LinePart, specific=model_richstring_ElseStart)
gen_model_richstring_IfConditionStart_LinePart = Generalization(general=LinePart, specific=model_richstring_IfConditionStart)
gen_model_richstring_EndIf_LinePart = Generalization(general=LinePart, specific=model_richstring_EndIf)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_types_JvmModule, JvmIdentifiableElement, XImportSection1, types_model_EObject, XExportSection, model_types_JvmIdentifiableElement, model_types_JvmArrayType, model_types_JvmDeclaredType, types_JvmMember, types_JvmComponentType, JvmTypeReference, model_types_JvmNoModule, model_types_JvmType, model_types_JvmVoid, JvmType, model_types_JvmComponentType, JvmArrayType, model_types_JvmPrimitiveType, JvmComponentType, model_types_JvmConstraintOwner, JvmTypeConstraint, model_types_JvmTypeConstraint, JvmConstraintOwner, model_types_JvmUpperBound, model_types_JvmLowerBound, model_types_JvmAnnotationType, JvmDeclaredType, JvmMember, model_types_JvmTypeParameter, types_JvmConstraintOwner, JvmTypeParameterDeclarator, model_types_JvmTypeParameterDeclarator, JvmTypeParameter, model_types_JvmTypeReference, model_types_JvmEnumerationType, JvmEnumerationLiteral, model_types_JvmEnumerationLiteral, JvmField, model_types_JvmGenericType, types_JvmDeclaredType, types_JvmTypeParameterDeclarator, JvmParameterizedTypeReference, model_types_JvmMultiTypeReference, JvmCompoundTypeReference, model_types_JvmMember, JvmAnnotationTarget, model_types_JvmParameterizedTypeReference, model_types_JvmGenericArrayTypeReference, model_types_JvmWildcardTypeReference, types_JvmTypeReference, model_types_JvmAnyTypeReference, model_types_JvmFeature, model_types_JvmField, JvmFeature, model_types_JvmExecutable, types_JvmFeature, XExpression, model_types_JvmConstructor, JvmExecutable, JvmFormalParameter, JvmAnnotationValue, model_types_JvmOperation, model_types_JvmFormalParameter, model_types_JvmAnnotationReference, JvmAnnotationType, model_types_JvmAnnotationValue, JvmOperation, model_types_JvmIntAnnotationValue, model_types_JvmAnnotationTarget, JvmAnnotationReference, model_types_JvmBooleanAnnotationValue, model_types_JvmByteAnnotationValue, model_types_JvmShortAnnotationValue, model_types_JvmLongAnnotationValue, model_types_JvmDoubleAnnotationValue, model_types_JvmFloatAnnotationValue, model_types_JvmCharAnnotationValue, model_types_JvmStringAnnotationValue, model_types_JvmTypeAnnotationValue, model_types_JvmAnnotationAnnotationValue, model_types_JvmEnumAnnotationValue, model_types_JvmDelegateTypeReference, model_types_JvmSpecializedTypeReference, model_types_JvmSynonymTypeReference, model_types_JvmUnknownTypeReference, model_types_JvmCompoundTypeReference, model_types_JvmCustomAnnotationValue, model_xbase_XExpression, model_xbase_XIfExpression, model_xbase_XSwitchExpression, xbase_XExpression, types_JvmIdentifiableElement, XCasePart, model_xbase_XCasePart, model_xbase_XBlockExpression, model_xbase_XVariableDeclaration, model_xbase_XVariableDeclarationList, model_xbase_XAbstractFeatureCall, model_xbase_XMemberFeatureCall, XAbstractFeatureCall, model_xbase_XMemberFeatureCall1, model_xbase_XFeatureCall, model_xbase_XConstructorCall, JvmConstructor, model_xbase_XBooleanLiteral, model_xbase_XNullLiteral, model_xbase_XNumberLiteral, model_xbase_XStringLiteral, model_xbase_XCollectionLiteral, model_xbase_XListLiteral, XCollectionLiteral, model_xbase_XKeyValuePair, model_xbase_XSetLiteral, model_xbase_XClosure, model_xbase_XCastedExpression, model_xbase_XBinaryOperation, model_xbase_XUnaryOperation, model_xbase_XForLoopExpression, model_xbase_XForEachExpression, model_xbase_XAbstractWhileExpression, model_xbase_XDoWhileExpression, XAbstractWhileExpression, model_xbase_XWhileExpression, model_xbase_XTypeLiteral, model_xbase_XInstanceOfExpression, model_xbase_XThrowExpression, model_xbase_XTryCatchFinallyExpression, XCatchClause, model_xbase_XCatchClause, model_xbase_XAssignment, model_xbase_XReturnExpression, model_xbase_XBreakExpression, model_xbase_XContinueExpression, model_xbase_XPrefixOperation, model_xbase_XPostfixOperation, model_xbase_XTernaryOperation, model_xbase_XIndexOperation, model_xbase_XFunctionDeclaration, model_xbase_XObjectLiteralPart, model_xbase_XObjectLiteral, XObjectLiteralPart, XtendTypeDeclaration, model_xbase_XArrayLiteral, model_ss_XtendFile, ss_model_EObject, model_ss_XtendClass, model_ss_XtendAnnotationTarget, XAnnotation, model_ss_XtendMember, XtendAnnotationTarget, model_ss_XtendFunction, XtendMember, XtendParameter, CreateExtensionInfo, model_ss_XtendField, model_ss_XtendParameter, model_ss_RichString, XBlockExpression, model_ss_RichStringLiteral, XStringLiteral, model_ss_RichStringForLoop, XForEachExpression, model_ss_RichStringIf, model_ss_RichStringElseIf, RichStringElseIf, model_ss_XtendConstructor, model_ss_CreateExtensionInfo, model_ss_XtendTypeDeclaration, model_ss_XtendAnnotationType, model_ss_XtendInterface, model_ss_XtendFormalParameter, model_ss_XtendDelegate, model_ss_XtendEnum, model_ss_XtendEnumLiteral, model_ss_XtendVariableDeclaration, XVariableDeclaration, model_xannotation_XAnnotation, XAnnotationElementValuePair, model_ss_XtendEvent, model_xannotation_XAnnotationElementValuePair, model_xtype_XComputedTypeReference, model_xtype_XImportSection, model_xtype_XFunctionTypeRef, JvmSpecializedTypeReference, model_xtype_XImportSection1, XImportDeclaration1, model_xtype_XImportDeclaration1, XImportItem, model_xtype_XImportItem, XImportDeclaration, model_xtype_XImportDeclaration, model_xtype_XExportDeclaration, XExportItem, model_xtype_XExportItem, model_richstring_ProcessedRichString, RichString, model_xtype_XExportSection, XExportDeclaration, LinePart, ProcessedRichString, model_richstring_LinePart, model_richstring_Literal, RichStringLiteral, Line, model_richstring_ForLoopEnd, model_richstring_Line, ForLoopStart, model_richstring_PrintedExpression, model_richstring_LineBreak, Literal, model_richstring_ForLoopStart, RichStringForLoop, ForLoopEnd, EndIf, model_richstring_ElseIfCondition, IfConditionStart, model_richstring_ElseStart, model_richstring_IfConditionStart, RichStringIf, ElseStart, ElseIfCondition, model_richstring_EndIf, JvmVisibility},
    associations={importSection0, contents1, componentType11, exportSection3, importSection5, contents7, arrayType10, constraints20, typeReference22, owner24, superTypes13, members14, declarator16, typeParameters18, implements28, literals26, extends27, declaringType39, arguments31, type33, componentType35, type37, annotationInfo41, type42, get49, defaultValue44, set46, expression56, parameters52, exceptions53, defaultValue60, returnType58, expression62, function65, annotations73, annotation74, values75, value78, parameterType68, operation81, value82, defaultValue70, values85, values87, values89, delegate91, equivalent93, type95, references97, if100, then102, else105, switch108, cases110, default112, case115, then117, typeGuard120, expressions123, type125, right127, declarations130, feature132, typeArguments133, implicitReceiver136, implicitFirstArgument139, memberCallTarget142, memberCallArguments144, memberCallTarget147, memberCallArguments149, featureCallArguments152, value154, constructor157, arguments158, typeArguments161, elements164, value166, key168, declaredFormalParameters171, expression173, implicitParameter176, returnType179, typeParameters182, type185, target187, leftOperand190, rightOperand192, operand195, condition197, loop199, init202, eachExpression205, forExpression208, eachExpression210, declaredParam213, type223, body218, type221, predicate216, expression230, expression225, expression228, declaredParam239, finallyExpression232, catchClauses235, expression237, assignable242, value244, expression247, operand249, operand251, trueOperand253, falseOperand255, condition258, expression261, index263, body266, returnType268, parameters271, properties274, type275, value278, elements280, importSection282, annotations299, xtendTypes284, contents286, exportSection288, extends291, implements293, typeParameters296, annotationInfo300, declaringType301, expression303, returnType305, parameters308, createExtensionInfo310, typeParameters312, exceptions315, type318, separator325, initialValue320, parameterType323, before327, after330, if333, if343, then335, then345, elseIfs338, else340, expression350, parameters352, createExpression348, members361, extends363, typeParameters365, typeParameters355, exceptions358, returnType368, parameters370, typeParameters373, type379, initialValue381, exceptions376, elementValuePairs384, value388, value391, annotationType385, paramTypes396, returnType398, type401, element393, importedType405, importDeclarations407, importItems408, importDeclarations404, exportItems412, exportedId413, richString415, importedId409, exportDeclarations411, parts417, richString419, line421, literal424, end426, lines416, start428, expression430, loop425, elseIfConditions435, endIf437, richStringElseIf439, ifConditionStart441, ifConditionStart443, richStringIf432, elseStart433, ifConditionStart446},
    generalizations={gen_model_types_JvmModule_JvmIdentifiableElement, gen_model_types_JvmArrayType_JvmComponentType, gen_model_types_JvmDeclaredType_types_JvmMember, gen_model_types_JvmDeclaredType_types_JvmComponentType, gen_model_types_JvmType_JvmIdentifiableElement, gen_model_types_JvmVoid_JvmType, gen_model_types_JvmComponentType_JvmType, gen_model_types_JvmPrimitiveType_JvmComponentType, gen_model_types_JvmUpperBound_JvmTypeConstraint, gen_model_types_JvmLowerBound_JvmTypeConstraint, gen_model_types_JvmAnnotationType_JvmDeclaredType, gen_model_types_JvmTypeParameter_types_JvmComponentType, gen_model_types_JvmTypeParameter_types_JvmConstraintOwner, gen_model_types_JvmEnumerationType_JvmDeclaredType, gen_model_types_JvmEnumerationLiteral_JvmField, gen_model_types_JvmGenericType_types_JvmDeclaredType, gen_model_types_JvmGenericType_types_JvmTypeParameterDeclarator, gen_model_types_JvmMultiTypeReference_JvmCompoundTypeReference, gen_model_types_JvmMember_JvmAnnotationTarget, gen_model_types_JvmParameterizedTypeReference_JvmTypeReference, gen_model_types_JvmGenericArrayTypeReference_JvmTypeReference, gen_model_types_JvmWildcardTypeReference_types_JvmTypeReference, gen_model_types_JvmWildcardTypeReference_types_JvmConstraintOwner, gen_model_types_JvmAnyTypeReference_JvmTypeReference, gen_model_types_JvmFeature_JvmMember, gen_model_types_JvmField_JvmFeature, gen_model_types_JvmExecutable_types_JvmFeature, gen_model_types_JvmExecutable_types_JvmTypeParameterDeclarator, gen_model_types_JvmConstructor_JvmExecutable, gen_model_types_JvmOperation_JvmExecutable, gen_model_types_JvmFormalParameter_JvmAnnotationTarget, gen_model_types_JvmIntAnnotationValue_JvmAnnotationValue, gen_model_types_JvmAnnotationTarget_JvmIdentifiableElement, gen_model_types_JvmBooleanAnnotationValue_JvmAnnotationValue, gen_model_types_JvmByteAnnotationValue_JvmAnnotationValue, gen_model_types_JvmShortAnnotationValue_JvmAnnotationValue, gen_model_types_JvmLongAnnotationValue_JvmAnnotationValue, gen_model_types_JvmDoubleAnnotationValue_JvmAnnotationValue, gen_model_types_JvmFloatAnnotationValue_JvmAnnotationValue, gen_model_types_JvmCharAnnotationValue_JvmAnnotationValue, gen_model_types_JvmStringAnnotationValue_JvmAnnotationValue, gen_model_types_JvmTypeAnnotationValue_JvmAnnotationValue, gen_model_types_JvmAnnotationAnnotationValue_JvmAnnotationValue, gen_model_types_JvmEnumAnnotationValue_JvmAnnotationValue, gen_model_types_JvmDelegateTypeReference_JvmTypeReference, gen_model_types_JvmSpecializedTypeReference_JvmTypeReference, gen_model_types_JvmSynonymTypeReference_JvmCompoundTypeReference, gen_model_types_JvmUnknownTypeReference_JvmTypeReference, gen_model_types_JvmCompoundTypeReference_JvmTypeReference, gen_model_types_JvmCustomAnnotationValue_JvmAnnotationValue, gen_model_xbase_XIfExpression_XExpression, gen_model_xbase_XSwitchExpression_xbase_XExpression, gen_model_xbase_XSwitchExpression_types_JvmIdentifiableElement, gen_model_xbase_XBlockExpression_XExpression, gen_model_xbase_XVariableDeclaration_xbase_XExpression, gen_model_xbase_XVariableDeclaration_types_JvmIdentifiableElement, gen_model_xbase_XVariableDeclarationList_XExpression, gen_model_xbase_XAbstractFeatureCall_XExpression, gen_model_xbase_XMemberFeatureCall_XAbstractFeatureCall, gen_model_xbase_XMemberFeatureCall1_XAbstractFeatureCall, gen_model_xbase_XFeatureCall_XAbstractFeatureCall, gen_model_xbase_XConstructorCall_XExpression, gen_model_xbase_XBooleanLiteral_XExpression, gen_model_xbase_XNullLiteral_XExpression, gen_model_xbase_XNumberLiteral_XExpression, gen_model_xbase_XStringLiteral_XExpression, gen_model_xbase_XCollectionLiteral_XExpression, gen_model_xbase_XListLiteral_XCollectionLiteral, gen_model_xbase_XKeyValuePair_XExpression, gen_model_xbase_XSetLiteral_XCollectionLiteral, gen_model_xbase_XClosure_xbase_XExpression, gen_model_xbase_XClosure_types_JvmIdentifiableElement, gen_model_xbase_XCastedExpression_XExpression, gen_model_xbase_XBinaryOperation_XAbstractFeatureCall, gen_model_xbase_XUnaryOperation_XAbstractFeatureCall, gen_model_xbase_XForLoopExpression_XExpression, gen_model_xbase_XForEachExpression_XExpression, gen_model_xbase_XAbstractWhileExpression_XExpression, gen_model_xbase_XDoWhileExpression_XAbstractWhileExpression, gen_model_xbase_XWhileExpression_XAbstractWhileExpression, gen_model_xbase_XTypeLiteral_XExpression, gen_model_xbase_XInstanceOfExpression_XExpression, gen_model_xbase_XThrowExpression_XExpression, gen_model_xbase_XTryCatchFinallyExpression_XExpression, gen_model_xbase_XAssignment_XAbstractFeatureCall, gen_model_xbase_XReturnExpression_XExpression, gen_model_xbase_XBreakExpression_XExpression, gen_model_xbase_XContinueExpression_XExpression, gen_model_xbase_XPrefixOperation_XAbstractFeatureCall, gen_model_xbase_XPostfixOperation_XAbstractFeatureCall, gen_model_xbase_XTernaryOperation_XExpression, gen_model_xbase_XIndexOperation_XAbstractFeatureCall, gen_model_xbase_XFunctionDeclaration_XExpression, gen_model_xbase_XObjectLiteral_XExpression, gen_model_xbase_XArrayLiteral_XExpression, gen_model_ss_XtendClass_XtendTypeDeclaration, gen_model_ss_XtendMember_XtendAnnotationTarget, gen_model_ss_XtendFunction_XtendMember, gen_model_ss_XtendField_XtendMember, gen_model_ss_XtendParameter_XtendAnnotationTarget, gen_model_ss_RichString_XBlockExpression, gen_model_ss_RichStringLiteral_XStringLiteral, gen_model_ss_RichStringForLoop_XForEachExpression, gen_model_ss_RichStringIf_XExpression, gen_model_ss_XtendConstructor_XtendMember, gen_model_ss_XtendTypeDeclaration_XtendMember, gen_model_ss_XtendAnnotationType_XtendTypeDeclaration, gen_model_ss_XtendInterface_XtendTypeDeclaration, gen_model_ss_XtendFormalParameter_JvmFormalParameter, gen_model_ss_XtendDelegate_XtendTypeDeclaration, gen_model_ss_XtendEnum_XtendTypeDeclaration, gen_model_ss_XtendEnumLiteral_XtendMember, gen_model_ss_XtendVariableDeclaration_XVariableDeclaration, gen_model_xannotation_XAnnotation_XExpression, gen_model_ss_XtendEvent_XtendMember, gen_model_xtype_XComputedTypeReference_JvmSpecializedTypeReference, gen_model_xtype_XFunctionTypeRef_JvmSpecializedTypeReference, gen_model_richstring_Literal_LinePart, gen_model_richstring_ForLoopEnd_LinePart, gen_model_richstring_PrintedExpression_LinePart, gen_model_richstring_LineBreak_Literal, gen_model_richstring_ForLoopStart_LinePart, gen_model_richstring_ElseIfCondition_LinePart, gen_model_richstring_ElseStart_LinePart, gen_model_richstring_IfConditionStart_LinePart, gen_model_richstring_EndIf_LinePart},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)