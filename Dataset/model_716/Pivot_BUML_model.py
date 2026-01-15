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
AssociativityKind: Enumeration = Enumeration(
    name="AssociativityKind",
    literals={
            EnumerationLiteral(name="left"),
			EnumerationLiteral(name="right")
    }
)

CollectionKind: Enumeration = Enumeration(
    name="CollectionKind",
    literals={
            EnumerationLiteral(name="Collection"),
			EnumerationLiteral(name="Set"),
			EnumerationLiteral(name="OrderedSet"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Sequence")
    }
)

TransitionKind: Enumeration = Enumeration(
    name="TransitionKind",
    literals={
            EnumerationLiteral(name="internal"),
			EnumerationLiteral(name="local"),
			EnumerationLiteral(name="external")
    }
)

PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork")
    }
)

# Classes
pivot_AnyType = Class(name="pivot::AnyType")
Class_ = Class(name="Class")
pivot_AssociationClass = Class(name="pivot::AssociationClass")
pivot_Property = Class(name="pivot::Property")
pivot_AssociationClassCallExp = Class(name="pivot::AssociationClassCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
pivot_Annotation = Class(name="pivot::Annotation")
NamedElement = Class(name="NamedElement")
pivot_Element = Class(name="pivot::Element", is_abstract=True)
pivot_Detail = Class(name="pivot::Detail")
pivot_BooleanLiteralExp = Class(name="pivot::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
pivot_CallExp = Class(name="pivot::CallExp", is_abstract=True)
OCLExpression = Class(name="OCLExpression")
pivot_BagType = Class(name="pivot::BagType")
CollectionType = Class(name="CollectionType")
pivot_Behavior = Class(name="pivot::Behavior", is_abstract=True)
pivot_Transition = Class(name="pivot::Transition")
pivot_OCLExpression = Class(name="pivot::OCLExpression", is_abstract=True)
pivot_CallOperationAction = Class(name="pivot::CallOperationAction")
pivot_Operation = Class(name="pivot::Operation")
pivot_Class = Class(name="pivot::Class")
Type = Class(name="Type")
Namespace = Class(name="Namespace")
TemplateableElement = Class(name="TemplateableElement")
pivot_Constraint = Class(name="pivot::Constraint")
pivot_StereotypeExtender = Class(name="pivot::StereotypeExtender")
pivot_Package = Class(name="pivot::Package")
pivot_CollectionItem = Class(name="pivot::CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
pivot_CollectionLiteralExp = Class(name="pivot::CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
pivot_CollectionLiteralPart = Class(name="pivot::CollectionLiteralPart", is_abstract=True)
TypedElement = Class(name="TypedElement")
pivot_CollectionType = Class(name="pivot::CollectionType")
DataType = Class(name="DataType")
pivot_Type = Class(name="pivot::Type", is_abstract=True)
pivot_Comment = Class(name="pivot::Comment")
Element = Class(name="Element")
pivot_CollectionRange = Class(name="pivot::CollectionRange")
pivot_OrphanCompletePackage = Class(name="pivot::OrphanCompletePackage")
pivot_Model = Class(name="pivot::Model")
pivot_PrimitiveCompletePackage = Class(name="pivot::PrimitiveCompletePackage")
pivot_CompleteClass = Class(name="pivot::CompleteClass")
pivot_CompletePackage = Class(name="pivot::CompletePackage")
pivot_CompleteEnvironment = Class(name="pivot::CompleteEnvironment")
pivot_CompleteModel = Class(name="pivot::CompleteModel")
pivot_StandardLibrary = Class(name="pivot::StandardLibrary")
pivot_Namespace = Class(name="pivot::Namespace", is_abstract=True)
pivot_LanguageExpression = Class(name="pivot::LanguageExpression", is_abstract=True)
pivot_DataType = Class(name="pivot::DataType")
pivot_ConnectionPointReference = Class(name="pivot::ConnectionPointReference")
Vertex = Class(name="Vertex")
pivot_Pseudostate = Class(name="pivot::Pseudostate")
pivot_State = Class(name="pivot::State")
pivot_DynamicType = Class(name="pivot::DynamicType")
DynamicElement = Class(name="DynamicElement")
pivot_DynamicValueSpecification = Class(name="pivot::DynamicValueSpecification")
ValueSpecification = Class(name="ValueSpecification")
Visitable = Class(name="Visitable")
pivot_DynamicBehavior = Class(name="pivot::DynamicBehavior")
Behavior = Class(name="Behavior")
DynamicType = Class(name="DynamicType")
pivot_DynamicElement = Class(name="pivot::DynamicElement")
pivot_DynamicProperty = Class(name="pivot::DynamicProperty")
pivot_Stereotype = Class(name="pivot::Stereotype")
pivot_EnumLiteralExp = Class(name="pivot::EnumLiteralExp")
pivot_EnumerationLiteral = Class(name="pivot::EnumerationLiteral")
pivot_Enumeration = Class(name="pivot::Enumeration")
pivot_ElementExtension = Class(name="pivot::ElementExtension")
pivot_Variable = Class(name="pivot::Variable")
pivot_Feature = Class(name="pivot::Feature", is_abstract=True)
InstanceSpecification = Class(name="InstanceSpecification")
pivot_ExpressionInOCL = Class(name="pivot::ExpressionInOCL")
LanguageExpression = Class(name="LanguageExpression")
pivot_Import = Class(name="pivot::Import")
pivot_FeatureCallExp = Class(name="pivot::FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
pivot_FinalState = Class(name="pivot::FinalState")
State = Class(name="State")
pivot_IfExp = Class(name="pivot::IfExp")
pivot_IntegerLiteralExp = Class(name="pivot::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
pivot_InvalidLiteralExp = Class(name="pivot::InvalidLiteralExp")
pivot_InvalidType = Class(name="pivot::InvalidType")
pivot_IterateExp = Class(name="pivot::IterateExp")
LoopExp = Class(name="LoopExp")
ReferringElement = Class(name="ReferringElement")
pivot_InstanceSpecification = Class(name="pivot::InstanceSpecification")
pivot_Slot = Class(name="pivot::Slot")
pivot_Iteration = Class(name="pivot::Iteration")
Operation = Class(name="Operation")
pivot_Parameter = Class(name="pivot::Parameter")
pivot_IteratorExp = Class(name="pivot::IteratorExp")
pivot_LetExp = Class(name="pivot::LetExp")
pivot_LambdaType = Class(name="pivot::LambdaType")
pivot_MapLiteralExp = Class(name="pivot::MapLiteralExp")
pivot_MapLiteralPart = Class(name="pivot::MapLiteralPart")
pivot_Library = Class(name="pivot::Library")
Package = Class(name="Package")
pivot_Precedence = Class(name="pivot::Precedence")
pivot_LiteralExp = Class(name="pivot::LiteralExp", is_abstract=True)
pivot_LoopExp = Class(name="pivot::LoopExp", is_abstract=True)
pivot_SendSignalAction = Class(name="pivot::SendSignalAction")
pivot_MessageType = Class(name="pivot::MessageType")
pivot_MapType = Class(name="pivot::MapType")
pivot_MessageExp = Class(name="pivot::MessageExp")
pivot_MorePivotable = Class(name="pivot::MorePivotable", is_abstract=True)
pivot_Nameable = Class(name="pivot::Nameable", is_abstract=True)
pivot_NamedElement = Class(name="pivot::NamedElement", is_abstract=True)
Nameable = Class(name="Nameable")
pivot_NavigationCallExp = Class(name="pivot::NavigationCallExp", is_abstract=True)
FeatureCallExp = Class(name="FeatureCallExp")
pivot_Signal = Class(name="pivot::Signal")
pivot_NumericLiteralExp = Class(name="pivot::NumericLiteralExp", is_abstract=True)
Feature = Class(name="Feature")
pivot_NullLiteralExp = Class(name="pivot::NullLiteralExp")
pivot_OperationCallExp = Class(name="pivot::OperationCallExp")
pivot_OppositePropertyCallExp = Class(name="pivot::OppositePropertyCallExp")
pivot_OrderedSetType = Class(name="pivot::OrderedSetType")
pivot_ProfileApplication = Class(name="pivot::ProfileApplication")
VariableDeclaration = Class(name="VariableDeclaration")
pivot_Pivotable = Class(name="pivot::Pivotable", is_abstract=True)
CompletePackage = Class(name="CompletePackage")
pivot_PrimitiveLiteralExp = Class(name="pivot::PrimitiveLiteralExp", is_abstract=True)
pivot_PrimitiveType = Class(name="pivot::PrimitiveType")
pivot_Profile = Class(name="pivot::Profile")
pivot_PropertyCallExp = Class(name="pivot::PropertyCallExp")
pivot_StateMachine = Class(name="pivot::StateMachine")
pivot_RealLiteralExp = Class(name="pivot::RealLiteralExp")
pivot_ReferringElement = Class(name="pivot::ReferringElement", is_abstract=True)
pivot_SelfType = Class(name="pivot::SelfType")
pivot_SequenceType = Class(name="pivot::SequenceType")
pivot_SetType = Class(name="pivot::SetType")
pivot_Region = Class(name="pivot::Region")
pivot_Vertex = Class(name="pivot::Vertex", is_abstract=True)
pivot_ShadowExp = Class(name="pivot::ShadowExp")
pivot_ShadowPart = Class(name="pivot::ShadowPart")
pivot_ValueSpecification = Class(name="pivot::ValueSpecification", is_abstract=True)
pivot_Trigger = Class(name="pivot::Trigger")
pivot_StateExp = Class(name="pivot::StateExp")
pivot_StringLiteralExp = Class(name="pivot::StringLiteralExp")
pivot_TemplateBinding = Class(name="pivot::TemplateBinding")
pivot_TemplateParameterSubstitution = Class(name="pivot::TemplateParameterSubstitution")
pivot_TemplateableElement = Class(name="pivot::TemplateableElement", is_abstract=True)
pivot_TemplateSignature = Class(name="pivot::TemplateSignature")
pivot_TemplateParameter = Class(name="pivot::TemplateParameter")
pivot_WildcardType = Class(name="pivot::WildcardType")
pivot_TupleType = Class(name="pivot::TupleType")
pivot_TupleLiteralExp = Class(name="pivot::TupleLiteralExp")
pivot_TupleLiteralPart = Class(name="pivot::TupleLiteralPart")
pivot_TypeExp = Class(name="pivot::TypeExp")
pivot_TypedElement = Class(name="pivot::TypedElement", is_abstract=True)
pivot_UnspecifiedValueExp = Class(name="pivot::UnspecifiedValueExp")
pivot_UnlimitedNaturalLiteralExp = Class(name="pivot::UnlimitedNaturalLiteralExp")
pivot_VariableDeclaration = Class(name="pivot::VariableDeclaration", is_abstract=True)
pivot_VariableExp = Class(name="pivot::VariableExp")
pivot_Visitable = Class(name="pivot::Visitable", is_abstract=True)
pivot_VoidType = Class(name="pivot::VoidType")

# pivot_AnyType class attributes and methods

# Class class attributes and methods

# pivot_AssociationClass class attributes and methods

# pivot_Property class attributes and methods
pivot_Property_isID: Property = Property(name="isID", type=StringType)
pivot_Property_isImplicit: Property = Property(name="isImplicit", type=StringType)
pivot_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
pivot_Property_isResolveProxies: Property = Property(name="isResolveProxies", type=StringType)
pivot_Property_isTransient: Property = Property(name="isTransient", type=StringType)
pivot_Property_isUnsettable: Property = Property(name="isUnsettable", type=StringType)
pivot_Property_isVolatile: Property = Property(name="isVolatile", type=StringType)
pivot_Property_defaultValue: Property = Property(name="defaultValue", type=StringType)
pivot_Property_defaultValueString: Property = Property(name="defaultValueString", type=StringType)
pivot_Property_isComposite: Property = Property(name="isComposite", type=StringType)
pivot_Property_isDerived: Property = Property(name="isDerived", type=StringType)
pivot_Property_m_isAttribute: Method = Method(name="isAttribute", parameters={Parameter(name='p')}, type=StringType)
pivot_Property_m_validateCompatibleDefaultExpression: Method = Method(name="validateCompatibleDefaultExpression", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Property.attributes={pivot_Property_defaultValue, pivot_Property_isVolatile, pivot_Property_defaultValueString, pivot_Property_isID, pivot_Property_isDerived, pivot_Property_isImplicit, pivot_Property_isReadOnly, pivot_Property_isResolveProxies, pivot_Property_isUnsettable, pivot_Property_isTransient, pivot_Property_isComposite}
pivot_Property.methods={pivot_Property_m_validateCompatibleDefaultExpression, pivot_Property_m_isAttribute}

# pivot_AssociationClassCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# pivot_Annotation class attributes and methods

# NamedElement class attributes and methods

# pivot_Element class attributes and methods
pivot_Element_m_allOwnedElements: Method = Method(name="allOwnedElements", parameters={}, type=Element)
pivot_Element_m_getValue: Method = Method(name="getValue", parameters={Parameter(name='propertyName'), Parameter(name='stereotype')}, type=Element)
pivot_Element.methods={pivot_Element_m_allOwnedElements, pivot_Element_m_getValue}

# pivot_Detail class attributes and methods
pivot_Detail_values: Property = Property(name="values", type=StringType)
pivot_Detail.attributes={pivot_Detail_values}

# pivot_BooleanLiteralExp class attributes and methods
pivot_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
pivot_BooleanLiteralExp_m_validateTypeIsBoolean: Method = Method(name="validateTypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_BooleanLiteralExp.attributes={pivot_BooleanLiteralExp_booleanSymbol}
pivot_BooleanLiteralExp.methods={pivot_BooleanLiteralExp_m_validateTypeIsBoolean}

# PrimitiveLiteralExp class attributes and methods

# pivot_CallExp class attributes and methods
pivot_CallExp_isImplicit: Property = Property(name="isImplicit", type=StringType)
pivot_CallExp_isSafe: Property = Property(name="isSafe", type=StringType)
pivot_CallExp_m_validateTypeIsNotInvalid: Method = Method(name="validateTypeIsNotInvalid", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CallExp.attributes={pivot_CallExp_isImplicit, pivot_CallExp_isSafe}
pivot_CallExp.methods={pivot_CallExp_m_validateTypeIsNotInvalid}

# OCLExpression class attributes and methods

# pivot_BagType class attributes and methods

# CollectionType class attributes and methods

# pivot_Behavior class attributes and methods

# pivot_Transition class attributes and methods
pivot_Transition_kind: Property = Property(name="kind", type=StringType)
pivot_Transition.attributes={pivot_Transition_kind}

# pivot_OCLExpression class attributes and methods

# pivot_CallOperationAction class attributes and methods

# pivot_Operation class attributes and methods
pivot_Operation_isInvalidating: Property = Property(name="isInvalidating", type=StringType)
pivot_Operation_isTypeof: Property = Property(name="isTypeof", type=StringType)
pivot_Operation_isValidating: Property = Property(name="isValidating", type=StringType)
pivot_Operation_m_validateCompatibleReturn: Method = Method(name="validateCompatibleReturn", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Operation_m_validateLoadableImplementation: Method = Method(name="validateLoadableImplementation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Operation_m_validateUniquePostconditionName: Method = Method(name="validateUniquePostconditionName", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Operation_m_validateUniquePreconditionName: Method = Method(name="validateUniquePreconditionName", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Operation.attributes={pivot_Operation_isInvalidating, pivot_Operation_isValidating, pivot_Operation_isTypeof}
pivot_Operation.methods={pivot_Operation_m_validateLoadableImplementation, pivot_Operation_m_validateUniquePostconditionName, pivot_Operation_m_validateUniquePreconditionName, pivot_Operation_m_validateCompatibleReturn}

# pivot_Class class attributes and methods
pivot_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
pivot_Class_isActive: Property = Property(name="isActive", type=StringType)
pivot_Class_isInterface: Property = Property(name="isInterface", type=StringType)
pivot_Class_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
pivot_Class_m_validateUniqueInvariantName: Method = Method(name="validateUniqueInvariantName", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Class.attributes={pivot_Class_isAbstract, pivot_Class_isActive, pivot_Class_isInterface, pivot_Class_instanceClassName}
pivot_Class.methods={pivot_Class_m_validateUniqueInvariantName}

# Type class attributes and methods

# Namespace class attributes and methods

# TemplateableElement class attributes and methods

# pivot_Constraint class attributes and methods
pivot_Constraint_isCallable: Property = Property(name="isCallable", type=StringType)
pivot_Constraint_m_validateUniqueName: Method = Method(name="validateUniqueName", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Constraint.attributes={pivot_Constraint_isCallable}
pivot_Constraint.methods={pivot_Constraint_m_validateUniqueName}

# pivot_StereotypeExtender class attributes and methods
pivot_StereotypeExtender_isRequired: Property = Property(name="isRequired", type=StringType)
pivot_StereotypeExtender.attributes={pivot_StereotypeExtender_isRequired}

# pivot_Package class attributes and methods
pivot_Package_URI: Property = Property(name="URI", type=StringType)
pivot_Package_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
pivot_Package.attributes={pivot_Package_URI, pivot_Package_nsPrefix}

# pivot_CollectionItem class attributes and methods
pivot_CollectionItem_m_validateTypeIsItemType: Method = Method(name="validateTypeIsItemType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionItem.methods={pivot_CollectionItem_m_validateTypeIsItemType}

# CollectionLiteralPart class attributes and methods

# pivot_CollectionLiteralExp class attributes and methods
pivot_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
pivot_CollectionLiteralExp_m_validateCollectionKindIsConcrete: Method = Method(name="validateCollectionKindIsConcrete", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_CollectionLiteralExp_m_validateOrderedSetKindIsOrderedSet: Method = Method(name="validateOrderedSetKindIsOrderedSet", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_CollectionLiteralExp_m_validateBagKindIsBag: Method = Method(name="validateBagKindIsBag", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionLiteralExp_m_validateSequenceKindIsSequence: Method = Method(name="validateSequenceKindIsSequence", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_CollectionLiteralExp_m_validateSetKindIsSet: Method = Method(name="validateSetKindIsSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionLiteralExp.attributes={pivot_CollectionLiteralExp_kind}
pivot_CollectionLiteralExp.methods={pivot_CollectionLiteralExp_m_validateBagKindIsBag, pivot_CollectionLiteralExp_m_validateSequenceKindIsSequence, pivot_CollectionLiteralExp_m_validateOrderedSetKindIsOrderedSet, pivot_CollectionLiteralExp_m_validateSetKindIsSet, pivot_CollectionLiteralExp_m_validateCollectionKindIsConcrete}

# LiteralExp class attributes and methods

# pivot_CollectionLiteralPart class attributes and methods
pivot_CollectionLiteralPart_m_validateTypeIsNotInvalid: Method = Method(name="validateTypeIsNotInvalid", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionLiteralPart.methods={pivot_CollectionLiteralPart_m_validateTypeIsNotInvalid}

# TypedElement class attributes and methods

# pivot_CollectionType class attributes and methods
pivot_CollectionType_isNullFree: Property = Property(name="isNullFree", type=StringType)
pivot_CollectionType_lower: Property = Property(name="lower", type=StringType)
pivot_CollectionType_upper: Property = Property(name="upper", type=StringType)
pivot_CollectionType.attributes={pivot_CollectionType_isNullFree, pivot_CollectionType_lower, pivot_CollectionType_upper}

# DataType class attributes and methods

# pivot_Type class attributes and methods
pivot_Type_m_flattenedType: Method = Method(name="flattenedType", parameters={}, type=Type)
pivot_Type_m_isClass: Method = Method(name="isClass", parameters={}, type=Class_)
pivot_Type_m_isTemplateParameter: Method = Method(name="isTemplateParameter", parameters={}, type=StringType)
pivot_Type_m_specializeIn: Method = Method(name="specializeIn", parameters={Parameter(name='selfType'), Parameter(name='expr')}, type=Type)
pivot_Type.methods={pivot_Type_m_isTemplateParameter, pivot_Type_m_flattenedType, pivot_Type_m_specializeIn, pivot_Type_m_isClass}

# pivot_Comment class attributes and methods
pivot_Comment_body: Property = Property(name="body", type=StringType)
pivot_Comment.attributes={pivot_Comment_body}

# Element class attributes and methods

# pivot_CollectionRange class attributes and methods

# pivot_OrphanCompletePackage class attributes and methods

# pivot_Model class attributes and methods
pivot_Model_externalURI: Property = Property(name="externalURI", type=StringType)
pivot_Model.attributes={pivot_Model_externalURI}

# pivot_PrimitiveCompletePackage class attributes and methods

# pivot_CompleteClass class attributes and methods

# pivot_CompletePackage class attributes and methods
pivot_CompletePackage_m_getOwnedCompleteClass: Method = Method(name="getOwnedCompleteClass", parameters={Parameter(name='name')}, type=StringType)
pivot_CompletePackage.methods={pivot_CompletePackage_m_getOwnedCompleteClass}

# pivot_CompleteEnvironment class attributes and methods

# pivot_CompleteModel class attributes and methods
pivot_CompleteModel_m_getOwnedCompletePackage: Method = Method(name="getOwnedCompletePackage", parameters={Parameter(name='name')}, type=StringType)
pivot_CompleteModel.methods={pivot_CompleteModel_m_getOwnedCompletePackage}

# pivot_StandardLibrary class attributes and methods

# pivot_Namespace class attributes and methods

# pivot_LanguageExpression class attributes and methods
pivot_LanguageExpression_body: Property = Property(name="body", type=StringType)
pivot_LanguageExpression_language: Property = Property(name="language", type=StringType)
pivot_LanguageExpression.attributes={pivot_LanguageExpression_language, pivot_LanguageExpression_body}

# pivot_DataType class attributes and methods
pivot_DataType_isSerializable: Property = Property(name="isSerializable", type=StringType)
pivot_DataType.attributes={pivot_DataType_isSerializable}

# pivot_ConnectionPointReference class attributes and methods

# Vertex class attributes and methods

# pivot_Pseudostate class attributes and methods
pivot_Pseudostate_kind: Property = Property(name="kind", type=StringType)
pivot_Pseudostate.attributes={pivot_Pseudostate_kind}

# pivot_State class attributes and methods
pivot_State_isComposite: Property = Property(name="isComposite", type=StringType)
pivot_State_isOrthogonal: Property = Property(name="isOrthogonal", type=StringType)
pivot_State_isSimple: Property = Property(name="isSimple", type=StringType)
pivot_State_isSubmachineState: Property = Property(name="isSubmachineState", type=StringType)
pivot_State.attributes={pivot_State_isOrthogonal, pivot_State_isSimple, pivot_State_isComposite, pivot_State_isSubmachineState}

# pivot_DynamicType class attributes and methods

# DynamicElement class attributes and methods

# pivot_DynamicValueSpecification class attributes and methods

# ValueSpecification class attributes and methods

# Visitable class attributes and methods

# pivot_DynamicBehavior class attributes and methods

# Behavior class attributes and methods

# DynamicType class attributes and methods

# pivot_DynamicElement class attributes and methods

# pivot_DynamicProperty class attributes and methods
pivot_DynamicProperty_default: Property = Property(name="default", type=StringType)
pivot_DynamicProperty.attributes={pivot_DynamicProperty_default}

# pivot_Stereotype class attributes and methods

# pivot_EnumLiteralExp class attributes and methods
pivot_EnumLiteralExp_m_validateTypeIsEnumerationType: Method = Method(name="validateTypeIsEnumerationType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_EnumLiteralExp.methods={pivot_EnumLiteralExp_m_validateTypeIsEnumerationType}

# pivot_EnumerationLiteral class attributes and methods
pivot_EnumerationLiteral_value: Property = Property(name="value", type=StringType)
pivot_EnumerationLiteral.attributes={pivot_EnumerationLiteral_value}

# pivot_Enumeration class attributes and methods

# pivot_ElementExtension class attributes and methods
pivot_ElementExtension_isApplied: Property = Property(name="isApplied", type=StringType)
pivot_ElementExtension_isRequired: Property = Property(name="isRequired", type=StringType)
pivot_ElementExtension.attributes={pivot_ElementExtension_isApplied, pivot_ElementExtension_isRequired}

# pivot_Variable class attributes and methods
pivot_Variable_isImplicit: Property = Property(name="isImplicit", type=StringType)
pivot_Variable_m_validateCompatibleInitialiserType: Method = Method(name="validateCompatibleInitialiserType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Variable.attributes={pivot_Variable_isImplicit}
pivot_Variable.methods={pivot_Variable_m_validateCompatibleInitialiserType}

# pivot_Feature class attributes and methods
pivot_Feature_implementation: Property = Property(name="implementation", type=StringType)
pivot_Feature_implementationClass: Property = Property(name="implementationClass", type=StringType)
pivot_Feature_isStatic: Property = Property(name="isStatic", type=StringType)
pivot_Feature_m_validateTypeIsNotInvalid: Method = Method(name="validateTypeIsNotInvalid", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Feature.attributes={pivot_Feature_implementationClass, pivot_Feature_isStatic, pivot_Feature_implementation}
pivot_Feature.methods={pivot_Feature_m_validateTypeIsNotInvalid}

# InstanceSpecification class attributes and methods

# pivot_ExpressionInOCL class attributes and methods

# LanguageExpression class attributes and methods

# pivot_Import class attributes and methods

# pivot_FeatureCallExp class attributes and methods
pivot_FeatureCallExp_isPre: Property = Property(name="isPre", type=StringType)
pivot_FeatureCallExp.attributes={pivot_FeatureCallExp_isPre}

# CallExp class attributes and methods

# pivot_FinalState class attributes and methods

# State class attributes and methods

# pivot_IfExp class attributes and methods
pivot_IfExp_m_validateTypeIsNotInvalid: Method = Method(name="validateTypeIsNotInvalid", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IfExp_m_validateConditionTypeIsBoolean: Method = Method(name="validateConditionTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IfExp.methods={pivot_IfExp_m_validateConditionTypeIsBoolean, pivot_IfExp_m_validateTypeIsNotInvalid}

# pivot_IntegerLiteralExp class attributes and methods
pivot_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
pivot_IntegerLiteralExp_m_validateTypeIsInteger: Method = Method(name="validateTypeIsInteger", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IntegerLiteralExp.attributes={pivot_IntegerLiteralExp_integerSymbol}
pivot_IntegerLiteralExp.methods={pivot_IntegerLiteralExp_m_validateTypeIsInteger}

# NumericLiteralExp class attributes and methods

# pivot_InvalidLiteralExp class attributes and methods

# pivot_InvalidType class attributes and methods

# pivot_IterateExp class attributes and methods
pivot_IterateExp_m_validateBodyTypeConformsToResultType: Method = Method(name="validateBodyTypeConformsToResultType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IterateExp_m_validateSafeSourceCanBeNull: Method = Method(name="validateSafeSourceCanBeNull", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IterateExp_m_validateTypeIsResultType: Method = Method(name="validateTypeIsResultType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IterateExp_m_validateUnsafeSourceCanNotBeNull: Method = Method(name="validateUnsafeSourceCanNotBeNull", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IterateExp_m_validateOneInitializer: Method = Method(name="validateOneInitializer", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IterateExp_m_validateSafeIteratorIsRequired: Method = Method(name="validateSafeIteratorIsRequired", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IterateExp.methods={pivot_IterateExp_m_validateOneInitializer, pivot_IterateExp_m_validateUnsafeSourceCanNotBeNull, pivot_IterateExp_m_validateSafeIteratorIsRequired, pivot_IterateExp_m_validateTypeIsResultType, pivot_IterateExp_m_validateSafeSourceCanBeNull, pivot_IterateExp_m_validateBodyTypeConformsToResultType}

# LoopExp class attributes and methods

# ReferringElement class attributes and methods

# pivot_InstanceSpecification class attributes and methods

# pivot_Slot class attributes and methods

# pivot_Iteration class attributes and methods

# Operation class attributes and methods

# pivot_Parameter class attributes and methods
pivot_Parameter_isTypeof: Property = Property(name="isTypeof", type=StringType)
pivot_Parameter.attributes={pivot_Parameter_isTypeof}

# pivot_IteratorExp class attributes and methods
pivot_IteratorExp_m_validateAnyHasOneIterator: Method = Method(name="validateAnyHasOneIterator", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_validateAnyTypeIsSourceElementType: Method = Method(name="validateAnyTypeIsSourceElementType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_validateClosureBodyTypeIsConformanttoIteratorType: Method = Method(name="validateClosureBodyTypeIsConformanttoIteratorType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_validateClosureElementTypeIsSourceElementType: Method = Method(name="validateClosureElementTypeIsSourceElementType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_validateAnyBodyTypeIsBoolean: Method = Method(name="validateAnyBodyTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_validateClosureTypeIsUniqueCollection: Method = Method(name="validateClosureTypeIsUniqueCollection", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_validateCollectElementTypeIsFlattenedBodyType: Method = Method(name="validateCollectElementTypeIsFlattenedBodyType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_validateCollectTypeIsUnordered: Method = Method(name="validateCollectTypeIsUnordered", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_validateIteratorTypeIsSourceElementType: Method = Method(name="validateIteratorTypeIsSourceElementType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_validateClosureHasOneIterator: Method = Method(name="validateClosureHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_validateClosureSourceElementTypeIsBodyElementType: Method = Method(name="validateClosureSourceElementTypeIsBodyElementType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_validateSortedByElementTypeIsSourceElementType: Method = Method(name="validateSortedByElementTypeIsSourceElementType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_validateSortedByIsOrderedIfSourceIsOrdered: Method = Method(name="validateSortedByIsOrderedIfSourceIsOrdered", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_validateSortedByIteratorTypeIsComparable: Method = Method(name="validateSortedByIteratorTypeIsComparable", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_validateUnsafeSourceCanNotBeNull: Method = Method(name="validateUnsafeSourceCanNotBeNull", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_validateSafeIteratorIsRequired: Method = Method(name="validateSafeIteratorIsRequired", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_validateSafeSourceCanBeNull: Method = Method(name="validateSafeSourceCanBeNull", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp.methods={pivot_IteratorExp_m_validateCollectElementTypeIsFlattenedBodyType, pivot_IteratorExp_m_validateSafeSourceCanBeNull, pivot_IteratorExp_m_validateSortedByElementTypeIsSourceElementType, pivot_IteratorExp_m_validateSortedByIsOrderedIfSourceIsOrdered, pivot_IteratorExp_m_validateClosureTypeIsUniqueCollection, pivot_IteratorExp_m_validateSortedByIteratorTypeIsComparable, pivot_IteratorExp_m_validateIteratorTypeIsSourceElementType, pivot_IteratorExp_m_validateClosureElementTypeIsSourceElementType, pivot_IteratorExp_m_validateAnyTypeIsSourceElementType, pivot_IteratorExp_m_validateClosureBodyTypeIsConformanttoIteratorType, pivot_IteratorExp_m_validateClosureHasOneIterator, pivot_IteratorExp_m_validateSafeIteratorIsRequired, pivot_IteratorExp_m_validateUnsafeSourceCanNotBeNull, pivot_IteratorExp_m_validateAnyBodyTypeIsBoolean, pivot_IteratorExp_m_validateClosureSourceElementTypeIsBodyElementType, pivot_IteratorExp_m_validateCollectTypeIsUnordered, pivot_IteratorExp_m_validateAnyHasOneIterator}

# pivot_LetExp class attributes and methods
pivot_LetExp_m_validateTypeIsInType: Method = Method(name="validateTypeIsInType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_LetExp_m_validateTypeIsNotInvalid: Method = Method(name="validateTypeIsNotInvalid", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_LetExp.methods={pivot_LetExp_m_validateTypeIsInType, pivot_LetExp_m_validateTypeIsNotInvalid}

# pivot_LambdaType class attributes and methods

# pivot_MapLiteralExp class attributes and methods

# pivot_MapLiteralPart class attributes and methods

# pivot_Library class attributes and methods

# Package class attributes and methods

# pivot_Precedence class attributes and methods
pivot_Precedence_associativity: Property = Property(name="associativity", type=StringType)
pivot_Precedence_order: Property = Property(name="order", type=StringType)
pivot_Precedence.attributes={pivot_Precedence_associativity, pivot_Precedence_order}

# pivot_LiteralExp class attributes and methods

# pivot_LoopExp class attributes and methods
pivot_LoopExp_m_validateSourceIsCollection: Method = Method(name="validateSourceIsCollection", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_LoopExp_m_validateNoInitializers: Method = Method(name="validateNoInitializers", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_LoopExp.methods={pivot_LoopExp_m_validateSourceIsCollection, pivot_LoopExp_m_validateNoInitializers}

# pivot_SendSignalAction class attributes and methods

# pivot_MessageType class attributes and methods

# pivot_MapType class attributes and methods

# pivot_MessageExp class attributes and methods
pivot_MessageExp_m_validateOneCallOrOneSend: Method = Method(name="validateOneCallOrOneSend", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_MessageExp_m_validateTargetIsNotACollection: Method = Method(name="validateTargetIsNotACollection", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_MessageExp.methods={pivot_MessageExp_m_validateOneCallOrOneSend, pivot_MessageExp_m_validateTargetIsNotACollection}

# pivot_MorePivotable class attributes and methods

# pivot_Nameable class attributes and methods

# pivot_NamedElement class attributes and methods
pivot_NamedElement_name: Property = Property(name="name", type=StringType)
pivot_NamedElement.attributes={pivot_NamedElement_name}

# Nameable class attributes and methods

# pivot_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# pivot_Signal class attributes and methods

# pivot_NumericLiteralExp class attributes and methods

# Feature class attributes and methods

# pivot_NullLiteralExp class attributes and methods

# pivot_OperationCallExp class attributes and methods
pivot_OperationCallExp_isVirtual: Property = Property(name="isVirtual", type=StringType)
pivot_OperationCallExp_m_validateArgumentCount: Method = Method(name="validateArgumentCount", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_OperationCallExp_m_validateArgumentTypeIsConformant: Method = Method(name="validateArgumentTypeIsConformant", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_OperationCallExp_m_validateSafeSourceCanBeNull: Method = Method(name="validateSafeSourceCanBeNull", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_OperationCallExp.attributes={pivot_OperationCallExp_isVirtual}
pivot_OperationCallExp.methods={pivot_OperationCallExp_m_validateSafeSourceCanBeNull, pivot_OperationCallExp_m_validateArgumentTypeIsConformant, pivot_OperationCallExp_m_validateArgumentCount}

# pivot_OppositePropertyCallExp class attributes and methods

# pivot_OrderedSetType class attributes and methods

# pivot_ProfileApplication class attributes and methods
pivot_ProfileApplication_isStrict: Property = Property(name="isStrict", type=StringType)
pivot_ProfileApplication.attributes={pivot_ProfileApplication_isStrict}

# VariableDeclaration class attributes and methods

# pivot_Pivotable class attributes and methods

# CompletePackage class attributes and methods

# pivot_PrimitiveLiteralExp class attributes and methods

# pivot_PrimitiveType class attributes and methods

# pivot_Profile class attributes and methods

# pivot_PropertyCallExp class attributes and methods
pivot_PropertyCallExp_m_getSpecializedReferredPropertyOwningType: Method = Method(name="getSpecializedReferredPropertyOwningType", parameters={}, type=Class_)
pivot_PropertyCallExp_m_getSpecializedReferredPropertyType: Method = Method(name="getSpecializedReferredPropertyType", parameters={}, type=Class_)
pivot_PropertyCallExp_m_validateCompatibleResultType: Method = Method(name="validateCompatibleResultType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_PropertyCallExp_m_validateNonStaticSourceTypeIsConformant: Method = Method(name="validateNonStaticSourceTypeIsConformant", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_PropertyCallExp_m_validateSafeSourceCanBeNull: Method = Method(name="validateSafeSourceCanBeNull", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_PropertyCallExp_m_validateUnsafeSourceCanNotBeNull: Method = Method(name="validateUnsafeSourceCanNotBeNull", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_PropertyCallExp.methods={pivot_PropertyCallExp_m_getSpecializedReferredPropertyType, pivot_PropertyCallExp_m_validateUnsafeSourceCanNotBeNull, pivot_PropertyCallExp_m_validateSafeSourceCanBeNull, pivot_PropertyCallExp_m_getSpecializedReferredPropertyOwningType, pivot_PropertyCallExp_m_validateCompatibleResultType, pivot_PropertyCallExp_m_validateNonStaticSourceTypeIsConformant}

# pivot_StateMachine class attributes and methods

# pivot_RealLiteralExp class attributes and methods
pivot_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
pivot_RealLiteralExp.attributes={pivot_RealLiteralExp_realSymbol}

# pivot_ReferringElement class attributes and methods
pivot_ReferringElement_m_getReferredElement: Method = Method(name="getReferredElement", parameters={}, type=Element)
pivot_ReferringElement.methods={pivot_ReferringElement_m_getReferredElement}

# pivot_SelfType class attributes and methods
pivot_SelfType_m_specializeIn: Method = Method(name="specializeIn", parameters={Parameter(name='selfType'), Parameter(name='expr')}, type=Type)
pivot_SelfType.methods={pivot_SelfType_m_specializeIn}

# pivot_SequenceType class attributes and methods

# pivot_SetType class attributes and methods

# pivot_Region class attributes and methods

# pivot_Vertex class attributes and methods

# pivot_ShadowExp class attributes and methods
pivot_ShadowExp_value: Property = Property(name="value", type=StringType)
pivot_ShadowExp_m_validateTypeIsNotInvalid: Method = Method(name="validateTypeIsNotInvalid", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_ShadowExp.attributes={pivot_ShadowExp_value}
pivot_ShadowExp.methods={pivot_ShadowExp_m_validateTypeIsNotInvalid}

# pivot_ShadowPart class attributes and methods
pivot_ShadowPart_m_validateTypeIsNotInvalid: Method = Method(name="validateTypeIsNotInvalid", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_ShadowPart.methods={pivot_ShadowPart_m_validateTypeIsNotInvalid}

# pivot_ValueSpecification class attributes and methods
pivot_ValueSpecification_m_booleanValue: Method = Method(name="booleanValue", parameters={}, type=StringType)
pivot_ValueSpecification_m_integerValue: Method = Method(name="integerValue", parameters={}, type=StringType)
pivot_ValueSpecification_m_unlimitedValue: Method = Method(name="unlimitedValue", parameters={}, type=StringType)
pivot_ValueSpecification_m_isComputable: Method = Method(name="isComputable", parameters={}, type=StringType)
pivot_ValueSpecification_m_isNull: Method = Method(name="isNull", parameters={}, type=StringType)
pivot_ValueSpecification_m_stringValue: Method = Method(name="stringValue", parameters={}, type=StringType)
pivot_ValueSpecification.methods={pivot_ValueSpecification_m_isComputable, pivot_ValueSpecification_m_stringValue, pivot_ValueSpecification_m_isNull, pivot_ValueSpecification_m_integerValue, pivot_ValueSpecification_m_unlimitedValue, pivot_ValueSpecification_m_booleanValue}

# pivot_Trigger class attributes and methods

# pivot_StateExp class attributes and methods
pivot_StateExp_m_validateTypeIsNotInvalid: Method = Method(name="validateTypeIsNotInvalid", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_StateExp.methods={pivot_StateExp_m_validateTypeIsNotInvalid}

# pivot_StringLiteralExp class attributes and methods
pivot_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
pivot_StringLiteralExp.attributes={pivot_StringLiteralExp_stringSymbol}

# pivot_TemplateBinding class attributes and methods

# pivot_TemplateParameterSubstitution class attributes and methods

# pivot_TemplateableElement class attributes and methods

# pivot_TemplateSignature class attributes and methods

# pivot_TemplateParameter class attributes and methods

# pivot_WildcardType class attributes and methods

# pivot_TupleType class attributes and methods

# pivot_TupleLiteralExp class attributes and methods

# pivot_TupleLiteralPart class attributes and methods

# pivot_TypeExp class attributes and methods

# pivot_TypedElement class attributes and methods
pivot_TypedElement_isMany: Property = Property(name="isMany", type=StringType)
pivot_TypedElement_isRequired: Property = Property(name="isRequired", type=StringType)
pivot_TypedElement_m_CompatibleBody: Method = Method(name="CompatibleBody", parameters={Parameter(name='bodySpecification')}, type=StringType)
pivot_TypedElement.attributes={pivot_TypedElement_isMany, pivot_TypedElement_isRequired}
pivot_TypedElement.methods={pivot_TypedElement_m_CompatibleBody}

# pivot_UnspecifiedValueExp class attributes and methods

# pivot_UnlimitedNaturalLiteralExp class attributes and methods
pivot_UnlimitedNaturalLiteralExp_unlimitedNaturalSymbol: Property = Property(name="unlimitedNaturalSymbol", type=StringType)
pivot_UnlimitedNaturalLiteralExp.attributes={pivot_UnlimitedNaturalLiteralExp_unlimitedNaturalSymbol}

# pivot_VariableDeclaration class attributes and methods
pivot_VariableDeclaration_m_validateTypeIsNotInvalid: Method = Method(name="validateTypeIsNotInvalid", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_VariableDeclaration.methods={pivot_VariableDeclaration_m_validateTypeIsNotInvalid}

# pivot_VariableExp class attributes and methods
pivot_VariableExp_isImplicit: Property = Property(name="isImplicit", type=StringType)
pivot_VariableExp_m_validateTypeIsNotInvalid: Method = Method(name="validateTypeIsNotInvalid", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_VariableExp.attributes={pivot_VariableExp_isImplicit}
pivot_VariableExp.methods={pivot_VariableExp_m_validateTypeIsNotInvalid}

# pivot_Visitable class attributes and methods

# pivot_VoidType class attributes and methods

# Relationships
references3: BinaryAssociation = BinaryAssociation(
    name="references3",
    ends={
        Property(name="pivot_Element5", type=pivot_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Annotation4", type=pivot_Element, multiplicity=Multiplicity(0, 9999))
    }
)
unownedAttributes6: BinaryAssociation = BinaryAssociation(
    name="unownedAttributes6",
    ends={
        Property(name="Property", type=pivot_AssociationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="associationClass", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedContents0: BinaryAssociation = BinaryAssociation(
    name="ownedContents0",
    ends={
        Property(name="pivot_Element", type=pivot_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Annotation", type=pivot_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDetails1: BinaryAssociation = BinaryAssociation(
    name="ownedDetails1",
    ends={
        Property(name="pivot_Detail", type=pivot_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Annotation2", type=pivot_Detail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredAssociationClass7: BinaryAssociation = BinaryAssociation(
    name="referredAssociationClass7",
    ends={
        Property(name="pivot_AssociationClass", type=pivot_AssociationClassCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_AssociationClassCallExp", type=pivot_AssociationClass, multiplicity=Multiplicity(0, 1))
    }
)
owningTransition8: BinaryAssociation = BinaryAssociation(
    name="owningTransition8",
    ends={
        Property(name="Transition", type=pivot_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEffect", type=pivot_Transition, multiplicity=Multiplicity(0, 1))
    }
)
ownedSource9: BinaryAssociation = BinaryAssociation(
    name="ownedSource9",
    ends={
        Property(name="pivot_OCLExpression", type=pivot_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CallExp", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation10: BinaryAssociation = BinaryAssociation(
    name="operation10",
    ends={
        Property(name="pivot_Operation", type=pivot_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CallOperationAction", type=pivot_Operation, multiplicity=Multiplicity(1, 1))
    }
)
ownedBehaviors12: BinaryAssociation = BinaryAssociation(
    name="ownedBehaviors12",
    ends={
        Property(name="pivot_Behavior", type=pivot_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Class", type=pivot_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extenders11: BinaryAssociation = BinaryAssociation(
    name="extenders11",
    ends={
        Property(name="StereotypeExtender", type=pivot_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=pivot_StereotypeExtender, multiplicity=Multiplicity(0, 9999))
    }
)
owningPackage19: BinaryAssociation = BinaryAssociation(
    name="owningPackage19",
    ends={
        Property(name="Package", type=pivot_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedClasses", type=pivot_Package, multiplicity=Multiplicity(0, 1))
    }
)
superClasses21: BinaryAssociation = BinaryAssociation(
    name="superClasses21",
    ends={
        Property(name="pivot_Class22", type=pivot_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Class20", type=pivot_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedInvariants13: BinaryAssociation = BinaryAssociation(
    name="ownedInvariants13",
    ends={
        Property(name="pivot_Constraint", type=pivot_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Class14", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperations15: BinaryAssociation = BinaryAssociation(
    name="ownedOperations15",
    ends={
        Property(name="Operation", type=pivot_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owningClass", type=pivot_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProperties16: BinaryAssociation = BinaryAssociation(
    name="ownedProperties16",
    ends={
        Property(name="Property18", type=pivot_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owningClass17", type=pivot_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedItem23: BinaryAssociation = BinaryAssociation(
    name="ownedItem23",
    ends={
        Property(name="pivot_OCLExpression24", type=pivot_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionItem", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedParts25: BinaryAssociation = BinaryAssociation(
    name="ownedParts25",
    ends={
        Property(name="pivot_CollectionLiteralPart", type=pivot_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionLiteralExp", type=pivot_CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedFirst26: BinaryAssociation = BinaryAssociation(
    name="ownedFirst26",
    ends={
        Property(name="pivot_OCLExpression27", type=pivot_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionRange", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedLast28: BinaryAssociation = BinaryAssociation(
    name="ownedLast28",
    ends={
        Property(name="pivot_OCLExpression30", type=pivot_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionRange29", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType31: BinaryAssociation = BinaryAssociation(
    name="elementType31",
    ends={
        Property(name="pivot_Type", type=pivot_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionType", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
orphanCompletePackage41: BinaryAssociation = BinaryAssociation(
    name="orphanCompletePackage41",
    ends={
        Property(name="pivot_OrphanCompletePackage", type=pivot_CompleteModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CompleteModel", type=pivot_OrphanCompletePackage, multiplicity=Multiplicity(0, 1))
    }
)
ownedCompletePackages42: BinaryAssociation = BinaryAssociation(
    name="ownedCompletePackages42",
    ends={
        Property(name="CompletePackage43", type=pivot_CompleteModel, multiplicity=Multiplicity(1, 1)),
        Property(name="owningCompleteModel", type=pivot_CompletePackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningCompleteEnvironment44: BinaryAssociation = BinaryAssociation(
    name="owningCompleteEnvironment44",
    ends={
        Property(name="CompleteEnvironment", type=pivot_CompleteModel, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedCompleteModel", type=pivot_CompleteEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
partialModels45: BinaryAssociation = BinaryAssociation(
    name="partialModels45",
    ends={
        Property(name="pivot_Model", type=pivot_CompleteModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CompleteModel46", type=pivot_Model, multiplicity=Multiplicity(0, 9999))
    }
)
primitiveCompletePackage47: BinaryAssociation = BinaryAssociation(
    name="primitiveCompletePackage47",
    ends={
        Property(name="pivot_PrimitiveCompletePackage", type=pivot_CompleteModel, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CompleteModel48", type=pivot_PrimitiveCompletePackage, multiplicity=Multiplicity(0, 1))
    }
)
ownedCompleteClasses49: BinaryAssociation = BinaryAssociation(
    name="ownedCompleteClasses49",
    ends={
        Property(name="CompleteClass", type=pivot_CompletePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="owningCompletePackage", type=pivot_CompleteClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedCompletePackages51: BinaryAssociation = BinaryAssociation(
    name="ownedCompletePackages51",
    ends={
        Property(name="CompletePackage53", type=pivot_CompletePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="owningCompletePackage52", type=pivot_CompletePackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningCompleteModel54: BinaryAssociation = BinaryAssociation(
    name="owningCompleteModel54",
    ends={
        Property(name="CompleteModel55", type=pivot_CompletePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedCompletePackages", type=pivot_CompleteModel, multiplicity=Multiplicity(0, 1))
    }
)
owningCompletePackage57: BinaryAssociation = BinaryAssociation(
    name="owningCompletePackage57",
    ends={
        Property(name="CompletePackage59", type=pivot_CompletePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedCompletePackages58", type=pivot_CompletePackage, multiplicity=Multiplicity(0, 1))
    }
)
annotatedElements32: BinaryAssociation = BinaryAssociation(
    name="annotatedElements32",
    ends={
        Property(name="Element", type=pivot_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="annotatingComments", type=pivot_Element, multiplicity=Multiplicity(0, 9999))
    }
)
owningElement33: BinaryAssociation = BinaryAssociation(
    name="owningElement33",
    ends={
        Property(name="Element34", type=pivot_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedComments", type=pivot_Element, multiplicity=Multiplicity(0, 1))
    }
)
owningCompletePackage35: BinaryAssociation = BinaryAssociation(
    name="owningCompletePackage35",
    ends={
        Property(name="CompletePackage", type=pivot_CompleteClass, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedCompleteClasses", type=pivot_CompletePackage, multiplicity=Multiplicity(0, 1))
    }
)
partialClasses36: BinaryAssociation = BinaryAssociation(
    name="partialClasses36",
    ends={
        Property(name="pivot_Class37", type=pivot_CompleteClass, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CompleteClass", type=pivot_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedCompleteModel38: BinaryAssociation = BinaryAssociation(
    name="ownedCompleteModel38",
    ends={
        Property(name="CompleteModel", type=pivot_CompleteEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="owningCompleteEnvironment", type=pivot_CompleteModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedStandardLibrary39: BinaryAssociation = BinaryAssociation(
    name="ownedStandardLibrary39",
    ends={
        Property(name="StandardLibrary", type=pivot_CompleteEnvironment, multiplicity=Multiplicity(1, 1)),
        Property(name="owningCompleteEnvironment40", type=pivot_StandardLibrary, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constrainedElements66: BinaryAssociation = BinaryAssociation(
    name="constrainedElements66",
    ends={
        Property(name="pivot_Element68", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Constraint67", type=pivot_Element, multiplicity=Multiplicity(0, 9999))
    }
)
context69: BinaryAssociation = BinaryAssociation(
    name="context69",
    ends={
        Property(name="pivot_Namespace", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Constraint70", type=pivot_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
ownedSpecification71: BinaryAssociation = BinaryAssociation(
    name="ownedSpecification71",
    ends={
        Property(name="LanguageExpression", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="owningConstraint", type=pivot_LanguageExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
owningPostContext72: BinaryAssociation = BinaryAssociation(
    name="owningPostContext72",
    ends={
        Property(name="Operation73", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPostconditions", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
owningPreContext74: BinaryAssociation = BinaryAssociation(
    name="owningPreContext74",
    ends={
        Property(name="Operation75", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPreconditions", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
owningState76: BinaryAssociation = BinaryAssociation(
    name="owningState76",
    ends={
        Property(name="State77", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStateInvariant", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
owningTransition78: BinaryAssociation = BinaryAssociation(
    name="owningTransition78",
    ends={
        Property(name="Transition79", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedGuard", type=pivot_Transition, multiplicity=Multiplicity(0, 1))
    }
)
redefinedConstraints81: BinaryAssociation = BinaryAssociation(
    name="redefinedConstraints81",
    ends={
        Property(name="pivot_Constraint82", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Constraint80", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
partialPackages60: BinaryAssociation = BinaryAssociation(
    name="partialPackages60",
    ends={
        Property(name="pivot_Package", type=pivot_CompletePackage, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CompletePackage", type=pivot_Package, multiplicity=Multiplicity(0, 9999))
    }
)
behavioralClass83: BinaryAssociation = BinaryAssociation(
    name="behavioralClass83",
    ends={
        Property(name="pivot_Class84", type=pivot_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DataType", type=pivot_Class, multiplicity=Multiplicity(0, 1))
    }
)
entries61: BinaryAssociation = BinaryAssociation(
    name="entries61",
    ends={
        Property(name="pivot_Pseudostate", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConnectionPointReference", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
exits62: BinaryAssociation = BinaryAssociation(
    name="exits62",
    ends={
        Property(name="pivot_Pseudostate64", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConnectionPointReference63", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
owningState65: BinaryAssociation = BinaryAssociation(
    name="owningState65",
    ends={
        Property(name="State", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedConnections", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty87: BinaryAssociation = BinaryAssociation(
    name="referredProperty87",
    ends={
        Property(name="pivot_Property", type=pivot_DynamicProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DynamicProperty", type=pivot_Property, multiplicity=Multiplicity(1, 1))
    }
)
ownedDynamicProperties88: BinaryAssociation = BinaryAssociation(
    name="ownedDynamicProperties88",
    ends={
        Property(name="pivot_DynamicProperty89", type=pivot_DynamicType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DynamicType", type=pivot_DynamicProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metaType85: BinaryAssociation = BinaryAssociation(
    name="metaType85",
    ends={
        Property(name="pivot_Type86", type=pivot_DynamicElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DynamicElement", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
base97: BinaryAssociation = BinaryAssociation(
    name="base97",
    ends={
        Property(name="Element98", type=pivot_ElementExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedExtensions", type=pivot_Element, multiplicity=Multiplicity(1, 1))
    }
)
stereotype99: BinaryAssociation = BinaryAssociation(
    name="stereotype99",
    ends={
        Property(name="pivot_Stereotype", type=pivot_ElementExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ElementExtension", type=pivot_Stereotype, multiplicity=Multiplicity(1, 1))
    }
)
referredLiteral100: BinaryAssociation = BinaryAssociation(
    name="referredLiteral100",
    ends={
        Property(name="pivot_EnumerationLiteral", type=pivot_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_EnumLiteralExp", type=pivot_EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
annotatingComments90: BinaryAssociation = BinaryAssociation(
    name="annotatingComments90",
    ends={
        Property(name="Comment", type=pivot_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="annotatedElements", type=pivot_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAnnotations92: BinaryAssociation = BinaryAssociation(
    name="ownedAnnotations92",
    ends={
        Property(name="pivot_Element93", type=pivot_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Element91", type=pivot_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedComments94: BinaryAssociation = BinaryAssociation(
    name="ownedComments94",
    ends={
        Property(name="Comment95", type=pivot_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="owningElement", type=pivot_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedExtensions96: BinaryAssociation = BinaryAssociation(
    name="ownedExtensions96",
    ends={
        Property(name="ElementExtension", type=pivot_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="base", type=pivot_ElementExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedBody103: BinaryAssociation = BinaryAssociation(
    name="ownedBody103",
    ends={
        Property(name="pivot_OCLExpression104", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedContext105: BinaryAssociation = BinaryAssociation(
    name="ownedContext105",
    ends={
        Property(name="pivot_Variable", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL106", type=pivot_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameters107: BinaryAssociation = BinaryAssociation(
    name="ownedParameters107",
    ends={
        Property(name="pivot_Variable109", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL108", type=pivot_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedResult110: BinaryAssociation = BinaryAssociation(
    name="ownedResult110",
    ends={
        Property(name="pivot_Variable112", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL111", type=pivot_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedLiterals101: BinaryAssociation = BinaryAssociation(
    name="ownedLiterals101",
    ends={
        Property(name="EnumerationLiteral", type=pivot_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="owningEnumeration", type=pivot_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningEnumeration102: BinaryAssociation = BinaryAssociation(
    name="owningEnumeration102",
    ends={
        Property(name="Enumeration", type=pivot_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiterals", type=pivot_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
ownedCondition113: BinaryAssociation = BinaryAssociation(
    name="ownedCondition113",
    ends={
        Property(name="pivot_OCLExpression114", type=pivot_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IfExp", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedElse115: BinaryAssociation = BinaryAssociation(
    name="ownedElse115",
    ends={
        Property(name="pivot_OCLExpression117", type=pivot_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IfExp116", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedThen118: BinaryAssociation = BinaryAssociation(
    name="ownedThen118",
    ends={
        Property(name="pivot_OCLExpression120", type=pivot_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IfExp119", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
importedNamespace121: BinaryAssociation = BinaryAssociation(
    name="importedNamespace121",
    ends={
        Property(name="pivot_Namespace122", type=pivot_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Import", type=pivot_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
ownedSpecification126: BinaryAssociation = BinaryAssociation(
    name="ownedSpecification126",
    ends={
        Property(name="pivot_LanguageExpression", type=pivot_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_InstanceSpecification127", type=pivot_LanguageExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningPackage128: BinaryAssociation = BinaryAssociation(
    name="owningPackage128",
    ends={
        Property(name="Package129", type=pivot_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedInstances", type=pivot_Package, multiplicity=Multiplicity(0, 1))
    }
)
classes123: BinaryAssociation = BinaryAssociation(
    name="classes123",
    ends={
        Property(name="pivot_Class124", type=pivot_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_InstanceSpecification", type=pivot_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedSlots125: BinaryAssociation = BinaryAssociation(
    name="ownedSlots125",
    ends={
        Property(name="Slot", type=pivot_InstanceSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="owningInstance", type=pivot_Slot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedResult130: BinaryAssociation = BinaryAssociation(
    name="ownedResult130",
    ends={
        Property(name="pivot_Variable131", type=pivot_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IterateExp", type=pivot_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedAccumulators132: BinaryAssociation = BinaryAssociation(
    name="ownedAccumulators132",
    ends={
        Property(name="pivot_Parameter", type=pivot_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Iteration", type=pivot_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedIterators133: BinaryAssociation = BinaryAssociation(
    name="ownedIterators133",
    ends={
        Property(name="pivot_Parameter135", type=pivot_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Iteration134", type=pivot_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningConstraint144: BinaryAssociation = BinaryAssociation(
    name="owningConstraint144",
    ends={
        Property(name="Constraint", type=pivot_LanguageExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedSpecification", type=pivot_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
ownedIn145: BinaryAssociation = BinaryAssociation(
    name="ownedIn145",
    ends={
        Property(name="pivot_OCLExpression146", type=pivot_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LetExp", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextType136: BinaryAssociation = BinaryAssociation(
    name="contextType136",
    ends={
        Property(name="pivot_Type137", type=pivot_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LambdaType", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
parameterType138: BinaryAssociation = BinaryAssociation(
    name="parameterType138",
    ends={
        Property(name="pivot_Type140", type=pivot_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LambdaType139", type=pivot_Type, multiplicity=Multiplicity(0, 9999))
    }
)
resultType141: BinaryAssociation = BinaryAssociation(
    name="resultType141",
    ends={
        Property(name="pivot_Type143", type=pivot_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LambdaType142", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
ownedBody151: BinaryAssociation = BinaryAssociation(
    name="ownedBody151",
    ends={
        Property(name="pivot_OCLExpression152", type=pivot_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LoopExp", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedIterators153: BinaryAssociation = BinaryAssociation(
    name="ownedIterators153",
    ends={
        Property(name="pivot_Variable155", type=pivot_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LoopExp154", type=pivot_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredIteration156: BinaryAssociation = BinaryAssociation(
    name="referredIteration156",
    ends={
        Property(name="pivot_Iteration158", type=pivot_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LoopExp157", type=pivot_Iteration, multiplicity=Multiplicity(0, 1))
    }
)
ownedParts159: BinaryAssociation = BinaryAssociation(
    name="ownedParts159",
    ends={
        Property(name="pivot_MapLiteralPart", type=pivot_MapLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MapLiteralExp", type=pivot_MapLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedKey160: BinaryAssociation = BinaryAssociation(
    name="ownedKey160",
    ends={
        Property(name="pivot_OCLExpression162", type=pivot_MapLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MapLiteralPart161", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedVariable147: BinaryAssociation = BinaryAssociation(
    name="ownedVariable147",
    ends={
        Property(name="pivot_Variable149", type=pivot_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LetExp148", type=pivot_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedPrecedences150: BinaryAssociation = BinaryAssociation(
    name="ownedPrecedences150",
    ends={
        Property(name="pivot_Precedence", type=pivot_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Library", type=pivot_Precedence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedArguments171: BinaryAssociation = BinaryAssociation(
    name="ownedArguments171",
    ends={
        Property(name="pivot_OCLExpression172", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedCalledOperation173: BinaryAssociation = BinaryAssociation(
    name="ownedCalledOperation173",
    ends={
        Property(name="pivot_CallOperationAction175", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp174", type=pivot_CallOperationAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedSentSignal176: BinaryAssociation = BinaryAssociation(
    name="ownedSentSignal176",
    ends={
        Property(name="pivot_SendSignalAction", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp177", type=pivot_SendSignalAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedTarget178: BinaryAssociation = BinaryAssociation(
    name="ownedTarget178",
    ends={
        Property(name="pivot_OCLExpression180", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp179", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedValue163: BinaryAssociation = BinaryAssociation(
    name="ownedValue163",
    ends={
        Property(name="pivot_OCLExpression165", type=pivot_MapLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MapLiteralPart164", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType166: BinaryAssociation = BinaryAssociation(
    name="keyType166",
    ends={
        Property(name="pivot_Type167", type=pivot_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MapType", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
valueType168: BinaryAssociation = BinaryAssociation(
    name="valueType168",
    ends={
        Property(name="pivot_Type170", type=pivot_MapType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MapType169", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
ownedImports185: BinaryAssociation = BinaryAssociation(
    name="ownedImports185",
    ends={
        Property(name="pivot_Import187", type=pivot_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Model186", type=pivot_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPackages188: BinaryAssociation = BinaryAssociation(
    name="ownedPackages188",
    ends={
        Property(name="pivot_Package190", type=pivot_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Model189", type=pivot_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedConstraints191: BinaryAssociation = BinaryAssociation(
    name="ownedConstraints191",
    ends={
        Property(name="pivot_Constraint193", type=pivot_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Namespace192", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation181: BinaryAssociation = BinaryAssociation(
    name="referredOperation181",
    ends={
        Property(name="pivot_Operation182", type=pivot_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageType", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
referredSignal183: BinaryAssociation = BinaryAssociation(
    name="referredSignal183",
    ends={
        Property(name="pivot_Signal", type=pivot_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageType184", type=pivot_Signal, multiplicity=Multiplicity(0, 1))
    }
)
typeValue199: BinaryAssociation = BinaryAssociation(
    name="typeValue199",
    ends={
        Property(name="pivot_Type201", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_OCLExpression200", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
navigationSource194: BinaryAssociation = BinaryAssociation(
    name="navigationSource194",
    ends={
        Property(name="pivot_Property195", type=pivot_NavigationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_NavigationCallExp", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
qualifiers196: BinaryAssociation = BinaryAssociation(
    name="qualifiers196",
    ends={
        Property(name="pivot_OCLExpression198", type=pivot_NavigationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_NavigationCallExp197", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 9999))
    }
)
bodyExpression202: BinaryAssociation = BinaryAssociation(
    name="bodyExpression202",
    ends={
        Property(name="pivot_LanguageExpression204", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation203", type=pivot_LanguageExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedParameters205: BinaryAssociation = BinaryAssociation(
    name="ownedParameters205",
    ends={
        Property(name="Parameter", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningOperation", type=pivot_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPostconditions206: BinaryAssociation = BinaryAssociation(
    name="ownedPostconditions206",
    ends={
        Property(name="Constraint207", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningPostContext", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedPreconditions208: BinaryAssociation = BinaryAssociation(
    name="ownedPreconditions208",
    ends={
        Property(name="Constraint209", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="owningPreContext", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningClass210: BinaryAssociation = BinaryAssociation(
    name="owningClass210",
    ends={
        Property(name="Class", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperations", type=pivot_Class, multiplicity=Multiplicity(0, 1))
    }
)
precedence211: BinaryAssociation = BinaryAssociation(
    name="precedence211",
    ends={
        Property(name="pivot_Precedence213", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation212", type=pivot_Precedence, multiplicity=Multiplicity(0, 1))
    }
)
ownedArguments220: BinaryAssociation = BinaryAssociation(
    name="ownedArguments220",
    ends={
        Property(name="pivot_OCLExpression221", type=pivot_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_OperationCallExp", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation222: BinaryAssociation = BinaryAssociation(
    name="referredOperation222",
    ends={
        Property(name="pivot_Operation224", type=pivot_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_OperationCallExp223", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty225: BinaryAssociation = BinaryAssociation(
    name="referredProperty225",
    ends={
        Property(name="pivot_Property226", type=pivot_OppositePropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_OppositePropertyCallExp", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
raisedExceptions214: BinaryAssociation = BinaryAssociation(
    name="raisedExceptions214",
    ends={
        Property(name="pivot_Type216", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation215", type=pivot_Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedInstances232: BinaryAssociation = BinaryAssociation(
    name="ownedInstances232",
    ends={
        Property(name="InstanceSpecification", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="owningPackage233", type=pivot_InstanceSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedOperations218: BinaryAssociation = BinaryAssociation(
    name="redefinedOperations218",
    ends={
        Property(name="pivot_Operation219", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation217", type=pivot_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedPackages235: BinaryAssociation = BinaryAssociation(
    name="ownedPackages235",
    ends={
        Property(name="Package237", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="owningPackage236", type=pivot_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProfileApplications238: BinaryAssociation = BinaryAssociation(
    name="ownedProfileApplications238",
    ends={
        Property(name="ProfileApplication", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="owningPackage239", type=pivot_ProfileApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningPackage241: BinaryAssociation = BinaryAssociation(
    name="owningPackage241",
    ends={
        Property(name="Package242", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPackages", type=pivot_Package, multiplicity=Multiplicity(0, 1))
    }
)
owningOperation243: BinaryAssociation = BinaryAssociation(
    name="owningOperation243",
    ends={
        Property(name="Operation244", type=pivot_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameters", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
importedPackages228: BinaryAssociation = BinaryAssociation(
    name="importedPackages228",
    ends={
        Property(name="pivot_Package229", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Package227", type=pivot_Package, multiplicity=Multiplicity(0, 9999))
    }
)
ownedClasses230: BinaryAssociation = BinaryAssociation(
    name="ownedClasses230",
    ends={
        Property(name="Class231", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="owningPackage", type=pivot_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
appliedProfile249: BinaryAssociation = BinaryAssociation(
    name="appliedProfile249",
    ends={
        Property(name="Profile", type=pivot_ProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="profileApplications", type=pivot_Profile, multiplicity=Multiplicity(1, 1))
    }
)
owningPackage250: BinaryAssociation = BinaryAssociation(
    name="owningPackage250",
    ends={
        Property(name="Package251", type=pivot_ProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedProfileApplications", type=pivot_Package, multiplicity=Multiplicity(1, 1))
    }
)
coercions245: BinaryAssociation = BinaryAssociation(
    name="coercions245",
    ends={
        Property(name="pivot_Operation246", type=pivot_PrimitiveType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_PrimitiveType", type=pivot_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
profileApplications247: BinaryAssociation = BinaryAssociation(
    name="profileApplications247",
    ends={
        Property(name="ProfileApplication248", type=pivot_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProfile", type=pivot_ProfileApplication, multiplicity=Multiplicity(0, 9999))
    }
)
keys254: BinaryAssociation = BinaryAssociation(
    name="keys254",
    ends={
        Property(name="pivot_Property255", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property253", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
opposite257: BinaryAssociation = BinaryAssociation(
    name="opposite257",
    ends={
        Property(name="pivot_Property258", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property256", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
associationClass252: BinaryAssociation = BinaryAssociation(
    name="associationClass252",
    ends={
        Property(name="AssociationClass", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="unownedAttributes", type=pivot_AssociationClass, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty268: BinaryAssociation = BinaryAssociation(
    name="referredProperty268",
    ends={
        Property(name="pivot_Property269", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property267", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty271: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty271",
    ends={
        Property(name="pivot_Property272", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property270", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedExpression259: BinaryAssociation = BinaryAssociation(
    name="ownedExpression259",
    ends={
        Property(name="pivot_LanguageExpression261", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property260", type=pivot_LanguageExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningClass262: BinaryAssociation = BinaryAssociation(
    name="owningClass262",
    ends={
        Property(name="Class263", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedProperties", type=pivot_Class, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperties265: BinaryAssociation = BinaryAssociation(
    name="redefinedProperties265",
    ends={
        Property(name="pivot_Property266", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property264", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
referredProperty273: BinaryAssociation = BinaryAssociation(
    name="referredProperty273",
    ends={
        Property(name="pivot_Property274", type=pivot_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_PropertyCallExp", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
owningState275: BinaryAssociation = BinaryAssociation(
    name="owningState275",
    ends={
        Property(name="State276", type=pivot_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedConnectionPoints", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
owningStateMachine277: BinaryAssociation = BinaryAssociation(
    name="owningStateMachine277",
    ends={
        Property(name="StateMachine", type=pivot_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedConnectionPoints278", type=pivot_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
ownedTransitions282: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions282",
    ends={
        Property(name="Transition284", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="owningRegion283", type=pivot_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningState285: BinaryAssociation = BinaryAssociation(
    name="owningState285",
    ends={
        Property(name="State286", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRegions", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
owningStateMachine287: BinaryAssociation = BinaryAssociation(
    name="owningStateMachine287",
    ends={
        Property(name="StateMachine289", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedRegions288", type=pivot_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
signal290: BinaryAssociation = BinaryAssociation(
    name="signal290",
    ends={
        Property(name="pivot_Signal292", type=pivot_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_SendSignalAction291", type=pivot_Signal, multiplicity=Multiplicity(1, 1))
    }
)
extendedRegion280: BinaryAssociation = BinaryAssociation(
    name="extendedRegion280",
    ends={
        Property(name="pivot_Region", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Region279", type=pivot_Region, multiplicity=Multiplicity(0, 1))
    }
)
ownedSubvertexes281: BinaryAssociation = BinaryAssociation(
    name="ownedSubvertexes281",
    ends={
        Property(name="Vertex", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="owningRegion", type=pivot_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedInit294: BinaryAssociation = BinaryAssociation(
    name="ownedInit294",
    ends={
        Property(name="pivot_OCLExpression296", type=pivot_ShadowPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ShadowPart295", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredProperty297: BinaryAssociation = BinaryAssociation(
    name="referredProperty297",
    ends={
        Property(name="pivot_Property299", type=pivot_ShadowPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ShadowPart298", type=pivot_Property, multiplicity=Multiplicity(1, 1))
    }
)
definingProperty300: BinaryAssociation = BinaryAssociation(
    name="definingProperty300",
    ends={
        Property(name="pivot_Property301", type=pivot_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Slot", type=pivot_Property, multiplicity=Multiplicity(1, 1))
    }
)
ownedParts293: BinaryAssociation = BinaryAssociation(
    name="ownedParts293",
    ends={
        Property(name="pivot_ShadowPart", type=pivot_ShadowExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ShadowExp", type=pivot_ShadowPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedConnectionPoints308: BinaryAssociation = BinaryAssociation(
    name="ownedConnectionPoints308",
    ends={
        Property(name="Pseudostate", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="owningState", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedValues302: BinaryAssociation = BinaryAssociation(
    name="ownedValues302",
    ends={
        Property(name="pivot_ValueSpecification", type=pivot_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Slot303", type=pivot_ValueSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningInstance304: BinaryAssociation = BinaryAssociation(
    name="owningInstance304",
    ends={
        Property(name="InstanceSpecification305", type=pivot_Slot, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedSlots", type=pivot_InstanceSpecification, multiplicity=Multiplicity(1, 1))
    }
)
owningCompleteEnvironment306: BinaryAssociation = BinaryAssociation(
    name="owningCompleteEnvironment306",
    ends={
        Property(name="CompleteEnvironment307", type=pivot_StandardLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedStandardLibrary", type=pivot_CompleteEnvironment, multiplicity=Multiplicity(0, 1))
    }
)
ownedEntry315: BinaryAssociation = BinaryAssociation(
    name="ownedEntry315",
    ends={
        Property(name="pivot_Behavior317", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State316", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedExit318: BinaryAssociation = BinaryAssociation(
    name="ownedExit318",
    ends={
        Property(name="pivot_Behavior320", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State319", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedRegions321: BinaryAssociation = BinaryAssociation(
    name="ownedRegions321",
    ends={
        Property(name="Region", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="owningState322", type=pivot_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedStateInvariant323: BinaryAssociation = BinaryAssociation(
    name="ownedStateInvariant323",
    ends={
        Property(name="Constraint325", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="owningState324", type=pivot_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedState327: BinaryAssociation = BinaryAssociation(
    name="redefinedState327",
    ends={
        Property(name="pivot_State328", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State326", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
ownedConnections309: BinaryAssociation = BinaryAssociation(
    name="ownedConnections309",
    ends={
        Property(name="ConnectionPointReference", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="owningState310", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDeferrableTriggers311: BinaryAssociation = BinaryAssociation(
    name="ownedDeferrableTriggers311",
    ends={
        Property(name="Trigger", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="owningState312", type=pivot_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDoActivity313: BinaryAssociation = BinaryAssociation(
    name="ownedDoActivity313",
    ends={
        Property(name="pivot_Behavior314", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedStateMachines334: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachines334",
    ends={
        Property(name="pivot_StateMachine", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_StateMachine333", type=pivot_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
ownedConnectionPoints335: BinaryAssociation = BinaryAssociation(
    name="ownedConnectionPoints335",
    ends={
        Property(name="Pseudostate336", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStateMachine", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRegions337: BinaryAssociation = BinaryAssociation(
    name="ownedRegions337",
    ends={
        Property(name="Region339", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStateMachine338", type=pivot_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
submachineStates340: BinaryAssociation = BinaryAssociation(
    name="submachineStates340",
    ends={
        Property(name="State341", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="submachines", type=pivot_State, multiplicity=Multiplicity(0, 9999))
    }
)
submachines329: BinaryAssociation = BinaryAssociation(
    name="submachines329",
    ends={
        Property(name="StateMachine330", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="submachineStates", type=pivot_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
referredState331: BinaryAssociation = BinaryAssociation(
    name="referredState331",
    ends={
        Property(name="pivot_State332", type=pivot_StateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_StateExp", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
owningStereotype346: BinaryAssociation = BinaryAssociation(
    name="owningStereotype346",
    ends={
        Property(name="Stereotype", type=pivot_StereotypeExtender, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedExtenders", type=pivot_Stereotype, multiplicity=Multiplicity(1, 1))
    }
)
ownedSubstitutions347: BinaryAssociation = BinaryAssociation(
    name="ownedSubstitutions347",
    ends={
        Property(name="TemplateParameterSubstitution", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="owningBinding", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
owningElement348: BinaryAssociation = BinaryAssociation(
    name="owningElement348",
    ends={
        Property(name="TemplateableElement", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedBindings", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
templateSignature349: BinaryAssociation = BinaryAssociation(
    name="templateSignature349",
    ends={
        Property(name="pivot_TemplateSignature", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateBinding", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
ownedExtenders342: BinaryAssociation = BinaryAssociation(
    name="ownedExtenders342",
    ends={
        Property(name="StereotypeExtender343", type=pivot_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="owningStereotype", type=pivot_StereotypeExtender, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class344: BinaryAssociation = BinaryAssociation(
    name="class344",
    ends={
        Property(name="Class345", type=pivot_StereotypeExtender, multiplicity=Multiplicity(1, 1)),
        Property(name="extenders", type=pivot_Class, multiplicity=Multiplicity(1, 1))
    }
)
formal356: BinaryAssociation = BinaryAssociation(
    name="formal356",
    ends={
        Property(name="pivot_TemplateParameter358", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameterSubstitution357", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1))
    }
)
ownedWildcard359: BinaryAssociation = BinaryAssociation(
    name="ownedWildcard359",
    ends={
        Property(name="pivot_WildcardType", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameterSubstitution360", type=pivot_WildcardType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningBinding361: BinaryAssociation = BinaryAssociation(
    name="owningBinding361",
    ends={
        Property(name="TemplateBinding", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedSubstitutions", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameters362: BinaryAssociation = BinaryAssociation(
    name="ownedParameters362",
    ends={
        Property(name="TemplateParameter", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="owningSignature", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
owningElement363: BinaryAssociation = BinaryAssociation(
    name="owningElement363",
    ends={
        Property(name="TemplateableElement364", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedSignature", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
constrainingClasses350: BinaryAssociation = BinaryAssociation(
    name="constrainingClasses350",
    ends={
        Property(name="pivot_Class351", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameter", type=pivot_Class, multiplicity=Multiplicity(0, 9999))
    }
)
owningSignature352: BinaryAssociation = BinaryAssociation(
    name="owningSignature352",
    ends={
        Property(name="TemplateSignature", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameters353", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
actual354: BinaryAssociation = BinaryAssociation(
    name="actual354",
    ends={
        Property(name="pivot_Type355", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameterSubstitution", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
unspecializedElement372: BinaryAssociation = BinaryAssociation(
    name="unspecializedElement372",
    ends={
        Property(name="pivot_TemplateableElement", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateableElement371", type=pivot_TemplateableElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedEffect373: BinaryAssociation = BinaryAssociation(
    name="ownedEffect373",
    ends={
        Property(name="Behavior", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTransition", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedGuard374: BinaryAssociation = BinaryAssociation(
    name="ownedGuard374",
    ends={
        Property(name="Constraint376", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTransition375", type=pivot_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedBindings365: BinaryAssociation = BinaryAssociation(
    name="ownedBindings365",
    ends={
        Property(name="TemplateBinding367", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningElement366", type=pivot_TemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedSignature368: BinaryAssociation = BinaryAssociation(
    name="ownedSignature368",
    ends={
        Property(name="TemplateSignature370", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningElement369", type=pivot_TemplateSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningRegion380: BinaryAssociation = BinaryAssociation(
    name="owningRegion380",
    ends={
        Property(name="Region381", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTransitions", type=pivot_Region, multiplicity=Multiplicity(1, 1))
    }
)
source382: BinaryAssociation = BinaryAssociation(
    name="source382",
    ends={
        Property(name="Vertex383", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=pivot_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target384: BinaryAssociation = BinaryAssociation(
    name="target384",
    ends={
        Property(name="Vertex385", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=pivot_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
ownedTriggers377: BinaryAssociation = BinaryAssociation(
    name="ownedTriggers377",
    ends={
        Property(name="Trigger379", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTransition378", type=pivot_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedInit391: BinaryAssociation = BinaryAssociation(
    name="ownedInit391",
    ends={
        Property(name="pivot_OCLExpression393", type=pivot_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TupleLiteralPart392", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
owningState386: BinaryAssociation = BinaryAssociation(
    name="owningState386",
    ends={
        Property(name="State387", type=pivot_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedDeferrableTriggers", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
owningTransition388: BinaryAssociation = BinaryAssociation(
    name="owningTransition388",
    ends={
        Property(name="Transition389", type=pivot_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTriggers", type=pivot_Transition, multiplicity=Multiplicity(0, 1))
    }
)
ownedParts390: BinaryAssociation = BinaryAssociation(
    name="ownedParts390",
    ends={
        Property(name="pivot_TupleLiteralPart", type=pivot_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TupleLiteralExp", type=pivot_TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredType394: BinaryAssociation = BinaryAssociation(
    name="referredType394",
    ends={
        Property(name="pivot_Type395", type=pivot_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TypeExp", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
type396: BinaryAssociation = BinaryAssociation(
    name="type396",
    ends={
        Property(name="pivot_Type397", type=pivot_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TypedElement", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
representedParameter401: BinaryAssociation = BinaryAssociation(
    name="representedParameter401",
    ends={
        Property(name="pivot_Parameter403", type=pivot_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Variable402", type=pivot_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
ownedInit398: BinaryAssociation = BinaryAssociation(
    name="ownedInit398",
    ends={
        Property(name="pivot_OCLExpression400", type=pivot_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Variable399", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredVariable406: BinaryAssociation = BinaryAssociation(
    name="referredVariable406",
    ends={
        Property(name="pivot_VariableDeclaration407", type=pivot_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_VariableExp", type=pivot_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
typeValue404: BinaryAssociation = BinaryAssociation(
    name="typeValue404",
    ends={
        Property(name="pivot_Type405", type=pivot_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_VariableDeclaration", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
owningRegion412: BinaryAssociation = BinaryAssociation(
    name="owningRegion412",
    ends={
        Property(name="Region413", type=pivot_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedSubvertexes", type=pivot_Region, multiplicity=Multiplicity(0, 1))
    }
)
incomingTransitions408: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions408",
    ends={
        Property(name="Transition409", type=pivot_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=pivot_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingTransitions410: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions410",
    ends={
        Property(name="Transition411", type=pivot_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=pivot_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
lowerBound414: BinaryAssociation = BinaryAssociation(
    name="lowerBound414",
    ends={
        Property(name="pivot_Type416", type=pivot_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_WildcardType415", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
upperBound417: BinaryAssociation = BinaryAssociation(
    name="upperBound417",
    ends={
        Property(name="pivot_Type419", type=pivot_WildcardType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_WildcardType418", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pivot_AnyType_Class = Generalization(general=Class_, specific=pivot_AnyType)
gen_pivot_AssociationClass_Class = Generalization(general=Class_, specific=pivot_AssociationClass)
gen_pivot_AssociationClassCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=pivot_AssociationClassCallExp)
gen_pivot_Annotation_NamedElement = Generalization(general=NamedElement, specific=pivot_Annotation)
gen_pivot_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_BooleanLiteralExp)
gen_pivot_CallExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_CallExp)
gen_pivot_BagType_CollectionType = Generalization(general=CollectionType, specific=pivot_BagType)
gen_pivot_Behavior_Class = Generalization(general=Class_, specific=pivot_Behavior)
gen_pivot_CallOperationAction_NamedElement = Generalization(general=NamedElement, specific=pivot_CallOperationAction)
gen_pivot_Class_Type = Generalization(general=Type, specific=pivot_Class)
gen_pivot_Class_Namespace = Generalization(general=Namespace, specific=pivot_Class)
gen_pivot_Class_TemplateableElement = Generalization(general=TemplateableElement, specific=pivot_Class)
gen_pivot_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=pivot_CollectionItem)
gen_pivot_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_CollectionLiteralExp)
gen_pivot_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=pivot_CollectionLiteralPart)
gen_pivot_CollectionType_DataType = Generalization(general=DataType, specific=pivot_CollectionType)
gen_pivot_Comment_Element = Generalization(general=Element, specific=pivot_Comment)
gen_pivot_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=pivot_CollectionRange)
gen_pivot_CompleteModel_NamedElement = Generalization(general=NamedElement, specific=pivot_CompleteModel)
gen_pivot_CompletePackage_NamedElement = Generalization(general=NamedElement, specific=pivot_CompletePackage)
gen_pivot_CompleteClass_NamedElement = Generalization(general=NamedElement, specific=pivot_CompleteClass)
gen_pivot_CompleteEnvironment_Element = Generalization(general=Element, specific=pivot_CompleteEnvironment)
gen_pivot_DataType_Class = Generalization(general=Class_, specific=pivot_DataType)
gen_pivot_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=pivot_ConnectionPointReference)
gen_pivot_Constraint_NamedElement = Generalization(general=NamedElement, specific=pivot_Constraint)
gen_pivot_DynamicType_Class = Generalization(general=Class_, specific=pivot_DynamicType)
gen_pivot_DynamicType_DynamicElement = Generalization(general=DynamicElement, specific=pivot_DynamicType)
gen_pivot_DynamicValueSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=pivot_DynamicValueSpecification)
gen_pivot_Element_Visitable = Generalization(general=Visitable, specific=pivot_Element)
gen_pivot_Detail_NamedElement = Generalization(general=NamedElement, specific=pivot_Detail)
gen_pivot_DynamicBehavior_Behavior = Generalization(general=Behavior, specific=pivot_DynamicBehavior)
gen_pivot_DynamicBehavior_DynamicType = Generalization(general=DynamicType, specific=pivot_DynamicBehavior)
gen_pivot_DynamicElement_Element = Generalization(general=Element, specific=pivot_DynamicElement)
gen_pivot_DynamicProperty_Element = Generalization(general=Element, specific=pivot_DynamicProperty)
gen_pivot_ElementExtension_Class = Generalization(general=Class_, specific=pivot_ElementExtension)
gen_pivot_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_EnumLiteralExp)
gen_pivot_Enumeration_DataType = Generalization(general=DataType, specific=pivot_Enumeration)
gen_pivot_Feature_TypedElement = Generalization(general=TypedElement, specific=pivot_Feature)
gen_pivot_EnumerationLiteral_InstanceSpecification = Generalization(general=InstanceSpecification, specific=pivot_EnumerationLiteral)
gen_pivot_ExpressionInOCL_LanguageExpression = Generalization(general=LanguageExpression, specific=pivot_ExpressionInOCL)
gen_pivot_Import_NamedElement = Generalization(general=NamedElement, specific=pivot_Import)
gen_pivot_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=pivot_FeatureCallExp)
gen_pivot_FinalState_State = Generalization(general=State, specific=pivot_FinalState)
gen_pivot_IfExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_IfExp)
gen_pivot_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=pivot_IntegerLiteralExp)
gen_pivot_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_InvalidLiteralExp)
gen_pivot_InvalidType_Class = Generalization(general=Class_, specific=pivot_InvalidType)
gen_pivot_IterateExp_LoopExp = Generalization(general=LoopExp, specific=pivot_IterateExp)
gen_pivot_IterateExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_IterateExp)
gen_pivot_InstanceSpecification_NamedElement = Generalization(general=NamedElement, specific=pivot_InstanceSpecification)
gen_pivot_Iteration_Operation = Generalization(general=Operation, specific=pivot_Iteration)
gen_pivot_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=pivot_IteratorExp)
gen_pivot_IteratorExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_IteratorExp)
gen_pivot_LetExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_LetExp)
gen_pivot_LambdaType_DataType = Generalization(general=DataType, specific=pivot_LambdaType)
gen_pivot_LanguageExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=pivot_LanguageExpression)
gen_pivot_MapLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_MapLiteralExp)
gen_pivot_MapLiteralPart_Element = Generalization(general=Element, specific=pivot_MapLiteralPart)
gen_pivot_Library_Package = Generalization(general=Package, specific=pivot_Library)
gen_pivot_LiteralExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_LiteralExp)
gen_pivot_LoopExp_CallExp = Generalization(general=CallExp, specific=pivot_LoopExp)
gen_pivot_MapType_DataType = Generalization(general=DataType, specific=pivot_MapType)
gen_pivot_MessageExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_MessageExp)
gen_pivot_NamedElement_Element = Generalization(general=Element, specific=pivot_NamedElement)
gen_pivot_NamedElement_Nameable = Generalization(general=Nameable, specific=pivot_NamedElement)
gen_pivot_Namespace_NamedElement = Generalization(general=NamedElement, specific=pivot_Namespace)
gen_pivot_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=pivot_NavigationCallExp)
gen_pivot_MessageType_Class = Generalization(general=Class_, specific=pivot_MessageType)
gen_pivot_Model_Namespace = Generalization(general=Namespace, specific=pivot_Model)
gen_pivot_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_NumericLiteralExp)
gen_pivot_OCLExpression_TypedElement = Generalization(general=TypedElement, specific=pivot_OCLExpression)
gen_pivot_Operation_Feature = Generalization(general=Feature, specific=pivot_Operation)
gen_pivot_Operation_Namespace = Generalization(general=Namespace, specific=pivot_Operation)
gen_pivot_Operation_TemplateableElement = Generalization(general=TemplateableElement, specific=pivot_Operation)
gen_pivot_NullLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_NullLiteralExp)
gen_pivot_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=pivot_OperationCallExp)
gen_pivot_OperationCallExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_OperationCallExp)
gen_pivot_OppositePropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=pivot_OppositePropertyCallExp)
gen_pivot_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=pivot_OrderedSetType)
gen_pivot_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=pivot_Parameter)
gen_pivot_Precedence_NamedElement = Generalization(general=NamedElement, specific=pivot_Precedence)
gen_pivot_PrimitiveCompletePackage_CompletePackage = Generalization(general=CompletePackage, specific=pivot_PrimitiveCompletePackage)
gen_pivot_OrphanCompletePackage_CompletePackage = Generalization(general=CompletePackage, specific=pivot_OrphanCompletePackage)
gen_pivot_Package_Namespace = Generalization(general=Namespace, specific=pivot_Package)
gen_pivot_ProfileApplication_Element = Generalization(general=Element, specific=pivot_ProfileApplication)
gen_pivot_Property_Feature = Generalization(general=Feature, specific=pivot_Property)
gen_pivot_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_PrimitiveLiteralExp)
gen_pivot_PrimitiveType_DataType = Generalization(general=DataType, specific=pivot_PrimitiveType)
gen_pivot_Profile_Package = Generalization(general=Package, specific=pivot_Profile)
gen_pivot_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=pivot_PropertyCallExp)
gen_pivot_PropertyCallExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_PropertyCallExp)
gen_pivot_Pseudostate_Vertex = Generalization(general=Vertex, specific=pivot_Pseudostate)
gen_pivot_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=pivot_RealLiteralExp)
gen_pivot_SelfType_Class = Generalization(general=Class_, specific=pivot_SelfType)
gen_pivot_SendSignalAction_NamedElement = Generalization(general=NamedElement, specific=pivot_SendSignalAction)
gen_pivot_SequenceType_CollectionType = Generalization(general=CollectionType, specific=pivot_SequenceType)
gen_pivot_Region_Namespace = Generalization(general=Namespace, specific=pivot_Region)
gen_pivot_ShadowPart_TypedElement = Generalization(general=TypedElement, specific=pivot_ShadowPart)
gen_pivot_Signal_Class = Generalization(general=Class_, specific=pivot_Signal)
gen_pivot_Slot_Element = Generalization(general=Element, specific=pivot_Slot)
gen_pivot_SetType_CollectionType = Generalization(general=CollectionType, specific=pivot_SetType)
gen_pivot_ShadowExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_ShadowExp)
gen_pivot_State_Namespace = Generalization(general=Namespace, specific=pivot_State)
gen_pivot_State_Vertex = Generalization(general=Vertex, specific=pivot_State)
gen_pivot_StandardLibrary_Element = Generalization(general=Element, specific=pivot_StandardLibrary)
gen_pivot_StateMachine_Behavior = Generalization(general=Behavior, specific=pivot_StateMachine)
gen_pivot_Stereotype_Class = Generalization(general=Class_, specific=pivot_Stereotype)
gen_pivot_StateExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_StateExp)
gen_pivot_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_StringLiteralExp)
gen_pivot_TemplateBinding_Element = Generalization(general=Element, specific=pivot_TemplateBinding)
gen_pivot_TemplateParameter_Type = Generalization(general=Type, specific=pivot_TemplateParameter)
gen_pivot_StereotypeExtender_Element = Generalization(general=Element, specific=pivot_StereotypeExtender)
gen_pivot_TemplateSignature_Element = Generalization(general=Element, specific=pivot_TemplateSignature)
gen_pivot_TemplateParameterSubstitution_Element = Generalization(general=Element, specific=pivot_TemplateParameterSubstitution)
gen_pivot_Transition_Namespace = Generalization(general=Namespace, specific=pivot_Transition)
gen_pivot_TemplateableElement_Element = Generalization(general=Element, specific=pivot_TemplateableElement)
gen_pivot_Trigger_NamedElement = Generalization(general=NamedElement, specific=pivot_Trigger)
gen_pivot_TupleType_DataType = Generalization(general=DataType, specific=pivot_TupleType)
gen_pivot_Type_NamedElement = Generalization(general=NamedElement, specific=pivot_Type)
gen_pivot_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_TupleLiteralExp)
gen_pivot_TupleLiteralPart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=pivot_TupleLiteralPart)
gen_pivot_TypeExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_TypeExp)
gen_pivot_TypeExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_TypeExp)
gen_pivot_TypedElement_NamedElement = Generalization(general=NamedElement, specific=pivot_TypedElement)
gen_pivot_UnspecifiedValueExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_UnspecifiedValueExp)
gen_pivot_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=pivot_ValueSpecification)
gen_pivot_UnlimitedNaturalLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=pivot_UnlimitedNaturalLiteralExp)
gen_pivot_Variable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=pivot_Variable)
gen_pivot_VariableDeclaration_TypedElement = Generalization(general=TypedElement, specific=pivot_VariableDeclaration)
gen_pivot_Vertex_NamedElement = Generalization(general=NamedElement, specific=pivot_Vertex)
gen_pivot_VariableExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_VariableExp)
gen_pivot_VariableExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_VariableExp)
gen_pivot_VoidType_Class = Generalization(general=Class_, specific=pivot_VoidType)
gen_pivot_WildcardType_Class = Generalization(general=Class_, specific=pivot_WildcardType)

# Domain Model
domain_model = DomainModel(
    name="pivot",
    types={pivot_AnyType, Class_, pivot_AssociationClass, pivot_Property, pivot_AssociationClassCallExp, NavigationCallExp, pivot_Annotation, NamedElement, pivot_Element, pivot_Detail, pivot_BooleanLiteralExp, PrimitiveLiteralExp, pivot_CallExp, OCLExpression, pivot_BagType, CollectionType, pivot_Behavior, pivot_Transition, pivot_OCLExpression, pivot_CallOperationAction, pivot_Operation, pivot_Class, Type, Namespace, TemplateableElement, pivot_Constraint, pivot_StereotypeExtender, pivot_Package, pivot_CollectionItem, CollectionLiteralPart, pivot_CollectionLiteralExp, LiteralExp, pivot_CollectionLiteralPart, TypedElement, pivot_CollectionType, DataType, pivot_Type, pivot_Comment, Element, pivot_CollectionRange, pivot_OrphanCompletePackage, pivot_Model, pivot_PrimitiveCompletePackage, pivot_CompleteClass, pivot_CompletePackage, pivot_CompleteEnvironment, pivot_CompleteModel, pivot_StandardLibrary, pivot_Namespace, pivot_LanguageExpression, pivot_DataType, pivot_ConnectionPointReference, Vertex, pivot_Pseudostate, pivot_State, pivot_DynamicType, DynamicElement, pivot_DynamicValueSpecification, ValueSpecification, Visitable, pivot_DynamicBehavior, Behavior, DynamicType, pivot_DynamicElement, pivot_DynamicProperty, pivot_Stereotype, pivot_EnumLiteralExp, pivot_EnumerationLiteral, pivot_Enumeration, pivot_ElementExtension, pivot_Variable, pivot_Feature, InstanceSpecification, pivot_ExpressionInOCL, LanguageExpression, pivot_Import, pivot_FeatureCallExp, CallExp, pivot_FinalState, State, pivot_IfExp, pivot_IntegerLiteralExp, NumericLiteralExp, pivot_InvalidLiteralExp, pivot_InvalidType, pivot_IterateExp, LoopExp, ReferringElement, pivot_InstanceSpecification, pivot_Slot, pivot_Iteration, Operation, pivot_Parameter, pivot_IteratorExp, pivot_LetExp, pivot_LambdaType, pivot_MapLiteralExp, pivot_MapLiteralPart, pivot_Library, Package, pivot_Precedence, pivot_LiteralExp, pivot_LoopExp, pivot_SendSignalAction, pivot_MessageType, pivot_MapType, pivot_MessageExp, pivot_MorePivotable, pivot_Nameable, pivot_NamedElement, Nameable, pivot_NavigationCallExp, FeatureCallExp, pivot_Signal, pivot_NumericLiteralExp, Feature, pivot_NullLiteralExp, pivot_OperationCallExp, pivot_OppositePropertyCallExp, pivot_OrderedSetType, pivot_ProfileApplication, VariableDeclaration, pivot_Pivotable, CompletePackage, pivot_PrimitiveLiteralExp, pivot_PrimitiveType, pivot_Profile, pivot_PropertyCallExp, pivot_StateMachine, pivot_RealLiteralExp, pivot_ReferringElement, pivot_SelfType, pivot_SequenceType, pivot_SetType, pivot_Region, pivot_Vertex, pivot_ShadowExp, pivot_ShadowPart, pivot_ValueSpecification, pivot_Trigger, pivot_StateExp, pivot_StringLiteralExp, pivot_TemplateBinding, pivot_TemplateParameterSubstitution, pivot_TemplateableElement, pivot_TemplateSignature, pivot_TemplateParameter, pivot_WildcardType, pivot_TupleType, pivot_TupleLiteralExp, pivot_TupleLiteralPart, pivot_TypeExp, pivot_TypedElement, pivot_UnspecifiedValueExp, pivot_UnlimitedNaturalLiteralExp, pivot_VariableDeclaration, pivot_VariableExp, pivot_Visitable, pivot_VoidType, AssociativityKind, CollectionKind, TransitionKind, PseudostateKind},
    associations={references3, unownedAttributes6, ownedContents0, ownedDetails1, referredAssociationClass7, owningTransition8, ownedSource9, operation10, ownedBehaviors12, extenders11, owningPackage19, superClasses21, ownedInvariants13, ownedOperations15, ownedProperties16, ownedItem23, ownedParts25, ownedFirst26, ownedLast28, elementType31, orphanCompletePackage41, ownedCompletePackages42, owningCompleteEnvironment44, partialModels45, primitiveCompletePackage47, ownedCompleteClasses49, ownedCompletePackages51, owningCompleteModel54, owningCompletePackage57, annotatedElements32, owningElement33, owningCompletePackage35, partialClasses36, ownedCompleteModel38, ownedStandardLibrary39, constrainedElements66, context69, ownedSpecification71, owningPostContext72, owningPreContext74, owningState76, owningTransition78, redefinedConstraints81, partialPackages60, behavioralClass83, entries61, exits62, owningState65, referredProperty87, ownedDynamicProperties88, metaType85, base97, stereotype99, referredLiteral100, annotatingComments90, ownedAnnotations92, ownedComments94, ownedExtensions96, ownedBody103, ownedContext105, ownedParameters107, ownedResult110, ownedLiterals101, owningEnumeration102, ownedCondition113, ownedElse115, ownedThen118, importedNamespace121, ownedSpecification126, owningPackage128, classes123, ownedSlots125, ownedResult130, ownedAccumulators132, ownedIterators133, owningConstraint144, ownedIn145, contextType136, parameterType138, resultType141, ownedBody151, ownedIterators153, referredIteration156, ownedParts159, ownedKey160, ownedVariable147, ownedPrecedences150, ownedArguments171, ownedCalledOperation173, ownedSentSignal176, ownedTarget178, ownedValue163, keyType166, valueType168, ownedImports185, ownedPackages188, ownedConstraints191, referredOperation181, referredSignal183, typeValue199, navigationSource194, qualifiers196, bodyExpression202, ownedParameters205, ownedPostconditions206, ownedPreconditions208, owningClass210, precedence211, ownedArguments220, referredOperation222, referredProperty225, raisedExceptions214, ownedInstances232, redefinedOperations218, ownedPackages235, ownedProfileApplications238, owningPackage241, owningOperation243, importedPackages228, ownedClasses230, appliedProfile249, owningPackage250, coercions245, profileApplications247, keys254, opposite257, associationClass252, referredProperty268, subsettedProperty271, ownedExpression259, owningClass262, redefinedProperties265, referredProperty273, owningState275, owningStateMachine277, ownedTransitions282, owningState285, owningStateMachine287, signal290, extendedRegion280, ownedSubvertexes281, ownedInit294, referredProperty297, definingProperty300, ownedParts293, ownedConnectionPoints308, ownedValues302, owningInstance304, owningCompleteEnvironment306, ownedEntry315, ownedExit318, ownedRegions321, ownedStateInvariant323, redefinedState327, ownedConnections309, ownedDeferrableTriggers311, ownedDoActivity313, extendedStateMachines334, ownedConnectionPoints335, ownedRegions337, submachineStates340, submachines329, referredState331, owningStereotype346, ownedSubstitutions347, owningElement348, templateSignature349, ownedExtenders342, class344, formal356, ownedWildcard359, owningBinding361, ownedParameters362, owningElement363, constrainingClasses350, owningSignature352, actual354, unspecializedElement372, ownedEffect373, ownedGuard374, ownedBindings365, ownedSignature368, owningRegion380, source382, target384, ownedTriggers377, ownedInit391, owningState386, owningTransition388, ownedParts390, referredType394, type396, representedParameter401, ownedInit398, referredVariable406, typeValue404, owningRegion412, incomingTransitions408, outgoingTransitions410, lowerBound414, upperBound417},
    generalizations={gen_pivot_AnyType_Class, gen_pivot_AssociationClass_Class, gen_pivot_AssociationClassCallExp_NavigationCallExp, gen_pivot_Annotation_NamedElement, gen_pivot_BooleanLiteralExp_PrimitiveLiteralExp, gen_pivot_CallExp_OCLExpression, gen_pivot_BagType_CollectionType, gen_pivot_Behavior_Class, gen_pivot_CallOperationAction_NamedElement, gen_pivot_Class_Type, gen_pivot_Class_Namespace, gen_pivot_Class_TemplateableElement, gen_pivot_CollectionItem_CollectionLiteralPart, gen_pivot_CollectionLiteralExp_LiteralExp, gen_pivot_CollectionLiteralPart_TypedElement, gen_pivot_CollectionType_DataType, gen_pivot_Comment_Element, gen_pivot_CollectionRange_CollectionLiteralPart, gen_pivot_CompleteModel_NamedElement, gen_pivot_CompletePackage_NamedElement, gen_pivot_CompleteClass_NamedElement, gen_pivot_CompleteEnvironment_Element, gen_pivot_DataType_Class, gen_pivot_ConnectionPointReference_Vertex, gen_pivot_Constraint_NamedElement, gen_pivot_DynamicType_Class, gen_pivot_DynamicType_DynamicElement, gen_pivot_DynamicValueSpecification_ValueSpecification, gen_pivot_Element_Visitable, gen_pivot_Detail_NamedElement, gen_pivot_DynamicBehavior_Behavior, gen_pivot_DynamicBehavior_DynamicType, gen_pivot_DynamicElement_Element, gen_pivot_DynamicProperty_Element, gen_pivot_ElementExtension_Class, gen_pivot_EnumLiteralExp_LiteralExp, gen_pivot_Enumeration_DataType, gen_pivot_Feature_TypedElement, gen_pivot_EnumerationLiteral_InstanceSpecification, gen_pivot_ExpressionInOCL_LanguageExpression, gen_pivot_Import_NamedElement, gen_pivot_FeatureCallExp_CallExp, gen_pivot_FinalState_State, gen_pivot_IfExp_OCLExpression, gen_pivot_IntegerLiteralExp_NumericLiteralExp, gen_pivot_InvalidLiteralExp_LiteralExp, gen_pivot_InvalidType_Class, gen_pivot_IterateExp_LoopExp, gen_pivot_IterateExp_ReferringElement, gen_pivot_InstanceSpecification_NamedElement, gen_pivot_Iteration_Operation, gen_pivot_IteratorExp_LoopExp, gen_pivot_IteratorExp_ReferringElement, gen_pivot_LetExp_OCLExpression, gen_pivot_LambdaType_DataType, gen_pivot_LanguageExpression_ValueSpecification, gen_pivot_MapLiteralExp_LiteralExp, gen_pivot_MapLiteralPart_Element, gen_pivot_Library_Package, gen_pivot_LiteralExp_OCLExpression, gen_pivot_LoopExp_CallExp, gen_pivot_MapType_DataType, gen_pivot_MessageExp_OCLExpression, gen_pivot_NamedElement_Element, gen_pivot_NamedElement_Nameable, gen_pivot_Namespace_NamedElement, gen_pivot_NavigationCallExp_FeatureCallExp, gen_pivot_MessageType_Class, gen_pivot_Model_Namespace, gen_pivot_NumericLiteralExp_PrimitiveLiteralExp, gen_pivot_OCLExpression_TypedElement, gen_pivot_Operation_Feature, gen_pivot_Operation_Namespace, gen_pivot_Operation_TemplateableElement, gen_pivot_NullLiteralExp_PrimitiveLiteralExp, gen_pivot_OperationCallExp_FeatureCallExp, gen_pivot_OperationCallExp_ReferringElement, gen_pivot_OppositePropertyCallExp_NavigationCallExp, gen_pivot_OrderedSetType_CollectionType, gen_pivot_Parameter_VariableDeclaration, gen_pivot_Precedence_NamedElement, gen_pivot_PrimitiveCompletePackage_CompletePackage, gen_pivot_OrphanCompletePackage_CompletePackage, gen_pivot_Package_Namespace, gen_pivot_ProfileApplication_Element, gen_pivot_Property_Feature, gen_pivot_PrimitiveLiteralExp_LiteralExp, gen_pivot_PrimitiveType_DataType, gen_pivot_Profile_Package, gen_pivot_PropertyCallExp_NavigationCallExp, gen_pivot_PropertyCallExp_ReferringElement, gen_pivot_Pseudostate_Vertex, gen_pivot_RealLiteralExp_NumericLiteralExp, gen_pivot_SelfType_Class, gen_pivot_SendSignalAction_NamedElement, gen_pivot_SequenceType_CollectionType, gen_pivot_Region_Namespace, gen_pivot_ShadowPart_TypedElement, gen_pivot_Signal_Class, gen_pivot_Slot_Element, gen_pivot_SetType_CollectionType, gen_pivot_ShadowExp_OCLExpression, gen_pivot_State_Namespace, gen_pivot_State_Vertex, gen_pivot_StandardLibrary_Element, gen_pivot_StateMachine_Behavior, gen_pivot_Stereotype_Class, gen_pivot_StateExp_OCLExpression, gen_pivot_StringLiteralExp_PrimitiveLiteralExp, gen_pivot_TemplateBinding_Element, gen_pivot_TemplateParameter_Type, gen_pivot_StereotypeExtender_Element, gen_pivot_TemplateSignature_Element, gen_pivot_TemplateParameterSubstitution_Element, gen_pivot_Transition_Namespace, gen_pivot_TemplateableElement_Element, gen_pivot_Trigger_NamedElement, gen_pivot_TupleType_DataType, gen_pivot_Type_NamedElement, gen_pivot_TupleLiteralExp_LiteralExp, gen_pivot_TupleLiteralPart_VariableDeclaration, gen_pivot_TypeExp_OCLExpression, gen_pivot_TypeExp_ReferringElement, gen_pivot_TypedElement_NamedElement, gen_pivot_UnspecifiedValueExp_OCLExpression, gen_pivot_ValueSpecification_TypedElement, gen_pivot_UnlimitedNaturalLiteralExp_NumericLiteralExp, gen_pivot_Variable_VariableDeclaration, gen_pivot_VariableDeclaration_TypedElement, gen_pivot_Vertex_NamedElement, gen_pivot_VariableExp_OCLExpression, gen_pivot_VariableExp_ReferringElement, gen_pivot_VoidType_Class, gen_pivot_WildcardType_Class},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)